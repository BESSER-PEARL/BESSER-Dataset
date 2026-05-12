from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Order:

    def __init__(self, Order_id: int, Order_num: int, Order_status: str, Order_edit: str, Order_delete: str):
        self.Order_id = Order_id
        self.Order_num = Order_num
        self.Order_status = Order_status
        self.Order_edit = Order_edit
        self.Order_delete = Order_delete
        
        pass
    @property
    def Order_edit(self):
        return self.__Order_edit
    @Order_edit.setter
    def Order_edit(self, Order_edit: str):
        self.__Order_edit = Order_edit

    @property
    def Order_status(self):
        return self.__Order_status
    @Order_status.setter
    def Order_status(self, Order_status: str):
        self.__Order_status = Order_status

    @property
    def Order_num(self):
        return self.__Order_num
    @Order_num.setter
    def Order_num(self, Order_num: int):
        self.__Order_num = Order_num

    @property
    def Order_id(self):
        return self.__Order_id
    @Order_id.setter
    def Order_id(self, Order_id: int):
        self.__Order_id = Order_id

    @property
    def Order_delete(self):
        return self.__Order_delete
    @Order_delete.setter
    def Order_delete(self, Order_delete: str):
        self.__Order_delete = Order_delete



class Chef:

    def __init__(self, Chef_id: int, Chef_name: str, Speciality: str, Status: str, order_id: int):
        self.Chef_id = Chef_id
        self.Chef_name = Chef_name
        self.Speciality = Speciality
        self.Status = Status
        self.order_id = order_id
        
        pass
    @property
    def Chef_name(self):
        return self.__Chef_name
    @Chef_name.setter
    def Chef_name(self, Chef_name: str):
        self.__Chef_name = Chef_name

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: int):
        self.__order_id = order_id

    @property
    def Chef_id(self):
        return self.__Chef_id
    @Chef_id.setter
    def Chef_id(self, Chef_id: int):
        self.__Chef_id = Chef_id

    @property
    def Speciality(self):
        return self.__Speciality
    @Speciality.setter
    def Speciality(self, Speciality: str):
        self.__Speciality = Speciality

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status



class Food_Items:

    def __init__(self, Items_id: int, Food_id: int, Material_id: int, quantity: int):
        self.Items_id = Items_id
        self.Food_id = Food_id
        self.Material_id = Material_id
        self.quantity = quantity
        
        pass
    @property
    def Material_id(self):
        return self.__Material_id
    @Material_id.setter
    def Material_id(self, Material_id: int):
        self.__Material_id = Material_id

    @property
    def Food_id(self):
        return self.__Food_id
    @Food_id.setter
    def Food_id(self, Food_id: int):
        self.__Food_id = Food_id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def Items_id(self):
        return self.__Items_id
    @Items_id.setter
    def Items_id(self, Items_id: int):
        self.__Items_id = Items_id



class Food_Sub_Category:

    def __init__(self, sub_id: int, sub_name: str, sub_descp: str, sub_image: str):
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.sub_descp = sub_descp
        self.sub_image = sub_image
        
        pass
    @property
    def sub_id(self):
        return self.__sub_id
    @sub_id.setter
    def sub_id(self, sub_id: int):
        self.__sub_id = sub_id

    @property
    def sub_image(self):
        return self.__sub_image
    @sub_image.setter
    def sub_image(self, sub_image: str):
        self.__sub_image = sub_image

    @property
    def sub_descp(self):
        return self.__sub_descp
    @sub_descp.setter
    def sub_descp(self, sub_descp: str):
        self.__sub_descp = sub_descp

    @property
    def sub_name(self):
        return self.__sub_name
    @sub_name.setter
    def sub_name(self, sub_name: str):
        self.__sub_name = sub_name



class Customer:

    def __init__(self, Customer_id: int, Customer_name: str, Status: str, TimeStamp: str, Table_id: int):
        self.Customer_id = Customer_id
        self.Customer_name = Customer_name
        self.Status = Status
        self.TimeStamp = TimeStamp
        self.Table_id = Table_id
        
        pass
    @property
    def TimeStamp(self):
        return self.__TimeStamp
    @TimeStamp.setter
    def TimeStamp(self, TimeStamp: str):
        self.__TimeStamp = TimeStamp

    @property
    def Customer_id(self):
        return self.__Customer_id
    @Customer_id.setter
    def Customer_id(self, Customer_id: int):
        self.__Customer_id = Customer_id

    @property
    def Customer_name(self):
        return self.__Customer_name
    @Customer_name.setter
    def Customer_name(self, Customer_name: str):
        self.__Customer_name = Customer_name

    @property
    def Table_id(self):
        return self.__Table_id
    @Table_id.setter
    def Table_id(self, Table_id: int):
        self.__Table_id = Table_id

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status



class Food_Category:

    def __init__(self, Category_id: int, Category_name: str, Category_descp: str, Category_image: str, sub_id: int):
        self.Category_id = Category_id
        self.Category_name = Category_name
        self.Category_descp = Category_descp
        self.Category_image = Category_image
        self.sub_id = sub_id
        
        pass
    @property
    def Category_name(self):
        return self.__Category_name
    @Category_name.setter
    def Category_name(self, Category_name: str):
        self.__Category_name = Category_name

    @property
    def Category_image(self):
        return self.__Category_image
    @Category_image.setter
    def Category_image(self, Category_image: str):
        self.__Category_image = Category_image

    @property
    def sub_id(self):
        return self.__sub_id
    @sub_id.setter
    def sub_id(self, sub_id: int):
        self.__sub_id = sub_id

    @property
    def Category_id(self):
        return self.__Category_id
    @Category_id.setter
    def Category_id(self, Category_id: int):
        self.__Category_id = Category_id

    @property
    def Category_descp(self):
        return self.__Category_descp
    @Category_descp.setter
    def Category_descp(self, Category_descp: str):
        self.__Category_descp = Category_descp



class Table:

    def __init__(self, Table_id: int, Table_num: int, Status: str):
        self.Table_id = Table_id
        self.Table_num = Table_num
        self.Status = Status
        
        pass
    @property
    def Table_id(self):
        return self.__Table_id
    @Table_id.setter
    def Table_id(self, Table_id: int):
        self.__Table_id = Table_id

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def Table_num(self):
        return self.__Table_num
    @Table_num.setter
    def Table_num(self, Table_num: int):
        self.__Table_num = Table_num



class Material:

    def __init__(self, Material_id: int, Material_name: str, Stock: str, Stock1: str, Unit: str):
        self.Material_id = Material_id
        self.Material_name = Material_name
        self.Stock = Stock
        self.Stock1 = Stock1
        self.Unit = Unit
        
        pass
    @property
    def Material_id(self):
        return self.__Material_id
    @Material_id.setter
    def Material_id(self, Material_id: int):
        self.__Material_id = Material_id

    @property
    def Stock1(self):
        return self.__Stock1
    @Stock1.setter
    def Stock1(self, Stock1: str):
        self.__Stock1 = Stock1

    @property
    def Stock(self):
        return self.__Stock
    @Stock.setter
    def Stock(self, Stock: str):
        self.__Stock = Stock

    @property
    def Material_name(self):
        return self.__Material_name
    @Material_name.setter
    def Material_name(self, Material_name: str):
        self.__Material_name = Material_name

    @property
    def Unit(self):
        return self.__Unit
    @Unit.setter
    def Unit(self, Unit: str):
        self.__Unit = Unit



class Food:

    def __init__(self, food_id: int, food_name: str, Category_id: int):
        self.food_id = food_id
        self.food_name = food_name
        self.Category_id = Category_id
        
        pass
    @property
    def food_id(self):
        return self.__food_id
    @food_id.setter
    def food_id(self, food_id: int):
        self.__food_id = food_id

    @property
    def food_name(self):
        return self.__food_name
    @food_name.setter
    def food_name(self, food_name: str):
        self.__food_name = food_name

    @property
    def Category_id(self):
        return self.__Category_id
    @Category_id.setter
    def Category_id(self, Category_id: int):
        self.__Category_id = Category_id

