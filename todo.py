from datetime import date
from typing import Optional
from dataclasses import dataclass

# DTO - Data Transfer Object

@dataclass
class Todo:
    name: str
    due_date: date
    description: Optional[str] = None
    is_done: bool = False
    # user_id: int

if __name__ == '__main__':
    todo = Todo(name='ler um livro', due_date=date(2025, 5, 20))
