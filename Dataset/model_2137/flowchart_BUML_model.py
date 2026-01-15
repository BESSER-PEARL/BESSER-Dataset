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
flowchart_Node = Class(name="flowchart::Node")
flowchart_Transition = Class(name="flowchart::Transition")
flowchart_Action = Class(name="flowchart::Action")
flowchart_Decision = Class(name="flowchart::Decision")
flowchart_Flowchart = Class(name="flowchart::Flowchart")

# flowchart_Node class attributes and methods
flowchart_Node_name: Property = Property(name="name", type=StringType)
flowchart_Node.attributes={flowchart_Node_name}

# flowchart_Transition class attributes and methods
flowchart_Transition_label: Property = Property(name="label", type=StringType)
flowchart_Transition.attributes={flowchart_Transition_label}

# flowchart_Action class attributes and methods
flowchart_Action_isAction: Property = Property(name="isAction", type=BooleanType)
flowchart_Action.attributes={flowchart_Action_isAction}

# flowchart_Decision class attributes and methods
flowchart_Decision_isDecision: Property = Property(name="isDecision", type=BooleanType)
flowchart_Decision_condition: Property = Property(name="condition", type=StringType)
flowchart_Decision.attributes={flowchart_Decision_condition, flowchart_Decision_isDecision}

# flowchart_Flowchart class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="flowchart_Node", type=flowchart_Flowchart, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchart_Flowchart", type=flowchart_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="flowchart_Transition", type=flowchart_Flowchart, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchart_Flowchart2", type=flowchart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=flowchart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=flowchart_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=flowchart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=flowchart_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
actionNode6: BinaryAssociation = BinaryAssociation(
    name="actionNode6",
    ends={
        Property(name="flowchart_Action", type=flowchart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchart_Node7", type=flowchart_Action, multiplicity=Multiplicity(0, 1))
    }
)
decisionNode8: BinaryAssociation = BinaryAssociation(
    name="decisionNode8",
    ends={
        Property(name="flowchart_Decision", type=flowchart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchart_Node9", type=flowchart_Decision, multiplicity=Multiplicity(0, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node", type=flowchart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=flowchart_Node, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="Node12", type=flowchart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=flowchart_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="flowchart",
    types={flowchart_Node, flowchart_Transition, flowchart_Action, flowchart_Decision, flowchart_Flowchart},
    associations={nodes0, transitions1, incoming3, outgoing4, actionNode6, decisionNode8, source10, target11},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)