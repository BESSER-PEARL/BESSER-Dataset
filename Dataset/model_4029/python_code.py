from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleClass_Attribute:

    def __init__(self, isPublic: bool, name: str, simpleClass_Attribute: "simpleClass_Class" = None, simpleClass_Attribute7: "simpleClass_Class" = None):
        self.isPublic = isPublic
        self.name = name
        self.simpleClass_Attribute = simpleClass_Attribute
        self.simpleClass_Attribute7 = simpleClass_Attribute7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def simpleClass_Attribute(self):
        return self.__simpleClass_Attribute

    @simpleClass_Attribute.setter
    def simpleClass_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Attribute__simpleClass_Attribute", None)
        self.__simpleClass_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class5"):
                opp_val = getattr(old_value, "simpleClass_Class5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class5"):
                opp_val = getattr(value, "simpleClass_Class5", None)
                if opp_val is None:
                    setattr(value, "simpleClass_Class5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleClass_Attribute7(self):
        return self.__simpleClass_Attribute7

    @simpleClass_Attribute7.setter
    def simpleClass_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Attribute__simpleClass_Attribute7", None)
        self.__simpleClass_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class8"):
                opp_val = getattr(old_value, "simpleClass_Class8", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class8"):
                opp_val = getattr(value, "simpleClass_Class8", None)
                setattr(value, "simpleClass_Class8", self)

class simpleClass_Class:

    def __init__(self, name: str, simpleClass_Class: "simpleClass_Model" = None, simpleClass_Class3: "simpleClass_Class" = None, simpleClass_Class1: set["simpleClass_Class"] = None, simpleClass_Class5: set["simpleClass_Attribute"] = None, simpleClass_Class8: "simpleClass_Attribute" = None):
        self.name = name
        self.simpleClass_Class = simpleClass_Class
        self.simpleClass_Class3 = simpleClass_Class3
        self.simpleClass_Class1 = simpleClass_Class1 if simpleClass_Class1 is not None else set()
        self.simpleClass_Class5 = simpleClass_Class5 if simpleClass_Class5 is not None else set()
        self.simpleClass_Class8 = simpleClass_Class8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleClass_Class3(self):
        return self.__simpleClass_Class3

    @simpleClass_Class3.setter
    def simpleClass_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class3", None)
        self.__simpleClass_Class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class1"):
                opp_val = getattr(old_value, "simpleClass_Class1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class1"):
                opp_val = getattr(value, "simpleClass_Class1", None)
                if opp_val is None:
                    setattr(value, "simpleClass_Class1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleClass_Class8(self):
        return self.__simpleClass_Class8

    @simpleClass_Class8.setter
    def simpleClass_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class8", None)
        self.__simpleClass_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Attribute7"):
                opp_val = getattr(old_value, "simpleClass_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Attribute7"):
                opp_val = getattr(value, "simpleClass_Attribute7", None)
                setattr(value, "simpleClass_Attribute7", self)

    @property
    def simpleClass_Class(self):
        return self.__simpleClass_Class

    @simpleClass_Class.setter
    def simpleClass_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class", None)
        self.__simpleClass_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Model"):
                opp_val = getattr(old_value, "simpleClass_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Model"):
                opp_val = getattr(value, "simpleClass_Model", None)
                if opp_val is None:
                    setattr(value, "simpleClass_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleClass_Class1(self):
        return self.__simpleClass_Class1

    @simpleClass_Class1.setter
    def simpleClass_Class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class1", None)
        self.__simpleClass_Class1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleClass_Class3"):
                    opp_val = getattr(item, "simpleClass_Class3", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleClass_Class3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleClass_Class3"):
                    opp_val = getattr(item, "simpleClass_Class3", None)
                    
                    setattr(item, "simpleClass_Class3", self)
                    

    @property
    def simpleClass_Class5(self):
        return self.__simpleClass_Class5

    @simpleClass_Class5.setter
    def simpleClass_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class5", None)
        self.__simpleClass_Class5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleClass_Attribute"):
                    opp_val = getattr(item, "simpleClass_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleClass_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleClass_Attribute"):
                    opp_val = getattr(item, "simpleClass_Attribute", None)
                    
                    setattr(item, "simpleClass_Attribute", self)
                    

class simpleClass_Model:

    pass