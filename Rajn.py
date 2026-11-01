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

app.run(port = 1995)


print("There is a change needed in this file changes suggested by shivam")