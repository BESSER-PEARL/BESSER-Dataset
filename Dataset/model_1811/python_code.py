from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DBLP_School:

    def __init__(self, name: str, address: str, DBLP_School: "DBLP_MastersThesis" = None, DBLP_School29: "DBLP_PhDThesis" = None):
        self.name = name
        self.address = address
        self.DBLP_School = DBLP_School
        self.DBLP_School29 = DBLP_School29
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DBLP_School(self):
        return self.__DBLP_School

    @DBLP_School.setter
    def DBLP_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_School__DBLP_School", None)
        self.__DBLP_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_MastersThesis"):
                opp_val = getattr(old_value, "DBLP_MastersThesis", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_MastersThesis", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_MastersThesis"):
                opp_val = getattr(value, "DBLP_MastersThesis", None)
                setattr(value, "DBLP_MastersThesis", self)

    @property
    def DBLP_School29(self):
        return self.__DBLP_School29

    @DBLP_School29.setter
    def DBLP_School29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_School__DBLP_School29", None)
        self.__DBLP_School29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_PhDThesis"):
                opp_val = getattr(old_value, "DBLP_PhDThesis", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_PhDThesis", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_PhDThesis"):
                opp_val = getattr(value, "DBLP_PhDThesis", None)
                setattr(value, "DBLP_PhDThesis", self)

class DBLP_Organization:

    def __init__(self, name: str, DBLP_Organization: "DBLP_InCollection" = None, DBLP_Organization27: "DBLP_Proceedings" = None, DBLP_Organization15: "DBLP_InProceedings" = None):
        self.name = name
        self.DBLP_Organization = DBLP_Organization
        self.DBLP_Organization27 = DBLP_Organization27
        self.DBLP_Organization15 = DBLP_Organization15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DBLP_Organization15(self):
        return self.__DBLP_Organization15

    @DBLP_Organization15.setter
    def DBLP_Organization15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Organization__DBLP_Organization15", None)
        self.__DBLP_Organization15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_InProceedings14"):
                opp_val = getattr(old_value, "DBLP_InProceedings14", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_InProceedings14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_InProceedings14"):
                opp_val = getattr(value, "DBLP_InProceedings14", None)
                setattr(value, "DBLP_InProceedings14", self)

    @property
    def DBLP_Organization27(self):
        return self.__DBLP_Organization27

    @DBLP_Organization27.setter
    def DBLP_Organization27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Organization__DBLP_Organization27", None)
        self.__DBLP_Organization27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Proceedings26"):
                opp_val = getattr(old_value, "DBLP_Proceedings26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Proceedings26"):
                opp_val = getattr(value, "DBLP_Proceedings26", None)
                if opp_val is None:
                    setattr(value, "DBLP_Proceedings26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DBLP_Organization(self):
        return self.__DBLP_Organization

    @DBLP_Organization.setter
    def DBLP_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Organization__DBLP_Organization", None)
        self.__DBLP_Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_InCollection7"):
                opp_val = getattr(old_value, "DBLP_InCollection7", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_InCollection7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_InCollection7"):
                opp_val = getattr(value, "DBLP_InCollection7", None)
                setattr(value, "DBLP_InCollection7", self)

class DBLP_Editor:

    def __init__(self, name: str, DBLP_Editor12: "DBLP_InProceedings" = None, DBLP_Editor: "DBLP_InCollection" = None, DBLP_Editor21: "DBLP_Proceedings" = None, DBLP_Editor31: "DBLP_Www" = None):
        self.name = name
        self.DBLP_Editor12 = DBLP_Editor12
        self.DBLP_Editor = DBLP_Editor
        self.DBLP_Editor21 = DBLP_Editor21
        self.DBLP_Editor31 = DBLP_Editor31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DBLP_Editor21(self):
        return self.__DBLP_Editor21

    @DBLP_Editor21.setter
    def DBLP_Editor21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Editor__DBLP_Editor21", None)
        self.__DBLP_Editor21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Proceedings"):
                opp_val = getattr(old_value, "DBLP_Proceedings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Proceedings"):
                opp_val = getattr(value, "DBLP_Proceedings", None)
                if opp_val is None:
                    setattr(value, "DBLP_Proceedings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DBLP_Editor12(self):
        return self.__DBLP_Editor12

    @DBLP_Editor12.setter
    def DBLP_Editor12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Editor__DBLP_Editor12", None)
        self.__DBLP_Editor12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_InProceedings"):
                opp_val = getattr(old_value, "DBLP_InProceedings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_InProceedings"):
                opp_val = getattr(value, "DBLP_InProceedings", None)
                if opp_val is None:
                    setattr(value, "DBLP_InProceedings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DBLP_Editor(self):
        return self.__DBLP_Editor

    @DBLP_Editor.setter
    def DBLP_Editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Editor__DBLP_Editor", None)
        self.__DBLP_Editor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_InCollection"):
                opp_val = getattr(old_value, "DBLP_InCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_InCollection"):
                opp_val = getattr(value, "DBLP_InCollection", None)
                if opp_val is None:
                    setattr(value, "DBLP_InCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DBLP_Editor31(self):
        return self.__DBLP_Editor31

    @DBLP_Editor31.setter
    def DBLP_Editor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Editor__DBLP_Editor31", None)
        self.__DBLP_Editor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Www"):
                opp_val = getattr(old_value, "DBLP_Www", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Www"):
                opp_val = getattr(value, "DBLP_Www", None)
                if opp_val is None:
                    setattr(value, "DBLP_Www", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DBLP_Publisher:

    def __init__(self, name: str, address: str, DBLP_Publisher: "DBLP_Book" = None, DBLP_Publisher10: "DBLP_InCollection" = None, DBLP_Publisher24: "DBLP_Proceedings" = None, DBLP_Publisher18: "DBLP_InProceedings" = None):
        self.name = name
        self.address = address
        self.DBLP_Publisher = DBLP_Publisher
        self.DBLP_Publisher10 = DBLP_Publisher10
        self.DBLP_Publisher24 = DBLP_Publisher24
        self.DBLP_Publisher18 = DBLP_Publisher18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def DBLP_Publisher10(self):
        return self.__DBLP_Publisher10

    @DBLP_Publisher10.setter
    def DBLP_Publisher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Publisher__DBLP_Publisher10", None)
        self.__DBLP_Publisher10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_InCollection9"):
                opp_val = getattr(old_value, "DBLP_InCollection9", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_InCollection9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_InCollection9"):
                opp_val = getattr(value, "DBLP_InCollection9", None)
                setattr(value, "DBLP_InCollection9", self)

    @property
    def DBLP_Publisher18(self):
        return self.__DBLP_Publisher18

    @DBLP_Publisher18.setter
    def DBLP_Publisher18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Publisher__DBLP_Publisher18", None)
        self.__DBLP_Publisher18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_InProceedings17"):
                opp_val = getattr(old_value, "DBLP_InProceedings17", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_InProceedings17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_InProceedings17"):
                opp_val = getattr(value, "DBLP_InProceedings17", None)
                setattr(value, "DBLP_InProceedings17", self)

    @property
    def DBLP_Publisher24(self):
        return self.__DBLP_Publisher24

    @DBLP_Publisher24.setter
    def DBLP_Publisher24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Publisher__DBLP_Publisher24", None)
        self.__DBLP_Publisher24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Proceedings23"):
                opp_val = getattr(old_value, "DBLP_Proceedings23", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Proceedings23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Proceedings23"):
                opp_val = getattr(value, "DBLP_Proceedings23", None)
                setattr(value, "DBLP_Proceedings23", self)

    @property
    def DBLP_Publisher(self):
        return self.__DBLP_Publisher

    @DBLP_Publisher.setter
    def DBLP_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Publisher__DBLP_Publisher", None)
        self.__DBLP_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Book"):
                opp_val = getattr(old_value, "DBLP_Book", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Book"):
                opp_val = getattr(value, "DBLP_Book", None)
                setattr(value, "DBLP_Book", self)

class Record:

    pass
class DBLP_InProceedings(Record):

    def __init__(self, bootitle: str, year: int, fromPage: int, toPage: int, month: str, title: str, DBLP_InProceedings: set["DBLP_Editor"] = None, DBLP_InProceedings14: "DBLP_Organization" = None, DBLP_InProceedings17: "DBLP_Publisher" = None):
        self.bootitle = bootitle
        self.year = year
        self.fromPage = fromPage
        self.toPage = toPage
        self.month = month
        self.title = title
        self.DBLP_InProceedings = DBLP_InProceedings if DBLP_InProceedings is not None else set()
        self.DBLP_InProceedings14 = DBLP_InProceedings14
        self.DBLP_InProceedings17 = DBLP_InProceedings17
        
    @property
    def fromPage(self) -> int:
        return self.__fromPage

    @fromPage.setter
    def fromPage(self, fromPage: int):
        self.__fromPage = fromPage

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def bootitle(self) -> str:
        return self.__bootitle

    @bootitle.setter
    def bootitle(self, bootitle: str):
        self.__bootitle = bootitle

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def toPage(self) -> int:
        return self.__toPage

    @toPage.setter
    def toPage(self, toPage: int):
        self.__toPage = toPage

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def DBLP_InProceedings(self):
        return self.__DBLP_InProceedings

    @DBLP_InProceedings.setter
    def DBLP_InProceedings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_InProceedings__DBLP_InProceedings", None)
        self.__DBLP_InProceedings = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBLP_Editor12"):
                    opp_val = getattr(item, "DBLP_Editor12", None)
                    
                    if opp_val == self:
                        setattr(item, "DBLP_Editor12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBLP_Editor12"):
                    opp_val = getattr(item, "DBLP_Editor12", None)
                    
                    setattr(item, "DBLP_Editor12", self)
                    

    @property
    def DBLP_InProceedings17(self):
        return self.__DBLP_InProceedings17

    @DBLP_InProceedings17.setter
    def DBLP_InProceedings17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_InProceedings__DBLP_InProceedings17", None)
        self.__DBLP_InProceedings17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Publisher18"):
                opp_val = getattr(old_value, "DBLP_Publisher18", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Publisher18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Publisher18"):
                opp_val = getattr(value, "DBLP_Publisher18", None)
                setattr(value, "DBLP_Publisher18", self)

    @property
    def DBLP_InProceedings14(self):
        return self.__DBLP_InProceedings14

    @DBLP_InProceedings14.setter
    def DBLP_InProceedings14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_InProceedings__DBLP_InProceedings14", None)
        self.__DBLP_InProceedings14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Organization15"):
                opp_val = getattr(old_value, "DBLP_Organization15", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Organization15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Organization15"):
                opp_val = getattr(value, "DBLP_Organization15", None)
                setattr(value, "DBLP_Organization15", self)

class DBLP_InCollection(Record):

    def __init__(self, title: str, bookTitle: str, year: int, fromPage: int, toPage: int, month: str, DBLP_InCollection: set["DBLP_Editor"] = None, DBLP_InCollection7: "DBLP_Organization" = None, DBLP_InCollection9: "DBLP_Publisher" = None):
        self.title = title
        self.bookTitle = bookTitle
        self.year = year
        self.fromPage = fromPage
        self.toPage = toPage
        self.month = month
        self.DBLP_InCollection = DBLP_InCollection if DBLP_InCollection is not None else set()
        self.DBLP_InCollection7 = DBLP_InCollection7
        self.DBLP_InCollection9 = DBLP_InCollection9
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def fromPage(self) -> int:
        return self.__fromPage

    @fromPage.setter
    def fromPage(self, fromPage: int):
        self.__fromPage = fromPage

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def toPage(self) -> int:
        return self.__toPage

    @toPage.setter
    def toPage(self, toPage: int):
        self.__toPage = toPage

    @property
    def bookTitle(self) -> str:
        return self.__bookTitle

    @bookTitle.setter
    def bookTitle(self, bookTitle: str):
        self.__bookTitle = bookTitle

    @property
    def DBLP_InCollection9(self):
        return self.__DBLP_InCollection9

    @DBLP_InCollection9.setter
    def DBLP_InCollection9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_InCollection__DBLP_InCollection9", None)
        self.__DBLP_InCollection9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Publisher10"):
                opp_val = getattr(old_value, "DBLP_Publisher10", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Publisher10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Publisher10"):
                opp_val = getattr(value, "DBLP_Publisher10", None)
                setattr(value, "DBLP_Publisher10", self)

    @property
    def DBLP_InCollection7(self):
        return self.__DBLP_InCollection7

    @DBLP_InCollection7.setter
    def DBLP_InCollection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_InCollection__DBLP_InCollection7", None)
        self.__DBLP_InCollection7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Organization"):
                opp_val = getattr(old_value, "DBLP_Organization", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Organization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Organization"):
                opp_val = getattr(value, "DBLP_Organization", None)
                setattr(value, "DBLP_Organization", self)

    @property
    def DBLP_InCollection(self):
        return self.__DBLP_InCollection

    @DBLP_InCollection.setter
    def DBLP_InCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_InCollection__DBLP_InCollection", None)
        self.__DBLP_InCollection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBLP_Editor"):
                    opp_val = getattr(item, "DBLP_Editor", None)
                    
                    if opp_val == self:
                        setattr(item, "DBLP_Editor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBLP_Editor"):
                    opp_val = getattr(item, "DBLP_Editor", None)
                    
                    setattr(item, "DBLP_Editor", self)
                    

class DBLP_Proceedings(Record):

    def __init__(self, month: str, title: str, year: int, isbn: str, DBLP_Proceedings: set["DBLP_Editor"] = None, DBLP_Proceedings23: "DBLP_Publisher" = None, DBLP_Proceedings26: set["DBLP_Organization"] = None):
        self.month = month
        self.title = title
        self.year = year
        self.isbn = isbn
        self.DBLP_Proceedings = DBLP_Proceedings if DBLP_Proceedings is not None else set()
        self.DBLP_Proceedings23 = DBLP_Proceedings23
        self.DBLP_Proceedings26 = DBLP_Proceedings26 if DBLP_Proceedings26 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def DBLP_Proceedings23(self):
        return self.__DBLP_Proceedings23

    @DBLP_Proceedings23.setter
    def DBLP_Proceedings23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Proceedings__DBLP_Proceedings23", None)
        self.__DBLP_Proceedings23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Publisher24"):
                opp_val = getattr(old_value, "DBLP_Publisher24", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Publisher24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Publisher24"):
                opp_val = getattr(value, "DBLP_Publisher24", None)
                setattr(value, "DBLP_Publisher24", self)

    @property
    def DBLP_Proceedings(self):
        return self.__DBLP_Proceedings

    @DBLP_Proceedings.setter
    def DBLP_Proceedings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Proceedings__DBLP_Proceedings", None)
        self.__DBLP_Proceedings = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBLP_Editor21"):
                    opp_val = getattr(item, "DBLP_Editor21", None)
                    
                    if opp_val == self:
                        setattr(item, "DBLP_Editor21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBLP_Editor21"):
                    opp_val = getattr(item, "DBLP_Editor21", None)
                    
                    setattr(item, "DBLP_Editor21", self)
                    

    @property
    def DBLP_Proceedings26(self):
        return self.__DBLP_Proceedings26

    @DBLP_Proceedings26.setter
    def DBLP_Proceedings26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Proceedings__DBLP_Proceedings26", None)
        self.__DBLP_Proceedings26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBLP_Organization27"):
                    opp_val = getattr(item, "DBLP_Organization27", None)
                    
                    if opp_val == self:
                        setattr(item, "DBLP_Organization27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBLP_Organization27"):
                    opp_val = getattr(item, "DBLP_Organization27", None)
                    
                    setattr(item, "DBLP_Organization27", self)
                    

class DBLP_Www(Record):

    def __init__(self, title: str, year: int, month: str, DBLP_Www: set["DBLP_Editor"] = None):
        self.title = title
        self.year = year
        self.month = month
        self.DBLP_Www = DBLP_Www if DBLP_Www is not None else set()
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def DBLP_Www(self):
        return self.__DBLP_Www

    @DBLP_Www.setter
    def DBLP_Www(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Www__DBLP_Www", None)
        self.__DBLP_Www = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBLP_Editor31"):
                    opp_val = getattr(item, "DBLP_Editor31", None)
                    
                    if opp_val == self:
                        setattr(item, "DBLP_Editor31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBLP_Editor31"):
                    opp_val = getattr(item, "DBLP_Editor31", None)
                    
                    setattr(item, "DBLP_Editor31", self)
                    

class DBLP_Book(Record):

    def __init__(self, month: str, volume: int, series: str, edition: int, isbn: str, title: str, year: int, DBLP_Book: "DBLP_Publisher" = None):
        self.month = month
        self.volume = volume
        self.series = series
        self.edition = edition
        self.isbn = isbn
        self.title = title
        self.year = year
        self.DBLP_Book = DBLP_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def edition(self) -> int:
        return self.__edition

    @edition.setter
    def edition(self, edition: int):
        self.__edition = edition

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int):
        self.__volume = volume

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def DBLP_Book(self):
        return self.__DBLP_Book

    @DBLP_Book.setter
    def DBLP_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Book__DBLP_Book", None)
        self.__DBLP_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_Publisher"):
                opp_val = getattr(old_value, "DBLP_Publisher", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_Publisher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_Publisher"):
                opp_val = getattr(value, "DBLP_Publisher", None)
                setattr(value, "DBLP_Publisher", self)

class DBLP_PhDThesis(Record):

    def __init__(self, title: str, year: int, month: str, DBLP_PhDThesis: "DBLP_School" = None):
        self.title = title
        self.year = year
        self.month = month
        self.DBLP_PhDThesis = DBLP_PhDThesis
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def DBLP_PhDThesis(self):
        return self.__DBLP_PhDThesis

    @DBLP_PhDThesis.setter
    def DBLP_PhDThesis(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_PhDThesis__DBLP_PhDThesis", None)
        self.__DBLP_PhDThesis = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_School29"):
                opp_val = getattr(old_value, "DBLP_School29", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_School29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_School29"):
                opp_val = getattr(value, "DBLP_School29", None)
                setattr(value, "DBLP_School29", self)

class DBLP_MastersThesis(Record):

    def __init__(self, title: str, year: int, month: str, DBLP_MastersThesis: "DBLP_School" = None):
        self.title = title
        self.year = year
        self.month = month
        self.DBLP_MastersThesis = DBLP_MastersThesis
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def DBLP_MastersThesis(self):
        return self.__DBLP_MastersThesis

    @DBLP_MastersThesis.setter
    def DBLP_MastersThesis(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_MastersThesis__DBLP_MastersThesis", None)
        self.__DBLP_MastersThesis = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBLP_School"):
                opp_val = getattr(old_value, "DBLP_School", None)
                if opp_val == self:
                    setattr(old_value, "DBLP_School", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBLP_School"):
                opp_val = getattr(value, "DBLP_School", None)
                setattr(value, "DBLP_School", self)

class DBLP_Article(Record):

    def __init__(self, title: str, fromPage: int, toPage: int, number: int, volume: str, month: str, year: int, articles: "DBLP_Journal" = None, Article: "DBLP_Journal" = None):
        self.title = title
        self.fromPage = fromPage
        self.toPage = toPage
        self.number = number
        self.volume = volume
        self.month = month
        self.year = year
        self.articles = articles
        self.Article = Article
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def fromPage(self) -> int:
        return self.__fromPage

    @fromPage.setter
    def fromPage(self, fromPage: int):
        self.__fromPage = fromPage

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def toPage(self) -> int:
        return self.__toPage

    @toPage.setter
    def toPage(self, toPage: int):
        self.__toPage = toPage

    @property
    def Article(self):
        return self.__Article

    @Article.setter
    def Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Article__Article", None)
        self.__Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "journal"):
                opp_val = getattr(old_value, "journal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "journal"):
                opp_val = getattr(value, "journal", None)
                if opp_val is None:
                    setattr(value, "journal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def articles(self):
        return self.__articles

    @articles.setter
    def articles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Article__articles", None)
        self.__articles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Journal"):
                opp_val = getattr(old_value, "Journal", None)
                if opp_val == self:
                    setattr(old_value, "Journal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Journal"):
                opp_val = getattr(value, "Journal", None)
                setattr(value, "Journal", self)

class DBLP_Author:

    def __init__(self, name: str, Author: "DBLP_Record" = None, authors: set["DBLP_Record"] = None):
        self.name = name
        self.Author = Author
        self.authors = authors if authors is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Author__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Record"):
                    opp_val = getattr(item, "Record", None)
                    
                    if opp_val == self:
                        setattr(item, "Record", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Record"):
                    opp_val = getattr(item, "Record", None)
                    
                    setattr(item, "Record", self)
                    

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "records"):
                opp_val = getattr(old_value, "records", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "records"):
                opp_val = getattr(value, "records", None)
                if opp_val is None:
                    setattr(value, "records", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DBLP_Record(ABC):

    def __init__(self, ee: str, url: str, key: str, mdate: str, records: set["DBLP_Author"] = None, Record: "DBLP_Author" = None):
        self.ee = ee
        self.url = url
        self.key = key
        self.mdate = mdate
        self.records = records if records is not None else set()
        self.Record = Record
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def ee(self) -> str:
        return self.__ee

    @ee.setter
    def ee(self, ee: str):
        self.__ee = ee

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def mdate(self) -> str:
        return self.__mdate

    @mdate.setter
    def mdate(self, mdate: str):
        self.__mdate = mdate

    @property
    def records(self):
        return self.__records

    @records.setter
    def records(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Record__records", None)
        self.__records = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    setattr(item, "Author", self)
                    

    @property
    def Record(self):
        return self.__Record

    @Record.setter
    def Record(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Record__Record", None)
        self.__Record = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DBLP_Journal:

    def __init__(self, name: str, Journal: "DBLP_Article" = None, journal: set["DBLP_Article"] = None):
        self.name = name
        self.Journal = Journal
        self.journal = journal if journal is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Journal(self):
        return self.__Journal

    @Journal.setter
    def Journal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Journal__Journal", None)
        self.__Journal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articles"):
                opp_val = getattr(old_value, "articles", None)
                if opp_val == self:
                    setattr(old_value, "articles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articles"):
                opp_val = getattr(value, "articles", None)
                setattr(value, "articles", self)

    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DBLP_Journal__journal", None)
        self.__journal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Article"):
                    opp_val = getattr(item, "Article", None)
                    
                    if opp_val == self:
                        setattr(item, "Article", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Article"):
                    opp_val = getattr(item, "Article", None)
                    
                    setattr(item, "Article", self)
                    
