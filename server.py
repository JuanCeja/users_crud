from flask import Flask, render_template, redirect, request

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("users.html",  users=User.get_all())

@app.route('/users')
def users():
    return render_template("/users.html", users=User.get_all())

@app.route("/users/new")
def new():
    return render_template('create_user.html')

@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        'id':id
    }
    return render_template('edit_user.html', user = User.get_one(data))

@app.route("/user/create", methods=['post'])
def create_user():
    id = User.create_user(request.form)
    return redirect('/users')
    
@app.route("/user/update", methods = ['post'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/')

@app.route("/user/show/<int:id>")
def show(id):
    data = {
        'id':id
    }
    return render_template('show_user.html', user = User.get_one(data))

if __name__ == "__main__":
    app.run(debug=True)