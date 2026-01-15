from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Model:

    pass
class Data_Methode:

    def __init__(self, nom: str, typeRetour: str, Data_Methode: "Data_Classe" = None, Data_Methode4: set["Data_Attribut"] = None):
        self.nom = nom
        self.typeRetour = typeRetour
        self.Data_Methode = Data_Methode
        self.Data_Methode4 = Data_Methode4 if Data_Methode4 is not None else set()
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def typeRetour(self) -> str:
        return self.__typeRetour

    @typeRetour.setter
    def typeRetour(self, typeRetour: str):
        self.__typeRetour = typeRetour

    @property
    def Data_Methode4(self):
        return self.__Data_Methode4

    @Data_Methode4.setter
    def Data_Methode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Methode__Data_Methode4", None)
        self.__Data_Methode4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Attribut5"):
                    opp_val = getattr(item, "Data_Attribut5", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Attribut5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Attribut5"):
                    opp_val = getattr(item, "Data_Attribut5", None)
                    
                    setattr(item, "Data_Attribut5", self)
                    

    @property
    def Data_Methode(self):
        return self.__Data_Methode

    @Data_Methode.setter
    def Data_Methode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Methode__Data_Methode", None)
        self.__Data_Methode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Classe2"):
                opp_val = getattr(old_value, "Data_Classe2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Classe2"):
                opp_val = getattr(value, "Data_Classe2", None)
                if opp_val is None:
                    setattr(value, "Data_Classe2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Attribut:

    def __init__(self, nom: str, type: str, Data_Attribut: "Data_Classe" = None, Data_Attribut5: "Data_Methode" = None):
        self.nom = nom
        self.type = type
        self.Data_Attribut = Data_Attribut
        self.Data_Attribut5 = Data_Attribut5
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

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

    @property
    def Data_Attribut5(self):
        return self.__Data_Attribut5

    @Data_Attribut5.setter
    def Data_Attribut5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribut__Data_Attribut5", None)
        self.__Data_Attribut5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Methode4"):
                opp_val = getattr(old_value, "Data_Methode4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Methode4"):
                opp_val = getattr(value, "Data_Methode4", None)
                if opp_val is None:
                    setattr(value, "Data_Methode4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Classe:

    def __init__(self, nom: str, Data_Classe: set["Data_Attribut"] = None, Data_Classe2: set["Data_Methode"] = None, Data_Classe7: "Data_Model" = None):
        self.nom = nom
        self.Data_Classe = Data_Classe if Data_Classe is not None else set()
        self.Data_Classe2 = Data_Classe2 if Data_Classe2 is not None else set()
        self.Data_Classe7 = Data_Classe7
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def Data_Classe2(self):
        return self.__Data_Classe2

    @Data_Classe2.setter
    def Data_Classe2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Classe__Data_Classe2", None)
        self.__Data_Classe2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Methode"):
                    opp_val = getattr(item, "Data_Methode", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Methode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Methode"):
                    opp_val = getattr(item, "Data_Methode", None)
                    
                    setattr(item, "Data_Methode", self)
                    

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
                    

    @property
    def Data_Classe7(self):
        return self.__Data_Classe7

    @Data_Classe7.setter
    def Data_Classe7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Classe__Data_Classe7", None)
        self.__Data_Classe7 = value
        
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
