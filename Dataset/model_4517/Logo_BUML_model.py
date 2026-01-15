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
Logo_LogoProgram = Class(name="Logo::LogoProgram")
Logo_Primitive = Class(name="Logo::Primitive", is_abstract=True)
Logo_Back = Class(name="Logo::Back")
Primitive = Class(name="Primitive")
Logo_Expression = Class(name="Logo::Expression")
Logo_Right = Class(name="Logo::Right")
Logo_PenDown = Class(name="Logo::PenDown")
Logo_PenUp = Class(name="Logo::PenUp")
Logo_Clear = Class(name="Logo::Clear")
Logo_Forward = Class(name="Logo::Forward")
Logo_Left = Class(name="Logo::Left")

# Logo_LogoProgram class attributes and methods

# Logo_Primitive class attributes and methods

# Logo_Back class attributes and methods

# Primitive class attributes and methods

# Logo_Expression class attributes and methods
Logo_Expression_m_eval: Method = Method(name="eval", parameters={Parameter(name='context')})
Logo_Expression.methods={Logo_Expression_m_eval}

# Logo_Right class attributes and methods

# Logo_PenDown class attributes and methods

# Logo_PenUp class attributes and methods

# Logo_Clear class attributes and methods

# Logo_Forward class attributes and methods

# Logo_Left class attributes and methods

# Relationships
primitives0: BinaryAssociation = BinaryAssociation(
    name="primitives0",
    ends={
        Property(name="Logo_Primitive", type=Logo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_LogoProgram", type=Logo_Primitive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="Logo_Expression", type=Logo_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Back", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle6: BinaryAssociation = BinaryAssociation(
    name="angle6",
    ends={
        Property(name="Logo_Expression7", type=Logo_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Right", type=Logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
steps2: BinaryAssociation = BinaryAssociation(
    name="steps2",
    ends={
        Property(name="Logo_Expression3", type=Logo_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Forward", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle4: BinaryAssociation = BinaryAssociation(
    name="angle4",
    ends={
        Property(name="Logo_Expression5", type=Logo_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Left", type=Logo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_Logo_Back_Primitive = Generalization(general=Primitive, specific=Logo_Back)
gen_Logo_Right_Primitive = Generalization(general=Primitive, specific=Logo_Right)
gen_Logo_PenDown_Primitive = Generalization(general=Primitive, specific=Logo_PenDown)
gen_Logo_PenUp_Primitive = Generalization(general=Primitive, specific=Logo_PenUp)
gen_Logo_Clear_Primitive = Generalization(general=Primitive, specific=Logo_Clear)
gen_Logo_Forward_Primitive = Generalization(general=Primitive, specific=Logo_Forward)
gen_Logo_Left_Primitive = Generalization(general=Primitive, specific=Logo_Left)

# Domain Model
domain_model = DomainModel(
    name="Logo",
    types={Logo_LogoProgram, Logo_Primitive, Logo_Back, Primitive, Logo_Expression, Logo_Right, Logo_PenDown, Logo_PenUp, Logo_Clear, Logo_Forward, Logo_Left},
    associations={primitives0, steps1, angle6, steps2, angle4},
    generalizations={gen_Logo_Back_Primitive, gen_Logo_Right_Primitive, gen_Logo_PenDown_Primitive, gen_Logo_PenUp_Primitive, gen_Logo_Clear_Primitive, gen_Logo_Forward_Primitive, gen_Logo_Left_Primitive},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)