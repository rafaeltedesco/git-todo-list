from dataclasses import dataclass

# DTO - Data Transfer Object

@dataclass
class User:
    name: str
    email: str
    user_id: int