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

# Classes
arduino_Board = Class(name="arduino::Board", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduino_Project = Class(name="arduino::Project")
arduino_AnalogPin = Class(name="arduino::AnalogPin")
arduino_ArduinoAnalogModule = Class(name="arduino::ArduinoAnalogModule", is_abstract=True)
arduino_Sketch = Class(name="arduino::Sketch")
arduino_Block = Class(name="arduino::Block")
arduino_Instruction = Class(name="arduino::Instruction", is_abstract=True)
arduino_ModuleAssignment = Class(name="arduino::ModuleAssignment")
ModuleInstruction = Class(name="ModuleInstruction")
Assignment = Class(name="Assignment")
arduino_ModuleInstruction = Class(name="arduino::ModuleInstruction", is_abstract=True)
Instruction = Class(name="Instruction")
arduino_Module = Class(name="arduino::Module", is_abstract=True)
arduino_DigitalPin = Class(name="arduino::DigitalPin")
Pin = Class(name="Pin")
arduino_ArduinoDigitalModule = Class(name="arduino::ArduinoDigitalModule", is_abstract=True)
arduino_Pin = Class(name="arduino::Pin", is_abstract=True)
arduino_NamedElement = Class(name="arduino::NamedElement", is_abstract=True)
arduino_Repeat = Class(name="arduino::Repeat")
Control = Class(name="Control")
arduino_ModuleGet = Class(name="arduino::ModuleGet", is_abstract=True)
Expression = Class(name="Expression")
arduino_While = Class(name="arduino::While")
arduino_BooleanExpression = Class(name="arduino::BooleanExpression", is_abstract=True)
arduino_BinaryExpression = Class(name="arduino::BinaryExpression", is_abstract=True)
arduino_Expression = Class(name="arduino::Expression", is_abstract=True)
arduino_Variable = Class(name="arduino::Variable", is_abstract=True)
arduino_Control = Class(name="arduino::Control", is_abstract=True)
arduino_Utilities = Class(name="arduino::Utilities", is_abstract=True)
arduino_Delay = Class(name="arduino::Delay")
Utilities = Class(name="Utilities")
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
arduino_VariableAssignment = Class(name="arduino::VariableAssignment")
arduino_BinaryIntegerExpression = Class(name="arduino::BinaryIntegerExpression")
BinaryExpression = Class(name="BinaryExpression")
IntegerExpression = Class(name="IntegerExpression")
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
arduino_BooleanVariable = Class(name="arduino::BooleanVariable")
arduino_BooleanModuleGet = Class(name="arduino::BooleanModuleGet")
ModuleGet = Class(name="ModuleGet")
arduino_MusicPlayer = Class(name="arduino::MusicPlayer")
arduino_ArduinoModule = Class(name="arduino::ArduinoModule", is_abstract=True)
Module = Class(name="Module")
arduino_ArduinoBoard = Class(name="arduino::ArduinoBoard")
Board = Class(name="Board")
ArduinoModule = Class(name="ArduinoModule")
arduino_BooleanVariableRef = Class(name="arduino::BooleanVariableRef")
arduino_ArduinoCommunicationModule = Class(name="arduino::ArduinoCommunicationModule", is_abstract=True)
arduino_BluetoothTransceiver = Class(name="arduino::BluetoothTransceiver")
arduino_Buzzer = Class(name="arduino::Buzzer")
arduino_RotationSensor = Class(name="arduino::RotationSensor")
ArduinoAnalogModule = Class(name="ArduinoAnalogModule")
arduino_MicroServo = Class(name="arduino::MicroServo")
arduino_InfraRedSensor = Class(name="arduino::InfraRedSensor")
arduino_AmbientLightSensor = Class(name="arduino::AmbientLightSensor")
arduino_SoundSensor = Class(name="arduino::SoundSensor")
arduino_Fan = Class(name="arduino::Fan")

# arduino_Board class attributes and methods

# NamedElement class attributes and methods

# arduino_Project class attributes and methods
arduino_Project_m_execute: Method = Method(name="execute", parameters={})
arduino_Project_m_main: Method = Method(name="main", parameters={})
arduino_Project_m_setup: Method = Method(name="setup", parameters={})
arduino_Project_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
arduino_Project.methods={arduino_Project_m_setup, arduino_Project_m_initializeModel, arduino_Project_m_main, arduino_Project_m_execute}

# arduino_AnalogPin class attributes and methods

# arduino_ArduinoAnalogModule class attributes and methods

# arduino_Sketch class attributes and methods

# arduino_Block class attributes and methods
arduino_Block_m_execute: Method = Method(name="execute", parameters={})
arduino_Block.methods={arduino_Block_m_execute}

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

# arduino_Module class attributes and methods

# arduino_DigitalPin class attributes and methods

# Pin class attributes and methods

# arduino_ArduinoDigitalModule class attributes and methods

# arduino_Pin class attributes and methods
arduino_Pin_level: Property = Property(name="level", type=StringType)
arduino_Pin.attributes={arduino_Pin_level}

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_Repeat class attributes and methods
arduino_Repeat_iteration: Property = Property(name="iteration", type=StringType)
arduino_Repeat_m_execute: Method = Method(name="execute", parameters={})
arduino_Repeat_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_Repeat_m_finalize: Method = Method(name="finalize", parameters={})
arduino_Repeat.attributes={arduino_Repeat_iteration}
arduino_Repeat.methods={arduino_Repeat_m_execute, arduino_Repeat_m_finalize, arduino_Repeat_m_evaluate}

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

# arduino_Variable class attributes and methods
arduino_Variable_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_Variable.methods={arduino_Variable_m_evaluate}

# arduino_Control class attributes and methods
arduino_Control_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_Control_m_execute: Method = Method(name="execute", parameters={})
arduino_Control.methods={arduino_Control_m_evaluate, arduino_Control_m_execute}

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

# arduino_Assignment class attributes and methods

# arduino_IntegerVariable class attributes and methods
arduino_IntegerVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
arduino_IntegerVariable_value: Property = Property(name="value", type=StringType)
arduino_IntegerVariable_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_IntegerVariable.attributes={arduino_IntegerVariable_initialValue, arduino_IntegerVariable_value}
arduino_IntegerVariable.methods={arduino_IntegerVariable_m_evaluate}

# Variable class attributes and methods

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

# arduino_VariableDeclaration class attributes and methods
arduino_VariableDeclaration_m_execute: Method = Method(name="execute", parameters={})
arduino_VariableDeclaration.methods={arduino_VariableDeclaration_m_execute}

# arduino_VariableRef class attributes and methods
arduino_VariableRef_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_VariableRef.methods={arduino_VariableRef_m_evaluate}

# arduino_IntegerVariableRef class attributes and methods

# VariableRef class attributes and methods

# arduino_LED class attributes and methods
arduino_LED_color: Property = Property(name="color", type=StringType)
arduino_LED.attributes={arduino_LED_color}

# ArduinoDigitalModule class attributes and methods

# arduino_PushButton class attributes and methods

# arduino_BooleanVariable class attributes and methods
arduino_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
arduino_BooleanVariable_value: Property = Property(name="value", type=StringType)
arduino_BooleanVariable_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BooleanVariable.attributes={arduino_BooleanVariable_initialValue, arduino_BooleanVariable_value}
arduino_BooleanVariable.methods={arduino_BooleanVariable_m_evaluate}

# arduino_BooleanModuleGet class attributes and methods
arduino_BooleanModuleGet_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
arduino_BooleanModuleGet.methods={arduino_BooleanModuleGet_m_evaluate}

# ModuleGet class attributes and methods

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

# arduino_Buzzer class attributes and methods

# arduino_RotationSensor class attributes and methods

# ArduinoAnalogModule class attributes and methods

# arduino_MicroServo class attributes and methods

# arduino_InfraRedSensor class attributes and methods

# arduino_AmbientLightSensor class attributes and methods

# arduino_SoundSensor class attributes and methods

# arduino_Fan class attributes and methods

# Relationships
project0: BinaryAssociation = BinaryAssociation(
    name="project0",
    ends={
        Property(name="1", type=arduino_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=arduino_Project, multiplicity=Multiplicity(1, 1))
    }
)
module3: BinaryAssociation = BinaryAssociation(
    name="module3",
    ends={
        Property(name="arduino_ArduinoAnalogModule", type=arduino_AnalogPin, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_AnalogPin", type=arduino_ArduinoAnalogModule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
project4: BinaryAssociation = BinaryAssociation(
    name="project4",
    ends={
        Property(name="6", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=arduino_Project, multiplicity=Multiplicity(1, 1))
    }
)
block7: BinaryAssociation = BinaryAssociation(
    name="block7",
    ends={
        Property(name="arduino_Block", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch", type=arduino_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
board8: BinaryAssociation = BinaryAssociation(
    name="board8",
    ends={
        Property(name="arduino_Board", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch9", type=arduino_Board, multiplicity=Multiplicity(0, 1))
    }
)
boards10: BinaryAssociation = BinaryAssociation(
    name="boards10",
    ends={
        Property(name="12", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="11", type=arduino_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketches13: BinaryAssociation = BinaryAssociation(
    name="sketches13",
    ends={
        Property(name="15", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=arduino_Sketch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module2: BinaryAssociation = BinaryAssociation(
    name="module2",
    ends={
        Property(name="arduino_ArduinoDigitalModule", type=arduino_DigitalPin, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_DigitalPin", type=arduino_ArduinoDigitalModule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module19: BinaryAssociation = BinaryAssociation(
    name="module19",
    ends={
        Property(name="arduino_Module20", type=arduino_ModuleGet, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleGet", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
condition21: BinaryAssociation = BinaryAssociation(
    name="condition21",
    ends={
        Property(name="arduino_BooleanExpression", type=arduino_While, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_While", type=arduino_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left22: BinaryAssociation = BinaryAssociation(
    name="left22",
    ends={
        Property(name="arduino_Expression", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right23: BinaryAssociation = BinaryAssociation(
    name="right23",
    ends={
        Property(name="arduino_Expression25", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression24", type=arduino_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module16: BinaryAssociation = BinaryAssociation(
    name="module16",
    ends={
        Property(name="arduino_Module", type=arduino_ModuleInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleInstruction", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
block17: BinaryAssociation = BinaryAssociation(
    name="block17",
    ends={
        Property(name="arduino_Block18", type=arduino_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Control", type=arduino_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition27: BinaryAssociation = BinaryAssociation(
    name="condition27",
    ends={
        Property(name="arduino_BooleanExpression28", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If", type=arduino_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock29: BinaryAssociation = BinaryAssociation(
    name="elseBlock29",
    ends={
        Property(name="arduino_Block31", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If30", type=arduino_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand32: BinaryAssociation = BinaryAssociation(
    name="operand32",
    ends={
        Property(name="arduino_Expression33", type=arduino_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Assignment", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable26: BinaryAssociation = BinaryAssociation(
    name="variable26",
    ends={
        Property(name="arduino_Variable", type=arduino_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableAssignment", type=arduino_Variable, multiplicity=Multiplicity(1, 1))
    }
)
operand34: BinaryAssociation = BinaryAssociation(
    name="operand34",
    ends={
        Property(name="arduino_Expression35", type=arduino_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_UnaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable36: BinaryAssociation = BinaryAssociation(
    name="variable36",
    ends={
        Property(name="arduino_Variable37", type=arduino_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableDeclaration", type=arduino_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable38: BinaryAssociation = BinaryAssociation(
    name="variable38",
    ends={
        Property(name="arduino_IntegerVariable", type=arduino_IntegerVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_IntegerVariableRef", type=arduino_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
instructions39: BinaryAssociation = BinaryAssociation(
    name="instructions39",
    ends={
        Property(name="arduino_Instruction", type=arduino_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Block40", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
digitalPins41: BinaryAssociation = BinaryAssociation(
    name="digitalPins41",
    ends={
        Property(name="arduino_DigitalPin42", type=arduino_ArduinoBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ArduinoBoard", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
analogPins43: BinaryAssociation = BinaryAssociation(
    name="analogPins43",
    ends={
        Property(name="arduino_AnalogPin45", type=arduino_ArduinoBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ArduinoBoard44", type=arduino_AnalogPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable46: BinaryAssociation = BinaryAssociation(
    name="variable46",
    ends={
        Property(name="arduino_BooleanVariable", type=arduino_BooleanVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BooleanVariableRef", type=arduino_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
connectedTransceiver48: BinaryAssociation = BinaryAssociation(
    name="connectedTransceiver48",
    ends={
        Property(name="arduino_BluetoothTransceiver", type=arduino_BluetoothTransceiver, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BluetoothTransceiver47", type=arduino_BluetoothTransceiver, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_arduino_Board_NamedElement = Generalization(general=NamedElement, specific=arduino_Board)
gen_arduino_AnalogPin_Pin = Generalization(general=Pin, specific=arduino_AnalogPin)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_ModuleAssignment_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_ModuleAssignment)
gen_arduino_ModuleAssignment_Assignment = Generalization(general=Assignment, specific=arduino_ModuleAssignment)
gen_arduino_ModuleInstruction_Instruction = Generalization(general=Instruction, specific=arduino_ModuleInstruction)
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_DigitalPin_Pin = Generalization(general=Pin, specific=arduino_DigitalPin)
gen_arduino_Pin_NamedElement = Generalization(general=NamedElement, specific=arduino_Pin)
gen_arduino_Repeat_Control = Generalization(general=Control, specific=arduino_Repeat)
gen_arduino_ModuleGet_Expression = Generalization(general=Expression, specific=arduino_ModuleGet)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_BinaryExpression_Expression = Generalization(general=Expression, specific=arduino_BinaryExpression)
gen_arduino_Variable_NamedElement = Generalization(general=NamedElement, specific=arduino_Variable)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_Utilities_Instruction = Generalization(general=Instruction, specific=arduino_Utilities)
gen_arduino_Delay_Utilities = Generalization(general=Utilities, specific=arduino_Delay)
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
gen_arduino_VariableAssignment_Instruction = Generalization(general=Instruction, specific=arduino_VariableAssignment)
gen_arduino_VariableAssignment_Assignment = Generalization(general=Assignment, specific=arduino_VariableAssignment)
gen_arduino_BinaryIntegerExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BinaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BooleanModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_BooleanModuleGet)
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
gen_arduino_BooleanVariable_Variable = Generalization(general=Variable, specific=arduino_BooleanVariable)
gen_arduino_MusicPlayer_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_MusicPlayer)
gen_arduino_ArduinoModule_Module = Generalization(general=Module, specific=arduino_ArduinoModule)
gen_arduino_ArduinoBoard_Board = Generalization(general=Board, specific=arduino_ArduinoBoard)
gen_arduino_ArduinoDigitalModule_ArduinoModule = Generalization(general=ArduinoModule, specific=arduino_ArduinoDigitalModule)
gen_arduino_ArduinoAnalogModule_ArduinoModule = Generalization(general=ArduinoModule, specific=arduino_ArduinoAnalogModule)
gen_arduino_BooleanVariableRef_VariableRef = Generalization(general=VariableRef, specific=arduino_BooleanVariableRef)
gen_arduino_BooleanVariableRef_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanVariableRef)
gen_arduino_ArduinoCommunicationModule_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_ArduinoCommunicationModule)
gen_arduino_BluetoothTransceiver_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_BluetoothTransceiver)
gen_arduino_Buzzer_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_Buzzer)
gen_arduino_RotationSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_RotationSensor)
gen_arduino_MicroServo_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_MicroServo)
gen_arduino_InfraRedSensor_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_InfraRedSensor)
gen_arduino_AmbientLightSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_AmbientLightSensor)
gen_arduino_SoundSensor_ArduinoAnalogModule = Generalization(general=ArduinoAnalogModule, specific=arduino_SoundSensor)
gen_arduino_Fan_ArduinoDigitalModule = Generalization(general=ArduinoDigitalModule, specific=arduino_Fan)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Board, NamedElement, arduino_Project, arduino_AnalogPin, arduino_ArduinoAnalogModule, arduino_Sketch, arduino_Block, arduino_Instruction, arduino_ModuleAssignment, ModuleInstruction, Assignment, arduino_ModuleInstruction, Instruction, arduino_Module, arduino_DigitalPin, Pin, arduino_ArduinoDigitalModule, arduino_Pin, arduino_NamedElement, arduino_Repeat, Control, arduino_ModuleGet, Expression, arduino_While, arduino_BooleanExpression, arduino_BinaryExpression, arduino_Expression, arduino_Variable, arduino_Control, arduino_Utilities, arduino_Delay, Utilities, arduino_BinaryBooleanExpression, BooleanExpression, arduino_Constant, arduino_If, arduino_IntegerConstant, Constant, arduino_BooleanConstant, arduino_IntegerExpression, arduino_Assignment, arduino_IntegerVariable, Variable, arduino_VariableAssignment, arduino_BinaryIntegerExpression, BinaryExpression, IntegerExpression, arduino_IntegerModuleGet, arduino_UnaryExpression, arduino_UnaryBooleanExpression, UnaryExpression, arduino_UnaryIntegerExpression, arduino_VariableDeclaration, arduino_VariableRef, arduino_IntegerVariableRef, VariableRef, arduino_LED, ArduinoDigitalModule, arduino_PushButton, arduino_BooleanVariable, arduino_BooleanModuleGet, ModuleGet, arduino_MusicPlayer, arduino_ArduinoModule, Module, arduino_ArduinoBoard, Board, ArduinoModule, arduino_BooleanVariableRef, arduino_ArduinoCommunicationModule, arduino_BluetoothTransceiver, arduino_Buzzer, arduino_RotationSensor, ArduinoAnalogModule, arduino_MicroServo, arduino_InfraRedSensor, arduino_AmbientLightSensor, arduino_SoundSensor, arduino_Fan, Time, BinaryIntegerOperatorKind, BinaryBooleanOperatorKind, UnaryIntegerOperatorKind, UnaryBooleanOperatorKind, Color},
    associations={project0, module3, project4, block7, board8, boards10, sketches13, module2, module19, condition21, left22, right23, module16, block17, condition27, elseBlock29, operand32, variable26, operand34, variable36, variable38, instructions39, digitalPins41, analogPins43, variable46, connectedTransceiver48},
    generalizations={gen_arduino_Board_NamedElement, gen_arduino_AnalogPin_Pin, gen_arduino_Sketch_NamedElement, gen_arduino_ModuleAssignment_ModuleInstruction, gen_arduino_ModuleAssignment_Assignment, gen_arduino_ModuleInstruction_Instruction, gen_arduino_Module_NamedElement, gen_arduino_DigitalPin_Pin, gen_arduino_Pin_NamedElement, gen_arduino_Repeat_Control, gen_arduino_ModuleGet_Expression, gen_arduino_While_Control, gen_arduino_BinaryExpression_Expression, gen_arduino_Variable_NamedElement, gen_arduino_Control_Instruction, gen_arduino_Utilities_Instruction, gen_arduino_Delay_Utilities, gen_arduino_BinaryBooleanExpression_BinaryExpression, gen_arduino_BinaryBooleanExpression_BooleanExpression, gen_arduino_Constant_Expression, gen_arduino_If_Control, gen_arduino_IntegerConstant_Constant, gen_arduino_IntegerConstant_IntegerExpression, gen_arduino_BooleanConstant_Constant, gen_arduino_BooleanConstant_BooleanExpression, gen_arduino_BooleanExpression_Expression, gen_arduino_IntegerExpression_Expression, gen_arduino_Assignment_Instruction, gen_arduino_IntegerVariable_Variable, gen_arduino_VariableAssignment_Instruction, gen_arduino_VariableAssignment_Assignment, gen_arduino_BinaryIntegerExpression_BinaryExpression, gen_arduino_BinaryIntegerExpression_IntegerExpression, gen_arduino_BooleanModuleGet_ModuleGet, gen_arduino_BooleanModuleGet_BooleanExpression, gen_arduino_IntegerModuleGet_ModuleGet, gen_arduino_IntegerModuleGet_IntegerExpression, gen_arduino_UnaryExpression_Expression, gen_arduino_UnaryBooleanExpression_UnaryExpression, gen_arduino_UnaryBooleanExpression_BooleanExpression, gen_arduino_UnaryIntegerExpression_UnaryExpression, gen_arduino_UnaryIntegerExpression_IntegerExpression, gen_arduino_VariableDeclaration_Instruction, gen_arduino_VariableRef_Expression, gen_arduino_IntegerVariableRef_VariableRef, gen_arduino_IntegerVariableRef_IntegerExpression, gen_arduino_LED_ArduinoDigitalModule, gen_arduino_PushButton_ArduinoDigitalModule, gen_arduino_BooleanVariable_Variable, gen_arduino_MusicPlayer_ArduinoAnalogModule, gen_arduino_ArduinoModule_Module, gen_arduino_ArduinoBoard_Board, gen_arduino_ArduinoDigitalModule_ArduinoModule, gen_arduino_ArduinoAnalogModule_ArduinoModule, gen_arduino_BooleanVariableRef_VariableRef, gen_arduino_BooleanVariableRef_BooleanExpression, gen_arduino_ArduinoCommunicationModule_ArduinoDigitalModule, gen_arduino_BluetoothTransceiver_ArduinoAnalogModule, gen_arduino_Buzzer_ArduinoDigitalModule, gen_arduino_RotationSensor_ArduinoAnalogModule, gen_arduino_MicroServo_ArduinoDigitalModule, gen_arduino_InfraRedSensor_ArduinoDigitalModule, gen_arduino_AmbientLightSensor_ArduinoAnalogModule, gen_arduino_SoundSensor_ArduinoAnalogModule, gen_arduino_Fan_ArduinoDigitalModule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)