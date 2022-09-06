#Importing flask package
from flask import Flask

app = Flask(__name__)

##Creating index page
@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'

## create two additional pages

#Page 2
@app.route('/Campus Location')
def campus_location():
    return 'South Hampton!'

#Page 3
@app.route('/Travel Time')
def drive_time():
    return 'Travel Time: Too long!'


## Note, if you want to run this app with the command `python app.py`, you need to add the following line to the end of the file
## so it can execute and stay running....
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)

