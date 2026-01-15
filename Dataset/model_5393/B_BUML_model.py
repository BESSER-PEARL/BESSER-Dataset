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
b_B = Class(name="b::B")
C = Class(name="C")

# b_B class attributes and methods
b_B_to_enum: Property = Property(name="to_enum", type=StringType)
b_B_custom_datatype: Property = Property(name="custom_datatype", type=StringType)
b_B.attributes={b_B_custom_datatype, b_B_to_enum}

# C class attributes and methods

# Generalizations
gen_b_B_C = Generalization(general=C, specific=b_B)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_B, C},
    associations={},
    generalizations={gen_b_B_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)