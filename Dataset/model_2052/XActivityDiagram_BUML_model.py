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
            EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="SMALLER"),
			EnumerationLiteral(name="SMALLER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS")
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
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode")
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable")
activitydiagram_Trace = Class(name="activitydiagram::Trace")
activitydiagram_Token = Class(name="activitydiagram::Token")
activitydiagram_ExecutableNode = Class(name="activitydiagram::ExecutableNode", is_abstract=True)
activitydiagram_Offer = Class(name="activitydiagram::Offer")
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable")
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_Action = Class(name="activitydiagram::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
activitydiagram_OpaqueAction = Class(name="activitydiagram::OpaqueAction")
Action = Class(name="Action")
activitydiagram_Expression = Class(name="activitydiagram::Expression", is_abstract=True)
activitydiagram_NamedElement = Class(name="activitydiagram::NamedElement", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
Variable = Class(name="Variable")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_Value = Class(name="activitydiagram::Value")
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable")
activitydiagram_BooleanExpression = Class(name="activitydiagram::BooleanExpression", is_abstract=True)
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_IntegerExpression = Class(name="activitydiagram::IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_IntegerCalculationExpression = Class(name="activitydiagram::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")
activitydiagram_InputValue = Class(name="activitydiagram::InputValue")
activitydiagram_Input = Class(name="activitydiagram::Input")
activitydiagram_ControlToken = Class(name="activitydiagram::ControlToken")
Token = Class(name="Token")
activitydiagram_ForkedToken = Class(name="activitydiagram::ForkedToken")

# activitydiagram_Activity class attributes and methods
activitydiagram_Activity_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
activitydiagram_Activity_m_main: Method = Method(name="main", parameters={})
activitydiagram_Activity_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_Activity_m_reset: Method = Method(name="reset", parameters={})
activitydiagram_Activity_m_getIntegerVariableValue: Method = Method(name="getIntegerVariableValue", parameters={Parameter(name='variableName')})
activitydiagram_Activity_m_getBooleanVariableValue: Method = Method(name="getBooleanVariableValue", parameters={Parameter(name='variableName')})
activitydiagram_Activity_m_getVariableValue: Method = Method(name="getVariableValue", parameters={Parameter(name='variableName')}, type=StringType)
activitydiagram_Activity_m_getVariable: Method = Method(name="getVariable", parameters={Parameter(name='variableName')}, type=StringType)
activitydiagram_Activity.methods={activitydiagram_Activity_m_execute, activitydiagram_Activity_m_main, activitydiagram_Activity_m_initializeModel, activitydiagram_Activity_m_getIntegerVariableValue, activitydiagram_Activity_m_getBooleanVariableValue, activitydiagram_Activity_m_reset, activitydiagram_Activity_m_getVariableValue, activitydiagram_Activity_m_getVariable}

# NamedElement class attributes and methods

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityNode_m_terminate: Method = Method(name="terminate", parameters={})
activitydiagram_ActivityNode_m_isReady: Method = Method(name="isReady", parameters={})
activitydiagram_ActivityNode_m_sendOffers: Method = Method(name="sendOffers", parameters={Parameter(name='tokens')})
activitydiagram_ActivityNode_m_takeOfferdTokens: Method = Method(name="takeOfferdTokens", parameters={}, type=StringType)
activitydiagram_ActivityNode_m_addTokens: Method = Method(name="addTokens", parameters={Parameter(name='tokens')})
activitydiagram_ActivityNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_ActivityNode_m_removeToken1: Method = Method(name="removeToken1", parameters={Parameter(name='token')})
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}
activitydiagram_ActivityNode.methods={activitydiagram_ActivityNode_m_removeToken1, activitydiagram_ActivityNode_m_isReady, activitydiagram_ActivityNode_m_sendOffers, activitydiagram_ActivityNode_m_terminate, activitydiagram_ActivityNode_m_hasOffers, activitydiagram_ActivityNode_m_addTokens, activitydiagram_ActivityNode_m_takeOfferdTokens, activitydiagram_ActivityNode_m_execute}

# activitydiagram_ActivityEdge class attributes and methods
activitydiagram_ActivityEdge_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='tokens')})
activitydiagram_ActivityEdge_m_takeOfferedTokens: Method = Method(name="takeOfferedTokens", parameters={}, type=StringType)
activitydiagram_ActivityEdge_m_hasOffer: Method = Method(name="hasOffer", parameters={})
activitydiagram_ActivityEdge.methods={activitydiagram_ActivityEdge_m_takeOfferedTokens, activitydiagram_ActivityEdge_m_hasOffer, activitydiagram_ActivityEdge_m_sendOffer}

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=StringType)
activitydiagram_Variable_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_Variable_m_init: Method = Method(name="init", parameters={})
activitydiagram_Variable_m_print: Method = Method(name="print", parameters={})
activitydiagram_Variable.attributes={activitydiagram_Variable_name}
activitydiagram_Variable.methods={activitydiagram_Variable_m_init, activitydiagram_Variable_m_execute, activitydiagram_Variable_m_print}

# activitydiagram_Trace class attributes and methods

# activitydiagram_Token class attributes and methods
activitydiagram_Token_m_isWithdrawn: Method = Method(name="isWithdrawn", parameters={})
activitydiagram_Token.methods={activitydiagram_Token_m_isWithdrawn}

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Offer class attributes and methods
activitydiagram_Offer_m_removeWithdrawnTokens: Method = Method(name="removeWithdrawnTokens", parameters={})
activitydiagram_Offer_m_hasTokens: Method = Method(name="hasTokens", parameters={})
activitydiagram_Offer.methods={activitydiagram_Offer_m_removeWithdrawnTokens, activitydiagram_Offer_m_hasTokens}

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods
activitydiagram_BooleanVariable_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_BooleanVariable_m_init: Method = Method(name="init", parameters={})
activitydiagram_BooleanVariable_m_print: Method = Method(name="print", parameters={})
activitydiagram_BooleanVariable.methods={activitydiagram_BooleanVariable_m_print, activitydiagram_BooleanVariable_m_init, activitydiagram_BooleanVariable_m_execute}

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods
activitydiagram_JoinNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_JoinNode.methods={activitydiagram_JoinNode_m_execute}

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods
activitydiagram_OpaqueAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_OpaqueAction.methods={activitydiagram_OpaqueAction_m_execute}

# Action class attributes and methods

# activitydiagram_Expression class attributes and methods
activitydiagram_Expression_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_Expression.methods={activitydiagram_Expression_m_execute}

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}
activitydiagram_NamedElement.methods={activitydiagram_NamedElement_m_execute}

# activitydiagram_InitialNode class attributes and methods
activitydiagram_InitialNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_InitialNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_InitialNode.methods={activitydiagram_InitialNode_m_execute, activitydiagram_InitialNode_m_hasOffers}

# ControlNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods
activitydiagram_ActivityFinalNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityFinalNode.methods={activitydiagram_ActivityFinalNode_m_execute}

# FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods
activitydiagram_ForkNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ForkNode.methods={activitydiagram_ForkNode_m_execute}

# Variable class attributes and methods

# activitydiagram_MergeNode class attributes and methods
activitydiagram_MergeNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_MergeNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_MergeNode.methods={activitydiagram_MergeNode_m_execute, activitydiagram_MergeNode_m_hasOffers}

# activitydiagram_DecisionNode class attributes and methods
activitydiagram_DecisionNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_DecisionNode_m_sendOffers: Method = Method(name="sendOffers", parameters={Parameter(name='tokens')})
activitydiagram_DecisionNode.methods={activitydiagram_DecisionNode_m_execute, activitydiagram_DecisionNode_m_sendOffers}

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods
activitydiagram_IntegerVariable_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_IntegerVariable_m_init: Method = Method(name="init", parameters={})
activitydiagram_IntegerVariable_m_print: Method = Method(name="print", parameters={})
activitydiagram_IntegerVariable.methods={activitydiagram_IntegerVariable_m_init, activitydiagram_IntegerVariable_m_print, activitydiagram_IntegerVariable_m_execute}

# activitydiagram_BooleanExpression class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_IntegerExpression class attributes and methods

# Expression class attributes and methods

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}
activitydiagram_BooleanUnaryExpression.methods={activitydiagram_BooleanUnaryExpression_m_execute}

# BooleanExpression class attributes and methods

# activitydiagram_IntegerCalculationExpression class attributes and methods
activitydiagram_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerCalculationExpression_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_IntegerCalculationExpression.attributes={activitydiagram_IntegerCalculationExpression_operator}
activitydiagram_IntegerCalculationExpression.methods={activitydiagram_IntegerCalculationExpression_m_execute}

# IntegerExpression class attributes and methods

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerComparisonExpression_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}
activitydiagram_IntegerComparisonExpression.methods={activitydiagram_IntegerComparisonExpression_m_execute}

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=BooleanType)
activitydiagram_BooleanBinaryExpression_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}
activitydiagram_BooleanBinaryExpression.methods={activitydiagram_BooleanBinaryExpression_m_execute}

# activitydiagram_InputValue class attributes and methods

# activitydiagram_Input class attributes and methods

# activitydiagram_ControlToken class attributes and methods

# Token class attributes and methods

# activitydiagram_ForkedToken class attributes and methods
activitydiagram_ForkedToken_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
activitydiagram_ForkedToken.attributes={activitydiagram_ForkedToken_remainingOffersCount}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="1", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="activitydiagram_ActivityEdge", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals3: BinaryAssociation = BinaryAssociation(
    name="locals3",
    ends={
        Property(name="activitydiagram_Variable", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity4", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs5: BinaryAssociation = BinaryAssociation(
    name="inputs5",
    ends={
        Property(name="activitydiagram_Variable7", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity6", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing10: BinaryAssociation = BinaryAssociation(
    name="outgoing10",
    ends={
        Property(name="12", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="11", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming13: BinaryAssociation = BinaryAssociation(
    name="incoming13",
    ends={
        Property(name="15", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity16: BinaryAssociation = BinaryAssociation(
    name="activity16",
    ends={
        Property(name="18", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
trace8: BinaryAssociation = BinaryAssociation(
    name="trace8",
    ends={
        Property(name="activitydiagram_Trace", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity9", type=activitydiagram_Trace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heldTokens19: BinaryAssociation = BinaryAssociation(
    name="heldTokens19",
    ends={
        Property(name="activitydiagram_Token", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="22", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="25", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offers26: BinaryAssociation = BinaryAssociation(
    name="offers26",
    ends={
        Property(name="activitydiagram_Offer", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge27", type=activitydiagram_Offer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard28: BinaryAssociation = BinaryAssociation(
    name="guard28",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
expressions29: BinaryAssociation = BinaryAssociation(
    name="expressions29",
    ends={
        Property(name="activitydiagram_Expression", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue30: BinaryAssociation = BinaryAssociation(
    name="initialValue30",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable31", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue32: BinaryAssociation = BinaryAssociation(
    name="currentValue32",
    ends={
        Property(name="activitydiagram_Value34", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable33", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1))
    }
)
operand235: BinaryAssociation = BinaryAssociation(
    name="operand235",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand136: BinaryAssociation = BinaryAssociation(
    name="operand136",
    ends={
        Property(name="activitydiagram_IntegerVariable38", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression37", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee39: BinaryAssociation = BinaryAssociation(
    name="assignee39",
    ends={
        Property(name="activitydiagram_BooleanVariable40", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee41: BinaryAssociation = BinaryAssociation(
    name="assignee41",
    ends={
        Property(name="activitydiagram_IntegerVariable42", type=activitydiagram_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerCalculationExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee43: BinaryAssociation = BinaryAssociation(
    name="assignee43",
    ends={
        Property(name="activitydiagram_BooleanVariable44", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand45: BinaryAssociation = BinaryAssociation(
    name="operand45",
    ends={
        Property(name="activitydiagram_BooleanVariable46", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand147: BinaryAssociation = BinaryAssociation(
    name="operand147",
    ends={
        Property(name="activitydiagram_BooleanVariable48", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand249: BinaryAssociation = BinaryAssociation(
    name="operand249",
    ends={
        Property(name="activitydiagram_BooleanVariable51", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression50", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
executedNodes64: BinaryAssociation = BinaryAssociation(
    name="executedNodes64",
    ends={
        Property(name="activitydiagram_ActivityNode66", type=activitydiagram_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Trace65", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
offeredTokens52: BinaryAssociation = BinaryAssociation(
    name="offeredTokens52",
    ends={
        Property(name="activitydiagram_Token54", type=activitydiagram_Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Offer53", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999))
    }
)
variable55: BinaryAssociation = BinaryAssociation(
    name="variable55",
    ends={
        Property(name="activitydiagram_Variable56", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 1))
    }
)
value57: BinaryAssociation = BinaryAssociation(
    name="value57",
    ends={
        Property(name="activitydiagram_Value59", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue58", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputValues60: BinaryAssociation = BinaryAssociation(
    name="inputValues60",
    ends={
        Property(name="activitydiagram_InputValue61", type=activitydiagram_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Input", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseToken62: BinaryAssociation = BinaryAssociation(
    name="baseToken62",
    ends={
        Property(name="activitydiagram_Token63", type=activitydiagram_ForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkedToken", type=activitydiagram_Token, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerCalculationExpression)
gen_activitydiagram_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_ControlToken_Token = Generalization(general=Token, specific=activitydiagram_ControlToken)
gen_activitydiagram_ForkedToken_Token = Generalization(general=Token, specific=activitydiagram_ForkedToken)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedElement, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_Trace, activitydiagram_Token, activitydiagram_ExecutableNode, activitydiagram_Offer, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlNode, ActivityNode, activitydiagram_JoinNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_Expression, activitydiagram_NamedElement, activitydiagram_InitialNode, ControlNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_ForkNode, Variable, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_Value, activitydiagram_IntegerVariable, activitydiagram_BooleanExpression, activitydiagram_BooleanValue, Value, activitydiagram_IntegerValue, activitydiagram_IntegerExpression, Expression, activitydiagram_BooleanUnaryExpression, BooleanExpression, activitydiagram_IntegerCalculationExpression, IntegerExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_BooleanBinaryExpression, activitydiagram_InputValue, activitydiagram_Input, activitydiagram_ControlToken, Token, activitydiagram_ForkedToken, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes0, edges2, locals3, inputs5, outgoing10, incoming13, activity16, trace8, heldTokens19, source20, target23, offers26, guard28, expressions29, initialValue30, currentValue32, operand235, operand136, assignee39, assignee41, assignee43, operand45, operand147, operand249, executedNodes64, offeredTokens52, variable55, value57, inputValues60, baseToken62},
    generalizations={gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_IntegerCalculationExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_IntegerExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_ControlToken_Token, gen_activitydiagram_ForkedToken_Token},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)