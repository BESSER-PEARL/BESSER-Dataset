from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FieldType:

    pass
class entities_EntityType(FieldType):

    pass
class entities_BasicType(FieldType):

    def __init__(self, typeName: str):
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class entities_FieldType:

    pass
class Expression:

    pass
class entities_FieldRef(Expression):

    pass
class entities_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class entities_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class entities_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class entities_Statement:

    pass
class entities_Field:

    def __init__(self, name: str, entities_Field11: "entities_AssignmentStatement" = None, entities_Field: "entities_Entity" = None, entities_Field13: "entities_FieldType" = None, entities_Field17: "entities_FieldRef" = None):
        self.name = name
        self.entities_Field11 = entities_Field11
        self.entities_Field = entities_Field
        self.entities_Field13 = entities_Field13
        self.entities_Field17 = entities_Field17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Field17(self):
        return self.__entities_Field17

    @entities_Field17.setter
    def entities_Field17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Field__entities_Field17", None)
        self.__entities_Field17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_FieldRef"):
                opp_val = getattr(old_value, "entities_FieldRef", None)
                if opp_val == self:
                    setattr(old_value, "entities_FieldRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_FieldRef"):
                opp_val = getattr(value, "entities_FieldRef", None)
                setattr(value, "entities_FieldRef", self)

    @property
    def entities_Field11(self):
        return self.__entities_Field11

    @entities_Field11.setter
    def entities_Field11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Field__entities_Field11", None)
        self.__entities_Field11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_AssignmentStatement"):
                opp_val = getattr(old_value, "entities_AssignmentStatement", None)
                if opp_val == self:
                    setattr(old_value, "entities_AssignmentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_AssignmentStatement"):
                opp_val = getattr(value, "entities_AssignmentStatement", None)
                setattr(value, "entities_AssignmentStatement", self)

    @property
    def entities_Field(self):
        return self.__entities_Field

    @entities_Field.setter
    def entities_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Field__entities_Field", None)
        self.__entities_Field = value
        
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
    def entities_Field13(self):
        return self.__entities_Field13

    @entities_Field13.setter
    def entities_Field13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Field__entities_Field13", None)
        self.__entities_Field13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_FieldType"):
                opp_val = getattr(old_value, "entities_FieldType", None)
                if opp_val == self:
                    setattr(old_value, "entities_FieldType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_FieldType"):
                opp_val = getattr(value, "entities_FieldType", None)
                setattr(value, "entities_FieldType", self)

class entities_Entity:

    def __init__(self, name: str, entities_Entity: "entities_Model" = None, entities_Entity3: "entities_Entity" = None, entities_Entity1: "entities_Entity" = None, entities_Entity5: set["entities_Field"] = None, entities_Entity7: set["entities_Statement"] = None, entities_Entity15: "entities_EntityType" = None):
        self.name = name
        self.entities_Entity = entities_Entity
        self.entities_Entity3 = entities_Entity3
        self.entities_Entity1 = entities_Entity1
        self.entities_Entity5 = entities_Entity5 if entities_Entity5 is not None else set()
        self.entities_Entity7 = entities_Entity7 if entities_Entity7 is not None else set()
        self.entities_Entity15 = entities_Entity15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Entity15(self):
        return self.__entities_Entity15

    @entities_Entity15.setter
    def entities_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity15", None)
        self.__entities_Entity15 = value
        
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
    def entities_Entity7(self):
        return self.__entities_Entity7

    @entities_Entity7.setter
    def entities_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity7", None)
        self.__entities_Entity7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entities_Statement"):
                    opp_val = getattr(item, "entities_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "entities_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entities_Statement"):
                    opp_val = getattr(item, "entities_Statement", None)
                    
                    setattr(item, "entities_Statement", self)
                    

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
                if hasattr(item, "entities_Field"):
                    opp_val = getattr(item, "entities_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "entities_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entities_Field"):
                    opp_val = getattr(item, "entities_Field", None)
                    
                    setattr(item, "entities_Field", self)
                    

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

class Statement:

    pass
class entities_PrintStatement(Statement):

    pass
class entities_AssignmentStatement(Statement):

    pass
class entities_Expression:

    pass
class entities_Model:

    pass