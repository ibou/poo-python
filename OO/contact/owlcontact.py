
from contact.abstract import ContactSystem
from contact.helpers import verify_adress


class OwlContactSystem(ContactSystem):
    
    def __init__(self, address):
        verify_adress(address)
        self.address = address
        self.owl = "ebooo D."
        super().__init__()

    def send(self, message)->None:
        """Envoi le message."""
        print(f"Envoi du message <<{message}>> au {self.address} par {self.owl}")

    def __str__(self)->str:
        return f"****Message envoyé à {self.address}"


