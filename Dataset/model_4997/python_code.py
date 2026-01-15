from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NodePort:

    pass
class ArtefactPortInstance:

    pass
class NodePortInstance:

    pass
class WithProperties:

    pass
class cloudml_core_ArtefactPortInstance(WithProperties):

    pass
class cloudml_core_Node(WithProperties):

    def __init__(self, minCore: int, minDisk: int, location: str, OS: str, sshKey: str, securityGroup: str, groupName: str, privateKey: str, imageID: str, is64os: bool, minRam: int, cloudml_core_Node: set["NodePort"] = None, cloudml_core_Node27: "Provider" = None):
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
        self.minRam = minRam
        self.cloudml_core_Node = cloudml_core_Node if cloudml_core_Node is not None else set()
        self.cloudml_core_Node27 = cloudml_core_Node27
        
    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def is64os(self) -> bool:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: bool):
        self.__is64os = is64os

    @property
    def imageID(self) -> str:
        return self.__imageID

    @imageID.setter
    def imageID(self, imageID: str):
        self.__imageID = imageID

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
    def minCore(self) -> int:
        return self.__minCore

    @minCore.setter
    def minCore(self, minCore: int):
        self.__minCore = minCore

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

    @property
    def minDisk(self) -> int:
        return self.__minDisk

    @minDisk.setter
    def minDisk(self, minDisk: int):
        self.__minDisk = minDisk

    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def OS(self) -> str:
        return self.__OS

    @OS.setter
    def OS(self, OS: str):
        self.__OS = OS

    @property
    def cloudml_core_Node27(self):
        return self.__cloudml_core_Node27

    @cloudml_core_Node27.setter
    def cloudml_core_Node27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_Node__cloudml_core_Node27", None)
        self.__cloudml_core_Node27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider28"):
                opp_val = getattr(old_value, "Provider28", None)
                if opp_val == self:
                    setattr(old_value, "Provider28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider28"):
                opp_val = getattr(value, "Provider28", None)
                setattr(value, "Provider28", self)

    @property
    def cloudml_core_Node(self):
        return self.__cloudml_core_Node

    @cloudml_core_Node.setter
    def cloudml_core_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_Node__cloudml_core_Node", None)
        self.__cloudml_core_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodePort"):
                    opp_val = getattr(item, "NodePort", None)
                    
                    if opp_val == self:
                        setattr(item, "NodePort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodePort"):
                    opp_val = getattr(item, "NodePort", None)
                    
                    setattr(item, "NodePort", self)
                    

class cloudml_core_NodePortInstance(WithProperties):

    pass
class cloudml_core_NodeInstance(WithProperties):

    def __init__(self, publicAddress: str, cloudml_core_NodeInstance: "Node" = None, cloudml_core_NodeInstance51: set["NodePortInstance"] = None):
        self.publicAddress = publicAddress
        self.cloudml_core_NodeInstance = cloudml_core_NodeInstance
        self.cloudml_core_NodeInstance51 = cloudml_core_NodeInstance51 if cloudml_core_NodeInstance51 is not None else set()
        
    @property
    def publicAddress(self) -> str:
        return self.__publicAddress

    @publicAddress.setter
    def publicAddress(self, publicAddress: str):
        self.__publicAddress = publicAddress

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
            if hasattr(old_value, "Node49"):
                opp_val = getattr(old_value, "Node49", None)
                if opp_val == self:
                    setattr(old_value, "Node49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node49"):
                opp_val = getattr(value, "Node49", None)
                setattr(value, "Node49", self)

    @property
    def cloudml_core_NodeInstance51(self):
        return self.__cloudml_core_NodeInstance51

    @cloudml_core_NodeInstance51.setter
    def cloudml_core_NodeInstance51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_NodeInstance__cloudml_core_NodeInstance51", None)
        self.__cloudml_core_NodeInstance51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodePortInstance52"):
                    opp_val = getattr(item, "NodePortInstance52", None)
                    
                    if opp_val == self:
                        setattr(item, "NodePortInstance52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodePortInstance52"):
                    opp_val = getattr(item, "NodePortInstance52", None)
                    
                    setattr(item, "NodePortInstance52", self)
                    

class cloudml_core_NodePort(WithProperties):

    pass
class cloudml_core_ArtefactInstance(WithProperties):

    pass
class cloudml_core_Resource(WithProperties):

    def __init__(self, deployingCommand: str, configurationCommand: str, startCommand: str, retrievingCommand: str):
        self.deployingCommand = deployingCommand
        self.configurationCommand = configurationCommand
        self.startCommand = startCommand
        self.retrievingCommand = retrievingCommand
        
    @property
    def deployingCommand(self) -> str:
        return self.__deployingCommand

    @deployingCommand.setter
    def deployingCommand(self, deployingCommand: str):
        self.__deployingCommand = deployingCommand

    @property
    def startCommand(self) -> str:
        return self.__startCommand

    @startCommand.setter
    def startCommand(self, startCommand: str):
        self.__startCommand = startCommand

    @property
    def retrievingCommand(self) -> str:
        return self.__retrievingCommand

    @retrievingCommand.setter
    def retrievingCommand(self, retrievingCommand: str):
        self.__retrievingCommand = retrievingCommand

    @property
    def configurationCommand(self) -> str:
        return self.__configurationCommand

    @configurationCommand.setter
    def configurationCommand(self, configurationCommand: str):
        self.__configurationCommand = configurationCommand

class Property:

    pass
class NamedElement:

    pass
class cloudml_core_Composite(NamedElement):

    pass
class cloudml_core_WithProperties(NamedElement):

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
class Resource:

    pass
class ArtefactPort:

    pass
class cloudml_core_Artefact(WithProperties):

    pass
class cloudml_core_ArtefactPort(WithProperties):

    def __init__(self, portNumber: int):
        self.portNumber = portNumber
        
    @property
    def portNumber(self) -> int:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: int):
        self.__portNumber = portNumber

class NodeInstance:

    pass
class ArtefactInstance:

    pass
class Node:

    pass
class Artefact:

    pass
class Provider:

    pass
class cloudml_core_DeploymentModel(WithProperties):

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
