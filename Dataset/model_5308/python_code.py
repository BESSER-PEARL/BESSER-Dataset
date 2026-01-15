from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeB_ElementX:

    def __init__(self, nameX: str):
        self.nameX = nameX
        
    @property
    def nameX(self) -> str:
        return self.__nameX

    @nameX.setter
    def nameX(self, nameX: str):
        self.__nameX = nameX

class TypeB_AnotherElement:

    def __init__(self, abstractBaseName: str, nameElement: str, type: str, additionalField: str):
        self.abstractBaseName = abstractBaseName
        self.nameElement = nameElement
        self.type = type
        self.additionalField = additionalField
        
    @property
    def nameElement(self) -> str:
        return self.__nameElement

    @nameElement.setter
    def nameElement(self, nameElement: str):
        self.__nameElement = nameElement

    @property
    def additionalField(self) -> str:
        return self.__additionalField

    @additionalField.setter
    def additionalField(self, additionalField: str):
        self.__additionalField = additionalField

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def abstractBaseName(self) -> str:
        return self.__abstractBaseName

    @abstractBaseName.setter
    def abstractBaseName(self, abstractBaseName: str):
        self.__abstractBaseName = abstractBaseName

class TypeB_Element:

    def __init__(self, abstractBaseName: str, nameElement: str, type: str):
        self.abstractBaseName = abstractBaseName
        self.nameElement = nameElement
        self.type = type
        
    @property
    def nameElement(self) -> str:
        return self.__nameElement

    @nameElement.setter
    def nameElement(self, nameElement: str):
        self.__nameElement = nameElement

    @property
    def abstractBaseName(self) -> str:
        return self.__abstractBaseName

    @abstractBaseName.setter
    def abstractBaseName(self, abstractBaseName: str):
        self.__abstractBaseName = abstractBaseName

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class ElementR:

    pass
class ElementX:

    pass
class Element:

    pass
class TypeB_SubElement(Element):

    def __init__(self, additionalField: str, Element: "TypeB_ListElement", Element3: "TypeB_ListElement"):
        self.additionalField = additionalField
        
    @property
    def additionalField(self) -> str:
        return self.__additionalField

    @additionalField.setter
    def additionalField(self, additionalField: str):
        self.__additionalField = additionalField

class TypeB_ListElement:

    def __init__(self, nameListElement: str, TypeB_ListElement: set["Element"] = None, TypeB_ListElement2: "Element" = None, TypeB_ListElement5: set["ElementX"] = None, TypeB_ListElement7: set["ElementR"] = None):
        self.nameListElement = nameListElement
        self.TypeB_ListElement = TypeB_ListElement if TypeB_ListElement is not None else set()
        self.TypeB_ListElement2 = TypeB_ListElement2
        self.TypeB_ListElement5 = TypeB_ListElement5 if TypeB_ListElement5 is not None else set()
        self.TypeB_ListElement7 = TypeB_ListElement7 if TypeB_ListElement7 is not None else set()
        
    @property
    def nameListElement(self) -> str:
        return self.__nameListElement

    @nameListElement.setter
    def nameListElement(self, nameListElement: str):
        self.__nameListElement = nameListElement

    @property
    def TypeB_ListElement7(self):
        return self.__TypeB_ListElement7

    @TypeB_ListElement7.setter
    def TypeB_ListElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_ListElement__TypeB_ListElement7", None)
        self.__TypeB_ListElement7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementR"):
                    opp_val = getattr(item, "ElementR", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementR", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementR"):
                    opp_val = getattr(item, "ElementR", None)
                    
                    setattr(item, "ElementR", self)
                    

    @property
    def TypeB_ListElement5(self):
        return self.__TypeB_ListElement5

    @TypeB_ListElement5.setter
    def TypeB_ListElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_ListElement__TypeB_ListElement5", None)
        self.__TypeB_ListElement5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementX"):
                    opp_val = getattr(item, "ElementX", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementX", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementX"):
                    opp_val = getattr(item, "ElementX", None)
                    
                    setattr(item, "ElementX", self)
                    

    @property
    def TypeB_ListElement2(self):
        return self.__TypeB_ListElement2

    @TypeB_ListElement2.setter
    def TypeB_ListElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_ListElement__TypeB_ListElement2", None)
        self.__TypeB_ListElement2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element3"):
                opp_val = getattr(old_value, "Element3", None)
                if opp_val == self:
                    setattr(old_value, "Element3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element3"):
                opp_val = getattr(value, "Element3", None)
                setattr(value, "Element3", self)

    @property
    def TypeB_ListElement(self):
        return self.__TypeB_ListElement

    @TypeB_ListElement.setter
    def TypeB_ListElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_ListElement__TypeB_ListElement", None)
        self.__TypeB_ListElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class TypeB_ElementS(ElementR):

    def __init__(self, nameS: str, ElementR: "TypeB_ListElement"):
        self.nameS = nameS
        
    @property
    def nameS(self) -> str:
        return self.__nameS

    @nameS.setter
    def nameS(self, nameS: str):
        self.__nameS = nameS

class TypeB_ElementR:

    def __init__(self, nameR: str):
        self.nameR = nameR
        
    @property
    def nameR(self) -> str:
        return self.__nameR

    @nameR.setter
    def nameR(self, nameR: str):
        self.__nameR = nameR

class TypeB_ElementY(ElementX):

    def __init__(self, nameY: str, ElementX: "TypeB_ListElement"):
        self.nameY = nameY
        
    @property
    def nameY(self) -> str:
        return self.__nameY

    @nameY.setter
    def nameY(self, nameY: str):
        self.__nameY = nameY
