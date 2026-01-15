from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Modele:

    pass
class Data_DeclarationType:

    def __init__(self, nom: str):
        self.nom = nom
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

class Data_Attribut:

    def __init__(self, estTableau: bool, typeStr: str, nom: str, Data_Attribut: "Data_Classe" = None, Data_Attribut2: "Data_Classe" = None):
        self.estTableau = estTableau
        self.typeStr = typeStr
        self.nom = nom
        self.Data_Attribut = Data_Attribut
        self.Data_Attribut2 = Data_Attribut2
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def estTableau(self) -> bool:
        return self.__estTableau

    @estTableau.setter
    def estTableau(self, estTableau: bool):
        self.__estTableau = estTableau

    @property
    def typeStr(self) -> str:
        return self.__typeStr

    @typeStr.setter
    def typeStr(self, typeStr: str):
        self.__typeStr = typeStr

    @property
    def Data_Attribut2(self):
        return self.__Data_Attribut2

    @Data_Attribut2.setter
    def Data_Attribut2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribut__Data_Attribut2", None)
        self.__Data_Attribut2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Classe3"):
                opp_val = getattr(old_value, "Data_Classe3", None)
                if opp_val == self:
                    setattr(old_value, "Data_Classe3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Classe3"):
                opp_val = getattr(value, "Data_Classe3", None)
                setattr(value, "Data_Classe3", self)

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

class DeclarationType:

    pass
class Data_Classe(DeclarationType):

    pass