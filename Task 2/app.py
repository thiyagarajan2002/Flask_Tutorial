from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome</h1>"

@app.route('/calculate/<num1>/<num2>', methods=['GET', 'POST'])
def calculate(num1, num2):
    if num1.isnumeric() and num2.isnumeric():
        num1,num2=int(num1),int(num2)
        if num2 == 0:
            division_result = "Undefined (division by zero)"
        else:
            division_result = num1 / num2
        return f"""
            Addition: {num1 + num2}<br>
            Subtraction: {num1 - num2}<br>
            Multiplication: {num1 * num2}<br>
            Division: {division_result}
            """
    else:
        return "Invalid data"


if __name__ == "__main__":
    app.run(debug=True, port=3010, host="0.0.0.0")
