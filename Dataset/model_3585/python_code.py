from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TypeA_AA(ABC):

    def __init__(self, nameA: str):
        self.nameA = nameA
        
    @property
    def nameA(self) -> str:
        return self.__nameA

    @nameA.setter
    def nameA(self, nameA: str):
        self.__nameA = nameA

class TypeA_ObjectR:

    def __init__(self, nameR: str):
        self.nameR = nameR
        
    @property
    def nameR(self) -> str:
        return self.__nameR

    @nameR.setter
    def nameR(self, nameR: str):
        self.__nameR = nameR

class TypeA_ObjectX:

    def __init__(self, nameX: str):
        self.nameX = nameX
        
    @property
    def nameX(self) -> str:
        return self.__nameX

    @nameX.setter
    def nameX(self, nameX: str):
        self.__nameX = nameX

class B:

    pass
class TypeA_C(B):

    def __init__(self, nameC: str):
        self.nameC = nameC
        
    @property
    def nameC(self) -> str:
        return self.__nameC

    @nameC.setter
    def nameC(self, nameC: str):
        self.__nameC = nameC

class ObjectR:

    pass
class TypeA_ObjectS(ObjectR):

    def __init__(self, nameS: str, ObjectR: "TypeA_ListElement"):
        self.nameS = nameS
        
    @property
    def nameS(self) -> str:
        return self.__nameS

    @nameS.setter
    def nameS(self, nameS: str):
        self.__nameS = nameS

class ObjectX:

    pass
class TypeA_ObjectY(ObjectX):

    def __init__(self, nameY: str, ObjectX: "TypeA_ListElement"):
        self.nameY = nameY
        
    @property
    def nameY(self) -> str:
        return self.__nameY

    @nameY.setter
    def nameY(self, nameY: str):
        self.__nameY = nameY

class AA:

    pass
class TypeA_D(AA):

    def __init__(self, nameD: str, AA3: "TypeA_ListElement", AA: "TypeA_ListElement"):
        self.nameD = nameD
        
    @property
    def nameD(self) -> str:
        return self.__nameD

    @nameD.setter
    def nameD(self, nameD: str):
        self.__nameD = nameD

class TypeA_B(AA):

    def __init__(self, nameB: str, AA3: "TypeA_ListElement", AA: "TypeA_ListElement"):
        self.nameB = nameB
        
    @property
    def nameB(self) -> str:
        return self.__nameB

    @nameB.setter
    def nameB(self, nameB: str):
        self.__nameB = nameB

class TypeA_ListElement:

    def __init__(self, nameListElement: str, TypeA_ListElement: set["AA"] = None, TypeA_ListElement2: "AA" = None, TypeA_ListElement5: set["ObjectX"] = None, TypeA_ListElement7: set["ObjectR"] = None):
        self.nameListElement = nameListElement
        self.TypeA_ListElement = TypeA_ListElement if TypeA_ListElement is not None else set()
        self.TypeA_ListElement2 = TypeA_ListElement2
        self.TypeA_ListElement5 = TypeA_ListElement5 if TypeA_ListElement5 is not None else set()
        self.TypeA_ListElement7 = TypeA_ListElement7 if TypeA_ListElement7 is not None else set()
        
    @property
    def nameListElement(self) -> str:
        return self.__nameListElement

    @nameListElement.setter
    def nameListElement(self, nameListElement: str):
        self.__nameListElement = nameListElement

    @property
    def TypeA_ListElement5(self):
        return self.__TypeA_ListElement5

    @TypeA_ListElement5.setter
    def TypeA_ListElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_ListElement__TypeA_ListElement5", None)
        self.__TypeA_ListElement5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectX"):
                    opp_val = getattr(item, "ObjectX", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectX", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectX"):
                    opp_val = getattr(item, "ObjectX", None)
                    
                    setattr(item, "ObjectX", self)
                    

    @property
    def TypeA_ListElement2(self):
        return self.__TypeA_ListElement2

    @TypeA_ListElement2.setter
    def TypeA_ListElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_ListElement__TypeA_ListElement2", None)
        self.__TypeA_ListElement2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AA3"):
                opp_val = getattr(old_value, "AA3", None)
                if opp_val == self:
                    setattr(old_value, "AA3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AA3"):
                opp_val = getattr(value, "AA3", None)
                setattr(value, "AA3", self)

    @property
    def TypeA_ListElement(self):
        return self.__TypeA_ListElement

    @TypeA_ListElement.setter
    def TypeA_ListElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_ListElement__TypeA_ListElement", None)
        self.__TypeA_ListElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AA"):
                    opp_val = getattr(item, "AA", None)
                    
                    if opp_val == self:
                        setattr(item, "AA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AA"):
                    opp_val = getattr(item, "AA", None)
                    
                    setattr(item, "AA", self)
                    

    @property
    def TypeA_ListElement7(self):
        return self.__TypeA_ListElement7

    @TypeA_ListElement7.setter
    def TypeA_ListElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_ListElement__TypeA_ListElement7", None)
        self.__TypeA_ListElement7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectR"):
                    opp_val = getattr(item, "ObjectR", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectR", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectR"):
                    opp_val = getattr(item, "ObjectR", None)
                    
                    setattr(item, "ObjectR", self)
                    
