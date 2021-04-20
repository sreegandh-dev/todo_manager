from flask import render_template, request, redirect
from models import Todo
from forms import db
from forms import app


# function for the home page where all the incomplete tasks are displayed
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_details = request.form['details']
        new_task = Todo(content=task_content, details=task_details)
        new_task.complete = False
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


# task is deleted from database
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting the task"


# function to update task , The data for a task is requested the home page using forms
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        task.details = request.form['details']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue completing your task"
    else:
        return render_template('update.html', task=task)


# approute and function to mark an uncompleted task as complete and
# displaying completed lists in a different page using a filter_by function
@app.route('/completed/<id>')
def completed(id):
    task = Todo.query.get_or_404(id)
    task.complete = True
    db.session.add(task)
    db.session.commit()
    tasks = Todo.query.filter_by(complete=True)
    return render_template('completed.html', tasks=tasks)


# to navigate to the list of completed tasks through the navbar
@app.route('/completed_tasks/')
def completed_tasks():
    tasks = Todo.query.filter_by(complete=True)
    return render_template('completed.html', tasks=tasks)


# app route and function to create new task
@app.route('/newtask/', methods=['GET', 'POST'])
def newtask():
    if request.method == 'POST':
        task_content = request.form['content']
        task_details = request.form['details']
        new_task = Todo(content=task_content, details=task_details, complete=False)
        new_task.complete = False
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/newtask/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.filter_by(complete=False)
        return render_template("newtask.html", tasks=tasks)


# to debug
if __name__ == "__main__":
    app.run(debug=True)

