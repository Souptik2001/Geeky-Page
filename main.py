from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_host = True

app = Flask(__name__)
app.secret_key='super-secret-key'
if (local_host):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri_sqlite"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
db = SQLAlchemy(app)

class Messages(db.Model):
    sl_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=True)
    ph_no = db.Column(db.String(120), unique=False, nullable=True)
    message = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=True)

class Posts(db.Model):
    sl_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    body = db.Column(db.String(120), unique=False, nullable=False)
    wr_by = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=True)

@app.route('/')
def home():
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
    datas= Posts.query.filter_by().all()[0:int(params["latest_posts_no"])]
    return render_template("index.html", datas=datas, params=params, logged=logged)

@app.route('/about')
def about():
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
    return render_template("about.html", params=params, logged=logged)

@app.route('/contact', methods={'GET', 'POST'})
def contact():
    logged="False"
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Messages(name = name, email = email, ph_no = phone, message = message, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
    return render_template("contact.html", params=params, logged=logged)

@app.route('/post/<string:post_no>')
def post(post_no):
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
    post = Posts.query.filter_by(sl_no=post_no).first()
    return render_template("post.html", post=post, params=params, logged=logged)

@app.route('/posts')
def posts():
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
    datas = Posts.query.filter_by().all()
    return render_template("posts.html", datas=datas, params=params, logged=logged)

@app.route('/login', methods = {'GET', 'POST'})
def login():
    logged="False"
    wrong='False'
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
    if(request.method == 'POST'):
        uname = request.form.get('uname')
        password = request.form.get('pass')
        if(uname == params['admin_user'] and password == params['admin_pass']):
            session['user'] = uname
            return redirect('/')
        else:
            wrong='True'
    return render_template("login.html", params=params, logged=logged, wrong=wrong)

@app.route('/logout')
def logout_user():
    if('user' in session and session['user'] == params['admin_user']):
        session.pop('user', None)
        return redirect('/')
    return redirect('/login')

@app.route('/dashboard', methods={'GET', 'POST'})
def dashboard():
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
        posts= Posts.query.filter_by().all()
        return render_template("dashboard.html", params=params, posts=posts,logged=logged)
    return redirect('/login')

@app.route('/dashboard/add', methods={'GET', 'POST'})
def dashboardadd():
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
        if(request.method=='POST'):
            title = request.form.get('title')
            body = request.form.get('body')
            wr_by = request.form.get('wr_by')
            slug = request.form.get('slug')
            blog_entry = Posts(title=title, body=body, wr_by=wr_by, date=datetime.now())
            db.session.add(blog_entry)
            db.session.commit()
            return render_template("sucessfull.html", params=params)
        return render_template("dashboardadd.html", params=params, logged=logged)
    return redirect('/login')

# @app.route('/dashboard/sucessfull')
# def editsucessfull():
#     return render_template("sucessfull.html", params=params)

@app.route('/dashboard/edit/<string:sl_no>', methods={'GET', 'POST'})#/<string:sl_no>
def dashboardedit(sl_no):#sl_no
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
        edit_post=Posts.query.filter_by(sl_no=sl_no).first()
        if(request.method=='POST'):
            edit_post.title= request.form.get('title')
            edit_post.body= request.form.get('body')
            edit_post.wr_by= request.form.get('wr_by')
            edit_post.date= datetime.now()
            db.session.commit()
            # return redirect('/dashboard/sucessfull')
            return render_template("sucessfull.html", params=params)
        return render_template("dashboardedit.html", params=params, post=edit_post, logged=logged)
    return redirect('/login')

@app.route('/dashboard/delete/<string:sl_no>')
def delete(sl_no):
    logged="False"
    if('user' in session and session['user'] == params['admin_user']):
        logged= "True"
        post_del = Posts.query.filter_by(sl_no = sl_no).first()
        db.session.delete(post_del)
        db.session.commit()
        return render_template("sucessfull.html", params=params, logged=logged)
    return redirect('/login')

app.run(host="0.0.0.0", port="1200",debug=True)
# app.run(debug=True)