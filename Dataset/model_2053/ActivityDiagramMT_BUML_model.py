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
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode")
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable")
activitydiagram_Offer = Class(name="activitydiagram::Offer")
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable")
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_ExecutableNode = Class(name="activitydiagram::ExecutableNode", is_abstract=True)
activitydiagram_Action = Class(name="activitydiagram::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
activitydiagram_OpaqueAction = Class(name="activitydiagram::OpaqueAction")
Action = Class(name="Action")
activitydiagram_Expression = Class(name="activitydiagram::Expression")
activitydiagram_NamedElement = Class(name="activitydiagram::NamedElement", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_Value = Class(name="activitydiagram::Value")
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable")
Variable = Class(name="Variable")
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_IntegerExpression = Class(name="activitydiagram::IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_BooleanExpression = Class(name="activitydiagram::BooleanExpression", is_abstract=True)
activitydiagram_IntegerCalculationExpression = Class(name="activitydiagram::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_InputValue = Class(name="activitydiagram::InputValue")
activitydiagram_Input = Class(name="activitydiagram::Input")
activitydiagram_Token = Class(name="activitydiagram::Token")
activitydiagram_Context = Class(name="activitydiagram::Context")
activitydiagram_Trace = Class(name="activitydiagram::Trace")
activitydiagram_ForkedToken = Class(name="activitydiagram::ForkedToken")
Token = Class(name="Token")
activitydiagram_ControlToken = Class(name="activitydiagram::ControlToken")

# activitydiagram_Activity class attributes and methods
activitydiagram_Activity_m_main: Method = Method(name="main", parameters={Parameter(name='value')})
activitydiagram_Activity_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_Activity_m_reset: Method = Method(name="reset", parameters={})
activitydiagram_Activity_m_writeToFile: Method = Method(name="writeToFile", parameters={})
activitydiagram_Activity_m_printTrace: Method = Method(name="printTrace", parameters={})
activitydiagram_Activity_m_getIntegerVariableValue: Method = Method(name="getIntegerVariableValue", parameters={Parameter(name='variableName')})
activitydiagram_Activity_m_getBooleanVariableValue: Method = Method(name="getBooleanVariableValue", parameters={Parameter(name='variableName')})
activitydiagram_Activity_m_getVariableValue: Method = Method(name="getVariableValue", parameters={Parameter(name='variableName')}, type=StringType)
activitydiagram_Activity_m_getVariable: Method = Method(name="getVariable", parameters={Parameter(name='variableName')}, type=StringType)
activitydiagram_Activity_m_writeTrace: Method = Method(name="writeTrace", parameters={})
activitydiagram_Activity.methods={activitydiagram_Activity_m_writeToFile, activitydiagram_Activity_m_main, activitydiagram_Activity_m_getVariable, activitydiagram_Activity_m_execute, activitydiagram_Activity_m_reset, activitydiagram_Activity_m_getIntegerVariableValue, activitydiagram_Activity_m_getVariableValue, activitydiagram_Activity_m_writeTrace, activitydiagram_Activity_m_printTrace, activitydiagram_Activity_m_getBooleanVariableValue}

# NamedElement class attributes and methods

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_ActivityNode_m_terminate: Method = Method(name="terminate", parameters={})
activitydiagram_ActivityNode_m_isReady: Method = Method(name="isReady", parameters={})
activitydiagram_ActivityNode_m_sendOffers: Method = Method(name="sendOffers", parameters={Parameter(name='tokens')})
activitydiagram_ActivityNode_m_takeOfferdTokens: Method = Method(name="takeOfferdTokens", parameters={}, type=StringType)
activitydiagram_ActivityNode_m_addTokens: Method = Method(name="addTokens", parameters={Parameter(name='tokens')})
activitydiagram_ActivityNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_ActivityNode_m_removeToken: Method = Method(name="removeToken", parameters={Parameter(name='token')})
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}
activitydiagram_ActivityNode.methods={activitydiagram_ActivityNode_m_removeToken, activitydiagram_ActivityNode_m_takeOfferdTokens, activitydiagram_ActivityNode_m_isReady, activitydiagram_ActivityNode_m_execute, activitydiagram_ActivityNode_m_terminate, activitydiagram_ActivityNode_m_addTokens, activitydiagram_ActivityNode_m_hasOffers, activitydiagram_ActivityNode_m_sendOffers}

# activitydiagram_ActivityEdge class attributes and methods
activitydiagram_ActivityEdge_m_sendOffer: Method = Method(name="sendOffer", parameters={Parameter(name='tokens')})
activitydiagram_ActivityEdge_m_takeOfferedTokens: Method = Method(name="takeOfferedTokens", parameters={}, type=StringType)
activitydiagram_ActivityEdge_m_hasOffer: Method = Method(name="hasOffer", parameters={})
activitydiagram_ActivityEdge.methods={activitydiagram_ActivityEdge_m_takeOfferedTokens, activitydiagram_ActivityEdge_m_hasOffer, activitydiagram_ActivityEdge_m_sendOffer}

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=StringType)
activitydiagram_Variable_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_Variable_m_init: Method = Method(name="init", parameters={Parameter(name='c')})
activitydiagram_Variable_m_print: Method = Method(name="print", parameters={})
activitydiagram_Variable.attributes={activitydiagram_Variable_name}
activitydiagram_Variable.methods={activitydiagram_Variable_m_execute, activitydiagram_Variable_m_print, activitydiagram_Variable_m_init}

# activitydiagram_Offer class attributes and methods
activitydiagram_Offer_m_hasTokens: Method = Method(name="hasTokens", parameters={})
activitydiagram_Offer_m_removeWithdrawnTokens: Method = Method(name="removeWithdrawnTokens", parameters={})
activitydiagram_Offer.methods={activitydiagram_Offer_m_removeWithdrawnTokens, activitydiagram_Offer_m_hasTokens}

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods
activitydiagram_BooleanVariable_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_BooleanVariable_m_print: Method = Method(name="print", parameters={})
activitydiagram_BooleanVariable.methods={activitydiagram_BooleanVariable_m_print, activitydiagram_BooleanVariable_m_execute}

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods
activitydiagram_OpaqueAction_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_OpaqueAction.methods={activitydiagram_OpaqueAction_m_execute}

# Action class attributes and methods

# activitydiagram_Expression class attributes and methods
activitydiagram_Expression_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_Expression.methods={activitydiagram_Expression_m_execute}

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}
activitydiagram_NamedElement.methods={activitydiagram_NamedElement_m_execute}

# activitydiagram_InitialNode class attributes and methods
activitydiagram_InitialNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_InitialNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_InitialNode.methods={activitydiagram_InitialNode_m_execute, activitydiagram_InitialNode_m_hasOffers}

# ControlNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods
activitydiagram_ActivityFinalNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_ActivityFinalNode.methods={activitydiagram_ActivityFinalNode_m_execute}

# FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods
activitydiagram_ForkNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_ForkNode.methods={activitydiagram_ForkNode_m_execute}

# activitydiagram_JoinNode class attributes and methods
activitydiagram_JoinNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_JoinNode.methods={activitydiagram_JoinNode_m_execute}

# activitydiagram_MergeNode class attributes and methods
activitydiagram_MergeNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_MergeNode_m_hasOffers: Method = Method(name="hasOffers", parameters={})
activitydiagram_MergeNode.methods={activitydiagram_MergeNode_m_hasOffers, activitydiagram_MergeNode_m_execute}

# activitydiagram_DecisionNode class attributes and methods
activitydiagram_DecisionNode_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_DecisionNode_m_sendOffers: Method = Method(name="sendOffers", parameters={Parameter(name='tokens')})
activitydiagram_DecisionNode.methods={activitydiagram_DecisionNode_m_execute, activitydiagram_DecisionNode_m_sendOffers}

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods
activitydiagram_IntegerVariable_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_IntegerVariable_m_print: Method = Method(name="print", parameters={})
activitydiagram_IntegerVariable.methods={activitydiagram_IntegerVariable_m_execute, activitydiagram_IntegerVariable_m_print}

# Variable class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_IntegerExpression class attributes and methods

# Expression class attributes and methods

# activitydiagram_BooleanExpression class attributes and methods

# activitydiagram_IntegerCalculationExpression class attributes and methods
activitydiagram_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerCalculationExpression_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_IntegerCalculationExpression.attributes={activitydiagram_IntegerCalculationExpression_operator}
activitydiagram_IntegerCalculationExpression.methods={activitydiagram_IntegerCalculationExpression_m_execute}

# IntegerExpression class attributes and methods

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}
activitydiagram_BooleanUnaryExpression.methods={activitydiagram_BooleanUnaryExpression_m_execute}

# BooleanExpression class attributes and methods

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=BooleanType)
activitydiagram_BooleanBinaryExpression_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}
activitydiagram_BooleanBinaryExpression.methods={activitydiagram_BooleanBinaryExpression_m_execute}

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerComparisonExpression_m_execute: Method = Method(name="execute", parameters={Parameter(name='c')})
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}
activitydiagram_IntegerComparisonExpression.methods={activitydiagram_IntegerComparisonExpression_m_execute}

# activitydiagram_InputValue class attributes and methods

# activitydiagram_Input class attributes and methods

# activitydiagram_Token class attributes and methods
activitydiagram_Token_m_transfer: Method = Method(name="transfer", parameters={Parameter(name='holder')}, type=StringType)
activitydiagram_Token_m_withdraw: Method = Method(name="withdraw", parameters={})
activitydiagram_Token_m_isWithdrawn: Method = Method(name="isWithdrawn", parameters={})
activitydiagram_Token.methods={activitydiagram_Token_m_withdraw, activitydiagram_Token_m_transfer, activitydiagram_Token_m_isWithdrawn}

# activitydiagram_Context class attributes and methods

# activitydiagram_Trace class attributes and methods

# activitydiagram_ForkedToken class attributes and methods
activitydiagram_ForkedToken_remainingOffersCount: Property = Property(name="remainingOffersCount", type=StringType)
activitydiagram_ForkedToken.attributes={activitydiagram_ForkedToken_remainingOffersCount}

# Token class attributes and methods

# activitydiagram_ControlToken class attributes and methods

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
offers23: BinaryAssociation = BinaryAssociation(
    name="offers23",
    ends={
        Property(name="activitydiagram_Offer", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge24", type=activitydiagram_Offer, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing8: BinaryAssociation = BinaryAssociation(
    name="outgoing8",
    ends={
        Property(name="10", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming11: BinaryAssociation = BinaryAssociation(
    name="incoming11",
    ends={
        Property(name="13", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity14: BinaryAssociation = BinaryAssociation(
    name="activity14",
    ends={
        Property(name="16", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="19", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="22", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard25: BinaryAssociation = BinaryAssociation(
    name="guard25",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
expressions26: BinaryAssociation = BinaryAssociation(
    name="expressions26",
    ends={
        Property(name="activitydiagram_Expression", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
initialValue27: BinaryAssociation = BinaryAssociation(
    name="initialValue27",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable28", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue29: BinaryAssociation = BinaryAssociation(
    name="currentValue29",
    ends={
        Property(name="activitydiagram_Value31", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable30", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand232: BinaryAssociation = BinaryAssociation(
    name="operand232",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand133: BinaryAssociation = BinaryAssociation(
    name="operand133",
    ends={
        Property(name="activitydiagram_IntegerVariable35", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression34", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee36: BinaryAssociation = BinaryAssociation(
    name="assignee36",
    ends={
        Property(name="activitydiagram_BooleanVariable37", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee38: BinaryAssociation = BinaryAssociation(
    name="assignee38",
    ends={
        Property(name="activitydiagram_IntegerVariable39", type=activitydiagram_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerCalculationExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee40: BinaryAssociation = BinaryAssociation(
    name="assignee40",
    ends={
        Property(name="activitydiagram_BooleanVariable41", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand42: BinaryAssociation = BinaryAssociation(
    name="operand42",
    ends={
        Property(name="activitydiagram_BooleanVariable43", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand144: BinaryAssociation = BinaryAssociation(
    name="operand144",
    ends={
        Property(name="activitydiagram_BooleanVariable45", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand246: BinaryAssociation = BinaryAssociation(
    name="operand246",
    ends={
        Property(name="activitydiagram_BooleanVariable48", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression47", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="activitydiagram_Value50", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue", type=activitydiagram_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable51: BinaryAssociation = BinaryAssociation(
    name="variable51",
    ends={
        Property(name="activitydiagram_Variable53", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue52", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues54: BinaryAssociation = BinaryAssociation(
    name="inputValues54",
    ends={
        Property(name="activitydiagram_InputValue55", type=activitydiagram_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Input", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offeredTokens56: BinaryAssociation = BinaryAssociation(
    name="offeredTokens56",
    ends={
        Property(name="activitydiagram_Token", type=activitydiagram_Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Offer57", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999))
    }
)
holder58: BinaryAssociation = BinaryAssociation(
    name="holder58",
    ends={
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Token59", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
output60: BinaryAssociation = BinaryAssociation(
    name="output60",
    ends={
        Property(name="activitydiagram_Trace", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context", type=activitydiagram_Trace, multiplicity=Multiplicity(0, 1))
    }
)
activity61: BinaryAssociation = BinaryAssociation(
    name="activity61",
    ends={
        Property(name="activitydiagram_Activity63", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context62", type=activitydiagram_Activity, multiplicity=Multiplicity(0, 1))
    }
)
parent65: BinaryAssociation = BinaryAssociation(
    name="parent65",
    ends={
        Property(name="activitydiagram_Context66", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context64", type=activitydiagram_Context, multiplicity=Multiplicity(0, 1))
    }
)
inputValues67: BinaryAssociation = BinaryAssociation(
    name="inputValues67",
    ends={
        Property(name="activitydiagram_InputValue69", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context68", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999))
    }
)
node70: BinaryAssociation = BinaryAssociation(
    name="node70",
    ends={
        Property(name="activitydiagram_JoinNode", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context71", type=activitydiagram_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)
executedNodes72: BinaryAssociation = BinaryAssociation(
    name="executedNodes72",
    ends={
        Property(name="activitydiagram_ActivityNode74", type=activitydiagram_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Trace73", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
baseToken75: BinaryAssociation = BinaryAssociation(
    name="baseToken75",
    ends={
        Property(name="activitydiagram_Token76", type=activitydiagram_ForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkedToken", type=activitydiagram_Token, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerCalculationExpression)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_ForkedToken_Token = Generalization(general=Token, specific=activitydiagram_ForkedToken)
gen_activitydiagram_ControlToken_Token = Generalization(general=Token, specific=activitydiagram_ControlToken)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedElement, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_Offer, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlNode, ActivityNode, activitydiagram_ExecutableNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_Expression, activitydiagram_NamedElement, activitydiagram_InitialNode, ControlNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_Value, activitydiagram_IntegerVariable, Variable, activitydiagram_BooleanValue, Value, activitydiagram_IntegerValue, activitydiagram_IntegerExpression, Expression, activitydiagram_BooleanExpression, activitydiagram_IntegerCalculationExpression, IntegerExpression, activitydiagram_BooleanUnaryExpression, BooleanExpression, activitydiagram_BooleanBinaryExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_InputValue, activitydiagram_Input, activitydiagram_Token, activitydiagram_Context, activitydiagram_Trace, activitydiagram_ForkedToken, Token, activitydiagram_ControlToken, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes0, edges2, locals3, inputs5, offers23, outgoing8, incoming11, activity14, source17, target20, guard25, expressions26, initialValue27, currentValue29, operand232, operand133, assignee36, assignee38, assignee40, operand42, operand144, operand246, value49, variable51, inputValues54, offeredTokens56, holder58, output60, activity61, parent65, inputValues67, node70, executedNodes72, baseToken75},
    generalizations={gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerCalculationExpression_IntegerExpression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_IntegerComparisonExpression_IntegerExpression, gen_activitydiagram_ForkedToken_Token, gen_activitydiagram_ControlToken_Token},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)