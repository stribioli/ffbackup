#!/usr/bin/python3

import sys
import sqlite3

db = sqlite3.connect('ffdata.sqlite3')
cur = db.cursor()

cur.execute('''
CREATE TABLE "history" (
    "uri"             TEXT NOT NULL,
    "title"           TEXT,
    "date"            INTEGER NOT NULL,
    "transitiontype"  INTEGER DEFAULT 1,
    UNIQUE("uri","date")
)
''')
db.commit()

cur.close()
db.close()
