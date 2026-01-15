from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Attribut:

    def __init__(self, name: str, type: str, Data_Attribut: "Data_Classe" = None):
        self.name = name
        self.type = type
        self.Data_Attribut = Data_Attribut
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "Data_Classe"):
                opp_val = getattr(old_value, "Data_Classe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Classe"):
                opp_val = getattr(value, "Data_Classe", None)
                if opp_val is None:
                    setattr(value, "Data_Classe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Classe:

    def __init__(self, name: str, Data_Classe: set["Data_Attribut"] = None):
        self.name = name
        self.Data_Classe = Data_Classe if Data_Classe is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Classe(self):
        return self.__Data_Classe

    @Data_Classe.setter
    def Data_Classe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Classe__Data_Classe", None)
        self.__Data_Classe = value if value is not None else set()
        
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
                    

class Data_Model:

    pass