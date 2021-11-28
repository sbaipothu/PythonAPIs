import pyodbc


def get_connection():
    # Trusted Connection to Named Instance
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=BikeStores;Trusted_Connection=yes;')


def prepare_results(cursor: pyodbc.Cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]