from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Environment(Enum):
    KUBERNETES = "KUBERNETES"
    DOCKER_SWARM = "DOCKER_SWARM"


############################################
# Definition of Classes
############################################

class model_Application:

    def __init__(self, name: str, totalMessages: str, totalData: str, weight: str, model_Application: set["model_StringToService"] = None, model_Application37: "model_StringToApplication" = None):
        self.name = name
        self.totalMessages = totalMessages
        self.totalData = totalData
        self.weight = weight
        self.model_Application = model_Application if model_Application is not None else set()
        self.model_Application37 = model_Application37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def totalData(self) -> str:
        return self.__totalData

    @totalData.setter
    def totalData(self, totalData: str):
        self.__totalData = totalData

    @property
    def totalMessages(self) -> str:
        return self.__totalMessages

    @totalMessages.setter
    def totalMessages(self, totalMessages: str):
        self.__totalMessages = totalMessages

    @property
    def model_Application37(self):
        return self.__model_Application37

    @model_Application37.setter
    def model_Application37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Application__model_Application37", None)
        self.__model_Application37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_StringToApplication36"):
                opp_val = getattr(old_value, "model_StringToApplication36", None)
                if opp_val == self:
                    setattr(old_value, "model_StringToApplication36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_StringToApplication36"):
                opp_val = getattr(value, "model_StringToApplication36", None)
                setattr(value, "model_StringToApplication36", self)

    @property
    def model_Application(self):
        return self.__model_Application

    @model_Application.setter
    def model_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Application__model_Application", None)
        self.__model_Application = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToService34"):
                    opp_val = getattr(item, "model_StringToService34", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToService34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToService34"):
                    opp_val = getattr(item, "model_StringToService34", None)
                    
                    setattr(item, "model_StringToService34", self)
                    

class model_StringToService:

    def __init__(self, key: str, model_StringToService: "model_Service" = None, model_StringToService34: "model_Application" = None):
        self.key = key
        self.model_StringToService = model_StringToService
        self.model_StringToService34 = model_StringToService34
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_StringToService(self):
        return self.__model_StringToService

    @model_StringToService.setter
    def model_StringToService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToService__model_StringToService", None)
        self.__model_StringToService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Service26"):
                opp_val = getattr(old_value, "model_Service26", None)
                if opp_val == self:
                    setattr(old_value, "model_Service26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Service26"):
                opp_val = getattr(value, "model_Service26", None)
                setattr(value, "model_Service26", self)

    @property
    def model_StringToService34(self):
        return self.__model_StringToService34

    @model_StringToService34.setter
    def model_StringToService34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToService__model_StringToService34", None)
        self.__model_StringToService34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Application"):
                opp_val = getattr(old_value, "model_Application", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Application"):
                opp_val = getattr(value, "model_Application", None)
                if opp_val is None:
                    setattr(value, "model_Application", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_ElementWithResources(ABC):

    pass
class model_StringToDoubleMap:

    def __init__(self, key: str, value: str, model_StringToDoubleMap: "model_Host" = None, model_StringToDoubleMap21: "model_ElementWithResources" = None, model_StringToDoubleMap24: "model_ElementWithResources" = None):
        self.key = key
        self.value = value
        self.model_StringToDoubleMap = model_StringToDoubleMap
        self.model_StringToDoubleMap21 = model_StringToDoubleMap21
        self.model_StringToDoubleMap24 = model_StringToDoubleMap24
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_StringToDoubleMap21(self):
        return self.__model_StringToDoubleMap21

    @model_StringToDoubleMap21.setter
    def model_StringToDoubleMap21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToDoubleMap__model_StringToDoubleMap21", None)
        self.__model_StringToDoubleMap21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ElementWithResources"):
                opp_val = getattr(old_value, "model_ElementWithResources", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ElementWithResources"):
                opp_val = getattr(value, "model_ElementWithResources", None)
                if opp_val is None:
                    setattr(value, "model_ElementWithResources", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_StringToDoubleMap24(self):
        return self.__model_StringToDoubleMap24

    @model_StringToDoubleMap24.setter
    def model_StringToDoubleMap24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToDoubleMap__model_StringToDoubleMap24", None)
        self.__model_StringToDoubleMap24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ElementWithResources23"):
                opp_val = getattr(old_value, "model_ElementWithResources23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ElementWithResources23"):
                opp_val = getattr(value, "model_ElementWithResources23", None)
                if opp_val is None:
                    setattr(value, "model_ElementWithResources23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_StringToDoubleMap(self):
        return self.__model_StringToDoubleMap

    @model_StringToDoubleMap.setter
    def model_StringToDoubleMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToDoubleMap__model_StringToDoubleMap", None)
        self.__model_StringToDoubleMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Host19"):
                opp_val = getattr(old_value, "model_Host19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Host19"):
                opp_val = getattr(value, "model_Host19", None)
                if opp_val is None:
                    setattr(value, "model_Host19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_StringToServiceInstance:

    def __init__(self, key: str, model_StringToServiceInstance: "model_Host" = None, model_StringToServiceInstance31: "model_ServiceInstance" = None):
        self.key = key
        self.model_StringToServiceInstance = model_StringToServiceInstance
        self.model_StringToServiceInstance31 = model_StringToServiceInstance31
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_StringToServiceInstance(self):
        return self.__model_StringToServiceInstance

    @model_StringToServiceInstance.setter
    def model_StringToServiceInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToServiceInstance__model_StringToServiceInstance", None)
        self.__model_StringToServiceInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Host17"):
                opp_val = getattr(old_value, "model_Host17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Host17"):
                opp_val = getattr(value, "model_Host17", None)
                if opp_val is None:
                    setattr(value, "model_Host17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_StringToServiceInstance31(self):
        return self.__model_StringToServiceInstance31

    @model_StringToServiceInstance31.setter
    def model_StringToServiceInstance31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToServiceInstance__model_StringToServiceInstance31", None)
        self.__model_StringToServiceInstance31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ServiceInstance32"):
                opp_val = getattr(old_value, "model_ServiceInstance32", None)
                if opp_val == self:
                    setattr(old_value, "model_ServiceInstance32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ServiceInstance32"):
                opp_val = getattr(value, "model_ServiceInstance32", None)
                setattr(value, "model_ServiceInstance32", self)

class model_Message:

    def __init__(self, name: str, avgResponseTime: str, timestamp: str, uid: str, messageSize: str, model_Message: "model_ServiceInstance" = None, model_Message11: "model_ServiceInstance" = None, model_Message14: "model_ServiceInstance" = None):
        self.name = name
        self.avgResponseTime = avgResponseTime
        self.timestamp = timestamp
        self.uid = uid
        self.messageSize = messageSize
        self.model_Message = model_Message
        self.model_Message11 = model_Message11
        self.model_Message14 = model_Message14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def messageSize(self) -> str:
        return self.__messageSize

    @messageSize.setter
    def messageSize(self, messageSize: str):
        self.__messageSize = messageSize

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def avgResponseTime(self) -> str:
        return self.__avgResponseTime

    @avgResponseTime.setter
    def avgResponseTime(self, avgResponseTime: str):
        self.__avgResponseTime = avgResponseTime

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def model_Message11(self):
        return self.__model_Message11

    @model_Message11.setter
    def model_Message11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Message__model_Message11", None)
        self.__model_Message11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ServiceInstance12"):
                opp_val = getattr(old_value, "model_ServiceInstance12", None)
                if opp_val == self:
                    setattr(old_value, "model_ServiceInstance12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ServiceInstance12"):
                opp_val = getattr(value, "model_ServiceInstance12", None)
                setattr(value, "model_ServiceInstance12", self)

    @property
    def model_Message14(self):
        return self.__model_Message14

    @model_Message14.setter
    def model_Message14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Message__model_Message14", None)
        self.__model_Message14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ServiceInstance15"):
                opp_val = getattr(old_value, "model_ServiceInstance15", None)
                if opp_val == self:
                    setattr(old_value, "model_ServiceInstance15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ServiceInstance15"):
                opp_val = getattr(value, "model_ServiceInstance15", None)
                setattr(value, "model_ServiceInstance15", self)

    @property
    def model_Message(self):
        return self.__model_Message

    @model_Message.setter
    def model_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Message__model_Message", None)
        self.__model_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ServiceInstance"):
                opp_val = getattr(old_value, "model_ServiceInstance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ServiceInstance"):
                opp_val = getattr(value, "model_ServiceInstance", None)
                if opp_val is None:
                    setattr(value, "model_ServiceInstance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ElementWithResources:

    pass
class model_Host(ElementWithResources):

    def __init__(self, hostAddress: str, name: str, cores: str, model_Host: "model_ServiceInstance" = None, model_Host17: set["model_StringToServiceInstance"] = None, model_Host19: set["model_StringToDoubleMap"] = None, model_Host29: "model_StringToHost" = None):
        self.hostAddress = hostAddress
        self.name = name
        self.cores = cores
        self.model_Host = model_Host
        self.model_Host17 = model_Host17 if model_Host17 is not None else set()
        self.model_Host19 = model_Host19 if model_Host19 is not None else set()
        self.model_Host29 = model_Host29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hostAddress(self) -> str:
        return self.__hostAddress

    @hostAddress.setter
    def hostAddress(self, hostAddress: str):
        self.__hostAddress = hostAddress

    @property
    def cores(self) -> str:
        return self.__cores

    @cores.setter
    def cores(self, cores: str):
        self.__cores = cores

    @property
    def model_Host19(self):
        return self.__model_Host19

    @model_Host19.setter
    def model_Host19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Host__model_Host19", None)
        self.__model_Host19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToDoubleMap"):
                    opp_val = getattr(item, "model_StringToDoubleMap", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToDoubleMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToDoubleMap"):
                    opp_val = getattr(item, "model_StringToDoubleMap", None)
                    
                    setattr(item, "model_StringToDoubleMap", self)
                    

    @property
    def model_Host(self):
        return self.__model_Host

    @model_Host.setter
    def model_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Host__model_Host", None)
        self.__model_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ServiceInstance9"):
                opp_val = getattr(old_value, "model_ServiceInstance9", None)
                if opp_val == self:
                    setattr(old_value, "model_ServiceInstance9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ServiceInstance9"):
                opp_val = getattr(value, "model_ServiceInstance9", None)
                setattr(value, "model_ServiceInstance9", self)

    @property
    def model_Host29(self):
        return self.__model_Host29

    @model_Host29.setter
    def model_Host29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Host__model_Host29", None)
        self.__model_Host29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_StringToHost28"):
                opp_val = getattr(old_value, "model_StringToHost28", None)
                if opp_val == self:
                    setattr(old_value, "model_StringToHost28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_StringToHost28"):
                opp_val = getattr(value, "model_StringToHost28", None)
                setattr(value, "model_StringToHost28", self)

    @property
    def model_Host17(self):
        return self.__model_Host17

    @model_Host17.setter
    def model_Host17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Host__model_Host17", None)
        self.__model_Host17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToServiceInstance"):
                    opp_val = getattr(item, "model_StringToServiceInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToServiceInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToServiceInstance"):
                    opp_val = getattr(item, "model_StringToServiceInstance", None)
                    
                    setattr(item, "model_StringToServiceInstance", self)
                    

class Service:

    pass
class model_ServiceInstance(Service, ElementWithResources):

    def __init__(self, id: str, address: str, containers: str, totalMessages: str, totalData: str, model_ServiceInstance: set["model_Message"] = None, model_ServiceInstance9: "model_Host" = None, model_ServiceInstance12: "model_Message" = None, model_ServiceInstance15: "model_Message" = None, model_ServiceInstance32: "model_StringToServiceInstance" = None):
        self.id = id
        self.address = address
        self.containers = containers
        self.totalMessages = totalMessages
        self.totalData = totalData
        self.model_ServiceInstance = model_ServiceInstance if model_ServiceInstance is not None else set()
        self.model_ServiceInstance9 = model_ServiceInstance9
        self.model_ServiceInstance12 = model_ServiceInstance12
        self.model_ServiceInstance15 = model_ServiceInstance15
        self.model_ServiceInstance32 = model_ServiceInstance32
        
    @property
    def totalData(self) -> str:
        return self.__totalData

    @totalData.setter
    def totalData(self, totalData: str):
        self.__totalData = totalData

    @property
    def containers(self) -> str:
        return self.__containers

    @containers.setter
    def containers(self, containers: str):
        self.__containers = containers

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def totalMessages(self) -> str:
        return self.__totalMessages

    @totalMessages.setter
    def totalMessages(self, totalMessages: str):
        self.__totalMessages = totalMessages

    @property
    def model_ServiceInstance32(self):
        return self.__model_ServiceInstance32

    @model_ServiceInstance32.setter
    def model_ServiceInstance32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ServiceInstance__model_ServiceInstance32", None)
        self.__model_ServiceInstance32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_StringToServiceInstance31"):
                opp_val = getattr(old_value, "model_StringToServiceInstance31", None)
                if opp_val == self:
                    setattr(old_value, "model_StringToServiceInstance31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_StringToServiceInstance31"):
                opp_val = getattr(value, "model_StringToServiceInstance31", None)
                setattr(value, "model_StringToServiceInstance31", self)

    @property
    def model_ServiceInstance15(self):
        return self.__model_ServiceInstance15

    @model_ServiceInstance15.setter
    def model_ServiceInstance15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ServiceInstance__model_ServiceInstance15", None)
        self.__model_ServiceInstance15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Message14"):
                opp_val = getattr(old_value, "model_Message14", None)
                if opp_val == self:
                    setattr(old_value, "model_Message14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Message14"):
                opp_val = getattr(value, "model_Message14", None)
                setattr(value, "model_Message14", self)

    @property
    def model_ServiceInstance9(self):
        return self.__model_ServiceInstance9

    @model_ServiceInstance9.setter
    def model_ServiceInstance9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ServiceInstance__model_ServiceInstance9", None)
        self.__model_ServiceInstance9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Host"):
                opp_val = getattr(old_value, "model_Host", None)
                if opp_val == self:
                    setattr(old_value, "model_Host", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Host"):
                opp_val = getattr(value, "model_Host", None)
                setattr(value, "model_Host", self)

    @property
    def model_ServiceInstance12(self):
        return self.__model_ServiceInstance12

    @model_ServiceInstance12.setter
    def model_ServiceInstance12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ServiceInstance__model_ServiceInstance12", None)
        self.__model_ServiceInstance12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Message11"):
                opp_val = getattr(old_value, "model_Message11", None)
                if opp_val == self:
                    setattr(old_value, "model_Message11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Message11"):
                opp_val = getattr(value, "model_Message11", None)
                setattr(value, "model_Message11", self)

    @property
    def model_ServiceInstance(self):
        return self.__model_ServiceInstance

    @model_ServiceInstance.setter
    def model_ServiceInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ServiceInstance__model_ServiceInstance", None)
        self.__model_ServiceInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Message"):
                    opp_val = getattr(item, "model_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Message"):
                    opp_val = getattr(item, "model_Message", None)
                    
                    setattr(item, "model_Message", self)
                    

class model_Affinity:

    def __init__(self, degree: str, model_Affinity: "model_Service" = None, model_Affinity5: "model_Service" = None):
        self.degree = degree
        self.model_Affinity = model_Affinity
        self.model_Affinity5 = model_Affinity5
        
    @property
    def degree(self) -> str:
        return self.__degree

    @degree.setter
    def degree(self, degree: str):
        self.__degree = degree

    @property
    def model_Affinity(self):
        return self.__model_Affinity

    @model_Affinity.setter
    def model_Affinity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Affinity__model_Affinity", None)
        self.__model_Affinity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Service"):
                opp_val = getattr(old_value, "model_Service", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Service"):
                opp_val = getattr(value, "model_Service", None)
                if opp_val is None:
                    setattr(value, "model_Service", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Affinity5(self):
        return self.__model_Affinity5

    @model_Affinity5.setter
    def model_Affinity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Affinity__model_Affinity5", None)
        self.__model_Affinity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Service6"):
                opp_val = getattr(old_value, "model_Service6", None)
                if opp_val == self:
                    setattr(old_value, "model_Service6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Service6"):
                opp_val = getattr(value, "model_Service6", None)
                setattr(value, "model_Service6", self)

class model_Service(ABC):

    def __init__(self, name: str, application: str, stateful: str, model_Service: set["model_Affinity"] = None, model_Service6: "model_Affinity" = None, model_Service26: "model_StringToService" = None):
        self.name = name
        self.application = application
        self.stateful = stateful
        self.model_Service = model_Service if model_Service is not None else set()
        self.model_Service6 = model_Service6
        self.model_Service26 = model_Service26
        
    @property
    def stateful(self) -> str:
        return self.__stateful

    @stateful.setter
    def stateful(self, stateful: str):
        self.__stateful = stateful

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

    @property
    def model_Service6(self):
        return self.__model_Service6

    @model_Service6.setter
    def model_Service6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Service__model_Service6", None)
        self.__model_Service6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Affinity5"):
                opp_val = getattr(old_value, "model_Affinity5", None)
                if opp_val == self:
                    setattr(old_value, "model_Affinity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Affinity5"):
                opp_val = getattr(value, "model_Affinity5", None)
                setattr(value, "model_Affinity5", self)

    @property
    def model_Service(self):
        return self.__model_Service

    @model_Service.setter
    def model_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Service__model_Service", None)
        self.__model_Service = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Affinity"):
                    opp_val = getattr(item, "model_Affinity", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Affinity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Affinity"):
                    opp_val = getattr(item, "model_Affinity", None)
                    
                    setattr(item, "model_Affinity", self)
                    

    @property
    def model_Service26(self):
        return self.__model_Service26

    @model_Service26.setter
    def model_Service26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Service__model_Service26", None)
        self.__model_Service26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_StringToService"):
                opp_val = getattr(old_value, "model_StringToService", None)
                if opp_val == self:
                    setattr(old_value, "model_StringToService", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_StringToService"):
                opp_val = getattr(value, "model_StringToService", None)
                setattr(value, "model_StringToService", self)

class model_StringToApplication:

    def __init__(self, key: str, model_StringToApplication: "model_Cluster" = None, model_StringToApplication36: "model_Application" = None):
        self.key = key
        self.model_StringToApplication = model_StringToApplication
        self.model_StringToApplication36 = model_StringToApplication36
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_StringToApplication36(self):
        return self.__model_StringToApplication36

    @model_StringToApplication36.setter
    def model_StringToApplication36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToApplication__model_StringToApplication36", None)
        self.__model_StringToApplication36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Application37"):
                opp_val = getattr(old_value, "model_Application37", None)
                if opp_val == self:
                    setattr(old_value, "model_Application37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Application37"):
                opp_val = getattr(value, "model_Application37", None)
                setattr(value, "model_Application37", self)

    @property
    def model_StringToApplication(self):
        return self.__model_StringToApplication

    @model_StringToApplication.setter
    def model_StringToApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToApplication__model_StringToApplication", None)
        self.__model_StringToApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Cluster2"):
                opp_val = getattr(old_value, "model_Cluster2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Cluster2"):
                opp_val = getattr(value, "model_Cluster2", None)
                if opp_val is None:
                    setattr(value, "model_Cluster2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Cluster:

    def __init__(self, environment: str, model_Cluster: set["model_StringToHost"] = None, model_Cluster2: set["model_StringToApplication"] = None):
        self.environment = environment
        self.model_Cluster = model_Cluster if model_Cluster is not None else set()
        self.model_Cluster2 = model_Cluster2 if model_Cluster2 is not None else set()
        
    @property
    def environment(self) -> str:
        return self.__environment

    @environment.setter
    def environment(self, environment: str):
        self.__environment = environment

    @property
    def model_Cluster(self):
        return self.__model_Cluster

    @model_Cluster.setter
    def model_Cluster(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Cluster__model_Cluster", None)
        self.__model_Cluster = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToHost"):
                    opp_val = getattr(item, "model_StringToHost", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToHost", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToHost"):
                    opp_val = getattr(item, "model_StringToHost", None)
                    
                    setattr(item, "model_StringToHost", self)
                    

    @property
    def model_Cluster2(self):
        return self.__model_Cluster2

    @model_Cluster2.setter
    def model_Cluster2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Cluster__model_Cluster2", None)
        self.__model_Cluster2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToApplication"):
                    opp_val = getattr(item, "model_StringToApplication", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToApplication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToApplication"):
                    opp_val = getattr(item, "model_StringToApplication", None)
                    
                    setattr(item, "model_StringToApplication", self)
                    

    def move(self, sourceHost: str, serviceId: str, destinationHost: str, application: str):
        # TODO: Implement move method
        pass

class model_StringToHost:

    def __init__(self, key: str, model_StringToHost: "model_Cluster" = None, model_StringToHost28: "model_Host" = None):
        self.key = key
        self.model_StringToHost = model_StringToHost
        self.model_StringToHost28 = model_StringToHost28
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_StringToHost28(self):
        return self.__model_StringToHost28

    @model_StringToHost28.setter
    def model_StringToHost28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToHost__model_StringToHost28", None)
        self.__model_StringToHost28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Host29"):
                opp_val = getattr(old_value, "model_Host29", None)
                if opp_val == self:
                    setattr(old_value, "model_Host29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Host29"):
                opp_val = getattr(value, "model_Host29", None)
                setattr(value, "model_Host29", self)

    @property
    def model_StringToHost(self):
        return self.__model_StringToHost

    @model_StringToHost.setter
    def model_StringToHost(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToHost__model_StringToHost", None)
        self.__model_StringToHost = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Cluster"):
                opp_val = getattr(old_value, "model_Cluster", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Cluster"):
                opp_val = getattr(value, "model_Cluster", None)
                if opp_val is None:
                    setattr(value, "model_Cluster", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
