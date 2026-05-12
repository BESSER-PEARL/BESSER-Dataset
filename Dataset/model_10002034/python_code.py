from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ShoppingCart:

    def __init__(self, price: str, orderID: int, customerID: int, booksOrder18: set["BooksOrder"] = None, customer21: set["Customer"] = None):
        self.price = price
        self.orderID = orderID
        self.customerID = customerID
        self.booksOrder18 = booksOrder18 if booksOrder18 is not None else set()
        self.customer21 = customer21 if customer21 is not None else set()
        
        pass
    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID

    @property
    def orderID(self):
        return self.__orderID
    @orderID.setter
    def orderID(self, orderID: int):
        self.__orderID = orderID

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def booksOrder18(self):
        return self.__booksOrder18
    @booksOrder18.setter
    def booksOrder18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__booksOrder18", None)
        self.__booksOrder18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shoppingCart19"):
                    opp_val = getattr(item, "shoppingCart19", None)
                    
                    if opp_val == self:
                        setattr(item, "shoppingCart19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shoppingCart19"):
                    opp_val = getattr(item, "shoppingCart19", None)
                    
                    setattr(item, "shoppingCart19", self)
                    

    @property
    def customer21(self):
        return self.__customer21
    @customer21.setter
    def customer21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer21", None)
        self.__customer21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shoppingCart20"):
                    opp_val = getattr(item, "shoppingCart20", None)
                    
                    if opp_val == self:
                        setattr(item, "shoppingCart20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shoppingCart20"):
                    opp_val = getattr(item, "shoppingCart20", None)
                    
                    setattr(item, "shoppingCart20", self)
                    



class Category:

    def __init__(self, categoryID: int, categoryName: str, sessionManager15: "SessionManager" = None, book16: "Book" = None):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.sessionManager15 = sessionManager15
        self.book16 = book16
        
        pass
    @property
    def categoryID(self):
        return self.__categoryID
    @categoryID.setter
    def categoryID(self, categoryID: int):
        self.__categoryID = categoryID

    @property
    def categoryName(self):
        return self.__categoryName
    @categoryName.setter
    def categoryName(self, categoryName: str):
        self.__categoryName = categoryName

    @property
    def sessionManager15(self):
        return self.__sessionManager15
    @sessionManager15.setter
    def sessionManager15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__sessionManager15", None)
        self.__sessionManager15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category14"):
                opp_val = getattr(old_value, "category14", None)
                if opp_val == self:
                    setattr(old_value, "category14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category14"):
                opp_val = getattr(value, "category14", None)
                setattr(value, "category14", self)

    @property
    def book16(self):
        return self.__book16
    @book16.setter
    def book16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__book16", None)
        self.__book16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category17"):
                opp_val = getattr(old_value, "category17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category17"):
                opp_val = getattr(value, "category17", None)
                if opp_val is None:
                    setattr(value, "category17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class AdvSearch:

    def __init__(self, bookTitle: str, categoryID: str, bookAuthor: str, bookLowCost: str, bookHighCost: str, bookSet13: set["BookSet"] = None):
        self.bookTitle = bookTitle
        self.categoryID = categoryID
        self.bookAuthor = bookAuthor
        self.bookLowCost = bookLowCost
        self.bookHighCost = bookHighCost
        self.bookSet13 = bookSet13 if bookSet13 is not None else set()
        
        pass
    @property
    def bookTitle(self):
        return self.__bookTitle
    @bookTitle.setter
    def bookTitle(self, bookTitle: str):
        self.__bookTitle = bookTitle

    @property
    def categoryID(self):
        return self.__categoryID
    @categoryID.setter
    def categoryID(self, categoryID: str):
        self.__categoryID = categoryID

    @property
    def bookAuthor(self):
        return self.__bookAuthor
    @bookAuthor.setter
    def bookAuthor(self, bookAuthor: str):
        self.__bookAuthor = bookAuthor

    @property
    def bookHighCost(self):
        return self.__bookHighCost
    @bookHighCost.setter
    def bookHighCost(self, bookHighCost: str):
        self.__bookHighCost = bookHighCost

    @property
    def bookLowCost(self):
        return self.__bookLowCost
    @bookLowCost.setter
    def bookLowCost(self, bookLowCost: str):
        self.__bookLowCost = bookLowCost

    @property
    def bookSet13(self):
        return self.__bookSet13
    @bookSet13.setter
    def bookSet13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AdvSearch__bookSet13", None)
        self.__bookSet13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "advSearch12"):
                    opp_val = getattr(item, "advSearch12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "advSearch12"):
                    opp_val = getattr(item, "advSearch12", None)
                    
                    if opp_val is None:
                        setattr(item, "advSearch12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Search:

    def __init__(self, bookTitle: str, categoryID: str, bookSet11: set["BookSet"] = None):
        self.bookTitle = bookTitle
        self.categoryID = categoryID
        self.bookSet11 = bookSet11 if bookSet11 is not None else set()
        
        pass
    @property
    def bookTitle(self):
        return self.__bookTitle
    @bookTitle.setter
    def bookTitle(self, bookTitle: str):
        self.__bookTitle = bookTitle

    @property
    def categoryID(self):
        return self.__categoryID
    @categoryID.setter
    def categoryID(self, categoryID: str):
        self.__categoryID = categoryID

    @property
    def bookSet11(self):
        return self.__bookSet11
    @bookSet11.setter
    def bookSet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Search__bookSet11", None)
        self.__bookSet11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "search10"):
                    opp_val = getattr(item, "search10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "search10"):
                    opp_val = getattr(item, "search10", None)
                    
                    if opp_val is None:
                        setattr(item, "search10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class BookSet:

    def __init__(self, bookID: int, bookName: str, search10: set["Search"] = None, advSearch12: set["AdvSearch"] = None):
        self.bookID = bookID
        self.bookName = bookName
        self.search10 = search10 if search10 is not None else set()
        self.advSearch12 = advSearch12 if advSearch12 is not None else set()
        
        pass
    @property
    def bookID(self):
        return self.__bookID
    @bookID.setter
    def bookID(self, bookID: int):
        self.__bookID = bookID

    @property
    def bookName(self):
        return self.__bookName
    @bookName.setter
    def bookName(self, bookName: str):
        self.__bookName = bookName

    @property
    def search10(self):
        return self.__search10
    @search10.setter
    def search10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookSet__search10", None)
        self.__search10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookSet11"):
                    opp_val = getattr(item, "bookSet11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookSet11"):
                    opp_val = getattr(item, "bookSet11", None)
                    
                    if opp_val is None:
                        setattr(item, "bookSet11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def advSearch12(self):
        return self.__advSearch12
    @advSearch12.setter
    def advSearch12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookSet__advSearch12", None)
        self.__advSearch12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookSet13"):
                    opp_val = getattr(item, "bookSet13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookSet13"):
                    opp_val = getattr(item, "bookSet13", None)
                    
                    if opp_val is None:
                        setattr(item, "bookSet13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Administrator:

    def __init__(self, adminID: int, password: str, name: str, email: str, phoneNo: str, booksOrder9: set["BooksOrder"] = None):
        self.adminID = adminID
        self.password = password
        self.name = name
        self.email = email
        self.phoneNo = phoneNo
        self.booksOrder9 = booksOrder9 if booksOrder9 is not None else set()
        
        pass
    @property
    def adminID(self):
        return self.__adminID
    @adminID.setter
    def adminID(self, adminID: int):
        self.__adminID = adminID

    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: str):
        self.__phoneNo = phoneNo

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

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def booksOrder9(self):
        return self.__booksOrder9
    @booksOrder9.setter
    def booksOrder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__booksOrder9", None)
        self.__booksOrder9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator8"):
                    opp_val = getattr(item, "administrator8", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator8"):
                    opp_val = getattr(item, "administrator8", None)
                    
                    setattr(item, "administrator8", self)
                    



class Book:

    def __init__(self, bookID: int, bookName: str, price: str, rating: int, authorName: str, imageURL: str, notes: str, productURL: str, categoryID: int, booksOrder7: "BooksOrder" = None, category17: set["Category"] = None):
        self.bookID = bookID
        self.bookName = bookName
        self.price = price
        self.rating = rating
        self.authorName = authorName
        self.imageURL = imageURL
        self.notes = notes
        self.productURL = productURL
        self.categoryID = categoryID
        self.booksOrder7 = booksOrder7
        self.category17 = category17 if category17 is not None else set()
        
        pass
    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def authorName(self):
        return self.__authorName
    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName

    @property
    def productURL(self):
        return self.__productURL
    @productURL.setter
    def productURL(self, productURL: str):
        self.__productURL = productURL

    @property
    def bookName(self):
        return self.__bookName
    @bookName.setter
    def bookName(self, bookName: str):
        self.__bookName = bookName

    @property
    def categoryID(self):
        return self.__categoryID
    @categoryID.setter
    def categoryID(self, categoryID: int):
        self.__categoryID = categoryID

    @property
    def imageURL(self):
        return self.__imageURL
    @imageURL.setter
    def imageURL(self, imageURL: str):
        self.__imageURL = imageURL

    @property
    def bookID(self):
        return self.__bookID
    @bookID.setter
    def bookID(self, bookID: int):
        self.__bookID = bookID

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def category17(self):
        return self.__category17
    @category17.setter
    def category17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__category17", None)
        self.__category17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book16"):
                    opp_val = getattr(item, "book16", None)
                    
                    if opp_val == self:
                        setattr(item, "book16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book16"):
                    opp_val = getattr(item, "book16", None)
                    
                    setattr(item, "book16", self)
                    

    @property
    def booksOrder7(self):
        return self.__booksOrder7
    @booksOrder7.setter
    def booksOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__booksOrder7", None)
        self.__booksOrder7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book6"):
                opp_val = getattr(old_value, "book6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book6"):
                opp_val = getattr(value, "book6", None)
                if opp_val is None:
                    setattr(value, "book6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class BooksOrder:

    def __init__(self, orderID: int, price: str, customerID: int, quantity: int, administrator8: "Administrator" = None, shoppingCart19: "ShoppingCart" = None, customer5: set["Customer"] = None, book6: set["Book"] = None):
        self.orderID = orderID
        self.price = price
        self.customerID = customerID
        self.quantity = quantity
        self.administrator8 = administrator8
        self.shoppingCart19 = shoppingCart19
        self.customer5 = customer5 if customer5 is not None else set()
        self.book6 = book6 if book6 is not None else set()
        
        pass
    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def orderID(self):
        return self.__orderID
    @orderID.setter
    def orderID(self, orderID: int):
        self.__orderID = orderID

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def book6(self):
        return self.__book6
    @book6.setter
    def book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BooksOrder__book6", None)
        self.__book6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "booksOrder7"):
                    opp_val = getattr(item, "booksOrder7", None)
                    
                    if opp_val == self:
                        setattr(item, "booksOrder7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "booksOrder7"):
                    opp_val = getattr(item, "booksOrder7", None)
                    
                    setattr(item, "booksOrder7", self)
                    

    @property
    def shoppingCart19(self):
        return self.__shoppingCart19
    @shoppingCart19.setter
    def shoppingCart19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BooksOrder__shoppingCart19", None)
        self.__shoppingCart19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksOrder18"):
                opp_val = getattr(old_value, "booksOrder18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksOrder18"):
                opp_val = getattr(value, "booksOrder18", None)
                if opp_val is None:
                    setattr(value, "booksOrder18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def administrator8(self):
        return self.__administrator8
    @administrator8.setter
    def administrator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BooksOrder__administrator8", None)
        self.__administrator8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksOrder9"):
                opp_val = getattr(old_value, "booksOrder9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksOrder9"):
                opp_val = getattr(value, "booksOrder9", None)
                if opp_val is None:
                    setattr(value, "booksOrder9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BooksOrder__customer5", None)
        self.__customer5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "booksOrder4"):
                    opp_val = getattr(item, "booksOrder4", None)
                    
                    if opp_val == self:
                        setattr(item, "booksOrder4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "booksOrder4"):
                    opp_val = getattr(item, "booksOrder4", None)
                    
                    setattr(item, "booksOrder4", self)
                    



class Customer:

    def __init__(self, email: str, phoneNo: int, CCinfo: str, customerID: str, password: str, name: str, address: str, shoppingCart20: "ShoppingCart" = None, booksOrder4: "BooksOrder" = None):
        self.email = email
        self.phoneNo = phoneNo
        self.CCinfo = CCinfo
        self.customerID = customerID
        self.password = password
        self.name = name
        self.address = address
        self.shoppingCart20 = shoppingCart20
        self.booksOrder4 = booksOrder4
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: str):
        self.__customerID = customerID

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def CCinfo(self):
        return self.__CCinfo
    @CCinfo.setter
    def CCinfo(self, CCinfo: str):
        self.__CCinfo = CCinfo

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phoneNo(self):
        return self.__phoneNo
    @phoneNo.setter
    def phoneNo(self, phoneNo: int):
        self.__phoneNo = phoneNo

    @property
    def shoppingCart20(self):
        return self.__shoppingCart20
    @shoppingCart20.setter
    def shoppingCart20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shoppingCart20", None)
        self.__shoppingCart20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer21"):
                opp_val = getattr(old_value, "customer21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer21"):
                opp_val = getattr(value, "customer21", None)
                if opp_val is None:
                    setattr(value, "customer21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def booksOrder4(self):
        return self.__booksOrder4
    @booksOrder4.setter
    def booksOrder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__booksOrder4", None)
        self.__booksOrder4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                if opp_val is None:
                    setattr(value, "customer5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class SessionManager:

    def __init__(self, userID: int, categoryName: str, category14: "Category" = None, user2: "User" = None):
        self.userID = userID
        self.categoryName = categoryName
        self.category14 = category14
        self.user2 = user2
        
        pass
    @property
    def categoryName(self):
        return self.__categoryName
    @categoryName.setter
    def categoryName(self, categoryName: str):
        self.__categoryName = categoryName

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def user2(self):
        return self.__user2
    @user2.setter
    def user2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SessionManager__user2", None)
        self.__user2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sessionManager3"):
                opp_val = getattr(old_value, "sessionManager3", None)
                if opp_val == self:
                    setattr(old_value, "sessionManager3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sessionManager3"):
                opp_val = getattr(value, "sessionManager3", None)
                setattr(value, "sessionManager3", self)

    @property
    def category14(self):
        return self.__category14
    @category14.setter
    def category14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SessionManager__category14", None)
        self.__category14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sessionManager15"):
                opp_val = getattr(old_value, "sessionManager15", None)
                if opp_val == self:
                    setattr(old_value, "sessionManager15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sessionManager15"):
                opp_val = getattr(value, "sessionManager15", None)
                setattr(value, "sessionManager15", self)



class User:

    def __init__(self, userID: int, password: str, loginStatus: str, user0: "User" = None, user1: "User" = None, sessionManager3: "SessionManager" = None):
        self.userID = userID
        self.password = password
        self.loginStatus = loginStatus
        self.user0 = user0
        self.user1 = user1
        self.sessionManager3 = sessionManager3
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user0"):
                opp_val = getattr(old_value, "user0", None)
                if opp_val == self:
                    setattr(old_value, "user0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user0"):
                opp_val = getattr(value, "user0", None)
                setattr(value, "user0", self)

    @property
    def sessionManager3(self):
        return self.__sessionManager3
    @sessionManager3.setter
    def sessionManager3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__sessionManager3", None)
        self.__sessionManager3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user2"):
                opp_val = getattr(old_value, "user2", None)
                if opp_val == self:
                    setattr(old_value, "user2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user2"):
                opp_val = getattr(value, "user2", None)
                setattr(value, "user2", self)

    @property
    def user0(self):
        return self.__user0
    @user0.setter
    def user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__user0", None)
        self.__user0 = value
        
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

