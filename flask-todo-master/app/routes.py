from app import app, db, mysql
from flask import render_template, request, redirect, url_for, session, flash, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import TodoForm
from .models import TodoList



# Landing Page
@app.route('/')
def index():
    return render_template('landing.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		confirm_password = check_password_hash(password, password)
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM users WHERE name = %s AND password = %s", [username, confirm_password])
		account = cur.fetchone()

		if account:
			session['logged_in'] = True
			session['username'] = account[1]

			if 'logged_in' in session:
				return redirect(url_for('todo'))

		else:
			return render_template('login.html')
	return render_template('login.html')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
	# Register
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['inpEmail']
		password = request.form['confirm-password']
		confirm_password = generate_password_hash(password)

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email, password) VALUE (%s,%s,%s)", (username, email, confirm_password))
		mysql.connection.commit()
		return redirect(url_for('login'))

	return render_template('register.html')

@app.route('/todo-list', methods=['get','post'])
def todo():
    form = TodoForm()
    if request.method == 'POST':
        data = request.form['todo']
        dataUp = TodoList(data)
        db.session.add(dataUp)
        db.session.commit()
        return redirect(url_for('todo'))
    return render_template('todo.html', form=form, data=TodoList.query.all(), judul='Flask | To-Do-List')


@app.route('/edit/<id>', methods=['POST','GET'])
def edit(id):
    form = TodoForm()
    editTodo = TodoList.query.filter_by(id=id).first()
    if request.method == 'POST':
        editTodo.mytodolist = request.form['todo']
        db.session.add(editTodo)
        db.session.commit()
        return redirect(url_for('todo'))
    return render_template('todo.html', form=form, editTodo=editTodo, edit='test', data=TodoList.query.all())


@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    data = TodoList.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('todo'))


