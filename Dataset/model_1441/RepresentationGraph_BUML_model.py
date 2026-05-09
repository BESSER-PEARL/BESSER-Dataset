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
RepresentationGraph_Circle = Class(name="RepresentationGraph_Circle")
ContainerElement = Class(name="ContainerElement")
RepresentationGraph_Rectangle = Class(name="RepresentationGraph_Rectangle")
RepresentationGraph_ContainerElement = Class(name="RepresentationGraph_ContainerElement", is_abstract=True)
RepresentationGraph_Rhombus = Class(name="RepresentationGraph_Rhombus")
RepresentationGraph_Diagram = Class(name="RepresentationGraph_Diagram")
RepresentationGraph_GraphicElement = Class(name="RepresentationGraph_GraphicElement", is_abstract=True)
RepresentationGraph_EdgeElement = Class(name="RepresentationGraph_EdgeElement")
GraphicElement = Class(name="GraphicElement")
RepresentationGraph_NodeElement = Class(name="RepresentationGraph_NodeElement", is_abstract=True)
RepresentationGraph_IconElement = Class(name="RepresentationGraph_IconElement")
NodeElement = Class(name="NodeElement")

# RepresentationGraph_Circle class attributes and methods
RepresentationGraph_Circle_radius: Property = Property(name="radius", type=StringType)
RepresentationGraph_Circle.attributes={RepresentationGraph_Circle_radius}

# ContainerElement class attributes and methods

# RepresentationGraph_Rectangle class attributes and methods
RepresentationGraph_Rectangle_width: Property = Property(name="width", type=StringType)
RepresentationGraph_Rectangle_height: Property = Property(name="height", type=StringType)
RepresentationGraph_Rectangle.attributes={RepresentationGraph_Rectangle_height, RepresentationGraph_Rectangle_width}

# RepresentationGraph_ContainerElement class attributes and methods

# RepresentationGraph_Rhombus class attributes and methods
RepresentationGraph_Rhombus_width: Property = Property(name="width", type=StringType)
RepresentationGraph_Rhombus_height: Property = Property(name="height", type=StringType)
RepresentationGraph_Rhombus.attributes={RepresentationGraph_Rhombus_width, RepresentationGraph_Rhombus_height}

# RepresentationGraph_Diagram class attributes and methods

# RepresentationGraph_GraphicElement class attributes and methods
RepresentationGraph_GraphicElement_color: Property = Property(name="color", type=StringType)
RepresentationGraph_GraphicElement_paletteName: Property = Property(name="paletteName", type=StringType)
RepresentationGraph_GraphicElement_paletteIconPath: Property = Property(name="paletteIconPath", type=StringType)
RepresentationGraph_GraphicElement.attributes={RepresentationGraph_GraphicElement_paletteIconPath, RepresentationGraph_GraphicElement_color, RepresentationGraph_GraphicElement_paletteName}

# RepresentationGraph_EdgeElement class attributes and methods

# GraphicElement class attributes and methods

# RepresentationGraph_NodeElement class attributes and methods
RepresentationGraph_NodeElement_label: Property = Property(name="label", type=StringType)
RepresentationGraph_NodeElement.attributes={RepresentationGraph_NodeElement_label}

# RepresentationGraph_IconElement class attributes and methods
RepresentationGraph_IconElement_filepath: Property = Property(name="filepath", type=StringType)
RepresentationGraph_IconElement.attributes={RepresentationGraph_IconElement_filepath}

# NodeElement class attributes and methods

# Relationships
contains8: BinaryAssociation = BinaryAssociation(
    name="contains8",
    ends={
        Property(name="RepresentationGraph_NodeElement9", type=RepresentationGraph_ContainerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationGraph_ContainerElement", type=RepresentationGraph_NodeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="RepresentationGraph_GraphicElement", type=RepresentationGraph_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationGraph_Diagram", type=RepresentationGraph_GraphicElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="RepresentationGraph_NodeElement", type=RepresentationGraph_EdgeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationGraph_EdgeElement", type=RepresentationGraph_NodeElement, multiplicity=Multiplicity(1, 1))
    }
)
target2: BinaryAssociation = BinaryAssociation(
    name="target2",
    ends={
        Property(name="RepresentationGraph_NodeElement4", type=RepresentationGraph_EdgeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationGraph_EdgeElement3", type=RepresentationGraph_NodeElement, multiplicity=Multiplicity(1, 1))
    }
)
link6: BinaryAssociation = BinaryAssociation(
    name="link6",
    ends={
        Property(name="RepresentationGraph_NodeElement7", type=RepresentationGraph_NodeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationGraph_NodeElement5", type=RepresentationGraph_NodeElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_RepresentationGraph_Circle_ContainerElement = Generalization(general=ContainerElement, specific=RepresentationGraph_Circle)
gen_RepresentationGraph_Rectangle_ContainerElement = Generalization(general=ContainerElement, specific=RepresentationGraph_Rectangle)
gen_RepresentationGraph_ContainerElement_NodeElement = Generalization(general=NodeElement, specific=RepresentationGraph_ContainerElement)
gen_RepresentationGraph_Rhombus_ContainerElement = Generalization(general=ContainerElement, specific=RepresentationGraph_Rhombus)
gen_RepresentationGraph_EdgeElement_GraphicElement = Generalization(general=GraphicElement, specific=RepresentationGraph_EdgeElement)
gen_RepresentationGraph_NodeElement_GraphicElement = Generalization(general=GraphicElement, specific=RepresentationGraph_NodeElement)
gen_RepresentationGraph_IconElement_NodeElement = Generalization(general=NodeElement, specific=RepresentationGraph_IconElement)

# Domain Model
domain_model = DomainModel(
    name="RepresentationGraph",
    types={RepresentationGraph_Circle, ContainerElement, RepresentationGraph_Rectangle, RepresentationGraph_ContainerElement, RepresentationGraph_Rhombus, RepresentationGraph_Diagram, RepresentationGraph_GraphicElement, RepresentationGraph_EdgeElement, GraphicElement, RepresentationGraph_NodeElement, RepresentationGraph_IconElement, NodeElement},
    associations={contains8, elements0, source1, target2, link6},
    generalizations={gen_RepresentationGraph_Circle_ContainerElement, gen_RepresentationGraph_Rectangle_ContainerElement, gen_RepresentationGraph_ContainerElement_NodeElement, gen_RepresentationGraph_Rhombus_ContainerElement, gen_RepresentationGraph_EdgeElement_GraphicElement, gen_RepresentationGraph_NodeElement_GraphicElement, gen_RepresentationGraph_IconElement_NodeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)