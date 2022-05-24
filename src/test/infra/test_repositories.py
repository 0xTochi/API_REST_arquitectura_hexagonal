from expects import (
    equal,
    expect
)

from infra.repositories import PaymentRepository
from test import BaseTestCase


class StubPayment:

    def as_dict(self):
        return {
            "documentoIdentificacionArrendatario": "1036946623",
            "codigoInmueble": "8871",
            "valorPagado": "500000",
            "fechaPago": "25/09/2020"
                }



class PaymentRepositoryTestCase(BaseTestCase):

    def test_it_inserts(self):
        payment = StubPayment()
        repository = PaymentRepository(self.db_connection)
        query = "SELECT * FROM pagos WHERE (documentoIdentificacionArrendatario = '1036946623' AND codigoInmueble = '8871' )"

        repository.insert(payment)

        expect(self._read_from_db(query)).to(
            equal({
                "documentoIdentificacionArrendatario": "1036946623",
                "codigoInmueble": "8871",
                "valorPagado": "500000",
                "fechaPago": "25/09/2020"
                })
        )

    def _read_from_db(self, sql_query):
        registry = self.db_connection.execute(sql_query).first()
        return dict(registry.items())
