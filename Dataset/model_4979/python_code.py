from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ExecutionPlatformInstance:

    pass
class cloudml_core_RequiredExecutionPlatformInstance(ExecutionPlatformInstance):

    pass
class cloudml_core_ProvidedExecutionPlatformInstance(ExecutionPlatformInstance):

    pass
class ExecutionPlatform:

    pass
class cloudml_core_RequiredExecutionPlatform(ExecutionPlatform):

    pass
class cloudml_core_ProvidedExecutionPlatform(ExecutionPlatform):

    pass
class PortInstance:

    pass
class cloudml_core_ProvidedPortInstance(PortInstance):

    pass
class cloudml_core_RequiredPortInstance(PortInstance):

    pass
class ProvidedExecutionPlatformInstance:

    pass
class ProvidedPortInstance:

    pass
class VMPortInstance:

    pass
class Port:

    pass
class cloudml_core_ProvidedPort(Port):

    pass
class cloudml_core_RequiredPort(Port):

    def __init__(self, isMandatory: bool, Port: "cloudml_core_PortInstance"):
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

class RequiredExecutionPlatform:

    pass
class RequiredExecutionPlatformInstance:

    pass
class RequiredPortInstance:

    pass
class VMPort:

    pass
class ExecuteInstance:

    pass
class RelationshipInstance:

    pass
class Relationship:

    pass
class VMInstance:

    pass
class VM:

    pass
class RequiredPort:

    pass
class ProvidedExecutionPlatform:

    pass
class ProvidedPort:

    pass
class Cloud:

    pass
class Component:

    pass
class cloudml_core_ExternalComponent(Component):

    def __init__(self, endPoint: str, login: str, passwd: str, location: str, serviceType: str, Region: str, cloudml_core_ExternalComponent: "Provider" = None, cloudml_core_ExternalComponent80: set["VMPort"] = None, Component59: "cloudml_core_ComponentInstance", Component: "cloudml_core_CloudMLModel", Component39: "cloudml_core_Port", Component85: "cloudml_core_ExecutionPlatform"):
        self.endPoint = endPoint
        self.login = login
        self.passwd = passwd
        self.location = location
        self.serviceType = serviceType
        self.Region = Region
        self.cloudml_core_ExternalComponent = cloudml_core_ExternalComponent
        self.cloudml_core_ExternalComponent80 = cloudml_core_ExternalComponent80 if cloudml_core_ExternalComponent80 is not None else set()
        
    @property
    def serviceType(self) -> str:
        return self.__serviceType

    @serviceType.setter
    def serviceType(self, serviceType: str):
        self.__serviceType = serviceType

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def Region(self) -> str:
        return self.__Region

    @Region.setter
    def Region(self, Region: str):
        self.__Region = Region

    @property
    def endPoint(self) -> str:
        return self.__endPoint

    @endPoint.setter
    def endPoint(self, endPoint: str):
        self.__endPoint = endPoint

    @property
    def passwd(self) -> str:
        return self.__passwd

    @passwd.setter
    def passwd(self, passwd: str):
        self.__passwd = passwd

    @property
    def cloudml_core_ExternalComponent(self):
        return self.__cloudml_core_ExternalComponent

    @cloudml_core_ExternalComponent.setter
    def cloudml_core_ExternalComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_ExternalComponent__cloudml_core_ExternalComponent", None)
        self.__cloudml_core_ExternalComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider78"):
                opp_val = getattr(old_value, "Provider78", None)
                if opp_val == self:
                    setattr(old_value, "Provider78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider78"):
                opp_val = getattr(value, "Provider78", None)
                setattr(value, "Provider78", self)

    @property
    def cloudml_core_ExternalComponent80(self):
        return self.__cloudml_core_ExternalComponent80

    @cloudml_core_ExternalComponent80.setter
    def cloudml_core_ExternalComponent80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_ExternalComponent__cloudml_core_ExternalComponent80", None)
        self.__cloudml_core_ExternalComponent80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VMPort81"):
                    opp_val = getattr(item, "VMPort81", None)
                    
                    if opp_val == self:
                        setattr(item, "VMPort81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VMPort81"):
                    opp_val = getattr(item, "VMPort81", None)
                    
                    setattr(item, "VMPort81", self)
                    

class cloudml_core_InternalComponent(Component):

    pass
class Provider:

    pass
class CloudMLElementWithProperties:

    pass
class cloudml_core_Port(CloudMLElementWithProperties):

    def __init__(self, isLocal: bool, portNumber: int, cloudml_core_Port: "Component" = None):
        self.isLocal = isLocal
        self.portNumber = portNumber
        self.cloudml_core_Port = cloudml_core_Port
        
    @property
    def isLocal(self) -> bool:
        return self.__isLocal

    @isLocal.setter
    def isLocal(self, isLocal: bool):
        self.__isLocal = isLocal

    @property
    def portNumber(self) -> int:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: int):
        self.__portNumber = portNumber

    @property
    def cloudml_core_Port(self):
        return self.__cloudml_core_Port

    @cloudml_core_Port.setter
    def cloudml_core_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_Port__cloudml_core_Port", None)
        self.__cloudml_core_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component39"):
                opp_val = getattr(old_value, "Component39", None)
                if opp_val == self:
                    setattr(old_value, "Component39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component39"):
                opp_val = getattr(value, "Component39", None)
                setattr(value, "Component39", self)

class cloudml_core_VMPort(CloudMLElementWithProperties):

    pass
class cloudml_core_Provider(CloudMLElementWithProperties):

    def __init__(self, credentials: str):
        self.credentials = credentials
        
    @property
    def credentials(self) -> str:
        return self.__credentials

    @credentials.setter
    def credentials(self, credentials: str):
        self.__credentials = credentials

class cloudml_core_PortInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_ExecutionPlatform(CloudMLElementWithProperties):

    pass
class cloudml_core_CloudMLModel(CloudMLElementWithProperties):

    pass
class cloudml_core_ExecutionPlatformInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_Cloud(CloudMLElementWithProperties):

    pass
class cloudml_core_ExecuteInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_VMPortInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_Component(CloudMLElementWithProperties):

    pass
class cloudml_core_Relationship(CloudMLElementWithProperties):

    pass
class cloudml_core_RelationshipInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_ComponentInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_Resource(CloudMLElementWithProperties):

    def __init__(self, downloadCommand: str, uploadCommand: str, installCommand: str, configureCommand: str, startCommand: str, stopCommand: str, requireCredentials: bool, executeLocally: bool):
        self.downloadCommand = downloadCommand
        self.uploadCommand = uploadCommand
        self.installCommand = installCommand
        self.configureCommand = configureCommand
        self.startCommand = startCommand
        self.stopCommand = stopCommand
        self.requireCredentials = requireCredentials
        self.executeLocally = executeLocally
        
    @property
    def stopCommand(self) -> str:
        return self.__stopCommand

    @stopCommand.setter
    def stopCommand(self, stopCommand: str):
        self.__stopCommand = stopCommand

    @property
    def executeLocally(self) -> bool:
        return self.__executeLocally

    @executeLocally.setter
    def executeLocally(self, executeLocally: bool):
        self.__executeLocally = executeLocally

    @property
    def uploadCommand(self) -> str:
        return self.__uploadCommand

    @uploadCommand.setter
    def uploadCommand(self, uploadCommand: str):
        self.__uploadCommand = uploadCommand

    @property
    def installCommand(self) -> str:
        return self.__installCommand

    @installCommand.setter
    def installCommand(self, installCommand: str):
        self.__installCommand = installCommand

    @property
    def startCommand(self) -> str:
        return self.__startCommand

    @startCommand.setter
    def startCommand(self, startCommand: str):
        self.__startCommand = startCommand

    @property
    def configureCommand(self) -> str:
        return self.__configureCommand

    @configureCommand.setter
    def configureCommand(self, configureCommand: str):
        self.__configureCommand = configureCommand

    @property
    def downloadCommand(self) -> str:
        return self.__downloadCommand

    @downloadCommand.setter
    def downloadCommand(self, downloadCommand: str):
        self.__downloadCommand = downloadCommand

    @property
    def requireCredentials(self) -> bool:
        return self.__requireCredentials

    @requireCredentials.setter
    def requireCredentials(self, requireCredentials: bool):
        self.__requireCredentials = requireCredentials

class Resource:

    pass
class Property:

    pass
class CloudMLElement:

    pass
class cloudml_core_CloudMLElementWithProperties(CloudMLElement):

    pass
class cloudml_core_Property(CloudMLElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cloudml_core_CloudMLElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class cloudml_NoUse:

    pass
class ExternalComponentInstance:

    pass
class cloudml_core_VMInstance(ExternalComponentInstance):

    def __init__(self, publicAddress: str, cloudml_core_VMInstance: set["VMPortInstance"] = None, ExternalComponentInstance: "cloudml_core_CloudMLModel"):
        self.publicAddress = publicAddress
        self.cloudml_core_VMInstance = cloudml_core_VMInstance if cloudml_core_VMInstance is not None else set()
        
    @property
    def publicAddress(self) -> str:
        return self.__publicAddress

    @publicAddress.setter
    def publicAddress(self, publicAddress: str):
        self.__publicAddress = publicAddress

    @property
    def cloudml_core_VMInstance(self):
        return self.__cloudml_core_VMInstance

    @cloudml_core_VMInstance.setter
    def cloudml_core_VMInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_VMInstance__cloudml_core_VMInstance", None)
        self.__cloudml_core_VMInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VMPortInstance"):
                    opp_val = getattr(item, "VMPortInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "VMPortInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VMPortInstance"):
                    opp_val = getattr(item, "VMPortInstance", None)
                    
                    setattr(item, "VMPortInstance", self)
                    

class InternalComponentInstance:

    pass
class ExternalComponent:

    pass
class cloudml_core_VM(ExternalComponent):

    def __init__(self, minRam: int, maxRam: int, minCores: int, maxCores: int, minStorage: int, maxStorage: int, os: str, is64os: bool, imageId: str, securityGroup: str, sshKey: str, privateKey: str, groupName: str, cloudml_core_VM: set["VMPort"] = None, ExternalComponent: "cloudml_core_CloudMLModel"):
        self.minRam = minRam
        self.maxRam = maxRam
        self.minCores = minCores
        self.maxCores = maxCores
        self.minStorage = minStorage
        self.maxStorage = maxStorage
        self.os = os
        self.is64os = is64os
        self.imageId = imageId
        self.securityGroup = securityGroup
        self.sshKey = sshKey
        self.privateKey = privateKey
        self.groupName = groupName
        self.cloudml_core_VM = cloudml_core_VM if cloudml_core_VM is not None else set()
        
    @property
    def is64os(self) -> bool:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: bool):
        self.__is64os = is64os

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def minStorage(self) -> int:
        return self.__minStorage

    @minStorage.setter
    def minStorage(self, minStorage: int):
        self.__minStorage = minStorage

    @property
    def maxCores(self) -> int:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: int):
        self.__maxCores = maxCores

    @property
    def os(self) -> str:
        return self.__os

    @os.setter
    def os(self, os: str):
        self.__os = os

    @property
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

    @property
    def maxStorage(self) -> int:
        return self.__maxStorage

    @maxStorage.setter
    def maxStorage(self, maxStorage: int):
        self.__maxStorage = maxStorage

    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def maxRam(self) -> int:
        return self.__maxRam

    @maxRam.setter
    def maxRam(self, maxRam: int):
        self.__maxRam = maxRam

    @property
    def sshKey(self) -> str:
        return self.__sshKey

    @sshKey.setter
    def sshKey(self, sshKey: str):
        self.__sshKey = sshKey

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

    @property
    def minCores(self) -> int:
        return self.__minCores

    @minCores.setter
    def minCores(self, minCores: int):
        self.__minCores = minCores

    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def cloudml_core_VM(self):
        return self.__cloudml_core_VM

    @cloudml_core_VM.setter
    def cloudml_core_VM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_VM__cloudml_core_VM", None)
        self.__cloudml_core_VM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VMPort"):
                    opp_val = getattr(item, "VMPort", None)
                    
                    if opp_val == self:
                        setattr(item, "VMPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VMPort"):
                    opp_val = getattr(item, "VMPort", None)
                    
                    setattr(item, "VMPort", self)
                    

class InternalComponent:

    pass
class ComponentInstance:

    pass
class cloudml_core_InternalComponentInstance(ComponentInstance):

    pass
class cloudml_core_ExternalComponentInstance(ComponentInstance):

    def __init__(self, ips: str, cloudml_core_ExternalComponentInstance: set["VMPortInstance"] = None, ComponentInstance87: "cloudml_core_ExecutionPlatformInstance", ComponentInstance68: "cloudml_core_PortInstance", ComponentInstance: "cloudml_core_CloudMLModel"):
        self.ips = ips
        self.cloudml_core_ExternalComponentInstance = cloudml_core_ExternalComponentInstance if cloudml_core_ExternalComponentInstance is not None else set()
        
    @property
    def ips(self) -> str:
        return self.__ips

    @ips.setter
    def ips(self, ips: str):
        self.__ips = ips

    @property
    def cloudml_core_ExternalComponentInstance(self):
        return self.__cloudml_core_ExternalComponentInstance

    @cloudml_core_ExternalComponentInstance.setter
    def cloudml_core_ExternalComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_ExternalComponentInstance__cloudml_core_ExternalComponentInstance", None)
        self.__cloudml_core_ExternalComponentInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VMPortInstance83"):
                    opp_val = getattr(item, "VMPortInstance83", None)
                    
                    if opp_val == self:
                        setattr(item, "VMPortInstance83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VMPortInstance83"):
                    opp_val = getattr(item, "VMPortInstance83", None)
                    
                    setattr(item, "VMPortInstance83", self)
                    
