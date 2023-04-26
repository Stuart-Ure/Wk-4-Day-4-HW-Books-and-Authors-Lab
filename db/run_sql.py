import psycopg2 
import psycopg2.extras as ext 

def run_sql(sql, values= None):
    conn = None
    results = []

    try:
        conn=psycopg2.connect("dbname='authors_books'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values)
        conn.commit()
        if cur.rowcount:
            results = cur.fetchall()
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results  