from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    blue = "blue"
    red = "red"
    white = "white"
class Time(Enum):
    MilliSecond = "MilliSecond"
    MicroSecond = "MicroSecond"
class BinaryBooleanOperatorKind(Enum):
    inf = "inf"
    sup = "sup"
    infOrEqual = "infOrEqual"
    supOrEqual = "supOrEqual"
    equal = "equal"
    and = "and"
    or = "or"
    Different = "Different"
class UnaryBooleanOperatorKind(Enum):
    not = "not"
class BinaryIntegerOperatorKind(Enum):
    minus = "minus"
    plus = "plus"
    mul = "mul"
    div = "div"
    min = "min"
    max = "max"
    pourcent = "pourcent"
class UnaryIntegerOperatorKind(Enum):
    minus = "minus"
    squareRoot = "squareRoot"


############################################
# Definition of Classes
############################################

class ArduinoAnalogModule:

    pass
class arduino_BluetoothTransceiver(ArduinoAnalogModule):

    def __init__(self, dataToSend: str, dataReceived: str, arduino_BluetoothTransceiver: "arduino_BluetoothTransceiver" = None, arduino_BluetoothTransceiver47: set["arduino_BluetoothTransceiver"] = None):
        self.dataToSend = dataToSend
        self.dataReceived = dataReceived
        self.arduino_BluetoothTransceiver = arduino_BluetoothTransceiver
        self.arduino_BluetoothTransceiver47 = arduino_BluetoothTransceiver47 if arduino_BluetoothTransceiver47 is not None else set()
        
    @property
    def dataToSend(self) -> str:
        return self.__dataToSend

    @dataToSend.setter
    def dataToSend(self, dataToSend: str):
        self.__dataToSend = dataToSend

    @property
    def dataReceived(self) -> str:
        return self.__dataReceived

    @dataReceived.setter
    def dataReceived(self, dataReceived: str):
        self.__dataReceived = dataReceived

    @property
    def arduino_BluetoothTransceiver47(self):
        return self.__arduino_BluetoothTransceiver47

    @arduino_BluetoothTransceiver47.setter
    def arduino_BluetoothTransceiver47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_BluetoothTransceiver__arduino_BluetoothTransceiver47", None)
        self.__arduino_BluetoothTransceiver47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_BluetoothTransceiver"):
                    opp_val = getattr(item, "arduino_BluetoothTransceiver", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_BluetoothTransceiver", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_BluetoothTransceiver"):
                    opp_val = getattr(item, "arduino_BluetoothTransceiver", None)
                    
                    setattr(item, "arduino_BluetoothTransceiver", self)
                    

    @property
    def arduino_BluetoothTransceiver(self):
        return self.__arduino_BluetoothTransceiver

    @arduino_BluetoothTransceiver.setter
    def arduino_BluetoothTransceiver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_BluetoothTransceiver__arduino_BluetoothTransceiver", None)
        self.__arduino_BluetoothTransceiver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BluetoothTransceiver47"):
                opp_val = getattr(old_value, "arduino_BluetoothTransceiver47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BluetoothTransceiver47"):
                opp_val = getattr(value, "arduino_BluetoothTransceiver47", None)
                if opp_val is None:
                    setattr(value, "arduino_BluetoothTransceiver47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def push(self):
        # TODO: Implement push method
        pass

class arduino_RotationSensor(ArduinoAnalogModule):

    pass
class ArduinoDigitalModule:

    pass
class arduino_Buzzer(ArduinoDigitalModule):

    pass
class arduino_PushButton(ArduinoDigitalModule):

    pass
class arduino_InfraRedSensor(ArduinoDigitalModule):

    pass
class arduino_MicroServo(ArduinoDigitalModule):

    pass
class arduino_ArduinoCommunicationModule(ArduinoDigitalModule):

    def __init__(self):
        
    def push(self):
        # TODO: Implement push method
        pass

class arduino_LED(ArduinoDigitalModule):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class VariableRef:

    pass
class UnaryExpression:

    pass
class ArduinoModule:

    pass
class Board:

    pass
class arduino_ArduinoBoard(Board):

    pass
class Module:

    pass
class arduino_ArduinoModule(Module):

    pass
class arduino_MusicPlayer(ArduinoAnalogModule):

    pass
class arduino_Fan(ArduinoDigitalModule):

    pass
class arduino_SoundSensor(ArduinoAnalogModule):

    pass
class arduino_AmbientLightSensor(ArduinoAnalogModule):

    pass
class Variable:

    pass
class arduino_BooleanVariable(Variable):

    def __init__(self, value: str, initialValue: bool, arduino_BooleanVariable: "arduino_BooleanVariableRef" = None):
        self.value = value
        self.initialValue = initialValue
        self.arduino_BooleanVariable = arduino_BooleanVariable
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def initialValue(self) -> bool:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: bool):
        self.__initialValue = initialValue

    @property
    def arduino_BooleanVariable(self):
        return self.__arduino_BooleanVariable

    @arduino_BooleanVariable.setter
    def arduino_BooleanVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_BooleanVariable__arduino_BooleanVariable", None)
        self.__arduino_BooleanVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BooleanVariableRef"):
                opp_val = getattr(old_value, "arduino_BooleanVariableRef", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BooleanVariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BooleanVariableRef"):
                opp_val = getattr(value, "arduino_BooleanVariableRef", None)
                setattr(value, "arduino_BooleanVariableRef", self)

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_IntegerVariable(Variable):

    def __init__(self, initialValue: int, value: str, arduino_IntegerVariable: "arduino_IntegerVariableRef" = None):
        self.initialValue = initialValue
        self.value = value
        self.arduino_IntegerVariable = arduino_IntegerVariable
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def initialValue(self) -> int:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue

    @property
    def arduino_IntegerVariable(self):
        return self.__arduino_IntegerVariable

    @arduino_IntegerVariable.setter
    def arduino_IntegerVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_IntegerVariable__arduino_IntegerVariable", None)
        self.__arduino_IntegerVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_IntegerVariableRef"):
                opp_val = getattr(old_value, "arduino_IntegerVariableRef", None)
                if opp_val == self:
                    setattr(old_value, "arduino_IntegerVariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_IntegerVariableRef"):
                opp_val = getattr(value, "arduino_IntegerVariableRef", None)
                setattr(value, "arduino_IntegerVariableRef", self)

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class Constant:

    pass
class ModuleGet:

    pass
class IntegerExpression:

    pass
class arduino_UnaryIntegerExpression(UnaryExpression, IntegerExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_IntegerModuleGet(ModuleGet, IntegerExpression):

    def __init__(self):
        
    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_IntegerVariableRef(VariableRef, IntegerExpression):

    pass
class arduino_IntegerConstant(Constant, IntegerExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class BinaryExpression:

    pass
class arduino_BinaryIntegerExpression(BinaryExpression, IntegerExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_Expression(ABC):

    def __init__(self, arduino_Expression: "arduino_BinaryExpression" = None, arduino_Expression25: "arduino_BinaryExpression" = None, arduino_Expression33: "arduino_Assignment" = None, arduino_Expression35: "arduino_UnaryExpression" = None):
        self.arduino_Expression = arduino_Expression
        self.arduino_Expression25 = arduino_Expression25
        self.arduino_Expression33 = arduino_Expression33
        self.arduino_Expression35 = arduino_Expression35
        
    @property
    def arduino_Expression25(self):
        return self.__arduino_Expression25

    @arduino_Expression25.setter
    def arduino_Expression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression25", None)
        self.__arduino_Expression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BinaryExpression24"):
                opp_val = getattr(old_value, "arduino_BinaryExpression24", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BinaryExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BinaryExpression24"):
                opp_val = getattr(value, "arduino_BinaryExpression24", None)
                setattr(value, "arduino_BinaryExpression24", self)

    @property
    def arduino_Expression33(self):
        return self.__arduino_Expression33

    @arduino_Expression33.setter
    def arduino_Expression33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression33", None)
        self.__arduino_Expression33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Assignment"):
                opp_val = getattr(old_value, "arduino_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Assignment"):
                opp_val = getattr(value, "arduino_Assignment", None)
                setattr(value, "arduino_Assignment", self)

    @property
    def arduino_Expression(self):
        return self.__arduino_Expression

    @arduino_Expression.setter
    def arduino_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression", None)
        self.__arduino_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BinaryExpression"):
                opp_val = getattr(old_value, "arduino_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BinaryExpression"):
                opp_val = getattr(value, "arduino_BinaryExpression", None)
                setattr(value, "arduino_BinaryExpression", self)

    @property
    def arduino_Expression35(self):
        return self.__arduino_Expression35

    @arduino_Expression35.setter
    def arduino_Expression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression35", None)
        self.__arduino_Expression35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_UnaryExpression"):
                opp_val = getattr(old_value, "arduino_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "arduino_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_UnaryExpression"):
                opp_val = getattr(value, "arduino_UnaryExpression", None)
                setattr(value, "arduino_UnaryExpression", self)

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class Utilities:

    pass
class arduino_Delay(Utilities):

    def __init__(self, unit: str, value: int):
        self.unit = unit
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    def execute(self):
        # TODO: Implement execute method
        pass

class Expression:

    pass
class arduino_BooleanExpression(Expression):

    pass
class arduino_UnaryExpression(Expression):

    pass
class arduino_IntegerExpression(Expression):

    pass
class arduino_BinaryExpression(Expression):

    pass
class arduino_VariableRef(Expression):

    def __init__(self):
        
    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_ModuleGet(Expression):

    pass
class arduino_Constant(Expression):

    def __init__(self):
        
    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class BooleanExpression:

    pass
class arduino_BooleanConstant(Constant, BooleanExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_BooleanVariableRef(VariableRef, BooleanExpression):

    pass
class arduino_BooleanModuleGet(ModuleGet, BooleanExpression):

    def __init__(self):
        
    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_UnaryBooleanExpression(UnaryExpression, BooleanExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class Instruction:

    pass
class arduino_Utilities(Instruction):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Control(Instruction):

    def __init__(self, arduino_Control: "arduino_Block" = None):
        self.arduino_Control = arduino_Control
        
    @property
    def arduino_Control(self):
        return self.__arduino_Control

    @arduino_Control.setter
    def arduino_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Control__arduino_Control", None)
        self.__arduino_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Block18"):
                opp_val = getattr(old_value, "arduino_Block18", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Block18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block18"):
                opp_val = getattr(value, "arduino_Block18", None)
                setattr(value, "arduino_Block18", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Assignment(Instruction):

    pass
class arduino_VariableDeclaration(Instruction):

    def __init__(self, arduino_VariableDeclaration: "arduino_Variable" = None):
        self.arduino_VariableDeclaration = arduino_VariableDeclaration
        
    @property
    def arduino_VariableDeclaration(self):
        return self.__arduino_VariableDeclaration

    @arduino_VariableDeclaration.setter
    def arduino_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_VariableDeclaration__arduino_VariableDeclaration", None)
        self.__arduino_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Variable37"):
                opp_val = getattr(old_value, "arduino_Variable37", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Variable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Variable37"):
                opp_val = getattr(value, "arduino_Variable37", None)
                setattr(value, "arduino_Variable37", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_BinaryBooleanExpression(BinaryExpression, BooleanExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_ModuleInstruction(Instruction):

    def __init__(self, arduino_ModuleInstruction: "arduino_Module" = None):
        self.arduino_ModuleInstruction = arduino_ModuleInstruction
        
    @property
    def arduino_ModuleInstruction(self):
        return self.__arduino_ModuleInstruction

    @arduino_ModuleInstruction.setter
    def arduino_ModuleInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_ModuleInstruction__arduino_ModuleInstruction", None)
        self.__arduino_ModuleInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Module"):
                opp_val = getattr(old_value, "arduino_Module", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Module"):
                opp_val = getattr(value, "arduino_Module", None)
                setattr(value, "arduino_Module", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class Control:

    pass
class arduino_If(Control):

    def __init__(self, arduino_If: "arduino_BooleanExpression" = None, arduino_If30: "arduino_Block" = None):
        self.arduino_If = arduino_If
        self.arduino_If30 = arduino_If30
        
    @property
    def arduino_If30(self):
        return self.__arduino_If30

    @arduino_If30.setter
    def arduino_If30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_If__arduino_If30", None)
        self.__arduino_If30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Block31"):
                opp_val = getattr(old_value, "arduino_Block31", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Block31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block31"):
                opp_val = getattr(value, "arduino_Block31", None)
                setattr(value, "arduino_Block31", self)

    @property
    def arduino_If(self):
        return self.__arduino_If

    @arduino_If.setter
    def arduino_If(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_If__arduino_If", None)
        self.__arduino_If = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BooleanExpression28"):
                opp_val = getattr(old_value, "arduino_BooleanExpression28", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BooleanExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BooleanExpression28"):
                opp_val = getattr(value, "arduino_BooleanExpression28", None)
                setattr(value, "arduino_BooleanExpression28", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_While(Control):

    def __init__(self, arduino_While: "arduino_BooleanExpression" = None):
        self.arduino_While = arduino_While
        
    @property
    def arduino_While(self):
        return self.__arduino_While

    @arduino_While.setter
    def arduino_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_While__arduino_While", None)
        self.__arduino_While = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BooleanExpression"):
                opp_val = getattr(old_value, "arduino_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BooleanExpression"):
                opp_val = getattr(value, "arduino_BooleanExpression", None)
                setattr(value, "arduino_BooleanExpression", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Repeat(Control):

    def __init__(self, iteration: str):
        self.iteration = iteration
        
    @property
    def iteration(self) -> str:
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: str):
        self.__iteration = iteration

    def finalize(self):
        # TODO: Implement finalize method
        pass

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Pin:

    pass
class arduino_DigitalPin(Pin):

    pass
class arduino_Project:

    def __init__(self, 6: "arduino_Sketch" = None, 11: set["arduino_Board"] = None, 14: set["arduino_Sketch"] = None, 1: "arduino_Board" = None):
        self.6 = 6
        self.11 = 11 if 11 is not None else set()
        self.14 = 14 if 14 is not None else set()
        self.1 = 1
        
    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Project__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Project__14", None)
        self.__14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    if opp_val == self:
                        setattr(item, "15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    setattr(item, "15", self)
                    

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Project__6", None)
        self.__6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "5"):
                opp_val = getattr(old_value, "5", None)
                if opp_val == self:
                    setattr(old_value, "5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "5"):
                opp_val = getattr(value, "5", None)
                setattr(value, "5", self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Project__11", None)
        self.__11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    if opp_val == self:
                        setattr(item, "12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    setattr(item, "12", self)
                    

    def setup(self):
        # TODO: Implement setup method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def initializeModel(self, args: str):
        # TODO: Implement initializeModel method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class NamedElement:

    pass
class arduino_Variable(NamedElement):

    def __init__(self, arduino_Variable: "arduino_VariableAssignment" = None, arduino_Variable37: "arduino_VariableDeclaration" = None):
        self.arduino_Variable = arduino_Variable
        self.arduino_Variable37 = arduino_Variable37
        
    @property
    def arduino_Variable37(self):
        return self.__arduino_Variable37

    @arduino_Variable37.setter
    def arduino_Variable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Variable__arduino_Variable37", None)
        self.__arduino_Variable37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_VariableDeclaration"):
                opp_val = getattr(old_value, "arduino_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "arduino_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_VariableDeclaration"):
                opp_val = getattr(value, "arduino_VariableDeclaration", None)
                setattr(value, "arduino_VariableDeclaration", self)

    @property
    def arduino_Variable(self):
        return self.__arduino_Variable

    @arduino_Variable.setter
    def arduino_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Variable__arduino_Variable", None)
        self.__arduino_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_VariableAssignment"):
                opp_val = getattr(old_value, "arduino_VariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "arduino_VariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_VariableAssignment"):
                opp_val = getattr(value, "arduino_VariableAssignment", None)
                setattr(value, "arduino_VariableAssignment", self)

    def evaluate(self) -> str:
        # TODO: Implement evaluate method
        pass

class arduino_Module(NamedElement):

    pass
class arduino_Board(NamedElement):

    pass
class Assignment:

    pass
class arduino_VariableAssignment(Instruction, Assignment):

    def __init__(self, arduino_VariableAssignment: "arduino_Variable" = None):
        self.arduino_VariableAssignment = arduino_VariableAssignment
        
    @property
    def arduino_VariableAssignment(self):
        return self.__arduino_VariableAssignment

    @arduino_VariableAssignment.setter
    def arduino_VariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_VariableAssignment__arduino_VariableAssignment", None)
        self.__arduino_VariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Variable"):
                opp_val = getattr(old_value, "arduino_Variable", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Variable"):
                opp_val = getattr(value, "arduino_Variable", None)
                setattr(value, "arduino_Variable", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class ModuleInstruction:

    pass
class arduino_ModuleAssignment(ModuleInstruction, Assignment):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Instruction(ABC):

    def __init__(self, arduino_Instruction: "arduino_Block" = None):
        self.arduino_Instruction = arduino_Instruction
        
    @property
    def arduino_Instruction(self):
        return self.__arduino_Instruction

    @arduino_Instruction.setter
    def arduino_Instruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction", None)
        self.__arduino_Instruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Block40"):
                opp_val = getattr(old_value, "arduino_Block40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block40"):
                opp_val = getattr(value, "arduino_Block40", None)
                if opp_val is None:
                    setattr(value, "arduino_Block40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def finalize(self):
        # TODO: Implement finalize method
        pass

class arduino_Block:

    def __init__(self, arduino_Block: "arduino_Sketch" = None, arduino_Block18: "arduino_Control" = None, arduino_Block31: "arduino_If" = None, arduino_Block40: set["arduino_Instruction"] = None):
        self.arduino_Block = arduino_Block
        self.arduino_Block18 = arduino_Block18
        self.arduino_Block31 = arduino_Block31
        self.arduino_Block40 = arduino_Block40 if arduino_Block40 is not None else set()
        
    @property
    def arduino_Block18(self):
        return self.__arduino_Block18

    @arduino_Block18.setter
    def arduino_Block18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block18", None)
        self.__arduino_Block18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Control"):
                opp_val = getattr(old_value, "arduino_Control", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Control", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Control"):
                opp_val = getattr(value, "arduino_Control", None)
                setattr(value, "arduino_Control", self)

    @property
    def arduino_Block40(self):
        return self.__arduino_Block40

    @arduino_Block40.setter
    def arduino_Block40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block40", None)
        self.__arduino_Block40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instruction"):
                    opp_val = getattr(item, "arduino_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instruction"):
                    opp_val = getattr(item, "arduino_Instruction", None)
                    
                    setattr(item, "arduino_Instruction", self)
                    

    @property
    def arduino_Block(self):
        return self.__arduino_Block

    @arduino_Block.setter
    def arduino_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block", None)
        self.__arduino_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch"):
                opp_val = getattr(old_value, "arduino_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch"):
                opp_val = getattr(value, "arduino_Sketch", None)
                setattr(value, "arduino_Sketch", self)

    @property
    def arduino_Block31(self):
        return self.__arduino_Block31

    @arduino_Block31.setter
    def arduino_Block31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block31", None)
        self.__arduino_Block31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_If30"):
                opp_val = getattr(old_value, "arduino_If30", None)
                if opp_val == self:
                    setattr(old_value, "arduino_If30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_If30"):
                opp_val = getattr(value, "arduino_If30", None)
                setattr(value, "arduino_If30", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Sketch(NamedElement):

    pass
class arduino_ArduinoAnalogModule(ArduinoModule):

    pass
class arduino_AnalogPin(Pin):

    pass
class arduino_Pin(NamedElement):

    def __init__(self, level: str):
        self.level = level
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

class arduino_ArduinoDigitalModule(ArduinoModule):

    pass