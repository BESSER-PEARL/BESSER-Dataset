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
C = Class(name="C")
source_C = Class(name="source::C")
source_D = Class(name="source::D")
B = Class(name="B")
source_A = Class(name="source::A")
source_B = Class(name="source::B")

# C class attributes and methods

# source_C class attributes and methods

# source_D class attributes and methods

# B class attributes and methods

# source_A class attributes and methods

# source_B class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="source_B", type=source_A, multiplicity=Multiplicity(1, 1)),
        Property(name="source_A", type=source_B, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_source_B_C = Generalization(general=C, specific=source_B)
gen_source_D_B = Generalization(general=B, specific=source_D)

# Domain Model
domain_model = DomainModel(
    name="source",
    types={C, source_C, source_D, B, source_A, source_B},
    associations={b0},
    generalizations={gen_source_B_C, gen_source_D_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)