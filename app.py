from flask import Flask, jsonify

app = Flask(__name__)

f = open('./html/index.html')
homepage = f.read()

@app.route('/')
def hello_world():
    return homepage

if __name__ == '__main__':
    app.run()