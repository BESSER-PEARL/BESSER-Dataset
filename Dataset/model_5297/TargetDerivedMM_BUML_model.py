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
tderived_D = Class(name="tderived::D")
tderived_B2 = Class(name="tderived::B2")
B = Class(name="B")
tderived_A2 = Class(name="tderived::A2")
A = Class(name="A")

# tderived_D class attributes and methods

# tderived_B2 class attributes and methods
tderived_B2_anotherName: Property = Property(name="anotherName", type=StringType)
tderived_B2.attributes={tderived_B2_anotherName}

# B class attributes and methods

# tderived_A2 class attributes and methods

# A class attributes and methods

# Relationships
ownsD0: BinaryAssociation = BinaryAssociation(
    name="ownsD0",
    ends={
        Property(name="tderived_D", type=tderived_A2, multiplicity=Multiplicity(1, 1)),
        Property(name="tderived_A2", type=tderived_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tderived_A2_A = Generalization(general=A, specific=tderived_A2)
gen_tderived_B2_B = Generalization(general=B, specific=tderived_B2)

# Domain Model
domain_model = DomainModel(
    name="tderived",
    types={tderived_D, tderived_B2, B, tderived_A2, A},
    associations={ownsD0},
    generalizations={gen_tderived_A2_A, gen_tderived_B2_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)