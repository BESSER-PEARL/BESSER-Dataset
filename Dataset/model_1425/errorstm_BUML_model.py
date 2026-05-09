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

# Enumerations
ActionKind: Enumeration = Enumeration(
    name="ActionKind",
    literals={
            EnumerationLiteral(name="ENTRY"),
			EnumerationLiteral(name="EXIT")
    }
)

# Classes
errorstm_StateMachine = Class(name="errorstm_StateMachine")
errorstm_Transition = Class(name="errorstm_Transition")
errorstm_AbstractState = Class(name="errorstm_AbstractState", is_abstract=True)
errorstm_Action = Class(name="errorstm_Action")
errorstm_CompositeState = Class(name="errorstm_CompositeState")
AbstractState = Class(name="AbstractState")
errorstm_InitialState = Class(name="errorstm_InitialState")
errorstm_SimpleState = Class(name="errorstm_SimpleState")
errorstm_FinalState = Class(name="errorstm_FinalState")

# errorstm_StateMachine class attributes and methods

# errorstm_Transition class attributes and methods
errorstm_Transition_event: Property = Property(name="event", type=StringType)
errorstm_Transition_guard: Property = Property(name="guard", type=StringType)
errorstm_Transition_name: Property = Property(name="name", type=StringType)
errorstm_Transition.attributes={errorstm_Transition_name, errorstm_Transition_guard, errorstm_Transition_event}

# errorstm_AbstractState class attributes and methods
errorstm_AbstractState_name: Property = Property(name="name", type=StringType)
errorstm_AbstractState.attributes={errorstm_AbstractState_name}

# errorstm_Action class attributes and methods
errorstm_Action_kind: Property = Property(name="kind", type=StringType)
errorstm_Action.attributes={errorstm_Action_kind}

# errorstm_CompositeState class attributes and methods

# AbstractState class attributes and methods

# errorstm_InitialState class attributes and methods

# errorstm_SimpleState class attributes and methods

# errorstm_FinalState class attributes and methods

# Relationships
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="errorstm_Transition", type=errorstm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="errorstm_CompositeState10", type=errorstm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="errorstm_CompositeState12", type=errorstm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="errorstm_StateMachine", type=errorstm_CompositeState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from_0: BinaryAssociation = BinaryAssociation(
    name="from_0",
    ends={
        Property(name="AbstractState", type=errorstm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=errorstm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="AbstractState2", type=errorstm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=errorstm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=errorstm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=errorstm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=errorstm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=errorstm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="errorstm_Action", type=errorstm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="errorstm_AbstractState", type=errorstm_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="errorstm_AbstractState8", type=errorstm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="errorstm_CompositeState", type=errorstm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_errorstm_CompositeState_AbstractState = Generalization(general=AbstractState, specific=errorstm_CompositeState)
gen_errorstm_InitialState_AbstractState = Generalization(general=AbstractState, specific=errorstm_InitialState)
gen_errorstm_SimpleState_AbstractState = Generalization(general=AbstractState, specific=errorstm_SimpleState)
gen_errorstm_FinalState_AbstractState = Generalization(general=AbstractState, specific=errorstm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="errorstm",
    types={errorstm_StateMachine, errorstm_Transition, errorstm_AbstractState, errorstm_Action, errorstm_CompositeState, AbstractState, errorstm_InitialState, errorstm_SimpleState, errorstm_FinalState, ActionKind},
    associations={transitions9, state11, from_0, to1, incoming3, outgoing4, actions6, states7},
    generalizations={gen_errorstm_CompositeState_AbstractState, gen_errorstm_InitialState_AbstractState, gen_errorstm_SimpleState_AbstractState, gen_errorstm_FinalState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)