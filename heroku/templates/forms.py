from flask.ext.wtf import Form
from wtforms import fields
#from wtforms.ext.sqlalchemy.fields import QuerySelectField

#from .models import Site


class TickerForm(Form):
    ticker = fields.StringField()

