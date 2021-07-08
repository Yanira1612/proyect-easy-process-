#from logging import NullHandler
from flask import Flask
from flask import render_template, request
from flask_mysqldb import MySQL


app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ' '
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/La_escuela')
def escuela():
    return render_template('La_escuela.html')

@app.route('/Director')
def director():
    return render_template('Director.html')    

@app.route('/MisionyVision')
def mision_vision():
    return render_template('Mision_vision.html') 
 
@app.route('/Objetivos')
def objetivos():
    return render_template('Objetivo.html') 

@app.route('/Plan_Estudios')
def plan_estudios():
    return render_template('Plan_estudios.html')

@app.route('/Grados_academicos')
def grados_academicos():
    return render_template('Grados_academicos.html')

#loging
@app.route('/Login')
def Login():
    return render_template('Login.html')

#agregar contacto
@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
       fullname = request.form['fullname']
       phone = request.form['phone']
       email = request.form['email']
       cur = mysql.connection.cursor()
       #cur.(SELECT *FROM flaskcontacts)
       cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
       mysql.connection.commit()
       return 'Datos recibidos satisfactoriamente'
       


if __name__ == '__main__':
    app.run(debug=True) 