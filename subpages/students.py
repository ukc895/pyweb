from flask import Flask, jsonify
import json

app = Flask(__name__)

#f = open('./html/index.html')
#homepage = f.read()

@app.route('/Students/', methods=['GET'])
def get_Students():
    return ''

if __name__ == '__main__':
    app.run()