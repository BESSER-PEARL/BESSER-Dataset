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
root_subsub_E = Class(name="root_subsub_E")
root_subsub_F = Class(name="root_subsub_F", is_abstract=True)
root_sub2_E = Class(name="root_sub2_E")
root_A = Class(name="root_A")
root_B = Class(name="root_B")
root_sub_C = Class(name="root_sub_C", is_abstract=True)
root_sub_D = Class(name="root_sub_D")

# root_subsub_E class attributes and methods

# root_subsub_F class attributes and methods

# root_sub2_E class attributes and methods

# root_A class attributes and methods

# root_B class attributes and methods

# root_sub_C class attributes and methods

# root_sub_D class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_subsub_E, root_subsub_F, root_sub2_E, root_A, root_B, root_sub_C, root_sub_D},
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