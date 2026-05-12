from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArrayList_Interrupter_(Enum):
    pass
class Memory__(Enum):
    pass
class ArrayList_Instruction_(Enum):
    pass
class Page__(Enum):
    pass
class ArrayList_ProcessData_(Enum):
    pass
class ArrayList_Integer_(Enum):
    pass

############################################
# Definition of Classes
############################################










class Task_Manager:

    def __init__(self, contactTable: JTable, scrollPane: JScrollPane, numberOfProcesses: JLabel, amountofFreeMemory: JLabel, amountofUsedMemory: JLabel, operating_System9: "Operating_System" = None, process10: "Process" = None):
        self.contactTable = contactTable
        self.scrollPane = scrollPane
        self.numberOfProcesses = numberOfProcesses
        self.amountofFreeMemory = amountofFreeMemory
        self.amountofUsedMemory = amountofUsedMemory
        self.operating_System9 = operating_System9
        self.process10 = process10
        
        pass
    @property
    def numberOfProcesses(self):
        return self.__numberOfProcesses
    @numberOfProcesses.setter
    def numberOfProcesses(self, numberOfProcesses: JLabel):
        self.__numberOfProcesses = numberOfProcesses

    @property
    def scrollPane(self):
        return self.__scrollPane
    @scrollPane.setter
    def scrollPane(self, scrollPane: JScrollPane):
        self.__scrollPane = scrollPane

    @property
    def contactTable(self):
        return self.__contactTable
    @contactTable.setter
    def contactTable(self, contactTable: JTable):
        self.__contactTable = contactTable

    @property
    def amountofUsedMemory(self):
        return self.__amountofUsedMemory
    @amountofUsedMemory.setter
    def amountofUsedMemory(self, amountofUsedMemory: JLabel):
        self.__amountofUsedMemory = amountofUsedMemory

    @property
    def amountofFreeMemory(self):
        return self.__amountofFreeMemory
    @amountofFreeMemory.setter
    def amountofFreeMemory(self, amountofFreeMemory: JLabel):
        self.__amountofFreeMemory = amountofFreeMemory

    @property
    def operating_System9(self):
        return self.__operating_System9
    @operating_System9.setter
    def operating_System9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task_Manager__operating_System9", None)
        self.__operating_System9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task_Manager8"):
                opp_val = getattr(old_value, "task_Manager8", None)
                if opp_val == self:
                    setattr(old_value, "task_Manager8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task_Manager8"):
                opp_val = getattr(value, "task_Manager8", None)
                setattr(value, "task_Manager8", self)

    @property
    def process10(self):
        return self.__process10
    @process10.setter
    def process10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task_Manager__process10", None)
        self.__process10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task_Manager11"):
                opp_val = getattr(old_value, "task_Manager11", None)
                if opp_val == self:
                    setattr(old_value, "task_Manager11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task_Manager11"):
                opp_val = getattr(value, "task_Manager11", None)
                setattr(value, "task_Manager11", self)



class Instruction_Interface:

    pass


class Exit:

    pass


class ArrayList_ProgramFileData_:

    pass


class Request:

    def __init__(self, startAddress: int, endAddress: int, processID: int, hard_Drive23: "Hard_Drive" = None):
        self.startAddress = startAddress
        self.endAddress = endAddress
        self.processID = processID
        self.hard_Drive23 = hard_Drive23
        
        pass
    @property
    def endAddress(self):
        return self.__endAddress
    @endAddress.setter
    def endAddress(self, endAddress: int):
        self.__endAddress = endAddress

    @property
    def startAddress(self):
        return self.__startAddress
    @startAddress.setter
    def startAddress(self, startAddress: int):
        self.__startAddress = startAddress

    @property
    def processID(self):
        return self.__processID
    @processID.setter
    def processID(self, processID: int):
        self.__processID = processID

    @property
    def hard_Drive23(self):
        return self.__hard_Drive23
    @hard_Drive23.setter
    def hard_Drive23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Request__hard_Drive23", None)
        self.__hard_Drive23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "request22"):
                opp_val = getattr(old_value, "request22", None)
                if opp_val == self:
                    setattr(old_value, "request22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "request22"):
                opp_val = getattr(value, "request22", None)
                setattr(value, "request22", self)



class JLabel:

    pass


class JScrollPane:

    pass


class JTable:

    pass


class JTextArea:

    pass


class Font:

    pass


class JTextField:

    pass


class JFrame:

    pass


class ProgramFileData:

    def __init__(self, name: str, memory: int, instructions: ArrayList_Instruction_, instruction20: "Instruction_Interface" = None):
        self.name = name
        self.memory = memory
        self.instructions = instructions
        self.instruction20 = instruction20
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory: int):
        self.__memory = memory

    @property
    def instructions(self):
        return self.__instructions
    @instructions.setter
    def instructions(self, instructions: ArrayList_Instruction_):
        self.__instructions = instructions

    @property
    def instruction20(self):
        return self.__instruction20
    @instruction20.setter
    def instruction20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProgramFileData__instruction20", None)
        self.__instruction20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programFileData21"):
                opp_val = getattr(old_value, "programFileData21", None)
                if opp_val == self:
                    setattr(old_value, "programFileData21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programFileData21"):
                opp_val = getattr(value, "programFileData21", None)
                setattr(value, "programFileData21", self)



class ProcessData:

    def __init__(self, name: str, startTime: str, instructions: ArrayList_Instruction_, memory: int, instruction5: "Instruction_Interface" = None):
        self.name = name
        self.startTime = startTime
        self.instructions = instructions
        self.memory = memory
        self.instruction5 = instruction5
        
        pass
    @property
    def instructions(self):
        return self.__instructions
    @instructions.setter
    def instructions(self, instructions: ArrayList_Instruction_):
        self.__instructions = instructions

    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory: int):
        self.__memory = memory

    @property
    def instruction5(self):
        return self.__instruction5
    @instruction5.setter
    def instruction5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProcessData__instruction5", None)
        self.__instruction5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processData4"):
                opp_val = getattr(old_value, "processData4", None)
                if opp_val == self:
                    setattr(old_value, "processData4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processData4"):
                opp_val = getattr(value, "processData4", None)
                setattr(value, "processData4", self)



class Process:

    def __init__(self, processState: str, registers: str, name: str, memoryUseage: int, task_Manager11: "Task_Manager" = None, exit3: "Exit" = None):
        self.processState = processState
        self.registers = registers
        self.name = name
        self.memoryUseage = memoryUseage
        self.task_Manager11 = task_Manager11
        self.exit3 = exit3
        
        pass
    @property
    def memoryUseage(self):
        return self.__memoryUseage
    @memoryUseage.setter
    def memoryUseage(self, memoryUseage: int):
        self.__memoryUseage = memoryUseage

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def processState(self):
        return self.__processState
    @processState.setter
    def processState(self, processState: str):
        self.__processState = processState

    @property
    def registers(self):
        return self.__registers
    @registers.setter
    def registers(self, registers: str):
        self.__registers = registers

    @property
    def task_Manager11(self):
        return self.__task_Manager11
    @task_Manager11.setter
    def task_Manager11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__task_Manager11", None)
        self.__task_Manager11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process10"):
                opp_val = getattr(old_value, "process10", None)
                if opp_val == self:
                    setattr(old_value, "process10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process10"):
                opp_val = getattr(value, "process10", None)
                setattr(value, "process10", self)

    @property
    def exit3(self):
        return self.__exit3
    @exit3.setter
    def exit3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__exit3", None)
        self.__exit3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process2"):
                opp_val = getattr(old_value, "process2", None)
                if opp_val == self:
                    setattr(old_value, "process2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process2"):
                opp_val = getattr(value, "process2", None)
                setattr(value, "process2", self)



class Object:

    pass


class Class:

    pass


class Prompt:

    def __init__(self, commandLine: JTextField, frameFont: Font, output: JTextArea, FONT_SIZE: int, operating_System7: "Operating_System" = None):
        self.commandLine = commandLine
        self.frameFont = frameFont
        self.output = output
        self.FONT_SIZE = FONT_SIZE
        self.operating_System7 = operating_System7
        
        pass
    @property
    def FONT_SIZE(self):
        return self.__FONT_SIZE
    @FONT_SIZE.setter
    def FONT_SIZE(self, FONT_SIZE: int):
        self.__FONT_SIZE = FONT_SIZE

    @property
    def output(self):
        return self.__output
    @output.setter
    def output(self, output: JTextArea):
        self.__output = output

    @property
    def frameFont(self):
        return self.__frameFont
    @frameFont.setter
    def frameFont(self, frameFont: Font):
        self.__frameFont = frameFont

    @property
    def commandLine(self):
        return self.__commandLine
    @commandLine.setter
    def commandLine(self, commandLine: JTextField):
        self.__commandLine = commandLine

    @property
    def operating_System7(self):
        return self.__operating_System7
    @operating_System7.setter
    def operating_System7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prompt__operating_System7", None)
        self.__operating_System7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prompt6"):
                opp_val = getattr(old_value, "prompt6", None)
                if opp_val == self:
                    setattr(old_value, "prompt6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prompt6"):
                opp_val = getattr(value, "prompt6", None)
                setattr(value, "prompt6", self)



class Hard_Drive:

    def __init__(self, memory: str, operating_System19: "Operating_System" = None, request22: "Request" = None):
        self.memory = memory
        self.operating_System19 = operating_System19
        self.request22 = request22
        
        pass
    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory: str):
        self.__memory = memory

    @property
    def request22(self):
        return self.__request22
    @request22.setter
    def request22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hard_Drive__request22", None)
        self.__request22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hard_Drive23"):
                opp_val = getattr(old_value, "hard_Drive23", None)
                if opp_val == self:
                    setattr(old_value, "hard_Drive23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hard_Drive23"):
                opp_val = getattr(value, "hard_Drive23", None)
                setattr(value, "hard_Drive23", self)

    @property
    def operating_System19(self):
        return self.__operating_System19
    @operating_System19.setter
    def operating_System19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hard_Drive__operating_System19", None)
        self.__operating_System19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hard_Drive18"):
                opp_val = getattr(old_value, "hard_Drive18", None)
                if opp_val == self:
                    setattr(old_value, "hard_Drive18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hard_Drive18"):
                opp_val = getattr(value, "hard_Drive18", None)
                setattr(value, "hard_Drive18", self)



class Memory:

    def __init__(self, memory: Memory__, table: Page__, operating_System17: "Operating_System" = None):
        self.memory = memory
        self.table = table
        self.operating_System17 = operating_System17
        
        pass
    @property
    def table(self):
        return self.__table
    @table.setter
    def table(self, table: Page__):
        self.__table = table

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory: Memory__):
        self.__memory = memory

    @property
    def operating_System17(self):
        return self.__operating_System17
    @operating_System17.setter
    def operating_System17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Memory__operating_System17", None)
        self.__operating_System17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memory16"):
                opp_val = getattr(old_value, "memory16", None)
                if opp_val == self:
                    setattr(old_value, "memory16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memory16"):
                opp_val = getattr(value, "memory16", None)
                setattr(value, "memory16", self)



class CPU:

    def __init__(self, registers: str, operating_System15: "Operating_System" = None):
        self.registers = registers
        self.operating_System15 = operating_System15
        
        pass
    @property
    def registers(self):
        return self.__registers
    @registers.setter
    def registers(self, registers: str):
        self.__registers = registers

    @property
    def operating_System15(self):
        return self.__operating_System15
    @operating_System15.setter
    def operating_System15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CPU__operating_System15", None)
        self.__operating_System15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cPU14"):
                opp_val = getattr(old_value, "cPU14", None)
                if opp_val == self:
                    setattr(old_value, "cPU14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cPU14"):
                opp_val = getattr(value, "cPU14", None)
                setattr(value, "cPU14", self)



class Clock:

    def __init__(self, clockCycle: int, operating_System13: "Operating_System" = None):
        self.clockCycle = clockCycle
        self.operating_System13 = operating_System13
        
        pass
    @property
    def clockCycle(self):
        return self.__clockCycle
    @clockCycle.setter
    def clockCycle(self, clockCycle: int):
        self.__clockCycle = clockCycle

    @property
    def operating_System13(self):
        return self.__operating_System13
    @operating_System13.setter
    def operating_System13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Clock__operating_System13", None)
        self.__operating_System13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clock12"):
                opp_val = getattr(old_value, "clock12", None)
                if opp_val == self:
                    setattr(old_value, "clock12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clock12"):
                opp_val = getattr(value, "clock12", None)
                setattr(value, "clock12", self)



class Operating_System:

    def __init__(self, clock: Clock, cpu: CPU, memory: Memory, hardDrive: Hard_Drive, prompt: Prompt, taskManager: Task_Manager, exit1: "Exit" = None, prompt6: "Prompt" = None, task_Manager8: "Task_Manager" = None, clock12: "Clock" = None, cPU14: "CPU" = None, memory16: "Memory" = None, hard_Drive18: "Hard_Drive" = None):
        self.clock = clock
        self.cpu = cpu
        self.memory = memory
        self.hardDrive = hardDrive
        self.prompt = prompt
        self.taskManager = taskManager
        self.exit1 = exit1
        self.prompt6 = prompt6
        self.task_Manager8 = task_Manager8
        self.clock12 = clock12
        self.cPU14 = cPU14
        self.memory16 = memory16
        self.hard_Drive18 = hard_Drive18
        
        pass
    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu: CPU):
        self.__cpu = cpu

    @property
    def clock(self):
        return self.__clock
    @clock.setter
    def clock(self, clock: Clock):
        self.__clock = clock

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory: Memory):
        self.__memory = memory

    @property
    def prompt(self):
        return self.__prompt
    @prompt.setter
    def prompt(self, prompt: Prompt):
        self.__prompt = prompt

    @property
    def taskManager(self):
        return self.__taskManager
    @taskManager.setter
    def taskManager(self, taskManager: Task_Manager):
        self.__taskManager = taskManager

    @property
    def hardDrive(self):
        return self.__hardDrive
    @hardDrive.setter
    def hardDrive(self, hardDrive: Hard_Drive):
        self.__hardDrive = hardDrive

    @property
    def prompt6(self):
        return self.__prompt6
    @prompt6.setter
    def prompt6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__prompt6", None)
        self.__prompt6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System7"):
                opp_val = getattr(old_value, "operating_System7", None)
                if opp_val == self:
                    setattr(old_value, "operating_System7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System7"):
                opp_val = getattr(value, "operating_System7", None)
                setattr(value, "operating_System7", self)

    @property
    def hard_Drive18(self):
        return self.__hard_Drive18
    @hard_Drive18.setter
    def hard_Drive18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__hard_Drive18", None)
        self.__hard_Drive18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System19"):
                opp_val = getattr(old_value, "operating_System19", None)
                if opp_val == self:
                    setattr(old_value, "operating_System19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System19"):
                opp_val = getattr(value, "operating_System19", None)
                setattr(value, "operating_System19", self)

    @property
    def exit1(self):
        return self.__exit1
    @exit1.setter
    def exit1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__exit1", None)
        self.__exit1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System0"):
                opp_val = getattr(old_value, "operating_System0", None)
                if opp_val == self:
                    setattr(old_value, "operating_System0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System0"):
                opp_val = getattr(value, "operating_System0", None)
                setattr(value, "operating_System0", self)

    @property
    def clock12(self):
        return self.__clock12
    @clock12.setter
    def clock12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__clock12", None)
        self.__clock12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System13"):
                opp_val = getattr(old_value, "operating_System13", None)
                if opp_val == self:
                    setattr(old_value, "operating_System13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System13"):
                opp_val = getattr(value, "operating_System13", None)
                setattr(value, "operating_System13", self)

    @property
    def task_Manager8(self):
        return self.__task_Manager8
    @task_Manager8.setter
    def task_Manager8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__task_Manager8", None)
        self.__task_Manager8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System9"):
                opp_val = getattr(old_value, "operating_System9", None)
                if opp_val == self:
                    setattr(old_value, "operating_System9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System9"):
                opp_val = getattr(value, "operating_System9", None)
                setattr(value, "operating_System9", self)

    @property
    def cPU14(self):
        return self.__cPU14
    @cPU14.setter
    def cPU14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__cPU14", None)
        self.__cPU14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System15"):
                opp_val = getattr(old_value, "operating_System15", None)
                if opp_val == self:
                    setattr(old_value, "operating_System15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System15"):
                opp_val = getattr(value, "operating_System15", None)
                setattr(value, "operating_System15", self)

    @property
    def memory16(self):
        return self.__memory16
    @memory16.setter
    def memory16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__memory16", None)
        self.__memory16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System17"):
                opp_val = getattr(old_value, "operating_System17", None)
                if opp_val == self:
                    setattr(old_value, "operating_System17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System17"):
                opp_val = getattr(value, "operating_System17", None)
                setattr(value, "operating_System17", self)

