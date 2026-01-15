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
kmLogo_BinaryExp = Class(name="kmLogo::BinaryExp", is_abstract=True)
kmLogo_Constant = Class(name="kmLogo::Constant")
kmLogo_Block = Class(name="kmLogo::Block")
kmLogo_If = Class(name="kmLogo::If")
ControlStructure = Class(name="ControlStructure")
kmLogo_ControlStructure = Class(name="kmLogo::ControlStructure")
kmLogo_For = Class(name="kmLogo::For")
kmLogo_Instruction = Class(name="kmLogo::Instruction", is_abstract=True)
kmLogo_MethodeCall = Class(name="kmLogo::MethodeCall")
Expression = Class(name="Expression")
kmLogo_MethodeDeclaration = Class(name="kmLogo::MethodeDeclaration")
kmLogo_Expression = Class(name="kmLogo::Expression", is_abstract=True)
Instruction = Class(name="Instruction")
kmLogo_Greater = Class(name="kmLogo::Greater")
kmLogo_Lower = Class(name="kmLogo::Lower")
kmLogo_JavaProgram = Class(name="kmLogo::JavaProgram")
kmLogo_Main = Class(name="kmLogo::Main")
kmLogo_While = Class(name="kmLogo::While")
kmLogo_Parameter = Class(name="kmLogo::Parameter")
kmLogo_ParameterCall = Class(name="kmLogo::ParameterCall")
kmLogo_Plus = Class(name="kmLogo::Plus")
BinaryExp = Class(name="BinaryExp")
kmLogo_Minus = Class(name="kmLogo::Minus")
kmLogo_Mult = Class(name="kmLogo::Mult")
kmLogo_Div = Class(name="kmLogo::Div")
kmLogo_Equals = Class(name="kmLogo::Equals")

# kmLogo_BinaryExp class attributes and methods

# kmLogo_Constant class attributes and methods
kmLogo_Constant_integerValue: Property = Property(name="integerValue", type=StringType)
kmLogo_Constant.attributes={kmLogo_Constant_integerValue}

# kmLogo_Block class attributes and methods

# kmLogo_If class attributes and methods

# ControlStructure class attributes and methods

# kmLogo_ControlStructure class attributes and methods

# kmLogo_For class attributes and methods

# kmLogo_Instruction class attributes and methods

# kmLogo_MethodeCall class attributes and methods

# Expression class attributes and methods

# kmLogo_MethodeDeclaration class attributes and methods
kmLogo_MethodeDeclaration_name: Property = Property(name="name", type=StringType)
kmLogo_MethodeDeclaration.attributes={kmLogo_MethodeDeclaration_name}

# kmLogo_Expression class attributes and methods

# Instruction class attributes and methods

# kmLogo_Greater class attributes and methods

# kmLogo_Lower class attributes and methods

# kmLogo_JavaProgram class attributes and methods
kmLogo_JavaProgram_name: Property = Property(name="name", type=StringType)
kmLogo_JavaProgram.attributes={kmLogo_JavaProgram_name}

# kmLogo_Main class attributes and methods

# kmLogo_While class attributes and methods

# kmLogo_Parameter class attributes and methods
kmLogo_Parameter_name: Property = Property(name="name", type=StringType)
kmLogo_Parameter.attributes={kmLogo_Parameter_name}

# kmLogo_ParameterCall class attributes and methods

# kmLogo_Plus class attributes and methods

# BinaryExp class attributes and methods

# kmLogo_Minus class attributes and methods

# kmLogo_Mult class attributes and methods

# kmLogo_Div class attributes and methods

# kmLogo_Equals class attributes and methods

# Relationships
lhs2: BinaryAssociation = BinaryAssociation(
    name="lhs2",
    ends={
        Property(name="kmLogo_Expression3", type=kmLogo_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_BinaryExp", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs4: BinaryAssociation = BinaryAssociation(
    name="rhs4",
    ends={
        Property(name="kmLogo_Expression6", type=kmLogo_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_BinaryExp5", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions7: BinaryAssociation = BinaryAssociation(
    name="instructions7",
    ends={
        Property(name="kmLogo_Instruction", type=kmLogo_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Block", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart8: BinaryAssociation = BinaryAssociation(
    name="thenPart8",
    ends={
        Property(name="kmLogo_Block9", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart10: BinaryAssociation = BinaryAssociation(
    name="elsePart10",
    ends={
        Property(name="kmLogo_Block12", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If11", type=kmLogo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="kmLogo_Expression14", type=kmLogo_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ControlStructure", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block15: BinaryAssociation = BinaryAssociation(
    name="block15",
    ends={
        Property(name="kmLogo_Block16", type=kmLogo_For, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_For", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodedeclaration0: BinaryAssociation = BinaryAssociation(
    name="methodedeclaration0",
    ends={
        Property(name="MethodeDeclaration", type=kmLogo_MethodeCall, multiplicity=Multiplicity(1, 1)),
        Property(name="methodecall", type=kmLogo_MethodeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="kmLogo_Expression", type=kmLogo_MethodeCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_MethodeCall", type=kmLogo_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main20: BinaryAssociation = BinaryAssociation(
    name="main20",
    ends={
        Property(name="kmLogo_Main", type=kmLogo_JavaProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_JavaProgram", type=kmLogo_Main, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodeDeclaration21: BinaryAssociation = BinaryAssociation(
    name="methodeDeclaration21",
    ends={
        Property(name="kmLogo_MethodeDeclaration", type=kmLogo_JavaProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_JavaProgram22", type=kmLogo_MethodeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instruction23: BinaryAssociation = BinaryAssociation(
    name="instruction23",
    ends={
        Property(name="kmLogo_Instruction25", type=kmLogo_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Main24", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instruction26: BinaryAssociation = BinaryAssociation(
    name="instruction26",
    ends={
        Property(name="kmLogo_Instruction28", type=kmLogo_MethodeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_MethodeDeclaration27", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter29: BinaryAssociation = BinaryAssociation(
    name="parameter29",
    ends={
        Property(name="kmLogo_Parameter31", type=kmLogo_MethodeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_MethodeDeclaration30", type=kmLogo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodecall32: BinaryAssociation = BinaryAssociation(
    name="methodecall32",
    ends={
        Property(name="MethodeCall", type=kmLogo_MethodeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodedeclaration", type=kmLogo_MethodeCall, multiplicity=Multiplicity(0, 9999))
    }
)
block17: BinaryAssociation = BinaryAssociation(
    name="block17",
    ends={
        Property(name="kmLogo_Block18", type=kmLogo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_While", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter19: BinaryAssociation = BinaryAssociation(
    name="parameter19",
    ends={
        Property(name="kmLogo_Parameter", type=kmLogo_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ParameterCall", type=kmLogo_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_kmLogo_BinaryExp_Expression = Generalization(general=Expression, specific=kmLogo_BinaryExp)
gen_kmLogo_Constant_Expression = Generalization(general=Expression, specific=kmLogo_Constant)
gen_kmLogo_Block_Instruction = Generalization(general=Instruction, specific=kmLogo_Block)
gen_kmLogo_If_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_If)
gen_kmLogo_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmLogo_ControlStructure)
gen_kmLogo_For_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_For)
gen_kmLogo_MethodeCall_Expression = Generalization(general=Expression, specific=kmLogo_MethodeCall)
gen_kmLogo_Expression_Instruction = Generalization(general=Instruction, specific=kmLogo_Expression)
gen_kmLogo_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Greater)
gen_kmLogo_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Lower)
gen_kmLogo_MethodeDeclaration_Instruction = Generalization(general=Instruction, specific=kmLogo_MethodeDeclaration)
gen_kmLogo_While_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_While)
gen_kmLogo_ParameterCall_Expression = Generalization(general=Expression, specific=kmLogo_ParameterCall)
gen_kmLogo_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Plus)
gen_kmLogo_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Minus)
gen_kmLogo_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Mult)
gen_kmLogo_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Div)
gen_kmLogo_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Equals)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_BinaryExp, kmLogo_Constant, kmLogo_Block, kmLogo_If, ControlStructure, kmLogo_ControlStructure, kmLogo_For, kmLogo_Instruction, kmLogo_MethodeCall, Expression, kmLogo_MethodeDeclaration, kmLogo_Expression, Instruction, kmLogo_Greater, kmLogo_Lower, kmLogo_JavaProgram, kmLogo_Main, kmLogo_While, kmLogo_Parameter, kmLogo_ParameterCall, kmLogo_Plus, BinaryExp, kmLogo_Minus, kmLogo_Mult, kmLogo_Div, kmLogo_Equals},
    associations={lhs2, rhs4, instructions7, thenPart8, elsePart10, condition13, block15, methodedeclaration0, expression1, main20, methodeDeclaration21, instruction23, instruction26, parameter29, methodecall32, block17, parameter19},
    generalizations={gen_kmLogo_BinaryExp_Expression, gen_kmLogo_Constant_Expression, gen_kmLogo_Block_Instruction, gen_kmLogo_If_ControlStructure, gen_kmLogo_ControlStructure_Instruction, gen_kmLogo_For_ControlStructure, gen_kmLogo_MethodeCall_Expression, gen_kmLogo_Expression_Instruction, gen_kmLogo_Greater_BinaryExp, gen_kmLogo_Lower_BinaryExp, gen_kmLogo_MethodeDeclaration_Instruction, gen_kmLogo_While_ControlStructure, gen_kmLogo_ParameterCall_Expression, gen_kmLogo_Plus_BinaryExp, gen_kmLogo_Minus_BinaryExp, gen_kmLogo_Mult_BinaryExp, gen_kmLogo_Div_BinaryExp, gen_kmLogo_Equals_BinaryExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)