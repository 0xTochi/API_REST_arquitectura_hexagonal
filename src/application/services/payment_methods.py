from domain.models import Payment
from ..exceptions import WrongBusinessRule
from datetime import datetime


class PaymentMethods:

    #def do(self, payment_date, document, code, value, repository):
    
    def insert_payment(self, payment_date, document, code, value, repository):

        payment = Payment(
             payment_date,
             document,
             code,
             value
        )

        
        repository.insert(payment)

        if int(value) == 1000000:
            return 'gracias por pagar todo tu arriendo'

        elif int(value) < 1000000:
            remaining = 1000000 - int(value)
            return f'gracias por el pago parcial, resta por pagar {remaining}'

    def update_payment(self, payment_date, document, code, value, repository):
    
        new_value = repository.select(document, code, value)
        
        repository.update( payment_date, document, code, new_value)
        if new_value >= 1000000:
            return 'gracias por pagar todo tu arriendo'
        elif int(new_value) < 1000000:
            remaining = 1000000 - int(new_value)
            return f'gracias por el pago parcial, resta por pagar {remaining}'