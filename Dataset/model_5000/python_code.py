from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArtefactPortInstance:

    pass
class cloudml_ServerPortInstance(ArtefactPortInstance):

    pass
class cloudml_ClientPortInstance(ArtefactPortInstance):

    pass
class ArtefactPort:

    pass
class cloudml_ClientPort(ArtefactPort):

    def __init__(self, isOptional: bool, cloudml_ClientPort: "cloudml_Artefact" = None, cloudml_ClientPort46: "cloudml_Binding" = None):
        self.isOptional = isOptional
        self.cloudml_ClientPort = cloudml_ClientPort
        self.cloudml_ClientPort46 = cloudml_ClientPort46
        
    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def cloudml_ClientPort(self):
        return self.__cloudml_ClientPort

    @cloudml_ClientPort.setter
    def cloudml_ClientPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ClientPort__cloudml_ClientPort", None)
        self.__cloudml_ClientPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Artefact23"):
                opp_val = getattr(old_value, "cloudml_Artefact23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Artefact23"):
                opp_val = getattr(value, "cloudml_Artefact23", None)
                if opp_val is None:
                    setattr(value, "cloudml_Artefact23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_ClientPort46(self):
        return self.__cloudml_ClientPort46

    @cloudml_ClientPort46.setter
    def cloudml_ClientPort46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ClientPort__cloudml_ClientPort46", None)
        self.__cloudml_ClientPort46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Binding45"):
                opp_val = getattr(old_value, "cloudml_Binding45", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Binding45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Binding45"):
                opp_val = getattr(value, "cloudml_Binding45", None)
                setattr(value, "cloudml_Binding45", self)

class cloudml_ServerPort(ArtefactPort):

    pass
class cloudml_UploadCommand:

    def __init__(self, source: str, target: str, cloudml_UploadCommand: "cloudml_Resource" = None):
        self.source = source
        self.target = target
        self.cloudml_UploadCommand = cloudml_UploadCommand
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def cloudml_UploadCommand(self):
        return self.__cloudml_UploadCommand

    @cloudml_UploadCommand.setter
    def cloudml_UploadCommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_UploadCommand__cloudml_UploadCommand", None)
        self.__cloudml_UploadCommand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Resource"):
                opp_val = getattr(old_value, "cloudml_Resource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Resource"):
                opp_val = getattr(value, "cloudml_Resource", None)
                if opp_val is None:
                    setattr(value, "cloudml_Resource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WithProperties:

    pass
class cloudml_ArtefactPortInstance(WithProperties):

    pass
class cloudml_Artefact(WithProperties):

    pass
class cloudml_Node(WithProperties):

    def __init__(self, minRam: int, minCore: int, minDisk: int, location: str, OS: str, sshKey: str, securityGroup: str, groupName: str, privateKey: str, imageID: str, is64os: bool, cloudml_Node: "cloudml_DeploymentModel" = None, cloudml_Node25: "cloudml_Provider" = None, cloudml_Node41: "cloudml_NodeInstance" = None):
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
        self.cloudml_Node = cloudml_Node
        self.cloudml_Node25 = cloudml_Node25
        self.cloudml_Node41 = cloudml_Node41
        
    @property
    def imageID(self) -> str:
        return self.__imageID

    @imageID.setter
    def imageID(self, imageID: str):
        self.__imageID = imageID

    @property
    def minDisk(self) -> int:
        return self.__minDisk

    @minDisk.setter
    def minDisk(self, minDisk: int):
        self.__minDisk = minDisk

    @property
    def sshKey(self) -> str:
        return self.__sshKey

    @sshKey.setter
    def sshKey(self, sshKey: str):
        self.__sshKey = sshKey

    @property
    def is64os(self) -> bool:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: bool):
        self.__is64os = is64os

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def minRam(self) -> int:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: int):
        self.__minRam = minRam

    @property
    def OS(self) -> str:
        return self.__OS

    @OS.setter
    def OS(self, OS: str):
        self.__OS = OS

    @property
    def minCore(self) -> int:
        return self.__minCore

    @minCore.setter
    def minCore(self, minCore: int):
        self.__minCore = minCore

    @property
    def cloudml_Node41(self):
        return self.__cloudml_Node41

    @cloudml_Node41.setter
    def cloudml_Node41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Node__cloudml_Node41", None)
        self.__cloudml_Node41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_NodeInstance40"):
                opp_val = getattr(old_value, "cloudml_NodeInstance40", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_NodeInstance40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_NodeInstance40"):
                opp_val = getattr(value, "cloudml_NodeInstance40", None)
                setattr(value, "cloudml_NodeInstance40", self)

    @property
    def cloudml_Node(self):
        return self.__cloudml_Node

    @cloudml_Node.setter
    def cloudml_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Node__cloudml_Node", None)
        self.__cloudml_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_DeploymentModel6"):
                opp_val = getattr(old_value, "cloudml_DeploymentModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_DeploymentModel6"):
                opp_val = getattr(value, "cloudml_DeploymentModel6", None)
                if opp_val is None:
                    setattr(value, "cloudml_DeploymentModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_Node25(self):
        return self.__cloudml_Node25

    @cloudml_Node25.setter
    def cloudml_Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Node__cloudml_Node25", None)
        self.__cloudml_Node25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Provider26"):
                opp_val = getattr(old_value, "cloudml_Provider26", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Provider26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Provider26"):
                opp_val = getattr(value, "cloudml_Provider26", None)
                setattr(value, "cloudml_Provider26", self)

class cloudml_DeploymentModel(WithProperties):

    pass
class cloudml_ArtefactInstance(WithProperties):

    pass
class cloudml_BindingInstance(WithProperties):

    pass
class cloudml_Provider(WithProperties):

    def __init__(self, credentials: str, cloudml_Provider: "cloudml_DeploymentModel" = None, cloudml_Provider26: "cloudml_Node" = None):
        self.credentials = credentials
        self.cloudml_Provider = cloudml_Provider
        self.cloudml_Provider26 = cloudml_Provider26
        
    @property
    def credentials(self) -> str:
        return self.__credentials

    @credentials.setter
    def credentials(self, credentials: str):
        self.__credentials = credentials

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
            if hasattr(old_value, "cloudml_DeploymentModel"):
                opp_val = getattr(old_value, "cloudml_DeploymentModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_DeploymentModel"):
                opp_val = getattr(value, "cloudml_DeploymentModel", None)
                if opp_val is None:
                    setattr(value, "cloudml_DeploymentModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cloudml_Provider26(self):
        return self.__cloudml_Provider26

    @cloudml_Provider26.setter
    def cloudml_Provider26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Provider__cloudml_Provider26", None)
        self.__cloudml_Provider26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Node25"):
                opp_val = getattr(old_value, "cloudml_Node25", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Node25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Node25"):
                opp_val = getattr(value, "cloudml_Node25", None)
                setattr(value, "cloudml_Node25", self)

class cloudml_NodeInstance(WithProperties):

    def __init__(self, publicAddress: str, id: str, cloudml_NodeInstance: "cloudml_DeploymentModel" = None, cloudml_NodeInstance34: "cloudml_ArtefactInstance" = None, cloudml_NodeInstance40: "cloudml_Node" = None):
        self.publicAddress = publicAddress
        self.id = id
        self.cloudml_NodeInstance = cloudml_NodeInstance
        self.cloudml_NodeInstance34 = cloudml_NodeInstance34
        self.cloudml_NodeInstance40 = cloudml_NodeInstance40
        
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
    def cloudml_NodeInstance40(self):
        return self.__cloudml_NodeInstance40

    @cloudml_NodeInstance40.setter
    def cloudml_NodeInstance40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_NodeInstance__cloudml_NodeInstance40", None)
        self.__cloudml_NodeInstance40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Node41"):
                opp_val = getattr(old_value, "cloudml_Node41", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Node41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Node41"):
                opp_val = getattr(value, "cloudml_Node41", None)
                setattr(value, "cloudml_Node41", self)

    @property
    def cloudml_NodeInstance34(self):
        return self.__cloudml_NodeInstance34

    @cloudml_NodeInstance34.setter
    def cloudml_NodeInstance34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_NodeInstance__cloudml_NodeInstance34", None)
        self.__cloudml_NodeInstance34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_ArtefactInstance33"):
                opp_val = getattr(old_value, "cloudml_ArtefactInstance33", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_ArtefactInstance33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_ArtefactInstance33"):
                opp_val = getattr(value, "cloudml_ArtefactInstance33", None)
                setattr(value, "cloudml_ArtefactInstance33", self)

    @property
    def cloudml_NodeInstance(self):
        return self.__cloudml_NodeInstance

    @cloudml_NodeInstance.setter
    def cloudml_NodeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_NodeInstance__cloudml_NodeInstance", None)
        self.__cloudml_NodeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_DeploymentModel12"):
                opp_val = getattr(old_value, "cloudml_DeploymentModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_DeploymentModel12"):
                opp_val = getattr(value, "cloudml_DeploymentModel12", None)
                if opp_val is None:
                    setattr(value, "cloudml_DeploymentModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cloudml_ArtefactPort(WithProperties):

    def __init__(self, portNumber: int, isRemote: bool, cloudml_ArtefactPort: "cloudml_Artefact" = None, cloudml_ArtefactPort28: "cloudml_ArtefactPortInstance" = None):
        self.portNumber = portNumber
        self.isRemote = isRemote
        self.cloudml_ArtefactPort = cloudml_ArtefactPort
        self.cloudml_ArtefactPort28 = cloudml_ArtefactPort28
        
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

    @property
    def cloudml_ArtefactPort28(self):
        return self.__cloudml_ArtefactPort28

    @cloudml_ArtefactPort28.setter
    def cloudml_ArtefactPort28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ArtefactPort__cloudml_ArtefactPort28", None)
        self.__cloudml_ArtefactPort28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_ArtefactPortInstance"):
                opp_val = getattr(old_value, "cloudml_ArtefactPortInstance", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_ArtefactPortInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_ArtefactPortInstance"):
                opp_val = getattr(value, "cloudml_ArtefactPortInstance", None)
                setattr(value, "cloudml_ArtefactPortInstance", self)

    @property
    def cloudml_ArtefactPort(self):
        return self.__cloudml_ArtefactPort

    @cloudml_ArtefactPort.setter
    def cloudml_ArtefactPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_ArtefactPort__cloudml_ArtefactPort", None)
        self.__cloudml_ArtefactPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Artefact16"):
                opp_val = getattr(old_value, "cloudml_Artefact16", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Artefact16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Artefact16"):
                opp_val = getattr(value, "cloudml_Artefact16", None)
                setattr(value, "cloudml_Artefact16", self)

class cloudml_Binding(WithProperties):

    pass
class cloudml_Resource(WithProperties):

    def __init__(self, retrievingCommand: str, deployingCommand: str, configurationCommand: str, startCommand: str, stopCommand: str, cloudml_Resource: set["cloudml_UploadCommand"] = None, cloudml_Resource19: "cloudml_Artefact" = None, cloudml_Resource52: "cloudml_Binding" = None, cloudml_Resource55: "cloudml_Binding" = None):
        self.retrievingCommand = retrievingCommand
        self.deployingCommand = deployingCommand
        self.configurationCommand = configurationCommand
        self.startCommand = startCommand
        self.stopCommand = stopCommand
        self.cloudml_Resource = cloudml_Resource if cloudml_Resource is not None else set()
        self.cloudml_Resource19 = cloudml_Resource19
        self.cloudml_Resource52 = cloudml_Resource52
        self.cloudml_Resource55 = cloudml_Resource55
        
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
    def stopCommand(self) -> str:
        return self.__stopCommand

    @stopCommand.setter
    def stopCommand(self, stopCommand: str):
        self.__stopCommand = stopCommand

    @property
    def deployingCommand(self) -> str:
        return self.__deployingCommand

    @deployingCommand.setter
    def deployingCommand(self, deployingCommand: str):
        self.__deployingCommand = deployingCommand

    @property
    def configurationCommand(self) -> str:
        return self.__configurationCommand

    @configurationCommand.setter
    def configurationCommand(self, configurationCommand: str):
        self.__configurationCommand = configurationCommand

    @property
    def cloudml_Resource52(self):
        return self.__cloudml_Resource52

    @cloudml_Resource52.setter
    def cloudml_Resource52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource52", None)
        self.__cloudml_Resource52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Binding51"):
                opp_val = getattr(old_value, "cloudml_Binding51", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Binding51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Binding51"):
                opp_val = getattr(value, "cloudml_Binding51", None)
                setattr(value, "cloudml_Binding51", self)

    @property
    def cloudml_Resource19(self):
        return self.__cloudml_Resource19

    @cloudml_Resource19.setter
    def cloudml_Resource19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource19", None)
        self.__cloudml_Resource19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Artefact18"):
                opp_val = getattr(old_value, "cloudml_Artefact18", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Artefact18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Artefact18"):
                opp_val = getattr(value, "cloudml_Artefact18", None)
                setattr(value, "cloudml_Artefact18", self)

    @property
    def cloudml_Resource55(self):
        return self.__cloudml_Resource55

    @cloudml_Resource55.setter
    def cloudml_Resource55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource55", None)
        self.__cloudml_Resource55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cloudml_Binding54"):
                opp_val = getattr(old_value, "cloudml_Binding54", None)
                if opp_val == self:
                    setattr(old_value, "cloudml_Binding54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_Binding54"):
                opp_val = getattr(value, "cloudml_Binding54", None)
                setattr(value, "cloudml_Binding54", self)

    @property
    def cloudml_Resource(self):
        return self.__cloudml_Resource

    @cloudml_Resource.setter
    def cloudml_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cloudml_Resource__cloudml_Resource", None)
        self.__cloudml_Resource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cloudml_UploadCommand"):
                    opp_val = getattr(item, "cloudml_UploadCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "cloudml_UploadCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cloudml_UploadCommand"):
                    opp_val = getattr(item, "cloudml_UploadCommand", None)
                    
                    setattr(item, "cloudml_UploadCommand", self)
                    

class NamedElement:

    pass
class cloudml_Composite(NamedElement):

    pass
class cloudml_WithProperties(NamedElement):

    pass
class cloudml_Property(NamedElement):

    def __init__(self, value: str, cloudml_Property: "cloudml_WithProperties" = None):
        self.value = value
        self.cloudml_Property = cloudml_Property
        
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
            if hasattr(old_value, "cloudml_WithProperties"):
                opp_val = getattr(old_value, "cloudml_WithProperties", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cloudml_WithProperties"):
                opp_val = getattr(value, "cloudml_WithProperties", None)
                if opp_val is None:
                    setattr(value, "cloudml_WithProperties", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CloudMLElement:

    pass
class cloudml_NamedElement(CloudMLElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class cloudml_CloudMLElement(ABC):

    pass