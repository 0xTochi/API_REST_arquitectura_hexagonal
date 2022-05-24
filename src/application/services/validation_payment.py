from domain.models import Payment
from ..exceptions import WrongBusinessRule
from datetime import datetime


class ValidationPayment:

    def do(self, payment_date, document, code, value):
        


        try:
            datetime.strptime(payment_date, '%d/%m/%Y')
        except:
            error = {'fechaPago': 'Formato de fecha incorrecto' }
            raise WrongBusinessRule(error)   

        try:
            int(document)
        except:
            error = {'documentoIdentificacionArrendatario': 'No es numérico' }
            raise WrongBusinessRule(error)    

        try:
            str(code)
        except:
            error = {'codigoInmueble': 'No es alfanumérico' }
            raise WrongBusinessRule(error)            

        if (int(value) > 1000000) | (int(value) < 1):
            error = {'valorPagado': 'El valor ingresado a pagar no es válido'}
            raise WrongBusinessRule(error)
        

        day_month = datetime.strptime(payment_date, '%d/%m/%Y').day
        if (day_month % 2) == 0:
            error = {'fechaPago': 'lo siento pero no se puede recibir el pago por decreto de administración'}
            raise WrongBusinessRule(error)
