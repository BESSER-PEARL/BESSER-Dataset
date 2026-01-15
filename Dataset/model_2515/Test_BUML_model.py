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

# Enumerations
EEnum0: Enumeration = Enumeration(
    name="EEnum0",
    literals={
            EnumerationLiteral(name="a"),
			EnumerationLiteral(name="b")
    }
)

# Classes
test_EClass2 = Class(name="test::EClass2")
test_EClass0 = Class(name="test::EClass0")
test_EClass1 = Class(name="test::EClass1")

# test_EClass2 class attributes and methods
test_EClass2_EAttribute0: Property = Property(name="EAttribute0", type=BooleanType)
test_EClass2_EAttribute1: Property = Property(name="EAttribute1", type=IntegerType)
test_EClass2.attributes={test_EClass2_EAttribute1, test_EClass2_EAttribute0}

# test_EClass0 class attributes and methods
test_EClass0_attr0: Property = Property(name="attr0", type=StringType)
test_EClass0_attr1: Property = Property(name="attr1", type=BooleanType)
test_EClass0.attributes={test_EClass0_attr0, test_EClass0_attr1}

# test_EClass1 class attributes and methods
test_EClass1_EAttribute0: Property = Property(name="EAttribute0", type=StringType)
test_EClass1.attributes={test_EClass1_EAttribute0}

# Relationships
EReference00: BinaryAssociation = BinaryAssociation(
    name="EReference00",
    ends={
        Property(name="test_EClass0", type=test_EClass1, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="test_EClass1", type=test_EClass0, multiplicity=Multiplicity(1, 1))
    }
)
EReference11: BinaryAssociation = BinaryAssociation(
    name="EReference11",
    ends={
        Property(name="test_EClass2", type=test_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="test_EClass02", type=test_EClass2, multiplicity=Multiplicity(0, 8), is_composite=True)
    }
)
EReference03: BinaryAssociation = BinaryAssociation(
    name="EReference03",
    ends={
        Property(name="test_EClass25", type=test_EClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="test_EClass14", type=test_EClass2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_EClass2, test_EClass0, test_EClass1, EEnum0},
    associations={EReference00, EReference11, EReference03},
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