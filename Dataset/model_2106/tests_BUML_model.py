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
tests_TestsModel = Class(name="tests::TestsModel")
tests_Test = Class(name="tests::Test")

# tests_TestsModel class attributes and methods

# tests_Test class attributes and methods
tests_Test_id: Property = Property(name="id", type=StringType)
tests_Test_version: Property = Property(name="version", type=StringType)
tests_Test.attributes={tests_Test_version, tests_Test_id}

# Relationships
tests0: BinaryAssociation = BinaryAssociation(
    name="tests0",
    ends={
        Property(name="tests_Test", type=tests_TestsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestsModel", type=tests_Test, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="tests",
    types={tests_TestsModel, tests_Test},
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