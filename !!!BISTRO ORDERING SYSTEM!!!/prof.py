from dataclasses import dataclass
from profiletype import Profiletype


@dataclass
class Profile:
    login: str
    admin_type: Profiletype
    password: str



    