from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ClassC:

    def __init__(self, attC1: int, attC2: bool, classB3: "ClassB" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.classB3 = classB3
        
        pass
    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def classB3(self):
        return self.__classB3
    @classB3.setter
    def classB3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassC__classB3", None)
        self.__classB3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classC2"):
                opp_val = getattr(old_value, "classC2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classC2"):
                opp_val = getattr(value, "classC2", None)
                if opp_val is None:
                    setattr(value, "classC2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ClassB:

    def __init__(self, attribute: int, classA1: "ClassA" = None, classC2: set["ClassC"] = None):
        self.attribute = attribute
        self.classA1 = classA1
        self.classC2 = classC2 if classC2 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: int):
        self.__attribute = attribute

    @property
    def classC2(self):
        return self.__classC2
    @classC2.setter
    def classC2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassB__classC2", None)
        self.__classC2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classB3"):
                    opp_val = getattr(item, "classB3", None)
                    
                    if opp_val == self:
                        setattr(item, "classB3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classB3"):
                    opp_val = getattr(item, "classB3", None)
                    
                    setattr(item, "classB3", self)
                    

    @property
    def classA1(self):
        return self.__classA1
    @classA1.setter
    def classA1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassB__classA1", None)
        self.__classA1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classB0"):
                opp_val = getattr(old_value, "classB0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classB0"):
                opp_val = getattr(value, "classB0", None)
                if opp_val is None:
                    setattr(value, "classB0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ClassA:

    def __init__(self, attA: str, classB0: set["ClassB"] = None):
        self.attA = attA
        self.classB0 = classB0 if classB0 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def classB0(self):
        return self.__classB0
    @classB0.setter
    def classB0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassA__classB0", None)
        self.__classB0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classA1"):
                    opp_val = getattr(item, "classA1", None)
                    
                    if opp_val == self:
                        setattr(item, "classA1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classA1"):
                    opp_val = getattr(item, "classA1", None)
                    
                    setattr(item, "classA1", self)
                    

