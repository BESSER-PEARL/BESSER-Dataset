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
fsa_Transition = Class(name="fsa::Transition")
fsa_FSA = Class(name="fsa::FSA")
fsa_State = Class(name="fsa::State")

# fsa_Transition class attributes and methods
fsa_Transition_event: Property = Property(name="event", type=StringType)
fsa_Transition.attributes={fsa_Transition_event}

# fsa_FSA class attributes and methods

# fsa_State class attributes and methods
fsa_State_name: Property = Property(name="name", type=StringType)
fsa_State_accepting: Property = Property(name="accepting", type=BooleanType)
fsa_State.attributes={fsa_State_accepting, fsa_State_name}

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="fsa_Transition", type=fsa_FSA, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_FSA2", type=fsa_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="fsa_State5", type=fsa_FSA, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_FSA4", type=fsa_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions6",
    ends={
        Property(name="Transition", type=fsa_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fromState", type=fsa_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsa_State", type=fsa_FSA, multiplicity=Multiplicity(1, 1)),
        Property(name="fsa_FSA", type=fsa_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions7: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions7",
    ends={
        Property(name="Transition8", type=fsa_State, multiplicity=Multiplicity(1, 1)),
        Property(name="toState", type=fsa_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fromState9: BinaryAssociation = BinaryAssociation(
    name="fromState9",
    ends={
        Property(name="State", type=fsa_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=fsa_State, multiplicity=Multiplicity(1, 1))
    }
)
toState10: BinaryAssociation = BinaryAssociation(
    name="toState10",
    ends={
        Property(name="State11", type=fsa_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=fsa_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsa",
    types={fsa_Transition, fsa_FSA, fsa_State},
    associations={transitions1, initialState3, outgoingTransitions6, states0, incomingTransitions7, fromState9, toState10},
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