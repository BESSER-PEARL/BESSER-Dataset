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
fsm_Transition = Class(name="fsm::Transition")

# fsm_Transition class attributes and methods
fsm_Transition_ls: Property = Property(name="ls", type=StringType)
fsm_Transition_als: Property = Property(name="als", type=StringType)
fsm_Transition.attributes={fsm_Transition_ls, fsm_Transition_als}

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition},
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