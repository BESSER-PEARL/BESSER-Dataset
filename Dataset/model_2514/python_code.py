from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MyEnum(Enum):
    ZERO = "ZERO"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"


############################################
# Definition of Classes
############################################

class model6_MyEnumListUnsettable:

    def __init__(self, myEnum: str):
        self.myEnum = myEnum
        
    @property
    def myEnum(self) -> str:
        return self.__myEnum

    @myEnum.setter
    def myEnum(self, myEnum: str):
        self.__myEnum = myEnum

class model6_MyEnumList:

    def __init__(self, myEnum: str):
        self.myEnum = myEnum
        
    @property
    def myEnum(self) -> str:
        return self.__myEnum

    @myEnum.setter
    def myEnum(self, myEnum: str):
        self.__myEnum = myEnum

class model6_G:

    def __init__(self, dummy: str, model6_G: "model6_BaseObject" = None, model6_G45: set["model6_BaseObject"] = None):
        self.dummy = dummy
        self.model6_G = model6_G
        self.model6_G45 = model6_G45 if model6_G45 is not None else set()
        
    @property
    def dummy(self) -> str:
        return self.__dummy

    @dummy.setter
    def dummy(self, dummy: str):
        self.__dummy = dummy

    @property
    def model6_G(self):
        return self.__model6_G

    @model6_G.setter
    def model6_G(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_G__model6_G", None)
        self.__model6_G = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_BaseObject43"):
                opp_val = getattr(old_value, "model6_BaseObject43", None)
                if opp_val == self:
                    setattr(old_value, "model6_BaseObject43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_BaseObject43"):
                opp_val = getattr(value, "model6_BaseObject43", None)
                setattr(value, "model6_BaseObject43", self)

    @property
    def model6_G45(self):
        return self.__model6_G45

    @model6_G45.setter
    def model6_G45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_G__model6_G45", None)
        self.__model6_G45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model6_BaseObject46"):
                    opp_val = getattr(item, "model6_BaseObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "model6_BaseObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model6_BaseObject46"):
                    opp_val = getattr(item, "model6_BaseObject46", None)
                    
                    setattr(item, "model6_BaseObject46", self)
                    

    def isAttributeModified(self) -> bool:
        # TODO: Implement isAttributeModified method
        pass

    def isReferenceModified(self) -> bool:
        # TODO: Implement isReferenceModified method
        pass

    def isListModified(self) -> bool:
        # TODO: Implement isListModified method
        pass

class model6_F:

    pass
class model6_E:

    pass
class model6_EObject:

    pass
class model6_C:

    pass
class model6_B:

    pass
class model6_D:

    pass
class model6_A:

    pass
class model6_PropertiesMapEntryValue:

    def __init__(self, label: str, model6_PropertiesMapEntryValue: "model6_PropertiesMapEntry" = None):
        self.label = label
        self.model6_PropertiesMapEntryValue = model6_PropertiesMapEntryValue
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def model6_PropertiesMapEntryValue(self):
        return self.__model6_PropertiesMapEntryValue

    @model6_PropertiesMapEntryValue.setter
    def model6_PropertiesMapEntryValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_PropertiesMapEntryValue__model6_PropertiesMapEntryValue", None)
        self.__model6_PropertiesMapEntryValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_PropertiesMapEntry30"):
                opp_val = getattr(old_value, "model6_PropertiesMapEntry30", None)
                if opp_val == self:
                    setattr(old_value, "model6_PropertiesMapEntry30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_PropertiesMapEntry30"):
                opp_val = getattr(value, "model6_PropertiesMapEntry30", None)
                setattr(value, "model6_PropertiesMapEntry30", self)

class model6_PropertiesMapEntry:

    def __init__(self, key: str, model6_PropertiesMapEntry: "model6_PropertiesMap" = None, model6_PropertiesMapEntry28: "model6_PropertiesMap" = None, model6_PropertiesMapEntry30: "model6_PropertiesMapEntryValue" = None):
        self.key = key
        self.model6_PropertiesMapEntry = model6_PropertiesMapEntry
        self.model6_PropertiesMapEntry28 = model6_PropertiesMapEntry28
        self.model6_PropertiesMapEntry30 = model6_PropertiesMapEntry30
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model6_PropertiesMapEntry(self):
        return self.__model6_PropertiesMapEntry

    @model6_PropertiesMapEntry.setter
    def model6_PropertiesMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_PropertiesMapEntry__model6_PropertiesMapEntry", None)
        self.__model6_PropertiesMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_PropertiesMap"):
                opp_val = getattr(old_value, "model6_PropertiesMap", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_PropertiesMap"):
                opp_val = getattr(value, "model6_PropertiesMap", None)
                if opp_val is None:
                    setattr(value, "model6_PropertiesMap", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_PropertiesMapEntry30(self):
        return self.__model6_PropertiesMapEntry30

    @model6_PropertiesMapEntry30.setter
    def model6_PropertiesMapEntry30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_PropertiesMapEntry__model6_PropertiesMapEntry30", None)
        self.__model6_PropertiesMapEntry30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_PropertiesMapEntryValue"):
                opp_val = getattr(old_value, "model6_PropertiesMapEntryValue", None)
                if opp_val == self:
                    setattr(old_value, "model6_PropertiesMapEntryValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_PropertiesMapEntryValue"):
                opp_val = getattr(value, "model6_PropertiesMapEntryValue", None)
                setattr(value, "model6_PropertiesMapEntryValue", self)

    @property
    def model6_PropertiesMapEntry28(self):
        return self.__model6_PropertiesMapEntry28

    @model6_PropertiesMapEntry28.setter
    def model6_PropertiesMapEntry28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_PropertiesMapEntry__model6_PropertiesMapEntry28", None)
        self.__model6_PropertiesMapEntry28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_PropertiesMap27"):
                opp_val = getattr(old_value, "model6_PropertiesMap27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_PropertiesMap27"):
                opp_val = getattr(value, "model6_PropertiesMap27", None)
                if opp_val is None:
                    setattr(value, "model6_PropertiesMap27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model6_PropertiesMap:

    def __init__(self, label: str, model6_PropertiesMap: set["model6_PropertiesMapEntry"] = None, model6_PropertiesMap27: set["model6_PropertiesMapEntry"] = None):
        self.label = label
        self.model6_PropertiesMap = model6_PropertiesMap if model6_PropertiesMap is not None else set()
        self.model6_PropertiesMap27 = model6_PropertiesMap27 if model6_PropertiesMap27 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def model6_PropertiesMap27(self):
        return self.__model6_PropertiesMap27

    @model6_PropertiesMap27.setter
    def model6_PropertiesMap27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_PropertiesMap__model6_PropertiesMap27", None)
        self.__model6_PropertiesMap27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model6_PropertiesMapEntry28"):
                    opp_val = getattr(item, "model6_PropertiesMapEntry28", None)
                    
                    if opp_val == self:
                        setattr(item, "model6_PropertiesMapEntry28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model6_PropertiesMapEntry28"):
                    opp_val = getattr(item, "model6_PropertiesMapEntry28", None)
                    
                    setattr(item, "model6_PropertiesMapEntry28", self)
                    

    @property
    def model6_PropertiesMap(self):
        return self.__model6_PropertiesMap

    @model6_PropertiesMap.setter
    def model6_PropertiesMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_PropertiesMap__model6_PropertiesMap", None)
        self.__model6_PropertiesMap = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model6_PropertiesMapEntry"):
                    opp_val = getattr(item, "model6_PropertiesMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "model6_PropertiesMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model6_PropertiesMapEntry"):
                    opp_val = getattr(item, "model6_PropertiesMapEntry", None)
                    
                    setattr(item, "model6_PropertiesMapEntry", self)
                    

class model6_UnorderedList:

    pass
class BaseObject:

    pass
class model6_ContainmentObject(BaseObject):

    pass
class model6_ReferenceObject(BaseObject):

    pass
class model6_BaseObject:

    def __init__(self, attributeOptional: str, attributeRequired: str, attributeList: str, model6_BaseObject: "model6_Root" = None, model6_BaseObject3: "model6_Root" = None, model6_BaseObject6: "model6_Root" = None, model6_BaseObject9: "model6_Root" = None, model6_BaseObject11: "model6_ReferenceObject" = None, model6_BaseObject14: "model6_ReferenceObject" = None, model6_BaseObject16: "model6_ContainmentObject" = None, model6_BaseObject19: "model6_ContainmentObject" = None, model6_BaseObject43: "model6_G" = None, model6_BaseObject46: "model6_G" = None):
        self.attributeOptional = attributeOptional
        self.attributeRequired = attributeRequired
        self.attributeList = attributeList
        self.model6_BaseObject = model6_BaseObject
        self.model6_BaseObject3 = model6_BaseObject3
        self.model6_BaseObject6 = model6_BaseObject6
        self.model6_BaseObject9 = model6_BaseObject9
        self.model6_BaseObject11 = model6_BaseObject11
        self.model6_BaseObject14 = model6_BaseObject14
        self.model6_BaseObject16 = model6_BaseObject16
        self.model6_BaseObject19 = model6_BaseObject19
        self.model6_BaseObject43 = model6_BaseObject43
        self.model6_BaseObject46 = model6_BaseObject46
        
    @property
    def attributeList(self) -> str:
        return self.__attributeList

    @attributeList.setter
    def attributeList(self, attributeList: str):
        self.__attributeList = attributeList

    @property
    def attributeOptional(self) -> str:
        return self.__attributeOptional

    @attributeOptional.setter
    def attributeOptional(self, attributeOptional: str):
        self.__attributeOptional = attributeOptional

    @property
    def attributeRequired(self) -> str:
        return self.__attributeRequired

    @attributeRequired.setter
    def attributeRequired(self, attributeRequired: str):
        self.__attributeRequired = attributeRequired

    @property
    def model6_BaseObject(self):
        return self.__model6_BaseObject

    @model6_BaseObject.setter
    def model6_BaseObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject", None)
        self.__model6_BaseObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_Root"):
                opp_val = getattr(old_value, "model6_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_Root"):
                opp_val = getattr(value, "model6_Root", None)
                if opp_val is None:
                    setattr(value, "model6_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject46(self):
        return self.__model6_BaseObject46

    @model6_BaseObject46.setter
    def model6_BaseObject46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject46", None)
        self.__model6_BaseObject46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_G45"):
                opp_val = getattr(old_value, "model6_G45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_G45"):
                opp_val = getattr(value, "model6_G45", None)
                if opp_val is None:
                    setattr(value, "model6_G45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject19(self):
        return self.__model6_BaseObject19

    @model6_BaseObject19.setter
    def model6_BaseObject19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject19", None)
        self.__model6_BaseObject19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_ContainmentObject18"):
                opp_val = getattr(old_value, "model6_ContainmentObject18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_ContainmentObject18"):
                opp_val = getattr(value, "model6_ContainmentObject18", None)
                if opp_val is None:
                    setattr(value, "model6_ContainmentObject18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject9(self):
        return self.__model6_BaseObject9

    @model6_BaseObject9.setter
    def model6_BaseObject9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject9", None)
        self.__model6_BaseObject9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_Root8"):
                opp_val = getattr(old_value, "model6_Root8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_Root8"):
                opp_val = getattr(value, "model6_Root8", None)
                if opp_val is None:
                    setattr(value, "model6_Root8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject3(self):
        return self.__model6_BaseObject3

    @model6_BaseObject3.setter
    def model6_BaseObject3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject3", None)
        self.__model6_BaseObject3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_Root2"):
                opp_val = getattr(old_value, "model6_Root2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_Root2"):
                opp_val = getattr(value, "model6_Root2", None)
                if opp_val is None:
                    setattr(value, "model6_Root2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject16(self):
        return self.__model6_BaseObject16

    @model6_BaseObject16.setter
    def model6_BaseObject16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject16", None)
        self.__model6_BaseObject16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_ContainmentObject"):
                opp_val = getattr(old_value, "model6_ContainmentObject", None)
                if opp_val == self:
                    setattr(old_value, "model6_ContainmentObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_ContainmentObject"):
                opp_val = getattr(value, "model6_ContainmentObject", None)
                setattr(value, "model6_ContainmentObject", self)

    @property
    def model6_BaseObject11(self):
        return self.__model6_BaseObject11

    @model6_BaseObject11.setter
    def model6_BaseObject11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject11", None)
        self.__model6_BaseObject11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_ReferenceObject"):
                opp_val = getattr(old_value, "model6_ReferenceObject", None)
                if opp_val == self:
                    setattr(old_value, "model6_ReferenceObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_ReferenceObject"):
                opp_val = getattr(value, "model6_ReferenceObject", None)
                setattr(value, "model6_ReferenceObject", self)

    @property
    def model6_BaseObject6(self):
        return self.__model6_BaseObject6

    @model6_BaseObject6.setter
    def model6_BaseObject6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject6", None)
        self.__model6_BaseObject6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_Root5"):
                opp_val = getattr(old_value, "model6_Root5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_Root5"):
                opp_val = getattr(value, "model6_Root5", None)
                if opp_val is None:
                    setattr(value, "model6_Root5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject14(self):
        return self.__model6_BaseObject14

    @model6_BaseObject14.setter
    def model6_BaseObject14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject14", None)
        self.__model6_BaseObject14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_ReferenceObject13"):
                opp_val = getattr(old_value, "model6_ReferenceObject13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_ReferenceObject13"):
                opp_val = getattr(value, "model6_ReferenceObject13", None)
                if opp_val is None:
                    setattr(value, "model6_ReferenceObject13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model6_BaseObject43(self):
        return self.__model6_BaseObject43

    @model6_BaseObject43.setter
    def model6_BaseObject43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model6_BaseObject__model6_BaseObject43", None)
        self.__model6_BaseObject43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6_G"):
                opp_val = getattr(old_value, "model6_G", None)
                if opp_val == self:
                    setattr(old_value, "model6_G", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6_G"):
                opp_val = getattr(value, "model6_G", None)
                setattr(value, "model6_G", self)

class model6_Root:

    pass