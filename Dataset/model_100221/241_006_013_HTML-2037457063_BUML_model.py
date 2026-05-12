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
HTML_HTML = Class(name="HTML_HTML")
HEAD = Class(name="HEAD")
BBODY = Class(name="BBODY")
HTML_HTMLElement = Class(name="HTML_HTMLElement")
HTMLElement = Class(name="HTMLElement")
HTML_HEAD = Class(name="HTML_HEAD")
HEADElement = Class(name="HEADElement")
HTML = Class(name="HTML")
HTML_HEADElement = Class(name="HTML_HEADElement", is_abstract=True)
HTML_LINK = Class(name="HTML_LINK")
HTML_TITLE = Class(name="HTML_TITLE")
HTML_BBODY = Class(name="HTML_BBODY")
BODYElement = Class(name="BODYElement")
HTML_BODYElement = Class(name="HTML_BODYElement", is_abstract=True)
HTML_H1 = Class(name="HTML_H1")
HTML_H2 = Class(name="HTML_H2")
HTML_H3 = Class(name="HTML_H3")
HTML_H4 = Class(name="HTML_H4")
HTML_EM = Class(name="HTML_EM")
HTML_BR = Class(name="HTML_BR")
HTML_STRONG = Class(name="HTML_STRONG")
HTML_IMG = Class(name="HTML_IMG")
HTML_STYLE = Class(name="HTML_STYLE")
HTML_SPAN = Class(name="HTML_SPAN")
HTML_A = Class(name="HTML_A")
HTML_P = Class(name="HTML_P")
HTML_TABLEElement = Class(name="HTML_TABLEElement", is_abstract=True)
HTML_TABLE = Class(name="HTML_TABLE")
TABLEElement = Class(name="TABLEElement")
HTML_DIV = Class(name="HTML_DIV")
TABLE = Class(name="TABLE")
TD = Class(name="TD")
HTML_TD = Class(name="HTML_TD")
TR = Class(name="TR")
HTML_TR = Class(name="HTML_TR")
HTML_TH = Class(name="HTML_TH")
HTML_SELECT = Class(name="HTML_SELECT")
HTML_UL = Class(name="HTML_UL")
HTML_LI = Class(name="HTML_LI")
HTML_H5 = Class(name="HTML_H5")
HTML_H6 = Class(name="HTML_H6")
HTML_Website = Class(name="HTML_Website")
HTML_OPTION = Class(name="HTML_OPTION")
HTML_ListElement = Class(name="HTML_ListElement", is_abstract=True)
HTML_OL = Class(name="HTML_OL")
ListElement = Class(name="ListElement")

# HTML_HTML class attributes and methods

# HEAD class attributes and methods

# BBODY class attributes and methods

# HTML_HTMLElement class attributes and methods
HTML_HTMLElement_value: Property = Property(name="value", type=StringType)
HTML_HTMLElement.attributes={HTML_HTMLElement_value}

# HTMLElement class attributes and methods

# HTML_HEAD class attributes and methods

# HEADElement class attributes and methods

# HTML class attributes and methods

# HTML_HEADElement class attributes and methods

# HTML_LINK class attributes and methods
HTML_LINK_rel: Property = Property(name="rel", type=StringType)
HTML_LINK_title: Property = Property(name="title", type=StringType)
HTML_LINK_ahref: Property = Property(name="ahref", type=StringType)
HTML_LINK_type: Property = Property(name="type", type=StringType)
HTML_LINK.attributes={HTML_LINK_type, HTML_LINK_title, HTML_LINK_rel, HTML_LINK_ahref}

# HTML_TITLE class attributes and methods

# HTML_BBODY class attributes and methods
HTML_BBODY_alink: Property = Property(name="alink", type=StringType)
HTML_BBODY_background: Property = Property(name="background", type=StringType)
HTML_BBODY_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_BBODY_text: Property = Property(name="text", type=StringType)
HTML_BBODY_link: Property = Property(name="link", type=StringType)
HTML_BBODY_vlink: Property = Property(name="vlink", type=StringType)
HTML_BBODY.attributes={HTML_BBODY_link, HTML_BBODY_alink, HTML_BBODY_text, HTML_BBODY_background, HTML_BBODY_bgcolor, HTML_BBODY_vlink}

# BODYElement class attributes and methods

# HTML_BODYElement class attributes and methods

# HTML_H1 class attributes and methods

# HTML_H2 class attributes and methods

# HTML_H3 class attributes and methods

# HTML_H4 class attributes and methods

# HTML_EM class attributes and methods

# HTML_BR class attributes and methods
HTML_BR_clear: Property = Property(name="clear", type=StringType)
HTML_BR.attributes={HTML_BR_clear}

# HTML_STRONG class attributes and methods

# HTML_IMG class attributes and methods
HTML_IMG_border: Property = Property(name="border", type=StringType)
HTML_IMG_src: Property = Property(name="src", type=StringType)
HTML_IMG_width: Property = Property(name="width", type=StringType)
HTML_IMG_height: Property = Property(name="height", type=StringType)
HTML_IMG_alt: Property = Property(name="alt", type=StringType)
HTML_IMG_align: Property = Property(name="align", type=StringType)
HTML_IMG_vspace: Property = Property(name="vspace", type=StringType)
HTML_IMG_hspace: Property = Property(name="hspace", type=StringType)
HTML_IMG_ismap: Property = Property(name="ismap", type=StringType)
HTML_IMG_usemap: Property = Property(name="usemap", type=StringType)
HTML_IMG.attributes={HTML_IMG_height, HTML_IMG_ismap, HTML_IMG_align, HTML_IMG_usemap, HTML_IMG_hspace, HTML_IMG_border, HTML_IMG_vspace, HTML_IMG_src, HTML_IMG_width, HTML_IMG_alt}

# HTML_STYLE class attributes and methods

# HTML_SPAN class attributes and methods
HTML_SPAN_style: Property = Property(name="style", type=StringType)
HTML_SPAN.attributes={HTML_SPAN_style}

# HTML_A class attributes and methods
HTML_A_ahref: Property = Property(name="ahref", type=StringType)
HTML_A_name: Property = Property(name="name", type=StringType)
HTML_A_id: Property = Property(name="id", type=StringType)
HTML_A.attributes={HTML_A_ahref, HTML_A_name, HTML_A_id}

# HTML_P class attributes and methods

# HTML_TABLEElement class attributes and methods
HTML_TABLEElement_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_TABLEElement_background: Property = Property(name="background", type=StringType)
HTML_TABLEElement.attributes={HTML_TABLEElement_bgcolor, HTML_TABLEElement_background}

# HTML_TABLE class attributes and methods
HTML_TABLE_border: Property = Property(name="border", type=StringType)
HTML_TABLE_width: Property = Property(name="width", type=StringType)
HTML_TABLE_cellspacing: Property = Property(name="cellspacing", type=StringType)
HTML_TABLE_cellpadding: Property = Property(name="cellpadding", type=StringType)
HTML_TABLE.attributes={HTML_TABLE_cellspacing, HTML_TABLE_border, HTML_TABLE_width, HTML_TABLE_cellpadding}

# TABLEElement class attributes and methods

# HTML_DIV class attributes and methods
HTML_DIV_align: Property = Property(name="align", type=StringType)
HTML_DIV.attributes={HTML_DIV_align}

# TABLE class attributes and methods

# TD class attributes and methods

# HTML_TD class attributes and methods
HTML_TD_colspan: Property = Property(name="colspan", type=StringType)
HTML_TD_rowspan: Property = Property(name="rowspan", type=StringType)
HTML_TD_valign: Property = Property(name="valign", type=StringType)
HTML_TD_align: Property = Property(name="align", type=StringType)
HTML_TD_width: Property = Property(name="width", type=StringType)
HTML_TD.attributes={HTML_TD_colspan, HTML_TD_align, HTML_TD_width, HTML_TD_rowspan, HTML_TD_valign}

# TR class attributes and methods

# HTML_TR class attributes and methods
HTML_TR_valign: Property = Property(name="valign", type=StringType)
HTML_TR_align: Property = Property(name="align", type=StringType)
HTML_TR.attributes={HTML_TR_align, HTML_TR_valign}

# HTML_TH class attributes and methods

# HTML_SELECT class attributes and methods
HTML_SELECT_multiple: Property = Property(name="multiple", type=StringType)
HTML_SELECT_size: Property = Property(name="size", type=StringType)
HTML_SELECT_name: Property = Property(name="name", type=StringType)
HTML_SELECT.attributes={HTML_SELECT_size, HTML_SELECT_name, HTML_SELECT_multiple}

# HTML_UL class attributes and methods

# HTML_LI class attributes and methods
HTML_LI_liValue: Property = Property(name="liValue", type=StringType)
HTML_LI.attributes={HTML_LI_liValue}

# HTML_H5 class attributes and methods

# HTML_H6 class attributes and methods

# HTML_Website class attributes and methods

# HTML_OPTION class attributes and methods
HTML_OPTION_selected: Property = Property(name="selected", type=StringType)
HTML_OPTION_optionValue: Property = Property(name="optionValue", type=StringType)
HTML_OPTION.attributes={HTML_OPTION_optionValue, HTML_OPTION_selected}

# HTML_ListElement class attributes and methods
HTML_ListElement_type: Property = Property(name="type", type=StringType)
HTML_ListElement.attributes={HTML_ListElement_type}

# HTML_OL class attributes and methods
HTML_OL_start: Property = Property(name="start", type=StringType)
HTML_OL.attributes={HTML_OL_start}

# ListElement class attributes and methods

# Relationships
head0: BinaryAssociation = BinaryAssociation(
    name="head0",
    ends={
        Property(name="HEAD", type=HTML_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html", type=HEAD, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bbody1: BinaryAssociation = BinaryAssociation(
    name="bbody1",
    ends={
        Property(name="BBODY", type=HTML_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html2", type=BBODY, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="HTMLElement", type=HTML_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="HTMLElement5", type=HTML_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=HTMLElement, multiplicity=Multiplicity(1, 1))
    }
)
headElements6: BinaryAssociation = BinaryAssociation(
    name="headElements6",
    ends={
        Property(name="HEADElement", type=HTML_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=HEADElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html7: BinaryAssociation = BinaryAssociation(
    name="html7",
    ends={
        Property(name="HTML", type=HTML_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head8", type=HTML, multiplicity=Multiplicity(1, 1))
    }
)
head9: BinaryAssociation = BinaryAssociation(
    name="head9",
    ends={
        Property(name="headElements", type=HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="HEAD10", type=HTML_HEADElement, multiplicity=Multiplicity(1, 1))
    }
)
bodyElements11: BinaryAssociation = BinaryAssociation(
    name="bodyElements11",
    ends={
        Property(name="BODYElement", type=HTML_BBODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=BODYElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html12: BinaryAssociation = BinaryAssociation(
    name="html12",
    ends={
        Property(name="HTML13", type=HTML_BBODY, multiplicity=Multiplicity(1, 1)),
        Property(name="bbody", type=HTML, multiplicity=Multiplicity(1, 1))
    }
)
body14: BinaryAssociation = BinaryAssociation(
    name="body14",
    ends={
        Property(name="BBODY15", type=HTML_BODYElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyElements", type=BBODY, multiplicity=Multiplicity(1, 1))
    }
)
table17: BinaryAssociation = BinaryAssociation(
    name="table17",
    ends={
        Property(name="TABLE", type=HTML_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="trs", type=TABLE, multiplicity=Multiplicity(1, 1))
    }
)
tds18: BinaryAssociation = BinaryAssociation(
    name="tds18",
    ends={
        Property(name="TD", type=HTML_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=TD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trs16: BinaryAssociation = BinaryAssociation(
    name="trs16",
    ends={
        Property(name="TR", type=HTML_TABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=TR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr19: BinaryAssociation = BinaryAssociation(
    name="tr19",
    ends={
        Property(name="TR20", type=HTML_TD, multiplicity=Multiplicity(1, 1)),
        Property(name="tds", type=TR, multiplicity=Multiplicity(1, 1))
    }
)
pages21: BinaryAssociation = BinaryAssociation(
    name="pages21",
    ends={
        Property(name="HTML22", type=HTML_Website, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_Website", type=HTML, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_HTML_HEAD_HTMLElement = Generalization(general=HTMLElement, specific=HTML_HEAD)
gen_HTML_HEADElement_HTMLElement = Generalization(general=HTMLElement, specific=HTML_HEADElement)
gen_HTML_LINK_HEADElement = Generalization(general=HEADElement, specific=HTML_LINK)
gen_HTML_TITLE_HEADElement = Generalization(general=HEADElement, specific=HTML_TITLE)
gen_HTML_BBODY_HTMLElement = Generalization(general=HTMLElement, specific=HTML_BBODY)
gen_HTML_BODYElement_HTMLElement = Generalization(general=HTMLElement, specific=HTML_BODYElement)
gen_HTML_H1_BODYElement = Generalization(general=BODYElement, specific=HTML_H1)
gen_HTML_H2_BODYElement = Generalization(general=BODYElement, specific=HTML_H2)
gen_HTML_H3_BODYElement = Generalization(general=BODYElement, specific=HTML_H3)
gen_HTML_H4_BODYElement = Generalization(general=BODYElement, specific=HTML_H4)
gen_HTML_EM_BODYElement = Generalization(general=BODYElement, specific=HTML_EM)
gen_HTML_BR_BODYElement = Generalization(general=BODYElement, specific=HTML_BR)
gen_HTML_STRONG_BODYElement = Generalization(general=BODYElement, specific=HTML_STRONG)
gen_HTML_IMG_BODYElement = Generalization(general=BODYElement, specific=HTML_IMG)
gen_HTML_STYLE_BODYElement = Generalization(general=BODYElement, specific=HTML_STYLE)
gen_HTML_SPAN_BODYElement = Generalization(general=BODYElement, specific=HTML_SPAN)
gen_HTML_A_BODYElement = Generalization(general=BODYElement, specific=HTML_A)
gen_HTML_P_BODYElement = Generalization(general=BODYElement, specific=HTML_P)
gen_HTML_TABLEElement_BODYElement = Generalization(general=BODYElement, specific=HTML_TABLEElement)
gen_HTML_TABLE_TABLEElement = Generalization(general=TABLEElement, specific=HTML_TABLE)
gen_HTML_DIV_BODYElement = Generalization(general=BODYElement, specific=HTML_DIV)
gen_HTML_TR_TABLEElement = Generalization(general=TABLEElement, specific=HTML_TR)
gen_HTML_TD_TABLEElement = Generalization(general=TABLEElement, specific=HTML_TD)
gen_HTML_TH_TD = Generalization(general=TD, specific=HTML_TH)
gen_HTML_UL_ListElement = Generalization(general=ListElement, specific=HTML_UL)
gen_HTML_LI_ListElement = Generalization(general=ListElement, specific=HTML_LI)
gen_HTML_H5_BODYElement = Generalization(general=BODYElement, specific=HTML_H5)
gen_HTML_H6_BODYElement = Generalization(general=BODYElement, specific=HTML_H6)
gen_HTML_OL_ListElement = Generalization(general=ListElement, specific=HTML_OL)

# Domain Model
domain_model = DomainModel(
    name="HTML",
    types={HTML_HTML, HEAD, BBODY, HTML_HTMLElement, HTMLElement, HTML_HEAD, HEADElement, HTML, HTML_HEADElement, HTML_LINK, HTML_TITLE, HTML_BBODY, BODYElement, HTML_BODYElement, HTML_H1, HTML_H2, HTML_H3, HTML_H4, HTML_EM, HTML_BR, HTML_STRONG, HTML_IMG, HTML_STYLE, HTML_SPAN, HTML_A, HTML_P, HTML_TABLEElement, HTML_TABLE, TABLEElement, HTML_DIV, TABLE, TD, HTML_TD, TR, HTML_TR, HTML_TH, HTML_SELECT, HTML_UL, HTML_LI, HTML_H5, HTML_H6, HTML_Website, HTML_OPTION, HTML_ListElement, HTML_OL, ListElement},
    associations={head0, bbody1, children3, parent4, headElements6, html7, head9, bodyElements11, html12, body14, table17, tds18, trs16, tr19, pages21},
    generalizations={gen_HTML_HEAD_HTMLElement, gen_HTML_HEADElement_HTMLElement, gen_HTML_LINK_HEADElement, gen_HTML_TITLE_HEADElement, gen_HTML_BBODY_HTMLElement, gen_HTML_BODYElement_HTMLElement, gen_HTML_H1_BODYElement, gen_HTML_H2_BODYElement, gen_HTML_H3_BODYElement, gen_HTML_H4_BODYElement, gen_HTML_EM_BODYElement, gen_HTML_BR_BODYElement, gen_HTML_STRONG_BODYElement, gen_HTML_IMG_BODYElement, gen_HTML_STYLE_BODYElement, gen_HTML_SPAN_BODYElement, gen_HTML_A_BODYElement, gen_HTML_P_BODYElement, gen_HTML_TABLEElement_BODYElement, gen_HTML_TABLE_TABLEElement, gen_HTML_DIV_BODYElement, gen_HTML_TR_TABLEElement, gen_HTML_TD_TABLEElement, gen_HTML_TH_TD, gen_HTML_UL_ListElement, gen_HTML_LI_ListElement, gen_HTML_H5_BODYElement, gen_HTML_H6_BODYElement, gen_HTML_OL_ListElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)