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
minuml2_Activity = Class(name="minuml2::Activity")
minuml2_ActivityNode = Class(name="minuml2::ActivityNode")
minuml2_ActivityEdge = Class(name="minuml2::ActivityEdge")
minuml2_ActivityGroup = Class(name="minuml2::ActivityGroup", is_abstract=True)
minuml2_ActivityPartition = Class(name="minuml2::ActivityPartition")
ActivityGroup = Class(name="ActivityGroup")
minuml2_OpaqueAction = Class(name="minuml2::OpaqueAction")
ActivityNode = Class(name="ActivityNode")
minuml2_ForkNode = Class(name="minuml2::ForkNode")
minuml2_JoinNode = Class(name="minuml2::JoinNode")
minuml2_DecisionNode = Class(name="minuml2::DecisionNode")
minuml2_ActivityFinalNode = Class(name="minuml2::ActivityFinalNode")
minuml2_ValueSpecification = Class(name="minuml2::ValueSpecification")
minuml2_ControlFlow = Class(name="minuml2::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
minuml2_ObjectFlow = Class(name="minuml2::ObjectFlow")
minuml2_OpaqueExpression = Class(name="minuml2::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")

# minuml2_Activity class attributes and methods

# minuml2_ActivityNode class attributes and methods

# minuml2_ActivityEdge class attributes and methods

# minuml2_ActivityGroup class attributes and methods

# minuml2_ActivityPartition class attributes and methods

# ActivityGroup class attributes and methods

# minuml2_OpaqueAction class attributes and methods

# ActivityNode class attributes and methods

# minuml2_ForkNode class attributes and methods

# minuml2_JoinNode class attributes and methods

# minuml2_DecisionNode class attributes and methods

# minuml2_ActivityFinalNode class attributes and methods

# minuml2_ValueSpecification class attributes and methods

# minuml2_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# minuml2_ObjectFlow class attributes and methods

# minuml2_OpaqueExpression class attributes and methods
minuml2_OpaqueExpression_language: Property = Property(name="language", type=StringType)
minuml2_OpaqueExpression_body: Property = Property(name="body", type=StringType)
minuml2_OpaqueExpression.attributes={minuml2_OpaqueExpression_language, minuml2_OpaqueExpression_body}

# ValueSpecification class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="minuml2_ActivityNode", type=minuml2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_Activity", type=minuml2_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="minuml2_ActivityEdge", type=minuml2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_Activity2", type=minuml2_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups3: BinaryAssociation = BinaryAssociation(
    name="groups3",
    ends={
        Property(name="minuml2_ActivityGroup", type=minuml2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_Activity4", type=minuml2_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="minuml2_ActivityNode7", type=minuml2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ActivityEdge6", type=minuml2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="minuml2_ActivityNode10", type=minuml2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ActivityEdge9", type=minuml2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard11: BinaryAssociation = BinaryAssociation(
    name="guard11",
    ends={
        Property(name="minuml2_ValueSpecification", type=minuml2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml2_ActivityEdge12", type=minuml2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_minuml2_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=minuml2_ActivityPartition)
gen_minuml2_OpaqueAction_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_OpaqueAction)
gen_minuml2_ForkNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_ForkNode)
gen_minuml2_JoinNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_JoinNode)
gen_minuml2_DecisionNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_DecisionNode)
gen_minuml2_ActivityFinalNode_ActivityNode = Generalization(general=ActivityNode, specific=minuml2_ActivityFinalNode)
gen_minuml2_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=minuml2_ControlFlow)
gen_minuml2_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=minuml2_ObjectFlow)
gen_minuml2_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=minuml2_OpaqueExpression)

# Domain Model
domain_model = DomainModel(
    name="minuml2",
    types={minuml2_Activity, minuml2_ActivityNode, minuml2_ActivityEdge, minuml2_ActivityGroup, minuml2_ActivityPartition, ActivityGroup, minuml2_OpaqueAction, ActivityNode, minuml2_ForkNode, minuml2_JoinNode, minuml2_DecisionNode, minuml2_ActivityFinalNode, minuml2_ValueSpecification, minuml2_ControlFlow, ActivityEdge, minuml2_ObjectFlow, minuml2_OpaqueExpression, ValueSpecification},
    associations={nodes0, edges1, groups3, source5, target8, guard11},
    generalizations={gen_minuml2_ActivityPartition_ActivityGroup, gen_minuml2_OpaqueAction_ActivityNode, gen_minuml2_ForkNode_ActivityNode, gen_minuml2_JoinNode_ActivityNode, gen_minuml2_DecisionNode_ActivityNode, gen_minuml2_ActivityFinalNode_ActivityNode, gen_minuml2_ControlFlow_ActivityEdge, gen_minuml2_ObjectFlow_ActivityEdge, gen_minuml2_OpaqueExpression_ValueSpecification},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)