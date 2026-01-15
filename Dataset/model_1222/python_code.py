from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NumberValue:

    pass
class SingleEntityValue:

    pass
class instances_AggregateValue:

    pass
class core_Instance:

    pass
class express_instances_LISTValue(core_Instance, instances_AggregateValue):

    pass
class LogicalValue:

    pass
class express_instances_BooleanValue(LogicalValue):

    pass
class express_instances_RealValue(NumberValue):

    pass
class express_instances_Population:

    pass
class express_instances_ArrayMember:

    def __init__(self, index: str, express_instances_ArrayMember: "Instance" = None):
        self.index = index
        self.express_instances_ArrayMember = express_instances_ArrayMember
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def express_instances_ArrayMember(self):
        return self.__express_instances_ArrayMember

    @express_instances_ArrayMember.setter
    def express_instances_ArrayMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_ArrayMember__express_instances_ArrayMember", None)
        self.__express_instances_ArrayMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance582"):
                opp_val = getattr(old_value, "Instance582", None)
                if opp_val == self:
                    setattr(old_value, "Instance582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance582"):
                opp_val = getattr(value, "Instance582", None)
                setattr(value, "Instance582", self)

class instances_ConcreteValue:

    pass
class instances_TypedInstance:

    pass
class BagMember:

    pass
class LISTValue:

    pass
class express_instances_GenericAggregate(LISTValue):

    pass
class express_instances_SingleEntityValue:

    pass
class EntityValue:

    pass
class express_instances_BagMember:

    def __init__(self, count: str, express_instances_BagMember: "Instance" = None):
        self.count = count
        self.express_instances_BagMember = express_instances_BagMember
        
    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def express_instances_BagMember(self):
        return self.__express_instances_BagMember

    @express_instances_BagMember.setter
    def express_instances_BagMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_BagMember__express_instances_BagMember", None)
        self.__express_instances_BagMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance558"):
                opp_val = getattr(old_value, "Instance558", None)
                if opp_val == self:
                    setattr(old_value, "Instance558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance558"):
                opp_val = getattr(value, "Instance558", None)
                setattr(value, "Instance558", self)

class TypedInstance:

    pass
class express_instances_SpecializedValue(TypedInstance):

    pass
class express_instances_EntityInstance(TypedInstance):

    def __init__(self, id: str, express_instances_EntityInstance: set["EntityType"] = None, EntityValue: "EntityValue" = None):
        self.id = id
        self.express_instances_EntityInstance = express_instances_EntityInstance if express_instances_EntityInstance is not None else set()
        self.EntityValue = EntityValue
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_instances_EntityInstance(self):
        return self.__express_instances_EntityInstance

    @express_instances_EntityInstance.setter
    def express_instances_EntityInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_EntityInstance__express_instances_EntityInstance", None)
        self.__express_instances_EntityInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EntityType544"):
                    opp_val = getattr(item, "EntityType544", None)
                    
                    if opp_val == self:
                        setattr(item, "EntityType544", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EntityType544"):
                    opp_val = getattr(item, "EntityType544", None)
                    
                    setattr(item, "EntityType544", self)
                    

    @property
    def EntityValue(self):
        return self.__EntityValue

    @EntityValue.setter
    def EntityValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_EntityInstance__EntityValue", None)
        self.__EntityValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instances542"):
                opp_val = getattr(old_value, "instances542", None)
                if opp_val == self:
                    setattr(old_value, "instances542", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instances542"):
                opp_val = getattr(value, "instances542", None)
                setattr(value, "instances542", self)

class express_instances_ListMember:

    def __init__(self, position: str, express_instances_ListMember: "Instance" = None):
        self.position = position
        self.express_instances_ListMember = express_instances_ListMember
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def express_instances_ListMember(self):
        return self.__express_instances_ListMember

    @express_instances_ListMember.setter
    def express_instances_ListMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_ListMember__express_instances_ListMember", None)
        self.__express_instances_ListMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance556"):
                opp_val = getattr(old_value, "Instance556", None)
                if opp_val == self:
                    setattr(old_value, "Instance556", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance556"):
                opp_val = getattr(value, "Instance556", None)
                setattr(value, "Instance556", self)

class StringValue:

    pass
class express_instances_TypeName(StringValue):

    pass
class ConcreteValue:

    pass
class express_instances_SimpleValue(ConcreteValue):

    def __init__(self, name: str, ConcreteValue: "express_instances_SpecializedValue"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class express_instances_AggregateValue(ConcreteValue):

    pass
class RealValue:

    pass
class express_instances_IntegerValue(RealValue):

    pass
class express_algorithms_VARVariable(ABC):

    pass
class express_instances_RoleName(StringValue):

    pass
class ArrayMember:

    pass
class AggregateValue:

    pass
class express_instances_SETValue(AggregateValue):

    pass
class express_instances_BAGValue(AggregateValue):

    pass
class express_instances_ARRAYValue(AggregateValue):

    pass
class express_instances_AttributeValue:

    pass
class core_GenericType:

    pass
class algorithms_Parameter:

    pass
class core_ActualType:

    pass
class AGGREGATEType:

    pass
class express_algorithms_ActualStructureConstraint:

    def __init__(self, label: str, AGGREGATEType: "AGGREGATEType" = None, express_algorithms_ActualStructureConstraint: "ActualStructure" = None):
        self.label = label
        self.AGGREGATEType = AGGREGATEType
        self.express_algorithms_ActualStructureConstraint = express_algorithms_ActualStructureConstraint
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def AGGREGATEType(self):
        return self.__AGGREGATEType

    @AGGREGATEType.setter
    def AGGREGATEType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualStructureConstraint__AGGREGATEType", None)
        self.__AGGREGATEType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core516"):
                opp_val = getattr(old_value, "core516", None)
                if opp_val == self:
                    setattr(old_value, "core516", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core516"):
                opp_val = getattr(value, "core516", None)
                setattr(value, "core516", self)

    @property
    def express_algorithms_ActualStructureConstraint(self):
        return self.__express_algorithms_ActualStructureConstraint

    @express_algorithms_ActualStructureConstraint.setter
    def express_algorithms_ActualStructureConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualStructureConstraint__express_algorithms_ActualStructureConstraint", None)
        self.__express_algorithms_ActualStructureConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualStructure518"):
                opp_val = getattr(old_value, "ActualStructure518", None)
                if opp_val == self:
                    setattr(old_value, "ActualStructure518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualStructure518"):
                opp_val = getattr(value, "ActualStructure518", None)
                setattr(value, "ActualStructure518", self)

class InParameter:

    pass
class ActualStructure:

    pass
class ActualAggregationType:

    pass
class express_algorithms_ActualBAGType(ActualAggregationType):

    pass
class express_algorithms_ActualLISTType(ActualAggregationType):

    pass
class express_algorithms_ActualSETType(ActualAggregationType):

    pass
class express_algorithms_ActualARRAYType(ActualAggregationType):

    def __init__(self, isOptional: str, express_algorithms_ActualARRAYType: "ArrayBound" = None, express_algorithms_ActualARRAYType495: "ArrayBound" = None):
        self.isOptional = isOptional
        self.express_algorithms_ActualARRAYType = express_algorithms_ActualARRAYType
        self.express_algorithms_ActualARRAYType495 = express_algorithms_ActualARRAYType495
        
    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

    @property
    def express_algorithms_ActualARRAYType495(self):
        return self.__express_algorithms_ActualARRAYType495

    @express_algorithms_ActualARRAYType495.setter
    def express_algorithms_ActualARRAYType495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualARRAYType__express_algorithms_ActualARRAYType495", None)
        self.__express_algorithms_ActualARRAYType495 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound496"):
                opp_val = getattr(old_value, "ArrayBound496", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound496"):
                opp_val = getattr(value, "ArrayBound496", None)
                setattr(value, "ArrayBound496", self)

    @property
    def express_algorithms_ActualARRAYType(self):
        return self.__express_algorithms_ActualARRAYType

    @express_algorithms_ActualARRAYType.setter
    def express_algorithms_ActualARRAYType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualARRAYType__express_algorithms_ActualARRAYType", None)
        self.__express_algorithms_ActualARRAYType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound493"):
                opp_val = getattr(old_value, "ArrayBound493", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound493"):
                opp_val = getattr(value, "ArrayBound493", None)
                setattr(value, "ArrayBound493", self)

class InVariable:

    pass
class RepeatStatement:

    pass
class EscapeStatement:

    pass
class SkipStatement:

    pass
class StatementBlock:

    pass
class express_algorithms_Statement:

    def __init__(self, text: str, StatementBlock: "StatementBlock" = None, express_algorithms_Statement: set["SkipStatement"] = None, express_algorithms_Statement482: set["EscapeStatement"] = None, RepeatStatement: "RepeatStatement" = None, Algorithm486: "Algorithm" = None):
        self.text = text
        self.StatementBlock = StatementBlock
        self.express_algorithms_Statement = express_algorithms_Statement if express_algorithms_Statement is not None else set()
        self.express_algorithms_Statement482 = express_algorithms_Statement482 if express_algorithms_Statement482 is not None else set()
        self.RepeatStatement = RepeatStatement
        self.Algorithm486 = Algorithm486
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def express_algorithms_Statement482(self):
        return self.__express_algorithms_Statement482

    @express_algorithms_Statement482.setter
    def express_algorithms_Statement482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__express_algorithms_Statement482", None)
        self.__express_algorithms_Statement482 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EscapeStatement"):
                    opp_val = getattr(item, "EscapeStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "EscapeStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EscapeStatement"):
                    opp_val = getattr(item, "EscapeStatement", None)
                    
                    setattr(item, "EscapeStatement", self)
                    

    @property
    def RepeatStatement(self):
        return self.__RepeatStatement

    @RepeatStatement.setter
    def RepeatStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__RepeatStatement", None)
        self.__RepeatStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements484"):
                opp_val = getattr(old_value, "statements484", None)
                if opp_val == self:
                    setattr(old_value, "statements484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements484"):
                opp_val = getattr(value, "statements484", None)
                setattr(value, "statements484", self)

    @property
    def Algorithm486(self):
        return self.__Algorithm486

    @Algorithm486.setter
    def Algorithm486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__Algorithm486", None)
        self.__Algorithm486 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "algorithms487"):
                opp_val = getattr(old_value, "algorithms487", None)
                if opp_val == self:
                    setattr(old_value, "algorithms487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "algorithms487"):
                opp_val = getattr(value, "algorithms487", None)
                setattr(value, "algorithms487", self)

    @property
    def express_algorithms_Statement(self):
        return self.__express_algorithms_Statement

    @express_algorithms_Statement.setter
    def express_algorithms_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__express_algorithms_Statement", None)
        self.__express_algorithms_Statement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SkipStatement"):
                    opp_val = getattr(item, "SkipStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "SkipStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SkipStatement"):
                    opp_val = getattr(item, "SkipStatement", None)
                    
                    setattr(item, "SkipStatement", self)
                    

    @property
    def StatementBlock(self):
        return self.__StatementBlock

    @StatementBlock.setter
    def StatementBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__StatementBlock", None)
        self.__StatementBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements479"):
                opp_val = getattr(old_value, "statements479", None)
                if opp_val == self:
                    setattr(old_value, "statements479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements479"):
                opp_val = getattr(value, "statements479", None)
                setattr(value, "statements479", self)

class ActualType:

    pass
class express_algorithms_ActualAGGREGATEType(ActualType):

    def __init__(self, label: str, express_algorithms_ActualAGGREGATEType: "SizeConstraint" = None, express_algorithms_ActualAGGREGATEType500: "ActualStructure" = None, express_algorithms_ActualAGGREGATEType502: "VariableType" = None, express_algorithms_ActualAGGREGATEType505: "SizeConstraint" = None, ActualType: "express_algorithms_ActualAggregationType"):
        self.label = label
        self.express_algorithms_ActualAGGREGATEType = express_algorithms_ActualAGGREGATEType
        self.express_algorithms_ActualAGGREGATEType500 = express_algorithms_ActualAGGREGATEType500
        self.express_algorithms_ActualAGGREGATEType502 = express_algorithms_ActualAGGREGATEType502
        self.express_algorithms_ActualAGGREGATEType505 = express_algorithms_ActualAGGREGATEType505
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def express_algorithms_ActualAGGREGATEType(self):
        return self.__express_algorithms_ActualAGGREGATEType

    @express_algorithms_ActualAGGREGATEType.setter
    def express_algorithms_ActualAGGREGATEType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType", None)
        self.__express_algorithms_ActualAGGREGATEType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint498"):
                opp_val = getattr(old_value, "SizeConstraint498", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint498", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint498"):
                opp_val = getattr(value, "SizeConstraint498", None)
                setattr(value, "SizeConstraint498", self)

    @property
    def express_algorithms_ActualAGGREGATEType505(self):
        return self.__express_algorithms_ActualAGGREGATEType505

    @express_algorithms_ActualAGGREGATEType505.setter
    def express_algorithms_ActualAGGREGATEType505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType505", None)
        self.__express_algorithms_ActualAGGREGATEType505 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint506"):
                opp_val = getattr(old_value, "SizeConstraint506", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint506", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint506"):
                opp_val = getattr(value, "SizeConstraint506", None)
                setattr(value, "SizeConstraint506", self)

    @property
    def express_algorithms_ActualAGGREGATEType502(self):
        return self.__express_algorithms_ActualAGGREGATEType502

    @express_algorithms_ActualAGGREGATEType502.setter
    def express_algorithms_ActualAGGREGATEType502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType502", None)
        self.__express_algorithms_ActualAGGREGATEType502 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableType503"):
                opp_val = getattr(old_value, "VariableType503", None)
                if opp_val == self:
                    setattr(old_value, "VariableType503", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableType503"):
                opp_val = getattr(value, "VariableType503", None)
                setattr(value, "VariableType503", self)

    @property
    def express_algorithms_ActualAGGREGATEType500(self):
        return self.__express_algorithms_ActualAGGREGATEType500

    @express_algorithms_ActualAGGREGATEType500.setter
    def express_algorithms_ActualAGGREGATEType500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType500", None)
        self.__express_algorithms_ActualAGGREGATEType500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualStructure"):
                opp_val = getattr(old_value, "ActualStructure", None)
                if opp_val == self:
                    setattr(old_value, "ActualStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualStructure"):
                opp_val = getattr(value, "ActualStructure", None)
                setattr(value, "ActualStructure", self)

class express_algorithms_ActualGenericType(ActualType):

    def __init__(self, isEntity: str, label: str, express_algorithms_ActualGenericType: "ActualDataType" = None, ActualType: "express_algorithms_ActualAggregationType"):
        self.isEntity = isEntity
        self.label = label
        self.express_algorithms_ActualGenericType = express_algorithms_ActualGenericType
        
    @property
    def isEntity(self) -> str:
        return self.__isEntity

    @isEntity.setter
    def isEntity(self, isEntity: str):
        self.__isEntity = isEntity

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def express_algorithms_ActualGenericType(self):
        return self.__express_algorithms_ActualGenericType

    @express_algorithms_ActualGenericType.setter
    def express_algorithms_ActualGenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualGenericType__express_algorithms_ActualGenericType", None)
        self.__express_algorithms_ActualGenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualDataType477"):
                opp_val = getattr(old_value, "ActualDataType477", None)
                if opp_val == self:
                    setattr(old_value, "ActualDataType477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualDataType477"):
                opp_val = getattr(value, "ActualDataType477", None)
                setattr(value, "ActualDataType477", self)

class core_AGGREGATEType:

    pass
class algorithms_GenericElement:

    pass
class express_algorithms_ActualDataType(core_GenericType, algorithms_GenericElement):

    pass
class express_algorithms_ActualStructure(core_AGGREGATEType, algorithms_GenericElement):

    pass
class core_AnonymousType:

    pass
class ActualDataType:

    pass
class GenericType:

    pass
class express_algorithms_ActualTypeConstraint:

    def __init__(self, label: str, GenericType: "GenericType" = None, express_algorithms_ActualTypeConstraint: "ActualDataType" = None):
        self.label = label
        self.GenericType = GenericType
        self.express_algorithms_ActualTypeConstraint = express_algorithms_ActualTypeConstraint
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def express_algorithms_ActualTypeConstraint(self):
        return self.__express_algorithms_ActualTypeConstraint

    @express_algorithms_ActualTypeConstraint.setter
    def express_algorithms_ActualTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualTypeConstraint__express_algorithms_ActualTypeConstraint", None)
        self.__express_algorithms_ActualTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualDataType"):
                opp_val = getattr(old_value, "ActualDataType", None)
                if opp_val == self:
                    setattr(old_value, "ActualDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualDataType"):
                opp_val = getattr(value, "ActualDataType", None)
                setattr(value, "ActualDataType", self)

    @property
    def GenericType(self):
        return self.__GenericType

    @GenericType.setter
    def GenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualTypeConstraint__GenericType", None)
        self.__GenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core468"):
                opp_val = getattr(old_value, "core468", None)
                if opp_val == self:
                    setattr(old_value, "core468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core468"):
                opp_val = getattr(value, "core468", None)
                setattr(value, "core468", self)

class Algorithm:

    pass
class express_algorithms_Procedure(Algorithm):

    pass
class express_algorithms_Function(Algorithm):

    pass
class AlgorithmScope:

    pass
class express_core_AggregationType(ABC):

    def __init__(self, isUnique: str, ordering: str, express_core_AggregationType426: "SizeConstraint" = None, express_core_AggregationType: "SizeConstraint" = None):
        self.isUnique = isUnique
        self.ordering = ordering
        self.express_core_AggregationType426 = express_core_AggregationType426
        self.express_core_AggregationType = express_core_AggregationType
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def express_core_AggregationType426(self):
        return self.__express_core_AggregationType426

    @express_core_AggregationType426.setter
    def express_core_AggregationType426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_AggregationType__express_core_AggregationType426", None)
        self.__express_core_AggregationType426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint427"):
                opp_val = getattr(old_value, "SizeConstraint427", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint427"):
                opp_val = getattr(value, "SizeConstraint427", None)
                setattr(value, "SizeConstraint427", self)

    @property
    def express_core_AggregationType(self):
        return self.__express_core_AggregationType

    @express_core_AggregationType.setter
    def express_core_AggregationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_AggregationType__express_core_AggregationType", None)
        self.__express_core_AggregationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint424"):
                opp_val = getattr(old_value, "SizeConstraint424", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint424"):
                opp_val = getattr(value, "SizeConstraint424", None)
                setattr(value, "SizeConstraint424", self)

class express_core_ScopedId:

    def __init__(self, localName: str, express_core_ScopedId: "Scope" = None):
        self.localName = localName
        self.express_core_ScopedId = express_core_ScopedId
        
    @property
    def localName(self) -> str:
        return self.__localName

    @localName.setter
    def localName(self, localName: str):
        self.__localName = localName

    @property
    def express_core_ScopedId(self):
        return self.__express_core_ScopedId

    @express_core_ScopedId.setter
    def express_core_ScopedId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ScopedId__express_core_ScopedId", None)
        self.__express_core_ScopedId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope422"):
                opp_val = getattr(old_value, "Scope422", None)
                if opp_val == self:
                    setattr(old_value, "Scope422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope422"):
                opp_val = getattr(value, "Scope422", None)
                setattr(value, "Scope422", self)

class DomainRule:

    pass
class express_core_ParameterType(ABC):

    pass
class SelectType:

    pass
class express_core_Scope(ABC):

    pass
class core_CommonElement:

    pass
class core_Scope:

    pass
class express_core_Relationship:

    pass
class ArrayBound:

    pass
class ConcreteType:

    pass
class express_core_Remark:

    def __init__(self, isTagged: str, isTail: str, text: str, Schema381: set["Schema"] = None, Scope384: "Scope" = None, NamedElement: set["NamedElement"] = None):
        self.isTagged = isTagged
        self.isTail = isTail
        self.text = text
        self.Schema381 = Schema381 if Schema381 is not None else set()
        self.Scope384 = Scope384
        self.NamedElement = NamedElement if NamedElement is not None else set()
        
    @property
    def isTail(self) -> str:
        return self.__isTail

    @isTail.setter
    def isTail(self, isTail: str):
        self.__isTail = isTail

    @property
    def isTagged(self) -> str:
        return self.__isTagged

    @isTagged.setter
    def isTagged(self, isTagged: str):
        self.__isTagged = isTagged

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Schema381(self):
        return self.__Schema381

    @Schema381.setter
    def Schema381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Remark__Schema381", None)
        self.__Schema381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core382"):
                    opp_val = getattr(item, "core382", None)
                    
                    if opp_val == self:
                        setattr(item, "core382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core382"):
                    opp_val = getattr(item, "core382", None)
                    
                    setattr(item, "core382", self)
                    

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Remark__NamedElement", None)
        self.__NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core387"):
                    opp_val = getattr(item, "core387", None)
                    
                    if opp_val == self:
                        setattr(item, "core387", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core387"):
                    opp_val = getattr(item, "core387", None)
                    
                    setattr(item, "core387", self)
                    

    @property
    def Scope384(self):
        return self.__Scope384

    @Scope384.setter
    def Scope384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Remark__Scope384", None)
        self.__Scope384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core385"):
                opp_val = getattr(old_value, "core385", None)
                if opp_val == self:
                    setattr(old_value, "core385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core385"):
                opp_val = getattr(value, "core385", None)
                setattr(value, "core385", self)

class express_core_Role(ABC):

    pass
class DomainConstraint:

    pass
class express_core_SizeConstraint(DomainConstraint):

    def __init__(self, bound: str, core369: "express_core_AttributeType"):
        self.bound = bound
        
    @property
    def bound(self) -> str:
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound

class express_core_LengthConstraint(DomainConstraint):

    def __init__(self, maxLength: str, isFixed: str, core369: "express_core_AttributeType"):
        self.maxLength = maxLength
        self.isFixed = isFixed
        
    @property
    def isFixed(self) -> str:
        return self.__isFixed

    @isFixed.setter
    def isFixed(self, isFixed: str):
        self.__isFixed = isFixed

    @property
    def maxLength(self) -> str:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength

class express_core_Instance(ABC):

    pass
class LocalScope:

    pass
class express_core_AlgorithmScope(LocalScope):

    pass
class AnonymousType:

    pass
class express_core_SimpleType(AnonymousType):

    def __init__(self, id: str, AnonymousType: "express_core_AnonymousType"):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class LengthConstraint:

    pass
class ActualTypeConstraint:

    pass
class express_core_AttributeType(ABC):

    pass
class express_core_DomainConstraint(ABC):

    pass
class express_core_NamedElement(ABC):

    pass
class core_VariableType:

    pass
class NumericType:

    pass
class express_core_RealType(NumericType):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class TypeElement:

    pass
class express_core_Attribute(TypeElement):

    def __init__(self, isAbstract: str, position: str, EntityType349: set["EntityType"] = None, AttributeType343: "AttributeType" = None, SingleEntityType346: "SingleEntityType" = None):
        self.isAbstract = isAbstract
        self.position = position
        self.EntityType349 = EntityType349 if EntityType349 is not None else set()
        self.AttributeType343 = AttributeType343
        self.SingleEntityType346 = SingleEntityType346
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def EntityType349(self):
        return self.__EntityType349

    @EntityType349.setter
    def EntityType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Attribute__EntityType349", None)
        self.__EntityType349 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core350"):
                    opp_val = getattr(item, "core350", None)
                    
                    if opp_val == self:
                        setattr(item, "core350", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core350"):
                    opp_val = getattr(item, "core350", None)
                    
                    setattr(item, "core350", self)
                    

    @property
    def AttributeType343(self):
        return self.__AttributeType343

    @AttributeType343.setter
    def AttributeType343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Attribute__AttributeType343", None)
        self.__AttributeType343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core344"):
                opp_val = getattr(old_value, "core344", None)
                if opp_val == self:
                    setattr(old_value, "core344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core344"):
                opp_val = getattr(value, "core344", None)
                setattr(value, "core344", self)

    @property
    def SingleEntityType346(self):
        return self.__SingleEntityType346

    @SingleEntityType346.setter
    def SingleEntityType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Attribute__SingleEntityType346", None)
        self.__SingleEntityType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core347"):
                opp_val = getattr(old_value, "core347", None)
                if opp_val == self:
                    setattr(old_value, "core347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core347"):
                opp_val = getattr(value, "core347", None)
                setattr(value, "core347", self)

class express_core_UniqueRule(TypeElement):

    def __init__(self, position: str, EntityType316: "EntityType" = None, express_core_UniqueRule: set["Attribute"] = None):
        self.position = position
        self.EntityType316 = EntityType316
        self.express_core_UniqueRule = express_core_UniqueRule if express_core_UniqueRule is not None else set()
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def EntityType316(self):
        return self.__EntityType316

    @EntityType316.setter
    def EntityType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_UniqueRule__EntityType316", None)
        self.__EntityType316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core317"):
                opp_val = getattr(old_value, "core317", None)
                if opp_val == self:
                    setattr(old_value, "core317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core317"):
                opp_val = getattr(value, "core317", None)
                setattr(value, "core317", self)

    @property
    def express_core_UniqueRule(self):
        return self.__express_core_UniqueRule

    @express_core_UniqueRule.setter
    def express_core_UniqueRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_UniqueRule__express_core_UniqueRule", None)
        self.__express_core_UniqueRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute319"):
                    opp_val = getattr(item, "Attribute319", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute319"):
                    opp_val = getattr(item, "Attribute319", None)
                    
                    setattr(item, "Attribute319", self)
                    

class core_ConcreteType:

    pass
class SimpleType:

    pass
class express_core_BinaryType(SimpleType):

    pass
class express_core_LogicType(SimpleType):

    pass
class express_core_StringType(SimpleType):

    pass
class express_core_NumericType(SimpleType):

    pass
class Schema:

    pass
class express_core_InterfacedElement:

    def __init__(self, isUSE: str, Schema: "Schema" = None, SchemaElement311: "SchemaElement" = None, express_core_InterfacedElement: "ScopedId" = None):
        self.isUSE = isUSE
        self.Schema = Schema
        self.SchemaElement311 = SchemaElement311
        self.express_core_InterfacedElement = express_core_InterfacedElement
        
    @property
    def isUSE(self) -> str:
        return self.__isUSE

    @isUSE.setter
    def isUSE(self, isUSE: str):
        self.__isUSE = isUSE

    @property
    def SchemaElement311(self):
        return self.__SchemaElement311

    @SchemaElement311.setter
    def SchemaElement311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InterfacedElement__SchemaElement311", None)
        self.__SchemaElement311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core312"):
                opp_val = getattr(old_value, "core312", None)
                if opp_val == self:
                    setattr(old_value, "core312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core312"):
                opp_val = getattr(value, "core312", None)
                setattr(value, "core312", self)

    @property
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InterfacedElement__Schema", None)
        self.__Schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core309"):
                opp_val = getattr(old_value, "core309", None)
                if opp_val == self:
                    setattr(old_value, "core309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core309"):
                opp_val = getattr(value, "core309", None)
                setattr(value, "core309", self)

    @property
    def express_core_InterfacedElement(self):
        return self.__express_core_InterfacedElement

    @express_core_InterfacedElement.setter
    def express_core_InterfacedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InterfacedElement__express_core_InterfacedElement", None)
        self.__express_core_InterfacedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScopedId314"):
                opp_val = getattr(old_value, "ScopedId314", None)
                if opp_val == self:
                    setattr(old_value, "ScopedId314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScopedId314"):
                opp_val = getattr(value, "ScopedId314", None)
                setattr(value, "ScopedId314", self)

class Remark:

    pass
class core_ParameterType:

    pass
class express_core_InstantiableType(core_ParameterType, core_VariableType):

    pass
class Relationship:

    pass
class InverseAttribute:

    pass
class SchemaElement:

    pass
class express_core_CommonElement(SchemaElement):

    pass
class InterfacedElement:

    pass
class express_core_DataType(ABC):

    pass
class UniqueRule:

    pass
class RangeRole:

    pass
class core_InstantiableType:

    pass
class express_core_AnonymousType(core_ConcreteType, core_InstantiableType):

    pass
class core_NamedType:

    pass
class express_core_DefinedType(core_NamedType, core_ConcreteType):

    pass
class express_core_EntityType(core_NamedType, core_InstantiableType):

    def __init__(self, isAbstract: str, Role249: set["Role"] = None, Redeclaration252: set["Redeclaration"] = None, Attribute255: set["Attribute"] = None, RangeRole: set["RangeRole"] = None, SingleEntityType260: "SingleEntityType" = None, Extent263: set["Extent"] = None, InvertibleAttribute266: set["InvertibleAttribute"] = None, DomainRole269: set["DomainRole"] = None, UniqueRule: set["UniqueRule"] = None, InvertibleAttribute274: set["InvertibleAttribute"] = None, express_core_EntityType: set["EntityType"] = None):
        self.isAbstract = isAbstract
        self.Role249 = Role249 if Role249 is not None else set()
        self.Redeclaration252 = Redeclaration252 if Redeclaration252 is not None else set()
        self.Attribute255 = Attribute255 if Attribute255 is not None else set()
        self.RangeRole = RangeRole if RangeRole is not None else set()
        self.SingleEntityType260 = SingleEntityType260
        self.Extent263 = Extent263 if Extent263 is not None else set()
        self.InvertibleAttribute266 = InvertibleAttribute266 if InvertibleAttribute266 is not None else set()
        self.DomainRole269 = DomainRole269 if DomainRole269 is not None else set()
        self.UniqueRule = UniqueRule if UniqueRule is not None else set()
        self.InvertibleAttribute274 = InvertibleAttribute274 if InvertibleAttribute274 is not None else set()
        self.express_core_EntityType = express_core_EntityType if express_core_EntityType is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def Role249(self):
        return self.__Role249

    @Role249.setter
    def Role249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__Role249", None)
        self.__Role249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core250"):
                    opp_val = getattr(item, "core250", None)
                    
                    if opp_val == self:
                        setattr(item, "core250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core250"):
                    opp_val = getattr(item, "core250", None)
                    
                    setattr(item, "core250", self)
                    

    @property
    def Extent263(self):
        return self.__Extent263

    @Extent263.setter
    def Extent263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__Extent263", None)
        self.__Extent263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules264"):
                    opp_val = getattr(item, "rules264", None)
                    
                    if opp_val == self:
                        setattr(item, "rules264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules264"):
                    opp_val = getattr(item, "rules264", None)
                    
                    setattr(item, "rules264", self)
                    

    @property
    def InvertibleAttribute266(self):
        return self.__InvertibleAttribute266

    @InvertibleAttribute266.setter
    def InvertibleAttribute266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__InvertibleAttribute266", None)
        self.__InvertibleAttribute266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core267"):
                    opp_val = getattr(item, "core267", None)
                    
                    if opp_val == self:
                        setattr(item, "core267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core267"):
                    opp_val = getattr(item, "core267", None)
                    
                    setattr(item, "core267", self)
                    

    @property
    def express_core_EntityType(self):
        return self.__express_core_EntityType

    @express_core_EntityType.setter
    def express_core_EntityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__express_core_EntityType", None)
        self.__express_core_EntityType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EntityType277"):
                    opp_val = getattr(item, "EntityType277", None)
                    
                    if opp_val == self:
                        setattr(item, "EntityType277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EntityType277"):
                    opp_val = getattr(item, "EntityType277", None)
                    
                    setattr(item, "EntityType277", self)
                    

    @property
    def InvertibleAttribute274(self):
        return self.__InvertibleAttribute274

    @InvertibleAttribute274.setter
    def InvertibleAttribute274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__InvertibleAttribute274", None)
        self.__InvertibleAttribute274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core275"):
                    opp_val = getattr(item, "core275", None)
                    
                    if opp_val == self:
                        setattr(item, "core275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core275"):
                    opp_val = getattr(item, "core275", None)
                    
                    setattr(item, "core275", self)
                    

    @property
    def Redeclaration252(self):
        return self.__Redeclaration252

    @Redeclaration252.setter
    def Redeclaration252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__Redeclaration252", None)
        self.__Redeclaration252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core253"):
                    opp_val = getattr(item, "core253", None)
                    
                    if opp_val == self:
                        setattr(item, "core253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core253"):
                    opp_val = getattr(item, "core253", None)
                    
                    setattr(item, "core253", self)
                    

    @property
    def SingleEntityType260(self):
        return self.__SingleEntityType260

    @SingleEntityType260.setter
    def SingleEntityType260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__SingleEntityType260", None)
        self.__SingleEntityType260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core261"):
                opp_val = getattr(old_value, "core261", None)
                if opp_val == self:
                    setattr(old_value, "core261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core261"):
                opp_val = getattr(value, "core261", None)
                setattr(value, "core261", self)

    @property
    def UniqueRule(self):
        return self.__UniqueRule

    @UniqueRule.setter
    def UniqueRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__UniqueRule", None)
        self.__UniqueRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core272"):
                    opp_val = getattr(item, "core272", None)
                    
                    if opp_val == self:
                        setattr(item, "core272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core272"):
                    opp_val = getattr(item, "core272", None)
                    
                    setattr(item, "core272", self)
                    

    @property
    def RangeRole(self):
        return self.__RangeRole

    @RangeRole.setter
    def RangeRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__RangeRole", None)
        self.__RangeRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core258"):
                    opp_val = getattr(item, "core258", None)
                    
                    if opp_val == self:
                        setattr(item, "core258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core258"):
                    opp_val = getattr(item, "core258", None)
                    
                    setattr(item, "core258", self)
                    

    @property
    def DomainRole269(self):
        return self.__DomainRole269

    @DomainRole269.setter
    def DomainRole269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__DomainRole269", None)
        self.__DomainRole269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core270"):
                    opp_val = getattr(item, "core270", None)
                    
                    if opp_val == self:
                        setattr(item, "core270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core270"):
                    opp_val = getattr(item, "core270", None)
                    
                    setattr(item, "core270", self)
                    

    @property
    def Attribute255(self):
        return self.__Attribute255

    @Attribute255.setter
    def Attribute255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__Attribute255", None)
        self.__Attribute255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core256"):
                    opp_val = getattr(item, "core256", None)
                    
                    if opp_val == self:
                        setattr(item, "core256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core256"):
                    opp_val = getattr(item, "core256", None)
                    
                    setattr(item, "core256", self)
                    

class Role:

    pass
class express_core_DomainRole(Role):

    pass
class express_core_RangeRole(Role):

    pass
class Redeclaration:

    pass
class AttributeType:

    pass
class express_core_Redeclaration:

    def __init__(self, position: str, isMandatory: str, express_core_Redeclaration: "Expression" = None, express_core_Redeclaration228: "AttributeType" = None, express_core_Redeclaration230: "Redeclaration" = None, express_core_Redeclaration232: "SizeConstraint" = None, EntityType238: "EntityType" = None, express_core_Redeclaration241: "Attribute" = None, express_core_Redeclaration244: "Role" = None, express_core_Redeclaration246: "ScopedId" = None, express_core_Redeclaration235: "SizeConstraint" = None):
        self.position = position
        self.isMandatory = isMandatory
        self.express_core_Redeclaration = express_core_Redeclaration
        self.express_core_Redeclaration228 = express_core_Redeclaration228
        self.express_core_Redeclaration230 = express_core_Redeclaration230
        self.express_core_Redeclaration232 = express_core_Redeclaration232
        self.EntityType238 = EntityType238
        self.express_core_Redeclaration241 = express_core_Redeclaration241
        self.express_core_Redeclaration244 = express_core_Redeclaration244
        self.express_core_Redeclaration246 = express_core_Redeclaration246
        self.express_core_Redeclaration235 = express_core_Redeclaration235
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def isMandatory(self) -> str:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: str):
        self.__isMandatory = isMandatory

    @property
    def express_core_Redeclaration246(self):
        return self.__express_core_Redeclaration246

    @express_core_Redeclaration246.setter
    def express_core_Redeclaration246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration246", None)
        self.__express_core_Redeclaration246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScopedId247"):
                opp_val = getattr(old_value, "ScopedId247", None)
                if opp_val == self:
                    setattr(old_value, "ScopedId247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScopedId247"):
                opp_val = getattr(value, "ScopedId247", None)
                setattr(value, "ScopedId247", self)

    @property
    def express_core_Redeclaration228(self):
        return self.__express_core_Redeclaration228

    @express_core_Redeclaration228.setter
    def express_core_Redeclaration228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration228", None)
        self.__express_core_Redeclaration228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeType"):
                opp_val = getattr(old_value, "AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeType"):
                opp_val = getattr(value, "AttributeType", None)
                setattr(value, "AttributeType", self)

    @property
    def express_core_Redeclaration235(self):
        return self.__express_core_Redeclaration235

    @express_core_Redeclaration235.setter
    def express_core_Redeclaration235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration235", None)
        self.__express_core_Redeclaration235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint236"):
                opp_val = getattr(old_value, "SizeConstraint236", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint236"):
                opp_val = getattr(value, "SizeConstraint236", None)
                setattr(value, "SizeConstraint236", self)

    @property
    def express_core_Redeclaration230(self):
        return self.__express_core_Redeclaration230

    @express_core_Redeclaration230.setter
    def express_core_Redeclaration230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration230", None)
        self.__express_core_Redeclaration230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Redeclaration"):
                opp_val = getattr(old_value, "Redeclaration", None)
                if opp_val == self:
                    setattr(old_value, "Redeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Redeclaration"):
                opp_val = getattr(value, "Redeclaration", None)
                setattr(value, "Redeclaration", self)

    @property
    def express_core_Redeclaration(self):
        return self.__express_core_Redeclaration

    @express_core_Redeclaration.setter
    def express_core_Redeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration", None)
        self.__express_core_Redeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression226"):
                opp_val = getattr(old_value, "Expression226", None)
                if opp_val == self:
                    setattr(old_value, "Expression226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression226"):
                opp_val = getattr(value, "Expression226", None)
                setattr(value, "Expression226", self)

    @property
    def express_core_Redeclaration244(self):
        return self.__express_core_Redeclaration244

    @express_core_Redeclaration244.setter
    def express_core_Redeclaration244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration244", None)
        self.__express_core_Redeclaration244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role"):
                opp_val = getattr(old_value, "Role", None)
                if opp_val == self:
                    setattr(old_value, "Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role"):
                opp_val = getattr(value, "Role", None)
                setattr(value, "Role", self)

    @property
    def EntityType238(self):
        return self.__EntityType238

    @EntityType238.setter
    def EntityType238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__EntityType238", None)
        self.__EntityType238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core239"):
                opp_val = getattr(old_value, "core239", None)
                if opp_val == self:
                    setattr(old_value, "core239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core239"):
                opp_val = getattr(value, "core239", None)
                setattr(value, "core239", self)

    @property
    def express_core_Redeclaration241(self):
        return self.__express_core_Redeclaration241

    @express_core_Redeclaration241.setter
    def express_core_Redeclaration241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration241", None)
        self.__express_core_Redeclaration241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute242"):
                opp_val = getattr(old_value, "Attribute242", None)
                if opp_val == self:
                    setattr(old_value, "Attribute242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute242"):
                opp_val = getattr(value, "Attribute242", None)
                setattr(value, "Attribute242", self)

    @property
    def express_core_Redeclaration232(self):
        return self.__express_core_Redeclaration232

    @express_core_Redeclaration232.setter
    def express_core_Redeclaration232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration232", None)
        self.__express_core_Redeclaration232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint233"):
                opp_val = getattr(old_value, "SizeConstraint233", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint233"):
                opp_val = getattr(value, "SizeConstraint233", None)
                setattr(value, "SizeConstraint233", self)

class ConcreteAggregationType:

    pass
class express_core_BAGType(ConcreteAggregationType):

    pass
class express_core_ARRAYType(ConcreteAggregationType):

    def __init__(self, isOptional: str, express_core_ARRAYType: "ArrayBound" = None, express_core_ARRAYType465: "ArrayBound" = None):
        self.isOptional = isOptional
        self.express_core_ARRAYType = express_core_ARRAYType
        self.express_core_ARRAYType465 = express_core_ARRAYType465
        
    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

    @property
    def express_core_ARRAYType(self):
        return self.__express_core_ARRAYType

    @express_core_ARRAYType.setter
    def express_core_ARRAYType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ARRAYType__express_core_ARRAYType", None)
        self.__express_core_ARRAYType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound463"):
                opp_val = getattr(old_value, "ArrayBound463", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound463"):
                opp_val = getattr(value, "ArrayBound463", None)
                setattr(value, "ArrayBound463", self)

    @property
    def express_core_ARRAYType465(self):
        return self.__express_core_ARRAYType465

    @express_core_ARRAYType465.setter
    def express_core_ARRAYType465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ARRAYType__express_core_ARRAYType465", None)
        self.__express_core_ARRAYType465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound466"):
                opp_val = getattr(old_value, "ArrayBound466", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound466"):
                opp_val = getattr(value, "ArrayBound466", None)
                setattr(value, "ArrayBound466", self)

class express_core_SETType(ConcreteAggregationType):

    pass
class express_core_LISTType(ConcreteAggregationType):

    pass
class express_core_ArrayBound:

    def __init__(self, bound: str, express_core_ArrayBound: "Expression" = None):
        self.bound = bound
        self.express_core_ArrayBound = express_core_ArrayBound
        
    @property
    def bound(self) -> str:
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound

    @property
    def express_core_ArrayBound(self):
        return self.__express_core_ArrayBound

    @express_core_ArrayBound.setter
    def express_core_ArrayBound(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ArrayBound__express_core_ArrayBound", None)
        self.__express_core_ArrayBound = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression224"):
                opp_val = getattr(old_value, "Expression224", None)
                if opp_val == self:
                    setattr(old_value, "Expression224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression224"):
                opp_val = getattr(value, "Expression224", None)
                setattr(value, "Expression224", self)

class core_AttributeType:

    pass
class express_core_NamedType(core_Scope, core_CommonElement, core_InstantiableType, core_AttributeType):

    pass
class express_core_GeneralizedType(core_AttributeType, core_ParameterType):

    pass
class core_DataType:

    pass
class express_core_VariableType(core_AttributeType, core_DataType):

    pass
class EnumerationType:

    pass
class GeneralAggregationType:

    pass
class express_core_GeneralARRAYType(GeneralAggregationType):

    def __init__(self, isOptional: str, express_core_GeneralARRAYType: "ArrayBound" = None, express_core_GeneralARRAYType402: "ArrayBound" = None):
        self.isOptional = isOptional
        self.express_core_GeneralARRAYType = express_core_GeneralARRAYType
        self.express_core_GeneralARRAYType402 = express_core_GeneralARRAYType402
        
    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

    @property
    def express_core_GeneralARRAYType402(self):
        return self.__express_core_GeneralARRAYType402

    @express_core_GeneralARRAYType402.setter
    def express_core_GeneralARRAYType402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_GeneralARRAYType__express_core_GeneralARRAYType402", None)
        self.__express_core_GeneralARRAYType402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound403"):
                opp_val = getattr(old_value, "ArrayBound403", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound403"):
                opp_val = getattr(value, "ArrayBound403", None)
                setattr(value, "ArrayBound403", self)

    @property
    def express_core_GeneralARRAYType(self):
        return self.__express_core_GeneralARRAYType

    @express_core_GeneralARRAYType.setter
    def express_core_GeneralARRAYType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_GeneralARRAYType__express_core_GeneralARRAYType", None)
        self.__express_core_GeneralARRAYType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound"):
                opp_val = getattr(old_value, "ArrayBound", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound"):
                opp_val = getattr(value, "ArrayBound", None)
                setattr(value, "ArrayBound", self)

class express_core_GeneralSETType(GeneralAggregationType):

    pass
class express_core_GeneralLISTType(GeneralAggregationType):

    pass
class express_core_GeneralBAGType(GeneralAggregationType):

    pass
class DefinedType:

    pass
class express_core_SelectType(DefinedType):

    def __init__(self, isExtensible: str, isEntity: str, NamedType438: set["NamedType"] = None, SelectType441: set["SelectType"] = None, SelectType444: "SelectType" = None, express_core_SelectType: set["NamedType"] = None):
        self.isExtensible = isExtensible
        self.isEntity = isEntity
        self.NamedType438 = NamedType438 if NamedType438 is not None else set()
        self.SelectType441 = SelectType441 if SelectType441 is not None else set()
        self.SelectType444 = SelectType444
        self.express_core_SelectType = express_core_SelectType if express_core_SelectType is not None else set()
        
    @property
    def isExtensible(self) -> str:
        return self.__isExtensible

    @isExtensible.setter
    def isExtensible(self, isExtensible: str):
        self.__isExtensible = isExtensible

    @property
    def isEntity(self) -> str:
        return self.__isEntity

    @isEntity.setter
    def isEntity(self, isEntity: str):
        self.__isEntity = isEntity

    @property
    def SelectType444(self):
        return self.__SelectType444

    @SelectType444.setter
    def SelectType444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__SelectType444", None)
        self.__SelectType444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core445"):
                opp_val = getattr(old_value, "core445", None)
                if opp_val == self:
                    setattr(old_value, "core445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core445"):
                opp_val = getattr(value, "core445", None)
                setattr(value, "core445", self)

    @property
    def express_core_SelectType(self):
        return self.__express_core_SelectType

    @express_core_SelectType.setter
    def express_core_SelectType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__express_core_SelectType", None)
        self.__express_core_SelectType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedType447"):
                    opp_val = getattr(item, "NamedType447", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedType447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedType447"):
                    opp_val = getattr(item, "NamedType447", None)
                    
                    setattr(item, "NamedType447", self)
                    

    @property
    def NamedType438(self):
        return self.__NamedType438

    @NamedType438.setter
    def NamedType438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__NamedType438", None)
        self.__NamedType438 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core439"):
                    opp_val = getattr(item, "core439", None)
                    
                    if opp_val == self:
                        setattr(item, "core439", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core439"):
                    opp_val = getattr(item, "core439", None)
                    
                    setattr(item, "core439", self)
                    

    @property
    def SelectType441(self):
        return self.__SelectType441

    @SelectType441.setter
    def SelectType441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__SelectType441", None)
        self.__SelectType441 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core442"):
                    opp_val = getattr(item, "core442", None)
                    
                    if opp_val == self:
                        setattr(item, "core442", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core442"):
                    opp_val = getattr(item, "core442", None)
                    
                    setattr(item, "core442", self)
                    

class express_core_SpecializedType(DefinedType):

    pass
class express_core_EnumerationType(DefinedType):

    def __init__(self, isExtensible: str, express_core_EnumerationType: set["EnumerationItem"] = None, EnumerationType: set["EnumerationType"] = None, EnumerationType221: "EnumerationType" = None, EnumerationItem217: set["EnumerationItem"] = None):
        self.isExtensible = isExtensible
        self.express_core_EnumerationType = express_core_EnumerationType if express_core_EnumerationType is not None else set()
        self.EnumerationType = EnumerationType if EnumerationType is not None else set()
        self.EnumerationType221 = EnumerationType221
        self.EnumerationItem217 = EnumerationItem217 if EnumerationItem217 is not None else set()
        
    @property
    def isExtensible(self) -> str:
        return self.__isExtensible

    @isExtensible.setter
    def isExtensible(self, isExtensible: str):
        self.__isExtensible = isExtensible

    @property
    def EnumerationType(self):
        return self.__EnumerationType

    @EnumerationType.setter
    def EnumerationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__EnumerationType", None)
        self.__EnumerationType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core219"):
                    opp_val = getattr(item, "core219", None)
                    
                    if opp_val == self:
                        setattr(item, "core219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core219"):
                    opp_val = getattr(item, "core219", None)
                    
                    setattr(item, "core219", self)
                    

    @property
    def EnumerationType221(self):
        return self.__EnumerationType221

    @EnumerationType221.setter
    def EnumerationType221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__EnumerationType221", None)
        self.__EnumerationType221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core222"):
                opp_val = getattr(old_value, "core222", None)
                if opp_val == self:
                    setattr(old_value, "core222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core222"):
                opp_val = getattr(value, "core222", None)
                setattr(value, "core222", self)

    @property
    def express_core_EnumerationType(self):
        return self.__express_core_EnumerationType

    @express_core_EnumerationType.setter
    def express_core_EnumerationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__express_core_EnumerationType", None)
        self.__express_core_EnumerationType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumerationItem215"):
                    opp_val = getattr(item, "EnumerationItem215", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumerationItem215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumerationItem215"):
                    opp_val = getattr(item, "EnumerationItem215", None)
                    
                    setattr(item, "EnumerationItem215", self)
                    

    @property
    def EnumerationItem217(self):
        return self.__EnumerationItem217

    @EnumerationItem217.setter
    def EnumerationItem217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__EnumerationItem217", None)
        self.__EnumerationItem217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "instances"):
                    opp_val = getattr(item, "instances", None)
                    
                    if opp_val == self:
                        setattr(item, "instances", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "instances"):
                    opp_val = getattr(item, "instances", None)
                    
                    setattr(item, "instances", self)
                    

class InvertibleAttribute:

    pass
class DomainRole:

    pass
class DataType:

    pass
class express_core_PartialEntityType(DataType):

    pass
class Scope:

    pass
class express_core_LocalScope(Scope):

    pass
class express_core_Schema(Scope):

    def __init__(self, name: str, version: str, Remark: set["Remark"] = None, InterfacedElement: set["InterfacedElement"] = None, SchemaElement: set["SchemaElement"] = None, SchemaElement290: set["SchemaElement"] = None, Scope: "express_core_Expression", core336: "express_core_NamedElement", Scope422: "express_core_ScopedId", core385: "express_core_Remark"):
        self.name = name
        self.version = version
        self.Remark = Remark if Remark is not None else set()
        self.InterfacedElement = InterfacedElement if InterfacedElement is not None else set()
        self.SchemaElement = SchemaElement if SchemaElement is not None else set()
        self.SchemaElement290 = SchemaElement290 if SchemaElement290 is not None else set()
        
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
    def SchemaElement290(self):
        return self.__SchemaElement290

    @SchemaElement290.setter
    def SchemaElement290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__SchemaElement290", None)
        self.__SchemaElement290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core291"):
                    opp_val = getattr(item, "core291", None)
                    
                    if opp_val == self:
                        setattr(item, "core291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core291"):
                    opp_val = getattr(item, "core291", None)
                    
                    setattr(item, "core291", self)
                    

    @property
    def Remark(self):
        return self.__Remark

    @Remark.setter
    def Remark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__Remark", None)
        self.__Remark = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core284"):
                    opp_val = getattr(item, "core284", None)
                    
                    if opp_val == self:
                        setattr(item, "core284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core284"):
                    opp_val = getattr(item, "core284", None)
                    
                    setattr(item, "core284", self)
                    

    @property
    def InterfacedElement(self):
        return self.__InterfacedElement

    @InterfacedElement.setter
    def InterfacedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__InterfacedElement", None)
        self.__InterfacedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core286"):
                    opp_val = getattr(item, "core286", None)
                    
                    if opp_val == self:
                        setattr(item, "core286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core286"):
                    opp_val = getattr(item, "core286", None)
                    
                    setattr(item, "core286", self)
                    

    @property
    def SchemaElement(self):
        return self.__SchemaElement

    @SchemaElement.setter
    def SchemaElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__SchemaElement", None)
        self.__SchemaElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core288"):
                    opp_val = getattr(item, "core288", None)
                    
                    if opp_val == self:
                        setattr(item, "core288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core288"):
                    opp_val = getattr(item, "core288", None)
                    
                    setattr(item, "core288", self)
                    

class Instance:

    pass
class express_instances_Indeterminate(Instance):

    pass
class express_instances_PartialEntityValue(Instance):

    pass
class express_instances_TypedInstance(Instance):

    pass
class express_instances_ConcreteValue(Instance):

    pass
class express_core_Expression:

    def __init__(self, text: str, express_core_Expression: "Instance" = None, express_core_Expression207: "Scope" = None, express_core_Expression209: "DataType" = None):
        self.text = text
        self.express_core_Expression = express_core_Expression
        self.express_core_Expression207 = express_core_Expression207
        self.express_core_Expression209 = express_core_Expression209
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def express_core_Expression209(self):
        return self.__express_core_Expression209

    @express_core_Expression209.setter
    def express_core_Expression209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Expression__express_core_Expression209", None)
        self.__express_core_Expression209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def express_core_Expression207(self):
        return self.__express_core_Expression207

    @express_core_Expression207.setter
    def express_core_Expression207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Expression__express_core_Expression207", None)
        self.__express_core_Expression207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope"):
                opp_val = getattr(old_value, "Scope", None)
                if opp_val == self:
                    setattr(old_value, "Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope"):
                opp_val = getattr(value, "Scope", None)
                setattr(value, "Scope", self)

    @property
    def express_core_Expression(self):
        return self.__express_core_Expression

    @express_core_Expression.setter
    def express_core_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Expression__express_core_Expression", None)
        self.__express_core_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance"):
                opp_val = getattr(old_value, "Instance", None)
                if opp_val == self:
                    setattr(old_value, "Instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance"):
                opp_val = getattr(value, "Instance", None)
                setattr(value, "Instance", self)

class InstantiableType:

    pass
class express_core_ConcreteType(InstantiableType):

    pass
class core_AggregationType:

    pass
class express_core_ConcreteAggregationType(core_AnonymousType, core_AggregationType):

    pass
class express_algorithms_ActualAggregationType(core_AggregationType, core_ActualType):

    pass
class core_GeneralizedType:

    pass
class express_core_GeneralAggregationType(core_AggregationType, core_GeneralizedType):

    pass
class core_TypeElement:

    pass
class express_instances_EnumerationItem(instances_TypedInstance, instances_ConcreteValue, core_TypeElement):

    def __init__(self, position: str, EnumerationType572: "EnumerationType" = None):
        self.position = position
        self.EnumerationType572 = EnumerationType572
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def EnumerationType572(self):
        return self.__EnumerationType572

    @EnumerationType572.setter
    def EnumerationType572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_EnumerationItem__EnumerationType572", None)
        self.__EnumerationType572 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core573"):
                opp_val = getattr(old_value, "core573", None)
                if opp_val == self:
                    setattr(old_value, "core573", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core573"):
                opp_val = getattr(value, "core573", None)
                setattr(value, "core573", self)

class core_DomainConstraint:

    pass
class express_core_DomainRule(core_TypeElement, core_DomainConstraint):

    def __init__(self, position: str):
        self.position = position
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

class ActualStructureConstraint:

    pass
class ParameterType:

    pass
class SizeConstraint:

    pass
class GeneralizedType:

    pass
class express_core_GenericType(GeneralizedType):

    def __init__(self, isEntity: str, ActualTypeConstraint: "ActualTypeConstraint" = None, GeneralizedType: "express_core_GeneralAggregationType", core436: "express_core_ParameterType"):
        self.isEntity = isEntity
        self.ActualTypeConstraint = ActualTypeConstraint
        
    @property
    def isEntity(self) -> str:
        return self.__isEntity

    @isEntity.setter
    def isEntity(self, isEntity: str):
        self.__isEntity = isEntity

    @property
    def ActualTypeConstraint(self):
        return self.__ActualTypeConstraint

    @ActualTypeConstraint.setter
    def ActualTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_GenericType__ActualTypeConstraint", None)
        self.__ActualTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "algorithms352"):
                opp_val = getattr(old_value, "algorithms352", None)
                if opp_val == self:
                    setattr(old_value, "algorithms352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "algorithms352"):
                opp_val = getattr(value, "algorithms352", None)
                setattr(value, "algorithms352", self)

class express_core_AGGREGATEType(GeneralizedType):

    pass
class PartialEntityType:

    pass
class express_core_SingleEntityType:

    pass
class NamedElement:

    pass
class express_core_SchemaElement(NamedElement):

    pass
class express_core_LocalElement(NamedElement):

    pass
class express_core_TypeElement(NamedElement):

    pass
class NamedType:

    pass
class ListMember:

    pass
class RepeatCount:

    pass
class express_expressions_MemberBinding:

    def __init__(self, position: str, express_expressions_MemberBinding: "RepeatCount" = None, express_expressions_MemberBinding177: set["ListMember"] = None, express_expressions_MemberBinding179: "Expression" = None):
        self.position = position
        self.express_expressions_MemberBinding = express_expressions_MemberBinding
        self.express_expressions_MemberBinding177 = express_expressions_MemberBinding177 if express_expressions_MemberBinding177 is not None else set()
        self.express_expressions_MemberBinding179 = express_expressions_MemberBinding179
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def express_expressions_MemberBinding(self):
        return self.__express_expressions_MemberBinding

    @express_expressions_MemberBinding.setter
    def express_expressions_MemberBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_MemberBinding__express_expressions_MemberBinding", None)
        self.__express_expressions_MemberBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepeatCount"):
                opp_val = getattr(old_value, "RepeatCount", None)
                if opp_val == self:
                    setattr(old_value, "RepeatCount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepeatCount"):
                opp_val = getattr(value, "RepeatCount", None)
                setattr(value, "RepeatCount", self)

    @property
    def express_expressions_MemberBinding177(self):
        return self.__express_expressions_MemberBinding177

    @express_expressions_MemberBinding177.setter
    def express_expressions_MemberBinding177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_MemberBinding__express_expressions_MemberBinding177", None)
        self.__express_expressions_MemberBinding177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ListMember"):
                    opp_val = getattr(item, "ListMember", None)
                    
                    if opp_val == self:
                        setattr(item, "ListMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ListMember"):
                    opp_val = getattr(item, "ListMember", None)
                    
                    setattr(item, "ListMember", self)
                    

    @property
    def express_expressions_MemberBinding179(self):
        return self.__express_expressions_MemberBinding179

    @express_expressions_MemberBinding179.setter
    def express_expressions_MemberBinding179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_MemberBinding__express_expressions_MemberBinding179", None)
        self.__express_expressions_MemberBinding179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression180"):
                opp_val = getattr(old_value, "Expression180", None)
                if opp_val == self:
                    setattr(old_value, "Expression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression180"):
                opp_val = getattr(value, "Expression180", None)
                setattr(value, "Expression180", self)

class FunctionResult:

    pass
class Function:

    pass
class AttributeValue:

    pass
class express_expressions_AttributeBinding:

    def __init__(self, position: str, express_expressions_AttributeBinding: "Expression" = None, express_expressions_AttributeBinding165: "AttributeValue" = None, express_expressions_AttributeBinding167: "ExplicitAttribute" = None):
        self.position = position
        self.express_expressions_AttributeBinding = express_expressions_AttributeBinding
        self.express_expressions_AttributeBinding165 = express_expressions_AttributeBinding165
        self.express_expressions_AttributeBinding167 = express_expressions_AttributeBinding167
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def express_expressions_AttributeBinding(self):
        return self.__express_expressions_AttributeBinding

    @express_expressions_AttributeBinding.setter
    def express_expressions_AttributeBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeBinding__express_expressions_AttributeBinding", None)
        self.__express_expressions_AttributeBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression163"):
                opp_val = getattr(old_value, "Expression163", None)
                if opp_val == self:
                    setattr(old_value, "Expression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression163"):
                opp_val = getattr(value, "Expression163", None)
                setattr(value, "Expression163", self)

    @property
    def express_expressions_AttributeBinding165(self):
        return self.__express_expressions_AttributeBinding165

    @express_expressions_AttributeBinding165.setter
    def express_expressions_AttributeBinding165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeBinding__express_expressions_AttributeBinding165", None)
        self.__express_expressions_AttributeBinding165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeValue"):
                opp_val = getattr(old_value, "AttributeValue", None)
                if opp_val == self:
                    setattr(old_value, "AttributeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeValue"):
                opp_val = getattr(value, "AttributeValue", None)
                setattr(value, "AttributeValue", self)

    @property
    def express_expressions_AttributeBinding167(self):
        return self.__express_expressions_AttributeBinding167

    @express_expressions_AttributeBinding167.setter
    def express_expressions_AttributeBinding167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeBinding__express_expressions_AttributeBinding167", None)
        self.__express_expressions_AttributeBinding167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExplicitAttribute168"):
                opp_val = getattr(old_value, "ExplicitAttribute168", None)
                if opp_val == self:
                    setattr(old_value, "ExplicitAttribute168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExplicitAttribute168"):
                opp_val = getattr(value, "ExplicitAttribute168", None)
                setattr(value, "ExplicitAttribute168", self)

class QueryVariable:

    pass
class core_Expression:

    pass
class Constant:

    pass
class Attribute:

    pass
class express_core_DerivedAttribute(Attribute):

    pass
class express_core_InverseAttribute(Attribute):

    def __init__(self, isUnique: str, DomainRole: "DomainRole" = None, InvertibleAttribute: "InvertibleAttribute" = None, Attribute242: "express_core_Redeclaration", core367: "express_core_AttributeType", Attribute537: "express_instances_RoleName", core256: "express_core_EntityType", Attribute319: "express_core_UniqueRule", Attribute153: "express_expressions_UsedInRef", Attribute: "express_expressions_AttributeRef", core187: "express_core_SingleEntityType"):
        self.isUnique = isUnique
        self.DomainRole = DomainRole
        self.InvertibleAttribute = InvertibleAttribute
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def DomainRole(self):
        return self.__DomainRole

    @DomainRole.setter
    def DomainRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InverseAttribute__DomainRole", None)
        self.__DomainRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core211"):
                opp_val = getattr(old_value, "core211", None)
                if opp_val == self:
                    setattr(old_value, "core211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core211"):
                opp_val = getattr(value, "core211", None)
                setattr(value, "core211", self)

    @property
    def InvertibleAttribute(self):
        return self.__InvertibleAttribute

    @InvertibleAttribute.setter
    def InvertibleAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InverseAttribute__InvertibleAttribute", None)
        self.__InvertibleAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core213"):
                opp_val = getattr(old_value, "core213", None)
                if opp_val == self:
                    setattr(old_value, "core213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core213"):
                opp_val = getattr(value, "core213", None)
                setattr(value, "core213", self)

class express_core_ExplicitAttribute(Attribute):

    def __init__(self, isOptional: str, Attribute242: "express_core_Redeclaration", core367: "express_core_AttributeType", Attribute537: "express_instances_RoleName", core256: "express_core_EntityType", Attribute319: "express_core_UniqueRule", Attribute153: "express_expressions_UsedInRef", Attribute: "express_expressions_AttributeRef", core187: "express_core_SingleEntityType"):
        self.isOptional = isOptional
        
    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

class Selector:

    pass
class express_expressions_GroupRef(Selector):

    def __init__(self, id: str, express_expressions_GroupRef: "SingleEntityType" = None):
        self.id = id
        self.express_expressions_GroupRef = express_expressions_GroupRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_GroupRef(self):
        return self.__express_expressions_GroupRef

    @express_expressions_GroupRef.setter
    def express_expressions_GroupRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_GroupRef__express_expressions_GroupRef", None)
        self.__express_expressions_GroupRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType149"):
                opp_val = getattr(old_value, "SingleEntityType149", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType149"):
                opp_val = getattr(value, "SingleEntityType149", None)
                setattr(value, "SingleEntityType149", self)

class express_expressions_UsedInRef(Selector):

    pass
class express_expressions_AttributeRef(Selector):

    def __init__(self, id: str, express_expressions_AttributeRef: "Attribute" = None):
        self.id = id
        self.express_expressions_AttributeRef = express_expressions_AttributeRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_AttributeRef(self):
        return self.__express_expressions_AttributeRef

    @express_expressions_AttributeRef.setter
    def express_expressions_AttributeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeRef__express_expressions_AttributeRef", None)
        self.__express_expressions_AttributeRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute"):
                opp_val = getattr(old_value, "Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute"):
                opp_val = getattr(value, "Attribute", None)
                setattr(value, "Attribute", self)

class ProcedureCall:

    pass
class Parameter:

    pass
class express_algorithms_InParameter(Parameter):

    pass
class FunctionCall:

    pass
class express_expressions_ActualParameter:

    def __init__(self, position: str, FunctionCall: "FunctionCall" = None, express_expressions_ActualParameter: "Parameter" = None, express_expressions_ActualParameter138: "VARExpression" = None, express_expressions_ActualParameter141: "Expression" = None, ProcedureCall: "ProcedureCall" = None):
        self.position = position
        self.FunctionCall = FunctionCall
        self.express_expressions_ActualParameter = express_expressions_ActualParameter
        self.express_expressions_ActualParameter138 = express_expressions_ActualParameter138
        self.express_expressions_ActualParameter141 = express_expressions_ActualParameter141
        self.ProcedureCall = ProcedureCall
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def FunctionCall(self):
        return self.__FunctionCall

    @FunctionCall.setter
    def FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__FunctionCall", None)
        self.__FunctionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions135"):
                opp_val = getattr(old_value, "expressions135", None)
                if opp_val == self:
                    setattr(old_value, "expressions135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions135"):
                opp_val = getattr(value, "expressions135", None)
                setattr(value, "expressions135", self)

    @property
    def express_expressions_ActualParameter(self):
        return self.__express_expressions_ActualParameter

    @express_expressions_ActualParameter.setter
    def express_expressions_ActualParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__express_expressions_ActualParameter", None)
        self.__express_expressions_ActualParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter"):
                opp_val = getattr(old_value, "Parameter", None)
                if opp_val == self:
                    setattr(old_value, "Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter"):
                opp_val = getattr(value, "Parameter", None)
                setattr(value, "Parameter", self)

    @property
    def ProcedureCall(self):
        return self.__ProcedureCall

    @ProcedureCall.setter
    def ProcedureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__ProcedureCall", None)
        self.__ProcedureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements"):
                opp_val = getattr(old_value, "statements", None)
                if opp_val == self:
                    setattr(old_value, "statements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements"):
                opp_val = getattr(value, "statements", None)
                setattr(value, "statements", self)

    @property
    def express_expressions_ActualParameter138(self):
        return self.__express_expressions_ActualParameter138

    @express_expressions_ActualParameter138.setter
    def express_expressions_ActualParameter138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__express_expressions_ActualParameter138", None)
        self.__express_expressions_ActualParameter138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARExpression139"):
                opp_val = getattr(old_value, "VARExpression139", None)
                if opp_val == self:
                    setattr(old_value, "VARExpression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARExpression139"):
                opp_val = getattr(value, "VARExpression139", None)
                setattr(value, "VARExpression139", self)

    @property
    def express_expressions_ActualParameter141(self):
        return self.__express_expressions_ActualParameter141

    @express_expressions_ActualParameter141.setter
    def express_expressions_ActualParameter141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__express_expressions_ActualParameter141", None)
        self.__express_expressions_ActualParameter141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression142"):
                opp_val = getattr(old_value, "Expression142", None)
                if opp_val == self:
                    setattr(old_value, "Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression142"):
                opp_val = getattr(value, "Expression142", None)
                setattr(value, "Expression142", self)

class MemberBinding:

    pass
class GenericAggregate:

    pass
class VariableType:

    pass
class express_core_ActualType(VariableType):

    pass
class AttributeBinding:

    pass
class PartialEntityValue:

    pass
class express_instances_EntityValue(PartialEntityValue):

    pass
class IndexOperation:

    pass
class express_expressions_StringIndex(IndexOperation):

    pass
class express_expressions_AggregateIndex(IndexOperation):

    pass
class express_expressions_BinaryIndex(IndexOperation):

    pass
class SimpleValue:

    pass
class express_instances_NumberValue(SimpleValue):

    pass
class express_instances_LogicalValue(SimpleValue):

    pass
class express_instances_BinaryValue(SimpleValue):

    pass
class express_instances_StringValue(SimpleValue):

    pass
class Operation:

    pass
class express_expressions_Coercion(Operation):

    pass
class express_expressions_UnaryOperation(Operation):

    def __init__(self, operator: str, express_expressions_UnaryOperation: "Expression" = None):
        self.operator = operator
        self.express_expressions_UnaryOperation = express_expressions_UnaryOperation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def express_expressions_UnaryOperation(self):
        return self.__express_expressions_UnaryOperation

    @express_expressions_UnaryOperation.setter
    def express_expressions_UnaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_UnaryOperation__express_expressions_UnaryOperation", None)
        self.__express_expressions_UnaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression151"):
                opp_val = getattr(old_value, "Expression151", None)
                if opp_val == self:
                    setattr(old_value, "Expression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression151"):
                opp_val = getattr(value, "Expression151", None)
                setattr(value, "Expression151", self)

class express_expressions_BinaryOperation(Operation):

    def __init__(self, operator: str, express_expressions_BinaryOperation: "Expression" = None, express_expressions_BinaryOperation113: "Expression" = None):
        self.operator = operator
        self.express_expressions_BinaryOperation = express_expressions_BinaryOperation
        self.express_expressions_BinaryOperation113 = express_expressions_BinaryOperation113
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def express_expressions_BinaryOperation(self):
        return self.__express_expressions_BinaryOperation

    @express_expressions_BinaryOperation.setter
    def express_expressions_BinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_BinaryOperation__express_expressions_BinaryOperation", None)
        self.__express_expressions_BinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression111"):
                opp_val = getattr(old_value, "Expression111", None)
                if opp_val == self:
                    setattr(old_value, "Expression111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression111"):
                opp_val = getattr(value, "Expression111", None)
                setattr(value, "Expression111", self)

    @property
    def express_expressions_BinaryOperation113(self):
        return self.__express_expressions_BinaryOperation113

    @express_expressions_BinaryOperation113.setter
    def express_expressions_BinaryOperation113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_BinaryOperation__express_expressions_BinaryOperation113", None)
        self.__express_expressions_BinaryOperation113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression114"):
                opp_val = getattr(old_value, "Expression114", None)
                if opp_val == self:
                    setattr(old_value, "Expression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression114"):
                opp_val = getattr(value, "Expression114", None)
                setattr(value, "Expression114", self)

class Indeterminate:

    pass
class EnumerationItem:

    pass
class Primary:

    pass
class express_expressions_Literal(Primary):

    pass
class express_expressions_VariableRef(Primary):

    def __init__(self, id: str, express_expressions_VariableRef: "NamedVariable" = None):
        self.id = id
        self.express_expressions_VariableRef = express_expressions_VariableRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_VariableRef(self):
        return self.__express_expressions_VariableRef

    @express_expressions_VariableRef.setter
    def express_expressions_VariableRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_VariableRef__express_expressions_VariableRef", None)
        self.__express_expressions_VariableRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedVariable"):
                opp_val = getattr(old_value, "NamedVariable", None)
                if opp_val == self:
                    setattr(old_value, "NamedVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedVariable"):
                opp_val = getattr(value, "NamedVariable", None)
                setattr(value, "NamedVariable", self)

class express_expressions_ExtentRef(Primary):

    def __init__(self, id: str, express_expressions_ExtentRef: "NamedType" = None):
        self.id = id
        self.express_expressions_ExtentRef = express_expressions_ExtentRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_ExtentRef(self):
        return self.__express_expressions_ExtentRef

    @express_expressions_ExtentRef.setter
    def express_expressions_ExtentRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ExtentRef__express_expressions_ExtentRef", None)
        self.__express_expressions_ExtentRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedType"):
                opp_val = getattr(old_value, "NamedType", None)
                if opp_val == self:
                    setattr(old_value, "NamedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedType"):
                opp_val = getattr(value, "NamedType", None)
                setattr(value, "NamedType", self)

class express_expressions_ConstantRef(Primary):

    def __init__(self, id: str, express_expressions_ConstantRef: "Constant" = None):
        self.id = id
        self.express_expressions_ConstantRef = express_expressions_ConstantRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_ConstantRef(self):
        return self.__express_expressions_ConstantRef

    @express_expressions_ConstantRef.setter
    def express_expressions_ConstantRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ConstantRef__express_expressions_ConstantRef", None)
        self.__express_expressions_ConstantRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constant"):
                opp_val = getattr(old_value, "Constant", None)
                if opp_val == self:
                    setattr(old_value, "Constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constant"):
                opp_val = getattr(value, "Constant", None)
                setattr(value, "Constant", self)

class express_expressions_IndeterminateRef(Primary):

    pass
class express_expressions_SELFRef(Primary):

    pass
class express_expressions_ParameterRef(Primary):

    def __init__(self, id: str, express_expressions_ParameterRef: "Parameter" = None):
        self.id = id
        self.express_expressions_ParameterRef = express_expressions_ParameterRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_ParameterRef(self):
        return self.__express_expressions_ParameterRef

    @express_expressions_ParameterRef.setter
    def express_expressions_ParameterRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ParameterRef__express_expressions_ParameterRef", None)
        self.__express_expressions_ParameterRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter144"):
                opp_val = getattr(old_value, "Parameter144", None)
                if opp_val == self:
                    setattr(old_value, "Parameter144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter144"):
                opp_val = getattr(value, "Parameter144", None)
                setattr(value, "Parameter144", self)

class express_expressions_EnumItemRef(Primary):

    def __init__(self, id: str, express_expressions_EnumItemRef: "EnumerationItem" = None):
        self.id = id
        self.express_expressions_EnumItemRef = express_expressions_EnumItemRef
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_EnumItemRef(self):
        return self.__express_expressions_EnumItemRef

    @express_expressions_EnumItemRef.setter
    def express_expressions_EnumItemRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_EnumItemRef__express_expressions_EnumItemRef", None)
        self.__express_expressions_EnumItemRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationItem"):
                opp_val = getattr(old_value, "EnumerationItem", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationItem"):
                opp_val = getattr(value, "EnumerationItem", None)
                setattr(value, "EnumerationItem", self)

class express_expressions_RepeatCount:

    pass
class CaseAction:

    pass
class Variable:

    pass
class express_algorithms_FunctionResult(Variable):

    pass
class express_algorithms_LocalVariable(Variable):

    pass
class express_algorithms_InVariable(Variable):

    pass
class SingleEntityType:

    pass
class ControlVariable:

    pass
class express_statements_CaseAction:

    def __init__(self, isDefault: str, express_statements_CaseAction: set["Expression"] = None, express_statements_CaseAction55: "Statement" = None):
        self.isDefault = isDefault
        self.express_statements_CaseAction = express_statements_CaseAction if express_statements_CaseAction is not None else set()
        self.express_statements_CaseAction55 = express_statements_CaseAction55
        
    @property
    def isDefault(self) -> str:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault

    @property
    def express_statements_CaseAction55(self):
        return self.__express_statements_CaseAction55

    @express_statements_CaseAction55.setter
    def express_statements_CaseAction55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_CaseAction__express_statements_CaseAction55", None)
        self.__express_statements_CaseAction55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement56"):
                opp_val = getattr(old_value, "Statement56", None)
                if opp_val == self:
                    setattr(old_value, "Statement56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement56"):
                opp_val = getattr(value, "Statement56", None)
                setattr(value, "Statement56", self)

    @property
    def express_statements_CaseAction(self):
        return self.__express_statements_CaseAction

    @express_statements_CaseAction.setter
    def express_statements_CaseAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_CaseAction__express_statements_CaseAction", None)
        self.__express_statements_CaseAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression53"):
                    opp_val = getattr(item, "Expression53", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression53"):
                    opp_val = getattr(item, "Expression53", None)
                    
                    setattr(item, "Expression53", self)
                    

class algorithms_VARVariable:

    pass
class express_algorithms_VARParameter(algorithms_Parameter, algorithms_VARVariable):

    pass
class algorithms_NamedVariable:

    pass
class express_statements_AliasVariable(algorithms_NamedVariable, algorithms_VARVariable):

    pass
class NamedVariable:

    pass
class express_expressions_QueryVariable(NamedVariable):

    pass
class express_algorithms_Variable(NamedVariable):

    pass
class express_statements_ControlVariable(NamedVariable):

    pass
class ExplicitAttribute:

    pass
class express_core_InvertibleAttribute(ExplicitAttribute):

    pass
class express_statements_VARExpression(ABC):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class VARVariable:

    pass
class ActualParameter:

    pass
class Procedure:

    pass
class LocalElement:

    pass
class express_algorithms_NamedVariable(LocalElement):

    pass
class express_algorithms_GenericElement(LocalElement):

    pass
class express_algorithms_Parameter(LocalElement):

    def __init__(self, inout: str, position: str, express_algorithms_Parameter: set["ActualStructureConstraint"] = None, express_algorithms_Parameter510: set["ActualTypeConstraint"] = None, express_algorithms_Parameter513: "ParameterType" = None, LocalElement: "express_core_LocalScope"):
        self.inout = inout
        self.position = position
        self.express_algorithms_Parameter = express_algorithms_Parameter if express_algorithms_Parameter is not None else set()
        self.express_algorithms_Parameter510 = express_algorithms_Parameter510 if express_algorithms_Parameter510 is not None else set()
        self.express_algorithms_Parameter513 = express_algorithms_Parameter513
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def inout(self) -> str:
        return self.__inout

    @inout.setter
    def inout(self, inout: str):
        self.__inout = inout

    @property
    def express_algorithms_Parameter513(self):
        return self.__express_algorithms_Parameter513

    @express_algorithms_Parameter513.setter
    def express_algorithms_Parameter513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Parameter__express_algorithms_Parameter513", None)
        self.__express_algorithms_Parameter513 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParameterType514"):
                opp_val = getattr(old_value, "ParameterType514", None)
                if opp_val == self:
                    setattr(old_value, "ParameterType514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParameterType514"):
                opp_val = getattr(value, "ParameterType514", None)
                setattr(value, "ParameterType514", self)

    @property
    def express_algorithms_Parameter(self):
        return self.__express_algorithms_Parameter

    @express_algorithms_Parameter.setter
    def express_algorithms_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Parameter__express_algorithms_Parameter", None)
        self.__express_algorithms_Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActualStructureConstraint508"):
                    opp_val = getattr(item, "ActualStructureConstraint508", None)
                    
                    if opp_val == self:
                        setattr(item, "ActualStructureConstraint508", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActualStructureConstraint508"):
                    opp_val = getattr(item, "ActualStructureConstraint508", None)
                    
                    setattr(item, "ActualStructureConstraint508", self)
                    

    @property
    def express_algorithms_Parameter510(self):
        return self.__express_algorithms_Parameter510

    @express_algorithms_Parameter510.setter
    def express_algorithms_Parameter510(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Parameter__express_algorithms_Parameter510", None)
        self.__express_algorithms_Parameter510 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActualTypeConstraint511"):
                    opp_val = getattr(item, "ActualTypeConstraint511", None)
                    
                    if opp_val == self:
                        setattr(item, "ActualTypeConstraint511", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActualTypeConstraint511"):
                    opp_val = getattr(item, "ActualTypeConstraint511", None)
                    
                    setattr(item, "ActualTypeConstraint511", self)
                    

class express_rules_NamedRule(LocalElement):

    def __init__(self, position: str, express_rules_NamedRule: "Expression" = None, LocalElement: "express_core_LocalScope"):
        self.position = position
        self.express_rules_NamedRule = express_rules_NamedRule
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def express_rules_NamedRule(self):
        return self.__express_rules_NamedRule

    @express_rules_NamedRule.setter
    def express_rules_NamedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_rules_NamedRule__express_rules_NamedRule", None)
        self.__express_rules_NamedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression26"):
                opp_val = getattr(old_value, "Expression26", None)
                if opp_val == self:
                    setattr(old_value, "Expression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression26"):
                opp_val = getattr(value, "Expression26", None)
                setattr(value, "Expression26", self)

class NamedRule:

    pass
class Statement:

    pass
class express_statements_ProcedureCall(Statement):

    pass
class express_statements_CaseStatement(Statement):

    pass
class express_statements_Assignment(Statement):

    pass
class express_statements_IfStatement(Statement):

    pass
class express_statements_StatementBlock(Statement):

    def __init__(self, delimited: str, Statement51: set["Statement"] = None, Statement85: "express_statements_IfStatement", Statement88: "express_statements_IfStatement", Statement: "express_rules_GlobalRule", algorithms: "express_statements_StatementBlock", algorithms521: "express_algorithms_Algorithm", algorithms66: "express_statements_RepeatStatement", Statement56: "express_statements_CaseAction", Statement32: "express_statements_AliasStatement"):
        self.delimited = delimited
        self.Statement51 = Statement51 if Statement51 is not None else set()
        
    @property
    def delimited(self) -> str:
        return self.__delimited

    @delimited.setter
    def delimited(self, delimited: str):
        self.__delimited = delimited

    @property
    def Statement51(self):
        return self.__Statement51

    @Statement51.setter
    def Statement51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_StatementBlock__Statement51", None)
        self.__Statement51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "algorithms"):
                    opp_val = getattr(item, "algorithms", None)
                    
                    if opp_val == self:
                        setattr(item, "algorithms", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "algorithms"):
                    opp_val = getattr(item, "algorithms", None)
                    
                    setattr(item, "algorithms", self)
                    

class express_statements_ControlStatement(Statement):

    pass
class AliasVariable:

    pass
class VARExpression:

    pass
class express_statements_AttributeCell(VARExpression):

    def __init__(self, id: str, express_statements_AttributeCell: "ExplicitAttribute" = None, express_statements_AttributeCell48: "VARExpression" = None, VARExpression: "express_statements_AliasStatement", VARExpression139: "express_expressions_ActualParameter", VARExpression61: "express_statements_MemberCell", VARExpression73: "express_statements_GroupCell", VARExpression49: "express_statements_AttributeCell", VARExpression44: "express_statements_AliasVariable", VARExpression95: "express_statements_Assignment"):
        self.id = id
        self.express_statements_AttributeCell = express_statements_AttributeCell
        self.express_statements_AttributeCell48 = express_statements_AttributeCell48
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_statements_AttributeCell(self):
        return self.__express_statements_AttributeCell

    @express_statements_AttributeCell.setter
    def express_statements_AttributeCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_AttributeCell__express_statements_AttributeCell", None)
        self.__express_statements_AttributeCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExplicitAttribute"):
                opp_val = getattr(old_value, "ExplicitAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ExplicitAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExplicitAttribute"):
                opp_val = getattr(value, "ExplicitAttribute", None)
                setattr(value, "ExplicitAttribute", self)

    @property
    def express_statements_AttributeCell48(self):
        return self.__express_statements_AttributeCell48

    @express_statements_AttributeCell48.setter
    def express_statements_AttributeCell48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_AttributeCell__express_statements_AttributeCell48", None)
        self.__express_statements_AttributeCell48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARExpression49"):
                opp_val = getattr(old_value, "VARExpression49", None)
                if opp_val == self:
                    setattr(old_value, "VARExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARExpression49"):
                opp_val = getattr(value, "VARExpression49", None)
                setattr(value, "VARExpression49", self)

class express_statements_VariableCell(VARExpression):

    def __init__(self, id: str, express_statements_VariableCell: "Variable" = None, VARExpression: "express_statements_AliasStatement", VARExpression139: "express_expressions_ActualParameter", VARExpression61: "express_statements_MemberCell", VARExpression73: "express_statements_GroupCell", VARExpression49: "express_statements_AttributeCell", VARExpression44: "express_statements_AliasVariable", VARExpression95: "express_statements_Assignment"):
        self.id = id
        self.express_statements_VariableCell = express_statements_VariableCell
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_statements_VariableCell(self):
        return self.__express_statements_VariableCell

    @express_statements_VariableCell.setter
    def express_statements_VariableCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_VariableCell__express_statements_VariableCell", None)
        self.__express_statements_VariableCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable"):
                opp_val = getattr(old_value, "Variable", None)
                if opp_val == self:
                    setattr(old_value, "Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable"):
                opp_val = getattr(value, "Variable", None)
                setattr(value, "Variable", self)

class express_statements_MemberCell(VARExpression):

    pass
class express_statements_VARCell(VARExpression):

    def __init__(self, id: str, express_statements_VARCell: "VARVariable" = None, VARExpression: "express_statements_AliasStatement", VARExpression139: "express_expressions_ActualParameter", VARExpression61: "express_statements_MemberCell", VARExpression73: "express_statements_GroupCell", VARExpression49: "express_statements_AttributeCell", VARExpression44: "express_statements_AliasVariable", VARExpression95: "express_statements_Assignment"):
        self.id = id
        self.express_statements_VARCell = express_statements_VARCell
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_statements_VARCell(self):
        return self.__express_statements_VARCell

    @express_statements_VARCell.setter
    def express_statements_VARCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_VARCell__express_statements_VARCell", None)
        self.__express_statements_VARCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARVariable"):
                opp_val = getattr(old_value, "VARVariable", None)
                if opp_val == self:
                    setattr(old_value, "VARVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARVariable"):
                opp_val = getattr(value, "VARVariable", None)
                setattr(value, "VARVariable", self)

class express_statements_GroupCell(VARExpression):

    def __init__(self, id: str, express_statements_GroupCell: "VARExpression" = None, express_statements_GroupCell75: "SingleEntityType" = None, VARExpression: "express_statements_AliasStatement", VARExpression139: "express_expressions_ActualParameter", VARExpression61: "express_statements_MemberCell", VARExpression73: "express_statements_GroupCell", VARExpression49: "express_statements_AttributeCell", VARExpression44: "express_statements_AliasVariable", VARExpression95: "express_statements_Assignment"):
        self.id = id
        self.express_statements_GroupCell = express_statements_GroupCell
        self.express_statements_GroupCell75 = express_statements_GroupCell75
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_statements_GroupCell75(self):
        return self.__express_statements_GroupCell75

    @express_statements_GroupCell75.setter
    def express_statements_GroupCell75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_GroupCell__express_statements_GroupCell75", None)
        self.__express_statements_GroupCell75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType"):
                opp_val = getattr(old_value, "SingleEntityType", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType"):
                opp_val = getattr(value, "SingleEntityType", None)
                setattr(value, "SingleEntityType", self)

    @property
    def express_statements_GroupCell(self):
        return self.__express_statements_GroupCell

    @express_statements_GroupCell.setter
    def express_statements_GroupCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_GroupCell__express_statements_GroupCell", None)
        self.__express_statements_GroupCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARExpression73"):
                opp_val = getattr(old_value, "VARExpression73", None)
                if opp_val == self:
                    setattr(old_value, "VARExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARExpression73"):
                opp_val = getattr(value, "VARExpression73", None)
                setattr(value, "VARExpression73", self)

class core_LocalScope:

    pass
class express_expressions_QueryExpression(core_LocalScope, core_Expression):

    pass
class algorithms_Statement:

    pass
class express_statements_RepeatStatement(core_LocalScope, algorithms_Statement):

    pass
class express_statements_AliasStatement(core_LocalScope, algorithms_Statement):

    pass
class ControlStatement:

    pass
class express_statements_EscapeStatement(ControlStatement):

    pass
class express_statements_NullStatement(ControlStatement):

    pass
class express_statements_ReturnStatement(ControlStatement):

    pass
class express_statements_SkipStatement(ControlStatement):

    pass
class EntityInstance:

    pass
class express_instances_MultiLeafInstance(EntityInstance):

    pass
class express_instances_SingleLeafInstance(EntityInstance):

    pass
class SETValue:

    pass
class express_rules_Extent(SETValue):

    pass
class SupertypeRule:

    pass
class Expression:

    pass
class express_expressions_AggregateInitializer(Expression):

    pass
class express_expressions_Primary(Expression):

    pass
class express_expressions_PartialEntityConstructor(Expression):

    def __init__(self, id: str, express_expressions_PartialEntityConstructor: "PartialEntityValue" = None, express_expressions_PartialEntityConstructor125: "SingleEntityType" = None, express_expressions_PartialEntityConstructor128: set["AttributeBinding"] = None, Expression332: "express_core_DomainConstraint", Expression224: "express_core_ArrayBound", Expression42: "express_statements_ControlVariable", Expression151: "express_expressions_UnaryOperation", Expression475: "express_algorithms_LocalVariable", Expression36: "express_statements_ControlVariable", Expression156: "express_expressions_QueryExpression", Expression130: "express_expressions_Coercion", Expression161: "express_expressions_QueryExpression", Expression142: "express_expressions_ActualParameter", Expression82: "express_statements_IfStatement", Expression147: "express_expressions_AggregateIndex", Expression58: "express_statements_MemberCell", Expression180: "express_expressions_MemberBinding", Expression103: "express_expressions_BinaryIndex", Expression63: "express_statements_RepeatStatement", Expression122: "express_expressions_StringIndex", Expression39: "express_statements_ControlVariable", Expression99: "express_expressions_RepeatCount", Expression26: "express_rules_NamedRule", Expression163: "express_expressions_AttributeBinding", Expression119: "express_expressions_StringIndex", Expression: "express_rules_SubtypeConstraint", Expression97: "express_expressions_Selector", Expression109: "express_expressions_IndexOperation", Expression546: "express_instances_Constant", Expression71: "express_statements_RepeatStatement", Expression371: "express_core_DerivedAttribute", Expression90: "express_statements_ReturnStatement", Expression106: "express_expressions_BinaryIndex", Expression80: "express_statements_CaseStatement", Expression53: "express_statements_CaseAction", Expression111: "express_expressions_BinaryOperation", Expression92: "express_statements_Assignment", Expression114: "express_expressions_BinaryOperation", Expression226: "express_core_Redeclaration"):
        self.id = id
        self.express_expressions_PartialEntityConstructor = express_expressions_PartialEntityConstructor
        self.express_expressions_PartialEntityConstructor125 = express_expressions_PartialEntityConstructor125
        self.express_expressions_PartialEntityConstructor128 = express_expressions_PartialEntityConstructor128 if express_expressions_PartialEntityConstructor128 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def express_expressions_PartialEntityConstructor128(self):
        return self.__express_expressions_PartialEntityConstructor128

    @express_expressions_PartialEntityConstructor128.setter
    def express_expressions_PartialEntityConstructor128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_PartialEntityConstructor__express_expressions_PartialEntityConstructor128", None)
        self.__express_expressions_PartialEntityConstructor128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeBinding"):
                    opp_val = getattr(item, "AttributeBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeBinding"):
                    opp_val = getattr(item, "AttributeBinding", None)
                    
                    setattr(item, "AttributeBinding", self)
                    

    @property
    def express_expressions_PartialEntityConstructor(self):
        return self.__express_expressions_PartialEntityConstructor

    @express_expressions_PartialEntityConstructor.setter
    def express_expressions_PartialEntityConstructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_PartialEntityConstructor__express_expressions_PartialEntityConstructor", None)
        self.__express_expressions_PartialEntityConstructor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PartialEntityValue"):
                opp_val = getattr(old_value, "PartialEntityValue", None)
                if opp_val == self:
                    setattr(old_value, "PartialEntityValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PartialEntityValue"):
                opp_val = getattr(value, "PartialEntityValue", None)
                setattr(value, "PartialEntityValue", self)

    @property
    def express_expressions_PartialEntityConstructor125(self):
        return self.__express_expressions_PartialEntityConstructor125

    @express_expressions_PartialEntityConstructor125.setter
    def express_expressions_PartialEntityConstructor125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_PartialEntityConstructor__express_expressions_PartialEntityConstructor125", None)
        self.__express_expressions_PartialEntityConstructor125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType126"):
                opp_val = getattr(old_value, "SingleEntityType126", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType126"):
                opp_val = getattr(value, "SingleEntityType126", None)
                setattr(value, "SingleEntityType126", self)

class express_expressions_Operation(Expression):

    pass
class express_expressions_FunctionCall(Expression):

    pass
class express_expressions_IndexOperation(Expression):

    pass
class express_expressions_Selector(Expression):

    pass
class Extent:

    pass
class express_rules_SubtypeConstraint:

    pass
class core_AlgorithmScope:

    pass
class express_algorithms_Algorithm(core_CommonElement, core_AlgorithmScope):

    pass
class core_SchemaElement:

    pass
class express_rules_GlobalRule(core_AlgorithmScope, core_SchemaElement):

    pass
class ScopedId:

    pass
class GlobalRule:

    pass
class Population:

    pass
class EntityType:

    pass
class CommonElement:

    pass
class express_instances_Constant(CommonElement):

    pass
class express_rules_SupertypeRule(CommonElement):

    def __init__(self, assertsAbstract: str, express_rules_SupertypeRule: "EntityType" = None, SubtypeConstraint: set["SubtypeConstraint"] = None, core356: "express_core_AlgorithmScope"):
        self.assertsAbstract = assertsAbstract
        self.express_rules_SupertypeRule = express_rules_SupertypeRule
        self.SubtypeConstraint = SubtypeConstraint if SubtypeConstraint is not None else set()
        
    @property
    def assertsAbstract(self) -> str:
        return self.__assertsAbstract

    @assertsAbstract.setter
    def assertsAbstract(self, assertsAbstract: str):
        self.__assertsAbstract = assertsAbstract

    @property
    def SubtypeConstraint(self):
        return self.__SubtypeConstraint

    @SubtypeConstraint.setter
    def SubtypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_rules_SupertypeRule__SubtypeConstraint", None)
        self.__SubtypeConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules"):
                    opp_val = getattr(item, "rules", None)
                    
                    if opp_val == self:
                        setattr(item, "rules", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules"):
                    opp_val = getattr(item, "rules", None)
                    
                    setattr(item, "rules", self)
                    

    @property
    def express_rules_SupertypeRule(self):
        return self.__express_rules_SupertypeRule

    @express_rules_SupertypeRule.setter
    def express_rules_SupertypeRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_rules_SupertypeRule__express_rules_SupertypeRule", None)
        self.__express_rules_SupertypeRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityType"):
                opp_val = getattr(old_value, "EntityType", None)
                if opp_val == self:
                    setattr(old_value, "EntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityType"):
                opp_val = getattr(value, "EntityType", None)
                setattr(value, "EntityType", self)

class SubtypeConstraint:

    pass
class express_rules_TOTAL_OVERConstraint(SubtypeConstraint):

    pass
class express_rules_ANDConstraint(SubtypeConstraint):

    pass
class express_rules_ONEOFConstraint(SubtypeConstraint):

    pass