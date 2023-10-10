from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ''.join([chr(ord(char) ^ 69) for char in "7$+e($7,&*+"])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
