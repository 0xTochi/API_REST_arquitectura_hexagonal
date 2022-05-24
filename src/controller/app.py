import os

from flask import (
    Flask,
    g,
    jsonify,
    request
)

from application.exceptions import WrongBusinessRule
from application.services import (
    ValidationPayment,
    PaymentMethods
)

from controller.exceptions import BadRequestException
from infra.database import (
    close_db_connection,
    init_db_engine,
    db_connect
)
from infra.repositories import PaymentRepository


app = Flask(__name__)


def get_db_connection(app):
    if 'db_con' not in g:
        db_engine = app.config.get('DB_ENGINE', None) or init_db_engine()
        g.db_con = db_connect(db_engine)
    return g.db_con


@app.errorhandler(BadRequestException)
@app.errorhandler(WrongBusinessRule)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response

@app.route('/api/pagos', methods=['GET', 'POST'])
def payment_method():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})

    obj = request.get_json()
    payment_date = obj['fechaPago']
    document = obj['documentoIdentificacionArrendatario']
    code = obj['codigoInmueble']
    value = obj['valorPagado']

    ValidationPayment().do(
        payment_date,
        document,
        code,
        value
        )

    try:
        payload = PaymentMethods().insert_payment(
        payment_date,
        document,
        code,
        value,
        repository=PaymentRepository(get_db_connection(app))
        )
    
    except:
        payload = PaymentMethods().update_payment(
        payment_date,
        document,
        code,
        value,
        repository=PaymentRepository(get_db_connection(app))
        )

    return jsonify(payload)


@app.teardown_appcontext
def teardown_db(exception=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        close_db_connection(db_con)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))