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
kmLogo_ASM_Instruction = Class(name="kmLogo_ASM_Instruction", is_abstract=True)
kmLogo_ASM_Primitive = Class(name="kmLogo_ASM_Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
kmLogo_ASM_Back = Class(name="kmLogo_ASM_Back")
Primitive = Class(name="Primitive")
Expression = Class(name="Expression")
kmLogo_ASM_Forward = Class(name="kmLogo_ASM_Forward")
kmLogo_ASM_Expression = Class(name="kmLogo_ASM_Expression", is_abstract=True)
kmLogo_ASM_BinaryExp = Class(name="kmLogo_ASM_BinaryExp", is_abstract=True)
kmLogo_ASM_UnaryExpression = Class(name="kmLogo_ASM_UnaryExpression", is_abstract=True)
kmLogo_ASM_Constant = Class(name="kmLogo_ASM_Constant")
kmLogo_ASM_ProcCall = Class(name="kmLogo_ASM_ProcCall")
ProcDeclaration = Class(name="ProcDeclaration")
kmLogo_ASM_ProcDeclaration = Class(name="kmLogo_ASM_ProcDeclaration")
kmLogo_ASM_Left = Class(name="kmLogo_ASM_Left")
kmLogo_ASM_Right = Class(name="kmLogo_ASM_Right")
kmLogo_ASM_PenDown = Class(name="kmLogo_ASM_PenDown")
kmLogo_ASM_PenUp = Class(name="kmLogo_ASM_PenUp")
kmLogo_ASM_Clear = Class(name="kmLogo_ASM_Clear")
Block = Class(name="Block")
kmLogo_ASM_ControlStructure = Class(name="kmLogo_ASM_ControlStructure")
kmLogo_ASM_Repeat = Class(name="kmLogo_ASM_Repeat")
kmLogo_ASM_While = Class(name="kmLogo_ASM_While")
kmLogo_ASM_Parameter = Class(name="kmLogo_ASM_Parameter")
kmLogo_ASM_ParameterCall = Class(name="kmLogo_ASM_ParameterCall")
kmLogo_ASM_Plus = Class(name="kmLogo_ASM_Plus")
BinaryExp = Class(name="BinaryExp")
kmLogo_ASM_Minus = Class(name="kmLogo_ASM_Minus")
Parameter_ = Class(name="Parameter")
ProcCall = Class(name="ProcCall")
kmLogo_ASM_Block = Class(name="kmLogo_ASM_Block")
kmLogo_ASM_If = Class(name="kmLogo_ASM_If")
ControlStructure = Class(name="ControlStructure")
kmLogo_ASM_Mult = Class(name="kmLogo_ASM_Mult")
kmLogo_ASM_Div = Class(name="kmLogo_ASM_Div")
kmLogo_ASM_Equals = Class(name="kmLogo_ASM_Equals")
kmLogo_ASM_Greater = Class(name="kmLogo_ASM_Greater")
kmLogo_ASM_Lower = Class(name="kmLogo_ASM_Lower")
kmLogo_ASM_Cos = Class(name="kmLogo_ASM_Cos")
UnaryExpression = Class(name="UnaryExpression")
kmLogo_ASM_Sin = Class(name="kmLogo_ASM_Sin")
kmLogo_ASM_Tan = Class(name="kmLogo_ASM_Tan")
kmLogo_ASM_LogoProgram = Class(name="kmLogo_ASM_LogoProgram")

# kmLogo_ASM_Instruction class attributes and methods

# kmLogo_ASM_Primitive class attributes and methods

# Instruction class attributes and methods

# kmLogo_ASM_Back class attributes and methods

# Primitive class attributes and methods

# Expression class attributes and methods

# kmLogo_ASM_Forward class attributes and methods

# kmLogo_ASM_Expression class attributes and methods

# kmLogo_ASM_BinaryExp class attributes and methods

# kmLogo_ASM_UnaryExpression class attributes and methods

# kmLogo_ASM_Constant class attributes and methods
kmLogo_ASM_Constant_value: Property = Property(name="value", type=FloatType)
kmLogo_ASM_Constant.attributes={kmLogo_ASM_Constant_value}

# kmLogo_ASM_ProcCall class attributes and methods

# ProcDeclaration class attributes and methods

# kmLogo_ASM_ProcDeclaration class attributes and methods
kmLogo_ASM_ProcDeclaration_name: Property = Property(name="name", type=StringType)
kmLogo_ASM_ProcDeclaration.attributes={kmLogo_ASM_ProcDeclaration_name}

# kmLogo_ASM_Left class attributes and methods

# kmLogo_ASM_Right class attributes and methods

# kmLogo_ASM_PenDown class attributes and methods

# kmLogo_ASM_PenUp class attributes and methods

# kmLogo_ASM_Clear class attributes and methods

# Block class attributes and methods

# kmLogo_ASM_ControlStructure class attributes and methods

# kmLogo_ASM_Repeat class attributes and methods

# kmLogo_ASM_While class attributes and methods

# kmLogo_ASM_Parameter class attributes and methods
kmLogo_ASM_Parameter_name: Property = Property(name="name", type=StringType)
kmLogo_ASM_Parameter.attributes={kmLogo_ASM_Parameter_name}

# kmLogo_ASM_ParameterCall class attributes and methods

# kmLogo_ASM_Plus class attributes and methods

# BinaryExp class attributes and methods

# kmLogo_ASM_Minus class attributes and methods

# Parameter class attributes and methods

# ProcCall class attributes and methods

# kmLogo_ASM_Block class attributes and methods

# kmLogo_ASM_If class attributes and methods

# ControlStructure class attributes and methods

# kmLogo_ASM_Mult class attributes and methods

# kmLogo_ASM_Div class attributes and methods

# kmLogo_ASM_Equals class attributes and methods

# kmLogo_ASM_Greater class attributes and methods

# kmLogo_ASM_Lower class attributes and methods

# kmLogo_ASM_Cos class attributes and methods

# UnaryExpression class attributes and methods

# kmLogo_ASM_Sin class attributes and methods

# kmLogo_ASM_Tan class attributes and methods

# kmLogo_ASM_LogoProgram class attributes and methods

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="Expression", type=kmLogo_ASM_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Back", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
expression12: BinaryAssociation = BinaryAssociation(
    name="expression12",
    ends={
        Property(name="Expression13", type=kmLogo_ASM_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_UnaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualArgs14: BinaryAssociation = BinaryAssociation(
    name="actualArgs14",
    ends={
        Property(name="Expression15", type=kmLogo_ASM_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ProcCall", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration16: BinaryAssociation = BinaryAssociation(
    name="declaration16",
    ends={
        Property(name="ProcDeclaration", type=kmLogo_ASM_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="procCall", type=ProcDeclaration, multiplicity=Multiplicity(1, 1))
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
angle5: BinaryAssociation = BinaryAssociation(
    name="angle5",
    ends={
        Property(name="Expression6", type=kmLogo_ASM_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Right", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart23: BinaryAssociation = BinaryAssociation(
    name="thenPart23",
    ends={
        Property(name="Block", type=kmLogo_ASM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_If", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart24: BinaryAssociation = BinaryAssociation(
    name="elsePart24",
    ends={
        Property(name="Block26", type=kmLogo_ASM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_If25", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition27: BinaryAssociation = BinaryAssociation(
    name="condition27",
    ends={
        Property(name="Expression28", type=kmLogo_ASM_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ControlStructure", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block29: BinaryAssociation = BinaryAssociation(
    name="block29",
    ends={
        Property(name="Block30", type=kmLogo_ASM_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Repeat", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block31: BinaryAssociation = BinaryAssociation(
    name="block31",
    ends={
        Property(name="Block32", type=kmLogo_ASM_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_While", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter33: BinaryAssociation = BinaryAssociation(
    name="parameter33",
    ends={
        Property(name="Parameter34", type=kmLogo_ASM_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ParameterCall", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
args17: BinaryAssociation = BinaryAssociation(
    name="args17",
    ends={
        Property(name="Parameter", type=kmLogo_ASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ProcDeclaration", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procCall18: BinaryAssociation = BinaryAssociation(
    name="procCall18",
    ends={
        Property(name="ProcCall", type=kmLogo_ASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=ProcCall, multiplicity=Multiplicity(0, 9999))
    }
)
instructions19: BinaryAssociation = BinaryAssociation(
    name="instructions19",
    ends={
        Property(name="Instruction", type=kmLogo_ASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_ProcDeclaration20", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions21: BinaryAssociation = BinaryAssociation(
    name="instructions21",
    ends={
        Property(name="Instruction22", type=kmLogo_ASM_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_Block", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions35: BinaryAssociation = BinaryAssociation(
    name="instructions35",
    ends={
        Property(name="Instruction36", type=kmLogo_ASM_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ASM_LogoProgram", type=Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_kmLogo_ASM_Primitive_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_Primitive)
gen_kmLogo_ASM_Back_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Back)
gen_kmLogo_ASM_Forward_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Forward)
gen_kmLogo_ASM_Clear_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Clear)
gen_kmLogo_ASM_Expression_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_Expression)
gen_kmLogo_ASM_BinaryExp_Expression = Generalization(general=Expression, specific=kmLogo_ASM_BinaryExp)
gen_kmLogo_ASM_UnaryExpression_Expression = Generalization(general=Expression, specific=kmLogo_ASM_UnaryExpression)
gen_kmLogo_ASM_Constant_Expression = Generalization(general=Expression, specific=kmLogo_ASM_Constant)
gen_kmLogo_ASM_ProcCall_Expression = Generalization(general=Expression, specific=kmLogo_ASM_ProcCall)
gen_kmLogo_ASM_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_ProcDeclaration)
gen_kmLogo_ASM_Left_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Left)
gen_kmLogo_ASM_Right_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_Right)
gen_kmLogo_ASM_PenDown_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_PenDown)
gen_kmLogo_ASM_PenUp_Primitive = Generalization(general=Primitive, specific=kmLogo_ASM_PenUp)
gen_kmLogo_ASM_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_ControlStructure)
gen_kmLogo_ASM_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_ASM_Repeat)
gen_kmLogo_ASM_While_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_ASM_While)
gen_kmLogo_ASM_ParameterCall_Expression = Generalization(general=Expression, specific=kmLogo_ASM_ParameterCall)
gen_kmLogo_ASM_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Plus)
gen_kmLogo_ASM_Block_Instruction = Generalization(general=Instruction, specific=kmLogo_ASM_Block)
gen_kmLogo_ASM_If_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_ASM_If)
gen_kmLogo_ASM_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Minus)
gen_kmLogo_ASM_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Mult)
gen_kmLogo_ASM_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Div)
gen_kmLogo_ASM_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Equals)
gen_kmLogo_ASM_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Greater)
gen_kmLogo_ASM_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_ASM_Lower)
gen_kmLogo_ASM_Cos_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_ASM_Cos)
gen_kmLogo_ASM_Sin_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_ASM_Sin)
gen_kmLogo_ASM_Tan_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_ASM_Tan)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_ASM_Instruction, kmLogo_ASM_Primitive, Instruction, kmLogo_ASM_Back, Primitive, Expression, kmLogo_ASM_Forward, kmLogo_ASM_Expression, kmLogo_ASM_BinaryExp, kmLogo_ASM_UnaryExpression, kmLogo_ASM_Constant, kmLogo_ASM_ProcCall, ProcDeclaration, kmLogo_ASM_ProcDeclaration, kmLogo_ASM_Left, kmLogo_ASM_Right, kmLogo_ASM_PenDown, kmLogo_ASM_PenUp, kmLogo_ASM_Clear, Block, kmLogo_ASM_ControlStructure, kmLogo_ASM_Repeat, kmLogo_ASM_While, kmLogo_ASM_Parameter, kmLogo_ASM_ParameterCall, kmLogo_ASM_Plus, BinaryExp, kmLogo_ASM_Minus, Parameter_, ProcCall, kmLogo_ASM_Block, kmLogo_ASM_If, ControlStructure, kmLogo_ASM_Mult, kmLogo_ASM_Div, kmLogo_ASM_Equals, kmLogo_ASM_Greater, kmLogo_ASM_Lower, kmLogo_ASM_Cos, UnaryExpression, kmLogo_ASM_Sin, kmLogo_ASM_Tan, kmLogo_ASM_LogoProgram},
    associations={steps0, lhs7, rhs9, expression12, actualArgs14, declaration16, steps1, angle3, angle5, thenPart23, elsePart24, condition27, block29, block31, parameter33, args17, procCall18, instructions19, instructions21, instructions35},
    generalizations={gen_kmLogo_ASM_Primitive_Instruction, gen_kmLogo_ASM_Back_Primitive, gen_kmLogo_ASM_Forward_Primitive, gen_kmLogo_ASM_Clear_Primitive, gen_kmLogo_ASM_Expression_Instruction, gen_kmLogo_ASM_BinaryExp_Expression, gen_kmLogo_ASM_UnaryExpression_Expression, gen_kmLogo_ASM_Constant_Expression, gen_kmLogo_ASM_ProcCall_Expression, gen_kmLogo_ASM_ProcDeclaration_Instruction, gen_kmLogo_ASM_Left_Primitive, gen_kmLogo_ASM_Right_Primitive, gen_kmLogo_ASM_PenDown_Primitive, gen_kmLogo_ASM_PenUp_Primitive, gen_kmLogo_ASM_ControlStructure_Instruction, gen_kmLogo_ASM_Repeat_ControlStructure, gen_kmLogo_ASM_While_ControlStructure, gen_kmLogo_ASM_ParameterCall_Expression, gen_kmLogo_ASM_Plus_BinaryExp, gen_kmLogo_ASM_Block_Instruction, gen_kmLogo_ASM_If_ControlStructure, gen_kmLogo_ASM_Minus_BinaryExp, gen_kmLogo_ASM_Mult_BinaryExp, gen_kmLogo_ASM_Div_BinaryExp, gen_kmLogo_ASM_Equals_BinaryExp, gen_kmLogo_ASM_Greater_BinaryExp, gen_kmLogo_ASM_Lower_BinaryExp, gen_kmLogo_ASM_Cos_UnaryExpression, gen_kmLogo_ASM_Sin_UnaryExpression, gen_kmLogo_ASM_Tan_UnaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)