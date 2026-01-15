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
test_EClass0 = Class(name="test::EClass0")
test_EClass1 = Class(name="test::EClass1")

# test_EClass0 class attributes and methods
test_EClass0_EAttribute0: Property = Property(name="EAttribute0", type=BooleanType)
test_EClass0.attributes={test_EClass0_EAttribute0}

# test_EClass1 class attributes and methods

# Relationships
EReference00: BinaryAssociation = BinaryAssociation(
    name="EReference00",
    ends={
        Property(name="test_EClass1", type=test_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="test_EClass0", type=test_EClass1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_EClass0, test_EClass1},
    associations={EReference00},
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