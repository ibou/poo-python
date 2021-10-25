
from contact.abstract import ContactSystem
from contact.helpers import validate_phone


class TextContactSystem(ContactSystem):
    def __init__(self, phone_number):
        super().__init__()
        validate_phone(phone_number)
        self.phone_number = phone_number

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" au numéro {self.phone_number}')

    def __str__(self):
        return f"Le numéro de téléphone est :::{self.phone_number}"
