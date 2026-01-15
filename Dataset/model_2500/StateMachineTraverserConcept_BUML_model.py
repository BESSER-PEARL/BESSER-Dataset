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
StateMachineTraverser_FSM = Class(name="StateMachineTraverser::FSM")
FSM = Class(name="FSM")
StateMachineTraverser_State = Class(name="StateMachineTraverser::State")
State = Class(name="State")

# StateMachineTraverser_FSM class attributes and methods
StateMachineTraverser_FSM_m_traverse: Method = Method(name="traverse", parameters={})
StateMachineTraverser_FSM_m_initials: Method = Method(name="initials", parameters={}, type=StringType)
StateMachineTraverser_FSM.methods={StateMachineTraverser_FSM_m_traverse, StateMachineTraverser_FSM_m_initials}

# FSM class attributes and methods

# StateMachineTraverser_State class attributes and methods
StateMachineTraverser_State_m_adjacent: Method = Method(name="adjacent", parameters={}, type=State)
StateMachineTraverser_State.methods={StateMachineTraverser_State_m_adjacent}

# State class attributes and methods

# Generalizations
gen_StateMachineTraverser_FSM_FSM = Generalization(general=FSM, specific=StateMachineTraverser_FSM)
gen_StateMachineTraverser_State_State = Generalization(general=State, specific=StateMachineTraverser_State)

# Domain Model
domain_model = DomainModel(
    name="StateMachineTraverser",
    types={StateMachineTraverser_FSM, FSM, StateMachineTraverser_State, State},
    associations={},
    generalizations={gen_StateMachineTraverser_FSM_FSM, gen_StateMachineTraverser_State_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)