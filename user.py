from dataclasses import dataclass

# DTO - Data Transfer Object

@dataclass
class User:
  
    def __init__(self, name:str, email:str, user_id:int):
        self.__name = None
        self.__email = None
        self.__user_id = None
        self.name = name
        self.email = email
        self.user_id = user_id


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        #valid
        self.__name = name
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        #valid
        self.__email = email

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id):
        #valid
        self.__user_id = user_id

    def change_email(self, new_email):
        self.email = new_email

    def create_task(self,title):
        pass
    
    def remove_task(self,task_id):
        pass
