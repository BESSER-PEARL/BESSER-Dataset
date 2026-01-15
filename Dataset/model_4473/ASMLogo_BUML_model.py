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
kmLogo_ASM_Instruction = Class(name="kmLogo::ASM::Instruction", is_abstract=True)
kmLogo_ASM_Primitive = Class(name="kmLogo::ASM::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
kmLogo_ASM_Back = Class(name="kmLogo::ASM::Back")
Primitive = Class(name="Primitive")
Expression = Class(name="Expression")
kmLogo_ASM_Right = Class(name="kmLogo::ASM::Right")
kmLogo_ASM_PenDown = Class(name="kmLogo::ASM::PenDown")
kmLogo_ASM_PenUp = Class(name="kmLogo::ASM::PenUp")
kmLogo_ASM_Clear = Class(name="kmLogo::ASM::Clear")
kmLogo_ASM_Expression = Class(name="kmLogo::ASM::Expression", is_abstract=True)
kmLogo_ASM_BinaryExp = Class(name="kmLogo::ASM::BinaryExp", is_abstract=True)
kmLogo_ASM_Constant = Class(name="kmLogo::ASM::Constant")
kmLogo_ASM_ProcCall = Class(name="kmLogo::ASM::ProcCall")
ProcDeclaration = Class(name="ProcDeclaration")
kmLogo_ASM_ProcDeclaration = Class(name="kmLogo::ASM::ProcDeclaration")
Parameter_ = Class(name="Parameter")
ProcCall = Class(name="ProcCall")
kmLogo_ASM_Forward = Class(name="kmLogo::ASM::Forward")
kmLogo_ASM_Left = Class(name="kmLogo::ASM::Left")
kmLogo_ASM_Repeat = Class(name="kmLogo::ASM::Repeat")
kmLogo_ASM_While = Class(name="kmLogo::ASM::While")
kmLogo_ASM_Parameter = Class(name="kmLogo::ASM::Parameter")
kmLogo_ASM_ParameterCall = Class(name="kmLogo::ASM::ParameterCall")
kmLogo_ASM_Plus = Class(name="kmLogo::ASM::Plus")
BinaryExp = Class(name="BinaryExp")
kmLogo_ASM_Minus = Class(name="kmLogo::ASM::Minus")
kmLogo_ASM_Mult = Class(name="kmLogo::ASM::Mult")
kmLogo_ASM_Div = Class(name="kmLogo::ASM::Div")
kmLogo_ASM_Equals = Class(name="kmLogo::ASM::Equals")
kmLogo_ASM_Greater = Class(name="kmLogo::ASM::Greater")
kmLogo_ASM_Lower = Class(name="kmLogo::ASM::Lower")
kmLogo_ASM_LogoProgram = Class(name="kmLogo::ASM::LogoProgram")
kmLogo_ASM_Block = Class(name="kmLogo::ASM::Block")
kmLogo_ASM_If = Class(name="kmLogo::ASM::If")
ControlStructure = Class(name="ControlStructure")
Block = Class(name="Block")
kmLogo_ASM_ControlStructure = Class(name="kmLogo::ASM::ControlStructure")

# kmLogo_ASM_Instruction class attributes and methods

# kmLogo_ASM_Primitive class attributes and methods

# Instruction class attributes and methods

# kmLogo_ASM_Back class attributes and methods

# Primitive class attributes and methods

# Expression class attributes and methods

# kmLogo_ASM_Right class attributes and methods

# kmLogo_ASM_PenDown class attributes and methods

# kmLogo_ASM_PenUp class attributes and methods

# kmLogo_ASM_Clear class attributes and methods

# kmLogo_ASM_Expression class attributes and methods

# kmLogo_ASM_BinaryExp class attributes and methods

# kmLogo_ASM_Constant class attributes and methods
kmLogo_ASM_Constant_integerValue: Property = Property(name="integerValue", type=StringType)
kmLogo_ASM_Constant.attributes={kmLogo_ASM_Constant_integerValue}

# kmLogo_ASM_ProcCall class attributes and methods

# ProcDeclaration class attributes and methods

# kmLogo_ASM_ProcDeclaration class attributes and methods
kmLogo_ASM_ProcDeclaration_name: Property = Property(name="name", type=StringType)
kmLogo_ASM_ProcDeclaration.attributes={kmLogo_ASM_ProcDeclaration_name}

# Parameter class attributes and methods

# ProcCall class attributes and methods

# kmLogo_ASM_Forward class attributes and methods

# kmLogo_ASM_Left class attributes and methods

# kmLogo_ASM_Repeat class attributes and methods

# kmLogo_ASM_While class attributes and methods

# kmLogo_ASM_Parameter class attributes and methods
kmLogo_ASM_Parameter_name: Property = Property(name="name", type=StringType)
kmLogo_ASM_Parameter.attributes={kmLogo_ASM_Parameter_name}

# kmLogo_ASM_ParameterCall class attributes and methods

# kmLogo_ASM_Plus class attributes and methods

# BinaryExp class attributes and methods

# kmLogo_ASM_Minus class attributes and methods

# kmLogo_ASM_Mult class attributes and methods

# kmLogo_ASM_Div class attributes and methods

# kmLogo_ASM_Equals class attributes and methods

# kmLogo_ASM_Greater class attributes and methods

# kmLogo_ASM_Lower class attributes and methods

# kmLogo_ASM_LogoProgram class attributes and methods

# kmLogo_ASM_Block class attributes and methods

# kmLogo_ASM_If class attributes and methods

# ControlStructure class attributes and methods

# Block class attributes and methods

# kmLogo_ASM_ControlStructure class attributes and methods

# Relationships
angle5: BinaryAssociation = BinaryAssociation(
    name="angle5",
    ends={
        Property(name="Expression6", type=kmLogo_ASM_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Right", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="Expression8", type=kmLogo_ASM_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_BinaryExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs9: BinaryAssociation = BinaryAssociation(
    name="rhs9",
    ends={
        Property(name="Expression11", type=kmLogo_ASM_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_BinaryExp10", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualArgs12: BinaryAssociation = BinaryAssociation(
    name="actualArgs12",
    ends={
        Property(name="Expression13", type=kmLogo_ASM_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ProcCall", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration14: BinaryAssociation = BinaryAssociation(
    name="declaration14",
    ends={
        Property(name="ASM", type=kmLogo_ASM_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcDeclaration", type=ProcDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
args15: BinaryAssociation = BinaryAssociation(
    name="args15",
    ends={
        Property(name="Parameter", type=kmLogo_ASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ProcDeclaration", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procCall16: BinaryAssociation = BinaryAssociation(
    name="procCall16",
    ends={
        Property(name="ASM17", type=kmLogo_ASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcCall", type=ProcCall, multiplicity=Multiplicity(0, 9999))
    }
)
instructions18: BinaryAssociation = BinaryAssociation(
    name="instructions18",
    ends={
        Property(name="Instruction", type=kmLogo_ASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ProcDeclaration19", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="Expression", type=kmLogo_ASM_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Back", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="Expression2", type=kmLogo_ASM_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Forward", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle3: BinaryAssociation = BinaryAssociation(
    name="angle3",
    ends={
        Property(name="Expression4", type=kmLogo_ASM_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Left", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="Expression27", type=kmLogo_ASM_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ControlStructure", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block28: BinaryAssociation = BinaryAssociation(
    name="block28",
    ends={
        Property(name="Block29", type=kmLogo_ASM_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Repeat", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block30: BinaryAssociation = BinaryAssociation(
    name="block30",
    ends={
        Property(name="Block31", type=kmLogo_ASM_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_While", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter32: BinaryAssociation = BinaryAssociation(
    name="parameter32",
    ends={
        Property(name="Parameter33", type=kmLogo_ASM_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ParameterCall", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
instructions34: BinaryAssociation = BinaryAssociation(
    name="instructions34",
    ends={
        Property(name="Instruction35", type=kmLogo_ASM_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_LogoProgram", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions20: BinaryAssociation = BinaryAssociation(
    name="instructions20",
    ends={
        Property(name="Instruction21", type=kmLogo_ASM_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Block", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart22: BinaryAssociation = BinaryAssociation(
    name="thenPart22",
    ends={
        Property(name="Block", type=kmLogo_ASM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_If", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart23: BinaryAssociation = BinaryAssociation(
    name="elsePart23",
    ends={
        Property(name="Block25", type=kmLogo_ASM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_If24", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kmLogo_ASM_Primitive_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_Primitive)
gen_kmLogo_ASM_Back_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Back)
gen_kmLogo_ASM_Right_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Right)
gen_kmLogo_ASM_PenDown_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_PenDown)
gen_kmLogo_ASM_PenUp_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_PenUp)
gen_kmLogo_ASM_Clear_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Clear)
gen_kmLogo_ASM_Expression_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_Expression)
gen_kmLogo_ASM_BinaryExp_Expression = Generalization(general=Expression, specific=kmLogo_ASM_BinaryExp)
gen_kmLogo_ASM_Constant_Expression = Generalization(general=Expression, specific=kmLogo_ASM_Constant)
gen_kmLogo_ASM_ProcCall_Expression = Generalization(general=Expression, specific=kmLogo_ASM_ProcCall)
gen_kmLogo_ASM_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_ProcDeclaration)
gen_kmLogo_ASM_Forward_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Forward)
gen_kmLogo_ASM_Left_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Left)
gen_kmLogo_ASM_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_ASM_Repeat)
gen_kmLogo_ASM_While_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_ASM_While)
gen_kmLogo_ASM_ParameterCall_Expression = Generalization(general=Expression, specific=kmLogo_ASM_ParameterCall)
gen_kmLogo_ASM_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Plus)
gen_kmLogo_ASM_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Minus)
gen_kmLogo_ASM_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Mult)
gen_kmLogo_ASM_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Div)
gen_kmLogo_ASM_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Equals)
gen_kmLogo_ASM_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Greater)
gen_kmLogo_ASM_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Lower)
gen_kmLogo_ASM_Block_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_Block)
gen_kmLogo_ASM_If_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_ASM_If)
gen_kmLogo_ASM_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_ControlStructure)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_ASM_Instruction, kmLogo_ASM_Primitive, Instruction, kmLogo_ASM_Back, Primitive, Expression, kmLogo_ASM_Right, kmLogo_ASM_PenDown, kmLogo_ASM_PenUp, kmLogo_ASM_Clear, kmLogo_ASM_Expression, kmLogo_ASM_BinaryExp, kmLogo_ASM_Constant, kmLogo_ASM_ProcCall, ProcDeclaration, kmLogo_ASM_ProcDeclaration, Parameter_, ProcCall, kmLogo_ASM_Forward, kmLogo_ASM_Left, kmLogo_ASM_Repeat, kmLogo_ASM_While, kmLogo_ASM_Parameter, kmLogo_ASM_ParameterCall, kmLogo_ASM_Plus, BinaryExp, kmLogo_ASM_Minus, kmLogo_ASM_Mult, kmLogo_ASM_Div, kmLogo_ASM_Equals, kmLogo_ASM_Greater, kmLogo_ASM_Lower, kmLogo_ASM_LogoProgram, kmLogo_ASM_Block, kmLogo_ASM_If, ControlStructure, Block, kmLogo_ASM_ControlStructure},
    associations={angle5, lhs7, rhs9, actualArgs12, declaration14, args15, procCall16, instructions18, steps0, steps1, angle3, condition26, block28, block30, parameter32, instructions34, instructions20, thenPart22, elsePart23},
    generalizations={gen_kmLogo_ASM_Primitive_Instruction, gen_kmLogo_ASM_Back_Primitive, gen_kmLogo_ASM_Right_Primitive, gen_kmLogo_ASM_PenDown_Primitive, gen_kmLogo_ASM_PenUp_Primitive, gen_kmLogo_ASM_Clear_Primitive, gen_kmLogo_ASM_Expression_Instruction, gen_kmLogo_ASM_BinaryExp_Expression, gen_kmLogo_ASM_Constant_Expression, gen_kmLogo_ASM_ProcCall_Expression, gen_kmLogo_ASM_ProcDeclaration_Instruction, gen_kmLogo_ASM_Forward_Primitive, gen_kmLogo_ASM_Left_Primitive, gen_kmLogo_ASM_Repeat_ControlStructure, gen_kmLogo_ASM_While_ControlStructure, gen_kmLogo_ASM_ParameterCall_Expression, gen_kmLogo_ASM_Plus_BinaryExp, gen_kmLogo_ASM_Minus_BinaryExp, gen_kmLogo_ASM_Mult_BinaryExp, gen_kmLogo_ASM_Div_BinaryExp, gen_kmLogo_ASM_Equals_BinaryExp, gen_kmLogo_ASM_Greater_BinaryExp, gen_kmLogo_ASM_Lower_BinaryExp, gen_kmLogo_ASM_Block_Instruction, gen_kmLogo_ASM_If_ControlStructure, gen_kmLogo_ASM_ControlStructure_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)