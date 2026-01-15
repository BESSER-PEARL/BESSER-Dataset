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
typeB_RootB = Class(name="typeB::RootB")
typeB_ElementB = Class(name="typeB::ElementB")

# typeB_RootB class attributes and methods

# typeB_ElementB class attributes and methods
typeB_ElementB_name: Property = Property(name="name", type=StringType)
typeB_ElementB.attributes={typeB_ElementB_name}

# Relationships
elms0: BinaryAssociation = BinaryAssociation(
    name="elms0",
    ends={
        Property(name="typeB_ElementB", type=typeB_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="typeB_RootB", type=typeB_ElementB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="typeB",
    types={typeB_RootB, typeB_ElementB},
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