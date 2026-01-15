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
essai_A = Class(name="essai::A")
Kind = Class(name="Kind")
essai_B = Class(name="essai::B")
Action = Class(name="Action")

# essai_A class attributes and methods

# Kind class attributes and methods

# essai_B class attributes and methods

# Action class attributes and methods

# Generalizations
gen_essai_A_Kind = Generalization(general=Kind, specific=essai_A)
gen_essai_B_Action = Generalization(general=Action, specific=essai_B)

# Domain Model
domain_model = DomainModel(
    name="essai",
    types={essai_A, Kind, essai_B, Action},
    associations={},
    generalizations={gen_essai_A_Kind, gen_essai_B_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)