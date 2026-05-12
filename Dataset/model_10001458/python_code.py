from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Bank_Mobile_Money_Agent_Actor:

    pass


class Confirm_Payment_UseCase:

    pass


class Edit_Book_UseCase:

    pass


class Add_Book_UseCase:

    pass


class Administrator_Actor:

    pass


class Logout_UseCase:

    pass


class Make_Payment_UseCase:

    pass


class Add_book__to_cart_UseCase:

    pass


class Search_Book_UseCase:

    pass


class Log_in_UseCase:

    pass


class Sign_up_UseCase:

    pass


class Customer_Actor:

    pass





class Category:

    def __init__(self, categoryID: int, categoryName: str, category26: "Category" = None, category27: "Category" = None, book28: set["Book"] = None):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.category26 = category26
        self.category27 = category27
        self.book28 = book28 if book28 is not None else set()
        
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
    def category27(self):
        return self.__category27
    @category27.setter
    def category27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__category27", None)
        self.__category27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category26"):
                opp_val = getattr(old_value, "category26", None)
                if opp_val == self:
                    setattr(old_value, "category26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category26"):
                opp_val = getattr(value, "category26", None)
                setattr(value, "category26", self)

    @property
    def category26(self):
        return self.__category26
    @category26.setter
    def category26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__category26", None)
        self.__category26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category27"):
                opp_val = getattr(old_value, "category27", None)
                if opp_val == self:
                    setattr(old_value, "category27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category27"):
                opp_val = getattr(value, "category27", None)
                setattr(value, "category27", self)

    @property
    def book28(self):
        return self.__book28
    @book28.setter
    def book28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__book28", None)
        self.__book28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "category29"):
                    opp_val = getattr(item, "category29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "category29"):
                    opp_val = getattr(item, "category29", None)
                    
                    if opp_val is None:
                        setattr(item, "category29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, CustomerID: int, username: str, email: str, administrator33: "Administrator" = None, book34: "Book" = None, customer36: "Customer" = None, customer37: "Customer" = None, book38: set["Book"] = None):
        self.CustomerID = CustomerID
        self.username = username
        self.email = email
        self.administrator33 = administrator33
        self.book34 = book34
        self.customer36 = customer36
        self.customer37 = customer37
        self.book38 = book38 if book38 is not None else set()
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def administrator33(self):
        return self.__administrator33
    @administrator33.setter
    def administrator33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__administrator33", None)
        self.__administrator33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer32"):
                opp_val = getattr(old_value, "customer32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer32"):
                opp_val = getattr(value, "customer32", None)
                if opp_val is None:
                    setattr(value, "customer32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def book38(self):
        return self.__book38
    @book38.setter
    def book38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__book38", None)
        self.__book38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer39"):
                    opp_val = getattr(item, "customer39", None)
                    
                    if opp_val == self:
                        setattr(item, "customer39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer39"):
                    opp_val = getattr(item, "customer39", None)
                    
                    setattr(item, "customer39", self)
                    

    @property
    def customer37(self):
        return self.__customer37
    @customer37.setter
    def customer37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer37", None)
        self.__customer37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer36"):
                opp_val = getattr(old_value, "customer36", None)
                if opp_val == self:
                    setattr(old_value, "customer36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer36"):
                opp_val = getattr(value, "customer36", None)
                setattr(value, "customer36", self)

    @property
    def customer36(self):
        return self.__customer36
    @customer36.setter
    def customer36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer36", None)
        self.__customer36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer37"):
                opp_val = getattr(old_value, "customer37", None)
                if opp_val == self:
                    setattr(old_value, "customer37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer37"):
                opp_val = getattr(value, "customer37", None)
                setattr(value, "customer37", self)

    @property
    def book34(self):
        return self.__book34
    @book34.setter
    def book34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__book34", None)
        self.__book34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer35"):
                opp_val = getattr(old_value, "customer35", None)
                if opp_val == self:
                    setattr(old_value, "customer35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer35"):
                opp_val = getattr(value, "customer35", None)
                setattr(value, "customer35", self)



class Book:

    def __init__(self, bookID: int, title: str, category: Customer, price: int, description: str, author: str, category29: set["Category"] = None, customer35: "Customer" = None, customer39: "Customer" = None, administrator25: "Administrator" = None, administrator23: "Administrator" = None):
        self.bookID = bookID
        self.title = title
        self.category = category
        self.price = price
        self.description = description
        self.author = author
        self.category29 = category29 if category29 is not None else set()
        self.customer35 = customer35
        self.customer39 = customer39
        self.administrator25 = administrator25
        self.administrator23 = administrator23
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bookID(self):
        return self.__bookID
    @bookID.setter
    def bookID(self, bookID: int):
        self.__bookID = bookID

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: Customer):
        self.__category = category

    @property
    def category29(self):
        return self.__category29
    @category29.setter
    def category29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__category29", None)
        self.__category29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book28"):
                    opp_val = getattr(item, "book28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book28"):
                    opp_val = getattr(item, "book28", None)
                    
                    if opp_val is None:
                        setattr(item, "book28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def customer35(self):
        return self.__customer35
    @customer35.setter
    def customer35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__customer35", None)
        self.__customer35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book34"):
                opp_val = getattr(old_value, "book34", None)
                if opp_val == self:
                    setattr(old_value, "book34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book34"):
                opp_val = getattr(value, "book34", None)
                setattr(value, "book34", self)

    @property
    def administrator23(self):
        return self.__administrator23
    @administrator23.setter
    def administrator23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__administrator23", None)
        self.__administrator23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book22"):
                opp_val = getattr(old_value, "book22", None)
                if opp_val == self:
                    setattr(old_value, "book22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book22"):
                opp_val = getattr(value, "book22", None)
                setattr(value, "book22", self)

    @property
    def administrator25(self):
        return self.__administrator25
    @administrator25.setter
    def administrator25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__administrator25", None)
        self.__administrator25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book24"):
                opp_val = getattr(old_value, "book24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book24"):
                opp_val = getattr(value, "book24", None)
                if opp_val is None:
                    setattr(value, "book24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer39(self):
        return self.__customer39
    @customer39.setter
    def customer39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__customer39", None)
        self.__customer39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book38"):
                opp_val = getattr(old_value, "book38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book38"):
                opp_val = getattr(value, "book38", None)
                if opp_val is None:
                    setattr(value, "book38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Administrator:

    def __init__(self, adminID: int, name: str, email: str, administrator30: "Administrator" = None, administrator31: "Administrator" = None, customer32: set["Customer"] = None, book24: set["Book"] = None, book22: "Book" = None):
        self.adminID = adminID
        self.name = name
        self.email = email
        self.administrator30 = administrator30
        self.administrator31 = administrator31
        self.customer32 = customer32 if customer32 is not None else set()
        self.book24 = book24 if book24 is not None else set()
        self.book22 = book22
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adminID(self):
        return self.__adminID
    @adminID.setter
    def adminID(self, adminID: int):
        self.__adminID = adminID

    @property
    def administrator30(self):
        return self.__administrator30
    @administrator30.setter
    def administrator30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__administrator30", None)
        self.__administrator30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator31"):
                opp_val = getattr(old_value, "administrator31", None)
                if opp_val == self:
                    setattr(old_value, "administrator31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator31"):
                opp_val = getattr(value, "administrator31", None)
                setattr(value, "administrator31", self)

    @property
    def administrator31(self):
        return self.__administrator31
    @administrator31.setter
    def administrator31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__administrator31", None)
        self.__administrator31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator30"):
                opp_val = getattr(old_value, "administrator30", None)
                if opp_val == self:
                    setattr(old_value, "administrator30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator30"):
                opp_val = getattr(value, "administrator30", None)
                setattr(value, "administrator30", self)

    @property
    def book22(self):
        return self.__book22
    @book22.setter
    def book22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__book22", None)
        self.__book22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator23"):
                opp_val = getattr(old_value, "administrator23", None)
                if opp_val == self:
                    setattr(old_value, "administrator23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator23"):
                opp_val = getattr(value, "administrator23", None)
                setattr(value, "administrator23", self)

    @property
    def book24(self):
        return self.__book24
    @book24.setter
    def book24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__book24", None)
        self.__book24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator25"):
                    opp_val = getattr(item, "administrator25", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator25"):
                    opp_val = getattr(item, "administrator25", None)
                    
                    setattr(item, "administrator25", self)
                    

    @property
    def customer32(self):
        return self.__customer32
    @customer32.setter
    def customer32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__customer32", None)
        self.__customer32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator33"):
                    opp_val = getattr(item, "administrator33", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator33"):
                    opp_val = getattr(item, "administrator33", None)
                    
                    setattr(item, "administrator33", self)
                    

