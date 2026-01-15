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
stateMachineEditRules_Transition = Class(name="stateMachineEditRules::Transition")
stateMachineEditRules_State = Class(name="stateMachineEditRules::State")
stateMachineEditRules_DFA = Class(name="stateMachineEditRules::DFA")

# stateMachineEditRules_Transition class attributes and methods
stateMachineEditRules_Transition_input: Property = Property(name="input", type=StringType)
stateMachineEditRules_Transition.attributes={stateMachineEditRules_Transition_input}

# stateMachineEditRules_State class attributes and methods
stateMachineEditRules_State_isStart: Property = Property(name="isStart", type=BooleanType)
stateMachineEditRules_State_isEnd: Property = Property(name="isEnd", type=BooleanType)
stateMachineEditRules_State_id: Property = Property(name="id", type=StringType)
stateMachineEditRules_State.attributes={stateMachineEditRules_State_id, stateMachineEditRules_State_isEnd, stateMachineEditRules_State_isStart}

# stateMachineEditRules_DFA class attributes and methods

# Relationships
to0: BinaryAssociation = BinaryAssociation(
    name="to0",
    ends={
        Property(name="State", type=stateMachineEditRules_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=stateMachineEditRules_State, multiplicity=Multiplicity(1, 1))
    }
)
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="outgoingTransitions", type=stateMachineEditRules_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State2", type=stateMachineEditRules_Transition, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions4: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions4",
    ends={
        Property(name="Transition5", type=stateMachineEditRules_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=stateMachineEditRules_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions3: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions3",
    ends={
        Property(name="Transition", type=stateMachineEditRules_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=stateMachineEditRules_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="stateMachineEditRules_State", type=stateMachineEditRules_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineEditRules_DFA", type=stateMachineEditRules_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions7: BinaryAssociation = BinaryAssociation(
    name="transitions7",
    ends={
        Property(name="stateMachineEditRules_Transition", type=stateMachineEditRules_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineEditRules_DFA8", type=stateMachineEditRules_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateMachineEditRules",
    types={stateMachineEditRules_Transition, stateMachineEditRules_State, stateMachineEditRules_DFA},
    associations={to0, from1, outgoingTransitions4, incomingTransitions3, states6, transitions7},
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