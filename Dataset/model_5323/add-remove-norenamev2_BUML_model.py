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
testPackage_ExistsInBoth = Class(name="testPackage::ExistsInBoth")
testPackage_sub_OnlyInWorkingCopy = Class(name="testPackage::sub::OnlyInWorkingCopy")

# testPackage_ExistsInBoth class attributes and methods

# testPackage_sub_OnlyInWorkingCopy class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_ExistsInBoth, testPackage_sub_OnlyInWorkingCopy},
    associations={},
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