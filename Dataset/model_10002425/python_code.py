from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Page__(Enum):
    pass
class ArrayList_Interrupter_(Enum):
    pass
class ProcessState(Enum):
    pass
class Memory__(Enum):
    pass
class ArrayList_ProcessData_(Enum):
    pass
class ArrayList_Instruction_(Enum):
    pass
class ArrayList_Integer_(Enum):
    pass

############################################
# Definition of Classes
############################################










class Task_Manager:

    def __init__(self, contactTable: JTable, scrollPane: JScrollPane, numberOfProcesses: JLabel, amountofFreeMemory: JLabel, amountofUsedMemory: JLabel, operating_System23: "Operating_System" = None, process24: "Process" = None):
        self.contactTable = contactTable
        self.scrollPane = scrollPane
        self.numberOfProcesses = numberOfProcesses
        self.amountofFreeMemory = amountofFreeMemory
        self.amountofUsedMemory = amountofUsedMemory
        self.operating_System23 = operating_System23
        self.process24 = process24
        
        pass
    @property
    def amountofFreeMemory(self):
        return self.__amountofFreeMemory
    @amountofFreeMemory.setter
    def amountofFreeMemory(self, amountofFreeMemory: JLabel):
        self.__amountofFreeMemory = amountofFreeMemory

    @property
    def contactTable(self):
        return self.__contactTable
    @contactTable.setter
    def contactTable(self, contactTable: JTable):
        self.__contactTable = contactTable

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
    def amountofUsedMemory(self):
        return self.__amountofUsedMemory
    @amountofUsedMemory.setter
    def amountofUsedMemory(self, amountofUsedMemory: JLabel):
        self.__amountofUsedMemory = amountofUsedMemory

    @property
    def process24(self):
        return self.__process24
    @process24.setter
    def process24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task_Manager__process24", None)
        self.__process24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task_Manager25"):
                opp_val = getattr(old_value, "task_Manager25", None)
                if opp_val == self:
                    setattr(old_value, "task_Manager25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task_Manager25"):
                opp_val = getattr(value, "task_Manager25", None)
                setattr(value, "task_Manager25", self)

    @property
    def operating_System23(self):
        return self.__operating_System23
    @operating_System23.setter
    def operating_System23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task_Manager__operating_System23", None)
        self.__operating_System23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task_Manager22"):
                opp_val = getattr(old_value, "task_Manager22", None)
                if opp_val == self:
                    setattr(old_value, "task_Manager22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task_Manager22"):
                opp_val = getattr(value, "task_Manager22", None)
                setattr(value, "task_Manager22", self)



class AbstractTableModel:

    pass


class ProcessTableModel:

    def __init__(self, columnNames: str, processList: str, numberProcesses: int, operating_System16: "Operating_System" = None, process18: "Process" = None):
        self.columnNames = columnNames
        self.processList = processList
        self.numberProcesses = numberProcesses
        self.operating_System16 = operating_System16
        self.process18 = process18
        
        pass
    @property
    def columnNames(self):
        return self.__columnNames
    @columnNames.setter
    def columnNames(self, columnNames: str):
        self.__columnNames = columnNames

    @property
    def numberProcesses(self):
        return self.__numberProcesses
    @numberProcesses.setter
    def numberProcesses(self, numberProcesses: int):
        self.__numberProcesses = numberProcesses

    @property
    def processList(self):
        return self.__processList
    @processList.setter
    def processList(self, processList: str):
        self.__processList = processList

    @property
    def process18(self):
        return self.__process18
    @process18.setter
    def process18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProcessTableModel__process18", None)
        self.__process18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processTableModel19"):
                opp_val = getattr(old_value, "processTableModel19", None)
                if opp_val == self:
                    setattr(old_value, "processTableModel19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processTableModel19"):
                opp_val = getattr(value, "processTableModel19", None)
                setattr(value, "processTableModel19", self)

    @property
    def operating_System16(self):
        return self.__operating_System16
    @operating_System16.setter
    def operating_System16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProcessTableModel__operating_System16", None)
        self.__operating_System16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processTableModel17"):
                opp_val = getattr(old_value, "processTableModel17", None)
                if opp_val == self:
                    setattr(old_value, "processTableModel17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processTableModel17"):
                opp_val = getattr(value, "processTableModel17", None)
                setattr(value, "processTableModel17", self)



class Main:

    pass


class Instruction_Print:

    pass


class Instruction_OpenBracket:

    pass


class Instruction_IncrementValue:

    pass


class Instruction_IncrementPointer:

    pass


class Instruction_DecrementValue:

    pass


class Instruction_CloseBracket:

    pass


class Instruction_DecrementPointer:

    pass


class Instruction_Yield:

    pass


class Instruction_Instruction_Interface:

    pass


class Instruction_Exit:

    pass


class Instruction_IO:

    pass


class Instruction_Calculate:

    def __init__(self, time: int, operating_System10: "Operating_System" = None):
        self.time = time
        self.operating_System10 = operating_System10
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def operating_System10(self):
        return self.__operating_System10
    @operating_System10.setter
    def operating_System10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Instruction_Calculate__operating_System10", None)
        self.__operating_System10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculate11"):
                opp_val = getattr(old_value, "calculate11", None)
                if opp_val == self:
                    setattr(old_value, "calculate11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculate11"):
                opp_val = getattr(value, "calculate11", None)
                setattr(value, "calculate11", self)



class Instruction_Out:

    pass


class ArrayList_ProgramFileData_:

    pass


class JobFileData:

    def __init__(self, programs: ArrayList_ProgramFileData_, startTimes: ArrayList_Integer_, programFileData46: "ProgramFileData" = None):
        self.programs = programs
        self.startTimes = startTimes
        self.programFileData46 = programFileData46
        
        pass
    @property
    def programs(self):
        return self.__programs
    @programs.setter
    def programs(self, programs: ArrayList_ProgramFileData_):
        self.__programs = programs

    @property
    def startTimes(self):
        return self.__startTimes
    @startTimes.setter
    def startTimes(self, startTimes: ArrayList_Integer_):
        self.__startTimes = startTimes

    @property
    def programFileData46(self):
        return self.__programFileData46
    @programFileData46.setter
    def programFileData46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JobFileData__programFileData46", None)
        self.__programFileData46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jobFileData47"):
                opp_val = getattr(old_value, "jobFileData47", None)
                if opp_val == self:
                    setattr(old_value, "jobFileData47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jobFileData47"):
                opp_val = getattr(value, "jobFileData47", None)
                setattr(value, "jobFileData47", self)



class Request:

    def __init__(self, startAddress: int, endAddress: int, processID: int, hard_Drive49: "Hard_Drive" = None):
        self.startAddress = startAddress
        self.endAddress = endAddress
        self.processID = processID
        self.hard_Drive49 = hard_Drive49
        
        pass
    @property
    def processID(self):
        return self.__processID
    @processID.setter
    def processID(self, processID: int):
        self.__processID = processID

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
    def hard_Drive49(self):
        return self.__hard_Drive49
    @hard_Drive49.setter
    def hard_Drive49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Request__hard_Drive49", None)
        self.__hard_Drive49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "request48"):
                opp_val = getattr(old_value, "request48", None)
                if opp_val == self:
                    setattr(old_value, "request48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "request48"):
                opp_val = getattr(value, "request48", None)
                setattr(value, "request48", self)



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

    def __init__(self, name: str, memory: int, instructions: ArrayList_Instruction_, instruction44: "Instruction_Instruction_Interface" = None, jobFileData47: "JobFileData" = None):
        self.name = name
        self.memory = memory
        self.instructions = instructions
        self.instruction44 = instruction44
        self.jobFileData47 = jobFileData47
        
        pass
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
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def instruction44(self):
        return self.__instruction44
    @instruction44.setter
    def instruction44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProgramFileData__instruction44", None)
        self.__instruction44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programFileData45"):
                opp_val = getattr(old_value, "programFileData45", None)
                if opp_val == self:
                    setattr(old_value, "programFileData45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programFileData45"):
                opp_val = getattr(value, "programFileData45", None)
                setattr(value, "programFileData45", self)

    @property
    def jobFileData47(self):
        return self.__jobFileData47
    @jobFileData47.setter
    def jobFileData47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProgramFileData__jobFileData47", None)
        self.__jobFileData47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programFileData46"):
                opp_val = getattr(old_value, "programFileData46", None)
                if opp_val == self:
                    setattr(old_value, "programFileData46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programFileData46"):
                opp_val = getattr(value, "programFileData46", None)
                setattr(value, "programFileData46", self)



class ProcessData:

    def __init__(self, name: str, startTime: str, instructions: ArrayList_Instruction_, memory: int, instruction15: "Instruction_Instruction_Interface" = None):
        self.name = name
        self.startTime = startTime
        self.instructions = instructions
        self.memory = memory
        self.instruction15 = instruction15
        
        pass
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
    def instruction15(self):
        return self.__instruction15
    @instruction15.setter
    def instruction15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProcessData__instruction15", None)
        self.__instruction15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processData14"):
                opp_val = getattr(old_value, "processData14", None)
                if opp_val == self:
                    setattr(old_value, "processData14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processData14"):
                opp_val = getattr(value, "processData14", None)
                setattr(value, "processData14", self)



class Process:

    def __init__(self, processState: ProcessState, registers: str, name: str, memoryUseage: int, iO5: "Instruction_IO" = None, exit9: "Instruction_Exit" = None, processTableModel19: "ProcessTableModel" = None, task_Manager25: "Task_Manager" = None, page43: "Page" = None):
        self.processState = processState
        self.registers = registers
        self.name = name
        self.memoryUseage = memoryUseage
        self.iO5 = iO5
        self.exit9 = exit9
        self.processTableModel19 = processTableModel19
        self.task_Manager25 = task_Manager25
        self.page43 = page43
        
        pass
    @property
    def registers(self):
        return self.__registers
    @registers.setter
    def registers(self, registers: str):
        self.__registers = registers

    @property
    def processState(self):
        return self.__processState
    @processState.setter
    def processState(self, processState: ProcessState):
        self.__processState = processState

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def memoryUseage(self):
        return self.__memoryUseage
    @memoryUseage.setter
    def memoryUseage(self, memoryUseage: int):
        self.__memoryUseage = memoryUseage

    @property
    def task_Manager25(self):
        return self.__task_Manager25
    @task_Manager25.setter
    def task_Manager25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__task_Manager25", None)
        self.__task_Manager25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process24"):
                opp_val = getattr(old_value, "process24", None)
                if opp_val == self:
                    setattr(old_value, "process24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process24"):
                opp_val = getattr(value, "process24", None)
                setattr(value, "process24", self)

    @property
    def exit9(self):
        return self.__exit9
    @exit9.setter
    def exit9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__exit9", None)
        self.__exit9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process8"):
                opp_val = getattr(old_value, "process8", None)
                if opp_val == self:
                    setattr(old_value, "process8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process8"):
                opp_val = getattr(value, "process8", None)
                setattr(value, "process8", self)

    @property
    def iO5(self):
        return self.__iO5
    @iO5.setter
    def iO5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__iO5", None)
        self.__iO5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process4"):
                opp_val = getattr(old_value, "process4", None)
                if opp_val == self:
                    setattr(old_value, "process4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process4"):
                opp_val = getattr(value, "process4", None)
                setattr(value, "process4", self)

    @property
    def page43(self):
        return self.__page43
    @page43.setter
    def page43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__page43", None)
        self.__page43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process42"):
                opp_val = getattr(old_value, "process42", None)
                if opp_val == self:
                    setattr(old_value, "process42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process42"):
                opp_val = getattr(value, "process42", None)
                setattr(value, "process42", self)

    @property
    def processTableModel19(self):
        return self.__processTableModel19
    @processTableModel19.setter
    def processTableModel19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Process__processTableModel19", None)
        self.__processTableModel19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process18"):
                opp_val = getattr(old_value, "process18", None)
                if opp_val == self:
                    setattr(old_value, "process18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process18"):
                opp_val = getattr(value, "process18", None)
                setattr(value, "process18", self)



class Object:

    pass


class Page:

    def __init__(self, free: bool, owner: Process, attribute: str, process42: "Process" = None, memory51: "Memory" = None):
        self.free = free
        self.owner = owner
        self.attribute = attribute
        self.process42 = process42
        self.memory51 = memory51
        
        pass
    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: Process):
        self.__owner = owner

    @property
    def free(self):
        return self.__free
    @free.setter
    def free(self, free: bool):
        self.__free = free

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def process42(self):
        return self.__process42
    @process42.setter
    def process42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__process42", None)
        self.__process42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page43"):
                opp_val = getattr(old_value, "page43", None)
                if opp_val == self:
                    setattr(old_value, "page43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page43"):
                opp_val = getattr(value, "page43", None)
                setattr(value, "page43", self)

    @property
    def memory51(self):
        return self.__memory51
    @memory51.setter
    def memory51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__memory51", None)
        self.__memory51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page50"):
                opp_val = getattr(old_value, "page50", None)
                if opp_val == self:
                    setattr(old_value, "page50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page50"):
                opp_val = getattr(value, "page50", None)
                setattr(value, "page50", self)



class Interrupter_Interface:

    pass


class Class:

    pass


class Prompt:

    def __init__(self, queuePosition: int, frame: JFrame, commandLine: JTextField, frameFont: Font, output: JTextArea, MAX_COMMAND_LENGTH: int, OUTPUT_HEIGHT: int, OUTPUT_WIDTH: int, FONT_SIZE: int, operating_System21: "Operating_System" = None):
        self.queuePosition = queuePosition
        self.frame = frame
        self.commandLine = commandLine
        self.frameFont = frameFont
        self.output = output
        self.MAX_COMMAND_LENGTH = MAX_COMMAND_LENGTH
        self.OUTPUT_HEIGHT = OUTPUT_HEIGHT
        self.OUTPUT_WIDTH = OUTPUT_WIDTH
        self.FONT_SIZE = FONT_SIZE
        self.operating_System21 = operating_System21
        
        pass
    @property
    def frame(self):
        return self.__frame
    @frame.setter
    def frame(self, frame: JFrame):
        self.__frame = frame

    @property
    def OUTPUT_HEIGHT(self):
        return self.__OUTPUT_HEIGHT
    @OUTPUT_HEIGHT.setter
    def OUTPUT_HEIGHT(self, OUTPUT_HEIGHT: int):
        self.__OUTPUT_HEIGHT = OUTPUT_HEIGHT

    @property
    def OUTPUT_WIDTH(self):
        return self.__OUTPUT_WIDTH
    @OUTPUT_WIDTH.setter
    def OUTPUT_WIDTH(self, OUTPUT_WIDTH: int):
        self.__OUTPUT_WIDTH = OUTPUT_WIDTH

    @property
    def commandLine(self):
        return self.__commandLine
    @commandLine.setter
    def commandLine(self, commandLine: JTextField):
        self.__commandLine = commandLine

    @property
    def MAX_COMMAND_LENGTH(self):
        return self.__MAX_COMMAND_LENGTH
    @MAX_COMMAND_LENGTH.setter
    def MAX_COMMAND_LENGTH(self, MAX_COMMAND_LENGTH: int):
        self.__MAX_COMMAND_LENGTH = MAX_COMMAND_LENGTH

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
    def FONT_SIZE(self):
        return self.__FONT_SIZE
    @FONT_SIZE.setter
    def FONT_SIZE(self, FONT_SIZE: int):
        self.__FONT_SIZE = FONT_SIZE

    @property
    def queuePosition(self):
        return self.__queuePosition
    @queuePosition.setter
    def queuePosition(self, queuePosition: int):
        self.__queuePosition = queuePosition

    @property
    def operating_System21(self):
        return self.__operating_System21
    @operating_System21.setter
    def operating_System21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prompt__operating_System21", None)
        self.__operating_System21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prompt20"):
                opp_val = getattr(old_value, "prompt20", None)
                if opp_val == self:
                    setattr(old_value, "prompt20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prompt20"):
                opp_val = getattr(value, "prompt20", None)
                setattr(value, "prompt20", self)



class Hard_Drive:

    def __init__(self, memory: str, operating_System41: "Operating_System" = None, request48: "Request" = None):
        self.memory = memory
        self.operating_System41 = operating_System41
        self.request48 = request48
        
        pass
    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory: str):
        self.__memory = memory

    @property
    def request48(self):
        return self.__request48
    @request48.setter
    def request48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hard_Drive__request48", None)
        self.__request48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hard_Drive49"):
                opp_val = getattr(old_value, "hard_Drive49", None)
                if opp_val == self:
                    setattr(old_value, "hard_Drive49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hard_Drive49"):
                opp_val = getattr(value, "hard_Drive49", None)
                setattr(value, "hard_Drive49", self)

    @property
    def operating_System41(self):
        return self.__operating_System41
    @operating_System41.setter
    def operating_System41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hard_Drive__operating_System41", None)
        self.__operating_System41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hard_Drive40"):
                opp_val = getattr(old_value, "hard_Drive40", None)
                if opp_val == self:
                    setattr(old_value, "hard_Drive40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hard_Drive40"):
                opp_val = getattr(value, "hard_Drive40", None)
                setattr(value, "hard_Drive40", self)



class IO_Device:

    def __init__(self, counter: int, operating_System39: "Operating_System" = None):
        self.counter = counter
        self.operating_System39 = operating_System39
        
        pass
    @property
    def counter(self):
        return self.__counter
    @counter.setter
    def counter(self, counter: int):
        self.__counter = counter

    @property
    def operating_System39(self):
        return self.__operating_System39
    @operating_System39.setter
    def operating_System39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IO_Device__operating_System39", None)
        self.__operating_System39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iO_Device38"):
                opp_val = getattr(old_value, "iO_Device38", None)
                if opp_val == self:
                    setattr(old_value, "iO_Device38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iO_Device38"):
                opp_val = getattr(value, "iO_Device38", None)
                setattr(value, "iO_Device38", self)



class Scheduler:

    def __init__(self, newQueue: ProcessData, readyQueue: Process, ioQueue: Process, identifier: int, operating_System37: "Operating_System" = None):
        self.newQueue = newQueue
        self.readyQueue = readyQueue
        self.ioQueue = ioQueue
        self.identifier = identifier
        self.operating_System37 = operating_System37
        
        pass
    @property
    def readyQueue(self):
        return self.__readyQueue
    @readyQueue.setter
    def readyQueue(self, readyQueue: Process):
        self.__readyQueue = readyQueue

    @property
    def ioQueue(self):
        return self.__ioQueue
    @ioQueue.setter
    def ioQueue(self, ioQueue: Process):
        self.__ioQueue = ioQueue

    @property
    def identifier(self):
        return self.__identifier
    @identifier.setter
    def identifier(self, identifier: int):
        self.__identifier = identifier

    @property
    def newQueue(self):
        return self.__newQueue
    @newQueue.setter
    def newQueue(self, newQueue: ProcessData):
        self.__newQueue = newQueue

    @property
    def operating_System37(self):
        return self.__operating_System37
    @operating_System37.setter
    def operating_System37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Scheduler__operating_System37", None)
        self.__operating_System37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduler36"):
                opp_val = getattr(old_value, "scheduler36", None)
                if opp_val == self:
                    setattr(old_value, "scheduler36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduler36"):
                opp_val = getattr(value, "scheduler36", None)
                setattr(value, "scheduler36", self)



class Memory:

    def __init__(self, memory: Memory__, table: Page__, operating_System35: "Operating_System" = None, page50: "Page" = None):
        self.memory = memory
        self.table = table
        self.operating_System35 = operating_System35
        self.page50 = page50
        
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
    def page50(self):
        return self.__page50
    @page50.setter
    def page50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Memory__page50", None)
        self.__page50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memory51"):
                opp_val = getattr(old_value, "memory51", None)
                if opp_val == self:
                    setattr(old_value, "memory51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memory51"):
                opp_val = getattr(value, "memory51", None)
                setattr(value, "memory51", self)

    @property
    def operating_System35(self):
        return self.__operating_System35
    @operating_System35.setter
    def operating_System35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Memory__operating_System35", None)
        self.__operating_System35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memory34"):
                opp_val = getattr(old_value, "memory34", None)
                if opp_val == self:
                    setattr(old_value, "memory34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memory34"):
                opp_val = getattr(value, "memory34", None)
                setattr(value, "memory34", self)



class Dispatcher:

    pass


class CPU:

    def __init__(self, registers: str, interruptQueue: ArrayList_Interrupter_, operating_System31: "Operating_System" = None):
        self.registers = registers
        self.interruptQueue = interruptQueue
        self.operating_System31 = operating_System31
        
        pass
    @property
    def interruptQueue(self):
        return self.__interruptQueue
    @interruptQueue.setter
    def interruptQueue(self, interruptQueue: ArrayList_Interrupter_):
        self.__interruptQueue = interruptQueue

    @property
    def registers(self):
        return self.__registers
    @registers.setter
    def registers(self, registers: str):
        self.__registers = registers

    @property
    def operating_System31(self):
        return self.__operating_System31
    @operating_System31.setter
    def operating_System31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CPU__operating_System31", None)
        self.__operating_System31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cPU30"):
                opp_val = getattr(old_value, "cPU30", None)
                if opp_val == self:
                    setattr(old_value, "cPU30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cPU30"):
                opp_val = getattr(value, "cPU30", None)
                setattr(value, "cPU30", self)



class Clock:

    def __init__(self, clockCycle: int, operating_System29: "Operating_System" = None):
        self.clockCycle = clockCycle
        self.operating_System29 = operating_System29
        
        pass
    @property
    def clockCycle(self):
        return self.__clockCycle
    @clockCycle.setter
    def clockCycle(self, clockCycle: int):
        self.__clockCycle = clockCycle

    @property
    def operating_System29(self):
        return self.__operating_System29
    @operating_System29.setter
    def operating_System29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Clock__operating_System29", None)
        self.__operating_System29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clock28"):
                opp_val = getattr(old_value, "clock28", None)
                if opp_val == self:
                    setattr(old_value, "clock28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clock28"):
                opp_val = getattr(value, "clock28", None)
                setattr(value, "clock28", self)



class Operating_System:

    def __init__(self, memory: Memory, scheduler: Scheduler, device: IO_Device, hardDrive: Hard_Drive, prompt: Prompt, taskManager: Task_Manager, MEMORY_SIZE: int, PAGE_SIZE: int, NUMBER_OF_REGISTERS: int, INSTRUCTION_REGISTER: int, PROC_BASE_REGISTER: int, PROC_LIMIT_REGISTER: int, PROCESS_ID_REGISTER: int, PROC_BASE_POINTER: int, PROC_DATA_POINTER: int, QUANTUM: int, clock: Clock, cpu: CPU, dispatcher: Dispatcher, yield1: "Instruction_Yield" = None, iO3: "Instruction_IO" = None, exit7: "Instruction_Exit" = None, calculate11: "Instruction_Calculate" = None, out13: "Instruction_Out" = None, processTableModel17: "ProcessTableModel" = None, prompt20: "Prompt" = None, task_Manager22: "Task_Manager" = None, main26: "Main" = None, clock28: "Clock" = None, cPU30: "CPU" = None, dispatcher32: "Dispatcher" = None, memory34: "Memory" = None, scheduler36: "Scheduler" = None, iO_Device38: "IO_Device" = None, hard_Drive40: "Hard_Drive" = None):
        self.memory = memory
        self.scheduler = scheduler
        self.device = device
        self.hardDrive = hardDrive
        self.prompt = prompt
        self.taskManager = taskManager
        self.MEMORY_SIZE = MEMORY_SIZE
        self.PAGE_SIZE = PAGE_SIZE
        self.NUMBER_OF_REGISTERS = NUMBER_OF_REGISTERS
        self.INSTRUCTION_REGISTER = INSTRUCTION_REGISTER
        self.PROC_BASE_REGISTER = PROC_BASE_REGISTER
        self.PROC_LIMIT_REGISTER = PROC_LIMIT_REGISTER
        self.PROCESS_ID_REGISTER = PROCESS_ID_REGISTER
        self.PROC_BASE_POINTER = PROC_BASE_POINTER
        self.PROC_DATA_POINTER = PROC_DATA_POINTER
        self.QUANTUM = QUANTUM
        self.clock = clock
        self.cpu = cpu
        self.dispatcher = dispatcher
        self.yield1 = yield1
        self.iO3 = iO3
        self.exit7 = exit7
        self.calculate11 = calculate11
        self.out13 = out13
        self.processTableModel17 = processTableModel17
        self.prompt20 = prompt20
        self.task_Manager22 = task_Manager22
        self.main26 = main26
        self.clock28 = clock28
        self.cPU30 = cPU30
        self.dispatcher32 = dispatcher32
        self.memory34 = memory34
        self.scheduler36 = scheduler36
        self.iO_Device38 = iO_Device38
        self.hard_Drive40 = hard_Drive40
        
        pass
    @property
    def PROC_DATA_POINTER(self):
        return self.__PROC_DATA_POINTER
    @PROC_DATA_POINTER.setter
    def PROC_DATA_POINTER(self, PROC_DATA_POINTER: int):
        self.__PROC_DATA_POINTER = PROC_DATA_POINTER

    @property
    def dispatcher(self):
        return self.__dispatcher
    @dispatcher.setter
    def dispatcher(self, dispatcher: Dispatcher):
        self.__dispatcher = dispatcher

    @property
    def PAGE_SIZE(self):
        return self.__PAGE_SIZE
    @PAGE_SIZE.setter
    def PAGE_SIZE(self, PAGE_SIZE: int):
        self.__PAGE_SIZE = PAGE_SIZE

    @property
    def PROC_BASE_REGISTER(self):
        return self.__PROC_BASE_REGISTER
    @PROC_BASE_REGISTER.setter
    def PROC_BASE_REGISTER(self, PROC_BASE_REGISTER: int):
        self.__PROC_BASE_REGISTER = PROC_BASE_REGISTER

    @property
    def PROC_BASE_POINTER(self):
        return self.__PROC_BASE_POINTER
    @PROC_BASE_POINTER.setter
    def PROC_BASE_POINTER(self, PROC_BASE_POINTER: int):
        self.__PROC_BASE_POINTER = PROC_BASE_POINTER

    @property
    def QUANTUM(self):
        return self.__QUANTUM
    @QUANTUM.setter
    def QUANTUM(self, QUANTUM: int):
        self.__QUANTUM = QUANTUM

    @property
    def NUMBER_OF_REGISTERS(self):
        return self.__NUMBER_OF_REGISTERS
    @NUMBER_OF_REGISTERS.setter
    def NUMBER_OF_REGISTERS(self, NUMBER_OF_REGISTERS: int):
        self.__NUMBER_OF_REGISTERS = NUMBER_OF_REGISTERS

    @property
    def prompt(self):
        return self.__prompt
    @prompt.setter
    def prompt(self, prompt: Prompt):
        self.__prompt = prompt

    @property
    def hardDrive(self):
        return self.__hardDrive
    @hardDrive.setter
    def hardDrive(self, hardDrive: Hard_Drive):
        self.__hardDrive = hardDrive

    @property
    def MEMORY_SIZE(self):
        return self.__MEMORY_SIZE
    @MEMORY_SIZE.setter
    def MEMORY_SIZE(self, MEMORY_SIZE: int):
        self.__MEMORY_SIZE = MEMORY_SIZE

    @property
    def scheduler(self):
        return self.__scheduler
    @scheduler.setter
    def scheduler(self, scheduler: Scheduler):
        self.__scheduler = scheduler

    @property
    def INSTRUCTION_REGISTER(self):
        return self.__INSTRUCTION_REGISTER
    @INSTRUCTION_REGISTER.setter
    def INSTRUCTION_REGISTER(self, INSTRUCTION_REGISTER: int):
        self.__INSTRUCTION_REGISTER = INSTRUCTION_REGISTER

    @property
    def taskManager(self):
        return self.__taskManager
    @taskManager.setter
    def taskManager(self, taskManager: Task_Manager):
        self.__taskManager = taskManager

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu: CPU):
        self.__cpu = cpu

    @property
    def device(self):
        return self.__device
    @device.setter
    def device(self, device: IO_Device):
        self.__device = device

    @property
    def PROCESS_ID_REGISTER(self):
        return self.__PROCESS_ID_REGISTER
    @PROCESS_ID_REGISTER.setter
    def PROCESS_ID_REGISTER(self, PROCESS_ID_REGISTER: int):
        self.__PROCESS_ID_REGISTER = PROCESS_ID_REGISTER

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
    def PROC_LIMIT_REGISTER(self):
        return self.__PROC_LIMIT_REGISTER
    @PROC_LIMIT_REGISTER.setter
    def PROC_LIMIT_REGISTER(self, PROC_LIMIT_REGISTER: int):
        self.__PROC_LIMIT_REGISTER = PROC_LIMIT_REGISTER

    @property
    def yield1(self):
        return self.__yield1
    @yield1.setter
    def yield1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__yield1", None)
        self.__yield1 = value
        
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
    def processTableModel17(self):
        return self.__processTableModel17
    @processTableModel17.setter
    def processTableModel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__processTableModel17", None)
        self.__processTableModel17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System16"):
                opp_val = getattr(old_value, "operating_System16", None)
                if opp_val == self:
                    setattr(old_value, "operating_System16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System16"):
                opp_val = getattr(value, "operating_System16", None)
                setattr(value, "operating_System16", self)

    @property
    def clock28(self):
        return self.__clock28
    @clock28.setter
    def clock28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__clock28", None)
        self.__clock28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System29"):
                opp_val = getattr(old_value, "operating_System29", None)
                if opp_val == self:
                    setattr(old_value, "operating_System29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System29"):
                opp_val = getattr(value, "operating_System29", None)
                setattr(value, "operating_System29", self)

    @property
    def iO_Device38(self):
        return self.__iO_Device38
    @iO_Device38.setter
    def iO_Device38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__iO_Device38", None)
        self.__iO_Device38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System39"):
                opp_val = getattr(old_value, "operating_System39", None)
                if opp_val == self:
                    setattr(old_value, "operating_System39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System39"):
                opp_val = getattr(value, "operating_System39", None)
                setattr(value, "operating_System39", self)

    @property
    def prompt20(self):
        return self.__prompt20
    @prompt20.setter
    def prompt20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__prompt20", None)
        self.__prompt20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System21"):
                opp_val = getattr(old_value, "operating_System21", None)
                if opp_val == self:
                    setattr(old_value, "operating_System21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System21"):
                opp_val = getattr(value, "operating_System21", None)
                setattr(value, "operating_System21", self)

    @property
    def exit7(self):
        return self.__exit7
    @exit7.setter
    def exit7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__exit7", None)
        self.__exit7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System6"):
                opp_val = getattr(old_value, "operating_System6", None)
                if opp_val == self:
                    setattr(old_value, "operating_System6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System6"):
                opp_val = getattr(value, "operating_System6", None)
                setattr(value, "operating_System6", self)

    @property
    def hard_Drive40(self):
        return self.__hard_Drive40
    @hard_Drive40.setter
    def hard_Drive40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__hard_Drive40", None)
        self.__hard_Drive40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System41"):
                opp_val = getattr(old_value, "operating_System41", None)
                if opp_val == self:
                    setattr(old_value, "operating_System41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System41"):
                opp_val = getattr(value, "operating_System41", None)
                setattr(value, "operating_System41", self)

    @property
    def task_Manager22(self):
        return self.__task_Manager22
    @task_Manager22.setter
    def task_Manager22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__task_Manager22", None)
        self.__task_Manager22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System23"):
                opp_val = getattr(old_value, "operating_System23", None)
                if opp_val == self:
                    setattr(old_value, "operating_System23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System23"):
                opp_val = getattr(value, "operating_System23", None)
                setattr(value, "operating_System23", self)

    @property
    def main26(self):
        return self.__main26
    @main26.setter
    def main26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__main26", None)
        self.__main26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System27"):
                opp_val = getattr(old_value, "operating_System27", None)
                if opp_val == self:
                    setattr(old_value, "operating_System27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System27"):
                opp_val = getattr(value, "operating_System27", None)
                setattr(value, "operating_System27", self)

    @property
    def scheduler36(self):
        return self.__scheduler36
    @scheduler36.setter
    def scheduler36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__scheduler36", None)
        self.__scheduler36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System37"):
                opp_val = getattr(old_value, "operating_System37", None)
                if opp_val == self:
                    setattr(old_value, "operating_System37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System37"):
                opp_val = getattr(value, "operating_System37", None)
                setattr(value, "operating_System37", self)

    @property
    def out13(self):
        return self.__out13
    @out13.setter
    def out13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__out13", None)
        self.__out13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System12"):
                opp_val = getattr(old_value, "operating_System12", None)
                if opp_val == self:
                    setattr(old_value, "operating_System12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System12"):
                opp_val = getattr(value, "operating_System12", None)
                setattr(value, "operating_System12", self)

    @property
    def cPU30(self):
        return self.__cPU30
    @cPU30.setter
    def cPU30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__cPU30", None)
        self.__cPU30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System31"):
                opp_val = getattr(old_value, "operating_System31", None)
                if opp_val == self:
                    setattr(old_value, "operating_System31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System31"):
                opp_val = getattr(value, "operating_System31", None)
                setattr(value, "operating_System31", self)

    @property
    def memory34(self):
        return self.__memory34
    @memory34.setter
    def memory34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__memory34", None)
        self.__memory34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System35"):
                opp_val = getattr(old_value, "operating_System35", None)
                if opp_val == self:
                    setattr(old_value, "operating_System35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System35"):
                opp_val = getattr(value, "operating_System35", None)
                setattr(value, "operating_System35", self)

    @property
    def iO3(self):
        return self.__iO3
    @iO3.setter
    def iO3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__iO3", None)
        self.__iO3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System2"):
                opp_val = getattr(old_value, "operating_System2", None)
                if opp_val == self:
                    setattr(old_value, "operating_System2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System2"):
                opp_val = getattr(value, "operating_System2", None)
                setattr(value, "operating_System2", self)

    @property
    def calculate11(self):
        return self.__calculate11
    @calculate11.setter
    def calculate11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__calculate11", None)
        self.__calculate11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System10"):
                opp_val = getattr(old_value, "operating_System10", None)
                if opp_val == self:
                    setattr(old_value, "operating_System10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System10"):
                opp_val = getattr(value, "operating_System10", None)
                setattr(value, "operating_System10", self)

    @property
    def dispatcher32(self):
        return self.__dispatcher32
    @dispatcher32.setter
    def dispatcher32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operating_System__dispatcher32", None)
        self.__dispatcher32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operating_System33"):
                opp_val = getattr(old_value, "operating_System33", None)
                if opp_val == self:
                    setattr(old_value, "operating_System33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operating_System33"):
                opp_val = getattr(value, "operating_System33", None)
                setattr(value, "operating_System33", self)

