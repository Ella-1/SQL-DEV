from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@localhost:5432/mysql'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hell world!'


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
