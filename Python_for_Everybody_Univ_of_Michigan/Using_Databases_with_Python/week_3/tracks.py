import xml.etree.ElementTree as elTree
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    cur_id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    cur_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    cur_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    cur_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = elTree.parse(fname)
all_tracks = stuff.findall('dict/dict/dict')
print('Dict count:', len(all_tracks))
for entry in all_tracks:
    if lookup(entry, 'Track ID') is None:
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(f"{name} | {artist} | {album} | {genre} | {count} | {rating} | {length}")

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
    VALUES ( ? );''', (artist,)
                )
    cur.execute('''SELECT cur_id
    FROM Artist
    WHERE name = ? ;''', (artist,)
                )
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
    VALUES ( ? );''', (genre,)
                )
    cur.execute('''SELECT cur_id
    FROM Genre
    WHERE name = ? ;''', (genre,)
                )
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id)'
                'VALUES ( ?, ? );', (album, artist_id)
                )
    cur.execute('''SELECT cur_id
    FROM Album
    WHERE title = ?;''', (album,)
                )
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
    (title, album_id, genre_id, len, rating, count) 
    VALUES ( ?, ?, ?, ?, ?, ? )''',
                (name, album_id, genre_id, length, rating, count)
                )

    conn.commit()
