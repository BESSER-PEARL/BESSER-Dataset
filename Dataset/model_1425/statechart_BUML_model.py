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
statechart_ModelElement = Class(name="statechart::ModelElement", is_abstract=True)
statechart_Transition = Class(name="statechart::Transition")
ModelElement = Class(name="ModelElement")
statechart_Action = Class(name="statechart::Action")
statechart_CompositeState = Class(name="statechart::CompositeState")
AbstractState = Class(name="AbstractState")
statechart_AbstractState = Class(name="statechart::AbstractState", is_abstract=True)
statechart_StateMachine = Class(name="statechart::StateMachine")
statechart_InitialState = Class(name="statechart::InitialState")
statechart_SimpleState = Class(name="statechart::SimpleState")
statechart_FinalState = Class(name="statechart::FinalState")

# statechart_ModelElement class attributes and methods
statechart_ModelElement_name: Property = Property(name="name", type=StringType)
statechart_ModelElement.attributes={statechart_ModelElement_name}

# statechart_Transition class attributes and methods
statechart_Transition_event: Property = Property(name="event", type=StringType)
statechart_Transition_guard: Property = Property(name="guard", type=StringType)
statechart_Transition.attributes={statechart_Transition_event, statechart_Transition_guard}

# ModelElement class attributes and methods

# statechart_Action class attributes and methods
statechart_Action_kind: Property = Property(name="kind", type=StringType)
statechart_Action.attributes={statechart_Action_kind}

# statechart_CompositeState class attributes and methods

# AbstractState class attributes and methods

# statechart_AbstractState class attributes and methods

# statechart_StateMachine class attributes and methods

# statechart_InitialState class attributes and methods

# statechart_SimpleState class attributes and methods

# statechart_FinalState class attributes and methods

# Relationships
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="from", type=statechart_Transition, multiplicity=Multiplicity(0, 9999)),
        Property(name="Transition5", type=statechart_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="statechart_Action", type=statechart_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_AbstractState", type=statechart_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="statechart_AbstractState8", type=statechart_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_CompositeState", type=statechart_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from0: BinaryAssociation = BinaryAssociation(
    name="from0",
    ends={
        Property(name="AbstractState", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statechart_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="AbstractState2", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statechart_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=statechart_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=statechart_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="statechart_Transition", type=statechart_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_CompositeState10", type=statechart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="statechart_CompositeState12", type=statechart_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_StateMachine", type=statechart_CompositeState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statechart_Transition_ModelElement = Generalization(general=ModelElement, specific=statechart_Transition)
gen_statechart_CompositeState_AbstractState = Generalization(general=AbstractState, specific=statechart_CompositeState)
gen_statechart_AbstractState_ModelElement = Generalization(general=ModelElement, specific=statechart_AbstractState)
gen_statechart_InitialState_AbstractState = Generalization(general=AbstractState, specific=statechart_InitialState)
gen_statechart_SimpleState_AbstractState = Generalization(general=AbstractState, specific=statechart_SimpleState)
gen_statechart_FinalState_AbstractState = Generalization(general=AbstractState, specific=statechart_FinalState)

# Domain Model
domain_model = DomainModel(
    name="statechart",
    types={statechart_ModelElement, statechart_Transition, ModelElement, statechart_Action, statechart_CompositeState, AbstractState, statechart_AbstractState, statechart_StateMachine, statechart_InitialState, statechart_SimpleState, statechart_FinalState, ActionKind},
    associations={outgoing4, actions6, states7, from0, to1, incoming3, transitions9, state11},
    generalizations={gen_statechart_Transition_ModelElement, gen_statechart_CompositeState_AbstractState, gen_statechart_AbstractState_ModelElement, gen_statechart_InitialState_AbstractState, gen_statechart_SimpleState_AbstractState, gen_statechart_FinalState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)