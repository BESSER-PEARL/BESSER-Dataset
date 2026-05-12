from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class student_record:

    def __init__(self, name: str, address: str, phone_number: str, fines: str, customer7: "student" = None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.fines = fines
        self.customer7 = customer7
        
        pass
    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fines(self):
        return self.__fines
    @fines.setter
    def fines(self, fines: str):
        self.__fines = fines

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student_record__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student_record6"):
                opp_val = getattr(old_value, "student_record6", None)
                if opp_val == self:
                    setattr(old_value, "student_record6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student_record6"):
                opp_val = getattr(value, "student_record6", None)
                setattr(value, "student_record6", self)



class vendor:

    def __init__(self, book_details: str, attribute: str):
        self.book_details = book_details
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def book_details(self):
        return self.__book_details
    @book_details.setter
    def book_details(self, book_details: str):
        self.__book_details = book_details



class student:

    def __init__(self, details: str, books_database5: "books_database" = None, student_record6: "student_record" = None):
        self.details = details
        self.books_database5 = books_database5
        self.student_record6 = student_record6
        
        pass
    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def books_database5(self):
        return self.__books_database5
    @books_database5.setter
    def books_database5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__books_database5", None)
        self.__books_database5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if opp_val == self:
                    setattr(old_value, "customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                setattr(value, "customer4", self)

    @property
    def student_record6(self):
        return self.__student_record6
    @student_record6.setter
    def student_record6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__student_record6", None)
        self.__student_record6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)



class books_database:

    def __init__(self, book_title: str, author: str, book_id: str, library3: "library" = None, customer4: "student" = None):
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.library3 = library3
        self.customer4 = customer4
        
        pass
    @property
    def book_title(self):
        return self.__book_title
    @book_title.setter
    def book_title(self, book_title: str):
        self.__book_title = book_title

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def book_id(self):
        return self.__book_id
    @book_id.setter
    def book_id(self, book_id: str):
        self.__book_id = book_id

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_database__customer4", None)
        self.__customer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books_database5"):
                opp_val = getattr(old_value, "books_database5", None)
                if opp_val == self:
                    setattr(old_value, "books_database5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books_database5"):
                opp_val = getattr(value, "books_database5", None)
                setattr(value, "books_database5", self)

    @property
    def library3(self):
        return self.__library3
    @library3.setter
    def library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_database__library3", None)
        self.__library3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books_database2"):
                opp_val = getattr(old_value, "books_database2", None)
                if opp_val == self:
                    setattr(old_value, "books_database2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books_database2"):
                opp_val = getattr(value, "books_database2", None)
                setattr(value, "books_database2", self)



class librarian:

    def __init__(self, name: str, library1: "library" = None):
        self.name = name
        self.library1 = library1
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library1(self):
        return self.__library1
    @library1.setter
    def library1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_librarian__library1", None)
        self.__library1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "librarian0"):
                opp_val = getattr(old_value, "librarian0", None)
                if opp_val == self:
                    setattr(old_value, "librarian0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "librarian0"):
                opp_val = getattr(value, "librarian0", None)
                setattr(value, "librarian0", self)



class library:

    def __init__(self, location: str, librarian0: "librarian" = None, books_database2: "books_database" = None):
        self.location = location
        self.librarian0 = librarian0
        self.books_database2 = books_database2
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def books_database2(self):
        return self.__books_database2
    @books_database2.setter
    def books_database2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library__books_database2", None)
        self.__books_database2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3"):
                opp_val = getattr(old_value, "library3", None)
                if opp_val == self:
                    setattr(old_value, "library3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3"):
                opp_val = getattr(value, "library3", None)
                setattr(value, "library3", self)

    @property
    def librarian0(self):
        return self.__librarian0
    @librarian0.setter
    def librarian0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library__librarian0", None)
        self.__librarian0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library1"):
                opp_val = getattr(old_value, "library1", None)
                if opp_val == self:
                    setattr(old_value, "library1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library1"):
                opp_val = getattr(value, "library1", None)
                setattr(value, "library1", self)

