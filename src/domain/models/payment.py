class Payment:

    def __init__(self, payment_date, document, code, value):
        self.payment_date = payment_date
        self.document = document
        self.code = code
        self.value = value

    def __str__(self):
        return f'<Está pagando el usuario {self.document}, el inmueble {self.code}>'

    def as_dict(self):

        #TODO: Ojo a las fechas falta el formato

        return {
            'fechaPago': self.payment_date,
            'documentoIdentificacionArrendatario': self.document,
            'codigoInmueble': self.code,
            'valorPagado': self.value
        }