# This is an example demonstrating the use of static assets such as
# HTML, JS, CSS, and image files. You'll place these static files inside
# the static subdirectory, and Flask will automatically make them available
# at the sub URL /static
from flask import Flask, render_template

app = Flask('MyApp')

@app.route('/')
def home():
    return render_template('button.html')

if __name__ == '__main__':
    app.run(debug=True)
