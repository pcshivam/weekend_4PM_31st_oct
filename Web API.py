from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/register", methods = ['POST'])
def register():
    data = request.get_json()
    connection = sqlite3.connect("sample.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee(ID text, password text)")
    cursor.execute("INSERT INTO employee VALUES ('{}','{}')".format(data["id"], data["password"]))
    connection.commit()
    connection.close()
    return "Employee details has been registered successfully"

@app.route("/show")
def show():
    connection = sqlite3.connect("sample.db")
    cursor = connection.cursor()
    employee_data = list(cursor.execute("SELECT * FROM employee"))
    return {"Employee details": employee_data}

@app.route("/update", methods = ['POST'])
def update():
    data = request.get_json()
    connection = sqlite3.connect("sample.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE employee SET password = '{}' where id = '{}'".format(data["password"],data["id"]))
    connection.commit()
    connection.close()
    return "Employee password has been updated successfully"

@app.route("/delete", methods = ['POST'])
def delete():
    data = request.get_json()
    connection = sqlite3.connect("sample.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from employee WHERE id = '{}'".format(data["id"]))
    connection.commit()
    connection.close()
    return "Employee details deleted successfully"

app.run(port = 1995)