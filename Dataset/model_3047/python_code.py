from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    String = "String"
    Short = "Short"
    Integer = "Integer"
    Long = "Long"
    Float = "Float"
    Double = "Double"
    Boolean = "Boolean"
    Byte = "Byte"
    Date = "Date"
    Datetime = "Datetime"
    Timestamp = "Timestamp"
    Decimal = "Decimal"


############################################
# Definition of Classes
############################################

class soa_Operation:

    def __init__(self, name: str, soa_Operation: "soa_Service" = None, soa_Operation25: set["soa_Feature"] = None, soa_Operation28: set["soa_Feature"] = None, soa_Operation31: set["soa_Exception"] = None):
        self.name = name
        self.soa_Operation = soa_Operation
        self.soa_Operation25 = soa_Operation25 if soa_Operation25 is not None else set()
        self.soa_Operation28 = soa_Operation28 if soa_Operation28 is not None else set()
        self.soa_Operation31 = soa_Operation31 if soa_Operation31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def soa_Operation31(self):
        return self.__soa_Operation31

    @soa_Operation31.setter
    def soa_Operation31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Operation__soa_Operation31", None)
        self.__soa_Operation31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Exception32"):
                    opp_val = getattr(item, "soa_Exception32", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Exception32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Exception32"):
                    opp_val = getattr(item, "soa_Exception32", None)
                    
                    setattr(item, "soa_Exception32", self)
                    

    @property
    def soa_Operation28(self):
        return self.__soa_Operation28

    @soa_Operation28.setter
    def soa_Operation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Operation__soa_Operation28", None)
        self.__soa_Operation28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Feature29"):
                    opp_val = getattr(item, "soa_Feature29", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Feature29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Feature29"):
                    opp_val = getattr(item, "soa_Feature29", None)
                    
                    setattr(item, "soa_Feature29", self)
                    

    @property
    def soa_Operation25(self):
        return self.__soa_Operation25

    @soa_Operation25.setter
    def soa_Operation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Operation__soa_Operation25", None)
        self.__soa_Operation25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Feature26"):
                    opp_val = getattr(item, "soa_Feature26", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Feature26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Feature26"):
                    opp_val = getattr(item, "soa_Feature26", None)
                    
                    setattr(item, "soa_Feature26", self)
                    

    @property
    def soa_Operation(self):
        return self.__soa_Operation

    @soa_Operation.setter
    def soa_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Operation__soa_Operation", None)
        self.__soa_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Service23"):
                opp_val = getattr(old_value, "soa_Service23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Service23"):
                opp_val = getattr(value, "soa_Service23", None)
                if opp_val is None:
                    setattr(value, "soa_Service23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FeatureType:

    pass
class soa_EntitiesFeature(FeatureType):

    pass
class soa_FeatureType:

    pass
class soa_Exception:

    def __init__(self, name: str, msg: str, soa_Exception: "soa_Exceptions" = None, soa_Exception32: "soa_Operation" = None):
        self.name = name
        self.msg = msg
        self.soa_Exception = soa_Exception
        self.soa_Exception32 = soa_Exception32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

    @property
    def soa_Exception(self):
        return self.__soa_Exception

    @soa_Exception.setter
    def soa_Exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Exception__soa_Exception", None)
        self.__soa_Exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Exceptions21"):
                opp_val = getattr(old_value, "soa_Exceptions21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Exceptions21"):
                opp_val = getattr(value, "soa_Exceptions21", None)
                if opp_val is None:
                    setattr(value, "soa_Exceptions21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soa_Exception32(self):
        return self.__soa_Exception32

    @soa_Exception32.setter
    def soa_Exception32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Exception__soa_Exception32", None)
        self.__soa_Exception32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Operation31"):
                opp_val = getattr(old_value, "soa_Operation31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Operation31"):
                opp_val = getattr(value, "soa_Operation31", None)
                if opp_val is None:
                    setattr(value, "soa_Operation31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class soa_GenericListFeature(FeatureType):

    pass
class soa_PrimitiveFeature(FeatureType):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class soa_Service:

    def __init__(self, name: str, soa_Service: "soa_Module" = None, soa_Service23: set["soa_Operation"] = None):
        self.name = name
        self.soa_Service = soa_Service
        self.soa_Service23 = soa_Service23 if soa_Service23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def soa_Service(self):
        return self.__soa_Service

    @soa_Service.setter
    def soa_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Service__soa_Service", None)
        self.__soa_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Module8"):
                opp_val = getattr(old_value, "soa_Module8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Module8"):
                opp_val = getattr(value, "soa_Module8", None)
                if opp_val is None:
                    setattr(value, "soa_Module8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soa_Service23(self):
        return self.__soa_Service23

    @soa_Service23.setter
    def soa_Service23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Service__soa_Service23", None)
        self.__soa_Service23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Operation"):
                    opp_val = getattr(item, "soa_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Operation"):
                    opp_val = getattr(item, "soa_Operation", None)
                    
                    setattr(item, "soa_Operation", self)
                    

class soa_Exceptions:

    pass
class soa_Feature:

    def __init__(self, name: str, soa_Feature: "soa_Entity" = None, soa_Feature13: set["soa_Comment"] = None, soa_Feature15: "soa_FeatureType" = None, soa_Feature26: "soa_Operation" = None, soa_Feature29: "soa_Operation" = None):
        self.name = name
        self.soa_Feature = soa_Feature
        self.soa_Feature13 = soa_Feature13 if soa_Feature13 is not None else set()
        self.soa_Feature15 = soa_Feature15
        self.soa_Feature26 = soa_Feature26
        self.soa_Feature29 = soa_Feature29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def soa_Feature29(self):
        return self.__soa_Feature29

    @soa_Feature29.setter
    def soa_Feature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Feature__soa_Feature29", None)
        self.__soa_Feature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Operation28"):
                opp_val = getattr(old_value, "soa_Operation28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Operation28"):
                opp_val = getattr(value, "soa_Operation28", None)
                if opp_val is None:
                    setattr(value, "soa_Operation28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soa_Feature26(self):
        return self.__soa_Feature26

    @soa_Feature26.setter
    def soa_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Feature__soa_Feature26", None)
        self.__soa_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Operation25"):
                opp_val = getattr(old_value, "soa_Operation25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Operation25"):
                opp_val = getattr(value, "soa_Operation25", None)
                if opp_val is None:
                    setattr(value, "soa_Operation25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soa_Feature15(self):
        return self.__soa_Feature15

    @soa_Feature15.setter
    def soa_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Feature__soa_Feature15", None)
        self.__soa_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_FeatureType"):
                opp_val = getattr(old_value, "soa_FeatureType", None)
                if opp_val == self:
                    setattr(old_value, "soa_FeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_FeatureType"):
                opp_val = getattr(value, "soa_FeatureType", None)
                setattr(value, "soa_FeatureType", self)

    @property
    def soa_Feature(self):
        return self.__soa_Feature

    @soa_Feature.setter
    def soa_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Feature__soa_Feature", None)
        self.__soa_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Entity"):
                opp_val = getattr(old_value, "soa_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Entity"):
                opp_val = getattr(value, "soa_Entity", None)
                if opp_val is None:
                    setattr(value, "soa_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soa_Feature13(self):
        return self.__soa_Feature13

    @soa_Feature13.setter
    def soa_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Feature__soa_Feature13", None)
        self.__soa_Feature13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Comment"):
                    opp_val = getattr(item, "soa_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Comment"):
                    opp_val = getattr(item, "soa_Comment", None)
                    
                    setattr(item, "soa_Comment", self)
                    

class Entities:

    pass
class soa_Entity(Entities):

    pass
class soa_Enum(Entities):

    def __init__(self, features: str):
        self.features = features
        
    @property
    def features(self) -> str:
        return self.__features

    @features.setter
    def features(self, features: str):
        self.__features = features

class soa_Comment:

    def __init__(self, value: str, soa_Comment: "soa_Feature" = None):
        self.value = value
        self.soa_Comment = soa_Comment
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def soa_Comment(self):
        return self.__soa_Comment

    @soa_Comment.setter
    def soa_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Comment__soa_Comment", None)
        self.__soa_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Feature13"):
                opp_val = getattr(old_value, "soa_Feature13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Feature13"):
                opp_val = getattr(value, "soa_Feature13", None)
                if opp_val is None:
                    setattr(value, "soa_Feature13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class soa_Entities:

    def __init__(self, name: str, soa_Entities: "soa_Model" = None, soa_Entities17: "soa_EntitiesFeature" = None):
        self.name = name
        self.soa_Entities = soa_Entities
        self.soa_Entities17 = soa_Entities17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def soa_Entities(self):
        return self.__soa_Entities

    @soa_Entities.setter
    def soa_Entities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Entities__soa_Entities", None)
        self.__soa_Entities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Model10"):
                opp_val = getattr(old_value, "soa_Model10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Model10"):
                opp_val = getattr(value, "soa_Model10", None)
                if opp_val is None:
                    setattr(value, "soa_Model10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soa_Entities17(self):
        return self.__soa_Entities17

    @soa_Entities17.setter
    def soa_Entities17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Entities__soa_Entities17", None)
        self.__soa_Entities17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_EntitiesFeature"):
                opp_val = getattr(old_value, "soa_EntitiesFeature", None)
                if opp_val == self:
                    setattr(old_value, "soa_EntitiesFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_EntitiesFeature"):
                opp_val = getattr(value, "soa_EntitiesFeature", None)
                setattr(value, "soa_EntitiesFeature", self)

class soa_Model:

    pass
class soa_Import:

    def __init__(self, importedNamespace: str, soa_Import: "soa_Module" = None):
        self.importedNamespace = importedNamespace
        self.soa_Import = soa_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def soa_Import(self):
        return self.__soa_Import

    @soa_Import.setter
    def soa_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Import__soa_Import", None)
        self.__soa_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Module2"):
                opp_val = getattr(old_value, "soa_Module2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Module2"):
                opp_val = getattr(value, "soa_Module2", None)
                if opp_val is None:
                    setattr(value, "soa_Module2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class soa_Module:

    def __init__(self, name: str, version: str, event: str, soa_Module: "soa_Architecture" = None, soa_Module2: set["soa_Import"] = None, soa_Module4: "soa_Model" = None, soa_Module6: "soa_Exceptions" = None, soa_Module8: set["soa_Service"] = None):
        self.name = name
        self.version = version
        self.event = event
        self.soa_Module = soa_Module
        self.soa_Module2 = soa_Module2 if soa_Module2 is not None else set()
        self.soa_Module4 = soa_Module4
        self.soa_Module6 = soa_Module6
        self.soa_Module8 = soa_Module8 if soa_Module8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def soa_Module2(self):
        return self.__soa_Module2

    @soa_Module2.setter
    def soa_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Module__soa_Module2", None)
        self.__soa_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Import"):
                    opp_val = getattr(item, "soa_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Import"):
                    opp_val = getattr(item, "soa_Import", None)
                    
                    setattr(item, "soa_Import", self)
                    

    @property
    def soa_Module8(self):
        return self.__soa_Module8

    @soa_Module8.setter
    def soa_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Module__soa_Module8", None)
        self.__soa_Module8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soa_Service"):
                    opp_val = getattr(item, "soa_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "soa_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soa_Service"):
                    opp_val = getattr(item, "soa_Service", None)
                    
                    setattr(item, "soa_Service", self)
                    

    @property
    def soa_Module6(self):
        return self.__soa_Module6

    @soa_Module6.setter
    def soa_Module6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Module__soa_Module6", None)
        self.__soa_Module6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Exceptions"):
                opp_val = getattr(old_value, "soa_Exceptions", None)
                if opp_val == self:
                    setattr(old_value, "soa_Exceptions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Exceptions"):
                opp_val = getattr(value, "soa_Exceptions", None)
                setattr(value, "soa_Exceptions", self)

    @property
    def soa_Module4(self):
        return self.__soa_Module4

    @soa_Module4.setter
    def soa_Module4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Module__soa_Module4", None)
        self.__soa_Module4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Model"):
                opp_val = getattr(old_value, "soa_Model", None)
                if opp_val == self:
                    setattr(old_value, "soa_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Model"):
                opp_val = getattr(value, "soa_Model", None)
                setattr(value, "soa_Model", self)

    @property
    def soa_Module(self):
        return self.__soa_Module

    @soa_Module.setter
    def soa_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Module__soa_Module", None)
        self.__soa_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Architecture"):
                opp_val = getattr(old_value, "soa_Architecture", None)
                if opp_val == self:
                    setattr(old_value, "soa_Architecture", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Architecture"):
                opp_val = getattr(value, "soa_Architecture", None)
                setattr(value, "soa_Architecture", self)

class soa_Architecture:

    def __init__(self, name: str, soa_Architecture: "soa_Module" = None):
        self.name = name
        self.soa_Architecture = soa_Architecture
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def soa_Architecture(self):
        return self.__soa_Architecture

    @soa_Architecture.setter
    def soa_Architecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soa_Architecture__soa_Architecture", None)
        self.__soa_Architecture = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soa_Module"):
                opp_val = getattr(old_value, "soa_Module", None)
                if opp_val == self:
                    setattr(old_value, "soa_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soa_Module"):
                opp_val = getattr(value, "soa_Module", None)
                setattr(value, "soa_Module", self)
