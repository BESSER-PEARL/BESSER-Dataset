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
ExpansionMode: Enumeration = Enumeration(
    name="ExpansionMode",
    literals={
            EnumerationLiteral(name="PARALLEL"),
			EnumerationLiteral(name="ITERATIVE")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="INACTIVE"),
			EnumerationLiteral(name="ACTIVE"),
			EnumerationLiteral(name="DONE")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT")
    }
)

# Classes
UML_Activity_mine_ActivityEdge = Class(name="UML::Activity::mine::ActivityEdge")
UML_Activity_mine_Element = Class(name="UML::Activity::mine::Element", is_abstract=True)
UML_Activity_mine_Activity = Class(name="UML::Activity::mine::Activity")
Element = Class(name="Element")
UML_Activity_mine_ActivityNode = Class(name="UML::Activity::mine::ActivityNode", is_abstract=True)
UML_Activity_mine_ExpansionRegion = Class(name="UML::Activity::mine::ExpansionRegion")
Action = Class(name="Action")
UML_Activity_mine_ControlNode = Class(name="UML::Activity::mine::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
UML_Activity_mine_ObjectNode = Class(name="UML::Activity::mine::ObjectNode")
UML_Activity_mine_Action = Class(name="UML::Activity::mine::Action")
UML_Activity_mine_Fork = Class(name="UML::Activity::mine::Fork")
ControlNode = Class(name="ControlNode")
UML_Activity_mine_Join = Class(name="UML::Activity::mine::Join")
UML_Activity_mine_ActivityInitialNode = Class(name="UML::Activity::mine::ActivityInitialNode")
UML_Activity_mine_ActivityFinalNode = Class(name="UML::Activity::mine::ActivityFinalNode")
UML_Activity_mine_DatastoreNode = Class(name="UML::Activity::mine::DatastoreNode")
ObjectNode = Class(name="ObjectNode")
UML_Activity_mine_ActivityParameterNode = Class(name="UML::Activity::mine::ActivityParameterNode")
UML_Activity_mine_ExpansionNode = Class(name="UML::Activity::mine::ExpansionNode")

# UML_Activity_mine_ActivityEdge class attributes and methods
UML_Activity_mine_ActivityEdge_objectFlow: Property = Property(name="objectFlow", type=BooleanType)
UML_Activity_mine_ActivityEdge.attributes={UML_Activity_mine_ActivityEdge_objectFlow}

# UML_Activity_mine_Element class attributes and methods
UML_Activity_mine_Element_name: Property = Property(name="name", type=StringType)
UML_Activity_mine_Element_elementID: Property = Property(name="elementID", type=StringType)
UML_Activity_mine_Element_properties: Property = Property(name="properties", type=StringType)
UML_Activity_mine_Element.attributes={UML_Activity_mine_Element_elementID, UML_Activity_mine_Element_properties, UML_Activity_mine_Element_name}

# UML_Activity_mine_Activity class attributes and methods

# Element class attributes and methods

# UML_Activity_mine_ActivityNode class attributes and methods

# UML_Activity_mine_ExpansionRegion class attributes and methods

# Action class attributes and methods

# UML_Activity_mine_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# UML_Activity_mine_ObjectNode class attributes and methods
UML_Activity_mine_ObjectNode_objects: Property = Property(name="objects", type=StringType)
UML_Activity_mine_ObjectNode_upperBound: Property = Property(name="upperBound", type=StringType)
UML_Activity_mine_ObjectNode.attributes={UML_Activity_mine_ObjectNode_upperBound, UML_Activity_mine_ObjectNode_objects}

# UML_Activity_mine_Action class attributes and methods
UML_Activity_mine_Action_inputs: Property = Property(name="inputs", type=StringType)
UML_Activity_mine_Action_outputs: Property = Property(name="outputs", type=StringType)
UML_Activity_mine_Action.attributes={UML_Activity_mine_Action_outputs, UML_Activity_mine_Action_inputs}

# UML_Activity_mine_Fork class attributes and methods

# ControlNode class attributes and methods

# UML_Activity_mine_Join class attributes and methods

# UML_Activity_mine_ActivityInitialNode class attributes and methods

# UML_Activity_mine_ActivityFinalNode class attributes and methods

# UML_Activity_mine_DatastoreNode class attributes and methods

# ObjectNode class attributes and methods

# UML_Activity_mine_ActivityParameterNode class attributes and methods
UML_Activity_mine_ActivityParameterNode_parameter: Property = Property(name="parameter", type=StringType)
UML_Activity_mine_ActivityParameterNode.attributes={UML_Activity_mine_ActivityParameterNode_parameter}

# UML_Activity_mine_ExpansionNode class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="UML_Activity_mine_ActivityNode", type=UML_Activity_mine_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Activity_mine_Activity", type=UML_Activity_mine_ActivityNode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="UML_Activity_mine_ActivityEdge", type=UML_Activity_mine_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Activity_mine_Activity2", type=UML_Activity_mine_ActivityEdge, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="ActivityNode", type=UML_Activity_mine_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=UML_Activity_mine_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="ActivityNode5", type=UML_Activity_mine_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=UML_Activity_mine_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="ActivityEdge", type=UML_Activity_mine_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=UML_Activity_mine_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="ActivityEdge8", type=UML_Activity_mine_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=UML_Activity_mine_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inputCollections9: BinaryAssociation = BinaryAssociation(
    name="inputCollections9",
    ends={
        Property(name="UML_Activity_mine_ExpansionNode", type=UML_Activity_mine_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Activity_mine_ExpansionRegion", type=UML_Activity_mine_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputCollections10: BinaryAssociation = BinaryAssociation(
    name="outputCollections10",
    ends={
        Property(name="UML_Activity_mine_ExpansionNode12", type=UML_Activity_mine_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Activity_mine_ExpansionRegion11", type=UML_Activity_mine_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
edges13: BinaryAssociation = BinaryAssociation(
    name="edges13",
    ends={
        Property(name="UML_Activity_mine_ActivityEdge15", type=UML_Activity_mine_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Activity_mine_ExpansionRegion14", type=UML_Activity_mine_ActivityEdge, multiplicity=Multiplicity(1, 9999))
    }
)
nodes16: BinaryAssociation = BinaryAssociation(
    name="nodes16",
    ends={
        Property(name="UML_Activity_mine_ActivityNode18", type=UML_Activity_mine_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Activity_mine_ExpansionRegion17", type=UML_Activity_mine_ActivityNode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML_Activity_mine_ActivityEdge_Element = Generalization(general=Element, specific=UML_Activity_mine_ActivityEdge)
gen_UML_Activity_mine_ActivityNode_Element = Generalization(general=Element, specific=UML_Activity_mine_ActivityNode)
gen_UML_Activity_mine_Activity_Element = Generalization(general=Element, specific=UML_Activity_mine_Activity)
gen_UML_Activity_mine_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML_Activity_mine_ExpansionNode)
gen_UML_Activity_mine_ExpansionRegion_Action = Generalization(general=Action, specific=UML_Activity_mine_ExpansionRegion)
gen_UML_Activity_mine_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=UML_Activity_mine_ControlNode)
gen_UML_Activity_mine_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=UML_Activity_mine_ObjectNode)
gen_UML_Activity_mine_Action_ActivityNode = Generalization(general=ActivityNode, specific=UML_Activity_mine_Action)
gen_UML_Activity_mine_Fork_ControlNode = Generalization(general=ControlNode, specific=UML_Activity_mine_Fork)
gen_UML_Activity_mine_Join_ControlNode = Generalization(general=ControlNode, specific=UML_Activity_mine_Join)
gen_UML_Activity_mine_ActivityInitialNode_ControlNode = Generalization(general=ControlNode, specific=UML_Activity_mine_ActivityInitialNode)
gen_UML_Activity_mine_ActivityFinalNode_ControlNode = Generalization(general=ControlNode, specific=UML_Activity_mine_ActivityFinalNode)
gen_UML_Activity_mine_DatastoreNode_ObjectNode = Generalization(general=ObjectNode, specific=UML_Activity_mine_DatastoreNode)
gen_UML_Activity_mine_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML_Activity_mine_ActivityParameterNode)

# Domain Model
domain_model = DomainModel(
    name="UML_Activity_mine",
    types={UML_Activity_mine_ActivityEdge, UML_Activity_mine_Element, UML_Activity_mine_Activity, Element, UML_Activity_mine_ActivityNode, UML_Activity_mine_ExpansionRegion, Action, UML_Activity_mine_ControlNode, ActivityNode, UML_Activity_mine_ObjectNode, UML_Activity_mine_Action, UML_Activity_mine_Fork, ControlNode, UML_Activity_mine_Join, UML_Activity_mine_ActivityInitialNode, UML_Activity_mine_ActivityFinalNode, UML_Activity_mine_DatastoreNode, ObjectNode, UML_Activity_mine_ActivityParameterNode, UML_Activity_mine_ExpansionNode, ExpansionMode, Status, Direction},
    associations={nodes0, edges1, target3, source4, incoming6, outgoing7, inputCollections9, outputCollections10, edges13, nodes16},
    generalizations={gen_UML_Activity_mine_ActivityEdge_Element, gen_UML_Activity_mine_ActivityNode_Element, gen_UML_Activity_mine_Activity_Element, gen_UML_Activity_mine_ExpansionNode_ObjectNode, gen_UML_Activity_mine_ExpansionRegion_Action, gen_UML_Activity_mine_ControlNode_ActivityNode, gen_UML_Activity_mine_ObjectNode_ActivityNode, gen_UML_Activity_mine_Action_ActivityNode, gen_UML_Activity_mine_Fork_ControlNode, gen_UML_Activity_mine_Join_ControlNode, gen_UML_Activity_mine_ActivityInitialNode_ControlNode, gen_UML_Activity_mine_ActivityFinalNode_ControlNode, gen_UML_Activity_mine_DatastoreNode_ObjectNode, gen_UML_Activity_mine_ActivityParameterNode_ObjectNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)