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
MyEnum: Enumeration = Enumeration(
    name="MyEnum",
    literals={
            EnumerationLiteral(name="X"),
			EnumerationLiteral(name="Y")
    }
)

# Classes
test_MyMetaClass = Class(name="test::MyMetaClass")
SubpackageMetaClass = Class(name="SubpackageMetaClass")
test_subpackage_SubpackageMetaClass = Class(name="test::subpackage::SubpackageMetaClass")

# test_MyMetaClass class attributes and methods
test_MyMetaClass_name: Property = Property(name="name", type=StringType)
test_MyMetaClass_enumAttr: Property = Property(name="enumAttr", type=StringType)
test_MyMetaClass.attributes={test_MyMetaClass_enumAttr, test_MyMetaClass_name}

# SubpackageMetaClass class attributes and methods

# test_subpackage_SubpackageMetaClass class attributes and methods
test_subpackage_SubpackageMetaClass_name: Property = Property(name="name", type=StringType)
test_subpackage_SubpackageMetaClass.attributes={test_subpackage_SubpackageMetaClass_name}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="test_MyMetaClass", type=test_MyMetaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="test_MyMetaClass0", type=test_MyMetaClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackageRef2: BinaryAssociation = BinaryAssociation(
    name="subPackageRef2",
    ends={
        Property(name="SubpackageMetaClass", type=test_MyMetaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="test_MyMetaClass3", type=SubpackageMetaClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_MyMetaClass, SubpackageMetaClass, test_subpackage_SubpackageMetaClass, MyEnum},
    associations={children1, subPackageRef2},
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