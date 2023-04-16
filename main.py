from flask import Flask


#app = Flask('app')
app = Flask(__name__)






from markupsafe import escape

#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return f'User {escape(username)}'



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'





@app.route('/login')
def login():
    return 'login'





from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/homepage/')
def homepage():
    return render_template('index.html')



@app.route('/user/<username>')
def profile(username):
    return render_template('usuarios.html', username=username)

@app.route('/')
def index():
    return render_template('index.html')




from flask import url_for
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))




#########################
'''
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
'''








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(debug=True)
