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
logo_LogoProgram = Class(name="logo::LogoProgram")
logo_Instruction = Class(name="logo::Instruction")
logo_Forward = Class(name="logo::Forward")
logo_Left = Class(name="logo::Left")
logo_Right = Class(name="logo::Right")
logo_ProcDeclaration = Class(name="logo::ProcDeclaration")
Instruction = Class(name="Instruction")
logo_Parameter = Class(name="logo::Parameter")
logo_ProcCall = Class(name="logo::ProcCall")

# logo_LogoProgram class attributes and methods

# logo_Instruction class attributes and methods

# logo_Forward class attributes and methods
logo_Forward_steps: Property = Property(name="steps", type=IntegerType)
logo_Forward.attributes={logo_Forward_steps}

# logo_Left class attributes and methods
logo_Left_angle: Property = Property(name="angle", type=IntegerType)
logo_Left.attributes={logo_Left_angle}

# logo_Right class attributes and methods
logo_Right_angle: Property = Property(name="angle", type=IntegerType)
logo_Right.attributes={logo_Right_angle}

# logo_ProcDeclaration class attributes and methods
logo_ProcDeclaration_name: Property = Property(name="name", type=StringType)
logo_ProcDeclaration.attributes={logo_ProcDeclaration_name}

# Instruction class attributes and methods

# logo_Parameter class attributes and methods
logo_Parameter_name: Property = Property(name="name", type=StringType)
logo_Parameter.attributes={logo_Parameter_name}

# logo_ProcCall class attributes and methods
logo_ProcCall_actualArgs: Property = Property(name="actualArgs", type=IntegerType)
logo_ProcCall.attributes={logo_ProcCall_actualArgs}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="logo_Instruction", type=logo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_LogoProgram", type=logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args1: BinaryAssociation = BinaryAssociation(
    name="args1",
    ends={
        Property(name="logo_Parameter", type=logo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcDeclaration", type=logo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions2: BinaryAssociation = BinaryAssociation(
    name="instructions2",
    ends={
        Property(name="logo_Instruction4", type=logo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcDeclaration3", type=logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration5: BinaryAssociation = BinaryAssociation(
    name="declaration5",
    ends={
        Property(name="logo_ProcDeclaration6", type=logo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_ProcCall", type=logo_ProcDeclaration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_logo_Forward_Instruction = Generalization(general=Instruction, specific=logo_Forward)
gen_logo_Left_Instruction = Generalization(general=Instruction, specific=logo_Left)
gen_logo_Right_Instruction = Generalization(general=Instruction, specific=logo_Right)
gen_logo_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=logo_ProcDeclaration)
gen_logo_ProcCall_Instruction = Generalization(general=Instruction, specific=logo_ProcCall)

# Domain Model
domain_model = DomainModel(
    name="logo",
    types={logo_LogoProgram, logo_Instruction, logo_Forward, logo_Left, logo_Right, logo_ProcDeclaration, Instruction, logo_Parameter, logo_ProcCall},
    associations={instructions0, args1, instructions2, declaration5},
    generalizations={gen_logo_Forward_Instruction, gen_logo_Left_Instruction, gen_logo_Right_Instruction, gen_logo_ProcDeclaration_Instruction, gen_logo_ProcCall_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)