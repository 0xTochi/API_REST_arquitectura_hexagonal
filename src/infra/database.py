import os

from sqlalchemy import (
    Column,
    MetaData,
    String,
    Integer,
    Table,
    Numeric,
    create_engine,
)

metadata = MetaData()

payment_table = Table(
    'pagos', metadata,
    Column('documentoIdentificacionArrendatario', String, primary_key=True),
    Column('codigoInmueble', String, primary_key=True),
    Column('fechaPago', String, nullable=False),
    Column('valorPagado', String, nullable=False)
)


def init_db_engine(db_url=None):
    uri = db_url or os.getenv('DB_URL')
    db_engine = create_engine(uri, convert_unicode=True)
    __create_tables_if_not_exists(db_engine)
    return db_engine


def db_connect(db_engine):
    return db_engine.connect()


def close_db_connection(db_connection):
    try:
        db_connection.close()
    except:
        pass


def __create_tables_if_not_exists(db_engine):
    payment_table.create(db_engine, checkfirst=True)
