from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import json

app = Flask(__name__)

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://curtis:Bassman784@localhost:3306/todo_app'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    content = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean, default=False) 
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

Bootstrap(app)

@app.route('/')
def index():
    todos = Todo.query.filter_by(complete=False)
    completed_todos = Todo.query.filter_by(complete=True)
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

@app.route('/delete/<id>', methods=["DELETE"])
def delete(id):
    todo = Todo.query.get(int(id))
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)