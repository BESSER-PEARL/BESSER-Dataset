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
test_containmentwalker_dependency_Foo = Class(name="test::containmentwalker::dependency::Foo")
ClassInOtherPackage = Class(name="ClassInOtherPackage")
test_containmentwalker_dependency_IsolatedClassInReachablePackage = Class(name="test::containmentwalker::dependency::IsolatedClassInReachablePackage")
test_containmentwalker_dependency_subpackage_ClassInOtherPackage = Class(name="test::containmentwalker::dependency::subpackage::ClassInOtherPackage")

# test_containmentwalker_dependency_Foo class attributes and methods

# ClassInOtherPackage class attributes and methods

# test_containmentwalker_dependency_IsolatedClassInReachablePackage class attributes and methods

# test_containmentwalker_dependency_subpackage_ClassInOtherPackage class attributes and methods

# Relationships
classinotherpackage0: BinaryAssociation = BinaryAssociation(
    name="classinotherpackage0",
    ends={
        Property(name="ClassInOtherPackage", type=test_containmentwalker_dependency_Foo, multiplicity=Multiplicity(1, 1)),
        Property(name="test_containmentwalker_dependency_Foo", type=ClassInOtherPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test_containmentwalker_dependency",
    types={test_containmentwalker_dependency_Foo, ClassInOtherPackage, test_containmentwalker_dependency_IsolatedClassInReachablePackage, test_containmentwalker_dependency_subpackage_ClassInOtherPackage},
    associations={classinotherpackage0},
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