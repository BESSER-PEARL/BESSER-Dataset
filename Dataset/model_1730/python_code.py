from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class resourceunload_Library:

    def __init__(self, name: str, resourceunload_Library: set["resourceunload_Book"] = None):
        self.name = name
        self.resourceunload_Library = resourceunload_Library if resourceunload_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def resourceunload_Library(self):
        return self.__resourceunload_Library

    @resourceunload_Library.setter
    def resourceunload_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourceunload_Library__resourceunload_Library", None)
        self.__resourceunload_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "resourceunload_Book"):
                    opp_val = getattr(item, "resourceunload_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "resourceunload_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "resourceunload_Book"):
                    opp_val = getattr(item, "resourceunload_Book", None)
                    
                    setattr(item, "resourceunload_Book", self)
                    

class resourceunload_Book:

    def __init__(self, title: str, resourceunload_Book: "resourceunload_Library" = None):
        self.title = title
        self.resourceunload_Book = resourceunload_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def resourceunload_Book(self):
        return self.__resourceunload_Book

    @resourceunload_Book.setter
    def resourceunload_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourceunload_Book__resourceunload_Book", None)
        self.__resourceunload_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceunload_Library"):
                opp_val = getattr(old_value, "resourceunload_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceunload_Library"):
                opp_val = getattr(value, "resourceunload_Library", None)
                if opp_val is None:
                    setattr(value, "resourceunload_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
