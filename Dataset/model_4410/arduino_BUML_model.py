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
ModuleKind: Enumeration = Enumeration(
    name="ModuleKind",
    literals={
            EnumerationLiteral(name="digital"),
			EnumerationLiteral(name="analog")
    }
)

Time: Enumeration = Enumeration(
    name="Time",
    literals={
            EnumerationLiteral(name="MilliSecond"),
			EnumerationLiteral(name="MicroSecond")
    }
)

Library: Enumeration = Enumeration(
    name="Library",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="servo"),
			EnumerationLiteral(name="music")
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

UnaryBooleanOperatorKind: Enumeration = Enumeration(
    name="UnaryBooleanOperatorKind",
    literals={
            EnumerationLiteral(name="not")
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

# Classes
arduino_Hardware = Class(name="arduino::Hardware")
NamedElement = Class(name="NamedElement")
arduino_Sketch = Class(name="arduino::Sketch")
Instruction = Class(name="Instruction")
arduino_Instruction = Class(name="arduino::Instruction", is_abstract=True)
arduino_Project = Class(name="arduino::Project")
arduino_Platform = Class(name="arduino::Platform")
arduino_Module = Class(name="arduino::Module", is_abstract=True)
arduino_Connector = Class(name="arduino::Connector")
arduino_DigitalPin = Class(name="arduino::DigitalPin")
arduino_AnalogPin = Class(name="arduino::AnalogPin")
Pin = Class(name="Pin")
arduino_Pin = Class(name="arduino::Pin", is_abstract=True)
arduino_Actuator = Class(name="arduino::Actuator")
arduino_NamedElement = Class(name="arduino::NamedElement", is_abstract=True)
arduino_Repeat = Class(name="arduino::Repeat")
Control = Class(name="Control")
arduino_ModuleGet = Class(name="arduino::ModuleGet", is_abstract=True)
Expression = Class(name="Expression")
arduino_ModuleAssignment = Class(name="arduino::ModuleAssignment")
ModuleInstruction = Class(name="ModuleInstruction")
Assignment = Class(name="Assignment")
arduino_ModuleInstruction = Class(name="arduino::ModuleInstruction", is_abstract=True)
arduino_Control = Class(name="arduino::Control", is_abstract=True)
arduino_Utilities = Class(name="arduino::Utilities", is_abstract=True)
arduino_Delay = Class(name="arduino::Delay")
Utilities = Class(name="Utilities")
arduino_Sensor = Class(name="arduino::Sensor")
Module = Class(name="Module")
BooleanExpression = Class(name="BooleanExpression")
arduino_Constant = Class(name="arduino::Constant", is_abstract=True)
arduino_If = Class(name="arduino::If")
arduino_IntegerConstant = Class(name="arduino::IntegerConstant")
Constant = Class(name="Constant")
arduino_BooleanConstant = Class(name="arduino::BooleanConstant")
arduino_While = Class(name="arduino::While")
arduino_Expression = Class(name="arduino::Expression", is_abstract=True)
arduino_BinaryExpression = Class(name="arduino::BinaryExpression", is_abstract=True)
arduino_Variable = Class(name="arduino::Variable", is_abstract=True)
arduino_VariableAssignment = Class(name="arduino::VariableAssignment")
arduino_BinaryIntegerExpression = Class(name="arduino::BinaryIntegerExpression")
BinaryExpression = Class(name="BinaryExpression")
IntegerExpression = Class(name="IntegerExpression")
arduino_BinaryBooleanExpression = Class(name="arduino::BinaryBooleanExpression")
arduino_UnaryExpression = Class(name="arduino::UnaryExpression", is_abstract=True)
arduino_UnaryBooleanExpression = Class(name="arduino::UnaryBooleanExpression")
UnaryExpression = Class(name="UnaryExpression")
arduino_UnaryIntegerExpression = Class(name="arduino::UnaryIntegerExpression")
arduino_VariableDeclaration = Class(name="arduino::VariableDeclaration")
arduino_BooleanExpression = Class(name="arduino::BooleanExpression", is_abstract=True)
arduino_IntegerExpression = Class(name="arduino::IntegerExpression", is_abstract=True)
arduino_Assignment = Class(name="arduino::Assignment", is_abstract=True)
arduino_IntegerVariable = Class(name="arduino::IntegerVariable")
Variable = Class(name="Variable")
arduino_BooleanVariable = Class(name="arduino::BooleanVariable")
arduino_BooleanModuleGet = Class(name="arduino::BooleanModuleGet")
ModuleGet = Class(name="ModuleGet")
arduino_IntegerModuleGet = Class(name="arduino::IntegerModuleGet")
arduino_VariableRef = Class(name="arduino::VariableRef")
arduino_Synchro = Class(name="arduino::Synchro")
InstantaneousInstruction = Class(name="InstantaneousInstruction")
arduino_InstantaneousInstruction = Class(name="arduino::InstantaneousInstruction", is_abstract=True)

# arduino_Hardware class attributes and methods

# NamedElement class attributes and methods

# arduino_Sketch class attributes and methods

# Instruction class attributes and methods

# arduino_Instruction class attributes and methods
arduino_Instruction_m_execute: Method = Method(name="execute", parameters={})
arduino_Instruction_m_finalize: Method = Method(name="finalize", parameters={})
arduino_Instruction.methods={arduino_Instruction_m_finalize, arduino_Instruction_m_execute}

# arduino_Project class attributes and methods

# arduino_Platform class attributes and methods
arduino_Platform_image: Property = Property(name="image", type=StringType)
arduino_Platform.attributes={arduino_Platform_image}

# arduino_Module class attributes and methods
arduino_Module_kind: Property = Property(name="kind", type=StringType)
arduino_Module_image: Property = Property(name="image", type=StringType)
arduino_Module_level: Property = Property(name="level", type=BooleanType)
arduino_Module_library: Property = Property(name="library", type=StringType)
arduino_Module.attributes={arduino_Module_library, arduino_Module_kind, arduino_Module_level, arduino_Module_image}

# arduino_Connector class attributes and methods

# arduino_DigitalPin class attributes and methods

# arduino_AnalogPin class attributes and methods

# Pin class attributes and methods

# arduino_Pin class attributes and methods
arduino_Pin_id: Property = Property(name="id", type=IntegerType)
arduino_Pin_level: Property = Property(name="level", type=IntegerType)
arduino_Pin.attributes={arduino_Pin_id, arduino_Pin_level}

# arduino_Actuator class attributes and methods

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_Repeat class attributes and methods
arduino_Repeat_iteration: Property = Property(name="iteration", type=IntegerType)
arduino_Repeat.attributes={arduino_Repeat_iteration}

# Control class attributes and methods

# arduino_ModuleGet class attributes and methods

# Expression class attributes and methods

# arduino_ModuleAssignment class attributes and methods

# ModuleInstruction class attributes and methods

# Assignment class attributes and methods

# arduino_ModuleInstruction class attributes and methods

# arduino_Control class attributes and methods
arduino_Control_m_evaluate: Method = Method(name="evaluate", parameters={}, type=BooleanType)
arduino_Control.methods={arduino_Control_m_evaluate}

# arduino_Utilities class attributes and methods

# arduino_Delay class attributes and methods
arduino_Delay_unit: Property = Property(name="unit", type=StringType)
arduino_Delay_value: Property = Property(name="value", type=IntegerType)
arduino_Delay.attributes={arduino_Delay_unit, arduino_Delay_value}

# Utilities class attributes and methods

# arduino_Sensor class attributes and methods

# Module class attributes and methods

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

# arduino_While class attributes and methods

# arduino_Expression class attributes and methods

# arduino_BinaryExpression class attributes and methods

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

# arduino_UnaryExpression class attributes and methods

# arduino_UnaryBooleanExpression class attributes and methods
arduino_UnaryBooleanExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryBooleanExpression.attributes={arduino_UnaryBooleanExpression_operator}

# UnaryExpression class attributes and methods

# arduino_UnaryIntegerExpression class attributes and methods
arduino_UnaryIntegerExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryIntegerExpression.attributes={arduino_UnaryIntegerExpression_operator}

# arduino_VariableDeclaration class attributes and methods

# arduino_BooleanExpression class attributes and methods

# arduino_IntegerExpression class attributes and methods

# arduino_Assignment class attributes and methods

# arduino_IntegerVariable class attributes and methods
arduino_IntegerVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
arduino_IntegerVariable.attributes={arduino_IntegerVariable_initialValue}

# Variable class attributes and methods

# arduino_BooleanVariable class attributes and methods
arduino_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
arduino_BooleanVariable.attributes={arduino_BooleanVariable_initialValue}

# arduino_BooleanModuleGet class attributes and methods

# ModuleGet class attributes and methods

# arduino_IntegerModuleGet class attributes and methods

# arduino_VariableRef class attributes and methods

# arduino_Synchro class attributes and methods

# InstantaneousInstruction class attributes and methods

# arduino_InstantaneousInstruction class attributes and methods

# Relationships
hardware9: BinaryAssociation = BinaryAssociation(
    name="hardware9",
    ends={
        Property(name="arduino_Hardware10", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch", type=arduino_Hardware, multiplicity=Multiplicity(1, 1))
    }
)
instructions11: BinaryAssociation = BinaryAssociation(
    name="instructions11",
    ends={
        Property(name="arduino_Instruction", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch12", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hardware13: BinaryAssociation = BinaryAssociation(
    name="hardware13",
    ends={
        Property(name="arduino_Hardware14", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project", type=arduino_Hardware, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modules15: BinaryAssociation = BinaryAssociation(
    name="modules15",
    ends={
        Property(name="arduino_Module17", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project16", type=arduino_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platform18: BinaryAssociation = BinaryAssociation(
    name="platform18",
    ends={
        Property(name="arduino_Platform20", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project19", type=arduino_Platform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketchs21: BinaryAssociation = BinaryAssociation(
    name="sketchs21",
    ends={
        Property(name="arduino_Sketch23", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project22", type=arduino_Sketch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platforms0: BinaryAssociation = BinaryAssociation(
    name="platforms0",
    ends={
        Property(name="arduino_Platform", type=arduino_Hardware, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Hardware", type=arduino_Platform, multiplicity=Multiplicity(1, 9999))
    }
)
modules1: BinaryAssociation = BinaryAssociation(
    name="modules1",
    ends={
        Property(name="arduino_Module", type=arduino_Hardware, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Hardware2", type=arduino_Module, multiplicity=Multiplicity(0, 9999))
    }
)
connectors3: BinaryAssociation = BinaryAssociation(
    name="connectors3",
    ends={
        Property(name="arduino_Connector", type=arduino_Hardware, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Hardware4", type=arduino_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
digitalPins5: BinaryAssociation = BinaryAssociation(
    name="digitalPins5",
    ends={
        Property(name="arduino_DigitalPin", type=arduino_Platform, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Platform6", type=arduino_DigitalPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
analogPins7: BinaryAssociation = BinaryAssociation(
    name="analogPins7",
    ends={
        Property(name="arduino_AnalogPin", type=arduino_Platform, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Platform8", type=arduino_AnalogPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pin37: BinaryAssociation = BinaryAssociation(
    name="pin37",
    ends={
        Property(name="arduino_Pin", type=arduino_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Connector38", type=arduino_Pin, multiplicity=Multiplicity(0, 1))
    }
)
module39: BinaryAssociation = BinaryAssociation(
    name="module39",
    ends={
        Property(name="arduino_Module41", type=arduino_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Connector40", type=arduino_Module, multiplicity=Multiplicity(0, 1))
    }
)
module42: BinaryAssociation = BinaryAssociation(
    name="module42",
    ends={
        Property(name="arduino_Module43", type=arduino_ModuleGet, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleGet", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
previous25: BinaryAssociation = BinaryAssociation(
    name="previous25",
    ends={
        Property(name="arduino_Instruction26", type=arduino_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Instruction24", type=arduino_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
next28: BinaryAssociation = BinaryAssociation(
    name="next28",
    ends={
        Property(name="arduino_Instruction29", type=arduino_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Instruction27", type=arduino_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
dependency31: BinaryAssociation = BinaryAssociation(
    name="dependency31",
    ends={
        Property(name="arduino_Instruction32", type=arduino_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Instruction30", type=arduino_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
module33: BinaryAssociation = BinaryAssociation(
    name="module33",
    ends={
        Property(name="arduino_Module34", type=arduino_ModuleInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleInstruction", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
instructions35: BinaryAssociation = BinaryAssociation(
    name="instructions35",
    ends={
        Property(name="arduino_Instruction36", type=arduino_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Control", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition51: BinaryAssociation = BinaryAssociation(
    name="condition51",
    ends={
        Property(name="arduino_Expression52", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition44: BinaryAssociation = BinaryAssociation(
    name="condition44",
    ends={
        Property(name="arduino_Expression", type=arduino_While, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_While", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left45: BinaryAssociation = BinaryAssociation(
    name="left45",
    ends={
        Property(name="arduino_Expression46", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="arduino_Expression49", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression48", type=arduino_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable50: BinaryAssociation = BinaryAssociation(
    name="variable50",
    ends={
        Property(name="arduino_Variable", type=arduino_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableAssignment", type=arduino_Variable, multiplicity=Multiplicity(1, 1))
    }
)
operand55: BinaryAssociation = BinaryAssociation(
    name="operand55",
    ends={
        Property(name="arduino_Expression56", type=arduino_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_UnaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable57: BinaryAssociation = BinaryAssociation(
    name="variable57",
    ends={
        Property(name="arduino_Variable58", type=arduino_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableDeclaration", type=arduino_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand53: BinaryAssociation = BinaryAssociation(
    name="operand53",
    ends={
        Property(name="arduino_Expression54", type=arduino_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Assignment", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable59: BinaryAssociation = BinaryAssociation(
    name="variable59",
    ends={
        Property(name="arduino_Variable60", type=arduino_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_VariableRef", type=arduino_Variable, multiplicity=Multiplicity(1, 1))
    }
)
synchro62: BinaryAssociation = BinaryAssociation(
    name="synchro62",
    ends={
        Property(name="Synchro", type=arduino_Synchro, multiplicity=Multiplicity(1, 1)),
        Property(name="synchroeOpposite", type=arduino_Synchro, multiplicity=Multiplicity(0, 9999))
    }
)
synchroeOpposite64: BinaryAssociation = BinaryAssociation(
    name="synchroeOpposite64",
    ends={
        Property(name="Synchro65", type=arduino_Synchro, multiplicity=Multiplicity(1, 1)),
        Property(name="synchro", type=arduino_Synchro, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_arduino_Hardware_NamedElement = Generalization(general=NamedElement, specific=arduino_Hardware)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_Sketch_Instruction = Generalization(general=Instruction, specific=arduino_Sketch)
gen_arduino_Platform_NamedElement = Generalization(general=NamedElement, specific=arduino_Platform)
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_DigitalPin_Pin = Generalization(general=Pin, specific=arduino_DigitalPin)
gen_arduino_AnalogPin_Pin = Generalization(general=Pin, specific=arduino_AnalogPin)
gen_arduino_Actuator_Module = Generalization(general=Module, specific=arduino_Actuator)
gen_arduino_Repeat_Control = Generalization(general=Control, specific=arduino_Repeat)
gen_arduino_ModuleGet_Expression = Generalization(general=Expression, specific=arduino_ModuleGet)
gen_arduino_Instruction_NamedElement = Generalization(general=NamedElement, specific=arduino_Instruction)
gen_arduino_ModuleAssignment_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_ModuleAssignment)
gen_arduino_ModuleAssignment_Assignment = Generalization(general=Assignment, specific=arduino_ModuleAssignment)
gen_arduino_ModuleInstruction_Instruction = Generalization(general=Instruction, specific=arduino_ModuleInstruction)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_Utilities_Instruction = Generalization(general=Instruction, specific=arduino_Utilities)
gen_arduino_Delay_Utilities = Generalization(general=Utilities, specific=arduino_Delay)
gen_arduino_Sensor_Module = Generalization(general=Module, specific=arduino_Sensor)
gen_arduino_BinaryBooleanExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryBooleanExpression)
gen_arduino_BinaryBooleanExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BinaryBooleanExpression)
gen_arduino_Constant_Expression = Generalization(general=Expression, specific=arduino_Constant)
gen_arduino_If_Control = Generalization(general=Control, specific=arduino_If)
gen_arduino_IntegerConstant_Constant = Generalization(general=Constant, specific=arduino_IntegerConstant)
gen_arduino_IntegerConstant_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerConstant)
gen_arduino_BooleanConstant_Constant = Generalization(general=Constant, specific=arduino_BooleanConstant)
gen_arduino_BooleanConstant_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanConstant)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_BinaryExpression_Expression = Generalization(general=Expression, specific=arduino_BinaryExpression)
gen_arduino_Variable_Expression = Generalization(general=Expression, specific=arduino_Variable)
gen_arduino_Variable_NamedElement = Generalization(general=NamedElement, specific=arduino_Variable)
gen_arduino_VariableAssignment_Instruction = Generalization(general=Instruction, specific=arduino_VariableAssignment)
gen_arduino_VariableAssignment_Assignment = Generalization(general=Assignment, specific=arduino_VariableAssignment)
gen_arduino_BinaryIntegerExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_BinaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_BinaryIntegerExpression)
gen_arduino_UnaryExpression_Expression = Generalization(general=Expression, specific=arduino_UnaryExpression)
gen_arduino_UnaryBooleanExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=arduino_UnaryBooleanExpression)
gen_arduino_UnaryBooleanExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_UnaryBooleanExpression)
gen_arduino_UnaryIntegerExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=arduino_UnaryIntegerExpression)
gen_arduino_UnaryIntegerExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_UnaryIntegerExpression)
gen_arduino_VariableDeclaration_Instruction = Generalization(general=Instruction, specific=arduino_VariableDeclaration)
gen_arduino_BooleanExpression_Expression = Generalization(general=Expression, specific=arduino_BooleanExpression)
gen_arduino_IntegerExpression_Expression = Generalization(general=Expression, specific=arduino_IntegerExpression)
gen_arduino_Assignment_Instruction = Generalization(general=Instruction, specific=arduino_Assignment)
gen_arduino_IntegerVariable_Variable = Generalization(general=Variable, specific=arduino_IntegerVariable)
gen_arduino_IntegerVariable_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerVariable)
gen_arduino_BooleanVariable_Variable = Generalization(general=Variable, specific=arduino_BooleanVariable)
gen_arduino_BooleanVariable_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanVariable)
gen_arduino_BooleanModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_BooleanModuleGet)
gen_arduino_BooleanModuleGet_BooleanExpression = Generalization(general=BooleanExpression, specific=arduino_BooleanModuleGet)
gen_arduino_IntegerModuleGet_ModuleGet = Generalization(general=ModuleGet, specific=arduino_IntegerModuleGet)
gen_arduino_IntegerModuleGet_IntegerExpression = Generalization(general=IntegerExpression, specific=arduino_IntegerModuleGet)
gen_arduino_VariableRef_Expression = Generalization(general=Expression, specific=arduino_VariableRef)
gen_arduino_Synchro_InstantaneousInstruction = Generalization(general=InstantaneousInstruction, specific=arduino_Synchro)
gen_arduino_InstantaneousInstruction_Instruction = Generalization(general=Instruction, specific=arduino_InstantaneousInstruction)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Hardware, NamedElement, arduino_Sketch, Instruction, arduino_Instruction, arduino_Project, arduino_Platform, arduino_Module, arduino_Connector, arduino_DigitalPin, arduino_AnalogPin, Pin, arduino_Pin, arduino_Actuator, arduino_NamedElement, arduino_Repeat, Control, arduino_ModuleGet, Expression, arduino_ModuleAssignment, ModuleInstruction, Assignment, arduino_ModuleInstruction, arduino_Control, arduino_Utilities, arduino_Delay, Utilities, arduino_Sensor, Module, BooleanExpression, arduino_Constant, arduino_If, arduino_IntegerConstant, Constant, arduino_BooleanConstant, arduino_While, arduino_Expression, arduino_BinaryExpression, arduino_Variable, arduino_VariableAssignment, arduino_BinaryIntegerExpression, BinaryExpression, IntegerExpression, arduino_BinaryBooleanExpression, arduino_UnaryExpression, arduino_UnaryBooleanExpression, UnaryExpression, arduino_UnaryIntegerExpression, arduino_VariableDeclaration, arduino_BooleanExpression, arduino_IntegerExpression, arduino_Assignment, arduino_IntegerVariable, Variable, arduino_BooleanVariable, arduino_BooleanModuleGet, ModuleGet, arduino_IntegerModuleGet, arduino_VariableRef, arduino_Synchro, InstantaneousInstruction, arduino_InstantaneousInstruction, ModuleKind, Time, Library, BinaryIntegerOperatorKind, UnaryBooleanOperatorKind, BinaryBooleanOperatorKind, UnaryIntegerOperatorKind},
    associations={hardware9, instructions11, hardware13, modules15, platform18, sketchs21, platforms0, modules1, connectors3, digitalPins5, analogPins7, pin37, module39, module42, previous25, next28, dependency31, module33, instructions35, condition51, condition44, left45, right47, variable50, operand55, variable57, operand53, variable59, synchro62, synchroeOpposite64},
    generalizations={gen_arduino_Hardware_NamedElement, gen_arduino_Sketch_NamedElement, gen_arduino_Sketch_Instruction, gen_arduino_Platform_NamedElement, gen_arduino_Module_NamedElement, gen_arduino_DigitalPin_Pin, gen_arduino_AnalogPin_Pin, gen_arduino_Actuator_Module, gen_arduino_Repeat_Control, gen_arduino_ModuleGet_Expression, gen_arduino_Instruction_NamedElement, gen_arduino_ModuleAssignment_ModuleInstruction, gen_arduino_ModuleAssignment_Assignment, gen_arduino_ModuleInstruction_Instruction, gen_arduino_Control_Instruction, gen_arduino_Utilities_Instruction, gen_arduino_Delay_Utilities, gen_arduino_Sensor_Module, gen_arduino_BinaryBooleanExpression_BinaryExpression, gen_arduino_BinaryBooleanExpression_BooleanExpression, gen_arduino_Constant_Expression, gen_arduino_If_Control, gen_arduino_IntegerConstant_Constant, gen_arduino_IntegerConstant_IntegerExpression, gen_arduino_BooleanConstant_Constant, gen_arduino_BooleanConstant_BooleanExpression, gen_arduino_While_Control, gen_arduino_BinaryExpression_Expression, gen_arduino_Variable_Expression, gen_arduino_Variable_NamedElement, gen_arduino_VariableAssignment_Instruction, gen_arduino_VariableAssignment_Assignment, gen_arduino_BinaryIntegerExpression_BinaryExpression, gen_arduino_BinaryIntegerExpression_IntegerExpression, gen_arduino_UnaryExpression_Expression, gen_arduino_UnaryBooleanExpression_UnaryExpression, gen_arduino_UnaryBooleanExpression_BooleanExpression, gen_arduino_UnaryIntegerExpression_UnaryExpression, gen_arduino_UnaryIntegerExpression_IntegerExpression, gen_arduino_VariableDeclaration_Instruction, gen_arduino_BooleanExpression_Expression, gen_arduino_IntegerExpression_Expression, gen_arduino_Assignment_Instruction, gen_arduino_IntegerVariable_Variable, gen_arduino_IntegerVariable_IntegerExpression, gen_arduino_BooleanVariable_Variable, gen_arduino_BooleanVariable_BooleanExpression, gen_arduino_BooleanModuleGet_ModuleGet, gen_arduino_BooleanModuleGet_BooleanExpression, gen_arduino_IntegerModuleGet_ModuleGet, gen_arduino_IntegerModuleGet_IntegerExpression, gen_arduino_VariableRef_Expression, gen_arduino_Synchro_InstantaneousInstruction, gen_arduino_InstantaneousInstruction_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)