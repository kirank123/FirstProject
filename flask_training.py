from flask import Flask, redirect, url_for, request, render_template
app =Flask(__name__)

'''
@app.route('/admin')
def hello_admin():
    return "<h1>Hello Back Admin!</h1>"


@app.route('/new/')
def new_world():
    return "New world"


@app.route('/guest/<guest>')
def hello_guest(guest):
    return f"Hello {guest} as guest"


@app.route('/user/<name>')
def hello_name(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
#    app.debug = True
#       app.run()
    app.run(debug=True)
'''

###### HTML Post and Get methods
'''
@app.route('/success/<name>')
def success(name):
    return f"Welcome {name}"


@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']     ##For POST method
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')    ##For GET method
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
'''

## Jina 2 template engine
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


if __name__ == '__main__':
    app.run(debug=True)
'''

## integer type data in HTML
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello1.html', marks=score)

if __name__ == '__main__':
    app.run(debug=True)
'''

@app.route('/result/')
def result():
    dict = {'phy':50, 'che':60, 'maths':70, 'Eng':80}
    return render_template("result.html", result=dict)


if __name__ == '__main__':
    app.run(debug=True)
