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
Time: Enumeration = Enumeration(
    name="Time",
    literals={
            EnumerationLiteral(name="MilliSecond"),
			EnumerationLiteral(name="MicroSecond")
    }
)

BinaryIntegerOperatorKind: Enumeration = Enumeration(
    name="BinaryIntegerOperatorKind",
    literals={
            EnumerationLiteral(name="pourcent"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max")
    }
)

BinaryBooleanOperatorKind: Enumeration = Enumeration(
    name="BinaryBooleanOperatorKind",
    literals={
            EnumerationLiteral(name="inf"),
			EnumerationLiteral(name="sup"),
			EnumerationLiteral(name="infOrEqual"),
			EnumerationLiteral(name="supOrEqual"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="and_"),
			EnumerationLiteral(name="or_"),
			EnumerationLiteral(name="Different")
    }
)

UnaryIntegerOperatorKind: Enumeration = Enumeration(
    name="UnaryIntegerOperatorKind",
    literals={
            EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="squareRoot")
    }
)

UnaryBooleanOperatorKind: Enumeration = Enumeration(
    name="UnaryBooleanOperatorKind",
    literals={
            EnumerationLiteral(name="not_")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="white")
    }
)

# Classes
arduino_DigitalPin = Class(name="arduino_DigitalPin")
Pin = Class(name="Pin")
arduino_ArduinoDigitalModule = Class(name="arduino_ArduinoDigitalModule", is_abstract=True)
arduino_Pin = Class(name="arduino_Pin", is_abstract=True)
arduino_AnalogPin = Class(name="arduino_AnalogPin")
arduino_ArduinoAnalogModule = Class(name="arduino_ArduinoAnalogModule", is_abstract=True)
arduino_Sketch = Class(name="arduino_Sketch")
arduino_Block = Class(name="arduino_Block")
arduino_Board = Class(name="arduino_Board", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduino_Project = Class(name="arduino_Project")
arduino_Control = Class(name="arduino_Control", is_abstract=True)
arduino_Module = Class(name="arduino_Module", is_abstract=True)
arduino_Utilities = Class(name="arduino_Utilities", is_abstract=True)
arduino_Delay = Class(name="arduino_Delay")
Utilities = Class(name="Utilities")
arduino_NamedElement = Class(name="arduino_NamedElement", is_abstract=True)
arduino_Repeat = Class(name="arduino_Repeat")
Control = Class(name="Control")
arduino_ModuleGet = Class(name="arduino_ModuleGet", is_abstract=True)
Expression = Class(name="Expression")
arduino_While = Class(name="arduino_While")
arduino_BooleanExpression = Class(name="arduino_BooleanExpression", is_abstract=True)
arduino_BinaryExpression = Class(name="arduino_BinaryExpression", is_abstract=True)
arduino_Expression = Class(name="arduino_Expression", is_abstract=True)
arduino_Instruction = Class(name="arduino_Instruction", is_abstract=True)
arduino_ModuleAssignment = Class(name="arduino_ModuleAssignment")
ModuleInstruction = Class(name="ModuleInstruction")
Assignment = Class(name="Assignment")
arduino_ModuleInstruction = Class(name="arduino_ModuleInstruction", is_abstract=True)
Instruction = Class(name="Instruction")
arduino_Variable = Class(name="arduino_Variable", is_abstract=True)
arduino_VariableAssignment = Class(name="arduino_VariableAssignment")
arduino_BinaryIntegerExpression = Class(name="arduino_BinaryIntegerExpression")
BinaryExpression = Class(name="BinaryExpression")
IntegerExpression = Class(name="IntegerExpression")
arduino_BinaryBooleanExpression = Class(name="arduino_BinaryBooleanExpression")
BooleanExpression = Class(name="BooleanExpression")
arduino_Constant = Class(name="arduino_Constant", is_abstract=True)
arduino_If = Class(name="arduino_If")
arduino_Assignment = Class(name="arduino_Assignment", is_abstract=True)
arduino_IntegerVariable = Class(name="arduino_IntegerVariable")
Variable = Class(name="Variable")
arduino_BooleanVariable = Class(name="arduino_BooleanVariable")
arduino_BooleanModuleGet = Class(name="arduino_BooleanModuleGet")
ModuleGet = Class(name="ModuleGet")
arduino_IntegerModuleGet = Class(name="arduino_IntegerModuleGet")
arduino_UnaryExpression = Class(name="arduino_UnaryExpression", is_abstract=True)
arduino_UnaryBooleanExpression = Class(name="arduino_UnaryBooleanExpression")
UnaryExpression = Class(name="UnaryExpression")
arduino_UnaryIntegerExpression = Class(name="arduino_UnaryIntegerExpression")
arduino_IntegerConstant = Class(name="arduino_IntegerConstant")
Constant = Class(name="Constant")
arduino_BooleanConstant = Class(name="arduino_BooleanConstant")
arduino_IntegerExpression = Class(name="arduino_IntegerExpression", is_abstract=True)
arduino_LED = Class(name="arduino_LED")
ArduinoDigitalModule = Class(name="ArduinoDigitalModule")
arduino_PushButton = Class(name="arduino_PushButton")
arduino_Buzzer = Class(name="arduino_Buzzer")
arduino_RotationSensor = Class(name="arduino_RotationSensor")
ArduinoAnalogModule = Class(name="ArduinoAnalogModule")
arduino_MicroServo = Class(name="arduino_MicroServo")
arduino_InfraRedSensor = Class(name="arduino_InfraRedSensor")
arduino_AmbientLightSensor = Class(name="arduino_AmbientLightSensor")
arduino_SoundSensor = Class(name="arduino_SoundSensor")
arduino_Fan = Class(name="arduino_Fan")
arduino_MusicPlayer = Class(name="arduino_MusicPlayer")
arduino_ArduinoModule = Class(name="arduino_ArduinoModule", is_abstract=True)
Module = Class(name="Module")
arduino_ArduinoBoard = Class(name="arduino_ArduinoBoard")
Board = Class(name="Board")
ArduinoModule = Class(name="ArduinoModule")
arduino_BooleanVariableRef = Class(name="arduino_BooleanVariableRef")
arduino_ArduinoCommunicationModule = Class(name="arduino_ArduinoCommunicationModule", is_abstract=True)
arduino_BluetoothTransceiver = Class(name="arduino_BluetoothTransceiver")
arduino_VariableDeclaration = Class(name="arduino_VariableDeclaration")
arduino_VariableRef = Class(name="arduino_VariableRef", is_abstract=True)
arduino_IntegerVariableRef = Class(name="arduino_IntegerVariableRef")
VariableRef = Class(name="VariableRef")

# arduino_DigitalPin class attributes and methods

# Pin class attributes and methods

# arduino_ArduinoDigitalModule class attributes and methods

# arduino_Pin class attributes and methods
arduino_Pin_level: Property = Property(name="level", type=StringType)
arduino_Pin.attributes={arduino_Pin_level}

# arduino_AnalogPin class attributes and methods

# arduino_ArduinoAnalogModule class attributes and methods

# arduino_Sketch class attributes and methods

# arduino_Block class attributes and methods
arduino_Block_m_execute: Method = Method(name="execute", parameters={})
arduino_Block.methods={arduino_Block_m_execute}

# arduino_Board class attributes and methods

# NamedElement class attributes and methods

# arduino_Project class attributes and methods
arduino_Project_m_execute: Method = Method(name="execute", parameters={})
arduino_Project_m_main: Method = Method(name="main", parameters={})
arduino_Project_m_setup: Method = Method(name="setup", parameters={})
arduino_Project_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='arduino_args', type=StringType)})
arduino_Project.methods={arduino_Project_m_execute, arduino_Project_m_initializeModel, arduino_Project_m_main, arduino_Project_m_setup}

# arduino_Control class attributes and methods
arduino_Control_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_Control_m_execute: Method = Method(name="execute", parameters={})
arduino_Control.methods={arduino_Control_m_evaluate, arduino_Control_m_execute}

# arduino_Module class attributes and methods

# arduino_Utilities class attributes and methods
arduino_Utilities_m_execute: Method = Method(name="execute", parameters={})
arduino_Utilities.methods={arduino_Utilities_m_execute}

# arduino_Delay class attributes and methods
arduino_Delay_unit: Property = Property(name="unit", type=StringType)
arduino_Delay_value: Property = Property(name="value", type=IntegerType)
arduino_Delay_m_execute: Method = Method(name="execute", parameters={})
arduino_Delay.attributes={arduino_Delay_value, arduino_Delay_unit}
arduino_Delay.methods={arduino_Delay_m_execute}

# Utilities class attributes and methods

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_Repeat class attributes and methods
arduino_Repeat_iteration: Property = Property(name="iteration", type=StringType)
arduino_Repeat_m_execute: Method = Method(name="execute", parameters={})
arduino_Repeat_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_Repeat_m_finalize: Method = Method(name="finalize", parameters={})
arduino_Repeat.attributes={arduino_Repeat_iteration}
arduino_Repeat.methods={arduino_Repeat_m_finalize, arduino_Repeat_m_evaluate, arduino_Repeat_m_execute}

# Control class attributes and methods

# arduino_ModuleGet class attributes and methods

# Expression class attributes and methods

# arduino_While class attributes and methods
arduino_While_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_While_m_execute: Method = Method(name="execute", parameters={})
arduino_While.methods={arduino_While_m_evaluate, arduino_While_m_execute}

# arduino_BooleanExpression class attributes and methods

# arduino_BinaryExpression class attributes and methods

# arduino_Expression class attributes and methods
arduino_Expression_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_Expression.methods={arduino_Expression_m_evaluate}

# arduino_Instruction class attributes and methods
arduino_Instruction_m_execute: Method = Method(name="execute", parameters={})
arduino_Instruction_m_finalize: Method = Method(name="finalize", parameters={})
arduino_Instruction.methods={arduino_Instruction_m_execute, arduino_Instruction_m_finalize}

# arduino_ModuleAssignment class attributes and methods
arduino_ModuleAssignment_m_execute: Method = Method(name="execute", parameters={})
arduino_ModuleAssignment.methods={arduino_ModuleAssignment_m_execute}

# ModuleInstruction class attributes and methods

# Assignment class attributes and methods

# arduino_ModuleInstruction class attributes and methods
arduino_ModuleInstruction_m_execute: Method = Method(name="execute", parameters={})
arduino_ModuleInstruction.methods={arduino_ModuleInstruction_m_execute}

# Instruction class attributes and methods

# arduino_Variable class attributes and methods
arduino_Variable_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_Variable.methods={arduino_Variable_m_evaluate}

# arduino_VariableAssignment class attributes and methods
arduino_VariableAssignment_m_execute: Method = Method(name="execute", parameters={})
arduino_VariableAssignment.methods={arduino_VariableAssignment_m_execute}

# arduino_BinaryIntegerExpression class attributes and methods
arduino_BinaryIntegerExpression_operator: Property = Property(name="operator", type=StringType)
arduino_BinaryIntegerExpression_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BinaryIntegerExpression.attributes={arduino_BinaryIntegerExpression_operator}
arduino_BinaryIntegerExpression.methods={arduino_BinaryIntegerExpression_m_evaluate}

# BinaryExpression class attributes and methods

# IntegerExpression class attributes and methods

# arduino_BinaryBooleanExpression class attributes and methods
arduino_BinaryBooleanExpression_operator: Property = Property(name="operator", type=StringType)
arduino_BinaryBooleanExpression_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BinaryBooleanExpression.attributes={arduino_BinaryBooleanExpression_operator}
arduino_BinaryBooleanExpression.methods={arduino_BinaryBooleanExpression_m_evaluate}

# BooleanExpression class attributes and methods

# arduino_Constant class attributes and methods
arduino_Constant_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_Constant.methods={arduino_Constant_m_evaluate}

# arduino_If class attributes and methods
arduino_If_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_If_m_execute: Method = Method(name="execute", parameters={})
arduino_If.methods={arduino_If_m_execute, arduino_If_m_evaluate}

# arduino_Assignment class attributes and methods

# arduino_IntegerVariable class attributes and methods
arduino_IntegerVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
arduino_IntegerVariable_value: Property = Property(name="value", type=StringType)
arduino_IntegerVariable_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_IntegerVariable.attributes={arduino_IntegerVariable_value, arduino_IntegerVariable_initialValue}
arduino_IntegerVariable.methods={arduino_IntegerVariable_m_evaluate}

# Variable class attributes and methods

# arduino_BooleanVariable class attributes and methods
arduino_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
arduino_BooleanVariable_value: Property = Property(name="value", type=StringType)
arduino_BooleanVariable_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BooleanVariable.attributes={arduino_BooleanVariable_value, arduino_BooleanVariable_initialValue}
arduino_BooleanVariable.methods={arduino_BooleanVariable_m_evaluate}

# arduino_BooleanModuleGet class attributes and methods
arduino_BooleanModuleGet_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BooleanModuleGet.methods={arduino_BooleanModuleGet_m_evaluate}

# ModuleGet class attributes and methods

# arduino_IntegerModuleGet class attributes and methods
arduino_IntegerModuleGet_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_IntegerModuleGet.methods={arduino_IntegerModuleGet_m_evaluate}

# arduino_UnaryExpression class attributes and methods

# arduino_UnaryBooleanExpression class attributes and methods
arduino_UnaryBooleanExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryBooleanExpression.attributes={arduino_UnaryBooleanExpression_operator}

# UnaryExpression class attributes and methods

# arduino_UnaryIntegerExpression class attributes and methods
arduino_UnaryIntegerExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryIntegerExpression.attributes={arduino_UnaryIntegerExpression_operator}

# arduino_IntegerConstant class attributes and methods
arduino_IntegerConstant_value: Property = Property(name="value", type=IntegerType)
arduino_IntegerConstant_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_IntegerConstant.attributes={arduino_IntegerConstant_value}
arduino_IntegerConstant.methods={arduino_IntegerConstant_m_evaluate}

# Constant class attributes and methods

# arduino_BooleanConstant class attributes and methods
arduino_BooleanConstant_value: Property = Property(name="value", type=BooleanType)
arduino_BooleanConstant_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BooleanConstant.attributes={arduino_BooleanConstant_value}
arduino_BooleanConstant.methods={arduino_BooleanConstant_m_evaluate}

# arduino_IntegerExpression class attributes and methods

# arduino_LED class attributes and methods
arduino_LED_color: Property = Property(name="color", type=StringType)
arduino_LED.attributes={arduino_LED_color}

# ArduinoDigitalModule class attributes and methods

# arduino_PushButton class attributes and methods

# arduino_Buzzer class attributes and methods

# arduino_RotationSensor class attributes and methods

# ArduinoAnalogModule class attributes and methods

# arduino_MicroServo class attributes and methods

# arduino_InfraRedSensor class attributes and methods

# arduino_AmbientLightSensor class attributes and methods

# arduino_SoundSensor class attributes and methods

# arduino_Fan class attributes and methods

# arduino_MusicPlayer class attributes and methods

# arduino_ArduinoModule class attributes and methods

# Module class attributes and methods

# arduino_ArduinoBoard class attributes and methods

# Board class attributes and methods

# ArduinoModule class attributes and methods

# arduino_BooleanVariableRef class attributes and methods

# arduino_ArduinoCommunicationModule class attributes and methods
arduino_ArduinoCommunicationModule_m_push: Method = Method(name="push", parameters={})
arduino_ArduinoCommunicationModule.methods={arduino_ArduinoCommunicationModule_m_push}

# arduino_BluetoothTransceiver class attributes and methods
arduino_BluetoothTransceiver_dataToSend: Property = Property(name="dataToSend", type=StringType)
arduino_BluetoothTransceiver_dataReceived: Property = Property(name="dataReceived", type=StringType)
arduino_BluetoothTransceiver_m_push: Method = Method(name="push", parameters={})
arduino_BluetoothTransceiver.attributes={arduino_BluetoothTransceiver_dataToSend, arduino_BluetoothTransceiver_dataReceived}
arduino_BluetoothTransceiver.methods={arduino_BluetoothTransceiver_m_push}

# arduino_VariableDeclaration class attributes and methods
arduino_VariableDeclaration_m_execute: Method = Method(name="execute", parameters={})
arduino_VariableDeclaration.methods={arduino_VariableDeclaration_m_execute}

# arduino_VariableRef class attributes and methods
arduino_VariableRef_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_VariableRef.methods={arduino_VariableRef_m_evaluate}

# arduino_IntegerVariableRef class attributes and methods

# VariableRef class attributes and methods

# Relationships
module1: BinaryAssociation = BinaryAssociation(
    name="module1",
    ends={
        Property(name="arduino_ArduinoDigitalModule", type=arduino_DigitalPin, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_DigitalPin", type=arduino_ArduinoDigitalModule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module2: BinaryAssociation = BinaryAssociation(
    name="module2",
    ends={
        Property(name="arduino_ArduinoAnalogModule", type=arduino_AnalogPin, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_AnalogPin", type=arduino_ArduinoAnalogModule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
project3: BinaryAssociation = BinaryAssociation(
    name="project3",
    ends={
        Property(name="Project4", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="sketches", type=arduino_Project, multiplicity=Multiplicity(1, 1))
    }
)
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="arduino_Block", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch", type=arduino_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
board6: BinaryAssociation = BinaryAssociation(
    name="board6",
    ends={
        Property(name="arduino_Board", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch7", type=arduino_Board, multiplicity=Multiplicity(0, 1))
    }
)
module11: BinaryAssociation = BinaryAssociation(
    name="module11",
    ends={
        Property(name="arduino_Module", type=arduino_ModuleInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleInstruction", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
project0: BinaryAssociation = BinaryAssociation(
    name="project0",
    ends={
        Property(name="Project", type=arduino_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="boards", type=arduino_Project, multiplicity=Multiplicity(1, 1))
    }
)
block12: BinaryAssociation = BinaryAssociation(
    name="block12",
    ends={
        Property(name="arduino_Block13", type=arduino_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Control", type=arduino_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
module14: BinaryAssociation = BinaryAssociation(
    name="module14",
    ends={
        Property(name="arduino_Module15", type=arduino_ModuleGet, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleGet", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
condition16: BinaryAssociation = BinaryAssociation(
    name="condition16",
    ends={
        Property(name="arduino_BooleanExpression", type=arduino_While, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_While", type=arduino_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boards8: BinaryAssociation = BinaryAssociation(
    name="boards8",
    ends={
        Property(name="Board", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=arduino_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketches9: BinaryAssociation = BinaryAssociation(
    name="sketches9",
    ends={
        Property(name="Sketch", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project10", type=arduino_Sketch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="arduino_Expression", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable21: BinaryAssociation = BinaryAssociation(
    name="variable21",
    ends={
        Property(name="arduino_Variable", type=arduino_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableAssignment", type=arduino_Variable, multiplicity=Multiplicity(1, 1))
    }
)
condition22: BinaryAssociation = BinaryAssociation(
    name="condition22",
    ends={
        Property(name="arduino_BooleanExpression23", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If", type=arduino_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="arduino_Expression20", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression19", type=arduino_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand27: BinaryAssociation = BinaryAssociation(
    name="operand27",
    ends={
        Property(name="arduino_Expression28", type=arduino_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Assignment", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand29: BinaryAssociation = BinaryAssociation(
    name="operand29",
    ends={
        Property(name="arduino_Expression30", type=arduino_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_UnaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock24: BinaryAssociation = BinaryAssociation(
    name="elseBlock24",
    ends={
        Property(name="arduino_Block26", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If25", type=arduino_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable33: BinaryAssociation = BinaryAssociation(
    name="variable33",
    ends={
        Property(name="arduino_IntegerVariable", type=arduino_IntegerVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_IntegerVariableRef", type=arduino_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
instructions34: BinaryAssociation = BinaryAssociation(
    name="instructions34",
    ends={
        Property(name="arduino_Instruction", type=arduino_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Block35", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
digitalPins36: BinaryAssociation = BinaryAssociation(
    name="digitalPins36",
    ends={
        Property(name="arduino_DigitalPin37", type=arduino_ArduinoBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ArduinoBoard", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
analogPins38: BinaryAssociation = BinaryAssociation(
    name="analogPins38",
    ends={
        Property(name="arduino_AnalogPin40", type=arduino_ArduinoBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ArduinoBoard39", type=arduino_AnalogPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable41: BinaryAssociation = BinaryAssociation(
    name="variable41",
    ends={
        Property(name="arduino_BooleanVariable", type=arduino_BooleanVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BooleanVariableRef", type=arduino_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
connectedTransceiver43: BinaryAssociation = BinaryAssociation(
    name="connectedTransceiver43",
    ends={
        Property(name="arduino_BluetoothTransceiver", type=arduino_BluetoothTransceiver, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BluetoothTransceiver42", type=arduino_BluetoothTransceiver, multiplicity=Multiplicity(0, 9999))
    }
)
variable31: BinaryAssociation = BinaryAssociation(
    name="variable31",
    ends={
        Property(name="arduino_Variable32", type=arduino_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableDeclaration", type=arduino_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_DigitalPin_Pin = Generalization(general=Pin, specific=arduino_DigitalPin)
gen_arduino_Pin_NamedElement = Generalization(general=NamedElement, specific=arduino_Pin)
gen_arduino_AnalogPin_Pin = Generalization(general=Pin, specific=arduino_AnalogPin)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_Board_NamedElement = Generalization(general=NamedElement, specific=arduino_Board)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_Utilities_Instruction = Generalization(general=Instruction, specific=arduino_Utilities)
gen_arduino_Delay_Utilities = Generalization(general=Utilities, specific=arduino_Delay)
gen_arduino_Repeat_Control = Generalization(general=Control, specific=arduino_Repeat)
gen_arduino_ModuleGet_Expression = Generalization(general=Expression, specific=arduino_ModuleGet)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_BinaryExpression_Expression = Generalization(general=Expression, specific=arduino_BinaryExpression)
gen_arduino_ModuleAssignment_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_ModuleAssignment)
gen_arduino_ModuleAssignment_Assignment = Generalization(general=Assignment, specific=arduino_ModuleAssignment)
gen_arduino_ModuleInstruction_Instruction = Generalization(general=Instruction, specific=arduino_ModuleInstruction)
gen_arduino_Variable_NamedElement = Generalization(general=NamedElement, specific=arduino_Variable)
gen_arduino_VariableAssignment_Instruction = Generalization(general=Instruction, specific=arduino_VariableAssignment)
gen_arduino_VariableAssignment_Assignment = Generalization(general=Assignment, specific=arduino_VariableAssignment)
gen_arduino_BinaryIntegerExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BinaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BinaryBooleanExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryBooleanExpression)
gen_arduino_BinaryBooleanExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BinaryBooleanExpression)
gen_arduino_Constant_Expression = Generalization(general=Expression, specific=arduino_Constant)
gen_arduino_If_Control = Generalization(general=Control, specific=arduino_If)
gen_arduino_Assignment_Instruction = Generalization(general=Instruction, specific=arduino_Assignment)
gen_arduino_IntegerVariable_Variable = Generalization(general=Variable, specific=arduino_IntegerVariable)
gen_arduino_BooleanVariable_Variable = Generalization(general=Variable, specific=arduino_BooleanVariable)
gen_arduino_BooleanModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_BooleanModuleGet)
gen_arduino_BooleanModuleGet_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanModuleGet)
gen_arduino_IntegerModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_IntegerModuleGet)
gen_arduino_IntegerModuleGet_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerModuleGet)
gen_arduino_UnaryExpression_Expression = Generalization(general=Expression, specific=arduino_UnaryExpression)
gen_arduino_UnaryBooleanExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=arduino_UnaryBooleanExpression)
gen_arduino_UnaryBooleanExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_UnaryBooleanExpression)
gen_arduino_UnaryIntegerExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=arduino_UnaryIntegerExpression)
gen_arduino_UnaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_UnaryIntegerExpression)
gen_arduino_IntegerConstant_Constant = Generalization(general=Constant, specific=arduino_IntegerConstant)
gen_arduino_IntegerConstant_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerConstant)
gen_arduino_BooleanConstant_Constant = Generalization(general=Constant, specific=arduino_BooleanConstant)
gen_arduino_BooleanConstant_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanConstant)
gen_arduino_BooleanExpression_Expression = Generalization(general=Expression, specific=arduino_BooleanExpression)
gen_arduino_IntegerExpression_Expression = Generalization(general=Expression, specific=arduino_IntegerExpression)
gen_arduino_LED_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_LED)
gen_arduino_PushButton_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_PushButton)
gen_arduino_Buzzer_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_Buzzer)
gen_arduino_RotationSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_RotationSensor)
gen_arduino_MicroServo_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_MicroServo)
gen_arduino_InfraRedSensor_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_InfraRedSensor)
gen_arduino_AmbientLightSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_AmbientLightSensor)
gen_arduino_SoundSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_SoundSensor)
gen_arduino_Fan_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_Fan)
gen_arduino_MusicPlayer_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_MusicPlayer)
gen_arduino_ArduinoModule_Module = Generalization(general=Module, specific=arduino_ArduinoModule)
gen_arduino_ArduinoBoard_Board = Generalization(general=Board, specific=arduino_ArduinoBoard)
gen_arduino_ArduinoDigitalModule_ArduinoModule = Generalization(general=ArduinoModule, specific=arduino_ArduinoDigitalModule)
gen_arduino_ArduinoAnalogModule_ArduinoModule = Generalization(general=ArduinoModule, specific=arduino_ArduinoAnalogModule)
gen_arduino_BooleanVariableRef_VariableRef = Generalization(general=VariableRef, specific=arduino_BooleanVariableRef)
gen_arduino_BooleanVariableRef_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanVariableRef)
gen_arduino_ArduinoCommunicationModule_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_ArduinoCommunicationModule)
gen_arduino_BluetoothTransceiver_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_BluetoothTransceiver)
gen_arduino_VariableDeclaration_Instruction = Generalization(general=Instruction, specific=arduino_VariableDeclaration)
gen_arduino_VariableRef_Expression = Generalization(general=Expression, specific=arduino_VariableRef)
gen_arduino_IntegerVariableRef_VariableRef = Generalization(general=VariableRef, specific=arduino_IntegerVariableRef)
gen_arduino_IntegerVariableRef_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerVariableRef)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_DigitalPin, Pin, arduino_ArduinoDigitalModule, arduino_Pin, arduino_AnalogPin, arduino_ArduinoAnalogModule, arduino_Sketch, arduino_Block, arduino_Board, NamedElement, arduino_Project, arduino_Control, arduino_Module, arduino_Utilities, arduino_Delay, Utilities, arduino_NamedElement, arduino_Repeat, Control, arduino_ModuleGet, Expression, arduino_While, arduino_BooleanExpression, arduino_BinaryExpression, arduino_Expression, arduino_Instruction, arduino_ModuleAssignment, ModuleInstruction, Assignment, arduino_ModuleInstruction, Instruction, arduino_Variable, arduino_VariableAssignment, arduino_BinaryIntegerExpression, BinaryExpression, IntegerExpression, arduino_BinaryBooleanExpression, BooleanExpression, arduino_Constant, arduino_If, arduino_Assignment, arduino_IntegerVariable, Variable, arduino_BooleanVariable, arduino_BooleanModuleGet, ModuleGet, arduino_IntegerModuleGet, arduino_UnaryExpression, arduino_UnaryBooleanExpression, UnaryExpression, arduino_UnaryIntegerExpression, arduino_IntegerConstant, Constant, arduino_BooleanConstant, arduino_IntegerExpression, arduino_LED, ArduinoDigitalModule, arduino_PushButton, arduino_Buzzer, arduino_RotationSensor, ArduinoAnalogModule, arduino_MicroServo, arduino_InfraRedSensor, arduino_AmbientLightSensor, arduino_SoundSensor, arduino_Fan, arduino_MusicPlayer, arduino_ArduinoModule, Module, arduino_ArduinoBoard, Board, ArduinoModule, arduino_BooleanVariableRef, arduino_ArduinoCommunicationModule, arduino_BluetoothTransceiver, arduino_VariableDeclaration, arduino_VariableRef, arduino_IntegerVariableRef, VariableRef, Time, BinaryIntegerOperatorKind, BinaryBooleanOperatorKind, UnaryIntegerOperatorKind, UnaryBooleanOperatorKind, Color},
    associations={module1, module2, project3, block5, board6, module11, project0, block12, module14, condition16, boards8, sketches9, left17, variable21, condition22, right18, operand27, operand29, elseBlock24, variable33, instructions34, digitalPins36, analogPins38, variable41, connectedTransceiver43, variable31},
    generalizations={gen_arduino_Module_NamedElement, gen_arduino_DigitalPin_Pin, gen_arduino_Pin_NamedElement, gen_arduino_AnalogPin_Pin, gen_arduino_Sketch_NamedElement, gen_arduino_Board_NamedElement, gen_arduino_Control_Instruction, gen_arduino_Utilities_Instruction, gen_arduino_Delay_Utilities, gen_arduino_Repeat_Control, gen_arduino_ModuleGet_Expression, gen_arduino_While_Control, gen_arduino_BinaryExpression_Expression, gen_arduino_ModuleAssignment_ModuleInstruction, gen_arduino_ModuleAssignment_Assignment, gen_arduino_ModuleInstruction_Instruction, gen_arduino_Variable_NamedElement, gen_arduino_VariableAssignment_Instruction, gen_arduino_VariableAssignment_Assignment, gen_arduino_BinaryIntegerExpression_BinaryExpression, gen_arduino_BinaryIntegerExpression_IntegerExpression, gen_arduino_BinaryBooleanExpression_BinaryExpression, gen_arduino_BinaryBooleanExpression_BooleanExpression, gen_arduino_Constant_Expression, gen_arduino_If_Control, gen_arduino_Assignment_Instruction, gen_arduino_IntegerVariable_Variable, gen_arduino_BooleanVariable_Variable, gen_arduino_BooleanModuleGet_ModuleGet, gen_arduino_BooleanModuleGet_BooleanExpression, gen_arduino_IntegerModuleGet_ModuleGet, gen_arduino_IntegerModuleGet_IntegerExpression, gen_arduino_UnaryExpression_Expression, gen_arduino_UnaryBooleanExpression_UnaryExpression, gen_arduino_UnaryBooleanExpression_BooleanExpression, gen_arduino_UnaryIntegerExpression_UnaryExpression, gen_arduino_UnaryIntegerExpression_IntegerExpression, gen_arduino_IntegerConstant_Constant, gen_arduino_IntegerConstant_IntegerExpression, gen_arduino_BooleanConstant_Constant, gen_arduino_BooleanConstant_BooleanExpression, gen_arduino_BooleanExpression_Expression, gen_arduino_IntegerExpression_Expression, gen_arduino_LED_ArduinoDigitalModule, gen_arduino_PushButton_ArduinoDigitalModule, gen_arduino_Buzzer_ArduinoDigitalModule, gen_arduino_RotationSensor_ArduinoAnalogModule, gen_arduino_MicroServo_ArduinoDigitalModule, gen_arduino_InfraRedSensor_ArduinoDigitalModule, gen_arduino_AmbientLightSensor_ArduinoAnalogModule, gen_arduino_SoundSensor_ArduinoAnalogModule, gen_arduino_Fan_ArduinoDigitalModule, gen_arduino_MusicPlayer_ArduinoAnalogModule, gen_arduino_ArduinoModule_Module, gen_arduino_ArduinoBoard_Board, gen_arduino_ArduinoDigitalModule_ArduinoModule, gen_arduino_ArduinoAnalogModule_ArduinoModule, gen_arduino_BooleanVariableRef_VariableRef, gen_arduino_BooleanVariableRef_BooleanExpression, gen_arduino_ArduinoCommunicationModule_ArduinoDigitalModule, gen_arduino_BluetoothTransceiver_ArduinoAnalogModule, gen_arduino_VariableDeclaration_Instruction, gen_arduino_VariableRef_Expression, gen_arduino_IntegerVariableRef_VariableRef, gen_arduino_IntegerVariableRef_IntegerExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)