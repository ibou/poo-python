""""Some methode for helping use systems"""


from typing import List

from contact.user import User


def verify_adress(address) -> None:
    """Fausse fonction qui retourne True."""
    return True


def validate_phone(phone_number: str) -> bool:
    """Retourne True par défaut."""
    return True


def send_mass_messages(message: str, user_list: List[User]) -> None:
    """ Envoie message"""
    for user in user_list:
        mail_merge = {"name": user.name, "contact_info": user.contact_method}
        customised_message = message.format(**mail_merge)
        user.send(customised_message)
