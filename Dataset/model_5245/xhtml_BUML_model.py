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

DirType: Enumeration = Enumeration(
    name="DirType",
    literals={
            EnumerationLiteral(name="ltr"),
			EnumerationLiteral(name="rtl")
    }
)

DirType1: Enumeration = Enumeration(
    name="DirType1",
    literals={
            EnumerationLiteral(name="rtl"),
			EnumerationLiteral(name="ltr")
    }
)

IsmapType: Enumeration = Enumeration(
    name="IsmapType",
    literals={
            EnumerationLiteral(name="ismap")
    }
)

NohrefType: Enumeration = Enumeration(
    name="NohrefType",
    literals={
            EnumerationLiteral(name="nohref")
    }
)

Scope: Enumeration = Enumeration(
    name="Scope",
    literals={
            EnumerationLiteral(name="row"),
			EnumerationLiteral(name="col"),
			EnumerationLiteral(name="rowgroup"),
			EnumerationLiteral(name="colgroup")
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
			EnumerationLiteral(name="all"),
			EnumerationLiteral(name="cols")
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
xhtml_AbbrType = Class(name="xhtml::AbbrType")
xhtml_BrType = Class(name="xhtml::BrType")
xhtml_SpanType = Class(name="xhtml::SpanType")
xhtml_BdoType = Class(name="xhtml::BdoType")
Inline = Class(name="Inline")
xhtml_AContent = Class(name="xhtml::AContent")
xhtml_BigType = Class(name="xhtml::BigType")
xhtml_SmallType = Class(name="xhtml::SmallType")
xhtml_EmType = Class(name="xhtml::EmType")
xhtml_StrongType = Class(name="xhtml::StrongType")
xhtml_MapType = Class(name="xhtml::MapType")
xhtml_ImgType = Class(name="xhtml::ImgType")
xhtml_TtType = Class(name="xhtml::TtType")
xhtml_IType = Class(name="xhtml::IType")
xhtml_BType = Class(name="xhtml::BType")
xhtml_VarType = Class(name="xhtml::VarType")
xhtml_CiteType = Class(name="xhtml::CiteType")
xhtml_DfnType = Class(name="xhtml::DfnType")
xhtml_CodeType = Class(name="xhtml::CodeType")
xhtml_QType = Class(name="xhtml::QType")
xhtml_SampType = Class(name="xhtml::SampType")
xhtml_KbdType = Class(name="xhtml::KbdType")
xhtml_AddressType = Class(name="xhtml::AddressType")
xhtml_AcronymType = Class(name="xhtml::AcronymType")
xhtml_SubType = Class(name="xhtml::SubType")
xhtml_SupType = Class(name="xhtml::SupType")
xhtml_AreaType = Class(name="xhtml::AreaType")
xhtml_AType = Class(name="xhtml::AType")
AContent = Class(name="AContent")
xhtml_H2Type = Class(name="xhtml::H2Type")
xhtml_H3Type = Class(name="xhtml::H3Type")
xhtml_H4Type = Class(name="xhtml::H4Type")
xhtml_H5Type = Class(name="xhtml::H5Type")
xhtml_Block = Class(name="xhtml::Block")
xhtml_PType = Class(name="xhtml::PType")
xhtml_H1Type = Class(name="xhtml::H1Type")
xhtml_H6Type = Class(name="xhtml::H6Type")
xhtml_DivType = Class(name="xhtml::DivType")
xhtml_UlType = Class(name="xhtml::UlType")
xhtml_OlType = Class(name="xhtml::OlType")
xhtml_HrType = Class(name="xhtml::HrType")
xhtml_BlockquoteType = Class(name="xhtml::BlockquoteType")
xhtml_DlType = Class(name="xhtml::DlType")
xhtml_PreType = Class(name="xhtml::PreType")
xhtml_TableType = Class(name="xhtml::TableType")
Block = Class(name="Block")
xhtml_CaptionType = Class(name="xhtml::CaptionType")
xhtml_ColgroupType = Class(name="xhtml::ColgroupType")
xhtml_ColType = Class(name="xhtml::ColType")
xhtml_DdType = Class(name="xhtml::DdType")
Flow = Class(name="Flow")
xhtml_DocumentRoot = Class(name="xhtml::DocumentRoot")
xhtml_DtType = Class(name="xhtml::DtType")
xhtml_EStringToStringMapEntry = Class(name="xhtml::EStringToStringMapEntry")
xhtml_LiType = Class(name="xhtml::LiType")
xhtml_TbodyType = Class(name="xhtml::TbodyType")
xhtml_TdType = Class(name="xhtml::TdType")
xhtml_TfootType = Class(name="xhtml::TfootType")
xhtml_ThType = Class(name="xhtml::ThType")
xhtml_TheadType = Class(name="xhtml::TheadType")
xhtml_TrType = Class(name="xhtml::TrType")
xhtml_Flow = Class(name="xhtml::Flow")
xhtml_Inline = Class(name="xhtml::Inline")
xhtml_PreContent = Class(name="xhtml::PreContent")
PreContent = Class(name="PreContent")

# xhtml_AbbrType class attributes and methods
xhtml_AbbrType_class: Property = Property(name="class", type=StringType)
xhtml_AbbrType_dir: Property = Property(name="dir", type=StringType)
xhtml_AbbrType_id: Property = Property(name="id", type=StringType)
xhtml_AbbrType_lang: Property = Property(name="lang", type=StringType)
xhtml_AbbrType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_AbbrType_style: Property = Property(name="style", type=StringType)
xhtml_AbbrType_title: Property = Property(name="title", type=StringType)
xhtml_AbbrType.attributes={xhtml_AbbrType_style, xhtml_AbbrType_id, xhtml_AbbrType_class, xhtml_AbbrType_lang1, xhtml_AbbrType_lang, xhtml_AbbrType_dir, xhtml_AbbrType_title}

# xhtml_BrType class attributes and methods
xhtml_BrType_class: Property = Property(name="class", type=StringType)
xhtml_BrType_id: Property = Property(name="id", type=StringType)
xhtml_BrType_style: Property = Property(name="style", type=StringType)
xhtml_BrType_title: Property = Property(name="title", type=StringType)
xhtml_BrType.attributes={xhtml_BrType_id, xhtml_BrType_style, xhtml_BrType_class, xhtml_BrType_title}

# xhtml_SpanType class attributes and methods
xhtml_SpanType_class: Property = Property(name="class", type=StringType)
xhtml_SpanType_dir: Property = Property(name="dir", type=StringType)
xhtml_SpanType_lang: Property = Property(name="lang", type=StringType)
xhtml_SpanType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_SpanType_style: Property = Property(name="style", type=StringType)
xhtml_SpanType_title: Property = Property(name="title", type=StringType)
xhtml_SpanType_id: Property = Property(name="id", type=StringType)
xhtml_SpanType.attributes={xhtml_SpanType_id, xhtml_SpanType_lang, xhtml_SpanType_dir, xhtml_SpanType_style, xhtml_SpanType_class, xhtml_SpanType_lang1, xhtml_SpanType_title}

# xhtml_BdoType class attributes and methods
xhtml_BdoType_lang: Property = Property(name="lang", type=StringType)
xhtml_BdoType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_BdoType_style: Property = Property(name="style", type=StringType)
xhtml_BdoType_title: Property = Property(name="title", type=StringType)
xhtml_BdoType_class: Property = Property(name="class", type=StringType)
xhtml_BdoType_dir: Property = Property(name="dir", type=StringType)
xhtml_BdoType_id: Property = Property(name="id", type=StringType)
xhtml_BdoType.attributes={xhtml_BdoType_lang, xhtml_BdoType_lang1, xhtml_BdoType_title, xhtml_BdoType_class, xhtml_BdoType_style, xhtml_BdoType_dir, xhtml_BdoType_id}

# Inline class attributes and methods

# xhtml_AContent class attributes and methods
xhtml_AContent_group: Property = Property(name="group", type=StringType)
xhtml_AContent_mixed: Property = Property(name="mixed", type=StringType)
xhtml_AContent.attributes={xhtml_AContent_mixed, xhtml_AContent_group}

# xhtml_BigType class attributes and methods
xhtml_BigType_class: Property = Property(name="class", type=StringType)
xhtml_BigType_dir: Property = Property(name="dir", type=StringType)
xhtml_BigType_id: Property = Property(name="id", type=StringType)
xhtml_BigType_lang: Property = Property(name="lang", type=StringType)
xhtml_BigType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_BigType_style: Property = Property(name="style", type=StringType)
xhtml_BigType_title: Property = Property(name="title", type=StringType)
xhtml_BigType.attributes={xhtml_BigType_style, xhtml_BigType_class, xhtml_BigType_lang, xhtml_BigType_title, xhtml_BigType_id, xhtml_BigType_lang1, xhtml_BigType_dir}

# xhtml_SmallType class attributes and methods
xhtml_SmallType_class: Property = Property(name="class", type=StringType)
xhtml_SmallType_dir: Property = Property(name="dir", type=StringType)
xhtml_SmallType_id: Property = Property(name="id", type=StringType)
xhtml_SmallType_lang: Property = Property(name="lang", type=StringType)
xhtml_SmallType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_SmallType_style: Property = Property(name="style", type=StringType)
xhtml_SmallType_title: Property = Property(name="title", type=StringType)
xhtml_SmallType.attributes={xhtml_SmallType_lang1, xhtml_SmallType_title, xhtml_SmallType_class, xhtml_SmallType_lang, xhtml_SmallType_dir, xhtml_SmallType_style, xhtml_SmallType_id}

# xhtml_EmType class attributes and methods
xhtml_EmType_dir: Property = Property(name="dir", type=StringType)
xhtml_EmType_id: Property = Property(name="id", type=StringType)
xhtml_EmType_lang: Property = Property(name="lang", type=StringType)
xhtml_EmType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_EmType_style: Property = Property(name="style", type=StringType)
xhtml_EmType_title: Property = Property(name="title", type=StringType)
xhtml_EmType_class: Property = Property(name="class", type=StringType)
xhtml_EmType.attributes={xhtml_EmType_lang, xhtml_EmType_lang1, xhtml_EmType_dir, xhtml_EmType_style, xhtml_EmType_title, xhtml_EmType_class, xhtml_EmType_id}

# xhtml_StrongType class attributes and methods
xhtml_StrongType_class: Property = Property(name="class", type=StringType)
xhtml_StrongType_dir: Property = Property(name="dir", type=StringType)
xhtml_StrongType_id: Property = Property(name="id", type=StringType)
xhtml_StrongType_lang: Property = Property(name="lang", type=StringType)
xhtml_StrongType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_StrongType_style: Property = Property(name="style", type=StringType)
xhtml_StrongType_title: Property = Property(name="title", type=StringType)
xhtml_StrongType.attributes={xhtml_StrongType_class, xhtml_StrongType_dir, xhtml_StrongType_style, xhtml_StrongType_title, xhtml_StrongType_lang1, xhtml_StrongType_id, xhtml_StrongType_lang}

# xhtml_MapType class attributes and methods
xhtml_MapType_block: Property = Property(name="block", type=StringType)
xhtml_MapType_class: Property = Property(name="class", type=StringType)
xhtml_MapType_dir: Property = Property(name="dir", type=StringType)
xhtml_MapType_id: Property = Property(name="id", type=StringType)
xhtml_MapType_lang: Property = Property(name="lang", type=StringType)
xhtml_MapType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_MapType_name: Property = Property(name="name", type=StringType)
xhtml_MapType_style: Property = Property(name="style", type=StringType)
xhtml_MapType_title: Property = Property(name="title", type=StringType)
xhtml_MapType.attributes={xhtml_MapType_name, xhtml_MapType_block, xhtml_MapType_title, xhtml_MapType_style, xhtml_MapType_dir, xhtml_MapType_lang, xhtml_MapType_lang1, xhtml_MapType_id, xhtml_MapType_class}

# xhtml_ImgType class attributes and methods
xhtml_ImgType_alt: Property = Property(name="alt", type=StringType)
xhtml_ImgType_class: Property = Property(name="class", type=StringType)
xhtml_ImgType_width: Property = Property(name="width", type=StringType)
xhtml_ImgType_dir: Property = Property(name="dir", type=StringType)
xhtml_ImgType_height: Property = Property(name="height", type=StringType)
xhtml_ImgType_id: Property = Property(name="id", type=StringType)
xhtml_ImgType_ismap: Property = Property(name="ismap", type=StringType)
xhtml_ImgType_lang: Property = Property(name="lang", type=StringType)
xhtml_ImgType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_ImgType_longdesc: Property = Property(name="longdesc", type=StringType)
xhtml_ImgType_src: Property = Property(name="src", type=StringType)
xhtml_ImgType_style: Property = Property(name="style", type=StringType)
xhtml_ImgType_title: Property = Property(name="title", type=StringType)
xhtml_ImgType_usemap: Property = Property(name="usemap", type=StringType)
xhtml_ImgType.attributes={xhtml_ImgType_title, xhtml_ImgType_style, xhtml_ImgType_width, xhtml_ImgType_longdesc, xhtml_ImgType_height, xhtml_ImgType_class, xhtml_ImgType_usemap, xhtml_ImgType_id, xhtml_ImgType_src, xhtml_ImgType_lang1, xhtml_ImgType_ismap, xhtml_ImgType_alt, xhtml_ImgType_dir, xhtml_ImgType_lang}

# xhtml_TtType class attributes and methods
xhtml_TtType_class: Property = Property(name="class", type=StringType)
xhtml_TtType_dir: Property = Property(name="dir", type=StringType)
xhtml_TtType_id: Property = Property(name="id", type=StringType)
xhtml_TtType_lang: Property = Property(name="lang", type=StringType)
xhtml_TtType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TtType_style: Property = Property(name="style", type=StringType)
xhtml_TtType_title: Property = Property(name="title", type=StringType)
xhtml_TtType.attributes={xhtml_TtType_id, xhtml_TtType_lang1, xhtml_TtType_lang, xhtml_TtType_title, xhtml_TtType_dir, xhtml_TtType_style, xhtml_TtType_class}

# xhtml_IType class attributes and methods
xhtml_IType_class: Property = Property(name="class", type=StringType)
xhtml_IType_dir: Property = Property(name="dir", type=StringType)
xhtml_IType_id: Property = Property(name="id", type=StringType)
xhtml_IType_lang: Property = Property(name="lang", type=StringType)
xhtml_IType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_IType_style: Property = Property(name="style", type=StringType)
xhtml_IType_title: Property = Property(name="title", type=StringType)
xhtml_IType.attributes={xhtml_IType_lang1, xhtml_IType_id, xhtml_IType_class, xhtml_IType_lang, xhtml_IType_style, xhtml_IType_title, xhtml_IType_dir}

# xhtml_BType class attributes and methods
xhtml_BType_class: Property = Property(name="class", type=StringType)
xhtml_BType_dir: Property = Property(name="dir", type=StringType)
xhtml_BType_id: Property = Property(name="id", type=StringType)
xhtml_BType_lang: Property = Property(name="lang", type=StringType)
xhtml_BType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_BType_style: Property = Property(name="style", type=StringType)
xhtml_BType_title: Property = Property(name="title", type=StringType)
xhtml_BType.attributes={xhtml_BType_style, xhtml_BType_id, xhtml_BType_lang, xhtml_BType_dir, xhtml_BType_class, xhtml_BType_lang1, xhtml_BType_title}

# xhtml_VarType class attributes and methods
xhtml_VarType_class: Property = Property(name="class", type=StringType)
xhtml_VarType_dir: Property = Property(name="dir", type=StringType)
xhtml_VarType_id: Property = Property(name="id", type=StringType)
xhtml_VarType_lang: Property = Property(name="lang", type=StringType)
xhtml_VarType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_VarType_style: Property = Property(name="style", type=StringType)
xhtml_VarType_title: Property = Property(name="title", type=StringType)
xhtml_VarType.attributes={xhtml_VarType_class, xhtml_VarType_style, xhtml_VarType_title, xhtml_VarType_lang1, xhtml_VarType_id, xhtml_VarType_dir, xhtml_VarType_lang}

# xhtml_CiteType class attributes and methods
xhtml_CiteType_dir: Property = Property(name="dir", type=StringType)
xhtml_CiteType_id: Property = Property(name="id", type=StringType)
xhtml_CiteType_lang: Property = Property(name="lang", type=StringType)
xhtml_CiteType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_CiteType_class: Property = Property(name="class", type=StringType)
xhtml_CiteType_style: Property = Property(name="style", type=StringType)
xhtml_CiteType_title: Property = Property(name="title", type=StringType)
xhtml_CiteType.attributes={xhtml_CiteType_class, xhtml_CiteType_title, xhtml_CiteType_id, xhtml_CiteType_lang, xhtml_CiteType_style, xhtml_CiteType_dir, xhtml_CiteType_lang1}

# xhtml_DfnType class attributes and methods
xhtml_DfnType_class: Property = Property(name="class", type=StringType)
xhtml_DfnType_dir: Property = Property(name="dir", type=StringType)
xhtml_DfnType_id: Property = Property(name="id", type=StringType)
xhtml_DfnType_lang: Property = Property(name="lang", type=StringType)
xhtml_DfnType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_DfnType_style: Property = Property(name="style", type=StringType)
xhtml_DfnType_title: Property = Property(name="title", type=StringType)
xhtml_DfnType.attributes={xhtml_DfnType_class, xhtml_DfnType_style, xhtml_DfnType_lang1, xhtml_DfnType_id, xhtml_DfnType_title, xhtml_DfnType_lang, xhtml_DfnType_dir}

# xhtml_CodeType class attributes and methods
xhtml_CodeType_lang: Property = Property(name="lang", type=StringType)
xhtml_CodeType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_CodeType_style: Property = Property(name="style", type=StringType)
xhtml_CodeType_title: Property = Property(name="title", type=StringType)
xhtml_CodeType_class: Property = Property(name="class", type=StringType)
xhtml_CodeType_dir: Property = Property(name="dir", type=StringType)
xhtml_CodeType_id: Property = Property(name="id", type=StringType)
xhtml_CodeType.attributes={xhtml_CodeType_lang, xhtml_CodeType_dir, xhtml_CodeType_title, xhtml_CodeType_class, xhtml_CodeType_style, xhtml_CodeType_lang1, xhtml_CodeType_id}

# xhtml_QType class attributes and methods
xhtml_QType_cite1: Property = Property(name="cite1", type=StringType)
xhtml_QType_dir: Property = Property(name="dir", type=StringType)
xhtml_QType_id: Property = Property(name="id", type=StringType)
xhtml_QType_lang: Property = Property(name="lang", type=StringType)
xhtml_QType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_QType_style: Property = Property(name="style", type=StringType)
xhtml_QType_title: Property = Property(name="title", type=StringType)
xhtml_QType_class: Property = Property(name="class", type=StringType)
xhtml_QType.attributes={xhtml_QType_lang, xhtml_QType_id, xhtml_QType_style, xhtml_QType_cite1, xhtml_QType_title, xhtml_QType_lang1, xhtml_QType_class, xhtml_QType_dir}

# xhtml_SampType class attributes and methods
xhtml_SampType_class: Property = Property(name="class", type=StringType)
xhtml_SampType_dir: Property = Property(name="dir", type=StringType)
xhtml_SampType_id: Property = Property(name="id", type=StringType)
xhtml_SampType_lang: Property = Property(name="lang", type=StringType)
xhtml_SampType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_SampType_style: Property = Property(name="style", type=StringType)
xhtml_SampType_title: Property = Property(name="title", type=StringType)
xhtml_SampType.attributes={xhtml_SampType_lang, xhtml_SampType_id, xhtml_SampType_lang1, xhtml_SampType_class, xhtml_SampType_title, xhtml_SampType_style, xhtml_SampType_dir}

# xhtml_KbdType class attributes and methods
xhtml_KbdType_class: Property = Property(name="class", type=StringType)
xhtml_KbdType_dir: Property = Property(name="dir", type=StringType)
xhtml_KbdType_lang: Property = Property(name="lang", type=StringType)
xhtml_KbdType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_KbdType_style: Property = Property(name="style", type=StringType)
xhtml_KbdType_title: Property = Property(name="title", type=StringType)
xhtml_KbdType_id: Property = Property(name="id", type=StringType)
xhtml_KbdType.attributes={xhtml_KbdType_lang1, xhtml_KbdType_style, xhtml_KbdType_lang, xhtml_KbdType_title, xhtml_KbdType_class, xhtml_KbdType_id, xhtml_KbdType_dir}

# xhtml_AddressType class attributes and methods
xhtml_AddressType_class: Property = Property(name="class", type=StringType)
xhtml_AddressType_dir: Property = Property(name="dir", type=StringType)
xhtml_AddressType_id: Property = Property(name="id", type=StringType)
xhtml_AddressType_lang: Property = Property(name="lang", type=StringType)
xhtml_AddressType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_AddressType_style: Property = Property(name="style", type=StringType)
xhtml_AddressType_title: Property = Property(name="title", type=StringType)
xhtml_AddressType.attributes={xhtml_AddressType_lang1, xhtml_AddressType_title, xhtml_AddressType_style, xhtml_AddressType_id, xhtml_AddressType_lang, xhtml_AddressType_class, xhtml_AddressType_dir}

# xhtml_AcronymType class attributes and methods
xhtml_AcronymType_lang: Property = Property(name="lang", type=StringType)
xhtml_AcronymType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_AcronymType_style: Property = Property(name="style", type=StringType)
xhtml_AcronymType_title: Property = Property(name="title", type=StringType)
xhtml_AcronymType_class: Property = Property(name="class", type=StringType)
xhtml_AcronymType_dir: Property = Property(name="dir", type=StringType)
xhtml_AcronymType_id: Property = Property(name="id", type=StringType)
xhtml_AcronymType.attributes={xhtml_AcronymType_lang1, xhtml_AcronymType_dir, xhtml_AcronymType_class, xhtml_AcronymType_title, xhtml_AcronymType_id, xhtml_AcronymType_style, xhtml_AcronymType_lang}

# xhtml_SubType class attributes and methods
xhtml_SubType_class: Property = Property(name="class", type=StringType)
xhtml_SubType_dir: Property = Property(name="dir", type=StringType)
xhtml_SubType_lang: Property = Property(name="lang", type=StringType)
xhtml_SubType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_SubType_style: Property = Property(name="style", type=StringType)
xhtml_SubType_title: Property = Property(name="title", type=StringType)
xhtml_SubType_id: Property = Property(name="id", type=StringType)
xhtml_SubType.attributes={xhtml_SubType_title, xhtml_SubType_dir, xhtml_SubType_id, xhtml_SubType_lang, xhtml_SubType_style, xhtml_SubType_class, xhtml_SubType_lang1}

# xhtml_SupType class attributes and methods
xhtml_SupType_class: Property = Property(name="class", type=StringType)
xhtml_SupType_dir: Property = Property(name="dir", type=StringType)
xhtml_SupType_id: Property = Property(name="id", type=StringType)
xhtml_SupType_lang: Property = Property(name="lang", type=StringType)
xhtml_SupType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_SupType_style: Property = Property(name="style", type=StringType)
xhtml_SupType_title: Property = Property(name="title", type=StringType)
xhtml_SupType.attributes={xhtml_SupType_lang, xhtml_SupType_class, xhtml_SupType_dir, xhtml_SupType_id, xhtml_SupType_title, xhtml_SupType_lang1, xhtml_SupType_style}

# xhtml_AreaType class attributes and methods
xhtml_AreaType_alt: Property = Property(name="alt", type=StringType)
xhtml_AreaType_class: Property = Property(name="class", type=StringType)
xhtml_AreaType_coords: Property = Property(name="coords", type=StringType)
xhtml_AreaType_dir: Property = Property(name="dir", type=StringType)
xhtml_AreaType_href: Property = Property(name="href", type=StringType)
xhtml_AreaType_id: Property = Property(name="id", type=StringType)
xhtml_AreaType_lang: Property = Property(name="lang", type=StringType)
xhtml_AreaType_accesskey: Property = Property(name="accesskey", type=StringType)
xhtml_AreaType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_AreaType_nohref: Property = Property(name="nohref", type=StringType)
xhtml_AreaType_shape: Property = Property(name="shape", type=StringType)
xhtml_AreaType_style: Property = Property(name="style", type=StringType)
xhtml_AreaType_tabindex: Property = Property(name="tabindex", type=StringType)
xhtml_AreaType_title: Property = Property(name="title", type=StringType)
xhtml_AreaType.attributes={xhtml_AreaType_id, xhtml_AreaType_coords, xhtml_AreaType_dir, xhtml_AreaType_href, xhtml_AreaType_accesskey, xhtml_AreaType_tabindex, xhtml_AreaType_nohref, xhtml_AreaType_title, xhtml_AreaType_lang, xhtml_AreaType_shape, xhtml_AreaType_lang1, xhtml_AreaType_style, xhtml_AreaType_alt, xhtml_AreaType_class}

# xhtml_AType class attributes and methods
xhtml_AType_coords: Property = Property(name="coords", type=StringType)
xhtml_AType_dir: Property = Property(name="dir", type=StringType)
xhtml_AType_href: Property = Property(name="href", type=StringType)
xhtml_AType_hreflang: Property = Property(name="hreflang", type=StringType)
xhtml_AType_id: Property = Property(name="id", type=StringType)
xhtml_AType_lang: Property = Property(name="lang", type=StringType)
xhtml_AType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_AType_name: Property = Property(name="name", type=StringType)
xhtml_AType_accesskey: Property = Property(name="accesskey", type=StringType)
xhtml_AType_charset: Property = Property(name="charset", type=StringType)
xhtml_AType_class: Property = Property(name="class", type=StringType)
xhtml_AType_rel: Property = Property(name="rel", type=StringType)
xhtml_AType_rev: Property = Property(name="rev", type=StringType)
xhtml_AType_shape: Property = Property(name="shape", type=StringType)
xhtml_AType_style: Property = Property(name="style", type=StringType)
xhtml_AType_tabindex: Property = Property(name="tabindex", type=StringType)
xhtml_AType_title: Property = Property(name="title", type=StringType)
xhtml_AType_type: Property = Property(name="type", type=StringType)
xhtml_AType.attributes={xhtml_AType_rel, xhtml_AType_shape, xhtml_AType_coords, xhtml_AType_class, xhtml_AType_type, xhtml_AType_charset, xhtml_AType_id, xhtml_AType_lang, xhtml_AType_href, xhtml_AType_accesskey, xhtml_AType_name, xhtml_AType_style, xhtml_AType_rev, xhtml_AType_title, xhtml_AType_lang1, xhtml_AType_hreflang, xhtml_AType_tabindex, xhtml_AType_dir}

# AContent class attributes and methods

# xhtml_H2Type class attributes and methods
xhtml_H2Type_lang: Property = Property(name="lang", type=StringType)
xhtml_H2Type_lang1: Property = Property(name="lang1", type=StringType)
xhtml_H2Type_style: Property = Property(name="style", type=StringType)
xhtml_H2Type_title: Property = Property(name="title", type=StringType)
xhtml_H2Type_class: Property = Property(name="class", type=StringType)
xhtml_H2Type_dir: Property = Property(name="dir", type=StringType)
xhtml_H2Type_id: Property = Property(name="id", type=StringType)
xhtml_H2Type.attributes={xhtml_H2Type_title, xhtml_H2Type_class, xhtml_H2Type_style, xhtml_H2Type_id, xhtml_H2Type_dir, xhtml_H2Type_lang, xhtml_H2Type_lang1}

# xhtml_H3Type class attributes and methods
xhtml_H3Type_class: Property = Property(name="class", type=StringType)
xhtml_H3Type_dir: Property = Property(name="dir", type=StringType)
xhtml_H3Type_id: Property = Property(name="id", type=StringType)
xhtml_H3Type_lang: Property = Property(name="lang", type=StringType)
xhtml_H3Type_lang1: Property = Property(name="lang1", type=StringType)
xhtml_H3Type_style: Property = Property(name="style", type=StringType)
xhtml_H3Type_title: Property = Property(name="title", type=StringType)
xhtml_H3Type.attributes={xhtml_H3Type_dir, xhtml_H3Type_id, xhtml_H3Type_lang, xhtml_H3Type_class, xhtml_H3Type_title, xhtml_H3Type_style, xhtml_H3Type_lang1}

# xhtml_H4Type class attributes and methods
xhtml_H4Type_title: Property = Property(name="title", type=StringType)
xhtml_H4Type_class: Property = Property(name="class", type=StringType)
xhtml_H4Type_dir: Property = Property(name="dir", type=StringType)
xhtml_H4Type_id: Property = Property(name="id", type=StringType)
xhtml_H4Type_lang: Property = Property(name="lang", type=StringType)
xhtml_H4Type_lang1: Property = Property(name="lang1", type=StringType)
xhtml_H4Type_style: Property = Property(name="style", type=StringType)
xhtml_H4Type.attributes={xhtml_H4Type_lang, xhtml_H4Type_style, xhtml_H4Type_title, xhtml_H4Type_lang1, xhtml_H4Type_class, xhtml_H4Type_id, xhtml_H4Type_dir}

# xhtml_H5Type class attributes and methods
xhtml_H5Type_class: Property = Property(name="class", type=StringType)
xhtml_H5Type_dir: Property = Property(name="dir", type=StringType)
xhtml_H5Type_id: Property = Property(name="id", type=StringType)
xhtml_H5Type_lang: Property = Property(name="lang", type=StringType)
xhtml_H5Type_lang1: Property = Property(name="lang1", type=StringType)
xhtml_H5Type_style: Property = Property(name="style", type=StringType)
xhtml_H5Type_title: Property = Property(name="title", type=StringType)
xhtml_H5Type.attributes={xhtml_H5Type_dir, xhtml_H5Type_id, xhtml_H5Type_lang, xhtml_H5Type_title, xhtml_H5Type_lang1, xhtml_H5Type_class, xhtml_H5Type_style}

# xhtml_Block class attributes and methods
xhtml_Block_block: Property = Property(name="block", type=StringType)
xhtml_Block.attributes={xhtml_Block_block}

# xhtml_PType class attributes and methods
xhtml_PType_class: Property = Property(name="class", type=StringType)
xhtml_PType_dir: Property = Property(name="dir", type=StringType)
xhtml_PType_id: Property = Property(name="id", type=StringType)
xhtml_PType_lang: Property = Property(name="lang", type=StringType)
xhtml_PType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_PType_style: Property = Property(name="style", type=StringType)
xhtml_PType_title: Property = Property(name="title", type=StringType)
xhtml_PType.attributes={xhtml_PType_dir, xhtml_PType_style, xhtml_PType_lang, xhtml_PType_class, xhtml_PType_id, xhtml_PType_title, xhtml_PType_lang1}

# xhtml_H1Type class attributes and methods
xhtml_H1Type_class: Property = Property(name="class", type=StringType)
xhtml_H1Type_dir: Property = Property(name="dir", type=StringType)
xhtml_H1Type_id: Property = Property(name="id", type=StringType)
xhtml_H1Type_lang: Property = Property(name="lang", type=StringType)
xhtml_H1Type_lang1: Property = Property(name="lang1", type=StringType)
xhtml_H1Type_style: Property = Property(name="style", type=StringType)
xhtml_H1Type_title: Property = Property(name="title", type=StringType)
xhtml_H1Type.attributes={xhtml_H1Type_style, xhtml_H1Type_title, xhtml_H1Type_lang, xhtml_H1Type_class, xhtml_H1Type_id, xhtml_H1Type_dir, xhtml_H1Type_lang1}

# xhtml_H6Type class attributes and methods
xhtml_H6Type_class: Property = Property(name="class", type=StringType)
xhtml_H6Type_dir: Property = Property(name="dir", type=StringType)
xhtml_H6Type_id: Property = Property(name="id", type=StringType)
xhtml_H6Type_lang: Property = Property(name="lang", type=StringType)
xhtml_H6Type_lang1: Property = Property(name="lang1", type=StringType)
xhtml_H6Type_style: Property = Property(name="style", type=StringType)
xhtml_H6Type_title: Property = Property(name="title", type=StringType)
xhtml_H6Type.attributes={xhtml_H6Type_style, xhtml_H6Type_id, xhtml_H6Type_title, xhtml_H6Type_lang1, xhtml_H6Type_dir, xhtml_H6Type_lang, xhtml_H6Type_class}

# xhtml_DivType class attributes and methods
xhtml_DivType_class: Property = Property(name="class", type=StringType)
xhtml_DivType_dir: Property = Property(name="dir", type=StringType)
xhtml_DivType_id: Property = Property(name="id", type=StringType)
xhtml_DivType_lang: Property = Property(name="lang", type=StringType)
xhtml_DivType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_DivType_style: Property = Property(name="style", type=StringType)
xhtml_DivType_title: Property = Property(name="title", type=StringType)
xhtml_DivType.attributes={xhtml_DivType_style, xhtml_DivType_title, xhtml_DivType_class, xhtml_DivType_lang1, xhtml_DivType_dir, xhtml_DivType_lang, xhtml_DivType_id}

# xhtml_UlType class attributes and methods
xhtml_UlType_class: Property = Property(name="class", type=StringType)
xhtml_UlType_dir: Property = Property(name="dir", type=StringType)
xhtml_UlType_id: Property = Property(name="id", type=StringType)
xhtml_UlType_lang: Property = Property(name="lang", type=StringType)
xhtml_UlType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_UlType_style: Property = Property(name="style", type=StringType)
xhtml_UlType_title: Property = Property(name="title", type=StringType)
xhtml_UlType.attributes={xhtml_UlType_style, xhtml_UlType_dir, xhtml_UlType_lang1, xhtml_UlType_lang, xhtml_UlType_id, xhtml_UlType_title, xhtml_UlType_class}

# xhtml_OlType class attributes and methods
xhtml_OlType_class: Property = Property(name="class", type=StringType)
xhtml_OlType_dir: Property = Property(name="dir", type=StringType)
xhtml_OlType_id: Property = Property(name="id", type=StringType)
xhtml_OlType_lang: Property = Property(name="lang", type=StringType)
xhtml_OlType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_OlType_style: Property = Property(name="style", type=StringType)
xhtml_OlType_title: Property = Property(name="title", type=StringType)
xhtml_OlType.attributes={xhtml_OlType_title, xhtml_OlType_lang1, xhtml_OlType_class, xhtml_OlType_lang, xhtml_OlType_dir, xhtml_OlType_id, xhtml_OlType_style}

# xhtml_HrType class attributes and methods
xhtml_HrType_dir: Property = Property(name="dir", type=StringType)
xhtml_HrType_id: Property = Property(name="id", type=StringType)
xhtml_HrType_lang: Property = Property(name="lang", type=StringType)
xhtml_HrType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_HrType_style: Property = Property(name="style", type=StringType)
xhtml_HrType_title: Property = Property(name="title", type=StringType)
xhtml_HrType_class: Property = Property(name="class", type=StringType)
xhtml_HrType.attributes={xhtml_HrType_lang, xhtml_HrType_dir, xhtml_HrType_title, xhtml_HrType_class, xhtml_HrType_style, xhtml_HrType_id, xhtml_HrType_lang1}

# xhtml_BlockquoteType class attributes and methods
xhtml_BlockquoteType_style: Property = Property(name="style", type=StringType)
xhtml_BlockquoteType_title: Property = Property(name="title", type=StringType)
xhtml_BlockquoteType_cite: Property = Property(name="cite", type=StringType)
xhtml_BlockquoteType_class: Property = Property(name="class", type=StringType)
xhtml_BlockquoteType_dir: Property = Property(name="dir", type=StringType)
xhtml_BlockquoteType_id: Property = Property(name="id", type=StringType)
xhtml_BlockquoteType_lang: Property = Property(name="lang", type=StringType)
xhtml_BlockquoteType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_BlockquoteType.attributes={xhtml_BlockquoteType_lang, xhtml_BlockquoteType_class, xhtml_BlockquoteType_title, xhtml_BlockquoteType_id, xhtml_BlockquoteType_lang1, xhtml_BlockquoteType_style, xhtml_BlockquoteType_dir, xhtml_BlockquoteType_cite}

# xhtml_DlType class attributes and methods
xhtml_DlType_dir: Property = Property(name="dir", type=StringType)
xhtml_DlType_id: Property = Property(name="id", type=StringType)
xhtml_DlType_lang: Property = Property(name="lang", type=StringType)
xhtml_DlType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_DlType_style: Property = Property(name="style", type=StringType)
xhtml_DlType_title: Property = Property(name="title", type=StringType)
xhtml_DlType_group: Property = Property(name="group", type=StringType)
xhtml_DlType_class: Property = Property(name="class", type=StringType)
xhtml_DlType.attributes={xhtml_DlType_class, xhtml_DlType_lang, xhtml_DlType_dir, xhtml_DlType_group, xhtml_DlType_id, xhtml_DlType_lang1, xhtml_DlType_style, xhtml_DlType_title}

# xhtml_PreType class attributes and methods
xhtml_PreType_class: Property = Property(name="class", type=StringType)
xhtml_PreType_dir: Property = Property(name="dir", type=StringType)
xhtml_PreType_id: Property = Property(name="id", type=StringType)
xhtml_PreType_lang: Property = Property(name="lang", type=StringType)
xhtml_PreType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_PreType_space: Property = Property(name="space", type=StringType)
xhtml_PreType_style: Property = Property(name="style", type=StringType)
xhtml_PreType_title: Property = Property(name="title", type=StringType)
xhtml_PreType.attributes={xhtml_PreType_id, xhtml_PreType_lang1, xhtml_PreType_space, xhtml_PreType_class, xhtml_PreType_style, xhtml_PreType_title, xhtml_PreType_dir, xhtml_PreType_lang}

# xhtml_TableType class attributes and methods
xhtml_TableType_border: Property = Property(name="border", type=StringType)
xhtml_TableType_cellpadding: Property = Property(name="cellpadding", type=StringType)
xhtml_TableType_cellspacing: Property = Property(name="cellspacing", type=StringType)
xhtml_TableType_class: Property = Property(name="class", type=StringType)
xhtml_TableType_dir: Property = Property(name="dir", type=StringType)
xhtml_TableType_id: Property = Property(name="id", type=StringType)
xhtml_TableType_lang: Property = Property(name="lang", type=StringType)
xhtml_TableType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TableType_rules: Property = Property(name="rules", type=StringType)
xhtml_TableType_style: Property = Property(name="style", type=StringType)
xhtml_TableType_summary: Property = Property(name="summary", type=StringType)
xhtml_TableType_title: Property = Property(name="title", type=StringType)
xhtml_TableType_width: Property = Property(name="width", type=StringType)
xhtml_TableType_frame: Property = Property(name="frame", type=StringType)
xhtml_TableType.attributes={xhtml_TableType_title, xhtml_TableType_width, xhtml_TableType_dir, xhtml_TableType_cellspacing, xhtml_TableType_class, xhtml_TableType_rules, xhtml_TableType_id, xhtml_TableType_style, xhtml_TableType_lang1, xhtml_TableType_frame, xhtml_TableType_cellpadding, xhtml_TableType_lang, xhtml_TableType_border, xhtml_TableType_summary}

# Block class attributes and methods

# xhtml_CaptionType class attributes and methods
xhtml_CaptionType_id: Property = Property(name="id", type=StringType)
xhtml_CaptionType_lang: Property = Property(name="lang", type=StringType)
xhtml_CaptionType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_CaptionType_style: Property = Property(name="style", type=StringType)
xhtml_CaptionType_title: Property = Property(name="title", type=StringType)
xhtml_CaptionType_class: Property = Property(name="class", type=StringType)
xhtml_CaptionType_dir: Property = Property(name="dir", type=StringType)
xhtml_CaptionType.attributes={xhtml_CaptionType_class, xhtml_CaptionType_style, xhtml_CaptionType_id, xhtml_CaptionType_lang, xhtml_CaptionType_lang1, xhtml_CaptionType_title, xhtml_CaptionType_dir}

# xhtml_ColgroupType class attributes and methods
xhtml_ColgroupType_align: Property = Property(name="align", type=StringType)
xhtml_ColgroupType_width: Property = Property(name="width", type=StringType)
xhtml_ColgroupType_char: Property = Property(name="char", type=StringType)
xhtml_ColgroupType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_ColgroupType_class: Property = Property(name="class", type=StringType)
xhtml_ColgroupType_dir: Property = Property(name="dir", type=StringType)
xhtml_ColgroupType_id: Property = Property(name="id", type=StringType)
xhtml_ColgroupType_lang: Property = Property(name="lang", type=StringType)
xhtml_ColgroupType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_ColgroupType_span: Property = Property(name="span", type=StringType)
xhtml_ColgroupType_style: Property = Property(name="style", type=StringType)
xhtml_ColgroupType_title: Property = Property(name="title", type=StringType)
xhtml_ColgroupType_valign: Property = Property(name="valign", type=StringType)
xhtml_ColgroupType.attributes={xhtml_ColgroupType_class, xhtml_ColgroupType_lang1, xhtml_ColgroupType_align, xhtml_ColgroupType_title, xhtml_ColgroupType_charoff, xhtml_ColgroupType_id, xhtml_ColgroupType_span, xhtml_ColgroupType_width, xhtml_ColgroupType_dir, xhtml_ColgroupType_valign, xhtml_ColgroupType_lang, xhtml_ColgroupType_char, xhtml_ColgroupType_style}

# xhtml_ColType class attributes and methods
xhtml_ColType_align: Property = Property(name="align", type=StringType)
xhtml_ColType_char: Property = Property(name="char", type=StringType)
xhtml_ColType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_ColType_class: Property = Property(name="class", type=StringType)
xhtml_ColType_dir: Property = Property(name="dir", type=StringType)
xhtml_ColType_id: Property = Property(name="id", type=StringType)
xhtml_ColType_lang: Property = Property(name="lang", type=StringType)
xhtml_ColType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_ColType_span: Property = Property(name="span", type=StringType)
xhtml_ColType_style: Property = Property(name="style", type=StringType)
xhtml_ColType_title: Property = Property(name="title", type=StringType)
xhtml_ColType_valign: Property = Property(name="valign", type=StringType)
xhtml_ColType_width: Property = Property(name="width", type=StringType)
xhtml_ColType.attributes={xhtml_ColType_class, xhtml_ColType_lang, xhtml_ColType_style, xhtml_ColType_width, xhtml_ColType_valign, xhtml_ColType_align, xhtml_ColType_span, xhtml_ColType_charoff, xhtml_ColType_char, xhtml_ColType_title, xhtml_ColType_lang1, xhtml_ColType_dir, xhtml_ColType_id}

# xhtml_DdType class attributes and methods
xhtml_DdType_class: Property = Property(name="class", type=StringType)
xhtml_DdType_dir: Property = Property(name="dir", type=StringType)
xhtml_DdType_id: Property = Property(name="id", type=StringType)
xhtml_DdType_lang: Property = Property(name="lang", type=StringType)
xhtml_DdType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_DdType_style: Property = Property(name="style", type=StringType)
xhtml_DdType_title: Property = Property(name="title", type=StringType)
xhtml_DdType.attributes={xhtml_DdType_lang1, xhtml_DdType_id, xhtml_DdType_style, xhtml_DdType_lang, xhtml_DdType_dir, xhtml_DdType_title, xhtml_DdType_class}

# Flow class attributes and methods

# xhtml_DocumentRoot class attributes and methods
xhtml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
xhtml_DocumentRoot.attributes={xhtml_DocumentRoot_mixed}

# xhtml_DtType class attributes and methods
xhtml_DtType_class: Property = Property(name="class", type=StringType)
xhtml_DtType_dir: Property = Property(name="dir", type=StringType)
xhtml_DtType_id: Property = Property(name="id", type=StringType)
xhtml_DtType_lang: Property = Property(name="lang", type=StringType)
xhtml_DtType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_DtType_style: Property = Property(name="style", type=StringType)
xhtml_DtType_title: Property = Property(name="title", type=StringType)
xhtml_DtType.attributes={xhtml_DtType_dir, xhtml_DtType_style, xhtml_DtType_id, xhtml_DtType_title, xhtml_DtType_lang, xhtml_DtType_class, xhtml_DtType_lang1}

# xhtml_EStringToStringMapEntry class attributes and methods

# xhtml_LiType class attributes and methods
xhtml_LiType_class: Property = Property(name="class", type=StringType)
xhtml_LiType_dir: Property = Property(name="dir", type=StringType)
xhtml_LiType_id: Property = Property(name="id", type=StringType)
xhtml_LiType_lang: Property = Property(name="lang", type=StringType)
xhtml_LiType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_LiType_style: Property = Property(name="style", type=StringType)
xhtml_LiType_title: Property = Property(name="title", type=StringType)
xhtml_LiType.attributes={xhtml_LiType_lang1, xhtml_LiType_dir, xhtml_LiType_style, xhtml_LiType_title, xhtml_LiType_lang, xhtml_LiType_id, xhtml_LiType_class}

# xhtml_TbodyType class attributes and methods
xhtml_TbodyType_align: Property = Property(name="align", type=StringType)
xhtml_TbodyType_char: Property = Property(name="char", type=StringType)
xhtml_TbodyType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TbodyType_class: Property = Property(name="class", type=StringType)
xhtml_TbodyType_id: Property = Property(name="id", type=StringType)
xhtml_TbodyType_lang: Property = Property(name="lang", type=StringType)
xhtml_TbodyType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TbodyType_style: Property = Property(name="style", type=StringType)
xhtml_TbodyType_title: Property = Property(name="title", type=StringType)
xhtml_TbodyType_valign: Property = Property(name="valign", type=StringType)
xhtml_TbodyType_dir: Property = Property(name="dir", type=StringType)
xhtml_TbodyType.attributes={xhtml_TbodyType_lang1, xhtml_TbodyType_char, xhtml_TbodyType_style, xhtml_TbodyType_class, xhtml_TbodyType_id, xhtml_TbodyType_align, xhtml_TbodyType_lang, xhtml_TbodyType_valign, xhtml_TbodyType_title, xhtml_TbodyType_dir, xhtml_TbodyType_charoff}

# xhtml_TdType class attributes and methods
xhtml_TdType_abbr1: Property = Property(name="abbr1", type=StringType)
xhtml_TdType_align: Property = Property(name="align", type=StringType)
xhtml_TdType_axis: Property = Property(name="axis", type=StringType)
xhtml_TdType_char: Property = Property(name="char", type=StringType)
xhtml_TdType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TdType_class: Property = Property(name="class", type=StringType)
xhtml_TdType_colspan: Property = Property(name="colspan", type=StringType)
xhtml_TdType_dir: Property = Property(name="dir", type=StringType)
xhtml_TdType_headers: Property = Property(name="headers", type=StringType)
xhtml_TdType_id: Property = Property(name="id", type=StringType)
xhtml_TdType_lang: Property = Property(name="lang", type=StringType)
xhtml_TdType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TdType_rowspan: Property = Property(name="rowspan", type=StringType)
xhtml_TdType_scope: Property = Property(name="scope", type=StringType)
xhtml_TdType_style: Property = Property(name="style", type=StringType)
xhtml_TdType_title: Property = Property(name="title", type=StringType)
xhtml_TdType_valign: Property = Property(name="valign", type=StringType)
xhtml_TdType.attributes={xhtml_TdType_dir, xhtml_TdType_class, xhtml_TdType_charoff, xhtml_TdType_abbr1, xhtml_TdType_id, xhtml_TdType_scope, xhtml_TdType_title, xhtml_TdType_headers, xhtml_TdType_axis, xhtml_TdType_colspan, xhtml_TdType_style, xhtml_TdType_align, xhtml_TdType_lang1, xhtml_TdType_rowspan, xhtml_TdType_valign, xhtml_TdType_char, xhtml_TdType_lang}

# xhtml_TfootType class attributes and methods
xhtml_TfootType_align: Property = Property(name="align", type=StringType)
xhtml_TfootType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TfootType_class: Property = Property(name="class", type=StringType)
xhtml_TfootType_dir: Property = Property(name="dir", type=StringType)
xhtml_TfootType_id: Property = Property(name="id", type=StringType)
xhtml_TfootType_lang: Property = Property(name="lang", type=StringType)
xhtml_TfootType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TfootType_style: Property = Property(name="style", type=StringType)
xhtml_TfootType_title: Property = Property(name="title", type=StringType)
xhtml_TfootType_valign: Property = Property(name="valign", type=StringType)
xhtml_TfootType_char: Property = Property(name="char", type=StringType)
xhtml_TfootType.attributes={xhtml_TfootType_align, xhtml_TfootType_lang1, xhtml_TfootType_title, xhtml_TfootType_valign, xhtml_TfootType_id, xhtml_TfootType_class, xhtml_TfootType_style, xhtml_TfootType_dir, xhtml_TfootType_lang, xhtml_TfootType_char, xhtml_TfootType_charoff}

# xhtml_ThType class attributes and methods
xhtml_ThType_abbr1: Property = Property(name="abbr1", type=StringType)
xhtml_ThType_align: Property = Property(name="align", type=StringType)
xhtml_ThType_axis: Property = Property(name="axis", type=StringType)
xhtml_ThType_char: Property = Property(name="char", type=StringType)
xhtml_ThType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_ThType_class: Property = Property(name="class", type=StringType)
xhtml_ThType_dir: Property = Property(name="dir", type=StringType)
xhtml_ThType_headers: Property = Property(name="headers", type=StringType)
xhtml_ThType_id: Property = Property(name="id", type=StringType)
xhtml_ThType_lang: Property = Property(name="lang", type=StringType)
xhtml_ThType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_ThType_rowspan: Property = Property(name="rowspan", type=StringType)
xhtml_ThType_scope: Property = Property(name="scope", type=StringType)
xhtml_ThType_style: Property = Property(name="style", type=StringType)
xhtml_ThType_title: Property = Property(name="title", type=StringType)
xhtml_ThType_valign: Property = Property(name="valign", type=StringType)
xhtml_ThType_colspan: Property = Property(name="colspan", type=StringType)
xhtml_ThType.attributes={xhtml_ThType_id, xhtml_ThType_rowspan, xhtml_ThType_class, xhtml_ThType_align, xhtml_ThType_abbr1, xhtml_ThType_colspan, xhtml_ThType_headers, xhtml_ThType_lang, xhtml_ThType_style, xhtml_ThType_valign, xhtml_ThType_axis, xhtml_ThType_scope, xhtml_ThType_charoff, xhtml_ThType_lang1, xhtml_ThType_title, xhtml_ThType_dir, xhtml_ThType_char}

# xhtml_TheadType class attributes and methods
xhtml_TheadType_align: Property = Property(name="align", type=StringType)
xhtml_TheadType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TheadType_class: Property = Property(name="class", type=StringType)
xhtml_TheadType_dir: Property = Property(name="dir", type=StringType)
xhtml_TheadType_id: Property = Property(name="id", type=StringType)
xhtml_TheadType_lang: Property = Property(name="lang", type=StringType)
xhtml_TheadType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TheadType_style: Property = Property(name="style", type=StringType)
xhtml_TheadType_title: Property = Property(name="title", type=StringType)
xhtml_TheadType_valign: Property = Property(name="valign", type=StringType)
xhtml_TheadType_char: Property = Property(name="char", type=StringType)
xhtml_TheadType.attributes={xhtml_TheadType_lang, xhtml_TheadType_charoff, xhtml_TheadType_align, xhtml_TheadType_style, xhtml_TheadType_title, xhtml_TheadType_dir, xhtml_TheadType_char, xhtml_TheadType_id, xhtml_TheadType_valign, xhtml_TheadType_class, xhtml_TheadType_lang1}

# xhtml_TrType class attributes and methods
xhtml_TrType_group: Property = Property(name="group", type=StringType)
xhtml_TrType_align: Property = Property(name="align", type=StringType)
xhtml_TrType_char: Property = Property(name="char", type=StringType)
xhtml_TrType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TrType_class: Property = Property(name="class", type=StringType)
xhtml_TrType_dir: Property = Property(name="dir", type=StringType)
xhtml_TrType_id: Property = Property(name="id", type=StringType)
xhtml_TrType_lang: Property = Property(name="lang", type=StringType)
xhtml_TrType_lang1: Property = Property(name="lang1", type=StringType)
xhtml_TrType_style: Property = Property(name="style", type=StringType)
xhtml_TrType_title: Property = Property(name="title", type=StringType)
xhtml_TrType_valign: Property = Property(name="valign", type=StringType)
xhtml_TrType.attributes={xhtml_TrType_group, xhtml_TrType_char, xhtml_TrType_title, xhtml_TrType_align, xhtml_TrType_class, xhtml_TrType_style, xhtml_TrType_valign, xhtml_TrType_charoff, xhtml_TrType_id, xhtml_TrType_lang1, xhtml_TrType_lang, xhtml_TrType_dir}

# xhtml_Flow class attributes and methods
xhtml_Flow_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Flow_group: Property = Property(name="group", type=StringType)
xhtml_Flow.attributes={xhtml_Flow_mixed, xhtml_Flow_group}

# xhtml_Inline class attributes and methods
xhtml_Inline_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Inline_inline: Property = Property(name="inline", type=StringType)
xhtml_Inline.attributes={xhtml_Inline_mixed, xhtml_Inline_inline}

# xhtml_PreContent class attributes and methods
xhtml_PreContent_mixed: Property = Property(name="mixed", type=StringType)
xhtml_PreContent_group: Property = Property(name="group", type=StringType)
xhtml_PreContent.attributes={xhtml_PreContent_mixed, xhtml_PreContent_group}

# PreContent class attributes and methods

# Relationships
br0: BinaryAssociation = BinaryAssociation(
    name="br0",
    ends={
        Property(name="xhtml_BrType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span1: BinaryAssociation = BinaryAssociation(
    name="span1",
    ends={
        Property(name="xhtml_SpanType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent2", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdo3: BinaryAssociation = BinaryAssociation(
    name="bdo3",
    ends={
        Property(name="xhtml_BdoType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent4", type=xhtml_BdoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big15: BinaryAssociation = BinaryAssociation(
    name="big15",
    ends={
        Property(name="xhtml_BigType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent16", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small17: BinaryAssociation = BinaryAssociation(
    name="small17",
    ends={
        Property(name="xhtml_SmallType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent18", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em19: BinaryAssociation = BinaryAssociation(
    name="em19",
    ends={
        Property(name="xhtml_EmType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent20", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong21: BinaryAssociation = BinaryAssociation(
    name="strong21",
    ends={
        Property(name="xhtml_StrongType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent22", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map5: BinaryAssociation = BinaryAssociation(
    name="map5",
    ends={
        Property(name="xhtml_MapType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent6", type=xhtml_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img7: BinaryAssociation = BinaryAssociation(
    name="img7",
    ends={
        Property(name="xhtml_ImgType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent8", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt9: BinaryAssociation = BinaryAssociation(
    name="tt9",
    ends={
        Property(name="xhtml_TtType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent10", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i11: BinaryAssociation = BinaryAssociation(
    name="i11",
    ends={
        Property(name="xhtml_IType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent12", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b13: BinaryAssociation = BinaryAssociation(
    name="b13",
    ends={
        Property(name="xhtml_BType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent14", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var33: BinaryAssociation = BinaryAssociation(
    name="var33",
    ends={
        Property(name="xhtml_VarType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent34", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite35: BinaryAssociation = BinaryAssociation(
    name="cite35",
    ends={
        Property(name="xhtml_CiteType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent36", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr37: BinaryAssociation = BinaryAssociation(
    name="abbr37",
    ends={
        Property(name="xhtml_AbbrType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent38", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn23: BinaryAssociation = BinaryAssociation(
    name="dfn23",
    ends={
        Property(name="xhtml_DfnType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent24", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code25: BinaryAssociation = BinaryAssociation(
    name="code25",
    ends={
        Property(name="xhtml_CodeType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent26", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q27: BinaryAssociation = BinaryAssociation(
    name="q27",
    ends={
        Property(name="xhtml_QType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent28", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp29: BinaryAssociation = BinaryAssociation(
    name="samp29",
    ends={
        Property(name="xhtml_SampType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent30", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd31: BinaryAssociation = BinaryAssociation(
    name="kbd31",
    ends={
        Property(name="xhtml_KbdType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent32", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym39: BinaryAssociation = BinaryAssociation(
    name="acronym39",
    ends={
        Property(name="xhtml_AcronymType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent40", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub41: BinaryAssociation = BinaryAssociation(
    name="sub41",
    ends={
        Property(name="xhtml_SubType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent42", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup43: BinaryAssociation = BinaryAssociation(
    name="sup43",
    ends={
        Property(name="xhtml_SupType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent44", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h248: BinaryAssociation = BinaryAssociation(
    name="h248",
    ends={
        Property(name="xhtml_H2Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block49", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h350: BinaryAssociation = BinaryAssociation(
    name="h350",
    ends={
        Property(name="xhtml_H3Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block51", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h452: BinaryAssociation = BinaryAssociation(
    name="h452",
    ends={
        Property(name="xhtml_H4Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block53", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p45: BinaryAssociation = BinaryAssociation(
    name="p45",
    ends={
        Property(name="xhtml_PType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h146: BinaryAssociation = BinaryAssociation(
    name="h146",
    ends={
        Property(name="xhtml_H1Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block47", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h554: BinaryAssociation = BinaryAssociation(
    name="h554",
    ends={
        Property(name="xhtml_H5Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block55", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h656: BinaryAssociation = BinaryAssociation(
    name="h656",
    ends={
        Property(name="xhtml_H6Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block57", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div58: BinaryAssociation = BinaryAssociation(
    name="div58",
    ends={
        Property(name="xhtml_DivType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block59", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul60: BinaryAssociation = BinaryAssociation(
    name="ul60",
    ends={
        Property(name="xhtml_UlType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block61", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol62: BinaryAssociation = BinaryAssociation(
    name="ol62",
    ends={
        Property(name="xhtml_OlType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block63", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr68: BinaryAssociation = BinaryAssociation(
    name="hr68",
    ends={
        Property(name="xhtml_HrType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block69", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote70: BinaryAssociation = BinaryAssociation(
    name="blockquote70",
    ends={
        Property(name="xhtml_BlockquoteType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block71", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address72: BinaryAssociation = BinaryAssociation(
    name="address72",
    ends={
        Property(name="xhtml_AddressType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block73", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl64: BinaryAssociation = BinaryAssociation(
    name="dl64",
    ends={
        Property(name="xhtml_DlType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block65", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre66: BinaryAssociation = BinaryAssociation(
    name="pre66",
    ends={
        Property(name="xhtml_PreType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block67", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table74: BinaryAssociation = BinaryAssociation(
    name="table74",
    ends={
        Property(name="xhtml_TableType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block75", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col76: BinaryAssociation = BinaryAssociation(
    name="col76",
    ends={
        Property(name="xhtml_ColType", type=xhtml_ColgroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ColgroupType", type=xhtml_ColType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dt77: BinaryAssociation = BinaryAssociation(
    name="dt77",
    ends={
        Property(name="xhtml_DtType", type=xhtml_DlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DlType78", type=xhtml_DtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dd79: BinaryAssociation = BinaryAssociation(
    name="dd79",
    ends={
        Property(name="xhtml_DdType", type=xhtml_DlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DlType80", type=xhtml_DdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
area96: BinaryAssociation = BinaryAssociation(
    name="area96",
    ends={
        Property(name="xhtml_AreaType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot97", type=xhtml_AreaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b98: BinaryAssociation = BinaryAssociation(
    name="b98",
    ends={
        Property(name="xhtml_BType100", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot99", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdo101: BinaryAssociation = BinaryAssociation(
    name="bdo101",
    ends={
        Property(name="xhtml_BdoType103", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot102", type=xhtml_BdoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big104: BinaryAssociation = BinaryAssociation(
    name="big104",
    ends={
        Property(name="xhtml_BigType106", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot105", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap81: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap81",
    ends={
        Property(name="xhtml_EStringToStringMapEntry", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot", type=xhtml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation82: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation82",
    ends={
        Property(name="xhtml_EStringToStringMapEntry84", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot83", type=xhtml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a85: BinaryAssociation = BinaryAssociation(
    name="a85",
    ends={
        Property(name="xhtml_AType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot86", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr87: BinaryAssociation = BinaryAssociation(
    name="abbr87",
    ends={
        Property(name="xhtml_AbbrType89", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot88", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym90: BinaryAssociation = BinaryAssociation(
    name="acronym90",
    ends={
        Property(name="xhtml_AcronymType92", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot91", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address93: BinaryAssociation = BinaryAssociation(
    name="address93",
    ends={
        Property(name="xhtml_AddressType95", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot94", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col121: BinaryAssociation = BinaryAssociation(
    name="col121",
    ends={
        Property(name="xhtml_ColType123", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot122", type=xhtml_ColType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colgroup124: BinaryAssociation = BinaryAssociation(
    name="colgroup124",
    ends={
        Property(name="xhtml_ColgroupType126", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot125", type=xhtml_ColgroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dd127: BinaryAssociation = BinaryAssociation(
    name="dd127",
    ends={
        Property(name="xhtml_DdType129", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot128", type=xhtml_DdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn130: BinaryAssociation = BinaryAssociation(
    name="dfn130",
    ends={
        Property(name="xhtml_DfnType132", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot131", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote107: BinaryAssociation = BinaryAssociation(
    name="blockquote107",
    ends={
        Property(name="xhtml_BlockquoteType109", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot108", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br110: BinaryAssociation = BinaryAssociation(
    name="br110",
    ends={
        Property(name="xhtml_BrType112", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot111", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caption113: BinaryAssociation = BinaryAssociation(
    name="caption113",
    ends={
        Property(name="xhtml_CaptionType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot114", type=xhtml_CaptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite115: BinaryAssociation = BinaryAssociation(
    name="cite115",
    ends={
        Property(name="xhtml_CiteType117", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot116", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code118: BinaryAssociation = BinaryAssociation(
    name="code118",
    ends={
        Property(name="xhtml_CodeType120", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot119", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2148: BinaryAssociation = BinaryAssociation(
    name="h2148",
    ends={
        Property(name="xhtml_H2Type150", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot149", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3151: BinaryAssociation = BinaryAssociation(
    name="h3151",
    ends={
        Property(name="xhtml_H3Type153", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot152", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4154: BinaryAssociation = BinaryAssociation(
    name="h4154",
    ends={
        Property(name="xhtml_H4Type156", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot155", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5157: BinaryAssociation = BinaryAssociation(
    name="h5157",
    ends={
        Property(name="xhtml_H5Type159", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot158", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div133: BinaryAssociation = BinaryAssociation(
    name="div133",
    ends={
        Property(name="xhtml_DivType135", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot134", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl136: BinaryAssociation = BinaryAssociation(
    name="dl136",
    ends={
        Property(name="xhtml_DlType138", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot137", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dt139: BinaryAssociation = BinaryAssociation(
    name="dt139",
    ends={
        Property(name="xhtml_DtType141", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot140", type=xhtml_DtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em142: BinaryAssociation = BinaryAssociation(
    name="em142",
    ends={
        Property(name="xhtml_EmType144", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot143", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1145: BinaryAssociation = BinaryAssociation(
    name="h1145",
    ends={
        Property(name="xhtml_H1Type147", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot146", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i166: BinaryAssociation = BinaryAssociation(
    name="i166",
    ends={
        Property(name="xhtml_IType168", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot167", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img169: BinaryAssociation = BinaryAssociation(
    name="img169",
    ends={
        Property(name="xhtml_ImgType171", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot170", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd172: BinaryAssociation = BinaryAssociation(
    name="kbd172",
    ends={
        Property(name="xhtml_KbdType174", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot173", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li175: BinaryAssociation = BinaryAssociation(
    name="li175",
    ends={
        Property(name="xhtml_LiType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot176", type=xhtml_LiType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6160: BinaryAssociation = BinaryAssociation(
    name="h6160",
    ends={
        Property(name="xhtml_H6Type162", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot161", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr163: BinaryAssociation = BinaryAssociation(
    name="hr163",
    ends={
        Property(name="xhtml_HrType165", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot164", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp192: BinaryAssociation = BinaryAssociation(
    name="samp192",
    ends={
        Property(name="xhtml_SampType194", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot193", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small195: BinaryAssociation = BinaryAssociation(
    name="small195",
    ends={
        Property(name="xhtml_SmallType197", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot196", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span198: BinaryAssociation = BinaryAssociation(
    name="span198",
    ends={
        Property(name="xhtml_SpanType200", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot199", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong201: BinaryAssociation = BinaryAssociation(
    name="strong201",
    ends={
        Property(name="xhtml_StrongType203", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot202", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map177: BinaryAssociation = BinaryAssociation(
    name="map177",
    ends={
        Property(name="xhtml_MapType179", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot178", type=xhtml_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol180: BinaryAssociation = BinaryAssociation(
    name="ol180",
    ends={
        Property(name="xhtml_OlType182", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot181", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p183: BinaryAssociation = BinaryAssociation(
    name="p183",
    ends={
        Property(name="xhtml_PType185", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot184", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre186: BinaryAssociation = BinaryAssociation(
    name="pre186",
    ends={
        Property(name="xhtml_PreType188", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot187", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q189: BinaryAssociation = BinaryAssociation(
    name="q189",
    ends={
        Property(name="xhtml_QType191", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot190", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table210: BinaryAssociation = BinaryAssociation(
    name="table210",
    ends={
        Property(name="xhtml_TableType212", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot211", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tbody213: BinaryAssociation = BinaryAssociation(
    name="tbody213",
    ends={
        Property(name="xhtml_TbodyType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot214", type=xhtml_TbodyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
td215: BinaryAssociation = BinaryAssociation(
    name="td215",
    ends={
        Property(name="xhtml_TdType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot216", type=xhtml_TdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub204: BinaryAssociation = BinaryAssociation(
    name="sub204",
    ends={
        Property(name="xhtml_SubType206", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot205", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup207: BinaryAssociation = BinaryAssociation(
    name="sup207",
    ends={
        Property(name="xhtml_SupType209", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot208", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul228: BinaryAssociation = BinaryAssociation(
    name="ul228",
    ends={
        Property(name="xhtml_UlType230", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot229", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var231: BinaryAssociation = BinaryAssociation(
    name="var231",
    ends={
        Property(name="xhtml_VarType233", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot232", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tfoot217: BinaryAssociation = BinaryAssociation(
    name="tfoot217",
    ends={
        Property(name="xhtml_TfootType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot218", type=xhtml_TfootType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
th219: BinaryAssociation = BinaryAssociation(
    name="th219",
    ends={
        Property(name="xhtml_ThType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot220", type=xhtml_ThType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead221: BinaryAssociation = BinaryAssociation(
    name="thead221",
    ends={
        Property(name="xhtml_TheadType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot222", type=xhtml_TheadType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr223: BinaryAssociation = BinaryAssociation(
    name="tr223",
    ends={
        Property(name="xhtml_TrType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot224", type=xhtml_TrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt225: BinaryAssociation = BinaryAssociation(
    name="tt225",
    ends={
        Property(name="xhtml_TtType227", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot226", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5248: BinaryAssociation = BinaryAssociation(
    name="h5248",
    ends={
        Property(name="xhtml_H5Type250", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow249", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6251: BinaryAssociation = BinaryAssociation(
    name="h6251",
    ends={
        Property(name="xhtml_H6Type253", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow252", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div254: BinaryAssociation = BinaryAssociation(
    name="div254",
    ends={
        Property(name="xhtml_DivType256", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow255", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p234: BinaryAssociation = BinaryAssociation(
    name="p234",
    ends={
        Property(name="xhtml_PType235", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1236: BinaryAssociation = BinaryAssociation(
    name="h1236",
    ends={
        Property(name="xhtml_H1Type238", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow237", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2239: BinaryAssociation = BinaryAssociation(
    name="h2239",
    ends={
        Property(name="xhtml_H2Type241", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow240", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3242: BinaryAssociation = BinaryAssociation(
    name="h3242",
    ends={
        Property(name="xhtml_H3Type244", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow243", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4245: BinaryAssociation = BinaryAssociation(
    name="h4245",
    ends={
        Property(name="xhtml_H4Type247", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow246", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr269: BinaryAssociation = BinaryAssociation(
    name="hr269",
    ends={
        Property(name="xhtml_HrType271", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow270", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote272: BinaryAssociation = BinaryAssociation(
    name="blockquote272",
    ends={
        Property(name="xhtml_BlockquoteType274", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow273", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address275: BinaryAssociation = BinaryAssociation(
    name="address275",
    ends={
        Property(name="xhtml_AddressType277", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow276", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul257: BinaryAssociation = BinaryAssociation(
    name="ul257",
    ends={
        Property(name="xhtml_UlType259", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow258", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol260: BinaryAssociation = BinaryAssociation(
    name="ol260",
    ends={
        Property(name="xhtml_OlType262", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow261", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl263: BinaryAssociation = BinaryAssociation(
    name="dl263",
    ends={
        Property(name="xhtml_DlType265", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow264", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre266: BinaryAssociation = BinaryAssociation(
    name="pre266",
    ends={
        Property(name="xhtml_PreType268", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow267", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img296: BinaryAssociation = BinaryAssociation(
    name="img296",
    ends={
        Property(name="xhtml_ImgType298", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow297", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt299: BinaryAssociation = BinaryAssociation(
    name="tt299",
    ends={
        Property(name="xhtml_TtType301", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow300", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i302: BinaryAssociation = BinaryAssociation(
    name="i302",
    ends={
        Property(name="xhtml_IType304", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow303", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table278: BinaryAssociation = BinaryAssociation(
    name="table278",
    ends={
        Property(name="xhtml_TableType280", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow279", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a281: BinaryAssociation = BinaryAssociation(
    name="a281",
    ends={
        Property(name="xhtml_AType283", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow282", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br284: BinaryAssociation = BinaryAssociation(
    name="br284",
    ends={
        Property(name="xhtml_BrType286", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow285", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span287: BinaryAssociation = BinaryAssociation(
    name="span287",
    ends={
        Property(name="xhtml_SpanType289", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow288", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdo290: BinaryAssociation = BinaryAssociation(
    name="bdo290",
    ends={
        Property(name="xhtml_BdoType292", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow291", type=xhtml_BdoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map293: BinaryAssociation = BinaryAssociation(
    name="map293",
    ends={
        Property(name="xhtml_MapType295", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow294", type=xhtml_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn320: BinaryAssociation = BinaryAssociation(
    name="dfn320",
    ends={
        Property(name="xhtml_DfnType322", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow321", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code323: BinaryAssociation = BinaryAssociation(
    name="code323",
    ends={
        Property(name="xhtml_CodeType325", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow324", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q326: BinaryAssociation = BinaryAssociation(
    name="q326",
    ends={
        Property(name="xhtml_QType328", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow327", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b305: BinaryAssociation = BinaryAssociation(
    name="b305",
    ends={
        Property(name="xhtml_BType307", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow306", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big308: BinaryAssociation = BinaryAssociation(
    name="big308",
    ends={
        Property(name="xhtml_BigType310", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow309", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small311: BinaryAssociation = BinaryAssociation(
    name="small311",
    ends={
        Property(name="xhtml_SmallType313", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow312", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em314: BinaryAssociation = BinaryAssociation(
    name="em314",
    ends={
        Property(name="xhtml_EmType316", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow315", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong317: BinaryAssociation = BinaryAssociation(
    name="strong317",
    ends={
        Property(name="xhtml_StrongType319", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow318", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym344: BinaryAssociation = BinaryAssociation(
    name="acronym344",
    ends={
        Property(name="xhtml_AcronymType346", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow345", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub347: BinaryAssociation = BinaryAssociation(
    name="sub347",
    ends={
        Property(name="xhtml_SubType349", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow348", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup350: BinaryAssociation = BinaryAssociation(
    name="sup350",
    ends={
        Property(name="xhtml_SupType352", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow351", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp329: BinaryAssociation = BinaryAssociation(
    name="samp329",
    ends={
        Property(name="xhtml_SampType331", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow330", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd332: BinaryAssociation = BinaryAssociation(
    name="kbd332",
    ends={
        Property(name="xhtml_KbdType334", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow333", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var335: BinaryAssociation = BinaryAssociation(
    name="var335",
    ends={
        Property(name="xhtml_VarType337", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow336", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite338: BinaryAssociation = BinaryAssociation(
    name="cite338",
    ends={
        Property(name="xhtml_CiteType340", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow339", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr341: BinaryAssociation = BinaryAssociation(
    name="abbr341",
    ends={
        Property(name="xhtml_AbbrType343", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow342", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a353: BinaryAssociation = BinaryAssociation(
    name="a353",
    ends={
        Property(name="xhtml_AType354", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br355: BinaryAssociation = BinaryAssociation(
    name="br355",
    ends={
        Property(name="xhtml_BrType357", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline356", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img367: BinaryAssociation = BinaryAssociation(
    name="img367",
    ends={
        Property(name="xhtml_ImgType369", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline368", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt370: BinaryAssociation = BinaryAssociation(
    name="tt370",
    ends={
        Property(name="xhtml_TtType372", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline371", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i373: BinaryAssociation = BinaryAssociation(
    name="i373",
    ends={
        Property(name="xhtml_IType375", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline374", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b376: BinaryAssociation = BinaryAssociation(
    name="b376",
    ends={
        Property(name="xhtml_BType378", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline377", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span358: BinaryAssociation = BinaryAssociation(
    name="span358",
    ends={
        Property(name="xhtml_SpanType360", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline359", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdo361: BinaryAssociation = BinaryAssociation(
    name="bdo361",
    ends={
        Property(name="xhtml_BdoType363", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline362", type=xhtml_BdoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map364: BinaryAssociation = BinaryAssociation(
    name="map364",
    ends={
        Property(name="xhtml_MapType366", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline365", type=xhtml_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn391: BinaryAssociation = BinaryAssociation(
    name="dfn391",
    ends={
        Property(name="xhtml_DfnType393", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline392", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big379: BinaryAssociation = BinaryAssociation(
    name="big379",
    ends={
        Property(name="xhtml_BigType381", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline380", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code394: BinaryAssociation = BinaryAssociation(
    name="code394",
    ends={
        Property(name="xhtml_CodeType396", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline395", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small382: BinaryAssociation = BinaryAssociation(
    name="small382",
    ends={
        Property(name="xhtml_SmallType384", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline383", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q397: BinaryAssociation = BinaryAssociation(
    name="q397",
    ends={
        Property(name="xhtml_QType399", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline398", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em385: BinaryAssociation = BinaryAssociation(
    name="em385",
    ends={
        Property(name="xhtml_EmType387", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline386", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp400: BinaryAssociation = BinaryAssociation(
    name="samp400",
    ends={
        Property(name="xhtml_SampType402", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline401", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong388: BinaryAssociation = BinaryAssociation(
    name="strong388",
    ends={
        Property(name="xhtml_StrongType390", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline389", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd403: BinaryAssociation = BinaryAssociation(
    name="kbd403",
    ends={
        Property(name="xhtml_KbdType405", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline404", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var406: BinaryAssociation = BinaryAssociation(
    name="var406",
    ends={
        Property(name="xhtml_VarType408", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline407", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite409: BinaryAssociation = BinaryAssociation(
    name="cite409",
    ends={
        Property(name="xhtml_CiteType411", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline410", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr412: BinaryAssociation = BinaryAssociation(
    name="abbr412",
    ends={
        Property(name="xhtml_AbbrType414", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline413", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym415: BinaryAssociation = BinaryAssociation(
    name="acronym415",
    ends={
        Property(name="xhtml_AcronymType417", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline416", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub418: BinaryAssociation = BinaryAssociation(
    name="sub418",
    ends={
        Property(name="xhtml_SubType420", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline419", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup421: BinaryAssociation = BinaryAssociation(
    name="sup421",
    ends={
        Property(name="xhtml_SupType423", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline422", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p424: BinaryAssociation = BinaryAssociation(
    name="p424",
    ends={
        Property(name="xhtml_PType426", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType425", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1427: BinaryAssociation = BinaryAssociation(
    name="h1427",
    ends={
        Property(name="xhtml_H1Type429", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType428", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2430: BinaryAssociation = BinaryAssociation(
    name="h2430",
    ends={
        Property(name="xhtml_H2Type432", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType431", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3433: BinaryAssociation = BinaryAssociation(
    name="h3433",
    ends={
        Property(name="xhtml_H3Type435", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType434", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4436: BinaryAssociation = BinaryAssociation(
    name="h4436",
    ends={
        Property(name="xhtml_H4Type438", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType437", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5439: BinaryAssociation = BinaryAssociation(
    name="h5439",
    ends={
        Property(name="xhtml_H5Type441", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType440", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6442: BinaryAssociation = BinaryAssociation(
    name="h6442",
    ends={
        Property(name="xhtml_H6Type444", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType443", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div445: BinaryAssociation = BinaryAssociation(
    name="div445",
    ends={
        Property(name="xhtml_DivType447", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType446", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul448: BinaryAssociation = BinaryAssociation(
    name="ul448",
    ends={
        Property(name="xhtml_UlType450", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType449", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol451: BinaryAssociation = BinaryAssociation(
    name="ol451",
    ends={
        Property(name="xhtml_OlType453", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType452", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl454: BinaryAssociation = BinaryAssociation(
    name="dl454",
    ends={
        Property(name="xhtml_DlType456", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType455", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre457: BinaryAssociation = BinaryAssociation(
    name="pre457",
    ends={
        Property(name="xhtml_PreType459", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType458", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr460: BinaryAssociation = BinaryAssociation(
    name="hr460",
    ends={
        Property(name="xhtml_HrType462", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType461", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote463: BinaryAssociation = BinaryAssociation(
    name="blockquote463",
    ends={
        Property(name="xhtml_BlockquoteType465", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType464", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address466: BinaryAssociation = BinaryAssociation(
    name="address466",
    ends={
        Property(name="xhtml_AddressType468", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType467", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table469: BinaryAssociation = BinaryAssociation(
    name="table469",
    ends={
        Property(name="xhtml_TableType471", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType470", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
area472: BinaryAssociation = BinaryAssociation(
    name="area472",
    ends={
        Property(name="xhtml_AreaType474", type=xhtml_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_MapType473", type=xhtml_AreaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li475: BinaryAssociation = BinaryAssociation(
    name="li475",
    ends={
        Property(name="xhtml_LiType477", type=xhtml_OlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_OlType476", type=xhtml_LiType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tt480: BinaryAssociation = BinaryAssociation(
    name="tt480",
    ends={
        Property(name="xhtml_TtType482", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent481", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i483: BinaryAssociation = BinaryAssociation(
    name="i483",
    ends={
        Property(name="xhtml_IType485", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent484", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b486: BinaryAssociation = BinaryAssociation(
    name="b486",
    ends={
        Property(name="xhtml_BType488", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent487", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big489: BinaryAssociation = BinaryAssociation(
    name="big489",
    ends={
        Property(name="xhtml_BigType491", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent490", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small492: BinaryAssociation = BinaryAssociation(
    name="small492",
    ends={
        Property(name="xhtml_SmallType494", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent493", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em495: BinaryAssociation = BinaryAssociation(
    name="em495",
    ends={
        Property(name="xhtml_EmType497", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent496", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong498: BinaryAssociation = BinaryAssociation(
    name="strong498",
    ends={
        Property(name="xhtml_StrongType500", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent499", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn501: BinaryAssociation = BinaryAssociation(
    name="dfn501",
    ends={
        Property(name="xhtml_DfnType503", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent502", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a478: BinaryAssociation = BinaryAssociation(
    name="a478",
    ends={
        Property(name="xhtml_AType479", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q507: BinaryAssociation = BinaryAssociation(
    name="q507",
    ends={
        Property(name="xhtml_QType509", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent508", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp510: BinaryAssociation = BinaryAssociation(
    name="samp510",
    ends={
        Property(name="xhtml_SampType512", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent511", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd513: BinaryAssociation = BinaryAssociation(
    name="kbd513",
    ends={
        Property(name="xhtml_KbdType515", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent514", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var516: BinaryAssociation = BinaryAssociation(
    name="var516",
    ends={
        Property(name="xhtml_VarType518", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent517", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite519: BinaryAssociation = BinaryAssociation(
    name="cite519",
    ends={
        Property(name="xhtml_CiteType521", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent520", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr522: BinaryAssociation = BinaryAssociation(
    name="abbr522",
    ends={
        Property(name="xhtml_AbbrType524", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent523", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym525: BinaryAssociation = BinaryAssociation(
    name="acronym525",
    ends={
        Property(name="xhtml_AcronymType527", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent526", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub528: BinaryAssociation = BinaryAssociation(
    name="sub528",
    ends={
        Property(name="xhtml_SubType530", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent529", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code504: BinaryAssociation = BinaryAssociation(
    name="code504",
    ends={
        Property(name="xhtml_CodeType506", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent505", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup531: BinaryAssociation = BinaryAssociation(
    name="sup531",
    ends={
        Property(name="xhtml_SupType533", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent532", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br534: BinaryAssociation = BinaryAssociation(
    name="br534",
    ends={
        Property(name="xhtml_BrType536", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent535", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span537: BinaryAssociation = BinaryAssociation(
    name="span537",
    ends={
        Property(name="xhtml_SpanType539", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent538", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdo540: BinaryAssociation = BinaryAssociation(
    name="bdo540",
    ends={
        Property(name="xhtml_BdoType542", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent541", type=xhtml_BdoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map543: BinaryAssociation = BinaryAssociation(
    name="map543",
    ends={
        Property(name="xhtml_MapType545", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent544", type=xhtml_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caption546: BinaryAssociation = BinaryAssociation(
    name="caption546",
    ends={
        Property(name="xhtml_CaptionType548", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType547", type=xhtml_CaptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col549: BinaryAssociation = BinaryAssociation(
    name="col549",
    ends={
        Property(name="xhtml_ColType551", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType550", type=xhtml_ColType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colgroup552: BinaryAssociation = BinaryAssociation(
    name="colgroup552",
    ends={
        Property(name="xhtml_ColgroupType554", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType553", type=xhtml_ColgroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead555: BinaryAssociation = BinaryAssociation(
    name="thead555",
    ends={
        Property(name="xhtml_TheadType557", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType556", type=xhtml_TheadType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tfoot558: BinaryAssociation = BinaryAssociation(
    name="tfoot558",
    ends={
        Property(name="xhtml_TfootType560", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType559", type=xhtml_TfootType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbody561: BinaryAssociation = BinaryAssociation(
    name="tbody561",
    ends={
        Property(name="xhtml_TbodyType563", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType562", type=xhtml_TbodyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr564: BinaryAssociation = BinaryAssociation(
    name="tr564",
    ends={
        Property(name="xhtml_TrType566", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType565", type=xhtml_TrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr567: BinaryAssociation = BinaryAssociation(
    name="tr567",
    ends={
        Property(name="xhtml_TrType569", type=xhtml_TbodyType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TbodyType568", type=xhtml_TrType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr570: BinaryAssociation = BinaryAssociation(
    name="tr570",
    ends={
        Property(name="xhtml_TrType572", type=xhtml_TfootType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TfootType571", type=xhtml_TrType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr573: BinaryAssociation = BinaryAssociation(
    name="tr573",
    ends={
        Property(name="xhtml_TrType575", type=xhtml_TheadType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TheadType574", type=xhtml_TrType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
th576: BinaryAssociation = BinaryAssociation(
    name="th576",
    ends={
        Property(name="xhtml_ThType578", type=xhtml_TrType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TrType577", type=xhtml_ThType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
td579: BinaryAssociation = BinaryAssociation(
    name="td579",
    ends={
        Property(name="xhtml_TdType581", type=xhtml_TrType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TrType580", type=xhtml_TdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li582: BinaryAssociation = BinaryAssociation(
    name="li582",
    ends={
        Property(name="xhtml_LiType584", type=xhtml_UlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_UlType583", type=xhtml_LiType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_xhtml_AbbrType_Inline = Generalization(general=Inline, specific=xhtml_AbbrType)
gen_xhtml_AddressType_Inline = Generalization(general=Inline, specific=xhtml_AddressType)
gen_xhtml_AcronymType_Inline = Generalization(general=Inline, specific=xhtml_AcronymType)
gen_xhtml_AType_AContent = Generalization(general=AContent, specific=xhtml_AType)
gen_xhtml_BigType_Inline = Generalization(general=Inline, specific=xhtml_BigType)
gen_xhtml_BdoType_Inline = Generalization(general=Inline, specific=xhtml_BdoType)
gen_xhtml_BType_Inline = Generalization(general=Inline, specific=xhtml_BType)
gen_xhtml_BlockquoteType_Block = Generalization(general=Block, specific=xhtml_BlockquoteType)
gen_xhtml_CaptionType_Inline = Generalization(general=Inline, specific=xhtml_CaptionType)
gen_xhtml_CiteType_Inline = Generalization(general=Inline, specific=xhtml_CiteType)
gen_xhtml_CodeType_Inline = Generalization(general=Inline, specific=xhtml_CodeType)
gen_xhtml_DdType_Flow = Generalization(general=Flow, specific=xhtml_DdType)
gen_xhtml_DivType_Flow = Generalization(general=Flow, specific=xhtml_DivType)
gen_xhtml_DfnType_Inline = Generalization(general=Inline, specific=xhtml_DfnType)
gen_xhtml_DtType_Inline = Generalization(general=Inline, specific=xhtml_DtType)
gen_xhtml_EmType_Inline = Generalization(general=Inline, specific=xhtml_EmType)
gen_xhtml_H1Type_Inline = Generalization(general=Inline, specific=xhtml_H1Type)
gen_xhtml_H3Type_Inline = Generalization(general=Inline, specific=xhtml_H3Type)
gen_xhtml_H2Type_Inline = Generalization(general=Inline, specific=xhtml_H2Type)
gen_xhtml_H5Type_Inline = Generalization(general=Inline, specific=xhtml_H5Type)
gen_xhtml_H4Type_Inline = Generalization(general=Inline, specific=xhtml_H4Type)
gen_xhtml_H6Type_Inline = Generalization(general=Inline, specific=xhtml_H6Type)
gen_xhtml_IType_Inline = Generalization(general=Inline, specific=xhtml_IType)
gen_xhtml_KbdType_Inline = Generalization(general=Inline, specific=xhtml_KbdType)
gen_xhtml_LiType_Flow = Generalization(general=Flow, specific=xhtml_LiType)
gen_xhtml_PreType_PreContent = Generalization(general=PreContent, specific=xhtml_PreType)
gen_xhtml_PType_Inline = Generalization(general=Inline, specific=xhtml_PType)
gen_xhtml_QType_Inline = Generalization(general=Inline, specific=xhtml_QType)
gen_xhtml_SampType_Inline = Generalization(general=Inline, specific=xhtml_SampType)
gen_xhtml_SmallType_Inline = Generalization(general=Inline, specific=xhtml_SmallType)
gen_xhtml_SpanType_Inline = Generalization(general=Inline, specific=xhtml_SpanType)
gen_xhtml_StrongType_Inline = Generalization(general=Inline, specific=xhtml_StrongType)
gen_xhtml_SubType_Inline = Generalization(general=Inline, specific=xhtml_SubType)
gen_xhtml_SupType_Inline = Generalization(general=Inline, specific=xhtml_SupType)
gen_xhtml_TdType_Flow = Generalization(general=Flow, specific=xhtml_TdType)
gen_xhtml_ThType_Flow = Generalization(general=Flow, specific=xhtml_ThType)
gen_xhtml_TtType_Inline = Generalization(general=Inline, specific=xhtml_TtType)
gen_xhtml_VarType_Inline = Generalization(general=Inline, specific=xhtml_VarType)

# Domain Model
domain_model = DomainModel(
    name="xhtml",
    types={xhtml_AbbrType, xhtml_BrType, xhtml_SpanType, xhtml_BdoType, Inline, xhtml_AContent, xhtml_BigType, xhtml_SmallType, xhtml_EmType, xhtml_StrongType, xhtml_MapType, xhtml_ImgType, xhtml_TtType, xhtml_IType, xhtml_BType, xhtml_VarType, xhtml_CiteType, xhtml_DfnType, xhtml_CodeType, xhtml_QType, xhtml_SampType, xhtml_KbdType, xhtml_AddressType, xhtml_AcronymType, xhtml_SubType, xhtml_SupType, xhtml_AreaType, xhtml_AType, AContent, xhtml_H2Type, xhtml_H3Type, xhtml_H4Type, xhtml_H5Type, xhtml_Block, xhtml_PType, xhtml_H1Type, xhtml_H6Type, xhtml_DivType, xhtml_UlType, xhtml_OlType, xhtml_HrType, xhtml_BlockquoteType, xhtml_DlType, xhtml_PreType, xhtml_TableType, Block, xhtml_CaptionType, xhtml_ColgroupType, xhtml_ColType, xhtml_DdType, Flow, xhtml_DocumentRoot, xhtml_DtType, xhtml_EStringToStringMapEntry, xhtml_LiType, xhtml_TbodyType, xhtml_TdType, xhtml_TfootType, xhtml_ThType, xhtml_TheadType, xhtml_TrType, xhtml_Flow, xhtml_Inline, xhtml_PreContent, PreContent, AlignType, DirType, DirType1, IsmapType, NohrefType, Scope, Shape, TFrame, TRules, ValignType},
    associations={br0, span1, bdo3, big15, small17, em19, strong21, map5, img7, tt9, i11, b13, var33, cite35, abbr37, dfn23, code25, q27, samp29, kbd31, acronym39, sub41, sup43, h248, h350, h452, p45, h146, h554, h656, div58, ul60, ol62, hr68, blockquote70, address72, dl64, pre66, table74, col76, dt77, dd79, area96, b98, bdo101, big104, xMLNSPrefixMap81, xSISchemaLocation82, a85, abbr87, acronym90, address93, col121, colgroup124, dd127, dfn130, blockquote107, br110, caption113, cite115, code118, h2148, h3151, h4154, h5157, div133, dl136, dt139, em142, h1145, i166, img169, kbd172, li175, h6160, hr163, samp192, small195, span198, strong201, map177, ol180, p183, pre186, q189, table210, tbody213, td215, sub204, sup207, ul228, var231, tfoot217, th219, thead221, tr223, tt225, h5248, h6251, div254, p234, h1236, h2239, h3242, h4245, hr269, blockquote272, address275, ul257, ol260, dl263, pre266, img296, tt299, i302, table278, a281, br284, span287, bdo290, map293, dfn320, code323, q326, b305, big308, small311, em314, strong317, acronym344, sub347, sup350, samp329, kbd332, var335, cite338, abbr341, a353, br355, img367, tt370, i373, b376, span358, bdo361, map364, dfn391, big379, code394, small382, q397, em385, samp400, strong388, kbd403, var406, cite409, abbr412, acronym415, sub418, sup421, p424, h1427, h2430, h3433, h4436, h5439, h6442, div445, ul448, ol451, dl454, pre457, hr460, blockquote463, address466, table469, area472, li475, tt480, i483, b486, big489, small492, em495, strong498, dfn501, a478, q507, samp510, kbd513, var516, cite519, abbr522, acronym525, sub528, code504, sup531, br534, span537, bdo540, map543, caption546, col549, colgroup552, thead555, tfoot558, tbody561, tr564, tr567, tr570, tr573, th576, td579, li582},
    generalizations={gen_xhtml_AbbrType_Inline, gen_xhtml_AddressType_Inline, gen_xhtml_AcronymType_Inline, gen_xhtml_AType_AContent, gen_xhtml_BigType_Inline, gen_xhtml_BdoType_Inline, gen_xhtml_BType_Inline, gen_xhtml_BlockquoteType_Block, gen_xhtml_CaptionType_Inline, gen_xhtml_CiteType_Inline, gen_xhtml_CodeType_Inline, gen_xhtml_DdType_Flow, gen_xhtml_DivType_Flow, gen_xhtml_DfnType_Inline, gen_xhtml_DtType_Inline, gen_xhtml_EmType_Inline, gen_xhtml_H1Type_Inline, gen_xhtml_H3Type_Inline, gen_xhtml_H2Type_Inline, gen_xhtml_H5Type_Inline, gen_xhtml_H4Type_Inline, gen_xhtml_H6Type_Inline, gen_xhtml_IType_Inline, gen_xhtml_KbdType_Inline, gen_xhtml_LiType_Flow, gen_xhtml_PreType_PreContent, gen_xhtml_PType_Inline, gen_xhtml_QType_Inline, gen_xhtml_SampType_Inline, gen_xhtml_SmallType_Inline, gen_xhtml_SpanType_Inline, gen_xhtml_StrongType_Inline, gen_xhtml_SubType_Inline, gen_xhtml_SupType_Inline, gen_xhtml_TdType_Flow, gen_xhtml_ThType_Flow, gen_xhtml_TtType_Inline, gen_xhtml_VarType_Inline},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)