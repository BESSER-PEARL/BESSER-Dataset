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
logoASM_Instruction = Class(name="logoASM::Instruction", is_abstract=True)
logoASM_Primitive = Class(name="logoASM::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
logoASM_Back = Class(name="logoASM::Back")
Primitive = Class(name="Primitive")
logoASM_Expression = Class(name="logoASM::Expression", is_abstract=True)
logoASM_Forward = Class(name="logoASM::Forward")
logoASM_Left = Class(name="logoASM::Left")
logoASM_Right = Class(name="logoASM::Right")
logoASM_PenDown = Class(name="logoASM::PenDown")
logoASM_PenUp = Class(name="logoASM::PenUp")
logoASM_Clear = Class(name="logoASM::Clear")
logoASM_BinaryExp = Class(name="logoASM::BinaryExp", is_abstract=True)
Expression = Class(name="Expression")
logoASM_ProcDeclaration = Class(name="logoASM::ProcDeclaration")
logoASM_Parameter = Class(name="logoASM::Parameter")
logoASM_Block = Class(name="logoASM::Block")
logoASM_If = Class(name="logoASM::If")
ControlStructure = Class(name="ControlStructure")
logoASM_ControlStructure = Class(name="logoASM::ControlStructure")
logoASM_Repeat = Class(name="logoASM::Repeat")
logoASM_While = Class(name="logoASM::While")
logoASM_Constant = Class(name="logoASM::Constant")
logoASM_ProcCall = Class(name="logoASM::ProcCall")
logoASM_Div = Class(name="logoASM::Div")
logoASM_Equals = Class(name="logoASM::Equals")
logoASM_Greater = Class(name="logoASM::Greater")
logoASM_Lower = Class(name="logoASM::Lower")
logoASM_LogoProgram = Class(name="logoASM::LogoProgram")
logoASM_ParameterCall = Class(name="logoASM::ParameterCall")
logoASM_Plus = Class(name="logoASM::Plus")
BinaryExp = Class(name="BinaryExp")
logoASM_Minus = Class(name="logoASM::Minus")
logoASM_Mult = Class(name="logoASM::Mult")

# logoASM_Instruction class attributes and methods

# logoASM_Primitive class attributes and methods

# Instruction class attributes and methods

# logoASM_Back class attributes and methods

# Primitive class attributes and methods

# logoASM_Expression class attributes and methods

# logoASM_Forward class attributes and methods

# logoASM_Left class attributes and methods

# logoASM_Right class attributes and methods

# logoASM_PenDown class attributes and methods

# logoASM_PenUp class attributes and methods

# logoASM_Clear class attributes and methods

# logoASM_BinaryExp class attributes and methods

# Expression class attributes and methods

# logoASM_ProcDeclaration class attributes and methods
logoASM_ProcDeclaration_name: Property = Property(name="name", type=StringType)
logoASM_ProcDeclaration.attributes={logoASM_ProcDeclaration_name}

# logoASM_Parameter class attributes and methods
logoASM_Parameter_name: Property = Property(name="name", type=StringType)
logoASM_Parameter.attributes={logoASM_Parameter_name}

# logoASM_Block class attributes and methods

# logoASM_If class attributes and methods

# ControlStructure class attributes and methods

# logoASM_ControlStructure class attributes and methods

# logoASM_Repeat class attributes and methods

# logoASM_While class attributes and methods

# logoASM_Constant class attributes and methods
logoASM_Constant_integerValue: Property = Property(name="integerValue", type=IntegerType)
logoASM_Constant.attributes={logoASM_Constant_integerValue}

# logoASM_ProcCall class attributes and methods

# logoASM_Div class attributes and methods

# logoASM_Equals class attributes and methods

# logoASM_Greater class attributes and methods

# logoASM_Lower class attributes and methods

# logoASM_LogoProgram class attributes and methods

# logoASM_ParameterCall class attributes and methods

# logoASM_Plus class attributes and methods

# BinaryExp class attributes and methods

# logoASM_Minus class attributes and methods

# logoASM_Mult class attributes and methods

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="logoASM_Expression", type=logoASM_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_Back", type=logoASM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="logoASM_Expression2", type=logoASM_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_Forward", type=logoASM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle3: BinaryAssociation = BinaryAssociation(
    name="angle3",
    ends={
        Property(name="logoASM_Expression4", type=logoASM_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_Left", type=logoASM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle5: BinaryAssociation = BinaryAssociation(
    name="angle5",
    ends={
        Property(name="logoASM_Expression6", type=logoASM_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_Right", type=logoASM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="logoASM_Expression8", type=logoASM_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_BinaryExp", type=logoASM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs9: BinaryAssociation = BinaryAssociation(
    name="rhs9",
    ends={
        Property(name="logoASM_Expression11", type=logoASM_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_BinaryExp10", type=logoASM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualArgs12: BinaryAssociation = BinaryAssociation(
    name="actualArgs12",
    ends={
        Property(name="logoASM_Expression13", type=logoASM_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_ProcCall", type=logoASM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration14: BinaryAssociation = BinaryAssociation(
    name="declaration14",
    ends={
        Property(name="logoASM_ProcDeclaration", type=logoASM_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_ProcCall15", type=logoASM_ProcDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
args16: BinaryAssociation = BinaryAssociation(
    name="args16",
    ends={
        Property(name="logoASM_Parameter", type=logoASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_ProcDeclaration17", type=logoASM_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions18: BinaryAssociation = BinaryAssociation(
    name="instructions18",
    ends={
        Property(name="logoASM_Instruction", type=logoASM_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_ProcDeclaration19", type=logoASM_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions20: BinaryAssociation = BinaryAssociation(
    name="instructions20",
    ends={
        Property(name="logoASM_Instruction21", type=logoASM_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_Block", type=logoASM_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart22: BinaryAssociation = BinaryAssociation(
    name="thenPart22",
    ends={
        Property(name="logoASM_Block23", type=logoASM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_If", type=logoASM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart24: BinaryAssociation = BinaryAssociation(
    name="elsePart24",
    ends={
        Property(name="logoASM_Block26", type=logoASM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_If25", type=logoASM_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition27: BinaryAssociation = BinaryAssociation(
    name="condition27",
    ends={
        Property(name="logoASM_Expression28", type=logoASM_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_ControlStructure", type=logoASM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block29: BinaryAssociation = BinaryAssociation(
    name="block29",
    ends={
        Property(name="logoASM_Block30", type=logoASM_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_Repeat", type=logoASM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block31: BinaryAssociation = BinaryAssociation(
    name="block31",
    ends={
        Property(name="logoASM_Block32", type=logoASM_While, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_While", type=logoASM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions35: BinaryAssociation = BinaryAssociation(
    name="instructions35",
    ends={
        Property(name="logoASM_Instruction36", type=logoASM_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_LogoProgram", type=logoASM_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter33: BinaryAssociation = BinaryAssociation(
    name="parameter33",
    ends={
        Property(name="logoASM_Parameter34", type=logoASM_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logoASM_ParameterCall", type=logoASM_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_logoASM_Primitive_Instruction = Generalization(general=Instruction, specific=logoASM_Primitive)
gen_logoASM_Back_Primitive = Generalization(general=Primitive, specific=logoASM_Back)
gen_logoASM_Forward_Primitive = Generalization(general=Primitive, specific=logoASM_Forward)
gen_logoASM_Left_Primitive = Generalization(general=Primitive, specific=logoASM_Left)
gen_logoASM_Right_Primitive = Generalization(general=Primitive, specific=logoASM_Right)
gen_logoASM_PenDown_Primitive = Generalization(general=Primitive, specific=logoASM_PenDown)
gen_logoASM_PenUp_Primitive = Generalization(general=Primitive, specific=logoASM_PenUp)
gen_logoASM_Clear_Primitive = Generalization(general=Primitive, specific=logoASM_Clear)
gen_logoASM_Expression_Instruction = Generalization(general=Instruction, specific=logoASM_Expression)
gen_logoASM_BinaryExp_Expression = Generalization(general=Expression, specific=logoASM_BinaryExp)
gen_logoASM_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=logoASM_ProcDeclaration)
gen_logoASM_Block_Instruction = Generalization(general=Instruction, specific=logoASM_Block)
gen_logoASM_If_ControlStructure = Generalization(general=ControlStructure, specific=logoASM_If)
gen_logoASM_ControlStructure_Instruction = Generalization(general=Instruction, specific=logoASM_ControlStructure)
gen_logoASM_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=logoASM_Repeat)
gen_logoASM_While_ControlStructure = Generalization(general=ControlStructure, specific=logoASM_While)
gen_logoASM_Constant_Expression = Generalization(general=Expression, specific=logoASM_Constant)
gen_logoASM_ProcCall_Expression = Generalization(general=Expression, specific=logoASM_ProcCall)
gen_logoASM_Div_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Div)
gen_logoASM_Equals_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Equals)
gen_logoASM_Greater_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Greater)
gen_logoASM_Lower_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Lower)
gen_logoASM_ParameterCall_Expression = Generalization(general=Expression, specific=logoASM_ParameterCall)
gen_logoASM_Plus_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Plus)
gen_logoASM_Minus_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Minus)
gen_logoASM_Mult_BinaryExp = Generalization(general=BinaryExp, specific=logoASM_Mult)

# Domain Model
domain_model = DomainModel(
    name="logoASM",
    types={logoASM_Instruction, logoASM_Primitive, Instruction, logoASM_Back, Primitive, logoASM_Expression, logoASM_Forward, logoASM_Left, logoASM_Right, logoASM_PenDown, logoASM_PenUp, logoASM_Clear, logoASM_BinaryExp, Expression, logoASM_ProcDeclaration, logoASM_Parameter, logoASM_Block, logoASM_If, ControlStructure, logoASM_ControlStructure, logoASM_Repeat, logoASM_While, logoASM_Constant, logoASM_ProcCall, logoASM_Div, logoASM_Equals, logoASM_Greater, logoASM_Lower, logoASM_LogoProgram, logoASM_ParameterCall, logoASM_Plus, BinaryExp, logoASM_Minus, logoASM_Mult},
    associations={steps0, steps1, angle3, angle5, lhs7, rhs9, actualArgs12, declaration14, args16, instructions18, instructions20, thenPart22, elsePart24, condition27, block29, block31, instructions35, parameter33},
    generalizations={gen_logoASM_Primitive_Instruction, gen_logoASM_Back_Primitive, gen_logoASM_Forward_Primitive, gen_logoASM_Left_Primitive, gen_logoASM_Right_Primitive, gen_logoASM_PenDown_Primitive, gen_logoASM_PenUp_Primitive, gen_logoASM_Clear_Primitive, gen_logoASM_Expression_Instruction, gen_logoASM_BinaryExp_Expression, gen_logoASM_ProcDeclaration_Instruction, gen_logoASM_Block_Instruction, gen_logoASM_If_ControlStructure, gen_logoASM_ControlStructure_Instruction, gen_logoASM_Repeat_ControlStructure, gen_logoASM_While_ControlStructure, gen_logoASM_Constant_Expression, gen_logoASM_ProcCall_Expression, gen_logoASM_Div_BinaryExp, gen_logoASM_Equals_BinaryExp, gen_logoASM_Greater_BinaryExp, gen_logoASM_Lower_BinaryExp, gen_logoASM_ParameterCall_Expression, gen_logoASM_Plus_BinaryExp, gen_logoASM_Minus_BinaryExp, gen_logoASM_Mult_BinaryExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)