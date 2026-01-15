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
testPackage_FirstClass = Class(name="testPackage::FirstClass")
testPackage_SecondClass = Class(name="testPackage::SecondClass")

# testPackage_FirstClass class attributes and methods

# testPackage_SecondClass class attributes and methods

# Relationships
testReference0: BinaryAssociation = BinaryAssociation(
    name="testReference0",
    ends={
        Property(name="ObligatoryContainerRelation.ecoreSecondClass", type=testPackage_FirstClass, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingReference", type=testPackage_SecondClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencingReference1: BinaryAssociation = BinaryAssociation(
    name="referencingReference1",
    ends={
        Property(name="ObligatoryContainerRelation.ecoreFirstClass", type=testPackage_SecondClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testReference", type=testPackage_FirstClass, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_FirstClass, testPackage_SecondClass},
    associations={testReference0, referencingReference1},
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