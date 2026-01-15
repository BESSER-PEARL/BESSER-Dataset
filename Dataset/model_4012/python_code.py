from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Model:

    def __init__(self, Name: str, Data_Model: set["Data_Class"] = None):
        self.Name = Name
        self.Data_Model = Data_Model if Data_Model is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Data_Model(self):
        return self.__Data_Model

    @Data_Model.setter
    def Data_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Model__Data_Model", None)
        self.__Data_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Class2"):
                    opp_val = getattr(item, "Data_Class2", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Class2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Class2"):
                    opp_val = getattr(item, "Data_Class2", None)
                    
                    setattr(item, "Data_Class2", self)
                    

class Data_Attribut:

    def __init__(self, Name: str, Type: str, Visibility: str, Static: bool, Data_Attribut: "Data_Class" = None):
        self.Name = Name
        self.Type = Type
        self.Visibility = Visibility
        self.Static = Static
        self.Data_Attribut = Data_Attribut
        
    @property
    def Static(self) -> bool:
        return self.__Static

    @Static.setter
    def Static(self, Static: bool):
        self.__Static = Static

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Visibility(self) -> str:
        return self.__Visibility

    @Visibility.setter
    def Visibility(self, Visibility: str):
        self.__Visibility = Visibility

    @property
    def Data_Attribut(self):
        return self.__Data_Attribut

    @Data_Attribut.setter
    def Data_Attribut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribut__Data_Attribut", None)
        self.__Data_Attribut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Class"):
                opp_val = getattr(old_value, "Data_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Class"):
                opp_val = getattr(value, "Data_Class", None)
                if opp_val is None:
                    setattr(value, "Data_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Class:

    def __init__(self, Name: str, Data_Class: set["Data_Attribut"] = None, Data_Class2: "Data_Model" = None):
        self.Name = Name
        self.Data_Class = Data_Class if Data_Class is not None else set()
        self.Data_Class2 = Data_Class2
        
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
        self.__Data_Class2 = value
        
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

    @property
    def Data_Class(self):
        return self.__Data_Class

    @Data_Class.setter
    def Data_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Class__Data_Class", None)
        self.__Data_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Attribut"):
                    opp_val = getattr(item, "Data_Attribut", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Attribut", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Attribut"):
                    opp_val = getattr(item, "Data_Attribut", None)
                    
                    setattr(item, "Data_Attribut", self)
                    
