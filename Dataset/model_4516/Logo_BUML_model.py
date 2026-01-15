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
logo_Right = Class(name="logo::Right")
logo_PenDown = Class(name="logo::PenDown")
logo_PenUp = Class(name="logo::PenUp")
logo_Clear = Class(name="logo::Clear")
logo_LogoProgram = Class(name="logo::LogoProgram")
logo_Instruction = Class(name="logo::Instruction")
logo_Backward = Class(name="logo::Backward")
Instruction = Class(name="Instruction")
logo_Expression = Class(name="logo::Expression")
logo_Forward = Class(name="logo::Forward")
logo_Left = Class(name="logo::Left")
logo_ParameterCall = Class(name="logo::ParameterCall")
logo_Constant = Class(name="logo::Constant")
Expression = Class(name="Expression")
logo_ProcCall = Class(name="logo::ProcCall")
logo_ProcDeclaration = Class(name="logo::ProcDeclaration")
logo_Parameter = Class(name="logo::Parameter")
logo_Block = Class(name="logo::Block")
logo_If = Class(name="logo::If")
logo_Repeat = Class(name="logo::Repeat")
logo_While = Class(name="logo::While")
logo_Div = Class(name="logo::Div")
logo_Equals = Class(name="logo::Equals")
logo_Greater = Class(name="logo::Greater")
logo_Lower = Class(name="logo::Lower")
logo_Plus = Class(name="logo::Plus")
logo_Minus = Class(name="logo::Minus")
logo_Mult = Class(name="logo::Mult")

# logo_Right class attributes and methods

# logo_PenDown class attributes and methods

# logo_PenUp class attributes and methods

# logo_Clear class attributes and methods

# logo_LogoProgram class attributes and methods

# logo_Instruction class attributes and methods

# logo_Backward class attributes and methods

# Instruction class attributes and methods

# logo_Expression class attributes and methods

# logo_Forward class attributes and methods

# logo_Left class attributes and methods

# logo_ParameterCall class attributes and methods

# logo_Constant class attributes and methods
logo_Constant_integerValue: Property = Property(name="integerValue", type=IntegerType)
logo_Constant.attributes={logo_Constant_integerValue}

# Expression class attributes and methods

# logo_ProcCall class attributes and methods

# logo_ProcDeclaration class attributes and methods
logo_ProcDeclaration_name: Property = Property(name="name", type=StringType)
logo_ProcDeclaration.attributes={logo_ProcDeclaration_name}

# logo_Parameter class attributes and methods
logo_Parameter_name: Property = Property(name="name", type=StringType)
logo_Parameter.attributes={logo_Parameter_name}

# logo_Block class attributes and methods

# logo_If class attributes and methods

# logo_Repeat class attributes and methods

# logo_While class attributes and methods

# logo_Div class attributes and methods

# logo_Equals class attributes and methods

# logo_Greater class attributes and methods

# logo_Lower class attributes and methods

# logo_Plus class attributes and methods

# logo_Minus class attributes and methods

# logo_Mult class attributes and methods

# Relationships
angle4: BinaryAssociation = BinaryAssociation(
    name="angle4",
    ends={
        Property(name="logo_Expression5", type=logo_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Left", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle6: BinaryAssociation = BinaryAssociation(
    name="angle6",
    ends={
        Property(name="logo_Expression7", type=logo_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Right", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="logo_Instruction", type=logo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_LogoProgram", type=logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="logo_Expression", type=logo_Backward, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Backward", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
steps2: BinaryAssociation = BinaryAssociation(
    name="steps2",
    ends={
        Property(name="logo_Expression3", type=logo_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Forward", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition32: BinaryAssociation = BinaryAssociation(
    name="condition32",
    ends={
        Property(name="logo_Expression33", type=logo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_While", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block34: BinaryAssociation = BinaryAssociation(
    name="block34",
    ends={
        Property(name="logo_Block36", type=logo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_While35", type=logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter37: BinaryAssociation = BinaryAssociation(
    name="parameter37",
    ends={
        Property(name="logo_Parameter38", type=logo_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ParameterCall", type=logo_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
declaration8: BinaryAssociation = BinaryAssociation(
    name="declaration8",
    ends={
        Property(name="logo_ProcDeclaration", type=logo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcCall", type=logo_ProcDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
actualArgs9: BinaryAssociation = BinaryAssociation(
    name="actualArgs9",
    ends={
        Property(name="logo_Expression11", type=logo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcCall10", type=logo_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args12: BinaryAssociation = BinaryAssociation(
    name="args12",
    ends={
        Property(name="logo_Parameter", type=logo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcDeclaration13", type=logo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions14: BinaryAssociation = BinaryAssociation(
    name="instructions14",
    ends={
        Property(name="logo_Instruction16", type=logo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcDeclaration15", type=logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions17: BinaryAssociation = BinaryAssociation(
    name="instructions17",
    ends={
        Property(name="logo_Instruction18", type=logo_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Block", type=logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition19: BinaryAssociation = BinaryAssociation(
    name="condition19",
    ends={
        Property(name="logo_Expression20", type=logo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_If", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart21: BinaryAssociation = BinaryAssociation(
    name="thenPart21",
    ends={
        Property(name="logo_Block23", type=logo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_If22", type=logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart24: BinaryAssociation = BinaryAssociation(
    name="elsePart24",
    ends={
        Property(name="logo_Block26", type=logo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_If25", type=logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition27: BinaryAssociation = BinaryAssociation(
    name="condition27",
    ends={
        Property(name="logo_Expression28", type=logo_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Repeat", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block29: BinaryAssociation = BinaryAssociation(
    name="block29",
    ends={
        Property(name="logo_Block31", type=logo_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Repeat30", type=logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs66: BinaryAssociation = BinaryAssociation(
    name="rhs66",
    ends={
        Property(name="logo_Expression68", type=logo_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Mult67", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs69: BinaryAssociation = BinaryAssociation(
    name="lhs69",
    ends={
        Property(name="logo_Expression70", type=logo_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Div", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs71: BinaryAssociation = BinaryAssociation(
    name="rhs71",
    ends={
        Property(name="logo_Expression73", type=logo_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Div72", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs39: BinaryAssociation = BinaryAssociation(
    name="lhs39",
    ends={
        Property(name="logo_Expression40", type=logo_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Equals", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs41: BinaryAssociation = BinaryAssociation(
    name="rhs41",
    ends={
        Property(name="logo_Expression43", type=logo_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Equals42", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs44: BinaryAssociation = BinaryAssociation(
    name="lhs44",
    ends={
        Property(name="logo_Expression45", type=logo_Greater, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Greater", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs46: BinaryAssociation = BinaryAssociation(
    name="rhs46",
    ends={
        Property(name="logo_Expression48", type=logo_Greater, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Greater47", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs49: BinaryAssociation = BinaryAssociation(
    name="lhs49",
    ends={
        Property(name="logo_Expression50", type=logo_Lower, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Lower", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs51: BinaryAssociation = BinaryAssociation(
    name="rhs51",
    ends={
        Property(name="logo_Expression53", type=logo_Lower, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Lower52", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs54: BinaryAssociation = BinaryAssociation(
    name="lhs54",
    ends={
        Property(name="logo_Expression55", type=logo_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Plus", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs56: BinaryAssociation = BinaryAssociation(
    name="rhs56",
    ends={
        Property(name="logo_Expression58", type=logo_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Plus57", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs59: BinaryAssociation = BinaryAssociation(
    name="lhs59",
    ends={
        Property(name="logo_Expression60", type=logo_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Minus", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs61: BinaryAssociation = BinaryAssociation(
    name="rhs61",
    ends={
        Property(name="logo_Expression63", type=logo_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Minus62", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs64: BinaryAssociation = BinaryAssociation(
    name="lhs64",
    ends={
        Property(name="logo_Expression65", type=logo_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Mult", type=logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_logo_Right_Instruction = Generalization(general=Instruction, specific=logo_Right)
gen_logo_PenDown_Instruction = Generalization(general=Instruction, specific=logo_PenDown)
gen_logo_PenUp_Instruction = Generalization(general=Instruction, specific=logo_PenUp)
gen_logo_Clear_Instruction = Generalization(general=Instruction, specific=logo_Clear)
gen_logo_Backward_Instruction = Generalization(general=Instruction, specific=logo_Backward)
gen_logo_Forward_Instruction = Generalization(general=Instruction, specific=logo_Forward)
gen_logo_Left_Instruction = Generalization(general=Instruction, specific=logo_Left)
gen_logo_ParameterCall_Instruction = Generalization(general=Instruction, specific=logo_ParameterCall)
gen_logo_ParameterCall_Expression = Generalization(general=Expression, specific=logo_ParameterCall)
gen_logo_Constant_Expression = Generalization(general=Expression, specific=logo_Constant)
gen_logo_ProcCall_Instruction = Generalization(general=Instruction, specific=logo_ProcCall)
gen_logo_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=logo_ProcDeclaration)
gen_logo_Block_Instruction = Generalization(general=Instruction, specific=logo_Block)
gen_logo_If_Instruction = Generalization(general=Instruction, specific=logo_If)
gen_logo_Repeat_Instruction = Generalization(general=Instruction, specific=logo_Repeat)
gen_logo_While_Instruction = Generalization(general=Instruction, specific=logo_While)
gen_logo_Div_Expression = Generalization(general=Expression, specific=logo_Div)
gen_logo_Equals_Expression = Generalization(general=Expression, specific=logo_Equals)
gen_logo_Greater_Expression = Generalization(general=Expression, specific=logo_Greater)
gen_logo_Lower_Expression = Generalization(general=Expression, specific=logo_Lower)
gen_logo_Plus_Expression = Generalization(general=Expression, specific=logo_Plus)
gen_logo_Minus_Expression = Generalization(general=Expression, specific=logo_Minus)
gen_logo_Mult_Expression = Generalization(general=Expression, specific=logo_Mult)

# Domain Model
domain_model = DomainModel(
    name="logo",
    types={logo_Right, logo_PenDown, logo_PenUp, logo_Clear, logo_LogoProgram, logo_Instruction, logo_Backward, Instruction, logo_Expression, logo_Forward, logo_Left, logo_ParameterCall, logo_Constant, Expression, logo_ProcCall, logo_ProcDeclaration, logo_Parameter, logo_Block, logo_If, logo_Repeat, logo_While, logo_Div, logo_Equals, logo_Greater, logo_Lower, logo_Plus, logo_Minus, logo_Mult},
    associations={angle4, angle6, instructions0, steps1, steps2, condition32, block34, parameter37, declaration8, actualArgs9, args12, instructions14, instructions17, condition19, thenPart21, elsePart24, condition27, block29, rhs66, lhs69, rhs71, lhs39, rhs41, lhs44, rhs46, lhs49, rhs51, lhs54, rhs56, lhs59, rhs61, lhs64},
    generalizations={gen_logo_Right_Instruction, gen_logo_PenDown_Instruction, gen_logo_PenUp_Instruction, gen_logo_Clear_Instruction, gen_logo_Backward_Instruction, gen_logo_Forward_Instruction, gen_logo_Left_Instruction, gen_logo_ParameterCall_Instruction, gen_logo_ParameterCall_Expression, gen_logo_Constant_Expression, gen_logo_ProcCall_Instruction, gen_logo_ProcDeclaration_Instruction, gen_logo_Block_Instruction, gen_logo_If_Instruction, gen_logo_Repeat_Instruction, gen_logo_While_Instruction, gen_logo_Div_Expression, gen_logo_Equals_Expression, gen_logo_Greater_Expression, gen_logo_Lower_Expression, gen_logo_Plus_Expression, gen_logo_Minus_Expression, gen_logo_Mult_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)