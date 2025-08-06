from flask import Blueprint, render_template, request, redirect, url_for
from .models import Comando
from .forms import ComandoForm
from . import db
from sqlalchemy import or_, func

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    query = request.args.get('q', '')
    if query:
        comandos = Comando.query.filter(
            or_(
                func.lower(Comando.nombre).like(f"%{query.lower()}%"),
                func.lower(Comando.descripcion).like(f"%{query.lower()}%"),
                func.lower(Comando.sistema).like(f"%{query.lower()}%")
            )
        ).all()
    else:
        comandos = Comando.query.all()
    return render_template('index.html', comandos=comandos, query=query)

@main.route('/add', methods=['GET', 'POST'])
def add():
    form = ComandoForm()
    if form.validate_on_submit():
        nuevo = Comando(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            sistema=form.sistema.data
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add.html', form=form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    comando = Comando.query.get_or_404(id)
    form = ComandoForm(obj=comando)
    if form.validate_on_submit():
        comando.nombre = form.nombre.data
        comando.descripcion = form.descripcion.data
        comando.sistema = form.sistema.data
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', form=form)

@main.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    comando = Comando.query.get_or_404(id)
    db.session.delete(comando)
    db.session.commit()
    return redirect(url_for('main.index'))

