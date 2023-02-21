from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional, DataRequired

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    # Pet name
    name = StringField("Pet Name", validators=[InputRequired()])
    # Species
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    # Photo URL
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    # Age
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    # Notes
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    #Available
    available = BooleanField("Available?", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing a pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Notes",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")

    
