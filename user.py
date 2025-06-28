# DTO - Data Transfer Object


class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def change_email(self, new_email):
        self.email = new_email

    def create_task(self, title):
        pass

    def remove_task(self, task_id):
        pass

