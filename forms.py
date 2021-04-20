from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# creates database using sqlalchemy
# declares a variable db to commit and add data to the test.db file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
