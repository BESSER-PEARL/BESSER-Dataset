from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class OrderChannel(Enum):
    WEB = "WEB"
    MAIL = "MAIL"
    PHONE = "PHONE"


############################################
# Definition of Classes
############################################

class Address:

    pass
class customerDsl_StreetAddress(Address):

    def __init__(self, street: str, city: str):
        self.street = street
        self.city = city
        
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

class customerDsl_Address:

    def __init__(self, name: str, zip: str, customerDsl_Address: "customerDsl_Customer" = None, customerDsl_Address12: "customerDsl_Order" = None):
        self.name = name
        self.zip = zip
        self.customerDsl_Address = customerDsl_Address
        self.customerDsl_Address12 = customerDsl_Address12
        
    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customerDsl_Address12(self):
        return self.__customerDsl_Address12

    @customerDsl_Address12.setter
    def customerDsl_Address12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Address__customerDsl_Address12", None)
        self.__customerDsl_Address12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_Order11"):
                opp_val = getattr(old_value, "customerDsl_Order11", None)
                if opp_val == self:
                    setattr(old_value, "customerDsl_Order11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_Order11"):
                opp_val = getattr(value, "customerDsl_Order11", None)
                setattr(value, "customerDsl_Order11", self)

    @property
    def customerDsl_Address(self):
        return self.__customerDsl_Address

    @customerDsl_Address.setter
    def customerDsl_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Address__customerDsl_Address", None)
        self.__customerDsl_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_Customer6"):
                opp_val = getattr(old_value, "customerDsl_Customer6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_Customer6"):
                opp_val = getattr(value, "customerDsl_Customer6", None)
                if opp_val is None:
                    setattr(value, "customerDsl_Customer6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class customerDsl_Product:

    def __init__(self, name: str, price: int, customerDsl_Product: "customerDsl_CustomerDb" = None):
        self.name = name
        self.price = price
        self.customerDsl_Product = customerDsl_Product
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def customerDsl_Product(self):
        return self.__customerDsl_Product

    @customerDsl_Product.setter
    def customerDsl_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Product__customerDsl_Product", None)
        self.__customerDsl_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_CustomerDb4"):
                opp_val = getattr(old_value, "customerDsl_CustomerDb4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_CustomerDb4"):
                opp_val = getattr(value, "customerDsl_CustomerDb4", None)
                if opp_val is None:
                    setattr(value, "customerDsl_CustomerDb4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class customerDsl_Order:

    def __init__(self, name: str, channel: str, customerDsl_Order8: "customerDsl_Customer" = None, customerDsl_Order: "customerDsl_CustomerDb" = None, customerDsl_Order11: "customerDsl_Address" = None):
        self.name = name
        self.channel = channel
        self.customerDsl_Order8 = customerDsl_Order8
        self.customerDsl_Order = customerDsl_Order
        self.customerDsl_Order11 = customerDsl_Order11
        
    @property
    def channel(self) -> str:
        return self.__channel

    @channel.setter
    def channel(self, channel: str):
        self.__channel = channel

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customerDsl_Order11(self):
        return self.__customerDsl_Order11

    @customerDsl_Order11.setter
    def customerDsl_Order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Order__customerDsl_Order11", None)
        self.__customerDsl_Order11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_Address12"):
                opp_val = getattr(old_value, "customerDsl_Address12", None)
                if opp_val == self:
                    setattr(old_value, "customerDsl_Address12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_Address12"):
                opp_val = getattr(value, "customerDsl_Address12", None)
                setattr(value, "customerDsl_Address12", self)

    @property
    def customerDsl_Order8(self):
        return self.__customerDsl_Order8

    @customerDsl_Order8.setter
    def customerDsl_Order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Order__customerDsl_Order8", None)
        self.__customerDsl_Order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_Customer9"):
                opp_val = getattr(old_value, "customerDsl_Customer9", None)
                if opp_val == self:
                    setattr(old_value, "customerDsl_Customer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_Customer9"):
                opp_val = getattr(value, "customerDsl_Customer9", None)
                setattr(value, "customerDsl_Customer9", self)

    @property
    def customerDsl_Order(self):
        return self.__customerDsl_Order

    @customerDsl_Order.setter
    def customerDsl_Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Order__customerDsl_Order", None)
        self.__customerDsl_Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_CustomerDb2"):
                opp_val = getattr(old_value, "customerDsl_CustomerDb2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_CustomerDb2"):
                opp_val = getattr(value, "customerDsl_CustomerDb2", None)
                if opp_val is None:
                    setattr(value, "customerDsl_CustomerDb2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class customerDsl_Customer:

    def __init__(self, name: str, fullName: str, customerDsl_Customer9: "customerDsl_Order" = None, customerDsl_Customer: "customerDsl_CustomerDb" = None, customerDsl_Customer6: set["customerDsl_Address"] = None):
        self.name = name
        self.fullName = fullName
        self.customerDsl_Customer9 = customerDsl_Customer9
        self.customerDsl_Customer = customerDsl_Customer
        self.customerDsl_Customer6 = customerDsl_Customer6 if customerDsl_Customer6 is not None else set()
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customerDsl_Customer9(self):
        return self.__customerDsl_Customer9

    @customerDsl_Customer9.setter
    def customerDsl_Customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Customer__customerDsl_Customer9", None)
        self.__customerDsl_Customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_Order8"):
                opp_val = getattr(old_value, "customerDsl_Order8", None)
                if opp_val == self:
                    setattr(old_value, "customerDsl_Order8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_Order8"):
                opp_val = getattr(value, "customerDsl_Order8", None)
                setattr(value, "customerDsl_Order8", self)

    @property
    def customerDsl_Customer6(self):
        return self.__customerDsl_Customer6

    @customerDsl_Customer6.setter
    def customerDsl_Customer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Customer__customerDsl_Customer6", None)
        self.__customerDsl_Customer6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customerDsl_Address"):
                    opp_val = getattr(item, "customerDsl_Address", None)
                    
                    if opp_val == self:
                        setattr(item, "customerDsl_Address", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customerDsl_Address"):
                    opp_val = getattr(item, "customerDsl_Address", None)
                    
                    setattr(item, "customerDsl_Address", self)
                    

    @property
    def customerDsl_Customer(self):
        return self.__customerDsl_Customer

    @customerDsl_Customer.setter
    def customerDsl_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDsl_Customer__customerDsl_Customer", None)
        self.__customerDsl_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerDsl_CustomerDb"):
                opp_val = getattr(old_value, "customerDsl_CustomerDb", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerDsl_CustomerDb"):
                opp_val = getattr(value, "customerDsl_CustomerDb", None)
                if opp_val is None:
                    setattr(value, "customerDsl_CustomerDb", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class customerDsl_CustomerDb:

    pass
class customerDsl_POBox(Address):

    def __init__(self, number: int):
        self.number = number
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number
