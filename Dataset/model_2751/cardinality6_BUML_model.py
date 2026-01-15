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
cardinality6_Root = Class(name="cardinality6::Root")
cardinality6_A = Class(name="cardinality6::A")
cardinality6_B = Class(name="cardinality6::B")

# cardinality6_Root class attributes and methods

# cardinality6_A class attributes and methods

# cardinality6_B class attributes and methods

# Relationships
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="cardinality6_A", type=cardinality6_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="cardinality6_Root", type=cardinality6_A, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="cardinality6_B", type=cardinality6_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="cardinality6_Root2", type=cardinality6_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="cardinality6",
    types={cardinality6_Root, cardinality6_A, cardinality6_B},
    associations={as0, bs1},
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