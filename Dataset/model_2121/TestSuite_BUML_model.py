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
testSuite_Model = Class(name="testSuite::Model")
testSuite_Test = Class(name="testSuite::Test")

# testSuite_Model class attributes and methods

# testSuite_Test class attributes and methods
testSuite_Test_name: Property = Property(name="name", type=StringType)
testSuite_Test.attributes={testSuite_Test_name}

# Relationships
tests0: BinaryAssociation = BinaryAssociation(
    name="tests0",
    ends={
        Property(name="testSuite_Test", type=testSuite_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="testSuite_Model", type=testSuite_Test, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="testSuite",
    types={testSuite_Model, testSuite_Test},
    associations={tests0},
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