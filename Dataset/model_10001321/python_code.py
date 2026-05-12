from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class enter_password_UseCase:

    pass


class driver_planing_UseCase:

    pass


class remove_user_UseCase:

    pass


class logout_UseCase:

    pass


class return_the_money_to_the_customer_UseCase:

    pass


class cancle_with_driver_UseCase:

    pass


class cancle_UseCase:

    pass


class submit_information_UseCase:

    pass


class payment_UseCase:

    pass


class changing_seats_by_admin_UseCase:

    pass


class book_a_ticket_UseCase:

    pass


class exciting_package_UseCase:

    pass


class send_message_to_number_registered_UseCase:

    pass


class view_seat_UseCase:

    pass


class ticket_printing_UseCase:

    pass


class search_item__UseCase:

    pass


class browse_item_UseCase:

    pass


class captcha_UseCase:

    pass


class view_item_UseCase:

    pass


class enter_user_name_UseCase:

    pass


class login_UseCase:

    pass


class admin_Actor:

    pass


class driver_Actor:

    pass


class guest_user_Actor:

    pass


class user_Actor:

    pass





class submit_information:

    pass


class user_register:

    pass


class admin:

    pass


class driver:

    pass


class user:

    pass


class pay:

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class cancle:

    pass


class book_a_ticket:

    pass


class view_item:

    pass


class login:

    def __init__(self, password: str, username: str):
        self.password = password
        self.username = username
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username



class person:

    def __init__(self, username: str, name: str, phone: str, password: str):
        self.username = username
        self.name = name
        self.phone = phone
        self.password = password
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

