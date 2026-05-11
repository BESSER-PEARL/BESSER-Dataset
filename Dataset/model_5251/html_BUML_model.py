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
BODYElement = Class(name="BODYElement")
Html_HTML = Class(name="Html_HTML")
HEAD = Class(name="HEAD")
Html_BODYElement = Class(name="Html_BODYElement", is_abstract=True)
BODY = Class(name="BODY")
Html_H1 = Class(name="Html_H1")
Html_H2 = Class(name="Html_H2")
Html_HTMLElement = Class(name="Html_HTMLElement")
Html_H3 = Class(name="Html_H3")
HTMLElement = Class(name="HTMLElement")
Html_HEAD = Class(name="Html_HEAD")
HEADElement = Class(name="HEADElement")
HTML = Class(name="HTML")
Html_HEADElement = Class(name="Html_HEADElement", is_abstract=True)
Html_LINK = Class(name="Html_LINK")
Html_TITLE = Class(name="Html_TITLE")
Html_BODY = Class(name="Html_BODY")
Html_BR = Class(name="Html_BR")
Html_MAP = Class(name="Html_MAP")
Html_AREA = Class(name="Html_AREA")
Html_H4 = Class(name="Html_H4")
Html_EM = Class(name="Html_EM")
Html_STRONG = Class(name="Html_STRONG")
Html_B = Class(name="Html_B")
Html_I = Class(name="Html_I")
Html_TT = Class(name="Html_TT")
Html_PRE = Class(name="Html_PRE")
Html_BIG = Class(name="Html_BIG")
Html_SMALL = Class(name="Html_SMALL")
Html_SUB = Class(name="Html_SUB")
Html_SUP = Class(name="Html_SUP")
Html_STRIKE = Class(name="Html_STRIKE")
Html_FONT = Class(name="Html_FONT")
Html_IMG = Class(name="Html_IMG")
Html_TABLE = Class(name="Html_TABLE")
TABLEElement = Class(name="TABLEElement")
TR = Class(name="TR")
Html_TR = Class(name="Html_TR")
Html_STYLE = Class(name="Html_STYLE")
Html_EMBED = Class(name="Html_EMBED")
Html_NOEMBED = Class(name="Html_NOEMBED")
Html_SPAN = Class(name="Html_SPAN")
Html_A = Class(name="Html_A")
Html_DIV = Class(name="Html_DIV")
Html_P = Class(name="Html_P")
Html_TABLEElement = Class(name="Html_TABLEElement", is_abstract=True)
Html_TEXTAREA = Class(name="Html_TEXTAREA")
Html_SELECT = Class(name="Html_SELECT")
Html_OPTION = Class(name="Html_OPTION")
TABLE = Class(name="TABLE")
TD = Class(name="TD")
Html_TD = Class(name="Html_TD")
Html_TH = Class(name="Html_TH")
Html_FORM = Class(name="Html_FORM")
Html_INPUT = Class(name="Html_INPUT")
Html_OBJECT = Class(name="Html_OBJECT")
Html_FRAMESET = Class(name="Html_FRAMESET")
Html_ListElement = Class(name="Html_ListElement", is_abstract=True)
Html_OL = Class(name="Html_OL")
ListElement = Class(name="ListElement")
Html_UL = Class(name="Html_UL")
Html_LI = Class(name="Html_LI")
Html_DL = Class(name="Html_DL")
Html_DT = Class(name="Html_DT")
Html_DD = Class(name="Html_DD")
Html_APPLET = Class(name="Html_APPLET")
Html_PARAM = Class(name="Html_PARAM")
Html_FRAME = Class(name="Html_FRAME")
Html_NOFRAME = Class(name="Html_NOFRAME")
Html_IFRAME = Class(name="Html_IFRAME")
FRAME = Class(name="FRAME")

# BODYElement class attributes and methods

# Html_HTML class attributes and methods

# HEAD class attributes and methods

# Html_BODYElement class attributes and methods

# BODY class attributes and methods

# Html_H1 class attributes and methods

# Html_H2 class attributes and methods

# Html_HTMLElement class attributes and methods
Html_HTMLElement_value: Property = Property(name="value", type=StringType)
Html_HTMLElement_id: Property = Property(name="id", type=StringType)
Html_HTMLElement_class_: Property = Property(name="class_", type=StringType)
Html_HTMLElement_title: Property = Property(name="title", type=StringType)
Html_HTMLElement.attributes={Html_HTMLElement_value, Html_HTMLElement_title, Html_HTMLElement_id, Html_HTMLElement_class_}

# Html_H3 class attributes and methods

# HTMLElement class attributes and methods

# Html_HEAD class attributes and methods

# HEADElement class attributes and methods

# HTML class attributes and methods

# Html_HEADElement class attributes and methods

# Html_LINK class attributes and methods
Html_LINK_rel: Property = Property(name="rel", type=StringType)
Html_LINK_ahref: Property = Property(name="ahref", type=StringType)
Html_LINK_type: Property = Property(name="type", type=StringType)
Html_LINK.attributes={Html_LINK_type, Html_LINK_ahref, Html_LINK_rel}

# Html_TITLE class attributes and methods

# Html_BODY class attributes and methods
Html_BODY_background: Property = Property(name="background", type=StringType)
Html_BODY_bgcolor: Property = Property(name="bgcolor", type=StringType)
Html_BODY_text: Property = Property(name="text", type=StringType)
Html_BODY_link: Property = Property(name="link", type=StringType)
Html_BODY_alink: Property = Property(name="alink", type=StringType)
Html_BODY_vlink: Property = Property(name="vlink", type=StringType)
Html_BODY.attributes={Html_BODY_vlink, Html_BODY_alink, Html_BODY_bgcolor, Html_BODY_text, Html_BODY_background, Html_BODY_link}

# Html_BR class attributes and methods
Html_BR_clear: Property = Property(name="clear", type=StringType)
Html_BR.attributes={Html_BR_clear}

# Html_MAP class attributes and methods

# Html_AREA class attributes and methods
Html_AREA_shape: Property = Property(name="shape", type=StringType)
Html_AREA_coords: Property = Property(name="coords", type=StringType)
Html_AREA_ahref: Property = Property(name="ahref", type=StringType)
Html_AREA.attributes={Html_AREA_shape, Html_AREA_ahref, Html_AREA_coords}

# Html_H4 class attributes and methods

# Html_EM class attributes and methods

# Html_STRONG class attributes and methods

# Html_B class attributes and methods

# Html_I class attributes and methods

# Html_TT class attributes and methods

# Html_PRE class attributes and methods

# Html_BIG class attributes and methods

# Html_SMALL class attributes and methods

# Html_SUB class attributes and methods

# Html_SUP class attributes and methods

# Html_STRIKE class attributes and methods

# Html_FONT class attributes and methods
Html_FONT_color: Property = Property(name="color", type=StringType)
Html_FONT_face: Property = Property(name="face", type=StringType)
Html_FONT_size: Property = Property(name="size", type=StringType)
Html_FONT.attributes={Html_FONT_size, Html_FONT_color, Html_FONT_face}

# Html_IMG class attributes and methods
Html_IMG_ismap: Property = Property(name="ismap", type=StringType)
Html_IMG_usemap: Property = Property(name="usemap", type=StringType)
Html_IMG_border: Property = Property(name="border", type=StringType)
Html_IMG_src: Property = Property(name="src", type=StringType)
Html_IMG_width: Property = Property(name="width", type=StringType)
Html_IMG_height: Property = Property(name="height", type=StringType)
Html_IMG_alt: Property = Property(name="alt", type=StringType)
Html_IMG_align: Property = Property(name="align", type=StringType)
Html_IMG_vspace: Property = Property(name="vspace", type=StringType)
Html_IMG_hspace: Property = Property(name="hspace", type=StringType)
Html_IMG.attributes={Html_IMG_alt, Html_IMG_align, Html_IMG_height, Html_IMG_src, Html_IMG_border, Html_IMG_vspace, Html_IMG_hspace, Html_IMG_width, Html_IMG_ismap, Html_IMG_usemap}

# Html_TABLE class attributes and methods
Html_TABLE_border: Property = Property(name="border", type=StringType)
Html_TABLE_width: Property = Property(name="width", type=StringType)
Html_TABLE_cellspacing: Property = Property(name="cellspacing", type=StringType)
Html_TABLE_cellpadding: Property = Property(name="cellpadding", type=StringType)
Html_TABLE.attributes={Html_TABLE_border, Html_TABLE_cellspacing, Html_TABLE_cellpadding, Html_TABLE_width}

# TABLEElement class attributes and methods

# TR class attributes and methods

# Html_TR class attributes and methods
Html_TR_valign: Property = Property(name="valign", type=StringType)
Html_TR_align: Property = Property(name="align", type=StringType)
Html_TR.attributes={Html_TR_valign, Html_TR_align}

# Html_STYLE class attributes and methods

# Html_EMBED class attributes and methods
Html_EMBED_src: Property = Property(name="src", type=StringType)
Html_EMBED_width: Property = Property(name="width", type=StringType)
Html_EMBED_height: Property = Property(name="height", type=StringType)
Html_EMBED_align: Property = Property(name="align", type=StringType)
Html_EMBED_vspace: Property = Property(name="vspace", type=StringType)
Html_EMBED_hspace: Property = Property(name="hspace", type=StringType)
Html_EMBED_border: Property = Property(name="border", type=StringType)
Html_EMBED.attributes={Html_EMBED_border, Html_EMBED_width, Html_EMBED_align, Html_EMBED_height, Html_EMBED_vspace, Html_EMBED_src, Html_EMBED_hspace}

# Html_NOEMBED class attributes and methods

# Html_SPAN class attributes and methods
Html_SPAN_style: Property = Property(name="style", type=StringType)
Html_SPAN.attributes={Html_SPAN_style}

# Html_A class attributes and methods
Html_A_ahref: Property = Property(name="ahref", type=StringType)
Html_A_name: Property = Property(name="name", type=StringType)
Html_A.attributes={Html_A_name, Html_A_ahref}

# Html_DIV class attributes and methods
Html_DIV_align: Property = Property(name="align", type=StringType)
Html_DIV.attributes={Html_DIV_align}

# Html_P class attributes and methods

# Html_TABLEElement class attributes and methods
Html_TABLEElement_bgcolor: Property = Property(name="bgcolor", type=StringType)
Html_TABLEElement_background: Property = Property(name="background", type=StringType)
Html_TABLEElement.attributes={Html_TABLEElement_bgcolor, Html_TABLEElement_background}

# Html_TEXTAREA class attributes and methods
Html_TEXTAREA_name: Property = Property(name="name", type=StringType)
Html_TEXTAREA_rows: Property = Property(name="rows", type=StringType)
Html_TEXTAREA_cols: Property = Property(name="cols", type=StringType)
Html_TEXTAREA.attributes={Html_TEXTAREA_name, Html_TEXTAREA_rows, Html_TEXTAREA_cols}

# Html_SELECT class attributes and methods
Html_SELECT_multiple: Property = Property(name="multiple", type=StringType)
Html_SELECT_size: Property = Property(name="size", type=StringType)
Html_SELECT_name: Property = Property(name="name", type=StringType)
Html_SELECT.attributes={Html_SELECT_name, Html_SELECT_size, Html_SELECT_multiple}

# Html_OPTION class attributes and methods
Html_OPTION_selected: Property = Property(name="selected", type=StringType)
Html_OPTION_optionValue: Property = Property(name="optionValue", type=StringType)
Html_OPTION.attributes={Html_OPTION_optionValue, Html_OPTION_selected}

# TABLE class attributes and methods

# TD class attributes and methods

# Html_TD class attributes and methods
Html_TD_colspan: Property = Property(name="colspan", type=StringType)
Html_TD_rowspan: Property = Property(name="rowspan", type=StringType)
Html_TD_valign: Property = Property(name="valign", type=StringType)
Html_TD_align: Property = Property(name="align", type=StringType)
Html_TD_width: Property = Property(name="width", type=StringType)
Html_TD.attributes={Html_TD_rowspan, Html_TD_colspan, Html_TD_width, Html_TD_align, Html_TD_valign}

# Html_TH class attributes and methods

# Html_FORM class attributes and methods
Html_FORM_action: Property = Property(name="action", type=StringType)
Html_FORM_method: Property = Property(name="method", type=StringType)
Html_FORM.attributes={Html_FORM_method, Html_FORM_action}

# Html_INPUT class attributes and methods
Html_INPUT_type: Property = Property(name="type", type=StringType)
Html_INPUT_align: Property = Property(name="align", type=StringType)
Html_INPUT_maxlength: Property = Property(name="maxlength", type=StringType)
Html_INPUT_size: Property = Property(name="size", type=StringType)
Html_INPUT_checked: Property = Property(name="checked", type=StringType)
Html_INPUT_src: Property = Property(name="src", type=StringType)
Html_INPUT_inputValue: Property = Property(name="inputValue", type=StringType)
Html_INPUT_name: Property = Property(name="name", type=StringType)
Html_INPUT.attributes={Html_INPUT_src, Html_INPUT_inputValue, Html_INPUT_align, Html_INPUT_checked, Html_INPUT_name, Html_INPUT_size, Html_INPUT_maxlength, Html_INPUT_type}

# Html_OBJECT class attributes and methods
Html_OBJECT_classid: Property = Property(name="classid", type=StringType)
Html_OBJECT_data: Property = Property(name="data", type=StringType)
Html_OBJECT_type: Property = Property(name="type", type=StringType)
Html_OBJECT_standby: Property = Property(name="standby", type=StringType)
Html_OBJECT.attributes={Html_OBJECT_classid, Html_OBJECT_type, Html_OBJECT_data, Html_OBJECT_standby}

# Html_FRAMESET class attributes and methods
Html_FRAMESET_rows: Property = Property(name="rows", type=StringType)
Html_FRAMESET_cols: Property = Property(name="cols", type=StringType)
Html_FRAMESET_framespacing: Property = Property(name="framespacing", type=StringType)
Html_FRAMESET_frameborder: Property = Property(name="frameborder", type=StringType)
Html_FRAMESET_border: Property = Property(name="border", type=StringType)
Html_FRAMESET.attributes={Html_FRAMESET_border, Html_FRAMESET_rows, Html_FRAMESET_frameborder, Html_FRAMESET_cols, Html_FRAMESET_framespacing}

# Html_ListElement class attributes and methods
Html_ListElement_type: Property = Property(name="type", type=StringType)
Html_ListElement.attributes={Html_ListElement_type}

# Html_OL class attributes and methods
Html_OL_start: Property = Property(name="start", type=StringType)
Html_OL.attributes={Html_OL_start}

# ListElement class attributes and methods

# Html_UL class attributes and methods

# Html_LI class attributes and methods
Html_LI_liValue: Property = Property(name="liValue", type=StringType)
Html_LI.attributes={Html_LI_liValue}

# Html_DL class attributes and methods

# Html_DT class attributes and methods

# Html_DD class attributes and methods

# Html_APPLET class attributes and methods
Html_APPLET_applet: Property = Property(name="applet", type=StringType)
Html_APPLET_class_: Property = Property(name="class_", type=StringType)
Html_APPLET_src: Property = Property(name="src", type=StringType)
Html_APPLET_align: Property = Property(name="align", type=StringType)
Html_APPLET_width: Property = Property(name="width", type=StringType)
Html_APPLET_height: Property = Property(name="height", type=StringType)
Html_APPLET.attributes={Html_APPLET_src, Html_APPLET_class_, Html_APPLET_width, Html_APPLET_height, Html_APPLET_align, Html_APPLET_applet}

# Html_PARAM class attributes and methods
Html_PARAM_name: Property = Property(name="name", type=StringType)
Html_PARAM_paramValue: Property = Property(name="paramValue", type=StringType)
Html_PARAM.attributes={Html_PARAM_name, Html_PARAM_paramValue}

# Html_FRAME class attributes and methods
Html_FRAME_src: Property = Property(name="src", type=StringType)
Html_FRAME_name: Property = Property(name="name", type=StringType)
Html_FRAME_marginwidth: Property = Property(name="marginwidth", type=StringType)
Html_FRAME_marginheight: Property = Property(name="marginheight", type=StringType)
Html_FRAME_scrolling: Property = Property(name="scrolling", type=StringType)
Html_FRAME_noresize: Property = Property(name="noresize", type=StringType)
Html_FRAME.attributes={Html_FRAME_scrolling, Html_FRAME_src, Html_FRAME_marginwidth, Html_FRAME_noresize, Html_FRAME_marginheight, Html_FRAME_name}

# Html_NOFRAME class attributes and methods

# Html_IFRAME class attributes and methods

# FRAME class attributes and methods

# Relationships
bodyElements11: BinaryAssociation = BinaryAssociation(
    name="bodyElements11",
    ends={
        Property(name="BODYElement", type=Html_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=BODYElement, multiplicity=Multiplicity(0, 9999))
    }
)
html12: BinaryAssociation = BinaryAssociation(
    name="html12",
    ends={
        Property(name="HTML14", type=Html_BODY, multiplicity=Multiplicity(1, 1)),
        Property(name="body13", type=HTML, multiplicity=Multiplicity(1, 1))
    }
)
head0: BinaryAssociation = BinaryAssociation(
    name="head0",
    ends={
        Property(name="HEAD", type=Html_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html", type=HEAD, multiplicity=Multiplicity(1, 1))
    }
)
body15: BinaryAssociation = BinaryAssociation(
    name="body15",
    ends={
        Property(name="BODY16", type=Html_BODYElement, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyElements", type=BODY, multiplicity=Multiplicity(1, 1))
    }
)
body1: BinaryAssociation = BinaryAssociation(
    name="body1",
    ends={
        Property(name="BODY", type=Html_HTML, multiplicity=Multiplicity(1, 1)),
        Property(name="html2", type=BODY, multiplicity=Multiplicity(1, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="HTMLElement", type=Html_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=HTMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="HTMLElement5", type=Html_HTMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=HTMLElement, multiplicity=Multiplicity(1, 1))
    }
)
headElements6: BinaryAssociation = BinaryAssociation(
    name="headElements6",
    ends={
        Property(name="HEADElement", type=Html_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=HEADElement, multiplicity=Multiplicity(0, 9999))
    }
)
html7: BinaryAssociation = BinaryAssociation(
    name="html7",
    ends={
        Property(name="HTML", type=Html_HEAD, multiplicity=Multiplicity(1, 1)),
        Property(name="head8", type=HTML, multiplicity=Multiplicity(1, 1))
    }
)
head9: BinaryAssociation = BinaryAssociation(
    name="head9",
    ends={
        Property(name="HEAD10", type=Html_HEADElement, multiplicity=Multiplicity(1, 1)),
        Property(name="headElements", type=HEAD, multiplicity=Multiplicity(1, 1))
    }
)
trs17: BinaryAssociation = BinaryAssociation(
    name="trs17",
    ends={
        Property(name="TR", type=Html_TABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=TR, multiplicity=Multiplicity(0, 9999))
    }
)
table18: BinaryAssociation = BinaryAssociation(
    name="table18",
    ends={
        Property(name="TABLE", type=Html_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="trs", type=TABLE, multiplicity=Multiplicity(1, 1))
    }
)
tds19: BinaryAssociation = BinaryAssociation(
    name="tds19",
    ends={
        Property(name="TD", type=Html_TR, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=TD, multiplicity=Multiplicity(0, 9999))
    }
)
tr20: BinaryAssociation = BinaryAssociation(
    name="tr20",
    ends={
        Property(name="TR21", type=Html_TD, multiplicity=Multiplicity(1, 1)),
        Property(name="tds", type=TR, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Html_BODYElement_HTMLElement = Generalization(general=HTMLElement, specific=Html_BODYElement)
gen_Html_H1_BODYElement = Generalization(general=BODYElement, specific=Html_H1)
gen_Html_H2_BODYElement = Generalization(general=BODYElement, specific=Html_H2)
gen_Html_H3_BODYElement = Generalization(general=BODYElement, specific=Html_H3)
gen_Html_HEAD_HTMLElement = Generalization(general=HTMLElement, specific=Html_HEAD)
gen_Html_HEADElement_HTMLElement = Generalization(general=HTMLElement, specific=Html_HEADElement)
gen_Html_LINK_HEADElement = Generalization(general=HEADElement, specific=Html_LINK)
gen_Html_TITLE_HEADElement = Generalization(general=HEADElement, specific=Html_TITLE)
gen_Html_BODY_HTMLElement = Generalization(general=HTMLElement, specific=Html_BODY)
gen_Html_BR_BODYElement = Generalization(general=BODYElement, specific=Html_BR)
gen_Html_MAP_BODYElement = Generalization(general=BODYElement, specific=Html_MAP)
gen_Html_AREA_BODYElement = Generalization(general=BODYElement, specific=Html_AREA)
gen_Html_H4_BODYElement = Generalization(general=BODYElement, specific=Html_H4)
gen_Html_EM_BODYElement = Generalization(general=BODYElement, specific=Html_EM)
gen_Html_STRONG_BODYElement = Generalization(general=BODYElement, specific=Html_STRONG)
gen_Html_B_BODYElement = Generalization(general=BODYElement, specific=Html_B)
gen_Html_I_BODYElement = Generalization(general=BODYElement, specific=Html_I)
gen_Html_TT_BODYElement = Generalization(general=BODYElement, specific=Html_TT)
gen_Html_PRE_BODYElement = Generalization(general=BODYElement, specific=Html_PRE)
gen_Html_BIG_BODYElement = Generalization(general=BODYElement, specific=Html_BIG)
gen_Html_SMALL_BODYElement = Generalization(general=BODYElement, specific=Html_SMALL)
gen_Html_SUB_BODYElement = Generalization(general=BODYElement, specific=Html_SUB)
gen_Html_SUP_BODYElement = Generalization(general=BODYElement, specific=Html_SUP)
gen_Html_STRIKE_BODYElement = Generalization(general=BODYElement, specific=Html_STRIKE)
gen_Html_FONT_BODYElement = Generalization(general=BODYElement, specific=Html_FONT)
gen_Html_IMG_BODYElement = Generalization(general=BODYElement, specific=Html_IMG)
gen_Html_TABLE_TABLEElement = Generalization(general=TABLEElement, specific=Html_TABLE)
gen_Html_TR_TABLEElement = Generalization(general=TABLEElement, specific=Html_TR)
gen_Html_STYLE_BODYElement = Generalization(general=BODYElement, specific=Html_STYLE)
gen_Html_EMBED_BODYElement = Generalization(general=BODYElement, specific=Html_EMBED)
gen_Html_NOEMBED_BODYElement = Generalization(general=BODYElement, specific=Html_NOEMBED)
gen_Html_SPAN_BODYElement = Generalization(general=BODYElement, specific=Html_SPAN)
gen_Html_A_BODYElement = Generalization(general=BODYElement, specific=Html_A)
gen_Html_DIV_BODYElement = Generalization(general=BODYElement, specific=Html_DIV)
gen_Html_P_BODYElement = Generalization(general=BODYElement, specific=Html_P)
gen_Html_TABLEElement_BODYElement = Generalization(general=BODYElement, specific=Html_TABLEElement)
gen_Html_TD_TABLEElement = Generalization(general=TABLEElement, specific=Html_TD)
gen_Html_TH_TD = Generalization(general=TD, specific=Html_TH)
gen_Html_OL_ListElement = Generalization(general=ListElement, specific=Html_OL)
gen_Html_UL_ListElement = Generalization(general=ListElement, specific=Html_UL)
gen_Html_LI_ListElement = Generalization(general=ListElement, specific=Html_LI)
gen_Html_IFRAME_FRAME = Generalization(general=FRAME, specific=Html_IFRAME)

# Domain Model
domain_model = DomainModel(
    name="Html",
    types={BODYElement, Html_HTML, HEAD, Html_BODYElement, BODY, Html_H1, Html_H2, Html_HTMLElement, Html_H3, HTMLElement, Html_HEAD, HEADElement, HTML, Html_HEADElement, Html_LINK, Html_TITLE, Html_BODY, Html_BR, Html_MAP, Html_AREA, Html_H4, Html_EM, Html_STRONG, Html_B, Html_I, Html_TT, Html_PRE, Html_BIG, Html_SMALL, Html_SUB, Html_SUP, Html_STRIKE, Html_FONT, Html_IMG, Html_TABLE, TABLEElement, TR, Html_TR, Html_STYLE, Html_EMBED, Html_NOEMBED, Html_SPAN, Html_A, Html_DIV, Html_P, Html_TABLEElement, Html_TEXTAREA, Html_SELECT, Html_OPTION, TABLE, TD, Html_TD, Html_TH, Html_FORM, Html_INPUT, Html_OBJECT, Html_FRAMESET, Html_ListElement, Html_OL, ListElement, Html_UL, Html_LI, Html_DL, Html_DT, Html_DD, Html_APPLET, Html_PARAM, Html_FRAME, Html_NOFRAME, Html_IFRAME, FRAME},
    associations={bodyElements11, html12, head0, body15, body1, children3, parent4, headElements6, html7, head9, trs17, table18, tds19, tr20},
    generalizations={gen_Html_BODYElement_HTMLElement, gen_Html_H1_BODYElement, gen_Html_H2_BODYElement, gen_Html_H3_BODYElement, gen_Html_HEAD_HTMLElement, gen_Html_HEADElement_HTMLElement, gen_Html_LINK_HEADElement, gen_Html_TITLE_HEADElement, gen_Html_BODY_HTMLElement, gen_Html_BR_BODYElement, gen_Html_MAP_BODYElement, gen_Html_AREA_BODYElement, gen_Html_H4_BODYElement, gen_Html_EM_BODYElement, gen_Html_STRONG_BODYElement, gen_Html_B_BODYElement, gen_Html_I_BODYElement, gen_Html_TT_BODYElement, gen_Html_PRE_BODYElement, gen_Html_BIG_BODYElement, gen_Html_SMALL_BODYElement, gen_Html_SUB_BODYElement, gen_Html_SUP_BODYElement, gen_Html_STRIKE_BODYElement, gen_Html_FONT_BODYElement, gen_Html_IMG_BODYElement, gen_Html_TABLE_TABLEElement, gen_Html_TR_TABLEElement, gen_Html_STYLE_BODYElement, gen_Html_EMBED_BODYElement, gen_Html_NOEMBED_BODYElement, gen_Html_SPAN_BODYElement, gen_Html_A_BODYElement, gen_Html_DIV_BODYElement, gen_Html_P_BODYElement, gen_Html_TABLEElement_BODYElement, gen_Html_TD_TABLEElement, gen_Html_TH_TD, gen_Html_OL_ListElement, gen_Html_UL_ListElement, gen_Html_LI_ListElement, gen_Html_IFRAME_FRAME},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)