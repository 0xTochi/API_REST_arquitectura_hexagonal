from domain.repositories import PaymentInterface
from infra.database import payment_table
from infra.repositories import BaseRepository
from sqlalchemy import text, and_


class PaymentRepository(BaseRepository, PaymentInterface):

    def insert(self, payment):
        with self.db_connection.begin():
            self.db_connection.execute(
                payment_table.insert(),
                payment.as_dict()
            )
    
    def select(self, document, code, value):
        t = text("SELECT valorPagado FROM pagos WHERE (documentoIdentificacionArrendatario = " + str(document) + " AND codigoInmueble = " + str(code) + " );")
        with self.db_connection.begin():
            result_query = self.db_connection.execute(t
                #payment_table.select().where(and_(payment_table.c.documentoIdentificacionArrendatario == document , payment_table.c.codigoInmueble == code )
            ).fetchone()

        return int(result_query[0]) + int(value)



    #(self, payment_date, document, code, value)
    def update(self, payment_date, document, code, value):
        t = text("INSERT or REPLACE into pagos VALUES ( " + str(document) + ", " + str(code) + ", " + str(payment_date) + ", " + str(value) + " );" )
        with self.db_connection.begin():
            self.db_connection.execute(t
                    #payment_table.update(),
                    #payment.as_dict()
                )

