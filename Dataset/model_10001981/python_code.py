from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class DBController:

    def __init__(self, CustomerLogin: User_abstract_):
        self.CustomerLogin = CustomerLogin
        
        pass
    @property
    def CustomerLogin(self):
        return self.__CustomerLogin
    @CustomerLogin.setter
    def CustomerLogin(self, CustomerLogin: User_abstract_):
        self.__CustomerLogin = CustomerLogin



class Database:

    def __init__(self, instance: Database, url: str, username: str, password: str):
        self.instance = instance
        self.url = url
        self.username = username
        self.password = password
        
        pass
    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url: str):
        self.__url = url

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
    def instance(self):
        return self.__instance
    @instance.setter
    def instance(self, instance: Database):
        self.__instance = instance



class Customer:

    def __init__(self, phonenumber: str, address: str, creditCardInfo: str, attribute: str):
        self.phonenumber = phonenumber
        self.address = address
        self.creditCardInfo = creditCardInfo
        self.attribute = attribute
        
        pass
    @property
    def creditCardInfo(self):
        return self.__creditCardInfo
    @creditCardInfo.setter
    def creditCardInfo(self, creditCardInfo: str):
        self.__creditCardInfo = creditCardInfo

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def phonenumber(self):
        return self.__phonenumber
    @phonenumber.setter
    def phonenumber(self, phonenumber: str):
        self.__phonenumber = phonenumber

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address



class User_abstract_:

    def __init__(self, name: str, password: str, email: str, userId: str):
        self.name = name
        self.password = password
        self.email = email
        self.userId = userId
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class ProductShow:

    def __init__(self, productId: str, productName: str, category: str, brand: str, sex: int, priceSale: float, image: str):
        self.productId = productId
        self.productName = productName
        self.category = category
        self.brand = brand
        self.sex = sex
        self.priceSale = priceSale
        self.image = image
        
        pass
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: int):
        self.__sex = sex

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def priceSale(self):
        return self.__priceSale
    @priceSale.setter
    def priceSale(self, priceSale: float):
        self.__priceSale = priceSale

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category



class Shoe:

    def __init__(self, productId: str, productName: str, category: str, brand: str, brand2: str, size: int, sex: int, priceCost: float, description: str, color: str):
        self.productId = productId
        self.productName = productName
        self.category = category
        self.brand = brand
        self.brand2 = brand2
        self.size = size
        self.sex = sex
        self.priceCost = priceCost
        self.description = description
        self.color = color
        
        pass
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def brand2(self):
        return self.__brand2
    @brand2.setter
    def brand2(self, brand2: str):
        self.__brand2 = brand2

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def priceCost(self):
        return self.__priceCost
    @priceCost.setter
    def priceCost(self, priceCost: float):
        self.__priceCost = priceCost

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: int):
        self.__sex = sex

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand



class Class:

    pass


class ProductShow2:

    def __init__(self, productId: str, productName: str, category: str, brand: str, sex: int, priceCost: float):
        self.productId = productId
        self.productName = productName
        self.category = category
        self.brand = brand
        self.sex = sex
        self.priceCost = priceCost
        
        pass
    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def priceCost(self):
        return self.__priceCost
    @priceCost.setter
    def priceCost(self, priceCost: float):
        self.__priceCost = priceCost

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: int):
        self.__sex = sex



class _unnamed:

    pass


class ProductDetail:

    def __init__(self, productId: str, productName: str, category: str, brand: str, sex: int, priceCost: float):
        self.productId = productId
        self.productName = productName
        self.category = category
        self.brand = brand
        self.sex = sex
        self.priceCost = priceCost
        
        pass
    @property
    def priceCost(self):
        return self.__priceCost
    @priceCost.setter
    def priceCost(self, priceCost: float):
        self.__priceCost = priceCost

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: int):
        self.__sex = sex

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category



class Admin:

    pass


class ClassV:

    pass


class ClassU:

    pass


class ClassT:

    pass


class ClassS:

    pass


class ClassR:

    pass


class ClassQ:

    pass


class InterfaceO_Interface:

    pass


class ClassP:

    pass


class ClassN:

    pass


class ClassM:

    pass


class ClassL:

    pass


class ClassK:

    pass


class ClassH:

    pass


class ClassJ:

    pass


class ClassG:

    pass


class ClassF:

    pass


class ClassE:

    pass


class ClassD:

    pass


class ClassC:

    def __init__(self, packageAttribute: str, publicAttribute: float, privateAttribute: int, protectedAttribute: str):
        self.packageAttribute = packageAttribute
        self.publicAttribute = publicAttribute
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        
        pass
    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

    @property
    def publicAttribute(self):
        return self.__publicAttribute
    @publicAttribute.setter
    def publicAttribute(self, publicAttribute: float):
        self.__publicAttribute = publicAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute

    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute



class ClassB:

    pass


class ClassA:

    def __init__(self, publicAttribute: float, privateAttribute: int, protectedAttribute: str, packageAttribute: str):
        self.publicAttribute = publicAttribute
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        self.packageAttribute = packageAttribute
        
        pass
    @property
    def publicAttribute(self):
        return self.__publicAttribute
    @publicAttribute.setter
    def publicAttribute(self, publicAttribute: float):
        self.__publicAttribute = publicAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute

    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute

    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute



class BankAccount:

    def __init__(self, ownerName: str, balance: float):
        self.ownerName = ownerName
        self.balance = balance
        
        pass
    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

