from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'db/helpdesk.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_ticket', methods=['GET', 'POST'])
def submit_ticket():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        category = request.form['category']
        description = request.form['description']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO tickets (name, email, category, description)
            VALUES (?, ?, ?, ?)
        ''', (name, email, category, description))
        db.commit()
        
        return redirect(url_for('index'))
    
    return render_template('submit_ticket.html')

@app.route('/view_tickets')
def view_tickets():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM tickets')
    tickets = cursor.fetchall()
    
    return render_template('view_tickets.html', tickets=tickets)

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL,
              category TEXT NOT NULL,
              description TEXT NOT NULL,
              status TEXT NOT NULL DEFAULT 'Open'
            )
        ''')
        db.commit()

init_db()

if __name__ == '__main__':
    app.run(debug=True)
