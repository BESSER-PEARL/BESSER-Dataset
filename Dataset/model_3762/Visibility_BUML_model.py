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
fsm_Transition_k: Property = Property(name="k", type=IntegerType)
fsm_Transition_m_f1: Method = Method(name="f1", parameters={})
fsm_Transition_m_f2: Method = Method(name="f2", parameters={})
fsm_Transition.attributes={fsm_Transition_k}
fsm_Transition.methods={fsm_Transition_m_f1, fsm_Transition_m_f2}

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