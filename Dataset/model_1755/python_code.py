from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class extralazy_Book:

    def __init__(self, title: str, subTitles: str, extralazy_Book: set["extralazy_Writer"] = None):
        self.title = title
        self.subTitles = subTitles
        self.extralazy_Book = extralazy_Book if extralazy_Book is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def subTitles(self) -> str:
        return self.__subTitles

    @subTitles.setter
    def subTitles(self, subTitles: str):
        self.__subTitles = subTitles

    @property
    def extralazy_Book(self):
        return self.__extralazy_Book

    @extralazy_Book.setter
    def extralazy_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extralazy_Book__extralazy_Book", None)
        self.__extralazy_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extralazy_Writer"):
                    opp_val = getattr(item, "extralazy_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "extralazy_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extralazy_Writer"):
                    opp_val = getattr(item, "extralazy_Writer", None)
                    
                    setattr(item, "extralazy_Writer", self)
                    

class extralazy_Writer:

    def __init__(self, name: str, extralazy_Writer: "extralazy_Book" = None):
        self.name = name
        self.extralazy_Writer = extralazy_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extralazy_Writer(self):
        return self.__extralazy_Writer

    @extralazy_Writer.setter
    def extralazy_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extralazy_Writer__extralazy_Writer", None)
        self.__extralazy_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extralazy_Book"):
                opp_val = getattr(old_value, "extralazy_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extralazy_Book"):
                opp_val = getattr(value, "extralazy_Book", None)
                if opp_val is None:
                    setattr(value, "extralazy_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
