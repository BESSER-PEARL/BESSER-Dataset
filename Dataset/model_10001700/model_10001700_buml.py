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
C1 = Class(name="C1")
C2 = Class(name="C2")
C3 = Class(name="C3")

# C1 class attributes and methods
C1_C1ID: Property = Property(name="C1ID", type=IntegerType)
C1.attributes={C1_C1ID}

# C2 class attributes and methods
C2_C2ID: Property = Property(name="C2ID", type=IntegerType)
C2_C1ID: Property = Property(name="C1ID", type=IntegerType)
C2_attribute: Property = Property(name="attribute", type=StringType)
C2.attributes={C2_attribute, C2_C1ID, C2_C2ID}

# C3 class attributes and methods

# Relationships
C1_C2: BinaryAssociation = BinaryAssociation(
    name="C1_C2",
    ends={
        Property(name="c20", type=C2, multiplicity=Multiplicity(1, 9999)),
        Property(name="c11", type=C1, multiplicity=Multiplicity(0, 1))
    }
)
C1_C3: BinaryAssociation = BinaryAssociation(
    name="C1_C3",
    ends={
        Property(name="c32", type=C3, multiplicity=Multiplicity(0, 1)),
        Property(name="c13", type=C1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_PUODQIBvEei_m5BAOg12zA",
    types={C1, C2, C3},
    associations={C1_C2, C1_C3},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)