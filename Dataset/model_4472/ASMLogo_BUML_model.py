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

# Classes
kmlogo_asm_Back = Class(name="kmlogo::asm::Back")
Primitive = Class(name="Primitive")
Expression = Class(name="Expression")
kmlogo_asm_Forward = Class(name="kmlogo::asm::Forward")
kmlogo_asm_Left = Class(name="kmlogo::asm::Left")
kmlogo_asm_Right = Class(name="kmlogo::asm::Right")
kmlogo_asm_PenDown = Class(name="kmlogo::asm::PenDown")
kmlogo_asm_PenUp = Class(name="kmlogo::asm::PenUp")
kmlogo_asm_Clear = Class(name="kmlogo::asm::Clear")
kmlogo_asm_Instruction = Class(name="kmlogo::asm::Instruction", is_abstract=True)
kmlogo_asm_Primitive = Class(name="kmlogo::asm::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
kmlogo_asm_Block = Class(name="kmlogo::asm::Block")
kmlogo_asm_If = Class(name="kmlogo::asm::If")
ControlStructure = Class(name="ControlStructure")
Block = Class(name="Block")
kmlogo_asm_ControlStructure = Class(name="kmlogo::asm::ControlStructure")
kmlogo_asm_Repeat = Class(name="kmlogo::asm::Repeat")
kmlogo_asm_While = Class(name="kmlogo::asm::While")
kmlogo_asm_Expression = Class(name="kmlogo::asm::Expression", is_abstract=True)
kmlogo_asm_BinaryExp = Class(name="kmlogo::asm::BinaryExp", is_abstract=True)
kmlogo_asm_Constant = Class(name="kmlogo::asm::Constant")
kmlogo_asm_ProcCall = Class(name="kmlogo::asm::ProcCall")
ProcDeclaration = Class(name="ProcDeclaration")
kmlogo_asm_ProcDeclaration = Class(name="kmlogo::asm::ProcDeclaration")
Parameter_ = Class(name="Parameter")
ProcCall = Class(name="ProcCall")
kmlogo_asm_Parameter = Class(name="kmlogo::asm::Parameter")
kmlogo_asm_ParameterCall = Class(name="kmlogo::asm::ParameterCall")
kmlogo_asm_Plus = Class(name="kmlogo::asm::Plus")
BinaryExp = Class(name="BinaryExp")
kmlogo_asm_Minus = Class(name="kmlogo::asm::Minus")
kmlogo_asm_Mult = Class(name="kmlogo::asm::Mult")
kmlogo_asm_Div = Class(name="kmlogo::asm::Div")
kmlogo_asm_Equals = Class(name="kmlogo::asm::Equals")
kmlogo_asm_Greater = Class(name="kmlogo::asm::Greater")
kmlogo_asm_Lower = Class(name="kmlogo::asm::Lower")
kmlogo_asm_LogoProgram = Class(name="kmlogo::asm::LogoProgram")

# kmlogo_asm_Back class attributes and methods

# Primitive class attributes and methods

# Expression class attributes and methods

# kmlogo_asm_Forward class attributes and methods

# kmlogo_asm_Left class attributes and methods

# kmlogo_asm_Right class attributes and methods

# kmlogo_asm_PenDown class attributes and methods

# kmlogo_asm_PenUp class attributes and methods

# kmlogo_asm_Clear class attributes and methods

# kmlogo_asm_Instruction class attributes and methods

# kmlogo_asm_Primitive class attributes and methods

# Instruction class attributes and methods

# kmlogo_asm_Block class attributes and methods

# kmlogo_asm_If class attributes and methods

# ControlStructure class attributes and methods

# Block class attributes and methods

# kmlogo_asm_ControlStructure class attributes and methods

# kmlogo_asm_Repeat class attributes and methods

# kmlogo_asm_While class attributes and methods

# kmlogo_asm_Expression class attributes and methods

# kmlogo_asm_BinaryExp class attributes and methods

# kmlogo_asm_Constant class attributes and methods
kmlogo_asm_Constant_integerValue: Property = Property(name="integerValue", type=StringType)
kmlogo_asm_Constant.attributes={kmlogo_asm_Constant_integerValue}

# kmlogo_asm_ProcCall class attributes and methods

# ProcDeclaration class attributes and methods

# kmlogo_asm_ProcDeclaration class attributes and methods
kmlogo_asm_ProcDeclaration_name: Property = Property(name="name", type=StringType)
kmlogo_asm_ProcDeclaration.attributes={kmlogo_asm_ProcDeclaration_name}

# Parameter class attributes and methods

# ProcCall class attributes and methods

# kmlogo_asm_Parameter class attributes and methods
kmlogo_asm_Parameter_name: Property = Property(name="name", type=StringType)
kmlogo_asm_Parameter.attributes={kmlogo_asm_Parameter_name}

# kmlogo_asm_ParameterCall class attributes and methods

# kmlogo_asm_Plus class attributes and methods

# BinaryExp class attributes and methods

# kmlogo_asm_Minus class attributes and methods

# kmlogo_asm_Mult class attributes and methods

# kmlogo_asm_Div class attributes and methods

# kmlogo_asm_Equals class attributes and methods

# kmlogo_asm_Greater class attributes and methods

# kmlogo_asm_Lower class attributes and methods

# kmlogo_asm_LogoProgram class attributes and methods

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="Expression", type=kmlogo_asm_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_Back", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="Expression2", type=kmlogo_asm_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_Forward", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle3: BinaryAssociation = BinaryAssociation(
    name="angle3",
    ends={
        Property(name="Expression4", type=kmlogo_asm_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_Left", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle5: BinaryAssociation = BinaryAssociation(
    name="angle5",
    ends={
        Property(name="Expression6", type=kmlogo_asm_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_Right", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instructions20: BinaryAssociation = BinaryAssociation(
    name="instructions20",
    ends={
        Property(name="Instruction", type=kmlogo_asm_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_ProcDeclaration21", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions22: BinaryAssociation = BinaryAssociation(
    name="instructions22",
    ends={
        Property(name="Instruction23", type=kmlogo_asm_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_Block", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart24: BinaryAssociation = BinaryAssociation(
    name="thenPart24",
    ends={
        Property(name="Block", type=kmlogo_asm_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_If", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart25: BinaryAssociation = BinaryAssociation(
    name="elsePart25",
    ends={
        Property(name="Block27", type=kmlogo_asm_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_If26", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition28: BinaryAssociation = BinaryAssociation(
    name="condition28",
    ends={
        Property(name="Expression29", type=kmlogo_asm_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_ControlStructure", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block30: BinaryAssociation = BinaryAssociation(
    name="block30",
    ends={
        Property(name="Block31", type=kmlogo_asm_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_Repeat", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block32: BinaryAssociation = BinaryAssociation(
    name="block32",
    ends={
        Property(name="Block33", type=kmlogo_asm_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_While", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="Expression8", type=kmlogo_asm_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_BinaryExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs9: BinaryAssociation = BinaryAssociation(
    name="rhs9",
    ends={
        Property(name="Expression11", type=kmlogo_asm_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_BinaryExp10", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualArgs12: BinaryAssociation = BinaryAssociation(
    name="actualArgs12",
    ends={
        Property(name="Expression13", type=kmlogo_asm_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_ProcCall", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration14: BinaryAssociation = BinaryAssociation(
    name="declaration14",
    ends={
        Property(name="15", type=kmlogo_asm_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=ProcDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
args16: BinaryAssociation = BinaryAssociation(
    name="args16",
    ends={
        Property(name="Parameter", type=kmlogo_asm_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_ProcDeclaration", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procCall17: BinaryAssociation = BinaryAssociation(
    name="procCall17",
    ends={
        Property(name="19", type=kmlogo_asm_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=ProcCall, multiplicity=Multiplicity(0, 9999))
    }
)
parameter34: BinaryAssociation = BinaryAssociation(
    name="parameter34",
    ends={
        Property(name="Parameter35", type=kmlogo_asm_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_ParameterCall", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
instructions36: BinaryAssociation = BinaryAssociation(
    name="instructions36",
    ends={
        Property(name="Instruction37", type=kmlogo_asm_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmlogo_asm_LogoProgram", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_kmlogo_asm_Back_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_Back)
gen_kmlogo_asm_Forward_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_Forward)
gen_kmlogo_asm_Left_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_Left)
gen_kmlogo_asm_Right_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_Right)
gen_kmlogo_asm_PenDown_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_PenDown)
gen_kmlogo_asm_PenUp_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_PenUp)
gen_kmlogo_asm_Clear_Primitive = Generalization(general=Primitive, specific=kmlogo_asm_Clear)
gen_kmlogo_asm_Primitive_Instruction = Generalization(general=Instruction, specific=kmlogo_asm_Primitive)
gen_kmlogo_asm_Block_Instruction = Generalization(general=Instruction, specific=kmlogo_asm_Block)
gen_kmlogo_asm_If_ControlStructure = Generalization(general=ControlStructure, specific=kmlogo_asm_If)
gen_kmlogo_asm_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmlogo_asm_ControlStructure)
gen_kmlogo_asm_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=kmlogo_asm_Repeat)
gen_kmlogo_asm_While_ControlStructure = Generalization(general=ControlStructure, specific=kmlogo_asm_While)
gen_kmlogo_asm_Expression_Instruction = Generalization(general=Instruction, specific=kmlogo_asm_Expression)
gen_kmlogo_asm_BinaryExp_Expression = Generalization(general=Expression, specific=kmlogo_asm_BinaryExp)
gen_kmlogo_asm_Constant_Expression = Generalization(general=Expression, specific=kmlogo_asm_Constant)
gen_kmlogo_asm_ProcCall_Expression = Generalization(general=Expression, specific=kmlogo_asm_ProcCall)
gen_kmlogo_asm_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=kmlogo_asm_ProcDeclaration)
gen_kmlogo_asm_ParameterCall_Expression = Generalization(general=Expression, specific=kmlogo_asm_ParameterCall)
gen_kmlogo_asm_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Plus)
gen_kmlogo_asm_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Minus)
gen_kmlogo_asm_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Mult)
gen_kmlogo_asm_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Div)
gen_kmlogo_asm_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Equals)
gen_kmlogo_asm_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Greater)
gen_kmlogo_asm_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmlogo_asm_Lower)

# Domain Model
domain_model = DomainModel(
    name="kmlogo",
    types={kmlogo_asm_Back, Primitive, Expression, kmlogo_asm_Forward, kmlogo_asm_Left, kmlogo_asm_Right, kmlogo_asm_PenDown, kmlogo_asm_PenUp, kmlogo_asm_Clear, kmlogo_asm_Instruction, kmlogo_asm_Primitive, Instruction, kmlogo_asm_Block, kmlogo_asm_If, ControlStructure, Block, kmlogo_asm_ControlStructure, kmlogo_asm_Repeat, kmlogo_asm_While, kmlogo_asm_Expression, kmlogo_asm_BinaryExp, kmlogo_asm_Constant, kmlogo_asm_ProcCall, ProcDeclaration, kmlogo_asm_ProcDeclaration, Parameter_, ProcCall, kmlogo_asm_Parameter, kmlogo_asm_ParameterCall, kmlogo_asm_Plus, BinaryExp, kmlogo_asm_Minus, kmlogo_asm_Mult, kmlogo_asm_Div, kmlogo_asm_Equals, kmlogo_asm_Greater, kmlogo_asm_Lower, kmlogo_asm_LogoProgram},
    associations={steps0, steps1, angle3, angle5, instructions20, instructions22, thenPart24, elsePart25, condition28, block30, block32, lhs7, rhs9, actualArgs12, declaration14, args16, procCall17, parameter34, instructions36},
    generalizations={gen_kmlogo_asm_Back_Primitive, gen_kmlogo_asm_Forward_Primitive, gen_kmlogo_asm_Left_Primitive, gen_kmlogo_asm_Right_Primitive, gen_kmlogo_asm_PenDown_Primitive, gen_kmlogo_asm_PenUp_Primitive, gen_kmlogo_asm_Clear_Primitive, gen_kmlogo_asm_Primitive_Instruction, gen_kmlogo_asm_Block_Instruction, gen_kmlogo_asm_If_ControlStructure, gen_kmlogo_asm_ControlStructure_Instruction, gen_kmlogo_asm_Repeat_ControlStructure, gen_kmlogo_asm_While_ControlStructure, gen_kmlogo_asm_Expression_Instruction, gen_kmlogo_asm_BinaryExp_Expression, gen_kmlogo_asm_Constant_Expression, gen_kmlogo_asm_ProcCall_Expression, gen_kmlogo_asm_ProcDeclaration_Instruction, gen_kmlogo_asm_ParameterCall_Expression, gen_kmlogo_asm_Plus_BinaryExp, gen_kmlogo_asm_Minus_BinaryExp, gen_kmlogo_asm_Mult_BinaryExp, gen_kmlogo_asm_Div_BinaryExp, gen_kmlogo_asm_Equals_BinaryExp, gen_kmlogo_asm_Greater_BinaryExp, gen_kmlogo_asm_Lower_BinaryExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)