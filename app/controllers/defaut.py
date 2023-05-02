from app import app
from datetime import datetime

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


from flask import render_template

@app.route('/basepage/')
@app.route('/base0/')
@app.route('/base/')
def basepage():
    return render_template('base.html')

@app.route('/base1/')
def base1():
    return render_template('base1.html')

@app.route('/base2/')
def base2():
    return render_template('base2.html')

@app.route('/homepage/')
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/sign-in/')
def sign_in():
    return render_template('sign-in.html')


@app.route('/user/<username>')
def profile(username):
    return render_template('usuarios.html', username=username)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('/bak/hello.html', name=name)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('bak/result.html', result = dict)


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


def do_the_login():
    return render_template('sign-in.html')

def show_the_login_form():
    return render_template('login.html')



from markupsafe import escape

#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return f'User {escape(username)}'



#########################



#########################
from flask import url_for
with app.test_request_context():
    print(url_for('index'))                         # function names to generate URLs to that particular function
    #print(url_for('basepage'))                      # function names to generate URLs to that particular function
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('hello', username='John Doe'))
    print(url_for('show_post', post_id='1'))
    print(url_for('static', filename='style.css'))
    print(url_for('static', filename='hello.css'))
    