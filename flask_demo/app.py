from flask import Flask, render_template
import pandas as pd
import pymysql
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = pd.read_sql('SELECT * FROM users', cnx)
    return render_template('index.html', data=data)
    
@app.route('/listUsers',  methods=['GET','POST'])
def listUsers():
    #cursor.execute("SELECT * FROM users")
    data = pd.read_sql('SELECT * FROM users', cnx)
    return render_template('listUsers.html', data=data) 

if __name__ == '__main__':
    app.run()

def get_connection():
    connection_string = ('mysql://bmgt406_demo03:PW@localhost/DATABASE?auth_plugin=mysql_native_password')
    engine = create_engine(connection_string)

    connection = engine.raw_connection()
    cursor = connection.cursor()

    return cursor

#mycursor = get_connection()
cnx = create_engine('mysql+pymysql://bmgt406_demo03:bmgt406_demo03@bmgt406.rhsmith.umd.edu/bmgt406_demo03_db')    
df = pd.read_sql('SELECT * FROM users', cnx) #read the entire table
