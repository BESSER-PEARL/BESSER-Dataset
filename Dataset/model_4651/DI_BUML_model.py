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
di_Style = Class(name="di::Style", is_abstract=True)
di_EObject = Class(name="di::EObject")
di_Edge = Class(name="di::Edge", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
di_DiagramElement = Class(name="di::DiagramElement", is_abstract=True)
di_Point = Class(name="di::Point")
di_Diagram = Class(name="di::Diagram", is_abstract=True)
Shape = Class(name="Shape")
di_Shape = Class(name="di::Shape", is_abstract=True)
di_Bounds = Class(name="di::Bounds")
di_Fill = Class(name="di::Fill")
di_Color = Class(name="di::Color")

# di_Style class attributes and methods
di_Style_fontItalic: Property = Property(name="fontItalic", type=StringType)
di_Style_fontBold: Property = Property(name="fontBold", type=StringType)
di_Style_fontUnderline: Property = Property(name="fontUnderline", type=StringType)
di_Style_fontStrikeThrough: Property = Property(name="fontStrikeThrough", type=StringType)
di_Style_fillOpacity: Property = Property(name="fillOpacity", type=StringType)
di_Style_strokeWidth: Property = Property(name="strokeWidth", type=StringType)
di_Style_strokeOpacity: Property = Property(name="strokeOpacity", type=StringType)
di_Style_strokeDashLength: Property = Property(name="strokeDashLength", type=StringType)
di_Style_fontSize: Property = Property(name="fontSize", type=StringType)
di_Style_fontName: Property = Property(name="fontName", type=StringType)
di_Style_m_valid_fill_opacity: Method = Method(name="valid_fill_opacity", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
di_Style_m_valid_stroke_width: Method = Method(name="valid_stroke_width", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
di_Style_m_valid_font_size: Method = Method(name="valid_font_size", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
di_Style_m_valid_dash_length_size: Method = Method(name="valid_dash_length_size", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
di_Style_m_valid_stroke_opacity: Method = Method(name="valid_stroke_opacity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
di_Style.attributes={di_Style_fontStrikeThrough, di_Style_fillOpacity, di_Style_strokeWidth, di_Style_fontUnderline, di_Style_fontSize, di_Style_fontBold, di_Style_fontItalic, di_Style_strokeOpacity, di_Style_fontName, di_Style_strokeDashLength}
di_Style.methods={di_Style_m_valid_font_size, di_Style_m_valid_dash_length_size, di_Style_m_valid_fill_opacity, di_Style_m_valid_stroke_width, di_Style_m_valid_stroke_opacity}

# di_EObject class attributes and methods

# di_Edge class attributes and methods

# DiagramElement class attributes and methods

# di_DiagramElement class attributes and methods
di_DiagramElement_id: Property = Property(name="id", type=StringType)
di_DiagramElement.attributes={di_DiagramElement_id}

# di_Point class attributes and methods

# di_Diagram class attributes and methods
di_Diagram_name: Property = Property(name="name", type=StringType)
di_Diagram_documentation: Property = Property(name="documentation", type=StringType)
di_Diagram_resolution: Property = Property(name="resolution", type=StringType)
di_Diagram.attributes={di_Diagram_resolution, di_Diagram_documentation, di_Diagram_name}

# Shape class attributes and methods

# di_Shape class attributes and methods

# di_Bounds class attributes and methods

# di_Fill class attributes and methods

# di_Color class attributes and methods

# Relationships
localStyle5: BinaryAssociation = BinaryAssociation(
    name="localStyle5",
    ends={
        Property(name="di_Style", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiagramElement", type=di_Style, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sharedStyle6: BinaryAssociation = BinaryAssociation(
    name="sharedStyle6",
    ends={
        Property(name="di_Style8", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiagramElement7", type=di_Style, multiplicity=Multiplicity(0, 1))
    }
)
modelElement9: BinaryAssociation = BinaryAssociation(
    name="modelElement9",
    ends={
        Property(name="di_EObject", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiagramElement10", type=di_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="di_DiagramElement12", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge", type=di_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
owningElement1: BinaryAssociation = BinaryAssociation(
    name="owningElement1",
    ends={
        Property(name="DiagramElement", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=di_DiagramElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement3: BinaryAssociation = BinaryAssociation(
    name="ownedElement3",
    ends={
        Property(name="DiagramElement4", type=di_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement", type=di_DiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="di_DiagramElement15", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge14", type=di_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
waypoint16: BinaryAssociation = BinaryAssociation(
    name="waypoint16",
    ends={
        Property(name="di_Point", type=di_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Edge17", type=di_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bounds18: BinaryAssociation = BinaryAssociation(
    name="bounds18",
    ends={
        Property(name="di_Bounds", type=di_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Shape", type=di_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill19: BinaryAssociation = BinaryAssociation(
    name="fill19",
    ends={
        Property(name="di_Fill", type=di_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Style20", type=di_Fill, multiplicity=Multiplicity(0, 1))
    }
)
fillColor21: BinaryAssociation = BinaryAssociation(
    name="fillColor21",
    ends={
        Property(name="di_Color", type=di_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Style22", type=di_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
strokeColor23: BinaryAssociation = BinaryAssociation(
    name="strokeColor23",
    ends={
        Property(name="di_Color25", type=di_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Style24", type=di_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fontColor26: BinaryAssociation = BinaryAssociation(
    name="fontColor26",
    ends={
        Property(name="di_Color28", type=di_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Style27", type=di_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_di_Edge_DiagramElement = Generalization(general=DiagramElement, specific=di_Edge)
gen_di_Diagram_Shape = Generalization(general=Shape, specific=di_Diagram)
gen_di_Shape_DiagramElement = Generalization(general=DiagramElement, specific=di_Shape)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={di_Style, di_EObject, di_Edge, DiagramElement, di_DiagramElement, di_Point, di_Diagram, Shape, di_Shape, di_Bounds, di_Fill, di_Color},
    associations={localStyle5, sharedStyle6, modelElement9, source11, owningElement1, ownedElement3, target13, waypoint16, bounds18, fill19, fillColor21, strokeColor23, fontColor26},
    generalizations={gen_di_Edge_DiagramElement, gen_di_Diagram_Shape, gen_di_Shape_DiagramElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)