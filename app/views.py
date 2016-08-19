from flask import render_template, flash, redirect, session, url_for, request
from app import app
from wtforms import Form, TextField, PasswordField,validators
from app import GPA
class LoginForm(Form):
	username = TextField("username", [validators.Required()])
	password = PasswordField("password", [validators.Required()])
@app.route('/',methods = ['GET','POST'])
def index():
	myform = LoginForm(request.form)
	if request.method == 'POST':
		pp = GPA.gpa()
		lists = pp.main(myform.username.data, myform.password.data)
		#lists = [1,2,3]
		return render_template('cca.html' , lists=lists)
	# 	if myform.username.data == 'ccc' and myform.password.data=='123' and myform.validata():
	# 		return redirect('http://www.baidu.com')
	# 	else:
	# 		message = 'LOGIN ERROR'
	# 		return render_template('index.html', message = message, form = myform)
	return render_template('index.html', form = myform)