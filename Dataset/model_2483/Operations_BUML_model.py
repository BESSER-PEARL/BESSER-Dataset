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
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_FSM class attributes and methods
fsm_FSM_m_i: Method = Method(name="i", parameters={Parameter(name='arg1')}, type=IntegerType)
fsm_FSM_m_j: Method = Method(name="j", parameters={Parameter(name='arg1'), Parameter(name='arg2')})
fsm_FSM_m_k: Method = Method(name="k", parameters={Parameter(name='arg1')}, type=StringType)
fsm_FSM.methods={fsm_FSM_m_i, fsm_FSM_m_j, fsm_FSM_m_k}

# fsm_State class attributes and methods

# fsm_Transition class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition},
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