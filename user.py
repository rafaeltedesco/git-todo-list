from dataclasses import dataclass

# DTO - Data Transfer Object

@dataclass
class Todo:
    name: str
    email: str
    user_id: int