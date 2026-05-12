from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Category:

    def __init__(self, id: int, name: str, photoPath: str, product14: set["Product"] = None):
        self.id = id
        self.name = name
        self.photoPath = photoPath
        self.product14 = product14 if product14 is not None else set()
        
        pass
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

    @property
    def photoPath(self):
        return self.__photoPath
    @photoPath.setter
    def photoPath(self, photoPath: str):
        self.__photoPath = photoPath

    @property
    def product14(self):
        return self.__product14
    @product14.setter
    def product14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__product14", None)
        self.__product14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "category15"):
                    opp_val = getattr(item, "category15", None)
                    
                    if opp_val == self:
                        setattr(item, "category15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "category15"):
                    opp_val = getattr(item, "category15", None)
                    
                    setattr(item, "category15", self)
                    



class Offer:

    def __init__(self, id: int, discount: int, beginDate: str, endDate: str, product13: "Product" = None):
        self.id = id
        self.discount = discount
        self.beginDate = beginDate
        self.endDate = endDate
        self.product13 = product13
        
        pass
    @property
    def endDate(self):
        return self.__endDate
    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def beginDate(self):
        return self.__beginDate
    @beginDate.setter
    def beginDate(self, beginDate: str):
        self.__beginDate = beginDate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount: int):
        self.__discount = discount

    @property
    def product13(self):
        return self.__product13
    @product13.setter
    def product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Offer__product13", None)
        self.__product13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "offer12"):
                opp_val = getattr(old_value, "offer12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "offer12"):
                opp_val = getattr(value, "offer12", None)
                if opp_val is None:
                    setattr(value, "offer12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Product:

    def __init__(self, id: int, name: str, description: str, price: int, photoPath: str, offer12: set["Offer"] = None, category15: "Category" = None, store17: "Store" = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.photoPath = photoPath
        self.offer12 = offer12 if offer12 is not None else set()
        self.category15 = category15
        self.store17 = store17
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def photoPath(self):
        return self.__photoPath
    @photoPath.setter
    def photoPath(self, photoPath: str):
        self.__photoPath = photoPath

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

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def store17(self):
        return self.__store17
    @store17.setter
    def store17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__store17", None)
        self.__store17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product16"):
                opp_val = getattr(old_value, "product16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product16"):
                opp_val = getattr(value, "product16", None)
                if opp_val is None:
                    setattr(value, "product16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def offer12(self):
        return self.__offer12
    @offer12.setter
    def offer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__offer12", None)
        self.__offer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product13"):
                    opp_val = getattr(item, "product13", None)
                    
                    if opp_val == self:
                        setattr(item, "product13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product13"):
                    opp_val = getattr(item, "product13", None)
                    
                    setattr(item, "product13", self)
                    

    @property
    def category15(self):
        return self.__category15
    @category15.setter
    def category15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__category15", None)
        self.__category15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product14"):
                opp_val = getattr(old_value, "product14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product14"):
                opp_val = getattr(value, "product14", None)
                if opp_val is None:
                    setattr(value, "product14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, id: int, createdAt: str, amount: int, buyer11: "Buyer" = None):
        self.id = id
        self.createdAt = createdAt
        self.amount = amount
        self.buyer11 = buyer11
        
        pass
    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def buyer11(self):
        return self.__buyer11
    @buyer11.setter
    def buyer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__buyer11", None)
        self.__buyer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                if opp_val is None:
                    setattr(value, "order10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Store:

    def __init__(self, id: int, name: str, photoPath: str, product16: set["Product"] = None, address6: "Address" = None, seller9: "Seller" = None):
        self.id = id
        self.name = name
        self.photoPath = photoPath
        self.product16 = product16 if product16 is not None else set()
        self.address6 = address6
        self.seller9 = seller9
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def photoPath(self):
        return self.__photoPath
    @photoPath.setter
    def photoPath(self, photoPath: str):
        self.__photoPath = photoPath

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def product16(self):
        return self.__product16
    @product16.setter
    def product16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__product16", None)
        self.__product16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "store17"):
                    opp_val = getattr(item, "store17", None)
                    
                    if opp_val == self:
                        setattr(item, "store17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "store17"):
                    opp_val = getattr(item, "store17", None)
                    
                    setattr(item, "store17", self)
                    

    @property
    def address6(self):
        return self.__address6
    @address6.setter
    def address6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__address6", None)
        self.__address6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store7"):
                opp_val = getattr(old_value, "store7", None)
                if opp_val == self:
                    setattr(old_value, "store7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store7"):
                opp_val = getattr(value, "store7", None)
                setattr(value, "store7", self)

    @property
    def seller9(self):
        return self.__seller9
    @seller9.setter
    def seller9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__seller9", None)
        self.__seller9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store8"):
                opp_val = getattr(old_value, "store8", None)
                if opp_val == self:
                    setattr(old_value, "store8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store8"):
                opp_val = getattr(value, "store8", None)
                setattr(value, "store8", self)



class Address:

    def __init__(self, id: int, street: str, zipCode: str, city: str, country: str, position4: "Position" = None, store7: "Store" = None):
        self.id = id
        self.street = street
        self.zipCode = zipCode
        self.city = city
        self.country = country
        self.position4 = position4
        self.store7 = store7
        
        pass
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def zipCode(self):
        return self.__zipCode
    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def store7(self):
        return self.__store7
    @store7.setter
    def store7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__store7", None)
        self.__store7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address6"):
                opp_val = getattr(old_value, "address6", None)
                if opp_val == self:
                    setattr(old_value, "address6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address6"):
                opp_val = getattr(value, "address6", None)
                setattr(value, "address6", self)

    @property
    def position4(self):
        return self.__position4
    @position4.setter
    def position4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__position4", None)
        self.__position4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address5"):
                opp_val = getattr(old_value, "address5", None)
                if opp_val == self:
                    setattr(old_value, "address5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address5"):
                opp_val = getattr(value, "address5", None)
                setattr(value, "address5", self)



class Position:

    def __init__(self, id: int, longitude: str, latitude: str, createdAt: str, buyer3: "Buyer" = None, address5: "Address" = None):
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
        self.createdAt = createdAt
        self.buyer3 = buyer3
        self.address5 = address5
        
        pass
    @property
    def latitude(self):
        return self.__latitude
    @latitude.setter
    def latitude(self, latitude: str):
        self.__latitude = latitude

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: str):
        self.__createdAt = createdAt

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def longitude(self):
        return self.__longitude
    @longitude.setter
    def longitude(self, longitude: str):
        self.__longitude = longitude

    @property
    def address5(self):
        return self.__address5
    @address5.setter
    def address5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Position__address5", None)
        self.__address5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "position4"):
                opp_val = getattr(old_value, "position4", None)
                if opp_val == self:
                    setattr(old_value, "position4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "position4"):
                opp_val = getattr(value, "position4", None)
                setattr(value, "position4", self)

    @property
    def buyer3(self):
        return self.__buyer3
    @buyer3.setter
    def buyer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Position__buyer3", None)
        self.__buyer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "position2"):
                opp_val = getattr(old_value, "position2", None)
                if opp_val == self:
                    setattr(old_value, "position2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "position2"):
                opp_val = getattr(value, "position2", None)
                setattr(value, "position2", self)



class Basket:

    def __init__(self, id: int, updatedAt: str, buyer1: "Buyer" = None):
        self.id = id
        self.updatedAt = updatedAt
        self.buyer1 = buyer1
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def updatedAt(self):
        return self.__updatedAt
    @updatedAt.setter
    def updatedAt(self, updatedAt: str):
        self.__updatedAt = updatedAt

    @property
    def buyer1(self):
        return self.__buyer1
    @buyer1.setter
    def buyer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Basket__buyer1", None)
        self.__buyer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basket0"):
                opp_val = getattr(old_value, "basket0", None)
                if opp_val == self:
                    setattr(old_value, "basket0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basket0"):
                opp_val = getattr(value, "basket0", None)
                setattr(value, "basket0", self)



class Seller:

    def __init__(self, registerNumber: str, store8: "Store" = None):
        self.registerNumber = registerNumber
        self.store8 = store8
        
        pass
    @property
    def registerNumber(self):
        return self.__registerNumber
    @registerNumber.setter
    def registerNumber(self, registerNumber: str):
        self.__registerNumber = registerNumber

    @property
    def store8(self):
        return self.__store8
    @store8.setter
    def store8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seller__store8", None)
        self.__store8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seller9"):
                opp_val = getattr(old_value, "seller9", None)
                if opp_val == self:
                    setattr(old_value, "seller9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seller9"):
                opp_val = getattr(value, "seller9", None)
                setattr(value, "seller9", self)



class Buyer:

    def __init__(self, email: str, basket0: "Basket" = None, position2: "Position" = None, order10: set["Order"] = None):
        self.email = email
        self.basket0 = basket0
        self.position2 = position2
        self.order10 = order10 if order10 is not None else set()
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def position2(self):
        return self.__position2
    @position2.setter
    def position2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Buyer__position2", None)
        self.__position2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "buyer3"):
                opp_val = getattr(old_value, "buyer3", None)
                if opp_val == self:
                    setattr(old_value, "buyer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buyer3"):
                opp_val = getattr(value, "buyer3", None)
                setattr(value, "buyer3", self)

    @property
    def basket0(self):
        return self.__basket0
    @basket0.setter
    def basket0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Buyer__basket0", None)
        self.__basket0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "buyer1"):
                opp_val = getattr(old_value, "buyer1", None)
                if opp_val == self:
                    setattr(old_value, "buyer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buyer1"):
                opp_val = getattr(value, "buyer1", None)
                setattr(value, "buyer1", self)

    @property
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Buyer__order10", None)
        self.__order10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "buyer11"):
                    opp_val = getattr(item, "buyer11", None)
                    
                    if opp_val == self:
                        setattr(item, "buyer11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "buyer11"):
                    opp_val = getattr(item, "buyer11", None)
                    
                    setattr(item, "buyer11", self)
                    



class User:

    def __init__(self, id: str, attribute: str, username: str, password: str, firstname: str, lastname: str):
        self.id = id
        self.attribute = attribute
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

