from db_fetcher import get_connection, prepare_results


def get_brands():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT brand_id, brand_name From production.brands')
        return prepare_results(cursor)
