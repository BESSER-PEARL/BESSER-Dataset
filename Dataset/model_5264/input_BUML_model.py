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
astrans_A = Class(name="astrans::A", is_abstract=True)
astrans_B = Class(name="astrans::B")
A = Class(name="A")
E = Class(name="E")

# astrans_A class attributes and methods

# astrans_B class attributes and methods

# A class attributes and methods

# E class attributes and methods

# Generalizations
gen_astrans_B_A = Generalization(general=A, specific=astrans_B)
gen_astrans_B_E = Generalization(general=E, specific=astrans_B)

# Domain Model
domain_model = DomainModel(
    name="astrans",
    types={astrans_A, astrans_B, A, E},
    associations={},
    generalizations={gen_astrans_B_A, gen_astrans_B_E},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)