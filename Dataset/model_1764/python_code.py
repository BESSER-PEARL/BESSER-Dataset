from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class writers_Book:

    pass
class writers_Writer:

    def __init__(self, name: str, writers_Writer: "writers_Catalog" = None, authors: set["writers_Book"] = None):
        self.name = name
        self.writers_Writer = writers_Writer
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
        old_value = getattr(self, f"_writers_Writer__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "books.ecoreBook"):
                    opp_val = getattr(item, "books.ecoreBook", None)
                    
                    if opp_val == self:
                        setattr(item, "books.ecoreBook", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "books.ecoreBook"):
                    opp_val = getattr(item, "books.ecoreBook", None)
                    
                    setattr(item, "books.ecoreBook", self)
                    

    @property
    def writers_Writer(self):
        return self.__writers_Writer

    @writers_Writer.setter
    def writers_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_writers_Writer__writers_Writer", None)
        self.__writers_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers_Catalog"):
                opp_val = getattr(old_value, "writers_Catalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers_Catalog"):
                opp_val = getattr(value, "writers_Catalog", None)
                if opp_val is None:
                    setattr(value, "writers_Catalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class writers_Catalog:

    pass