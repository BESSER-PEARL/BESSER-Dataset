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
package_subpackage_A = Class(name="package::subpackage::A")
package_subpackage_B = Class(name="package::subpackage::B")
package_subpackage_C = Class(name="package::subpackage::C")
A = Class(name="A")

# package_subpackage_A class attributes and methods

# package_subpackage_B class attributes and methods

# package_subpackage_C class attributes and methods

# A class attributes and methods

# Generalizations
gen_package_subpackage_C_A = Generalization(general=A, specific=package_subpackage_C)

# Domain Model
domain_model = DomainModel(
    name="package",
    types={package_subpackage_A, package_subpackage_B, package_subpackage_C, A},
    associations={},
    generalizations={gen_package_subpackage_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)