from flask import Flask, jsonify
import json

# Open JSON file stored in data folder
f = open("./data/students.json")
data = f.read()
f.close()

# Print the data and type of data
print(data)
print('')
print('Type of data', type(data))

# Convert the data from string to JSON format again
students = json.loads(data)['Students']

# Retrieve only names from the JSON data
names = [student['name'] for student in students]
print(names)

# Initialize Flask application
app = Flask(__name__)

# Open the Homepage HTML file and read its data
f = open('./html/index.html')
homepage = f.read()
f.close()

# This decorator works with sub-page /Students 
@app.route('/Students/', methods=['GET'])
def get_Students():
    html = "<table><tr><th>Name</th></tr><tr><td>"
    for name in names:
        html = html + name + '</td></tr>'
        if (name != names[-1]):
            html = html + '<tr><td>'
        else:
            html = html + '</table>'
    print(html)

    return html

# This decorator opens homepage of the application
@app.route('/')
def hello_world():
    return homepage

# Here interpreter checks to see if this is the main code or being used in other python code and runs the code accordingly.
if __name__ == '__main__':
    app.run()