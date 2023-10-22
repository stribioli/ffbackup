#!/usr/bin/python3

import sys, json, re, math
import sqlite3

input = json.load(sys.stdin)

pattern1 = re.compile(r':[0-9]+}$')
pattern2a = re.compile(r':[0-9]+}$')
pattern2b = re.compile(r':[0-9]+}$')

db = sqlite3.connect('history.sqlite3')
cur = db.cursor()

items = []

for entry in input:
    rawData = entry['data']
    try:
        if (not rawData.endswith(']}')
                and re.search(pattern1, rawData)
                and (re.search(pattern2a, rawData) or re.search(pattern2b, rawData))):
            rawData = rawData + ']}'

        data = json.loads(rawData)

        for visit in data['visits']:
            if 'title' not in data:
                data['title'] = ''
            items.append({'uri': data['histUri'], 'title': data['title'], 'date': math.floor(visit['date']/1e6), 'transitiontype': visit['type']})
    except Exception as e:
        print('An exception occurred:', type(e).__name__, e, file=sys.stderr)
        print('We choked on:', rawData, file=sys.stderr)

cur.executemany("INSERT OR IGNORE INTO history VALUES(:uri, :title, :date, :transitiontype)", items)
print("Rows written:", cur.rowcount, file=sys.stderr)
db.commit()

cur.close()
db.close()
