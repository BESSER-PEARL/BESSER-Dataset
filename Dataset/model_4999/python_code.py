from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class cloudml_core_UploadCommand:

    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class ClientPortInstance:

    pass
class ServerPortInstance:

    pass
class ArtefactPortInstance:

    pass
class cloudml_core_ClientPortInstance(ArtefactPortInstance):

    pass
class cloudml_core_ServerPortInstance(ArtefactPortInstance):

    pass
class ClientPort:

    pass
class ServerPort:

    pass
class Resource:

    pass
class ArtefactPort:

    pass
class cloudml_core_ClientPort(ArtefactPort):

    def __init__(self, isOptional: bool, ArtefactPort25: "cloudml_core_ArtefactPortInstance", ArtefactPort: "cloudml_core_Artefact"):
        self.isOptional = isOptional
        
    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

class cloudml_core_ServerPort(ArtefactPort):

    pass
class BindingInstance:

    pass
class NodeInstance:

    pass
class ArtefactInstance:

    pass
class Binding:

    pass
class Node:

    pass
class Artefact:

    pass
class Provider:

    pass
class UploadCommand:

    pass
class WithProperties:

    pass
class cloudml_core_ArtefactPortInstance(WithProperties):

    pass
class cloudml_core_NodeInstance(WithProperties):

    def __init__(self, publicAddress: str, id: str, cloudml_core_NodeInstance: "Node" = None):
        self.publicAddress = publicAddress
        self.id = id
        self.cloudml_core_NodeInstance = cloudml_core_NodeInstance
        
    @property
    def publicAddress(self) -> str:
        return self.__publicAddress

    @publicAddress.setter
    def publicAddress(self, publicAddress: str):
        self.__publicAddress = publicAddress

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def cloudml_core_NodeInstance(self):
        return self.__cloudml_core_NodeInstance

    @cloudml_core_NodeInstance.setter
    def cloudml_core_NodeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_NodeInstance__cloudml_core_NodeInstance", None)
        self.__cloudml_core_NodeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node36"):
                opp_val = getattr(old_value, "Node36", None)
                if opp_val == self:
                    setattr(old_value, "Node36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node36"):
                opp_val = getattr(value, "Node36", None)
                setattr(value, "Node36", self)

class cloudml_core_Node(WithProperties):

    def __init__(self, minRam: int, minCore: int, minDisk: int, location: str, OS: str, sshKey: str, securityGroup: str, groupName: str, privateKey: str, imageID: str, is64os: bool, cloudml_core_Node: "Provider" = None):
        self.minRam = minRam
        self.minCore = minCore
        self.minDisk = minDisk
        self.location = location
        self.OS = OS
        self.sshKey = sshKey
        self.securityGroup = securityGroup
        self.groupName = groupName
        self.privateKey = privateKey
        self.imageID = imageID
        self.is64os = is64os
        self.cloudml_core_Node = cloudml_core_Node
        
    @property
    def OS(self) -> str:
        return self.__OS

    @OS.setter
    def OS(self, OS: str):
        self.__OS = OS

    @property
    def imageID(self) -> str:
        return self.__imageID

    @imageID.setter
    def imageID(self, imageID: str):
        self.__imageID = imageID

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
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def minDisk(self) -> int:
        return self.__minDisk

    @minDisk.setter
    def minDisk(self, minDisk: int):
        self.__minDisk = minDisk

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def sshKey(self) -> str:
        return self.__sshKey

    @sshKey.setter
    def sshKey(self, sshKey: str):
        self.__sshKey = sshKey

    @property
    def minCore(self) -> int:
        return self.__minCore

    @minCore.setter
    def minCore(self, minCore: int):
        self.__minCore = minCore

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def cloudml_core_Node(self):
        return self.__cloudml_core_Node

    @cloudml_core_Node.setter
    def cloudml_core_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_Node__cloudml_core_Node", None)
        self.__cloudml_core_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider23"):
                opp_val = getattr(old_value, "Provider23", None)
                if opp_val == self:
                    setattr(old_value, "Provider23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider23"):
                opp_val = getattr(value, "Provider23", None)
                setattr(value, "Provider23", self)

class cloudml_core_Artefact(WithProperties):

    pass
class cloudml_core_DeploymentModel(WithProperties):

    pass
class cloudml_core_Binding(WithProperties):

    pass
class cloudml_core_Provider(WithProperties):

    def __init__(self, credentials: str):
        self.credentials = credentials
        
    @property
    def credentials(self) -> str:
        return self.__credentials

    @credentials.setter
    def credentials(self, credentials: str):
        self.__credentials = credentials

class cloudml_core_ArtefactPort(WithProperties):

    def __init__(self, portNumber: int, isRemote: bool):
        self.portNumber = portNumber
        self.isRemote = isRemote
        
    @property
    def isRemote(self) -> bool:
        return self.__isRemote

    @isRemote.setter
    def isRemote(self, isRemote: bool):
        self.__isRemote = isRemote

    @property
    def portNumber(self) -> int:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: int):
        self.__portNumber = portNumber

class cloudml_core_ArtefactInstance(WithProperties):

    pass
class cloudml_core_BindingInstance(WithProperties):

    pass
class cloudml_core_Resource(WithProperties):

    def __init__(self, retrievingCommand: str, deployingCommand: str, configurationCommand: str, startCommand: str, stopCommand: str, cloudml_core_Resource: set["UploadCommand"] = None):
        self.retrievingCommand = retrievingCommand
        self.deployingCommand = deployingCommand
        self.configurationCommand = configurationCommand
        self.startCommand = startCommand
        self.stopCommand = stopCommand
        self.cloudml_core_Resource = cloudml_core_Resource if cloudml_core_Resource is not None else set()
        
    @property
    def retrievingCommand(self) -> str:
        return self.__retrievingCommand

    @retrievingCommand.setter
    def retrievingCommand(self, retrievingCommand: str):
        self.__retrievingCommand = retrievingCommand

    @property
    def deployingCommand(self) -> str:
        return self.__deployingCommand

    @deployingCommand.setter
    def deployingCommand(self, deployingCommand: str):
        self.__deployingCommand = deployingCommand

    @property
    def stopCommand(self) -> str:
        return self.__stopCommand

    @stopCommand.setter
    def stopCommand(self, stopCommand: str):
        self.__stopCommand = stopCommand

    @property
    def configurationCommand(self) -> str:
        return self.__configurationCommand

    @configurationCommand.setter
    def configurationCommand(self, configurationCommand: str):
        self.__configurationCommand = configurationCommand

    @property
    def startCommand(self) -> str:
        return self.__startCommand

    @startCommand.setter
    def startCommand(self, startCommand: str):
        self.__startCommand = startCommand

    @property
    def cloudml_core_Resource(self):
        return self.__cloudml_core_Resource

    @cloudml_core_Resource.setter
    def cloudml_core_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_Resource__cloudml_core_Resource", None)
        self.__cloudml_core_Resource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UploadCommand"):
                    opp_val = getattr(item, "UploadCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "UploadCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UploadCommand"):
                    opp_val = getattr(item, "UploadCommand", None)
                    
                    setattr(item, "UploadCommand", self)
                    

class Property:

    pass
class NamedElement:

    pass
class cloudml_core_WithProperties(NamedElement):

    pass
class cloudml_core_Composite(NamedElement):

    pass
class cloudml_core_Property(NamedElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CloudMLElement:

    pass
class cloudml_core_NamedElement(CloudMLElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class cloudml_core_CloudMLElement(ABC):

    pass