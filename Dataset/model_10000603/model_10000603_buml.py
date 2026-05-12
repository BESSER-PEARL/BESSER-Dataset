####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Byte: Enumeration = Enumeration(
    name="Byte",
    literals={
            
    }
)

pcb_PCB_Status: Enumeration = Enumeration(
    name="pcb_PCB_Status",
    literals={
            
    }
)

cpu_InstructionSet: Enumeration = Enumeration(
    name="cpu_InstructionSet",
    literals={
            
    }
)

driver_CPUSchedulingPolicy: Enumeration = Enumeration(
    name="driver_CPUSchedulingPolicy",
    literals={
            
    }
)

# Classes
memory_Memory = Class(name="memory_Memory")
memory_Word = Class(name="memory_Word")
memory_MMU = Class(name="memory_MMU")
pcb_PCB = Class(name="pcb_PCB")
pcb_TaskManager = Class(name="pcb_TaskManager")
cpu_CPU = Class(name="cpu_CPU")
cpu_DMAChannel = Class(name="cpu_DMAChannel")
cpu_ExecutableInstruction = Class(name="cpu_ExecutableInstruction", is_abstract=True)
cpu_ArithmeticExecutableInstruction = Class(name="cpu_ArithmeticExecutableInstruction")
cpu_ConditionalExecutableInstruction = Class(name="cpu_ConditionalExecutableInstruction")
cpu_UnconditionalJumpExecutableInstruction = Class(name="cpu_UnconditionalJumpExecutableInstruction")
cpu_IOExecutableInstruction = Class(name="cpu_IOExecutableInstruction")
driver_Driver = Class(name="driver_Driver")
driver_Loader = Class(name="driver_Loader")
driver_Dispatcher = Class(name="driver_Dispatcher")
driver_Scheduler = Class(name="driver_Scheduler")
java_lang_Runnable_Interface = Class(name="java_lang_Runnable_Interface")

# memory_Memory class attributes and methods
memory_Memory_storage: Property = Property(name="storage", type=memory_Word)
memory_Memory.attributes={memory_Memory_storage}

# memory_Word class attributes and methods
memory_Word_data: Property = Property(name="data", type=IntegerType)
memory_Word.attributes={memory_Word_data}

# memory_MMU class attributes and methods
memory_MMU_RAM: Property = Property(name="RAM", type=memory_Memory)
memory_MMU.attributes={memory_MMU_RAM}

# pcb_PCB class attributes and methods
pcb_PCB_pid: Property = Property(name="pid", type=IntegerType)
pcb_PCB_startDiskInstructionAddress: Property = Property(name="startDiskInstructionAddress", type=IntegerType)
pcb_PCB_instructionLength: Property = Property(name="instructionLength", type=IntegerType)
pcb_PCB_startDiskInputBufferAddress: Property = Property(name="startDiskInputBufferAddress", type=IntegerType)
pcb_PCB_inputBufferLength: Property = Property(name="inputBufferLength", type=IntegerType)
pcb_PCB_startDiskOutputBufferAddress: Property = Property(name="startDiskOutputBufferAddress", type=IntegerType)
pcb_PCB_outputBufferLength: Property = Property(name="outputBufferLength", type=IntegerType)
pcb_PCB_startDiskTempBufferAddress: Property = Property(name="startDiskTempBufferAddress", type=IntegerType)
pcb_PCB_tempBufferLength: Property = Property(name="tempBufferLength", type=IntegerType)
pcb_PCB_priority: Property = Property(name="priority", type=IntegerType)
pcb_PCB_cpuid: Property = Property(name="cpuid", type=IntegerType)
pcb_PCB_programCounter: Property = Property(name="programCounter", type=IntegerType)
pcb_PCB_executionCount: Property = Property(name="executionCount", type=IntegerType)
pcb_PCB_numIO: Property = Property(name="numIO", type=IntegerType)
pcb_PCB_clock: Property = Property(name="clock", type=IntegerType)
pcb_PCB_elapsedWaitTime: Property = Property(name="elapsedWaitTime", type=IntegerType)
pcb_PCB_elapsedRunTime: Property = Property(name="elapsedRunTime", type=IntegerType)
pcb_PCB.attributes={pcb_PCB_outputBufferLength, pcb_PCB_startDiskTempBufferAddress, pcb_PCB_tempBufferLength, pcb_PCB_startDiskOutputBufferAddress, pcb_PCB_elapsedRunTime, pcb_PCB_elapsedWaitTime, pcb_PCB_priority, pcb_PCB_instructionLength, pcb_PCB_startDiskInputBufferAddress, pcb_PCB_pid, pcb_PCB_programCounter, pcb_PCB_executionCount, pcb_PCB_startDiskInstructionAddress, pcb_PCB_cpuid, pcb_PCB_clock, pcb_PCB_inputBufferLength, pcb_PCB_numIO}

# pcb_TaskManager class attributes and methods
pcb_TaskManager_processes: Property = Property(name="processes", type=pcb_PCB)
pcb_TaskManager.attributes={pcb_TaskManager_processes}

# cpu_CPU class attributes and methods
cpu_CPU_dmaChannel: Property = Property(name="dmaChannel", type=StringType)
cpu_CPU_pcb: Property = Property(name="pcb", type=pcb_PCB)
cpu_CPU_previousInstruction: Property = Property(name="previousInstruction", type=cpu_ExecutableInstruction)
cpu_CPU_log: Property = Property(name="log", type=StringType)
cpu_CPU_shutdown: Property = Property(name="shutdown", type=BooleanType)
cpu_CPU_idleTime: Property = Property(name="idleTime", type=IntegerType)
cpu_CPU_cache: Property = Property(name="cache", type=memory_Memory)
cpu_CPU_executeTime: Property = Property(name="executeTime", type=IntegerType)
cpu_CPU_numProcesses: Property = Property(name="numProcesses", type=IntegerType)
cpu_CPU_register: Property = Property(name="register", type=memory_Memory)
cpu_CPU_cpuids: Property = Property(name="cpuids", type=IntegerType)
cpu_CPU_cpuid: Property = Property(name="cpuid", type=IntegerType)
cpu_CPU.attributes={cpu_CPU_pcb, cpu_CPU_cpuid, cpu_CPU_shutdown, cpu_CPU_executeTime, cpu_CPU_idleTime, cpu_CPU_numProcesses, cpu_CPU_dmaChannel, cpu_CPU_cache, cpu_CPU_register, cpu_CPU_log, cpu_CPU_previousInstruction, cpu_CPU_cpuids}

# cpu_DMAChannel class attributes and methods
cpu_DMAChannel_mmu: Property = Property(name="mmu", type=StringType)
cpu_DMAChannel.attributes={cpu_DMAChannel_mmu}

# cpu_ExecutableInstruction class attributes and methods
cpu_ExecutableInstruction_type: Property = Property(name="type", type=cpu_InstructionSet)
cpu_ExecutableInstruction_registers: Property = Property(name="registers", type=memory_Memory)
cpu_ExecutableInstruction.attributes={cpu_ExecutableInstruction_type, cpu_ExecutableInstruction_registers}

# cpu_ArithmeticExecutableInstruction class attributes and methods
cpu_ArithmeticExecutableInstruction_s1: Property = Property(name="s1", type=IntegerType)
cpu_ArithmeticExecutableInstruction_s2: Property = Property(name="s2", type=IntegerType)
cpu_ArithmeticExecutableInstruction_d: Property = Property(name="d", type=IntegerType)
cpu_ArithmeticExecutableInstruction.attributes={cpu_ArithmeticExecutableInstruction_s1, cpu_ArithmeticExecutableInstruction_d, cpu_ArithmeticExecutableInstruction_s2}

# cpu_ConditionalExecutableInstruction class attributes and methods
cpu_ConditionalExecutableInstruction_cpu: Property = Property(name="cpu", type=cpu_CPU)
cpu_ConditionalExecutableInstruction_bReg: Property = Property(name="bReg", type=IntegerType)
cpu_ConditionalExecutableInstruction_dReg: Property = Property(name="dReg", type=IntegerType)
cpu_ConditionalExecutableInstruction_data: Property = Property(name="data", type=IntegerType)
cpu_ConditionalExecutableInstruction_cache: Property = Property(name="cache", type=memory_Memory)
cpu_ConditionalExecutableInstruction.attributes={cpu_ConditionalExecutableInstruction_cache, cpu_ConditionalExecutableInstruction_data, cpu_ConditionalExecutableInstruction_cpu, cpu_ConditionalExecutableInstruction_bReg, cpu_ConditionalExecutableInstruction_dReg}

# cpu_UnconditionalJumpExecutableInstruction class attributes and methods
cpu_UnconditionalJumpExecutableInstruction_cpu: Property = Property(name="cpu", type=cpu_CPU)
cpu_UnconditionalJumpExecutableInstruction_address: Property = Property(name="address", type=IntegerType)
cpu_UnconditionalJumpExecutableInstruction.attributes={cpu_UnconditionalJumpExecutableInstruction_cpu, cpu_UnconditionalJumpExecutableInstruction_address}

# cpu_IOExecutableInstruction class attributes and methods
cpu_IOExecutableInstruction_reg1: Property = Property(name="reg1", type=IntegerType)
cpu_IOExecutableInstruction_reg2: Property = Property(name="reg2", type=IntegerType)
cpu_IOExecutableInstruction_address: Property = Property(name="address", type=IntegerType)
cpu_IOExecutableInstruction.attributes={cpu_IOExecutableInstruction_reg1, cpu_IOExecutableInstruction_address, cpu_IOExecutableInstruction_reg2}

# driver_Driver class attributes and methods
driver_Driver_loader: Property = Property(name="loader", type=driver_Loader)
driver_Driver_taskManager: Property = Property(name="taskManager", type=pcb_TaskManager)
driver_Driver_registerSize: Property = Property(name="registerSize", type=IntegerType)
driver_Driver_cacheSize: Property = Property(name="cacheSize", type=IntegerType)
driver_Driver_ramSize: Property = Property(name="ramSize", type=IntegerType)
driver_Driver_scheduler: Property = Property(name="scheduler", type=driver_Scheduler)
driver_Driver_dispatcher: Property = Property(name="dispatcher", type=driver_Dispatcher)
driver_Driver_cpus: Property = Property(name="cpus", type=cpu_CPU)
driver_Driver_threads: Property = Property(name="threads", type=StringType)
driver_Driver_disk: Property = Property(name="disk", type=memory_Memory)
driver_Driver_idleTimes: Property = Property(name="idleTimes", type=IntegerType)
driver_Driver_executeTimes: Property = Property(name="executeTimes", type=IntegerType)
driver_Driver.attributes={driver_Driver_cacheSize, driver_Driver_loader, driver_Driver_threads, driver_Driver_scheduler, driver_Driver_disk, driver_Driver_executeTimes, driver_Driver_registerSize, driver_Driver_idleTimes, driver_Driver_taskManager, driver_Driver_cpus, driver_Driver_dispatcher, driver_Driver_ramSize}

# driver_Loader class attributes and methods
driver_Loader_pid: Property = Property(name="pid", type=IntegerType)
driver_Loader_instructionsLength: Property = Property(name="instructionsLength", type=IntegerType)
driver_Loader_priority: Property = Property(name="priority", type=IntegerType)
driver_Loader_inputBuffSize: Property = Property(name="inputBuffSize", type=IntegerType)
driver_Loader_outputBuffSize: Property = Property(name="outputBuffSize", type=IntegerType)
driver_Loader_tempBuffSize: Property = Property(name="tempBuffSize", type=IntegerType)
driver_Loader_startInstructionAddress: Property = Property(name="startInstructionAddress", type=IntegerType)
driver_Loader_startInputBufferAddress: Property = Property(name="startInputBufferAddress", type=IntegerType)
driver_Loader_startOutputBufferAddress: Property = Property(name="startOutputBufferAddress", type=IntegerType)
driver_Loader_startTempBufferAddress: Property = Property(name="startTempBufferAddress", type=IntegerType)
driver_Loader_endInstructionAddress: Property = Property(name="endInstructionAddress", type=IntegerType)
driver_Loader_endInputBufferAddres: Property = Property(name="endInputBufferAddres", type=IntegerType)
driver_Loader_endOutputBufferAddress: Property = Property(name="endOutputBufferAddress", type=IntegerType)
driver_Loader_endTempBufferAddress: Property = Property(name="endTempBufferAddress", type=IntegerType)
driver_Loader_currAddress: Property = Property(name="currAddress", type=IntegerType)
driver_Loader_disk: Property = Property(name="disk", type=memory_Memory)
driver_Loader_programFile: Property = Property(name="programFile", type=StringType)
driver_Loader_processList: Property = Property(name="processList", type=pcb_TaskManager)
driver_Loader.attributes={driver_Loader_priority, driver_Loader_inputBuffSize, driver_Loader_startTempBufferAddress, driver_Loader_currAddress, driver_Loader_programFile, driver_Loader_processList, driver_Loader_outputBuffSize, driver_Loader_startOutputBufferAddress, driver_Loader_endInputBufferAddres, driver_Loader_endOutputBufferAddress, driver_Loader_instructionsLength, driver_Loader_pid, driver_Loader_startInputBufferAddress, driver_Loader_endInstructionAddress, driver_Loader_startInstructionAddress, driver_Loader_disk, driver_Loader_endTempBufferAddress, driver_Loader_tempBuffSize}

# driver_Dispatcher class attributes and methods
driver_Dispatcher_taskManager: Property = Property(name="taskManager", type=pcb_TaskManager)
driver_Dispatcher_cpus: Property = Property(name="cpus", type=cpu_CPU)
driver_Dispatcher_mmu: Property = Property(name="mmu", type=memory_MMU)
driver_Dispatcher.attributes={driver_Dispatcher_taskManager, driver_Dispatcher_mmu, driver_Dispatcher_cpus}

# driver_Scheduler class attributes and methods
driver_Scheduler_mmu: Property = Property(name="mmu", type=memory_MMU)
driver_Scheduler_disk: Property = Property(name="disk", type=memory_Memory)
driver_Scheduler_taskManager: Property = Property(name="taskManager", type=pcb_TaskManager)
driver_Scheduler_schedulingMethod: Property = Property(name="schedulingMethod", type=driver_CPUSchedulingPolicy)
driver_Scheduler.attributes={driver_Scheduler_schedulingMethod, driver_Scheduler_disk, driver_Scheduler_mmu, driver_Scheduler_taskManager}

# java_lang_Runnable_Interface class attributes and methods

# Relationships
Memory_Word: BinaryAssociation = BinaryAssociation(
    name="Memory_Word",
    ends={
        Property(name="word0", type=memory_Word, multiplicity=Multiplicity(0, 9999)),
        Property(name="memory1", type=memory_Memory, multiplicity=Multiplicity(0, 9999))
    }
)
MMU_Memory: BinaryAssociation = BinaryAssociation(
    name="MMU_Memory",
    ends={
        Property(name="memory2", type=memory_Memory, multiplicity=Multiplicity(1, 1)),
        Property(name="mmu3", type=memory_MMU, multiplicity=Multiplicity(0, 1))
    }
)
PCB_TaskManager: BinaryAssociation = BinaryAssociation(
    name="PCB_TaskManager",
    ends={
        Property(name="taskManager4", type=pcb_TaskManager, multiplicity=Multiplicity(1, 1)),
        Property(name="pcb5", type=pcb_PCB, multiplicity=Multiplicity(0, 9999))
    }
)
TaskManager_Driver: BinaryAssociation = BinaryAssociation(
    name="TaskManager_Driver",
    ends={
        Property(name="driver6", type=driver_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="taskManager7", type=pcb_TaskManager, multiplicity=Multiplicity(1, 1))
    }
)
CPU_DMAChannel: BinaryAssociation = BinaryAssociation(
    name="CPU_DMAChannel",
    ends={
        Property(name="dmaChannel8", type=cpu_DMAChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="cpu9", type=cpu_CPU, multiplicity=Multiplicity(1, 1))
    }
)
Driver_CPU: BinaryAssociation = BinaryAssociation(
    name="Driver_CPU",
    ends={
        Property(name="cpu10", type=cpu_CPU, multiplicity=Multiplicity(1, 9999)),
        Property(name="driver11", type=driver_Driver, multiplicity=Multiplicity(1, 1))
    }
)
Driver_Scheduler: BinaryAssociation = BinaryAssociation(
    name="Driver_Scheduler",
    ends={
        Property(name="scheduler12", type=driver_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="driver13", type=driver_Driver, multiplicity=Multiplicity(1, 1))
    }
)
Driver_Loader: BinaryAssociation = BinaryAssociation(
    name="Driver_Loader",
    ends={
        Property(name="loader14", type=driver_Loader, multiplicity=Multiplicity(1, 1)),
        Property(name="driver15", type=driver_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
Driver_Dispatcher: BinaryAssociation = BinaryAssociation(
    name="Driver_Dispatcher",
    ends={
        Property(name="dispatcher16", type=driver_Dispatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="driver17", type=driver_Driver, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_49aa0d6e_dd03_4380_824f_f8aed9689fd8",
    types={memory_Memory, memory_Word, memory_MMU, pcb_PCB, pcb_TaskManager, cpu_CPU, cpu_DMAChannel, cpu_ExecutableInstruction, cpu_ArithmeticExecutableInstruction, cpu_ConditionalExecutableInstruction, cpu_UnconditionalJumpExecutableInstruction, cpu_IOExecutableInstruction, driver_Driver, driver_Loader, driver_Dispatcher, driver_Scheduler, java_lang_Runnable_Interface, Byte, pcb_PCB_Status, cpu_InstructionSet, driver_CPUSchedulingPolicy},
    associations={Memory_Word, MMU_Memory, PCB_TaskManager, TaskManager_Driver, CPU_DMAChannel, Driver_CPU, Driver_Scheduler, Driver_Loader, Driver_Dispatcher},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)