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
minuml2_ActivityFinalNode = Class(name="minuml2::ActivityFinalNode")
minuml2_ModelElement = Class(name="minuml2::ModelElement")
minuml2_ActivityPartition = Class(name="minuml2::ActivityPartition")
minuml2_Activity = Class(name="minuml2::Activity")
ModelElement = Class(name="ModelElement")
minuml2_ActivityNode = Class(name="minuml2::ActivityNode", is_abstract=True)
minuml2_ActivityEdge = Class(name="minuml2::ActivityEdge")
minuml2_OpaqueAction = Class(name="minuml2::OpaqueAction")
ActivityNode = Class(name="ActivityNode")
minuml2_InitialNode = Class(name="minuml2::InitialNode")
minuml2_DecisionNode = Class(name="minuml2::DecisionNode")
minuml2_ForkNode = Class(name="minuml2::ForkNode")
minuml2_JoinNode = Class(name="minuml2::JoinNode")
minuml2_OpaqueExpression = Class(name="minuml2::OpaqueExpression")
minuml2_ControlFlow = Class(name="minuml2::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
minuml2_ObjectFlow = Class(name="minuml2::ObjectFlow")
minuml2_ObjectNode = Class(name="minuml2::ObjectNode")

# minuml2_ActivityFinalNode class attributes and methods

# minuml2_ModelElement class attributes and methods
minuml2_ModelElement_name: Property = Property(name="name", type=StringType)
minuml2_ModelElement.attributes={minuml2_ModelElement_name}

# minuml2_ActivityPartition class attributes and methods

# minuml2_Activity class attributes and methods

# ModelElement class attributes and methods

# minuml2_ActivityNode class attributes and methods

# minuml2_ActivityEdge class attributes and methods

# minuml2_OpaqueAction class attributes and methods

# ActivityNode class attributes and methods

# minuml2_InitialNode class attributes and methods

# minuml2_DecisionNode class attributes and methods

# minuml2_ForkNode class attributes and methods

# minuml2_JoinNode class attributes and methods

# minuml2_OpaqueExpression class attributes and methods
minuml2_OpaqueExpression_language: Property = Property(name="language", type=StringType)
minuml2_OpaqueExpression_body: Property = Property(name="body", type=StringType)
minuml2_OpaqueExpression.attributes={minuml2_OpaqueExpression_body, minuml2_OpaqueExpression_language}

# minuml2_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# minuml2_ObjectFlow class attributes and methods

# minuml2_ObjectNode class attributes and methods

# Relationships
partition0: BinaryAssociation = BinaryAssociation(
    name="partition0",
    ends={
        Property(name="minuml2_ActivityPartition", type=minuml2_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ModelElement", type=minuml2_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
node1: BinaryAssociation = BinaryAssociation(
    name="node1",
    ends={
        Property(name="minuml2_ActivityNode", type=minuml2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_Activity", type=minuml2_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge2: BinaryAssociation = BinaryAssociation(
    name="edge2",
    ends={
        Property(name="minuml2_ActivityEdge", type=minuml2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_Activity3", type=minuml2_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group4: BinaryAssociation = BinaryAssociation(
    name="group4",
    ends={
        Property(name="minuml2_ActivityPartition6", type=minuml2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_Activity5", type=minuml2_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes7: BinaryAssociation = BinaryAssociation(
    name="nodes7",
    ends={
        Property(name="minuml2_ActivityNode9", type=minuml2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ActivityPartition8", type=minuml2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
edges10: BinaryAssociation = BinaryAssociation(
    name="edges10",
    ends={
        Property(name="minuml2_ActivityEdge12", type=minuml2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ActivityPartition11", type=minuml2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing13: BinaryAssociation = BinaryAssociation(
    name="outgoing13",
    ends={
        Property(name="ActivityEdge", type=minuml2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=minuml2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming14: BinaryAssociation = BinaryAssociation(
    name="incoming14",
    ends={
        Property(name="ActivityEdge15", type=minuml2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=minuml2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="ActivityNode", type=minuml2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=minuml2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="ActivityNode18", type=minuml2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=minuml2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard19: BinaryAssociation = BinaryAssociation(
    name="guard19",
    ends={
        Property(name="minuml2_OpaqueExpression", type=minuml2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ActivityEdge20", type=minuml2_OpaqueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="minuml2_ModelElement22", type=minuml2_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ObjectFlow", type=minuml2_ModelElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_minuml2_ActivityFinalNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_ActivityFinalNode)
gen_minuml2_ActivityEdge_ModelElement = Generalization(general=ModelElement, specific=minuml2_ActivityEdge)
gen_minuml2_Activity_ModelElement = Generalization(general=ModelElement, specific=minuml2_Activity)
gen_minuml2_ActivityPartition_ModelElement = Generalization(general=ModelElement, specific=minuml2_ActivityPartition)
gen_minuml2_ActivityNode_ModelElement = Generalization(general=ModelElement, specific=minuml2_ActivityNode)
gen_minuml2_OpaqueAction_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_OpaqueAction)
gen_minuml2_InitialNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_InitialNode)
gen_minuml2_DecisionNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_DecisionNode)
gen_minuml2_ForkNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_ForkNode)
gen_minuml2_JoinNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_JoinNode)
gen_minuml2_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=minuml2_ControlFlow)
gen_minuml2_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=minuml2_ObjectFlow)
gen_minuml2_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_ObjectNode)

# Domain Model
domain_model = DomainModel(
    name="minuml2",
    types={minuml2_ActivityFinalNode, minuml2_ModelElement, minuml2_ActivityPartition, minuml2_Activity, ModelElement, minuml2_ActivityNode, minuml2_ActivityEdge, minuml2_OpaqueAction, ActivityNode, minuml2_InitialNode, minuml2_DecisionNode, minuml2_ForkNode, minuml2_JoinNode, minuml2_OpaqueExpression, minuml2_ControlFlow, ActivityEdge, minuml2_ObjectFlow, minuml2_ObjectNode},
    associations={partition0, node1, edge2, group4, nodes7, edges10, outgoing13, incoming14, source16, target17, guard19, type21},
    generalizations={gen_minuml2_ActivityFinalNode_ActivityNode, gen_minuml2_ActivityEdge_ModelElement, gen_minuml2_Activity_ModelElement, gen_minuml2_ActivityPartition_ModelElement, gen_minuml2_ActivityNode_ModelElement, gen_minuml2_OpaqueAction_ActivityNode, gen_minuml2_InitialNode_ActivityNode, gen_minuml2_DecisionNode_ActivityNode, gen_minuml2_ForkNode_ActivityNode, gen_minuml2_JoinNode_ActivityNode, gen_minuml2_ControlFlow_ActivityEdge, gen_minuml2_ObjectFlow_ActivityEdge, gen_minuml2_ObjectNode_ActivityNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)