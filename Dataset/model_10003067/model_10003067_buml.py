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
Operating_System = Class(name="Operating_System")
Clock = Class(name="Clock")
CPU = Class(name="CPU")
Memory = Class(name="Memory")
Hard_Drive = Class(name="Hard_Drive")
Prompt = Class(name="Prompt")
Class_ = Class(name="Class")
Object = Class(name="Object")
Process = Class(name="Process")
ProcessData = Class(name="ProcessData")
ProgramFileData = Class(name="ProgramFileData")
JFrame = Class(name="JFrame")
JTextField = Class(name="JTextField")
Font = Class(name="Font")
JTextArea = Class(name="JTextArea")
JTable = Class(name="JTable")
JScrollPane = Class(name="JScrollPane")
JLabel = Class(name="JLabel")
Request = Class(name="Request")
ArrayList_ProgramFileData_ = Class(name="ArrayList_ProgramFileData_")
Exit = Class(name="Exit")
Instruction_Interface = Class(name="Instruction_Interface")
Task_Manager = Class(name="Task_Manager")

# Operating_System class attributes and methods
Operating_System_clock: Property = Property(name="clock", type=Clock)
Operating_System_cpu: Property = Property(name="cpu", type=CPU)
Operating_System_memory: Property = Property(name="memory", type=Memory)
Operating_System_hardDrive: Property = Property(name="hardDrive", type=Hard_Drive)
Operating_System_prompt: Property = Property(name="prompt", type=Prompt)
Operating_System_taskManager: Property = Property(name="taskManager", type=Task_Manager)
Operating_System.attributes={Operating_System_taskManager, Operating_System_clock, Operating_System_cpu, Operating_System_prompt, Operating_System_memory, Operating_System_hardDrive}

# Clock class attributes and methods
Clock_clockCycle: Property = Property(name="clockCycle", type=IntegerType)
Clock.attributes={Clock_clockCycle}

# CPU class attributes and methods
CPU_registers: Property = Property(name="registers", type=StringType)
CPU.attributes={CPU_registers}

# Memory class attributes and methods
Memory_memory: Property = Property(name="memory", type=Memory__)
Memory_table: Property = Property(name="table", type=Page__)
Memory.attributes={Memory_table, Memory_memory}

# Hard_Drive class attributes and methods
Hard_Drive_memory: Property = Property(name="memory", type=StringType)
Hard_Drive.attributes={Hard_Drive_memory}

# Prompt class attributes and methods
Prompt_commandLine: Property = Property(name="commandLine", type=JTextField)
Prompt_frameFont: Property = Property(name="frameFont", type=Font)
Prompt_output: Property = Property(name="output", type=JTextArea)
Prompt_FONT_SIZE: Property = Property(name="FONT_SIZE", type=IntegerType)
Prompt.attributes={Prompt_frameFont, Prompt_FONT_SIZE, Prompt_commandLine, Prompt_output}

# Class class attributes and methods

# Object class attributes and methods

# Process class attributes and methods
Process_processState: Property = Property(name="processState", type=StringType)
Process_registers: Property = Property(name="registers", type=StringType)
Process_name: Property = Property(name="name", type=StringType)
Process_memoryUseage: Property = Property(name="memoryUseage", type=IntegerType)
Process.attributes={Process_memoryUseage, Process_name, Process_processState, Process_registers}

# ProcessData class attributes and methods
ProcessData_name: Property = Property(name="name", type=StringType)
ProcessData_startTime: Property = Property(name="startTime", type=StringType)
ProcessData_instructions: Property = Property(name="instructions", type=ArrayList_Instruction_)
ProcessData_memory: Property = Property(name="memory", type=IntegerType)
ProcessData.attributes={ProcessData_name, ProcessData_startTime, ProcessData_instructions, ProcessData_memory}

# ProgramFileData class attributes and methods
ProgramFileData_name: Property = Property(name="name", type=StringType)
ProgramFileData_memory: Property = Property(name="memory", type=IntegerType)
ProgramFileData_instructions: Property = Property(name="instructions", type=ArrayList_Instruction_)
ProgramFileData.attributes={ProgramFileData_instructions, ProgramFileData_memory, ProgramFileData_name}

# JFrame class attributes and methods

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

# ArrayList_ProgramFileData_ class attributes and methods

# Exit class attributes and methods

# Instruction_Interface class attributes and methods

# Task_Manager class attributes and methods
Task_Manager_contactTable: Property = Property(name="contactTable", type=JTable)
Task_Manager_scrollPane: Property = Property(name="scrollPane", type=JScrollPane)
Task_Manager_numberOfProcesses: Property = Property(name="numberOfProcesses", type=JLabel)
Task_Manager_amountofFreeMemory: Property = Property(name="amountofFreeMemory", type=JLabel)
Task_Manager_amountofUsedMemory: Property = Property(name="amountofUsedMemory", type=JLabel)
Task_Manager.attributes={Task_Manager_amountofUsedMemory, Task_Manager_scrollPane, Task_Manager_amountofFreeMemory, Task_Manager_contactTable, Task_Manager_numberOfProcesses}

# Relationships
Exit_Operating_System: BinaryAssociation = BinaryAssociation(
    name="Exit_Operating_System",
    ends={
        Property(name="operating_System0", type=Operating_System, multiplicity=Multiplicity(0, 1)),
        Property(name="exit1", type=Exit, multiplicity=Multiplicity(0, 1))
    }
)
Instruction_ProcessData: BinaryAssociation = BinaryAssociation(
    name="Instruction_ProcessData",
    ends={
        Property(name="processData4", type=ProcessData, multiplicity=Multiplicity(0, 1)),
        Property(name="instruction5", type=Instruction_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Prompt: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Prompt",
    ends={
        Property(name="prompt6", type=Prompt, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System7", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Task_Manager: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Task_Manager",
    ends={
        Property(name="task_Manager8", type=Task_Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System9", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Task_Manager_Process: BinaryAssociation = BinaryAssociation(
    name="Task_Manager_Process",
    ends={
        Property(name="process10", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="task_Manager11", type=Task_Manager, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Clock: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Clock",
    ends={
        Property(name="clock12", type=Clock, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System13", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_CPU: BinaryAssociation = BinaryAssociation(
    name="Operating_System_CPU",
    ends={
        Property(name="cPU14", type=CPU, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System15", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Memory: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Memory",
    ends={
        Property(name="memory16", type=Memory, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System17", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
Operating_System_Hard_Drive: BinaryAssociation = BinaryAssociation(
    name="Operating_System_Hard_Drive",
    ends={
        Property(name="hard_Drive18", type=Hard_Drive, multiplicity=Multiplicity(0, 1)),
        Property(name="operating_System19", type=Operating_System, multiplicity=Multiplicity(0, 1))
    }
)
ProgramFileData_Instruction: BinaryAssociation = BinaryAssociation(
    name="ProgramFileData_Instruction",
    ends={
        Property(name="instruction20", type=Instruction_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="programFileData21", type=ProgramFileData, multiplicity=Multiplicity(0, 1))
    }
)
Hard_Drive_Request: BinaryAssociation = BinaryAssociation(
    name="Hard_Drive_Request",
    ends={
        Property(name="request22", type=Request, multiplicity=Multiplicity(0, 1)),
        Property(name="hard_Drive23", type=Hard_Drive, multiplicity=Multiplicity(0, 1))
    }
)
Exit_Process: BinaryAssociation = BinaryAssociation(
    name="Exit_Process",
    ends={
        Property(name="process2", type=Process, multiplicity=Multiplicity(0, 1)),
        Property(name="exit3", type=Exit, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="faec2d9a_8cd6_43d9_b318_870dd0707893",
    types={Operating_System, Clock, CPU, Memory, Hard_Drive, Prompt, Class_, Object, Process, ProcessData, ProgramFileData, JFrame, JTextField, Font, JTextArea, JTable, JScrollPane, JLabel, Request, ArrayList_ProgramFileData_, Exit, Instruction_Interface, Task_Manager, ArrayList_Interrupter_, Memory__, Page__, ArrayList_Instruction_, ArrayList_Integer_, ArrayList_ProcessData_},
    associations={Exit_Operating_System, Instruction_ProcessData, Operating_System_Prompt, Operating_System_Task_Manager, Task_Manager_Process, Operating_System_Clock, Operating_System_CPU, Operating_System_Memory, Operating_System_Hard_Drive, ProgramFileData_Instruction, Hard_Drive_Request, Exit_Process},
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