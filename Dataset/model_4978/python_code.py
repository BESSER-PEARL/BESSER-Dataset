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
class cloudml_core_ProvidedExecutionPlatform(ExecutionPlatform):

    pass
class cloudml_core_RequiredExecutionPlatform(ExecutionPlatform):

    pass
class PortInstance:

    pass
class cloudml_core_RequiredPortInstance(PortInstance):

    pass
class RequiredExecutionPlatformInstance:

    pass
class RequiredPortInstance:

    pass
class ProvidedExecutionPlatformInstance:

    pass
class cloudml_core_ProvidedPortInstance(PortInstance):

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
class ProvidedPortInstance:

    pass
class VMPortInstance:

    pass
class VMPort:

    pass
class ExecuteInstance:

    pass
class RelationshipInstance:

    pass
class Relationship:

    pass
class RequiredPort:

    pass
class ProvidedExecutionPlatform:

    pass
class ProvidedPort:

    pass
class CloudMLElementWithProperties:

    pass
class cloudml_core_VMPortInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_RelationshipInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_ExecuteInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_Cloud(CloudMLElementWithProperties):

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

class cloudml_core_VMPort(CloudMLElementWithProperties):

    pass
class cloudml_core_ComponentInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_Relationship(CloudMLElementWithProperties):

    pass
class cloudml_core_Component(CloudMLElementWithProperties):

    pass
class cloudml_core_ExecutionPlatformInstance(CloudMLElementWithProperties):

    pass
class cloudml_core_PortInstance(CloudMLElementWithProperties):

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
            if hasattr(old_value, "Component41"):
                opp_val = getattr(old_value, "Component41", None)
                if opp_val == self:
                    setattr(old_value, "Component41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component41"):
                opp_val = getattr(value, "Component41", None)
                setattr(value, "Component41", self)

class cloudml_core_ExecutionPlatform(CloudMLElementWithProperties):

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
    def stopCommand(self) -> str:
        return self.__stopCommand

    @stopCommand.setter
    def stopCommand(self, stopCommand: str):
        self.__stopCommand = stopCommand

    @property
    def uploadCommand(self) -> str:
        return self.__uploadCommand

    @uploadCommand.setter
    def uploadCommand(self, uploadCommand: str):
        self.__uploadCommand = uploadCommand

    @property
    def configureCommand(self) -> str:
        return self.__configureCommand

    @configureCommand.setter
    def configureCommand(self, configureCommand: str):
        self.__configureCommand = configureCommand

    @property
    def executeLocally(self) -> bool:
        return self.__executeLocally

    @executeLocally.setter
    def executeLocally(self, executeLocally: bool):
        self.__executeLocally = executeLocally

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

class PuppetResource:

    pass
class Resource:

    pass
class cloudml_core_PuppetResource(Resource):

    def __init__(self, masterEndpoint: str, repositoryEndpoint: str, configureHostnameCommand: str, username: str, repositoryKey: str, configurationFile: str, manifestEntry: str, Resource49: "cloudml_core_Relationship", Resource: "cloudml_core_CloudMLElementWithProperties", Resource52: "cloudml_core_Relationship"):
        self.masterEndpoint = masterEndpoint
        self.repositoryEndpoint = repositoryEndpoint
        self.configureHostnameCommand = configureHostnameCommand
        self.username = username
        self.repositoryKey = repositoryKey
        self.configurationFile = configurationFile
        self.manifestEntry = manifestEntry
        
    @property
    def configurationFile(self) -> str:
        return self.__configurationFile

    @configurationFile.setter
    def configurationFile(self, configurationFile: str):
        self.__configurationFile = configurationFile

    @property
    def repositoryKey(self) -> str:
        return self.__repositoryKey

    @repositoryKey.setter
    def repositoryKey(self, repositoryKey: str):
        self.__repositoryKey = repositoryKey

    @property
    def repositoryEndpoint(self) -> str:
        return self.__repositoryEndpoint

    @repositoryEndpoint.setter
    def repositoryEndpoint(self, repositoryEndpoint: str):
        self.__repositoryEndpoint = repositoryEndpoint

    @property
    def masterEndpoint(self) -> str:
        return self.__masterEndpoint

    @masterEndpoint.setter
    def masterEndpoint(self, masterEndpoint: str):
        self.__masterEndpoint = masterEndpoint

    @property
    def configureHostnameCommand(self) -> str:
        return self.__configureHostnameCommand

    @configureHostnameCommand.setter
    def configureHostnameCommand(self, configureHostnameCommand: str):
        self.__configureHostnameCommand = configureHostnameCommand

    @property
    def manifestEntry(self) -> str:
        return self.__manifestEntry

    @manifestEntry.setter
    def manifestEntry(self, manifestEntry: str):
        self.__manifestEntry = manifestEntry

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

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

class VMInstance:

    pass
class VM:

    pass
class ExternalComponentInstance:

    pass
class cloudml_core_VMInstance(ExternalComponentInstance):

    def __init__(self, publicAddress: str, id: str, cloudml_core_VMInstance: set["VMPortInstance"] = None, ExternalComponentInstance: "cloudml_core_CloudMLModel"):
        self.publicAddress = publicAddress
        self.id = id
        self.cloudml_core_VMInstance = cloudml_core_VMInstance if cloudml_core_VMInstance is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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

    def __init__(self, minCores: int, maxCores: int, minStorage: int, maxStorage: int, os: str, is64os: bool, imageId: str, securityGroup: str, sshKey: str, privateKey: str, groupName: str, providerSpecificTypeName: str, minRam: int, maxRam: int, cloudml_core_VM: set["VMPort"] = None, ExternalComponent: "cloudml_core_CloudMLModel"):
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
        self.providerSpecificTypeName = providerSpecificTypeName
        self.minRam = minRam
        self.maxRam = maxRam
        self.cloudml_core_VM = cloudml_core_VM if cloudml_core_VM is not None else set()
        
    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def maxCores(self) -> int:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: int):
        self.__maxCores = maxCores

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
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

    @property
    def maxRam(self) -> int:
        return self.__maxRam

    @maxRam.setter
    def maxRam(self, maxRam: int):
        self.__maxRam = maxRam

    @property
    def minCores(self) -> int:
        return self.__minCores

    @minCores.setter
    def minCores(self, minCores: int):
        self.__minCores = minCores

    @property
    def maxStorage(self) -> int:
        return self.__maxStorage

    @maxStorage.setter
    def maxStorage(self, maxStorage: int):
        self.__maxStorage = maxStorage

    @property
    def is64os(self) -> bool:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: bool):
        self.__is64os = is64os

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

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
    def os(self) -> str:
        return self.__os

    @os.setter
    def os(self, os: str):
        self.__os = os

    @property
    def providerSpecificTypeName(self) -> str:
        return self.__providerSpecificTypeName

    @providerSpecificTypeName.setter
    def providerSpecificTypeName(self, providerSpecificTypeName: str):
        self.__providerSpecificTypeName = providerSpecificTypeName

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

    def __init__(self, ips: str, cloudml_core_ExternalComponentInstance: set["VMPortInstance"] = None, ComponentInstance89: "cloudml_core_ExecutionPlatformInstance", ComponentInstance: "cloudml_core_CloudMLModel", ComponentInstance70: "cloudml_core_PortInstance"):
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
                if hasattr(item, "VMPortInstance85"):
                    opp_val = getattr(item, "VMPortInstance85", None)
                    
                    if opp_val == self:
                        setattr(item, "VMPortInstance85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VMPortInstance85"):
                    opp_val = getattr(item, "VMPortInstance85", None)
                    
                    setattr(item, "VMPortInstance85", self)
                    

class Cloud:

    pass
class Component:

    pass
class cloudml_core_ExternalComponent(Component):

    def __init__(self, endPoint: str, login: str, passwd: str, location: str, serviceType: str, Region: str, cloudml_core_ExternalComponent: "Provider" = None, cloudml_core_ExternalComponent82: set["VMPort"] = None, Component41: "cloudml_core_Port", Component87: "cloudml_core_ExecutionPlatform", Component61: "cloudml_core_ComponentInstance", Component: "cloudml_core_CloudMLModel"):
        self.endPoint = endPoint
        self.login = login
        self.passwd = passwd
        self.location = location
        self.serviceType = serviceType
        self.Region = Region
        self.cloudml_core_ExternalComponent = cloudml_core_ExternalComponent
        self.cloudml_core_ExternalComponent82 = cloudml_core_ExternalComponent82 if cloudml_core_ExternalComponent82 is not None else set()
        
    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def serviceType(self) -> str:
        return self.__serviceType

    @serviceType.setter
    def serviceType(self, serviceType: str):
        self.__serviceType = serviceType

    @property
    def endPoint(self) -> str:
        return self.__endPoint

    @endPoint.setter
    def endPoint(self, endPoint: str):
        self.__endPoint = endPoint

    @property
    def Region(self) -> str:
        return self.__Region

    @Region.setter
    def Region(self, Region: str):
        self.__Region = Region

    @property
    def passwd(self) -> str:
        return self.__passwd

    @passwd.setter
    def passwd(self, passwd: str):
        self.__passwd = passwd

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

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
            if hasattr(old_value, "Provider80"):
                opp_val = getattr(old_value, "Provider80", None)
                if opp_val == self:
                    setattr(old_value, "Provider80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider80"):
                opp_val = getattr(value, "Provider80", None)
                setattr(value, "Provider80", self)

    @property
    def cloudml_core_ExternalComponent82(self):
        return self.__cloudml_core_ExternalComponent82

    @cloudml_core_ExternalComponent82.setter
    def cloudml_core_ExternalComponent82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_ExternalComponent__cloudml_core_ExternalComponent82", None)
        self.__cloudml_core_ExternalComponent82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VMPort83"):
                    opp_val = getattr(item, "VMPort83", None)
                    
                    if opp_val == self:
                        setattr(item, "VMPort83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VMPort83"):
                    opp_val = getattr(item, "VMPort83", None)
                    
                    setattr(item, "VMPort83", self)
                    

class cloudml_core_InternalComponent(Component):

    pass
class Provider:

    pass
class cloudml_core_CloudMLModel(CloudMLElementWithProperties):

    pass