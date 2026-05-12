from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class MAINTAINS_THE_PRODUCTS_SERVICES_UseCase:

    pass


class ADMINISTRATOR_Actor:

    pass


class SUPPORT_AND_FEEDBACK_UseCase:

    pass


class DELIVERS_THE_PRODUCT_UseCase:

    pass


class PAYS_THE_BILL_UseCase:

    pass


class SELECTS_THE_MODE_OF_PAYMENT_UseCase:

    pass


class ADDS_ITEMS_SERVICE_TO_CART_UseCase:

    pass


class SELECTS_THE_ITEMS_SERVICE_UseCase:

    pass


class VISITS_ECOMMERCE_TAB_UseCase:

    pass


class CUSTOMER_Actor:

    pass





class Transaction:

    def __init__(self, cashondelivery: int, debitcard: int, creditcard: int):
        self.cashondelivery = cashondelivery
        self.debitcard = debitcard
        self.creditcard = creditcard
        
        pass
    @property
    def debitcard(self):
        return self.__debitcard
    @debitcard.setter
    def debitcard(self, debitcard: int):
        self.__debitcard = debitcard

    @property
    def cashondelivery(self):
        return self.__cashondelivery
    @cashondelivery.setter
    def cashondelivery(self, cashondelivery: int):
        self.__cashondelivery = cashondelivery

    @property
    def creditcard(self):
        return self.__creditcard
    @creditcard.setter
    def creditcard(self, creditcard: int):
        self.__creditcard = creditcard



class Warehouse:

    def __init__(self, database: str, location: str):
        self.database = database
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def database(self):
        return self.__database
    @database.setter
    def database(self, database: str):
        self.__database = database



class Product:

    def __init__(self, name: str, id: int, type: str):
        self.name = name
        self.id = id
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Order:

    def __init__(self, item: str, quantity: int, list: str, attribute: str):
        self.item = item
        self.quantity = quantity
        self.list = list
        self.attribute = attribute
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self, item: str):
        self.__item = item

    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, list: str):
        self.__list = list



class Customer:

    def __init__(self, name: str, id: int, mailid: str, address: str, phoneno: int):
        self.name = name
        self.id = id
        self.mailid = mailid
        self.address = address
        self.phoneno = phoneno
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def mailid(self):
        return self.__mailid
    @mailid.setter
    def mailid(self, mailid: str):
        self.__mailid = mailid

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

