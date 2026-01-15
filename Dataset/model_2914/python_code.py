from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class metamodel_Extension_MQPublishing:

    def __init__(self, queue: str, metamodel_Extension_MQPublishing: "metamodel_EntityObserver" = None):
        self.queue = queue
        self.metamodel_Extension_MQPublishing = metamodel_Extension_MQPublishing
        
    @property
    def queue(self) -> str:
        return self.__queue

    @queue.setter
    def queue(self, queue: str):
        self.__queue = queue

    @property
    def metamodel_Extension_MQPublishing(self):
        return self.__metamodel_Extension_MQPublishing

    @metamodel_Extension_MQPublishing.setter
    def metamodel_Extension_MQPublishing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Extension_MQPublishing__metamodel_Extension_MQPublishing", None)
        self.__metamodel_Extension_MQPublishing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_EntityObserver20"):
                opp_val = getattr(old_value, "metamodel_EntityObserver20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_EntityObserver20"):
                opp_val = getattr(value, "metamodel_EntityObserver20", None)
                if opp_val is None:
                    setattr(value, "metamodel_EntityObserver20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Type(ABC):

    def __init__(self, name: str, metamodel_Type: "metamodel_Variable" = None, metamodel_Type32: "metamodel_Model" = None):
        self.name = name
        self.metamodel_Type = metamodel_Type
        self.metamodel_Type32 = metamodel_Type32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Type(self):
        return self.__metamodel_Type

    @metamodel_Type.setter
    def metamodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type", None)
        self.__metamodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Variable15"):
                opp_val = getattr(old_value, "metamodel_Variable15", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Variable15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Variable15"):
                opp_val = getattr(value, "metamodel_Variable15", None)
                setattr(value, "metamodel_Variable15", self)

    @property
    def metamodel_Type32(self):
        return self.__metamodel_Type32

    @metamodel_Type32.setter
    def metamodel_Type32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type32", None)
        self.__metamodel_Type32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Model31"):
                opp_val = getattr(old_value, "metamodel_Model31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Model31"):
                opp_val = getattr(value, "metamodel_Model31", None)
                if opp_val is None:
                    setattr(value, "metamodel_Model31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_ActsAs:

    def __init__(self, actsAsWhat: str, metamodel_ActsAs: "metamodel_Entity" = None):
        self.actsAsWhat = actsAsWhat
        self.metamodel_ActsAs = metamodel_ActsAs
        
    @property
    def actsAsWhat(self) -> str:
        return self.__actsAsWhat

    @actsAsWhat.setter
    def actsAsWhat(self, actsAsWhat: str):
        self.__actsAsWhat = actsAsWhat

    @property
    def metamodel_ActsAs(self):
        return self.__metamodel_ActsAs

    @metamodel_ActsAs.setter
    def metamodel_ActsAs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_ActsAs__metamodel_ActsAs", None)
        self.__metamodel_ActsAs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity9"):
                opp_val = getattr(old_value, "metamodel_Entity9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity9"):
                opp_val = getattr(value, "metamodel_Entity9", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_EntityObserver:

    pass
class metamodel_ConnectionToEntity:

    def __init__(self, name: str, cardinalityMany: bool, metamodel_ConnectionToEntity12: "metamodel_Entity" = None, metamodel_ConnectionToEntity: "metamodel_Entity" = None, metamodel_ConnectionToEntity5: "metamodel_Entity" = None):
        self.name = name
        self.cardinalityMany = cardinalityMany
        self.metamodel_ConnectionToEntity12 = metamodel_ConnectionToEntity12
        self.metamodel_ConnectionToEntity = metamodel_ConnectionToEntity
        self.metamodel_ConnectionToEntity5 = metamodel_ConnectionToEntity5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cardinalityMany(self) -> bool:
        return self.__cardinalityMany

    @cardinalityMany.setter
    def cardinalityMany(self, cardinalityMany: bool):
        self.__cardinalityMany = cardinalityMany

    @property
    def metamodel_ConnectionToEntity(self):
        return self.__metamodel_ConnectionToEntity

    @metamodel_ConnectionToEntity.setter
    def metamodel_ConnectionToEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_ConnectionToEntity__metamodel_ConnectionToEntity", None)
        self.__metamodel_ConnectionToEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity2"):
                opp_val = getattr(old_value, "metamodel_Entity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity2"):
                opp_val = getattr(value, "metamodel_Entity2", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_ConnectionToEntity5(self):
        return self.__metamodel_ConnectionToEntity5

    @metamodel_ConnectionToEntity5.setter
    def metamodel_ConnectionToEntity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_ConnectionToEntity__metamodel_ConnectionToEntity5", None)
        self.__metamodel_ConnectionToEntity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity4"):
                opp_val = getattr(old_value, "metamodel_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity4"):
                opp_val = getattr(value, "metamodel_Entity4", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_ConnectionToEntity12(self):
        return self.__metamodel_ConnectionToEntity12

    @metamodel_ConnectionToEntity12.setter
    def metamodel_ConnectionToEntity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_ConnectionToEntity__metamodel_ConnectionToEntity12", None)
        self.__metamodel_ConnectionToEntity12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity13"):
                opp_val = getattr(old_value, "metamodel_Entity13", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Entity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity13"):
                opp_val = getattr(value, "metamodel_Entity13", None)
                setattr(value, "metamodel_Entity13", self)

class metamodel_Variable(ABC):

    def __init__(self, name: str, metamodel_Variable15: "metamodel_Type" = None, metamodel_Variable: "metamodel_Entity" = None, metamodel_Variable17: "metamodel_Validation_ValueRestriction" = None):
        self.name = name
        self.metamodel_Variable15 = metamodel_Variable15
        self.metamodel_Variable = metamodel_Variable
        self.metamodel_Variable17 = metamodel_Variable17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Variable15(self):
        return self.__metamodel_Variable15

    @metamodel_Variable15.setter
    def metamodel_Variable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Variable__metamodel_Variable15", None)
        self.__metamodel_Variable15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type"):
                opp_val = getattr(old_value, "metamodel_Type", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type"):
                opp_val = getattr(value, "metamodel_Type", None)
                setattr(value, "metamodel_Type", self)

    @property
    def metamodel_Variable17(self):
        return self.__metamodel_Variable17

    @metamodel_Variable17.setter
    def metamodel_Variable17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Variable__metamodel_Variable17", None)
        self.__metamodel_Variable17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Validation_ValueRestriction18"):
                opp_val = getattr(old_value, "metamodel_Validation_ValueRestriction18", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Validation_ValueRestriction18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Validation_ValueRestriction18"):
                opp_val = getattr(value, "metamodel_Validation_ValueRestriction18", None)
                setattr(value, "metamodel_Validation_ValueRestriction18", self)

    @property
    def metamodel_Variable(self):
        return self.__metamodel_Variable

    @metamodel_Variable.setter
    def metamodel_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Variable__metamodel_Variable", None)
        self.__metamodel_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity"):
                opp_val = getattr(old_value, "metamodel_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity"):
                opp_val = getattr(value, "metamodel_Entity", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class metamodel_Model(Type):

    pass
class metamodel_Controller(Type):

    pass
class metamodel_View(Type):

    pass
class metamodel_Datatype(Type):

    pass
class metamodel_Entity(Type):

    def __init__(self, base: str, metamodel_Entity13: "metamodel_ConnectionToEntity" = None, metamodel_Entity: set["metamodel_Variable"] = None, metamodel_Entity2: set["metamodel_ConnectionToEntity"] = None, metamodel_Entity4: set["metamodel_ConnectionToEntity"] = None, metamodel_Entity7: set["metamodel_EntityObserver"] = None, metamodel_Entity9: set["metamodel_ActsAs"] = None, metamodel_Entity29: "metamodel_Model" = None):
        self.base = base
        self.metamodel_Entity13 = metamodel_Entity13
        self.metamodel_Entity = metamodel_Entity if metamodel_Entity is not None else set()
        self.metamodel_Entity2 = metamodel_Entity2 if metamodel_Entity2 is not None else set()
        self.metamodel_Entity4 = metamodel_Entity4 if metamodel_Entity4 is not None else set()
        self.metamodel_Entity7 = metamodel_Entity7 if metamodel_Entity7 is not None else set()
        self.metamodel_Entity9 = metamodel_Entity9 if metamodel_Entity9 is not None else set()
        self.metamodel_Entity29 = metamodel_Entity29
        
    @property
    def base(self) -> str:
        return self.__base

    @base.setter
    def base(self, base: str):
        self.__base = base

    @property
    def metamodel_Entity(self):
        return self.__metamodel_Entity

    @metamodel_Entity.setter
    def metamodel_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity", None)
        self.__metamodel_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Variable"):
                    opp_val = getattr(item, "metamodel_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Variable"):
                    opp_val = getattr(item, "metamodel_Variable", None)
                    
                    setattr(item, "metamodel_Variable", self)
                    

    @property
    def metamodel_Entity7(self):
        return self.__metamodel_Entity7

    @metamodel_Entity7.setter
    def metamodel_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity7", None)
        self.__metamodel_Entity7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_EntityObserver"):
                    opp_val = getattr(item, "metamodel_EntityObserver", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_EntityObserver", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_EntityObserver"):
                    opp_val = getattr(item, "metamodel_EntityObserver", None)
                    
                    setattr(item, "metamodel_EntityObserver", self)
                    

    @property
    def metamodel_Entity4(self):
        return self.__metamodel_Entity4

    @metamodel_Entity4.setter
    def metamodel_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity4", None)
        self.__metamodel_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_ConnectionToEntity5"):
                    opp_val = getattr(item, "metamodel_ConnectionToEntity5", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_ConnectionToEntity5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_ConnectionToEntity5"):
                    opp_val = getattr(item, "metamodel_ConnectionToEntity5", None)
                    
                    setattr(item, "metamodel_ConnectionToEntity5", self)
                    

    @property
    def metamodel_Entity2(self):
        return self.__metamodel_Entity2

    @metamodel_Entity2.setter
    def metamodel_Entity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity2", None)
        self.__metamodel_Entity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_ConnectionToEntity"):
                    opp_val = getattr(item, "metamodel_ConnectionToEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_ConnectionToEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_ConnectionToEntity"):
                    opp_val = getattr(item, "metamodel_ConnectionToEntity", None)
                    
                    setattr(item, "metamodel_ConnectionToEntity", self)
                    

    @property
    def metamodel_Entity9(self):
        return self.__metamodel_Entity9

    @metamodel_Entity9.setter
    def metamodel_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity9", None)
        self.__metamodel_Entity9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_ActsAs"):
                    opp_val = getattr(item, "metamodel_ActsAs", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_ActsAs", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_ActsAs"):
                    opp_val = getattr(item, "metamodel_ActsAs", None)
                    
                    setattr(item, "metamodel_ActsAs", self)
                    

    @property
    def metamodel_Entity13(self):
        return self.__metamodel_Entity13

    @metamodel_Entity13.setter
    def metamodel_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity13", None)
        self.__metamodel_Entity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_ConnectionToEntity12"):
                opp_val = getattr(old_value, "metamodel_ConnectionToEntity12", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_ConnectionToEntity12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_ConnectionToEntity12"):
                opp_val = getattr(value, "metamodel_ConnectionToEntity12", None)
                setattr(value, "metamodel_ConnectionToEntity12", self)

    @property
    def metamodel_Entity29(self):
        return self.__metamodel_Entity29

    @metamodel_Entity29.setter
    def metamodel_Entity29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Entity__metamodel_Entity29", None)
        self.__metamodel_Entity29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Model28"):
                opp_val = getattr(old_value, "metamodel_Model28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Model28"):
                opp_val = getattr(value, "metamodel_Model28", None)
                if opp_val is None:
                    setattr(value, "metamodel_Model28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Variable:

    pass
class metamodel_StaticVariable(Variable):

    pass
class metamodel_PlainVariable(Variable):

    pass
class metamodel_TransientVariable(Variable):

    pass
class metamodel_ValueRestriction_Value:

    def __init__(self, value: str, metamodel_ValueRestriction_Value: "metamodel_Validation_ValueRestriction" = None):
        self.value = value
        self.metamodel_ValueRestriction_Value = metamodel_ValueRestriction_Value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def metamodel_ValueRestriction_Value(self):
        return self.__metamodel_ValueRestriction_Value

    @metamodel_ValueRestriction_Value.setter
    def metamodel_ValueRestriction_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_ValueRestriction_Value__metamodel_ValueRestriction_Value", None)
        self.__metamodel_ValueRestriction_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Validation_ValueRestriction"):
                opp_val = getattr(old_value, "metamodel_Validation_ValueRestriction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Validation_ValueRestriction"):
                opp_val = getattr(value, "metamodel_Validation_ValueRestriction", None)
                if opp_val is None:
                    setattr(value, "metamodel_Validation_ValueRestriction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Validation_ValueRestriction:

    pass