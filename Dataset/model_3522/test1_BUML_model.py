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
test1_ConceptA = Class(name="test1::ConceptA")
test1_ConceptB = Class(name="test1::ConceptB")
ConceptA = Class(name="ConceptA")

# test1_ConceptA class attributes and methods

# test1_ConceptB class attributes and methods

# ConceptA class attributes and methods

# Generalizations
gen_test1_ConceptB_ConceptA = Generalization(general=ConceptA, specific=test1_ConceptB)

# Domain Model
domain_model = DomainModel(
    name="test1",
    types={test1_ConceptA, test1_ConceptB, ConceptA},
    associations={},
    generalizations={gen_test1_ConceptB_ConceptA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)