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
            EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max"),
			EnumerationLiteral(name="pourcent")
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
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
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
            EnumerationLiteral(name="not")
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

ChangeType: Enumeration = Enumeration(
    name="ChangeType",
    literals={
            EnumerationLiteral(name="RISING"),
			EnumerationLiteral(name="FALLING"),
			EnumerationLiteral(name="CHANGE")
    }
)

# Classes
arduino_Board = Class(name="arduino::Board", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduino_Project = Class(name="arduino::Project")
arduino_Module = Class(name="arduino::Module", is_abstract=True)
arduino_DigitalPin = Class(name="arduino::DigitalPin")
Pin = Class(name="Pin")
arduino_ArduinoDigitalModule = Class(name="arduino::ArduinoDigitalModule", is_abstract=True)
arduino_Pin = Class(name="arduino::Pin", is_abstract=True)
arduino_AnalogPin = Class(name="arduino::AnalogPin")
arduino_ArduinoAnalogModule = Class(name="arduino::ArduinoAnalogModule", is_abstract=True)
arduino_Sketch = Class(name="arduino::Sketch")
arduino_Block = Class(name="arduino::Block")
arduino_Expression = Class(name="arduino::Expression", is_abstract=True)
arduino_Instruction = Class(name="arduino::Instruction", is_abstract=True)
arduino_ModuleAssignment = Class(name="arduino::ModuleAssignment")
ModuleInstruction = Class(name="ModuleInstruction")
Assignment = Class(name="Assignment")
arduino_ModuleInstruction = Class(name="arduino::ModuleInstruction", is_abstract=True)
Instruction = Class(name="Instruction")
arduino_Control = Class(name="arduino::Control", is_abstract=True)
arduino_Utilities = Class(name="arduino::Utilities", is_abstract=True)
arduino_Delay = Class(name="arduino::Delay")
Utilities = Class(name="Utilities")
arduino_NamedElement = Class(name="arduino::NamedElement", is_abstract=True)
arduino_Repeat = Class(name="arduino::Repeat")
Control = Class(name="Control")
arduino_ModuleGet = Class(name="arduino::ModuleGet", is_abstract=True)
Expression = Class(name="Expression")
arduino_While = Class(name="arduino::While")
arduino_BooleanExpression = Class(name="arduino::BooleanExpression", is_abstract=True)
arduino_BinaryExpression = Class(name="arduino::BinaryExpression", is_abstract=True)
arduino_BooleanVariable = Class(name="arduino::BooleanVariable")
arduino_BooleanModuleGet = Class(name="arduino::BooleanModuleGet")
ModuleGet = Class(name="ModuleGet")
arduino_Variable = Class(name="arduino::Variable", is_abstract=True)
arduino_VariableAssignment = Class(name="arduino::VariableAssignment")
arduino_BinaryIntegerExpression = Class(name="arduino::BinaryIntegerExpression")
BinaryExpression = Class(name="BinaryExpression")
IntegerExpression = Class(name="IntegerExpression")
arduino_BinaryBooleanExpression = Class(name="arduino::BinaryBooleanExpression")
BooleanExpression = Class(name="BooleanExpression")
arduino_Constant = Class(name="arduino::Constant", is_abstract=True)
arduino_If = Class(name="arduino::If")
arduino_IntegerConstant = Class(name="arduino::IntegerConstant")
Constant = Class(name="Constant")
arduino_BooleanConstant = Class(name="arduino::BooleanConstant")
arduino_IntegerExpression = Class(name="arduino::IntegerExpression", is_abstract=True)
arduino_Assignment = Class(name="arduino::Assignment", is_abstract=True)
arduino_IntegerVariable = Class(name="arduino::IntegerVariable")
Variable = Class(name="Variable")
arduino_AmbientLightSensor = Class(name="arduino::AmbientLightSensor")
arduino_SoundSensor = Class(name="arduino::SoundSensor")
arduino_Fan = Class(name="arduino::Fan")
arduino_IntegerModuleGet = Class(name="arduino::IntegerModuleGet")
arduino_UnaryExpression = Class(name="arduino::UnaryExpression", is_abstract=True)
arduino_UnaryBooleanExpression = Class(name="arduino::UnaryBooleanExpression")
UnaryExpression = Class(name="UnaryExpression")
arduino_UnaryIntegerExpression = Class(name="arduino::UnaryIntegerExpression")
arduino_VariableDeclaration = Class(name="arduino::VariableDeclaration")
arduino_VariableRef = Class(name="arduino::VariableRef", is_abstract=True)
arduino_IntegerVariableRef = Class(name="arduino::IntegerVariableRef")
VariableRef = Class(name="VariableRef")
arduino_LED = Class(name="arduino::LED")
ArduinoDigitalModule = Class(name="ArduinoDigitalModule")
arduino_PushButton = Class(name="arduino::PushButton")
arduino_Buzzer = Class(name="arduino::Buzzer")
arduino_RotationSensor = Class(name="arduino::RotationSensor")
ArduinoAnalogModule = Class(name="ArduinoAnalogModule")
arduino_MicroServo = Class(name="arduino::MicroServo")
arduino_InfraRedSensor = Class(name="arduino::InfraRedSensor")
arduino_MusicPlayer = Class(name="arduino::MusicPlayer")
arduino_ArduinoModule = Class(name="arduino::ArduinoModule", is_abstract=True)
Module = Class(name="Module")
arduino_WaitFor = Class(name="arduino::WaitFor")
arduino_ArduinoBoard = Class(name="arduino::ArduinoBoard")
Board = Class(name="Board")
ArduinoModule = Class(name="ArduinoModule")
arduino_BooleanVariableRef = Class(name="arduino::BooleanVariableRef")
arduino_ArduinoCommunicationModule = Class(name="arduino::ArduinoCommunicationModule", is_abstract=True)
arduino_BluetoothTransceiver = Class(name="arduino::BluetoothTransceiver")

# arduino_Board class attributes and methods

# NamedElement class attributes and methods

# arduino_Project class attributes and methods

# arduino_Module class attributes and methods

# arduino_DigitalPin class attributes and methods

# Pin class attributes and methods

# arduino_ArduinoDigitalModule class attributes and methods

# arduino_Pin class attributes and methods
arduino_Pin_level: Property = Property(name="level", type=IntegerType)
arduino_Pin.attributes={arduino_Pin_level}

# arduino_AnalogPin class attributes and methods

# arduino_ArduinoAnalogModule class attributes and methods

# arduino_Sketch class attributes and methods

# arduino_Block class attributes and methods

# arduino_Expression class attributes and methods

# arduino_Instruction class attributes and methods

# arduino_ModuleAssignment class attributes and methods

# ModuleInstruction class attributes and methods

# Assignment class attributes and methods

# arduino_ModuleInstruction class attributes and methods

# Instruction class attributes and methods

# arduino_Control class attributes and methods

# arduino_Utilities class attributes and methods

# arduino_Delay class attributes and methods
arduino_Delay_unit: Property = Property(name="unit", type=StringType)
arduino_Delay_value: Property = Property(name="value", type=IntegerType)
arduino_Delay.attributes={arduino_Delay_value, arduino_Delay_unit}

# Utilities class attributes and methods

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_Repeat class attributes and methods
arduino_Repeat_iteration: Property = Property(name="iteration", type=IntegerType)
arduino_Repeat.attributes={arduino_Repeat_iteration}

# Control class attributes and methods

# arduino_ModuleGet class attributes and methods

# Expression class attributes and methods

# arduino_While class attributes and methods

# arduino_BooleanExpression class attributes and methods

# arduino_BinaryExpression class attributes and methods

# arduino_BooleanVariable class attributes and methods
arduino_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
arduino_BooleanVariable.attributes={arduino_BooleanVariable_initialValue}

# arduino_BooleanModuleGet class attributes and methods

# ModuleGet class attributes and methods

# arduino_Variable class attributes and methods

# arduino_VariableAssignment class attributes and methods

# arduino_BinaryIntegerExpression class attributes and methods
arduino_BinaryIntegerExpression_operator: Property = Property(name="operator", type=StringType)
arduino_BinaryIntegerExpression.attributes={arduino_BinaryIntegerExpression_operator}

# BinaryExpression class attributes and methods

# IntegerExpression class attributes and methods

# arduino_BinaryBooleanExpression class attributes and methods
arduino_BinaryBooleanExpression_operator: Property = Property(name="operator", type=StringType)
arduino_BinaryBooleanExpression.attributes={arduino_BinaryBooleanExpression_operator}

# BooleanExpression class attributes and methods

# arduino_Constant class attributes and methods

# arduino_If class attributes and methods

# arduino_IntegerConstant class attributes and methods
arduino_IntegerConstant_value: Property = Property(name="value", type=IntegerType)
arduino_IntegerConstant.attributes={arduino_IntegerConstant_value}

# Constant class attributes and methods

# arduino_BooleanConstant class attributes and methods
arduino_BooleanConstant_value: Property = Property(name="value", type=BooleanType)
arduino_BooleanConstant.attributes={arduino_BooleanConstant_value}

# arduino_IntegerExpression class attributes and methods

# arduino_Assignment class attributes and methods

# arduino_IntegerVariable class attributes and methods
arduino_IntegerVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
arduino_IntegerVariable.attributes={arduino_IntegerVariable_initialValue}

# Variable class attributes and methods

# arduino_AmbientLightSensor class attributes and methods

# arduino_SoundSensor class attributes and methods

# arduino_Fan class attributes and methods

# arduino_IntegerModuleGet class attributes and methods

# arduino_UnaryExpression class attributes and methods

# arduino_UnaryBooleanExpression class attributes and methods
arduino_UnaryBooleanExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryBooleanExpression.attributes={arduino_UnaryBooleanExpression_operator}

# UnaryExpression class attributes and methods

# arduino_UnaryIntegerExpression class attributes and methods
arduino_UnaryIntegerExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryIntegerExpression.attributes={arduino_UnaryIntegerExpression_operator}

# arduino_VariableDeclaration class attributes and methods

# arduino_VariableRef class attributes and methods

# arduino_IntegerVariableRef class attributes and methods

# VariableRef class attributes and methods

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

# arduino_MusicPlayer class attributes and methods

# arduino_ArduinoModule class attributes and methods

# Module class attributes and methods

# arduino_WaitFor class attributes and methods
arduino_WaitFor_mode: Property = Property(name="mode", type=StringType)
arduino_WaitFor.attributes={arduino_WaitFor_mode}

# arduino_ArduinoBoard class attributes and methods

# Board class attributes and methods

# ArduinoModule class attributes and methods

# arduino_BooleanVariableRef class attributes and methods

# arduino_ArduinoCommunicationModule class attributes and methods

# arduino_BluetoothTransceiver class attributes and methods

# Relationships
board6: BinaryAssociation = BinaryAssociation(
    name="board6",
    ends={
        Property(name="arduino_Board", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch7", type=arduino_Board, multiplicity=Multiplicity(0, 1))
    }
)
boards8: BinaryAssociation = BinaryAssociation(
    name="boards8",
    ends={
        Property(name="Board", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=arduino_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project0: BinaryAssociation = BinaryAssociation(
    name="project0",
    ends={
        Property(name="Project", type=arduino_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="boards", type=arduino_Project, multiplicity=Multiplicity(1, 1))
    }
)
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
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="arduino_Expression", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="arduino_Expression20", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression19", type=arduino_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sketches9: BinaryAssociation = BinaryAssociation(
    name="sketches9",
    ends={
        Property(name="Sketch", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project10", type=arduino_Sketch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module11: BinaryAssociation = BinaryAssociation(
    name="module11",
    ends={
        Property(name="arduino_Module", type=arduino_ModuleInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleInstruction", type=arduino_Module, multiplicity=Multiplicity(1, 1))
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
elseBlock24: BinaryAssociation = BinaryAssociation(
    name="elseBlock24",
    ends={
        Property(name="arduino_Block26", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If25", type=arduino_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
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
variable31: BinaryAssociation = BinaryAssociation(
    name="variable31",
    ends={
        Property(name="arduino_Variable32", type=arduino_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableDeclaration", type=arduino_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable33: BinaryAssociation = BinaryAssociation(
    name="variable33",
    ends={
        Property(name="arduino_IntegerVariable", type=arduino_IntegerVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_IntegerVariableRef", type=arduino_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
pin34: BinaryAssociation = BinaryAssociation(
    name="pin34",
    ends={
        Property(name="arduino_Pin", type=arduino_WaitFor, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_WaitFor", type=arduino_Pin, multiplicity=Multiplicity(0, 1))
    }
)
instructions35: BinaryAssociation = BinaryAssociation(
    name="instructions35",
    ends={
        Property(name="arduino_Instruction", type=arduino_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Block36", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
digitalPins37: BinaryAssociation = BinaryAssociation(
    name="digitalPins37",
    ends={
        Property(name="arduino_DigitalPin38", type=arduino_ArduinoBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ArduinoBoard", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
analogPins39: BinaryAssociation = BinaryAssociation(
    name="analogPins39",
    ends={
        Property(name="arduino_AnalogPin41", type=arduino_ArduinoBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ArduinoBoard40", type=arduino_AnalogPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable42: BinaryAssociation = BinaryAssociation(
    name="variable42",
    ends={
        Property(name="arduino_BooleanVariable", type=arduino_BooleanVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BooleanVariableRef", type=arduino_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
connectedTransceiver44: BinaryAssociation = BinaryAssociation(
    name="connectedTransceiver44",
    ends={
        Property(name="arduino_BluetoothTransceiver", type=arduino_BluetoothTransceiver, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BluetoothTransceiver43", type=arduino_BluetoothTransceiver, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_arduino_Board_NamedElement = Generalization(general=NamedElement, specific=arduino_Board)
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_DigitalPin_Pin = Generalization(general=Pin, specific=arduino_DigitalPin)
gen_arduino_Pin_NamedElement = Generalization(general=NamedElement, specific=arduino_Pin)
gen_arduino_AnalogPin_Pin = Generalization(general=Pin, specific=arduino_AnalogPin)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_ModuleAssignment_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_ModuleAssignment)
gen_arduino_ModuleAssignment_Assignment = Generalization(general=Assignment, specific=arduino_ModuleAssignment)
gen_arduino_ModuleInstruction_Instruction = Generalization(general=Instruction, specific=arduino_ModuleInstruction)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_Utilities_Instruction = Generalization(general=Instruction, specific=arduino_Utilities)
gen_arduino_Delay_Utilities = Generalization(general=Utilities, specific=arduino_Delay)
gen_arduino_Repeat_Control = Generalization(general=Control, specific=arduino_Repeat)
gen_arduino_ModuleGet_Expression = Generalization(general=Expression, specific=arduino_ModuleGet)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_BinaryExpression_Expression = Generalization(general=Expression, specific=arduino_BinaryExpression)
gen_arduino_BooleanVariable_Variable = Generalization(general=Variable, specific=arduino_BooleanVariable)
gen_arduino_BooleanModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_BooleanModuleGet)
gen_arduino_Variable_NamedElement = Generalization(general=NamedElement, specific=arduino_Variable)
gen_arduino_VariableAssignment_Instruction = Generalization(general=Instruction, specific=arduino_VariableAssignment)
gen_arduino_VariableAssignment_Assignment = Generalization(general=Assignment, specific=arduino_VariableAssignment)
gen_arduino_BinaryIntegerExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BinaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BinaryBooleanExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryBooleanExpression)
gen_arduino_BinaryBooleanExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BinaryBooleanExpression)
gen_arduino_Constant_Expression = Generalization(general=Expression, specific=arduino_Constant)
gen_arduino_If_Control = Generalization(general=Control, specific=arduino_If)
gen_arduino_IntegerConstant_Constant = Generalization(general=Constant, specific=arduino_IntegerConstant)
gen_arduino_IntegerConstant_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerConstant)
gen_arduino_BooleanConstant_Constant = Generalization(general=Constant, specific=arduino_BooleanConstant)
gen_arduino_BooleanConstant_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanConstant)
gen_arduino_BooleanExpression_Expression = Generalization(general=Expression, specific=arduino_BooleanExpression)
gen_arduino_IntegerExpression_Expression = Generalization(general=Expression, specific=arduino_IntegerExpression)
gen_arduino_Assignment_Instruction = Generalization(general=Instruction, specific=arduino_Assignment)
gen_arduino_IntegerVariable_Variable = Generalization(general=Variable, specific=arduino_IntegerVariable)
gen_arduino_InfraRedSensor_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_InfraRedSensor)
gen_arduino_AmbientLightSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_AmbientLightSensor)
gen_arduino_SoundSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_SoundSensor)
gen_arduino_Fan_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_Fan)
gen_arduino_BooleanModuleGet_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanModuleGet)
gen_arduino_IntegerModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_IntegerModuleGet)
gen_arduino_IntegerModuleGet_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerModuleGet)
gen_arduino_UnaryExpression_Expression = Generalization(general=Expression, specific=arduino_UnaryExpression)
gen_arduino_UnaryBooleanExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=arduino_UnaryBooleanExpression)
gen_arduino_UnaryBooleanExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_UnaryBooleanExpression)
gen_arduino_UnaryIntegerExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=arduino_UnaryIntegerExpression)
gen_arduino_UnaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_UnaryIntegerExpression)
gen_arduino_VariableDeclaration_Instruction = Generalization(general=Instruction, specific=arduino_VariableDeclaration)
gen_arduino_VariableRef_Expression = Generalization(general=Expression, specific=arduino_VariableRef)
gen_arduino_IntegerVariableRef_VariableRef = Generalization(general=VariableRef, specific=arduino_IntegerVariableRef)
gen_arduino_IntegerVariableRef_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerVariableRef)
gen_arduino_LED_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_LED)
gen_arduino_PushButton_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_PushButton)
gen_arduino_Buzzer_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_Buzzer)
gen_arduino_RotationSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_RotationSensor)
gen_arduino_MicroServo_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_MicroServo)
gen_arduino_MusicPlayer_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_MusicPlayer)
gen_arduino_ArduinoModule_Module = Generalization(general=Module, specific=arduino_ArduinoModule)
gen_arduino_WaitFor_Utilities = Generalization(general=Utilities, specific=arduino_WaitFor)
gen_arduino_ArduinoBoard_Board = Generalization(general=Board, specific=arduino_ArduinoBoard)
gen_arduino_ArduinoDigitalModule_ArduinoModule = Generalization(general=ArduinoModule, specific=arduino_ArduinoDigitalModule)
gen_arduino_ArduinoAnalogModule_ArduinoModule = Generalization(general=ArduinoModule, specific=arduino_ArduinoAnalogModule)
gen_arduino_BooleanVariableRef_VariableRef = Generalization(general=VariableRef, specific=arduino_BooleanVariableRef)
gen_arduino_BooleanVariableRef_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanVariableRef)
gen_arduino_ArduinoCommunicationModule_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_ArduinoCommunicationModule)
gen_arduino_BluetoothTransceiver_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_BluetoothTransceiver)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Board, NamedElement, arduino_Project, arduino_Module, arduino_DigitalPin, Pin, arduino_ArduinoDigitalModule, arduino_Pin, arduino_AnalogPin, arduino_ArduinoAnalogModule, arduino_Sketch, arduino_Block, arduino_Expression, arduino_Instruction, arduino_ModuleAssignment, ModuleInstruction, Assignment, arduino_ModuleInstruction, Instruction, arduino_Control, arduino_Utilities, arduino_Delay, Utilities, arduino_NamedElement, arduino_Repeat, Control, arduino_ModuleGet, Expression, arduino_While, arduino_BooleanExpression, arduino_BinaryExpression, arduino_BooleanVariable, arduino_BooleanModuleGet, ModuleGet, arduino_Variable, arduino_VariableAssignment, arduino_BinaryIntegerExpression, BinaryExpression, IntegerExpression, arduino_BinaryBooleanExpression, BooleanExpression, arduino_Constant, arduino_If, arduino_IntegerConstant, Constant, arduino_BooleanConstant, arduino_IntegerExpression, arduino_Assignment, arduino_IntegerVariable, Variable, arduino_AmbientLightSensor, arduino_SoundSensor, arduino_Fan, arduino_IntegerModuleGet, arduino_UnaryExpression, arduino_UnaryBooleanExpression, UnaryExpression, arduino_UnaryIntegerExpression, arduino_VariableDeclaration, arduino_VariableRef, arduino_IntegerVariableRef, VariableRef, arduino_LED, ArduinoDigitalModule, arduino_PushButton, arduino_Buzzer, arduino_RotationSensor, ArduinoAnalogModule, arduino_MicroServo, arduino_InfraRedSensor, arduino_MusicPlayer, arduino_ArduinoModule, Module, arduino_WaitFor, arduino_ArduinoBoard, Board, ArduinoModule, arduino_BooleanVariableRef, arduino_ArduinoCommunicationModule, arduino_BluetoothTransceiver, Time, BinaryIntegerOperatorKind, BinaryBooleanOperatorKind, UnaryIntegerOperatorKind, UnaryBooleanOperatorKind, Color, ChangeType},
    associations={board6, boards8, project0, module1, module2, project3, block5, left17, right18, sketches9, module11, block12, module14, condition16, variable21, condition22, elseBlock24, operand27, operand29, variable31, variable33, pin34, instructions35, digitalPins37, analogPins39, variable42, connectedTransceiver44},
    generalizations={gen_arduino_Board_NamedElement, gen_arduino_Module_NamedElement, gen_arduino_DigitalPin_Pin, gen_arduino_Pin_NamedElement, gen_arduino_AnalogPin_Pin, gen_arduino_Sketch_NamedElement, gen_arduino_ModuleAssignment_ModuleInstruction, gen_arduino_ModuleAssignment_Assignment, gen_arduino_ModuleInstruction_Instruction, gen_arduino_Control_Instruction, gen_arduino_Utilities_Instruction, gen_arduino_Delay_Utilities, gen_arduino_Repeat_Control, gen_arduino_ModuleGet_Expression, gen_arduino_While_Control, gen_arduino_BinaryExpression_Expression, gen_arduino_BooleanVariable_Variable, gen_arduino_BooleanModuleGet_ModuleGet, gen_arduino_Variable_NamedElement, gen_arduino_VariableAssignment_Instruction, gen_arduino_VariableAssignment_Assignment, gen_arduino_BinaryIntegerExpression_BinaryExpression, gen_arduino_BinaryIntegerExpression_IntegerExpression, gen_arduino_BinaryBooleanExpression_BinaryExpression, gen_arduino_BinaryBooleanExpression_BooleanExpression, gen_arduino_Constant_Expression, gen_arduino_If_Control, gen_arduino_IntegerConstant_Constant, gen_arduino_IntegerConstant_IntegerExpression, gen_arduino_BooleanConstant_Constant, gen_arduino_BooleanConstant_BooleanExpression, gen_arduino_BooleanExpression_Expression, gen_arduino_IntegerExpression_Expression, gen_arduino_Assignment_Instruction, gen_arduino_IntegerVariable_Variable, gen_arduino_InfraRedSensor_ArduinoDigitalModule, gen_arduino_AmbientLightSensor_ArduinoAnalogModule, gen_arduino_SoundSensor_ArduinoAnalogModule, gen_arduino_Fan_ArduinoDigitalModule, gen_arduino_BooleanModuleGet_BooleanExpression, gen_arduino_IntegerModuleGet_ModuleGet, gen_arduino_IntegerModuleGet_IntegerExpression, gen_arduino_UnaryExpression_Expression, gen_arduino_UnaryBooleanExpression_UnaryExpression, gen_arduino_UnaryBooleanExpression_BooleanExpression, gen_arduino_UnaryIntegerExpression_UnaryExpression, gen_arduino_UnaryIntegerExpression_IntegerExpression, gen_arduino_VariableDeclaration_Instruction, gen_arduino_VariableRef_Expression, gen_arduino_IntegerVariableRef_VariableRef, gen_arduino_IntegerVariableRef_IntegerExpression, gen_arduino_LED_ArduinoDigitalModule, gen_arduino_PushButton_ArduinoDigitalModule, gen_arduino_Buzzer_ArduinoDigitalModule, gen_arduino_RotationSensor_ArduinoAnalogModule, gen_arduino_MicroServo_ArduinoDigitalModule, gen_arduino_MusicPlayer_ArduinoAnalogModule, gen_arduino_ArduinoModule_Module, gen_arduino_WaitFor_Utilities, gen_arduino_ArduinoBoard_Board, gen_arduino_ArduinoDigitalModule_ArduinoModule, gen_arduino_ArduinoAnalogModule_ArduinoModule, gen_arduino_BooleanVariableRef_VariableRef, gen_arduino_BooleanVariableRef_BooleanExpression, gen_arduino_ArduinoCommunicationModule_ArduinoDigitalModule, gen_arduino_BluetoothTransceiver_ArduinoAnalogModule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)