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
abc_A = Class(name="abc::A")
abc_B = Class(name="abc::B")
A = Class(name="A")
abc_C = Class(name="abc::C")

# abc_A class attributes and methods

# abc_B class attributes and methods

# A class attributes and methods

# abc_C class attributes and methods

# Generalizations
gen_abc_B_A = Generalization(general=A, specific=abc_B)

# Domain Model
domain_model = DomainModel(
    name="abc",
    types={abc_A, abc_B, A, abc_C},
    associations={},
    generalizations={gen_abc_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)