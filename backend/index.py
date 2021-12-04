from flask import Flask, jsonify
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
app = Flask(__name__)
  
  
app.secret_key = 'your secret key'
  
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Abhishek9991361402'
app.config['MYSQL_DB'] = 'newsapp'
  
  
mysql = MySQL(app)



@app.route('/')
def get_news():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM news")
    rows = cursor.fetchall()
    res=''
    k=0
    

    return str(rows)



    

if __name__ == "__main__":
    app.run(debug=True)

