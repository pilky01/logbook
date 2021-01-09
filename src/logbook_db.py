#!/usr/bin/env python3

import sqlite3 as sqlite3

db_path = './data/logbook_data.db'


def airfield_search(term):
    ##Search result lists second parameter e.g. origin --lists--> name
    query = '''SELECT id, name, icao_code, iata_code
               FROM airports WHERE name LIKE ?;'''
    term_string = "%"+term+"%"
    dbcon = sqlite3.connect(db_path)
    dbcon.row_factory = sqlite3.Row
    cursor = dbcon.cursor()
    result = cursor.execute(query, (term_string,)).fetchall()
    dbcon.close()
    
    return result

def aircraft_search(term):
    ##Search result lists second parameter e.g. origin --lists--> name
    query = '''SELECT aircraft.id, aircraft.registration,
               aircraft_type.type_name, aircraft_type.multi
               FROM aircraft, aircraft_type
               WHERE aircraft.type = aircraft_type.id
               AND registration LIKE ?;'''
    term_string = "%"+term+"%"
    dbcon = sqlite3.connect(db_path)
    dbcon.row_factory = sqlite3.Row
    cursor = dbcon.cursor()
    result = cursor.execute(query, (term_string,)).fetchall()
    dbcon.close()
    print(result[0].keys())
    return result
