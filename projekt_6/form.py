from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired
import datetime

#The class represents the variables used in form
class ArticleForm(Form):
    title = StringField('title', validators=[DataRequired()])#Title of article, required field
    publ_date = DateTimeField(default=datetime.datetime.now)
    text = TextAreaField('text')#text-content - required
