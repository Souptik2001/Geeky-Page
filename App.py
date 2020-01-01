from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_host = True

app = Flask(__name__)
if (local_host):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
db = SQLAlchemy(app)

class Messages(db.Model):
    sl_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    ph_no = db.Column(db.String(120), unique=False, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=True)

class Posts(db.Model):
    sl_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    body = db.Column(db.String(120), unique=False, nullable=False)
    wr_by = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=True)
    slug = db.Column(db.String(120), unique=False, nullable=True)

@app.route('/')
def home():
    # if('user' in session and session['user']):
    datas= Posts.query.filter_by().all()[0:int(params["latest_posts_no"])]
    return render_template("index.html", datas=datas, params=params)

@app.route('/about')
def about():
    return render_template("about.html", params=params)

@app.route('/contact', methods={'GET', 'POST'})
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Messages(name = name, email = email, ph_no = phone, message = message, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html", params=params)

@app.route('/post/<string:post_slug>')
def post(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html", post=post, params=params)

@app.route('/posts')
def posts():
    datas = Posts.query.filter_by().all()
    return render_template("posts.html", datas=datas, params=params)

@app.route('/login')
def login():
    return render_template("login.html", params=params)

@app.route('/dashboard', methods={'GET', 'POST'})
def dashboard():
    posts= Posts.query.filter_by().all()
    return render_template("dashboard.html", params=params, posts=posts)

@app.route('/dashboard/add', methods={'GET', 'POST'})
def dashboardadd():
    if(request.method=='POST'):
        title = request.form.get('title')
        body = request.form.get('body')
        wr_by = request.form.get('wr_by')
        slug = request.form.get('slug')
        blog_entry = Posts(title=title, body=body, wr_by=wr_by, slug=slug, date=datetime.now())
        db.session.add(blog_entry)
        db.session.commit()
        return render_template("sucessfull.html", params=params)
    return render_template("dashboardadd.html", params=params)

# @app.route('/dashboard/sucessfull')
# def editsucessfull():
#     return render_template("sucessfull.html", params=params)

@app.route('/dashboard/edit/<string:sl_no>', methods={'GET', 'POST'})#/<string:sl_no>
def dashboardedit(sl_no):#sl_no
    edit_post=Posts.query.filter_by(sl_no=sl_no).first()
    if(request.method=='POST'):
        edit_post.title= request.form.get('title')
        edit_post.body= request.form.get('body')
        edit_post.wr_by= request.form.get('wr_by')
        edit_post.slug= edit_post.slug
        edit_post.date= datetime.now()
        db.session.commit()
        # return redirect('/dashboard/sucessfull')
        return render_template("sucessfull.html", params=params)
    return render_template("dashboardedit.html", params=params, post=edit_post)

@app.route('/dashboard/delete/<string:sl_no>')
def delete(sl_no):
    post_del = Posts.query.filter_by(sl_no = sl_no).first()
    db.session.delete(post_del)
    db.session.commit()
    return render_template("sucessfull.html", params=params)

app.run(debug=True)