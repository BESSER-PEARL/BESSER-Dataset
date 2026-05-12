from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Staff:

    def __init__(self, name: str, id: int, book8: "Book" = None, magazine10: "Magazine" = None, media12: "Media" = None, computer14: "Computer" = None):
        self.name = name
        self.id = id
        self.book8 = book8
        self.magazine10 = magazine10
        self.media12 = media12
        self.computer14 = computer14
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def magazine10(self):
        return self.__magazine10
    @magazine10.setter
    def magazine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__magazine10", None)
        self.__magazine10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff11"):
                opp_val = getattr(old_value, "staff11", None)
                if opp_val == self:
                    setattr(old_value, "staff11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff11"):
                opp_val = getattr(value, "staff11", None)
                setattr(value, "staff11", self)

    @property
    def book8(self):
        return self.__book8
    @book8.setter
    def book8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__book8", None)
        self.__book8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff9"):
                opp_val = getattr(old_value, "staff9", None)
                if opp_val == self:
                    setattr(old_value, "staff9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff9"):
                opp_val = getattr(value, "staff9", None)
                setattr(value, "staff9", self)

    @property
    def media12(self):
        return self.__media12
    @media12.setter
    def media12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__media12", None)
        self.__media12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff13"):
                opp_val = getattr(old_value, "staff13", None)
                if opp_val == self:
                    setattr(old_value, "staff13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff13"):
                opp_val = getattr(value, "staff13", None)
                setattr(value, "staff13", self)

    @property
    def computer14(self):
        return self.__computer14
    @computer14.setter
    def computer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__computer14", None)
        self.__computer14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff15"):
                opp_val = getattr(old_value, "staff15", None)
                if opp_val == self:
                    setattr(old_value, "staff15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff15"):
                opp_val = getattr(value, "staff15", None)
                setattr(value, "staff15", self)



class Media:

    def __init__(self, type: int, refNum: int, patron5: "Patron" = None, staff13: "Staff" = None):
        self.type = type
        self.refNum = refNum
        self.patron5 = patron5
        self.staff13 = staff13
        
        pass
    @property
    def refNum(self):
        return self.__refNum
    @refNum.setter
    def refNum(self, refNum: int):
        self.__refNum = refNum

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def patron5(self):
        return self.__patron5
    @patron5.setter
    def patron5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Media__patron5", None)
        self.__patron5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "media4"):
                opp_val = getattr(old_value, "media4", None)
                if opp_val == self:
                    setattr(old_value, "media4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "media4"):
                opp_val = getattr(value, "media4", None)
                setattr(value, "media4", self)

    @property
    def staff13(self):
        return self.__staff13
    @staff13.setter
    def staff13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Media__staff13", None)
        self.__staff13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "media12"):
                opp_val = getattr(old_value, "media12", None)
                if opp_val == self:
                    setattr(old_value, "media12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "media12"):
                opp_val = getattr(value, "media12", None)
                setattr(value, "media12", self)



class Computer:

    def __init__(self, compID: int, patron7: "Patron" = None, staff15: "Staff" = None):
        self.compID = compID
        self.patron7 = patron7
        self.staff15 = staff15
        
        pass
    @property
    def compID(self):
        return self.__compID
    @compID.setter
    def compID(self, compID: int):
        self.__compID = compID

    @property
    def staff15(self):
        return self.__staff15
    @staff15.setter
    def staff15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Computer__staff15", None)
        self.__staff15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "computer14"):
                opp_val = getattr(old_value, "computer14", None)
                if opp_val == self:
                    setattr(old_value, "computer14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "computer14"):
                opp_val = getattr(value, "computer14", None)
                setattr(value, "computer14", self)

    @property
    def patron7(self):
        return self.__patron7
    @patron7.setter
    def patron7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Computer__patron7", None)
        self.__patron7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "computer6"):
                opp_val = getattr(old_value, "computer6", None)
                if opp_val == self:
                    setattr(old_value, "computer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "computer6"):
                opp_val = getattr(value, "computer6", None)
                setattr(value, "computer6", self)



class Patron:

    def __init__(self, name: str, id: int, position: str, magazine2: "Magazine" = None, media4: "Media" = None, computer6: "Computer" = None, book0: "Book" = None):
        self.name = name
        self.id = id
        self.position = position
        self.magazine2 = magazine2
        self.media4 = media4
        self.computer6 = computer6
        self.book0 = book0
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def media4(self):
        return self.__media4
    @media4.setter
    def media4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__media4", None)
        self.__media4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron5"):
                opp_val = getattr(old_value, "patron5", None)
                if opp_val == self:
                    setattr(old_value, "patron5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron5"):
                opp_val = getattr(value, "patron5", None)
                setattr(value, "patron5", self)

    @property
    def magazine2(self):
        return self.__magazine2
    @magazine2.setter
    def magazine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__magazine2", None)
        self.__magazine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron3"):
                opp_val = getattr(old_value, "patron3", None)
                if opp_val == self:
                    setattr(old_value, "patron3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron3"):
                opp_val = getattr(value, "patron3", None)
                setattr(value, "patron3", self)

    @property
    def book0(self):
        return self.__book0
    @book0.setter
    def book0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__book0", None)
        self.__book0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron1"):
                opp_val = getattr(old_value, "patron1", None)
                if opp_val == self:
                    setattr(old_value, "patron1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron1"):
                opp_val = getattr(value, "patron1", None)
                setattr(value, "patron1", self)

    @property
    def computer6(self):
        return self.__computer6
    @computer6.setter
    def computer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patron__computer6", None)
        self.__computer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron7"):
                opp_val = getattr(old_value, "patron7", None)
                if opp_val == self:
                    setattr(old_value, "patron7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron7"):
                opp_val = getattr(value, "patron7", None)
                setattr(value, "patron7", self)



class Magazine:

    def __init__(self, name: str, issueNum: int, location: str, patron3: "Patron" = None, staff11: "Staff" = None):
        self.name = name
        self.issueNum = issueNum
        self.location = location
        self.patron3 = patron3
        self.staff11 = staff11
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def issueNum(self):
        return self.__issueNum
    @issueNum.setter
    def issueNum(self, issueNum: int):
        self.__issueNum = issueNum

    @property
    def staff11(self):
        return self.__staff11
    @staff11.setter
    def staff11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Magazine__staff11", None)
        self.__staff11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "magazine10"):
                opp_val = getattr(old_value, "magazine10", None)
                if opp_val == self:
                    setattr(old_value, "magazine10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "magazine10"):
                opp_val = getattr(value, "magazine10", None)
                setattr(value, "magazine10", self)

    @property
    def patron3(self):
        return self.__patron3
    @patron3.setter
    def patron3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Magazine__patron3", None)
        self.__patron3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "magazine2"):
                opp_val = getattr(old_value, "magazine2", None)
                if opp_val == self:
                    setattr(old_value, "magazine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "magazine2"):
                opp_val = getattr(value, "magazine2", None)
                setattr(value, "magazine2", self)



class Book:

    def __init__(self, title: str, author: str, refNum: int, dueDate: str, staff9: "Staff" = None, patron1: "Patron" = None):
        self.title = title
        self.author = author
        self.refNum = refNum
        self.dueDate = dueDate
        self.staff9 = staff9
        self.patron1 = patron1
        
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def dueDate(self):
        return self.__dueDate
    @dueDate.setter
    def dueDate(self, dueDate: str):
        self.__dueDate = dueDate

    @property
    def refNum(self):
        return self.__refNum
    @refNum.setter
    def refNum(self, refNum: int):
        self.__refNum = refNum

    @property
    def patron1(self):
        return self.__patron1
    @patron1.setter
    def patron1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__patron1", None)
        self.__patron1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book0"):
                opp_val = getattr(old_value, "book0", None)
                if opp_val == self:
                    setattr(old_value, "book0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book0"):
                opp_val = getattr(value, "book0", None)
                setattr(value, "book0", self)

    @property
    def staff9(self):
        return self.__staff9
    @staff9.setter
    def staff9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__staff9", None)
        self.__staff9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book8"):
                opp_val = getattr(old_value, "book8", None)
                if opp_val == self:
                    setattr(old_value, "book8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book8"):
                opp_val = getattr(value, "book8", None)
                setattr(value, "book8", self)

