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

# Classes
activitydiagram_Activity = Class(name="activitydiagram::Activity")
NamedActivity = Class(name="NamedActivity")
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge", is_abstract=True)
activitydiagram_Variable = Class(name="activitydiagram::Variable", is_abstract=True)
activitydiagram_ControlFlow = Class(name="activitydiagram::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activitydiagram_BooleanVariable = Class(name="activitydiagram::BooleanVariable", is_abstract=True)
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activitydiagram_ExecutableNode = Class(name="activitydiagram::ExecutableNode", is_abstract=True)
activitydiagram_Token = Class(name="activitydiagram::Token")
activitydiagram_Offer = Class(name="activitydiagram::Offer")
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_Action = Class(name="activitydiagram::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
activitydiagram_OpaqueAction = Class(name="activitydiagram::OpaqueAction")
Action = Class(name="Action")
activitydiagram_Exp = Class(name="activitydiagram::Exp", is_abstract=True)
activitydiagram_NamedActivity = Class(name="activitydiagram::NamedActivity", is_abstract=True)
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_Input = Class(name="activitydiagram::Input")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
Variable = Class(name="Variable")
activitydiagram_Value = Class(name="activitydiagram::Value", is_abstract=True)
activitydiagram_InputValue = Class(name="activitydiagram::InputValue")
activitydiagram_ControlToken = Class(name="activitydiagram::ControlToken")
Token = Class(name="Token")
activitydiagram_ForkedToken = Class(name="activitydiagram::ForkedToken")
activitydiagram_Trace = Class(name="activitydiagram::Trace")
activitydiagram_BooleanValue = Class(name="activitydiagram::BooleanValue")
Value = Class(name="Value")
activitydiagram_IntegerValue = Class(name="activitydiagram::IntegerValue")
activitydiagram_IntegerVariable = Class(name="activitydiagram::IntegerVariable", is_abstract=True)
activitydiagram_Context = Class(name="activitydiagram::Context")

# activitydiagram_Activity class attributes and methods

# NamedActivity class attributes and methods

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_running: Property = Property(name="running", type=BooleanType)
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_running}

# activitydiagram_ActivityEdge class attributes and methods

# activitydiagram_Variable class attributes and methods

# activitydiagram_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activitydiagram_BooleanVariable class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ExecutableNode class attributes and methods

# activitydiagram_Token class attributes and methods

# activitydiagram_Offer class attributes and methods

# activitydiagram_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods

# activitydiagram_MergeNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods

# activitydiagram_Action class attributes and methods

# ExecutableNode class attributes and methods

# activitydiagram_OpaqueAction class attributes and methods

# Action class attributes and methods

# activitydiagram_Exp class attributes and methods

# activitydiagram_NamedActivity class attributes and methods
activitydiagram_NamedActivity_name: Property = Property(name="name", type=StringType)
activitydiagram_NamedActivity.attributes={activitydiagram_NamedActivity_name}

# activitydiagram_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activitydiagram_Input class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# Variable class attributes and methods

# activitydiagram_Value class attributes and methods

# activitydiagram_InputValue class attributes and methods

# activitydiagram_ControlToken class attributes and methods

# Token class attributes and methods

# activitydiagram_ForkedToken class attributes and methods
activitydiagram_ForkedToken_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
activitydiagram_ForkedToken.attributes={activitydiagram_ForkedToken_remainingOffersCount}

# activitydiagram_Trace class attributes and methods

# activitydiagram_BooleanValue class attributes and methods
activitydiagram_BooleanValue_value: Property = Property(name="value", type=BooleanType)
activitydiagram_BooleanValue.attributes={activitydiagram_BooleanValue_value}

# Value class attributes and methods

# activitydiagram_IntegerValue class attributes and methods
activitydiagram_IntegerValue_value: Property = Property(name="value", type=FloatType)
activitydiagram_IntegerValue.attributes={activitydiagram_IntegerValue_value}

# activitydiagram_IntegerVariable class attributes and methods

# activitydiagram_Context class attributes and methods

# Relationships
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="ActivityEdge", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
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
guard18: BinaryAssociation = BinaryAssociation(
    name="guard18",
    ends={
        Property(name="activitydiagram_BooleanVariable", type=activitydiagram_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ControlFlow", type=activitydiagram_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
heldTokens11: BinaryAssociation = BinaryAssociation(
    name="heldTokens11",
    ends={
        Property(name="Token", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="holder", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="ActivityNode13", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="ActivityNode15", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offers16: BinaryAssociation = BinaryAssociation(
    name="offers16",
    ends={
        Property(name="activitydiagram_Offer", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ActivityEdge17", type=activitydiagram_Offer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions19: BinaryAssociation = BinaryAssociation(
    name="expressions19",
    ends={
        Property(name="activitydiagram_Exp", type=activitydiagram_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_OpaqueAction", type=activitydiagram_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputValues30: BinaryAssociation = BinaryAssociation(
    name="inputValues30",
    ends={
        Property(name="activitydiagram_InputValue31", type=activitydiagram_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Input", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue20: BinaryAssociation = BinaryAssociation(
    name="initialValue20",
    ends={
        Property(name="activitydiagram_Value", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable21", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue22: BinaryAssociation = BinaryAssociation(
    name="currentValue22",
    ends={
        Property(name="activitydiagram_Value24", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Variable23", type=activitydiagram_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="activitydiagram_Value26", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue", type=activitydiagram_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable27: BinaryAssociation = BinaryAssociation(
    name="variable27",
    ends={
        Property(name="activitydiagram_Variable29", type=activitydiagram_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_InputValue28", type=activitydiagram_Variable, multiplicity=Multiplicity(1, 1))
    }
)
baseToken36: BinaryAssociation = BinaryAssociation(
    name="baseToken36",
    ends={
        Property(name="activitydiagram_Token37", type=activitydiagram_ForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_ForkedToken", type=activitydiagram_Token, multiplicity=Multiplicity(0, 1))
    }
)
holder32: BinaryAssociation = BinaryAssociation(
    name="holder32",
    ends={
        Property(name="ActivityNode33", type=activitydiagram_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="heldTokens", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offeredTokens34: BinaryAssociation = BinaryAssociation(
    name="offeredTokens34",
    ends={
        Property(name="activitydiagram_Token", type=activitydiagram_Offer, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Offer35", type=activitydiagram_Token, multiplicity=Multiplicity(0, 9999))
    }
)
executedNodes38: BinaryAssociation = BinaryAssociation(
    name="executedNodes38",
    ends={
        Property(name="activitydiagram_ActivityNode", type=activitydiagram_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Trace", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
output39: BinaryAssociation = BinaryAssociation(
    name="output39",
    ends={
        Property(name="activitydiagram_Trace40", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context", type=activitydiagram_Trace, multiplicity=Multiplicity(0, 1))
    }
)
activity41: BinaryAssociation = BinaryAssociation(
    name="activity41",
    ends={
        Property(name="activitydiagram_Activity43", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context42", type=activitydiagram_Activity, multiplicity=Multiplicity(0, 1))
    }
)
inputValues44: BinaryAssociation = BinaryAssociation(
    name="inputValues44",
    ends={
        Property(name="activitydiagram_InputValue46", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context45", type=activitydiagram_InputValue, multiplicity=Multiplicity(0, 9999))
    }
)
node47: BinaryAssociation = BinaryAssociation(
    name="node47",
    ends={
        Property(name="activitydiagram_JoinNode", type=activitydiagram_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram_Context48", type=activitydiagram_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_activitydiagram_Activity_NamedActivity = Generalization(general=NamedActivity, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityNode_NamedActivity = Generalization(general=NamedActivity, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activitydiagram_ControlFlow)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ExecutableNode)
gen_activitydiagram_ActivityEdge_NamedActivity = Generalization(general=NamedActivity, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activitydiagram_Action)
gen_activitydiagram_OpaqueAction_Action = Generalization(general=Action, specific=activitydiagram_OpaqueAction)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_BooleanVariable_Variable = Generalization(general=Variable, specific=activitydiagram_BooleanVariable)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_ControlToken_Token = Generalization(general=Token, specific=activitydiagram_ControlToken)
gen_activitydiagram_ForkedToken_Token = Generalization(general=Token, specific=activitydiagram_ForkedToken)
gen_activitydiagram_BooleanValue_Value = Generalization(general=Value, specific=activitydiagram_BooleanValue)
gen_activitydiagram_IntegerValue_Value = Generalization(general=Value, specific=activitydiagram_IntegerValue)
gen_activitydiagram_IntegerVariable_Variable = Generalization(general=Variable, specific=activitydiagram_IntegerVariable)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, NamedActivity, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_Variable, activitydiagram_ControlFlow, ActivityEdge, activitydiagram_BooleanVariable, activitydiagram_ControlNode, ActivityNode, activitydiagram_ExecutableNode, activitydiagram_Token, activitydiagram_Offer, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_ForkNode, activitydiagram_JoinNode, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_Action, ExecutableNode, activitydiagram_OpaqueAction, Action, activitydiagram_Exp, activitydiagram_NamedActivity, activitydiagram_InitialNode, ControlNode, activitydiagram_Input, activitydiagram_FinalNode, Variable, activitydiagram_Value, activitydiagram_InputValue, activitydiagram_ControlToken, Token, activitydiagram_ForkedToken, activitydiagram_Trace, activitydiagram_BooleanValue, Value, activitydiagram_IntegerValue, activitydiagram_IntegerVariable, activitydiagram_Context},
    associations={outgoing7, incoming8, activity10, nodes0, edges1, locals2, inputs4, guard18, heldTokens11, source12, target14, offers16, expressions19, inputValues30, initialValue20, currentValue22, value25, variable27, baseToken36, holder32, offeredTokens34, executedNodes38, output39, activity41, inputValues44, node47},
    generalizations={gen_activitydiagram_Activity_NamedActivity, gen_activitydiagram_ActivityNode_NamedActivity, gen_activitydiagram_ControlFlow_ActivityEdge, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_ExecutableNode_ActivityNode, gen_activitydiagram_ActivityEdge_NamedActivity, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_Action_ExecutableNode, gen_activitydiagram_OpaqueAction_Action, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_BooleanVariable_Variable, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_ControlToken_Token, gen_activitydiagram_ForkedToken_Token, gen_activitydiagram_BooleanValue_Value, gen_activitydiagram_IntegerValue_Value, gen_activitydiagram_IntegerVariable_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)