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
testSubpackages1_subpackage3_class4 = Class(name="testSubpackages1::subpackage3::class4")
testSubpackages2_root_class2 = Class(name="testSubpackages2::root::class2")

# testSubpackages1_subpackage3_class4 class attributes and methods

# testSubpackages2_root_class2 class attributes and methods

# Relationships
refClass40: BinaryAssociation = BinaryAssociation(
    name="refClass40",
    ends={
        Property(name="testSubpackages1_subpackage3_class4", type=testSubpackages2_root_class2, multiplicity=Multiplicity(1, 1)),
        Property(name="testSubpackages2_root_class2", type=testSubpackages1_subpackage3_class4, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testSubpackages2_root",
    types={testSubpackages1_subpackage3_class4, testSubpackages2_root_class2},
    associations={refClass40},
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