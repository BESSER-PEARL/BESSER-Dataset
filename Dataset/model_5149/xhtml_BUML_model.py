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
AlignType: Enumeration = Enumeration(
    name="AlignType",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="justify"),
			EnumerationLiteral(name="char")
    }
)

ImageKind: Enumeration = Enumeration(
    name="ImageKind",
    literals={
            EnumerationLiteral(name="applicationPostscript"),
			EnumerationLiteral(name="applicationPdf"),
			EnumerationLiteral(name="applicationPng"),
			EnumerationLiteral(name="applicationSvgXml"),
			EnumerationLiteral(name="applicationJpeg"),
			EnumerationLiteral(name="imageGif")
    }
)

MediaType: Enumeration = Enumeration(
    name="MediaType",
    literals={
            EnumerationLiteral(name="textPlain"),
			EnumerationLiteral(name="textHtml"),
			EnumerationLiteral(name="applicationPdf"),
			EnumerationLiteral(name="textXml"),
			EnumerationLiteral(name="textRtf"),
			EnumerationLiteral(name="applicationMsword"),
			EnumerationLiteral(name="audioMpeg"),
			EnumerationLiteral(name="imagePng"),
			EnumerationLiteral(name="imageGif"),
			EnumerationLiteral(name="imageJpeg"),
			EnumerationLiteral(name="videoMpeg")
    }
)

MifClassType: Enumeration = Enumeration(
    name="MifClassType",
    literals={
            EnumerationLiteral(name="inserted"),
			EnumerationLiteral(name="deleted"),
			EnumerationLiteral(name="changed")
    }
)

ObjectName: Enumeration = Enumeration(
    name="ObjectName",
    literals={
            EnumerationLiteral(name="constructedElement"),
			EnumerationLiteral(name="footnote"),
			EnumerationLiteral(name="requirementRef"),
			EnumerationLiteral(name="externalSpecRef"),
			EnumerationLiteral(name="staticModelRef"),
			EnumerationLiteral(name="subjectAreaRef"),
			EnumerationLiteral(name="classRef"),
			EnumerationLiteral(name="stateRef"),
			EnumerationLiteral(name="transitionRef"),
			EnumerationLiteral(name="attributeRef"),
			EnumerationLiteral(name="associationEndRef"),
			EnumerationLiteral(name="triggerEventRef"),
			EnumerationLiteral(name="applicationRoleRef"),
			EnumerationLiteral(name="interactionRef"),
			EnumerationLiteral(name="vocabularyModelRef"),
			EnumerationLiteral(name="conceptDomainRef"),
			EnumerationLiteral(name="figureRef"),
			EnumerationLiteral(name="tableRef"),
			EnumerationLiteral(name="itemName"),
			EnumerationLiteral(name="annotationRef"),
			EnumerationLiteral(name="artifactGroupRef"),
			EnumerationLiteral(name="packageRef"),
			EnumerationLiteral(name="domainAnalysisModelRef"),
			EnumerationLiteral(name="domainInstanceExampleRef"),
			EnumerationLiteral(name="glossaryRef"),
			EnumerationLiteral(name="glossaryTermRef"),
			EnumerationLiteral(name="storyboardRef"),
			EnumerationLiteral(name="freehandDocumentRef"),
			EnumerationLiteral(name="publicationRef"),
			EnumerationLiteral(name="datatypeModelRef"),
			EnumerationLiteral(name="datatypeRef"),
			EnumerationLiteral(name="propertyRef"),
			EnumerationLiteral(name="vocabularyCodeSystemRef"),
			EnumerationLiteral(name="vocabularyCodeRef"),
			EnumerationLiteral(name="vocabularyValueSetRef"),
			EnumerationLiteral(name="testScenarioRef"),
			EnumerationLiteral(name="testCaseRef")
    }
)

ParamName: Enumeration = Enumeration(
    name="ParamName",
    literals={
            EnumerationLiteral(name="linkToEnd"),
			EnumerationLiteral(name="withinClassName"),
			EnumerationLiteral(name="relationshipName"),
			EnumerationLiteral(name="attributeName"),
			EnumerationLiteral(name="className"),
			EnumerationLiteral(name="supplierBindingArgumentDatatype"),
			EnumerationLiteral(name="datatypeName"),
			EnumerationLiteral(name="conversionDatatype"),
			EnumerationLiteral(name="propertyName"),
			EnumerationLiteral(name="termName"),
			EnumerationLiteral(name="stateName"),
			EnumerationLiteral(name="stateTransitionName"),
			EnumerationLiteral(name="subjectAreaName"),
			EnumerationLiteral(name="codeSystemId"),
			EnumerationLiteral(name="code"),
			EnumerationLiteral(name="constructType"),
			EnumerationLiteral(name="id"),
			EnumerationLiteral(name="item"),
			EnumerationLiteral(name="annotationKind"),
			EnumerationLiteral(name="root"),
			EnumerationLiteral(name="domain"),
			EnumerationLiteral(name="realmNamespace"),
			EnumerationLiteral(name="version"),
			EnumerationLiteral(name="artifact"),
			EnumerationLiteral(name="subArtifact"),
			EnumerationLiteral(name="name"),
			EnumerationLiteral(name="artifactName"),
			EnumerationLiteral(name="group")
    }
)

Shape: Enumeration = Enumeration(
    name="Shape",
    literals={
            EnumerationLiteral(name="rect"),
			EnumerationLiteral(name="circle"),
			EnumerationLiteral(name="poly"),
			EnumerationLiteral(name="default")
    }
)

StyleSheet: Enumeration = Enumeration(
    name="StyleSheet",
    literals={
            EnumerationLiteral(name="Requirement"),
			EnumerationLiteral(name="Indent"),
			EnumerationLiteral(name="Note"),
			EnumerationLiteral(name="NonNumbered"),
			EnumerationLiteral(name="BackgroundAqua"),
			EnumerationLiteral(name="BackgroundLime"),
			EnumerationLiteral(name="BackgroundPink"),
			EnumerationLiteral(name="BackgroundYellow")
    }
)

TFrame: Enumeration = Enumeration(
    name="TFrame",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="above"),
			EnumerationLiteral(name="below"),
			EnumerationLiteral(name="hsides"),
			EnumerationLiteral(name="lhs"),
			EnumerationLiteral(name="rhs"),
			EnumerationLiteral(name="vsides"),
			EnumerationLiteral(name="box"),
			EnumerationLiteral(name="border")
    }
)

TRules: Enumeration = Enumeration(
    name="TRules",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="groups"),
			EnumerationLiteral(name="rows"),
			EnumerationLiteral(name="cols"),
			EnumerationLiteral(name="all")
    }
)

ValignType: Enumeration = Enumeration(
    name="ValignType",
    literals={
            EnumerationLiteral(name="top"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="baseline")
    }
)

# Classes
xhtml_A = Class(name="xhtml::A")
AContent = Class(name="AContent")
xhtml_Abbr = Class(name="xhtml::Abbr")
Inline = Class(name="Inline")
xhtml_AContent = Class(name="xhtml::AContent")
xhtml_Br = Class(name="xhtml::Br")
xhtml_Span = Class(name="xhtml::Span")
xhtml_Img = Class(name="xhtml::Img")
xhtml_Tt = Class(name="xhtml::Tt")
xhtml_I = Class(name="xhtml::I")
xhtml_B = Class(name="xhtml::B")
xhtml_Big = Class(name="xhtml::Big")
xhtml_Small = Class(name="xhtml::Small")
xhtml_Object = Class(name="xhtml::Object")
xhtml_Em = Class(name="xhtml::Em")
xhtml_Strong = Class(name="xhtml::Strong")
xhtml_Dfn = Class(name="xhtml::Dfn")
xhtml_Code = Class(name="xhtml::Code")
xhtml_Q = Class(name="xhtml::Q")
xhtml_Samp = Class(name="xhtml::Samp")
xhtml_Kbd = Class(name="xhtml::Kbd")
xhtml_Var = Class(name="xhtml::Var")
xhtml_Cite = Class(name="xhtml::Cite")
xhtml_Acronym = Class(name="xhtml::Acronym")
xhtml_Sub = Class(name="xhtml::Sub")
xhtml_Sup = Class(name="xhtml::Sup")
xhtml_Block = Class(name="xhtml::Block")
xhtml_P = Class(name="xhtml::P")
xhtml_Div = Class(name="xhtml::Div")
xhtml_Ul = Class(name="xhtml::Ul")
xhtml_Dl = Class(name="xhtml::Dl")
xhtml_Pre = Class(name="xhtml::Pre")
xhtml_Hr = Class(name="xhtml::Hr")
xhtml_Blockquote = Class(name="xhtml::Blockquote")
xhtml_Table = Class(name="xhtml::Table")
Block = Class(name="Block")
xhtml_Ol = Class(name="xhtml::Ol")
xhtml_Caption = Class(name="xhtml::Caption")
xhtml_Col = Class(name="xhtml::Col")
xhtml_Colgroup = Class(name="xhtml::Colgroup")
xhtml_Dd = Class(name="xhtml::Dd")
xhtml_Del = Class(name="xhtml::Del")
Flow = Class(name="Flow")
xhtml_Dt = Class(name="xhtml::Dt")
xhtml_Flow = Class(name="xhtml::Flow")
xhtml_Inline = Class(name="xhtml::Inline")
xhtml_Ins = Class(name="xhtml::Ins")
xhtml_Li = Class(name="xhtml::Li")
xhtml_Param = Class(name="xhtml::Param")
PreContent = Class(name="PreContent")
xhtml_PreContent = Class(name="xhtml::PreContent")
xhtml_Tr = Class(name="xhtml::Tr")
xhtml_Thead = Class(name="xhtml::Thead")
xhtml_Tfoot = Class(name="xhtml::Tfoot")
xhtml_Tbody = Class(name="xhtml::Tbody")
xhtml_Td = Class(name="xhtml::Td")
xhtml_Th = Class(name="xhtml::Th")

# xhtml_A class attributes and methods
xhtml_A_class: Property = Property(name="class", type=StringType)
xhtml_A_coords: Property = Property(name="coords", type=StringType)
xhtml_A_href: Property = Property(name="href", type=StringType)
xhtml_A_lang: Property = Property(name="lang", type=StringType)
xhtml_A_name: Property = Property(name="name", type=StringType)
xhtml_A_shape: Property = Property(name="shape", type=StringType)
xhtml_A_style: Property = Property(name="style", type=StringType)
xhtml_A_type: Property = Property(name="type", type=StringType)
xhtml_A.attributes={xhtml_A_class, xhtml_A_href, xhtml_A_style, xhtml_A_type, xhtml_A_shape, xhtml_A_lang, xhtml_A_name, xhtml_A_coords}

# AContent class attributes and methods

# xhtml_Abbr class attributes and methods
xhtml_Abbr_class: Property = Property(name="class", type=StringType)
xhtml_Abbr_lang: Property = Property(name="lang", type=StringType)
xhtml_Abbr_style: Property = Property(name="style", type=StringType)
xhtml_Abbr.attributes={xhtml_Abbr_style, xhtml_Abbr_lang, xhtml_Abbr_class}

# Inline class attributes and methods

# xhtml_AContent class attributes and methods
xhtml_AContent_mixed: Property = Property(name="mixed", type=StringType)
xhtml_AContent_group: Property = Property(name="group", type=StringType)
xhtml_AContent.attributes={xhtml_AContent_mixed, xhtml_AContent_group}

# xhtml_Br class attributes and methods
xhtml_Br_class: Property = Property(name="class", type=StringType)
xhtml_Br_style: Property = Property(name="style", type=StringType)
xhtml_Br.attributes={xhtml_Br_class, xhtml_Br_style}

# xhtml_Span class attributes and methods
xhtml_Span_class: Property = Property(name="class", type=StringType)
xhtml_Span_lang: Property = Property(name="lang", type=StringType)
xhtml_Span_style: Property = Property(name="style", type=StringType)
xhtml_Span.attributes={xhtml_Span_style, xhtml_Span_class, xhtml_Span_lang}

# xhtml_Img class attributes and methods
xhtml_Img_lang: Property = Property(name="lang", type=StringType)
xhtml_Img_src: Property = Property(name="src", type=StringType)
xhtml_Img_style: Property = Property(name="style", type=StringType)
xhtml_Img_width: Property = Property(name="width", type=StringType)
xhtml_Img_alt: Property = Property(name="alt", type=StringType)
xhtml_Img_class: Property = Property(name="class", type=StringType)
xhtml_Img_height: Property = Property(name="height", type=StringType)
xhtml_Img_hl7Id: Property = Property(name="hl7Id", type=StringType)
xhtml_Img_imageType: Property = Property(name="imageType", type=StringType)
xhtml_Img.attributes={xhtml_Img_width, xhtml_Img_hl7Id, xhtml_Img_height, xhtml_Img_imageType, xhtml_Img_class, xhtml_Img_src, xhtml_Img_style, xhtml_Img_alt, xhtml_Img_lang}

# xhtml_Tt class attributes and methods
xhtml_Tt_class: Property = Property(name="class", type=StringType)
xhtml_Tt_lang: Property = Property(name="lang", type=StringType)
xhtml_Tt_style: Property = Property(name="style", type=StringType)
xhtml_Tt.attributes={xhtml_Tt_class, xhtml_Tt_style, xhtml_Tt_lang}

# xhtml_I class attributes and methods
xhtml_I_class: Property = Property(name="class", type=StringType)
xhtml_I_lang: Property = Property(name="lang", type=StringType)
xhtml_I_style: Property = Property(name="style", type=StringType)
xhtml_I.attributes={xhtml_I_lang, xhtml_I_style, xhtml_I_class}

# xhtml_B class attributes and methods
xhtml_B_class: Property = Property(name="class", type=StringType)
xhtml_B_lang: Property = Property(name="lang", type=StringType)
xhtml_B_style: Property = Property(name="style", type=StringType)
xhtml_B.attributes={xhtml_B_lang, xhtml_B_style, xhtml_B_class}

# xhtml_Big class attributes and methods
xhtml_Big_class: Property = Property(name="class", type=StringType)
xhtml_Big_lang: Property = Property(name="lang", type=StringType)
xhtml_Big_style: Property = Property(name="style", type=StringType)
xhtml_Big.attributes={xhtml_Big_lang, xhtml_Big_class, xhtml_Big_style}

# xhtml_Small class attributes and methods
xhtml_Small_class: Property = Property(name="class", type=StringType)
xhtml_Small_lang: Property = Property(name="lang", type=StringType)
xhtml_Small_style: Property = Property(name="style", type=StringType)
xhtml_Small.attributes={xhtml_Small_style, xhtml_Small_class, xhtml_Small_lang}

# xhtml_Object class attributes and methods
xhtml_Object_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Object_group: Property = Property(name="group", type=StringType)
xhtml_Object_hl7Id: Property = Property(name="hl7Id", type=StringType)
xhtml_Object_name: Property = Property(name="name", type=StringType)
xhtml_Object.attributes={xhtml_Object_hl7Id, xhtml_Object_mixed, xhtml_Object_name, xhtml_Object_group}

# xhtml_Em class attributes and methods
xhtml_Em_class: Property = Property(name="class", type=StringType)
xhtml_Em_lang: Property = Property(name="lang", type=StringType)
xhtml_Em_style: Property = Property(name="style", type=StringType)
xhtml_Em.attributes={xhtml_Em_style, xhtml_Em_lang, xhtml_Em_class}

# xhtml_Strong class attributes and methods
xhtml_Strong_lang: Property = Property(name="lang", type=StringType)
xhtml_Strong_style: Property = Property(name="style", type=StringType)
xhtml_Strong_class: Property = Property(name="class", type=StringType)
xhtml_Strong.attributes={xhtml_Strong_class, xhtml_Strong_style, xhtml_Strong_lang}

# xhtml_Dfn class attributes and methods
xhtml_Dfn_class: Property = Property(name="class", type=StringType)
xhtml_Dfn_lang: Property = Property(name="lang", type=StringType)
xhtml_Dfn_style: Property = Property(name="style", type=StringType)
xhtml_Dfn.attributes={xhtml_Dfn_class, xhtml_Dfn_lang, xhtml_Dfn_style}

# xhtml_Code class attributes and methods
xhtml_Code_class: Property = Property(name="class", type=StringType)
xhtml_Code_lang: Property = Property(name="lang", type=StringType)
xhtml_Code_style: Property = Property(name="style", type=StringType)
xhtml_Code.attributes={xhtml_Code_class, xhtml_Code_lang, xhtml_Code_style}

# xhtml_Q class attributes and methods
xhtml_Q_cite1: Property = Property(name="cite1", type=StringType)
xhtml_Q_class: Property = Property(name="class", type=StringType)
xhtml_Q_lang: Property = Property(name="lang", type=StringType)
xhtml_Q_style: Property = Property(name="style", type=StringType)
xhtml_Q.attributes={xhtml_Q_style, xhtml_Q_class, xhtml_Q_lang, xhtml_Q_cite1}

# xhtml_Samp class attributes and methods
xhtml_Samp_lang: Property = Property(name="lang", type=StringType)
xhtml_Samp_style: Property = Property(name="style", type=StringType)
xhtml_Samp_class: Property = Property(name="class", type=StringType)
xhtml_Samp.attributes={xhtml_Samp_class, xhtml_Samp_style, xhtml_Samp_lang}

# xhtml_Kbd class attributes and methods
xhtml_Kbd_class: Property = Property(name="class", type=StringType)
xhtml_Kbd_lang: Property = Property(name="lang", type=StringType)
xhtml_Kbd_style: Property = Property(name="style", type=StringType)
xhtml_Kbd.attributes={xhtml_Kbd_class, xhtml_Kbd_lang, xhtml_Kbd_style}

# xhtml_Var class attributes and methods
xhtml_Var_class: Property = Property(name="class", type=StringType)
xhtml_Var_lang: Property = Property(name="lang", type=StringType)
xhtml_Var_style: Property = Property(name="style", type=StringType)
xhtml_Var.attributes={xhtml_Var_lang, xhtml_Var_style, xhtml_Var_class}

# xhtml_Cite class attributes and methods
xhtml_Cite_class: Property = Property(name="class", type=StringType)
xhtml_Cite_style: Property = Property(name="style", type=StringType)
xhtml_Cite_lang: Property = Property(name="lang", type=StringType)
xhtml_Cite.attributes={xhtml_Cite_class, xhtml_Cite_lang, xhtml_Cite_style}

# xhtml_Acronym class attributes and methods
xhtml_Acronym_class: Property = Property(name="class", type=StringType)
xhtml_Acronym_lang: Property = Property(name="lang", type=StringType)
xhtml_Acronym_style: Property = Property(name="style", type=StringType)
xhtml_Acronym.attributes={xhtml_Acronym_lang, xhtml_Acronym_style, xhtml_Acronym_class}

# xhtml_Sub class attributes and methods
xhtml_Sub_class: Property = Property(name="class", type=StringType)
xhtml_Sub_lang: Property = Property(name="lang", type=StringType)
xhtml_Sub_style: Property = Property(name="style", type=StringType)
xhtml_Sub.attributes={xhtml_Sub_lang, xhtml_Sub_style, xhtml_Sub_class}

# xhtml_Sup class attributes and methods
xhtml_Sup_class: Property = Property(name="class", type=StringType)
xhtml_Sup_lang: Property = Property(name="lang", type=StringType)
xhtml_Sup_style: Property = Property(name="style", type=StringType)
xhtml_Sup.attributes={xhtml_Sup_style, xhtml_Sup_lang, xhtml_Sup_class}

# xhtml_Block class attributes and methods
xhtml_Block_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Block_block: Property = Property(name="block", type=StringType)
xhtml_Block.attributes={xhtml_Block_mixed, xhtml_Block_block}

# xhtml_P class attributes and methods
xhtml_P_class: Property = Property(name="class", type=StringType)
xhtml_P_lang: Property = Property(name="lang", type=StringType)
xhtml_P_style: Property = Property(name="style", type=StringType)
xhtml_P.attributes={xhtml_P_lang, xhtml_P_class, xhtml_P_style}

# xhtml_Div class attributes and methods
xhtml_Div_class: Property = Property(name="class", type=StringType)
xhtml_Div_hl7Id: Property = Property(name="hl7Id", type=StringType)
xhtml_Div_lang: Property = Property(name="lang", type=StringType)
xhtml_Div_title: Property = Property(name="title", type=StringType)
xhtml_Div_style: Property = Property(name="style", type=StringType)
xhtml_Div.attributes={xhtml_Div_title, xhtml_Div_lang, xhtml_Div_hl7Id, xhtml_Div_class, xhtml_Div_style}

# xhtml_Ul class attributes and methods
xhtml_Ul_lang: Property = Property(name="lang", type=StringType)
xhtml_Ul_style: Property = Property(name="style", type=StringType)
xhtml_Ul_li: Property = Property(name="li", type=StringType)
xhtml_Ul_class: Property = Property(name="class", type=StringType)
xhtml_Ul.attributes={xhtml_Ul_li, xhtml_Ul_lang, xhtml_Ul_style, xhtml_Ul_class}

# xhtml_Dl class attributes and methods
xhtml_Dl_group: Property = Property(name="group", type=StringType)
xhtml_Dl_class: Property = Property(name="class", type=StringType)
xhtml_Dl_lang: Property = Property(name="lang", type=StringType)
xhtml_Dl_style: Property = Property(name="style", type=StringType)
xhtml_Dl.attributes={xhtml_Dl_lang, xhtml_Dl_style, xhtml_Dl_class, xhtml_Dl_group}

# xhtml_Pre class attributes and methods
xhtml_Pre_class: Property = Property(name="class", type=StringType)
xhtml_Pre_lang: Property = Property(name="lang", type=StringType)
xhtml_Pre_space: Property = Property(name="space", type=StringType)
xhtml_Pre_style: Property = Property(name="style", type=StringType)
xhtml_Pre.attributes={xhtml_Pre_space, xhtml_Pre_style, xhtml_Pre_lang, xhtml_Pre_class}

# xhtml_Hr class attributes and methods
xhtml_Hr_class: Property = Property(name="class", type=StringType)
xhtml_Hr_lang: Property = Property(name="lang", type=StringType)
xhtml_Hr_style: Property = Property(name="style", type=StringType)
xhtml_Hr.attributes={xhtml_Hr_lang, xhtml_Hr_style, xhtml_Hr_class}

# xhtml_Blockquote class attributes and methods
xhtml_Blockquote_cite: Property = Property(name="cite", type=StringType)
xhtml_Blockquote_lang: Property = Property(name="lang", type=StringType)
xhtml_Blockquote_style: Property = Property(name="style", type=StringType)
xhtml_Blockquote_class: Property = Property(name="class", type=StringType)
xhtml_Blockquote.attributes={xhtml_Blockquote_class, xhtml_Blockquote_cite, xhtml_Blockquote_lang, xhtml_Blockquote_style}

# xhtml_Table class attributes and methods
xhtml_Table_border: Property = Property(name="border", type=StringType)
xhtml_Table_cellpadding: Property = Property(name="cellpadding", type=StringType)
xhtml_Table_cellspacing: Property = Property(name="cellspacing", type=StringType)
xhtml_Table_class: Property = Property(name="class", type=StringType)
xhtml_Table_frame: Property = Property(name="frame", type=StringType)
xhtml_Table_hl7Id: Property = Property(name="hl7Id", type=StringType)
xhtml_Table_lang: Property = Property(name="lang", type=StringType)
xhtml_Table_rules: Property = Property(name="rules", type=StringType)
xhtml_Table_style: Property = Property(name="style", type=StringType)
xhtml_Table_width: Property = Property(name="width", type=StringType)
xhtml_Table.attributes={xhtml_Table_border, xhtml_Table_style, xhtml_Table_hl7Id, xhtml_Table_rules, xhtml_Table_lang, xhtml_Table_cellspacing, xhtml_Table_frame, xhtml_Table_class, xhtml_Table_width, xhtml_Table_cellpadding}

# Block class attributes and methods

# xhtml_Ol class attributes and methods
xhtml_Ol_lang: Property = Property(name="lang", type=StringType)
xhtml_Ol_style: Property = Property(name="style", type=StringType)
xhtml_Ol_li: Property = Property(name="li", type=StringType)
xhtml_Ol_class: Property = Property(name="class", type=StringType)
xhtml_Ol.attributes={xhtml_Ol_class, xhtml_Ol_li, xhtml_Ol_style, xhtml_Ol_lang}

# xhtml_Caption class attributes and methods
xhtml_Caption_class: Property = Property(name="class", type=StringType)
xhtml_Caption_lang: Property = Property(name="lang", type=StringType)
xhtml_Caption_style: Property = Property(name="style", type=StringType)
xhtml_Caption.attributes={xhtml_Caption_style, xhtml_Caption_lang, xhtml_Caption_class}

# xhtml_Col class attributes and methods
xhtml_Col_align: Property = Property(name="align", type=StringType)
xhtml_Col_char: Property = Property(name="char", type=StringType)
xhtml_Col_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Col_class: Property = Property(name="class", type=StringType)
xhtml_Col_lang: Property = Property(name="lang", type=StringType)
xhtml_Col_span: Property = Property(name="span", type=StringType)
xhtml_Col_style: Property = Property(name="style", type=StringType)
xhtml_Col_valign: Property = Property(name="valign", type=StringType)
xhtml_Col_width: Property = Property(name="width", type=StringType)
xhtml_Col.attributes={xhtml_Col_span, xhtml_Col_char, xhtml_Col_align, xhtml_Col_width, xhtml_Col_lang, xhtml_Col_class, xhtml_Col_style, xhtml_Col_valign, xhtml_Col_charoff}

# xhtml_Colgroup class attributes and methods
xhtml_Colgroup_align: Property = Property(name="align", type=StringType)
xhtml_Colgroup_char: Property = Property(name="char", type=StringType)
xhtml_Colgroup_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Colgroup_class: Property = Property(name="class", type=StringType)
xhtml_Colgroup_lang: Property = Property(name="lang", type=StringType)
xhtml_Colgroup_span: Property = Property(name="span", type=StringType)
xhtml_Colgroup_style: Property = Property(name="style", type=StringType)
xhtml_Colgroup_valign: Property = Property(name="valign", type=StringType)
xhtml_Colgroup_width: Property = Property(name="width", type=StringType)
xhtml_Colgroup.attributes={xhtml_Colgroup_span, xhtml_Colgroup_char, xhtml_Colgroup_width, xhtml_Colgroup_valign, xhtml_Colgroup_lang, xhtml_Colgroup_class, xhtml_Colgroup_align, xhtml_Colgroup_charoff, xhtml_Colgroup_style}

# xhtml_Dd class attributes and methods
xhtml_Dd_lang: Property = Property(name="lang", type=StringType)
xhtml_Dd_style: Property = Property(name="style", type=StringType)
xhtml_Dd_class: Property = Property(name="class", type=StringType)
xhtml_Dd.attributes={xhtml_Dd_style, xhtml_Dd_lang, xhtml_Dd_class}

# xhtml_Del class attributes and methods

# Flow class attributes and methods

# xhtml_Dt class attributes and methods
xhtml_Dt_class: Property = Property(name="class", type=StringType)
xhtml_Dt_lang: Property = Property(name="lang", type=StringType)
xhtml_Dt_style: Property = Property(name="style", type=StringType)
xhtml_Dt.attributes={xhtml_Dt_style, xhtml_Dt_lang, xhtml_Dt_class}

# xhtml_Flow class attributes and methods
xhtml_Flow_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Flow_group: Property = Property(name="group", type=StringType)
xhtml_Flow.attributes={xhtml_Flow_mixed, xhtml_Flow_group}

# xhtml_Inline class attributes and methods
xhtml_Inline_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Inline_inline: Property = Property(name="inline", type=StringType)
xhtml_Inline.attributes={xhtml_Inline_inline, xhtml_Inline_mixed}

# xhtml_Ins class attributes and methods

# xhtml_Li class attributes and methods
xhtml_Li_class: Property = Property(name="class", type=StringType)
xhtml_Li_lang: Property = Property(name="lang", type=StringType)
xhtml_Li_style: Property = Property(name="style", type=StringType)
xhtml_Li.attributes={xhtml_Li_style, xhtml_Li_class, xhtml_Li_lang}

# xhtml_Param class attributes and methods
xhtml_Param_name: Property = Property(name="name", type=StringType)
xhtml_Param_value: Property = Property(name="value", type=StringType)
xhtml_Param.attributes={xhtml_Param_name, xhtml_Param_value}

# PreContent class attributes and methods

# xhtml_PreContent class attributes and methods
xhtml_PreContent_mixed: Property = Property(name="mixed", type=StringType)
xhtml_PreContent_group: Property = Property(name="group", type=StringType)
xhtml_PreContent.attributes={xhtml_PreContent_group, xhtml_PreContent_mixed}

# xhtml_Tr class attributes and methods
xhtml_Tr_group: Property = Property(name="group", type=StringType)
xhtml_Tr_valign: Property = Property(name="valign", type=StringType)
xhtml_Tr_align: Property = Property(name="align", type=StringType)
xhtml_Tr_char: Property = Property(name="char", type=StringType)
xhtml_Tr_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Tr_class: Property = Property(name="class", type=StringType)
xhtml_Tr_lang: Property = Property(name="lang", type=StringType)
xhtml_Tr_style: Property = Property(name="style", type=StringType)
xhtml_Tr.attributes={xhtml_Tr_align, xhtml_Tr_char, xhtml_Tr_charoff, xhtml_Tr_group, xhtml_Tr_lang, xhtml_Tr_valign, xhtml_Tr_class, xhtml_Tr_style}

# xhtml_Thead class attributes and methods
xhtml_Thead_style: Property = Property(name="style", type=StringType)
xhtml_Thead_valign: Property = Property(name="valign", type=StringType)
xhtml_Thead_align: Property = Property(name="align", type=StringType)
xhtml_Thead_char: Property = Property(name="char", type=StringType)
xhtml_Thead_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Thead_class: Property = Property(name="class", type=StringType)
xhtml_Thead_lang: Property = Property(name="lang", type=StringType)
xhtml_Thead.attributes={xhtml_Thead_lang, xhtml_Thead_valign, xhtml_Thead_charoff, xhtml_Thead_char, xhtml_Thead_class, xhtml_Thead_style, xhtml_Thead_align}

# xhtml_Tfoot class attributes and methods
xhtml_Tfoot_class: Property = Property(name="class", type=StringType)
xhtml_Tfoot_lang: Property = Property(name="lang", type=StringType)
xhtml_Tfoot_style: Property = Property(name="style", type=StringType)
xhtml_Tfoot_valign: Property = Property(name="valign", type=StringType)
xhtml_Tfoot_align: Property = Property(name="align", type=StringType)
xhtml_Tfoot_char: Property = Property(name="char", type=StringType)
xhtml_Tfoot_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Tfoot.attributes={xhtml_Tfoot_valign, xhtml_Tfoot_char, xhtml_Tfoot_class, xhtml_Tfoot_style, xhtml_Tfoot_charoff, xhtml_Tfoot_align, xhtml_Tfoot_lang}

# xhtml_Tbody class attributes and methods
xhtml_Tbody_align: Property = Property(name="align", type=StringType)
xhtml_Tbody_char: Property = Property(name="char", type=StringType)
xhtml_Tbody_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Tbody_class: Property = Property(name="class", type=StringType)
xhtml_Tbody_lang: Property = Property(name="lang", type=StringType)
xhtml_Tbody_style: Property = Property(name="style", type=StringType)
xhtml_Tbody_valign: Property = Property(name="valign", type=StringType)
xhtml_Tbody.attributes={xhtml_Tbody_charoff, xhtml_Tbody_char, xhtml_Tbody_style, xhtml_Tbody_class, xhtml_Tbody_align, xhtml_Tbody_lang, xhtml_Tbody_valign}

# xhtml_Td class attributes and methods
xhtml_Td_colspan: Property = Property(name="colspan", type=StringType)
xhtml_Td_lang: Property = Property(name="lang", type=StringType)
xhtml_Td_rowspan: Property = Property(name="rowspan", type=StringType)
xhtml_Td_style: Property = Property(name="style", type=StringType)
xhtml_Td_valign: Property = Property(name="valign", type=StringType)
xhtml_Td_align: Property = Property(name="align", type=StringType)
xhtml_Td_char: Property = Property(name="char", type=StringType)
xhtml_Td_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Td_class: Property = Property(name="class", type=StringType)
xhtml_Td.attributes={xhtml_Td_charoff, xhtml_Td_style, xhtml_Td_rowspan, xhtml_Td_align, xhtml_Td_class, xhtml_Td_colspan, xhtml_Td_valign, xhtml_Td_lang, xhtml_Td_char}

# xhtml_Th class attributes and methods
xhtml_Th_colspan: Property = Property(name="colspan", type=StringType)
xhtml_Th_lang: Property = Property(name="lang", type=StringType)
xhtml_Th_rowspan: Property = Property(name="rowspan", type=StringType)
xhtml_Th_style: Property = Property(name="style", type=StringType)
xhtml_Th_valign: Property = Property(name="valign", type=StringType)
xhtml_Th_align: Property = Property(name="align", type=StringType)
xhtml_Th_char: Property = Property(name="char", type=StringType)
xhtml_Th_charoff: Property = Property(name="charoff", type=StringType)
xhtml_Th_class: Property = Property(name="class", type=StringType)
xhtml_Th.attributes={xhtml_Th_align, xhtml_Th_charoff, xhtml_Th_class, xhtml_Th_colspan, xhtml_Th_lang, xhtml_Th_valign, xhtml_Th_char, xhtml_Th_rowspan, xhtml_Th_style}

# Relationships
br0: BinaryAssociation = BinaryAssociation(
    name="br0",
    ends={
        Property(name="xhtml_Br", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent", type=xhtml_Br, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span1: BinaryAssociation = BinaryAssociation(
    name="span1",
    ends={
        Property(name="xhtml_Span", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent2", type=xhtml_Span, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img5: BinaryAssociation = BinaryAssociation(
    name="img5",
    ends={
        Property(name="xhtml_Img", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent6", type=xhtml_Img, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt7: BinaryAssociation = BinaryAssociation(
    name="tt7",
    ends={
        Property(name="xhtml_Tt", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent8", type=xhtml_Tt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i9: BinaryAssociation = BinaryAssociation(
    name="i9",
    ends={
        Property(name="xhtml_I", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent10", type=xhtml_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b11: BinaryAssociation = BinaryAssociation(
    name="b11",
    ends={
        Property(name="xhtml_B", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent12", type=xhtml_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big13: BinaryAssociation = BinaryAssociation(
    name="big13",
    ends={
        Property(name="xhtml_Big", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent14", type=xhtml_Big, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small15: BinaryAssociation = BinaryAssociation(
    name="small15",
    ends={
        Property(name="xhtml_Small", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent16", type=xhtml_Small, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object3: BinaryAssociation = BinaryAssociation(
    name="object3",
    ends={
        Property(name="xhtml_Object", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent4", type=xhtml_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em17: BinaryAssociation = BinaryAssociation(
    name="em17",
    ends={
        Property(name="xhtml_Em", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent18", type=xhtml_Em, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong19: BinaryAssociation = BinaryAssociation(
    name="strong19",
    ends={
        Property(name="xhtml_Strong", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent20", type=xhtml_Strong, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn21: BinaryAssociation = BinaryAssociation(
    name="dfn21",
    ends={
        Property(name="xhtml_Dfn", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent22", type=xhtml_Dfn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code23: BinaryAssociation = BinaryAssociation(
    name="code23",
    ends={
        Property(name="xhtml_Code", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent24", type=xhtml_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q25: BinaryAssociation = BinaryAssociation(
    name="q25",
    ends={
        Property(name="xhtml_Q", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent26", type=xhtml_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp27: BinaryAssociation = BinaryAssociation(
    name="samp27",
    ends={
        Property(name="xhtml_Samp", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent28", type=xhtml_Samp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd29: BinaryAssociation = BinaryAssociation(
    name="kbd29",
    ends={
        Property(name="xhtml_Kbd", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent30", type=xhtml_Kbd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var31: BinaryAssociation = BinaryAssociation(
    name="var31",
    ends={
        Property(name="xhtml_Var", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent32", type=xhtml_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite33: BinaryAssociation = BinaryAssociation(
    name="cite33",
    ends={
        Property(name="xhtml_Cite", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent34", type=xhtml_Cite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr35: BinaryAssociation = BinaryAssociation(
    name="abbr35",
    ends={
        Property(name="xhtml_Abbr", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent36", type=xhtml_Abbr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym37: BinaryAssociation = BinaryAssociation(
    name="acronym37",
    ends={
        Property(name="xhtml_Acronym", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent38", type=xhtml_Acronym, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub39: BinaryAssociation = BinaryAssociation(
    name="sub39",
    ends={
        Property(name="xhtml_Sub", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent40", type=xhtml_Sub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup41: BinaryAssociation = BinaryAssociation(
    name="sup41",
    ends={
        Property(name="xhtml_Sup", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent42", type=xhtml_Sup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p43: BinaryAssociation = BinaryAssociation(
    name="p43",
    ends={
        Property(name="xhtml_P", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block", type=xhtml_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div44: BinaryAssociation = BinaryAssociation(
    name="div44",
    ends={
        Property(name="xhtml_Div", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block45", type=xhtml_Div, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul46: BinaryAssociation = BinaryAssociation(
    name="ul46",
    ends={
        Property(name="xhtml_Ul", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block47", type=xhtml_Ul, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol48: BinaryAssociation = BinaryAssociation(
    name="ol48",
    ends={
        Property(name="xhtml_Block49", type=xhtml_Ol, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xhtml_Ol", type=xhtml_Block, multiplicity=Multiplicity(1, 1))
    }
)
dl50: BinaryAssociation = BinaryAssociation(
    name="dl50",
    ends={
        Property(name="xhtml_Dl", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block51", type=xhtml_Dl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre52: BinaryAssociation = BinaryAssociation(
    name="pre52",
    ends={
        Property(name="xhtml_Pre", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block53", type=xhtml_Pre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr54: BinaryAssociation = BinaryAssociation(
    name="hr54",
    ends={
        Property(name="xhtml_Hr", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block55", type=xhtml_Hr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote56: BinaryAssociation = BinaryAssociation(
    name="blockquote56",
    ends={
        Property(name="xhtml_Blockquote", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block57", type=xhtml_Blockquote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table58: BinaryAssociation = BinaryAssociation(
    name="table58",
    ends={
        Property(name="xhtml_Table", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block59", type=xhtml_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col60: BinaryAssociation = BinaryAssociation(
    name="col60",
    ends={
        Property(name="xhtml_Col", type=xhtml_Colgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Colgroup", type=xhtml_Col, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dt61: BinaryAssociation = BinaryAssociation(
    name="dt61",
    ends={
        Property(name="xhtml_Dt", type=xhtml_Dl, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Dl62", type=xhtml_Dt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dd63: BinaryAssociation = BinaryAssociation(
    name="dd63",
    ends={
        Property(name="xhtml_Dd", type=xhtml_Dl, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Dl64", type=xhtml_Dd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p65: BinaryAssociation = BinaryAssociation(
    name="p65",
    ends={
        Property(name="xhtml_P66", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow", type=xhtml_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div67: BinaryAssociation = BinaryAssociation(
    name="div67",
    ends={
        Property(name="xhtml_Div69", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow68", type=xhtml_Div, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul70: BinaryAssociation = BinaryAssociation(
    name="ul70",
    ends={
        Property(name="xhtml_Ul72", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow71", type=xhtml_Ul, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol73: BinaryAssociation = BinaryAssociation(
    name="ol73",
    ends={
        Property(name="xhtml_Ol75", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow74", type=xhtml_Ol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl76: BinaryAssociation = BinaryAssociation(
    name="dl76",
    ends={
        Property(name="xhtml_Dl78", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow77", type=xhtml_Dl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre79: BinaryAssociation = BinaryAssociation(
    name="pre79",
    ends={
        Property(name="xhtml_Pre81", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow80", type=xhtml_Pre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr82: BinaryAssociation = BinaryAssociation(
    name="hr82",
    ends={
        Property(name="xhtml_Hr84", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow83", type=xhtml_Hr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote85: BinaryAssociation = BinaryAssociation(
    name="blockquote85",
    ends={
        Property(name="xhtml_Blockquote87", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow86", type=xhtml_Blockquote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a91: BinaryAssociation = BinaryAssociation(
    name="a91",
    ends={
        Property(name="xhtml_A", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow92", type=xhtml_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br93: BinaryAssociation = BinaryAssociation(
    name="br93",
    ends={
        Property(name="xhtml_Br95", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow94", type=xhtml_Br, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span96: BinaryAssociation = BinaryAssociation(
    name="span96",
    ends={
        Property(name="xhtml_Span98", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow97", type=xhtml_Span, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object99: BinaryAssociation = BinaryAssociation(
    name="object99",
    ends={
        Property(name="xhtml_Object101", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow100", type=xhtml_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img102: BinaryAssociation = BinaryAssociation(
    name="img102",
    ends={
        Property(name="xhtml_Img104", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow103", type=xhtml_Img, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt105: BinaryAssociation = BinaryAssociation(
    name="tt105",
    ends={
        Property(name="xhtml_Tt107", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow106", type=xhtml_Tt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table88: BinaryAssociation = BinaryAssociation(
    name="table88",
    ends={
        Property(name="xhtml_Table90", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow89", type=xhtml_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b111: BinaryAssociation = BinaryAssociation(
    name="b111",
    ends={
        Property(name="xhtml_B113", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow112", type=xhtml_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big114: BinaryAssociation = BinaryAssociation(
    name="big114",
    ends={
        Property(name="xhtml_Big116", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow115", type=xhtml_Big, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small117: BinaryAssociation = BinaryAssociation(
    name="small117",
    ends={
        Property(name="xhtml_Small119", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow118", type=xhtml_Small, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q132: BinaryAssociation = BinaryAssociation(
    name="q132",
    ends={
        Property(name="xhtml_Q134", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow133", type=xhtml_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp135: BinaryAssociation = BinaryAssociation(
    name="samp135",
    ends={
        Property(name="xhtml_Samp137", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow136", type=xhtml_Samp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd138: BinaryAssociation = BinaryAssociation(
    name="kbd138",
    ends={
        Property(name="xhtml_Kbd140", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow139", type=xhtml_Kbd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i108: BinaryAssociation = BinaryAssociation(
    name="i108",
    ends={
        Property(name="xhtml_I110", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow109", type=xhtml_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em120: BinaryAssociation = BinaryAssociation(
    name="em120",
    ends={
        Property(name="xhtml_Em122", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow121", type=xhtml_Em, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong123: BinaryAssociation = BinaryAssociation(
    name="strong123",
    ends={
        Property(name="xhtml_Strong125", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow124", type=xhtml_Strong, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn126: BinaryAssociation = BinaryAssociation(
    name="dfn126",
    ends={
        Property(name="xhtml_Dfn128", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow127", type=xhtml_Dfn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code129: BinaryAssociation = BinaryAssociation(
    name="code129",
    ends={
        Property(name="xhtml_Code131", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow130", type=xhtml_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub153: BinaryAssociation = BinaryAssociation(
    name="sub153",
    ends={
        Property(name="xhtml_Sub155", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow154", type=xhtml_Sub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup156: BinaryAssociation = BinaryAssociation(
    name="sup156",
    ends={
        Property(name="xhtml_Sup158", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow157", type=xhtml_Sup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var141: BinaryAssociation = BinaryAssociation(
    name="var141",
    ends={
        Property(name="xhtml_Var143", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow142", type=xhtml_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite144: BinaryAssociation = BinaryAssociation(
    name="cite144",
    ends={
        Property(name="xhtml_Cite146", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow145", type=xhtml_Cite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr147: BinaryAssociation = BinaryAssociation(
    name="abbr147",
    ends={
        Property(name="xhtml_Abbr149", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow148", type=xhtml_Abbr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym150: BinaryAssociation = BinaryAssociation(
    name="acronym150",
    ends={
        Property(name="xhtml_Acronym152", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow151", type=xhtml_Acronym, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thumbnail160: BinaryAssociation = BinaryAssociation(
    name="thumbnail160",
    ends={
        Property(name="xhtml_Img161", type=xhtml_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Img159", type=xhtml_Img, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
img173: BinaryAssociation = BinaryAssociation(
    name="img173",
    ends={
        Property(name="xhtml_Img175", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline174", type=xhtml_Img, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt176: BinaryAssociation = BinaryAssociation(
    name="tt176",
    ends={
        Property(name="xhtml_Tt178", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline177", type=xhtml_Tt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i179: BinaryAssociation = BinaryAssociation(
    name="i179",
    ends={
        Property(name="xhtml_I181", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline180", type=xhtml_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a162: BinaryAssociation = BinaryAssociation(
    name="a162",
    ends={
        Property(name="xhtml_A163", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline", type=xhtml_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br164: BinaryAssociation = BinaryAssociation(
    name="br164",
    ends={
        Property(name="xhtml_Br166", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline165", type=xhtml_Br, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span167: BinaryAssociation = BinaryAssociation(
    name="span167",
    ends={
        Property(name="xhtml_Span169", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline168", type=xhtml_Span, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object170: BinaryAssociation = BinaryAssociation(
    name="object170",
    ends={
        Property(name="xhtml_Object172", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline171", type=xhtml_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn197: BinaryAssociation = BinaryAssociation(
    name="dfn197",
    ends={
        Property(name="xhtml_Dfn199", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline198", type=xhtml_Dfn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code200: BinaryAssociation = BinaryAssociation(
    name="code200",
    ends={
        Property(name="xhtml_Code202", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline201", type=xhtml_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q203: BinaryAssociation = BinaryAssociation(
    name="q203",
    ends={
        Property(name="xhtml_Q205", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline204", type=xhtml_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b182: BinaryAssociation = BinaryAssociation(
    name="b182",
    ends={
        Property(name="xhtml_B184", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline183", type=xhtml_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big185: BinaryAssociation = BinaryAssociation(
    name="big185",
    ends={
        Property(name="xhtml_Big187", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline186", type=xhtml_Big, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small188: BinaryAssociation = BinaryAssociation(
    name="small188",
    ends={
        Property(name="xhtml_Small190", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline189", type=xhtml_Small, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em191: BinaryAssociation = BinaryAssociation(
    name="em191",
    ends={
        Property(name="xhtml_Em193", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline192", type=xhtml_Em, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong194: BinaryAssociation = BinaryAssociation(
    name="strong194",
    ends={
        Property(name="xhtml_Strong196", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline195", type=xhtml_Strong, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr218: BinaryAssociation = BinaryAssociation(
    name="abbr218",
    ends={
        Property(name="xhtml_Abbr220", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline219", type=xhtml_Abbr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym221: BinaryAssociation = BinaryAssociation(
    name="acronym221",
    ends={
        Property(name="xhtml_Acronym223", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline222", type=xhtml_Acronym, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub224: BinaryAssociation = BinaryAssociation(
    name="sub224",
    ends={
        Property(name="xhtml_Sub226", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline225", type=xhtml_Sub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp206: BinaryAssociation = BinaryAssociation(
    name="samp206",
    ends={
        Property(name="xhtml_Samp208", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline207", type=xhtml_Samp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd209: BinaryAssociation = BinaryAssociation(
    name="kbd209",
    ends={
        Property(name="xhtml_Kbd211", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline210", type=xhtml_Kbd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var212: BinaryAssociation = BinaryAssociation(
    name="var212",
    ends={
        Property(name="xhtml_Var214", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline213", type=xhtml_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite215: BinaryAssociation = BinaryAssociation(
    name="cite215",
    ends={
        Property(name="xhtml_Cite217", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline216", type=xhtml_Cite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup227: BinaryAssociation = BinaryAssociation(
    name="sup227",
    ends={
        Property(name="xhtml_Sup229", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline228", type=xhtml_Sup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param230: BinaryAssociation = BinaryAssociation(
    name="param230",
    ends={
        Property(name="xhtml_Param", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object231", type=xhtml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre247: BinaryAssociation = BinaryAssociation(
    name="pre247",
    ends={
        Property(name="xhtml_Pre249", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object248", type=xhtml_Pre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr250: BinaryAssociation = BinaryAssociation(
    name="hr250",
    ends={
        Property(name="xhtml_Hr252", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object251", type=xhtml_Hr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote253: BinaryAssociation = BinaryAssociation(
    name="blockquote253",
    ends={
        Property(name="xhtml_Blockquote255", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object254", type=xhtml_Blockquote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p232: BinaryAssociation = BinaryAssociation(
    name="p232",
    ends={
        Property(name="xhtml_P234", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object233", type=xhtml_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div235: BinaryAssociation = BinaryAssociation(
    name="div235",
    ends={
        Property(name="xhtml_Div237", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object236", type=xhtml_Div, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul238: BinaryAssociation = BinaryAssociation(
    name="ul238",
    ends={
        Property(name="xhtml_Ul240", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object239", type=xhtml_Ul, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol241: BinaryAssociation = BinaryAssociation(
    name="ol241",
    ends={
        Property(name="xhtml_Ol243", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object242", type=xhtml_Ol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl244: BinaryAssociation = BinaryAssociation(
    name="dl244",
    ends={
        Property(name="xhtml_Dl246", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object245", type=xhtml_Dl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object269: BinaryAssociation = BinaryAssociation(
    name="object269",
    ends={
        Property(name="xhtml_Object270", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object268", type=xhtml_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img271: BinaryAssociation = BinaryAssociation(
    name="img271",
    ends={
        Property(name="xhtml_Img273", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object272", type=xhtml_Img, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt274: BinaryAssociation = BinaryAssociation(
    name="tt274",
    ends={
        Property(name="xhtml_Tt276", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object275", type=xhtml_Tt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table256: BinaryAssociation = BinaryAssociation(
    name="table256",
    ends={
        Property(name="xhtml_Table258", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object257", type=xhtml_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a259: BinaryAssociation = BinaryAssociation(
    name="a259",
    ends={
        Property(name="xhtml_A261", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object260", type=xhtml_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br262: BinaryAssociation = BinaryAssociation(
    name="br262",
    ends={
        Property(name="xhtml_Br264", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object263", type=xhtml_Br, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span265: BinaryAssociation = BinaryAssociation(
    name="span265",
    ends={
        Property(name="xhtml_Span267", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object266", type=xhtml_Span, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small286: BinaryAssociation = BinaryAssociation(
    name="small286",
    ends={
        Property(name="xhtml_Small288", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object287", type=xhtml_Small, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em289: BinaryAssociation = BinaryAssociation(
    name="em289",
    ends={
        Property(name="xhtml_Em291", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object290", type=xhtml_Em, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong292: BinaryAssociation = BinaryAssociation(
    name="strong292",
    ends={
        Property(name="xhtml_Strong294", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object293", type=xhtml_Strong, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i277: BinaryAssociation = BinaryAssociation(
    name="i277",
    ends={
        Property(name="xhtml_I279", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object278", type=xhtml_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b280: BinaryAssociation = BinaryAssociation(
    name="b280",
    ends={
        Property(name="xhtml_B282", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object281", type=xhtml_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big283: BinaryAssociation = BinaryAssociation(
    name="big283",
    ends={
        Property(name="xhtml_Big285", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object284", type=xhtml_Big, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp304: BinaryAssociation = BinaryAssociation(
    name="samp304",
    ends={
        Property(name="xhtml_Samp306", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object305", type=xhtml_Samp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd307: BinaryAssociation = BinaryAssociation(
    name="kbd307",
    ends={
        Property(name="xhtml_Kbd309", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object308", type=xhtml_Kbd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var310: BinaryAssociation = BinaryAssociation(
    name="var310",
    ends={
        Property(name="xhtml_Var312", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object311", type=xhtml_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn295: BinaryAssociation = BinaryAssociation(
    name="dfn295",
    ends={
        Property(name="xhtml_Dfn297", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object296", type=xhtml_Dfn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code298: BinaryAssociation = BinaryAssociation(
    name="code298",
    ends={
        Property(name="xhtml_Code300", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object299", type=xhtml_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q301: BinaryAssociation = BinaryAssociation(
    name="q301",
    ends={
        Property(name="xhtml_Q303", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object302", type=xhtml_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite313: BinaryAssociation = BinaryAssociation(
    name="cite313",
    ends={
        Property(name="xhtml_Cite315", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object314", type=xhtml_Cite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr316: BinaryAssociation = BinaryAssociation(
    name="abbr316",
    ends={
        Property(name="xhtml_Abbr318", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object317", type=xhtml_Abbr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym319: BinaryAssociation = BinaryAssociation(
    name="acronym319",
    ends={
        Property(name="xhtml_Acronym321", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object320", type=xhtml_Acronym, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub322: BinaryAssociation = BinaryAssociation(
    name="sub322",
    ends={
        Property(name="xhtml_Sub324", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object323", type=xhtml_Sub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup325: BinaryAssociation = BinaryAssociation(
    name="sup325",
    ends={
        Property(name="xhtml_Sup327", type=xhtml_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Object326", type=xhtml_Sup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li1328: BinaryAssociation = BinaryAssociation(
    name="li1328",
    ends={
        Property(name="xhtml_Li", type=xhtml_Ol, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Ol329", type=xhtml_Li, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
a330: BinaryAssociation = BinaryAssociation(
    name="a330",
    ends={
        Property(name="xhtml_A331", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent", type=xhtml_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt332: BinaryAssociation = BinaryAssociation(
    name="tt332",
    ends={
        Property(name="xhtml_Tt334", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent333", type=xhtml_Tt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em347: BinaryAssociation = BinaryAssociation(
    name="em347",
    ends={
        Property(name="xhtml_Em349", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent348", type=xhtml_Em, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong350: BinaryAssociation = BinaryAssociation(
    name="strong350",
    ends={
        Property(name="xhtml_Strong352", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent351", type=xhtml_Strong, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn353: BinaryAssociation = BinaryAssociation(
    name="dfn353",
    ends={
        Property(name="xhtml_Dfn355", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent354", type=xhtml_Dfn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i335: BinaryAssociation = BinaryAssociation(
    name="i335",
    ends={
        Property(name="xhtml_I337", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent336", type=xhtml_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b338: BinaryAssociation = BinaryAssociation(
    name="b338",
    ends={
        Property(name="xhtml_B340", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent339", type=xhtml_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big341: BinaryAssociation = BinaryAssociation(
    name="big341",
    ends={
        Property(name="xhtml_Big343", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent342", type=xhtml_Big, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small344: BinaryAssociation = BinaryAssociation(
    name="small344",
    ends={
        Property(name="xhtml_Small346", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent345", type=xhtml_Small, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var368: BinaryAssociation = BinaryAssociation(
    name="var368",
    ends={
        Property(name="xhtml_Var370", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent369", type=xhtml_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite371: BinaryAssociation = BinaryAssociation(
    name="cite371",
    ends={
        Property(name="xhtml_Cite373", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent372", type=xhtml_Cite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr374: BinaryAssociation = BinaryAssociation(
    name="abbr374",
    ends={
        Property(name="xhtml_Abbr376", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent375", type=xhtml_Abbr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code356: BinaryAssociation = BinaryAssociation(
    name="code356",
    ends={
        Property(name="xhtml_Code358", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent357", type=xhtml_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q359: BinaryAssociation = BinaryAssociation(
    name="q359",
    ends={
        Property(name="xhtml_Q361", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent360", type=xhtml_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp362: BinaryAssociation = BinaryAssociation(
    name="samp362",
    ends={
        Property(name="xhtml_Samp364", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent363", type=xhtml_Samp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd365: BinaryAssociation = BinaryAssociation(
    name="kbd365",
    ends={
        Property(name="xhtml_Kbd367", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent366", type=xhtml_Kbd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup383: BinaryAssociation = BinaryAssociation(
    name="sup383",
    ends={
        Property(name="xhtml_Sup385", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent384", type=xhtml_Sup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br386: BinaryAssociation = BinaryAssociation(
    name="br386",
    ends={
        Property(name="xhtml_Br388", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent387", type=xhtml_Br, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span389: BinaryAssociation = BinaryAssociation(
    name="span389",
    ends={
        Property(name="xhtml_Span391", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent390", type=xhtml_Span, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym377: BinaryAssociation = BinaryAssociation(
    name="acronym377",
    ends={
        Property(name="xhtml_Acronym379", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent378", type=xhtml_Acronym, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub380: BinaryAssociation = BinaryAssociation(
    name="sub380",
    ends={
        Property(name="xhtml_Sub382", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent381", type=xhtml_Sub, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caption392: BinaryAssociation = BinaryAssociation(
    name="caption392",
    ends={
        Property(name="xhtml_Caption", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table393", type=xhtml_Caption, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tr406: BinaryAssociation = BinaryAssociation(
    name="tr406",
    ends={
        Property(name="xhtml_Tr", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table407", type=xhtml_Tr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col394: BinaryAssociation = BinaryAssociation(
    name="col394",
    ends={
        Property(name="xhtml_Col396", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table395", type=xhtml_Col, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colgroup397: BinaryAssociation = BinaryAssociation(
    name="colgroup397",
    ends={
        Property(name="xhtml_Colgroup399", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table398", type=xhtml_Colgroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead400: BinaryAssociation = BinaryAssociation(
    name="thead400",
    ends={
        Property(name="xhtml_Thead", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table401", type=xhtml_Thead, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tfoot402: BinaryAssociation = BinaryAssociation(
    name="tfoot402",
    ends={
        Property(name="xhtml_Tfoot", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table403", type=xhtml_Tfoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbody404: BinaryAssociation = BinaryAssociation(
    name="tbody404",
    ends={
        Property(name="xhtml_Tbody", type=xhtml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Table405", type=xhtml_Tbody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr408: BinaryAssociation = BinaryAssociation(
    name="tr408",
    ends={
        Property(name="xhtml_Tr410", type=xhtml_Tbody, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Tbody409", type=xhtml_Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr411: BinaryAssociation = BinaryAssociation(
    name="tr411",
    ends={
        Property(name="xhtml_Tr413", type=xhtml_Tfoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Tfoot412", type=xhtml_Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
th417: BinaryAssociation = BinaryAssociation(
    name="th417",
    ends={
        Property(name="xhtml_Th", type=xhtml_Tr, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Tr418", type=xhtml_Th, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr414: BinaryAssociation = BinaryAssociation(
    name="tr414",
    ends={
        Property(name="xhtml_Tr416", type=xhtml_Thead, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Thead415", type=xhtml_Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
td419: BinaryAssociation = BinaryAssociation(
    name="td419",
    ends={
        Property(name="xhtml_Td", type=xhtml_Tr, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Tr420", type=xhtml_Td, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li1421: BinaryAssociation = BinaryAssociation(
    name="li1421",
    ends={
        Property(name="xhtml_Li423", type=xhtml_Ul, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Ul422", type=xhtml_Li, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_xhtml_A_AContent = Generalization(general=AContent, specific=xhtml_A)
gen_xhtml_Abbr_Inline = Generalization(general=Inline, specific=xhtml_Abbr)
gen_xhtml_Acronym_Inline = Generalization(general=Inline, specific=xhtml_Acronym)
gen_xhtml_B_Inline = Generalization(general=Inline, specific=xhtml_B)
gen_xhtml_Big_Inline = Generalization(general=Inline, specific=xhtml_Big)
gen_xhtml_Blockquote_Block = Generalization(general=Block, specific=xhtml_Blockquote)
gen_xhtml_Caption_Inline = Generalization(general=Inline, specific=xhtml_Caption)
gen_xhtml_Cite_Inline = Generalization(general=Inline, specific=xhtml_Cite)
gen_xhtml_Code_Inline = Generalization(general=Inline, specific=xhtml_Code)
gen_xhtml_Del_Flow = Generalization(general=Flow, specific=xhtml_Del)
gen_xhtml_Dfn_Inline = Generalization(general=Inline, specific=xhtml_Dfn)
gen_xhtml_Div_Flow = Generalization(general=Flow, specific=xhtml_Div)
gen_xhtml_Dd_Flow = Generalization(general=Flow, specific=xhtml_Dd)
gen_xhtml_Dt_Inline = Generalization(general=Inline, specific=xhtml_Dt)
gen_xhtml_Em_Inline = Generalization(general=Inline, specific=xhtml_Em)
gen_xhtml_I_Inline = Generalization(general=Inline, specific=xhtml_I)
gen_xhtml_Li_Flow = Generalization(general=Flow, specific=xhtml_Li)
gen_xhtml_Ins_Flow = Generalization(general=Flow, specific=xhtml_Ins)
gen_xhtml_Kbd_Inline = Generalization(general=Inline, specific=xhtml_Kbd)
gen_xhtml_P_Inline = Generalization(general=Inline, specific=xhtml_P)
gen_xhtml_Pre_PreContent = Generalization(general=PreContent, specific=xhtml_Pre)
gen_xhtml_Small_Inline = Generalization(general=Inline, specific=xhtml_Small)
gen_xhtml_Q_Inline = Generalization(general=Inline, specific=xhtml_Q)
gen_xhtml_Samp_Inline = Generalization(general=Inline, specific=xhtml_Samp)
gen_xhtml_Span_Inline = Generalization(general=Inline, specific=xhtml_Span)
gen_xhtml_Strong_Inline = Generalization(general=Inline, specific=xhtml_Strong)
gen_xhtml_Sub_Inline = Generalization(general=Inline, specific=xhtml_Sub)
gen_xhtml_Sup_Inline = Generalization(general=Inline, specific=xhtml_Sup)
gen_xhtml_Td_Flow = Generalization(general=Flow, specific=xhtml_Td)
gen_xhtml_Th_Flow = Generalization(general=Flow, specific=xhtml_Th)
gen_xhtml_Tt_Inline = Generalization(general=Inline, specific=xhtml_Tt)
gen_xhtml_Var_Inline = Generalization(general=Inline, specific=xhtml_Var)

# Domain Model
domain_model = DomainModel(
    name="xhtml",
    types={xhtml_A, AContent, xhtml_Abbr, Inline, xhtml_AContent, xhtml_Br, xhtml_Span, xhtml_Img, xhtml_Tt, xhtml_I, xhtml_B, xhtml_Big, xhtml_Small, xhtml_Object, xhtml_Em, xhtml_Strong, xhtml_Dfn, xhtml_Code, xhtml_Q, xhtml_Samp, xhtml_Kbd, xhtml_Var, xhtml_Cite, xhtml_Acronym, xhtml_Sub, xhtml_Sup, xhtml_Block, xhtml_P, xhtml_Div, xhtml_Ul, xhtml_Dl, xhtml_Pre, xhtml_Hr, xhtml_Blockquote, xhtml_Table, Block, xhtml_Ol, xhtml_Caption, xhtml_Col, xhtml_Colgroup, xhtml_Dd, xhtml_Del, Flow, xhtml_Dt, xhtml_Flow, xhtml_Inline, xhtml_Ins, xhtml_Li, xhtml_Param, PreContent, xhtml_PreContent, xhtml_Tr, xhtml_Thead, xhtml_Tfoot, xhtml_Tbody, xhtml_Td, xhtml_Th, AlignType, ImageKind, MediaType, MifClassType, ObjectName, ParamName, Shape, StyleSheet, TFrame, TRules, ValignType},
    associations={br0, span1, img5, tt7, i9, b11, big13, small15, object3, em17, strong19, dfn21, code23, q25, samp27, kbd29, var31, cite33, abbr35, acronym37, sub39, sup41, p43, div44, ul46, ol48, dl50, pre52, hr54, blockquote56, table58, col60, dt61, dd63, p65, div67, ul70, ol73, dl76, pre79, hr82, blockquote85, a91, br93, span96, object99, img102, tt105, table88, b111, big114, small117, q132, samp135, kbd138, i108, em120, strong123, dfn126, code129, sub153, sup156, var141, cite144, abbr147, acronym150, thumbnail160, img173, tt176, i179, a162, br164, span167, object170, dfn197, code200, q203, b182, big185, small188, em191, strong194, abbr218, acronym221, sub224, samp206, kbd209, var212, cite215, sup227, param230, pre247, hr250, blockquote253, p232, div235, ul238, ol241, dl244, object269, img271, tt274, table256, a259, br262, span265, small286, em289, strong292, i277, b280, big283, samp304, kbd307, var310, dfn295, code298, q301, cite313, abbr316, acronym319, sub322, sup325, li1328, a330, tt332, em347, strong350, dfn353, i335, b338, big341, small344, var368, cite371, abbr374, code356, q359, samp362, kbd365, sup383, br386, span389, acronym377, sub380, caption392, tr406, col394, colgroup397, thead400, tfoot402, tbody404, tr408, tr411, th417, tr414, td419, li1421},
    generalizations={gen_xhtml_A_AContent, gen_xhtml_Abbr_Inline, gen_xhtml_Acronym_Inline, gen_xhtml_B_Inline, gen_xhtml_Big_Inline, gen_xhtml_Blockquote_Block, gen_xhtml_Caption_Inline, gen_xhtml_Cite_Inline, gen_xhtml_Code_Inline, gen_xhtml_Del_Flow, gen_xhtml_Dfn_Inline, gen_xhtml_Div_Flow, gen_xhtml_Dd_Flow, gen_xhtml_Dt_Inline, gen_xhtml_Em_Inline, gen_xhtml_I_Inline, gen_xhtml_Li_Flow, gen_xhtml_Ins_Flow, gen_xhtml_Kbd_Inline, gen_xhtml_P_Inline, gen_xhtml_Pre_PreContent, gen_xhtml_Small_Inline, gen_xhtml_Q_Inline, gen_xhtml_Samp_Inline, gen_xhtml_Span_Inline, gen_xhtml_Strong_Inline, gen_xhtml_Sub_Inline, gen_xhtml_Sup_Inline, gen_xhtml_Td_Flow, gen_xhtml_Th_Flow, gen_xhtml_Tt_Inline, gen_xhtml_Var_Inline},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)