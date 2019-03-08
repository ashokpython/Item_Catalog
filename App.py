from flask import Flask, render_template, redirect, request, url_for, flash
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"


#MySQL Database connection

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'ashok'


mysql = MySQL(app)

@app.route('/')
def Index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM employee")
	data = cur.fetchall()
	# print(data)
	cur.close()

	return render_template('index.html', employee = data)


#for employee data insertion into database

@app.route('/insert', methods = ['POST'])
def insert():
	if request.method == 'POST':
		id = request.form['id']
		name = request.form['name']
		dob = request.form['dob']
		designation = request.form['designation']
		salary = request.form['salary']
		emailaddress = request.form['emailaddress']
		joining_date = request.form['joining_date']
		work_location = request.form['work_location']
		experience = request.form['experience']
		address = request.form['address']
		phone = request.form['phone']

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO employee(id, name, dob, designation, salary, emailaddress, phone, joining_date, work_location, experience, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
			(id, name, dob, designation, salary, emailaddress, phone, joining_date, work_location, experience, address))
		mysql.connection.commit()
		flash("Congratulation, Your Data Successfully Inserted Into Employee Database")
		return redirect(url_for('Index'))


#for employee data updating into database


@app.route('/update', methods = ['POST', 'GET'])
def update():
	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		dob = request.form['dob']
		designation = request.form['designation']
		salary = request.form['salary']
		emailaddress = request.form['emailaddress']
		joining_date = request.form['joining_date']
		work_location = request.form['work_location']
		experience = request.form['experience']
		address = request.form['address']
		phone = request.form['phone']

		cur = mysql.connection.cursor()
		cur.execute("""
			UPDATE employee
			SET name = %s, 
				dob = %s, 
				designation = %s, 
				salary = %s, 
				emailaddress = %s, 
				joining_date = %s, 
				work_location = %s, 
				experience = %s, 
				address = %s,
				phone = %s
			WHERE
				id = %s
				""", (name, dob, designation, salary, emailaddress, joining_date, work_location, experience, address, phone, id_data))

		mysql.connection.commit()
		flash("Congratulation, Your Data Successfully Updated to Employee Database")
		return redirect(url_for('Index'))

# Deleting data from employee database

@app.route('/delete/<string:id_data>', methods = ['POST' , 'GET'])
def delete(id_data):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM employee WHERE id = %s", (id_data))
	mysql.connection.commit()
	return redirect(url_for('Index'))


if __name__ == "__main__":
	app.run(debug=True)
