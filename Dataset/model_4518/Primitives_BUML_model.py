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
Primitives_LogoProgram = Class(name="Primitives::LogoProgram")
Primitives_Instruction = Class(name="Primitives::Instruction", is_abstract=True)
Primitives_Primitive = Class(name="Primitives::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
Primitives_Forward = Class(name="Primitives::Forward")
Primitive = Class(name="Primitive")
Primitives_Expression = Class(name="Primitives::Expression", is_abstract=True)
Primitives_Back = Class(name="Primitives::Back")
Primitives_Left = Class(name="Primitives::Left")
Primitives_Right = Class(name="Primitives::Right")

# Primitives_LogoProgram class attributes and methods

# Primitives_Instruction class attributes and methods

# Primitives_Primitive class attributes and methods

# Instruction class attributes and methods

# Primitives_Forward class attributes and methods

# Primitive class attributes and methods

# Primitives_Expression class attributes and methods
Primitives_Expression_m_eval: Method = Method(name="eval", parameters={Parameter(name='context')}, type=StringType)
Primitives_Expression.methods={Primitives_Expression_m_eval}

# Primitives_Back class attributes and methods

# Primitives_Left class attributes and methods

# Primitives_Right class attributes and methods

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="Primitives_Instruction", type=Primitives_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="Primitives_LogoProgram", type=Primitives_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="Primitives_Expression", type=Primitives_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="Primitives_Forward", type=Primitives_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps2: BinaryAssociation = BinaryAssociation(
    name="steps2",
    ends={
        Property(name="Primitives_Expression3", type=Primitives_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="Primitives_Back", type=Primitives_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle4: BinaryAssociation = BinaryAssociation(
    name="angle4",
    ends={
        Property(name="Primitives_Expression5", type=Primitives_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="Primitives_Left", type=Primitives_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle6: BinaryAssociation = BinaryAssociation(
    name="angle6",
    ends={
        Property(name="Primitives_Expression7", type=Primitives_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="Primitives_Right", type=Primitives_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Primitives_Primitive_Instruction = Generalization(general=Instruction, specific=Primitives_Primitive)
gen_Primitives_Forward_Primitive = Generalization(general=Primitive, specific=Primitives_Forward)
gen_Primitives_Back_Primitive = Generalization(general=Primitive, specific=Primitives_Back)
gen_Primitives_Left_Primitive = Generalization(general=Primitive, specific=Primitives_Left)
gen_Primitives_Right_Primitive = Generalization(general=Primitive, specific=Primitives_Right)
gen_Primitives_Expression_Instruction = Generalization(general=Instruction, specific=Primitives_Expression)

# Domain Model
domain_model = DomainModel(
    name="Primitives",
    types={Primitives_LogoProgram, Primitives_Instruction, Primitives_Primitive, Instruction, Primitives_Forward, Primitive, Primitives_Expression, Primitives_Back, Primitives_Left, Primitives_Right},
    associations={instructions0, steps1, steps2, angle4, angle6},
    generalizations={gen_Primitives_Primitive_Instruction, gen_Primitives_Forward_Primitive, gen_Primitives_Back_Primitive, gen_Primitives_Left_Primitive, gen_Primitives_Right_Primitive, gen_Primitives_Expression_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)