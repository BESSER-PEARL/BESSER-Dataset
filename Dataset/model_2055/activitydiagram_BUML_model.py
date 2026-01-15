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
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable", is_abstract=True)
activitydiagram_Token = Class(name="activitydiagram::Token", is_abstract=True)
activitydiagram_Trace = Class(name="activitydiagram::Trace")
activitydiagram_ExecutableNode = Class(name="activitydiagram::ExecutableNode", is_abstract=True)
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
activitydiagram_Offer = Class(name="activitydiagram::Offer")
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable")
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable")
Variable = Class(name="Variable")
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_IntegerExpression = Class(name="activitydiagram::IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_Value = Class(name="activitydiagram::Value", is_abstract=True)
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_BooleanExpression = Class(name="activitydiagram::BooleanExpression", is_abstract=True)
activitydiagram_IntegerCalculationExpression = Class(name="activitydiagram::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")
activitydiagram_Input = Class(name="activitydiagram::Input")
activitydiagram_ControlToken = Class(name="activitydiagram::ControlToken")
Token = Class(name="Token")
activitydiagram_ForkedToken = Class(name="activitydiagram::ForkedToken")
activitydiagram_InputValue = Class(name="activitydiagram::InputValue")

# activitydiagram_Activity class attributes and methods

# NamedElement class attributes and methods

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}

# activitydiagram_ActivityEdge class attributes and methods

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=StringType)
activitydiagram_Variable.attributes={activitydiagram_Variable_name}

# activitydiagram_Token class attributes and methods

# activitydiagram_Trace class attributes and methods

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods

# Action class attributes and methods

# activitydiagram_Expression class attributes and methods

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}

# activitydiagram_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# activitydiagram_Offer class attributes and methods

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods

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

# activitydiagram_ForkNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods

# activitydiagram_MergeNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}

# activitydiagram_BooleanExpression class attributes and methods

# activitydiagram_IntegerCalculationExpression class attributes and methods
activitydiagram_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerCalculationExpression.attributes={activitydiagram_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}

# activitydiagram_Input class attributes and methods

# activitydiagram_ControlToken class attributes and methods

# Token class attributes and methods

# activitydiagram_ForkedToken class attributes and methods
activitydiagram_ForkedToken_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
activitydiagram_ForkedToken.attributes={activitydiagram_ForkedToken_remainingOffersCount}

# activitydiagram_InputValue class attributes and methods

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
incoming10: BinaryAssociation = BinaryAssociation(
    name="incoming10",
    ends={
        Property(name="ActivityEdge11", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity12: BinaryAssociation = BinaryAssociation(
    name="activity12",
    ends={
        Property(name="Activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
heldTokens13: BinaryAssociation = BinaryAssociation(
    name="heldTokens13",
    ends={
        Property(name="Token", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="holder", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="ActivityNode15", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
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
outgoing9: BinaryAssociation = BinaryAssociation(
    name="outgoing9",
    ends={
        Property(name="ActivityEdge", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
expressions21: BinaryAssociation = BinaryAssociation(
    name="expressions21",
    ends={
        Property(name="activitydiagram_Expression", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="ActivityNode17", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offers18: BinaryAssociation = BinaryAssociation(
    name="offers18",
    ends={
        Property(name="activitydiagram_Offer", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge19", type=activitydiagram_Offer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard20: BinaryAssociation = BinaryAssociation(
    name="guard20",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
currentValue24: BinaryAssociation = BinaryAssociation(
    name="currentValue24",
    ends={
        Property(name="activitydiagram_Value26", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable25", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue22: BinaryAssociation = BinaryAssociation(
    name="initialValue22",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable23", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignee35: BinaryAssociation = BinaryAssociation(
    name="assignee35",
    ends={
        Property(name="activitydiagram_BooleanVariable36", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand227: BinaryAssociation = BinaryAssociation(
    name="operand227",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand128: BinaryAssociation = BinaryAssociation(
    name="operand128",
    ends={
        Property(name="activitydiagram_IntegerVariable30", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression29", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee31: BinaryAssociation = BinaryAssociation(
    name="assignee31",
    ends={
        Property(name="activitydiagram_BooleanVariable32", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee33: BinaryAssociation = BinaryAssociation(
    name="assignee33",
    ends={
        Property(name="activitydiagram_IntegerVariable34", type=activitydiagram_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerCalculationExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand139: BinaryAssociation = BinaryAssociation(
    name="operand139",
    ends={
        Property(name="activitydiagram_BooleanVariable40", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand241: BinaryAssociation = BinaryAssociation(
    name="operand241",
    ends={
        Property(name="activitydiagram_BooleanVariable43", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression42", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
offeredTokens44: BinaryAssociation = BinaryAssociation(
    name="offeredTokens44",
    ends={
        Property(name="activitydiagram_Token", type=activitydiagram_Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Offer45", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999))
    }
)
operand37: BinaryAssociation = BinaryAssociation(
    name="operand37",
    ends={
        Property(name="activitydiagram_BooleanVariable38", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
variable52: BinaryAssociation = BinaryAssociation(
    name="variable52",
    ends={
        Property(name="activitydiagram_Variable54", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue53", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues55: BinaryAssociation = BinaryAssociation(
    name="inputValues55",
    ends={
        Property(name="activitydiagram_InputValue56", type=activitydiagram_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Input", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseToken57: BinaryAssociation = BinaryAssociation(
    name="baseToken57",
    ends={
        Property(name="activitydiagram_Token58", type=activitydiagram_ForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkedToken", type=activitydiagram_Token, multiplicity=Multiplicity(1, 1))
    }
)
holder46: BinaryAssociation = BinaryAssociation(
    name="holder46",
    ends={
        Property(name="ActivityNode47", type=activitydiagram_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="heldTokens", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
executedNodes48: BinaryAssociation = BinaryAssociation(
    name="executedNodes48",
    ends={
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Trace49", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
value50: BinaryAssociation = BinaryAssociation(
    name="value50",
    ends={
        Property(name="activitydiagram_Value51", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue", type=activitydiagram_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerCalculationExpression)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_ControlToken_Token = Generalization(general=Token, specific=activitydiagram_ControlToken)
gen_activitydiagram_ForkedToken_Token = Generalization(general=Token, specific=activitydiagram_ForkedToken)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedElement, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_Token, activitydiagram_Trace, activitydiagram_ExecutableNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_Expression, activitydiagram_NamedElement, activitydiagram_InitialNode, ControlNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_Offer, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlNode, ActivityNode, activitydiagram_IntegerVariable, Variable, activitydiagram_BooleanValue, Value, activitydiagram_IntegerValue, activitydiagram_IntegerExpression, Expression, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_Value, activitydiagram_IntegerComparisonExpression, activitydiagram_BooleanExpression, activitydiagram_IntegerCalculationExpression, IntegerExpression, activitydiagram_BooleanUnaryExpression, BooleanExpression, activitydiagram_BooleanBinaryExpression, activitydiagram_Input, activitydiagram_ControlToken, Token, activitydiagram_ForkedToken, activitydiagram_InputValue, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes0, edges1, locals2, incoming10, activity12, heldTokens13, source14, inputs4, trace7, outgoing9, expressions21, target16, offers18, guard20, currentValue24, initialValue22, assignee35, operand227, operand128, assignee31, assignee33, operand139, operand241, offeredTokens44, operand37, variable52, inputValues55, baseToken57, holder46, executedNodes48, value50},
    generalizations={gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_IntegerComparisonExpression_IntegerExpression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerCalculationExpression_IntegerExpression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_ControlToken_Token, gen_activitydiagram_ForkedToken_Token},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)