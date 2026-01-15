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
test1unique_ConceptA = Class(name="test1unique::ConceptA")

# test1unique_ConceptA class attributes and methods
test1unique_ConceptA_bs: Property = Property(name="bs", type=StringType)
test1unique_ConceptA.attributes={test1unique_ConceptA_bs}

# Domain Model
domain_model = DomainModel(
    name="test1unique",
    types={test1unique_ConceptA},
    associations={},
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