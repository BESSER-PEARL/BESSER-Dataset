from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Hall_book:

    def __init__(self, get_hall_no: str, get_room_type: str, cost_per_day: str):
        self.get_hall_no = get_hall_no
        self.get_room_type = get_room_type
        self.cost_per_day = cost_per_day
        
        pass
    @property
    def get_room_type(self):
        return self.__get_room_type
    @get_room_type.setter
    def get_room_type(self, get_room_type: str):
        self.__get_room_type = get_room_type

    @property
    def cost_per_day(self):
        return self.__cost_per_day
    @cost_per_day.setter
    def cost_per_day(self, cost_per_day: str):
        self.__cost_per_day = cost_per_day

    @property
    def get_hall_no(self):
        return self.__get_hall_no
    @get_hall_no.setter
    def get_hall_no(self, get_hall_no: str):
        self.__get_hall_no = get_hall_no



class View_and_place_order:

    def __init__(self, order_view: User, place_order: User):
        self.order_view = order_view
        self.place_order = place_order
        
        pass
    @property
    def place_order(self):
        return self.__place_order
    @place_order.setter
    def place_order(self, place_order: User):
        self.__place_order = place_order

    @property
    def order_view(self):
        return self.__order_view
    @order_view.setter
    def order_view(self, order_view: User):
        self.__order_view = order_view



class Decoration_book:

    def __init__(self, Decor_type: Decoration_book, cost: str, Square_feet: str):
        self.Decor_type = Decor_type
        self.cost = cost
        self.Square_feet = Square_feet
        
        pass
    @property
    def Decor_type(self):
        return self.__Decor_type
    @Decor_type.setter
    def Decor_type(self, Decor_type: Decoration_book):
        self.__Decor_type = Decor_type

    @property
    def Square_feet(self):
        return self.__Square_feet
    @Square_feet.setter
    def Square_feet(self, Square_feet: str):
        self.__Square_feet = Square_feet

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost



class Catering_book:

    def __init__(self, get_menu: str, get_cost: str):
        self.get_menu = get_menu
        self.get_cost = get_cost
        
        pass
    @property
    def get_cost(self):
        return self.__get_cost
    @get_cost.setter
    def get_cost(self, get_cost: str):
        self.__get_cost = get_cost

    @property
    def get_menu(self):
        return self.__get_menu
    @get_menu.setter
    def get_menu(self, get_menu: str):
        self.__get_menu = get_menu



class View_and_update:

    def __init__(self, order_view: Admin, update_order: Admin):
        self.order_view = order_view
        self.update_order = update_order
        
        pass
    @property
    def order_view(self):
        return self.__order_view
    @order_view.setter
    def order_view(self, order_view: Admin):
        self.__order_view = order_view

    @property
    def update_order(self):
        return self.__update_order
    @update_order.setter
    def update_order(self, update_order: Admin):
        self.__update_order = update_order



class Hall:

    def __init__(self, get_hall_no: str, get_room_type: str, cost_per_day: str):
        self.get_hall_no = get_hall_no
        self.get_room_type = get_room_type
        self.cost_per_day = cost_per_day
        
        pass
    @property
    def cost_per_day(self):
        return self.__cost_per_day
    @cost_per_day.setter
    def cost_per_day(self, cost_per_day: str):
        self.__cost_per_day = cost_per_day

    @property
    def get_room_type(self):
        return self.__get_room_type
    @get_room_type.setter
    def get_room_type(self, get_room_type: str):
        self.__get_room_type = get_room_type

    @property
    def get_hall_no(self):
        return self.__get_hall_no
    @get_hall_no.setter
    def get_hall_no(self, get_hall_no: str):
        self.__get_hall_no = get_hall_no



class Decoration:

    def __init__(self, Decor_type: Decoration, cost: str, Square_feet: str):
        self.Decor_type = Decor_type
        self.cost = cost
        self.Square_feet = Square_feet
        
        pass
    @property
    def Square_feet(self):
        return self.__Square_feet
    @Square_feet.setter
    def Square_feet(self, Square_feet: str):
        self.__Square_feet = Square_feet

    @property
    def Decor_type(self):
        return self.__Decor_type
    @Decor_type.setter
    def Decor_type(self, Decor_type: Decoration):
        self.__Decor_type = Decor_type

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost



class Catering:

    def __init__(self, get_menu: str, get_cost: str):
        self.get_menu = get_menu
        self.get_cost = get_cost
        
        pass
    @property
    def get_cost(self):
        return self.__get_cost
    @get_cost.setter
    def get_cost(self, get_cost: str):
        self.__get_cost = get_cost

    @property
    def get_menu(self):
        return self.__get_menu
    @get_menu.setter
    def get_menu(self, get_menu: str):
        self.__get_menu = get_menu



class Admin:

    def __init__(self, userID: int, userName: str, password: str):
        self.userID = userID
        self.userName = userName
        self.password = password
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID



class User:

    def __init__(self, userID: int, userName: str, password: str):
        self.userID = userID
        self.userName = userName
        self.password = password
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class void:

    pass


class LOGIN:

    def __init__(self, f_Name: str, l_Name: str, user_Name: str, password: str):
        self.f_Name = f_Name
        self.l_Name = l_Name
        self.user_Name = user_Name
        self.password = password
        
        pass
    @property
    def l_Name(self):
        return self.__l_Name
    @l_Name.setter
    def l_Name(self, l_Name: str):
        self.__l_Name = l_Name

    @property
    def user_Name(self):
        return self.__user_Name
    @user_Name.setter
    def user_Name(self, user_Name: str):
        self.__user_Name = user_Name

    @property
    def f_Name(self):
        return self.__f_Name
    @f_Name.setter
    def f_Name(self, f_Name: str):
        self.__f_Name = f_Name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

