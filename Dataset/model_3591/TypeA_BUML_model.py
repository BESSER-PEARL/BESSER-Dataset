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
TypeA_A = Class(name="TypeA::A")
TypeA_B = Class(name="TypeA::B")

# TypeA_A class attributes and methods
TypeA_A_nameA: Property = Property(name="nameA", type=StringType)
TypeA_A.attributes={TypeA_A_nameA}

# TypeA_B class attributes and methods
TypeA_B_nameB: Property = Property(name="nameB", type=StringType)
TypeA_B.attributes={TypeA_B_nameB}

# Relationships
elms1: BinaryAssociation = BinaryAssociation(
    name="elms1",
    ends={
        Property(name="TypeA_A3", type=TypeA_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_B2", type=TypeA_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elms0: BinaryAssociation = BinaryAssociation(
    name="elms0",
    ends={
        Property(name="TypeA_B", type=TypeA_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_A", type=TypeA_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeA",
    types={TypeA_A, TypeA_B},
    associations={elms1, elms0},
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