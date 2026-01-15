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
TypeB_A = Class(name="TypeB::A")
TypeB_B = Class(name="TypeB::B")

# TypeB_A class attributes and methods
TypeB_A_name: Property = Property(name="name", type=StringType)
TypeB_A_isNameABC: Property = Property(name="isNameABC", type=BooleanType)
TypeB_A.attributes={TypeB_A_name, TypeB_A_isNameABC}

# TypeB_B class attributes and methods
TypeB_B_name: Property = Property(name="name", type=StringType)
TypeB_B.attributes={TypeB_B_name}

# Relationships
elms0: BinaryAssociation = BinaryAssociation(
    name="elms0",
    ends={
        Property(name="TypeB_B", type=TypeB_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_A", type=TypeB_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elms1: BinaryAssociation = BinaryAssociation(
    name="elms1",
    ends={
        Property(name="TypeB_A3", type=TypeB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_B2", type=TypeB_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstAElement4: BinaryAssociation = BinaryAssociation(
    name="firstAElement4",
    ends={
        Property(name="TypeB_A6", type=TypeB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_B5", type=TypeB_A, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aElementWithName7: BinaryAssociation = BinaryAssociation(
    name="aElementWithName7",
    ends={
        Property(name="TypeB_A9", type=TypeB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_B8", type=TypeB_A, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeB",
    types={TypeB_A, TypeB_B},
    associations={elms0, elms1, firstAElement4, aElementWithName7},
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