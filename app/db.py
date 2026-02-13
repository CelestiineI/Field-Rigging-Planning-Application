import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="proqee",
        user="postgres",
        password="BestPresident7",
        host="localhost",
        port=5432
    )