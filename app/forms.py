from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])