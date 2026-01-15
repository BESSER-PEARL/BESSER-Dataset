from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VMSize(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"
class ProviderType(Enum):
    Flexiant = "Flexiant"
    Openstack = "Openstack"


############################################
# Definition of Classes
############################################

class Cluster:

    pass
class ddsm_StormCluster(Cluster):

    def __init__(self, number_of_workers: str):
        self.number_of_workers = number_of_workers
        
    @property
    def number_of_workers(self) -> str:
        return self.__number_of_workers

    @number_of_workers.setter
    def number_of_workers(self, number_of_workers: str):
        self.__number_of_workers = number_of_workers

class Resource:

    pass
class ddsm_ChefResource(Resource):

    def __init__(self, cookbookId: str):
        self.cookbookId = cookbookId
        
    @property
    def cookbookId(self) -> str:
        return self.__cookbookId

    @cookbookId.setter
    def cookbookId(self, cookbookId: str):
        self.__cookbookId = cookbookId

class InternalComponent:

    pass
class ddsm_HDFSDataNode(InternalComponent):

    pass
class ddsm_Kafka(InternalComponent):

    pass
class ddsm_YarnNodeManager(InternalComponent):

    pass
class ddsm_HDFSNameNode(InternalComponent):

    pass
class ddsm_ClientNode(InternalComponent):

    def __init__(self, type: str, artifactUrl: str, mainClass: str):
        self.type = type
        self.artifactUrl = artifactUrl
        self.mainClass = mainClass
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mainClass(self) -> str:
        return self.__mainClass

    @mainClass.setter
    def mainClass(self, mainClass: str):
        self.__mainClass = mainClass

    @property
    def artifactUrl(self) -> str:
        return self.__artifactUrl

    @artifactUrl.setter
    def artifactUrl(self, artifactUrl: str):
        self.__artifactUrl = artifactUrl

class ddsm_StormNimbus(InternalComponent):

    def __init__(self, taskTimeout: str, supervisorTimeout: str, monitorFrequency: str, queueSize: str, retryTimes: str, retryInterval: str):
        self.taskTimeout = taskTimeout
        self.supervisorTimeout = supervisorTimeout
        self.monitorFrequency = monitorFrequency
        self.queueSize = queueSize
        self.retryTimes = retryTimes
        self.retryInterval = retryInterval
        
    @property
    def supervisorTimeout(self) -> str:
        return self.__supervisorTimeout

    @supervisorTimeout.setter
    def supervisorTimeout(self, supervisorTimeout: str):
        self.__supervisorTimeout = supervisorTimeout

    @property
    def taskTimeout(self) -> str:
        return self.__taskTimeout

    @taskTimeout.setter
    def taskTimeout(self, taskTimeout: str):
        self.__taskTimeout = taskTimeout

    @property
    def retryTimes(self) -> str:
        return self.__retryTimes

    @retryTimes.setter
    def retryTimes(self, retryTimes: str):
        self.__retryTimes = retryTimes

    @property
    def retryInterval(self) -> str:
        return self.__retryInterval

    @retryInterval.setter
    def retryInterval(self, retryInterval: str):
        self.__retryInterval = retryInterval

    @property
    def queueSize(self) -> str:
        return self.__queueSize

    @queueSize.setter
    def queueSize(self, queueSize: str):
        self.__queueSize = queueSize

    @property
    def monitorFrequency(self) -> str:
        return self.__monitorFrequency

    @monitorFrequency.setter
    def monitorFrequency(self, monitorFrequency: str):
        self.__monitorFrequency = monitorFrequency

class ddsm_Zookeeper(InternalComponent):

    def __init__(self, tickTime: str, initLimit: str, syncLimit: str):
        self.tickTime = tickTime
        self.initLimit = initLimit
        self.syncLimit = syncLimit
        
    @property
    def tickTime(self) -> str:
        return self.__tickTime

    @tickTime.setter
    def tickTime(self, tickTime: str):
        self.__tickTime = tickTime

    @property
    def initLimit(self) -> str:
        return self.__initLimit

    @initLimit.setter
    def initLimit(self, initLimit: str):
        self.__initLimit = initLimit

    @property
    def syncLimit(self) -> str:
        return self.__syncLimit

    @syncLimit.setter
    def syncLimit(self, syncLimit: str):
        self.__syncLimit = syncLimit

class ddsm_YarnResourceManager(InternalComponent):

    pass
class ddsm_StormSupervisor(InternalComponent):

    def __init__(self, workerStartTimeout: str, cpuCapacity: str, memoryCapacity: str, heartbeatFrequency: str):
        self.workerStartTimeout = workerStartTimeout
        self.cpuCapacity = cpuCapacity
        self.memoryCapacity = memoryCapacity
        self.heartbeatFrequency = heartbeatFrequency
        
    @property
    def memoryCapacity(self) -> str:
        return self.__memoryCapacity

    @memoryCapacity.setter
    def memoryCapacity(self, memoryCapacity: str):
        self.__memoryCapacity = memoryCapacity

    @property
    def workerStartTimeout(self) -> str:
        return self.__workerStartTimeout

    @workerStartTimeout.setter
    def workerStartTimeout(self, workerStartTimeout: str):
        self.__workerStartTimeout = workerStartTimeout

    @property
    def cpuCapacity(self) -> str:
        return self.__cpuCapacity

    @cpuCapacity.setter
    def cpuCapacity(self, cpuCapacity: str):
        self.__cpuCapacity = cpuCapacity

    @property
    def heartbeatFrequency(self) -> str:
        return self.__heartbeatFrequency

    @heartbeatFrequency.setter
    def heartbeatFrequency(self, heartbeatFrequency: str):
        self.__heartbeatFrequency = heartbeatFrequency

class ddsm_DDSM:

    def __init__(self, modelId: str, description: str, ddsm_DDSM: set["ddsm_CloudElement"] = None, ddsm_DDSM32: set["ddsm_Property"] = None, ddsm_DDSM35: set["ddsm_Resource"] = None):
        self.modelId = modelId
        self.description = description
        self.ddsm_DDSM = ddsm_DDSM if ddsm_DDSM is not None else set()
        self.ddsm_DDSM32 = ddsm_DDSM32 if ddsm_DDSM32 is not None else set()
        self.ddsm_DDSM35 = ddsm_DDSM35 if ddsm_DDSM35 is not None else set()
        
    @property
    def modelId(self) -> str:
        return self.__modelId

    @modelId.setter
    def modelId(self, modelId: str):
        self.__modelId = modelId

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ddsm_DDSM35(self):
        return self.__ddsm_DDSM35

    @ddsm_DDSM35.setter
    def ddsm_DDSM35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_DDSM__ddsm_DDSM35", None)
        self.__ddsm_DDSM35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Resource36"):
                    opp_val = getattr(item, "ddsm_Resource36", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Resource36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Resource36"):
                    opp_val = getattr(item, "ddsm_Resource36", None)
                    
                    setattr(item, "ddsm_Resource36", self)
                    

    @property
    def ddsm_DDSM(self):
        return self.__ddsm_DDSM

    @ddsm_DDSM.setter
    def ddsm_DDSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_DDSM__ddsm_DDSM", None)
        self.__ddsm_DDSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_CloudElement30"):
                    opp_val = getattr(item, "ddsm_CloudElement30", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_CloudElement30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_CloudElement30"):
                    opp_val = getattr(item, "ddsm_CloudElement30", None)
                    
                    setattr(item, "ddsm_CloudElement30", self)
                    

    @property
    def ddsm_DDSM32(self):
        return self.__ddsm_DDSM32

    @ddsm_DDSM32.setter
    def ddsm_DDSM32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_DDSM__ddsm_DDSM32", None)
        self.__ddsm_DDSM32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Property33"):
                    opp_val = getattr(item, "ddsm_Property33", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Property33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Property33"):
                    opp_val = getattr(item, "ddsm_Property33", None)
                    
                    setattr(item, "ddsm_Property33", self)
                    

class ExecutionPlatform:

    pass
class ExternalComponent:

    pass
class ddsm_Cluster(ExternalComponent):

    pass
class ddsm_VM(ExternalComponent):

    def __init__(self, is64os: str, imageId: str, maxCores: str, publicPorts: str, maxRam: str, maxStorage: str, minCores: str, minRam: str, minStorage: str, os: str, privateKey: str, providerSpecificTypeName: str, securityGroup: str, sshKey: str, publicAddress: str, instances: str, genericSize: str, ddsm_VM: "ddsm_Cluster" = None):
        self.is64os = is64os
        self.imageId = imageId
        self.maxCores = maxCores
        self.publicPorts = publicPorts
        self.maxRam = maxRam
        self.maxStorage = maxStorage
        self.minCores = minCores
        self.minRam = minRam
        self.minStorage = minStorage
        self.os = os
        self.privateKey = privateKey
        self.providerSpecificTypeName = providerSpecificTypeName
        self.securityGroup = securityGroup
        self.sshKey = sshKey
        self.publicAddress = publicAddress
        self.instances = instances
        self.genericSize = genericSize
        self.ddsm_VM = ddsm_VM
        
    @property
    def providerSpecificTypeName(self) -> str:
        return self.__providerSpecificTypeName

    @providerSpecificTypeName.setter
    def providerSpecificTypeName(self, providerSpecificTypeName: str):
        self.__providerSpecificTypeName = providerSpecificTypeName

    @property
    def publicPorts(self) -> str:
        return self.__publicPorts

    @publicPorts.setter
    def publicPorts(self, publicPorts: str):
        self.__publicPorts = publicPorts

    @property
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

    @property
    def maxStorage(self) -> str:
        return self.__maxStorage

    @maxStorage.setter
    def maxStorage(self, maxStorage: str):
        self.__maxStorage = maxStorage

    @property
    def os(self) -> str:
        return self.__os

    @os.setter
    def os(self, os: str):
        self.__os = os

    @property
    def minRam(self) -> str:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: str):
        self.__minRam = minRam

    @property
    def minCores(self) -> str:
        return self.__minCores

    @minCores.setter
    def minCores(self, minCores: str):
        self.__minCores = minCores

    @property
    def minStorage(self) -> str:
        return self.__minStorage

    @minStorage.setter
    def minStorage(self, minStorage: str):
        self.__minStorage = minStorage

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def instances(self) -> str:
        return self.__instances

    @instances.setter
    def instances(self, instances: str):
        self.__instances = instances

    @property
    def genericSize(self) -> str:
        return self.__genericSize

    @genericSize.setter
    def genericSize(self, genericSize: str):
        self.__genericSize = genericSize

    @property
    def sshKey(self) -> str:
        return self.__sshKey

    @sshKey.setter
    def sshKey(self, sshKey: str):
        self.__sshKey = sshKey

    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def is64os(self) -> str:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: str):
        self.__is64os = is64os

    @property
    def publicAddress(self) -> str:
        return self.__publicAddress

    @publicAddress.setter
    def publicAddress(self, publicAddress: str):
        self.__publicAddress = publicAddress

    @property
    def maxCores(self) -> str:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: str):
        self.__maxCores = maxCores

    @property
    def maxRam(self) -> str:
        return self.__maxRam

    @maxRam.setter
    def maxRam(self, maxRam: str):
        self.__maxRam = maxRam

    @property
    def ddsm_VM(self):
        return self.__ddsm_VM

    @ddsm_VM.setter
    def ddsm_VM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_VM__ddsm_VM", None)
        self.__ddsm_VM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Cluster"):
                opp_val = getattr(old_value, "ddsm_Cluster", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Cluster"):
                opp_val = getattr(value, "ddsm_Cluster", None)
                if opp_val is None:
                    setattr(value, "ddsm_Cluster", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsm_Property:

    def __init__(self, propertyId: str, value: str, ddsm_Property: "ddsm_CloudElement" = None, ddsm_Property33: "ddsm_DDSM" = None):
        self.propertyId = propertyId
        self.value = value
        self.ddsm_Property = ddsm_Property
        self.ddsm_Property33 = ddsm_Property33
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def propertyId(self) -> str:
        return self.__propertyId

    @propertyId.setter
    def propertyId(self, propertyId: str):
        self.__propertyId = propertyId

    @property
    def ddsm_Property33(self):
        return self.__ddsm_Property33

    @ddsm_Property33.setter
    def ddsm_Property33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Property__ddsm_Property33", None)
        self.__ddsm_Property33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_DDSM32"):
                opp_val = getattr(old_value, "ddsm_DDSM32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_DDSM32"):
                opp_val = getattr(value, "ddsm_DDSM32", None)
                if opp_val is None:
                    setattr(value, "ddsm_DDSM32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_Property(self):
        return self.__ddsm_Property

    @ddsm_Property.setter
    def ddsm_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Property__ddsm_Property", None)
        self.__ddsm_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_CloudElement2"):
                opp_val = getattr(old_value, "ddsm_CloudElement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_CloudElement2"):
                opp_val = getattr(value, "ddsm_CloudElement2", None)
                if opp_val is None:
                    setattr(value, "ddsm_CloudElement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Port:

    pass
class ddsm_RequiredExecutionPlatform(ExecutionPlatform):

    def __init__(self, isMandatory: bool, ddsm_RequiredExecutionPlatform: "ddsm_InternalComponent" = None, ddsm_RequiredExecutionPlatform24: "ddsm_ExecutionBinding" = None):
        self.isMandatory = isMandatory
        self.ddsm_RequiredExecutionPlatform = ddsm_RequiredExecutionPlatform
        self.ddsm_RequiredExecutionPlatform24 = ddsm_RequiredExecutionPlatform24
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def ddsm_RequiredExecutionPlatform(self):
        return self.__ddsm_RequiredExecutionPlatform

    @ddsm_RequiredExecutionPlatform.setter
    def ddsm_RequiredExecutionPlatform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredExecutionPlatform__ddsm_RequiredExecutionPlatform", None)
        self.__ddsm_RequiredExecutionPlatform = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_InternalComponent11"):
                opp_val = getattr(old_value, "ddsm_InternalComponent11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_InternalComponent11"):
                opp_val = getattr(value, "ddsm_InternalComponent11", None)
                if opp_val is None:
                    setattr(value, "ddsm_InternalComponent11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_RequiredExecutionPlatform24(self):
        return self.__ddsm_RequiredExecutionPlatform24

    @ddsm_RequiredExecutionPlatform24.setter
    def ddsm_RequiredExecutionPlatform24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredExecutionPlatform__ddsm_RequiredExecutionPlatform24", None)
        self.__ddsm_RequiredExecutionPlatform24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_ExecutionBinding"):
                opp_val = getattr(old_value, "ddsm_ExecutionBinding", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_ExecutionBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_ExecutionBinding"):
                opp_val = getattr(value, "ddsm_ExecutionBinding", None)
                setattr(value, "ddsm_ExecutionBinding", self)

class ddsm_RequiredPort(Port):

    def __init__(self, isMandatory: bool, ddsm_RequiredPort: "ddsm_InternalComponent" = None, ddsm_RequiredPort22: "ddsm_Relationship" = None):
        self.isMandatory = isMandatory
        self.ddsm_RequiredPort = ddsm_RequiredPort
        self.ddsm_RequiredPort22 = ddsm_RequiredPort22
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def ddsm_RequiredPort22(self):
        return self.__ddsm_RequiredPort22

    @ddsm_RequiredPort22.setter
    def ddsm_RequiredPort22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredPort__ddsm_RequiredPort22", None)
        self.__ddsm_RequiredPort22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Relationship21"):
                opp_val = getattr(old_value, "ddsm_Relationship21", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Relationship21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Relationship21"):
                opp_val = getattr(value, "ddsm_Relationship21", None)
                setattr(value, "ddsm_Relationship21", self)

    @property
    def ddsm_RequiredPort(self):
        return self.__ddsm_RequiredPort

    @ddsm_RequiredPort.setter
    def ddsm_RequiredPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredPort__ddsm_RequiredPort", None)
        self.__ddsm_RequiredPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_InternalComponent"):
                opp_val = getattr(old_value, "ddsm_InternalComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_InternalComponent"):
                opp_val = getattr(value, "ddsm_InternalComponent", None)
                if opp_val is None:
                    setattr(value, "ddsm_InternalComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Component:

    pass
class ddsm_ExternalComponent(Component):

    def __init__(self, location: str, login: str, password: str, region: str, serviceType: str, ddsm_ExternalComponent: "ddsm_Provider" = None):
        self.location = location
        self.login = login
        self.password = password
        self.region = region
        self.serviceType = serviceType
        self.ddsm_ExternalComponent = ddsm_ExternalComponent
        
    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def region(self) -> str:
        return self.__region

    @region.setter
    def region(self, region: str):
        self.__region = region

    @property
    def serviceType(self) -> str:
        return self.__serviceType

    @serviceType.setter
    def serviceType(self, serviceType: str):
        self.__serviceType = serviceType

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def ddsm_ExternalComponent(self):
        return self.__ddsm_ExternalComponent

    @ddsm_ExternalComponent.setter
    def ddsm_ExternalComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_ExternalComponent__ddsm_ExternalComponent", None)
        self.__ddsm_ExternalComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Provider"):
                opp_val = getattr(old_value, "ddsm_Provider", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Provider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Provider"):
                opp_val = getattr(value, "ddsm_Provider", None)
                setattr(value, "ddsm_Provider", self)

class ddsm_InternalComponent(Component):

    pass
class ddsm_ProvidedExecutionPlatform(ExecutionPlatform):

    pass
class ddsm_ProvidedPort(Port):

    pass
class CloudElement:

    pass
class ddsm_Relationship(CloudElement):

    pass
class ddsm_Port(CloudElement):

    def __init__(self, isLocal: bool, portNumber: str):
        self.isLocal = isLocal
        self.portNumber = portNumber
        
    @property
    def isLocal(self) -> bool:
        return self.__isLocal

    @isLocal.setter
    def isLocal(self, isLocal: bool):
        self.__isLocal = isLocal

    @property
    def portNumber(self) -> str:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: str):
        self.__portNumber = portNumber

class ddsm_ExecutionBinding(CloudElement):

    pass
class ddsm_ExecutionPlatform(CloudElement):

    pass
class ddsm_Provider(CloudElement):

    def __init__(self, credentialsPath: str, type: str, ddsm_Provider: "ddsm_ExternalComponent" = None):
        self.credentialsPath = credentialsPath
        self.type = type
        self.ddsm_Provider = ddsm_Provider
        
    @property
    def credentialsPath(self) -> str:
        return self.__credentialsPath

    @credentialsPath.setter
    def credentialsPath(self, credentialsPath: str):
        self.__credentialsPath = credentialsPath

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ddsm_Provider(self):
        return self.__ddsm_Provider

    @ddsm_Provider.setter
    def ddsm_Provider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Provider__ddsm_Provider", None)
        self.__ddsm_Provider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_ExternalComponent"):
                opp_val = getattr(old_value, "ddsm_ExternalComponent", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_ExternalComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_ExternalComponent"):
                opp_val = getattr(value, "ddsm_ExternalComponent", None)
                setattr(value, "ddsm_ExternalComponent", self)

class ddsm_Component(CloudElement):

    pass
class ddsm_Resource:

    def __init__(self, downloadCommand: str, createCommand: str, configureCommand: str, installCommand: str, startCommand: str, stopCommand: str, resourceId: str, ddsm_Resource: "ddsm_CloudElement" = None, ddsm_Resource36: "ddsm_DDSM" = None):
        self.downloadCommand = downloadCommand
        self.createCommand = createCommand
        self.configureCommand = configureCommand
        self.installCommand = installCommand
        self.startCommand = startCommand
        self.stopCommand = stopCommand
        self.resourceId = resourceId
        self.ddsm_Resource = ddsm_Resource
        self.ddsm_Resource36 = ddsm_Resource36
        
    @property
    def createCommand(self) -> str:
        return self.__createCommand

    @createCommand.setter
    def createCommand(self, createCommand: str):
        self.__createCommand = createCommand

    @property
    def startCommand(self) -> str:
        return self.__startCommand

    @startCommand.setter
    def startCommand(self, startCommand: str):
        self.__startCommand = startCommand

    @property
    def resourceId(self) -> str:
        return self.__resourceId

    @resourceId.setter
    def resourceId(self, resourceId: str):
        self.__resourceId = resourceId

    @property
    def stopCommand(self) -> str:
        return self.__stopCommand

    @stopCommand.setter
    def stopCommand(self, stopCommand: str):
        self.__stopCommand = stopCommand

    @property
    def configureCommand(self) -> str:
        return self.__configureCommand

    @configureCommand.setter
    def configureCommand(self, configureCommand: str):
        self.__configureCommand = configureCommand

    @property
    def installCommand(self) -> str:
        return self.__installCommand

    @installCommand.setter
    def installCommand(self, installCommand: str):
        self.__installCommand = installCommand

    @property
    def downloadCommand(self) -> str:
        return self.__downloadCommand

    @downloadCommand.setter
    def downloadCommand(self, downloadCommand: str):
        self.__downloadCommand = downloadCommand

    @property
    def ddsm_Resource36(self):
        return self.__ddsm_Resource36

    @ddsm_Resource36.setter
    def ddsm_Resource36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource36", None)
        self.__ddsm_Resource36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_DDSM35"):
                opp_val = getattr(old_value, "ddsm_DDSM35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_DDSM35"):
                opp_val = getattr(value, "ddsm_DDSM35", None)
                if opp_val is None:
                    setattr(value, "ddsm_DDSM35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_Resource(self):
        return self.__ddsm_Resource

    @ddsm_Resource.setter
    def ddsm_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource", None)
        self.__ddsm_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_CloudElement"):
                opp_val = getattr(old_value, "ddsm_CloudElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_CloudElement"):
                opp_val = getattr(value, "ddsm_CloudElement", None)
                if opp_val is None:
                    setattr(value, "ddsm_CloudElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsm_CloudElement(ABC):

    def __init__(self, elementId: str, description: str, ddsm_CloudElement: set["ddsm_Resource"] = None, ddsm_CloudElement2: set["ddsm_Property"] = None, ddsm_CloudElement30: "ddsm_DDSM" = None):
        self.elementId = elementId
        self.description = description
        self.ddsm_CloudElement = ddsm_CloudElement if ddsm_CloudElement is not None else set()
        self.ddsm_CloudElement2 = ddsm_CloudElement2 if ddsm_CloudElement2 is not None else set()
        self.ddsm_CloudElement30 = ddsm_CloudElement30
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def elementId(self) -> str:
        return self.__elementId

    @elementId.setter
    def elementId(self, elementId: str):
        self.__elementId = elementId

    @property
    def ddsm_CloudElement30(self):
        return self.__ddsm_CloudElement30

    @ddsm_CloudElement30.setter
    def ddsm_CloudElement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_CloudElement__ddsm_CloudElement30", None)
        self.__ddsm_CloudElement30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_DDSM"):
                opp_val = getattr(old_value, "ddsm_DDSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_DDSM"):
                opp_val = getattr(value, "ddsm_DDSM", None)
                if opp_val is None:
                    setattr(value, "ddsm_DDSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_CloudElement2(self):
        return self.__ddsm_CloudElement2

    @ddsm_CloudElement2.setter
    def ddsm_CloudElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_CloudElement__ddsm_CloudElement2", None)
        self.__ddsm_CloudElement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Property"):
                    opp_val = getattr(item, "ddsm_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Property"):
                    opp_val = getattr(item, "ddsm_Property", None)
                    
                    setattr(item, "ddsm_Property", self)
                    

    @property
    def ddsm_CloudElement(self):
        return self.__ddsm_CloudElement

    @ddsm_CloudElement.setter
    def ddsm_CloudElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_CloudElement__ddsm_CloudElement", None)
        self.__ddsm_CloudElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Resource"):
                    opp_val = getattr(item, "ddsm_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Resource"):
                    opp_val = getattr(item, "ddsm_Resource", None)
                    
                    setattr(item, "ddsm_Resource", self)
                    
