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
activitydiagram_NamedElement = Class(name="activitydiagram::NamedElement", is_abstract=True)
activitydiagram_Activity = Class(name="activitydiagram::Activity")
NamedElement = Class(name="NamedElement")
activitydiagram_Event = Class(name="activitydiagram::Event")
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable", is_abstract=True)
activitydiagram_OpaqueAction = Class(name="activitydiagram::OpaqueAction")
Action = Class(name="Action")
activitydiagram_VariableAssignment = Class(name="activitydiagram::VariableAssignment", is_abstract=True)
activitydiagram_AcceptEventAction = Class(name="activitydiagram::AcceptEventAction")
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable")
activitydiagram_Action = Class(name="activitydiagram::Action", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
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
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_IntegerBinaryExpression = Class(name="activitydiagram::IntegerBinaryExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_IntegerVariableAssignment = Class(name="activitydiagram::IntegerVariableAssignment")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")
activitydiagram_BooleanVariableAssignment = Class(name="activitydiagram::BooleanVariableAssignment")
VariableAssignment = Class(name="VariableAssignment")

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}

# activitydiagram_Activity class attributes and methods

# NamedElement class attributes and methods

# activitydiagram_Event class attributes and methods

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}

# activitydiagram_ActivityEdge class attributes and methods

# activitydiagram_Variable class attributes and methods
activitydiagram_Variable_name: Property = Property(name="name", type=StringType)
activitydiagram_Variable.attributes={activitydiagram_Variable_name}

# activitydiagram_OpaqueAction class attributes and methods

# Action class attributes and methods

# activitydiagram_VariableAssignment class attributes and methods

# activitydiagram_AcceptEventAction class attributes and methods

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods
activitydiagram_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
activitydiagram_BooleanVariable.attributes={activitydiagram_BooleanVariable_initialValue}

# activitydiagram_Action class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_MergeNode class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# activitydiagram_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# FinalNode class attributes and methods

# activitydiagram_FlowFinalNode class attributes and methods

# activitydiagram_Expression class attributes and methods

# Expression class attributes and methods

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerExpression class attributes and methods

# activitydiagram_BooleanExpression class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods
activitydiagram_IntegerVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
activitydiagram_IntegerVariable.attributes={activitydiagram_IntegerVariable_initialValue}

# Variable class attributes and methods

# IntegerExpression class attributes and methods

# BooleanExpression class attributes and methods

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_IntegerBinaryExpression class attributes and methods
activitydiagram_IntegerBinaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerBinaryExpression.attributes={activitydiagram_IntegerBinaryExpression_operator}

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}

# activitydiagram_IntegerVariableAssignment class attributes and methods

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}

# activitydiagram_BooleanVariableAssignment class attributes and methods

# VariableAssignment class attributes and methods

# Relationships
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
assignments18: BinaryAssociation = BinaryAssociation(
    name="assignments18",
    ends={
        Property(name="activitydiagram_VariableAssignment", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_VariableAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard11: BinaryAssociation = BinaryAssociation(
    name="guard11",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
activity12: BinaryAssociation = BinaryAssociation(
    name="activity12",
    ends={
        Property(name="Activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
incoming13: BinaryAssociation = BinaryAssociation(
    name="incoming13",
    ends={
        Property(name="activitydiagram_ActivityEdge14", type=activitydiagram_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Action", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing15: BinaryAssociation = BinaryAssociation(
    name="outgoing15",
    ends={
        Property(name="activitydiagram_ActivityEdge17", type=activitydiagram_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Action16", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing31: BinaryAssociation = BinaryAssociation(
    name="outgoing31",
    ends={
        Property(name="activitydiagram_ActivityEdge33", type=activitydiagram_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_DecisionNode32", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming34: BinaryAssociation = BinaryAssociation(
    name="incoming34",
    ends={
        Property(name="activitydiagram_ActivityEdge35", type=activitydiagram_MergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_MergeNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
eventType19: BinaryAssociation = BinaryAssociation(
    name="eventType19",
    ends={
        Property(name="activitydiagram_Event20", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction", type=activitydiagram_Event, multiplicity=Multiplicity(1, 1))
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="activitydiagram_ActivityEdge23", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction22", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
outgoing24: BinaryAssociation = BinaryAssociation(
    name="outgoing24",
    ends={
        Property(name="activitydiagram_ActivityEdge26", type=activitydiagram_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_AcceptEventAction25", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing27: BinaryAssociation = BinaryAssociation(
    name="outgoing27",
    ends={
        Property(name="activitydiagram_ActivityEdge28", type=activitydiagram_InitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InitialNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming29: BinaryAssociation = BinaryAssociation(
    name="incoming29",
    ends={
        Property(name="activitydiagram_ActivityEdge30", type=activitydiagram_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_DecisionNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming49: BinaryAssociation = BinaryAssociation(
    name="incoming49",
    ends={
        Property(name="activitydiagram_ActivityEdge50", type=activitydiagram_FinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_FinalNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing36: BinaryAssociation = BinaryAssociation(
    name="outgoing36",
    ends={
        Property(name="activitydiagram_ActivityEdge38", type=activitydiagram_MergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_MergeNode37", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
incoming39: BinaryAssociation = BinaryAssociation(
    name="incoming39",
    ends={
        Property(name="activitydiagram_ActivityEdge40", type=activitydiagram_ForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
outgoing41: BinaryAssociation = BinaryAssociation(
    name="outgoing41",
    ends={
        Property(name="activitydiagram_ActivityEdge43", type=activitydiagram_ForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkNode42", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming44: BinaryAssociation = BinaryAssociation(
    name="incoming44",
    ends={
        Property(name="activitydiagram_ActivityEdge45", type=activitydiagram_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_JoinNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing46: BinaryAssociation = BinaryAssociation(
    name="outgoing46",
    ends={
        Property(name="activitydiagram_ActivityEdge48", type=activitydiagram_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_JoinNode47", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
operand257: BinaryAssociation = BinaryAssociation(
    name="operand257",
    ends={
        Property(name="activitydiagram_IntegerExpression59", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression58", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand60: BinaryAssociation = BinaryAssociation(
    name="operand60",
    ends={
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
operand151: BinaryAssociation = BinaryAssociation(
    name="operand151",
    ends={
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerBinaryExpression", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand252: BinaryAssociation = BinaryAssociation(
    name="operand252",
    ends={
        Property(name="activitydiagram_IntegerExpression54", type=activitydiagram_IntegerBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerBinaryExpression53", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand155: BinaryAssociation = BinaryAssociation(
    name="operand155",
    ends={
        Property(name="activitydiagram_IntegerExpression56", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
expression68: BinaryAssociation = BinaryAssociation(
    name="expression68",
    ends={
        Property(name="activitydiagram_BooleanVariableAssignment69", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="activitydiagram_BooleanExpression70", type=activitydiagram_BooleanVariableAssignment, multiplicity=Multiplicity(1, 1))
    }
)
operand161: BinaryAssociation = BinaryAssociation(
    name="operand161",
    ends={
        Property(name="activitydiagram_BooleanExpression62", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
operand263: BinaryAssociation = BinaryAssociation(
    name="operand263",
    ends={
        Property(name="activitydiagram_BooleanExpression65", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression64", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignee66: BinaryAssociation = BinaryAssociation(
    name="assignee66",
    ends={
        Property(name="activitydiagram_BooleanVariable67", type=activitydiagram_BooleanVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanVariableAssignment", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee71: BinaryAssociation = BinaryAssociation(
    name="assignee71",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerVariableAssignment", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
expression72: BinaryAssociation = BinaryAssociation(
    name="expression72",
    ends={
        Property(name="activitydiagram_IntegerExpression74", type=activitydiagram_IntegerVariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerVariableAssignment73", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_Event_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Event)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_AcceptEventAction_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_AcceptEventAction)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_Action_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_Action)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_BooleanValue_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanValue)
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
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerValue_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerBinaryExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerBinaryExpression)
gen_activitydiagram_IntegerBinaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerBinaryExpression)
gen_activitydiagram_IntegerComparisonExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_IntegerVariableAssignment_VariableAssignment = Generalization(general=VariableAssignment, specific=activitydiagram_IntegerVariableAssignment)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)
gen_activitydiagram_BooleanVariableAssignment_VariableAssignment = Generalization(general=VariableAssignment, specific=activitydiagram_BooleanVariableAssignment)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_NamedElement, activitydiagram_Activity, NamedElement, activitydiagram_Event, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_OpaqueAction, Action, activitydiagram_VariableAssignment, activitydiagram_AcceptEventAction, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_Action, ActivityNode, activitydiagram_MergeNode, activitydiagram_ControlNode, activitydiagram_InitialNode, ControlNode, activitydiagram_DecisionNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_BooleanValue, Value, FinalNode, activitydiagram_FlowFinalNode, activitydiagram_Expression, Expression, activitydiagram_Value, activitydiagram_IntegerExpression, activitydiagram_BooleanExpression, activitydiagram_IntegerVariable, Variable, IntegerExpression, BooleanExpression, activitydiagram_BooleanUnaryExpression, activitydiagram_IntegerValue, activitydiagram_IntegerBinaryExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_IntegerVariableAssignment, activitydiagram_BooleanBinaryExpression, activitydiagram_BooleanVariableAssignment, VariableAssignment, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={source6, target8, events0, nodes1, edges2, locals4, assignments18, guard11, activity12, incoming13, outgoing15, outgoing31, incoming34, eventType19, incoming21, outgoing24, outgoing27, incoming29, incoming49, outgoing36, incoming39, outgoing41, incoming44, outgoing46, operand257, operand60, operand151, operand252, operand155, expression68, operand161, operand263, assignee66, assignee71, expression72},
    generalizations={gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_Event_NamedElement, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_AcceptEventAction_ActivityNode, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_Action_ActivityNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_BooleanValue_BooleanExpression, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_FlowFinalNode_FinalNode, gen_activitydiagram_Variable_Expression, gen_activitydiagram_Value_Expression, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_IntegerVariable_IntegerExpression, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_BooleanVariable_BooleanExpression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerValue_IntegerExpression, gen_activitydiagram_IntegerBinaryExpression_Expression, gen_activitydiagram_IntegerBinaryExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_BooleanExpression, gen_activitydiagram_IntegerVariableAssignment_VariableAssignment, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression, gen_activitydiagram_BooleanVariableAssignment_VariableAssignment},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)