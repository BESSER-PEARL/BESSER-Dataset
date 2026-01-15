from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ElementType:

    pass
class entities_BasicType(ElementType):

    def __init__(self, typeName: str):
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class entities_EntityType(ElementType):

    pass
class entities_ElementType:

    pass
class entities_AttributeType:

    def __init__(self, array: bool, length: int, entities_AttributeType: "entities_Attribute" = None, entities_AttributeType9: "entities_ElementType" = None):
        self.array = array
        self.length = length
        self.entities_AttributeType = entities_AttributeType
        self.entities_AttributeType9 = entities_AttributeType9
        
    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def entities_AttributeType(self):
        return self.__entities_AttributeType

    @entities_AttributeType.setter
    def entities_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_AttributeType__entities_AttributeType", None)
        self.__entities_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Attribute7"):
                opp_val = getattr(old_value, "entities_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "entities_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Attribute7"):
                opp_val = getattr(value, "entities_Attribute7", None)
                setattr(value, "entities_Attribute7", self)

    @property
    def entities_AttributeType9(self):
        return self.__entities_AttributeType9

    @entities_AttributeType9.setter
    def entities_AttributeType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_AttributeType__entities_AttributeType9", None)
        self.__entities_AttributeType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_ElementType"):
                opp_val = getattr(old_value, "entities_ElementType", None)
                if opp_val == self:
                    setattr(old_value, "entities_ElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_ElementType"):
                opp_val = getattr(value, "entities_ElementType", None)
                setattr(value, "entities_ElementType", self)

class entities_Attribute:

    def __init__(self, name: str, entities_Attribute: "entities_Entity" = None, entities_Attribute7: "entities_AttributeType" = None):
        self.name = name
        self.entities_Attribute = entities_Attribute
        self.entities_Attribute7 = entities_Attribute7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Attribute(self):
        return self.__entities_Attribute

    @entities_Attribute.setter
    def entities_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Attribute__entities_Attribute", None)
        self.__entities_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity5"):
                opp_val = getattr(old_value, "entities_Entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity5"):
                opp_val = getattr(value, "entities_Entity5", None)
                if opp_val is None:
                    setattr(value, "entities_Entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entities_Attribute7(self):
        return self.__entities_Attribute7

    @entities_Attribute7.setter
    def entities_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Attribute__entities_Attribute7", None)
        self.__entities_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_AttributeType"):
                opp_val = getattr(old_value, "entities_AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "entities_AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_AttributeType"):
                opp_val = getattr(value, "entities_AttributeType", None)
                setattr(value, "entities_AttributeType", self)

class entities_Entity:

    def __init__(self, name: str, entities_Entity: "entities_Model" = None, entities_Entity3: "entities_Entity" = None, entities_Entity1: "entities_Entity" = None, entities_Entity5: set["entities_Attribute"] = None, entities_Entity11: "entities_EntityType" = None):
        self.name = name
        self.entities_Entity = entities_Entity
        self.entities_Entity3 = entities_Entity3
        self.entities_Entity1 = entities_Entity1
        self.entities_Entity5 = entities_Entity5 if entities_Entity5 is not None else set()
        self.entities_Entity11 = entities_Entity11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Entity1(self):
        return self.__entities_Entity1

    @entities_Entity1.setter
    def entities_Entity1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity1", None)
        self.__entities_Entity1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity3"):
                opp_val = getattr(old_value, "entities_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "entities_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity3"):
                opp_val = getattr(value, "entities_Entity3", None)
                setattr(value, "entities_Entity3", self)

    @property
    def entities_Entity5(self):
        return self.__entities_Entity5

    @entities_Entity5.setter
    def entities_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity5", None)
        self.__entities_Entity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entities_Attribute"):
                    opp_val = getattr(item, "entities_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "entities_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entities_Attribute"):
                    opp_val = getattr(item, "entities_Attribute", None)
                    
                    setattr(item, "entities_Attribute", self)
                    

    @property
    def entities_Entity3(self):
        return self.__entities_Entity3

    @entities_Entity3.setter
    def entities_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity3", None)
        self.__entities_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity1"):
                opp_val = getattr(old_value, "entities_Entity1", None)
                if opp_val == self:
                    setattr(old_value, "entities_Entity1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity1"):
                opp_val = getattr(value, "entities_Entity1", None)
                setattr(value, "entities_Entity1", self)

    @property
    def entities_Entity11(self):
        return self.__entities_Entity11

    @entities_Entity11.setter
    def entities_Entity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity11", None)
        self.__entities_Entity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_EntityType"):
                opp_val = getattr(old_value, "entities_EntityType", None)
                if opp_val == self:
                    setattr(old_value, "entities_EntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_EntityType"):
                opp_val = getattr(value, "entities_EntityType", None)
                setattr(value, "entities_EntityType", self)

    @property
    def entities_Entity(self):
        return self.__entities_Entity

    @entities_Entity.setter
    def entities_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity", None)
        self.__entities_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Model"):
                opp_val = getattr(old_value, "entities_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Model"):
                opp_val = getattr(value, "entities_Model", None)
                if opp_val is None:
                    setattr(value, "entities_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entities_Model:

    pass