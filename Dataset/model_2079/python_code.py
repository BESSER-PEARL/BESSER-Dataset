from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Language(Enum):
    PYTHON = "PYTHON"
    BASH = "BASH"
    JAVA = "JAVA"
class VMSize(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"
class ProviderType(Enum):
    FCO = "FCO"
    Openstack = "Openstack"


############################################
# Definition of Classes
############################################

class PeerToPeerPlatform:

    pass
class ddsm_KafkaCluster(PeerToPeerPlatform):

    pass
class ddsm_CassandraCluster(PeerToPeerPlatform):

    pass
class ddsm_ZookeeperCluster(PeerToPeerPlatform):

    def __init__(self, tickTime: int, syncLimit: int, initLimit: int):
        self.tickTime = tickTime
        self.syncLimit = syncLimit
        self.initLimit = initLimit
        
    @property
    def tickTime(self) -> int:
        return self.__tickTime

    @tickTime.setter
    def tickTime(self, tickTime: int):
        self.__tickTime = tickTime

    @property
    def initLimit(self) -> int:
        return self.__initLimit

    @initLimit.setter
    def initLimit(self, initLimit: int):
        self.__initLimit = initLimit

    @property
    def syncLimit(self) -> int:
        return self.__syncLimit

    @syncLimit.setter
    def syncLimit(self, syncLimit: int):
        self.__syncLimit = syncLimit

class ddsm_Crontab:

    def __init__(self, min: int, hour: int, dayOfMonth: int, month: int, dayOfWeek: int, ddsm_Crontab: "ddsm_ClientNode" = None):
        self.min = min
        self.hour = hour
        self.dayOfMonth = dayOfMonth
        self.month = month
        self.dayOfWeek = dayOfWeek
        self.ddsm_Crontab = ddsm_Crontab
        
    @property
    def dayOfMonth(self) -> int:
        return self.__dayOfMonth

    @dayOfMonth.setter
    def dayOfMonth(self, dayOfMonth: int):
        self.__dayOfMonth = dayOfMonth

    @property
    def hour(self) -> int:
        return self.__hour

    @hour.setter
    def hour(self, hour: int):
        self.__hour = hour

    @property
    def dayOfWeek(self) -> int:
        return self.__dayOfWeek

    @dayOfWeek.setter
    def dayOfWeek(self, dayOfWeek: int):
        self.__dayOfWeek = dayOfWeek

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def month(self) -> int:
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month

    @property
    def ddsm_Crontab(self):
        return self.__ddsm_Crontab

    @ddsm_Crontab.setter
    def ddsm_Crontab(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Crontab__ddsm_Crontab", None)
        self.__ddsm_Crontab = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_ClientNode56"):
                opp_val = getattr(old_value, "ddsm_ClientNode56", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_ClientNode56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_ClientNode56"):
                opp_val = getattr(value, "ddsm_ClientNode56", None)
                setattr(value, "ddsm_ClientNode56", self)

class InternalComponent:

    pass
class ddsm_MasterNode(InternalComponent):

    pass
class ddsm_MasterSlavePlatform(InternalComponent):

    pass
class ddsm_PeersQuorum(InternalComponent):

    pass
class ddsm_PeerNode(InternalComponent):

    pass
class ddsm_SlaveNode(InternalComponent):

    pass
class ddsm_PeerToPeerPlatform(InternalComponent):

    pass
class ddsm_ClientNode(InternalComponent):

    def __init__(self, skipRunningJob: bool, numberOfSubmissions: int, ddsm_ClientNode: "ddsm_JobSubmission" = None, ddsm_ClientNode56: "ddsm_Crontab" = None):
        self.skipRunningJob = skipRunningJob
        self.numberOfSubmissions = numberOfSubmissions
        self.ddsm_ClientNode = ddsm_ClientNode
        self.ddsm_ClientNode56 = ddsm_ClientNode56
        
    @property
    def numberOfSubmissions(self) -> int:
        return self.__numberOfSubmissions

    @numberOfSubmissions.setter
    def numberOfSubmissions(self, numberOfSubmissions: int):
        self.__numberOfSubmissions = numberOfSubmissions

    @property
    def skipRunningJob(self) -> bool:
        return self.__skipRunningJob

    @skipRunningJob.setter
    def skipRunningJob(self, skipRunningJob: bool):
        self.__skipRunningJob = skipRunningJob

    @property
    def ddsm_ClientNode(self):
        return self.__ddsm_ClientNode

    @ddsm_ClientNode.setter
    def ddsm_ClientNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_ClientNode__ddsm_ClientNode", None)
        self.__ddsm_ClientNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_JobSubmission"):
                opp_val = getattr(old_value, "ddsm_JobSubmission", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_JobSubmission", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_JobSubmission"):
                opp_val = getattr(value, "ddsm_JobSubmission", None)
                setattr(value, "ddsm_JobSubmission", self)

    @property
    def ddsm_ClientNode56(self):
        return self.__ddsm_ClientNode56

    @ddsm_ClientNode56.setter
    def ddsm_ClientNode56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_ClientNode__ddsm_ClientNode56", None)
        self.__ddsm_ClientNode56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Crontab"):
                opp_val = getattr(old_value, "ddsm_Crontab", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Crontab", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Crontab"):
                opp_val = getattr(value, "ddsm_Crontab", None)
                setattr(value, "ddsm_Crontab", self)

class MasterSlavePlatform:

    pass
class ddsm_HDFSCluster(MasterSlavePlatform):

    pass
class ddsm_YarnCluster(MasterSlavePlatform):

    pass
class ddsm_SparkCluster(MasterSlavePlatform):

    def __init__(self, driverMemory: int, driverCores: int, maxResultSize: int, UIPort: int, sparkExecutorMemory: int):
        self.driverMemory = driverMemory
        self.driverCores = driverCores
        self.maxResultSize = maxResultSize
        self.UIPort = UIPort
        self.sparkExecutorMemory = sparkExecutorMemory
        
    @property
    def UIPort(self) -> int:
        return self.__UIPort

    @UIPort.setter
    def UIPort(self, UIPort: int):
        self.__UIPort = UIPort

    @property
    def sparkExecutorMemory(self) -> int:
        return self.__sparkExecutorMemory

    @sparkExecutorMemory.setter
    def sparkExecutorMemory(self, sparkExecutorMemory: int):
        self.__sparkExecutorMemory = sparkExecutorMemory

    @property
    def maxResultSize(self) -> int:
        return self.__maxResultSize

    @maxResultSize.setter
    def maxResultSize(self, maxResultSize: int):
        self.__maxResultSize = maxResultSize

    @property
    def driverCores(self) -> int:
        return self.__driverCores

    @driverCores.setter
    def driverCores(self, driverCores: int):
        self.__driverCores = driverCores

    @property
    def driverMemory(self) -> int:
        return self.__driverMemory

    @driverMemory.setter
    def driverMemory(self, driverMemory: int):
        self.__driverMemory = driverMemory

class ddsm_StormCluster(MasterSlavePlatform):

    def __init__(self, taskTimeout: int, supervisorFrequency: int, queueSize: int, monitorFrequency: int, retryTimes: int, retryInterval: int, workerStartTimeout: int, heartbeatFrequency: int, cpuCapacity: int, memoryCapacity: int):
        self.taskTimeout = taskTimeout
        self.supervisorFrequency = supervisorFrequency
        self.queueSize = queueSize
        self.monitorFrequency = monitorFrequency
        self.retryTimes = retryTimes
        self.retryInterval = retryInterval
        self.workerStartTimeout = workerStartTimeout
        self.heartbeatFrequency = heartbeatFrequency
        self.cpuCapacity = cpuCapacity
        self.memoryCapacity = memoryCapacity
        
    @property
    def memoryCapacity(self) -> int:
        return self.__memoryCapacity

    @memoryCapacity.setter
    def memoryCapacity(self, memoryCapacity: int):
        self.__memoryCapacity = memoryCapacity

    @property
    def retryTimes(self) -> int:
        return self.__retryTimes

    @retryTimes.setter
    def retryTimes(self, retryTimes: int):
        self.__retryTimes = retryTimes

    @property
    def supervisorFrequency(self) -> int:
        return self.__supervisorFrequency

    @supervisorFrequency.setter
    def supervisorFrequency(self, supervisorFrequency: int):
        self.__supervisorFrequency = supervisorFrequency

    @property
    def taskTimeout(self) -> int:
        return self.__taskTimeout

    @taskTimeout.setter
    def taskTimeout(self, taskTimeout: int):
        self.__taskTimeout = taskTimeout

    @property
    def monitorFrequency(self) -> int:
        return self.__monitorFrequency

    @monitorFrequency.setter
    def monitorFrequency(self, monitorFrequency: int):
        self.__monitorFrequency = monitorFrequency

    @property
    def queueSize(self) -> int:
        return self.__queueSize

    @queueSize.setter
    def queueSize(self, queueSize: int):
        self.__queueSize = queueSize

    @property
    def workerStartTimeout(self) -> int:
        return self.__workerStartTimeout

    @workerStartTimeout.setter
    def workerStartTimeout(self, workerStartTimeout: int):
        self.__workerStartTimeout = workerStartTimeout

    @property
    def cpuCapacity(self) -> int:
        return self.__cpuCapacity

    @cpuCapacity.setter
    def cpuCapacity(self, cpuCapacity: int):
        self.__cpuCapacity = cpuCapacity

    @property
    def heartbeatFrequency(self) -> int:
        return self.__heartbeatFrequency

    @heartbeatFrequency.setter
    def heartbeatFrequency(self, heartbeatFrequency: int):
        self.__heartbeatFrequency = heartbeatFrequency

    @property
    def retryInterval(self) -> int:
        return self.__retryInterval

    @retryInterval.setter
    def retryInterval(self, retryInterval: int):
        self.__retryInterval = retryInterval

class ddsm_DDSM:

    def __init__(self, modelId: str, description: str, ddsm_DDSM: set["ddsm_CloudElement"] = None, ddsm_DDSM46: set["ddsm_Property"] = None, ddsm_DDSM49: set["ddsm_Resource"] = None, ddsm_DDSM52: set["ddsm_Artifact"] = None):
        self.modelId = modelId
        self.description = description
        self.ddsm_DDSM = ddsm_DDSM if ddsm_DDSM is not None else set()
        self.ddsm_DDSM46 = ddsm_DDSM46 if ddsm_DDSM46 is not None else set()
        self.ddsm_DDSM49 = ddsm_DDSM49 if ddsm_DDSM49 is not None else set()
        self.ddsm_DDSM52 = ddsm_DDSM52 if ddsm_DDSM52 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def modelId(self) -> str:
        return self.__modelId

    @modelId.setter
    def modelId(self, modelId: str):
        self.__modelId = modelId

    @property
    def ddsm_DDSM49(self):
        return self.__ddsm_DDSM49

    @ddsm_DDSM49.setter
    def ddsm_DDSM49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_DDSM__ddsm_DDSM49", None)
        self.__ddsm_DDSM49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Resource50"):
                    opp_val = getattr(item, "ddsm_Resource50", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Resource50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Resource50"):
                    opp_val = getattr(item, "ddsm_Resource50", None)
                    
                    setattr(item, "ddsm_Resource50", self)
                    

    @property
    def ddsm_DDSM46(self):
        return self.__ddsm_DDSM46

    @ddsm_DDSM46.setter
    def ddsm_DDSM46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_DDSM__ddsm_DDSM46", None)
        self.__ddsm_DDSM46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Property47"):
                    opp_val = getattr(item, "ddsm_Property47", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Property47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Property47"):
                    opp_val = getattr(item, "ddsm_Property47", None)
                    
                    setattr(item, "ddsm_Property47", self)
                    

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
                if hasattr(item, "ddsm_CloudElement44"):
                    opp_val = getattr(item, "ddsm_CloudElement44", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_CloudElement44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_CloudElement44"):
                    opp_val = getattr(item, "ddsm_CloudElement44", None)
                    
                    setattr(item, "ddsm_CloudElement44", self)
                    

    @property
    def ddsm_DDSM52(self):
        return self.__ddsm_DDSM52

    @ddsm_DDSM52.setter
    def ddsm_DDSM52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_DDSM__ddsm_DDSM52", None)
        self.__ddsm_DDSM52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsm_Artifact53"):
                    opp_val = getattr(item, "ddsm_Artifact53", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsm_Artifact53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsm_Artifact53"):
                    opp_val = getattr(item, "ddsm_Artifact53", None)
                    
                    setattr(item, "ddsm_Artifact53", self)
                    

class ExternalComponent:

    pass
class ddsm_VM(ExternalComponent):

    def __init__(self, is64os: str, imageId: str, maxCores: str, maxRam: str, maxStorage: str, minCores: str, minRam: str, minStorage: str, os: str, privateKey: str, providerSpecificTypeName: str, securityGroup: str, sshKey: str, publicAddress: str, genericSize: str, instances: int, publicPorts: int):
        self.is64os = is64os
        self.imageId = imageId
        self.maxCores = maxCores
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
        self.genericSize = genericSize
        self.instances = instances
        self.publicPorts = publicPorts
        
    @property
    def publicAddress(self) -> str:
        return self.__publicAddress

    @publicAddress.setter
    def publicAddress(self, publicAddress: str):
        self.__publicAddress = publicAddress

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
    def is64os(self) -> str:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: str):
        self.__is64os = is64os

    @property
    def minRam(self) -> str:
        return self.__minRam

    @minRam.setter
    def minRam(self, minRam: str):
        self.__minRam = minRam

    @property
    def instances(self) -> int:
        return self.__instances

    @instances.setter
    def instances(self, instances: int):
        self.__instances = instances

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

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
    def publicPorts(self) -> int:
        return self.__publicPorts

    @publicPorts.setter
    def publicPorts(self, publicPorts: int):
        self.__publicPorts = publicPorts

    @property
    def minCores(self) -> str:
        return self.__minCores

    @minCores.setter
    def minCores(self, minCores: str):
        self.__minCores = minCores

    @property
    def os(self) -> str:
        return self.__os

    @os.setter
    def os(self, os: str):
        self.__os = os

    @property
    def minStorage(self) -> str:
        return self.__minStorage

    @minStorage.setter
    def minStorage(self, minStorage: str):
        self.__minStorage = minStorage

    @property
    def providerSpecificTypeName(self) -> str:
        return self.__providerSpecificTypeName

    @providerSpecificTypeName.setter
    def providerSpecificTypeName(self, providerSpecificTypeName: str):
        self.__providerSpecificTypeName = providerSpecificTypeName

    @property
    def maxCores(self) -> str:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: str):
        self.__maxCores = maxCores

    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def maxRam(self) -> str:
        return self.__maxRam

    @maxRam.setter
    def maxRam(self, maxRam: str):
        self.__maxRam = maxRam

class ExecutionPlatform:

    pass
class Port:

    pass
class ddsm_RequiredExecutionPlatform(ExecutionPlatform):

    def __init__(self, isMandatory: bool, ddsm_RequiredExecutionPlatform: "ddsm_InternalComponent" = None, ddsm_RequiredExecutionPlatform38: "ddsm_ExecutionBinding" = None, ddsm_RequiredExecutionPlatform65: "ddsm_MasterSlavePlatform" = None, ddsm_RequiredExecutionPlatform60: "ddsm_PeerToPeerPlatform" = None, ddsm_RequiredExecutionPlatform62: "ddsm_MasterSlavePlatform" = None):
        self.isMandatory = isMandatory
        self.ddsm_RequiredExecutionPlatform = ddsm_RequiredExecutionPlatform
        self.ddsm_RequiredExecutionPlatform38 = ddsm_RequiredExecutionPlatform38
        self.ddsm_RequiredExecutionPlatform65 = ddsm_RequiredExecutionPlatform65
        self.ddsm_RequiredExecutionPlatform60 = ddsm_RequiredExecutionPlatform60
        self.ddsm_RequiredExecutionPlatform62 = ddsm_RequiredExecutionPlatform62
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def ddsm_RequiredExecutionPlatform65(self):
        return self.__ddsm_RequiredExecutionPlatform65

    @ddsm_RequiredExecutionPlatform65.setter
    def ddsm_RequiredExecutionPlatform65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredExecutionPlatform__ddsm_RequiredExecutionPlatform65", None)
        self.__ddsm_RequiredExecutionPlatform65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_MasterSlavePlatform64"):
                opp_val = getattr(old_value, "ddsm_MasterSlavePlatform64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_MasterSlavePlatform64"):
                opp_val = getattr(value, "ddsm_MasterSlavePlatform64", None)
                if opp_val is None:
                    setattr(value, "ddsm_MasterSlavePlatform64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_RequiredExecutionPlatform38(self):
        return self.__ddsm_RequiredExecutionPlatform38

    @ddsm_RequiredExecutionPlatform38.setter
    def ddsm_RequiredExecutionPlatform38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredExecutionPlatform__ddsm_RequiredExecutionPlatform38", None)
        self.__ddsm_RequiredExecutionPlatform38 = value
        
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
            if hasattr(old_value, "ddsm_InternalComponent25"):
                opp_val = getattr(old_value, "ddsm_InternalComponent25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_InternalComponent25"):
                opp_val = getattr(value, "ddsm_InternalComponent25", None)
                if opp_val is None:
                    setattr(value, "ddsm_InternalComponent25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_RequiredExecutionPlatform62(self):
        return self.__ddsm_RequiredExecutionPlatform62

    @ddsm_RequiredExecutionPlatform62.setter
    def ddsm_RequiredExecutionPlatform62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredExecutionPlatform__ddsm_RequiredExecutionPlatform62", None)
        self.__ddsm_RequiredExecutionPlatform62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_MasterSlavePlatform"):
                opp_val = getattr(old_value, "ddsm_MasterSlavePlatform", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_MasterSlavePlatform", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_MasterSlavePlatform"):
                opp_val = getattr(value, "ddsm_MasterSlavePlatform", None)
                setattr(value, "ddsm_MasterSlavePlatform", self)

    @property
    def ddsm_RequiredExecutionPlatform60(self):
        return self.__ddsm_RequiredExecutionPlatform60

    @ddsm_RequiredExecutionPlatform60.setter
    def ddsm_RequiredExecutionPlatform60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredExecutionPlatform__ddsm_RequiredExecutionPlatform60", None)
        self.__ddsm_RequiredExecutionPlatform60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_PeerToPeerPlatform"):
                opp_val = getattr(old_value, "ddsm_PeerToPeerPlatform", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_PeerToPeerPlatform"):
                opp_val = getattr(value, "ddsm_PeerToPeerPlatform", None)
                if opp_val is None:
                    setattr(value, "ddsm_PeerToPeerPlatform", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsm_RequiredPort(Port):

    def __init__(self, isMandatory: bool, ddsm_RequiredPort: "ddsm_InternalComponent" = None, ddsm_RequiredPort36: "ddsm_Relationship" = None):
        self.isMandatory = isMandatory
        self.ddsm_RequiredPort = ddsm_RequiredPort
        self.ddsm_RequiredPort36 = ddsm_RequiredPort36
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def ddsm_RequiredPort36(self):
        return self.__ddsm_RequiredPort36

    @ddsm_RequiredPort36.setter
    def ddsm_RequiredPort36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_RequiredPort__ddsm_RequiredPort36", None)
        self.__ddsm_RequiredPort36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Relationship35"):
                opp_val = getattr(old_value, "ddsm_Relationship35", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Relationship35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Relationship35"):
                opp_val = getattr(value, "ddsm_Relationship35", None)
                setattr(value, "ddsm_Relationship35", self)

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

    def __init__(self, location: str, login: str, password: str, region: str, serviceType: str, endPoint: str, ddsm_ExternalComponent: "ddsm_Provider" = None):
        self.location = location
        self.login = login
        self.password = password
        self.region = region
        self.serviceType = serviceType
        self.endPoint = endPoint
        self.ddsm_ExternalComponent = ddsm_ExternalComponent
        
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
    def endPoint(self) -> str:
        return self.__endPoint

    @endPoint.setter
    def endPoint(self, endPoint: str):
        self.__endPoint = endPoint

    @property
    def serviceType(self) -> str:
        return self.__serviceType

    @serviceType.setter
    def serviceType(self, serviceType: str):
        self.__serviceType = serviceType

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def region(self) -> str:
        return self.__region

    @region.setter
    def region(self, region: str):
        self.__region = region

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
class ddsm_ExecutionBinding(CloudElement):

    pass
class ddsm_JobSubmission(CloudElement):

    def __init__(self, artifactUrl: str, mainClass: str, applicationArguments: str, ddsm_JobSubmission: "ddsm_ClientNode" = None):
        self.artifactUrl = artifactUrl
        self.mainClass = mainClass
        self.applicationArguments = applicationArguments
        self.ddsm_JobSubmission = ddsm_JobSubmission
        
    @property
    def applicationArguments(self) -> str:
        return self.__applicationArguments

    @applicationArguments.setter
    def applicationArguments(self, applicationArguments: str):
        self.__applicationArguments = applicationArguments

    @property
    def artifactUrl(self) -> str:
        return self.__artifactUrl

    @artifactUrl.setter
    def artifactUrl(self, artifactUrl: str):
        self.__artifactUrl = artifactUrl

    @property
    def mainClass(self) -> str:
        return self.__mainClass

    @mainClass.setter
    def mainClass(self, mainClass: str):
        self.__mainClass = mainClass

    @property
    def ddsm_JobSubmission(self):
        return self.__ddsm_JobSubmission

    @ddsm_JobSubmission.setter
    def ddsm_JobSubmission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_JobSubmission__ddsm_JobSubmission", None)
        self.__ddsm_JobSubmission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_ClientNode"):
                opp_val = getattr(old_value, "ddsm_ClientNode", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_ClientNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_ClientNode"):
                opp_val = getattr(value, "ddsm_ClientNode", None)
                setattr(value, "ddsm_ClientNode", self)

class ddsm_Relationship(CloudElement):

    pass
class ddsm_ExecutionPlatform(CloudElement):

    pass
class ddsm_Provider(CloudElement):

    def __init__(self, type: str, credentialsPath: str, ddsm_Provider: "ddsm_ExternalComponent" = None):
        self.type = type
        self.credentialsPath = credentialsPath
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
class ddsm_Port(CloudElement):

    def __init__(self, isLocal: bool, portNumber: str):
        self.isLocal = isLocal
        self.portNumber = portNumber
        
    @property
    def portNumber(self) -> str:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: str):
        self.__portNumber = portNumber

    @property
    def isLocal(self) -> bool:
        return self.__isLocal

    @isLocal.setter
    def isLocal(self, isLocal: bool):
        self.__isLocal = isLocal

class ddsm_Artifact:

    def __init__(self, resources: str, language: str, artifactPath: str, arguments: str, ddsm_Artifact16: "ddsm_Resource" = None, ddsm_Artifact19: "ddsm_Resource" = None, ddsm_Artifact: "ddsm_Resource" = None, ddsm_Artifact7: "ddsm_Resource" = None, ddsm_Artifact10: "ddsm_Resource" = None, ddsm_Artifact13: "ddsm_Resource" = None, ddsm_Artifact53: "ddsm_DDSM" = None):
        self.resources = resources
        self.language = language
        self.artifactPath = artifactPath
        self.arguments = arguments
        self.ddsm_Artifact16 = ddsm_Artifact16
        self.ddsm_Artifact19 = ddsm_Artifact19
        self.ddsm_Artifact = ddsm_Artifact
        self.ddsm_Artifact7 = ddsm_Artifact7
        self.ddsm_Artifact10 = ddsm_Artifact10
        self.ddsm_Artifact13 = ddsm_Artifact13
        self.ddsm_Artifact53 = ddsm_Artifact53
        
    @property
    def artifactPath(self) -> str:
        return self.__artifactPath

    @artifactPath.setter
    def artifactPath(self, artifactPath: str):
        self.__artifactPath = artifactPath

    @property
    def resources(self) -> str:
        return self.__resources

    @resources.setter
    def resources(self, resources: str):
        self.__resources = resources

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def arguments(self) -> str:
        return self.__arguments

    @arguments.setter
    def arguments(self, arguments: str):
        self.__arguments = arguments

    @property
    def ddsm_Artifact(self):
        return self.__ddsm_Artifact

    @ddsm_Artifact.setter
    def ddsm_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact", None)
        self.__ddsm_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Resource4"):
                opp_val = getattr(old_value, "ddsm_Resource4", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Resource4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Resource4"):
                opp_val = getattr(value, "ddsm_Resource4", None)
                setattr(value, "ddsm_Resource4", self)

    @property
    def ddsm_Artifact10(self):
        return self.__ddsm_Artifact10

    @ddsm_Artifact10.setter
    def ddsm_Artifact10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact10", None)
        self.__ddsm_Artifact10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Resource9"):
                opp_val = getattr(old_value, "ddsm_Resource9", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Resource9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Resource9"):
                opp_val = getattr(value, "ddsm_Resource9", None)
                setattr(value, "ddsm_Resource9", self)

    @property
    def ddsm_Artifact53(self):
        return self.__ddsm_Artifact53

    @ddsm_Artifact53.setter
    def ddsm_Artifact53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact53", None)
        self.__ddsm_Artifact53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_DDSM52"):
                opp_val = getattr(old_value, "ddsm_DDSM52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_DDSM52"):
                opp_val = getattr(value, "ddsm_DDSM52", None)
                if opp_val is None:
                    setattr(value, "ddsm_DDSM52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_Artifact16(self):
        return self.__ddsm_Artifact16

    @ddsm_Artifact16.setter
    def ddsm_Artifact16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact16", None)
        self.__ddsm_Artifact16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Resource15"):
                opp_val = getattr(old_value, "ddsm_Resource15", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Resource15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Resource15"):
                opp_val = getattr(value, "ddsm_Resource15", None)
                setattr(value, "ddsm_Resource15", self)

    @property
    def ddsm_Artifact13(self):
        return self.__ddsm_Artifact13

    @ddsm_Artifact13.setter
    def ddsm_Artifact13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact13", None)
        self.__ddsm_Artifact13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Resource12"):
                opp_val = getattr(old_value, "ddsm_Resource12", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Resource12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Resource12"):
                opp_val = getattr(value, "ddsm_Resource12", None)
                setattr(value, "ddsm_Resource12", self)

    @property
    def ddsm_Artifact7(self):
        return self.__ddsm_Artifact7

    @ddsm_Artifact7.setter
    def ddsm_Artifact7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact7", None)
        self.__ddsm_Artifact7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Resource6"):
                opp_val = getattr(old_value, "ddsm_Resource6", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Resource6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Resource6"):
                opp_val = getattr(value, "ddsm_Resource6", None)
                setattr(value, "ddsm_Resource6", self)

    @property
    def ddsm_Artifact19(self):
        return self.__ddsm_Artifact19

    @ddsm_Artifact19.setter
    def ddsm_Artifact19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Artifact__ddsm_Artifact19", None)
        self.__ddsm_Artifact19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Resource18"):
                opp_val = getattr(old_value, "ddsm_Resource18", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Resource18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Resource18"):
                opp_val = getattr(value, "ddsm_Resource18", None)
                setattr(value, "ddsm_Resource18", self)

class ddsm_Property:

    def __init__(self, propertyId: str, value: str, ddsm_Property: "ddsm_CloudElement" = None, ddsm_Property47: "ddsm_DDSM" = None):
        self.propertyId = propertyId
        self.value = value
        self.ddsm_Property = ddsm_Property
        self.ddsm_Property47 = ddsm_Property47
        
    @property
    def propertyId(self) -> str:
        return self.__propertyId

    @propertyId.setter
    def propertyId(self, propertyId: str):
        self.__propertyId = propertyId

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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

    @property
    def ddsm_Property47(self):
        return self.__ddsm_Property47

    @ddsm_Property47.setter
    def ddsm_Property47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Property__ddsm_Property47", None)
        self.__ddsm_Property47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_DDSM46"):
                opp_val = getattr(old_value, "ddsm_DDSM46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_DDSM46"):
                opp_val = getattr(value, "ddsm_DDSM46", None)
                if opp_val is None:
                    setattr(value, "ddsm_DDSM46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsm_CloudElement(ABC):

    def __init__(self, elementId: str, description: str, ddsm_CloudElement: set["ddsm_Resource"] = None, ddsm_CloudElement2: set["ddsm_Property"] = None, ddsm_CloudElement44: "ddsm_DDSM" = None):
        self.elementId = elementId
        self.description = description
        self.ddsm_CloudElement = ddsm_CloudElement if ddsm_CloudElement is not None else set()
        self.ddsm_CloudElement2 = ddsm_CloudElement2 if ddsm_CloudElement2 is not None else set()
        self.ddsm_CloudElement44 = ddsm_CloudElement44
        
    @property
    def elementId(self) -> str:
        return self.__elementId

    @elementId.setter
    def elementId(self, elementId: str):
        self.__elementId = elementId

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ddsm_CloudElement44(self):
        return self.__ddsm_CloudElement44

    @ddsm_CloudElement44.setter
    def ddsm_CloudElement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_CloudElement__ddsm_CloudElement44", None)
        self.__ddsm_CloudElement44 = value
        
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
                    

class ddsm_Resource:

    def __init__(self, resourceId: str, ddsm_Resource: "ddsm_CloudElement" = None, ddsm_Resource15: "ddsm_Artifact" = None, ddsm_Resource4: "ddsm_Artifact" = None, ddsm_Resource6: "ddsm_Artifact" = None, ddsm_Resource9: "ddsm_Artifact" = None, ddsm_Resource12: "ddsm_Artifact" = None, ddsm_Resource18: "ddsm_Artifact" = None, ddsm_Resource50: "ddsm_DDSM" = None):
        self.resourceId = resourceId
        self.ddsm_Resource = ddsm_Resource
        self.ddsm_Resource15 = ddsm_Resource15
        self.ddsm_Resource4 = ddsm_Resource4
        self.ddsm_Resource6 = ddsm_Resource6
        self.ddsm_Resource9 = ddsm_Resource9
        self.ddsm_Resource12 = ddsm_Resource12
        self.ddsm_Resource18 = ddsm_Resource18
        self.ddsm_Resource50 = ddsm_Resource50
        
    @property
    def resourceId(self) -> str:
        return self.__resourceId

    @resourceId.setter
    def resourceId(self, resourceId: str):
        self.__resourceId = resourceId

    @property
    def ddsm_Resource50(self):
        return self.__ddsm_Resource50

    @ddsm_Resource50.setter
    def ddsm_Resource50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource50", None)
        self.__ddsm_Resource50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_DDSM49"):
                opp_val = getattr(old_value, "ddsm_DDSM49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_DDSM49"):
                opp_val = getattr(value, "ddsm_DDSM49", None)
                if opp_val is None:
                    setattr(value, "ddsm_DDSM49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsm_Resource9(self):
        return self.__ddsm_Resource9

    @ddsm_Resource9.setter
    def ddsm_Resource9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource9", None)
        self.__ddsm_Resource9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Artifact10"):
                opp_val = getattr(old_value, "ddsm_Artifact10", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Artifact10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Artifact10"):
                opp_val = getattr(value, "ddsm_Artifact10", None)
                setattr(value, "ddsm_Artifact10", self)

    @property
    def ddsm_Resource15(self):
        return self.__ddsm_Resource15

    @ddsm_Resource15.setter
    def ddsm_Resource15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource15", None)
        self.__ddsm_Resource15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Artifact16"):
                opp_val = getattr(old_value, "ddsm_Artifact16", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Artifact16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Artifact16"):
                opp_val = getattr(value, "ddsm_Artifact16", None)
                setattr(value, "ddsm_Artifact16", self)

    @property
    def ddsm_Resource4(self):
        return self.__ddsm_Resource4

    @ddsm_Resource4.setter
    def ddsm_Resource4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource4", None)
        self.__ddsm_Resource4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Artifact"):
                opp_val = getattr(old_value, "ddsm_Artifact", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Artifact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Artifact"):
                opp_val = getattr(value, "ddsm_Artifact", None)
                setattr(value, "ddsm_Artifact", self)

    @property
    def ddsm_Resource12(self):
        return self.__ddsm_Resource12

    @ddsm_Resource12.setter
    def ddsm_Resource12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource12", None)
        self.__ddsm_Resource12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Artifact13"):
                opp_val = getattr(old_value, "ddsm_Artifact13", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Artifact13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Artifact13"):
                opp_val = getattr(value, "ddsm_Artifact13", None)
                setattr(value, "ddsm_Artifact13", self)

    @property
    def ddsm_Resource6(self):
        return self.__ddsm_Resource6

    @ddsm_Resource6.setter
    def ddsm_Resource6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource6", None)
        self.__ddsm_Resource6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Artifact7"):
                opp_val = getattr(old_value, "ddsm_Artifact7", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Artifact7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Artifact7"):
                opp_val = getattr(value, "ddsm_Artifact7", None)
                setattr(value, "ddsm_Artifact7", self)

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

    @property
    def ddsm_Resource18(self):
        return self.__ddsm_Resource18

    @ddsm_Resource18.setter
    def ddsm_Resource18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsm_Resource__ddsm_Resource18", None)
        self.__ddsm_Resource18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsm_Artifact19"):
                opp_val = getattr(old_value, "ddsm_Artifact19", None)
                if opp_val == self:
                    setattr(old_value, "ddsm_Artifact19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsm_Artifact19"):
                opp_val = getattr(value, "ddsm_Artifact19", None)
                setattr(value, "ddsm_Artifact19", self)
