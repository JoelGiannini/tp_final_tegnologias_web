from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ComandoForm(FlaskForm):
    nombre = StringField('Nombre del Comando', validators=[DataRequired()])
    descripcion = StringField('Descripción', validators=[DataRequired()])
    sistema = StringField('Sistema Operativo', validators=[DataRequired()])
    submit = SubmitField('Guardar')

