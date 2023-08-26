import sqlite3
from Posts.PostModel import Post

def InitDB():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    print(Post.generate_create_table_sql())
    cursor.execute(Post.generate_create_table_sql())
    conn.commit()
    conn.close()

def ConnectToDB():
    conn = sqlite3.connect('mydatabase.db')
    return conn
    '''
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    '''
