from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TodoForm(FlaskForm):
    masukanTodo = StringField('To Do List')
    submit = SubmitField('Add')
    update = SubmitField('Simpan')

