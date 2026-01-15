from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Provider:

    pass
class NodePort:

    pass
class ArtefactPortInstance:

    pass
class NodePortInstance:

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
class Resource:

    pass
class ArtefactPort:

    pass
class NodeInstance:

    pass
class ArtefactInstance:

    pass
class Node:

    pass
class Artefact:

    pass
class WithProperties:

    pass
class cloudml_core_DeploymentModel(WithProperties):

    pass
class cloudml_core_NodeInstance(WithProperties):

    def __init__(self, publicAddress: str, cloudml_core_NodeInstance: "NodeInstance" = None, cloudml_core_NodeInstance48: set["NodePortInstance"] = None):
        self.publicAddress = publicAddress
        self.cloudml_core_NodeInstance = cloudml_core_NodeInstance
        self.cloudml_core_NodeInstance48 = cloudml_core_NodeInstance48 if cloudml_core_NodeInstance48 is not None else set()
        
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
            if hasattr(old_value, "NodeInstance46"):
                opp_val = getattr(old_value, "NodeInstance46", None)
                if opp_val == self:
                    setattr(old_value, "NodeInstance46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeInstance46"):
                opp_val = getattr(value, "NodeInstance46", None)
                setattr(value, "NodeInstance46", self)

    @property
    def cloudml_core_NodeInstance48(self):
        return self.__cloudml_core_NodeInstance48

    @cloudml_core_NodeInstance48.setter
    def cloudml_core_NodeInstance48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_NodeInstance__cloudml_core_NodeInstance48", None)
        self.__cloudml_core_NodeInstance48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodePortInstance49"):
                    opp_val = getattr(item, "NodePortInstance49", None)
                    
                    if opp_val == self:
                        setattr(item, "NodePortInstance49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodePortInstance49"):
                    opp_val = getattr(item, "NodePortInstance49", None)
                    
                    setattr(item, "NodePortInstance49", self)
                    

class cloudml_core_ArtefactPort(WithProperties):

    pass
class cloudml_core_Artefact(WithProperties):

    pass
class cloudml_core_NodePort(WithProperties):

    pass
class cloudml_core_Node(WithProperties):

    def __init__(self, privateKey: str, imageID: str, is64os: bool, minRam: int, minCore: int, minDisk: int, location: str, OS: str, sshKey: str, securityGroup: str, groupName: str, cloudml_core_Node: set["NodePort"] = None, cloudml_core_Node25: "Provider" = None):
        self.privateKey = privateKey
        self.imageID = imageID
        self.is64os = is64os
        self.minRam = minRam
        self.minCore = minCore
        self.minDisk = minDisk
        self.location = location
        self.OS = OS
        self.sshKey = sshKey
        self.securityGroup = securityGroup
        self.groupName = groupName
        self.cloudml_core_Node = cloudml_core_Node if cloudml_core_Node is not None else set()
        self.cloudml_core_Node25 = cloudml_core_Node25
        
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
    def minCore(self) -> int:
        return self.__minCore

    @minCore.setter
    def minCore(self, minCore: int):
        self.__minCore = minCore

    @property
    def OS(self) -> str:
        return self.__OS

    @OS.setter
    def OS(self, OS: str):
        self.__OS = OS

    @property
    def minDisk(self) -> int:
        return self.__minDisk

    @minDisk.setter
    def minDisk(self, minDisk: int):
        self.__minDisk = minDisk

    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

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
                    

    @property
    def cloudml_core_Node25(self):
        return self.__cloudml_core_Node25

    @cloudml_core_Node25.setter
    def cloudml_core_Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_core_Node__cloudml_core_Node25", None)
        self.__cloudml_core_Node25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider"):
                opp_val = getattr(old_value, "Provider", None)
                if opp_val == self:
                    setattr(old_value, "Provider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider"):
                opp_val = getattr(value, "Provider", None)
                setattr(value, "Provider", self)

class cloudml_core_NodePortInstance(WithProperties):

    pass
class cloudml_core_ArtefactInstance(WithProperties):

    pass
class cloudml_core_Provider(WithProperties):

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        
    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

class cloudml_core_ArtefactPortInstance(WithProperties):

    pass
class cloudml_core_Resource(WithProperties):

    def __init__(self, retrievingResourceCommand: str, deployingResourceCommand: str):
        self.retrievingResourceCommand = retrievingResourceCommand
        self.deployingResourceCommand = deployingResourceCommand
        
    @property
    def deployingResourceCommand(self) -> str:
        return self.__deployingResourceCommand

    @deployingResourceCommand.setter
    def deployingResourceCommand(self, deployingResourceCommand: str):
        self.__deployingResourceCommand = deployingResourceCommand

    @property
    def retrievingResourceCommand(self) -> str:
        return self.__retrievingResourceCommand

    @retrievingResourceCommand.setter
    def retrievingResourceCommand(self, retrievingResourceCommand: str):
        self.__retrievingResourceCommand = retrievingResourceCommand

class Property:

    pass