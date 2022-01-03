from flask import Flask, request, render_template
import sqlite3 as sql
import gunicorn


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    conn = sql.connect('test.db')
    conn.row_factory = sql.Row
    cur = conn.cursor()
    query = 'SELECT * FROM test'
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return render_template('Home.html', rows=rows)


@app.route('/new_entry')
def new_entry():
    return render_template('NewEntry.html')


@app.route('/InsertData', methods=['GET', 'POST'])
def InsertData():
    if request.method == 'POST':
        try:
            name = request.form['name']
            dob = request.form['dob']
            age = request.form['age']
            email = request.form['email']
            var = (name,dob,age,email)

            with sql.connect('test.db') as conn:
                cur = conn.cursor()
                query = 'INSERT INTO test (name,dob,age,email) VALUES (?,?,?,?)'
                cur.execute(query, var)
                conn.commit()
                flag = 'Success'

        except Exception as e :
            conn.rollback()
            flag = 'Fail'

        finally:
            conn.close()
            return render_template('result.html', flag=flag)


if __name__ == '__main__':
    app.run()


