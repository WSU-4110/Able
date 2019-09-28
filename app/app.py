from flask import Flask

# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
app = Flask(__name__)

# Root directory route. This will always be the first page to load.
@app.route('/')
def hello_world():
    # Telling it what to render out. When it gets more complex, we will be passing HTML templates within these functions
    return 'Hello World!'


# Can't really explain what this does technically, but it works ¯\_(ツ)_/¯
if __name__ == '__main__':
    app.run()
