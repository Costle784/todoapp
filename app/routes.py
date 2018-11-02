from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Todo

@app.route('/')
def index():
    todos = Todo.query.filter_by(complete=False).all()
    completed_todos = Todo.query.filter_by(complete=True).all()
    return render_template('index.html', todos=todos, completed_todos=completed_todos)

@app.route('/add', methods=["POST"])
def add():
    todo = Todo(content=request.form['todoitem'],
                complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update', methods=["POST"])
def update():
    for key in dict(request.form):
        todo = Todo.query.filter_by(id=int(key)).one()
        todo.complete = True
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.get(int(id))
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))