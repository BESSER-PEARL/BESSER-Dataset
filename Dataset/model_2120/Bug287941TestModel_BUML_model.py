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
bug287941TestModel_Test = Class(name="bug287941TestModel::Test")
bug287941TestModel_Test2 = Class(name="bug287941TestModel::Test2")

# bug287941TestModel_Test class attributes and methods
bug287941TestModel_Test_testAttr: Property = Property(name="testAttr", type=StringType)
bug287941TestModel_Test.attributes={bug287941TestModel_Test_testAttr}

# bug287941TestModel_Test2 class attributes and methods

# Relationships
testRef0: BinaryAssociation = BinaryAssociation(
    name="testRef0",
    ends={
        Property(name="bug287941TestModel_Test2", type=bug287941TestModel_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="bug287941TestModel_Test", type=bug287941TestModel_Test2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bug287941TestModel",
    types={bug287941TestModel_Test, bug287941TestModel_Test2},
    associations={testRef0},
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