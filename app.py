from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "adopt_pet"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pet-adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def home_page():

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET","POST"])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
    
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
    
        return render_template("createpet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        
        return redirect("/")

    else:
       
        return render_template("editpet.html", form=form, pet=pet)



