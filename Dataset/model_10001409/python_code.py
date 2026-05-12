from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Byte(Enum):
    pass
class pcb_PCB_Status(Enum):
    pass
class cpu_InstructionSet(Enum):
    pass
class driver_CPUSchedulingPolicy(Enum):
    pass

############################################
# Definition of Classes
############################################










class java_lang_Runnable_Interface:

    pass


class driver_Scheduler:

    def __init__(self, mmu: memory_MMU, disk: memory_Memory, taskManager: pcb_TaskManager, schedulingMethod: driver_CPUSchedulingPolicy, driver13: "driver_Driver" = None):
        self.mmu = mmu
        self.disk = disk
        self.taskManager = taskManager
        self.schedulingMethod = schedulingMethod
        self.driver13 = driver13
        
        pass
    @property
    def mmu(self):
        return self.__mmu
    @mmu.setter
    def mmu(self, mmu: memory_MMU):
        self.__mmu = mmu

    @property
    def taskManager(self):
        return self.__taskManager
    @taskManager.setter
    def taskManager(self, taskManager: pcb_TaskManager):
        self.__taskManager = taskManager

    @property
    def schedulingMethod(self):
        return self.__schedulingMethod
    @schedulingMethod.setter
    def schedulingMethod(self, schedulingMethod: driver_CPUSchedulingPolicy):
        self.__schedulingMethod = schedulingMethod

    @property
    def disk(self):
        return self.__disk
    @disk.setter
    def disk(self, disk: memory_Memory):
        self.__disk = disk

    @property
    def driver13(self):
        return self.__driver13
    @driver13.setter
    def driver13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Scheduler__driver13", None)
        self.__driver13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduler12"):
                opp_val = getattr(old_value, "scheduler12", None)
                if opp_val == self:
                    setattr(old_value, "scheduler12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduler12"):
                opp_val = getattr(value, "scheduler12", None)
                setattr(value, "scheduler12", self)



class driver_Dispatcher:

    def __init__(self, taskManager: pcb_TaskManager, cpus: cpu_CPU, mmu: memory_MMU, driver17: "driver_Driver" = None):
        self.taskManager = taskManager
        self.cpus = cpus
        self.mmu = mmu
        self.driver17 = driver17
        
        pass
    @property
    def mmu(self):
        return self.__mmu
    @mmu.setter
    def mmu(self, mmu: memory_MMU):
        self.__mmu = mmu

    @property
    def cpus(self):
        return self.__cpus
    @cpus.setter
    def cpus(self, cpus: cpu_CPU):
        self.__cpus = cpus

    @property
    def taskManager(self):
        return self.__taskManager
    @taskManager.setter
    def taskManager(self, taskManager: pcb_TaskManager):
        self.__taskManager = taskManager

    @property
    def driver17(self):
        return self.__driver17
    @driver17.setter
    def driver17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Dispatcher__driver17", None)
        self.__driver17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dispatcher16"):
                opp_val = getattr(old_value, "dispatcher16", None)
                if opp_val == self:
                    setattr(old_value, "dispatcher16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dispatcher16"):
                opp_val = getattr(value, "dispatcher16", None)
                setattr(value, "dispatcher16", self)



class driver_Loader:

    def __init__(self, pid: int, instructionsLength: int, priority: int, inputBuffSize: int, outputBuffSize: int, tempBuffSize: int, startInstructionAddress: int, startInputBufferAddress: int, startOutputBufferAddress: int, startTempBufferAddress: int, endInstructionAddress: int, endInputBufferAddres: int, endOutputBufferAddress: int, endTempBufferAddress: int, currAddress: int, disk: memory_Memory, programFile: str, processList: pcb_TaskManager, driver15: set["driver_Driver"] = None):
        self.pid = pid
        self.instructionsLength = instructionsLength
        self.priority = priority
        self.inputBuffSize = inputBuffSize
        self.outputBuffSize = outputBuffSize
        self.tempBuffSize = tempBuffSize
        self.startInstructionAddress = startInstructionAddress
        self.startInputBufferAddress = startInputBufferAddress
        self.startOutputBufferAddress = startOutputBufferAddress
        self.startTempBufferAddress = startTempBufferAddress
        self.endInstructionAddress = endInstructionAddress
        self.endInputBufferAddres = endInputBufferAddres
        self.endOutputBufferAddress = endOutputBufferAddress
        self.endTempBufferAddress = endTempBufferAddress
        self.currAddress = currAddress
        self.disk = disk
        self.programFile = programFile
        self.processList = processList
        self.driver15 = driver15 if driver15 is not None else set()
        
        pass
    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def startInstructionAddress(self):
        return self.__startInstructionAddress
    @startInstructionAddress.setter
    def startInstructionAddress(self, startInstructionAddress: int):
        self.__startInstructionAddress = startInstructionAddress

    @property
    def startOutputBufferAddress(self):
        return self.__startOutputBufferAddress
    @startOutputBufferAddress.setter
    def startOutputBufferAddress(self, startOutputBufferAddress: int):
        self.__startOutputBufferAddress = startOutputBufferAddress

    @property
    def processList(self):
        return self.__processList
    @processList.setter
    def processList(self, processList: pcb_TaskManager):
        self.__processList = processList

    @property
    def outputBuffSize(self):
        return self.__outputBuffSize
    @outputBuffSize.setter
    def outputBuffSize(self, outputBuffSize: int):
        self.__outputBuffSize = outputBuffSize

    @property
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self, pid: int):
        self.__pid = pid

    @property
    def startInputBufferAddress(self):
        return self.__startInputBufferAddress
    @startInputBufferAddress.setter
    def startInputBufferAddress(self, startInputBufferAddress: int):
        self.__startInputBufferAddress = startInputBufferAddress

    @property
    def inputBuffSize(self):
        return self.__inputBuffSize
    @inputBuffSize.setter
    def inputBuffSize(self, inputBuffSize: int):
        self.__inputBuffSize = inputBuffSize

    @property
    def endTempBufferAddress(self):
        return self.__endTempBufferAddress
    @endTempBufferAddress.setter
    def endTempBufferAddress(self, endTempBufferAddress: int):
        self.__endTempBufferAddress = endTempBufferAddress

    @property
    def endInstructionAddress(self):
        return self.__endInstructionAddress
    @endInstructionAddress.setter
    def endInstructionAddress(self, endInstructionAddress: int):
        self.__endInstructionAddress = endInstructionAddress

    @property
    def startTempBufferAddress(self):
        return self.__startTempBufferAddress
    @startTempBufferAddress.setter
    def startTempBufferAddress(self, startTempBufferAddress: int):
        self.__startTempBufferAddress = startTempBufferAddress

    @property
    def currAddress(self):
        return self.__currAddress
    @currAddress.setter
    def currAddress(self, currAddress: int):
        self.__currAddress = currAddress

    @property
    def endOutputBufferAddress(self):
        return self.__endOutputBufferAddress
    @endOutputBufferAddress.setter
    def endOutputBufferAddress(self, endOutputBufferAddress: int):
        self.__endOutputBufferAddress = endOutputBufferAddress

    @property
    def tempBuffSize(self):
        return self.__tempBuffSize
    @tempBuffSize.setter
    def tempBuffSize(self, tempBuffSize: int):
        self.__tempBuffSize = tempBuffSize

    @property
    def programFile(self):
        return self.__programFile
    @programFile.setter
    def programFile(self, programFile: str):
        self.__programFile = programFile

    @property
    def disk(self):
        return self.__disk
    @disk.setter
    def disk(self, disk: memory_Memory):
        self.__disk = disk

    @property
    def instructionsLength(self):
        return self.__instructionsLength
    @instructionsLength.setter
    def instructionsLength(self, instructionsLength: int):
        self.__instructionsLength = instructionsLength

    @property
    def endInputBufferAddres(self):
        return self.__endInputBufferAddres
    @endInputBufferAddres.setter
    def endInputBufferAddres(self, endInputBufferAddres: int):
        self.__endInputBufferAddres = endInputBufferAddres

    @property
    def driver15(self):
        return self.__driver15
    @driver15.setter
    def driver15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Loader__driver15", None)
        self.__driver15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "loader14"):
                    opp_val = getattr(item, "loader14", None)
                    
                    if opp_val == self:
                        setattr(item, "loader14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "loader14"):
                    opp_val = getattr(item, "loader14", None)
                    
                    setattr(item, "loader14", self)
                    



class driver_Driver:

    def __init__(self, loader: driver_Loader, taskManager: pcb_TaskManager, registerSize: int, cacheSize: int, ramSize: int, scheduler: driver_Scheduler, dispatcher: driver_Dispatcher, cpus: cpu_CPU, threads: str, disk: memory_Memory, idleTimes: int, executeTimes: int, taskManager7: "pcb_TaskManager" = None, cpu10: set["cpu_CPU"] = None, scheduler12: "driver_Scheduler" = None, loader14: "driver_Loader" = None, dispatcher16: "driver_Dispatcher" = None):
        self.loader = loader
        self.taskManager = taskManager
        self.registerSize = registerSize
        self.cacheSize = cacheSize
        self.ramSize = ramSize
        self.scheduler = scheduler
        self.dispatcher = dispatcher
        self.cpus = cpus
        self.threads = threads
        self.disk = disk
        self.idleTimes = idleTimes
        self.executeTimes = executeTimes
        self.taskManager7 = taskManager7
        self.cpu10 = cpu10 if cpu10 is not None else set()
        self.scheduler12 = scheduler12
        self.loader14 = loader14
        self.dispatcher16 = dispatcher16
        
        pass
    @property
    def disk(self):
        return self.__disk
    @disk.setter
    def disk(self, disk: memory_Memory):
        self.__disk = disk

    @property
    def threads(self):
        return self.__threads
    @threads.setter
    def threads(self, threads: str):
        self.__threads = threads

    @property
    def cpus(self):
        return self.__cpus
    @cpus.setter
    def cpus(self, cpus: cpu_CPU):
        self.__cpus = cpus

    @property
    def idleTimes(self):
        return self.__idleTimes
    @idleTimes.setter
    def idleTimes(self, idleTimes: int):
        self.__idleTimes = idleTimes

    @property
    def ramSize(self):
        return self.__ramSize
    @ramSize.setter
    def ramSize(self, ramSize: int):
        self.__ramSize = ramSize

    @property
    def cacheSize(self):
        return self.__cacheSize
    @cacheSize.setter
    def cacheSize(self, cacheSize: int):
        self.__cacheSize = cacheSize

    @property
    def loader(self):
        return self.__loader
    @loader.setter
    def loader(self, loader: driver_Loader):
        self.__loader = loader

    @property
    def registerSize(self):
        return self.__registerSize
    @registerSize.setter
    def registerSize(self, registerSize: int):
        self.__registerSize = registerSize

    @property
    def taskManager(self):
        return self.__taskManager
    @taskManager.setter
    def taskManager(self, taskManager: pcb_TaskManager):
        self.__taskManager = taskManager

    @property
    def executeTimes(self):
        return self.__executeTimes
    @executeTimes.setter
    def executeTimes(self, executeTimes: int):
        self.__executeTimes = executeTimes

    @property
    def dispatcher(self):
        return self.__dispatcher
    @dispatcher.setter
    def dispatcher(self, dispatcher: driver_Dispatcher):
        self.__dispatcher = dispatcher

    @property
    def scheduler(self):
        return self.__scheduler
    @scheduler.setter
    def scheduler(self, scheduler: driver_Scheduler):
        self.__scheduler = scheduler

    @property
    def loader14(self):
        return self.__loader14
    @loader14.setter
    def loader14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Driver__loader14", None)
        self.__loader14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver15"):
                opp_val = getattr(old_value, "driver15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver15"):
                opp_val = getattr(value, "driver15", None)
                if opp_val is None:
                    setattr(value, "driver15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def taskManager7(self):
        return self.__taskManager7
    @taskManager7.setter
    def taskManager7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Driver__taskManager7", None)
        self.__taskManager7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver6"):
                opp_val = getattr(old_value, "driver6", None)
                if opp_val == self:
                    setattr(old_value, "driver6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver6"):
                opp_val = getattr(value, "driver6", None)
                setattr(value, "driver6", self)

    @property
    def dispatcher16(self):
        return self.__dispatcher16
    @dispatcher16.setter
    def dispatcher16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Driver__dispatcher16", None)
        self.__dispatcher16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver17"):
                opp_val = getattr(old_value, "driver17", None)
                if opp_val == self:
                    setattr(old_value, "driver17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver17"):
                opp_val = getattr(value, "driver17", None)
                setattr(value, "driver17", self)

    @property
    def cpu10(self):
        return self.__cpu10
    @cpu10.setter
    def cpu10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Driver__cpu10", None)
        self.__cpu10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver11"):
                    opp_val = getattr(item, "driver11", None)
                    
                    if opp_val == self:
                        setattr(item, "driver11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver11"):
                    opp_val = getattr(item, "driver11", None)
                    
                    setattr(item, "driver11", self)
                    

    @property
    def scheduler12(self):
        return self.__scheduler12
    @scheduler12.setter
    def scheduler12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Driver__scheduler12", None)
        self.__scheduler12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver13"):
                opp_val = getattr(old_value, "driver13", None)
                if opp_val == self:
                    setattr(old_value, "driver13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver13"):
                opp_val = getattr(value, "driver13", None)
                setattr(value, "driver13", self)



class cpu_IOExecutableInstruction:

    def __init__(self, reg1: int, reg2: int, address: int):
        self.reg1 = reg1
        self.reg2 = reg2
        self.address = address
        
        pass
    @property
    def reg1(self):
        return self.__reg1
    @reg1.setter
    def reg1(self, reg1: int):
        self.__reg1 = reg1

    @property
    def reg2(self):
        return self.__reg2
    @reg2.setter
    def reg2(self, reg2: int):
        self.__reg2 = reg2

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: int):
        self.__address = address



class cpu_UnconditionalJumpExecutableInstruction:

    def __init__(self, cpu: cpu_CPU, address: int):
        self.cpu = cpu
        self.address = address
        
        pass
    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu: cpu_CPU):
        self.__cpu = cpu

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: int):
        self.__address = address



class cpu_ConditionalExecutableInstruction:

    def __init__(self, cpu: cpu_CPU, bReg: int, dReg: int, data: int, cache: memory_Memory):
        self.cpu = cpu
        self.bReg = bReg
        self.dReg = dReg
        self.data = data
        self.cache = cache
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: int):
        self.__data = data

    @property
    def dReg(self):
        return self.__dReg
    @dReg.setter
    def dReg(self, dReg: int):
        self.__dReg = dReg

    @property
    def cache(self):
        return self.__cache
    @cache.setter
    def cache(self, cache: memory_Memory):
        self.__cache = cache

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu: cpu_CPU):
        self.__cpu = cpu

    @property
    def bReg(self):
        return self.__bReg
    @bReg.setter
    def bReg(self, bReg: int):
        self.__bReg = bReg



class cpu_ArithmeticExecutableInstruction:

    def __init__(self, s1: int, s2: int, d: int):
        self.s1 = s1
        self.s2 = s2
        self.d = d
        
        pass
    @property
    def s1(self):
        return self.__s1
    @s1.setter
    def s1(self, s1: int):
        self.__s1 = s1

    @property
    def s2(self):
        return self.__s2
    @s2.setter
    def s2(self, s2: int):
        self.__s2 = s2

    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d



class cpu_ExecutableInstruction(ABC):

    def __init__(self, type: cpu_InstructionSet, registers: memory_Memory):
        self.type = type
        self.registers = registers
        
        pass
    @property
    def registers(self):
        return self.__registers
    @registers.setter
    def registers(self, registers: memory_Memory):
        self.__registers = registers

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: cpu_InstructionSet):
        self.__type = type



class cpu_DMAChannel:

    def __init__(self, mmu: str, cpu9: "cpu_CPU" = None):
        self.mmu = mmu
        self.cpu9 = cpu9
        
        pass
    @property
    def mmu(self):
        return self.__mmu
    @mmu.setter
    def mmu(self, mmu: str):
        self.__mmu = mmu

    @property
    def cpu9(self):
        return self.__cpu9
    @cpu9.setter
    def cpu9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpu_DMAChannel__cpu9", None)
        self.__cpu9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmaChannel8"):
                opp_val = getattr(old_value, "dmaChannel8", None)
                if opp_val == self:
                    setattr(old_value, "dmaChannel8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmaChannel8"):
                opp_val = getattr(value, "dmaChannel8", None)
                setattr(value, "dmaChannel8", self)



class cpu_CPU:

    def __init__(self, cpuids: int, cpuid: int, register: memory_Memory, cache: memory_Memory, dmaChannel: str, pcb: pcb_PCB, previousInstruction: cpu_ExecutableInstruction, log: str, shutdown: bool, idleTime: int, executeTime: int, numProcesses: int, dmaChannel8: "cpu_DMAChannel" = None, driver11: "driver_Driver" = None):
        self.cpuids = cpuids
        self.cpuid = cpuid
        self.register = register
        self.cache = cache
        self.dmaChannel = dmaChannel
        self.pcb = pcb
        self.previousInstruction = previousInstruction
        self.log = log
        self.shutdown = shutdown
        self.idleTime = idleTime
        self.executeTime = executeTime
        self.numProcesses = numProcesses
        self.dmaChannel8 = dmaChannel8
        self.driver11 = driver11
        
        pass
    @property
    def executeTime(self):
        return self.__executeTime
    @executeTime.setter
    def executeTime(self, executeTime: int):
        self.__executeTime = executeTime

    @property
    def register(self):
        return self.__register
    @register.setter
    def register(self, register: memory_Memory):
        self.__register = register

    @property
    def pcb(self):
        return self.__pcb
    @pcb.setter
    def pcb(self, pcb: pcb_PCB):
        self.__pcb = pcb

    @property
    def cache(self):
        return self.__cache
    @cache.setter
    def cache(self, cache: memory_Memory):
        self.__cache = cache

    @property
    def previousInstruction(self):
        return self.__previousInstruction
    @previousInstruction.setter
    def previousInstruction(self, previousInstruction: cpu_ExecutableInstruction):
        self.__previousInstruction = previousInstruction

    @property
    def shutdown(self):
        return self.__shutdown
    @shutdown.setter
    def shutdown(self, shutdown: bool):
        self.__shutdown = shutdown

    @property
    def numProcesses(self):
        return self.__numProcesses
    @numProcesses.setter
    def numProcesses(self, numProcesses: int):
        self.__numProcesses = numProcesses

    @property
    def idleTime(self):
        return self.__idleTime
    @idleTime.setter
    def idleTime(self, idleTime: int):
        self.__idleTime = idleTime

    @property
    def dmaChannel(self):
        return self.__dmaChannel
    @dmaChannel.setter
    def dmaChannel(self, dmaChannel: str):
        self.__dmaChannel = dmaChannel

    @property
    def cpuid(self):
        return self.__cpuid
    @cpuid.setter
    def cpuid(self, cpuid: int):
        self.__cpuid = cpuid

    @property
    def cpuids(self):
        return self.__cpuids
    @cpuids.setter
    def cpuids(self, cpuids: int):
        self.__cpuids = cpuids

    @property
    def log(self):
        return self.__log
    @log.setter
    def log(self, log: str):
        self.__log = log

    @property
    def driver11(self):
        return self.__driver11
    @driver11.setter
    def driver11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpu_CPU__driver11", None)
        self.__driver11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpu10"):
                opp_val = getattr(old_value, "cpu10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpu10"):
                opp_val = getattr(value, "cpu10", None)
                if opp_val is None:
                    setattr(value, "cpu10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dmaChannel8(self):
        return self.__dmaChannel8
    @dmaChannel8.setter
    def dmaChannel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpu_CPU__dmaChannel8", None)
        self.__dmaChannel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpu9"):
                opp_val = getattr(old_value, "cpu9", None)
                if opp_val == self:
                    setattr(old_value, "cpu9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpu9"):
                opp_val = getattr(value, "cpu9", None)
                setattr(value, "cpu9", self)



class pcb_TaskManager:

    def __init__(self, processes: pcb_PCB, pcb5: set["pcb_PCB"] = None, driver6: "driver_Driver" = None):
        self.processes = processes
        self.pcb5 = pcb5 if pcb5 is not None else set()
        self.driver6 = driver6
        
        pass
    @property
    def processes(self):
        return self.__processes
    @processes.setter
    def processes(self, processes: pcb_PCB):
        self.__processes = processes

    @property
    def driver6(self):
        return self.__driver6
    @driver6.setter
    def driver6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcb_TaskManager__driver6", None)
        self.__driver6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskManager7"):
                opp_val = getattr(old_value, "taskManager7", None)
                if opp_val == self:
                    setattr(old_value, "taskManager7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskManager7"):
                opp_val = getattr(value, "taskManager7", None)
                setattr(value, "taskManager7", self)

    @property
    def pcb5(self):
        return self.__pcb5
    @pcb5.setter
    def pcb5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcb_TaskManager__pcb5", None)
        self.__pcb5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "taskManager4"):
                    opp_val = getattr(item, "taskManager4", None)
                    
                    if opp_val == self:
                        setattr(item, "taskManager4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "taskManager4"):
                    opp_val = getattr(item, "taskManager4", None)
                    
                    setattr(item, "taskManager4", self)
                    



class pcb_PCB:

    def __init__(self, pid: int, startDiskInstructionAddress: int, instructionLength: int, startDiskInputBufferAddress: int, inputBufferLength: int, startDiskOutputBufferAddress: int, outputBufferLength: int, startDiskTempBufferAddress: int, tempBufferLength: int, priority: int, cpuid: int, programCounter: int, executionCount: int, numIO: int, clock: int, elapsedWaitTime: int, elapsedRunTime: int, taskManager4: "pcb_TaskManager" = None):
        self.pid = pid
        self.startDiskInstructionAddress = startDiskInstructionAddress
        self.instructionLength = instructionLength
        self.startDiskInputBufferAddress = startDiskInputBufferAddress
        self.inputBufferLength = inputBufferLength
        self.startDiskOutputBufferAddress = startDiskOutputBufferAddress
        self.outputBufferLength = outputBufferLength
        self.startDiskTempBufferAddress = startDiskTempBufferAddress
        self.tempBufferLength = tempBufferLength
        self.priority = priority
        self.cpuid = cpuid
        self.programCounter = programCounter
        self.executionCount = executionCount
        self.numIO = numIO
        self.clock = clock
        self.elapsedWaitTime = elapsedWaitTime
        self.elapsedRunTime = elapsedRunTime
        self.taskManager4 = taskManager4
        
        pass
    @property
    def elapsedWaitTime(self):
        return self.__elapsedWaitTime
    @elapsedWaitTime.setter
    def elapsedWaitTime(self, elapsedWaitTime: int):
        self.__elapsedWaitTime = elapsedWaitTime

    @property
    def tempBufferLength(self):
        return self.__tempBufferLength
    @tempBufferLength.setter
    def tempBufferLength(self, tempBufferLength: int):
        self.__tempBufferLength = tempBufferLength

    @property
    def startDiskTempBufferAddress(self):
        return self.__startDiskTempBufferAddress
    @startDiskTempBufferAddress.setter
    def startDiskTempBufferAddress(self, startDiskTempBufferAddress: int):
        self.__startDiskTempBufferAddress = startDiskTempBufferAddress

    @property
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self, pid: int):
        self.__pid = pid

    @property
    def outputBufferLength(self):
        return self.__outputBufferLength
    @outputBufferLength.setter
    def outputBufferLength(self, outputBufferLength: int):
        self.__outputBufferLength = outputBufferLength

    @property
    def instructionLength(self):
        return self.__instructionLength
    @instructionLength.setter
    def instructionLength(self, instructionLength: int):
        self.__instructionLength = instructionLength

    @property
    def inputBufferLength(self):
        return self.__inputBufferLength
    @inputBufferLength.setter
    def inputBufferLength(self, inputBufferLength: int):
        self.__inputBufferLength = inputBufferLength

    @property
    def startDiskInputBufferAddress(self):
        return self.__startDiskInputBufferAddress
    @startDiskInputBufferAddress.setter
    def startDiskInputBufferAddress(self, startDiskInputBufferAddress: int):
        self.__startDiskInputBufferAddress = startDiskInputBufferAddress

    @property
    def programCounter(self):
        return self.__programCounter
    @programCounter.setter
    def programCounter(self, programCounter: int):
        self.__programCounter = programCounter

    @property
    def executionCount(self):
        return self.__executionCount
    @executionCount.setter
    def executionCount(self, executionCount: int):
        self.__executionCount = executionCount

    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def cpuid(self):
        return self.__cpuid
    @cpuid.setter
    def cpuid(self, cpuid: int):
        self.__cpuid = cpuid

    @property
    def startDiskInstructionAddress(self):
        return self.__startDiskInstructionAddress
    @startDiskInstructionAddress.setter
    def startDiskInstructionAddress(self, startDiskInstructionAddress: int):
        self.__startDiskInstructionAddress = startDiskInstructionAddress

    @property
    def startDiskOutputBufferAddress(self):
        return self.__startDiskOutputBufferAddress
    @startDiskOutputBufferAddress.setter
    def startDiskOutputBufferAddress(self, startDiskOutputBufferAddress: int):
        self.__startDiskOutputBufferAddress = startDiskOutputBufferAddress

    @property
    def clock(self):
        return self.__clock
    @clock.setter
    def clock(self, clock: int):
        self.__clock = clock

    @property
    def numIO(self):
        return self.__numIO
    @numIO.setter
    def numIO(self, numIO: int):
        self.__numIO = numIO

    @property
    def elapsedRunTime(self):
        return self.__elapsedRunTime
    @elapsedRunTime.setter
    def elapsedRunTime(self, elapsedRunTime: int):
        self.__elapsedRunTime = elapsedRunTime

    @property
    def taskManager4(self):
        return self.__taskManager4
    @taskManager4.setter
    def taskManager4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcb_PCB__taskManager4", None)
        self.__taskManager4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pcb5"):
                opp_val = getattr(old_value, "pcb5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pcb5"):
                opp_val = getattr(value, "pcb5", None)
                if opp_val is None:
                    setattr(value, "pcb5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class memory_MMU:

    def __init__(self, RAM: memory_Memory, memory2: "memory_Memory" = None):
        self.RAM = RAM
        self.memory2 = memory2
        
        pass
    @property
    def RAM(self):
        return self.__RAM
    @RAM.setter
    def RAM(self, RAM: memory_Memory):
        self.__RAM = RAM

    @property
    def memory2(self):
        return self.__memory2
    @memory2.setter
    def memory2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_memory_MMU__memory2", None)
        self.__memory2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmu3"):
                opp_val = getattr(old_value, "mmu3", None)
                if opp_val == self:
                    setattr(old_value, "mmu3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmu3"):
                opp_val = getattr(value, "mmu3", None)
                setattr(value, "mmu3", self)



class memory_Word:

    def __init__(self, data: int, memory1: set["memory_Memory"] = None):
        self.data = data
        self.memory1 = memory1 if memory1 is not None else set()
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: int):
        self.__data = data

    @property
    def memory1(self):
        return self.__memory1
    @memory1.setter
    def memory1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_memory_Word__memory1", None)
        self.__memory1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "word0"):
                    opp_val = getattr(item, "word0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "word0"):
                    opp_val = getattr(item, "word0", None)
                    
                    if opp_val is None:
                        setattr(item, "word0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class memory_Memory:

    def __init__(self, storage: memory_Word, word0: set["memory_Word"] = None, mmu3: "memory_MMU" = None):
        self.storage = storage
        self.word0 = word0 if word0 is not None else set()
        self.mmu3 = mmu3
        
        pass
    @property
    def storage(self):
        return self.__storage
    @storage.setter
    def storage(self, storage: memory_Word):
        self.__storage = storage

    @property
    def word0(self):
        return self.__word0
    @word0.setter
    def word0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_memory_Memory__word0", None)
        self.__word0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "memory1"):
                    opp_val = getattr(item, "memory1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "memory1"):
                    opp_val = getattr(item, "memory1", None)
                    
                    if opp_val is None:
                        setattr(item, "memory1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def mmu3(self):
        return self.__mmu3
    @mmu3.setter
    def mmu3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_memory_Memory__mmu3", None)
        self.__mmu3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memory2"):
                opp_val = getattr(old_value, "memory2", None)
                if opp_val == self:
                    setattr(old_value, "memory2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memory2"):
                opp_val = getattr(value, "memory2", None)
                setattr(value, "memory2", self)

