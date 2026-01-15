from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class samples_Book:

    def __init__(self, title: str, samples_Book: "samples_Author" = None, samples_Book2: "samples_Author" = None):
        self.title = title
        self.samples_Book = samples_Book
        self.samples_Book2 = samples_Book2
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def samples_Book(self):
        return self.__samples_Book

    @samples_Book.setter
    def samples_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samples_Book__samples_Book", None)
        self.__samples_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samples_Author"):
                opp_val = getattr(old_value, "samples_Author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samples_Author"):
                opp_val = getattr(value, "samples_Author", None)
                if opp_val is None:
                    setattr(value, "samples_Author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def samples_Book2(self):
        return self.__samples_Book2

    @samples_Book2.setter
    def samples_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samples_Book__samples_Book2", None)
        self.__samples_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samples_Author3"):
                opp_val = getattr(old_value, "samples_Author3", None)
                if opp_val == self:
                    setattr(old_value, "samples_Author3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samples_Author3"):
                opp_val = getattr(value, "samples_Author3", None)
                setattr(value, "samples_Author3", self)

class samples_Author:

    def __init__(self, name: str, samples_Author: set["samples_Book"] = None, samples_Author3: "samples_Book" = None):
        self.name = name
        self.samples_Author = samples_Author if samples_Author is not None else set()
        self.samples_Author3 = samples_Author3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def samples_Author(self):
        return self.__samples_Author

    @samples_Author.setter
    def samples_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samples_Author__samples_Author", None)
        self.__samples_Author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "samples_Book"):
                    opp_val = getattr(item, "samples_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "samples_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "samples_Book"):
                    opp_val = getattr(item, "samples_Book", None)
                    
                    setattr(item, "samples_Book", self)
                    

    @property
    def samples_Author3(self):
        return self.__samples_Author3

    @samples_Author3.setter
    def samples_Author3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_samples_Author__samples_Author3", None)
        self.__samples_Author3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samples_Book2"):
                opp_val = getattr(old_value, "samples_Book2", None)
                if opp_val == self:
                    setattr(old_value, "samples_Book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samples_Book2"):
                opp_val = getattr(value, "samples_Book2", None)
                setattr(value, "samples_Book2", self)
