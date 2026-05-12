from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Add_user_and_Assign_role_UseCase:

    pass


class Add_Edit_Delete_menus_menu_items__UseCase:

    pass


class Access_the_system_UseCase:

    pass


class Admin_Actor:

    pass


class Edit_personal_Information_UseCase:

    pass


class View_Food_products_UseCase:

    pass


class View_open_bill_and_ordered_items_UseCase:

    pass


class See_order_Status_UseCase:

    pass


class Write_Review_UseCase:

    pass


class order_food_UseCase:

    pass


class Log_in_logout_UseCase:

    pass


class Customer_Actor:

    pass


class Add_Edit_Delete_menus_UseCase:

    pass


class Login_Logout_UseCase:

    pass


class Operator_Actor:

    pass


class Update_status_of_orders_UseCase:

    pass


class View_order_transation_UseCase:

    pass





class Food:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class View_order_transation_UseCase1:

    pass
