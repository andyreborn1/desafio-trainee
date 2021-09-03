import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    conn = psycopg2.connect(
        database="postgres",
        user="student",
        password="student",
        host="127.0.0.1",
        port="5433",
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # create sparkify database with UTF8 encoding
    cursor.execute("drop database if exists sparkifydb")
    cursor.execute(
        "CREATE database sparkifydb with template = template0 encoding = 'UTF8'"
    )

    # close connection to default database
    conn.close()
    cursor.close()

    # connect to sparkify database
    conn = psycopg2.connect(
        database="sparkifydb",
        user="student",
        password="student",
        host="127.0.0.1",
        port="5433",
    )

    cursor = conn.cursor()

    return cursor, conn


def drop_tables(cur, conn):

    for table in drop_table_queries:
        cur.execute(table)

    conn.commit()
    print("tables dropped")


def create_tables(cur, conn):

    for table in create_table_queries:
        cur.execute(table)

    conn.commit()
    print("tables created")


def main():

    cursor, conn = create_database()
    print("main")

    drop_tables(cursor, conn)
    create_tables(cursor, conn)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
