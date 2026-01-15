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
MessageCheckerTypes: Enumeration = Enumeration(
    name="MessageCheckerTypes",
    literals={
            EnumerationLiteral(name="conditional"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="unconditional"),
			EnumerationLiteral(name="always")
    }
)

LanguageTypes: Enumeration = Enumeration(
    name="LanguageTypes",
    literals={
            EnumerationLiteral(name="java"),
			EnumerationLiteral(name="groovy"),
			EnumerationLiteral(name="relogo")
    }
)

PseudoStateTypes: Enumeration = Enumeration(
    name="PseudoStateTypes",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="entry"),
			EnumerationLiteral(name="choice")
    }
)

TriggerTypes: Enumeration = Enumeration(
    name="TriggerTypes",
    literals={
            EnumerationLiteral(name="always"),
			EnumerationLiteral(name="timed"),
			EnumerationLiteral(name="exponential"),
			EnumerationLiteral(name="probability"),
			EnumerationLiteral(name="condition"),
			EnumerationLiteral(name="message")
    }
)

# Classes
scmodel_AbstractState = Class(name="scmodel::AbstractState", is_abstract=True)
scmodel_Transition = Class(name="scmodel::Transition")
scmodel_StateMachine = Class(name="scmodel::StateMachine")
scmodel_State = Class(name="scmodel::State")
AbstractState = Class(name="AbstractState")
scmodel_FinalState = Class(name="scmodel::FinalState")
State = Class(name="State")
scmodel_CompositeState = Class(name="scmodel::CompositeState")
scmodel_PseudoState = Class(name="scmodel::PseudoState")
scmodel_History = Class(name="scmodel::History")

# scmodel_AbstractState class attributes and methods
scmodel_AbstractState_id: Property = Property(name="id", type=StringType)
scmodel_AbstractState_onEnter: Property = Property(name="onEnter", type=StringType)
scmodel_AbstractState_onExit: Property = Property(name="onExit", type=StringType)
scmodel_AbstractState_language: Property = Property(name="language", type=StringType)
scmodel_AbstractState_uuid: Property = Property(name="uuid", type=StringType)
scmodel_AbstractState_onEnterImports: Property = Property(name="onEnterImports", type=StringType)
scmodel_AbstractState_onExitImports: Property = Property(name="onExitImports", type=StringType)
scmodel_AbstractState.attributes={scmodel_AbstractState_uuid, scmodel_AbstractState_onExit, scmodel_AbstractState_onEnter, scmodel_AbstractState_onEnterImports, scmodel_AbstractState_onExitImports, scmodel_AbstractState_language, scmodel_AbstractState_id}

# scmodel_Transition class attributes and methods
scmodel_Transition_onTransitionImports: Property = Property(name="onTransitionImports", type=StringType)
scmodel_Transition_outOfBranch: Property = Property(name="outOfBranch", type=BooleanType)
scmodel_Transition_defaultTransition: Property = Property(name="defaultTransition", type=BooleanType)
scmodel_Transition_triggerType: Property = Property(name="triggerType", type=StringType)
scmodel_Transition_triggerTime: Property = Property(name="triggerTime", type=FloatType)
scmodel_Transition_triggerConditionCode: Property = Property(name="triggerConditionCode", type=StringType)
scmodel_Transition_triggerConditionCodeImports: Property = Property(name="triggerConditionCodeImports", type=StringType)
scmodel_Transition_triggerCodeLanguage: Property = Property(name="triggerCodeLanguage", type=StringType)
scmodel_Transition_messageCheckerType: Property = Property(name="messageCheckerType", type=StringType)
scmodel_Transition_messageCheckerClass: Property = Property(name="messageCheckerClass", type=StringType)
scmodel_Transition_priority: Property = Property(name="priority", type=FloatType)
scmodel_Transition_onTransition: Property = Property(name="onTransition", type=StringType)
scmodel_Transition_triggerProbCode: Property = Property(name="triggerProbCode", type=StringType)
scmodel_Transition_triggerProbCodeImports: Property = Property(name="triggerProbCodeImports", type=StringType)
scmodel_Transition_messageCheckerCode: Property = Property(name="messageCheckerCode", type=StringType)
scmodel_Transition_messageCheckerCodeImports: Property = Property(name="messageCheckerCodeImports", type=StringType)
scmodel_Transition_messageCheckerConditionLanguage: Property = Property(name="messageCheckerConditionLanguage", type=StringType)
scmodel_Transition_id: Property = Property(name="id", type=StringType)
scmodel_Transition_guard: Property = Property(name="guard", type=StringType)
scmodel_Transition_guardImports: Property = Property(name="guardImports", type=StringType)
scmodel_Transition_triggerTimedCode: Property = Property(name="triggerTimedCode", type=StringType)
scmodel_Transition_triggerTimedCodeImports: Property = Property(name="triggerTimedCodeImports", type=StringType)
scmodel_Transition_triggerExpRateCode: Property = Property(name="triggerExpRateCode", type=StringType)
scmodel_Transition_triggerExpRateCodeImports: Property = Property(name="triggerExpRateCodeImports", type=StringType)
scmodel_Transition_uuid: Property = Property(name="uuid", type=StringType)
scmodel_Transition_selfTransition: Property = Property(name="selfTransition", type=BooleanType)
scmodel_Transition.attributes={scmodel_Transition_guard, scmodel_Transition_triggerTime, scmodel_Transition_triggerType, scmodel_Transition_messageCheckerConditionLanguage, scmodel_Transition_triggerCodeLanguage, scmodel_Transition_triggerExpRateCodeImports, scmodel_Transition_id, scmodel_Transition_guardImports, scmodel_Transition_uuid, scmodel_Transition_messageCheckerCode, scmodel_Transition_triggerTimedCodeImports, scmodel_Transition_priority, scmodel_Transition_messageCheckerCodeImports, scmodel_Transition_outOfBranch, scmodel_Transition_triggerProbCodeImports, scmodel_Transition_triggerProbCode, scmodel_Transition_messageCheckerClass, scmodel_Transition_triggerTimedCode, scmodel_Transition_triggerConditionCodeImports, scmodel_Transition_defaultTransition, scmodel_Transition_triggerExpRateCode, scmodel_Transition_messageCheckerType, scmodel_Transition_onTransitionImports, scmodel_Transition_triggerConditionCode, scmodel_Transition_onTransition, scmodel_Transition_selfTransition}

# scmodel_StateMachine class attributes and methods
scmodel_StateMachine_agentType: Property = Property(name="agentType", type=StringType)
scmodel_StateMachine_package: Property = Property(name="package", type=StringType)
scmodel_StateMachine_className: Property = Property(name="className", type=StringType)
scmodel_StateMachine_language: Property = Property(name="language", type=StringType)
scmodel_StateMachine_nextID: Property = Property(name="nextID", type=IntegerType)
scmodel_StateMachine_id: Property = Property(name="id", type=StringType)
scmodel_StateMachine_uuid: Property = Property(name="uuid", type=StringType)
scmodel_StateMachine_priority: Property = Property(name="priority", type=FloatType)
scmodel_StateMachine.attributes={scmodel_StateMachine_priority, scmodel_StateMachine_id, scmodel_StateMachine_agentType, scmodel_StateMachine_className, scmodel_StateMachine_uuid, scmodel_StateMachine_language, scmodel_StateMachine_package, scmodel_StateMachine_nextID}

# scmodel_State class attributes and methods

# AbstractState class attributes and methods

# scmodel_FinalState class attributes and methods

# State class attributes and methods

# scmodel_CompositeState class attributes and methods

# scmodel_PseudoState class attributes and methods
scmodel_PseudoState_type: Property = Property(name="type", type=StringType)
scmodel_PseudoState.attributes={scmodel_PseudoState_type}

# scmodel_History class attributes and methods
scmodel_History_shallow: Property = Property(name="shallow", type=BooleanType)
scmodel_History.attributes={scmodel_History_shallow}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="scmodel_AbstractState", type=scmodel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="scmodel_StateMachine", type=scmodel_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="scmodel_Transition", type=scmodel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="scmodel_StateMachine2", type=scmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="scmodel_AbstractState5", type=scmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="scmodel_Transition4", type=scmodel_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="scmodel_AbstractState8", type=scmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="scmodel_Transition7", type=scmodel_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="scmodel_AbstractState10", type=scmodel_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="scmodel_CompositeState", type=scmodel_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_scmodel_State_AbstractState = Generalization(general=AbstractState, specific=scmodel_State)
gen_scmodel_FinalState_State = Generalization(general=State, specific=scmodel_FinalState)
gen_scmodel_CompositeState_AbstractState = Generalization(general=AbstractState, specific=scmodel_CompositeState)
gen_scmodel_PseudoState_AbstractState = Generalization(general=AbstractState, specific=scmodel_PseudoState)
gen_scmodel_History_State = Generalization(general=State, specific=scmodel_History)

# Domain Model
domain_model = DomainModel(
    name="scmodel",
    types={scmodel_AbstractState, scmodel_Transition, scmodel_StateMachine, scmodel_State, AbstractState, scmodel_FinalState, State, scmodel_CompositeState, scmodel_PseudoState, scmodel_History, MessageCheckerTypes, LanguageTypes, PseudoStateTypes, TriggerTypes},
    associations={states0, transitions1, from3, to6, children9},
    generalizations={gen_scmodel_State_AbstractState, gen_scmodel_FinalState_State, gen_scmodel_CompositeState_AbstractState, gen_scmodel_PseudoState_AbstractState, gen_scmodel_History_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)