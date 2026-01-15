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
typeA_RootA = Class(name="typeA::RootA")
typeA_ElementA = Class(name="typeA::ElementA")

# typeA_RootA class attributes and methods
typeA_RootA_name: Property = Property(name="name", type=StringType)
typeA_RootA.attributes={typeA_RootA_name}

# typeA_ElementA class attributes and methods
typeA_ElementA_name: Property = Property(name="name", type=StringType)
typeA_ElementA.attributes={typeA_ElementA_name}

# Relationships
elms0: BinaryAssociation = BinaryAssociation(
    name="elms0",
    ends={
        Property(name="typeA_ElementA", type=typeA_RootA, multiplicity=Multiplicity(1, 1)),
        Property(name="typeA_RootA", type=typeA_ElementA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="typeA",
    types={typeA_RootA, typeA_ElementA},
    associations={elms0},
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