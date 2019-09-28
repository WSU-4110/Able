from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
# Instantiates the Flask app I think?
app = Flask(__name__, template_folder='templates')
Bootstrap(app)

# Root directory route. This will always be the first page to load.
@app.route('/')
def main_page():
    # Telling it what to render out. When it gets more complex, we will be passing HTML templates within these functions
    return render_template('main.html')


# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
# I just now this makes it able to run
if __name__ == '__main__':
    app.run()
