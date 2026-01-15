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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Black"),
			EnumerationLiteral(name="Blue"),
			EnumerationLiteral(name="Cyan"),
			EnumerationLiteral(name="Gray"),
			EnumerationLiteral(name="Green"),
			EnumerationLiteral(name="Orange"),
			EnumerationLiteral(name="Red"),
			EnumerationLiteral(name="White"),
			EnumerationLiteral(name="Yellow")
    }
)

Brightness: Enumeration = Enumeration(
    name="Brightness",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Dark"),
			EnumerationLiteral(name="Light")
    }
)

FontStyle: Enumeration = Enumeration(
    name="FontStyle",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Bold"),
			EnumerationLiteral(name="Italic")
    }
)

NodeFigure: Enumeration = Enumeration(
    name="NodeFigure",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Ellipse"),
			EnumerationLiteral(name="Polygon"),
			EnumerationLiteral(name="Rectangle"),
			EnumerationLiteral(name="Rounded"),
			EnumerationLiteral(name="SVG"),
			EnumerationLiteral(name="Image")
    }
)

LinkFigure: Enumeration = Enumeration(
    name="LinkFigure",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Arrow"),
			EnumerationLiteral(name="ClosedArrow"),
			EnumerationLiteral(name="FilledClosedArrow"),
			EnumerationLiteral(name="Rhomb"),
			EnumerationLiteral(name="FilledRhomb"),
			EnumerationLiteral(name="Square"),
			EnumerationLiteral(name="FilledSquare"),
			EnumerationLiteral(name="None")
    }
)

Placement: Enumeration = Enumeration(
    name="Placement",
    literals={
            EnumerationLiteral(name="External"),
			EnumerationLiteral(name="Internal"),
			EnumerationLiteral(name="None")
    }
)

LayoutCompartment: Enumeration = Enumeration(
    name="LayoutCompartment",
    literals={
            EnumerationLiteral(name="Free"),
			EnumerationLiteral(name="List")
    }
)

Texture: Enumeration = Enumeration(
    name="Texture",
    literals={
            EnumerationLiteral(name="Solid"),
			EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Dash"),
			EnumerationLiteral(name="Dot")
    }
)

# Classes
cevinedit_CEViNEditRoot = Class(name="cevinedit::CEViNEditRoot")
cevinedit_Diagram = Class(name="cevinedit::Diagram")
cevinedit_PersonalizedElement = Class(name="cevinedit::PersonalizedElement", is_abstract=True)
cevinedit_LinkEClass = Class(name="cevinedit::LinkEClass")
Link = Class(name="Link")
cevinedit_CompartmentEReferenceCont = Class(name="cevinedit::CompartmentEReferenceCont")
cevinedit_AffixedEReferenceCont = Class(name="cevinedit::AffixedEReferenceCont")
cevinedit_LabelEAttribute = Class(name="cevinedit::LabelEAttribute")
cevinedit_LinkEReferenceNonCont = Class(name="cevinedit::LinkEReferenceNonCont")
cevinedit_Link = Class(name="cevinedit::Link", is_abstract=True)
cevinedit_NodeEClass = Class(name="cevinedit::NodeEClass")
PersonalizedElement = Class(name="PersonalizedElement")

# cevinedit_CEViNEditRoot class attributes and methods
cevinedit_CEViNEditRoot_sourceMM: Property = Property(name="sourceMM", type=StringType)
cevinedit_CEViNEditRoot.attributes={cevinedit_CEViNEditRoot_sourceMM}

# cevinedit_Diagram class attributes and methods
cevinedit_Diagram_name: Property = Property(name="name", type=StringType)
cevinedit_Diagram_modelExtension: Property = Property(name="modelExtension", type=StringType)
cevinedit_Diagram.attributes={cevinedit_Diagram_modelExtension, cevinedit_Diagram_name}

# cevinedit_PersonalizedElement class attributes and methods
cevinedit_PersonalizedElement_name: Property = Property(name="name", type=StringType)
cevinedit_PersonalizedElement_icon: Property = Property(name="icon", type=StringType)
cevinedit_PersonalizedElement.attributes={cevinedit_PersonalizedElement_name, cevinedit_PersonalizedElement_icon}

# cevinedit_LinkEClass class attributes and methods
cevinedit_LinkEClass_source: Property = Property(name="source", type=StringType)
cevinedit_LinkEClass_target: Property = Property(name="target", type=StringType)
cevinedit_LinkEClass.attributes={cevinedit_LinkEClass_target, cevinedit_LinkEClass_source}

# Link class attributes and methods

# cevinedit_CompartmentEReferenceCont class attributes and methods
cevinedit_CompartmentEReferenceCont_collapsible: Property = Property(name="collapsible", type=BooleanType)
cevinedit_CompartmentEReferenceCont_layout: Property = Property(name="layout", type=StringType)
cevinedit_CompartmentEReferenceCont.attributes={cevinedit_CompartmentEReferenceCont_layout, cevinedit_CompartmentEReferenceCont_collapsible}

# cevinedit_AffixedEReferenceCont class attributes and methods

# cevinedit_LabelEAttribute class attributes and methods

# cevinedit_LinkEReferenceNonCont class attributes and methods

# cevinedit_Link class attributes and methods
cevinedit_Link_brightness: Property = Property(name="brightness", type=StringType)
cevinedit_Link_color: Property = Property(name="color", type=StringType)
cevinedit_Link_labelFontStyle: Property = Property(name="labelFontStyle", type=StringType)
cevinedit_Link_sourceDecoration: Property = Property(name="sourceDecoration", type=StringType)
cevinedit_Link_targetDecoration: Property = Property(name="targetDecoration", type=StringType)
cevinedit_Link_texture: Property = Property(name="texture", type=StringType)
cevinedit_Link_width: Property = Property(name="width", type=IntegerType)
cevinedit_Link_label: Property = Property(name="label", type=StringType)
cevinedit_Link.attributes={cevinedit_Link_brightness, cevinedit_Link_texture, cevinedit_Link_labelFontStyle, cevinedit_Link_color, cevinedit_Link_sourceDecoration, cevinedit_Link_label, cevinedit_Link_targetDecoration, cevinedit_Link_width}

# cevinedit_NodeEClass class attributes and methods
cevinedit_NodeEClass_labelPlacement: Property = Property(name="labelPlacement", type=StringType)
cevinedit_NodeEClass_labelFontStyle: Property = Property(name="labelFontStyle", type=StringType)
cevinedit_NodeEClass_label: Property = Property(name="label", type=StringType)
cevinedit_NodeEClass_imagePath: Property = Property(name="imagePath", type=StringType)
cevinedit_NodeEClass_listPointsPolygon: Property = Property(name="listPointsPolygon", type=StringType)
cevinedit_NodeEClass_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
cevinedit_NodeEClass_borderColor: Property = Property(name="borderColor", type=StringType)
cevinedit_NodeEClass_borderTexture: Property = Property(name="borderTexture", type=StringType)
cevinedit_NodeEClass_borderWidth: Property = Property(name="borderWidth", type=IntegerType)
cevinedit_NodeEClass_brightness: Property = Property(name="brightness", type=StringType)
cevinedit_NodeEClass_figure: Property = Property(name="figure", type=StringType)
cevinedit_NodeEClass_resizable: Property = Property(name="resizable", type=BooleanType)
cevinedit_NodeEClass_size: Property = Property(name="size", type=StringType)
cevinedit_NodeEClass.attributes={cevinedit_NodeEClass_resizable, cevinedit_NodeEClass_label, cevinedit_NodeEClass_brightness, cevinedit_NodeEClass_labelPlacement, cevinedit_NodeEClass_size, cevinedit_NodeEClass_borderWidth, cevinedit_NodeEClass_figure, cevinedit_NodeEClass_borderTexture, cevinedit_NodeEClass_labelFontStyle, cevinedit_NodeEClass_listPointsPolygon, cevinedit_NodeEClass_backgroundColor, cevinedit_NodeEClass_borderColor, cevinedit_NodeEClass_imagePath}

# PersonalizedElement class attributes and methods

# Relationships
diagram0: BinaryAssociation = BinaryAssociation(
    name="diagram0",
    ends={
        Property(name="cevinedit_Diagram", type=cevinedit_CEViNEditRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="cevinedit_CEViNEditRoot", type=cevinedit_Diagram, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containsElem1: BinaryAssociation = BinaryAssociation(
    name="containsElem1",
    ends={
        Property(name="cevinedit_PersonalizedElement", type=cevinedit_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="cevinedit_Diagram2", type=cevinedit_PersonalizedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cevinedit_LinkEClass_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_LinkEClass)
gen_cevinedit_LinkEClass_Link = Generalization(general=Link, specific=cevinedit_LinkEClass)
gen_cevinedit_CompartmentEReferenceCont_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_CompartmentEReferenceCont)
gen_cevinedit_AffixedEReferenceCont_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_AffixedEReferenceCont)
gen_cevinedit_LabelEAttribute_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_LabelEAttribute)
gen_cevinedit_LinkEReferenceNonCont_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_LinkEReferenceNonCont)
gen_cevinedit_LinkEReferenceNonCont_Link = Generalization(general=Link, specific=cevinedit_LinkEReferenceNonCont)
gen_cevinedit_Link_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_Link)
gen_cevinedit_NodeEClass_PersonalizedElement = Generalization(general=PersonalizedElement, specific=cevinedit_NodeEClass)

# Domain Model
domain_model = DomainModel(
    name="cevinedit",
    types={cevinedit_CEViNEditRoot, cevinedit_Diagram, cevinedit_PersonalizedElement, cevinedit_LinkEClass, Link, cevinedit_CompartmentEReferenceCont, cevinedit_AffixedEReferenceCont, cevinedit_LabelEAttribute, cevinedit_LinkEReferenceNonCont, cevinedit_Link, cevinedit_NodeEClass, PersonalizedElement, Color, Brightness, FontStyle, NodeFigure, LinkFigure, Placement, LayoutCompartment, Texture},
    associations={diagram0, containsElem1},
    generalizations={gen_cevinedit_LinkEClass_PersonalizedElement, gen_cevinedit_LinkEClass_Link, gen_cevinedit_CompartmentEReferenceCont_PersonalizedElement, gen_cevinedit_AffixedEReferenceCont_PersonalizedElement, gen_cevinedit_LabelEAttribute_PersonalizedElement, gen_cevinedit_LinkEReferenceNonCont_PersonalizedElement, gen_cevinedit_LinkEReferenceNonCont_Link, gen_cevinedit_Link_PersonalizedElement, gen_cevinedit_NodeEClass_PersonalizedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)