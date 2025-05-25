from flask import Flask,render_template,request,redirect,url_for
from connection import login_user,register_user

app=Flask(__name__)

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
        return "Login success"
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

    if password == confirm_password:
        data = {
            "Full Name": fullname,
            "Email Id": email,
            "Phone Number": phone,
            "Gender": gender,
            "Department": department,
            "Domain": domain,
            "Password": password
        }
        result = register_user(data)  # ⬅️ Use renamed function here
        if result:
            return "Register success"
        return redirect(url_for('register_page'))  # Ensure route name matches
    return redirect(url_for('register_page'))


if __name__=='__main__':
    app.run(host='localhost',debug=True,port=5050)