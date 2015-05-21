from contextlib import contextmanager
import psycopg2, psycopg2.extras
from psycopg2.pool import ThreadedConnectionPool

pool = None
def setup_db(app, **dbparams):
    global pool
    if not app.debug:
        import logging
        soh = logging.StreamHandler()
        soh.setLevel(logging.WARNING)
        logger = logging.getLogger()
        logger.addHandler(soh)

    pool = ThreadedConnectionPool(1, 20, **dbparams)

@contextmanager
def get_db_connection():
    """
    psycopg2 connection context manager.
    Fetch a connection from the connection pool and release it.
    """
    try:
        connection = pool.getconn()
        yield connection
    finally:
        pool.putconn(connection)

@contextmanager
def get_db_cursor(commit=False):
    """
    psycopg2 connection.cursor context manager.
    Creates a new cursor and closes it, commiting changes if specified.
    """
    with get_db_connection() as connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            yield cursor
            if commit:
                connection.commit()
        finally:
            cursor.close()
