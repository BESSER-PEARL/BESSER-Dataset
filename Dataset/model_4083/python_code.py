from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleUML_UMLAttribute:

    def __init__(self, umlName: str, simpleUML_UMLAttribute: "simpleUML_UMLClass" = None):
        self.umlName = umlName
        self.simpleUML_UMLAttribute = simpleUML_UMLAttribute
        
    @property
    def umlName(self) -> str:
        return self.__umlName

    @umlName.setter
    def umlName(self, umlName: str):
        self.__umlName = umlName

    @property
    def simpleUML_UMLAttribute(self):
        return self.__simpleUML_UMLAttribute

    @simpleUML_UMLAttribute.setter
    def simpleUML_UMLAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLAttribute__simpleUML_UMLAttribute", None)
        self.__simpleUML_UMLAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_UMLClass7"):
                opp_val = getattr(old_value, "simpleUML_UMLClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_UMLClass7"):
                opp_val = getattr(value, "simpleUML_UMLClass7", None)
                if opp_val is None:
                    setattr(value, "simpleUML_UMLClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleUML_Generalization:

    pass
class simpleUML_UMLClass:

    def __init__(self, umlName: str, simpleUML_UMLClass: "simpleUML_Model" = None, simpleUML_UMLClass3: "simpleUML_UMLClass" = None, simpleUML_UMLClass1: set["simpleUML_UMLClass"] = None, simpleUML_UMLClass5: set["simpleUML_Generalization"] = None, simpleUML_UMLClass7: set["simpleUML_UMLAttribute"] = None, simpleUML_UMLClass10: "simpleUML_Generalization" = None):
        self.umlName = umlName
        self.simpleUML_UMLClass = simpleUML_UMLClass
        self.simpleUML_UMLClass3 = simpleUML_UMLClass3
        self.simpleUML_UMLClass1 = simpleUML_UMLClass1 if simpleUML_UMLClass1 is not None else set()
        self.simpleUML_UMLClass5 = simpleUML_UMLClass5 if simpleUML_UMLClass5 is not None else set()
        self.simpleUML_UMLClass7 = simpleUML_UMLClass7 if simpleUML_UMLClass7 is not None else set()
        self.simpleUML_UMLClass10 = simpleUML_UMLClass10
        
    @property
    def umlName(self) -> str:
        return self.__umlName

    @umlName.setter
    def umlName(self, umlName: str):
        self.__umlName = umlName

    @property
    def simpleUML_UMLClass10(self):
        return self.__simpleUML_UMLClass10

    @simpleUML_UMLClass10.setter
    def simpleUML_UMLClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass10", None)
        self.__simpleUML_UMLClass10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_Generalization9"):
                opp_val = getattr(old_value, "simpleUML_Generalization9", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_Generalization9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_Generalization9"):
                opp_val = getattr(value, "simpleUML_Generalization9", None)
                setattr(value, "simpleUML_Generalization9", self)

    @property
    def simpleUML_UMLClass7(self):
        return self.__simpleUML_UMLClass7

    @simpleUML_UMLClass7.setter
    def simpleUML_UMLClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass7", None)
        self.__simpleUML_UMLClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleUML_UMLAttribute"):
                    opp_val = getattr(item, "simpleUML_UMLAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleUML_UMLAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleUML_UMLAttribute"):
                    opp_val = getattr(item, "simpleUML_UMLAttribute", None)
                    
                    setattr(item, "simpleUML_UMLAttribute", self)
                    

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
    def simpleUML_UMLClass1(self):
        return self.__simpleUML_UMLClass1

    @simpleUML_UMLClass1.setter
    def simpleUML_UMLClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass1", None)
        self.__simpleUML_UMLClass1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleUML_UMLClass3"):
                    opp_val = getattr(item, "simpleUML_UMLClass3", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleUML_UMLClass3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleUML_UMLClass3"):
                    opp_val = getattr(item, "simpleUML_UMLClass3", None)
                    
                    setattr(item, "simpleUML_UMLClass3", self)
                    

    @property
    def simpleUML_UMLClass3(self):
        return self.__simpleUML_UMLClass3

    @simpleUML_UMLClass3.setter
    def simpleUML_UMLClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass3", None)
        self.__simpleUML_UMLClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_UMLClass1"):
                opp_val = getattr(old_value, "simpleUML_UMLClass1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_UMLClass1"):
                opp_val = getattr(value, "simpleUML_UMLClass1", None)
                if opp_val is None:
                    setattr(value, "simpleUML_UMLClass1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleUML_UMLClass5(self):
        return self.__simpleUML_UMLClass5

    @simpleUML_UMLClass5.setter
    def simpleUML_UMLClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_UMLClass__simpleUML_UMLClass5", None)
        self.__simpleUML_UMLClass5 = value if value is not None else set()
        
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
                    

class simpleUML_Model:

    pass