# -*- coding: utf-8 -*-
# {{{ application.name }}}
# {{{ author.name }}}

from flask.ext.wtf import Form
import wtforms.fields as fields
from wtforms.validators import Required, Optional, Length

class SubForm(Form):
    "This is an individual"
    friend = fields.SelectField(
        label="Friend Name",
        validators=[Optional()])

class ExampleForm(Form):
    sex = fields.RadioField(label="Sex", choices=[("M", "Male"), ("F", "Female")])
    subfield = fields.FieldList(fields.FormField(SubForm))
