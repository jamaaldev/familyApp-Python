import sqlite3 as sql

conn = sql.connect('family_bootcamp.db')
# Aliases name conn.cursor in to cursor
cursor = conn.cursor()
