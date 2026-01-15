from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ExecutionPlatformInstance:

    pass
class Resource:

    pass
class PortInstance:

    pass
class ExecutionPlatform:

    pass
class cloudml_RequiredExecutionPlatformInstance(ExecutionPlatformInstance):

    pass
class cloudml_RequiredPortInstance(PortInstance):

    pass
class ComponentInstance:

    pass
class cloudml_ProvidedExecutionPlatformInstance(ExecutionPlatformInstance):

    pass
class cloudml_ProvidedPortInstance(PortInstance):

    pass
class ExternalComponentInstance:

    pass
class Port:

    pass
class cloudml_RequiredExecutionPlatform(ExecutionPlatform):

    pass
class cloudml_RequiredPort(Port):

    def __init__(self, isMandatory: bool, cloudml_RequiredPort: "cloudml_InternalComponent" = None, cloudml_RequiredPort47: "cloudml_Relationship" = None):
        self.isMandatory = isMandatory
        self.cloudml_RequiredPort = cloudml_RequiredPort
        self.cloudml_RequiredPort47 = cloudml_RequiredPort47
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def cloudml_RequiredPort47(self):
        return self.__cloudml_RequiredPort47

    @cloudml_RequiredPort47.setter
    def cloudml_RequiredPort47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_RequiredPort__cloudml_RequiredPort47", None)
        self.__cloudml_RequiredPort47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Relationship46"):
                opp_val = getattr(old_value, "cloudml_Relationship46", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Relationship46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Relationship46"):
                opp_val = getattr(value, "cloudml_Relationship46", None)
                setattr(value, "cloudml_Relationship46", self)

    @property
    def cloudml_RequiredPort(self):
        return self.__cloudml_RequiredPort

    @cloudml_RequiredPort.setter
    def cloudml_RequiredPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_RequiredPort__cloudml_RequiredPort", None)
        self.__cloudml_RequiredPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_InternalComponent37"):
                opp_val = getattr(old_value, "cloudml_InternalComponent37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_InternalComponent37"):
                opp_val = getattr(value, "cloudml_InternalComponent37", None)
                if opp_val is None:
                    setattr(value, "cloudml_InternalComponent37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Component:

    pass
class cloudml_ProvidedExecutionPlatform(ExecutionPlatform):

    pass
class cloudml_ProvidedPort(Port):

    pass
class ExternalComponent:

    pass
class cloudml_VMInstance(ExternalComponentInstance):

    def __init__(self, publicAddress: str, id: str, cloudml_VMInstance: "cloudml_CloudMLModel" = None, cloudml_VMInstance59: "cloudml_Cloud" = None, cloudml_VMInstance61: set["cloudml_VMPortInstance"] = None):
        self.publicAddress = publicAddress
        self.id = id
        self.cloudml_VMInstance = cloudml_VMInstance
        self.cloudml_VMInstance59 = cloudml_VMInstance59
        self.cloudml_VMInstance61 = cloudml_VMInstance61 if cloudml_VMInstance61 is not None else set()
        
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
    def cloudml_VMInstance(self):
        return self.__cloudml_VMInstance

    @cloudml_VMInstance.setter
    def cloudml_VMInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_VMInstance__cloudml_VMInstance", None)
        self.__cloudml_VMInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLModel23"):
                opp_val = getattr(old_value, "cloudml_CloudMLModel23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLModel23"):
                opp_val = getattr(value, "cloudml_CloudMLModel23", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLModel23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_VMInstance61(self):
        return self.__cloudml_VMInstance61

    @cloudml_VMInstance61.setter
    def cloudml_VMInstance61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_VMInstance__cloudml_VMInstance61", None)
        self.__cloudml_VMInstance61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cloudml_VMPortInstance"):
                    opp_val = getattr(item, "cloudml_VMPortInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "cloudml_VMPortInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cloudml_VMPortInstance"):
                    opp_val = getattr(item, "cloudml_VMPortInstance", None)
                    
                    setattr(item, "cloudml_VMPortInstance", self)
                    

    @property
    def cloudml_VMInstance59(self):
        return self.__cloudml_VMInstance59

    @cloudml_VMInstance59.setter
    def cloudml_VMInstance59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_VMInstance__cloudml_VMInstance59", None)
        self.__cloudml_VMInstance59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Cloud58"):
                opp_val = getattr(old_value, "cloudml_Cloud58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Cloud58"):
                opp_val = getattr(value, "cloudml_Cloud58", None)
                if opp_val is None:
                    setattr(value, "cloudml_Cloud58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_VM(ExternalComponent):

    def __init__(self, minRam: int, maxRam: int, minCores: int, maxCores: int, minStorage: int, maxStorage: int, os: str, is64os: bool, imageId: str, securityGroup: str, sshKey: str, privateKey: str, groupName: str, providerSpecificTypeName: str, cloudml_VM: "cloudml_CloudMLModel" = None, cloudml_VM31: set["cloudml_VMPort"] = None):
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
        self.providerSpecificTypeName = providerSpecificTypeName
        self.cloudml_VM = cloudml_VM
        self.cloudml_VM31 = cloudml_VM31 if cloudml_VM31 is not None else set()
        
    @property
    def maxStorage(self) -> int:
        return self.__maxStorage

    @maxStorage.setter
    def maxStorage(self, maxStorage: int):
        self.__maxStorage = maxStorage

    @property
    def sshKey(self) -> str:
        return self.__sshKey

    @sshKey.setter
    def sshKey(self, sshKey: str):
        self.__sshKey = sshKey

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def is64os(self) -> bool:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: bool):
        self.__is64os = is64os

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
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

    @property
    def minStorage(self) -> int:
        return self.__minStorage

    @minStorage.setter
    def minStorage(self, minStorage: int):
        self.__minStorage = minStorage

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

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
    def providerSpecificTypeName(self) -> str:
        return self.__providerSpecificTypeName

    @providerSpecificTypeName.setter
    def providerSpecificTypeName(self, providerSpecificTypeName: str):
        self.__providerSpecificTypeName = providerSpecificTypeName

    @property
    def maxCores(self) -> int:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: int):
        self.__maxCores = maxCores

    @property
    def cloudml_VM31(self):
        return self.__cloudml_VM31

    @cloudml_VM31.setter
    def cloudml_VM31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_VM__cloudml_VM31", None)
        self.__cloudml_VM31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cloudml_VMPort"):
                    opp_val = getattr(item, "cloudml_VMPort", None)
                    
                    if opp_val == self:
                        setattr(item, "cloudml_VMPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cloudml_VMPort"):
                    opp_val = getattr(item, "cloudml_VMPort", None)
                    
                    setattr(item, "cloudml_VMPort", self)
                    

    @property
    def cloudml_VM(self):
        return self.__cloudml_VM

    @cloudml_VM.setter
    def cloudml_VM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_VM__cloudml_VM", None)
        self.__cloudml_VM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLModel21"):
                opp_val = getattr(old_value, "cloudml_CloudMLModel21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLModel21"):
                opp_val = getattr(value, "cloudml_CloudMLModel21", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLModel21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_ExternalComponentInstance(ComponentInstance):

    def __init__(self, ips: str, cloudml_ExternalComponentInstance: "cloudml_CloudMLModel" = None, cloudml_ExternalComponentInstance97: set["cloudml_VMPortInstance"] = None):
        self.ips = ips
        self.cloudml_ExternalComponentInstance = cloudml_ExternalComponentInstance
        self.cloudml_ExternalComponentInstance97 = cloudml_ExternalComponentInstance97 if cloudml_ExternalComponentInstance97 is not None else set()
        
    @property
    def ips(self) -> str:
        return self.__ips

    @ips.setter
    def ips(self, ips: str):
        self.__ips = ips

    @property
    def cloudml_ExternalComponentInstance97(self):
        return self.__cloudml_ExternalComponentInstance97

    @cloudml_ExternalComponentInstance97.setter
    def cloudml_ExternalComponentInstance97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ExternalComponentInstance__cloudml_ExternalComponentInstance97", None)
        self.__cloudml_ExternalComponentInstance97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cloudml_VMPortInstance98"):
                    opp_val = getattr(item, "cloudml_VMPortInstance98", None)
                    
                    if opp_val == self:
                        setattr(item, "cloudml_VMPortInstance98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cloudml_VMPortInstance98"):
                    opp_val = getattr(item, "cloudml_VMPortInstance98", None)
                    
                    setattr(item, "cloudml_VMPortInstance98", self)
                    

    @property
    def cloudml_ExternalComponentInstance(self):
        return self.__cloudml_ExternalComponentInstance

    @cloudml_ExternalComponentInstance.setter
    def cloudml_ExternalComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ExternalComponentInstance__cloudml_ExternalComponentInstance", None)
        self.__cloudml_ExternalComponentInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLModel19"):
                opp_val = getattr(old_value, "cloudml_CloudMLModel19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLModel19"):
                opp_val = getattr(value, "cloudml_CloudMLModel19", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLModel19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_InternalComponentInstance(ComponentInstance):

    pass
class cloudml_ExternalComponent(Component):

    def __init__(self, endPoint: str, login: str, passwd: str, location: str, serviceType: str, Region: str, cloudml_ExternalComponent: "cloudml_CloudMLModel" = None, cloudml_ExternalComponent91: "cloudml_Provider" = None, cloudml_ExternalComponent94: set["cloudml_VMPort"] = None):
        self.endPoint = endPoint
        self.login = login
        self.passwd = passwd
        self.location = location
        self.serviceType = serviceType
        self.Region = Region
        self.cloudml_ExternalComponent = cloudml_ExternalComponent
        self.cloudml_ExternalComponent91 = cloudml_ExternalComponent91
        self.cloudml_ExternalComponent94 = cloudml_ExternalComponent94 if cloudml_ExternalComponent94 is not None else set()
        
    @property
    def serviceType(self) -> str:
        return self.__serviceType

    @serviceType.setter
    def serviceType(self, serviceType: str):
        self.__serviceType = serviceType

    @property
    def passwd(self) -> str:
        return self.__passwd

    @passwd.setter
    def passwd(self, passwd: str):
        self.__passwd = passwd

    @property
    def Region(self) -> str:
        return self.__Region

    @Region.setter
    def Region(self, Region: str):
        self.__Region = Region

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def endPoint(self) -> str:
        return self.__endPoint

    @endPoint.setter
    def endPoint(self, endPoint: str):
        self.__endPoint = endPoint

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def cloudml_ExternalComponent91(self):
        return self.__cloudml_ExternalComponent91

    @cloudml_ExternalComponent91.setter
    def cloudml_ExternalComponent91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ExternalComponent__cloudml_ExternalComponent91", None)
        self.__cloudml_ExternalComponent91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Provider92"):
                opp_val = getattr(old_value, "cloudml_Provider92", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Provider92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Provider92"):
                opp_val = getattr(value, "cloudml_Provider92", None)
                setattr(value, "cloudml_Provider92", self)

    @property
    def cloudml_ExternalComponent(self):
        return self.__cloudml_ExternalComponent

    @cloudml_ExternalComponent.setter
    def cloudml_ExternalComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ExternalComponent__cloudml_ExternalComponent", None)
        self.__cloudml_ExternalComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLModel15"):
                opp_val = getattr(old_value, "cloudml_CloudMLModel15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLModel15"):
                opp_val = getattr(value, "cloudml_CloudMLModel15", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLModel15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_ExternalComponent94(self):
        return self.__cloudml_ExternalComponent94

    @cloudml_ExternalComponent94.setter
    def cloudml_ExternalComponent94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ExternalComponent__cloudml_ExternalComponent94", None)
        self.__cloudml_ExternalComponent94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cloudml_VMPort95"):
                    opp_val = getattr(item, "cloudml_VMPort95", None)
                    
                    if opp_val == self:
                        setattr(item, "cloudml_VMPort95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cloudml_VMPort95"):
                    opp_val = getattr(item, "cloudml_VMPort95", None)
                    
                    setattr(item, "cloudml_VMPort95", self)
                    

class cloudml_InternalComponent(Component):

    pass
class CloudMLElementWithProperties:

    pass
class cloudml_Provider(CloudMLElementWithProperties):

    def __init__(self, credentials: str, cloudml_Provider: "cloudml_CloudMLModel" = None, cloudml_Provider92: "cloudml_ExternalComponent" = None):
        self.credentials = credentials
        self.cloudml_Provider = cloudml_Provider
        self.cloudml_Provider92 = cloudml_Provider92
        
    @property
    def credentials(self) -> str:
        return self.__credentials

    @credentials.setter
    def credentials(self, credentials: str):
        self.__credentials = credentials

    @property
    def cloudml_Provider92(self):
        return self.__cloudml_Provider92

    @cloudml_Provider92.setter
    def cloudml_Provider92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Provider__cloudml_Provider92", None)
        self.__cloudml_Provider92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_ExternalComponent91"):
                opp_val = getattr(old_value, "cloudml_ExternalComponent91", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_ExternalComponent91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_ExternalComponent91"):
                opp_val = getattr(value, "cloudml_ExternalComponent91", None)
                setattr(value, "cloudml_ExternalComponent91", self)

    @property
    def cloudml_Provider(self):
        return self.__cloudml_Provider

    @cloudml_Provider.setter
    def cloudml_Provider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Provider__cloudml_Provider", None)
        self.__cloudml_Provider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLModel"):
                opp_val = getattr(old_value, "cloudml_CloudMLModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLModel"):
                opp_val = getattr(value, "cloudml_CloudMLModel", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_ExecutionPlatform(CloudMLElementWithProperties):

    pass
class cloudml_VMPortInstance(CloudMLElementWithProperties):

    pass
class cloudml_ComponentInstance(CloudMLElementWithProperties):

    pass
class cloudml_Cloud(CloudMLElementWithProperties):

    pass
class cloudml_VMPort(CloudMLElementWithProperties):

    pass
class cloudml_Component(CloudMLElementWithProperties):

    pass
class cloudml_ExecuteInstance(CloudMLElementWithProperties):

    pass
class cloudml_Relationship(CloudMLElementWithProperties):

    pass
class cloudml_RelationshipInstance(CloudMLElementWithProperties):

    pass
class cloudml_ExecutionPlatformInstance(CloudMLElementWithProperties):

    pass
class cloudml_PortInstance(CloudMLElementWithProperties):

    pass
class cloudml_CloudMLModel(CloudMLElementWithProperties):

    pass
class cloudml_Port(CloudMLElementWithProperties):

    def __init__(self, isLocal: bool, portNumber: int, cloudml_Port: "cloudml_Component" = None, cloudml_Port77: "cloudml_PortInstance" = None):
        self.isLocal = isLocal
        self.portNumber = portNumber
        self.cloudml_Port = cloudml_Port
        self.cloudml_Port77 = cloudml_Port77
        
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
    def cloudml_Port77(self):
        return self.__cloudml_Port77

    @cloudml_Port77.setter
    def cloudml_Port77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Port__cloudml_Port77", None)
        self.__cloudml_Port77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_PortInstance"):
                opp_val = getattr(old_value, "cloudml_PortInstance", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_PortInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_PortInstance"):
                opp_val = getattr(value, "cloudml_PortInstance", None)
                setattr(value, "cloudml_PortInstance", self)

    @property
    def cloudml_Port(self):
        return self.__cloudml_Port

    @cloudml_Port.setter
    def cloudml_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Port__cloudml_Port", None)
        self.__cloudml_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Component44"):
                opp_val = getattr(old_value, "cloudml_Component44", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Component44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Component44"):
                opp_val = getattr(value, "cloudml_Component44", None)
                setattr(value, "cloudml_Component44", self)

class cloudml_PuppetResource(Resource):

    def __init__(self, masterEndpoint: str, repositoryEndpoint: str, configureHostnameCommand: str, username: str, repositoryKey: str, configurationFile: str, manifestEntry: str, cloudml_PuppetResource: "cloudml_CloudMLElementWithProperties" = None):
        self.masterEndpoint = masterEndpoint
        self.repositoryEndpoint = repositoryEndpoint
        self.configureHostnameCommand = configureHostnameCommand
        self.username = username
        self.repositoryKey = repositoryKey
        self.configurationFile = configurationFile
        self.manifestEntry = manifestEntry
        self.cloudml_PuppetResource = cloudml_PuppetResource
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def manifestEntry(self) -> str:
        return self.__manifestEntry

    @manifestEntry.setter
    def manifestEntry(self, manifestEntry: str):
        self.__manifestEntry = manifestEntry

    @property
    def repositoryEndpoint(self) -> str:
        return self.__repositoryEndpoint

    @repositoryEndpoint.setter
    def repositoryEndpoint(self, repositoryEndpoint: str):
        self.__repositoryEndpoint = repositoryEndpoint

    @property
    def configureHostnameCommand(self) -> str:
        return self.__configureHostnameCommand

    @configureHostnameCommand.setter
    def configureHostnameCommand(self, configureHostnameCommand: str):
        self.__configureHostnameCommand = configureHostnameCommand

    @property
    def masterEndpoint(self) -> str:
        return self.__masterEndpoint

    @masterEndpoint.setter
    def masterEndpoint(self, masterEndpoint: str):
        self.__masterEndpoint = masterEndpoint

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
    def cloudml_PuppetResource(self):
        return self.__cloudml_PuppetResource

    @cloudml_PuppetResource.setter
    def cloudml_PuppetResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_PuppetResource__cloudml_PuppetResource", None)
        self.__cloudml_PuppetResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLElementWithProperties4"):
                opp_val = getattr(old_value, "cloudml_CloudMLElementWithProperties4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLElementWithProperties4"):
                opp_val = getattr(value, "cloudml_CloudMLElementWithProperties4", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLElementWithProperties4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_Resource(CloudMLElementWithProperties):

    def __init__(self, downloadCommand: str, uploadCommand: str, installCommand: str, configureCommand: str, startCommand: str, stopCommand: str, requireCredentials: bool, executeLocally: bool, cloudml_Resource: "cloudml_CloudMLElementWithProperties" = None, cloudml_Resource53: "cloudml_Relationship" = None, cloudml_Resource56: "cloudml_Relationship" = None):
        self.downloadCommand = downloadCommand
        self.uploadCommand = uploadCommand
        self.installCommand = installCommand
        self.configureCommand = configureCommand
        self.startCommand = startCommand
        self.stopCommand = stopCommand
        self.requireCredentials = requireCredentials
        self.executeLocally = executeLocally
        self.cloudml_Resource = cloudml_Resource
        self.cloudml_Resource53 = cloudml_Resource53
        self.cloudml_Resource56 = cloudml_Resource56
        
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
    def startCommand(self) -> str:
        return self.__startCommand

    @startCommand.setter
    def startCommand(self, startCommand: str):
        self.__startCommand = startCommand

    @property
    def executeLocally(self) -> bool:
        return self.__executeLocally

    @executeLocally.setter
    def executeLocally(self, executeLocally: bool):
        self.__executeLocally = executeLocally

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
    def requireCredentials(self) -> bool:
        return self.__requireCredentials

    @requireCredentials.setter
    def requireCredentials(self, requireCredentials: bool):
        self.__requireCredentials = requireCredentials

    @property
    def cloudml_Resource(self):
        return self.__cloudml_Resource

    @cloudml_Resource.setter
    def cloudml_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource", None)
        self.__cloudml_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLElementWithProperties2"):
                opp_val = getattr(old_value, "cloudml_CloudMLElementWithProperties2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLElementWithProperties2"):
                opp_val = getattr(value, "cloudml_CloudMLElementWithProperties2", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLElementWithProperties2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_Resource53(self):
        return self.__cloudml_Resource53

    @cloudml_Resource53.setter
    def cloudml_Resource53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource53", None)
        self.__cloudml_Resource53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Relationship52"):
                opp_val = getattr(old_value, "cloudml_Relationship52", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Relationship52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Relationship52"):
                opp_val = getattr(value, "cloudml_Relationship52", None)
                setattr(value, "cloudml_Relationship52", self)

    @property
    def cloudml_Resource56(self):
        return self.__cloudml_Resource56

    @cloudml_Resource56.setter
    def cloudml_Resource56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource56", None)
        self.__cloudml_Resource56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Relationship55"):
                opp_val = getattr(old_value, "cloudml_Relationship55", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Relationship55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Relationship55"):
                opp_val = getattr(value, "cloudml_Relationship55", None)
                setattr(value, "cloudml_Relationship55", self)

class CloudMLElement:

    pass
class cloudml_CloudMLElementWithProperties(CloudMLElement):

    pass
class cloudml_Property(CloudMLElement):

    def __init__(self, value: str, cloudml_Property: "cloudml_CloudMLElementWithProperties" = None, cloudml_Property111: "cloudml_RequiredExecutionPlatform" = None, cloudml_Property108: "cloudml_ProvidedExecutionPlatform" = None):
        self.value = value
        self.cloudml_Property = cloudml_Property
        self.cloudml_Property111 = cloudml_Property111
        self.cloudml_Property108 = cloudml_Property108
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def cloudml_Property(self):
        return self.__cloudml_Property

    @cloudml_Property.setter
    def cloudml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Property__cloudml_Property", None)
        self.__cloudml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_CloudMLElementWithProperties"):
                opp_val = getattr(old_value, "cloudml_CloudMLElementWithProperties", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_CloudMLElementWithProperties"):
                opp_val = getattr(value, "cloudml_CloudMLElementWithProperties", None)
                if opp_val is None:
                    setattr(value, "cloudml_CloudMLElementWithProperties", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_Property111(self):
        return self.__cloudml_Property111

    @cloudml_Property111.setter
    def cloudml_Property111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Property__cloudml_Property111", None)
        self.__cloudml_Property111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_RequiredExecutionPlatform110"):
                opp_val = getattr(old_value, "cloudml_RequiredExecutionPlatform110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_RequiredExecutionPlatform110"):
                opp_val = getattr(value, "cloudml_RequiredExecutionPlatform110", None)
                if opp_val is None:
                    setattr(value, "cloudml_RequiredExecutionPlatform110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_Property108(self):
        return self.__cloudml_Property108

    @cloudml_Property108.setter
    def cloudml_Property108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Property__cloudml_Property108", None)
        self.__cloudml_Property108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_ProvidedExecutionPlatform107"):
                opp_val = getattr(old_value, "cloudml_ProvidedExecutionPlatform107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_ProvidedExecutionPlatform107"):
                opp_val = getattr(value, "cloudml_ProvidedExecutionPlatform107", None)
                if opp_val is None:
                    setattr(value, "cloudml_ProvidedExecutionPlatform107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_CloudMLElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
