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
activitydiagram_ActivityNode = Class(name="activitydiagram_ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram_ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram_Variable", is_abstract=True)
activitydiagram_ControlToken = Class(name="activitydiagram_ControlToken")
activitydiagram_ControlFlow = Class(name="activitydiagram_ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram_BooleanVariable")
activitydiagram_NamedElement = Class(name="activitydiagram_NamedElement", is_abstract=True)
activitydiagram_Activity = Class(name="activitydiagram_Activity")
NamedElement = Class(name="NamedElement")
activitydiagram_Event = Class(name="activitydiagram_Event")
activitydiagram_OpaqueAction = Class(name="activitydiagram_OpaqueAction")
Action = Class(name="Action")
activitydiagram_VariableAssignment = Class(name="activitydiagram_VariableAssignment", is_abstract=True)
activitydiagram_AcceptEventAction = Class(name="activitydiagram_AcceptEventAction")
activitydiagram_ControlNode = Class(name="activitydiagram_ControlNode", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram_InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_Action = Class(name="activitydiagram_Action", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_ForkNode = Class(name="activitydiagram_ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram_JoinNode")
activitydiagram_FinalNode = Class(name="activitydiagram_FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_FlowFinalNode = Class(name="activitydiagram_FlowFinalNode")
activitydiagram_DecisionNode = Class(name="activitydiagram_DecisionNode")
activitydiagram_MergeNode = Class(name="activitydiagram_MergeNode")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_BooleanValue = Class(name="activitydiagram_BooleanValue")
Value = Class(name="Value")
activitydiagram_IntegerValue = Class(name="activitydiagram_IntegerValue")
activitydiagram_IntegerBinaryExpression = Class(name="activitydiagram_IntegerBinaryExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram_IntegerComparisonExpression")
activitydiagram_Expression = Class(name="activitydiagram_Expression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_Value = Class(name="activitydiagram_Value", is_abstract=True)
activitydiagram_IntegerExpression = Class(name="activitydiagram_IntegerExpression", is_abstract=True)
activitydiagram_BooleanExpression = Class(name="activitydiagram_BooleanExpression", is_abstract=True)
activitydiagram_IntegerVariable = Class(name="activitydiagram_IntegerVariable")
Variable = Class(name="Variable")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_BooleanVariableAssignment = Class(name="activitydiagram_BooleanVariableAssignment")
VariableAssignment = Class(name="VariableAssignment")
activitydiagram_IntegerVariableAssignment = Class(name="activitydiagram_IntegerVariableAssignment")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram_BooleanUnaryExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram_BooleanBinaryExpression")
activitydiagram_Offer = Class(name="activitydiagram_Offer")

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityNode_m_terminate: Method = Method(name="terminate", parameters={})
activitydiagram_ActivityNode_m_isReady: Method = Method(name="isReady", parameters={})
activitydiagram_ActivityNode_m_addToken: Method = Method(name="addToken", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_ActivityNode_m_canAddToken: Method = Method(name="canAddToken", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_ActivityNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_ActivityNode_m_removeToken: Method = Method(name="removeToken", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}
activitydiagram_ActivityNode.methods={activitydiagram_ActivityNode_m_canAddToken, activitydiagram_ActivityNode_m_execute, activitydiagram_ActivityNode_m_addToken, activitydiagram_ActivityNode_m_terminate, activitydiagram_ActivityNode_m_hasOffers, activitydiagram_ActivityNode_m_removeToken, activitydiagram_ActivityNode_m_isReady}

# activitydiagram_ActivityEdge class attributes and methods
activitydiagram_ActivityEdge_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_ActivityEdge_m_takeOfferedToken: Method = Method(name="takeOfferedToken", parameters={}, type=StringType)
activitydiagram_ActivityEdge_m_hasOffer: Method = Method(name="hasOffer", parameters={})
activitydiagram_ActivityEdge.methods={activitydiagram_ActivityEdge_m_takeOfferedToken, activitydiagram_ActivityEdge_m_hasOffer, activitydiagram_ActivityEdge_m_sendOffer}

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=IntegerType)
activitydiagram_Variable_m_init: Method = Method(name="init", parameters={})
activitydiagram_Variable.attributes={activitydiagram_Variable_name}
activitydiagram_Variable.methods={activitydiagram_Variable_m_init}

# activitydiagram_ControlToken class attributes and methods
activitydiagram_ControlToken_m_isWithdrawn: Method = Method(name="isWithdrawn", parameters={})
activitydiagram_ControlToken.methods={activitydiagram_ControlToken_m_isWithdrawn}

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods
activitydiagram_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
activitydiagram_BooleanVariable_currentValue: Property = Property(name="currentValue", type=BooleanType)
activitydiagram_BooleanVariable_m_init: Method = Method(name="init", parameters={})
activitydiagram_BooleanVariable_m_evaluate: Method = Method(name="evaluate", parameters={})
activitydiagram_BooleanVariable.attributes={activitydiagram_BooleanVariable_initialValue, activitydiagram_BooleanVariable_currentValue}
activitydiagram_BooleanVariable.methods={activitydiagram_BooleanVariable_m_evaluate, activitydiagram_BooleanVariable_m_init}

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=BooleanType)
activitydiagram_NamedElement_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}
activitydiagram_NamedElement.methods={activitydiagram_NamedElement_m_execute}

# activitydiagram_Activity class attributes and methods
activitydiagram_Activity_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='activitydiagram_args', type=StringType)})
activitydiagram_Activity_m_main: Method = Method(name="main", parameters={})
activitydiagram_Activity_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_Activity.methods={activitydiagram_Activity_m_execute, activitydiagram_Activity_m_initializeModel, activitydiagram_Activity_m_main}

# NamedElement class attributes and methods

# activitydiagram_Event class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods
activitydiagram_OpaqueAction_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_OpaqueAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_OpaqueAction_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_OpaqueAction.methods={activitydiagram_OpaqueAction_m_sendOffer, activitydiagram_OpaqueAction_m_execute, activitydiagram_OpaqueAction_m_hasOffers}

# Action class attributes and methods

# activitydiagram_VariableAssignment class attributes and methods
activitydiagram_VariableAssignment_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_VariableAssignment.methods={activitydiagram_VariableAssignment_m_execute}

# activitydiagram_AcceptEventAction class attributes and methods
activitydiagram_AcceptEventAction_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_AcceptEventAction_m_canAccept: Method = Method(name="canAccept", parameters={Parameter(name='activitydiagram_event', type=StringType)})
activitydiagram_AcceptEventAction_m_accept: Method = Method(name="accept", parameters={Parameter(name='activitydiagram_event', type=StringType)})
activitydiagram_AcceptEventAction_m_waitForEvent: Method = Method(name="waitForEvent", parameters={})
activitydiagram_AcceptEventAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_AcceptEventAction_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_AcceptEventAction.methods={activitydiagram_AcceptEventAction_m_sendOffer, activitydiagram_AcceptEventAction_m_canAccept, activitydiagram_AcceptEventAction_m_hasOffers, activitydiagram_AcceptEventAction_m_waitForEvent, activitydiagram_AcceptEventAction_m_execute, activitydiagram_AcceptEventAction_m_accept}

# activitydiagram_ControlNode class attributes and methods

# activitydiagram_InitialNode class attributes and methods
activitydiagram_InitialNode_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='activitydiagram_token', type=StringType)})
activitydiagram_InitialNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_InitialNode.methods={activitydiagram_InitialNode_m_sendOffer, activitydiagram_InitialNode_m_execute}

# ControlNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods
activitydiagram_ForkNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ForkNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_ForkNode.methods={activitydiagram_ForkNode_m_execute, activitydiagram_ForkNode_m_hasOffers}

# activitydiagram_JoinNode class attributes and methods
activitydiagram_JoinNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_JoinNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_JoinNode.methods={activitydiagram_JoinNode_m_hasOffers, activitydiagram_JoinNode_m_execute}

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

# activitydiagram_DecisionNode class attributes and methods
activitydiagram_DecisionNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_DecisionNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_DecisionNode.methods={activitydiagram_DecisionNode_m_hasOffers, activitydiagram_DecisionNode_m_execute}

# activitydiagram_MergeNode class attributes and methods
activitydiagram_MergeNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_MergeNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_MergeNode.methods={activitydiagram_MergeNode_m_hasOffers, activitydiagram_MergeNode_m_execute}

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

# activitydiagram_BooleanVariableAssignment class attributes and methods
activitydiagram_BooleanVariableAssignment_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_BooleanVariableAssignment.methods={activitydiagram_BooleanVariableAssignment_m_execute}

# VariableAssignment class attributes and methods

# activitydiagram_IntegerVariableAssignment class attributes and methods
activitydiagram_IntegerVariableAssignment_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_IntegerVariableAssignment.methods={activitydiagram_IntegerVariableAssignment_m_execute}

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

# activitydiagram_Offer class attributes and methods

# Relationships
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="ActivityNode", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="activitydiagram_ActivityEdge", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity3", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals4: BinaryAssociation = BinaryAssociation(
    name="locals4",
    ends={
        Property(name="activitydiagram_Variable", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity5", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge7", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="activitydiagram_ActivityNode10", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge9", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offeredTokens11: BinaryAssociation = BinaryAssociation(
    name="offeredTokens11",
    ends={
        Property(name="activitydiagram_ControlToken", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge12", type=activitydiagram_ControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard13: BinaryAssociation = BinaryAssociation(
    name="guard13",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="activitydiagram_Event", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity", type=activitydiagram_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignments23: BinaryAssociation = BinaryAssociation(
    name="assignments23",
    ends={
        Property(name="activitydiagram_VariableAssignment", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_VariableAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventType24: BinaryAssociation = BinaryAssociation(
    name="eventType24",
    ends={
        Property(name="activitydiagram_Event25", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction", type=activitydiagram_Event, multiplicity=Multiplicity(1, 1))
    }
)
incoming26: BinaryAssociation = BinaryAssociation(
    name="incoming26",
    ends={
        Property(name="activitydiagram_ActivityEdge28", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction27", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
outgoing29: BinaryAssociation = BinaryAssociation(
    name="outgoing29",
    ends={
        Property(name="activitydiagram_ActivityEdge31", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction30", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
activity14: BinaryAssociation = BinaryAssociation(
    name="activity14",
    ends={
        Property(name="Activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
heldTokens15: BinaryAssociation = BinaryAssociation(
    name="heldTokens15",
    ends={
        Property(name="activitydiagram_ControlToken17", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityNode16", type=activitydiagram_ControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming18: BinaryAssociation = BinaryAssociation(
    name="incoming18",
    ends={
        Property(name="activitydiagram_ActivityEdge19", type=activitydiagram_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Action", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing20: BinaryAssociation = BinaryAssociation(
    name="outgoing20",
    ends={
        Property(name="activitydiagram_ActivityEdge22", type=activitydiagram_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Action21", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming44: BinaryAssociation = BinaryAssociation(
    name="incoming44",
    ends={
        Property(name="activitydiagram_ActivityEdge45", type=activitydiagram_ForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing46: BinaryAssociation = BinaryAssociation(
    name="outgoing46",
    ends={
        Property(name="activitydiagram_ActivityEdge48", type=activitydiagram_ForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkNode47", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming49: BinaryAssociation = BinaryAssociation(
    name="incoming49",
    ends={
        Property(name="activitydiagram_ActivityEdge50", type=activitydiagram_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_JoinNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing51: BinaryAssociation = BinaryAssociation(
    name="outgoing51",
    ends={
        Property(name="activitydiagram_ActivityEdge53", type=activitydiagram_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_JoinNode52", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming54: BinaryAssociation = BinaryAssociation(
    name="incoming54",
    ends={
        Property(name="activitydiagram_ActivityEdge55", type=activitydiagram_FinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_FinalNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing32: BinaryAssociation = BinaryAssociation(
    name="outgoing32",
    ends={
        Property(name="activitydiagram_ActivityEdge33", type=activitydiagram_InitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InitialNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming34: BinaryAssociation = BinaryAssociation(
    name="incoming34",
    ends={
        Property(name="activitydiagram_ActivityEdge35", type=activitydiagram_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_DecisionNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing36: BinaryAssociation = BinaryAssociation(
    name="outgoing36",
    ends={
        Property(name="activitydiagram_ActivityEdge38", type=activitydiagram_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_DecisionNode37", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming39: BinaryAssociation = BinaryAssociation(
    name="incoming39",
    ends={
        Property(name="activitydiagram_ActivityEdge40", type=activitydiagram_MergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_MergeNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing41: BinaryAssociation = BinaryAssociation(
    name="outgoing41",
    ends={
        Property(name="activitydiagram_ActivityEdge43", type=activitydiagram_MergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_MergeNode42", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
operand156: BinaryAssociation = BinaryAssociation(
    name="operand156",
    ends={
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerBinaryExpression", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand257: BinaryAssociation = BinaryAssociation(
    name="operand257",
    ends={
        Property(name="activitydiagram_IntegerExpression59", type=activitydiagram_IntegerBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerBinaryExpression58", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand268: BinaryAssociation = BinaryAssociation(
    name="operand268",
    ends={
        Property(name="activitydiagram_BooleanExpression70", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression69", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignee71: BinaryAssociation = BinaryAssociation(
    name="assignee71",
    ends={
        Property(name="activitydiagram_BooleanVariable72", type=activitydiagram_BooleanVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanVariableAssignment", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
expression73: BinaryAssociation = BinaryAssociation(
    name="expression73",
    ends={
        Property(name="activitydiagram_BooleanExpression75", type=activitydiagram_BooleanVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanVariableAssignment74", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignee76: BinaryAssociation = BinaryAssociation(
    name="assignee76",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerVariableAssignment", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
expression77: BinaryAssociation = BinaryAssociation(
    name="expression77",
    ends={
        Property(name="activitydiagram_IntegerExpression79", type=activitydiagram_IntegerVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerVariableAssignment78", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand160: BinaryAssociation = BinaryAssociation(
    name="operand160",
    ends={
        Property(name="activitydiagram_IntegerExpression61", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand262: BinaryAssociation = BinaryAssociation(
    name="operand262",
    ends={
        Property(name="activitydiagram_IntegerExpression64", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression63", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand65: BinaryAssociation = BinaryAssociation(
    name="operand65",
    ends={
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
operand166: BinaryAssociation = BinaryAssociation(
    name="operand166",
    ends={
        Property(name="activitydiagram_BooleanExpression67", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_activitydiagram_Event_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Event)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_AcceptEventAction_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_AcceptEventAction)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_Action_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_Action)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_FlowFinalNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanVariable_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_BooleanValue_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerValue_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerBinaryExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerBinaryExpression)
gen_activitydiagram_IntegerBinaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerBinaryExpression)
gen_activitydiagram_IntegerComparisonExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_Variable_Expression = Generalization(general=Expression, specific=activitydiagram_Variable)
gen_activitydiagram_Value_Expression = Generalization(general=Expression, specific=activitydiagram_Value)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_IntegerVariable_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_BooleanVariableAssignment_VariableAssignment = Generalization(general=VariableAssignment, specific=activitydiagram_BooleanVariableAssignment)
gen_activitydiagram_IntegerVariableAssignment_VariableAssignment = Generalization(general=VariableAssignment, specific=activitydiagram_IntegerVariableAssignment)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_ControlToken, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_NamedElement, activitydiagram_Activity, NamedElement, activitydiagram_Event, activitydiagram_OpaqueAction, Action, activitydiagram_VariableAssignment, activitydiagram_AcceptEventAction, activitydiagram_ControlNode, activitydiagram_InitialNode, ControlNode, activitydiagram_Action, ActivityNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_FlowFinalNode, activitydiagram_DecisionNode, activitydiagram_MergeNode, BooleanExpression, activitydiagram_BooleanValue, Value, activitydiagram_IntegerValue, activitydiagram_IntegerBinaryExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_Expression, Expression, activitydiagram_Value, activitydiagram_IntegerExpression, activitydiagram_BooleanExpression, activitydiagram_IntegerVariable, Variable, IntegerExpression, activitydiagram_BooleanVariableAssignment, VariableAssignment, activitydiagram_IntegerVariableAssignment, activitydiagram_BooleanUnaryExpression, activitydiagram_BooleanBinaryExpression, activitydiagram_Offer, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes1, edges2, locals4, source6, target8, offeredTokens11, guard13, events0, assignments23, eventType24, incoming26, outgoing29, activity14, heldTokens15, incoming18, outgoing20, incoming44, outgoing46, incoming49, outgoing51, incoming54, outgoing32, incoming34, outgoing36, incoming39, outgoing41, operand156, operand257, operand268, assignee71, expression73, assignee76, expression77, operand160, operand262, operand65, operand166},
    generalizations={gen_activitydiagram_Event_NamedElement, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_AcceptEventAction_ActivityNode, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_Action_ActivityNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_FlowFinalNode_FinalNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanVariable_BooleanExpression, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_BooleanValue_BooleanExpression, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerValue_IntegerExpression, gen_activitydiagram_IntegerBinaryExpression_Expression, gen_activitydiagram_IntegerBinaryExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_BooleanExpression, gen_activitydiagram_Variable_Expression, gen_activitydiagram_Value_Expression, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_IntegerVariable_IntegerExpression, gen_activitydiagram_BooleanVariableAssignment_VariableAssignment, gen_activitydiagram_IntegerVariableAssignment_VariableAssignment, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)