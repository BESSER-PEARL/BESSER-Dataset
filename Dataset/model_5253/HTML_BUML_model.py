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
html_HTMLElement = Class(name="html::HTMLElement")
HTMLElement = Class(name="HTMLElement")
html_HEADElement = Class(name="html::HEADElement", is_abstract=True)
html_LINK = Class(name="html::LINK")
HEADElement = Class(name="HEADElement")
html_TITLE = Class(name="html::TITLE")
html_HTML = Class(name="html::HTML")
html_HEAD = Class(name="html::HEAD")
html_BODY = Class(name="html::BODY")
html_H2 = Class(name="html::H2")
html_H3 = Class(name="html::H3")
html_H4 = Class(name="html::H4")
html_EM = Class(name="html::EM")
html_STRONG = Class(name="html::STRONG")
html_B = Class(name="html::B")
html_I = Class(name="html::I")
html_TT = Class(name="html::TT")
html_PRE = Class(name="html::PRE")
html_BIG = Class(name="html::BIG")
html_SMALL = Class(name="html::SMALL")
html_SUB = Class(name="html::SUB")
html_SUP = Class(name="html::SUP")
html_STRIKE = Class(name="html::STRIKE")
html_FONT = Class(name="html::FONT")
html_IMG = Class(name="html::IMG")
html_BODYElement = Class(name="html::BODYElement", is_abstract=True)
html_BR = Class(name="html::BR")
html_H1 = Class(name="html::H1")
BODYElement = Class(name="BODYElement")
html_STYLE = Class(name="html::STYLE")
html_EMBED = Class(name="html::EMBED")
html_NOEMBED = Class(name="html::NOEMBED")
html_SPAN = Class(name="html::SPAN")
html_A = Class(name="html::A")
html_DIV = Class(name="html::DIV")
html_P = Class(name="html::P")
html_TABLEElement = Class(name="html::TABLEElement", is_abstract=True)
html_TABLE = Class(name="html::TABLE")
TABLEElement = Class(name="TABLEElement")
html_MAP = Class(name="html::MAP")
html_AREA = Class(name="html::AREA")
html_TD = Class(name="html::TD")
html_TH = Class(name="html::TH")
TD = Class(name="TD")
html_FORM = Class(name="html::FORM")
html_INPUT = Class(name="html::INPUT")
html_TEXTAREA = Class(name="html::TEXTAREA")
html_TR = Class(name="html::TR")
html_UL = Class(name="html::UL")
html_LI = Class(name="html::LI")
html_DL = Class(name="html::DL")
html_DT = Class(name="html::DT")
html_DD = Class(name="html::DD")
html_APPLET = Class(name="html::APPLET")
html_PARAM = Class(name="html::PARAM")
html_OBJECT = Class(name="html::OBJECT")
html_FRAMESET = Class(name="html::FRAMESET")
html_SELECT = Class(name="html::SELECT")
html_OPTION = Class(name="html::OPTION")
html_ListElement = Class(name="html::ListElement", is_abstract=True)
html_OL = Class(name="html::OL")
ListElement = Class(name="ListElement")
html_FRAME = Class(name="html::FRAME")
html_NOFRAME = Class(name="html::NOFRAME")
html_IFRAME = Class(name="html::IFRAME")
FRAME = Class(name="FRAME")

# html_HTMLElement class attributes and methods
html_HTMLElement_value: Property = Property(name="value", type=StringType)
html_HTMLElement.attributes={html_HTMLElement_value}

# HTMLElement class attributes and methods

# html_HEADElement class attributes and methods

# html_LINK class attributes and methods
html_LINK_rel: Property = Property(name="rel", type=StringType)
html_LINK_title: Property = Property(name="title", type=StringType)
html_LINK_ahref: Property = Property(name="ahref", type=StringType)
html_LINK_type: Property = Property(name="type", type=StringType)
html_LINK.attributes={html_LINK_title, html_LINK_type, html_LINK_ahref, html_LINK_rel}

# HEADElement class attributes and methods

# html_TITLE class attributes and methods

# html_HTML class attributes and methods

# html_HEAD class attributes and methods

# html_BODY class attributes and methods
html_BODY_background: Property = Property(name="background", type=StringType)
html_BODY_bgcolor: Property = Property(name="bgcolor", type=StringType)
html_BODY_text: Property = Property(name="text", type=StringType)
html_BODY_link: Property = Property(name="link", type=StringType)
html_BODY_alink: Property = Property(name="alink", type=StringType)
html_BODY_vlink: Property = Property(name="vlink", type=StringType)
html_BODY.attributes={html_BODY_text, html_BODY_bgcolor, html_BODY_link, html_BODY_background, html_BODY_vlink, html_BODY_alink}

# html_H2 class attributes and methods

# html_H3 class attributes and methods

# html_H4 class attributes and methods

# html_EM class attributes and methods

# html_STRONG class attributes and methods

# html_B class attributes and methods

# html_I class attributes and methods

# html_TT class attributes and methods

# html_PRE class attributes and methods

# html_BIG class attributes and methods

# html_SMALL class attributes and methods

# html_SUB class attributes and methods

# html_SUP class attributes and methods

# html_STRIKE class attributes and methods

# html_FONT class attributes and methods
html_FONT_color: Property = Property(name="color", type=StringType)
html_FONT_face: Property = Property(name="face", type=StringType)
html_FONT_size: Property = Property(name="size", type=StringType)
html_FONT.attributes={html_FONT_size, html_FONT_face, html_FONT_color}

# html_IMG class attributes and methods
html_IMG_src: Property = Property(name="src", type=StringType)
html_IMG_width: Property = Property(name="width", type=StringType)
html_IMG_height: Property = Property(name="height", type=StringType)
html_IMG_alt: Property = Property(name="alt", type=StringType)
html_IMG_align: Property = Property(name="align", type=StringType)
html_IMG_vspace: Property = Property(name="vspace", type=StringType)
html_IMG_hspace: Property = Property(name="hspace", type=StringType)
html_IMG_ismap: Property = Property(name="ismap", type=StringType)
html_IMG_usemap: Property = Property(name="usemap", type=StringType)
html_IMG_border: Property = Property(name="border", type=StringType)
html_IMG.attributes={html_IMG_src, html_IMG_alt, html_IMG_align, html_IMG_border, html_IMG_width, html_IMG_vspace, html_IMG_ismap, html_IMG_usemap, html_IMG_height, html_IMG_hspace}

# html_BODYElement class attributes and methods

# html_BR class attributes and methods
html_BR_clear: Property = Property(name="clear", type=StringType)
html_BR.attributes={html_BR_clear}

# html_H1 class attributes and methods

# BODYElement class attributes and methods

# html_STYLE class attributes and methods

# html_EMBED class attributes and methods
html_EMBED_src: Property = Property(name="src", type=StringType)
html_EMBED_width: Property = Property(name="width", type=StringType)
html_EMBED_height: Property = Property(name="height", type=StringType)
html_EMBED_align: Property = Property(name="align", type=StringType)
html_EMBED_vspace: Property = Property(name="vspace", type=StringType)
html_EMBED_hspace: Property = Property(name="hspace", type=StringType)
html_EMBED_border: Property = Property(name="border", type=StringType)
html_EMBED.attributes={html_EMBED_width, html_EMBED_border, html_EMBED_hspace, html_EMBED_vspace, html_EMBED_align, html_EMBED_src, html_EMBED_height}

# html_NOEMBED class attributes and methods

# html_SPAN class attributes and methods
html_SPAN_style: Property = Property(name="style", type=StringType)
html_SPAN.attributes={html_SPAN_style}

# html_A class attributes and methods
html_A_ahref: Property = Property(name="ahref", type=StringType)
html_A_name: Property = Property(name="name", type=StringType)
html_A_id: Property = Property(name="id", type=StringType)
html_A.attributes={html_A_ahref, html_A_id, html_A_name}

# html_DIV class attributes and methods
html_DIV_align: Property = Property(name="align", type=StringType)
html_DIV.attributes={html_DIV_align}

# html_P class attributes and methods

# html_TABLEElement class attributes and methods
html_TABLEElement_bgcolor: Property = Property(name="bgcolor", type=StringType)
html_TABLEElement_background: Property = Property(name="background", type=StringType)
html_TABLEElement.attributes={html_TABLEElement_background, html_TABLEElement_bgcolor}

# html_TABLE class attributes and methods
html_TABLE_border: Property = Property(name="border", type=StringType)
html_TABLE_width: Property = Property(name="width", type=StringType)
html_TABLE_cellspacing: Property = Property(name="cellspacing", type=StringType)
html_TABLE_cellpadding: Property = Property(name="cellpadding", type=StringType)
html_TABLE.attributes={html_TABLE_width, html_TABLE_cellpadding, html_TABLE_cellspacing, html_TABLE_border}

# TABLEElement class attributes and methods

# html_MAP class attributes and methods

# html_AREA class attributes and methods
html_AREA_ahref: Property = Property(name="ahref", type=StringType)
html_AREA_shape: Property = Property(name="shape", type=StringType)
html_AREA_coords: Property = Property(name="coords", type=StringType)
html_AREA.attributes={html_AREA_coords, html_AREA_ahref, html_AREA_shape}

# html_TD class attributes and methods
html_TD_colspan: Property = Property(name="colspan", type=StringType)
html_TD_rowspan: Property = Property(name="rowspan", type=StringType)
html_TD_valign: Property = Property(name="valign", type=StringType)
html_TD_align: Property = Property(name="align", type=StringType)
html_TD_width: Property = Property(name="width", type=StringType)
html_TD.attributes={html_TD_align, html_TD_rowspan, html_TD_valign, html_TD_width, html_TD_colspan}

# html_TH class attributes and methods

# TD class attributes and methods

# html_FORM class attributes and methods
html_FORM_action: Property = Property(name="action", type=StringType)
html_FORM_method: Property = Property(name="method", type=StringType)
html_FORM.attributes={html_FORM_action, html_FORM_method}

# html_INPUT class attributes and methods
html_INPUT_align: Property = Property(name="align", type=StringType)
html_INPUT_maxlength: Property = Property(name="maxlength", type=StringType)
html_INPUT_size: Property = Property(name="size", type=StringType)
html_INPUT_checked: Property = Property(name="checked", type=StringType)
html_INPUT_src: Property = Property(name="src", type=StringType)
html_INPUT_inputValue: Property = Property(name="inputValue", type=StringType)
html_INPUT_name: Property = Property(name="name", type=StringType)
html_INPUT_type: Property = Property(name="type", type=StringType)
html_INPUT.attributes={html_INPUT_name, html_INPUT_align, html_INPUT_inputValue, html_INPUT_type, html_INPUT_src, html_INPUT_maxlength, html_INPUT_size, html_INPUT_checked}

# html_TEXTAREA class attributes and methods
html_TEXTAREA_name: Property = Property(name="name", type=StringType)
html_TEXTAREA_rows: Property = Property(name="rows", type=StringType)
html_TEXTAREA_cols: Property = Property(name="cols", type=StringType)
html_TEXTAREA.attributes={html_TEXTAREA_name, html_TEXTAREA_cols, html_TEXTAREA_rows}

# html_TR class attributes and methods
html_TR_valign: Property = Property(name="valign", type=StringType)
html_TR_align: Property = Property(name="align", type=StringType)
html_TR.attributes={html_TR_valign, html_TR_align}

# html_UL class attributes and methods

# html_LI class attributes and methods
html_LI_liValue: Property = Property(name="liValue", type=StringType)
html_LI.attributes={html_LI_liValue}

# html_DL class attributes and methods

# html_DT class attributes and methods

# html_DD class attributes and methods

# html_APPLET class attributes and methods
html_APPLET_applet: Property = Property(name="applet", type=StringType)
html_APPLET_class: Property = Property(name="class", type=StringType)
html_APPLET_src: Property = Property(name="src", type=StringType)
html_APPLET_align: Property = Property(name="align", type=StringType)
html_APPLET_width: Property = Property(name="width", type=StringType)
html_APPLET_height: Property = Property(name="height", type=StringType)
html_APPLET.attributes={html_APPLET_width, html_APPLET_src, html_APPLET_height, html_APPLET_class, html_APPLET_align, html_APPLET_applet}

# html_PARAM class attributes and methods
html_PARAM_name: Property = Property(name="name", type=StringType)
html_PARAM_paramValue: Property = Property(name="paramValue", type=StringType)
html_PARAM.attributes={html_PARAM_paramValue, html_PARAM_name}

# html_OBJECT class attributes and methods
html_OBJECT_classid: Property = Property(name="classid", type=StringType)
html_OBJECT_id: Property = Property(name="id", type=StringType)
html_OBJECT_data: Property = Property(name="data", type=StringType)
html_OBJECT_type: Property = Property(name="type", type=StringType)
html_OBJECT_standby: Property = Property(name="standby", type=StringType)
html_OBJECT.attributes={html_OBJECT_data, html_OBJECT_standby, html_OBJECT_classid, html_OBJECT_id, html_OBJECT_type}

# html_FRAMESET class attributes and methods
html_FRAMESET_rows: Property = Property(name="rows", type=StringType)
html_FRAMESET_cols: Property = Property(name="cols", type=StringType)
html_FRAMESET_framespacing: Property = Property(name="framespacing", type=StringType)
html_FRAMESET_frameborder: Property = Property(name="frameborder", type=StringType)
html_FRAMESET_border: Property = Property(name="border", type=StringType)
html_FRAMESET.attributes={html_FRAMESET_border, html_FRAMESET_cols, html_FRAMESET_rows, html_FRAMESET_frameborder, html_FRAMESET_framespacing}

# html_SELECT class attributes and methods
html_SELECT_multiple: Property = Property(name="multiple", type=StringType)
html_SELECT_size: Property = Property(name="size", type=StringType)
html_SELECT_name: Property = Property(name="name", type=StringType)
html_SELECT.attributes={html_SELECT_multiple, html_SELECT_name, html_SELECT_size}

# html_OPTION class attributes and methods
html_OPTION_selected: Property = Property(name="selected", type=StringType)
html_OPTION_optionValue: Property = Property(name="optionValue", type=StringType)
html_OPTION.attributes={html_OPTION_selected, html_OPTION_optionValue}

# html_ListElement class attributes and methods
html_ListElement_type: Property = Property(name="type", type=StringType)
html_ListElement.attributes={html_ListElement_type}

# html_OL class attributes and methods
html_OL_start: Property = Property(name="start", type=StringType)
html_OL.attributes={html_OL_start}

# ListElement class attributes and methods

# html_FRAME class attributes and methods
html_FRAME_src: Property = Property(name="src", type=StringType)
html_FRAME_name: Property = Property(name="name", type=StringType)
html_FRAME_marginwidth: Property = Property(name="marginwidth", type=StringType)
html_FRAME_marginheight: Property = Property(name="marginheight", type=StringType)
html_FRAME_scrolling: Property = Property(name="scrolling", type=StringType)
html_FRAME_noresize: Property = Property(name="noresize", type=StringType)
html_FRAME.attributes={html_FRAME_marginwidth, html_FRAME_marginheight, html_FRAME_src, html_FRAME_noresize, html_FRAME_name, html_FRAME_scrolling}

# html_NOFRAME class attributes and methods

# html_IFRAME class attributes and methods

# FRAME class attributes and methods

# Relationships
body1: BinaryAssociation = BinaryAssociation(
    name="body1",
    ends={
        Property(name="html2", type=html_BODY, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="BODY", type=html_HTML, multiplicity=Multiplicity(1, 1))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="HTMLElement", type=html_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=html_HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent6: BinaryAssociation = BinaryAssociation(
    name="parent6",
    ends={
        Property(name="HTMLElement7", type=html_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=html_HTMLElement, multiplicity=Multiplicity(0, 1))
    }
)
headElements8: BinaryAssociation = BinaryAssociation(
    name="headElements8",
    ends={
        Property(name="HEADElement", type=html_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=html_HEADElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html9: BinaryAssociation = BinaryAssociation(
    name="html9",
    ends={
        Property(name="HTML", type=html_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head10", type=html_HTML, multiplicity=Multiplicity(1, 1))
    }
)
head11: BinaryAssociation = BinaryAssociation(
    name="head11",
    ends={
        Property(name="HEAD12", type=html_HEADElement, multiplicity=Multiplicity(1, 1)),
        Property(name="headElements", type=html_HEAD, multiplicity=Multiplicity(1, 1))
    }
)
head0: BinaryAssociation = BinaryAssociation(
    name="head0",
    ends={
        Property(name="HEAD", type=html_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html", type=html_HEAD, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyElements13: BinaryAssociation = BinaryAssociation(
    name="bodyElements13",
    ends={
        Property(name="BODYElement", type=html_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=html_BODYElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html14: BinaryAssociation = BinaryAssociation(
    name="html14",
    ends={
        Property(name="HTML16", type=html_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body15", type=html_HTML, multiplicity=Multiplicity(1, 1))
    }
)
body17: BinaryAssociation = BinaryAssociation(
    name="body17",
    ends={
        Property(name="BODY18", type=html_BODYElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyElements", type=html_BODY, multiplicity=Multiplicity(0, 1))
    }
)
tds21: BinaryAssociation = BinaryAssociation(
    name="tds21",
    ends={
        Property(name="TD", type=html_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=html_TD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr22: BinaryAssociation = BinaryAssociation(
    name="tr22",
    ends={
        Property(name="TR23", type=html_TD, multiplicity=Multiplicity(1, 1)),
        Property(name="tds", type=html_TR, multiplicity=Multiplicity(1, 1))
    }
)
trs19: BinaryAssociation = BinaryAssociation(
    name="trs19",
    ends={
        Property(name="TR", type=html_TABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=html_TR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table20: BinaryAssociation = BinaryAssociation(
    name="table20",
    ends={
        Property(name="TABLE", type=html_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="trs", type=html_TABLE, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_html_HEAD_HTMLElement = Generalization(general=HTMLElement, specific=html_HEAD)
gen_html_HEADElement_HTMLElement = Generalization(general=HTMLElement, specific=html_HEADElement)
gen_html_LINK_HEADElement = Generalization(general=HEADElement, specific=html_LINK)
gen_html_TITLE_HEADElement = Generalization(general=HEADElement, specific=html_TITLE)
gen_html_BODY_HTMLElement = Generalization(general=HTMLElement, specific=html_BODY)
gen_html_H2_BODYElement = Generalization(general=BODYElement, specific=html_H2)
gen_html_H3_BODYElement = Generalization(general=BODYElement, specific=html_H3)
gen_html_H4_BODYElement = Generalization(general=BODYElement, specific=html_H4)
gen_html_EM_BODYElement = Generalization(general=BODYElement, specific=html_EM)
gen_html_STRONG_BODYElement = Generalization(general=BODYElement, specific=html_STRONG)
gen_html_B_BODYElement = Generalization(general=BODYElement, specific=html_B)
gen_html_I_BODYElement = Generalization(general=BODYElement, specific=html_I)
gen_html_TT_BODYElement = Generalization(general=BODYElement, specific=html_TT)
gen_html_PRE_BODYElement = Generalization(general=BODYElement, specific=html_PRE)
gen_html_BIG_BODYElement = Generalization(general=BODYElement, specific=html_BIG)
gen_html_SMALL_BODYElement = Generalization(general=BODYElement, specific=html_SMALL)
gen_html_SUB_BODYElement = Generalization(general=BODYElement, specific=html_SUB)
gen_html_SUP_BODYElement = Generalization(general=BODYElement, specific=html_SUP)
gen_html_STRIKE_BODYElement = Generalization(general=BODYElement, specific=html_STRIKE)
gen_html_FONT_BODYElement = Generalization(general=BODYElement, specific=html_FONT)
gen_html_IMG_BODYElement = Generalization(general=BODYElement, specific=html_IMG)
gen_html_BR_BODYElement = Generalization(general=BODYElement, specific=html_BR)
gen_html_BODYElement_HTMLElement = Generalization(general=HTMLElement, specific=html_BODYElement)
gen_html_H1_BODYElement = Generalization(general=BODYElement, specific=html_H1)
gen_html_STYLE_BODYElement = Generalization(general=BODYElement, specific=html_STYLE)
gen_html_EMBED_BODYElement = Generalization(general=BODYElement, specific=html_EMBED)
gen_html_NOEMBED_BODYElement = Generalization(general=BODYElement, specific=html_NOEMBED)
gen_html_SPAN_BODYElement = Generalization(general=BODYElement, specific=html_SPAN)
gen_html_A_BODYElement = Generalization(general=BODYElement, specific=html_A)
gen_html_DIV_BODYElement = Generalization(general=BODYElement, specific=html_DIV)
gen_html_P_BODYElement = Generalization(general=BODYElement, specific=html_P)
gen_html_TABLEElement_BODYElement = Generalization(general=BODYElement, specific=html_TABLEElement)
gen_html_TABLE_TABLEElement = Generalization(general=TABLEElement, specific=html_TABLE)
gen_html_MAP_BODYElement = Generalization(general=BODYElement, specific=html_MAP)
gen_html_AREA_BODYElement = Generalization(general=BODYElement, specific=html_AREA)
gen_html_TD_TABLEElement = Generalization(general=TABLEElement, specific=html_TD)
gen_html_TH_TD = Generalization(general=TD, specific=html_TH)
gen_html_TR_TABLEElement = Generalization(general=TABLEElement, specific=html_TR)
gen_html_UL_ListElement = Generalization(general=ListElement, specific=html_UL)
gen_html_LI_ListElement = Generalization(general=ListElement, specific=html_LI)
gen_html_OL_ListElement = Generalization(general=ListElement, specific=html_OL)
gen_html_IFRAME_FRAME = Generalization(general=FRAME, specific=html_IFRAME)

# Domain Model
domain_model = DomainModel(
    name="html",
    types={html_HTMLElement, HTMLElement, html_HEADElement, html_LINK, HEADElement, html_TITLE, html_HTML, html_HEAD, html_BODY, html_H2, html_H3, html_H4, html_EM, html_STRONG, html_B, html_I, html_TT, html_PRE, html_BIG, html_SMALL, html_SUB, html_SUP, html_STRIKE, html_FONT, html_IMG, html_BODYElement, html_BR, html_H1, BODYElement, html_STYLE, html_EMBED, html_NOEMBED, html_SPAN, html_A, html_DIV, html_P, html_TABLEElement, html_TABLE, TABLEElement, html_MAP, html_AREA, html_TD, html_TH, TD, html_FORM, html_INPUT, html_TEXTAREA, html_TR, html_UL, html_LI, html_DL, html_DT, html_DD, html_APPLET, html_PARAM, html_OBJECT, html_FRAMESET, html_SELECT, html_OPTION, html_ListElement, html_OL, ListElement, html_FRAME, html_NOFRAME, html_IFRAME, FRAME},
    associations={body1, children4, parent6, headElements8, html9, head11, head0, bodyElements13, html14, body17, tds21, tr22, trs19, table20},
    generalizations={gen_html_HEAD_HTMLElement, gen_html_HEADElement_HTMLElement, gen_html_LINK_HEADElement, gen_html_TITLE_HEADElement, gen_html_BODY_HTMLElement, gen_html_H2_BODYElement, gen_html_H3_BODYElement, gen_html_H4_BODYElement, gen_html_EM_BODYElement, gen_html_STRONG_BODYElement, gen_html_B_BODYElement, gen_html_I_BODYElement, gen_html_TT_BODYElement, gen_html_PRE_BODYElement, gen_html_BIG_BODYElement, gen_html_SMALL_BODYElement, gen_html_SUB_BODYElement, gen_html_SUP_BODYElement, gen_html_STRIKE_BODYElement, gen_html_FONT_BODYElement, gen_html_IMG_BODYElement, gen_html_BR_BODYElement, gen_html_BODYElement_HTMLElement, gen_html_H1_BODYElement, gen_html_STYLE_BODYElement, gen_html_EMBED_BODYElement, gen_html_NOEMBED_BODYElement, gen_html_SPAN_BODYElement, gen_html_A_BODYElement, gen_html_DIV_BODYElement, gen_html_P_BODYElement, gen_html_TABLEElement_BODYElement, gen_html_TABLE_TABLEElement, gen_html_MAP_BODYElement, gen_html_AREA_BODYElement, gen_html_TD_TABLEElement, gen_html_TH_TD, gen_html_TR_TABLEElement, gen_html_UL_ListElement, gen_html_LI_ListElement, gen_html_OL_ListElement, gen_html_IFRAME_FRAME},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)