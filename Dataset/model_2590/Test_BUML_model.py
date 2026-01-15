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
root_A = Class(name="root::A")
root_subpackage1_B = Class(name="root::subpackage1::B")
root_subsubpackage1_D = Class(name="root::subsubpackage1::D")
root_subpackage2_C = Class(name="root::subpackage2::C")

# root_A class attributes and methods

# root_subpackage1_B class attributes and methods

# root_subsubpackage1_D class attributes and methods

# root_subpackage2_C class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_A, root_subpackage1_B, root_subsubpackage1_D, root_subpackage2_C},
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