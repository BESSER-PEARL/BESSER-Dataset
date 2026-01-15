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
defaultname_HTML = Class(name="defaultname::HTML")
defaultname_HEAD = Class(name="defaultname::HEAD")
defaultname_BODYElement = Class(name="defaultname::BODYElement", is_abstract=True)
defaultname_BODY = Class(name="defaultname::BODY")
defaultname_HTMLElement = Class(name="defaultname::HTMLElement")
HTMLElement = Class(name="HTMLElement")
defaultname_HEADElement = Class(name="defaultname::HEADElement", is_abstract=True)
defaultname_LINK = Class(name="defaultname::LINK")
HEADElement = Class(name="HEADElement")
defaultname_TITLE = Class(name="defaultname::TITLE")
defaultname_BR = Class(name="defaultname::BR")
defaultname_H1 = Class(name="defaultname::H1")
BODYElement = Class(name="BODYElement")
defaultname_H2 = Class(name="defaultname::H2")
defaultname_H3 = Class(name="defaultname::H3")
defaultname_H4 = Class(name="defaultname::H4")
defaultname_EM = Class(name="defaultname::EM")
defaultname_STRONG = Class(name="defaultname::STRONG")
defaultname_B = Class(name="defaultname::B")
defaultname_I = Class(name="defaultname::I")
defaultname_TT = Class(name="defaultname::TT")
defaultname_PRE = Class(name="defaultname::PRE")
defaultname_BIG = Class(name="defaultname::BIG")
defaultname_SMALL = Class(name="defaultname::SMALL")
defaultname_SUB = Class(name="defaultname::SUB")
defaultname_SUP = Class(name="defaultname::SUP")
defaultname_STRIKE = Class(name="defaultname::STRIKE")
defaultname_FONT = Class(name="defaultname::FONT")
defaultname_IMG = Class(name="defaultname::IMG")
defaultname_TR = Class(name="defaultname::TR")
defaultname_MAP = Class(name="defaultname::MAP")
defaultname_AREA = Class(name="defaultname::AREA")
defaultname_STYLE = Class(name="defaultname::STYLE")
defaultname_EMBED = Class(name="defaultname::EMBED")
defaultname_NOEMBED = Class(name="defaultname::NOEMBED")
defaultname_SPAN = Class(name="defaultname::SPAN")
defaultname_A = Class(name="defaultname::A")
defaultname_DIV = Class(name="defaultname::DIV")
defaultname_P = Class(name="defaultname::P")
defaultname_TABLEElement = Class(name="defaultname::TABLEElement", is_abstract=True)
defaultname_TABLE = Class(name="defaultname::TABLE")
TABLEElement = Class(name="TABLEElement")
defaultname_OPTION = Class(name="defaultname::OPTION")
defaultname_ListElement = Class(name="defaultname::ListElement", is_abstract=True)
defaultname_OL = Class(name="defaultname::OL")
ListElement = Class(name="ListElement")
defaultname_TD = Class(name="defaultname::TD")
defaultname_TH = Class(name="defaultname::TH")
TD = Class(name="TD")
defaultname_FORM = Class(name="defaultname::FORM")
defaultname_INPUT = Class(name="defaultname::INPUT")
defaultname_TEXTAREA = Class(name="defaultname::TEXTAREA")
defaultname_SELECT = Class(name="defaultname::SELECT")
defaultname_NOFRAME = Class(name="defaultname::NOFRAME")
defaultname_IFRAME = Class(name="defaultname::IFRAME")
FRAME = Class(name="FRAME")
defaultname_UL = Class(name="defaultname::UL")
defaultname_LI = Class(name="defaultname::LI")
defaultname_DL = Class(name="defaultname::DL")
defaultname_DT = Class(name="defaultname::DT")
defaultname_DD = Class(name="defaultname::DD")
defaultname_APPLET = Class(name="defaultname::APPLET")
defaultname_PARAM = Class(name="defaultname::PARAM")
defaultname_OBJECT = Class(name="defaultname::OBJECT")
defaultname_FRAMESET = Class(name="defaultname::FRAMESET")
defaultname_FRAME = Class(name="defaultname::FRAME")

# defaultname_HTML class attributes and methods

# defaultname_HEAD class attributes and methods

# defaultname_BODYElement class attributes and methods

# defaultname_BODY class attributes and methods
defaultname_BODY_text: Property = Property(name="text", type=StringType)
defaultname_BODY_link: Property = Property(name="link", type=StringType)
defaultname_BODY_alink: Property = Property(name="alink", type=StringType)
defaultname_BODY_vlink: Property = Property(name="vlink", type=StringType)
defaultname_BODY_background: Property = Property(name="background", type=StringType)
defaultname_BODY_bgcolor: Property = Property(name="bgcolor", type=StringType)
defaultname_BODY.attributes={defaultname_BODY_alink, defaultname_BODY_link, defaultname_BODY_background, defaultname_BODY_bgcolor, defaultname_BODY_vlink, defaultname_BODY_text}

# defaultname_HTMLElement class attributes and methods
defaultname_HTMLElement_value: Property = Property(name="value", type=StringType)
defaultname_HTMLElement.attributes={defaultname_HTMLElement_value}

# HTMLElement class attributes and methods

# defaultname_HEADElement class attributes and methods

# defaultname_LINK class attributes and methods
defaultname_LINK_rel: Property = Property(name="rel", type=StringType)
defaultname_LINK_title: Property = Property(name="title", type=StringType)
defaultname_LINK_ahref: Property = Property(name="ahref", type=StringType)
defaultname_LINK_type: Property = Property(name="type", type=StringType)
defaultname_LINK.attributes={defaultname_LINK_type, defaultname_LINK_rel, defaultname_LINK_title, defaultname_LINK_ahref}

# HEADElement class attributes and methods

# defaultname_TITLE class attributes and methods

# defaultname_BR class attributes and methods
defaultname_BR_clear: Property = Property(name="clear", type=StringType)
defaultname_BR.attributes={defaultname_BR_clear}

# defaultname_H1 class attributes and methods

# BODYElement class attributes and methods

# defaultname_H2 class attributes and methods

# defaultname_H3 class attributes and methods

# defaultname_H4 class attributes and methods

# defaultname_EM class attributes and methods

# defaultname_STRONG class attributes and methods

# defaultname_B class attributes and methods

# defaultname_I class attributes and methods

# defaultname_TT class attributes and methods

# defaultname_PRE class attributes and methods

# defaultname_BIG class attributes and methods

# defaultname_SMALL class attributes and methods

# defaultname_SUB class attributes and methods

# defaultname_SUP class attributes and methods

# defaultname_STRIKE class attributes and methods

# defaultname_FONT class attributes and methods
defaultname_FONT_color: Property = Property(name="color", type=StringType)
defaultname_FONT_face: Property = Property(name="face", type=StringType)
defaultname_FONT_size: Property = Property(name="size", type=StringType)
defaultname_FONT.attributes={defaultname_FONT_face, defaultname_FONT_size, defaultname_FONT_color}

# defaultname_IMG class attributes and methods
defaultname_IMG_hspace: Property = Property(name="hspace", type=StringType)
defaultname_IMG_ismap: Property = Property(name="ismap", type=StringType)
defaultname_IMG_usemap: Property = Property(name="usemap", type=StringType)
defaultname_IMG_border: Property = Property(name="border", type=StringType)
defaultname_IMG_src: Property = Property(name="src", type=StringType)
defaultname_IMG_width: Property = Property(name="width", type=StringType)
defaultname_IMG_height: Property = Property(name="height", type=StringType)
defaultname_IMG_alt: Property = Property(name="alt", type=StringType)
defaultname_IMG_align: Property = Property(name="align", type=StringType)
defaultname_IMG_vspace: Property = Property(name="vspace", type=StringType)
defaultname_IMG.attributes={defaultname_IMG_height, defaultname_IMG_src, defaultname_IMG_ismap, defaultname_IMG_hspace, defaultname_IMG_border, defaultname_IMG_usemap, defaultname_IMG_align, defaultname_IMG_width, defaultname_IMG_alt, defaultname_IMG_vspace}

# defaultname_TR class attributes and methods
defaultname_TR_valign: Property = Property(name="valign", type=StringType)
defaultname_TR_align: Property = Property(name="align", type=StringType)
defaultname_TR.attributes={defaultname_TR_valign, defaultname_TR_align}

# defaultname_MAP class attributes and methods

# defaultname_AREA class attributes and methods
defaultname_AREA_shape: Property = Property(name="shape", type=StringType)
defaultname_AREA_coords: Property = Property(name="coords", type=StringType)
defaultname_AREA_ahref: Property = Property(name="ahref", type=StringType)
defaultname_AREA.attributes={defaultname_AREA_ahref, defaultname_AREA_coords, defaultname_AREA_shape}

# defaultname_STYLE class attributes and methods

# defaultname_EMBED class attributes and methods
defaultname_EMBED_src: Property = Property(name="src", type=StringType)
defaultname_EMBED_width: Property = Property(name="width", type=StringType)
defaultname_EMBED_height: Property = Property(name="height", type=StringType)
defaultname_EMBED_align: Property = Property(name="align", type=StringType)
defaultname_EMBED_vspace: Property = Property(name="vspace", type=StringType)
defaultname_EMBED_hspace: Property = Property(name="hspace", type=StringType)
defaultname_EMBED_border: Property = Property(name="border", type=StringType)
defaultname_EMBED.attributes={defaultname_EMBED_align, defaultname_EMBED_src, defaultname_EMBED_border, defaultname_EMBED_vspace, defaultname_EMBED_height, defaultname_EMBED_width, defaultname_EMBED_hspace}

# defaultname_NOEMBED class attributes and methods

# defaultname_SPAN class attributes and methods
defaultname_SPAN_style: Property = Property(name="style", type=StringType)
defaultname_SPAN.attributes={defaultname_SPAN_style}

# defaultname_A class attributes and methods
defaultname_A_ahref: Property = Property(name="ahref", type=StringType)
defaultname_A_name: Property = Property(name="name", type=StringType)
defaultname_A_id: Property = Property(name="id", type=StringType)
defaultname_A.attributes={defaultname_A_name, defaultname_A_id, defaultname_A_ahref}

# defaultname_DIV class attributes and methods
defaultname_DIV_align: Property = Property(name="align", type=StringType)
defaultname_DIV.attributes={defaultname_DIV_align}

# defaultname_P class attributes and methods

# defaultname_TABLEElement class attributes and methods
defaultname_TABLEElement_bgcolor: Property = Property(name="bgcolor", type=StringType)
defaultname_TABLEElement_background: Property = Property(name="background", type=StringType)
defaultname_TABLEElement.attributes={defaultname_TABLEElement_background, defaultname_TABLEElement_bgcolor}

# defaultname_TABLE class attributes and methods
defaultname_TABLE_cellpadding: Property = Property(name="cellpadding", type=StringType)
defaultname_TABLE_border: Property = Property(name="border", type=StringType)
defaultname_TABLE_width: Property = Property(name="width", type=StringType)
defaultname_TABLE_cellspacing: Property = Property(name="cellspacing", type=StringType)
defaultname_TABLE.attributes={defaultname_TABLE_border, defaultname_TABLE_cellspacing, defaultname_TABLE_width, defaultname_TABLE_cellpadding}

# TABLEElement class attributes and methods

# defaultname_OPTION class attributes and methods
defaultname_OPTION_selected: Property = Property(name="selected", type=StringType)
defaultname_OPTION_optionValue: Property = Property(name="optionValue", type=StringType)
defaultname_OPTION.attributes={defaultname_OPTION_optionValue, defaultname_OPTION_selected}

# defaultname_ListElement class attributes and methods
defaultname_ListElement_type: Property = Property(name="type", type=StringType)
defaultname_ListElement.attributes={defaultname_ListElement_type}

# defaultname_OL class attributes and methods
defaultname_OL_start: Property = Property(name="start", type=StringType)
defaultname_OL.attributes={defaultname_OL_start}

# ListElement class attributes and methods

# defaultname_TD class attributes and methods
defaultname_TD_colspan: Property = Property(name="colspan", type=StringType)
defaultname_TD_rowspan: Property = Property(name="rowspan", type=StringType)
defaultname_TD_valign: Property = Property(name="valign", type=StringType)
defaultname_TD_align: Property = Property(name="align", type=StringType)
defaultname_TD_width: Property = Property(name="width", type=StringType)
defaultname_TD.attributes={defaultname_TD_rowspan, defaultname_TD_colspan, defaultname_TD_align, defaultname_TD_width, defaultname_TD_valign}

# defaultname_TH class attributes and methods

# TD class attributes and methods

# defaultname_FORM class attributes and methods
defaultname_FORM_action: Property = Property(name="action", type=StringType)
defaultname_FORM_method: Property = Property(name="method", type=StringType)
defaultname_FORM.attributes={defaultname_FORM_action, defaultname_FORM_method}

# defaultname_INPUT class attributes and methods
defaultname_INPUT_align: Property = Property(name="align", type=StringType)
defaultname_INPUT_maxlength: Property = Property(name="maxlength", type=StringType)
defaultname_INPUT_size: Property = Property(name="size", type=StringType)
defaultname_INPUT_checked: Property = Property(name="checked", type=StringType)
defaultname_INPUT_src: Property = Property(name="src", type=StringType)
defaultname_INPUT_inputValue: Property = Property(name="inputValue", type=StringType)
defaultname_INPUT_name: Property = Property(name="name", type=StringType)
defaultname_INPUT_type: Property = Property(name="type", type=StringType)
defaultname_INPUT.attributes={defaultname_INPUT_checked, defaultname_INPUT_src, defaultname_INPUT_inputValue, defaultname_INPUT_name, defaultname_INPUT_align, defaultname_INPUT_type, defaultname_INPUT_maxlength, defaultname_INPUT_size}

# defaultname_TEXTAREA class attributes and methods
defaultname_TEXTAREA_name: Property = Property(name="name", type=StringType)
defaultname_TEXTAREA_rows: Property = Property(name="rows", type=StringType)
defaultname_TEXTAREA_cols: Property = Property(name="cols", type=StringType)
defaultname_TEXTAREA.attributes={defaultname_TEXTAREA_rows, defaultname_TEXTAREA_cols, defaultname_TEXTAREA_name}

# defaultname_SELECT class attributes and methods
defaultname_SELECT_name: Property = Property(name="name", type=StringType)
defaultname_SELECT_multiple: Property = Property(name="multiple", type=StringType)
defaultname_SELECT_size: Property = Property(name="size", type=StringType)
defaultname_SELECT.attributes={defaultname_SELECT_name, defaultname_SELECT_multiple, defaultname_SELECT_size}

# defaultname_NOFRAME class attributes and methods

# defaultname_IFRAME class attributes and methods

# FRAME class attributes and methods

# defaultname_UL class attributes and methods

# defaultname_LI class attributes and methods
defaultname_LI_liValue: Property = Property(name="liValue", type=StringType)
defaultname_LI.attributes={defaultname_LI_liValue}

# defaultname_DL class attributes and methods

# defaultname_DT class attributes and methods

# defaultname_DD class attributes and methods

# defaultname_APPLET class attributes and methods
defaultname_APPLET_applet: Property = Property(name="applet", type=StringType)
defaultname_APPLET_class: Property = Property(name="class", type=StringType)
defaultname_APPLET_src: Property = Property(name="src", type=StringType)
defaultname_APPLET_align: Property = Property(name="align", type=StringType)
defaultname_APPLET_width: Property = Property(name="width", type=StringType)
defaultname_APPLET_height: Property = Property(name="height", type=StringType)
defaultname_APPLET.attributes={defaultname_APPLET_height, defaultname_APPLET_applet, defaultname_APPLET_src, defaultname_APPLET_width, defaultname_APPLET_align, defaultname_APPLET_class}

# defaultname_PARAM class attributes and methods
defaultname_PARAM_name: Property = Property(name="name", type=StringType)
defaultname_PARAM_paramValue: Property = Property(name="paramValue", type=StringType)
defaultname_PARAM.attributes={defaultname_PARAM_paramValue, defaultname_PARAM_name}

# defaultname_OBJECT class attributes and methods
defaultname_OBJECT_classid: Property = Property(name="classid", type=StringType)
defaultname_OBJECT_id: Property = Property(name="id", type=StringType)
defaultname_OBJECT_data: Property = Property(name="data", type=StringType)
defaultname_OBJECT_type: Property = Property(name="type", type=StringType)
defaultname_OBJECT_standby: Property = Property(name="standby", type=StringType)
defaultname_OBJECT.attributes={defaultname_OBJECT_classid, defaultname_OBJECT_id, defaultname_OBJECT_standby, defaultname_OBJECT_type, defaultname_OBJECT_data}

# defaultname_FRAMESET class attributes and methods
defaultname_FRAMESET_rows: Property = Property(name="rows", type=StringType)
defaultname_FRAMESET_cols: Property = Property(name="cols", type=StringType)
defaultname_FRAMESET_framespacing: Property = Property(name="framespacing", type=StringType)
defaultname_FRAMESET_frameborder: Property = Property(name="frameborder", type=StringType)
defaultname_FRAMESET_border: Property = Property(name="border", type=StringType)
defaultname_FRAMESET.attributes={defaultname_FRAMESET_frameborder, defaultname_FRAMESET_framespacing, defaultname_FRAMESET_rows, defaultname_FRAMESET_cols, defaultname_FRAMESET_border}

# defaultname_FRAME class attributes and methods
defaultname_FRAME_marginheight: Property = Property(name="marginheight", type=StringType)
defaultname_FRAME_scrolling: Property = Property(name="scrolling", type=StringType)
defaultname_FRAME_noresize: Property = Property(name="noresize", type=StringType)
defaultname_FRAME_src: Property = Property(name="src", type=StringType)
defaultname_FRAME_name: Property = Property(name="name", type=StringType)
defaultname_FRAME_marginwidth: Property = Property(name="marginwidth", type=StringType)
defaultname_FRAME.attributes={defaultname_FRAME_scrolling, defaultname_FRAME_marginheight, defaultname_FRAME_name, defaultname_FRAME_noresize, defaultname_FRAME_src, defaultname_FRAME_marginwidth}

# Relationships
head0: BinaryAssociation = BinaryAssociation(
    name="head0",
    ends={
        Property(name="HEAD", type=defaultname_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html", type=defaultname_HEAD, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyElements13: BinaryAssociation = BinaryAssociation(
    name="bodyElements13",
    ends={
        Property(name="BODYElement", type=defaultname_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=defaultname_BODYElement, multiplicity=Multiplicity(0, 9999))
    }
)
body1: BinaryAssociation = BinaryAssociation(
    name="body1",
    ends={
        Property(name="BODY", type=defaultname_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html2", type=defaultname_BODY, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="HTMLElement", type=defaultname_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=defaultname_HTMLElement, multiplicity=Multiplicity(0, 9999))
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="HTMLElement7", type=defaultname_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=defaultname_HTMLElement, multiplicity=Multiplicity(1, 1))
    }
)
headElements8: BinaryAssociation = BinaryAssociation(
    name="headElements8",
    ends={
        Property(name="HEADElement", type=defaultname_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=defaultname_HEADElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html9: BinaryAssociation = BinaryAssociation(
    name="html9",
    ends={
        Property(name="HTML", type=defaultname_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head10", type=defaultname_HTML, multiplicity=Multiplicity(1, 1))
    }
)
head11: BinaryAssociation = BinaryAssociation(
    name="head11",
    ends={
        Property(name="HEAD12", type=defaultname_HEADElement, multiplicity=Multiplicity(1, 1)),
        Property(name="headElements", type=defaultname_HEAD, multiplicity=Multiplicity(1, 1))
    }
)
html14: BinaryAssociation = BinaryAssociation(
    name="html14",
    ends={
        Property(name="HTML16", type=defaultname_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body15", type=defaultname_HTML, multiplicity=Multiplicity(1, 1))
    }
)
body17: BinaryAssociation = BinaryAssociation(
    name="body17",
    ends={
        Property(name="BODY18", type=defaultname_BODYElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyElements", type=defaultname_BODY, multiplicity=Multiplicity(1, 1))
    }
)
trs19: BinaryAssociation = BinaryAssociation(
    name="trs19",
    ends={
        Property(name="TR", type=defaultname_TABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=defaultname_TR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table20: BinaryAssociation = BinaryAssociation(
    name="table20",
    ends={
        Property(name="TABLE", type=defaultname_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="trs", type=defaultname_TABLE, multiplicity=Multiplicity(1, 1))
    }
)
tds21: BinaryAssociation = BinaryAssociation(
    name="tds21",
    ends={
        Property(name="TD", type=defaultname_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=defaultname_TD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr22: BinaryAssociation = BinaryAssociation(
    name="tr22",
    ends={
        Property(name="TR23", type=defaultname_TD, multiplicity=Multiplicity(1, 1)),
        Property(name="tds", type=defaultname_TR, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_defaultname_HEAD_HTMLElement = Generalization(general=HTMLElement, specific=defaultname_HEAD)
gen_defaultname_HEADElement_HTMLElement = Generalization(general=HTMLElement, specific=defaultname_HEADElement)
gen_defaultname_LINK_HEADElement = Generalization(general=HEADElement, specific=defaultname_LINK)
gen_defaultname_TITLE_HEADElement = Generalization(general=HEADElement, specific=defaultname_TITLE)
gen_defaultname_BODY_HTMLElement = Generalization(general=HTMLElement, specific=defaultname_BODY)
gen_defaultname_BR_BODYElement = Generalization(general=BODYElement, specific=defaultname_BR)
gen_defaultname_BODYElement_HTMLElement = Generalization(general=HTMLElement, specific=defaultname_BODYElement)
gen_defaultname_H1_BODYElement = Generalization(general=BODYElement, specific=defaultname_H1)
gen_defaultname_H2_BODYElement = Generalization(general=BODYElement, specific=defaultname_H2)
gen_defaultname_H3_BODYElement = Generalization(general=BODYElement, specific=defaultname_H3)
gen_defaultname_H4_BODYElement = Generalization(general=BODYElement, specific=defaultname_H4)
gen_defaultname_EM_BODYElement = Generalization(general=BODYElement, specific=defaultname_EM)
gen_defaultname_STRONG_BODYElement = Generalization(general=BODYElement, specific=defaultname_STRONG)
gen_defaultname_B_BODYElement = Generalization(general=BODYElement, specific=defaultname_B)
gen_defaultname_I_BODYElement = Generalization(general=BODYElement, specific=defaultname_I)
gen_defaultname_TT_BODYElement = Generalization(general=BODYElement, specific=defaultname_TT)
gen_defaultname_PRE_BODYElement = Generalization(general=BODYElement, specific=defaultname_PRE)
gen_defaultname_BIG_BODYElement = Generalization(general=BODYElement, specific=defaultname_BIG)
gen_defaultname_SMALL_BODYElement = Generalization(general=BODYElement, specific=defaultname_SMALL)
gen_defaultname_SUB_BODYElement = Generalization(general=BODYElement, specific=defaultname_SUB)
gen_defaultname_SUP_BODYElement = Generalization(general=BODYElement, specific=defaultname_SUP)
gen_defaultname_STRIKE_BODYElement = Generalization(general=BODYElement, specific=defaultname_STRIKE)
gen_defaultname_FONT_BODYElement = Generalization(general=BODYElement, specific=defaultname_FONT)
gen_defaultname_IMG_BODYElement = Generalization(general=BODYElement, specific=defaultname_IMG)
gen_defaultname_TR_TABLEElement = Generalization(general=TABLEElement, specific=defaultname_TR)
gen_defaultname_MAP_BODYElement = Generalization(general=BODYElement, specific=defaultname_MAP)
gen_defaultname_AREA_BODYElement = Generalization(general=BODYElement, specific=defaultname_AREA)
gen_defaultname_STYLE_BODYElement = Generalization(general=BODYElement, specific=defaultname_STYLE)
gen_defaultname_EMBED_BODYElement = Generalization(general=BODYElement, specific=defaultname_EMBED)
gen_defaultname_NOEMBED_BODYElement = Generalization(general=BODYElement, specific=defaultname_NOEMBED)
gen_defaultname_SPAN_BODYElement = Generalization(general=BODYElement, specific=defaultname_SPAN)
gen_defaultname_A_BODYElement = Generalization(general=BODYElement, specific=defaultname_A)
gen_defaultname_DIV_BODYElement = Generalization(general=BODYElement, specific=defaultname_DIV)
gen_defaultname_P_BODYElement = Generalization(general=BODYElement, specific=defaultname_P)
gen_defaultname_TABLEElement_BODYElement = Generalization(general=BODYElement, specific=defaultname_TABLEElement)
gen_defaultname_TABLE_TABLEElement = Generalization(general=TABLEElement, specific=defaultname_TABLE)
gen_defaultname_OL_ListElement = Generalization(general=ListElement, specific=defaultname_OL)
gen_defaultname_TD_TABLEElement = Generalization(general=TABLEElement, specific=defaultname_TD)
gen_defaultname_TH_TD = Generalization(general=TD, specific=defaultname_TH)
gen_defaultname_IFRAME_FRAME = Generalization(general=FRAME, specific=defaultname_IFRAME)
gen_defaultname_UL_ListElement = Generalization(general=ListElement, specific=defaultname_UL)
gen_defaultname_LI_ListElement = Generalization(general=ListElement, specific=defaultname_LI)

# Domain Model
domain_model = DomainModel(
    name="defaultname",
    types={defaultname_HTML, defaultname_HEAD, defaultname_BODYElement, defaultname_BODY, defaultname_HTMLElement, HTMLElement, defaultname_HEADElement, defaultname_LINK, HEADElement, defaultname_TITLE, defaultname_BR, defaultname_H1, BODYElement, defaultname_H2, defaultname_H3, defaultname_H4, defaultname_EM, defaultname_STRONG, defaultname_B, defaultname_I, defaultname_TT, defaultname_PRE, defaultname_BIG, defaultname_SMALL, defaultname_SUB, defaultname_SUP, defaultname_STRIKE, defaultname_FONT, defaultname_IMG, defaultname_TR, defaultname_MAP, defaultname_AREA, defaultname_STYLE, defaultname_EMBED, defaultname_NOEMBED, defaultname_SPAN, defaultname_A, defaultname_DIV, defaultname_P, defaultname_TABLEElement, defaultname_TABLE, TABLEElement, defaultname_OPTION, defaultname_ListElement, defaultname_OL, ListElement, defaultname_TD, defaultname_TH, TD, defaultname_FORM, defaultname_INPUT, defaultname_TEXTAREA, defaultname_SELECT, defaultname_NOFRAME, defaultname_IFRAME, FRAME, defaultname_UL, defaultname_LI, defaultname_DL, defaultname_DT, defaultname_DD, defaultname_APPLET, defaultname_PARAM, defaultname_OBJECT, defaultname_FRAMESET, defaultname_FRAME},
    associations={head0, bodyElements13, body1, children4, parent6, headElements8, html9, head11, html14, body17, trs19, table20, tds21, tr22},
    generalizations={gen_defaultname_HEAD_HTMLElement, gen_defaultname_HEADElement_HTMLElement, gen_defaultname_LINK_HEADElement, gen_defaultname_TITLE_HEADElement, gen_defaultname_BODY_HTMLElement, gen_defaultname_BR_BODYElement, gen_defaultname_BODYElement_HTMLElement, gen_defaultname_H1_BODYElement, gen_defaultname_H2_BODYElement, gen_defaultname_H3_BODYElement, gen_defaultname_H4_BODYElement, gen_defaultname_EM_BODYElement, gen_defaultname_STRONG_BODYElement, gen_defaultname_B_BODYElement, gen_defaultname_I_BODYElement, gen_defaultname_TT_BODYElement, gen_defaultname_PRE_BODYElement, gen_defaultname_BIG_BODYElement, gen_defaultname_SMALL_BODYElement, gen_defaultname_SUB_BODYElement, gen_defaultname_SUP_BODYElement, gen_defaultname_STRIKE_BODYElement, gen_defaultname_FONT_BODYElement, gen_defaultname_IMG_BODYElement, gen_defaultname_TR_TABLEElement, gen_defaultname_MAP_BODYElement, gen_defaultname_AREA_BODYElement, gen_defaultname_STYLE_BODYElement, gen_defaultname_EMBED_BODYElement, gen_defaultname_NOEMBED_BODYElement, gen_defaultname_SPAN_BODYElement, gen_defaultname_A_BODYElement, gen_defaultname_DIV_BODYElement, gen_defaultname_P_BODYElement, gen_defaultname_TABLEElement_BODYElement, gen_defaultname_TABLE_TABLEElement, gen_defaultname_OL_ListElement, gen_defaultname_TD_TABLEElement, gen_defaultname_TH_TD, gen_defaultname_IFRAME_FRAME, gen_defaultname_UL_ListElement, gen_defaultname_LI_ListElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)