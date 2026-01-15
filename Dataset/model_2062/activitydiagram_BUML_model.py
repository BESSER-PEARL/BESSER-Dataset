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
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable", is_abstract=True)
activitydiagram_Signal = Class(name="activitydiagram::Signal")
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode", is_abstract=True)
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
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_Value = Class(name="activitydiagram::Value", is_abstract=True)
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable")
Variable = Class(name="Variable")
activitydiagram_Expression = Class(name="activitydiagram::Expression", is_abstract=True)
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
activitydiagram_NamedElement = Class(name="activitydiagram::NamedElement", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_IntegerExpression = Class(name="activitydiagram::IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_BooleanExpression = Class(name="activitydiagram::BooleanExpression", is_abstract=True)
activitydiagram_IntegerCalculationExpression = Class(name="activitydiagram::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")
activitydiagram_Input = Class(name="activitydiagram::Input")
activitydiagram_SendSignalAction = Class(name="activitydiagram::SendSignalAction")
activitydiagram_AcceptEventAction = Class(name="activitydiagram::AcceptEventAction")
activitydiagram_SignalEvent = Class(name="activitydiagram::SignalEvent")
Signal = Class(name="Signal")
activitydiagram_InputValue = Class(name="activitydiagram::InputValue")

# activitydiagram_Activity class attributes and methods

# NamedElement class attributes and methods

# activitydiagram_ActivityEdge class attributes and methods

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=StringType)
activitydiagram_Variable.attributes={activitydiagram_Variable_name}

# activitydiagram_Signal class attributes and methods

# activitydiagram_ActivityNode class attributes and methods

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods

# Action class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods

# activitydiagram_MergeNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods

# Variable class attributes and methods

# activitydiagram_Expression class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}

# activitydiagram_InitialNode class attributes and methods

# ControlNode class attributes and methods

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

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}

# activitydiagram_Input class attributes and methods

# activitydiagram_SendSignalAction class attributes and methods

# activitydiagram_AcceptEventAction class attributes and methods

# activitydiagram_SignalEvent class attributes and methods

# Signal class attributes and methods

# activitydiagram_InputValue class attributes and methods

# Relationships
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
signals8: BinaryAssociation = BinaryAssociation(
    name="signals8",
    ends={
        Property(name="activitydiagram_Signal", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Activity9", type=activitydiagram_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="1", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="24", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard25: BinaryAssociation = BinaryAssociation(
    name="guard25",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
activity16: BinaryAssociation = BinaryAssociation(
    name="activity16",
    ends={
        Property(name="18", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="21", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
initialValue27: BinaryAssociation = BinaryAssociation(
    name="initialValue27",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable28", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions26: BinaryAssociation = BinaryAssociation(
    name="expressions26",
    ends={
        Property(name="activitydiagram_Expression", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
assignee37: BinaryAssociation = BinaryAssociation(
    name="assignee37",
    ends={
        Property(name="activitydiagram_BooleanVariable38", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
variable48: BinaryAssociation = BinaryAssociation(
    name="variable48",
    ends={
        Property(name="activitydiagram_Variable50", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue49", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues51: BinaryAssociation = BinaryAssociation(
    name="inputValues51",
    ends={
        Property(name="activitydiagram_InputValue52", type=activitydiagram_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Input", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal53: BinaryAssociation = BinaryAssociation(
    name="signal53",
    ends={
        Property(name="activitydiagram_Signal54", type=activitydiagram_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_SendSignalAction", type=activitydiagram_Signal, multiplicity=Multiplicity(0, 1))
    }
)
trigger55: BinaryAssociation = BinaryAssociation(
    name="trigger55",
    ends={
        Property(name="activitydiagram_SignalEvent", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction", type=activitydiagram_SignalEvent, multiplicity=Multiplicity(0, 1))
    }
)
value46: BinaryAssociation = BinaryAssociation(
    name="value46",
    ends={
        Property(name="activitydiagram_Value47", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue", type=activitydiagram_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerCalculationExpression)
gen_activitydiagram_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_SendSignalAction_Action = Generalization(general=Action, specific=activitydiagram_SendSignalAction)
gen_activitydiagram_AcceptEventAction_Action = Generalization(general=Action, specific=activitydiagram_AcceptEventAction)
gen_activitydiagram_Signal_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Signal)
gen_activitydiagram_SignalEvent_Signal = Generalization(general=Signal, specific=activitydiagram_SignalEvent)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedElement, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_Signal, activitydiagram_ActivityNode, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlNode, ActivityNode, activitydiagram_ExecutableNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_Value, activitydiagram_IntegerVariable, Variable, activitydiagram_Expression, activitydiagram_BooleanValue, Value, activitydiagram_NamedElement, activitydiagram_InitialNode, ControlNode, activitydiagram_IntegerExpression, Expression, activitydiagram_BooleanExpression, activitydiagram_IntegerCalculationExpression, IntegerExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_IntegerValue, activitydiagram_BooleanUnaryExpression, BooleanExpression, activitydiagram_BooleanBinaryExpression, activitydiagram_Input, activitydiagram_SendSignalAction, activitydiagram_AcceptEventAction, activitydiagram_SignalEvent, Signal, activitydiagram_InputValue, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={edges2, locals3, inputs5, signals8, outgoing10, incoming13, nodes0, target22, guard25, activity16, source19, initialValue27, expressions26, operand229, operand130, assignee33, assignee35, operand39, operand141, operand243, assignee37, variable48, inputValues51, signal53, trigger55, value46},
    generalizations={gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerCalculationExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_IntegerExpression, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_SendSignalAction_Action, gen_activitydiagram_AcceptEventAction_Action, gen_activitydiagram_Signal_NamedElement, gen_activitydiagram_SignalEvent_Signal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)