from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class remove_title_UseCase:

    pass


class buy_book_from_publisher_UseCase:

    pass


class check_account__UseCase:

    pass


class update_details_UseCase:

    pass


class add_book_UseCase:

    pass


class maintenance_database_UseCase:

    pass


class DBA_Actor:

    pass


class display_details_UseCase:

    pass


class publish_book_UseCase:

    pass


class buy_book_from_author_UseCase:

    pass


class publisher_Actor:

    pass


class remove_reservation_UseCase:

    pass


class issue_book_UseCase:

    pass


class make_reservation_UseCase:

    pass


class search_for_book_UseCase:

    pass


class librarian_Actor:

    pass





class publisher:

    def __init__(self, id: int, name: str, address: str, email: str, website: str, dBA22: "DBA" = None, book25: "book" = None):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.website = website
        self.dBA22 = dBA22
        self.book25 = book25
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website(self):
        return self.__website
    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def dBA22(self):
        return self.__dBA22
    @dBA22.setter
    def dBA22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publisher__dBA22", None)
        self.__dBA22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publisher23"):
                opp_val = getattr(old_value, "publisher23", None)
                if opp_val == self:
                    setattr(old_value, "publisher23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publisher23"):
                opp_val = getattr(value, "publisher23", None)
                setattr(value, "publisher23", self)

    @property
    def book25(self):
        return self.__book25
    @book25.setter
    def book25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publisher__book25", None)
        self.__book25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publisher224"):
                opp_val = getattr(old_value, "publisher224", None)
                if opp_val == self:
                    setattr(old_value, "publisher224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publisher224"):
                opp_val = getattr(value, "publisher224", None)
                setattr(value, "publisher224", self)



class book:

    def __init__(self, ISBN: int, title: str, pages: int, author: str, publisher: str, type: str, publisher224: "publisher" = None, loan_book27: "loan_book" = None):
        self.ISBN = ISBN
        self.title = title
        self.pages = pages
        self.author = author
        self.publisher = publisher
        self.type = type
        self.publisher224 = publisher224
        self.loan_book27 = loan_book27
        
        pass
    @property
    def ISBN(self):
        return self.__ISBN
    @ISBN.setter
    def ISBN(self, ISBN: int):
        self.__ISBN = ISBN

    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def loan_book27(self):
        return self.__loan_book27
    @loan_book27.setter
    def loan_book27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book__loan_book27", None)
        self.__loan_book27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book26"):
                opp_val = getattr(old_value, "book26", None)
                if opp_val == self:
                    setattr(old_value, "book26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book26"):
                opp_val = getattr(value, "book26", None)
                setattr(value, "book26", self)

    @property
    def publisher224(self):
        return self.__publisher224
    @publisher224.setter
    def publisher224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book__publisher224", None)
        self.__publisher224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book25"):
                opp_val = getattr(old_value, "book25", None)
                if opp_val == self:
                    setattr(old_value, "book25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book25"):
                opp_val = getattr(value, "book25", None)
                setattr(value, "book25", self)



class DBA:

    def __init__(self, ID: int, name: str, email: str, librarian21: "librarian" = None, publisher23: "publisher" = None):
        self.ID = ID
        self.name = name
        self.email = email
        self.librarian21 = librarian21
        self.publisher23 = publisher23
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

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
    def publisher23(self):
        return self.__publisher23
    @publisher23.setter
    def publisher23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBA__publisher23", None)
        self.__publisher23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dBA22"):
                opp_val = getattr(old_value, "dBA22", None)
                if opp_val == self:
                    setattr(old_value, "dBA22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dBA22"):
                opp_val = getattr(value, "dBA22", None)
                setattr(value, "dBA22", self)

    @property
    def librarian21(self):
        return self.__librarian21
    @librarian21.setter
    def librarian21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBA__librarian21", None)
        self.__librarian21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dBA20"):
                opp_val = getattr(old_value, "dBA20", None)
                if opp_val == self:
                    setattr(old_value, "dBA20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dBA20"):
                opp_val = getattr(value, "dBA20", None)
                setattr(value, "dBA20", self)



class loan_book:

    def __init__(self, id: int, loan_date: date, due_date: date, returned_date: date, cost: int, user17: "user" = None, book26: "book" = None):
        self.id = id
        self.loan_date = loan_date
        self.due_date = due_date
        self.returned_date = returned_date
        self.cost = cost
        self.user17 = user17
        self.book26 = book26
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def returned_date(self):
        return self.__returned_date
    @returned_date.setter
    def returned_date(self, returned_date: date):
        self.__returned_date = returned_date

    @property
    def loan_date(self):
        return self.__loan_date
    @loan_date.setter
    def loan_date(self, loan_date: date):
        self.__loan_date = loan_date

    @property
    def due_date(self):
        return self.__due_date
    @due_date.setter
    def due_date(self, due_date: date):
        self.__due_date = due_date

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: int):
        self.__cost = cost

    @property
    def book26(self):
        return self.__book26
    @book26.setter
    def book26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_book__book26", None)
        self.__book26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loan_book27"):
                opp_val = getattr(old_value, "loan_book27", None)
                if opp_val == self:
                    setattr(old_value, "loan_book27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loan_book27"):
                opp_val = getattr(value, "loan_book27", None)
                setattr(value, "loan_book27", self)

    @property
    def user17(self):
        return self.__user17
    @user17.setter
    def user17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan_book__user17", None)
        self.__user17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loan_book216"):
                opp_val = getattr(old_value, "loan_book216", None)
                if opp_val == self:
                    setattr(old_value, "loan_book216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loan_book216"):
                opp_val = getattr(value, "loan_book216", None)
                setattr(value, "loan_book216", self)



class date:

    pass


class librarian:

    def __init__(self, job: str, id: int, name: str, birth_date: date, address: str, email: str, hire_date: date, user19: "user" = None, dBA20: "DBA" = None):
        self.job = job
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.email = email
        self.hire_date = hire_date
        self.user19 = user19
        self.dBA20 = dBA20
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def job(self):
        return self.__job
    @job.setter
    def job(self, job: str):
        self.__job = job

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def birth_date(self):
        return self.__birth_date
    @birth_date.setter
    def birth_date(self, birth_date: date):
        self.__birth_date = birth_date

    @property
    def hire_date(self):
        return self.__hire_date
    @hire_date.setter
    def hire_date(self, hire_date: date):
        self.__hire_date = hire_date

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
    def dBA20(self):
        return self.__dBA20
    @dBA20.setter
    def dBA20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_librarian__dBA20", None)
        self.__dBA20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "librarian21"):
                opp_val = getattr(old_value, "librarian21", None)
                if opp_val == self:
                    setattr(old_value, "librarian21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "librarian21"):
                opp_val = getattr(value, "librarian21", None)
                setattr(value, "librarian21", self)

    @property
    def user19(self):
        return self.__user19
    @user19.setter
    def user19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_librarian__user19", None)
        self.__user19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "librarian18"):
                opp_val = getattr(old_value, "librarian18", None)
                if opp_val == self:
                    setattr(old_value, "librarian18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "librarian18"):
                opp_val = getattr(value, "librarian18", None)
                setattr(value, "librarian18", self)



class student:

    def __init__(self, student_card: int):
        self.student_card = student_card
        
        pass
    @property
    def student_card(self):
        return self.__student_card
    @student_card.setter
    def student_card(self, student_card: int):
        self.__student_card = student_card



class ordinary_user:

    pass


class user:

    def __init__(self, id: int, first_name: str, last_name: str, phone_number: int, address: str, card: int, email: str, loan_book216: "loan_book" = None, librarian18: "librarian" = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.card = card
        self.email = email
        self.loan_book216 = loan_book216
        self.librarian18 = librarian18
        
        pass
    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: int):
        self.__card = card

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, phone_number: int):
        self.__phone_number = phone_number

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
    def address(self, address: str):
        self.__address = address

    @property
    def loan_book216(self):
        return self.__loan_book216
    @loan_book216.setter
    def loan_book216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__loan_book216", None)
        self.__loan_book216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user17"):
                opp_val = getattr(old_value, "user17", None)
                if opp_val == self:
                    setattr(old_value, "user17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user17"):
                opp_val = getattr(value, "user17", None)
                setattr(value, "user17", self)

    @property
    def librarian18(self):
        return self.__librarian18
    @librarian18.setter
    def librarian18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__librarian18", None)
        self.__librarian18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user19"):
                opp_val = getattr(old_value, "user19", None)
                if opp_val == self:
                    setattr(old_value, "user19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user19"):
                opp_val = getattr(value, "user19", None)
                setattr(value, "user19", self)



class system_Component:

    pass
