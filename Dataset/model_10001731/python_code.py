from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Book_Delivery__UseCase:

    pass


class Generating_Membership_Card_UseCase:

    pass


class Authentication_UseCase:

    pass


class Registration__UseCase:

    pass


class Add_Member_UseCase:

    pass


class Remove_Member_UseCase:

    pass


class Book_Maintenance__UseCase:

    pass


class Bank_Accounting_Actor:

    pass


class Credit_Card_Authentication_Service_Actor:

    pass


class PayPal_Authentication_Service_Actor:

    pass


class Payment_Authentecation_System_Actor:

    pass


class Payment_UseCase:

    pass


class Bank_Server_Side_Authentication_UseCase:

    pass


class _UseCase:

    pass


class Payment_System_UseCase:

    pass


class Cash_UseCase:

    pass


class Debit_Card_UseCase:

    pass


class Credit_Card_UseCase:

    pass


class PayPal_UseCase:

    pass


class Billing_UseCase:

    pass


class ID_Authentication_Server_UseCase:

    pass


class User_Actor:

    pass


class Add_to_Borrow_basket_UseCase:

    pass


class Suggestion_UseCase:

    pass


class Searching_UseCase:

    pass


class List_view__UseCase:

    pass


class Viewing_Books_UseCase:

    pass


class ID_Authentication_Server_Actor:

    pass


class Guest_Actor:

    pass


class Recieving_Book_UseCase:

    pass


class Enter_Password_UseCase:

    pass


class Enter__Username_UseCase:

    pass


class Capatcha_UseCase:

    pass


class Borrow_Book_UseCase:

    pass


class View_Books_UseCase:

    pass


class Person_Actor:

    pass


class User_Maintenance_UseCase:

    pass


class Delete_Book_UseCase:

    pass


class Add_Book_UseCase:

    pass


class Log_in_UseCase:

    pass


class Librarian_Actor:

    pass





class Billing_UseCase1:

    pass


class Library:

    def __init__(self, LibraryID: int, Address: str, book33: set["Book"] = None, person34: set["Person"] = None):
        self.LibraryID = LibraryID
        self.Address = Address
        self.book33 = book33 if book33 is not None else set()
        self.person34 = person34 if person34 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def LibraryID(self):
        return self.__LibraryID
    @LibraryID.setter
    def LibraryID(self, LibraryID: int):
        self.__LibraryID = LibraryID

    @property
    def person34(self):
        return self.__person34
    @person34.setter
    def person34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library__person34", None)
        self.__person34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library35"):
                    opp_val = getattr(item, "library35", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library35"):
                    opp_val = getattr(item, "library35", None)
                    
                    if opp_val is None:
                        setattr(item, "library35", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def book33(self):
        return self.__book33
    @book33.setter
    def book33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library__book33", None)
        self.__book33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library32"):
                    opp_val = getattr(item, "library32", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library32"):
                    opp_val = getattr(item, "library32", None)
                    
                    if opp_val is None:
                        setattr(item, "library32", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class BookBorrow:

    def __init__(self, BorrowID: int, InDate: str, OutDate: str, BookID: int, UserCode: Enter__Username_UseCase, book29: set["Book"] = None, user30: set["User"] = None):
        self.BorrowID = BorrowID
        self.InDate = InDate
        self.OutDate = OutDate
        self.BookID = BookID
        self.UserCode = UserCode
        self.book29 = book29 if book29 is not None else set()
        self.user30 = user30 if user30 is not None else set()
        
        pass
    @property
    def BookID(self):
        return self.__BookID
    @BookID.setter
    def BookID(self, BookID: int):
        self.__BookID = BookID

    @property
    def OutDate(self):
        return self.__OutDate
    @OutDate.setter
    def OutDate(self, OutDate: str):
        self.__OutDate = OutDate

    @property
    def UserCode(self):
        return self.__UserCode
    @UserCode.setter
    def UserCode(self, UserCode: Enter__Username_UseCase):
        self.__UserCode = UserCode

    @property
    def BorrowID(self):
        return self.__BorrowID
    @BorrowID.setter
    def BorrowID(self, BorrowID: int):
        self.__BorrowID = BorrowID

    @property
    def InDate(self):
        return self.__InDate
    @InDate.setter
    def InDate(self, InDate: str):
        self.__InDate = InDate

    @property
    def book29(self):
        return self.__book29
    @book29.setter
    def book29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookBorrow__book29", None)
        self.__book29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookBorrow28"):
                    opp_val = getattr(item, "bookBorrow28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookBorrow28"):
                    opp_val = getattr(item, "bookBorrow28", None)
                    
                    if opp_val is None:
                        setattr(item, "bookBorrow28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def user30(self):
        return self.__user30
    @user30.setter
    def user30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookBorrow__user30", None)
        self.__user30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookBorrow31"):
                    opp_val = getattr(item, "bookBorrow31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookBorrow31"):
                    opp_val = getattr(item, "bookBorrow31", None)
                    
                    if opp_val is None:
                        setattr(item, "bookBorrow31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class User:

    def __init__(self, UserCode: int, attribute: str, Active: bool, RegistrationDate: str, Mail: str, Address: str, Phone: int, bookBorrow31: set["BookBorrow"] = None):
        self.UserCode = UserCode
        self.attribute = attribute
        self.Active = Active
        self.RegistrationDate = RegistrationDate
        self.Mail = Mail
        self.Address = Address
        self.Phone = Phone
        self.bookBorrow31 = bookBorrow31 if bookBorrow31 is not None else set()
        
        pass
    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Active(self):
        return self.__Active
    @Active.setter
    def Active(self, Active: bool):
        self.__Active = Active

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Mail(self):
        return self.__Mail
    @Mail.setter
    def Mail(self, Mail: str):
        self.__Mail = Mail

    @property
    def UserCode(self):
        return self.__UserCode
    @UserCode.setter
    def UserCode(self, UserCode: int):
        self.__UserCode = UserCode

    @property
    def RegistrationDate(self):
        return self.__RegistrationDate
    @RegistrationDate.setter
    def RegistrationDate(self, RegistrationDate: str):
        self.__RegistrationDate = RegistrationDate

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def bookBorrow31(self):
        return self.__bookBorrow31
    @bookBorrow31.setter
    def bookBorrow31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__bookBorrow31", None)
        self.__bookBorrow31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user30"):
                    opp_val = getattr(item, "user30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user30"):
                    opp_val = getattr(item, "user30", None)
                    
                    if opp_val is None:
                        setattr(item, "user30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Librarian:

    def __init__(self, LibID: int, Department: str):
        self.LibID = LibID
        self.Department = Department
        
        pass
    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def LibID(self):
        return self.__LibID
    @LibID.setter
    def LibID(self, LibID: int):
        self.__LibID = LibID



class Guest:

    def __init__(self, GuestID: int):
        self.GuestID = GuestID
        
        pass
    @property
    def GuestID(self):
        return self.__GuestID
    @GuestID.setter
    def GuestID(self, GuestID: int):
        self.__GuestID = GuestID



class Person:

    def __init__(self, PersonID: int, PersonName: str, BirthDay: str, LibraryID: int, library35: set["Library"] = None):
        self.PersonID = PersonID
        self.PersonName = PersonName
        self.BirthDay = BirthDay
        self.LibraryID = LibraryID
        self.library35 = library35 if library35 is not None else set()
        
        pass
    @property
    def PersonName(self):
        return self.__PersonName
    @PersonName.setter
    def PersonName(self, PersonName: str):
        self.__PersonName = PersonName

    @property
    def LibraryID(self):
        return self.__LibraryID
    @LibraryID.setter
    def LibraryID(self, LibraryID: int):
        self.__LibraryID = LibraryID

    @property
    def PersonID(self):
        return self.__PersonID
    @PersonID.setter
    def PersonID(self, PersonID: int):
        self.__PersonID = PersonID

    @property
    def BirthDay(self):
        return self.__BirthDay
    @BirthDay.setter
    def BirthDay(self, BirthDay: str):
        self.__BirthDay = BirthDay

    @property
    def library35(self):
        return self.__library35
    @library35.setter
    def library35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__library35", None)
        self.__library35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person34"):
                    opp_val = getattr(item, "person34", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person34"):
                    opp_val = getattr(item, "person34", None)
                    
                    if opp_val is None:
                        setattr(item, "person34", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Book:

    def __init__(self, BookID: int, BookName: str, PubName: str, Price: int, LibraryID: int, bookBorrow28: set["BookBorrow"] = None, library32: set["Library"] = None):
        self.BookID = BookID
        self.BookName = BookName
        self.PubName = PubName
        self.Price = Price
        self.LibraryID = LibraryID
        self.bookBorrow28 = bookBorrow28 if bookBorrow28 is not None else set()
        self.library32 = library32 if library32 is not None else set()
        
        pass
    @property
    def BookName(self):
        return self.__BookName
    @BookName.setter
    def BookName(self, BookName: str):
        self.__BookName = BookName

    @property
    def BookID(self):
        return self.__BookID
    @BookID.setter
    def BookID(self, BookID: int):
        self.__BookID = BookID

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def PubName(self):
        return self.__PubName
    @PubName.setter
    def PubName(self, PubName: str):
        self.__PubName = PubName

    @property
    def LibraryID(self):
        return self.__LibraryID
    @LibraryID.setter
    def LibraryID(self, LibraryID: int):
        self.__LibraryID = LibraryID

    @property
    def bookBorrow28(self):
        return self.__bookBorrow28
    @bookBorrow28.setter
    def bookBorrow28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__bookBorrow28", None)
        self.__bookBorrow28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book29"):
                    opp_val = getattr(item, "book29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book29"):
                    opp_val = getattr(item, "book29", None)
                    
                    if opp_val is None:
                        setattr(item, "book29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def library32(self):
        return self.__library32
    @library32.setter
    def library32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__library32", None)
        self.__library32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "book33"):
                    opp_val = getattr(item, "book33", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "book33"):
                    opp_val = getattr(item, "book33", None)
                    
                    if opp_val is None:
                        setattr(item, "book33", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Credit_Card_UseCase1:

    pass


class PayPal_UseCase1:

    pass
