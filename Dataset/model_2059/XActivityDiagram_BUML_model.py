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
IntegerCalculationOperator: Enumeration = Enumeration(
    name="IntegerCalculationOperator",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUBRACT")
    }
)

IntegerComparisonOperator: Enumeration = Enumeration(
    name="IntegerComparisonOperator",
    literals={
            EnumerationLiteral(name="SMALLER"),
			EnumerationLiteral(name="SMALLER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="GREATER")
    }
)

BooleanUnaryOperator: Enumeration = Enumeration(
    name="BooleanUnaryOperator",
    literals={
            EnumerationLiteral(name="NOT")
    }
)

BooleanBinaryOperator: Enumeration = Enumeration(
    name="BooleanBinaryOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
activitydiagram_Activity = Class(name="activitydiagram::Activity")
NamedElement = Class(name="NamedElement")
activitydiagram_Event = Class(name="activitydiagram::Event")
activitydiagram_NamedElement = Class(name="activitydiagram::NamedElement", is_abstract=True)
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable", is_abstract=True)
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable")
activitydiagram_ControlToken = Class(name="activitydiagram::ControlToken")
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
activitydiagram_Action = Class(name="activitydiagram::Action", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_OpaqueAction = Class(name="activitydiagram::OpaqueAction")
Action = Class(name="Action")
activitydiagram_VariableAssignment = Class(name="activitydiagram::VariableAssignment", is_abstract=True)
activitydiagram_AcceptEventAction = Class(name="activitydiagram::AcceptEventAction")
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_FlowFinalNode = Class(name="activitydiagram::FlowFinalNode")
activitydiagram_Expression = Class(name="activitydiagram::Expression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_Value = Class(name="activitydiagram::Value", is_abstract=True)
activitydiagram_IntegerExpression = Class(name="activitydiagram::IntegerExpression", is_abstract=True)
activitydiagram_BooleanExpression = Class(name="activitydiagram::BooleanExpression", is_abstract=True)
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable")
Variable = Class(name="Variable")
IntegerExpression = Class(name="IntegerExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_IntegerBinaryExpression = Class(name="activitydiagram::IntegerBinaryExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")
activitydiagram_BooleanVariableAssignment = Class(name="activitydiagram::BooleanVariableAssignment")
VariableAssignment = Class(name="VariableAssignment")
activitydiagram_IntegerVariableAssignment = Class(name="activitydiagram::IntegerVariableAssignment")
activitydiagram_Offer = Class(name="activitydiagram::Offer")

# activitydiagram_Activity class attributes and methods
activitydiagram_Activity_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
activitydiagram_Activity_m_main: Method = Method(name="main", parameters={})
activitydiagram_Activity_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_Activity.methods={activitydiagram_Activity_m_execute, activitydiagram_Activity_m_initializeModel, activitydiagram_Activity_m_main}

# NamedElement class attributes and methods

# activitydiagram_Event class attributes and methods

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=BooleanType)
activitydiagram_NamedElement_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}
activitydiagram_NamedElement.methods={activitydiagram_NamedElement_m_execute}

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityNode_m_terminate: Method = Method(name="terminate", parameters={})
activitydiagram_ActivityNode_m_removeToken: Method = Method(name="removeToken", parameters={Parameter(name='token')})
activitydiagram_ActivityNode_m_isReady: Method = Method(name="isReady", parameters={})
activitydiagram_ActivityNode_m_addToken: Method = Method(name="addToken", parameters={Parameter(name='token')})
activitydiagram_ActivityNode_m_canAddToken: Method = Method(name="canAddToken", parameters={Parameter(name='token')})
activitydiagram_ActivityNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}
activitydiagram_ActivityNode.methods={activitydiagram_ActivityNode_m_terminate, activitydiagram_ActivityNode_m_hasOffers, activitydiagram_ActivityNode_m_addToken, activitydiagram_ActivityNode_m_execute, activitydiagram_ActivityNode_m_canAddToken, activitydiagram_ActivityNode_m_removeToken, activitydiagram_ActivityNode_m_isReady}

# activitydiagram_ActivityEdge class attributes and methods
activitydiagram_ActivityEdge_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='token')})
activitydiagram_ActivityEdge_m_takeOfferedToken: Method = Method(name="takeOfferedToken", parameters={}, type=StringType)
activitydiagram_ActivityEdge_m_hasOffer: Method = Method(name="hasOffer", parameters={})
activitydiagram_ActivityEdge.methods={activitydiagram_ActivityEdge_m_sendOffer, activitydiagram_ActivityEdge_m_takeOfferedToken, activitydiagram_ActivityEdge_m_hasOffer}

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=IntegerType)
activitydiagram_Variable_m_init: Method = Method(name="init", parameters={})
activitydiagram_Variable.attributes={activitydiagram_Variable_name}
activitydiagram_Variable.methods={activitydiagram_Variable_m_init}

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods
activitydiagram_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
activitydiagram_BooleanVariable_currentValue: Property = Property(name="currentValue", type=BooleanType)
activitydiagram_BooleanVariable_m_init: Method = Method(name="init", parameters={})
activitydiagram_BooleanVariable_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_BooleanVariable.attributes={activitydiagram_BooleanVariable_currentValue, activitydiagram_BooleanVariable_initialValue}
activitydiagram_BooleanVariable.methods={activitydiagram_BooleanVariable_m_init, activitydiagram_BooleanVariable_m_evaluate}

# activitydiagram_ControlToken class attributes and methods
activitydiagram_ControlToken_m_isWithdrawn: Method = Method(name="isWithdrawn", parameters={})
activitydiagram_ControlToken.methods={activitydiagram_ControlToken_m_isWithdrawn}

# activitydiagram_ControlFlow class attributes and methods

# activitydiagram_Action class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods
activitydiagram_OpaqueAction_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='token')})
activitydiagram_OpaqueAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_OpaqueAction_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_OpaqueAction.methods={activitydiagram_OpaqueAction_m_sendOffer, activitydiagram_OpaqueAction_m_execute, activitydiagram_OpaqueAction_m_hasOffers}

# Action class attributes and methods

# activitydiagram_VariableAssignment class attributes and methods
activitydiagram_VariableAssignment_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_VariableAssignment.methods={activitydiagram_VariableAssignment_m_execute}

# activitydiagram_AcceptEventAction class attributes and methods
activitydiagram_AcceptEventAction_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='token')})
activitydiagram_AcceptEventAction_m_canAccept: Method = Method(name="canAccept", parameters={Parameter(name='event')})
activitydiagram_AcceptEventAction_m_accept: Method = Method(name="accept", parameters={Parameter(name='event')})
activitydiagram_AcceptEventAction_m_waitForEvent: Method = Method(name="waitForEvent", parameters={})
activitydiagram_AcceptEventAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_AcceptEventAction_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_AcceptEventAction.methods={activitydiagram_AcceptEventAction_m_execute, activitydiagram_AcceptEventAction_m_sendOffer, activitydiagram_AcceptEventAction_m_canAccept, activitydiagram_AcceptEventAction_m_accept, activitydiagram_AcceptEventAction_m_hasOffers, activitydiagram_AcceptEventAction_m_waitForEvent}

# activitydiagram_ControlNode class attributes and methods

# activitydiagram_InitialNode class attributes and methods
activitydiagram_InitialNode_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='token')})
activitydiagram_InitialNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_InitialNode.methods={activitydiagram_InitialNode_m_execute, activitydiagram_InitialNode_m_sendOffer}

# ControlNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods
activitydiagram_DecisionNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_DecisionNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_DecisionNode.methods={activitydiagram_DecisionNode_m_execute, activitydiagram_DecisionNode_m_hasOffers}

# activitydiagram_MergeNode class attributes and methods
activitydiagram_MergeNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_MergeNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_MergeNode.methods={activitydiagram_MergeNode_m_hasOffers, activitydiagram_MergeNode_m_execute}

# activitydiagram_ForkNode class attributes and methods
activitydiagram_ForkNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_ForkNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ForkNode.methods={activitydiagram_ForkNode_m_execute, activitydiagram_ForkNode_m_hasOffers}

# activitydiagram_JoinNode class attributes and methods
activitydiagram_JoinNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_JoinNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_JoinNode.methods={activitydiagram_JoinNode_m_execute, activitydiagram_JoinNode_m_hasOffers}

# activitydiagram_FinalNode class attributes and methods
activitydiagram_FinalNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_FinalNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_FinalNode.methods={activitydiagram_FinalNode_m_execute, activitydiagram_FinalNode_m_hasOffers}

# activitydiagram_ActivityFinalNode class attributes and methods
activitydiagram_ActivityFinalNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityFinalNode.methods={activitydiagram_ActivityFinalNode_m_execute}

# FinalNode class attributes and methods

# activitydiagram_FlowFinalNode class attributes and methods
activitydiagram_FlowFinalNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_FlowFinalNode.methods={activitydiagram_FlowFinalNode_m_execute}

# activitydiagram_Expression class attributes and methods

# Expression class attributes and methods

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerExpression class attributes and methods
activitydiagram_IntegerExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_IntegerExpression.methods={activitydiagram_IntegerExpression_m_evaluate}

# activitydiagram_BooleanExpression class attributes and methods
activitydiagram_BooleanExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_BooleanExpression.methods={activitydiagram_BooleanExpression_m_evaluate}

# activitydiagram_IntegerVariable class attributes and methods
activitydiagram_IntegerVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
activitydiagram_IntegerVariable_currentValue: Property = Property(name="currentValue", type=BooleanType)
activitydiagram_IntegerVariable_m_init: Method = Method(name="init", parameters={})
activitydiagram_IntegerVariable_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_IntegerVariable.attributes={activitydiagram_IntegerVariable_initialValue, activitydiagram_IntegerVariable_currentValue}
activitydiagram_IntegerVariable.methods={activitydiagram_IntegerVariable_m_init, activitydiagram_IntegerVariable_m_evaluate}

# Variable class attributes and methods

# IntegerExpression class attributes and methods

# BooleanExpression class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_IntegerBinaryExpression class attributes and methods
activitydiagram_IntegerBinaryExpression_operator: Property = Property(name="operator", type=BooleanType)
activitydiagram_IntegerBinaryExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_IntegerBinaryExpression.attributes={activitydiagram_IntegerBinaryExpression_operator}
activitydiagram_IntegerBinaryExpression.methods={activitydiagram_IntegerBinaryExpression_m_evaluate}

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=BooleanType)
activitydiagram_IntegerComparisonExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}
activitydiagram_IntegerComparisonExpression.methods={activitydiagram_IntegerComparisonExpression_m_evaluate}

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=BooleanType)
activitydiagram_BooleanUnaryExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}
activitydiagram_BooleanUnaryExpression.methods={activitydiagram_BooleanUnaryExpression_m_evaluate}

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=BooleanType)
activitydiagram_BooleanBinaryExpression_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}
activitydiagram_BooleanBinaryExpression.methods={activitydiagram_BooleanBinaryExpression_m_evaluate}

# activitydiagram_BooleanVariableAssignment class attributes and methods
activitydiagram_BooleanVariableAssignment_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_BooleanVariableAssignment.methods={activitydiagram_BooleanVariableAssignment_m_execute}

# VariableAssignment class attributes and methods

# activitydiagram_IntegerVariableAssignment class attributes and methods
activitydiagram_IntegerVariableAssignment_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_IntegerVariableAssignment.methods={activitydiagram_IntegerVariableAssignment_m_execute}

# activitydiagram_Offer class attributes and methods

# Relationships
locals5: BinaryAssociation = BinaryAssociation(
    name="locals5",
    ends={
        Property(name="activitydiagram_Variable", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity6", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="activitydiagram_Event", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity", type=activitydiagram_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="2", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges3: BinaryAssociation = BinaryAssociation(
    name="edges3",
    ends={
        Property(name="activitydiagram_ActivityEdge", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity4", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard14: BinaryAssociation = BinaryAssociation(
    name="guard14",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge8", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="activitydiagram_ActivityNode11", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge10", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offeredTokens12: BinaryAssociation = BinaryAssociation(
    name="offeredTokens12",
    ends={
        Property(name="activitydiagram_ControlToken", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge13", type=activitydiagram_ControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity15: BinaryAssociation = BinaryAssociation(
    name="activity15",
    ends={
        Property(name="17", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
heldTokens18: BinaryAssociation = BinaryAssociation(
    name="heldTokens18",
    ends={
        Property(name="activitydiagram_ControlToken20", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityNode19", type=activitydiagram_ControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="activitydiagram_ActivityEdge22", type=activitydiagram_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Action", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing23: BinaryAssociation = BinaryAssociation(
    name="outgoing23",
    ends={
        Property(name="activitydiagram_ActivityEdge25", type=activitydiagram_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Action24", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
assignments26: BinaryAssociation = BinaryAssociation(
    name="assignments26",
    ends={
        Property(name="activitydiagram_VariableAssignment", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_VariableAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventType27: BinaryAssociation = BinaryAssociation(
    name="eventType27",
    ends={
        Property(name="activitydiagram_Event28", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction", type=activitydiagram_Event, multiplicity=Multiplicity(1, 1))
    }
)
incoming29: BinaryAssociation = BinaryAssociation(
    name="incoming29",
    ends={
        Property(name="activitydiagram_ActivityEdge31", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction30", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
outgoing32: BinaryAssociation = BinaryAssociation(
    name="outgoing32",
    ends={
        Property(name="activitydiagram_ActivityEdge34", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction33", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing35: BinaryAssociation = BinaryAssociation(
    name="outgoing35",
    ends={
        Property(name="activitydiagram_ActivityEdge36", type=activitydiagram_InitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InitialNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming37: BinaryAssociation = BinaryAssociation(
    name="incoming37",
    ends={
        Property(name="activitydiagram_ActivityEdge38", type=activitydiagram_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_DecisionNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing39: BinaryAssociation = BinaryAssociation(
    name="outgoing39",
    ends={
        Property(name="activitydiagram_ActivityEdge41", type=activitydiagram_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_DecisionNode40", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming42: BinaryAssociation = BinaryAssociation(
    name="incoming42",
    ends={
        Property(name="activitydiagram_ActivityEdge43", type=activitydiagram_MergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_MergeNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing44: BinaryAssociation = BinaryAssociation(
    name="outgoing44",
    ends={
        Property(name="activitydiagram_ActivityEdge46", type=activitydiagram_MergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_MergeNode45", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming47: BinaryAssociation = BinaryAssociation(
    name="incoming47",
    ends={
        Property(name="activitydiagram_ActivityEdge48", type=activitydiagram_ForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing49: BinaryAssociation = BinaryAssociation(
    name="outgoing49",
    ends={
        Property(name="activitydiagram_ActivityEdge51", type=activitydiagram_ForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkNode50", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming52: BinaryAssociation = BinaryAssociation(
    name="incoming52",
    ends={
        Property(name="activitydiagram_ActivityEdge53", type=activitydiagram_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_JoinNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing54: BinaryAssociation = BinaryAssociation(
    name="outgoing54",
    ends={
        Property(name="activitydiagram_ActivityEdge56", type=activitydiagram_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_JoinNode55", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming57: BinaryAssociation = BinaryAssociation(
    name="incoming57",
    ends={
        Property(name="activitydiagram_ActivityEdge58", type=activitydiagram_FinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_FinalNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
operand159: BinaryAssociation = BinaryAssociation(
    name="operand159",
    ends={
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerBinaryExpression", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand260: BinaryAssociation = BinaryAssociation(
    name="operand260",
    ends={
        Property(name="activitydiagram_IntegerExpression62", type=activitydiagram_IntegerBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerBinaryExpression61", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand163: BinaryAssociation = BinaryAssociation(
    name="operand163",
    ends={
        Property(name="activitydiagram_IntegerExpression64", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand265: BinaryAssociation = BinaryAssociation(
    name="operand265",
    ends={
        Property(name="activitydiagram_IntegerExpression67", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression66", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand68: BinaryAssociation = BinaryAssociation(
    name="operand68",
    ends={
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
operand169: BinaryAssociation = BinaryAssociation(
    name="operand169",
    ends={
        Property(name="activitydiagram_BooleanExpression70", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
operand271: BinaryAssociation = BinaryAssociation(
    name="operand271",
    ends={
        Property(name="activitydiagram_BooleanExpression73", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression72", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignee74: BinaryAssociation = BinaryAssociation(
    name="assignee74",
    ends={
        Property(name="activitydiagram_BooleanVariable75", type=activitydiagram_BooleanVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanVariableAssignment", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
expression76: BinaryAssociation = BinaryAssociation(
    name="expression76",
    ends={
        Property(name="activitydiagram_BooleanExpression78", type=activitydiagram_BooleanVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanVariableAssignment77", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignee79: BinaryAssociation = BinaryAssociation(
    name="assignee79",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerVariableAssignment", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
expression80: BinaryAssociation = BinaryAssociation(
    name="expression80",
    ends={
        Property(name="activitydiagram_IntegerExpression82", type=activitydiagram_IntegerVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerVariableAssignment81", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_Event_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Event)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_Action_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_AcceptEventAction_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_AcceptEventAction)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_FlowFinalNode)
gen_activitydiagram_Variable_Expression = Generalization(general=Expression, specific=activitydiagram_Variable)
gen_activitydiagram_Value_Expression = Generalization(general=Expression, specific=activitydiagram_Value)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_IntegerVariable_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanVariable_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_BooleanValue_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerValue_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerBinaryExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerBinaryExpression)
gen_activitydiagram_IntegerBinaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerBinaryExpression)
gen_activitydiagram_IntegerComparisonExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_BooleanVariableAssignment_VariableAssignment = Generalization(general=VariableAssignment, specific=activitydiagram_BooleanVariableAssignment)
gen_activitydiagram_IntegerVariableAssignment_VariableAssignment = Generalization(general=VariableAssignment, specific=activitydiagram_IntegerVariableAssignment)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedElement, activitydiagram_Event, activitydiagram_NamedElement, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlToken, activitydiagram_ControlFlow, activitydiagram_Action, ActivityNode, activitydiagram_OpaqueAction, Action, activitydiagram_VariableAssignment, activitydiagram_AcceptEventAction, activitydiagram_ControlNode, activitydiagram_InitialNode, ControlNode, activitydiagram_DecisionNode, activitydiagram_MergeNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_FlowFinalNode, activitydiagram_Expression, Expression, activitydiagram_Value, activitydiagram_IntegerExpression, activitydiagram_BooleanExpression, activitydiagram_IntegerVariable, Variable, IntegerExpression, BooleanExpression, activitydiagram_BooleanValue, Value, activitydiagram_IntegerValue, activitydiagram_IntegerBinaryExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_BooleanUnaryExpression, activitydiagram_BooleanBinaryExpression, activitydiagram_BooleanVariableAssignment, VariableAssignment, activitydiagram_IntegerVariableAssignment, activitydiagram_Offer, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={locals5, events0, nodes1, edges3, guard14, source7, target9, offeredTokens12, activity15, heldTokens18, incoming21, outgoing23, assignments26, eventType27, incoming29, outgoing32, outgoing35, incoming37, outgoing39, incoming42, outgoing44, incoming47, outgoing49, incoming52, outgoing54, incoming57, operand159, operand260, operand163, operand265, operand68, operand169, operand271, assignee74, expression76, assignee79, expression80},
    generalizations={gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_Event_NamedElement, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_Action_ActivityNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_AcceptEventAction_ActivityNode, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_FlowFinalNode_FinalNode, gen_activitydiagram_Variable_Expression, gen_activitydiagram_Value_Expression, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_IntegerVariable_IntegerExpression, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanVariable_BooleanExpression, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_BooleanValue_BooleanExpression, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerValue_IntegerExpression, gen_activitydiagram_IntegerBinaryExpression_Expression, gen_activitydiagram_IntegerBinaryExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_BooleanExpression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_BooleanVariableAssignment_VariableAssignment, gen_activitydiagram_IntegerVariableAssignment_VariableAssignment},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)