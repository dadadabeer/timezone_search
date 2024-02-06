
from sqlite3 import connect
from contextlib import closing
import sqlite3
_DATABASE_URL = 'geonames.sqlite' 

def find_timezones(search_term):
    with sqlite3.connect(_DATABASE_URL) as connection:
        cursor = connection.cursor()
        query = """
        SELECT g.name, c.countryname, g.timezone
        FROM geonames AS g
        JOIN country AS c ON g.countrycode = c.countrycode
        WHERE g.name LIKE ? OR c.countryname LIKE ?
        """
        search_pattern = f'%{search_term}%'
        cursor.execute(query, (search_pattern, search_pattern))
        results = cursor.fetchall()
        return results





