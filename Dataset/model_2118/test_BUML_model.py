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
test_Tests = Class(name="test::Tests", is_abstract=True)
test_AbstractTest = Class(name="test::AbstractTest", is_abstract=True)

# test_Tests class attributes and methods
test_Tests_name: Property = Property(name="name", type=StringType)
test_Tests.attributes={test_Tests_name}

# test_AbstractTest class attributes and methods
test_AbstractTest_text: Property = Property(name="text", type=StringType)
test_AbstractTest.attributes={test_AbstractTest_text}

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Tests, test_AbstractTest},
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