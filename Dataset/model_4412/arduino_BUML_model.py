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
UnaryOperatorKind: Enumeration = Enumeration(
    name="UnaryOperatorKind",
    literals={
            EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="neg")
    }
)

BinaryOperatorKind: Enumeration = Enumeration(
    name="BinaryOperatorKind",
    literals={
            EnumerationLiteral(name="sub"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max"),
			EnumerationLiteral(name="mod"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="le"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="ge"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="neq")
    }
)

# Classes
arduino_NamedElement = Class(name="arduino::NamedElement", is_abstract=True)
arduino_Project = Class(name="arduino::Project")
NamedElement = Class(name="NamedElement")
arduino_Board = Class(name="arduino::Board")
arduino_OutputModule = Class(name="arduino::OutputModule", is_abstract=True)
Module = Class(name="Module")
arduino_Led = Class(name="arduino::Led")
OutputModule = Class(name="OutputModule")
arduino_InputModule = Class(name="arduino::InputModule", is_abstract=True)
arduino_PushButton = Class(name="arduino::PushButton")
InputModule = Class(name="InputModule")
arduino_Block = Class(name="arduino::Block")
arduino_Instruction = Class(name="arduino::Instruction", is_abstract=True)
arduino_Control = Class(name="arduino::Control", is_abstract=True)
Instruction = Class(name="Instruction")
arduino_If = Class(name="arduino::If")
Control = Class(name="Control")
arduino_Expression = Class(name="arduino::Expression", is_abstract=True)
arduino_While = Class(name="arduino::While")
arduino_ModuleSet = Class(name="arduino::ModuleSet", is_abstract=True)
arduino_SetLed = Class(name="arduino::SetLed")
ModuleSet = Class(name="ModuleSet")
arduino_Delay = Class(name="arduino::Delay")
arduino_Sketch = Class(name="arduino::Sketch")
arduino_Module = Class(name="arduino::Module", is_abstract=True)
arduino_UnaryExpression = Class(name="arduino::UnaryExpression")
arduino_BinaryExpression = Class(name="arduino::BinaryExpression")
arduino_ModuleGet = Class(name="arduino::ModuleGet")
arduino_WaitFor = Class(name="arduino::WaitFor")
arduino_Constant = Class(name="arduino::Constant")
Expression = Class(name="Expression")

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_Project class attributes and methods

# NamedElement class attributes and methods

# arduino_Board class attributes and methods

# arduino_OutputModule class attributes and methods

# Module class attributes and methods

# arduino_Led class attributes and methods

# OutputModule class attributes and methods

# arduino_InputModule class attributes and methods

# arduino_PushButton class attributes and methods

# InputModule class attributes and methods

# arduino_Block class attributes and methods

# arduino_Instruction class attributes and methods

# arduino_Control class attributes and methods

# Instruction class attributes and methods

# arduino_If class attributes and methods

# Control class attributes and methods

# arduino_Expression class attributes and methods

# arduino_While class attributes and methods

# arduino_ModuleSet class attributes and methods

# arduino_SetLed class attributes and methods

# ModuleSet class attributes and methods

# arduino_Delay class attributes and methods
arduino_Delay_value: Property = Property(name="value", type=IntegerType)
arduino_Delay.attributes={arduino_Delay_value}

# arduino_Sketch class attributes and methods

# arduino_Module class attributes and methods

# arduino_UnaryExpression class attributes and methods
arduino_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryExpression.attributes={arduino_UnaryExpression_operator}

# arduino_BinaryExpression class attributes and methods
arduino_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
arduino_BinaryExpression.attributes={arduino_BinaryExpression_operator}

# arduino_ModuleGet class attributes and methods

# arduino_WaitFor class attributes and methods

# arduino_Constant class attributes and methods
arduino_Constant_value: Property = Property(name="value", type=IntegerType)
arduino_Constant.attributes={arduino_Constant_value}

# Expression class attributes and methods

# Relationships
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="arduino_Block", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch6", type=arduino_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions7: BinaryAssociation = BinaryAssociation(
    name="instructions7",
    ends={
        Property(name="arduino_Instruction", type=arduino_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Block8", type=arduino_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block9: BinaryAssociation = BinaryAssociation(
    name="block9",
    ends={
        Property(name="arduino_Block10", type=arduino_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Control", type=arduino_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition11: BinaryAssociation = BinaryAssociation(
    name="condition11",
    ends={
        Property(name="arduino_Expression", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock12: BinaryAssociation = BinaryAssociation(
    name="elseBlock12",
    ends={
        Property(name="arduino_Block14", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If13", type=arduino_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="arduino_Expression16", type=arduino_While, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_While", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="arduino_Expression18", type=arduino_ModuleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleSet", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
led19: BinaryAssociation = BinaryAssociation(
    name="led19",
    ends={
        Property(name="arduino_Led", type=arduino_SetLed, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_SetLed", type=arduino_Led, multiplicity=Multiplicity(1, 1))
    }
)
board0: BinaryAssociation = BinaryAssociation(
    name="board0",
    ends={
        Property(name="arduino_Board", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project", type=arduino_Board, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sketch1: BinaryAssociation = BinaryAssociation(
    name="sketch1",
    ends={
        Property(name="arduino_Sketch", type=arduino_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Project2", type=arduino_Sketch, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modules3: BinaryAssociation = BinaryAssociation(
    name="modules3",
    ends={
        Property(name="arduino_Module", type=arduino_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Board4", type=arduino_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand24: BinaryAssociation = BinaryAssociation(
    name="operand24",
    ends={
        Property(name="arduino_Expression25", type=arduino_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_UnaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left26: BinaryAssociation = BinaryAssociation(
    name="left26",
    ends={
        Property(name="arduino_Expression27", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression", type=arduino_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="arduino_Expression30", type=arduino_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_BinaryExpression29", type=arduino_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module31: BinaryAssociation = BinaryAssociation(
    name="module31",
    ends={
        Property(name="arduino_Module32", type=arduino_ModuleGet, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ModuleGet", type=arduino_Module, multiplicity=Multiplicity(1, 1))
    }
)
module20: BinaryAssociation = BinaryAssociation(
    name="module20",
    ends={
        Property(name="arduino_Module21", type=arduino_WaitFor, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_WaitFor", type=arduino_Module, multiplicity=Multiplicity(0, 1))
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="arduino_Constant", type=arduino_WaitFor, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_WaitFor23", type=arduino_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_arduino_Project_NamedElement = Generalization(general=NamedElement, specific=arduino_Project)
gen_arduino_OutputModule_Module = Generalization(general=Module, specific=arduino_OutputModule)
gen_arduino_Led_OutputModule = Generalization(general=OutputModule, specific=arduino_Led)
gen_arduino_InputModule_Module = Generalization(general=Module, specific=arduino_InputModule)
gen_arduino_PushButton_InputModule = Generalization(general=InputModule, specific=arduino_PushButton)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_If_Control = Generalization(general=Control, specific=arduino_If)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_ModuleSet_Instruction = Generalization(general=Instruction, specific=arduino_ModuleSet)
gen_arduino_SetLed_ModuleSet = Generalization(general=ModuleSet, specific=arduino_SetLed)
gen_arduino_Delay_Instruction = Generalization(general=Instruction, specific=arduino_Delay)
gen_arduino_Board_NamedElement = Generalization(general=NamedElement, specific=arduino_Board)
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_UnaryExpression_Expression = Generalization(general=Expression, specific=arduino_UnaryExpression)
gen_arduino_BinaryExpression_Expression = Generalization(general=Expression, specific=arduino_BinaryExpression)
gen_arduino_ModuleGet_Expression = Generalization(general=Expression, specific=arduino_ModuleGet)
gen_arduino_WaitFor_Instruction = Generalization(general=Instruction, specific=arduino_WaitFor)
gen_arduino_Constant_Expression = Generalization(general=Expression, specific=arduino_Constant)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_NamedElement, arduino_Project, NamedElement, arduino_Board, arduino_OutputModule, Module, arduino_Led, OutputModule, arduino_InputModule, arduino_PushButton, InputModule, arduino_Block, arduino_Instruction, arduino_Control, Instruction, arduino_If, Control, arduino_Expression, arduino_While, arduino_ModuleSet, arduino_SetLed, ModuleSet, arduino_Delay, arduino_Sketch, arduino_Module, arduino_UnaryExpression, arduino_BinaryExpression, arduino_ModuleGet, arduino_WaitFor, arduino_Constant, Expression, UnaryOperatorKind, BinaryOperatorKind},
    associations={block5, instructions7, block9, condition11, elseBlock12, condition15, value17, led19, board0, sketch1, modules3, operand24, left26, right28, module31, module20, value22},
    generalizations={gen_arduino_Project_NamedElement, gen_arduino_OutputModule_Module, gen_arduino_Led_OutputModule, gen_arduino_InputModule_Module, gen_arduino_PushButton_InputModule, gen_arduino_Sketch_NamedElement, gen_arduino_Control_Instruction, gen_arduino_If_Control, gen_arduino_While_Control, gen_arduino_ModuleSet_Instruction, gen_arduino_SetLed_ModuleSet, gen_arduino_Delay_Instruction, gen_arduino_Board_NamedElement, gen_arduino_Module_NamedElement, gen_arduino_UnaryExpression_Expression, gen_arduino_BinaryExpression_Expression, gen_arduino_ModuleGet_Expression, gen_arduino_WaitFor_Instruction, gen_arduino_Constant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)