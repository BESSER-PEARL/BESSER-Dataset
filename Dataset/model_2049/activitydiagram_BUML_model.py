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

# Classes
activitydiagram_ActivityNode = Class(name="activitydiagram_ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram_ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram_Variable", is_abstract=True)
activitydiagram_Trace = Class(name="activitydiagram_Trace")
activitydiagram_Signal = Class(name="activitydiagram_Signal")
activitydiagram_Activity = Class(name="activitydiagram_Activity")
NamedElement = Class(name="NamedElement")
activitydiagram_ControlFlow = Class(name="activitydiagram_ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram_BooleanVariable")
activitydiagram_ControlNode = Class(name="activitydiagram_ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_ExecutableNode = Class(name="activitydiagram_ExecutableNode", is_abstract=True)
activitydiagram_Action = Class(name="activitydiagram_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
activitydiagram_OpaqueAction = Class(name="activitydiagram_OpaqueAction")
Action = Class(name="Action")
activitydiagram_Expression = Class(name="activitydiagram_Expression", is_abstract=True)
activitydiagram_NamedElement = Class(name="activitydiagram_NamedElement", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram_InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_FinalNode = Class(name="activitydiagram_FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram_ForkNode")
activitydiagram_Token = Class(name="activitydiagram_Token", is_abstract=True)
activitydiagram_Offer = Class(name="activitydiagram_Offer")
activitydiagram_IntegerValue = Class(name="activitydiagram_IntegerValue")
activitydiagram_IntegerExpression = Class(name="activitydiagram_IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_BooleanExpression = Class(name="activitydiagram_BooleanExpression", is_abstract=True)
activitydiagram_IntegerCalculationExpression = Class(name="activitydiagram_IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram_IntegerComparisonExpression")
activitydiagram_JoinNode = Class(name="activitydiagram_JoinNode")
activitydiagram_MergeNode = Class(name="activitydiagram_MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram_DecisionNode")
activitydiagram_Value = Class(name="activitydiagram_Value", is_abstract=True)
activitydiagram_IntegerVariable = Class(name="activitydiagram_IntegerVariable")
Variable = Class(name="Variable")
activitydiagram_BooleanValue = Class(name="activitydiagram_BooleanValue")
Value = Class(name="Value")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram_BooleanBinaryExpression")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram_BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_ControlToken = Class(name="activitydiagram_ControlToken")
Token = Class(name="Token")
activitydiagram_ForkedToken = Class(name="activitydiagram_ForkedToken")
activitydiagram_SendSignalAction = Class(name="activitydiagram_SendSignalAction")
activitydiagram_AcceptEventAction = Class(name="activitydiagram_AcceptEventAction")
activitydiagram_SignalEvent = Class(name="activitydiagram_SignalEvent")
Signal = Class(name="Signal")
activitydiagram_InputValue = Class(name="activitydiagram_InputValue")
activitydiagram_Input = Class(name="activitydiagram_Input")

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityNode_m_terminate: Method = Method(name="terminate", parameters={})
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}
activitydiagram_ActivityNode.methods={activitydiagram_ActivityNode_m_execute, activitydiagram_ActivityNode_m_terminate}

# activitydiagram_ActivityEdge class attributes and methods
activitydiagram_ActivityEdge_m_evaluateGuard: Method = Method(name="evaluateGuard", parameters={})
activitydiagram_ActivityEdge_m_clearOffer: Method = Method(name="clearOffer", parameters={})
activitydiagram_ActivityEdge.methods={activitydiagram_ActivityEdge_m_clearOffer, activitydiagram_ActivityEdge_m_evaluateGuard}

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=StringType)
activitydiagram_Variable.attributes={activitydiagram_Variable_name}

# activitydiagram_Trace class attributes and methods

# activitydiagram_Signal class attributes and methods

# activitydiagram_Activity class attributes and methods
activitydiagram_Activity_inputValuePath: Property = Property(name="inputValuePath", type=StringType)
activitydiagram_Activity_m_finish: Method = Method(name="finish", parameters={})
activitydiagram_Activity_m_initialize: Method = Method(name="initialize", parameters={})
activitydiagram_Activity.attributes={activitydiagram_Activity_inputValuePath}
activitydiagram_Activity.methods={activitydiagram_Activity_m_finish, activitydiagram_Activity_m_initialize}

# NamedElement class attributes and methods

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods
activitydiagram_OpaqueAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_OpaqueAction.methods={activitydiagram_OpaqueAction_m_execute}

# Action class attributes and methods

# activitydiagram_Expression class attributes and methods

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}

# activitydiagram_InitialNode class attributes and methods
activitydiagram_InitialNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_InitialNode.methods={activitydiagram_InitialNode_m_execute}

# ControlNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods
activitydiagram_ActivityFinalNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ActivityFinalNode.methods={activitydiagram_ActivityFinalNode_m_execute}

# FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods
activitydiagram_ForkNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_ForkNode.methods={activitydiagram_ForkNode_m_execute}

# activitydiagram_Token class attributes and methods

# activitydiagram_Offer class attributes and methods

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_IntegerExpression class attributes and methods

# Expression class attributes and methods

# activitydiagram_BooleanExpression class attributes and methods

# activitydiagram_IntegerCalculationExpression class attributes and methods
activitydiagram_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerCalculationExpression.attributes={activitydiagram_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}

# activitydiagram_JoinNode class attributes and methods
activitydiagram_JoinNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_JoinNode.methods={activitydiagram_JoinNode_m_execute}

# activitydiagram_MergeNode class attributes and methods
activitydiagram_MergeNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_MergeNode.methods={activitydiagram_MergeNode_m_execute}

# activitydiagram_DecisionNode class attributes and methods
activitydiagram_DecisionNode_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_DecisionNode.methods={activitydiagram_DecisionNode_m_execute}

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods

# Variable class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# activitydiagram_ControlToken class attributes and methods

# Token class attributes and methods

# activitydiagram_ForkedToken class attributes and methods
activitydiagram_ForkedToken_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
activitydiagram_ForkedToken.attributes={activitydiagram_ForkedToken_remainingOffersCount}

# activitydiagram_SendSignalAction class attributes and methods
activitydiagram_SendSignalAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_SendSignalAction.methods={activitydiagram_SendSignalAction_m_execute}

# activitydiagram_AcceptEventAction class attributes and methods
activitydiagram_AcceptEventAction_m_execute: Method = Method(name="execute", parameters={})
activitydiagram_AcceptEventAction.methods={activitydiagram_AcceptEventAction_m_execute}

# activitydiagram_SignalEvent class attributes and methods

# Signal class attributes and methods

# activitydiagram_InputValue class attributes and methods

# activitydiagram_Input class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="ActivityNode", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="activitydiagram_ActivityEdge", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals2: BinaryAssociation = BinaryAssociation(
    name="locals2",
    ends={
        Property(name="activitydiagram_Variable", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity3", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs4: BinaryAssociation = BinaryAssociation(
    name="inputs4",
    ends={
        Property(name="activitydiagram_Variable6", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity5", type=activitydiagram_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trace7: BinaryAssociation = BinaryAssociation(
    name="trace7",
    ends={
        Property(name="activitydiagram_Trace", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity8", type=activitydiagram_Trace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signals9: BinaryAssociation = BinaryAssociation(
    name="signals9",
    ends={
        Property(name="activitydiagram_Signal", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity10", type=activitydiagram_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="ActivityEdge", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
guard22: BinaryAssociation = BinaryAssociation(
    name="guard22",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
expressions23: BinaryAssociation = BinaryAssociation(
    name="expressions23",
    ends={
        Property(name="activitydiagram_Expression", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming12: BinaryAssociation = BinaryAssociation(
    name="incoming12",
    ends={
        Property(name="ActivityEdge13", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
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
        Property(name="Token", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="holder", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="ActivityNode17", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="ActivityNode19", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offers20: BinaryAssociation = BinaryAssociation(
    name="offers20",
    ends={
        Property(name="activitydiagram_Offer", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge21", type=activitydiagram_Offer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand229: BinaryAssociation = BinaryAssociation(
    name="operand229",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand130: BinaryAssociation = BinaryAssociation(
    name="operand130",
    ends={
        Property(name="activitydiagram_IntegerVariable32", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression31", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee33: BinaryAssociation = BinaryAssociation(
    name="assignee33",
    ends={
        Property(name="activitydiagram_BooleanVariable34", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee35: BinaryAssociation = BinaryAssociation(
    name="assignee35",
    ends={
        Property(name="activitydiagram_IntegerVariable36", type=activitydiagram_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerCalculationExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee37: BinaryAssociation = BinaryAssociation(
    name="assignee37",
    ends={
        Property(name="activitydiagram_BooleanVariable38", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
initialValue24: BinaryAssociation = BinaryAssociation(
    name="initialValue24",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable25", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue26: BinaryAssociation = BinaryAssociation(
    name="currentValue26",
    ends={
        Property(name="activitydiagram_Value28", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable27", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand39: BinaryAssociation = BinaryAssociation(
    name="operand39",
    ends={
        Property(name="activitydiagram_BooleanVariable40", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand141: BinaryAssociation = BinaryAssociation(
    name="operand141",
    ends={
        Property(name="activitydiagram_BooleanVariable42", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand243: BinaryAssociation = BinaryAssociation(
    name="operand243",
    ends={
        Property(name="activitydiagram_BooleanVariable45", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression44", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
baseToken59: BinaryAssociation = BinaryAssociation(
    name="baseToken59",
    ends={
        Property(name="activitydiagram_Token60", type=activitydiagram_ForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkedToken", type=activitydiagram_Token, multiplicity=Multiplicity(1, 1))
    }
)
signal61: BinaryAssociation = BinaryAssociation(
    name="signal61",
    ends={
        Property(name="activitydiagram_Signal62", type=activitydiagram_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_SendSignalAction", type=activitydiagram_Signal, multiplicity=Multiplicity(0, 1))
    }
)
trigger63: BinaryAssociation = BinaryAssociation(
    name="trigger63",
    ends={
        Property(name="activitydiagram_SignalEvent", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction", type=activitydiagram_SignalEvent, multiplicity=Multiplicity(0, 1))
    }
)
offeredTokens46: BinaryAssociation = BinaryAssociation(
    name="offeredTokens46",
    ends={
        Property(name="activitydiagram_Token", type=activitydiagram_Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Offer47", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999))
    }
)
holder48: BinaryAssociation = BinaryAssociation(
    name="holder48",
    ends={
        Property(name="ActivityNode49", type=activitydiagram_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="heldTokens", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
executedNodes50: BinaryAssociation = BinaryAssociation(
    name="executedNodes50",
    ends={
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Trace51", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
value52: BinaryAssociation = BinaryAssociation(
    name="value52",
    ends={
        Property(name="activitydiagram_Value53", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue", type=activitydiagram_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable54: BinaryAssociation = BinaryAssociation(
    name="variable54",
    ends={
        Property(name="activitydiagram_Variable56", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue55", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues57: BinaryAssociation = BinaryAssociation(
    name="inputValues57",
    ends={
        Property(name="activitydiagram_InputValue58", type=activitydiagram_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Input", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerCalculationExpression)
gen_activitydiagram_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_ControlToken_Token = Generalization(general=Token, specific=activitydiagram_ControlToken)
gen_activitydiagram_ForkedToken_Token = Generalization(general=Token, specific=activitydiagram_ForkedToken)
gen_activitydiagram_SendSignalAction_Action = Generalization(general=Action, specific=activitydiagram_SendSignalAction)
gen_activitydiagram_AcceptEventAction_Action = Generalization(general=Action, specific=activitydiagram_AcceptEventAction)
gen_activitydiagram_Signal_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Signal)
gen_activitydiagram_SignalEvent_Signal = Generalization(general=Signal, specific=activitydiagram_SignalEvent)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_Trace, activitydiagram_Signal, activitydiagram_Activity, NamedElement, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlNode, ActivityNode, activitydiagram_ExecutableNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_Expression, activitydiagram_NamedElement, activitydiagram_InitialNode, ControlNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_ForkNode, activitydiagram_Token, activitydiagram_Offer, activitydiagram_IntegerValue, activitydiagram_IntegerExpression, Expression, activitydiagram_BooleanExpression, activitydiagram_IntegerCalculationExpression, IntegerExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_JoinNode, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_Value, activitydiagram_IntegerVariable, Variable, activitydiagram_BooleanValue, Value, activitydiagram_BooleanBinaryExpression, activitydiagram_BooleanUnaryExpression, BooleanExpression, activitydiagram_ControlToken, Token, activitydiagram_ForkedToken, activitydiagram_SendSignalAction, activitydiagram_AcceptEventAction, activitydiagram_SignalEvent, Signal, activitydiagram_InputValue, activitydiagram_Input, IntegerCalculationOperator, BooleanUnaryOperator, BooleanBinaryOperator, IntegerComparisonOperator},
    associations={nodes0, edges1, locals2, inputs4, trace7, signals9, outgoing11, guard22, expressions23, incoming12, activity14, heldTokens15, source16, target18, offers20, operand229, operand130, assignee33, assignee35, assignee37, initialValue24, currentValue26, operand39, operand141, operand243, baseToken59, signal61, trigger63, offeredTokens46, holder48, executedNodes50, value52, variable54, inputValues57},
    generalizations={gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerCalculationExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_IntegerExpression, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_ControlToken_Token, gen_activitydiagram_ForkedToken_Token, gen_activitydiagram_SendSignalAction_Action, gen_activitydiagram_AcceptEventAction_Action, gen_activitydiagram_Signal_NamedElement, gen_activitydiagram_SignalEvent_Signal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)