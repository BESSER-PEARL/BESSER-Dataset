from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleUML_Generalization:

    pass
class simpleUML_UMLClass:

    def __init__(self, umlName: str, simpleUML_UMLClass: "simpleUML_Model" = None, simpleUML_UMLClass2: set["simpleUML_Generalization"] = None, simpleUML_UMLClass5: "simpleUML_Generalization" = None):
        self.umlName = umlName
        self.simpleUML_UMLClass = simpleUML_UMLClass
        self.simpleUML_UMLClass2 = simpleUML_UMLClass2 if simpleUML_UMLClass2 is not None else set()
        self.simpleUML_UMLClass5 = simpleUML_UMLClass5
        
    @property
    def umlName(self) -> str:
        return self.__umlName

    @umlName.setter
    def umlName(self, umlName: str):
        self.__umlName = umlName

    @property
    def simpleUML_UMLClass2(self):
        return self.__simpleUML_UMLClass2

    @simpleUML_UMLClass2.setter
    def simpleUML_UMLClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass2", None)
        self.__simpleUML_UMLClass2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleUML_Generalization"):
                    opp_val = getattr(item, "simpleUML_Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleUML_Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleUML_Generalization"):
                    opp_val = getattr(item, "simpleUML_Generalization", None)
                    
                    setattr(item, "simpleUML_Generalization", self)
                    

    @property
    def simpleUML_UMLClass(self):
        return self.__simpleUML_UMLClass

    @simpleUML_UMLClass.setter
    def simpleUML_UMLClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass", None)
        self.__simpleUML_UMLClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_Model"):
                opp_val = getattr(old_value, "simpleUML_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_Model"):
                opp_val = getattr(value, "simpleUML_Model", None)
                if opp_val is None:
                    setattr(value, "simpleUML_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleUML_UMLClass5(self):
        return self.__simpleUML_UMLClass5

    @simpleUML_UMLClass5.setter
    def simpleUML_UMLClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass5", None)
        self.__simpleUML_UMLClass5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_Generalization4"):
                opp_val = getattr(old_value, "simpleUML_Generalization4", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_Generalization4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_Generalization4"):
                opp_val = getattr(value, "simpleUML_Generalization4", None)
                setattr(value, "simpleUML_Generalization4", self)

class simpleUML_Model:

    pass