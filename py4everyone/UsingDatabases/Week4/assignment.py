import sqlite3
import json

conn = sqlite3.connect('py4everyone/UsingDatabases/Week4/wk4_assignment.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'roster_data.json'
jsonFile = open("/Users/conanchan/Documents/Coursera/py4everyone/UsingDatabases/Week4/"+fname)
data = json.load(jsonFile)

for entry in data:
    name = entry[0]
    course = entry[1]
    role = entry[2]
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    # Run select statement to get ID of user and Course
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Course WHERE title = ?',(course,))
    course_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, role,))
    
    conn.commit()
conn.close() 