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
testSubpackages1_root_class1 = Class(name="testSubpackages1::root::class1")
class3 = Class(name="class3")
testSubpackages1_root_testSubpackages1_subpackage1_class2 = Class(name="testSubpackages1::root::testSubpackages1::subpackage1::class2")
testSubpackages1_root_testSubpackages1_subpackage3_class4 = Class(name="testSubpackages1::root::testSubpackages1::subpackage3::class4")
testSubpackages1_root_testSubpackages1_subpackage2_class3 = Class(name="testSubpackages1::root::testSubpackages1::subpackage2::class3")

# testSubpackages1_root_class1 class attributes and methods
testSubpackages1_root_class1_a: Property = Property(name="a", type=DateType)
testSubpackages1_root_class1.attributes={testSubpackages1_root_class1_a}

# class3 class attributes and methods

# testSubpackages1_root_testSubpackages1_subpackage1_class2 class attributes and methods

# testSubpackages1_root_testSubpackages1_subpackage3_class4 class attributes and methods

# testSubpackages1_root_testSubpackages1_subpackage2_class3 class attributes and methods

# Relationships
ref_class30: BinaryAssociation = BinaryAssociation(
    name="ref_class30",
    ends={
        Property(name="class3", type=testSubpackages1_root_class1, multiplicity=Multiplicity(1, 1)),
        Property(name="testSubpackages1_root_class1", type=class3, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testSubpackages1_root",
    types={testSubpackages1_root_class1, class3, testSubpackages1_root_testSubpackages1_subpackage1_class2, testSubpackages1_root_testSubpackages1_subpackage3_class4, testSubpackages1_root_testSubpackages1_subpackage2_class3},
    associations={ref_class30},
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