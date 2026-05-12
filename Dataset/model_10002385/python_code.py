from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, customerId: int, customerName: str, customerAddress: str, customerPhone: int, customerPaymentInfo: str, user1: "User" = None, Customer_Shopping_Cart_04: "Shopping_Cart" = None, search6: set["Search"] = None):
        self.customerId = customerId
        self.customerName = customerName
        self.customerAddress = customerAddress
        self.customerPhone = customerPhone
        self.customerPaymentInfo = customerPaymentInfo
        self.user1 = user1
        self.Customer_Shopping_Cart_04 = Customer_Shopping_Cart_04
        self.search6 = search6 if search6 is not None else set()
        
        pass
    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def customerPaymentInfo(self):
        return self.__customerPaymentInfo
    @customerPaymentInfo.setter
    def customerPaymentInfo(self, customerPaymentInfo: str):
        self.__customerPaymentInfo = customerPaymentInfo

    @property
    def customerPhone(self):
        return self.__customerPhone
    @customerPhone.setter
    def customerPhone(self, customerPhone: int):
        self.__customerPhone = customerPhone

    @property
    def customerAddress(self):
        return self.__customerAddress
    @customerAddress.setter
    def customerAddress(self, customerAddress: str):
        self.__customerAddress = customerAddress

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def Customer_Shopping_Cart_04(self):
        return self.__Customer_Shopping_Cart_04
    @Customer_Shopping_Cart_04.setter
    def Customer_Shopping_Cart_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Shopping_Cart_04", None)
        self.__Customer_Shopping_Cart_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addBookToCart5"):
                opp_val = getattr(old_value, "addBookToCart5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addBookToCart5"):
                opp_val = getattr(value, "addBookToCart5", None)
                if opp_val is None:
                    setattr(value, "addBookToCart5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def search6(self):
        return self.__search6
    @search6.setter
    def search6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__search6", None)
        self.__search6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "searchBook7"):
                    opp_val = getattr(item, "searchBook7", None)
                    
                    if opp_val == self:
                        setattr(item, "searchBook7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "searchBook7"):
                    opp_val = getattr(item, "searchBook7", None)
                    
                    setattr(item, "searchBook7", self)
                    

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if opp_val == self:
                    setattr(old_value, "customer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                setattr(value, "customer0", self)



class User:

    def __init__(self, userId: int, password: str, customer0: "Customer" = None, admin2: set["Admin"] = None):
        self.userId = userId
        self.password = password
        self.customer0 = customer0
        self.admin2 = admin2 if admin2 is not None else set()
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def admin2(self):
        return self.__admin2
    @admin2.setter
    def admin2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__admin2", None)
        self.__admin2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_addUserAsMember3"):
                    opp_val = getattr(item, "_addUserAsMember3", None)
                    
                    if opp_val == self:
                        setattr(item, "_addUserAsMember3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_addUserAsMember3"):
                    opp_val = getattr(item, "_addUserAsMember3", None)
                    
                    setattr(item, "_addUserAsMember3", self)
                    



class Payment:

    def __init__(self, paymentId: int, paymentTotal: str):
        self.paymentId = paymentId
        self.paymentTotal = paymentTotal
        
        pass
    @property
    def paymentTotal(self):
        return self.__paymentTotal
    @paymentTotal.setter
    def paymentTotal(self, paymentTotal: str):
        self.__paymentTotal = paymentTotal

    @property
    def paymentId(self):
        return self.__paymentId
    @paymentId.setter
    def paymentId(self, paymentId: int):
        self.__paymentId = paymentId



class Bookstore_Shop:

    def __init__(self, User: User, Admin: Admin):
        self.User = User
        self.Admin = Admin
        
        pass
    @property
    def Admin(self):
        return self.__Admin
    @Admin.setter
    def Admin(self, Admin: Admin):
        self.__Admin = Admin

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: User):
        self.__User = User



class Order:

    def __init__(self, orderId: int, price: str, customerId: int, NumberOfBooks: int, orderIsUndatedToCart11: "Shopping_Cart" = None, addBook12: "Admin" = None):
        self.orderId = orderId
        self.price = price
        self.customerId = customerId
        self.NumberOfBooks = NumberOfBooks
        self.orderIsUndatedToCart11 = orderIsUndatedToCart11
        self.addBook12 = addBook12
        
        pass
    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def NumberOfBooks(self):
        return self.__NumberOfBooks
    @NumberOfBooks.setter
    def NumberOfBooks(self, NumberOfBooks: int):
        self.__NumberOfBooks = NumberOfBooks

    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def addBook12(self):
        return self.__addBook12
    @addBook12.setter
    def addBook12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__addBook12", None)
        self.__addBook12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderBook13"):
                opp_val = getattr(old_value, "orderBook13", None)
                if opp_val == self:
                    setattr(old_value, "orderBook13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderBook13"):
                opp_val = getattr(value, "orderBook13", None)
                setattr(value, "orderBook13", self)

    @property
    def orderIsUndatedToCart11(self):
        return self.__orderIsUndatedToCart11
    @orderIsUndatedToCart11.setter
    def orderIsUndatedToCart11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderIsUndatedToCart11", None)
        self.__orderIsUndatedToCart11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderBook10"):
                opp_val = getattr(old_value, "orderBook10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderBook10"):
                opp_val = getattr(value, "orderBook10", None)
                if opp_val is None:
                    setattr(value, "orderBook10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class BookSet:

    def __init__(self, bookIsbn: int, bookTitle: str, search9: "Search" = None):
        self.bookIsbn = bookIsbn
        self.bookTitle = bookTitle
        self.search9 = search9
        
        pass
    @property
    def bookIsbn(self):
        return self.__bookIsbn
    @bookIsbn.setter
    def bookIsbn(self, bookIsbn: int):
        self.__bookIsbn = bookIsbn

    @property
    def bookTitle(self):
        return self.__bookTitle
    @bookTitle.setter
    def bookTitle(self, bookTitle: str):
        self.__bookTitle = bookTitle

    @property
    def search9(self):
        return self.__search9
    @search9.setter
    def search9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookSet__search9", None)
        self.__search9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookSet8"):
                opp_val = getattr(old_value, "bookSet8", None)
                if opp_val == self:
                    setattr(old_value, "bookSet8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookSet8"):
                opp_val = getattr(value, "bookSet8", None)
                setattr(value, "bookSet8", self)



class Search:

    def __init__(self, bookTitle: str, authorName: str, priceLimit: str, searchBook7: "Customer" = None, bookSet8: "BookSet" = None):
        self.bookTitle = bookTitle
        self.authorName = authorName
        self.priceLimit = priceLimit
        self.searchBook7 = searchBook7
        self.bookSet8 = bookSet8
        
        pass
    @property
    def bookTitle(self):
        return self.__bookTitle
    @bookTitle.setter
    def bookTitle(self, bookTitle: str):
        self.__bookTitle = bookTitle

    @property
    def priceLimit(self):
        return self.__priceLimit
    @priceLimit.setter
    def priceLimit(self, priceLimit: str):
        self.__priceLimit = priceLimit

    @property
    def authorName(self):
        return self.__authorName
    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName

    @property
    def searchBook7(self):
        return self.__searchBook7
    @searchBook7.setter
    def searchBook7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Search__searchBook7", None)
        self.__searchBook7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "search6"):
                opp_val = getattr(old_value, "search6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "search6"):
                opp_val = getattr(value, "search6", None)
                if opp_val is None:
                    setattr(value, "search6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bookSet8(self):
        return self.__bookSet8
    @bookSet8.setter
    def bookSet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Search__bookSet8", None)
        self.__bookSet8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "search9"):
                opp_val = getattr(old_value, "search9", None)
                if opp_val == self:
                    setattr(old_value, "search9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "search9"):
                opp_val = getattr(value, "search9", None)
                setattr(value, "search9", self)



class Shopping_Cart:

    def __init__(self, orderId: int, price: str, customerId: Customer, addBookToCart5: set["Customer"] = None, orderBook10: set["Order"] = None):
        self.orderId = orderId
        self.price = price
        self.customerId = customerId
        self.addBookToCart5 = addBookToCart5 if addBookToCart5 is not None else set()
        self.orderBook10 = orderBook10 if orderBook10 is not None else set()
        
        pass
    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: Customer):
        self.__customerId = customerId

    @property
    def orderBook10(self):
        return self.__orderBook10
    @orderBook10.setter
    def orderBook10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__orderBook10", None)
        self.__orderBook10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orderIsUndatedToCart11"):
                    opp_val = getattr(item, "orderIsUndatedToCart11", None)
                    
                    if opp_val == self:
                        setattr(item, "orderIsUndatedToCart11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orderIsUndatedToCart11"):
                    opp_val = getattr(item, "orderIsUndatedToCart11", None)
                    
                    setattr(item, "orderIsUndatedToCart11", self)
                    

    @property
    def addBookToCart5(self):
        return self.__addBookToCart5
    @addBookToCart5.setter
    def addBookToCart5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__addBookToCart5", None)
        self.__addBookToCart5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Shopping_Cart_04"):
                    opp_val = getattr(item, "Customer_Shopping_Cart_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Shopping_Cart_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Shopping_Cart_04"):
                    opp_val = getattr(item, "Customer_Shopping_Cart_04", None)
                    
                    setattr(item, "Customer_Shopping_Cart_04", self)
                    



class Admin:

    def __init__(self, adminId: int, adminPassword: str, adminName: str, adminRmail: str, _addUserAsMember3: "User" = None, orderBook13: "Order" = None):
        self.adminId = adminId
        self.adminPassword = adminPassword
        self.adminName = adminName
        self.adminRmail = adminRmail
        self._addUserAsMember3 = _addUserAsMember3
        self.orderBook13 = orderBook13
        
        pass
    @property
    def adminPassword(self):
        return self.__adminPassword
    @adminPassword.setter
    def adminPassword(self, adminPassword: str):
        self.__adminPassword = adminPassword

    @property
    def adminId(self):
        return self.__adminId
    @adminId.setter
    def adminId(self, adminId: int):
        self.__adminId = adminId

    @property
    def adminRmail(self):
        return self.__adminRmail
    @adminRmail.setter
    def adminRmail(self, adminRmail: str):
        self.__adminRmail = adminRmail

    @property
    def adminName(self):
        return self.__adminName
    @adminName.setter
    def adminName(self, adminName: str):
        self.__adminName = adminName

    @property
    def orderBook13(self):
        return self.__orderBook13
    @orderBook13.setter
    def orderBook13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__orderBook13", None)
        self.__orderBook13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addBook12"):
                opp_val = getattr(old_value, "addBook12", None)
                if opp_val == self:
                    setattr(old_value, "addBook12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addBook12"):
                opp_val = getattr(value, "addBook12", None)
                setattr(value, "addBook12", self)

    @property
    def _addUserAsMember3(self):
        return self.___addUserAsMember3
    @_addUserAsMember3.setter
    def _addUserAsMember3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin___addUserAsMember3", None)
        self.___addUserAsMember3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin2"):
                opp_val = getattr(old_value, "admin2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin2"):
                opp_val = getattr(value, "admin2", None)
                if opp_val is None:
                    setattr(value, "admin2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

