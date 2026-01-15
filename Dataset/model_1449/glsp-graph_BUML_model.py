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
GSide: Enumeration = Enumeration(
    name="GSide",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="on")
    }
)

GSeverity: Enumeration = Enumeration(
    name="GSeverity",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="info")
    }
)

# Classes
graph_GModelElement = Class(name="graph::GModelElement", is_abstract=True)
graph_GShapeElement = Class(name="graph::GShapeElement", is_abstract=True)
GModelElement = Class(name="GModelElement")
GBoundsAware = Class(name="GBoundsAware")
graph_GGraph = Class(name="graph::GGraph")
GModelRoot = Class(name="GModelRoot")
graph_GLayoutOptions = Class(name="graph::GLayoutOptions")
graph_GModelRoot = Class(name="graph::GModelRoot")
graph_GBounds = Class(name="graph::GBounds")
graph_GNode = Class(name="graph::GNode")
GShapeElement = Class(name="GShapeElement")
GEdgeLayoutable = Class(name="GEdgeLayoutable")
GLayouting = Class(name="GLayouting")
graph_GEdge = Class(name="graph::GEdge")
graph_GPoint = Class(name="graph::GPoint")
graph_GIssueMarker = Class(name="graph::GIssueMarker")
graph_GIssue = Class(name="graph::GIssue")
graph_GPort = Class(name="graph::GPort")
graph_GButton = Class(name="graph::GButton")
graph_GBoundsAware = Class(name="graph::GBoundsAware", is_abstract=True)
graph_GDimension = Class(name="graph::GDimension")
graph_GCompartment = Class(name="graph::GCompartment")
graph_GLabel = Class(name="graph::GLabel")
GAlignable = Class(name="GAlignable")
graph_GEdgeLayoutable = Class(name="graph::GEdgeLayoutable", is_abstract=True)
graph_GEdgePlacement = Class(name="graph::GEdgePlacement")
graph_GLayouting = Class(name="graph::GLayouting", is_abstract=True)
graph_GAlignable = Class(name="graph::GAlignable")
graph_GHtmlRoot = Class(name="graph::GHtmlRoot")
graph_GPreRenderedElement = Class(name="graph::GPreRenderedElement")

# graph_GModelElement class attributes and methods
graph_GModelElement_id: Property = Property(name="id", type=StringType)
graph_GModelElement_trace: Property = Property(name="trace", type=StringType)
graph_GModelElement_type: Property = Property(name="type", type=StringType)
graph_GModelElement_cssClasses: Property = Property(name="cssClasses", type=StringType)
graph_GModelElement.attributes={graph_GModelElement_cssClasses, graph_GModelElement_id, graph_GModelElement_type, graph_GModelElement_trace}

# graph_GShapeElement class attributes and methods

# GModelElement class attributes and methods

# GBoundsAware class attributes and methods

# graph_GGraph class attributes and methods

# GModelRoot class attributes and methods

# graph_GLayoutOptions class attributes and methods
graph_GLayoutOptions_paddingLeft: Property = Property(name="paddingLeft", type=StringType)
graph_GLayoutOptions_paddingRight: Property = Property(name="paddingRight", type=StringType)
graph_GLayoutOptions_paddingTop: Property = Property(name="paddingTop", type=StringType)
graph_GLayoutOptions_paddingBottom: Property = Property(name="paddingBottom", type=StringType)
graph_GLayoutOptions_paddingFactor: Property = Property(name="paddingFactor", type=StringType)
graph_GLayoutOptions_resizeContainer: Property = Property(name="resizeContainer", type=BooleanType)
graph_GLayoutOptions_vGap: Property = Property(name="vGap", type=StringType)
graph_GLayoutOptions_hGap: Property = Property(name="hGap", type=StringType)
graph_GLayoutOptions_vAlign: Property = Property(name="vAlign", type=StringType)
graph_GLayoutOptions_hAlign: Property = Property(name="hAlign", type=StringType)
graph_GLayoutOptions_minWidth: Property = Property(name="minWidth", type=StringType)
graph_GLayoutOptions_minHeight: Property = Property(name="minHeight", type=StringType)
graph_GLayoutOptions.attributes={graph_GLayoutOptions_paddingBottom, graph_GLayoutOptions_vAlign, graph_GLayoutOptions_vGap, graph_GLayoutOptions_minHeight, graph_GLayoutOptions_paddingRight, graph_GLayoutOptions_hGap, graph_GLayoutOptions_resizeContainer, graph_GLayoutOptions_paddingLeft, graph_GLayoutOptions_minWidth, graph_GLayoutOptions_paddingTop, graph_GLayoutOptions_hAlign, graph_GLayoutOptions_paddingFactor}

# graph_GModelRoot class attributes and methods
graph_GModelRoot_revision: Property = Property(name="revision", type=IntegerType)
graph_GModelRoot.attributes={graph_GModelRoot_revision}

# graph_GBounds class attributes and methods
graph_GBounds_x: Property = Property(name="x", type=FloatType)
graph_GBounds_y: Property = Property(name="y", type=FloatType)
graph_GBounds_width: Property = Property(name="width", type=FloatType)
graph_GBounds_height: Property = Property(name="height", type=FloatType)
graph_GBounds.attributes={graph_GBounds_x, graph_GBounds_y, graph_GBounds_height, graph_GBounds_width}

# graph_GNode class attributes and methods

# GShapeElement class attributes and methods

# GEdgeLayoutable class attributes and methods

# GLayouting class attributes and methods

# graph_GEdge class attributes and methods
graph_GEdge_sourceId: Property = Property(name="sourceId", type=StringType)
graph_GEdge_targetId: Property = Property(name="targetId", type=StringType)
graph_GEdge.attributes={graph_GEdge_targetId, graph_GEdge_sourceId}

# graph_GPoint class attributes and methods
graph_GPoint_x: Property = Property(name="x", type=FloatType)
graph_GPoint_y: Property = Property(name="y", type=FloatType)
graph_GPoint.attributes={graph_GPoint_x, graph_GPoint_y}

# graph_GIssueMarker class attributes and methods

# graph_GIssue class attributes and methods
graph_GIssue_severity: Property = Property(name="severity", type=StringType)
graph_GIssue_message: Property = Property(name="message", type=StringType)
graph_GIssue.attributes={graph_GIssue_message, graph_GIssue_severity}

# graph_GPort class attributes and methods

# graph_GButton class attributes and methods
graph_GButton_enabled: Property = Property(name="enabled", type=BooleanType)
graph_GButton.attributes={graph_GButton_enabled}

# graph_GBoundsAware class attributes and methods

# graph_GDimension class attributes and methods
graph_GDimension_width: Property = Property(name="width", type=FloatType)
graph_GDimension_height: Property = Property(name="height", type=FloatType)
graph_GDimension.attributes={graph_GDimension_height, graph_GDimension_width}

# graph_GCompartment class attributes and methods

# graph_GLabel class attributes and methods
graph_GLabel_text: Property = Property(name="text", type=StringType)
graph_GLabel.attributes={graph_GLabel_text}

# GAlignable class attributes and methods

# graph_GEdgeLayoutable class attributes and methods

# graph_GEdgePlacement class attributes and methods
graph_GEdgePlacement_position: Property = Property(name="position", type=StringType)
graph_GEdgePlacement_offset: Property = Property(name="offset", type=StringType)
graph_GEdgePlacement_side: Property = Property(name="side", type=StringType)
graph_GEdgePlacement.attributes={graph_GEdgePlacement_position, graph_GEdgePlacement_side, graph_GEdgePlacement_offset}

# graph_GLayouting class attributes and methods
graph_GLayouting_layout: Property = Property(name="layout", type=StringType)
graph_GLayouting.attributes={graph_GLayouting_layout}

# graph_GAlignable class attributes and methods

# graph_GHtmlRoot class attributes and methods
graph_GHtmlRoot_classes: Property = Property(name="classes", type=StringType)
graph_GHtmlRoot.attributes={graph_GHtmlRoot_classes}

# graph_GPreRenderedElement class attributes and methods
graph_GPreRenderedElement_code: Property = Property(name="code", type=StringType)
graph_GPreRenderedElement.attributes={graph_GPreRenderedElement_code}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="2", type=graph_GModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=graph_GModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="6", type=graph_GModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=graph_GModelElement, multiplicity=Multiplicity(0, 1))
    }
)
layoutOptions7: BinaryAssociation = BinaryAssociation(
    name="layoutOptions7",
    ends={
        Property(name="graph_GLayoutOptions", type=graph_GGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GGraph", type=graph_GLayoutOptions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
canvasBounds8: BinaryAssociation = BinaryAssociation(
    name="canvasBounds8",
    ends={
        Property(name="graph_GBounds", type=graph_GModelRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GModelRoot", type=graph_GBounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
routingPoints9: BinaryAssociation = BinaryAssociation(
    name="routingPoints9",
    ends={
        Property(name="graph_GPoint", type=graph_GEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GEdge", type=graph_GPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
issues15: BinaryAssociation = BinaryAssociation(
    name="issues15",
    ends={
        Property(name="graph_GIssue", type=graph_GIssueMarker, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GIssueMarker", type=graph_GIssue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position16: BinaryAssociation = BinaryAssociation(
    name="position16",
    ends={
        Property(name="graph_GPoint17", type=graph_GBoundsAware, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GBoundsAware", type=graph_GPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size18: BinaryAssociation = BinaryAssociation(
    name="size18",
    ends={
        Property(name="graph_GDimension", type=graph_GBoundsAware, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GBoundsAware19", type=graph_GDimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="graph_GModelElement", type=graph_GEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GEdge11", type=graph_GModelElement, multiplicity=Multiplicity(0, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="graph_GModelElement14", type=graph_GEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GEdge13", type=graph_GModelElement, multiplicity=Multiplicity(0, 1))
    }
)
edgePlacement20: BinaryAssociation = BinaryAssociation(
    name="edgePlacement20",
    ends={
        Property(name="graph_GEdgePlacement", type=graph_GEdgeLayoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GEdgeLayoutable", type=graph_GEdgePlacement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layoutOptions21: BinaryAssociation = BinaryAssociation(
    name="layoutOptions21",
    ends={
        Property(name="graph_GLayoutOptions22", type=graph_GLayouting, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GLayouting", type=graph_GLayoutOptions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alignment23: BinaryAssociation = BinaryAssociation(
    name="alignment23",
    ends={
        Property(name="graph_GPoint24", type=graph_GAlignable, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GAlignable", type=graph_GPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_graph_GShapeElement_GModelElement = Generalization(general=GModelElement, specific=graph_GShapeElement)
gen_graph_GShapeElement_GBoundsAware = Generalization(general=GBoundsAware, specific=graph_GShapeElement)
gen_graph_GGraph_GModelRoot = Generalization(general=GModelRoot, specific=graph_GGraph)
gen_graph_GGraph_GBoundsAware = Generalization(general=GBoundsAware, specific=graph_GGraph)
gen_graph_GModelRoot_GModelElement = Generalization(general=GModelElement, specific=graph_GModelRoot)
gen_graph_GNode_GShapeElement = Generalization(general=GShapeElement, specific=graph_GNode)
gen_graph_GNode_GEdgeLayoutable = Generalization(general=GEdgeLayoutable, specific=graph_GNode)
gen_graph_GNode_GLayouting = Generalization(general=GLayouting, specific=graph_GNode)
gen_graph_GEdge_GModelElement = Generalization(general=GModelElement, specific=graph_GEdge)
gen_graph_GIssueMarker_GShapeElement = Generalization(general=GShapeElement, specific=graph_GIssueMarker)
gen_graph_GPort_GShapeElement = Generalization(general=GShapeElement, specific=graph_GPort)
gen_graph_GButton_GShapeElement = Generalization(general=GShapeElement, specific=graph_GButton)
gen_graph_GCompartment_GShapeElement = Generalization(general=GShapeElement, specific=graph_GCompartment)
gen_graph_GCompartment_GLayouting = Generalization(general=GLayouting, specific=graph_GCompartment)
gen_graph_GLabel_GAlignable = Generalization(general=GAlignable, specific=graph_GLabel)
gen_graph_GLabel_GEdgeLayoutable = Generalization(general=GEdgeLayoutable, specific=graph_GLabel)
gen_graph_GLabel_GShapeElement = Generalization(general=GShapeElement, specific=graph_GLabel)
gen_graph_GHtmlRoot_GModelRoot = Generalization(general=GModelRoot, specific=graph_GHtmlRoot)
gen_graph_GPreRenderedElement_GModelElement = Generalization(general=GModelElement, specific=graph_GPreRenderedElement)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_GModelElement, graph_GShapeElement, GModelElement, GBoundsAware, graph_GGraph, GModelRoot, graph_GLayoutOptions, graph_GModelRoot, graph_GBounds, graph_GNode, GShapeElement, GEdgeLayoutable, GLayouting, graph_GEdge, graph_GPoint, graph_GIssueMarker, graph_GIssue, graph_GPort, graph_GButton, graph_GBoundsAware, graph_GDimension, graph_GCompartment, graph_GLabel, GAlignable, graph_GEdgeLayoutable, graph_GEdgePlacement, graph_GLayouting, graph_GAlignable, graph_GHtmlRoot, graph_GPreRenderedElement, GSide, GSeverity},
    associations={children1, parent4, layoutOptions7, canvasBounds8, routingPoints9, issues15, position16, size18, source10, target12, edgePlacement20, layoutOptions21, alignment23},
    generalizations={gen_graph_GShapeElement_GModelElement, gen_graph_GShapeElement_GBoundsAware, gen_graph_GGraph_GModelRoot, gen_graph_GGraph_GBoundsAware, gen_graph_GModelRoot_GModelElement, gen_graph_GNode_GShapeElement, gen_graph_GNode_GEdgeLayoutable, gen_graph_GNode_GLayouting, gen_graph_GEdge_GModelElement, gen_graph_GIssueMarker_GShapeElement, gen_graph_GPort_GShapeElement, gen_graph_GButton_GShapeElement, gen_graph_GCompartment_GShapeElement, gen_graph_GCompartment_GLayouting, gen_graph_GLabel_GAlignable, gen_graph_GLabel_GEdgeLayoutable, gen_graph_GLabel_GShapeElement, gen_graph_GHtmlRoot_GModelRoot, gen_graph_GPreRenderedElement_GModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)