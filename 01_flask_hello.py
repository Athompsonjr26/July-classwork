# the Flask class from the flask module
from flask import Flask

# Creates a flash app object
app = Flask('MyApp')

# Sets up a URL handler for the root URL: /
@app.route('/')
def hello():
    # send the text "Hello, world!" to the browser
    return '<h1>Hello, world!</h1>'

# Start the server if this file is run as a script on the command line
if __name__ == '__main__':
    # run the server in debug mode, which will automatically
    # restart the server for you on save
    app.run(debug=True)
