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
adwithoutruntime_Activity = Class(name="adwithoutruntime::Activity")
NamedElement = Class(name="NamedElement")
adwithoutruntime_ActivityNode = Class(name="adwithoutruntime::ActivityNode", is_abstract=True)
adwithoutruntime_ActivityEdge = Class(name="adwithoutruntime::ActivityEdge", is_abstract=True)
adwithoutruntime_Variable = Class(name="adwithoutruntime::Variable", is_abstract=True)
adwithoutruntime_OpaqueAction = Class(name="adwithoutruntime::OpaqueAction")
Action = Class(name="Action")
adwithoutruntime_Expression = Class(name="adwithoutruntime::Expression", is_abstract=True)
adwithoutruntime_NamedElement = Class(name="adwithoutruntime::NamedElement", is_abstract=True)
adwithoutruntime_InitialNode = Class(name="adwithoutruntime::InitialNode")
ControlNode = Class(name="ControlNode")
adwithoutruntime_FinalNode = Class(name="adwithoutruntime::FinalNode", is_abstract=True)
adwithoutruntime_ActivityFinalNode = Class(name="adwithoutruntime::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
adwithoutruntime_ForkNode = Class(name="adwithoutruntime::ForkNode")
adwithoutruntime_JoinNode = Class(name="adwithoutruntime::JoinNode")
adwithoutruntime_MergeNode = Class(name="adwithoutruntime::MergeNode")
adwithoutruntime_DecisionNode = Class(name="adwithoutruntime::DecisionNode")
adwithoutruntime_Value = Class(name="adwithoutruntime::Value", is_abstract=True)
adwithoutruntime_IntegerVariable = Class(name="adwithoutruntime::IntegerVariable")
Variable = Class(name="Variable")
adwithoutruntime_BooleanValue = Class(name="adwithoutruntime::BooleanValue")
Value = Class(name="Value")
adwithoutruntime_IntegerValue = Class(name="adwithoutruntime::IntegerValue")
adwithoutruntime_IntegerExpression = Class(name="adwithoutruntime::IntegerExpression", is_abstract=True)
Expression = Class(name="Expression")
adwithoutruntime_ControlFlow = Class(name="adwithoutruntime::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
adwithoutruntime_BooleanVariable = Class(name="adwithoutruntime::BooleanVariable")
adwithoutruntime_ControlNode = Class(name="adwithoutruntime::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
adwithoutruntime_ExecutableNode = Class(name="adwithoutruntime::ExecutableNode", is_abstract=True)
adwithoutruntime_Action = Class(name="adwithoutruntime::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
adwithoutruntime_BooleanUnaryExpression = Class(name="adwithoutruntime::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
adwithoutruntime_BooleanBinaryExpression = Class(name="adwithoutruntime::BooleanBinaryExpression")
adwithoutruntime_BooleanExpression = Class(name="adwithoutruntime::BooleanExpression", is_abstract=True)
adwithoutruntime_IntegerCalculationExpression = Class(name="adwithoutruntime::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
adwithoutruntime_IntegerComparisonExpression = Class(name="adwithoutruntime::IntegerComparisonExpression")

# adwithoutruntime_Activity class attributes and methods

# NamedElement class attributes and methods

# adwithoutruntime_ActivityNode class attributes and methods

# adwithoutruntime_ActivityEdge class attributes and methods

# adwithoutruntime_Variable class attributes and methods
adwithoutruntime_Variable_name: Property = Property(name="name", type=StringType)
adwithoutruntime_Variable.attributes={adwithoutruntime_Variable_name}

# adwithoutruntime_OpaqueAction class attributes and methods

# Action class attributes and methods

# adwithoutruntime_Expression class attributes and methods

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

# adwithoutruntime_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# adwithoutruntime_BooleanVariable class attributes and methods

# adwithoutruntime_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# adwithoutruntime_ExecutableNode class attributes and methods

# adwithoutruntime_Action class attributes and methods

# ExecutableNode class attributes and methods

# adwithoutruntime_BooleanUnaryExpression class attributes and methods
adwithoutruntime_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_BooleanUnaryExpression.attributes={adwithoutruntime_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# adwithoutruntime_BooleanBinaryExpression class attributes and methods
adwithoutruntime_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_BooleanBinaryExpression.attributes={adwithoutruntime_BooleanBinaryExpression_operator}

# adwithoutruntime_BooleanExpression class attributes and methods

# adwithoutruntime_IntegerCalculationExpression class attributes and methods
adwithoutruntime_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_IntegerCalculationExpression.attributes={adwithoutruntime_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

# adwithoutruntime_IntegerComparisonExpression class attributes and methods
adwithoutruntime_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
adwithoutruntime_IntegerComparisonExpression.attributes={adwithoutruntime_IntegerComparisonExpression_operator}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="1", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges2: BinaryAssociation = BinaryAssociation(
    name="edges2",
    ends={
        Property(name="adwithoutruntime_ActivityEdge", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Activity", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals3: BinaryAssociation = BinaryAssociation(
    name="locals3",
    ends={
        Property(name="adwithoutruntime_Variable", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Activity4", type=adwithoutruntime_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs5: BinaryAssociation = BinaryAssociation(
    name="inputs5",
    ends={
        Property(name="adwithoutruntime_Variable7", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Activity6", type=adwithoutruntime_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing8: BinaryAssociation = BinaryAssociation(
    name="outgoing8",
    ends={
        Property(name="10", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming11: BinaryAssociation = BinaryAssociation(
    name="incoming11",
    ends={
        Property(name="13", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity14: BinaryAssociation = BinaryAssociation(
    name="activity14",
    ends={
        Property(name="16", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=adwithoutruntime_Activity, multiplicity=Multiplicity(1, 1))
    }
)
expressions24: BinaryAssociation = BinaryAssociation(
    name="expressions24",
    ends={
        Property(name="adwithoutruntime_Expression", type=adwithoutruntime_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_OpaqueAction", type=adwithoutruntime_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue25: BinaryAssociation = BinaryAssociation(
    name="initialValue25",
    ends={
        Property(name="adwithoutruntime_Value", type=adwithoutruntime_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Variable26", type=adwithoutruntime_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue27: BinaryAssociation = BinaryAssociation(
    name="currentValue27",
    ends={
        Property(name="adwithoutruntime_Value29", type=adwithoutruntime_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_Variable28", type=adwithoutruntime_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="19", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="22", type=adwithoutruntime_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=adwithoutruntime_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard23: BinaryAssociation = BinaryAssociation(
    name="guard23",
    ends={
        Property(name="adwithoutruntime_BooleanVariable", type=adwithoutruntime_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_ControlFlow", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand40: BinaryAssociation = BinaryAssociation(
    name="operand40",
    ends={
        Property(name="adwithoutruntime_BooleanVariable41", type=adwithoutruntime_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanUnaryExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand142: BinaryAssociation = BinaryAssociation(
    name="operand142",
    ends={
        Property(name="adwithoutruntime_BooleanVariable43", type=adwithoutruntime_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanBinaryExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand244: BinaryAssociation = BinaryAssociation(
    name="operand244",
    ends={
        Property(name="adwithoutruntime_BooleanVariable46", type=adwithoutruntime_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanBinaryExpression45", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand230: BinaryAssociation = BinaryAssociation(
    name="operand230",
    ends={
        Property(name="adwithoutruntime_IntegerVariable", type=adwithoutruntime_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerExpression", type=adwithoutruntime_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand131: BinaryAssociation = BinaryAssociation(
    name="operand131",
    ends={
        Property(name="adwithoutruntime_IntegerVariable33", type=adwithoutruntime_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerExpression32", type=adwithoutruntime_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee34: BinaryAssociation = BinaryAssociation(
    name="assignee34",
    ends={
        Property(name="adwithoutruntime_BooleanVariable35", type=adwithoutruntime_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_BooleanExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee36: BinaryAssociation = BinaryAssociation(
    name="assignee36",
    ends={
        Property(name="adwithoutruntime_IntegerVariable37", type=adwithoutruntime_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerCalculationExpression", type=adwithoutruntime_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee38: BinaryAssociation = BinaryAssociation(
    name="assignee38",
    ends={
        Property(name="adwithoutruntime_BooleanVariable39", type=adwithoutruntime_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adwithoutruntime_IntegerComparisonExpression", type=adwithoutruntime_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_adwithoutruntime_Activity_NamedElement = Generalization(general=NamedElement, specific=adwithoutruntime_Activity)
gen_adwithoutruntime_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=adwithoutruntime_ActivityNode)
gen_adwithoutruntime_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=adwithoutruntime_ActivityEdge)
gen_adwithoutruntime_OpaqueAction_Action = Generalization(general=Action, specific=adwithoutruntime_OpaqueAction)
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
gen_adwithoutruntime_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=adwithoutruntime_ControlFlow)
gen_adwithoutruntime_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=adwithoutruntime_ControlNode)
gen_adwithoutruntime_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=adwithoutruntime_ExecutableNode)
gen_adwithoutruntime_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=adwithoutruntime_Action)
gen_adwithoutruntime_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=adwithoutruntime_BooleanUnaryExpression)
gen_adwithoutruntime_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=adwithoutruntime_BooleanBinaryExpression)
gen_adwithoutruntime_IntegerExpression_Expression = Generalization(general=Expression, specific=adwithoutruntime_IntegerExpression)
gen_adwithoutruntime_BooleanExpression_Expression = Generalization(general=Expression, specific=adwithoutruntime_BooleanExpression)
gen_adwithoutruntime_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=adwithoutruntime_IntegerCalculationExpression)
gen_adwithoutruntime_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=adwithoutruntime_IntegerComparisonExpression)

# Domain Model
domain_model = DomainModel(
    name="adwithoutruntime",
    types={adwithoutruntime_Activity, NamedElement, adwithoutruntime_ActivityNode, adwithoutruntime_ActivityEdge, adwithoutruntime_Variable, adwithoutruntime_OpaqueAction, Action, adwithoutruntime_Expression, adwithoutruntime_NamedElement, adwithoutruntime_InitialNode, ControlNode, adwithoutruntime_FinalNode, adwithoutruntime_ActivityFinalNode, FinalNode, adwithoutruntime_ForkNode, adwithoutruntime_JoinNode, adwithoutruntime_MergeNode, adwithoutruntime_DecisionNode, adwithoutruntime_Value, adwithoutruntime_IntegerVariable, Variable, adwithoutruntime_BooleanValue, Value, adwithoutruntime_IntegerValue, adwithoutruntime_IntegerExpression, Expression, adwithoutruntime_ControlFlow, ActivityEdge, adwithoutruntime_BooleanVariable, adwithoutruntime_ControlNode, ActivityNode, adwithoutruntime_ExecutableNode, adwithoutruntime_Action, ExecutableNode, adwithoutruntime_BooleanUnaryExpression, BooleanExpression, adwithoutruntime_BooleanBinaryExpression, adwithoutruntime_BooleanExpression, adwithoutruntime_IntegerCalculationExpression, IntegerExpression, adwithoutruntime_IntegerComparisonExpression, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={nodes0, edges2, locals3, inputs5, outgoing8, incoming11, activity14, expressions24, initialValue25, currentValue27, source17, target20, guard23, operand40, operand142, operand244, operand230, operand131, assignee34, assignee36, assignee38},
    generalizations={gen_adwithoutruntime_Activity_NamedElement, gen_adwithoutruntime_ActivityNode_NamedElement, gen_adwithoutruntime_ActivityEdge_NamedElement, gen_adwithoutruntime_OpaqueAction_Action, gen_adwithoutruntime_InitialNode_ControlNode, gen_adwithoutruntime_FinalNode_ControlNode, gen_adwithoutruntime_ActivityFinalNode_FinalNode, gen_adwithoutruntime_ForkNode_ControlNode, gen_adwithoutruntime_JoinNode_ControlNode, gen_adwithoutruntime_MergeNode_ControlNode, gen_adwithoutruntime_DecisionNode_ControlNode, gen_adwithoutruntime_IntegerVariable_Variable, gen_adwithoutruntime_BooleanVariable_Variable, gen_adwithoutruntime_BooleanValue_Value, gen_adwithoutruntime_IntegerValue_Value, gen_adwithoutruntime_ControlFlow_ActivityEdge, gen_adwithoutruntime_ControlNode_ActivityNode, gen_adwithoutruntime_ExecutableNode_ActivityNode, gen_adwithoutruntime_Action_ExecutableNode, gen_adwithoutruntime_BooleanUnaryExpression_BooleanExpression, gen_adwithoutruntime_BooleanBinaryExpression_BooleanExpression, gen_adwithoutruntime_IntegerExpression_Expression, gen_adwithoutruntime_BooleanExpression_Expression, gen_adwithoutruntime_IntegerCalculationExpression_IntegerExpression, gen_adwithoutruntime_IntegerComparisonExpression_IntegerExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)