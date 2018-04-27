
import os
import sqlite3
import json
from util.c_tokenizer import C_Tokenizer
tokenize = C_Tokenizer().tokenize

db_path = 'data/iitk-dataset/dataset.db'

with sqlite3.connect(db_path) as conn:
    conn.execute('''ALTER TABLE Code ADD tokenized_code text;''')
    conn.execute('''ALTER TABLE Code ADD name_dict;''')
    conn.execute('''ALTER TABLE Code ADD name_seq;''')
    conn.execute('''ALTER TABLE Code ADD codelength integer;''')

tuples = []
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    for row in cursor.execute("SELECT code_id, code FROM Code;"):
        code_id = str(row[0])
        code = row[1].encode('utf-8')
        tokenized_code, name_dict, name_seq = tokenize(code)
        codelength = len(tokenized_code.split())
        tuples.append((tokenized_code, json.dumps(name_dict),
                       json.dumps(name_seq), codelength, code_id))

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.executemany(
        "UPDATE Code SET tokenized_code=?, name_dict=?, name_seq=?, codelength=? WHERE code_id=?;", tuples)
    conn.commit()
