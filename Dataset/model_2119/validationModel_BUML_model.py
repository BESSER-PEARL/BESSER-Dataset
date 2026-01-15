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
ValidationModel_UnitTest = Class(name="ValidationModel::UnitTest")
ValidationModel_TestContainer = Class(name="ValidationModel::TestContainer")

# ValidationModel_UnitTest class attributes and methods
ValidationModel_UnitTest_name: Property = Property(name="name", type=StringType)
ValidationModel_UnitTest_id: Property = Property(name="id", type=StringType)
ValidationModel_UnitTest_isTested: Property = Property(name="isTested", type=BooleanType)
ValidationModel_UnitTest.attributes={ValidationModel_UnitTest_name, ValidationModel_UnitTest_id, ValidationModel_UnitTest_isTested}

# ValidationModel_TestContainer class attributes and methods

# Relationships
tests0: BinaryAssociation = BinaryAssociation(
    name="tests0",
    ends={
        Property(name="ValidationModel_UnitTest", type=ValidationModel_TestContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ValidationModel_TestContainer", type=ValidationModel_UnitTest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ValidationModel",
    types={ValidationModel_UnitTest, ValidationModel_TestContainer},
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