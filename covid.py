from flask import Flask
from waitress import serve

app = Flask('__name__')

@app.route('/')
def home():
    return "OK"

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)