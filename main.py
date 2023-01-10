from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'New to Flask!'


app.run(host='0.0.0.0', port=81)
