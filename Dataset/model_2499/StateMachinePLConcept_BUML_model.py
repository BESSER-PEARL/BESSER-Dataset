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
statemachine_FSM = Class(name="statemachine::FSM")
statemachine_State = Class(name="statemachine::State")
statemachine_Transition = Class(name="statemachine::Transition")

# statemachine_FSM class attributes and methods
statemachine_FSM_m_states: Method = Method(name="states", parameters={}, type=StringType)
statemachine_FSM_m_transitions: Method = Method(name="transitions", parameters={}, type=StringType)
statemachine_FSM.methods={statemachine_FSM_m_states, statemachine_FSM_m_transitions}

# statemachine_State class attributes and methods

# statemachine_Transition class attributes and methods
statemachine_Transition_m_src: Method = Method(name="src", parameters={}, type=StringType)
statemachine_Transition_m_tar: Method = Method(name="tar", parameters={}, type=StringType)
statemachine_Transition.methods={statemachine_Transition_m_tar, statemachine_Transition_m_src}

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_FSM, statemachine_State, statemachine_Transition},
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