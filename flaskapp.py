from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# SQLite Database Setup
DATABASE = '/home/ubuntu/flaskapp/peddansi.db'

# Route to display the registration form
@app.route('/')
def index():
    return render_template('register.html')

# Route to handle registration form submission
@app.route('/register', methods=['POST'])
def register():
    try:
        # Get form data
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        # Insert data into SQLite database
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
