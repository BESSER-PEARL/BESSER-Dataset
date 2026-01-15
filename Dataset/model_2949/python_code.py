from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class jsonldConverter_EnumItem:

    def __init__(self, name: str, type: str, jsonldConverter_EnumItem: "jsonldConverter_Enum" = None):
        self.name = name
        self.type = type
        self.jsonldConverter_EnumItem = jsonldConverter_EnumItem
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jsonldConverter_EnumItem(self):
        return self.__jsonldConverter_EnumItem

    @jsonldConverter_EnumItem.setter
    def jsonldConverter_EnumItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsonldConverter_EnumItem__jsonldConverter_EnumItem", None)
        self.__jsonldConverter_EnumItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsonldConverter_Enum"):
                opp_val = getattr(old_value, "jsonldConverter_Enum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsonldConverter_Enum"):
                opp_val = getattr(value, "jsonldConverter_Enum", None)
                if opp_val is None:
                    setattr(value, "jsonldConverter_Enum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class jsonldConverter_Enum(Type):

    pass
class jsonldConverter_Entity(Type):

    pass
class jsonldConverter_DataType(Type):

    pass
class jsonldConverter_Type:

    def __init__(self, name: str, jsonldConverter_Type7: "jsonldConverter_Property" = None, jsonldConverter_Type: "jsonldConverter_Model" = None):
        self.name = name
        self.jsonldConverter_Type7 = jsonldConverter_Type7
        self.jsonldConverter_Type = jsonldConverter_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jsonldConverter_Type(self):
        return self.__jsonldConverter_Type

    @jsonldConverter_Type.setter
    def jsonldConverter_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsonldConverter_Type__jsonldConverter_Type", None)
        self.__jsonldConverter_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsonldConverter_Model"):
                opp_val = getattr(old_value, "jsonldConverter_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsonldConverter_Model"):
                opp_val = getattr(value, "jsonldConverter_Model", None)
                if opp_val is None:
                    setattr(value, "jsonldConverter_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jsonldConverter_Type7(self):
        return self.__jsonldConverter_Type7

    @jsonldConverter_Type7.setter
    def jsonldConverter_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsonldConverter_Type__jsonldConverter_Type7", None)
        self.__jsonldConverter_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsonldConverter_Property6"):
                opp_val = getattr(old_value, "jsonldConverter_Property6", None)
                if opp_val == self:
                    setattr(old_value, "jsonldConverter_Property6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsonldConverter_Property6"):
                opp_val = getattr(value, "jsonldConverter_Property6", None)
                setattr(value, "jsonldConverter_Property6", self)

class jsonldConverter_Property:

    def __init__(self, name: str, many: bool, one: bool, jsonldConverter_Property: "jsonldConverter_Entity" = None, jsonldConverter_Property6: "jsonldConverter_Type" = None):
        self.name = name
        self.many = many
        self.one = one
        self.jsonldConverter_Property = jsonldConverter_Property
        self.jsonldConverter_Property6 = jsonldConverter_Property6
        
    @property
    def one(self) -> bool:
        return self.__one

    @one.setter
    def one(self, one: bool):
        self.__one = one

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def jsonldConverter_Property(self):
        return self.__jsonldConverter_Property

    @jsonldConverter_Property.setter
    def jsonldConverter_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsonldConverter_Property__jsonldConverter_Property", None)
        self.__jsonldConverter_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsonldConverter_Entity4"):
                opp_val = getattr(old_value, "jsonldConverter_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsonldConverter_Entity4"):
                opp_val = getattr(value, "jsonldConverter_Entity4", None)
                if opp_val is None:
                    setattr(value, "jsonldConverter_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jsonldConverter_Property6(self):
        return self.__jsonldConverter_Property6

    @jsonldConverter_Property6.setter
    def jsonldConverter_Property6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsonldConverter_Property__jsonldConverter_Property6", None)
        self.__jsonldConverter_Property6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsonldConverter_Type7"):
                opp_val = getattr(old_value, "jsonldConverter_Type7", None)
                if opp_val == self:
                    setattr(old_value, "jsonldConverter_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsonldConverter_Type7"):
                opp_val = getattr(value, "jsonldConverter_Type7", None)
                setattr(value, "jsonldConverter_Type7", self)

class jsonldConverter_Model:

    pass