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
ArrayList_Interrupter_: Enumeration = Enumeration(
    name="ArrayList_Interrupter_",
    literals={
            
    }
)

ProcessState: Enumeration = Enumeration(
    name="ProcessState",
    literals={
            
    }
)

Memory__: Enumeration = Enumeration(
    name="Memory__",
    literals={
            
    }
)

Page__: Enumeration = Enumeration(
    name="Page__",
    literals={
            
    }
)

ArrayList_Instruction_: Enumeration = Enumeration(
    name="ArrayList_Instruction_",
    literals={
            
    }
)

ArrayList_Integer_: Enumeration = Enumeration(
    name="ArrayList_Integer_",
    literals={
            
    }
)

ArrayList_ProcessData_: Enumeration = Enumeration(
    name="ArrayList_ProcessData_",
    literals={
            
    }
)

# Classes
JTextField = Class(name="JTextField")
Font = Class(name="Font")
JTextArea = Class(name="JTextArea")
JTable = Class(name="JTable")
JScrollPane = Class(name="JScrollPane")
JLabel = Class(name="JLabel")
Request = Class(name="Request")
JobFileData = Class(name="JobFileData")
ArrayList_ProgramFileData_ = Class(name="ArrayList_ProgramFileData_")
Instruction_Out = Class(name="Instruction_Out")
Instruction_Calculate = Class(name="Instruction_Calculate")
Instruction_IO = Class(name="Instruction_IO")
Instruction_Exit = Class(name="Instruction_Exit")
Instruction_Instruction_Interface = Class(name="Instruction_Instruction_Interface")
Instruction_Yield = Class(name="Instruction_Yield")
Instruction_DecrementPointer = Class(name="Instruction_DecrementPointer")
Instruction_CloseBracket = Class(name="Instruction_CloseBracket")
Instruction_DecrementValue = Class(name="Instruction_DecrementValue")
Instruction_IncrementPointer = Class(name="Instruction_IncrementPointer")
Instruction_IncrementValue = Class(name="Instruction_IncrementValue")
Instruction_OpenBracket = Class(name="Instruction_OpenBracket")
Instruction_Print = Class(name="Instruction_Print")
Main = Class(name="Main")
ProcessTableModel = Class(name="ProcessTableModel")
AbstractTableModel = Class(name="AbstractTableModel")
Task_Manager = Class(name="Task_Manager")
Operating_System = Class(name="Operating_System")
Clock = Class(name="Clock")
CPU = Class(name="CPU")
Dispatcher = Class(name="Dispatcher")
Memory = Class(name="Memory")
Scheduler = Class(name="Scheduler")
IO_Device = Class(name="IO_Device")
Hard_Drive = Class(name="Hard_Drive")
Prompt = Class(name="Prompt")
Class_ = Class(name="Class")
Interrupter_Interface = Class(name="Interrupter_Interface")
Page = Class(name="Page")
Object = Class(name="Object")
Process = Class(name="Process")
ProcessData = Class(name="ProcessData")
ProgramFileData = Class(name="ProgramFileData")
JFrame = Class(name="JFrame")

# JTextField class attributes and methods

# Font class attributes and methods

# JTextArea class attributes and methods

# JTable class attributes and methods

# JScrollPane class attributes and methods

# JLabel class attributes and methods

# Request class attributes and methods
Request_startAddress: Property = Property(name="startAddress", type=IntegerType)
Request_endAddress: Property = Property(name="endAddress", type=IntegerType)
Request_processID: Property = Property(name="processID", type=IntegerType)
Request.attributes={Request_endAddress, Request_startAddress, Request_processID}

# JobFileData class attributes and methods
JobFileData_programs: Property = Property(name="programs", type=ArrayList_ProgramFileData_)
JobFileData_startTimes: Property = Property(name="startTimes", type=ArrayList_Integer_)
JobFileData.attributes={JobFileData_programs, JobFileData_startTimes}

# ArrayList_ProgramFileData_ class attributes and methods

# Instruction_Out class attributes and methods

# Instruction_Calculate class attributes and methods
Instruction_Calculate_time: Property = Property(name="time", type=IntegerType)
Instruction_Calculate.attributes={Instruction_Calculate_time}

# Instruction_IO class attributes and methods

# Instruction_Exit class attributes and methods

# Instruction_Instruction_Interface class attributes and methods

# Instruction_Yield class attributes and methods

# Instruction_DecrementPointer class attributes and methods

# Instruction_CloseBracket class attributes and methods

# Instruction_DecrementValue class attributes and methods

# Instruction_IncrementPointer class attributes and methods

# Instruction_IncrementValue class attributes and methods

# Instruction_OpenBracket class attributes and methods

# Instruction_Print class attributes and methods

# Main class attributes and methods

# ProcessTableModel class attributes and methods
ProcessTableModel_columnNames: Property = Property(name="columnNames", type=StringType)
ProcessTableModel_processList: Property = Property(name="processList", type=StringType)
ProcessTableModel_numberProcesses: Property = Property(name="numberProcesses", type=IntegerType)
ProcessTableModel.attributes={ProcessTableModel_numberProcesses, ProcessTableModel_columnNames, ProcessTableModel_processList}

# AbstractTableModel class attributes and methods

# Task_Manager class attributes and methods
Task_Manager_contactTable: Property = Property(name="contactTable", type=JTable)
Task_Manager_scrollPane: Property = Property(name="scrollPane", type=JScrollPane)
Task_Manager_numberOfProcesses: Property = Property(name="numberOfProcesses", type=JLabel)
Task_Manager_amountofFreeMemory: Property = Property(name="amountofFreeMemory", type=JLabel)
Task_Manager_amountofUsedMemory: Property = Property(name="amountofUsedMemory", type=JLabel)
Task_Manager.attributes={Task_Manager_numberOfProcesses, Task_Manager_contactTable, Task_Manager_amountofFreeMemory, Task_Manager_amountofUsedMemory, Task_Manager_scrollPane}

# Operating_System class attributes and methods
Operating_System_MEMORY_SIZE: Property = Property(name="MEMORY_SIZE", type=IntegerType)
Operating_System_PAGE_SIZE: Property = Property(name="PAGE_SIZE", type=IntegerType)
Operating_System_NUMBER_OF_REGISTERS: Property = Property(name="NUMBER_OF_REGISTERS", type=IntegerType)
Operating_System_INSTRUCTION_REGISTER: Property = Property(name="INSTRUCTION_REGISTER", type=IntegerType)
Operating_System_PROC_BASE_REGISTER: Property = Property(name="PROC_BASE_REGISTER", type=IntegerType)
Operating_System_PROC_LIMIT_REGISTER: Property = Property(name="PROC_LIMIT_REGISTER", type=IntegerType)
Operating_System_PROCESS_ID_REGISTER: Property = Property(name="PROCESS_ID_REGISTER", type=IntegerType)
Operating_System_PROC_BASE_POINTER: Property = Property(name="PROC_BASE_POINTER", type=IntegerType)
Operating_System_PROC_DATA_POINTER: Property = Property(name="PROC_DATA_POINTER", type=IntegerType)
Operating_System_QUANTUM: Property = Property(name="QUANTUM", type=IntegerType)
Operating_System_clock: Property = Property(name="clock", type=Clock)
Operating_System_cpu: Property = Property(name="cpu", type=CPU)
Operating_System_dispatcher: Property = Property(name="dispatcher", type=Dispatcher)
Operating_System_memory: Property = Property(name="memory", type=Memory)
Operating_System_scheduler: Property = Property(name="scheduler", type=Scheduler)
Operating_System_device: Property = Property(name="device", type=IO_Device)
Operating_System_hardDrive: Property = Property(name="hardDrive", type=Hard_Drive)
Operating_System_prompt: Property = Property(name="prompt", type=Prompt)
Operating_System_taskManager: Property = Property(name="taskManager", type=Task_Manager)
Operating_System.attributes={Operating_System_PAGE_SIZE, Operating_System_taskManager, Operating_System_PROC_DATA_POINTER, Operating_System_PROCESS_ID_REGISTER, Operating_System_prompt, Operating_System_PROC_BASE_REGISTER, Operating_System_dispatcher, Operating_System_PROC_LIMIT_REGISTER, Operating_System_device, Operating_System_clock, Operating_System_PROC_BASE_POINTER, Operating_System_memory, Operating_System_NUMBER_OF_REGISTERS, Operating_System_cpu, Operating_System_INSTRUCTION_REGISTER, Operating_System_QUANTUM, Operating_System_hardDrive, Operating_System_MEMORY_SIZE, Operating_System_scheduler}

# Clock class attributes and methods
Clock_clockCycle: Property = Property(name="clockCycle", type=IntegerType)
Clock.attributes={Clock_clockCycle}

# CPU class attributes and methods
CPU_registers: Property = Property(name="registers", type=StringType)
CPU_interruptQueue: Property = Property(name="interruptQueue", type=ArrayList_Interrupter_)
CPU.attributes={CPU_registers, CPU_interruptQueue}

# Dispatcher class attributes and methods

# Memory class attributes and methods
Memory_memory: Property = Property(name="memory", type=Memory__)
Memory_table: Property = Property(name="table", type=Page__)
Memory.attributes={Memory_memory, Memory_table}

# Scheduler class attributes and methods
Scheduler_newQueue: Property = Property(name="newQueue", type=ProcessData)
Scheduler_readyQueue: Property = Property(name="readyQueue", type=Process)
Scheduler_ioQueue: Property = Property(name="ioQueue", type=Process)
Scheduler_identifier: Property = Property(name="identifier", type=IntegerType)
Scheduler.attributes={Scheduler_newQueue, Scheduler_readyQueue, Scheduler_identifier, Scheduler_ioQueue}

# IO_Device class attributes and methods
IO_Device_counter: Property = Property(name="counter", type=IntegerType)
IO_Device.attributes={IO_Device_counter}

# Hard_Drive class attributes and methods
Hard_Drive_memory: Property = Property(name="memory", type=StringType)
Hard_Drive.attributes={Hard_Drive_memory}

# Prompt class attributes and methods
Prompt_queuePosition: Property = Property(name="queuePosition", type=IntegerType)
Prompt_frame: Property = Property(name="frame", type=JFrame)
Prompt_commandLine: Property = Property(name="commandLine", type=JTextField)
Prompt_frameFont: Property = Property(name="frameFont", type=Font)
Prompt_output: Property = Property(name="output", type=JTextArea)
Prompt_MAX_COMMAND_LENGTH: Property = Property(name="MAX_COMMAND_LENGTH", type=IntegerType)
Prompt_OUTPUT_HEIGHT: Property = Property(name="OUTPUT_HEIGHT", type=IntegerType)
Prompt_OUTPUT_WIDTH: Property = Property(name="OUTPUT_WIDTH", type=IntegerType)
Prompt_FONT_SIZE: Property = Property(name="FONT_SIZE", type=IntegerType)
Prompt.attributes={Prompt_FONT_SIZE, Prompt_frame, Prompt_frameFont, Prompt_output, Prompt_MAX_COMMAND_LENGTH, Prompt_commandLine, Prompt_queuePosition, Prompt_OUTPUT_HEIGHT, Prompt_OUTPUT_WIDTH}

# Class class attributes and methods

# Interrupter_Interface class attributes and methods

# Page class attributes and methods
Page_owner: Property = Property(name="owner", type=Process)
Page_attribute: Property = Property(name="attribute", type=StringType)
Page_free: Property = Property(name="free", type=BooleanType)
Page.attributes={Page_owner, Page_attribute, Page_free}

# Object class attributes and methods

# Process class attributes and methods
Process_processState: Property = Property(name="processState", type=ProcessState)
Process_registers: Property = Property(name="registers", type=StringType)
Process_name: Property = Property(name="name", type=StringType)
Process_memoryUseage: Property = Property(name="memoryUseage", type=IntegerType)
Process.attributes={Process_registers, Process_name, Process_memoryUseage, Process_processState}

# ProcessData class attributes and methods
ProcessData_name: Property = Property(name="name", type=StringType)
ProcessData_startTime: Property = Property(name="startTime", type=StringType)
ProcessData_instructions: Property = Property(name="instructions", type=ArrayList_Instruction_)
ProcessData_memory: Property = Property(name="memory", type=IntegerType)
ProcessData.attributes={ProcessData_instructions, ProcessData_memory, ProcessData_name, ProcessData_startTime}

# ProgramFileData class attributes and methods
ProgramFileData_name: Property = Property(name="name", type=StringType)
ProgramFileData_memory: Property = Property(name="memory", type=IntegerType)
ProgramFileData_instructions: Property = Property(name="instructions", type=ArrayList_Instruction_)
ProgramFileData.attributes={ProgramFileData_instructions, ProgramFileData_memory, ProgramFileData_name}

# JFrame class attributes and methods

# Relationships
ProcessTableModel_Operating_System: BinaryAssociation = BinaryAssociation(
    name="ProcessTableModel_Operating_System",
    ends={
        Property(name="operating_System16", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="processTableModel17", type=ProcessTableModel, multiplicity=Multiplicity(0, 1))
    }
)
ProcessTableModel_Process: BinaryAssociation = BinaryAssociation(
    name="ProcessTableModel_Process",
    ends={
        Property(name="process18", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="processTableModel19", type=ProcessTableModel, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Prompt: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Prompt",
    ends={
        Property(name="prompt20", type=Prompt, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System21", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Task_Manager: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Task_Manager",
    ends={
        Property(name="task_Manager22", type=Task_Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System23", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Task_Manager_Process: BinaryAssociation = BinaryAssociation(
    name="Task_Manager_Process",
    ends={
        Property(name="process24", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="task_Manager25", type=Task_Manager, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Main: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Main",
    ends={
        Property(name="main26", type=Main, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System27", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Clock: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Clock",
    ends={
        Property(name="clock28", type=Clock, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System29", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_CPU: BinaryAssociation = BinaryAssociation(
    name="Operating_System_CPU",
    ends={
        Property(name="cPU30", type=CPU, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System31", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Dispatcher: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Dispatcher",
    ends={
        Property(name="dispatcher32", type=Dispatcher, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System33", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Memory: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Memory",
    ends={
        Property(name="memory34", type=Memory, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System35", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Yield_Operating_System: BinaryAssociation = BinaryAssociation(
    name="Yield_Operating_System",
    ends={
        Property(name="operating_System0", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="yield1", type=Instruction_Yield, multiplicity=Multiplicity(0, 1))
    }
)
IO_Operating_System: BinaryAssociation = BinaryAssociation(
    name="IO_Operating_System",
    ends={
        Property(name="operating_System2", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="iO3", type=Instruction_IO, multiplicity=Multiplicity(0, 1))
    }
)
IO_Process: BinaryAssociation = BinaryAssociation(
    name="IO_Process",
    ends={
        Property(name="process4", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="iO5", type=Instruction_IO, multiplicity=Multiplicity(0, 1))
    }
)
Exit_Operating_System: BinaryAssociation = BinaryAssociation(
    name="Exit_Operating_System",
    ends={
        Property(name="operating_System6", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="exit7", type=Instruction_Exit, multiplicity=Multiplicity(0, 1))
    }
)
Exit_Process: BinaryAssociation = BinaryAssociation(
    name="Exit_Process",
    ends={
        Property(name="process8", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="exit9", type=Instruction_Exit, multiplicity=Multiplicity(0, 1))
    }
)
Calculate_Operating_System: BinaryAssociation = BinaryAssociation(
    name="Calculate_Operating_System",
    ends={
        Property(name="operating_System10", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="calculate11", type=Instruction_Calculate, multiplicity=Multiplicity(0, 1))
    }
)
Out_Operating_System: BinaryAssociation = BinaryAssociation(
    name="Out_Operating_System",
    ends={
        Property(name="operating_System12", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="out13", type=Instruction_Out, multiplicity=Multiplicity(0, 1))
    }
)
Instruction_ProcessData: BinaryAssociation = BinaryAssociation(
    name="Instruction_ProcessData",
    ends={
        Property(name="processData14", type=ProcessData, multiplicity=Multiplicity(0, 1)),
        Property(name="instruction15", type=Instruction_Instruction_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Scheduler: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Scheduler",
    ends={
        Property(name="scheduler36", type=Scheduler, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System37", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_IO_Device: BinaryAssociation = BinaryAssociation(
    name="Operating_System_IO_Device",
    ends={
        Property(name="iO_Device38", type=IO_Device, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System39", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Hard_Drive: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Hard_Drive",
    ends={
        Property(name="hard_Drive40", type=Hard_Drive, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System41", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Page_Process: BinaryAssociation = BinaryAssociation(
    name="Page_Process",
    ends={
        Property(name="process42", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="page43", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
ProgramFileData_Instruction: BinaryAssociation = BinaryAssociation(
    name="ProgramFileData_Instruction",
    ends={
        Property(name="instruction44", type=Instruction_Instruction_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="programFileData45", type=ProgramFileData, multiplicity=Multiplicity(0, 1))
    }
)
JobFileData_ProgramFileData: BinaryAssociation = BinaryAssociation(
    name="JobFileData_ProgramFileData",
    ends={
        Property(name="programFileData46", type=ProgramFileData, multiplicity=Multiplicity(0, 1)),
        Property(name="jobFileData47", type=JobFileData, multiplicity=Multiplicity(0, 1))
    }
)
Hard_Drive_Request: BinaryAssociation = BinaryAssociation(
    name="Hard_Drive_Request",
    ends={
        Property(name="request48", type=Request, multiplicity=Multiplicity(0, 1)),
        Property(name="hard_Drive49", type=Hard_Drive, multiplicity=Multiplicity(0, 1))
    }
)
Memory_Page: BinaryAssociation = BinaryAssociation(
    name="Memory_Page",
    ends={
        Property(name="page50", type=Page, multiplicity=Multiplicity(0, 1)),
        Property(name="memory51", type=Memory, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_416e9965_907c_4d7b_a3a0_f5a559a8ac60",
    types={JTextField, Font, JTextArea, JTable, JScrollPane, JLabel, Request, JobFileData, ArrayList_ProgramFileData_, Instruction_Out, Instruction_Calculate, Instruction_IO, Instruction_Exit, Instruction_Instruction_Interface, Instruction_Yield, Instruction_DecrementPointer, Instruction_CloseBracket, Instruction_DecrementValue, Instruction_IncrementPointer, Instruction_IncrementValue, Instruction_OpenBracket, Instruction_Print, Main, ProcessTableModel, AbstractTableModel, Task_Manager, Operating_System, Clock, CPU, Dispatcher, Memory, Scheduler, IO_Device, Hard_Drive, Prompt, Class_, Interrupter_Interface, Page, Object, Process, ProcessData, ProgramFileData, JFrame, ArrayList_Interrupter_, ProcessState, Memory__, Page__, ArrayList_Instruction_, ArrayList_Integer_, ArrayList_ProcessData_},
    associations={ProcessTableModel_Operating_System, ProcessTableModel_Process, Operating_System_Prompt, Operating_System_Task_Manager, Task_Manager_Process, Operating_System_Main, Operating_System_Clock, Operating_System_CPU, Operating_System_Dispatcher, Operating_System_Memory, Yield_Operating_System, IO_Operating_System, IO_Process, Exit_Operating_System, Exit_Process, Calculate_Operating_System, Out_Operating_System, Instruction_ProcessData, Operating_System_Scheduler, Operating_System_IO_Device, Operating_System_Hard_Drive, Page_Process, ProgramFileData_Instruction, JobFileData_ProgramFileData, Hard_Drive_Request, Memory_Page},
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