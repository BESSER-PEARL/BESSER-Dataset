from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class comicBookCollection_Person:

    def __init__(self, name: str, comicBookCollection_Person: "comicBookCollection_Book" = None, comicBookCollection_Person9: "comicBookCollection_Book" = None, comicBookCollection_Person12: "comicBookCollection_Book" = None, comicBookCollection_Person15: "comicBookCollection_Book" = None):
        self.name = name
        self.comicBookCollection_Person = comicBookCollection_Person
        self.comicBookCollection_Person9 = comicBookCollection_Person9
        self.comicBookCollection_Person12 = comicBookCollection_Person12
        self.comicBookCollection_Person15 = comicBookCollection_Person15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comicBookCollection_Person9(self):
        return self.__comicBookCollection_Person9

    @comicBookCollection_Person9.setter
    def comicBookCollection_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Person__comicBookCollection_Person9", None)
        self.__comicBookCollection_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Book8"):
                opp_val = getattr(old_value, "comicBookCollection_Book8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Book8"):
                opp_val = getattr(value, "comicBookCollection_Book8", None)
                if opp_val is None:
                    setattr(value, "comicBookCollection_Book8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comicBookCollection_Person15(self):
        return self.__comicBookCollection_Person15

    @comicBookCollection_Person15.setter
    def comicBookCollection_Person15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Person__comicBookCollection_Person15", None)
        self.__comicBookCollection_Person15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Book14"):
                opp_val = getattr(old_value, "comicBookCollection_Book14", None)
                if opp_val == self:
                    setattr(old_value, "comicBookCollection_Book14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Book14"):
                opp_val = getattr(value, "comicBookCollection_Book14", None)
                setattr(value, "comicBookCollection_Book14", self)

    @property
    def comicBookCollection_Person12(self):
        return self.__comicBookCollection_Person12

    @comicBookCollection_Person12.setter
    def comicBookCollection_Person12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Person__comicBookCollection_Person12", None)
        self.__comicBookCollection_Person12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Book11"):
                opp_val = getattr(old_value, "comicBookCollection_Book11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Book11"):
                opp_val = getattr(value, "comicBookCollection_Book11", None)
                if opp_val is None:
                    setattr(value, "comicBookCollection_Book11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comicBookCollection_Person(self):
        return self.__comicBookCollection_Person

    @comicBookCollection_Person.setter
    def comicBookCollection_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Person__comicBookCollection_Person", None)
        self.__comicBookCollection_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Book6"):
                opp_val = getattr(old_value, "comicBookCollection_Book6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Book6"):
                opp_val = getattr(value, "comicBookCollection_Book6", None)
                if opp_val is None:
                    setattr(value, "comicBookCollection_Book6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comicBookCollection_Book:

    def __init__(self, title: str, publicationDate: str, comicBookCollection_Book: "comicBookCollection_Series" = None, comicBookCollection_Book6: set["comicBookCollection_Person"] = None, comicBookCollection_Book8: set["comicBookCollection_Person"] = None, comicBookCollection_Book11: set["comicBookCollection_Person"] = None, comicBookCollection_Book14: "comicBookCollection_Person" = None):
        self.title = title
        self.publicationDate = publicationDate
        self.comicBookCollection_Book = comicBookCollection_Book
        self.comicBookCollection_Book6 = comicBookCollection_Book6 if comicBookCollection_Book6 is not None else set()
        self.comicBookCollection_Book8 = comicBookCollection_Book8 if comicBookCollection_Book8 is not None else set()
        self.comicBookCollection_Book11 = comicBookCollection_Book11 if comicBookCollection_Book11 is not None else set()
        self.comicBookCollection_Book14 = comicBookCollection_Book14
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def publicationDate(self) -> str:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: str):
        self.__publicationDate = publicationDate

    @property
    def comicBookCollection_Book14(self):
        return self.__comicBookCollection_Book14

    @comicBookCollection_Book14.setter
    def comicBookCollection_Book14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Book__comicBookCollection_Book14", None)
        self.__comicBookCollection_Book14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Person15"):
                opp_val = getattr(old_value, "comicBookCollection_Person15", None)
                if opp_val == self:
                    setattr(old_value, "comicBookCollection_Person15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Person15"):
                opp_val = getattr(value, "comicBookCollection_Person15", None)
                setattr(value, "comicBookCollection_Person15", self)

    @property
    def comicBookCollection_Book11(self):
        return self.__comicBookCollection_Book11

    @comicBookCollection_Book11.setter
    def comicBookCollection_Book11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Book__comicBookCollection_Book11", None)
        self.__comicBookCollection_Book11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comicBookCollection_Person12"):
                    opp_val = getattr(item, "comicBookCollection_Person12", None)
                    
                    if opp_val == self:
                        setattr(item, "comicBookCollection_Person12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comicBookCollection_Person12"):
                    opp_val = getattr(item, "comicBookCollection_Person12", None)
                    
                    setattr(item, "comicBookCollection_Person12", self)
                    

    @property
    def comicBookCollection_Book8(self):
        return self.__comicBookCollection_Book8

    @comicBookCollection_Book8.setter
    def comicBookCollection_Book8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Book__comicBookCollection_Book8", None)
        self.__comicBookCollection_Book8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comicBookCollection_Person9"):
                    opp_val = getattr(item, "comicBookCollection_Person9", None)
                    
                    if opp_val == self:
                        setattr(item, "comicBookCollection_Person9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comicBookCollection_Person9"):
                    opp_val = getattr(item, "comicBookCollection_Person9", None)
                    
                    setattr(item, "comicBookCollection_Person9", self)
                    

    @property
    def comicBookCollection_Book6(self):
        return self.__comicBookCollection_Book6

    @comicBookCollection_Book6.setter
    def comicBookCollection_Book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Book__comicBookCollection_Book6", None)
        self.__comicBookCollection_Book6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comicBookCollection_Person"):
                    opp_val = getattr(item, "comicBookCollection_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "comicBookCollection_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comicBookCollection_Person"):
                    opp_val = getattr(item, "comicBookCollection_Person", None)
                    
                    setattr(item, "comicBookCollection_Person", self)
                    

    @property
    def comicBookCollection_Book(self):
        return self.__comicBookCollection_Book

    @comicBookCollection_Book.setter
    def comicBookCollection_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Book__comicBookCollection_Book", None)
        self.__comicBookCollection_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Series4"):
                opp_val = getattr(old_value, "comicBookCollection_Series4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Series4"):
                opp_val = getattr(value, "comicBookCollection_Series4", None)
                if opp_val is None:
                    setattr(value, "comicBookCollection_Series4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comicBookCollection_Series:

    def __init__(self, seriesTitle: str, comicBookCollection_Series: "comicBookCollection_Publisher" = None, comicBookCollection_Series4: set["comicBookCollection_Book"] = None):
        self.seriesTitle = seriesTitle
        self.comicBookCollection_Series = comicBookCollection_Series
        self.comicBookCollection_Series4 = comicBookCollection_Series4 if comicBookCollection_Series4 is not None else set()
        
    @property
    def seriesTitle(self) -> str:
        return self.__seriesTitle

    @seriesTitle.setter
    def seriesTitle(self, seriesTitle: str):
        self.__seriesTitle = seriesTitle

    @property
    def comicBookCollection_Series4(self):
        return self.__comicBookCollection_Series4

    @comicBookCollection_Series4.setter
    def comicBookCollection_Series4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Series__comicBookCollection_Series4", None)
        self.__comicBookCollection_Series4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comicBookCollection_Book"):
                    opp_val = getattr(item, "comicBookCollection_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "comicBookCollection_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comicBookCollection_Book"):
                    opp_val = getattr(item, "comicBookCollection_Book", None)
                    
                    setattr(item, "comicBookCollection_Book", self)
                    

    @property
    def comicBookCollection_Series(self):
        return self.__comicBookCollection_Series

    @comicBookCollection_Series.setter
    def comicBookCollection_Series(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Series__comicBookCollection_Series", None)
        self.__comicBookCollection_Series = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_Publisher2"):
                opp_val = getattr(old_value, "comicBookCollection_Publisher2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_Publisher2"):
                opp_val = getattr(value, "comicBookCollection_Publisher2", None)
                if opp_val is None:
                    setattr(value, "comicBookCollection_Publisher2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comicBookCollection_Publisher:

    def __init__(self, publishingName: str, comicBookCollection_Publisher: "comicBookCollection_ComicBookCollection" = None, comicBookCollection_Publisher2: set["comicBookCollection_Series"] = None):
        self.publishingName = publishingName
        self.comicBookCollection_Publisher = comicBookCollection_Publisher
        self.comicBookCollection_Publisher2 = comicBookCollection_Publisher2 if comicBookCollection_Publisher2 is not None else set()
        
    @property
    def publishingName(self) -> str:
        return self.__publishingName

    @publishingName.setter
    def publishingName(self, publishingName: str):
        self.__publishingName = publishingName

    @property
    def comicBookCollection_Publisher2(self):
        return self.__comicBookCollection_Publisher2

    @comicBookCollection_Publisher2.setter
    def comicBookCollection_Publisher2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Publisher__comicBookCollection_Publisher2", None)
        self.__comicBookCollection_Publisher2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comicBookCollection_Series"):
                    opp_val = getattr(item, "comicBookCollection_Series", None)
                    
                    if opp_val == self:
                        setattr(item, "comicBookCollection_Series", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comicBookCollection_Series"):
                    opp_val = getattr(item, "comicBookCollection_Series", None)
                    
                    setattr(item, "comicBookCollection_Series", self)
                    

    @property
    def comicBookCollection_Publisher(self):
        return self.__comicBookCollection_Publisher

    @comicBookCollection_Publisher.setter
    def comicBookCollection_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBookCollection_Publisher__comicBookCollection_Publisher", None)
        self.__comicBookCollection_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBookCollection_ComicBookCollection"):
                opp_val = getattr(old_value, "comicBookCollection_ComicBookCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBookCollection_ComicBookCollection"):
                opp_val = getattr(value, "comicBookCollection_ComicBookCollection", None)
                if opp_val is None:
                    setattr(value, "comicBookCollection_ComicBookCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comicBookCollection_ComicBookCollection:

    pass