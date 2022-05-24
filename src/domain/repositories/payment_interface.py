from abc import (
    ABCMeta,
    abstractmethod
)

class PaymentInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, payment):
        pass
