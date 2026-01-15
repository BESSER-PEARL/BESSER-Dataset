from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class type_EStringToStringMapEntry:

    pass
class type_XMLTypeDocumentRoot:

    def __init__(self, mixed: str, cDATA: str, comment: str, text: str, type_XMLTypeDocumentRoot: set["type_EStringToStringMapEntry"] = None, type_XMLTypeDocumentRoot3: set["type_EStringToStringMapEntry"] = None, type_XMLTypeDocumentRoot6: set["type_ProcessingInstruction"] = None):
        self.mixed = mixed
        self.cDATA = cDATA
        self.comment = comment
        self.text = text
        self.type_XMLTypeDocumentRoot = type_XMLTypeDocumentRoot if type_XMLTypeDocumentRoot is not None else set()
        self.type_XMLTypeDocumentRoot3 = type_XMLTypeDocumentRoot3 if type_XMLTypeDocumentRoot3 is not None else set()
        self.type_XMLTypeDocumentRoot6 = type_XMLTypeDocumentRoot6 if type_XMLTypeDocumentRoot6 is not None else set()
        
    @property
    def cDATA(self) -> str:
        return self.__cDATA

    @cDATA.setter
    def cDATA(self, cDATA: str):
        self.__cDATA = cDATA

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def type_XMLTypeDocumentRoot6(self):
        return self.__type_XMLTypeDocumentRoot6

    @type_XMLTypeDocumentRoot6.setter
    def type_XMLTypeDocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_XMLTypeDocumentRoot__type_XMLTypeDocumentRoot6", None)
        self.__type_XMLTypeDocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_ProcessingInstruction"):
                    opp_val = getattr(item, "type_ProcessingInstruction", None)
                    
                    if opp_val == self:
                        setattr(item, "type_ProcessingInstruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_ProcessingInstruction"):
                    opp_val = getattr(item, "type_ProcessingInstruction", None)
                    
                    setattr(item, "type_ProcessingInstruction", self)
                    

    @property
    def type_XMLTypeDocumentRoot(self):
        return self.__type_XMLTypeDocumentRoot

    @type_XMLTypeDocumentRoot.setter
    def type_XMLTypeDocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_XMLTypeDocumentRoot__type_XMLTypeDocumentRoot", None)
        self.__type_XMLTypeDocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_EStringToStringMapEntry"):
                    opp_val = getattr(item, "type_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "type_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_EStringToStringMapEntry"):
                    opp_val = getattr(item, "type_EStringToStringMapEntry", None)
                    
                    setattr(item, "type_EStringToStringMapEntry", self)
                    

    @property
    def type_XMLTypeDocumentRoot3(self):
        return self.__type_XMLTypeDocumentRoot3

    @type_XMLTypeDocumentRoot3.setter
    def type_XMLTypeDocumentRoot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_XMLTypeDocumentRoot__type_XMLTypeDocumentRoot3", None)
        self.__type_XMLTypeDocumentRoot3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "type_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "type_EStringToStringMapEntry4", None)
                    
                    if opp_val == self:
                        setattr(item, "type_EStringToStringMapEntry4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "type_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "type_EStringToStringMapEntry4", None)
                    
                    setattr(item, "type_EStringToStringMapEntry4", self)
                    

class type_EDataType:

    pass
class AnyType:

    pass
class type_SimpleAnyType(AnyType):

    def __init__(self, rawValue: str, value: str, type_SimpleAnyType: "type_EDataType" = None):
        self.rawValue = rawValue
        self.value = value
        self.type_SimpleAnyType = type_SimpleAnyType
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def rawValue(self) -> str:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: str):
        self.__rawValue = rawValue

    @property
    def type_SimpleAnyType(self):
        return self.__type_SimpleAnyType

    @type_SimpleAnyType.setter
    def type_SimpleAnyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_SimpleAnyType__type_SimpleAnyType", None)
        self.__type_SimpleAnyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_EDataType"):
                opp_val = getattr(old_value, "type_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "type_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_EDataType"):
                opp_val = getattr(value, "type_EDataType", None)
                setattr(value, "type_EDataType", self)

class type_ProcessingInstruction:

    def __init__(self, data: str, target: str, type_ProcessingInstruction: "type_XMLTypeDocumentRoot" = None):
        self.data = data
        self.target = target
        self.type_ProcessingInstruction = type_ProcessingInstruction
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def type_ProcessingInstruction(self):
        return self.__type_ProcessingInstruction

    @type_ProcessingInstruction.setter
    def type_ProcessingInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_type_ProcessingInstruction__type_ProcessingInstruction", None)
        self.__type_ProcessingInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_XMLTypeDocumentRoot6"):
                opp_val = getattr(old_value, "type_XMLTypeDocumentRoot6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_XMLTypeDocumentRoot6"):
                opp_val = getattr(value, "type_XMLTypeDocumentRoot6", None)
                if opp_val is None:
                    setattr(value, "type_XMLTypeDocumentRoot6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_AnyType:

    def __init__(self, mixed: str, any: str, anyAttribute: str):
        self.mixed = mixed
        self.any = any
        self.anyAttribute = anyAttribute
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute
