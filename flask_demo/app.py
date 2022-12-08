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
""" from flask import Flask, render_template
import mysql.connector

mydatabase = mysql.connector.connect(
    host = 'localhost(or any other host)', user = 'name_of_user',
    passwd = 'db_password', database = 'database_name')


mycursor = mydatabase.cursor()

#There you can add home page and others. It is completely depends on you

@app.route('/example.html')
def example():
   mycursor.execute('SELECT * FROM user_info')
   data = mycursor.fetchall()
   return render_template('example.html', output_data = data)

 """

""" from flask import Flask, request,render_template
import psycopg2
try: 
    conn = psycopg2.connect(database="bmgt406_demo03_db", user="bmgt406_demo03",  
    password="bmgt406_demo03", host="bmgt406.rhsmith.umd.edu")
    print("connected")
except:
    print ("I am unable to connect to the database")
mycursor =conn.cursor()
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/v_timestamp')
def v_timestamp():
    mycursor.execute("SELECT * FROM v_timestamp1")
    data = mycursor.fetchall()
    return render_template('v_timestamp.html', data=data) """

