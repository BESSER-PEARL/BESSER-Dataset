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
ABC_B = Class(name="ABC::B")
A = Class(name="A")
ABC_C = Class(name="ABC::C")
ABC_D = Class(name="ABC::D")
ABC_A = Class(name="ABC::A", is_abstract=True)

# ABC_B class attributes and methods

# A class attributes and methods

# ABC_C class attributes and methods

# ABC_D class attributes and methods

# ABC_A class attributes and methods

# Relationships
aes0: BinaryAssociation = BinaryAssociation(
    name="aes0",
    ends={
        Property(name="ABC_A", type=ABC_D, multiplicity=Multiplicity(1, 1)),
        Property(name="ABC_D", type=ABC_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ABC_B_A = Generalization(general=A, specific=ABC_B)
gen_ABC_C_A = Generalization(general=A, specific=ABC_C)

# Domain Model
domain_model = DomainModel(
    name="ABC",
    types={ABC_B, A, ABC_C, ABC_D, ABC_A},
    associations={aes0},
    generalizations={gen_ABC_B_A, gen_ABC_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)