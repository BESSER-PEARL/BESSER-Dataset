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
testPackage_SuperClass = Class(name="testPackage::SuperClass")
testPackage_SubClass = Class(name="testPackage::SubClass")

# testPackage_SuperClass class attributes and methods

# testPackage_SubClass class attributes and methods

# Relationships
testReference0: BinaryAssociation = BinaryAssociation(
    name="testReference0",
    ends={
        Property(name="testPackage_SuperClass", type=testPackage_SubClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_SubClass", type=testPackage_SuperClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_SuperClass, testPackage_SubClass},
    associations={testReference0},
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