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
StyleKey: Enumeration = Enumeration(
    name="StyleKey",
    literals={
            EnumerationLiteral(name="backgroundColor"),
			EnumerationLiteral(name="color"),
			EnumerationLiteral(name="display"),
			EnumerationLiteral(name="lineHeight"),
			EnumerationLiteral(name="textAlign"),
			EnumerationLiteral(name="textDecoration"),
			EnumerationLiteral(name="width"),
			EnumerationLiteral(name="padding")
    }
)

# Classes
HTML_Style = Class(name="HTML::Style")
HTML_TABLE = Class(name="HTML::TABLE")
HTMLElement = Class(name="HTMLElement")
HTML_TR = Class(name="HTML::TR")
HTML_HTML = Class(name="HTML::HTML")
HTML_HTMLElement = Class(name="HTML::HTMLElement")
HTML_B = Class(name="HTML::B")
HTML_U = Class(name="HTML::U")
HTML_I = Class(name="HTML::I")
HTML_S = Class(name="HTML::S")
HTML_IMG = Class(name="HTML::IMG")
HTML_BR = Class(name="HTML::BR")
HTML_HR = Class(name="HTML::HR")
HTML_TD = Class(name="HTML::TD")
HTML_DIV = Class(name="HTML::DIV")
HTML_SPAN = Class(name="HTML::SPAN")
HTML_P = Class(name="HTML::P")
HTML_A = Class(name="HTML::A")
HTML_FONT = Class(name="HTML::FONT")

# HTML_Style class attributes and methods
HTML_Style_key: Property = Property(name="key", type=StringType)
HTML_Style_value: Property = Property(name="value", type=StringType)
HTML_Style.attributes={HTML_Style_key, HTML_Style_value}

# HTML_TABLE class attributes and methods
HTML_TABLE_border: Property = Property(name="border", type=IntegerType)
HTML_TABLE_width: Property = Property(name="width", type=StringType)
HTML_TABLE_cellspacing: Property = Property(name="cellspacing", type=StringType)
HTML_TABLE_cellpadding: Property = Property(name="cellpadding", type=StringType)
HTML_TABLE_align: Property = Property(name="align", type=StringType)
HTML_TABLE_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_TABLE.attributes={HTML_TABLE_align, HTML_TABLE_bgcolor, HTML_TABLE_cellspacing, HTML_TABLE_width, HTML_TABLE_border, HTML_TABLE_cellpadding}

# HTMLElement class attributes and methods

# HTML_TR class attributes and methods
HTML_TR_valign: Property = Property(name="valign", type=StringType)
HTML_TR_align: Property = Property(name="align", type=StringType)
HTML_TR_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_TR_height: Property = Property(name="height", type=StringType)
HTML_TR.attributes={HTML_TR_align, HTML_TR_height, HTML_TR_valign, HTML_TR_bgcolor}

# HTML_HTML class attributes and methods

# HTML_HTMLElement class attributes and methods

# HTML_B class attributes and methods

# HTML_U class attributes and methods

# HTML_I class attributes and methods

# HTML_S class attributes and methods

# HTML_IMG class attributes and methods
HTML_IMG_src: Property = Property(name="src", type=StringType)
HTML_IMG_width: Property = Property(name="width", type=StringType)
HTML_IMG_height: Property = Property(name="height", type=StringType)
HTML_IMG_border: Property = Property(name="border", type=StringType)
HTML_IMG.attributes={HTML_IMG_width, HTML_IMG_border, HTML_IMG_height, HTML_IMG_src}

# HTML_BR class attributes and methods

# HTML_HR class attributes and methods
HTML_HR_color: Property = Property(name="color", type=StringType)
HTML_HR.attributes={HTML_HR_color}

# HTML_TD class attributes and methods
HTML_TD_colspan: Property = Property(name="colspan", type=StringType)
HTML_TD_rowspan: Property = Property(name="rowspan", type=StringType)
HTML_TD_valign: Property = Property(name="valign", type=StringType)
HTML_TD_align: Property = Property(name="align", type=StringType)
HTML_TD_width: Property = Property(name="width", type=StringType)
HTML_TD_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_TD_height: Property = Property(name="height", type=StringType)
HTML_TD.attributes={HTML_TD_align, HTML_TD_colspan, HTML_TD_rowspan, HTML_TD_valign, HTML_TD_bgcolor, HTML_TD_height, HTML_TD_width}

# HTML_DIV class attributes and methods
HTML_DIV_align: Property = Property(name="align", type=StringType)
HTML_DIV.attributes={HTML_DIV_align}

# HTML_SPAN class attributes and methods

# HTML_P class attributes and methods
HTML_P_align: Property = Property(name="align", type=StringType)
HTML_P.attributes={HTML_P_align}

# HTML_A class attributes and methods
HTML_A_ref: Property = Property(name="ref", type=StringType)
HTML_A.attributes={HTML_A_ref}

# HTML_FONT class attributes and methods
HTML_FONT_color: Property = Property(name="color", type=StringType)
HTML_FONT_face: Property = Property(name="face", type=StringType)
HTML_FONT_size: Property = Property(name="size", type=StringType)
HTML_FONT_value: Property = Property(name="value", type=StringType)
HTML_FONT.attributes={HTML_FONT_face, HTML_FONT_color, HTML_FONT_value, HTML_FONT_size}

# Relationships
elements2: BinaryAssociation = BinaryAssociation(
    name="elements2",
    ends={
        Property(name="HTML_HTMLElement3", type=HTML_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_HTMLElement1", type=HTML_HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styles4: BinaryAssociation = BinaryAssociation(
    name="styles4",
    ends={
        Property(name="HTML_Style", type=HTML_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_HTMLElement5", type=HTML_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trs6: BinaryAssociation = BinaryAssociation(
    name="trs6",
    ends={
        Property(name="HTML_TR", type=HTML_TABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_TABLE", type=HTML_TR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
htmlElements0: BinaryAssociation = BinaryAssociation(
    name="htmlElements0",
    ends={
        Property(name="HTML_HTMLElement", type=HTML_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_HTML", type=HTML_HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tds7: BinaryAssociation = BinaryAssociation(
    name="tds7",
    ends={
        Property(name="HTML_TD", type=HTML_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_TR8", type=HTML_TD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_HTML_TABLE_HTMLElement = Generalization(general=HTMLElement, specific=HTML_TABLE)
gen_HTML_TR_HTMLElement = Generalization(general=HTMLElement, specific=HTML_TR)
gen_HTML_B_HTMLElement = Generalization(general=HTMLElement, specific=HTML_B)
gen_HTML_U_HTMLElement = Generalization(general=HTMLElement, specific=HTML_U)
gen_HTML_I_HTMLElement = Generalization(general=HTMLElement, specific=HTML_I)
gen_HTML_S_HTMLElement = Generalization(general=HTMLElement, specific=HTML_S)
gen_HTML_IMG_HTMLElement = Generalization(general=HTMLElement, specific=HTML_IMG)
gen_HTML_BR_HTMLElement = Generalization(general=HTMLElement, specific=HTML_BR)
gen_HTML_HR_HTMLElement = Generalization(general=HTMLElement, specific=HTML_HR)
gen_HTML_TD_HTMLElement = Generalization(general=HTMLElement, specific=HTML_TD)
gen_HTML_DIV_HTMLElement = Generalization(general=HTMLElement, specific=HTML_DIV)
gen_HTML_SPAN_HTMLElement = Generalization(general=HTMLElement, specific=HTML_SPAN)
gen_HTML_P_HTMLElement = Generalization(general=HTMLElement, specific=HTML_P)
gen_HTML_A_HTMLElement = Generalization(general=HTMLElement, specific=HTML_A)
gen_HTML_FONT_HTMLElement = Generalization(general=HTMLElement, specific=HTML_FONT)

# Domain Model
domain_model = DomainModel(
    name="HTML",
    types={HTML_Style, HTML_TABLE, HTMLElement, HTML_TR, HTML_HTML, HTML_HTMLElement, HTML_B, HTML_U, HTML_I, HTML_S, HTML_IMG, HTML_BR, HTML_HR, HTML_TD, HTML_DIV, HTML_SPAN, HTML_P, HTML_A, HTML_FONT, StyleKey},
    associations={elements2, styles4, trs6, htmlElements0, tds7},
    generalizations={gen_HTML_TABLE_HTMLElement, gen_HTML_TR_HTMLElement, gen_HTML_B_HTMLElement, gen_HTML_U_HTMLElement, gen_HTML_I_HTMLElement, gen_HTML_S_HTMLElement, gen_HTML_IMG_HTMLElement, gen_HTML_BR_HTMLElement, gen_HTML_HR_HTMLElement, gen_HTML_TD_HTMLElement, gen_HTML_DIV_HTMLElement, gen_HTML_SPAN_HTMLElement, gen_HTML_P_HTMLElement, gen_HTML_A_HTMLElement, gen_HTML_FONT_HTMLElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)