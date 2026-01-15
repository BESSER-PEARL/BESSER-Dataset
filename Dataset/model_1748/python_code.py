from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Author:

    def __init__(self, firstName: str, lastName: str, model_Author: "model_Book" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.model_Author = model_Author
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def model_Author(self):
        return self.__model_Author

    @model_Author.setter
    def model_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Author__model_Author", None)
        self.__model_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Book2"):
                opp_val = getattr(old_value, "model_Book2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Book2"):
                opp_val = getattr(value, "model_Book2", None)
                if opp_val is None:
                    setattr(value, "model_Book2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Book:

    def __init__(self, title: str, model_Book: "model_Library" = None, model_Book2: set["model_Author"] = None):
        self.title = title
        self.model_Book = model_Book
        self.model_Book2 = model_Book2 if model_Book2 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def model_Book(self):
        return self.__model_Book

    @model_Book.setter
    def model_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book", None)
        self.__model_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library"):
                opp_val = getattr(old_value, "model_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library"):
                opp_val = getattr(value, "model_Library", None)
                if opp_val is None:
                    setattr(value, "model_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book2(self):
        return self.__model_Book2

    @model_Book2.setter
    def model_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book2", None)
        self.__model_Book2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Author"):
                    opp_val = getattr(item, "model_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Author"):
                    opp_val = getattr(item, "model_Author", None)
                    
                    setattr(item, "model_Author", self)
                    

class model_Library:

    pass