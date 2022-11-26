from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    pages = IntegerField("Page numbers", validators=[DataRequired()])
    publish_date = DateField("Publish date", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    isbn = StringField("ISBN", validators=[DataRequired()])
    submit = SubmitField("Create book")