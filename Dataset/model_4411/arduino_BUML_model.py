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

ModuleKind: Enumeration = Enumeration(
    name="ModuleKind",
    literals={
            EnumerationLiteral(name="digital"),
			EnumerationLiteral(name="analog")
    }
)

OperatorKind: Enumeration = Enumeration(
    name="OperatorKind",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="upper"),
			EnumerationLiteral(name="lower"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="diff"),
			EnumerationLiteral(name="upperOrEqual"),
			EnumerationLiteral(name="lowerOrEqual"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max"),
			EnumerationLiteral(name="pourcent"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="not")
    }
)

ParameterType: Enumeration = Enumeration(
    name="ParameterType",
    literals={
            EnumerationLiteral(name="Delay"),
			EnumerationLiteral(name="Level"),
			EnumerationLiteral(name="Status"),
			EnumerationLiteral(name="Constant"),
			EnumerationLiteral(name="Sensor")
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

# Classes
arduino_Connector = Class(name="arduino::Connector")
arduino_DigitalPin = Class(name="arduino::DigitalPin")
arduino_AnalogPin = Class(name="arduino::AnalogPin")
Pin = Class(name="Pin")
arduino_Pin = Class(name="arduino::Pin", is_abstract=True)
arduino_Sketch = Class(name="arduino::Sketch")
Instruction = Class(name="Instruction")
arduino_Instruction = Class(name="arduino::Instruction", is_abstract=True)
arduino_Function = Class(name="arduino::Function")
arduino_Project = Class(name="arduino::Project")
arduino_Hardware = Class(name="arduino::Hardware")
NamedElement = Class(name="NamedElement")
arduino_Platform = Class(name="arduino::Platform")
arduino_Module = Class(name="arduino::Module", is_abstract=True)
arduino_Status = Class(name="arduino::Status")
ModuleInstruction = Class(name="ModuleInstruction")
Value = Class(name="Value")
arduino_Sensor = Class(name="arduino::Sensor")
arduino_Level = Class(name="arduino::Level")
arduino_Value = Class(name="arduino::Value", is_abstract=True)
arduino_ModuleInstruction = Class(name="arduino::ModuleInstruction", is_abstract=True)
Parameter_ = Class(name="Parameter")
arduino_Control = Class(name="arduino::Control", is_abstract=True)
arduino_Utilities = Class(name="arduino::Utilities", is_abstract=True)
arduino_IO = Class(name="arduino::IO", is_abstract=True)
arduino_Delay = Class(name="arduino::Delay")
Utilities = Class(name="Utilities")
arduino_InputModule = Class(name="arduino::InputModule")
Module = Class(name="Module")
arduino_OutputModule = Class(name="arduino::OutputModule")
arduino_NamedElement = Class(name="arduino::NamedElement", is_abstract=True)
arduino_While = Class(name="arduino::While")
arduino_BooleanOperator = Class(name="arduino::BooleanOperator")
arduino_MathOperator = Class(name="arduino::MathOperator", is_abstract=True)
arduino_Variable = Class(name="arduino::Variable")
arduino_Set = Class(name="arduino::Set")
arduino_NumericalOperator = Class(name="arduino::NumericalOperator")
MathOperator = Class(name="MathOperator")
arduino_Repeat = Class(name="arduino::Repeat")
Control = Class(name="Control")
BooleanOperator = Class(name="BooleanOperator")
arduino_ParameterDefinition = Class(name="arduino::ParameterDefinition")
arduino_Parameter = Class(name="arduino::Parameter", is_abstract=True)
arduino_FunctionCall = Class(name="arduino::FunctionCall")
arduino_ParameterCall = Class(name="arduino::ParameterCall")
arduino_Constant = Class(name="arduino::Constant")
arduino_If = Class(name="arduino::If")

# arduino_Connector class attributes and methods

# arduino_DigitalPin class attributes and methods

# arduino_AnalogPin class attributes and methods

# Pin class attributes and methods

# arduino_Pin class attributes and methods
arduino_Pin_id: Property = Property(name="id", type=IntegerType)
arduino_Pin.attributes={arduino_Pin_id}

# arduino_Sketch class attributes and methods

# Instruction class attributes and methods

# arduino_Instruction class attributes and methods

# arduino_Function class attributes and methods
arduino_Function_name: Property = Property(name="name", type=StringType)
arduino_Function.attributes={arduino_Function_name}

# arduino_Project class attributes and methods

# arduino_Hardware class attributes and methods

# NamedElement class attributes and methods

# arduino_Platform class attributes and methods
arduino_Platform_image: Property = Property(name="image", type=StringType)
arduino_Platform.attributes={arduino_Platform_image}

# arduino_Module class attributes and methods
arduino_Module_kind: Property = Property(name="kind", type=StringType)
arduino_Module_image: Property = Property(name="image", type=StringType)
arduino_Module_level: Property = Property(name="level", type=BooleanType)
arduino_Module_library: Property = Property(name="library", type=StringType)
arduino_Module.attributes={arduino_Module_level, arduino_Module_image, arduino_Module_kind, arduino_Module_library}

# arduino_Status class attributes and methods
arduino_Status_status: Property = Property(name="status", type=BooleanType)
arduino_Status.attributes={arduino_Status_status}

# ModuleInstruction class attributes and methods

# Value class attributes and methods

# arduino_Sensor class attributes and methods

# arduino_Level class attributes and methods

# arduino_Value class attributes and methods
arduino_Value_value: Property = Property(name="value", type=StringType)
arduino_Value.attributes={arduino_Value_value}

# arduino_ModuleInstruction class attributes and methods

# Parameter class attributes and methods

# arduino_Control class attributes and methods

# arduino_Utilities class attributes and methods

# arduino_IO class attributes and methods

# arduino_Delay class attributes and methods
arduino_Delay_unit: Property = Property(name="unit", type=StringType)
arduino_Delay_value: Property = Property(name="value", type=IntegerType)
arduino_Delay.attributes={arduino_Delay_value, arduino_Delay_unit}

# Utilities class attributes and methods

# arduino_InputModule class attributes and methods

# Module class attributes and methods

# arduino_OutputModule class attributes and methods

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_While class attributes and methods

# arduino_BooleanOperator class attributes and methods

# arduino_MathOperator class attributes and methods
arduino_MathOperator_operator: Property = Property(name="operator", type=StringType)
arduino_MathOperator.attributes={arduino_MathOperator_operator}

# arduino_Variable class attributes and methods
arduino_Variable_name: Property = Property(name="name", type=StringType)
arduino_Variable.attributes={arduino_Variable_name}

# arduino_Set class attributes and methods

# arduino_NumericalOperator class attributes and methods

# MathOperator class attributes and methods

# arduino_Repeat class attributes and methods
arduino_Repeat_iteration: Property = Property(name="iteration", type=IntegerType)
arduino_Repeat.attributes={arduino_Repeat_iteration}

# Control class attributes and methods

# BooleanOperator class attributes and methods

# arduino_ParameterDefinition class attributes and methods
arduino_ParameterDefinition_type: Property = Property(name="type", type=StringType)
arduino_ParameterDefinition_name: Property = Property(name="name", type=StringType)
arduino_ParameterDefinition.attributes={arduino_ParameterDefinition_name, arduino_ParameterDefinition_type}

# arduino_Parameter class attributes and methods

# arduino_FunctionCall class attributes and methods

# arduino_ParameterCall class attributes and methods

# arduino_Constant class attributes and methods

# arduino_If class attributes and methods

# Relationships
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
functions13: BinaryAssociation = BinaryAssociation(
    name="functions13",
    ends={
        Property(name="arduino_Function", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch14", type=arduino_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hardware15: BinaryAssociation = BinaryAssociation(
    name="hardware15",
    ends={
        Property(name="arduino_Hardware16", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project", type=arduino_Hardware, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sketch17: BinaryAssociation = BinaryAssociation(
    name="sketch17",
    ends={
        Property(name="arduino_Sketch19", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project18", type=arduino_Sketch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
platforms0: BinaryAssociation = BinaryAssociation(
    name="platforms0",
    ends={
        Property(name="arduino_Platform", type=arduino_Hardware, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Hardware", type=arduino_Platform, multiplicity=Multiplicity(1, 9999))
    }
)
next30: BinaryAssociation = BinaryAssociation(
    name="next30",
    ends={
        Property(name="arduino_Instruction31", type=arduino_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Instruction29", type=arduino_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
sensor32: BinaryAssociation = BinaryAssociation(
    name="sensor32",
    ends={
        Property(name="Sensor", type=arduino_Status, multiplicity=Multiplicity(1, 1)),
        Property(name="status", type=arduino_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
level33: BinaryAssociation = BinaryAssociation(
    name="level33",
    ends={
        Property(name="arduino_Value", type=arduino_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Level", type=arduino_Value, multiplicity=Multiplicity(1, 1))
    }
)
module34: BinaryAssociation = BinaryAssociation(
    name="module34",
    ends={
        Property(name="arduino_Module35", type=arduino_ModuleInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleInstruction", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
instructions36: BinaryAssociation = BinaryAssociation(
    name="instructions36",
    ends={
        Property(name="arduino_Instruction37", type=arduino_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Control", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules20: BinaryAssociation = BinaryAssociation(
    name="modules20",
    ends={
        Property(name="arduino_Module22", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project21", type=arduino_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platform23: BinaryAssociation = BinaryAssociation(
    name="platform23",
    ends={
        Property(name="arduino_Platform25", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project24", type=arduino_Platform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
previous27: BinaryAssociation = BinaryAssociation(
    name="previous27",
    ends={
        Property(name="arduino_Instruction28", type=arduino_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Instruction26", type=arduino_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
status43: BinaryAssociation = BinaryAssociation(
    name="status43",
    ends={
        Property(name="Status", type=arduino_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor", type=arduino_Status, multiplicity=Multiplicity(0, 9999))
    }
)
condition44: BinaryAssociation = BinaryAssociation(
    name="condition44",
    ends={
        Property(name="arduino_BooleanOperator", type=arduino_While, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_While", type=arduino_BooleanOperator, multiplicity=Multiplicity(1, 1))
    }
)
left45: BinaryAssociation = BinaryAssociation(
    name="left45",
    ends={
        Property(name="arduino_Value46", type=arduino_MathOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_MathOperator", type=arduino_Value, multiplicity=Multiplicity(1, 1))
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="arduino_Value49", type=arduino_MathOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_MathOperator48", type=arduino_Value, multiplicity=Multiplicity(0, 1))
    }
)
variable50: BinaryAssociation = BinaryAssociation(
    name="variable50",
    ends={
        Property(name="arduino_Variable", type=arduino_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Set", type=arduino_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="arduino_Value53", type=arduino_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Set52", type=arduino_Value, multiplicity=Multiplicity(1, 1))
    }
)
pin38: BinaryAssociation = BinaryAssociation(
    name="pin38",
    ends={
        Property(name="arduino_Pin", type=arduino_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Connector39", type=arduino_Pin, multiplicity=Multiplicity(0, 1))
    }
)
module40: BinaryAssociation = BinaryAssociation(
    name="module40",
    ends={
        Property(name="arduino_Module42", type=arduino_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Connector41", type=arduino_Module, multiplicity=Multiplicity(0, 1))
    }
)
condition54: BinaryAssociation = BinaryAssociation(
    name="condition54",
    ends={
        Property(name="arduino_BooleanOperator55", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If", type=arduino_BooleanOperator, multiplicity=Multiplicity(1, 1))
    }
)
paramDefs56: BinaryAssociation = BinaryAssociation(
    name="paramDefs56",
    ends={
        Property(name="arduino_ParameterDefinition", type=arduino_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Function57", type=arduino_ParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions58: BinaryAssociation = BinaryAssociation(
    name="instructions58",
    ends={
        Property(name="arduino_Instruction60", type=arduino_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Function59", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition61: BinaryAssociation = BinaryAssociation(
    name="definition61",
    ends={
        Property(name="arduino_ParameterDefinition62", type=arduino_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Parameter", type=arduino_ParameterDefinition, multiplicity=Multiplicity(0, 1))
    }
)
definition63: BinaryAssociation = BinaryAssociation(
    name="definition63",
    ends={
        Property(name="arduino_Function64", type=arduino_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_FunctionCall", type=arduino_Function, multiplicity=Multiplicity(1, 1))
    }
)
parameters65: BinaryAssociation = BinaryAssociation(
    name="parameters65",
    ends={
        Property(name="arduino_Parameter67", type=arduino_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_FunctionCall66", type=arduino_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
definition68: BinaryAssociation = BinaryAssociation(
    name="definition68",
    ends={
        Property(name="arduino_ParameterDefinition69", type=arduino_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ParameterCall", type=arduino_ParameterDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_arduino_Platform_NamedElement = Generalization(general=NamedElement, specific=arduino_Platform)
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_DigitalPin_Pin = Generalization(general=Pin, specific=arduino_DigitalPin)
gen_arduino_AnalogPin_Pin = Generalization(general=Pin, specific=arduino_AnalogPin)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_Sketch_Instruction = Generalization(general=Instruction, specific=arduino_Sketch)
gen_arduino_Hardware_NamedElement = Generalization(general=NamedElement, specific=arduino_Hardware)
gen_arduino_Status_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_Status)
gen_arduino_Status_Value = Generalization(general=Value, specific=arduino_Status)
gen_arduino_Level_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_Level)
gen_arduino_ModuleInstruction_Instruction = Generalization(general=Instruction, specific=arduino_ModuleInstruction)
gen_arduino_ModuleInstruction_Parameter = Generalization(general=Parameter_, specific=arduino_ModuleInstruction)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_Utilities_Instruction = Generalization(general=Instruction, specific=arduino_Utilities)
gen_arduino_Utilities_Parameter = Generalization(general=Parameter_, specific=arduino_Utilities)
gen_arduino_IO_Instruction = Generalization(general=Instruction, specific=arduino_IO)
gen_arduino_Delay_Utilities = Generalization(general=Utilities, specific=arduino_Delay)
gen_arduino_InputModule_Module = Generalization(general=Module, specific=arduino_InputModule)
gen_arduino_OutputModule_Module = Generalization(general=Module, specific=arduino_OutputModule)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_MathOperator_Value = Generalization(general=Value, specific=arduino_MathOperator)
gen_arduino_MathOperator_Instruction = Generalization(general=Instruction, specific=arduino_MathOperator)
gen_arduino_Variable_Value = Generalization(general=Value, specific=arduino_Variable)
gen_arduino_Variable_Instruction = Generalization(general=Instruction, specific=arduino_Variable)
gen_arduino_Set_Instruction = Generalization(general=Instruction, specific=arduino_Set)
gen_arduino_NumericalOperator_MathOperator = Generalization(general=MathOperator, specific=arduino_NumericalOperator)
gen_arduino_BooleanOperator_MathOperator = Generalization(general=MathOperator, specific=arduino_BooleanOperator)
gen_arduino_Value_Instruction = Generalization(general=Instruction, specific=arduino_Value)
gen_arduino_Value_Parameter = Generalization(general=Parameter_, specific=arduino_Value)
gen_arduino_Repeat_Control = Generalization(general=Control, specific=arduino_Repeat)
gen_arduino_Sensor_ModuleInstruction = Generalization(general=ModuleInstruction, specific=arduino_Sensor)
gen_arduino_Sensor_BooleanOperator = Generalization(general=BooleanOperator, specific=arduino_Sensor)
gen_arduino_FunctionCall_Instruction = Generalization(general=Instruction, specific=arduino_FunctionCall)
gen_arduino_ParameterCall_Instruction = Generalization(general=Instruction, specific=arduino_ParameterCall)
gen_arduino_Constant_Value = Generalization(general=Value, specific=arduino_Constant)
gen_arduino_If_Control = Generalization(general=Control, specific=arduino_If)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Connector, arduino_DigitalPin, arduino_AnalogPin, Pin, arduino_Pin, arduino_Sketch, Instruction, arduino_Instruction, arduino_Function, arduino_Project, arduino_Hardware, NamedElement, arduino_Platform, arduino_Module, arduino_Status, ModuleInstruction, Value, arduino_Sensor, arduino_Level, arduino_Value, arduino_ModuleInstruction, Parameter_, arduino_Control, arduino_Utilities, arduino_IO, arduino_Delay, Utilities, arduino_InputModule, Module, arduino_OutputModule, arduino_NamedElement, arduino_While, arduino_BooleanOperator, arduino_MathOperator, arduino_Variable, arduino_Set, arduino_NumericalOperator, MathOperator, arduino_Repeat, Control, BooleanOperator, arduino_ParameterDefinition, arduino_Parameter, arduino_FunctionCall, arduino_ParameterCall, arduino_Constant, arduino_If, Time, ModuleKind, OperatorKind, ParameterType, Library},
    associations={modules1, connectors3, digitalPins5, analogPins7, hardware9, instructions11, functions13, hardware15, sketch17, platforms0, next30, sensor32, level33, module34, instructions36, modules20, platform23, previous27, status43, condition44, left45, right47, variable50, value51, pin38, module40, condition54, paramDefs56, instructions58, definition61, definition63, parameters65, definition68},
    generalizations={gen_arduino_Platform_NamedElement, gen_arduino_Module_NamedElement, gen_arduino_DigitalPin_Pin, gen_arduino_AnalogPin_Pin, gen_arduino_Sketch_NamedElement, gen_arduino_Sketch_Instruction, gen_arduino_Hardware_NamedElement, gen_arduino_Status_ModuleInstruction, gen_arduino_Status_Value, gen_arduino_Level_ModuleInstruction, gen_arduino_ModuleInstruction_Instruction, gen_arduino_ModuleInstruction_Parameter, gen_arduino_Control_Instruction, gen_arduino_Utilities_Instruction, gen_arduino_Utilities_Parameter, gen_arduino_IO_Instruction, gen_arduino_Delay_Utilities, gen_arduino_InputModule_Module, gen_arduino_OutputModule_Module, gen_arduino_While_Control, gen_arduino_MathOperator_Value, gen_arduino_MathOperator_Instruction, gen_arduino_Variable_Value, gen_arduino_Variable_Instruction, gen_arduino_Set_Instruction, gen_arduino_NumericalOperator_MathOperator, gen_arduino_BooleanOperator_MathOperator, gen_arduino_Value_Instruction, gen_arduino_Value_Parameter, gen_arduino_Repeat_Control, gen_arduino_Sensor_ModuleInstruction, gen_arduino_Sensor_BooleanOperator, gen_arduino_FunctionCall_Instruction, gen_arduino_ParameterCall_Instruction, gen_arduino_Constant_Value, gen_arduino_If_Control},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)