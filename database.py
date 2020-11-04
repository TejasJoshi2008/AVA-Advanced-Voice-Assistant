import sqlite3

def connection_on():
    connection  = sqlite3.connect("commands.db")
    return connection

def get_question():
    con = connection_on()
    cur = con.cursor()
    cur.execute("SELECT*from questionANDanswer")
    return cur.fetchall()

def insert(question,answer):
    con = connection_on()
    cur = con.cursor()
    que = f"INSERT INTO questionANDanswer values('"+question+"','"+answer+"')"
    cur.execute(que)
    con.commit()

def get_answer(question):
    rows = get_question()
    answer = ""
    for row in rows:
        if row[0].lower() == question.lower():
            answer = row[1]
    return answer
