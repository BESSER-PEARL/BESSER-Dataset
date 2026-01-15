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
HTML_HTML = Class(name="HTML::HTML")
HTML_HEAD = Class(name="HTML::HEAD")
HTML_BODY = Class(name="HTML::BODY")
HTML_HTMLElement = Class(name="HTML::HTMLElement")
HTMLElement = Class(name="HTMLElement")
HTML_HEADElement = Class(name="HTML::HEADElement", is_abstract=True)
HTML_LINK = Class(name="HTML::LINK")
HEADElement = Class(name="HEADElement")
HTML_TITLE = Class(name="HTML::TITLE")
HTML_BODYElement = Class(name="HTML::BODYElement", is_abstract=True)
HTML_H1 = Class(name="HTML::H1")
BODYElement = Class(name="BODYElement")
HTML_H2 = Class(name="HTML::H2")
HTML_H3 = Class(name="HTML::H3")
HTML_H4 = Class(name="HTML::H4")
HTML_EM = Class(name="HTML::EM")
HTML_STRONG = Class(name="HTML::STRONG")
HTML_B = Class(name="HTML::B")
HTML_TT = Class(name="HTML::TT")
HTML_PRE = Class(name="HTML::PRE")
HTML_BIG = Class(name="HTML::BIG")
HTML_SMALL = Class(name="HTML::SMALL")
HTML_SUB = Class(name="HTML::SUB")
HTML_SUP = Class(name="HTML::SUP")
HTML_STRIKE = Class(name="HTML::STRIKE")
HTML_FONT = Class(name="HTML::FONT")
HTML_IMG = Class(name="HTML::IMG")
HTML_BR = Class(name="HTML::BR")
HTML_MAP = Class(name="HTML::MAP")
HTML_AREA = Class(name="HTML::AREA")
HTML_STYLE = Class(name="HTML::STYLE")
HTML_EMBED = Class(name="HTML::EMBED")
HTML_I = Class(name="HTML::I")
HTML_NOEMBED = Class(name="HTML::NOEMBED")
HTML_SPAN = Class(name="HTML::SPAN")
HTML_A = Class(name="HTML::A")
HTML_DIV = Class(name="HTML::DIV")
HTML_P = Class(name="HTML::P")
HTML_TABLEElement = Class(name="HTML::TABLEElement", is_abstract=True)
HTML_TABLE = Class(name="HTML::TABLE")
TABLEElement = Class(name="TABLEElement")
HTML_TR = Class(name="HTML::TR")
HTML_TD = Class(name="HTML::TD")
HTML_TH = Class(name="HTML::TH")
TD = Class(name="TD")
HTML_FORM = Class(name="HTML::FORM")
HTML_INPUT = Class(name="HTML::INPUT")
HTML_TEXTAREA = Class(name="HTML::TEXTAREA")
HTML_SELECT = Class(name="HTML::SELECT")
HTML_OPTION = Class(name="HTML::OPTION")
HTML_ListElement = Class(name="HTML::ListElement", is_abstract=True)
HTML_OL = Class(name="HTML::OL")
ListElement = Class(name="ListElement")
HTML_UL = Class(name="HTML::UL")
HTML_LI = Class(name="HTML::LI")
HTML_DL = Class(name="HTML::DL")
HTML_DT = Class(name="HTML::DT")
HTML_DD = Class(name="HTML::DD")
HTML_APPLET = Class(name="HTML::APPLET")
HTML_PARAM = Class(name="HTML::PARAM")
HTML_OBJECT = Class(name="HTML::OBJECT")
HTML_FRAMESET = Class(name="HTML::FRAMESET")
HTML_FRAME = Class(name="HTML::FRAME")
HTML_NOFRAME = Class(name="HTML::NOFRAME")
HTML_IFRAME = Class(name="HTML::IFRAME")
FRAME = Class(name="FRAME")

# HTML_HTML class attributes and methods

# HTML_HEAD class attributes and methods

# HTML_BODY class attributes and methods
HTML_BODY_background: Property = Property(name="background", type=StringType)
HTML_BODY_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_BODY_text: Property = Property(name="text", type=StringType)
HTML_BODY_link: Property = Property(name="link", type=StringType)
HTML_BODY_alink: Property = Property(name="alink", type=StringType)
HTML_BODY_vlink: Property = Property(name="vlink", type=StringType)
HTML_BODY.attributes={HTML_BODY_bgcolor, HTML_BODY_background, HTML_BODY_link, HTML_BODY_text, HTML_BODY_alink, HTML_BODY_vlink}

# HTML_HTMLElement class attributes and methods
HTML_HTMLElement_value: Property = Property(name="value", type=StringType)
HTML_HTMLElement.attributes={HTML_HTMLElement_value}

# HTMLElement class attributes and methods

# HTML_HEADElement class attributes and methods

# HTML_LINK class attributes and methods
HTML_LINK_rel: Property = Property(name="rel", type=StringType)
HTML_LINK_title: Property = Property(name="title", type=StringType)
HTML_LINK_ahref: Property = Property(name="ahref", type=StringType)
HTML_LINK_type: Property = Property(name="type", type=StringType)
HTML_LINK.attributes={HTML_LINK_type, HTML_LINK_ahref, HTML_LINK_title, HTML_LINK_rel}

# HEADElement class attributes and methods

# HTML_TITLE class attributes and methods

# HTML_BODYElement class attributes and methods

# HTML_H1 class attributes and methods

# BODYElement class attributes and methods

# HTML_H2 class attributes and methods

# HTML_H3 class attributes and methods

# HTML_H4 class attributes and methods

# HTML_EM class attributes and methods

# HTML_STRONG class attributes and methods

# HTML_B class attributes and methods

# HTML_TT class attributes and methods

# HTML_PRE class attributes and methods

# HTML_BIG class attributes and methods

# HTML_SMALL class attributes and methods

# HTML_SUB class attributes and methods

# HTML_SUP class attributes and methods

# HTML_STRIKE class attributes and methods

# HTML_FONT class attributes and methods
HTML_FONT_color: Property = Property(name="color", type=StringType)
HTML_FONT_face: Property = Property(name="face", type=StringType)
HTML_FONT_size: Property = Property(name="size", type=StringType)
HTML_FONT.attributes={HTML_FONT_color, HTML_FONT_size, HTML_FONT_face}

# HTML_IMG class attributes and methods
HTML_IMG_src: Property = Property(name="src", type=StringType)
HTML_IMG_width: Property = Property(name="width", type=StringType)
HTML_IMG_height: Property = Property(name="height", type=StringType)
HTML_IMG_alt: Property = Property(name="alt", type=StringType)
HTML_IMG_align: Property = Property(name="align", type=StringType)
HTML_IMG_vspace: Property = Property(name="vspace", type=StringType)
HTML_IMG_hspace: Property = Property(name="hspace", type=StringType)
HTML_IMG_ismap: Property = Property(name="ismap", type=StringType)
HTML_IMG_usemap: Property = Property(name="usemap", type=StringType)
HTML_IMG_border: Property = Property(name="border", type=StringType)
HTML_IMG.attributes={HTML_IMG_alt, HTML_IMG_vspace, HTML_IMG_width, HTML_IMG_usemap, HTML_IMG_hspace, HTML_IMG_src, HTML_IMG_align, HTML_IMG_ismap, HTML_IMG_height, HTML_IMG_border}

# HTML_BR class attributes and methods
HTML_BR_clear: Property = Property(name="clear", type=StringType)
HTML_BR.attributes={HTML_BR_clear}

# HTML_MAP class attributes and methods

# HTML_AREA class attributes and methods
HTML_AREA_shape: Property = Property(name="shape", type=StringType)
HTML_AREA_coords: Property = Property(name="coords", type=StringType)
HTML_AREA_ahref: Property = Property(name="ahref", type=StringType)
HTML_AREA.attributes={HTML_AREA_ahref, HTML_AREA_coords, HTML_AREA_shape}

# HTML_STYLE class attributes and methods

# HTML_EMBED class attributes and methods
HTML_EMBED_src: Property = Property(name="src", type=StringType)
HTML_EMBED_width: Property = Property(name="width", type=StringType)
HTML_EMBED_height: Property = Property(name="height", type=StringType)
HTML_EMBED_align: Property = Property(name="align", type=StringType)
HTML_EMBED_vspace: Property = Property(name="vspace", type=StringType)
HTML_EMBED_hspace: Property = Property(name="hspace", type=StringType)
HTML_EMBED_border: Property = Property(name="border", type=StringType)
HTML_EMBED.attributes={HTML_EMBED_hspace, HTML_EMBED_height, HTML_EMBED_src, HTML_EMBED_border, HTML_EMBED_align, HTML_EMBED_vspace, HTML_EMBED_width}

# HTML_I class attributes and methods

# HTML_NOEMBED class attributes and methods

# HTML_SPAN class attributes and methods
HTML_SPAN_style: Property = Property(name="style", type=StringType)
HTML_SPAN.attributes={HTML_SPAN_style}

# HTML_A class attributes and methods
HTML_A_ahref: Property = Property(name="ahref", type=StringType)
HTML_A_name: Property = Property(name="name", type=StringType)
HTML_A_id: Property = Property(name="id", type=StringType)
HTML_A.attributes={HTML_A_id, HTML_A_ahref, HTML_A_name}

# HTML_DIV class attributes and methods
HTML_DIV_align: Property = Property(name="align", type=StringType)
HTML_DIV.attributes={HTML_DIV_align}

# HTML_P class attributes and methods

# HTML_TABLEElement class attributes and methods
HTML_TABLEElement_bgcolor: Property = Property(name="bgcolor", type=StringType)
HTML_TABLEElement_background: Property = Property(name="background", type=StringType)
HTML_TABLEElement.attributes={HTML_TABLEElement_background, HTML_TABLEElement_bgcolor}

# HTML_TABLE class attributes and methods
HTML_TABLE_border: Property = Property(name="border", type=StringType)
HTML_TABLE_width: Property = Property(name="width", type=StringType)
HTML_TABLE_cellspacing: Property = Property(name="cellspacing", type=StringType)
HTML_TABLE_cellpadding: Property = Property(name="cellpadding", type=StringType)
HTML_TABLE.attributes={HTML_TABLE_cellspacing, HTML_TABLE_cellpadding, HTML_TABLE_border, HTML_TABLE_width}

# TABLEElement class attributes and methods

# HTML_TR class attributes and methods
HTML_TR_valign: Property = Property(name="valign", type=StringType)
HTML_TR_align: Property = Property(name="align", type=StringType)
HTML_TR.attributes={HTML_TR_align, HTML_TR_valign}

# HTML_TD class attributes and methods
HTML_TD_colspan: Property = Property(name="colspan", type=StringType)
HTML_TD_rowspan: Property = Property(name="rowspan", type=StringType)
HTML_TD_valign: Property = Property(name="valign", type=StringType)
HTML_TD_align: Property = Property(name="align", type=StringType)
HTML_TD_width: Property = Property(name="width", type=StringType)
HTML_TD.attributes={HTML_TD_colspan, HTML_TD_valign, HTML_TD_align, HTML_TD_rowspan, HTML_TD_width}

# HTML_TH class attributes and methods

# TD class attributes and methods

# HTML_FORM class attributes and methods
HTML_FORM_action: Property = Property(name="action", type=StringType)
HTML_FORM_method: Property = Property(name="method", type=StringType)
HTML_FORM.attributes={HTML_FORM_action, HTML_FORM_method}

# HTML_INPUT class attributes and methods
HTML_INPUT_align: Property = Property(name="align", type=StringType)
HTML_INPUT_maxlength: Property = Property(name="maxlength", type=StringType)
HTML_INPUT_size: Property = Property(name="size", type=StringType)
HTML_INPUT_checked: Property = Property(name="checked", type=StringType)
HTML_INPUT_src: Property = Property(name="src", type=StringType)
HTML_INPUT_inputValue: Property = Property(name="inputValue", type=StringType)
HTML_INPUT_name: Property = Property(name="name", type=StringType)
HTML_INPUT_type: Property = Property(name="type", type=StringType)
HTML_INPUT.attributes={HTML_INPUT_checked, HTML_INPUT_type, HTML_INPUT_maxlength, HTML_INPUT_inputValue, HTML_INPUT_src, HTML_INPUT_align, HTML_INPUT_name, HTML_INPUT_size}

# HTML_TEXTAREA class attributes and methods
HTML_TEXTAREA_name: Property = Property(name="name", type=StringType)
HTML_TEXTAREA_rows: Property = Property(name="rows", type=StringType)
HTML_TEXTAREA_cols: Property = Property(name="cols", type=StringType)
HTML_TEXTAREA.attributes={HTML_TEXTAREA_name, HTML_TEXTAREA_cols, HTML_TEXTAREA_rows}

# HTML_SELECT class attributes and methods
HTML_SELECT_multiple: Property = Property(name="multiple", type=StringType)
HTML_SELECT_size: Property = Property(name="size", type=StringType)
HTML_SELECT_name: Property = Property(name="name", type=StringType)
HTML_SELECT.attributes={HTML_SELECT_size, HTML_SELECT_multiple, HTML_SELECT_name}

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

# HTML_UL class attributes and methods

# HTML_LI class attributes and methods
HTML_LI_liValue: Property = Property(name="liValue", type=StringType)
HTML_LI.attributes={HTML_LI_liValue}

# HTML_DL class attributes and methods

# HTML_DT class attributes and methods

# HTML_DD class attributes and methods

# HTML_APPLET class attributes and methods
HTML_APPLET_applet: Property = Property(name="applet", type=StringType)
HTML_APPLET_class: Property = Property(name="class", type=StringType)
HTML_APPLET_src: Property = Property(name="src", type=StringType)
HTML_APPLET_align: Property = Property(name="align", type=StringType)
HTML_APPLET_width: Property = Property(name="width", type=StringType)
HTML_APPLET_height: Property = Property(name="height", type=StringType)
HTML_APPLET.attributes={HTML_APPLET_applet, HTML_APPLET_height, HTML_APPLET_class, HTML_APPLET_src, HTML_APPLET_width, HTML_APPLET_align}

# HTML_PARAM class attributes and methods
HTML_PARAM_name: Property = Property(name="name", type=StringType)
HTML_PARAM_paramValue: Property = Property(name="paramValue", type=StringType)
HTML_PARAM.attributes={HTML_PARAM_name, HTML_PARAM_paramValue}

# HTML_OBJECT class attributes and methods
HTML_OBJECT_classid: Property = Property(name="classid", type=StringType)
HTML_OBJECT_id: Property = Property(name="id", type=StringType)
HTML_OBJECT_data: Property = Property(name="data", type=StringType)
HTML_OBJECT_type: Property = Property(name="type", type=StringType)
HTML_OBJECT_standby: Property = Property(name="standby", type=StringType)
HTML_OBJECT.attributes={HTML_OBJECT_type, HTML_OBJECT_data, HTML_OBJECT_standby, HTML_OBJECT_id, HTML_OBJECT_classid}

# HTML_FRAMESET class attributes and methods
HTML_FRAMESET_rows: Property = Property(name="rows", type=StringType)
HTML_FRAMESET_cols: Property = Property(name="cols", type=StringType)
HTML_FRAMESET_framespacing: Property = Property(name="framespacing", type=StringType)
HTML_FRAMESET_frameborder: Property = Property(name="frameborder", type=StringType)
HTML_FRAMESET_border: Property = Property(name="border", type=StringType)
HTML_FRAMESET.attributes={HTML_FRAMESET_framespacing, HTML_FRAMESET_frameborder, HTML_FRAMESET_border, HTML_FRAMESET_rows, HTML_FRAMESET_cols}

# HTML_FRAME class attributes and methods
HTML_FRAME_src: Property = Property(name="src", type=StringType)
HTML_FRAME_name: Property = Property(name="name", type=StringType)
HTML_FRAME_marginwidth: Property = Property(name="marginwidth", type=StringType)
HTML_FRAME_marginheight: Property = Property(name="marginheight", type=StringType)
HTML_FRAME_scrolling: Property = Property(name="scrolling", type=StringType)
HTML_FRAME_noresize: Property = Property(name="noresize", type=StringType)
HTML_FRAME.attributes={HTML_FRAME_marginwidth, HTML_FRAME_marginheight, HTML_FRAME_name, HTML_FRAME_scrolling, HTML_FRAME_src, HTML_FRAME_noresize}

# HTML_NOFRAME class attributes and methods

# HTML_IFRAME class attributes and methods

# FRAME class attributes and methods

# Relationships
head0: BinaryAssociation = BinaryAssociation(
    name="head0",
    ends={
        Property(name="HEAD", type=HTML_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html", type=HTML_HEAD, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body1: BinaryAssociation = BinaryAssociation(
    name="body1",
    ends={
        Property(name="BODY", type=HTML_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html2", type=HTML_BODY, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="HTML_HTMLElement", type=HTML_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_HTMLElement3", type=HTML_HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headElements5: BinaryAssociation = BinaryAssociation(
    name="headElements5",
    ends={
        Property(name="HEADElement", type=HTML_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=HTML_HEADElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html6: BinaryAssociation = BinaryAssociation(
    name="html6",
    ends={
        Property(name="HTML", type=HTML_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head7", type=HTML_HTML, multiplicity=Multiplicity(1, 1))
    }
)
head8: BinaryAssociation = BinaryAssociation(
    name="head8",
    ends={
        Property(name="HEAD9", type=HTML_HEADElement, multiplicity=Multiplicity(1, 1)),
        Property(name="headElements", type=HTML_HEAD, multiplicity=Multiplicity(1, 1))
    }
)
bodyElements10: BinaryAssociation = BinaryAssociation(
    name="bodyElements10",
    ends={
        Property(name="HTML_BODYElement", type=HTML_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="HTML_BODY", type=HTML_BODYElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html11: BinaryAssociation = BinaryAssociation(
    name="html11",
    ends={
        Property(name="HTML12", type=HTML_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=HTML_HTML, multiplicity=Multiplicity(1, 1))
    }
)
trs13: BinaryAssociation = BinaryAssociation(
    name="trs13",
    ends={
        Property(name="TR", type=HTML_TABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=HTML_TR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table14: BinaryAssociation = BinaryAssociation(
    name="table14",
    ends={
        Property(name="TABLE", type=HTML_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="trs", type=HTML_TABLE, multiplicity=Multiplicity(1, 1))
    }
)
tds15: BinaryAssociation = BinaryAssociation(
    name="tds15",
    ends={
        Property(name="TD", type=HTML_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=HTML_TD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr16: BinaryAssociation = BinaryAssociation(
    name="tr16",
    ends={
        Property(name="TR17", type=HTML_TD, multiplicity=Multiplicity(1, 1)),
        Property(name="tds", type=HTML_TR, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HTML_HEAD_HTMLElement = Generalization(general=HTMLElement, specific=HTML_HEAD)
gen_HTML_HEADElement_HTMLElement = Generalization(general=HTMLElement, specific=HTML_HEADElement)
gen_HTML_LINK_HEADElement = Generalization(general=HEADElement, specific=HTML_LINK)
gen_HTML_TITLE_HEADElement = Generalization(general=HEADElement, specific=HTML_TITLE)
gen_HTML_BODY_HTMLElement = Generalization(general=HTMLElement, specific=HTML_BODY)
gen_HTML_BODYElement_HTMLElement = Generalization(general=HTMLElement, specific=HTML_BODYElement)
gen_HTML_H1_BODYElement = Generalization(general=BODYElement, specific=HTML_H1)
gen_HTML_H2_BODYElement = Generalization(general=BODYElement, specific=HTML_H2)
gen_HTML_H3_BODYElement = Generalization(general=BODYElement, specific=HTML_H3)
gen_HTML_H4_BODYElement = Generalization(general=BODYElement, specific=HTML_H4)
gen_HTML_EM_BODYElement = Generalization(general=BODYElement, specific=HTML_EM)
gen_HTML_STRONG_BODYElement = Generalization(general=BODYElement, specific=HTML_STRONG)
gen_HTML_B_BODYElement = Generalization(general=BODYElement, specific=HTML_B)
gen_HTML_I_BODYElement = Generalization(general=BODYElement, specific=HTML_I)
gen_HTML_TT_BODYElement = Generalization(general=BODYElement, specific=HTML_TT)
gen_HTML_PRE_BODYElement = Generalization(general=BODYElement, specific=HTML_PRE)
gen_HTML_BIG_BODYElement = Generalization(general=BODYElement, specific=HTML_BIG)
gen_HTML_SMALL_BODYElement = Generalization(general=BODYElement, specific=HTML_SMALL)
gen_HTML_SUB_BODYElement = Generalization(general=BODYElement, specific=HTML_SUB)
gen_HTML_SUP_BODYElement = Generalization(general=BODYElement, specific=HTML_SUP)
gen_HTML_STRIKE_BODYElement = Generalization(general=BODYElement, specific=HTML_STRIKE)
gen_HTML_FONT_BODYElement = Generalization(general=BODYElement, specific=HTML_FONT)
gen_HTML_IMG_BODYElement = Generalization(general=BODYElement, specific=HTML_IMG)
gen_HTML_BR_BODYElement = Generalization(general=BODYElement, specific=HTML_BR)
gen_HTML_MAP_BODYElement = Generalization(general=BODYElement, specific=HTML_MAP)
gen_HTML_AREA_BODYElement = Generalization(general=BODYElement, specific=HTML_AREA)
gen_HTML_STYLE_BODYElement = Generalization(general=BODYElement, specific=HTML_STYLE)
gen_HTML_EMBED_BODYElement = Generalization(general=BODYElement, specific=HTML_EMBED)
gen_HTML_NOEMBED_BODYElement = Generalization(general=BODYElement, specific=HTML_NOEMBED)
gen_HTML_SPAN_BODYElement = Generalization(general=BODYElement, specific=HTML_SPAN)
gen_HTML_A_BODYElement = Generalization(general=BODYElement, specific=HTML_A)
gen_HTML_DIV_BODYElement = Generalization(general=BODYElement, specific=HTML_DIV)
gen_HTML_P_BODYElement = Generalization(general=BODYElement, specific=HTML_P)
gen_HTML_TABLEElement_BODYElement = Generalization(general=BODYElement, specific=HTML_TABLEElement)
gen_HTML_TABLE_TABLEElement = Generalization(general=TABLEElement, specific=HTML_TABLE)
gen_HTML_TR_TABLEElement = Generalization(general=TABLEElement, specific=HTML_TR)
gen_HTML_TD_TABLEElement = Generalization(general=TABLEElement, specific=HTML_TD)
gen_HTML_TH_TD = Generalization(general=TD, specific=HTML_TH)
gen_HTML_OL_ListElement = Generalization(general=ListElement, specific=HTML_OL)
gen_HTML_UL_ListElement = Generalization(general=ListElement, specific=HTML_UL)
gen_HTML_LI_ListElement = Generalization(general=ListElement, specific=HTML_LI)
gen_HTML_IFRAME_FRAME = Generalization(general=FRAME, specific=HTML_IFRAME)

# Domain Model
domain_model = DomainModel(
    name="HTML",
    types={HTML_HTML, HTML_HEAD, HTML_BODY, HTML_HTMLElement, HTMLElement, HTML_HEADElement, HTML_LINK, HEADElement, HTML_TITLE, HTML_BODYElement, HTML_H1, BODYElement, HTML_H2, HTML_H3, HTML_H4, HTML_EM, HTML_STRONG, HTML_B, HTML_TT, HTML_PRE, HTML_BIG, HTML_SMALL, HTML_SUB, HTML_SUP, HTML_STRIKE, HTML_FONT, HTML_IMG, HTML_BR, HTML_MAP, HTML_AREA, HTML_STYLE, HTML_EMBED, HTML_I, HTML_NOEMBED, HTML_SPAN, HTML_A, HTML_DIV, HTML_P, HTML_TABLEElement, HTML_TABLE, TABLEElement, HTML_TR, HTML_TD, HTML_TH, TD, HTML_FORM, HTML_INPUT, HTML_TEXTAREA, HTML_SELECT, HTML_OPTION, HTML_ListElement, HTML_OL, ListElement, HTML_UL, HTML_LI, HTML_DL, HTML_DT, HTML_DD, HTML_APPLET, HTML_PARAM, HTML_OBJECT, HTML_FRAMESET, HTML_FRAME, HTML_NOFRAME, HTML_IFRAME, FRAME},
    associations={head0, body1, children4, headElements5, html6, head8, bodyElements10, html11, trs13, table14, tds15, tr16},
    generalizations={gen_HTML_HEAD_HTMLElement, gen_HTML_HEADElement_HTMLElement, gen_HTML_LINK_HEADElement, gen_HTML_TITLE_HEADElement, gen_HTML_BODY_HTMLElement, gen_HTML_BODYElement_HTMLElement, gen_HTML_H1_BODYElement, gen_HTML_H2_BODYElement, gen_HTML_H3_BODYElement, gen_HTML_H4_BODYElement, gen_HTML_EM_BODYElement, gen_HTML_STRONG_BODYElement, gen_HTML_B_BODYElement, gen_HTML_I_BODYElement, gen_HTML_TT_BODYElement, gen_HTML_PRE_BODYElement, gen_HTML_BIG_BODYElement, gen_HTML_SMALL_BODYElement, gen_HTML_SUB_BODYElement, gen_HTML_SUP_BODYElement, gen_HTML_STRIKE_BODYElement, gen_HTML_FONT_BODYElement, gen_HTML_IMG_BODYElement, gen_HTML_BR_BODYElement, gen_HTML_MAP_BODYElement, gen_HTML_AREA_BODYElement, gen_HTML_STYLE_BODYElement, gen_HTML_EMBED_BODYElement, gen_HTML_NOEMBED_BODYElement, gen_HTML_SPAN_BODYElement, gen_HTML_A_BODYElement, gen_HTML_DIV_BODYElement, gen_HTML_P_BODYElement, gen_HTML_TABLEElement_BODYElement, gen_HTML_TABLE_TABLEElement, gen_HTML_TR_TABLEElement, gen_HTML_TD_TABLEElement, gen_HTML_TH_TD, gen_HTML_OL_ListElement, gen_HTML_UL_ListElement, gen_HTML_LI_ListElement, gen_HTML_IFRAME_FRAME},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)