from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributePrimitiveValue(Enum):
    String = "String"
    int = "int"
    boolean = "boolean"
    char = "char"
    float = "float"
    long = "long"
    short = "short"
class CRUDOperation(Enum):
    create = "create"
    update = "update"
    delete = "delete"
    retrieve = "retrieve"
class CommandType(Enum):
    compensate = "compensate"
    invoke = "invoke"
    reply = "reply"


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class micro_PrimitiveTypeAttribute(Attribute):

    def __init__(self, type: str, micro_PrimitiveTypeAttribute: "micro_Model" = None):
        self.type = type
        self.micro_PrimitiveTypeAttribute = micro_PrimitiveTypeAttribute
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def micro_PrimitiveTypeAttribute(self):
        return self.__micro_PrimitiveTypeAttribute

    @micro_PrimitiveTypeAttribute.setter
    def micro_PrimitiveTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_PrimitiveTypeAttribute__micro_PrimitiveTypeAttribute", None)
        self.__micro_PrimitiveTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Model52"):
                opp_val = getattr(old_value, "micro_Model52", None)
                if opp_val == self:
                    setattr(old_value, "micro_Model52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Model52"):
                opp_val = getattr(value, "micro_Model52", None)
                setattr(value, "micro_Model52", self)

class micro_ReferenceAttribute(Attribute):

    pass
class micro_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Service:

    pass
class micro_ViewService(Service):

    pass
class micro_AggregateService(Service):

    def __init__(self, micro_AggregateService: "micro_API" = None, micro_AggregateService12: set["micro_ModelEvent"] = None, AggregateService: "micro_ModelEvent" = None, aggregateService: set["micro_ModelEvent"] = None, aggregateService9: set["micro_Operation"] = None, micro_AggregateService15: set["micro_Model"] = None, micro_AggregateService18: "micro_ViewService" = None, AggregateService26: "micro_Operation" = None):
        self.micro_AggregateService = micro_AggregateService
        self.micro_AggregateService12 = micro_AggregateService12 if micro_AggregateService12 is not None else set()
        self.AggregateService = AggregateService
        self.aggregateService = aggregateService if aggregateService is not None else set()
        self.aggregateService9 = aggregateService9 if aggregateService9 is not None else set()
        self.micro_AggregateService15 = micro_AggregateService15 if micro_AggregateService15 is not None else set()
        self.micro_AggregateService18 = micro_AggregateService18
        self.AggregateService26 = AggregateService26
        
    @property
    def micro_AggregateService15(self):
        return self.__micro_AggregateService15

    @micro_AggregateService15.setter
    def micro_AggregateService15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__micro_AggregateService15", None)
        self.__micro_AggregateService15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "micro_Model16"):
                    opp_val = getattr(item, "micro_Model16", None)
                    
                    if opp_val == self:
                        setattr(item, "micro_Model16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "micro_Model16"):
                    opp_val = getattr(item, "micro_Model16", None)
                    
                    setattr(item, "micro_Model16", self)
                    

    @property
    def micro_AggregateService18(self):
        return self.__micro_AggregateService18

    @micro_AggregateService18.setter
    def micro_AggregateService18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__micro_AggregateService18", None)
        self.__micro_AggregateService18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_ViewService"):
                opp_val = getattr(old_value, "micro_ViewService", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_ViewService"):
                opp_val = getattr(value, "micro_ViewService", None)
                if opp_val is None:
                    setattr(value, "micro_ViewService", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregateService9(self):
        return self.__aggregateService9

    @aggregateService9.setter
    def aggregateService9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__aggregateService9", None)
        self.__aggregateService9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def micro_AggregateService(self):
        return self.__micro_AggregateService

    @micro_AggregateService.setter
    def micro_AggregateService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__micro_AggregateService", None)
        self.__micro_AggregateService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_API"):
                opp_val = getattr(old_value, "micro_API", None)
                if opp_val == self:
                    setattr(old_value, "micro_API", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_API"):
                opp_val = getattr(value, "micro_API", None)
                setattr(value, "micro_API", self)

    @property
    def micro_AggregateService12(self):
        return self.__micro_AggregateService12

    @micro_AggregateService12.setter
    def micro_AggregateService12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__micro_AggregateService12", None)
        self.__micro_AggregateService12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "micro_ModelEvent13"):
                    opp_val = getattr(item, "micro_ModelEvent13", None)
                    
                    if opp_val == self:
                        setattr(item, "micro_ModelEvent13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "micro_ModelEvent13"):
                    opp_val = getattr(item, "micro_ModelEvent13", None)
                    
                    setattr(item, "micro_ModelEvent13", self)
                    

    @property
    def AggregateService(self):
        return self.__AggregateService

    @AggregateService.setter
    def AggregateService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__AggregateService", None)
        self.__AggregateService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelEvents"):
                opp_val = getattr(old_value, "modelEvents", None)
                if opp_val == self:
                    setattr(old_value, "modelEvents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelEvents"):
                opp_val = getattr(value, "modelEvents", None)
                setattr(value, "modelEvents", self)

    @property
    def aggregateService(self):
        return self.__aggregateService

    @aggregateService.setter
    def aggregateService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__aggregateService", None)
        self.__aggregateService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelEvent"):
                    opp_val = getattr(item, "ModelEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelEvent"):
                    opp_val = getattr(item, "ModelEvent", None)
                    
                    setattr(item, "ModelEvent", self)
                    

    @property
    def AggregateService26(self):
        return self.__AggregateService26

    @AggregateService26.setter
    def AggregateService26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__AggregateService26", None)
        self.__AggregateService26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation"):
                opp_val = getattr(old_value, "operation", None)
                if opp_val == self:
                    setattr(old_value, "operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation"):
                opp_val = getattr(value, "operation", None)
                setattr(value, "operation", self)

    def ReferenceModelsIncluded(self) -> bool:
        # TODO: Implement ReferenceModelsIncluded method
        pass

class micro_Attribute(ABC):

    def __init__(self, name: str, isMany: bool, isId: bool, isGenerated: bool, Attribute: "micro_Model" = None, attributes: "micro_Model" = None):
        self.name = name
        self.isMany = isMany
        self.isId = isId
        self.isGenerated = isGenerated
        self.Attribute = Attribute
        self.attributes = attributes
        
    @property
    def isGenerated(self) -> bool:
        return self.__isGenerated

    @isGenerated.setter
    def isGenerated(self, isGenerated: bool):
        self.__isGenerated = isGenerated

    @property
    def isId(self) -> bool:
        return self.__isId

    @isId.setter
    def isId(self, isId: bool):
        self.__isId = isId

    @property
    def isMany(self) -> bool:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: bool):
        self.__isMany = isMany

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                if opp_val is None:
                    setattr(value, "model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model"):
                opp_val = getattr(old_value, "Model", None)
                if opp_val == self:
                    setattr(old_value, "Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model"):
                opp_val = getattr(value, "Model", None)
                setattr(value, "Model", self)

class NamedElement:

    pass
class micro_Service(NamedElement):

    def __init__(self, fullname: str, description: str, shortname: str, port: int, micro_Service: "micro_MicroserviceArchitecture" = None):
        self.fullname = fullname
        self.description = description
        self.shortname = shortname
        self.port = port
        self.micro_Service = micro_Service
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortname(self) -> str:
        return self.__shortname

    @shortname.setter
    def shortname(self, shortname: str):
        self.__shortname = shortname

    @property
    def fullname(self) -> str:
        return self.__fullname

    @fullname.setter
    def fullname(self, fullname: str):
        self.__fullname = fullname

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def micro_Service(self):
        return self.__micro_Service

    @micro_Service.setter
    def micro_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Service__micro_Service", None)
        self.__micro_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_MicroserviceArchitecture"):
                opp_val = getattr(old_value, "micro_MicroserviceArchitecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_MicroserviceArchitecture"):
                opp_val = getattr(value, "micro_MicroserviceArchitecture", None)
                if opp_val is None:
                    setattr(value, "micro_MicroserviceArchitecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class micro_API(NamedElement):

    pass
class micro_Operation(NamedElement):

    def __init__(self, operationType: str, isMethodController: bool, Operation: "micro_AggregateService" = None, micro_Operation: "micro_Event" = None, micro_Operation21: "micro_Saga" = None, micro_Operation23: "micro_Model" = None, operation: "micro_AggregateService" = None):
        self.operationType = operationType
        self.isMethodController = isMethodController
        self.Operation = Operation
        self.micro_Operation = micro_Operation
        self.micro_Operation21 = micro_Operation21
        self.micro_Operation23 = micro_Operation23
        self.operation = operation
        
    @property
    def operationType(self) -> str:
        return self.__operationType

    @operationType.setter
    def operationType(self, operationType: str):
        self.__operationType = operationType

    @property
    def isMethodController(self) -> bool:
        return self.__isMethodController

    @isMethodController.setter
    def isMethodController(self, isMethodController: bool):
        self.__isMethodController = isMethodController

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__operation", None)
        self.__operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AggregateService26"):
                opp_val = getattr(old_value, "AggregateService26", None)
                if opp_val == self:
                    setattr(old_value, "AggregateService26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AggregateService26"):
                opp_val = getattr(value, "AggregateService26", None)
                setattr(value, "AggregateService26", self)

    @property
    def micro_Operation21(self):
        return self.__micro_Operation21

    @micro_Operation21.setter
    def micro_Operation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__micro_Operation21", None)
        self.__micro_Operation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Saga"):
                opp_val = getattr(old_value, "micro_Saga", None)
                if opp_val == self:
                    setattr(old_value, "micro_Saga", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Saga"):
                opp_val = getattr(value, "micro_Saga", None)
                setattr(value, "micro_Saga", self)

    @property
    def micro_Operation23(self):
        return self.__micro_Operation23

    @micro_Operation23.setter
    def micro_Operation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__micro_Operation23", None)
        self.__micro_Operation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Model24"):
                opp_val = getattr(old_value, "micro_Model24", None)
                if opp_val == self:
                    setattr(old_value, "micro_Model24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Model24"):
                opp_val = getattr(value, "micro_Model24", None)
                setattr(value, "micro_Model24", self)

    @property
    def micro_Operation(self):
        return self.__micro_Operation

    @micro_Operation.setter
    def micro_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__micro_Operation", None)
        self.__micro_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Event"):
                opp_val = getattr(old_value, "micro_Event", None)
                if opp_val == self:
                    setattr(old_value, "micro_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Event"):
                opp_val = getattr(value, "micro_Event", None)
                setattr(value, "micro_Event", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregateService9"):
                opp_val = getattr(old_value, "aggregateService9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregateService9"):
                opp_val = getattr(value, "aggregateService9", None)
                if opp_val is None:
                    setattr(value, "aggregateService9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class micro_Saga(NamedElement):

    pass
class micro_ModelEvent(NamedElement):

    pass
class micro_Step(NamedElement):

    pass
class micro_Command(NamedElement):

    def __init__(self, commandType: str, isReplyInfoMany: bool, Command: "micro_API" = None, micro_Command: "micro_Info" = None, commands: "micro_API" = None, micro_Command42: "micro_Step" = None):
        self.commandType = commandType
        self.isReplyInfoMany = isReplyInfoMany
        self.Command = Command
        self.micro_Command = micro_Command
        self.commands = commands
        self.micro_Command42 = micro_Command42
        
    @property
    def isReplyInfoMany(self) -> bool:
        return self.__isReplyInfoMany

    @isReplyInfoMany.setter
    def isReplyInfoMany(self, isReplyInfoMany: bool):
        self.__isReplyInfoMany = isReplyInfoMany

    @property
    def commandType(self) -> str:
        return self.__commandType

    @commandType.setter
    def commandType(self, commandType: str):
        self.__commandType = commandType

    @property
    def micro_Command42(self):
        return self.__micro_Command42

    @micro_Command42.setter
    def micro_Command42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Command__micro_Command42", None)
        self.__micro_Command42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Step"):
                opp_val = getattr(old_value, "micro_Step", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Step"):
                opp_val = getattr(value, "micro_Step", None)
                if opp_val is None:
                    setattr(value, "micro_Step", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Command(self):
        return self.__Command

    @Command.setter
    def Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Command__Command", None)
        self.__Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "api29"):
                opp_val = getattr(old_value, "api29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "api29"):
                opp_val = getattr(value, "api29", None)
                if opp_val is None:
                    setattr(value, "api29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Command__commands", None)
        self.__commands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "API"):
                opp_val = getattr(old_value, "API", None)
                if opp_val == self:
                    setattr(old_value, "API", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "API"):
                opp_val = getattr(value, "API", None)
                setattr(value, "API", self)

    @property
    def micro_Command(self):
        return self.__micro_Command

    @micro_Command.setter
    def micro_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Command__micro_Command", None)
        self.__micro_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Info"):
                opp_val = getattr(old_value, "micro_Info", None)
                if opp_val == self:
                    setattr(old_value, "micro_Info", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Info"):
                opp_val = getattr(value, "micro_Info", None)
                setattr(value, "micro_Info", self)

class micro_Data(NamedElement):

    pass
class micro_Event(NamedElement):

    pass
class micro_Model(NamedElement):

    pass
class micro_Info(NamedElement):

    pass
class micro_MicroserviceArchitecture(NamedElement):

    pass