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
PrimitivesProv_Primitive = Class(name="PrimitivesProv::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
PrimitivesProv_Forward = Class(name="PrimitivesProv::Forward")
Primitive = Class(name="Primitive")
PrimitivesProv_Back = Class(name="PrimitivesProv::Back")
PrimitivesProv_Left = Class(name="PrimitivesProv::Left")
PrimitivesProv_Right = Class(name="PrimitivesProv::Right")
PrimitivesProv_LogoProgram = Class(name="PrimitivesProv::LogoProgram")
PrimitivesProv_Instruction = Class(name="PrimitivesProv::Instruction", is_abstract=True)

# PrimitivesProv_Primitive class attributes and methods

# Instruction class attributes and methods

# PrimitivesProv_Forward class attributes and methods

# Primitive class attributes and methods

# PrimitivesProv_Back class attributes and methods

# PrimitivesProv_Left class attributes and methods

# PrimitivesProv_Right class attributes and methods

# PrimitivesProv_LogoProgram class attributes and methods

# PrimitivesProv_Instruction class attributes and methods
PrimitivesProv_Instruction_m_evalInstruction: Method = Method(name="evalInstruction", parameters={Parameter(name='context')})
PrimitivesProv_Instruction.methods={PrimitivesProv_Instruction_m_evalInstruction}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="PrimitivesProv_Instruction", type=PrimitivesProv_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="PrimitivesProv_LogoProgram", type=PrimitivesProv_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PrimitivesProv_Primitive_Instruction = Generalization(general=Instruction, specific=PrimitivesProv_Primitive)
gen_PrimitivesProv_Forward_Primitive = Generalization(general=Primitive, specific=PrimitivesProv_Forward)
gen_PrimitivesProv_Back_Primitive = Generalization(general=Primitive, specific=PrimitivesProv_Back)
gen_PrimitivesProv_Left_Primitive = Generalization(general=Primitive, specific=PrimitivesProv_Left)
gen_PrimitivesProv_Right_Primitive = Generalization(general=Primitive, specific=PrimitivesProv_Right)

# Domain Model
domain_model = DomainModel(
    name="PrimitivesProv",
    types={PrimitivesProv_Primitive, Instruction, PrimitivesProv_Forward, Primitive, PrimitivesProv_Back, PrimitivesProv_Left, PrimitivesProv_Right, PrimitivesProv_LogoProgram, PrimitivesProv_Instruction},
    associations={instructions0},
    generalizations={gen_PrimitivesProv_Primitive_Instruction, gen_PrimitivesProv_Forward_Primitive, gen_PrimitivesProv_Back_Primitive, gen_PrimitivesProv_Left_Primitive, gen_PrimitivesProv_Right_Primitive},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)