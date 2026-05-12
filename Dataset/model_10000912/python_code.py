from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class system_Category:

    def __init__(self, id: str, section: str, name: str, parent: system_Category, icon: str):
        self.id = id
        self.section = section
        self.name = name
        self.parent = parent
        self.icon = icon
        
        pass
    @property
    def icon(self):
        return self.__icon
    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, parent: system_Category):
        self.__parent = parent

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class marketing_Review:

    def __init__(self, id: str, product: marketing_Product, user: user_User, rating: datatypes_Number, description: str):
        self.id = id
        self.product = product
        self.user = user
        self.rating = rating
        self.description = description
        
        pass
    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product: marketing_Product):
        self.__product = product

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: datatypes_Number):
        self.__rating = rating

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: user_User):
        self.__user = user



class marketing_Tags:

    def __init__(self, id: str, busId_: user_Business, name: datatypes_String):
        self.id = id
        self.busId_ = busId_
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: datatypes_String):
        self.__name = name

    @property
    def busId_(self):
        return self.__busId_
    @busId_.setter
    def busId_(self, busId_: user_Business):
        self.__busId_ = busId_

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class marketing_Product:

    def __init__(self, id: str, busId: user_Business, name: str, ccategory: system_Category, price: float, active: bool, created: date, expires: date, reviews: marketing_Review):
        self.id = id
        self.busId = busId
        self.name = name
        self.ccategory = ccategory
        self.price = price
        self.active = active
        self.created = created
        self.expires = expires
        self.reviews = reviews
        
        pass
    @property
    def created(self):
        return self.__created
    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def ccategory(self):
        return self.__ccategory
    @ccategory.setter
    def ccategory(self, ccategory: system_Category):
        self.__ccategory = ccategory

    @property
    def expires(self):
        return self.__expires
    @expires.setter
    def expires(self, expires: date):
        self.__expires = expires

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def reviews(self, reviews: marketing_Review):
        self.__reviews = reviews

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def busId(self):
        return self.__busId
    @busId.setter
    def busId(self, busId: user_Business):
        self.__busId = busId

    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, active: bool):
        self.__active = active



class user_Provider:

    def __init__(self, uid: str, providerId: str, displayName: str, email: str, photoURL: str):
        self.uid = uid
        self.providerId = providerId
        self.displayName = displayName
        self.email = email
        self.photoURL = photoURL
        
        pass
    @property
    def displayName(self):
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def providerId(self):
        return self.__providerId
    @providerId.setter
    def providerId(self, providerId: str):
        self.__providerId = providerId

    @property
    def photoURL(self):
        return self.__photoURL
    @photoURL.setter
    def photoURL(self, photoURL: str):
        self.__photoURL = photoURL

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid



class user_Address:

    def __init__(self, street: str, suburb: str, state: str, postcode: str, country: datatypes_String):
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.country = country
        
        pass
    @property
    def suburb(self):
        return self.__suburb
    @suburb.setter
    def suburb(self, suburb: str):
        self.__suburb = suburb

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: datatypes_String):
        self.__country = country

    @property
    def postcode(self):
        return self.__postcode
    @postcode.setter
    def postcode(self, postcode: str):
        self.__postcode = postcode

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street: str):
        self.__street = street



class user_User:

    def __init__(self, id: datatypes_String, fiirstName: datatypes_String, lastName: datatypes_String, email: str, phone: datatypes_String, displayName: str, photoURL: str, address: user_Address, provider: user_Provider, interests: system_Category, wishlist: marketing_Product, purchaseHistory: marketing_Product, reviews: marketing_Review, business: user_Business):
        self.id = id
        self.fiirstName = fiirstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.displayName = displayName
        self.photoURL = photoURL
        self.address = address
        self.provider = provider
        self.interests = interests
        self.wishlist = wishlist
        self.purchaseHistory = purchaseHistory
        self.reviews = reviews
        self.business = business
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: user_Address):
        self.__address = address

    @property
    def wishlist(self):
        return self.__wishlist
    @wishlist.setter
    def wishlist(self, wishlist: marketing_Product):
        self.__wishlist = wishlist

    @property
    def photoURL(self):
        return self.__photoURL
    @photoURL.setter
    def photoURL(self, photoURL: str):
        self.__photoURL = photoURL

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName: datatypes_String):
        self.__lastName = lastName

    @property
    def business(self):
        return self.__business
    @business.setter
    def business(self, business: user_Business):
        self.__business = business

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: datatypes_String):
        self.__id = id

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def reviews(self, reviews: marketing_Review):
        self.__reviews = reviews

    @property
    def purchaseHistory(self):
        return self.__purchaseHistory
    @purchaseHistory.setter
    def purchaseHistory(self, purchaseHistory: marketing_Product):
        self.__purchaseHistory = purchaseHistory

    @property
    def fiirstName(self):
        return self.__fiirstName
    @fiirstName.setter
    def fiirstName(self, fiirstName: datatypes_String):
        self.__fiirstName = fiirstName

    @property
    def interests(self):
        return self.__interests
    @interests.setter
    def interests(self, interests: system_Category):
        self.__interests = interests

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: datatypes_String):
        self.__phone = phone

    @property
    def displayName(self):
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def provider(self):
        return self.__provider
    @provider.setter
    def provider(self, provider: user_Provider):
        self.__provider = provider



class user_Business:

    def __init__(self, id: datatypes_String, name: datatypes_String, category: str, website: str, email: str, phone: str, address: user_Address, adminUser: user_User, staffUsers: user_User, products: marketing_Product, avgRatings: datatypes_Number):
        self.id = id
        self.name = name
        self.category = category
        self.website = website
        self.email = email
        self.phone = phone
        self.address = address
        self.adminUser = adminUser
        self.staffUsers = staffUsers
        self.products = products
        self.avgRatings = avgRatings
        
        pass
    @property
    def adminUser(self):
        return self.__adminUser
    @adminUser.setter
    def adminUser(self, adminUser: user_User):
        self.__adminUser = adminUser

    @property
    def products(self):
        return self.__products
    @products.setter
    def products(self, products: marketing_Product):
        self.__products = products

    @property
    def staffUsers(self):
        return self.__staffUsers
    @staffUsers.setter
    def staffUsers(self, staffUsers: user_User):
        self.__staffUsers = staffUsers

    @property
    def avgRatings(self):
        return self.__avgRatings
    @avgRatings.setter
    def avgRatings(self, avgRatings: datatypes_Number):
        self.__avgRatings = avgRatings

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: user_Address):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: datatypes_String):
        self.__id = id

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def website(self):
        return self.__website
    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: datatypes_String):
        self.__name = name



class datatypes_Value(ABC):

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class datatypes_Array:

    def __init__(self, data: datatypes_Value):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: datatypes_Value):
        self.__data = data



class datatypes_Bool:

    def __init__(self, data: bool):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: bool):
        self.__data = data



class datatypes_String:

    def __init__(self, data: datatypes_String):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: datatypes_String):
        self.__data = data



class datatypes_Number:

    def __init__(self, data: int):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: int):
        self.__data = data



class datatypes_Null(ABC):

    pass


class datatypes_Json:

    def __init__(self, values: datatypes_Value):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values
    @values.setter
    def values(self, values: datatypes_Value):
        self.__values = values



class datatypes_Documents:

    def __init__(self, file: str, data: datatypes_Json, file_name: str, tab_counter: int):
        self.file = file
        self.data = data
        self.file_name = file_name
        self.tab_counter = tab_counter
        
        pass
    @property
    def tab_counter(self):
        return self.__tab_counter
    @tab_counter.setter
    def tab_counter(self, tab_counter: int):
        self.__tab_counter = tab_counter

    @property
    def file(self):
        return self.__file
    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: datatypes_Json):
        self.__data = data

    @property
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name = file_name

