from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class example_Folder:

    def __init__(self, name: str, example_Folder: "example_Folder" = None, example_Folder0: "example_Folder" = None):
        self.name = name
        self.example_Folder = example_Folder
        self.example_Folder0 = example_Folder0
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def example_Folder0(self):
        return self.__example_Folder0

    @example_Folder0.setter
    def example_Folder0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_example_Folder__example_Folder0", None)
        self.__example_Folder0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "example_Folder"):
                opp_val = getattr(old_value, "example_Folder", None)
                if opp_val == self:
                    setattr(old_value, "example_Folder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "example_Folder"):
                opp_val = getattr(value, "example_Folder", None)
                setattr(value, "example_Folder", self)

    @property
    def example_Folder(self):
        return self.__example_Folder

    @example_Folder.setter
    def example_Folder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_example_Folder__example_Folder", None)
        self.__example_Folder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "example_Folder0"):
                opp_val = getattr(old_value, "example_Folder0", None)
                if opp_val == self:
                    setattr(old_value, "example_Folder0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "example_Folder0"):
                opp_val = getattr(value, "example_Folder0", None)
                setattr(value, "example_Folder0", self)
