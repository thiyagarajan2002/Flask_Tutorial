from flask import Flask,render_template,request,redirect,url_for,flash
from connection import login_user,register_user,check_email,password_hash,password_check
from datetime import datetime

app=Flask(__name__)
app.secret_key = 'random string'
@app.route('/')
def home():
    return render_template('home.html')
 

@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def login_process():
    email = request.form.get("email")
    password = request.form.get("password")
    result=login_user(email,password)
    if result:
        if password_check(password, result['Password']):
            return "Login success"
        flash("Invalid Password")
        return redirect(url_for('login'))
    flash("Invalid Details")
    return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register_process():
    fullname = request.form.get("fullname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    gender = request.form.get("gender")
    department = request.form.get("department")
    domain = request.form.get("domain")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")
    date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if password != confirm_password:
        flash("Passwords do not match")
        return redirect(url_for('register'))
    if check_email(email):
        flash("Email already exists")
        return redirect(url_for('register'))
    data = {
            "Full Name": fullname,
            "Email Id": email,
            "Phone Number": phone,
            "Gender": gender,
            "Department": department,
            "Domain": domain,
            "Password": password_hash(password),
            "Date and time":date_time # type: ignore
    }
    result = register_user(data)  # ⬅️ Use renamed function here
    if result:
        return "Register success"
    flash("Registration failed")
    return redirect(url_for('register'))
    

if __name__=='__main__':
    app.run(host='localhost',debug=True,port=5050)