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
kmLogo_Forward = Class(name="kmLogo::Forward")
kmLogo_Left = Class(name="kmLogo::Left")
kmLogo_LogoProgram = Class(name="kmLogo::LogoProgram")
kmLogo_Instruction = Class(name="kmLogo::Instruction", is_abstract=True)
kmLogo_Primitive = Class(name="kmLogo::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
kmLogo_Back = Class(name="kmLogo::Back")
Primitive = Class(name="Primitive")
kmLogo_Expression = Class(name="kmLogo::Expression", is_abstract=True)
kmLogo_Block = Class(name="kmLogo::Block")
kmLogo_Right = Class(name="kmLogo::Right")
kmLogo_PenDown = Class(name="kmLogo::PenDown")
kmLogo_PenUp = Class(name="kmLogo::PenUp")
kmLogo_Clear = Class(name="kmLogo::Clear")
kmLogo_BinaryExp = Class(name="kmLogo::BinaryExp", is_abstract=True)
Expression = Class(name="Expression")
kmLogo_Constant = Class(name="kmLogo::Constant")
kmLogo_ProcCall = Class(name="kmLogo::ProcCall")
kmLogo_ProcDeclaration = Class(name="kmLogo::ProcDeclaration")
kmLogo_Parameter = Class(name="kmLogo::Parameter")
kmLogo_If = Class(name="kmLogo::If")
ControlStructure = Class(name="ControlStructure")
kmLogo_ControlStructure = Class(name="kmLogo::ControlStructure")
kmLogo_Repeat = Class(name="kmLogo::Repeat")
kmLogo_While = Class(name="kmLogo::While")
kmLogo_ParameterCall = Class(name="kmLogo::ParameterCall")
kmLogo_Plus = Class(name="kmLogo::Plus")
BinaryExp = Class(name="BinaryExp")
kmLogo_Minus = Class(name="kmLogo::Minus")
kmLogo_Mult = Class(name="kmLogo::Mult")
kmLogo_Div = Class(name="kmLogo::Div")
kmLogo_Equals = Class(name="kmLogo::Equals")
kmLogo_Greater = Class(name="kmLogo::Greater")
kmLogo_Lower = Class(name="kmLogo::Lower")

# kmLogo_Forward class attributes and methods

# kmLogo_Left class attributes and methods

# kmLogo_LogoProgram class attributes and methods

# kmLogo_Instruction class attributes and methods

# kmLogo_Primitive class attributes and methods

# Instruction class attributes and methods

# kmLogo_Back class attributes and methods

# Primitive class attributes and methods

# kmLogo_Expression class attributes and methods

# kmLogo_Block class attributes and methods

# kmLogo_Right class attributes and methods

# kmLogo_PenDown class attributes and methods

# kmLogo_PenUp class attributes and methods

# kmLogo_Clear class attributes and methods

# kmLogo_BinaryExp class attributes and methods

# Expression class attributes and methods

# kmLogo_Constant class attributes and methods
kmLogo_Constant_integerValue: Property = Property(name="integerValue", type=IntegerType)
kmLogo_Constant.attributes={kmLogo_Constant_integerValue}

# kmLogo_ProcCall class attributes and methods

# kmLogo_ProcDeclaration class attributes and methods
kmLogo_ProcDeclaration_name: Property = Property(name="name", type=StringType)
kmLogo_ProcDeclaration.attributes={kmLogo_ProcDeclaration_name}

# kmLogo_Parameter class attributes and methods
kmLogo_Parameter_name: Property = Property(name="name", type=StringType)
kmLogo_Parameter.attributes={kmLogo_Parameter_name}

# kmLogo_If class attributes and methods

# ControlStructure class attributes and methods

# kmLogo_ControlStructure class attributes and methods

# kmLogo_Repeat class attributes and methods

# kmLogo_While class attributes and methods

# kmLogo_ParameterCall class attributes and methods

# kmLogo_Plus class attributes and methods

# BinaryExp class attributes and methods

# kmLogo_Minus class attributes and methods

# kmLogo_Mult class attributes and methods

# kmLogo_Div class attributes and methods

# kmLogo_Equals class attributes and methods

# kmLogo_Greater class attributes and methods

# kmLogo_Lower class attributes and methods

# Relationships
steps2: BinaryAssociation = BinaryAssociation(
    name="steps2",
    ends={
        Property(name="kmLogo_Expression3", type=kmLogo_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Forward", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="kmLogo_Instruction", type=kmLogo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_LogoProgram", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="kmLogo_Expression", type=kmLogo_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Back", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions21: BinaryAssociation = BinaryAssociation(
    name="instructions21",
    ends={
        Property(name="kmLogo_Instruction23", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcDeclaration22", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
angle4: BinaryAssociation = BinaryAssociation(
    name="angle4",
    ends={
        Property(name="kmLogo_Expression5", type=kmLogo_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Left", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle6: BinaryAssociation = BinaryAssociation(
    name="angle6",
    ends={
        Property(name="kmLogo_Expression7", type=kmLogo_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Right", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs8: BinaryAssociation = BinaryAssociation(
    name="lhs8",
    ends={
        Property(name="kmLogo_Expression9", type=kmLogo_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_BinaryExp", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs10: BinaryAssociation = BinaryAssociation(
    name="rhs10",
    ends={
        Property(name="kmLogo_Expression12", type=kmLogo_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_BinaryExp11", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualArgs13: BinaryAssociation = BinaryAssociation(
    name="actualArgs13",
    ends={
        Property(name="kmLogo_Expression14", type=kmLogo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcCall", type=kmLogo_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration15: BinaryAssociation = BinaryAssociation(
    name="declaration15",
    ends={
        Property(name="16", type=kmLogo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
args17: BinaryAssociation = BinaryAssociation(
    name="args17",
    ends={
        Property(name="kmLogo_Parameter", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcDeclaration", type=kmLogo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procCall18: BinaryAssociation = BinaryAssociation(
    name="procCall18",
    ends={
        Property(name="20", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=kmLogo_ProcCall, multiplicity=Multiplicity(0, 9999))
    }
)
instructions24: BinaryAssociation = BinaryAssociation(
    name="instructions24",
    ends={
        Property(name="kmLogo_Instruction25", type=kmLogo_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Block", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart26: BinaryAssociation = BinaryAssociation(
    name="thenPart26",
    ends={
        Property(name="kmLogo_Block27", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart28: BinaryAssociation = BinaryAssociation(
    name="elsePart28",
    ends={
        Property(name="kmLogo_Block30", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If29", type=kmLogo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="kmLogo_Expression32", type=kmLogo_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ControlStructure", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block33: BinaryAssociation = BinaryAssociation(
    name="block33",
    ends={
        Property(name="kmLogo_Block34", type=kmLogo_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Repeat", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block35: BinaryAssociation = BinaryAssociation(
    name="block35",
    ends={
        Property(name="kmLogo_Block36", type=kmLogo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_While", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter37: BinaryAssociation = BinaryAssociation(
    name="parameter37",
    ends={
        Property(name="kmLogo_Parameter38", type=kmLogo_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ParameterCall", type=kmLogo_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_kmLogo_Forward_Primitive = Generalization(general=Primitive, specific=kmLogo_Forward)
gen_kmLogo_Left_Primitive = Generalization(general=Primitive, specific=kmLogo_Left)
gen_kmLogo_Primitive_Instruction = Generalization(general=Instruction, specific=kmLogo_Primitive)
gen_kmLogo_Back_Primitive = Generalization(general=Primitive, specific=kmLogo_Back)
gen_kmLogo_Block_Instruction = Generalization(general=Instruction, specific=kmLogo_Block)
gen_kmLogo_Right_Primitive = Generalization(general=Primitive, specific=kmLogo_Right)
gen_kmLogo_PenDown_Primitive = Generalization(general=Primitive, specific=kmLogo_PenDown)
gen_kmLogo_PenUp_Primitive = Generalization(general=Primitive, specific=kmLogo_PenUp)
gen_kmLogo_Clear_Primitive = Generalization(general=Primitive, specific=kmLogo_Clear)
gen_kmLogo_Expression_Instruction = Generalization(general=Instruction, specific=kmLogo_Expression)
gen_kmLogo_BinaryExp_Expression = Generalization(general=Expression, specific=kmLogo_BinaryExp)
gen_kmLogo_Constant_Expression = Generalization(general=Expression, specific=kmLogo_Constant)
gen_kmLogo_ProcCall_Expression = Generalization(general=Expression, specific=kmLogo_ProcCall)
gen_kmLogo_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=kmLogo_ProcDeclaration)
gen_kmLogo_If_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_If)
gen_kmLogo_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmLogo_ControlStructure)
gen_kmLogo_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_Repeat)
gen_kmLogo_While_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_While)
gen_kmLogo_ParameterCall_Expression = Generalization(general=Expression, specific=kmLogo_ParameterCall)
gen_kmLogo_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Plus)
gen_kmLogo_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Minus)
gen_kmLogo_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Mult)
gen_kmLogo_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Div)
gen_kmLogo_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Equals)
gen_kmLogo_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Greater)
gen_kmLogo_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Lower)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_Forward, kmLogo_Left, kmLogo_LogoProgram, kmLogo_Instruction, kmLogo_Primitive, Instruction, kmLogo_Back, Primitive, kmLogo_Expression, kmLogo_Block, kmLogo_Right, kmLogo_PenDown, kmLogo_PenUp, kmLogo_Clear, kmLogo_BinaryExp, Expression, kmLogo_Constant, kmLogo_ProcCall, kmLogo_ProcDeclaration, kmLogo_Parameter, kmLogo_If, ControlStructure, kmLogo_ControlStructure, kmLogo_Repeat, kmLogo_While, kmLogo_ParameterCall, kmLogo_Plus, BinaryExp, kmLogo_Minus, kmLogo_Mult, kmLogo_Div, kmLogo_Equals, kmLogo_Greater, kmLogo_Lower},
    associations={steps2, instructions0, steps1, instructions21, angle4, angle6, lhs8, rhs10, actualArgs13, declaration15, args17, procCall18, instructions24, thenPart26, elsePart28, condition31, block33, block35, parameter37},
    generalizations={gen_kmLogo_Forward_Primitive, gen_kmLogo_Left_Primitive, gen_kmLogo_Primitive_Instruction, gen_kmLogo_Back_Primitive, gen_kmLogo_Block_Instruction, gen_kmLogo_Right_Primitive, gen_kmLogo_PenDown_Primitive, gen_kmLogo_PenUp_Primitive, gen_kmLogo_Clear_Primitive, gen_kmLogo_Expression_Instruction, gen_kmLogo_BinaryExp_Expression, gen_kmLogo_Constant_Expression, gen_kmLogo_ProcCall_Expression, gen_kmLogo_ProcDeclaration_Instruction, gen_kmLogo_If_ControlStructure, gen_kmLogo_ControlStructure_Instruction, gen_kmLogo_Repeat_ControlStructure, gen_kmLogo_While_ControlStructure, gen_kmLogo_ParameterCall_Expression, gen_kmLogo_Plus_BinaryExp, gen_kmLogo_Minus_BinaryExp, gen_kmLogo_Mult_BinaryExp, gen_kmLogo_Div_BinaryExp, gen_kmLogo_Equals_BinaryExp, gen_kmLogo_Greater_BinaryExp, gen_kmLogo_Lower_BinaryExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)