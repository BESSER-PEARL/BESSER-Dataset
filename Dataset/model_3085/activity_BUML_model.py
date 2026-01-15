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
ObjectNodeKind: Enumeration = Enumeration(
    name="ObjectNodeKind",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="NoBuffer"),
			EnumerationLiteral(name="Overwrite")
    }
)

ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="ordered"),
			EnumerationLiteral(name="unordered")
    }
)

# Classes
activity_ValueSpecification = Class(name="activity::ValueSpecification")
activity_ActivityNode = Class(name="activity::ActivityNode", is_abstract=True)
activity_AbstractActivity = Class(name="activity::AbstractActivity", is_abstract=True)
AbstractBehavior = Class(name="AbstractBehavior")
TraceableElement = Class(name="TraceableElement")
activity_ActivityEdge = Class(name="activity::ActivityEdge", is_abstract=True)
ModelElement = Class(name="ModelElement")
activity_AbstractAction = Class(name="activity::AbstractAction", is_abstract=True)
activity_ObjectFlow = Class(name="activity::ObjectFlow", is_abstract=True)
ActivityEdge = Class(name="ActivityEdge")
activity_ActivityPartition = Class(name="activity::ActivityPartition", is_abstract=True)
AbstractNamedElement = Class(name="AbstractNamedElement")
activity_IState = Class(name="activity::IState")
activity_AbstractBehavior = Class(name="activity::AbstractBehavior")
ActivityNode = Class(name="ActivityNode")
activity_InputPin = Class(name="activity::InputPin", is_abstract=True)
activity_OutputPin = Class(name="activity::OutputPin", is_abstract=True)
activity_AcceptEventAction = Class(name="activity::AcceptEventAction", is_abstract=True)
AbstractAction = Class(name="AbstractAction")
activity_ObjectNode = Class(name="activity::ObjectNode", is_abstract=True)
activity_Pin = Class(name="activity::Pin", is_abstract=True)
ObjectNode = Class(name="ObjectNode")
Pin = Class(name="Pin")

# activity_ValueSpecification class attributes and methods

# activity_ActivityNode class attributes and methods

# activity_AbstractActivity class attributes and methods
activity_AbstractActivity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
activity_AbstractActivity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
activity_AbstractActivity.attributes={activity_AbstractActivity_isSingleExecution, activity_AbstractActivity_isReadOnly}

# AbstractBehavior class attributes and methods

# TraceableElement class attributes and methods

# activity_ActivityEdge class attributes and methods
activity_ActivityEdge_kindOfRate: Property = Property(name="kindOfRate", type=StringType)
activity_ActivityEdge.attributes={activity_ActivityEdge_kindOfRate}

# ModelElement class attributes and methods

# activity_AbstractAction class attributes and methods

# activity_ObjectFlow class attributes and methods
activity_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
activity_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
activity_ObjectFlow.attributes={activity_ObjectFlow_isMulticast, activity_ObjectFlow_isMultireceive}

# ActivityEdge class attributes and methods

# activity_ActivityPartition class attributes and methods
activity_ActivityPartition_isDimension: Property = Property(name="isDimension", type=BooleanType)
activity_ActivityPartition_isExternal: Property = Property(name="isExternal", type=BooleanType)
activity_ActivityPartition.attributes={activity_ActivityPartition_isExternal, activity_ActivityPartition_isDimension}

# AbstractNamedElement class attributes and methods

# activity_IState class attributes and methods

# activity_AbstractBehavior class attributes and methods

# ActivityNode class attributes and methods

# activity_InputPin class attributes and methods

# activity_OutputPin class attributes and methods

# activity_AcceptEventAction class attributes and methods
activity_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=BooleanType)
activity_AcceptEventAction.attributes={activity_AcceptEventAction_isUnmarshall}

# AbstractAction class attributes and methods

# activity_ObjectNode class attributes and methods
activity_ObjectNode_isControlType: Property = Property(name="isControlType", type=BooleanType)
activity_ObjectNode_kindOfNode: Property = Property(name="kindOfNode", type=StringType)
activity_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
activity_ObjectNode.attributes={activity_ObjectNode_isControlType, activity_ObjectNode_kindOfNode, activity_ObjectNode_ordering}

# activity_Pin class attributes and methods
activity_Pin_isControl: Property = Property(name="isControl", type=BooleanType)
activity_Pin.attributes={activity_Pin_isControl}

# ObjectNode class attributes and methods

# Pin class attributes and methods

# Relationships
rate0: BinaryAssociation = BinaryAssociation(
    name="rate0",
    ends={
        Property(name="activity_ValueSpecification", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityEdge", type=activity_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
probability1: BinaryAssociation = BinaryAssociation(
    name="probability1",
    ends={
        Property(name="activity_ValueSpecification3", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityEdge2", type=activity_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="activity_ActivityNode", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityEdge5", type=activity_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="activity_ActivityNode8", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityEdge7", type=activity_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
outgoing15: BinaryAssociation = BinaryAssociation(
    name="outgoing15",
    ends={
        Property(name="activity_ActivityEdge17", type=activity_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityNode16", type=activity_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming18: BinaryAssociation = BinaryAssociation(
    name="incoming18",
    ends={
        Property(name="activity_ActivityEdge20", type=activity_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityNode19", type=activity_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
guard9: BinaryAssociation = BinaryAssociation(
    name="guard9",
    ends={
        Property(name="activity_ValueSpecification11", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityEdge10", type=activity_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
weight12: BinaryAssociation = BinaryAssociation(
    name="weight12",
    ends={
        Property(name="activity_ValueSpecification14", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityEdge13", type=activity_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound24: BinaryAssociation = BinaryAssociation(
    name="upperBound24",
    ends={
        Property(name="activity_ValueSpecification25", type=activity_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ObjectNode", type=activity_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inState26: BinaryAssociation = BinaryAssociation(
    name="inState26",
    ends={
        Property(name="activity_IState", type=activity_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ObjectNode27", type=activity_IState, multiplicity=Multiplicity(0, 9999))
    }
)
selection28: BinaryAssociation = BinaryAssociation(
    name="selection28",
    ends={
        Property(name="activity_AbstractBehavior", type=activity_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ObjectNode29", type=activity_AbstractBehavior, multiplicity=Multiplicity(0, 1))
    }
)
inputs21: BinaryAssociation = BinaryAssociation(
    name="inputs21",
    ends={
        Property(name="activity_InputPin", type=activity_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_AbstractAction", type=activity_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs22: BinaryAssociation = BinaryAssociation(
    name="outputs22",
    ends={
        Property(name="activity_OutputPin", type=activity_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_AbstractAction23", type=activity_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_activity_AbstractActivity_AbstractBehavior = Generalization(general=AbstractBehavior, specific=activity_AbstractActivity)
gen_activity_AbstractActivity_TraceableElement = Generalization(general=TraceableElement, specific=activity_AbstractActivity)
gen_activity_ActivityEdge_ModelElement = Generalization(general=ModelElement, specific=activity_ActivityEdge)
gen_activity_ActivityNode_AbstractNamedElement = Generalization(general=AbstractNamedElement, specific=activity_ActivityNode)
gen_activity_AbstractAction_AbstractNamedElement = Generalization(general=AbstractNamedElement, specific=activity_AbstractAction)
gen_activity_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activity_ObjectFlow)
gen_activity_ActivityPartition_AbstractNamedElement = Generalization(general=AbstractNamedElement, specific=activity_ActivityPartition)
gen_activity_ActivityPartition_ModelElement = Generalization(general=ModelElement, specific=activity_ActivityPartition)
gen_activity_AbstractAction_ActivityNode = Generalization(general=ActivityNode, specific=activity_AbstractAction)
gen_activity_AcceptEventAction_AbstractAction = Generalization(general=AbstractAction, specific=activity_AcceptEventAction)
gen_activity_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=activity_ObjectNode)
gen_activity_ObjectNode_AbstractNamedElement = Generalization(general=AbstractNamedElement, specific=activity_ObjectNode)
gen_activity_Pin_ObjectNode = Generalization(general=ObjectNode, specific=activity_Pin)
gen_activity_InputPin_Pin = Generalization(general=Pin, specific=activity_InputPin)
gen_activity_OutputPin_Pin = Generalization(general=Pin, specific=activity_OutputPin)

# Domain Model
domain_model = DomainModel(
    name="activity",
    types={activity_ValueSpecification, activity_ActivityNode, activity_AbstractActivity, AbstractBehavior, TraceableElement, activity_ActivityEdge, ModelElement, activity_AbstractAction, activity_ObjectFlow, ActivityEdge, activity_ActivityPartition, AbstractNamedElement, activity_IState, activity_AbstractBehavior, ActivityNode, activity_InputPin, activity_OutputPin, activity_AcceptEventAction, AbstractAction, activity_ObjectNode, activity_Pin, ObjectNode, Pin, ObjectNodeKind, ObjectNodeOrderingKind},
    associations={rate0, probability1, target4, source6, outgoing15, incoming18, guard9, weight12, upperBound24, inState26, selection28, inputs21, outputs22},
    generalizations={gen_activity_AbstractActivity_AbstractBehavior, gen_activity_AbstractActivity_TraceableElement, gen_activity_ActivityEdge_ModelElement, gen_activity_ActivityNode_AbstractNamedElement, gen_activity_AbstractAction_AbstractNamedElement, gen_activity_ObjectFlow_ActivityEdge, gen_activity_ActivityPartition_AbstractNamedElement, gen_activity_ActivityPartition_ModelElement, gen_activity_AbstractAction_ActivityNode, gen_activity_AcceptEventAction_AbstractAction, gen_activity_ObjectNode_ActivityNode, gen_activity_ObjectNode_AbstractNamedElement, gen_activity_Pin_ObjectNode, gen_activity_InputPin_Pin, gen_activity_OutputPin_Pin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)