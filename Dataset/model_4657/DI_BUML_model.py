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
di_Point = Class(name="di::Point")
di_Shape = Class(name="di::Shape", is_abstract=True)
Node = Class(name="Node")
di_Bounds = Class(name="di::Bounds")
di_LabeledEdge = Class(name="di::LabeledEdge", is_abstract=True)
Edge = Class(name="Edge")
di_DiagramElement = Class(name="di::DiagramElement", is_abstract=True)
di_Diagram = Class(name="di::Diagram", is_abstract=True)
di_EObject = Class(name="di::EObject")
di_Style = Class(name="di::Style", is_abstract=True)
di_Node = Class(name="di::Node", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
di_Edge = Class(name="di::Edge", is_abstract=True)
di_Label = Class(name="di::Label", is_abstract=True)
di_LabeledShape = Class(name="di::LabeledShape", is_abstract=True)
Shape = Class(name="Shape")
di_Plane = Class(name="di::Plane", is_abstract=True)

# di_Point class attributes and methods

# di_Shape class attributes and methods

# Node class attributes and methods

# di_Bounds class attributes and methods

# di_LabeledEdge class attributes and methods

# Edge class attributes and methods

# di_DiagramElement class attributes and methods

# di_Diagram class attributes and methods
di_Diagram_name: Property = Property(name="name", type=StringType)
di_Diagram_documentation: Property = Property(name="documentation", type=StringType)
di_Diagram_resolution: Property = Property(name="resolution", type=FloatType)
di_Diagram.attributes={di_Diagram_name, di_Diagram_resolution, di_Diagram_documentation}

# di_EObject class attributes and methods

# di_Style class attributes and methods

# di_Node class attributes and methods

# DiagramElement class attributes and methods

# di_Edge class attributes and methods

# di_Label class attributes and methods

# di_LabeledShape class attributes and methods

# Shape class attributes and methods

# di_Plane class attributes and methods
di_Plane_m_plane_element_type: Method = Method(name="plane_element_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
di_Plane.methods={di_Plane_m_plane_element_type}

# Relationships
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="di_DiagramElement17", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge16", type=di_DiagramElement, multiplicity=Multiplicity(0, 1))
    }
)
waypoint18: BinaryAssociation = BinaryAssociation(
    name="waypoint18",
    ends={
        Property(name="di_Point", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge19", type=di_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
bounds20: BinaryAssociation = BinaryAssociation(
    name="bounds20",
    ends={
        Property(name="di_Bounds", type=di_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Shape", type=di_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningDiagram0: BinaryAssociation = BinaryAssociation(
    name="owningDiagram0",
    ends={
        Property(name="Diagram", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rootElement", type=di_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
owningElement2: BinaryAssociation = BinaryAssociation(
    name="owningElement2",
    ends={
        Property(name="DiagramElement", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=di_DiagramElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement4: BinaryAssociation = BinaryAssociation(
    name="ownedElement4",
    ends={
        Property(name="DiagramElement5", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement", type=di_DiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
modelElement6: BinaryAssociation = BinaryAssociation(
    name="modelElement6",
    ends={
        Property(name="di_EObject", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiagramElement", type=di_EObject, multiplicity=Multiplicity(0, 1))
    }
)
style7: BinaryAssociation = BinaryAssociation(
    name="style7",
    ends={
        Property(name="di_Style", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiagramElement8", type=di_Style, multiplicity=Multiplicity(0, 1))
    }
)
ownedStyle9: BinaryAssociation = BinaryAssociation(
    name="ownedStyle9",
    ends={
        Property(name="di_Style10", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram", type=di_Style, multiplicity=Multiplicity(0, 9999))
    }
)
rootElement11: BinaryAssociation = BinaryAssociation(
    name="rootElement11",
    ends={
        Property(name="DiagramElement12", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="owningDiagram", type=di_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="di_DiagramElement14", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge", type=di_DiagramElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedLabel21: BinaryAssociation = BinaryAssociation(
    name="ownedLabel21",
    ends={
        Property(name="di_Label", type=di_LabeledEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_LabeledEdge", type=di_Label, multiplicity=Multiplicity(0, 9999))
    }
)
bounds22: BinaryAssociation = BinaryAssociation(
    name="bounds22",
    ends={
        Property(name="di_Bounds24", type=di_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Label23", type=di_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLabel25: BinaryAssociation = BinaryAssociation(
    name="ownedLabel25",
    ends={
        Property(name="di_Label26", type=di_LabeledShape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_LabeledShape", type=di_Label, multiplicity=Multiplicity(0, 9999))
    }
)
planeElement27: BinaryAssociation = BinaryAssociation(
    name="planeElement27",
    ends={
        Property(name="di_DiagramElement28", type=di_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Plane", type=di_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_di_Shape_Node = Generalization(general=Node, specific=di_Shape)
gen_di_LabeledEdge_Edge = Generalization(general=Edge, specific=di_LabeledEdge)
gen_di_Node_DiagramElement = Generalization(general=DiagramElement, specific=di_Node)
gen_di_Edge_DiagramElement = Generalization(general=DiagramElement, specific=di_Edge)
gen_di_Label_Node = Generalization(general=Node, specific=di_Label)
gen_di_LabeledShape_Shape = Generalization(general=Shape, specific=di_LabeledShape)
gen_di_Plane_Node = Generalization(general=Node, specific=di_Plane)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={di_Point, di_Shape, Node, di_Bounds, di_LabeledEdge, Edge, di_DiagramElement, di_Diagram, di_EObject, di_Style, di_Node, DiagramElement, di_Edge, di_Label, di_LabeledShape, Shape, di_Plane},
    associations={target15, waypoint18, bounds20, owningDiagram0, owningElement2, ownedElement4, modelElement6, style7, ownedStyle9, rootElement11, source13, ownedLabel21, bounds22, ownedLabel25, planeElement27},
    generalizations={gen_di_Shape_Node, gen_di_LabeledEdge_Edge, gen_di_Node_DiagramElement, gen_di_Edge_DiagramElement, gen_di_Label_Node, gen_di_LabeledShape_Shape, gen_di_Plane_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)