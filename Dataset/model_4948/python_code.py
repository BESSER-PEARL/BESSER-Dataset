from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CRUDOperation(Enum):
    create = "create"
    update = "update"
    delete = "delete"
    retrieve = "retrieve"
class AttributePrimitiveValue(Enum):
    char = "char"
    float = "float"
    long = "long"
    short = "short"
    String = "String"
    int = "int"
    boolean = "boolean"
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
            if hasattr(old_value, "micro_Model42"):
                opp_val = getattr(old_value, "micro_Model42", None)
                if opp_val == self:
                    setattr(old_value, "micro_Model42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Model42"):
                opp_val = getattr(value, "micro_Model42", None)
                setattr(value, "micro_Model42", self)

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

class micro_Attribute(ABC):

    def __init__(self, name: str, isMany: bool, isId: bool, isGenerated: bool, Attribute: "micro_Model" = None, attributes: "micro_Model" = None):
        self.name = name
        self.isMany = isMany
        self.isId = isId
        self.isGenerated = isGenerated
        self.Attribute = Attribute
        self.attributes = attributes
        
    @property
    def isMany(self) -> bool:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: bool):
        self.__isMany = isMany

    @property
    def isGenerated(self) -> bool:
        return self.__isGenerated

    @isGenerated.setter
    def isGenerated(self, isGenerated: bool):
        self.__isGenerated = isGenerated

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isId(self) -> bool:
        return self.__isId

    @isId.setter
    def isId(self, isId: bool):
        self.__isId = isId

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
            if hasattr(old_value, "Model38"):
                opp_val = getattr(old_value, "Model38", None)
                if opp_val == self:
                    setattr(old_value, "Model38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model38"):
                opp_val = getattr(value, "Model38", None)
                setattr(value, "Model38", self)

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

class Service:

    pass
class micro_AggregateService(Service):

    def __init__(self, aggregateService: set["micro_Operation"] = None, micro_AggregateService: "micro_API" = None, aggregateService6: set["micro_Model"] = None, micro_AggregateService8: "micro_ViewService" = None, AggregateService: "micro_Model" = None, AggregateService15: "micro_Operation" = None):
        self.aggregateService = aggregateService if aggregateService is not None else set()
        self.micro_AggregateService = micro_AggregateService
        self.aggregateService6 = aggregateService6 if aggregateService6 is not None else set()
        self.micro_AggregateService8 = micro_AggregateService8
        self.AggregateService = AggregateService
        self.AggregateService15 = AggregateService15
        
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
            if hasattr(old_value, "models"):
                opp_val = getattr(old_value, "models", None)
                if opp_val == self:
                    setattr(old_value, "models", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "models"):
                opp_val = getattr(value, "models", None)
                setattr(value, "models", self)

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
    def aggregateService6(self):
        return self.__aggregateService6

    @aggregateService6.setter
    def aggregateService6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__aggregateService6", None)
        self.__aggregateService6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model"):
                    opp_val = getattr(item, "Model", None)
                    
                    if opp_val == self:
                        setattr(item, "Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model"):
                    opp_val = getattr(item, "Model", None)
                    
                    setattr(item, "Model", self)
                    

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
    def micro_AggregateService8(self):
        return self.__micro_AggregateService8

    @micro_AggregateService8.setter
    def micro_AggregateService8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__micro_AggregateService8", None)
        self.__micro_AggregateService8 = value
        
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
    def AggregateService15(self):
        return self.__AggregateService15

    @AggregateService15.setter
    def AggregateService15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_AggregateService__AggregateService15", None)
        self.__AggregateService15 = value
        
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

class micro_ViewService(Service):

    pass
class NamedElement:

    pass
class micro_API(NamedElement):

    pass
class micro_Step(NamedElement):

    pass
class micro_Service(NamedElement):

    def __init__(self, fullname: str, description: str, shortname: str, port: int, micro_Service: "micro_MicroserviceArchitecture" = None):
        self.fullname = fullname
        self.description = description
        self.shortname = shortname
        self.port = port
        self.micro_Service = micro_Service
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def shortname(self) -> str:
        return self.__shortname

    @shortname.setter
    def shortname(self, shortname: str):
        self.__shortname = shortname

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def fullname(self) -> str:
        return self.__fullname

    @fullname.setter
    def fullname(self, fullname: str):
        self.__fullname = fullname

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

class micro_Data(NamedElement):

    pass
class micro_Saga(NamedElement):

    pass
class micro_Info(NamedElement):

    pass
class micro_Operation(NamedElement):

    def __init__(self, operationType: str, isMethodController: bool, Operation: "micro_AggregateService" = None, micro_Operation: "micro_Event" = None, micro_Operation11: "micro_Saga" = None, micro_Operation13: "micro_Model" = None, operation: "micro_AggregateService" = None):
        self.operationType = operationType
        self.isMethodController = isMethodController
        self.Operation = Operation
        self.micro_Operation = micro_Operation
        self.micro_Operation11 = micro_Operation11
        self.micro_Operation13 = micro_Operation13
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
    def micro_Operation13(self):
        return self.__micro_Operation13

    @micro_Operation13.setter
    def micro_Operation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__micro_Operation13", None)
        self.__micro_Operation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "micro_Model"):
                opp_val = getattr(old_value, "micro_Model", None)
                if opp_val == self:
                    setattr(old_value, "micro_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "micro_Model"):
                opp_val = getattr(value, "micro_Model", None)
                setattr(value, "micro_Model", self)

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
            if hasattr(old_value, "aggregateService"):
                opp_val = getattr(old_value, "aggregateService", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregateService"):
                opp_val = getattr(value, "aggregateService", None)
                if opp_val is None:
                    setattr(value, "aggregateService", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def micro_Operation11(self):
        return self.__micro_Operation11

    @micro_Operation11.setter
    def micro_Operation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__micro_Operation11", None)
        self.__micro_Operation11 = value
        
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
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Operation__operation", None)
        self.__operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AggregateService15"):
                opp_val = getattr(old_value, "AggregateService15", None)
                if opp_val == self:
                    setattr(old_value, "AggregateService15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AggregateService15"):
                opp_val = getattr(value, "AggregateService15", None)
                setattr(value, "AggregateService15", self)

class micro_Event(NamedElement):

    pass
class micro_Model(NamedElement):

    pass
class micro_Command(NamedElement):

    def __init__(self, commandType: str, isReplyInfoMany: bool, Command: "micro_API" = None, micro_Command: "micro_Info" = None, commands: "micro_API" = None, micro_Command31: "micro_Step" = None):
        self.commandType = commandType
        self.isReplyInfoMany = isReplyInfoMany
        self.Command = Command
        self.micro_Command = micro_Command
        self.commands = commands
        self.micro_Command31 = micro_Command31
        
    @property
    def commandType(self) -> str:
        return self.__commandType

    @commandType.setter
    def commandType(self, commandType: str):
        self.__commandType = commandType

    @property
    def isReplyInfoMany(self) -> bool:
        return self.__isReplyInfoMany

    @isReplyInfoMany.setter
    def isReplyInfoMany(self, isReplyInfoMany: bool):
        self.__isReplyInfoMany = isReplyInfoMany

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
            if hasattr(old_value, "api18"):
                opp_val = getattr(old_value, "api18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "api18"):
                opp_val = getattr(value, "api18", None)
                if opp_val is None:
                    setattr(value, "api18", set([self]))
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
    def micro_Command31(self):
        return self.__micro_Command31

    @micro_Command31.setter
    def micro_Command31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_micro_Command__micro_Command31", None)
        self.__micro_Command31 = value
        
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

class micro_MicroserviceArchitecture(NamedElement):

    pass