from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class features_Feature:

    def __init__(self, nome: str, mandatory: bool, features_Feature: "features_Root" = None, features_Feature3: "features_Feature" = None, features_Feature1: set["features_Feature"] = None):
        self.nome = nome
        self.mandatory = mandatory
        self.features_Feature = features_Feature
        self.features_Feature3 = features_Feature3
        self.features_Feature1 = features_Feature1 if features_Feature1 is not None else set()
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def features_Feature3(self):
        return self.__features_Feature3

    @features_Feature3.setter
    def features_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature3", None)
        self.__features_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature1"):
                opp_val = getattr(old_value, "features_Feature1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature1"):
                opp_val = getattr(value, "features_Feature1", None)
                if opp_val is None:
                    setattr(value, "features_Feature1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_Feature(self):
        return self.__features_Feature

    @features_Feature.setter
    def features_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature", None)
        self.__features_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Root"):
                opp_val = getattr(old_value, "features_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Root"):
                opp_val = getattr(value, "features_Root", None)
                if opp_val is None:
                    setattr(value, "features_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_Feature1(self):
        return self.__features_Feature1

    @features_Feature1.setter
    def features_Feature1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature1", None)
        self.__features_Feature1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "features_Feature3"):
                    opp_val = getattr(item, "features_Feature3", None)
                    
                    if opp_val == self:
                        setattr(item, "features_Feature3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "features_Feature3"):
                    opp_val = getattr(item, "features_Feature3", None)
                    
                    setattr(item, "features_Feature3", self)
                    

class features_Root:

    pass