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
root_container_border_node_1 = Class(name="root::container::border::node::1")
root_container_border_node_2 = Class(name="root::container::border::node::2")
root_container_border_node_3 = Class(name="root::container::border::node::3")

# root_container_border_node_1 class attributes and methods

# root_container_border_node_2 class attributes and methods

# root_container_border_node_3 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_container_border_node_1, root_container_border_node_2, root_container_border_node_3},
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