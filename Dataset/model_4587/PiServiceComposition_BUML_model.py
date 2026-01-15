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
EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="PRE"),
			EnumerationLiteral(name="POST"),
			EnumerationLiteral(name="TIME")
    }
)

ActionType: Enumeration = Enumeration(
    name="ActionType",
    literals={
            EnumerationLiteral(name="WS"),
			EnumerationLiteral(name="AOP")
    }
)

# Classes
PiServiceComposition_CompositionServiceModel = Class(name="PiServiceComposition::CompositionServiceModel")
PiServiceComposition_ActivityPartition = Class(name="PiServiceComposition::ActivityPartition", is_abstract=True)
PiServiceComposition_Activity = Class(name="PiServiceComposition::Activity", is_abstract=True)
PiServiceComposition_ActivityEdge = Class(name="PiServiceComposition::ActivityEdge", is_abstract=True)
PiServiceComposition_Policy = Class(name="PiServiceComposition::Policy")
PiServiceComposition_Variable = Class(name="PiServiceComposition::Variable")
PiServiceComposition_NamedElement = Class(name="PiServiceComposition::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
PiServiceComposition_ActivityNode = Class(name="PiServiceComposition::ActivityNode", is_abstract=True)
PiServiceComposition_ExecutableNode = Class(name="PiServiceComposition::ExecutableNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
PiServiceComposition_ControlNode = Class(name="PiServiceComposition::ControlNode", is_abstract=True)
PiServiceComposition_ObjectNode = Class(name="PiServiceComposition::ObjectNode")
PiServiceComposition_InitialNode = Class(name="PiServiceComposition::InitialNode")
ControlNode = Class(name="ControlNode")
PiServiceComposition_FinalNode = Class(name="PiServiceComposition::FinalNode", is_abstract=True)
PiServiceComposition_ForkNode = Class(name="PiServiceComposition::ForkNode")
PiServiceComposition_JoinNode = Class(name="PiServiceComposition::JoinNode")
PiServiceComposition_DecisionNode = Class(name="PiServiceComposition::DecisionNode")
PiServiceComposition_MergeNode = Class(name="PiServiceComposition::MergeNode")
PiServiceComposition_ActivityFinalNode = Class(name="PiServiceComposition::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
PiServiceComposition_ServiceActivity = Class(name="PiServiceComposition::ServiceActivity")
Activity = Class(name="Activity")
PiServiceComposition_Action = Class(name="PiServiceComposition::Action")
PiServiceComposition_ControlFlow = Class(name="PiServiceComposition::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
PiServiceComposition_ObjectFlow = Class(name="PiServiceComposition::ObjectFlow")
ExecutableNode = Class(name="ExecutableNode")
PiServiceComposition_BussinessCollaborator = Class(name="PiServiceComposition::BussinessCollaborator")
ActivityPartition = Class(name="ActivityPartition")
PiServiceComposition_Rule = Class(name="PiServiceComposition::Rule")

# PiServiceComposition_CompositionServiceModel class attributes and methods

# PiServiceComposition_ActivityPartition class attributes and methods
PiServiceComposition_ActivityPartition_isDimension: Property = Property(name="isDimension", type=BooleanType)
PiServiceComposition_ActivityPartition_isExternal: Property = Property(name="isExternal", type=BooleanType)
PiServiceComposition_ActivityPartition.attributes={PiServiceComposition_ActivityPartition_isExternal, PiServiceComposition_ActivityPartition_isDimension}

# PiServiceComposition_Activity class attributes and methods

# PiServiceComposition_ActivityEdge class attributes and methods

# PiServiceComposition_Policy class attributes and methods
PiServiceComposition_Policy_name: Property = Property(name="name", type=StringType)
PiServiceComposition_Policy.attributes={PiServiceComposition_Policy_name}

# PiServiceComposition_Variable class attributes and methods
PiServiceComposition_Variable_name: Property = Property(name="name", type=StringType)
PiServiceComposition_Variable_type: Property = Property(name="type", type=StringType)
PiServiceComposition_Variable.attributes={PiServiceComposition_Variable_name, PiServiceComposition_Variable_type}

# PiServiceComposition_NamedElement class attributes and methods
PiServiceComposition_NamedElement_name: Property = Property(name="name", type=StringType)
PiServiceComposition_NamedElement.attributes={PiServiceComposition_NamedElement_name}

# NamedElement class attributes and methods

# PiServiceComposition_ActivityNode class attributes and methods

# PiServiceComposition_ExecutableNode class attributes and methods

# ActivityNode class attributes and methods

# PiServiceComposition_ControlNode class attributes and methods

# PiServiceComposition_ObjectNode class attributes and methods

# PiServiceComposition_InitialNode class attributes and methods

# ControlNode class attributes and methods

# PiServiceComposition_FinalNode class attributes and methods

# PiServiceComposition_ForkNode class attributes and methods

# PiServiceComposition_JoinNode class attributes and methods

# PiServiceComposition_DecisionNode class attributes and methods

# PiServiceComposition_MergeNode class attributes and methods

# PiServiceComposition_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# PiServiceComposition_ServiceActivity class attributes and methods

# Activity class attributes and methods

# PiServiceComposition_Action class attributes and methods
PiServiceComposition_Action_type: Property = Property(name="type", type=StringType)
PiServiceComposition_Action.attributes={PiServiceComposition_Action_type}

# PiServiceComposition_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# PiServiceComposition_ObjectFlow class attributes and methods

# ExecutableNode class attributes and methods

# PiServiceComposition_BussinessCollaborator class attributes and methods

# ActivityPartition class attributes and methods

# PiServiceComposition_Rule class attributes and methods
PiServiceComposition_Rule_name: Property = Property(name="name", type=StringType)
PiServiceComposition_Rule_event: Property = Property(name="event", type=StringType)
PiServiceComposition_Rule_condition: Property = Property(name="condition", type=StringType)
PiServiceComposition_Rule_action: Property = Property(name="action", type=StringType)
PiServiceComposition_Rule.attributes={PiServiceComposition_Rule_action, PiServiceComposition_Rule_condition, PiServiceComposition_Rule_event, PiServiceComposition_Rule_name}

# Relationships
partition0: BinaryAssociation = BinaryAssociation(
    name="partition0",
    ends={
        Property(name="PiServiceComposition_ActivityPartition", type=PiServiceComposition_CompositionServiceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_CompositionServiceModel", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities1: BinaryAssociation = BinaryAssociation(
    name="activities1",
    ends={
        Property(name="PiServiceComposition_Activity", type=PiServiceComposition_CompositionServiceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_CompositionServiceModel2", type=PiServiceComposition_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges3: BinaryAssociation = BinaryAssociation(
    name="edges3",
    ends={
        Property(name="PiServiceComposition_ActivityEdge", type=PiServiceComposition_CompositionServiceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_CompositionServiceModel4", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositionPolices5: BinaryAssociation = BinaryAssociation(
    name="compositionPolices5",
    ends={
        Property(name="PiServiceComposition_Policy", type=PiServiceComposition_CompositionServiceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_CompositionServiceModel6", type=PiServiceComposition_Policy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vars7: BinaryAssociation = BinaryAssociation(
    name="vars7",
    ends={
        Property(name="PiServiceComposition_Variable", type=PiServiceComposition_CompositionServiceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_CompositionServiceModel8", type=PiServiceComposition_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node9: BinaryAssociation = BinaryAssociation(
    name="node9",
    ends={
        Property(name="PiServiceComposition_ActivityNode", type=PiServiceComposition_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_Activity10", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
APartition12: BinaryAssociation = BinaryAssociation(
    name="APartition12",
    ends={
        Property(name="PiServiceComposition_ActivityPartition13", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_ActivityPartition11", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity25: BinaryAssociation = BinaryAssociation(
    name="activity25",
    ends={
        Property(name="PiServiceComposition_Activity27", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_ActivityNode26", type=PiServiceComposition_Activity, multiplicity=Multiplicity(0, 1))
    }
)
incoming28: BinaryAssociation = BinaryAssociation(
    name="incoming28",
    ends={
        Property(name="ActivityEdge29", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing30: BinaryAssociation = BinaryAssociation(
    name="outgoing30",
    ends={
        Property(name="ActivityEdge31", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement33: BinaryAssociation = BinaryAssociation(
    name="redefinedElement33",
    ends={
        Property(name="PiServiceComposition_ActivityNode34", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_ActivityNode32", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
partition35: BinaryAssociation = BinaryAssociation(
    name="partition35",
    ends={
        Property(name="ActivityPartition36", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
action37: BinaryAssociation = BinaryAssociation(
    name="action37",
    ends={
        Property(name="PiServiceComposition_Action", type=PiServiceComposition_ServiceActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_ServiceActivity", type=PiServiceComposition_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edges14: BinaryAssociation = BinaryAssociation(
    name="edges14",
    ends={
        Property(name="ActivityEdge", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="partition", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
nodes15: BinaryAssociation = BinaryAssociation(
    name="nodes15",
    ends={
        Property(name="ActivityNode", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="partition16", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="ActivityNode18", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="ActivityNode20", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=PiServiceComposition_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement22: BinaryAssociation = BinaryAssociation(
    name="redefinedElement22",
    ends={
        Property(name="PiServiceComposition_ActivityEdge23", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_ActivityEdge21", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
partition24: BinaryAssociation = BinaryAssociation(
    name="partition24",
    ends={
        Property(name="ActivityPartition", type=PiServiceComposition_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=PiServiceComposition_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
contains46: BinaryAssociation = BinaryAssociation(
    name="contains46",
    ends={
        Property(name="Rule", type=PiServiceComposition_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="policy", type=PiServiceComposition_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
hasVars47: BinaryAssociation = BinaryAssociation(
    name="hasVars47",
    ends={
        Property(name="PiServiceComposition_Variable49", type=PiServiceComposition_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_Policy48", type=PiServiceComposition_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
typeOperation50: BinaryAssociation = BinaryAssociation(
    name="typeOperation50",
    ends={
        Property(name="BussinessCollaborator", type=PiServiceComposition_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="hasPolices", type=PiServiceComposition_BussinessCollaborator, multiplicity=Multiplicity(0, 9999))
    }
)
action51: BinaryAssociation = BinaryAssociation(
    name="action51",
    ends={
        Property(name="Action", type=PiServiceComposition_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="definePolices", type=PiServiceComposition_Action, multiplicity=Multiplicity(0, 9999))
    }
)
hasPolices38: BinaryAssociation = BinaryAssociation(
    name="hasPolices38",
    ends={
        Property(name="PiServiceComposition_Policy40", type=PiServiceComposition_ServiceActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="PiServiceComposition_ServiceActivity39", type=PiServiceComposition_Policy, multiplicity=Multiplicity(0, 9999))
    }
)
definePolices41: BinaryAssociation = BinaryAssociation(
    name="definePolices41",
    ends={
        Property(name="Policy", type=PiServiceComposition_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="action", type=PiServiceComposition_Policy, multiplicity=Multiplicity(0, 1))
    }
)
hasPolices42: BinaryAssociation = BinaryAssociation(
    name="hasPolices42",
    ends={
        Property(name="Policy43", type=PiServiceComposition_BussinessCollaborator, multiplicity=Multiplicity(1, 1)),
        Property(name="typeOperation", type=PiServiceComposition_Policy, multiplicity=Multiplicity(0, 9999))
    }
)
policy44: BinaryAssociation = BinaryAssociation(
    name="policy44",
    ends={
        Property(name="Policy45", type=PiServiceComposition_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=PiServiceComposition_Policy, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PiServiceComposition_Activity_NamedElement = Generalization(general=NamedElement, specific=PiServiceComposition_Activity)
gen_PiServiceComposition_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=PiServiceComposition_ActivityPartition)
gen_PiServiceComposition_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=PiServiceComposition_ObjectFlow)
gen_PiServiceComposition_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=PiServiceComposition_ActivityNode)
gen_PiServiceComposition_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=PiServiceComposition_ExecutableNode)
gen_PiServiceComposition_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=PiServiceComposition_ControlNode)
gen_PiServiceComposition_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=PiServiceComposition_ObjectNode)
gen_PiServiceComposition_InitialNode_ControlNode = Generalization(general=ControlNode, specific=PiServiceComposition_InitialNode)
gen_PiServiceComposition_FinalNode_ControlNode = Generalization(general=ControlNode, specific=PiServiceComposition_FinalNode)
gen_PiServiceComposition_ForkNode_ControlNode = Generalization(general=ControlNode, specific=PiServiceComposition_ForkNode)
gen_PiServiceComposition_JoinNode_ControlNode = Generalization(general=ControlNode, specific=PiServiceComposition_JoinNode)
gen_PiServiceComposition_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=PiServiceComposition_DecisionNode)
gen_PiServiceComposition_MergeNode_ControlNode = Generalization(general=ControlNode, specific=PiServiceComposition_MergeNode)
gen_PiServiceComposition_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=PiServiceComposition_ActivityFinalNode)
gen_PiServiceComposition_ServiceActivity_Activity = Generalization(general=Activity, specific=PiServiceComposition_ServiceActivity)
gen_PiServiceComposition_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=PiServiceComposition_ActivityEdge)
gen_PiServiceComposition_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=PiServiceComposition_ControlFlow)
gen_PiServiceComposition_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=PiServiceComposition_Action)
gen_PiServiceComposition_BussinessCollaborator_ActivityPartition = Generalization(general=ActivityPartition, specific=PiServiceComposition_BussinessCollaborator)

# Domain Model
domain_model = DomainModel(
    name="PiServiceComposition",
    types={PiServiceComposition_CompositionServiceModel, PiServiceComposition_ActivityPartition, PiServiceComposition_Activity, PiServiceComposition_ActivityEdge, PiServiceComposition_Policy, PiServiceComposition_Variable, PiServiceComposition_NamedElement, NamedElement, PiServiceComposition_ActivityNode, PiServiceComposition_ExecutableNode, ActivityNode, PiServiceComposition_ControlNode, PiServiceComposition_ObjectNode, PiServiceComposition_InitialNode, ControlNode, PiServiceComposition_FinalNode, PiServiceComposition_ForkNode, PiServiceComposition_JoinNode, PiServiceComposition_DecisionNode, PiServiceComposition_MergeNode, PiServiceComposition_ActivityFinalNode, FinalNode, PiServiceComposition_ServiceActivity, Activity, PiServiceComposition_Action, PiServiceComposition_ControlFlow, ActivityEdge, PiServiceComposition_ObjectFlow, ExecutableNode, PiServiceComposition_BussinessCollaborator, ActivityPartition, PiServiceComposition_Rule, EventType, ActionType},
    associations={partition0, activities1, edges3, compositionPolices5, vars7, node9, APartition12, activity25, incoming28, outgoing30, redefinedElement33, partition35, action37, edges14, nodes15, target17, source19, redefinedElement22, partition24, contains46, hasVars47, typeOperation50, action51, hasPolices38, definePolices41, hasPolices42, policy44},
    generalizations={gen_PiServiceComposition_Activity_NamedElement, gen_PiServiceComposition_ActivityPartition_NamedElement, gen_PiServiceComposition_ObjectFlow_ActivityEdge, gen_PiServiceComposition_ActivityNode_NamedElement, gen_PiServiceComposition_ExecutableNode_ActivityNode, gen_PiServiceComposition_ControlNode_ActivityNode, gen_PiServiceComposition_ObjectNode_ActivityNode, gen_PiServiceComposition_InitialNode_ControlNode, gen_PiServiceComposition_FinalNode_ControlNode, gen_PiServiceComposition_ForkNode_ControlNode, gen_PiServiceComposition_JoinNode_ControlNode, gen_PiServiceComposition_DecisionNode_ControlNode, gen_PiServiceComposition_MergeNode_ControlNode, gen_PiServiceComposition_ActivityFinalNode_FinalNode, gen_PiServiceComposition_ServiceActivity_Activity, gen_PiServiceComposition_ActivityEdge_NamedElement, gen_PiServiceComposition_ControlFlow_ActivityEdge, gen_PiServiceComposition_Action_ExecutableNode, gen_PiServiceComposition_BussinessCollaborator_ActivityPartition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)