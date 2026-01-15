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
test_Person = Class(name="test::Person")

# test_Person class attributes and methods
test_Person_age: Property = Property(name="age", type=IntegerType)
test_Person_m_isAgeValid: Method = Method(name="isAgeValid", parameters={Parameter(name='map'), Parameter(name='diag')}, type=BooleanType)
test_Person.attributes={test_Person_age}
test_Person.methods={test_Person_m_isAgeValid}

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Person},
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