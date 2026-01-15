from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Paper_Author:

    def __init__(self, email: str, name: str, Paper_Author: "Paper_Paper" = None):
        self.email = email
        self.name = name
        self.Paper_Author = Paper_Author
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Paper_Author(self):
        return self.__Paper_Author

    @Paper_Author.setter
    def Paper_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paper_Author__Paper_Author", None)
        self.__Paper_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper_Paper2"):
                opp_val = getattr(old_value, "Paper_Paper2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper_Paper2"):
                opp_val = getattr(value, "Paper_Paper2", None)
                if opp_val is None:
                    setattr(value, "Paper_Paper2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Paper_Paper:

    def __init__(self, title: str, Paper_Paper: "Paper_Papers" = None, Paper_Paper2: set["Paper_Author"] = None):
        self.title = title
        self.Paper_Paper = Paper_Paper
        self.Paper_Paper2 = Paper_Paper2 if Paper_Paper2 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Paper_Paper(self):
        return self.__Paper_Paper

    @Paper_Paper.setter
    def Paper_Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paper_Paper__Paper_Paper", None)
        self.__Paper_Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper_Papers"):
                opp_val = getattr(old_value, "Paper_Papers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper_Papers"):
                opp_val = getattr(value, "Paper_Papers", None)
                if opp_val is None:
                    setattr(value, "Paper_Papers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Paper_Paper2(self):
        return self.__Paper_Paper2

    @Paper_Paper2.setter
    def Paper_Paper2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paper_Paper__Paper_Paper2", None)
        self.__Paper_Paper2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Paper_Author"):
                    opp_val = getattr(item, "Paper_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Paper_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Paper_Author"):
                    opp_val = getattr(item, "Paper_Author", None)
                    
                    setattr(item, "Paper_Author", self)
                    

class Paper_Papers:

    pass