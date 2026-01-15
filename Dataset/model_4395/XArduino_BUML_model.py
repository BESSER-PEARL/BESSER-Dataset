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
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="le"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="ge"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="neq"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max"),
			EnumerationLiteral(name="mod")
    }
)

# Classes
arduino_NamedElement = Class(name="arduino::NamedElement", is_abstract=True)
arduino_Project = Class(name="arduino::Project")
NamedElement = Class(name="NamedElement")
arduino_Board = Class(name="arduino::Board")
arduino_Sketch = Class(name="arduino::Sketch")
arduino_Module = Class(name="arduino::Module", is_abstract=True)
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
arduino_WaitFor = Class(name="arduino::WaitFor")
arduino_Constant = Class(name="arduino::Constant")
Expression = Class(name="Expression")
arduino_UnaryExpression = Class(name="arduino::UnaryExpression")
arduino_BinaryExpression = Class(name="arduino::BinaryExpression")
arduino_ModuleGet = Class(name="arduino::ModuleGet")
arduino_Delay = Class(name="arduino::Delay")

# arduino_NamedElement class attributes and methods
arduino_NamedElement_name: Property = Property(name="name", type=StringType)
arduino_NamedElement.attributes={arduino_NamedElement_name}

# arduino_Project class attributes and methods

# NamedElement class attributes and methods

# arduino_Board class attributes and methods

# arduino_Sketch class attributes and methods
arduino_Sketch_m_execute: Method = Method(name="execute", parameters={})
arduino_Sketch.methods={arduino_Sketch_m_execute}

# arduino_Module class attributes and methods
arduino_Module_level: Property = Property(name="level", type=StringType)
arduino_Module.attributes={arduino_Module_level}

# arduino_OutputModule class attributes and methods

# Module class attributes and methods

# arduino_Led class attributes and methods

# OutputModule class attributes and methods

# arduino_InputModule class attributes and methods

# arduino_PushButton class attributes and methods
arduino_PushButton_m_press: Method = Method(name="press", parameters={})
arduino_PushButton_m_release: Method = Method(name="release", parameters={})
arduino_PushButton.methods={arduino_PushButton_m_press, arduino_PushButton_m_release}

# InputModule class attributes and methods

# arduino_Block class attributes and methods
arduino_Block_m_execute: Method = Method(name="execute", parameters={})
arduino_Block.methods={arduino_Block_m_execute}

# arduino_Instruction class attributes and methods
arduino_Instruction_m_execute: Method = Method(name="execute", parameters={})
arduino_Instruction_m_finalize: Method = Method(name="finalize", parameters={})
arduino_Instruction.methods={arduino_Instruction_m_execute, arduino_Instruction_m_finalize}

# arduino_Control class attributes and methods
arduino_Control_m_execute: Method = Method(name="execute", parameters={})
arduino_Control.methods={arduino_Control_m_execute}

# Instruction class attributes and methods

# arduino_If class attributes and methods
arduino_If_m_execute: Method = Method(name="execute", parameters={})
arduino_If.methods={arduino_If_m_execute}

# Control class attributes and methods

# arduino_Expression class attributes and methods
arduino_Expression_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_Expression.methods={arduino_Expression_m_evaluate}

# arduino_While class attributes and methods
arduino_While_m_execute: Method = Method(name="execute", parameters={})
arduino_While.methods={arduino_While_m_execute}

# arduino_ModuleSet class attributes and methods
arduino_ModuleSet_m_execute: Method = Method(name="execute", parameters={})
arduino_ModuleSet.methods={arduino_ModuleSet_m_execute}

# arduino_SetLed class attributes and methods
arduino_SetLed_m_execute: Method = Method(name="execute", parameters={})
arduino_SetLed.methods={arduino_SetLed_m_execute}

# ModuleSet class attributes and methods

# arduino_WaitFor class attributes and methods
arduino_WaitFor_m_execute: Method = Method(name="execute", parameters={})
arduino_WaitFor_m_setActivated: Method = Method(name="setActivated", parameters={})
arduino_WaitFor.methods={arduino_WaitFor_m_setActivated, arduino_WaitFor_m_execute}

# arduino_Constant class attributes and methods
arduino_Constant_value: Property = Property(name="value", type=StringType)
arduino_Constant_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_Constant.attributes={arduino_Constant_value}
arduino_Constant.methods={arduino_Constant_m_evaluate}

# Expression class attributes and methods

# arduino_UnaryExpression class attributes and methods
arduino_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
arduino_UnaryExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_UnaryExpression.attributes={arduino_UnaryExpression_operator}
arduino_UnaryExpression.methods={arduino_UnaryExpression_m_evaluate}

# arduino_BinaryExpression class attributes and methods
arduino_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
arduino_BinaryExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_BinaryExpression.attributes={arduino_BinaryExpression_operator}
arduino_BinaryExpression.methods={arduino_BinaryExpression_m_evaluate}

# arduino_ModuleGet class attributes and methods
arduino_ModuleGet_m_evaluate: Method = Method(name="evaluate", parameters={})
arduino_ModuleGet.methods={arduino_ModuleGet_m_evaluate}

# arduino_Delay class attributes and methods
arduino_Delay_value: Property = Property(name="value", type=StringType)
arduino_Delay_m_execute: Method = Method(name="execute", parameters={})
arduino_Delay.attributes={arduino_Delay_value}
arduino_Delay.methods={arduino_Delay_m_execute}

# Relationships
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
led19: BinaryAssociation = BinaryAssociation(
    name="led19",
    ends={
        Property(name="arduino_Led", type=arduino_SetLed, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_SetLed", type=arduino_Led, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_arduino_Project_NamedElement = Generalization(general=NamedElement, specific=arduino_Project)
gen_arduino_Board_NamedElement = Generalization(general=NamedElement, specific=arduino_Board)
gen_arduino_Module_NamedElement = Generalization(general=NamedElement, specific=arduino_Module)
gen_arduino_OutputModule_Module = Generalization(general=Module, specific=arduino_OutputModule)
gen_arduino_Led_OutputModule = Generalization(general=OutputModule, specific=arduino_Led)
gen_arduino_InputModule_Module = Generalization(general=Module, specific=arduino_InputModule)
gen_arduino_PushButton_InputModule = Generalization(general=InputModule, specific=arduino_PushButton)
gen_arduino_Control_Instruction = Generalization(general=Instruction, specific=arduino_Control)
gen_arduino_If_Control = Generalization(general=Control, specific=arduino_If)
gen_arduino_While_Control = Generalization(general=Control, specific=arduino_While)
gen_arduino_ModuleSet_Instruction = Generalization(general=Instruction, specific=arduino_ModuleSet)
gen_arduino_SetLed_ModuleSet = Generalization(general=ModuleSet, specific=arduino_SetLed)
gen_arduino_Sketch_NamedElement = Generalization(general=NamedElement, specific=arduino_Sketch)
gen_arduino_WaitFor_Instruction = Generalization(general=Instruction, specific=arduino_WaitFor)
gen_arduino_Constant_Expression = Generalization(general=Expression, specific=arduino_Constant)
gen_arduino_UnaryExpression_Expression = Generalization(general=Expression, specific=arduino_UnaryExpression)
gen_arduino_BinaryExpression_Expression = Generalization(general=Expression, specific=arduino_BinaryExpression)
gen_arduino_ModuleGet_Expression = Generalization(general=Expression, specific=arduino_ModuleGet)
gen_arduino_Delay_Instruction = Generalization(general=Instruction, specific=arduino_Delay)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_NamedElement, arduino_Project, NamedElement, arduino_Board, arduino_Sketch, arduino_Module, arduino_OutputModule, Module, arduino_Led, OutputModule, arduino_InputModule, arduino_PushButton, InputModule, arduino_Block, arduino_Instruction, arduino_Control, Instruction, arduino_If, Control, arduino_Expression, arduino_While, arduino_ModuleSet, arduino_SetLed, ModuleSet, arduino_WaitFor, arduino_Constant, Expression, arduino_UnaryExpression, arduino_BinaryExpression, arduino_ModuleGet, arduino_Delay, UnaryOperatorKind, BinaryOperatorKind},
    associations={board0, sketch1, modules3, block5, instructions7, block9, condition11, elseBlock12, condition15, value17, module20, value22, operand24, left26, right28, module31, led19},
    generalizations={gen_arduino_Project_NamedElement, gen_arduino_Board_NamedElement, gen_arduino_Module_NamedElement, gen_arduino_OutputModule_Module, gen_arduino_Led_OutputModule, gen_arduino_InputModule_Module, gen_arduino_PushButton_InputModule, gen_arduino_Control_Instruction, gen_arduino_If_Control, gen_arduino_While_Control, gen_arduino_ModuleSet_Instruction, gen_arduino_SetLed_ModuleSet, gen_arduino_Sketch_NamedElement, gen_arduino_WaitFor_Instruction, gen_arduino_Constant_Expression, gen_arduino_UnaryExpression_Expression, gen_arduino_BinaryExpression_Expression, gen_arduino_ModuleGet_Expression, gen_arduino_Delay_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)