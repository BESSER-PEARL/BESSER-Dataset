from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Attribute:

    def __init__(self, Type: str, Name: str, Data_Attribute: "Data_Class" = None):
        self.Type = Type
        self.Name = Name
        self.Data_Attribute = Data_Attribute
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Data_Attribute(self):
        return self.__Data_Attribute

    @Data_Attribute.setter
    def Data_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribute__Data_Attribute", None)
        self.__Data_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Class2"):
                opp_val = getattr(old_value, "Data_Class2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Class2"):
                opp_val = getattr(value, "Data_Class2", None)
                if opp_val is None:
                    setattr(value, "Data_Class2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Class:

    def __init__(self, Name: str, Data_Class: "Data_Model" = None, Data_Class2: set["Data_Attribute"] = None):
        self.Name = Name
        self.Data_Class = Data_Class
        self.Data_Class2 = Data_Class2 if Data_Class2 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Data_Class2(self):
        return self.__Data_Class2

    @Data_Class2.setter
    def Data_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Class__Data_Class2", None)
        self.__Data_Class2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Attribute"):
                    opp_val = getattr(item, "Data_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Attribute"):
                    opp_val = getattr(item, "Data_Attribute", None)
                    
                    setattr(item, "Data_Attribute", self)
                    

    @property
    def Data_Class(self):
        return self.__Data_Class

    @Data_Class.setter
    def Data_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Class__Data_Class", None)
        self.__Data_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Model"):
                opp_val = getattr(old_value, "Data_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Model"):
                opp_val = getattr(value, "Data_Model", None)
                if opp_val is None:
                    setattr(value, "Data_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Model:

    pass