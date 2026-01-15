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
TimeConstraintType: Enumeration = Enumeration(
    name="TimeConstraintType",
    literals={
            EnumerationLiteral(name="START"),
			EnumerationLiteral(name="STOP"),
			EnumerationLiteral(name="CHECK")
    }
)

NumericCompareOperator: Enumeration = Enumeration(
    name="NumericCompareOperator",
    literals={
            EnumerationLiteral(name="MORE_THAN"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="LESS_OR_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="MORE_OR_EQUALS")
    }
)

EventProcessingContext: Enumeration = Enumeration(
    name="EventProcessingContext",
    literals={
            EnumerationLiteral(name="STRICT_IMMEDIATE"),
			EnumerationLiteral(name="CHRONICLE"),
			EnumerationLiteral(name="RECENT"),
			EnumerationLiteral(name="UNRESTRICTED"),
			EnumerationLiteral(name="IMMEDIATE")
    }
)

# Classes
internalsm_State = Class(name="internalsm::State")
internalsm_EventToken = Class(name="internalsm::EventToken")
internalsm_Transition = Class(name="internalsm::Transition")
internalsm_TimeConstraint = Class(name="internalsm::TimeConstraint")
internalsm_Event = Class(name="internalsm::Event")
internalsm_Guard = Class(name="internalsm::Guard")
internalsm_TrapState = Class(name="internalsm::TrapState")
internalsm_AtomicEventPattern = Class(name="internalsm::AtomicEventPattern")
internalsm_FinalState = Class(name="internalsm::FinalState")
State = Class(name="State")
internalsm_InitState = Class(name="internalsm::InitState")
internalsm_StateMachine = Class(name="internalsm::StateMachine")
internalsm_EventPattern = Class(name="internalsm::EventPattern")
internalsm_InternalExecutionModel = Class(name="internalsm::InternalExecutionModel")
internalsm_TimeConstraintSpecification = Class(name="internalsm::TimeConstraintSpecification")

# internalsm_State class attributes and methods
internalsm_State_label: Property = Property(name="label", type=StringType)
internalsm_State.attributes={internalsm_State_label}

# internalsm_EventToken class attributes and methods

# internalsm_Transition class attributes and methods

# internalsm_TimeConstraint class attributes and methods
internalsm_TimeConstraint_type: Property = Property(name="type", type=StringType)
internalsm_TimeConstraint.attributes={internalsm_TimeConstraint_type}

# internalsm_Event class attributes and methods

# internalsm_Guard class attributes and methods

# internalsm_TrapState class attributes and methods

# internalsm_AtomicEventPattern class attributes and methods

# internalsm_FinalState class attributes and methods

# State class attributes and methods

# internalsm_InitState class attributes and methods

# internalsm_StateMachine class attributes and methods
internalsm_StateMachine_priority: Property = Property(name="priority", type=IntegerType)
internalsm_StateMachine_context: Property = Property(name="context", type=StringType)
internalsm_StateMachine.attributes={internalsm_StateMachine_context, internalsm_StateMachine_priority}

# internalsm_EventPattern class attributes and methods

# internalsm_InternalExecutionModel class attributes and methods
internalsm_InternalExecutionModel_context: Property = Property(name="context", type=StringType)
internalsm_InternalExecutionModel.attributes={internalsm_InternalExecutionModel_context}

# internalsm_TimeConstraintSpecification class attributes and methods
internalsm_TimeConstraintSpecification_id: Property = Property(name="id", type=StringType)
internalsm_TimeConstraintSpecification_expectedLength: Property = Property(name="expectedLength", type=StringType)
internalsm_TimeConstraintSpecification_startTimestamp: Property = Property(name="startTimestamp", type=StringType)
internalsm_TimeConstraintSpecification_stopTimestamp: Property = Property(name="stopTimestamp", type=StringType)
internalsm_TimeConstraintSpecification_m_handleTimeConstraint: Method = Method(name="handleTimeConstraint", parameters={})
internalsm_TimeConstraintSpecification.attributes={internalsm_TimeConstraintSpecification_expectedLength, internalsm_TimeConstraintSpecification_stopTimestamp, internalsm_TimeConstraintSpecification_startTimestamp, internalsm_TimeConstraintSpecification_id}
internalsm_TimeConstraintSpecification.methods={internalsm_TimeConstraintSpecification_m_handleTimeConstraint}

# Relationships
eventTokens3: BinaryAssociation = BinaryAssociation(
    name="eventTokens3",
    ends={
        Property(name="EventToken", type=internalsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="currentState", type=internalsm_EventToken, multiplicity=Multiplicity(0, 9999))
    }
)
outTransitions0: BinaryAssociation = BinaryAssociation(
    name="outTransitions0",
    ends={
        Property(name="Transition", type=internalsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="preState", type=internalsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inTransitions1: BinaryAssociation = BinaryAssociation(
    name="inTransitions1",
    ends={
        Property(name="Transition2", type=internalsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="postState", type=internalsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
guard8: BinaryAssociation = BinaryAssociation(
    name="guard8",
    ends={
        Property(name="internalsm_Guard", type=internalsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_Transition", type=internalsm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeConstraints4: BinaryAssociation = BinaryAssociation(
    name="timeConstraints4",
    ends={
        Property(name="internalsm_TimeConstraint", type=internalsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_State", type=internalsm_TimeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lastProcessedEvent5: BinaryAssociation = BinaryAssociation(
    name="lastProcessedEvent5",
    ends={
        Property(name="internalsm_Event", type=internalsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_State6", type=internalsm_Event, multiplicity=Multiplicity(0, 1))
    }
)
preState7: BinaryAssociation = BinaryAssociation(
    name="preState7",
    ends={
        Property(name="State", type=internalsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=internalsm_State, multiplicity=Multiplicity(1, 1))
    }
)
postState9: BinaryAssociation = BinaryAssociation(
    name="postState9",
    ends={
        Property(name="State10", type=internalsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=internalsm_State, multiplicity=Multiplicity(1, 1))
    }
)
eventType11: BinaryAssociation = BinaryAssociation(
    name="eventType11",
    ends={
        Property(name="internalsm_AtomicEventPattern", type=internalsm_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_Guard12", type=internalsm_AtomicEventPattern, multiplicity=Multiplicity(1, 1))
    }
)
stateMachines16: BinaryAssociation = BinaryAssociation(
    name="stateMachines16",
    ends={
        Property(name="internalsm_StateMachine17", type=internalsm_InternalExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_InternalExecutionModel", type=internalsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states13: BinaryAssociation = BinaryAssociation(
    name="states13",
    ends={
        Property(name="internalsm_State14", type=internalsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_StateMachine", type=internalsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventPattern15: BinaryAssociation = BinaryAssociation(
    name="eventPattern15",
    ends={
        Property(name="CEPMeta.ecoreEventPattern", type=internalsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=internalsm_EventPattern, multiplicity=Multiplicity(1, 1))
    }
)
latestEvent18: BinaryAssociation = BinaryAssociation(
    name="latestEvent18",
    ends={
        Property(name="internalsm_Event20", type=internalsm_InternalExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_InternalExecutionModel19", type=internalsm_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventTokens21: BinaryAssociation = BinaryAssociation(
    name="eventTokens21",
    ends={
        Property(name="internalsm_EventToken", type=internalsm_InternalExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_InternalExecutionModel22", type=internalsm_EventToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState23: BinaryAssociation = BinaryAssociation(
    name="currentState23",
    ends={
        Property(name="State24", type=internalsm_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTokens", type=internalsm_State, multiplicity=Multiplicity(0, 1))
    }
)
recordedEvents25: BinaryAssociation = BinaryAssociation(
    name="recordedEvents25",
    ends={
        Property(name="internalsm_Event27", type=internalsm_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_EventToken26", type=internalsm_Event, multiplicity=Multiplicity(0, 9999))
    }
)
timeConstraintSpecification28: BinaryAssociation = BinaryAssociation(
    name="timeConstraintSpecification28",
    ends={
        Property(name="internalsm_TimeConstraintSpecification", type=internalsm_TimeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="internalsm_TimeConstraint29", type=internalsm_TimeConstraintSpecification, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_internalsm_InitState_State = Generalization(general=State, specific=internalsm_InitState)
gen_internalsm_TrapState_State = Generalization(general=State, specific=internalsm_TrapState)
gen_internalsm_FinalState_State = Generalization(general=State, specific=internalsm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="internalsm",
    types={internalsm_State, internalsm_EventToken, internalsm_Transition, internalsm_TimeConstraint, internalsm_Event, internalsm_Guard, internalsm_TrapState, internalsm_AtomicEventPattern, internalsm_FinalState, State, internalsm_InitState, internalsm_StateMachine, internalsm_EventPattern, internalsm_InternalExecutionModel, internalsm_TimeConstraintSpecification, TimeConstraintType, NumericCompareOperator, EventProcessingContext},
    associations={eventTokens3, outTransitions0, inTransitions1, guard8, timeConstraints4, lastProcessedEvent5, preState7, postState9, eventType11, stateMachines16, states13, eventPattern15, latestEvent18, eventTokens21, currentState23, recordedEvents25, timeConstraintSpecification28},
    generalizations={gen_internalsm_InitState_State, gen_internalsm_TrapState_State, gen_internalsm_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)