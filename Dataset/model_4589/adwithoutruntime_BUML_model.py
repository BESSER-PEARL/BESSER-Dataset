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
adwithoutruntime_ActivityNode = Class(name="adwithoutruntime_ActivityNode", is_abstract=True)
adwithoutruntime_ActivityEdge = Class(name="adwithoutruntime_ActivityEdge", is_abstract=True)
adwithoutruntime_Variable = Class(name="adwithoutruntime_Variable", is_abstract=True)
adwithoutruntime_ControlFlow = Class(name="adwithoutruntime_ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
adwithoutruntime_BooleanVariable = Class(name="adwithoutruntime_BooleanVariable")
adwithoutruntime_ControlNode = Class(name="adwithoutruntime_ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
adwithoutruntime_ExecutableNode = Class(name="adwithoutruntime_ExecutableNode", is_abstract=True)
adwithoutruntime_Action = Class(name="adwithoutruntime_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
adwithoutruntime_Activity = Class(name="adwithoutruntime_Activity")
NamedElement = Class(name="NamedElement")
adwithoutruntime_NamedElement = Class(name="adwithoutruntime_NamedElement", is_abstract=True)
adwithoutruntime_InitialNode = Class(name="adwithoutruntime_InitialNode")
ControlNode = Class(name="ControlNode")
adwithoutruntime_FinalNode = Class(name="adwithoutruntime_FinalNode", is_abstract=True)
adwithoutruntime_ActivityFinalNode = Class(name="adwithoutruntime_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
adwithoutruntime_ForkNode = Class(name="adwithoutruntime_ForkNode")
adwithoutruntime_JoinNode = Class(name="adwithoutruntime_JoinNode")
adwithoutruntime_MergeNode = Class(name="adwithoutruntime_MergeNode")
adwithoutruntime_DecisionNode = Class(name="adwithoutruntime_DecisionNode")
adwithoutruntime_Value = Class(name="adwithoutruntime_Value", is_abstract=True)
adwithoutruntime_IntegerVariable = Class(name="adwithoutruntime_IntegerVariable")
Variable = Class(name="Variable")
adwithoutruntime_BooleanValue = Class(name="adwithoutruntime_BooleanValue")
Value = Class(name="Value")
adwithoutruntime_IntegerValue = Class(name="adwithoutruntime_IntegerValue")
adwithoutruntime_IntegerExpression = Class(name="adwithoutruntime_IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
adwithoutruntime_BooleanExpression = Class(name="adwithoutruntime_BooleanExpression", is_abstract=True)
adwithoutruntime_OpaqueAction = Class(name="adwithoutruntime_OpaqueAction")
Action = Class(name="Action")
adwithoutruntime_Expression = Class(name="adwithoutruntime_Expression", is_abstract=True)
adwithoutruntime_IntegerComparisonExpression = Class(name="adwithoutruntime_IntegerComparisonExpression")
adwithoutruntime_BooleanUnaryExpression = Class(name="adwithoutruntime_BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
adwithoutruntime_BooleanBinaryExpression = Class(name="adwithoutruntime_BooleanBinaryExpression")
adwithoutruntime_IntegerCalculationExpression = Class(name="adwithoutruntime_IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")

# adwithoutruntime_ActivityNode class attributes and methods

# adwithoutruntime_ActivityEdge class attributes and methods

# adwithoutruntime_Variable class attributes and methods
adwithoutruntime_Variable_name: Property = Property(name="name", type=StringType)
adwithoutruntime_Variable.attributes={adwithoutruntime_Variable_name}

# adwithoutruntime_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# adwithoutruntime_BooleanVariable class attributes and methods

# adwithoutruntime_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# adwithoutruntime_ExecutableNode class attributes and methods

# adwithoutruntime_Action class attributes and methods

# ExecutableNode class attributes and methods

# adwithoutruntime_Activity class attributes and methods

# NamedElement class attributes and methods

# adwithoutruntime_NamedElement class attributes and methods
adwithoutruntime_NamedElement_name: Property = Property(name="name", type=StringType)
adwithoutruntime_NamedElement.attributes={adwithoutruntime_NamedElement_name}

# adwithoutruntime_InitialNode class attributes and methods

# ControlNode class attributes and methods

# adwithoutruntime_FinalNode class attributes and methods

# adwithoutruntime_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# adwithoutruntime_ForkNode class attributes and methods

# adwithoutruntime_JoinNode class attributes and methods

# adwithoutruntime_MergeNode class attributes and methods

# adwithoutruntime_DecisionNode class attributes and methods

# adwithoutruntime_Value class attributes and methods

# adwithoutruntime_IntegerVariable class attributes and methods

# Variable class attributes and methods

# adwithoutruntime_BooleanValue class attributes and methods
adwithoutruntime_BooleanValue_value: Property = Property(name="value", type=BooleanType)
adwithoutruntime_BooleanValue.attributes={adwithoutruntime_BooleanValue_value}

# Value class attributes and methods

# adwithoutruntime_IntegerValue class attributes and methods
adwithoutruntime_IntegerValue_value: Property = Property(name="value", type=IntegerType)
adwithoutruntime_IntegerValue.attributes={adwithoutruntime_IntegerValue_value}

# adwithoutruntime_IntegerExpression class attributes and methods

# Expression class attributes and methods

# adwithoutruntime_BooleanExpression class attributes and methods

# adwithoutruntime_OpaqueAction class attributes and methods

# Action class attributes and methods

# adwithoutruntime_Expression class attributes and methods

# adwithoutruntime_IntegerComparisonExpression class attributes and methods
adwithoutruntime_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_IntegerComparisonExpression.attributes={adwithoutruntime_IntegerComparisonExpression_operator}

# adwithoutruntime_BooleanUnaryExpression class attributes and methods
adwithoutruntime_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_BooleanUnaryExpression.attributes={adwithoutruntime_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# adwithoutruntime_BooleanBinaryExpression class attributes and methods
adwithoutruntime_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_BooleanBinaryExpression.attributes={adwithoutruntime_BooleanBinaryExpression_operator}

# adwithoutruntime_IntegerCalculationExpression class attributes and methods
adwithoutruntime_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_IntegerCalculationExpression.attributes={adwithoutruntime_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="ActivityNode", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="adwithoutruntime_ActivityEdge", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Activity", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals2: BinaryAssociation = BinaryAssociation(
    name="locals2",
    ends={
        Property(name="adwithoutruntime_Variable", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Activity3", type=adwithoutruntime_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs4: BinaryAssociation = BinaryAssociation(
    name="inputs4",
    ends={
        Property(name="adwithoutruntime_Variable6", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Activity5", type=adwithoutruntime_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="ActivityEdge", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="ActivityEdge9", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity10: BinaryAssociation = BinaryAssociation(
    name="activity10",
    ends={
        Property(name="Activity", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="ActivityNode12", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="ActivityNode14", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard15: BinaryAssociation = BinaryAssociation(
    name="guard15",
    ends={
        Property(name="adwithoutruntime_BooleanVariable", type=adwithoutruntime_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_ControlFlow", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
initialValue17: BinaryAssociation = BinaryAssociation(
    name="initialValue17",
    ends={
        Property(name="adwithoutruntime_Value", type=adwithoutruntime_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Variable18", type=adwithoutruntime_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue19: BinaryAssociation = BinaryAssociation(
    name="currentValue19",
    ends={
        Property(name="adwithoutruntime_Value21", type=adwithoutruntime_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Variable20", type=adwithoutruntime_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand222: BinaryAssociation = BinaryAssociation(
    name="operand222",
    ends={
        Property(name="adwithoutruntime_IntegerVariable", type=adwithoutruntime_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerExpression", type=adwithoutruntime_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand123: BinaryAssociation = BinaryAssociation(
    name="operand123",
    ends={
        Property(name="adwithoutruntime_IntegerVariable25", type=adwithoutruntime_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerExpression24", type=adwithoutruntime_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee26: BinaryAssociation = BinaryAssociation(
    name="assignee26",
    ends={
        Property(name="adwithoutruntime_BooleanVariable27", type=adwithoutruntime_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
expressions16: BinaryAssociation = BinaryAssociation(
    name="expressions16",
    ends={
        Property(name="adwithoutruntime_Expression", type=adwithoutruntime_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_OpaqueAction", type=adwithoutruntime_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignee30: BinaryAssociation = BinaryAssociation(
    name="assignee30",
    ends={
        Property(name="adwithoutruntime_BooleanVariable31", type=adwithoutruntime_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerComparisonExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand32: BinaryAssociation = BinaryAssociation(
    name="operand32",
    ends={
        Property(name="adwithoutruntime_BooleanVariable33", type=adwithoutruntime_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanUnaryExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand134: BinaryAssociation = BinaryAssociation(
    name="operand134",
    ends={
        Property(name="adwithoutruntime_BooleanVariable35", type=adwithoutruntime_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanBinaryExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand236: BinaryAssociation = BinaryAssociation(
    name="operand236",
    ends={
        Property(name="adwithoutruntime_BooleanVariable38", type=adwithoutruntime_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanBinaryExpression37", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee28: BinaryAssociation = BinaryAssociation(
    name="assignee28",
    ends={
        Property(name="adwithoutruntime_IntegerVariable29", type=adwithoutruntime_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerCalculationExpression", type=adwithoutruntime_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_adwithoutruntime_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=adwithoutruntime_ActivityNode)
gen_adwithoutruntime_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=adwithoutruntime_ActivityEdge)
gen_adwithoutruntime_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=adwithoutruntime_ControlFlow)
gen_adwithoutruntime_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=adwithoutruntime_ControlNode)
gen_adwithoutruntime_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=adwithoutruntime_ExecutableNode)
gen_adwithoutruntime_Activity_NamedElement = Generalization(general=NamedElement, specific=adwithoutruntime_Activity)
gen_adwithoutruntime_InitialNode_ControlNode = Generalization(general=ControlNode, specific=adwithoutruntime_InitialNode)
gen_adwithoutruntime_FinalNode_ControlNode = Generalization(general=ControlNode, specific=adwithoutruntime_FinalNode)
gen_adwithoutruntime_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=adwithoutruntime_ActivityFinalNode)
gen_adwithoutruntime_ForkNode_ControlNode = Generalization(general=ControlNode, specific=adwithoutruntime_ForkNode)
gen_adwithoutruntime_JoinNode_ControlNode = Generalization(general=ControlNode, specific=adwithoutruntime_JoinNode)
gen_adwithoutruntime_MergeNode_ControlNode = Generalization(general=ControlNode, specific=adwithoutruntime_MergeNode)
gen_adwithoutruntime_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=adwithoutruntime_DecisionNode)
gen_adwithoutruntime_IntegerVariable_Variable = Generalization(general=Variable, specific=adwithoutruntime_IntegerVariable)
gen_adwithoutruntime_BooleanVariable_Variable = Generalization(general=Variable, specific=adwithoutruntime_BooleanVariable)
gen_adwithoutruntime_BooleanValue_Value = Generalization(general=Value, specific=adwithoutruntime_BooleanValue)
gen_adwithoutruntime_IntegerValue_Value = Generalization(general=Value, specific=adwithoutruntime_IntegerValue)
gen_adwithoutruntime_IntegerExpression_Expression = Generalization(general=Expression, specific=adwithoutruntime_IntegerExpression)
gen_adwithoutruntime_BooleanExpression_Expression = Generalization(general=Expression, specific=adwithoutruntime_BooleanExpression)
gen_adwithoutruntime_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=adwithoutruntime_Action)
gen_adwithoutruntime_OpaqueAction_Action = Generalization(general=Action, specific=adwithoutruntime_OpaqueAction)
gen_adwithoutruntime_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=adwithoutruntime_IntegerComparisonExpression)
gen_adwithoutruntime_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=adwithoutruntime_BooleanUnaryExpression)
gen_adwithoutruntime_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=adwithoutruntime_BooleanBinaryExpression)
gen_adwithoutruntime_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=adwithoutruntime_IntegerCalculationExpression)

# Domain Model
domain_model = DomainModel(
    name="adwithoutruntime",
    types={adwithoutruntime_ActivityNode, adwithoutruntime_ActivityEdge, adwithoutruntime_Variable, adwithoutruntime_ControlFlow, ActivityEdge, adwithoutruntime_BooleanVariable, adwithoutruntime_ControlNode, ActivityNode, adwithoutruntime_ExecutableNode, adwithoutruntime_Action, ExecutableNode, adwithoutruntime_Activity, NamedElement, adwithoutruntime_NamedElement, adwithoutruntime_InitialNode, ControlNode, adwithoutruntime_FinalNode, adwithoutruntime_ActivityFinalNode, FinalNode, adwithoutruntime_ForkNode, adwithoutruntime_JoinNode, adwithoutruntime_MergeNode, adwithoutruntime_DecisionNode, adwithoutruntime_Value, adwithoutruntime_IntegerVariable, Variable, adwithoutruntime_BooleanValue, Value, adwithoutruntime_IntegerValue, adwithoutruntime_IntegerExpression, Expression, adwithoutruntime_BooleanExpression, adwithoutruntime_OpaqueAction, Action, adwithoutruntime_Expression, adwithoutruntime_IntegerComparisonExpression, adwithoutruntime_BooleanUnaryExpression, BooleanExpression, adwithoutruntime_BooleanBinaryExpression, adwithoutruntime_IntegerCalculationExpression, IntegerExpression, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes0, edges1, locals2, inputs4, outgoing7, incoming8, activity10, source11, target13, guard15, initialValue17, currentValue19, operand222, operand123, assignee26, expressions16, assignee30, operand32, operand134, operand236, assignee28},
    generalizations={gen_adwithoutruntime_ActivityNode_NamedElement, gen_adwithoutruntime_ActivityEdge_NamedElement, gen_adwithoutruntime_ControlFlow_ActivityEdge, gen_adwithoutruntime_ControlNode_ActivityNode, gen_adwithoutruntime_ExecutableNode_ActivityNode, gen_adwithoutruntime_Activity_NamedElement, gen_adwithoutruntime_InitialNode_ControlNode, gen_adwithoutruntime_FinalNode_ControlNode, gen_adwithoutruntime_ActivityFinalNode_FinalNode, gen_adwithoutruntime_ForkNode_ControlNode, gen_adwithoutruntime_JoinNode_ControlNode, gen_adwithoutruntime_MergeNode_ControlNode, gen_adwithoutruntime_DecisionNode_ControlNode, gen_adwithoutruntime_IntegerVariable_Variable, gen_adwithoutruntime_BooleanVariable_Variable, gen_adwithoutruntime_BooleanValue_Value, gen_adwithoutruntime_IntegerValue_Value, gen_adwithoutruntime_IntegerExpression_Expression, gen_adwithoutruntime_BooleanExpression_Expression, gen_adwithoutruntime_Action_ExecutableNode, gen_adwithoutruntime_OpaqueAction_Action, gen_adwithoutruntime_IntegerComparisonExpression_IntegerExpression, gen_adwithoutruntime_BooleanUnaryExpression_BooleanExpression, gen_adwithoutruntime_BooleanBinaryExpression_BooleanExpression, gen_adwithoutruntime_IntegerCalculationExpression_IntegerExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)