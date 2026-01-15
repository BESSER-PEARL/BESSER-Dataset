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
use_registered_classes_A = Class(name="use::registered::classes::A")
use_registered_classes_B = Class(name="use::registered::classes::B")
use_registered_classes_C = Class(name="use::registered::classes::C")

# use_registered_classes_A class attributes and methods
use_registered_classes_A_x: Property = Property(name="x", type=IntegerType)
use_registered_classes_A_y: Property = Property(name="y", type=StringType)
use_registered_classes_A_z: Property = Property(name="z", type=StringType)
use_registered_classes_A.attributes={use_registered_classes_A_x, use_registered_classes_A_z, use_registered_classes_A_y}

# use_registered_classes_B class attributes and methods

# use_registered_classes_C class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="use_registered_classes",
    types={use_registered_classes_A, use_registered_classes_B, use_registered_classes_C},
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