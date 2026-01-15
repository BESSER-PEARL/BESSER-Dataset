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
gemoc_FSM = Class(name="gemoc::FSM")
gemoc_State = Class(name="gemoc::State")
gemoc_Transition = Class(name="gemoc::Transition")

# gemoc_FSM class attributes and methods
gemoc_FSM_name: Property = Property(name="name", type=BooleanType)
gemoc_FSM_m_print: Method = Method(name="print", parameters={})
gemoc_FSM_m_initialize: Method = Method(name="initialize", parameters={})
gemoc_FSM_m_main: Method = Method(name="main", parameters={})
gemoc_FSM_m_setCurrentState: Method = Method(name="setCurrentState", parameters={Parameter(name='state')})
gemoc_FSM.attributes={gemoc_FSM_name}
gemoc_FSM.methods={gemoc_FSM_m_print, gemoc_FSM_m_initialize, gemoc_FSM_m_setCurrentState, gemoc_FSM_m_main}

# gemoc_State class attributes and methods
gemoc_State_name: Property = Property(name="name", type=StringType)
gemoc_State_m_step: Method = Method(name="step", parameters={Parameter(name='inputString')})
gemoc_State_m_isValidTrigger: Method = Method(name="isValidTrigger", parameters={Parameter(name='trigger')})
gemoc_State.attributes={gemoc_State_name}
gemoc_State.methods={gemoc_State_m_isValidTrigger, gemoc_State_m_step}

# gemoc_Transition class attributes and methods
gemoc_Transition_name: Property = Property(name="name", type=StringType)
gemoc_Transition_trigger: Property = Property(name="trigger", type=StringType)
gemoc_Transition_m_fire: Method = Method(name="fire", parameters={})
gemoc_Transition.attributes={gemoc_Transition_name, gemoc_Transition_trigger}
gemoc_Transition.methods={gemoc_Transition_m_fire}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="gemoc_State", type=gemoc_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="gemoc_FSM", type=gemoc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="gemoc_Transition", type=gemoc_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="gemoc_FSM2", type=gemoc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fSM8: BinaryAssociation = BinaryAssociation(
    name="fSM8",
    ends={
        Property(name="gemoc_FSM10", type=gemoc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="gemoc_State9", type=gemoc_FSM, multiplicity=Multiplicity(0, 1))
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="13", type=gemoc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=gemoc_State, multiplicity=Multiplicity(0, 1))
    }
)
src14: BinaryAssociation = BinaryAssociation(
    name="src14",
    ends={
        Property(name="16", type=gemoc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=gemoc_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="4", type=gemoc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=gemoc_Transition, multiplicity=Multiplicity(0, 1))
    }
)
outcoming5: BinaryAssociation = BinaryAssociation(
    name="outcoming5",
    ends={
        Property(name="7", type=gemoc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=gemoc_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="gemoc",
    types={gemoc_FSM, gemoc_State, gemoc_Transition},
    associations={state0, transition1, fSM8, state11, src14, incoming3, outcoming5},
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