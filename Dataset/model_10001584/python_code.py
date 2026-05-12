from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class lecturer:

    def __init__(self, module: str, staff19: "Staff" = None):
        self.module = module
        self.staff19 = staff19
        
        pass
    @property
    def module(self):
        return self.__module
    @module.setter
    def module(self, module: str):
        self.__module = module

    @property
    def staff19(self):
        return self.__staff19
    @staff19.setter
    def staff19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lecturer__staff19", None)
        self.__staff19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "professor18"):
                opp_val = getattr(old_value, "professor18", None)
                if opp_val == self:
                    setattr(old_value, "professor18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "professor18"):
                opp_val = getattr(value, "professor18", None)
                setattr(value, "professor18", self)



class admin:

    def __init__(self, Experience: str, staff16: "Staff" = None):
        self.Experience = Experience
        self.staff16 = staff16
        
        pass
    @property
    def Experience(self):
        return self.__Experience
    @Experience.setter
    def Experience(self, Experience: str):
        self.__Experience = Experience

    @property
    def staff16(self):
        return self.__staff16
    @staff16.setter
    def staff16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__staff16", None)
        self.__staff16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registar17"):
                opp_val = getattr(old_value, "registar17", None)
                if opp_val == self:
                    setattr(old_value, "registar17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registar17"):
                opp_val = getattr(value, "registar17", None)
                setattr(value, "registar17", self)



class Staff:

    def __init__(self, Staff_ID: int, fname: str, lname: str, position: str, address: str, gender: str, email: str, contact: int, username: str, password: str, registar17: "admin" = None, professor18: "lecturer" = None):
        self.Staff_ID = Staff_ID
        self.fname = fname
        self.lname = lname
        self.position = position
        self.address = address
        self.gender = gender
        self.email = email
        self.contact = contact
        self.username = username
        self.password = password
        self.registar17 = registar17
        self.professor18 = professor18
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: int):
        self.__contact = contact

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

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
    def Staff_ID(self):
        return self.__Staff_ID
    @Staff_ID.setter
    def Staff_ID(self, Staff_ID: int):
        self.__Staff_ID = Staff_ID

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def registar17(self):
        return self.__registar17
    @registar17.setter
    def registar17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__registar17", None)
        self.__registar17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff16"):
                opp_val = getattr(old_value, "staff16", None)
                if opp_val == self:
                    setattr(old_value, "staff16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff16"):
                opp_val = getattr(value, "staff16", None)
                setattr(value, "staff16", self)

    @property
    def professor18(self):
        return self.__professor18
    @professor18.setter
    def professor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__professor18", None)
        self.__professor18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff19"):
                opp_val = getattr(old_value, "staff19", None)
                if opp_val == self:
                    setattr(old_value, "staff19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff19"):
                opp_val = getattr(value, "staff19", None)
                setattr(value, "staff19", self)



class Reserved:

    def __init__(self, reserved_date: str, books5: set["Books"] = None, member6: set["Member"] = None):
        self.reserved_date = reserved_date
        self.books5 = books5 if books5 is not None else set()
        self.member6 = member6 if member6 is not None else set()
        
        pass
    @property
    def reserved_date(self):
        return self.__reserved_date
    @reserved_date.setter
    def reserved_date(self, reserved_date: str):
        self.__reserved_date = reserved_date

    @property
    def member6(self):
        return self.__member6
    @member6.setter
    def member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reserved__member6", None)
        self.__member6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reserved7"):
                    opp_val = getattr(item, "reserved7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reserved7"):
                    opp_val = getattr(item, "reserved7", None)
                    
                    if opp_val is None:
                        setattr(item, "reserved7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def books5(self):
        return self.__books5
    @books5.setter
    def books5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reserved__books5", None)
        self.__books5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reserved4"):
                    opp_val = getattr(item, "reserved4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reserved4"):
                    opp_val = getattr(item, "reserved4", None)
                    
                    if opp_val is None:
                        setattr(item, "reserved4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Borrowed:

    def __init__(self, borrowed_date: str, returned_date: str, books1: set["Books"] = None, member2: set["Member"] = None):
        self.borrowed_date = borrowed_date
        self.returned_date = returned_date
        self.books1 = books1 if books1 is not None else set()
        self.member2 = member2 if member2 is not None else set()
        
        pass
    @property
    def borrowed_date(self):
        return self.__borrowed_date
    @borrowed_date.setter
    def borrowed_date(self, borrowed_date: str):
        self.__borrowed_date = borrowed_date

    @property
    def returned_date(self):
        return self.__returned_date
    @returned_date.setter
    def returned_date(self, returned_date: str):
        self.__returned_date = returned_date

    @property
    def books1(self):
        return self.__books1
    @books1.setter
    def books1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Borrowed__books1", None)
        self.__books1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "borrowed0"):
                    opp_val = getattr(item, "borrowed0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "borrowed0"):
                    opp_val = getattr(item, "borrowed0", None)
                    
                    if opp_val is None:
                        setattr(item, "borrowed0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def member2(self):
        return self.__member2
    @member2.setter
    def member2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Borrowed__member2", None)
        self.__member2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "borrowed3"):
                    opp_val = getattr(item, "borrowed3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "borrowed3"):
                    opp_val = getattr(item, "borrowed3", None)
                    
                    if opp_val is None:
                        setattr(item, "borrowed3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Fine:

    def __init__(self, book_id: int, member_id: int, fine_amount: int, borrowed_date: str, returned_date: str, librarian11: set["Librarian"] = None, member12: "Member" = None):
        self.book_id = book_id
        self.member_id = member_id
        self.fine_amount = fine_amount
        self.borrowed_date = borrowed_date
        self.returned_date = returned_date
        self.librarian11 = librarian11 if librarian11 is not None else set()
        self.member12 = member12
        
        pass
    @property
    def member_id(self):
        return self.__member_id
    @member_id.setter
    def member_id(self, member_id: int):
        self.__member_id = member_id

    @property
    def fine_amount(self):
        return self.__fine_amount
    @fine_amount.setter
    def fine_amount(self, fine_amount: int):
        self.__fine_amount = fine_amount

    @property
    def returned_date(self):
        return self.__returned_date
    @returned_date.setter
    def returned_date(self, returned_date: str):
        self.__returned_date = returned_date

    @property
    def book_id(self):
        return self.__book_id
    @book_id.setter
    def book_id(self, book_id: int):
        self.__book_id = book_id

    @property
    def borrowed_date(self):
        return self.__borrowed_date
    @borrowed_date.setter
    def borrowed_date(self, borrowed_date: str):
        self.__borrowed_date = borrowed_date

    @property
    def librarian11(self):
        return self.__librarian11
    @librarian11.setter
    def librarian11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fine__librarian11", None)
        self.__librarian11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fine10"):
                    opp_val = getattr(item, "fine10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fine10"):
                    opp_val = getattr(item, "fine10", None)
                    
                    if opp_val is None:
                        setattr(item, "fine10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def member12(self):
        return self.__member12
    @member12.setter
    def member12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fine__member12", None)
        self.__member12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fine13"):
                opp_val = getattr(old_value, "fine13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fine13"):
                opp_val = getattr(value, "fine13", None)
                if opp_val is None:
                    setattr(value, "fine13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Librarian:

    def __init__(self, member_id: int, member_pwd: str, fname: str, lname: str, gender: str, dob: str, address: str, cont_no: int, books8: set["Books"] = None, fine10: set["Fine"] = None, member15: set["Member"] = None):
        self.member_id = member_id
        self.member_pwd = member_pwd
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.dob = dob
        self.address = address
        self.cont_no = cont_no
        self.books8 = books8 if books8 is not None else set()
        self.fine10 = fine10 if fine10 is not None else set()
        self.member15 = member15 if member15 is not None else set()
        
        pass
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def member_id(self):
        return self.__member_id
    @member_id.setter
    def member_id(self, member_id: int):
        self.__member_id = member_id

    @property
    def member_pwd(self):
        return self.__member_pwd
    @member_pwd.setter
    def member_pwd(self, member_pwd: str):
        self.__member_pwd = member_pwd

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def cont_no(self):
        return self.__cont_no
    @cont_no.setter
    def cont_no(self, cont_no: int):
        self.__cont_no = cont_no

    @property
    def member15(self):
        return self.__member15
    @member15.setter
    def member15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__member15", None)
        self.__member15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian14"):
                    opp_val = getattr(item, "librarian14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian14"):
                    opp_val = getattr(item, "librarian14", None)
                    
                    if opp_val is None:
                        setattr(item, "librarian14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def books8(self):
        return self.__books8
    @books8.setter
    def books8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__books8", None)
        self.__books8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian9"):
                    opp_val = getattr(item, "librarian9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian9"):
                    opp_val = getattr(item, "librarian9", None)
                    
                    if opp_val is None:
                        setattr(item, "librarian9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def fine10(self):
        return self.__fine10
    @fine10.setter
    def fine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__fine10", None)
        self.__fine10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian11"):
                    opp_val = getattr(item, "librarian11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian11"):
                    opp_val = getattr(item, "librarian11", None)
                    
                    if opp_val is None:
                        setattr(item, "librarian11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Member:

    def __init__(self, member_id: int, member_pwd: str, fname: str, lname: str, gender: str, dob: str, address: str, cont_no: int, reserved7: set["Reserved"] = None, fine13: set["Fine"] = None, librarian14: set["Librarian"] = None, borrowed3: set["Borrowed"] = None):
        self.member_id = member_id
        self.member_pwd = member_pwd
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.dob = dob
        self.address = address
        self.cont_no = cont_no
        self.reserved7 = reserved7 if reserved7 is not None else set()
        self.fine13 = fine13 if fine13 is not None else set()
        self.librarian14 = librarian14 if librarian14 is not None else set()
        self.borrowed3 = borrowed3 if borrowed3 is not None else set()
        
        pass
    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def cont_no(self):
        return self.__cont_no
    @cont_no.setter
    def cont_no(self, cont_no: int):
        self.__cont_no = cont_no

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def member_id(self):
        return self.__member_id
    @member_id.setter
    def member_id(self, member_id: int):
        self.__member_id = member_id

    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def member_pwd(self):
        return self.__member_pwd
    @member_pwd.setter
    def member_pwd(self, member_pwd: str):
        self.__member_pwd = member_pwd

    @property
    def fine13(self):
        return self.__fine13
    @fine13.setter
    def fine13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Member__fine13", None)
        self.__fine13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "member12"):
                    opp_val = getattr(item, "member12", None)
                    
                    if opp_val == self:
                        setattr(item, "member12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "member12"):
                    opp_val = getattr(item, "member12", None)
                    
                    setattr(item, "member12", self)
                    

    @property
    def librarian14(self):
        return self.__librarian14
    @librarian14.setter
    def librarian14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Member__librarian14", None)
        self.__librarian14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "member15"):
                    opp_val = getattr(item, "member15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "member15"):
                    opp_val = getattr(item, "member15", None)
                    
                    if opp_val is None:
                        setattr(item, "member15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def reserved7(self):
        return self.__reserved7
    @reserved7.setter
    def reserved7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Member__reserved7", None)
        self.__reserved7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "member6"):
                    opp_val = getattr(item, "member6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "member6"):
                    opp_val = getattr(item, "member6", None)
                    
                    if opp_val is None:
                        setattr(item, "member6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def borrowed3(self):
        return self.__borrowed3
    @borrowed3.setter
    def borrowed3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Member__borrowed3", None)
        self.__borrowed3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "member2"):
                    opp_val = getattr(item, "member2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "member2"):
                    opp_val = getattr(item, "member2", None)
                    
                    if opp_val is None:
                        setattr(item, "member2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Books:

    def __init__(self, book_id: int, title: str, author_name: str, ISBN_no: str, publisher: str, book_qty: int, reserved4: set["Reserved"] = None, librarian9: set["Librarian"] = None, borrowed0: set["Borrowed"] = None):
        self.book_id = book_id
        self.title = title
        self.author_name = author_name
        self.ISBN_no = ISBN_no
        self.publisher = publisher
        self.book_qty = book_qty
        self.reserved4 = reserved4 if reserved4 is not None else set()
        self.librarian9 = librarian9 if librarian9 is not None else set()
        self.borrowed0 = borrowed0 if borrowed0 is not None else set()
        
        pass
    @property
    def ISBN_no(self):
        return self.__ISBN_no
    @ISBN_no.setter
    def ISBN_no(self, ISBN_no: str):
        self.__ISBN_no = ISBN_no

    @property
    def book_id(self):
        return self.__book_id
    @book_id.setter
    def book_id(self, book_id: int):
        self.__book_id = book_id

    @property
    def author_name(self):
        return self.__author_name
    @author_name.setter
    def author_name(self, author_name: str):
        self.__author_name = author_name

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def book_qty(self):
        return self.__book_qty
    @book_qty.setter
    def book_qty(self, book_qty: int):
        self.__book_qty = book_qty

    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def borrowed0(self):
        return self.__borrowed0
    @borrowed0.setter
    def borrowed0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books__borrowed0", None)
        self.__borrowed0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "books1"):
                    opp_val = getattr(item, "books1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "books1"):
                    opp_val = getattr(item, "books1", None)
                    
                    if opp_val is None:
                        setattr(item, "books1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def reserved4(self):
        return self.__reserved4
    @reserved4.setter
    def reserved4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books__reserved4", None)
        self.__reserved4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "books5"):
                    opp_val = getattr(item, "books5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "books5"):
                    opp_val = getattr(item, "books5", None)
                    
                    if opp_val is None:
                        setattr(item, "books5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def librarian9(self):
        return self.__librarian9
    @librarian9.setter
    def librarian9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books__librarian9", None)
        self.__librarian9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "books8"):
                    opp_val = getattr(item, "books8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "books8"):
                    opp_val = getattr(item, "books8", None)
                    
                    if opp_val is None:
                        setattr(item, "books8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

