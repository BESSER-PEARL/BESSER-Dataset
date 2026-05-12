from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Member:

    def __init__(self, id: int, username: str, password: str, name: str, log9: "log" = None, book11: "Book" = None):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.log9 = log9
        self.book11 = book11
        
        pass
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
    def log9(self):
        return self.__log9
    @log9.setter
    def log9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Member__log9", None)
        self.__log9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "member8"):
                opp_val = getattr(old_value, "member8", None)
                if opp_val == self:
                    setattr(old_value, "member8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "member8"):
                opp_val = getattr(value, "member8", None)
                setattr(value, "member8", self)

    @property
    def book11(self):
        return self.__book11
    @book11.setter
    def book11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Member__book11", None)
        self.__book11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "member10"):
                opp_val = getattr(old_value, "member10", None)
                if opp_val == self:
                    setattr(old_value, "member10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "member10"):
                opp_val = getattr(value, "member10", None)
                setattr(value, "member10", self)



class Book:

    def __init__(self, name: str, author: str, guest5: "Guest" = None, admin7: "Admin" = None, member10: "Member" = None):
        self.name = name
        self.author = author
        self.guest5 = guest5
        self.admin7 = admin7
        self.member10 = member10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def admin7(self):
        return self.__admin7
    @admin7.setter
    def admin7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__admin7", None)
        self.__admin7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book6"):
                opp_val = getattr(old_value, "book6", None)
                if opp_val == self:
                    setattr(old_value, "book6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book6"):
                opp_val = getattr(value, "book6", None)
                setattr(value, "book6", self)

    @property
    def guest5(self):
        return self.__guest5
    @guest5.setter
    def guest5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__guest5", None)
        self.__guest5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book4"):
                opp_val = getattr(old_value, "book4", None)
                if opp_val == self:
                    setattr(old_value, "book4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book4"):
                opp_val = getattr(value, "book4", None)
                setattr(value, "book4", self)

    @property
    def member10(self):
        return self.__member10
    @member10.setter
    def member10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__member10", None)
        self.__member10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book11"):
                opp_val = getattr(old_value, "book11", None)
                if opp_val == self:
                    setattr(old_value, "book11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book11"):
                opp_val = getattr(value, "book11", None)
                setattr(value, "book11", self)



class Guest:

    pass


class log:

    pass


class Admin:

    def __init__(self, id: int, username: str, password: str, log1: "log" = None, book6: "Book" = None):
        self.id = id
        self.username = username
        self.password = password
        self.log1 = log1
        self.book6 = book6
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
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
    def book6(self):
        return self.__book6
    @book6.setter
    def book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__book6", None)
        self.__book6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin7"):
                opp_val = getattr(old_value, "admin7", None)
                if opp_val == self:
                    setattr(old_value, "admin7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin7"):
                opp_val = getattr(value, "admin7", None)
                setattr(value, "admin7", self)

    @property
    def log1(self):
        return self.__log1
    @log1.setter
    def log1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__log1", None)
        self.__log1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin0"):
                opp_val = getattr(old_value, "admin0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin0"):
                opp_val = getattr(value, "admin0", None)
                if opp_val is None:
                    setattr(value, "admin0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Librarian:

    def __init__(self, id: int, attribute: str, password: str, log3: "log" = None):
        self.id = id
        self.attribute = attribute
        self.password = password
        self.log3 = log3
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def log3(self):
        return self.__log3
    @log3.setter
    def log3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Librarian__log3", None)
        self.__log3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "librarian2"):
                opp_val = getattr(old_value, "librarian2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "librarian2"):
                opp_val = getattr(value, "librarian2", None)
                if opp_val is None:
                    setattr(value, "librarian2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

