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

IntegerComparisionOperator: Enumeration = Enumeration(
    name="IntegerComparisionOperator",
    literals={
            EnumerationLiteral(name="SMALLER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="SMALLER")
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
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_ExecutableNode = Class(name="activitydiagram::ExecutableNode", is_abstract=True)
activitydiagram_Action = Class(name="activitydiagram::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
activitydiagram_OpaqueAction = Class(name="activitydiagram::OpaqueAction")
Action = Class(name="Action")
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable")
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_Expression = Class(name="activitydiagram::Expression", is_abstract=True)
activitydiagram_NamedElement = Class(name="activitydiagram::NamedElement", is_abstract=True)
activitydiagram_Value = Class(name="activitydiagram::Value", is_abstract=True)
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable")
Variable = Class(name="Variable")
activitydiagram_StringVariable = Class(name="activitydiagram::StringVariable")
activitydiagram_StringValue = Class(name="activitydiagram::StringValue")
Value = Class(name="Value")
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_BooleanExpression = Class(name="activitydiagram::BooleanExpression", is_abstract=True)
activitydiagram_IntegerCalculationExpression = Class(name="activitydiagram::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
activitydiagram_IntegerComparisonExpression = Class(name="activitydiagram::IntegerComparisonExpression")
activitydiagram_IntegerExpression = Class(name="activitydiagram::IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
activitydiagram_BooleanUnaryExpression = Class(name="activitydiagram::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
activitydiagram_BooleanBinaryExpression = Class(name="activitydiagram::BooleanBinaryExpression")

# activitydiagram_Activity class attributes and methods

# NamedElement class attributes and methods

# activitydiagram_ActivityNode class attributes and methods

# activitydiagram_ActivityEdge class attributes and methods

# activitydiagram_Variable class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods

# Action class attributes and methods

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods

# activitydiagram_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods

# activitydiagram_Expression class attributes and methods

# activitydiagram_NamedElement class attributes and methods
activitydiagram_NamedElement_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedElement.attributes={activitydiagram_NamedElement_name}

# activitydiagram_Value class attributes and methods

# activitydiagram_IntegerVariable class attributes and methods

# Variable class attributes and methods

# activitydiagram_StringVariable class attributes and methods

# activitydiagram_StringValue class attributes and methods
activitydiagram_StringValue_value: Property = Property(name="value", type=StringType)
activitydiagram_StringValue.attributes={activitydiagram_StringValue_value}

# Value class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=IntegerType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_MergeNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods

# activitydiagram_BooleanExpression class attributes and methods

# activitydiagram_IntegerCalculationExpression class attributes and methods
activitydiagram_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerCalculationExpression.attributes={activitydiagram_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

# activitydiagram_IntegerComparisonExpression class attributes and methods
activitydiagram_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_IntegerComparisonExpression.attributes={activitydiagram_IntegerComparisonExpression_operator}

# activitydiagram_IntegerExpression class attributes and methods

# Expression class attributes and methods

# activitydiagram_BooleanUnaryExpression class attributes and methods
activitydiagram_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanUnaryExpression.attributes={activitydiagram_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# activitydiagram_BooleanBinaryExpression class attributes and methods
activitydiagram_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
activitydiagram_BooleanBinaryExpression.attributes={activitydiagram_BooleanBinaryExpression_operator}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="ActivityNode", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="ActivityEdge9", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity10: BinaryAssociation = BinaryAssociation(
    name="activity10",
    ends={
        Property(name="Activity", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="ActivityNode12", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="ActivityNode14", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
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
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="ActivityEdge", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
guard15: BinaryAssociation = BinaryAssociation(
    name="guard15",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
expressions16: BinaryAssociation = BinaryAssociation(
    name="expressions16",
    ends={
        Property(name="activitydiagram_Expression", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue17: BinaryAssociation = BinaryAssociation(
    name="initialValue17",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable18", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand120: BinaryAssociation = BinaryAssociation(
    name="operand120",
    ends={
        Property(name="activitydiagram_IntegerVariable22", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression21", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee23: BinaryAssociation = BinaryAssociation(
    name="assignee23",
    ends={
        Property(name="activitydiagram_BooleanVariable24", type=activitydiagram_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee25: BinaryAssociation = BinaryAssociation(
    name="assignee25",
    ends={
        Property(name="activitydiagram_IntegerVariable26", type=activitydiagram_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerCalculationExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee27: BinaryAssociation = BinaryAssociation(
    name="assignee27",
    ends={
        Property(name="activitydiagram_BooleanVariable28", type=activitydiagram_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerComparisonExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand219: BinaryAssociation = BinaryAssociation(
    name="operand219",
    ends={
        Property(name="activitydiagram_IntegerVariable", type=activitydiagram_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_IntegerExpression", type=activitydiagram_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand29: BinaryAssociation = BinaryAssociation(
    name="operand29",
    ends={
        Property(name="activitydiagram_BooleanVariable30", type=activitydiagram_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanUnaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand131: BinaryAssociation = BinaryAssociation(
    name="operand131",
    ends={
        Property(name="activitydiagram_BooleanVariable32", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand233: BinaryAssociation = BinaryAssociation(
    name="operand233",
    ends={
        Property(name="activitydiagram_BooleanVariable35", type=activitydiagram_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_BooleanBinaryExpression34", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)
gen_activitydiagram_StringVariable_Variable = Generalization(general=Variable, specific=activitydiagram_StringVariable)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_StringValue_Value = Generalization(general=Value, specific=activitydiagram_StringValue)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_Variable_NamedElement = Generalization(general=NamedElement, specific=activitydiagram_Variable)
gen_activitydiagram_BooleanExpression_Expression = Generalization(general=Expression, specific=activitydiagram_BooleanExpression)
gen_activitydiagram_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerCalculationExpression)
gen_activitydiagram_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=activitydiagram_IntegerComparisonExpression)
gen_activitydiagram_IntegerExpression_Expression = Generalization(general=Expression, specific=activitydiagram_IntegerExpression)
gen_activitydiagram_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanUnaryExpression)
gen_activitydiagram_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=activitydiagram_BooleanBinaryExpression)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedElement, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_ControlNode, ActivityNode, activitydiagram_ExecutableNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_InitialNode, ControlNode, activitydiagram_FinalNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_Expression, activitydiagram_NamedElement, activitydiagram_Value, activitydiagram_IntegerVariable, Variable, activitydiagram_StringVariable, activitydiagram_StringValue, Value, activitydiagram_BooleanValue, activitydiagram_IntegerValue, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_BooleanExpression, activitydiagram_IntegerCalculationExpression, IntegerExpression, activitydiagram_IntegerComparisonExpression, activitydiagram_IntegerExpression, Expression, activitydiagram_BooleanUnaryExpression, BooleanExpression, activitydiagram_BooleanBinaryExpression, IntegerCalculationOperator, IntegerComparisionOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes0, incoming8, activity10, source11, target13, edges1, locals2, inputs4, outgoing7, guard15, expressions16, initialValue17, operand120, assignee23, assignee25, assignee27, operand219, operand29, operand131, operand233},
    generalizations={gen_activitydiagram_Activity_NamedElement, gen_activitydiagram_ActivityEdge_NamedElement, gen_activitydiagram_ActivityNode_NamedElement, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_IntegerVariable_Variable, gen_activitydiagram_StringVariable_Variable, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_StringValue_Value, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_Variable_NamedElement, gen_activitydiagram_BooleanExpression_Expression, gen_activitydiagram_IntegerCalculationExpression_IntegerExpression, gen_activitydiagram_IntegerComparisonExpression_IntegerExpression, gen_activitydiagram_IntegerExpression_Expression, gen_activitydiagram_BooleanUnaryExpression_BooleanExpression, gen_activitydiagram_BooleanBinaryExpression_BooleanExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)