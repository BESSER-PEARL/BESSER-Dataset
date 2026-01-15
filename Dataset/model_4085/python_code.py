from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleUML_UMLAttribute:

    def __init__(self, umlName: str, simpleUML_UMLAttribute: "simpleUML_SimpleClass" = None):
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
            if hasattr(old_value, "simpleUML_SimpleClass7"):
                opp_val = getattr(old_value, "simpleUML_SimpleClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_SimpleClass7"):
                opp_val = getattr(value, "simpleUML_SimpleClass7", None)
                if opp_val is None:
                    setattr(value, "simpleUML_SimpleClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleUML_Generalization:

    pass
class simpleUML_SimpleClass:

    def __init__(self, simpleName: str, simpleUML_SimpleClass: "simpleUML_Model" = None, simpleUML_SimpleClass3: "simpleUML_SimpleClass" = None, simpleUML_SimpleClass1: set["simpleUML_SimpleClass"] = None, simpleUML_SimpleClass5: set["simpleUML_Generalization"] = None, simpleUML_SimpleClass7: set["simpleUML_UMLAttribute"] = None, simpleUML_SimpleClass10: "simpleUML_Generalization" = None):
        self.simpleName = simpleName
        self.simpleUML_SimpleClass = simpleUML_SimpleClass
        self.simpleUML_SimpleClass3 = simpleUML_SimpleClass3
        self.simpleUML_SimpleClass1 = simpleUML_SimpleClass1 if simpleUML_SimpleClass1 is not None else set()
        self.simpleUML_SimpleClass5 = simpleUML_SimpleClass5 if simpleUML_SimpleClass5 is not None else set()
        self.simpleUML_SimpleClass7 = simpleUML_SimpleClass7 if simpleUML_SimpleClass7 is not None else set()
        self.simpleUML_SimpleClass10 = simpleUML_SimpleClass10
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

    @property
    def simpleUML_SimpleClass(self):
        return self.__simpleUML_SimpleClass

    @simpleUML_SimpleClass.setter
    def simpleUML_SimpleClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_SimpleClass__simpleUML_SimpleClass", None)
        self.__simpleUML_SimpleClass = value
        
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
    def simpleUML_SimpleClass5(self):
        return self.__simpleUML_SimpleClass5

    @simpleUML_SimpleClass5.setter
    def simpleUML_SimpleClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_SimpleClass__simpleUML_SimpleClass5", None)
        self.__simpleUML_SimpleClass5 = value if value is not None else set()
        
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
    def simpleUML_SimpleClass10(self):
        return self.__simpleUML_SimpleClass10

    @simpleUML_SimpleClass10.setter
    def simpleUML_SimpleClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_SimpleClass__simpleUML_SimpleClass10", None)
        self.__simpleUML_SimpleClass10 = value
        
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
    def simpleUML_SimpleClass1(self):
        return self.__simpleUML_SimpleClass1

    @simpleUML_SimpleClass1.setter
    def simpleUML_SimpleClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_SimpleClass__simpleUML_SimpleClass1", None)
        self.__simpleUML_SimpleClass1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleUML_SimpleClass3"):
                    opp_val = getattr(item, "simpleUML_SimpleClass3", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleUML_SimpleClass3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleUML_SimpleClass3"):
                    opp_val = getattr(item, "simpleUML_SimpleClass3", None)
                    
                    setattr(item, "simpleUML_SimpleClass3", self)
                    

    @property
    def simpleUML_SimpleClass3(self):
        return self.__simpleUML_SimpleClass3

    @simpleUML_SimpleClass3.setter
    def simpleUML_SimpleClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_SimpleClass__simpleUML_SimpleClass3", None)
        self.__simpleUML_SimpleClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_SimpleClass1"):
                opp_val = getattr(old_value, "simpleUML_SimpleClass1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_SimpleClass1"):
                opp_val = getattr(value, "simpleUML_SimpleClass1", None)
                if opp_val is None:
                    setattr(value, "simpleUML_SimpleClass1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleUML_SimpleClass7(self):
        return self.__simpleUML_SimpleClass7

    @simpleUML_SimpleClass7.setter
    def simpleUML_SimpleClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_SimpleClass__simpleUML_SimpleClass7", None)
        self.__simpleUML_SimpleClass7 = value if value is not None else set()
        
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
                    

class simpleUML_Model:

    pass