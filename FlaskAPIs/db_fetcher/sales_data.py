from db_fetcher import get_connection, prepare_results
from sales.models import Store


def get_stores():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT store_id, store_name, phone, email, street, city, state, zip_code From sales.stores')
        return prepare_results(cursor)


def get_store(store_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT store_id, store_name, phone, email, street, city, state, zip_code From sales.stores where store_id={store_id}')
        return prepare_results(cursor)


def create_store(store: Store):
    try:
        insert_query = '''INSERT INTO sales.Stores (store_name, phone, email, street, city, state, zip_code) 
        VALUES (?, ?, ?, ?, ?, ?, ?);'''
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(insert_query, (store.store_name, store.phone, store.email, store.street, store.city, store.state, store.zip_code))
            cursor.commit()
    except Exception as e:
        print(str(e))


def delete_store(store_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'DELETE From sales.stores where store_id={store_id}')
        cursor.commit()


def update_store(store_id):
    pass
    # with get_connection() as conn:
    #     cursor = conn.cursor()
    #     cursor.execute(f'DELETE From sales.stores where store_id={store_id}')
    #     return prepare_results(cursor)