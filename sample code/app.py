from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])  # or just @app.route('/hello')
def hello():
    name = request.args
    name=name['name']  # Get data from URL query string
    return f'Hello, {name}!' if name else 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

"""
dic={'name':'ps'}
print(dic.get('name'))
"""
