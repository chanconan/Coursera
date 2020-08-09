import sqlite3
import re
import xml.etree.ElementTree as ET

conn = sqlite3.connect('wk2_assignment.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE,
    FOREIGN KEY (artist_id) REFERENCES Artist (id)
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER,
    FOREIGN KEY (album_id) REFERENCES Album (id),
    FOREIGN KEY (genre_id) REFERENCES Genre (id)
);
''')

def lookup(data, key):
    found = False
    for child in data:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Library.xml'
xmlFile = "/Users/conanchan/Documents/Coursera/py4everyone/tracks/"+fname

library = ET.parse(xmlFile)

lib_info = library.findall('./dict/dict/dict')
for entry in lib_info:
    if lookup(entry, 'Track ID') is None: continue

    name = lookup(entry,'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry,'Album')
    genre = lookup(entry,'Genre')
    length = lookup(entry,'Total Time')
    rating = lookup(entry,'Rating')
    count = lookup(entry,'Play Count')

    if name is None or artist is None or album is None or genre is None:
        continue

    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?) ''', (artist,))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''', (artist,))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?) ''', (genre,))
    cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
    cur.execute('''SELECT id FROM Album WHERE title = ?''', (album,))
    album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))
    
    conn.commit()
cur.close()