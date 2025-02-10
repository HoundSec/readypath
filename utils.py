import sqlite3

def generate_token():
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT word FROM adjectives ORDER BY RANDOM() LIMIT 1")
    adjective = cursor.fetchone()
    
    cursor.execute("SELECT word FROM nouns ORDER BY RANDOM() LIMIT 1")
    noun = cursor.fetchone()
    
    conn.close()
    
    if adjective and noun:
        return f"{adjective[0]}-{noun[0]}"
    return None
