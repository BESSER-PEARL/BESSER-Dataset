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
test_A = Class(name="test::A")
test_B = Class(name="test::B")
test_C = Class(name="test::C")
test_D = Class(name="test::D")
test_EClassToEStringMap = Class(name="test::EClassToEStringMap")
test_EClassToAMap = Class(name="test::EClassToAMap")
test_EClass = Class(name="test::EClass")

# test_A class attributes and methods

# test_B class attributes and methods

# test_C class attributes and methods

# test_D class attributes and methods
test_D_x: Property = Property(name="x", type=StringType)
test_D_yList: Property = Property(name="yList", type=IntegerType)
test_D.attributes={test_D_yList, test_D_x}

# test_EClassToEStringMap class attributes and methods
test_EClassToEStringMap_value: Property = Property(name="value", type=StringType)
test_EClassToEStringMap.attributes={test_EClassToEStringMap_value}

# test_EClassToAMap class attributes and methods

# test_EClass class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="test_B", type=test_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test_A", type=test_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="test_C", type=test_B, multiplicity=Multiplicity(1, 1)),
        Property(name="test_B2", type=test_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cList3: BinaryAssociation = BinaryAssociation(
    name="cList3",
    ends={
        Property(name="test_C5", type=test_B, multiplicity=Multiplicity(1, 1)),
        Property(name="test_B4", type=test_C, multiplicity=Multiplicity(0, 9999))
    }
)
d6: BinaryAssociation = BinaryAssociation(
    name="d6",
    ends={
        Property(name="test_D", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C7", type=test_D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eClassToString8: BinaryAssociation = BinaryAssociation(
    name="eClassToString8",
    ends={
        Property(name="test_EClassToEStringMap", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C9", type=test_EClassToEStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eClassToA10: BinaryAssociation = BinaryAssociation(
    name="eClassToA10",
    ends={
        Property(name="test_EClassToAMap", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C11", type=test_EClassToAMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key15: BinaryAssociation = BinaryAssociation(
    name="key15",
    ends={
        Property(name="test_EClass", type=test_EClassToEStringMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_EClassToEStringMap16", type=test_EClass, multiplicity=Multiplicity(0, 1))
    }
)
key17: BinaryAssociation = BinaryAssociation(
    name="key17",
    ends={
        Property(name="test_EClass19", type=test_EClassToAMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_EClassToAMap18", type=test_EClass, multiplicity=Multiplicity(0, 1))
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="test_A22", type=test_EClassToAMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_EClassToAMap21", type=test_A, multiplicity=Multiplicity(0, 1))
    }
)
a12: BinaryAssociation = BinaryAssociation(
    name="a12",
    ends={
        Property(name="test_A14", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C13", type=test_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_A, test_B, test_C, test_D, test_EClassToEStringMap, test_EClassToAMap, test_EClass},
    associations={b0, c1, cList3, d6, eClassToString8, eClassToA10, key15, key17, value20, a12},
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