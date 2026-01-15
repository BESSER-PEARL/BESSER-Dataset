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
B = Class(name="B")
root_B = Class(name="root::B", is_abstract=True)
root_A2 = Class(name="root::A2")

# root_A class attributes and methods

# B class attributes and methods

# root_B class attributes and methods

# root_A2 class attributes and methods

# Generalizations
gen_root_A_B = Generalization(general=B, specific=root_A)
gen_root_A2_B = Generalization(general=B, specific=root_A2)

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_A, B, root_B, root_A2},
    associations={},
    generalizations={gen_root_A_B, gen_root_A2_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)