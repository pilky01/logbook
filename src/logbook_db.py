#!/usr/bin/env python3

import sqlite3 as sqlite3

db_path = './data/logbook_data.db'


def search_selection(term, source):
    ##Search result lists second parameter e.g. origin --lists--> name
    source_dict = { "origin" : '''SELECT id, name, icao_code, iata_code
                                  FROM airports WHERE name LIKE ?;''',
                    "destination" : '''SELECT id, name, icao_code, iata_code
                                  FROM airports WHERE name LIKE ?;''',
                    "aircraft" : '''SELECT id, registration, type
                                   FROM aircraft WHERE registration LIKE ?;''',
                   }
    term_string = "%"+term+"%"
    dbcon = sqlite3.connect(db_path)
    dbcon.row_factory = sqlite3.Row
    cursor = dbcon.cursor()
    result = cursor.execute(source_dict[source], (term_string,)).fetchall()
    dbcon.close()
    return result
