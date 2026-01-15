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

DeclareType: Enumeration = Enumeration(
    name="DeclareType",
    literals={
            EnumerationLiteral(name="declare")
    }
)

IsmapType: Enumeration = Enumeration(
    name="IsmapType",
    literals={
            EnumerationLiteral(name="ismap")
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

ValignType: Enumeration = Enumeration(
    name="ValignType",
    literals={
            EnumerationLiteral(name="top"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="baseline")
    }
)

ValuetypeType: Enumeration = Enumeration(
    name="ValuetypeType",
    literals={
            EnumerationLiteral(name="data"),
			EnumerationLiteral(name="ref"),
			EnumerationLiteral(name="object")
    }
)

# Classes
xhtml_AbbrType = Class(name="xhtml::AbbrType")
Inline = Class(name="Inline")
xhtml_ObjectType = Class(name="xhtml::ObjectType")
xhtml_ImgType = Class(name="xhtml::ImgType")
xhtml_TtType = Class(name="xhtml::TtType")
xhtml_AContent = Class(name="xhtml::AContent")
xhtml_BrType = Class(name="xhtml::BrType")
xhtml_SpanType = Class(name="xhtml::SpanType")
xhtml_StrikeType = Class(name="xhtml::StrikeType")
xhtml_EmType = Class(name="xhtml::EmType")
xhtml_StrongType = Class(name="xhtml::StrongType")
xhtml_IType = Class(name="xhtml::IType")
xhtml_BType = Class(name="xhtml::BType")
xhtml_BigType = Class(name="xhtml::BigType")
xhtml_SmallType = Class(name="xhtml::SmallType")
xhtml_UType = Class(name="xhtml::UType")
xhtml_KbdType = Class(name="xhtml::KbdType")
xhtml_VarType = Class(name="xhtml::VarType")
xhtml_CiteType = Class(name="xhtml::CiteType")
xhtml_DfnType = Class(name="xhtml::DfnType")
xhtml_CodeType = Class(name="xhtml::CodeType")
xhtml_QType = Class(name="xhtml::QType")
xhtml_SampType = Class(name="xhtml::SampType")
xhtml_SupType = Class(name="xhtml::SupType")
xhtml_InsType = Class(name="xhtml::InsType")
xhtml_AcronymType = Class(name="xhtml::AcronymType")
xhtml_SubType = Class(name="xhtml::SubType")
xhtml_DelType = Class(name="xhtml::DelType")
xhtml_AddressType = Class(name="xhtml::AddressType")
xhtml_AType = Class(name="xhtml::AType")
AContent = Class(name="AContent")
xhtml_H2Type = Class(name="xhtml::H2Type")
xhtml_H3Type = Class(name="xhtml::H3Type")
xhtml_H4Type = Class(name="xhtml::H4Type")
xhtml_H5Type = Class(name="xhtml::H5Type")
xhtml_H6Type = Class(name="xhtml::H6Type")
xhtml_Block = Class(name="xhtml::Block")
xhtml_PType = Class(name="xhtml::PType")
xhtml_H1Type = Class(name="xhtml::H1Type")
xhtml_DlType = Class(name="xhtml::DlType")
xhtml_PreType = Class(name="xhtml::PreType")
xhtml_HrType = Class(name="xhtml::HrType")
xhtml_BlockquoteType = Class(name="xhtml::BlockquoteType")
xhtml_TableType = Class(name="xhtml::TableType")
xhtml_DivType = Class(name="xhtml::DivType")
xhtml_UlType = Class(name="xhtml::UlType")
xhtml_OlType = Class(name="xhtml::OlType")
Block = Class(name="Block")
xhtml_BodyType = Class(name="xhtml::BodyType")
xhtml_CaptionType = Class(name="xhtml::CaptionType")
xhtml_ColgroupType = Class(name="xhtml::ColgroupType")
xhtml_ColType = Class(name="xhtml::ColType")
xhtml_DdType = Class(name="xhtml::DdType")
Flow = Class(name="Flow")
xhtml_DocumentRoot = Class(name="xhtml::DocumentRoot")
xhtml_EStringToStringMapEntry = Class(name="xhtml::EStringToStringMapEntry")
xhtml_DtType = Class(name="xhtml::DtType")
xhtml_LiType = Class(name="xhtml::LiType")
xhtml_HtmlType = Class(name="xhtml::HtmlType")
xhtml_ParamType = Class(name="xhtml::ParamType")
xhtml_TfootType = Class(name="xhtml::TfootType")
xhtml_ThType = Class(name="xhtml::ThType")
xhtml_TheadType = Class(name="xhtml::TheadType")
xhtml_TrType = Class(name="xhtml::TrType")
xhtml_TbodyType = Class(name="xhtml::TbodyType")
xhtml_TdType = Class(name="xhtml::TdType")
xhtml_Flow = Class(name="xhtml::Flow")
xhtml_FormContent = Class(name="xhtml::FormContent")
xhtml_Inline = Class(name="xhtml::Inline")
xhtml_PreContent = Class(name="xhtml::PreContent")
PreContent = Class(name="PreContent")

# xhtml_AbbrType class attributes and methods
xhtml_AbbrType_class: Property = Property(name="class", type=StringType)
xhtml_AbbrType_id: Property = Property(name="id", type=StringType)
xhtml_AbbrType_style: Property = Property(name="style", type=StringType)
xhtml_AbbrType_title: Property = Property(name="title", type=StringType)
xhtml_AbbrType.attributes={xhtml_AbbrType_title, xhtml_AbbrType_class, xhtml_AbbrType_style, xhtml_AbbrType_id}

# Inline class attributes and methods

# xhtml_ObjectType class attributes and methods
xhtml_ObjectType_mixed: Property = Property(name="mixed", type=StringType)
xhtml_ObjectType_group: Property = Property(name="group", type=StringType)
xhtml_ObjectType_archive: Property = Property(name="archive", type=StringType)
xhtml_ObjectType_class: Property = Property(name="class", type=StringType)
xhtml_ObjectType_classid: Property = Property(name="classid", type=StringType)
xhtml_ObjectType_id: Property = Property(name="id", type=StringType)
xhtml_ObjectType_name: Property = Property(name="name", type=StringType)
xhtml_ObjectType_standby: Property = Property(name="standby", type=StringType)
xhtml_ObjectType_style: Property = Property(name="style", type=StringType)
xhtml_ObjectType_tabindex: Property = Property(name="tabindex", type=StringType)
xhtml_ObjectType_title: Property = Property(name="title", type=StringType)
xhtml_ObjectType_type: Property = Property(name="type", type=StringType)
xhtml_ObjectType_usemap: Property = Property(name="usemap", type=StringType)
xhtml_ObjectType_width: Property = Property(name="width", type=StringType)
xhtml_ObjectType_codebase: Property = Property(name="codebase", type=StringType)
xhtml_ObjectType_codetype: Property = Property(name="codetype", type=StringType)
xhtml_ObjectType_data: Property = Property(name="data", type=StringType)
xhtml_ObjectType_declare: Property = Property(name="declare", type=StringType)
xhtml_ObjectType_height: Property = Property(name="height", type=StringType)
xhtml_ObjectType.attributes={xhtml_ObjectType_standby, xhtml_ObjectType_group, xhtml_ObjectType_declare, xhtml_ObjectType_tabindex, xhtml_ObjectType_style, xhtml_ObjectType_codetype, xhtml_ObjectType_title, xhtml_ObjectType_height, xhtml_ObjectType_codebase, xhtml_ObjectType_usemap, xhtml_ObjectType_id, xhtml_ObjectType_type, xhtml_ObjectType_class, xhtml_ObjectType_mixed, xhtml_ObjectType_data, xhtml_ObjectType_name, xhtml_ObjectType_width, xhtml_ObjectType_classid, xhtml_ObjectType_archive}

# xhtml_ImgType class attributes and methods
xhtml_ImgType_style: Property = Property(name="style", type=StringType)
xhtml_ImgType_title: Property = Property(name="title", type=StringType)
xhtml_ImgType_usemap: Property = Property(name="usemap", type=StringType)
xhtml_ImgType_width: Property = Property(name="width", type=StringType)
xhtml_ImgType_alt: Property = Property(name="alt", type=StringType)
xhtml_ImgType_class: Property = Property(name="class", type=StringType)
xhtml_ImgType_height: Property = Property(name="height", type=StringType)
xhtml_ImgType_id: Property = Property(name="id", type=StringType)
xhtml_ImgType_ismap: Property = Property(name="ismap", type=StringType)
xhtml_ImgType_longdesc: Property = Property(name="longdesc", type=StringType)
xhtml_ImgType_src: Property = Property(name="src", type=StringType)
xhtml_ImgType.attributes={xhtml_ImgType_usemap, xhtml_ImgType_width, xhtml_ImgType_src, xhtml_ImgType_style, xhtml_ImgType_title, xhtml_ImgType_id, xhtml_ImgType_height, xhtml_ImgType_longdesc, xhtml_ImgType_class, xhtml_ImgType_alt, xhtml_ImgType_ismap}

# xhtml_TtType class attributes and methods
xhtml_TtType_id: Property = Property(name="id", type=StringType)
xhtml_TtType_style: Property = Property(name="style", type=StringType)
xhtml_TtType_class: Property = Property(name="class", type=StringType)
xhtml_TtType_title: Property = Property(name="title", type=StringType)
xhtml_TtType.attributes={xhtml_TtType_title, xhtml_TtType_style, xhtml_TtType_id, xhtml_TtType_class}

# xhtml_AContent class attributes and methods
xhtml_AContent_mixed: Property = Property(name="mixed", type=StringType)
xhtml_AContent_group: Property = Property(name="group", type=StringType)
xhtml_AContent.attributes={xhtml_AContent_group, xhtml_AContent_mixed}

# xhtml_BrType class attributes and methods
xhtml_BrType_class: Property = Property(name="class", type=StringType)
xhtml_BrType_id: Property = Property(name="id", type=StringType)
xhtml_BrType_style: Property = Property(name="style", type=StringType)
xhtml_BrType_title: Property = Property(name="title", type=StringType)
xhtml_BrType.attributes={xhtml_BrType_style, xhtml_BrType_class, xhtml_BrType_title, xhtml_BrType_id}

# xhtml_SpanType class attributes and methods
xhtml_SpanType_class: Property = Property(name="class", type=StringType)
xhtml_SpanType_id: Property = Property(name="id", type=StringType)
xhtml_SpanType_style: Property = Property(name="style", type=StringType)
xhtml_SpanType_title: Property = Property(name="title", type=StringType)
xhtml_SpanType.attributes={xhtml_SpanType_style, xhtml_SpanType_id, xhtml_SpanType_class, xhtml_SpanType_title}

# xhtml_StrikeType class attributes and methods
xhtml_StrikeType_class: Property = Property(name="class", type=StringType)
xhtml_StrikeType_id: Property = Property(name="id", type=StringType)
xhtml_StrikeType_style: Property = Property(name="style", type=StringType)
xhtml_StrikeType_title: Property = Property(name="title", type=StringType)
xhtml_StrikeType.attributes={xhtml_StrikeType_title, xhtml_StrikeType_class, xhtml_StrikeType_style, xhtml_StrikeType_id}

# xhtml_EmType class attributes and methods
xhtml_EmType_class: Property = Property(name="class", type=StringType)
xhtml_EmType_id: Property = Property(name="id", type=StringType)
xhtml_EmType_style: Property = Property(name="style", type=StringType)
xhtml_EmType_title: Property = Property(name="title", type=StringType)
xhtml_EmType.attributes={xhtml_EmType_title, xhtml_EmType_style, xhtml_EmType_id, xhtml_EmType_class}

# xhtml_StrongType class attributes and methods
xhtml_StrongType_class: Property = Property(name="class", type=StringType)
xhtml_StrongType_id: Property = Property(name="id", type=StringType)
xhtml_StrongType_style: Property = Property(name="style", type=StringType)
xhtml_StrongType_title: Property = Property(name="title", type=StringType)
xhtml_StrongType.attributes={xhtml_StrongType_class, xhtml_StrongType_title, xhtml_StrongType_id, xhtml_StrongType_style}

# xhtml_IType class attributes and methods
xhtml_IType_class: Property = Property(name="class", type=StringType)
xhtml_IType_id: Property = Property(name="id", type=StringType)
xhtml_IType_style: Property = Property(name="style", type=StringType)
xhtml_IType_title: Property = Property(name="title", type=StringType)
xhtml_IType.attributes={xhtml_IType_style, xhtml_IType_class, xhtml_IType_id, xhtml_IType_title}

# xhtml_BType class attributes and methods
xhtml_BType_title: Property = Property(name="title", type=StringType)
xhtml_BType_class: Property = Property(name="class", type=StringType)
xhtml_BType_id: Property = Property(name="id", type=StringType)
xhtml_BType_style: Property = Property(name="style", type=StringType)
xhtml_BType.attributes={xhtml_BType_title, xhtml_BType_id, xhtml_BType_class, xhtml_BType_style}

# xhtml_BigType class attributes and methods
xhtml_BigType_class: Property = Property(name="class", type=StringType)
xhtml_BigType_id: Property = Property(name="id", type=StringType)
xhtml_BigType_style: Property = Property(name="style", type=StringType)
xhtml_BigType_title: Property = Property(name="title", type=StringType)
xhtml_BigType.attributes={xhtml_BigType_id, xhtml_BigType_title, xhtml_BigType_style, xhtml_BigType_class}

# xhtml_SmallType class attributes and methods
xhtml_SmallType_class: Property = Property(name="class", type=StringType)
xhtml_SmallType_id: Property = Property(name="id", type=StringType)
xhtml_SmallType_style: Property = Property(name="style", type=StringType)
xhtml_SmallType_title: Property = Property(name="title", type=StringType)
xhtml_SmallType.attributes={xhtml_SmallType_title, xhtml_SmallType_id, xhtml_SmallType_style, xhtml_SmallType_class}

# xhtml_UType class attributes and methods
xhtml_UType_style: Property = Property(name="style", type=StringType)
xhtml_UType_title: Property = Property(name="title", type=StringType)
xhtml_UType_class: Property = Property(name="class", type=StringType)
xhtml_UType_id: Property = Property(name="id", type=StringType)
xhtml_UType.attributes={xhtml_UType_id, xhtml_UType_class, xhtml_UType_title, xhtml_UType_style}

# xhtml_KbdType class attributes and methods
xhtml_KbdType_class: Property = Property(name="class", type=StringType)
xhtml_KbdType_id: Property = Property(name="id", type=StringType)
xhtml_KbdType_style: Property = Property(name="style", type=StringType)
xhtml_KbdType_title: Property = Property(name="title", type=StringType)
xhtml_KbdType.attributes={xhtml_KbdType_title, xhtml_KbdType_style, xhtml_KbdType_id, xhtml_KbdType_class}

# xhtml_VarType class attributes and methods
xhtml_VarType_class: Property = Property(name="class", type=StringType)
xhtml_VarType_id: Property = Property(name="id", type=StringType)
xhtml_VarType_style: Property = Property(name="style", type=StringType)
xhtml_VarType_title: Property = Property(name="title", type=StringType)
xhtml_VarType.attributes={xhtml_VarType_class, xhtml_VarType_style, xhtml_VarType_title, xhtml_VarType_id}

# xhtml_CiteType class attributes and methods
xhtml_CiteType_class: Property = Property(name="class", type=StringType)
xhtml_CiteType_id: Property = Property(name="id", type=StringType)
xhtml_CiteType_style: Property = Property(name="style", type=StringType)
xhtml_CiteType_title: Property = Property(name="title", type=StringType)
xhtml_CiteType.attributes={xhtml_CiteType_id, xhtml_CiteType_class, xhtml_CiteType_title, xhtml_CiteType_style}

# xhtml_DfnType class attributes and methods
xhtml_DfnType_class: Property = Property(name="class", type=StringType)
xhtml_DfnType_id: Property = Property(name="id", type=StringType)
xhtml_DfnType_style: Property = Property(name="style", type=StringType)
xhtml_DfnType_title: Property = Property(name="title", type=StringType)
xhtml_DfnType.attributes={xhtml_DfnType_id, xhtml_DfnType_class, xhtml_DfnType_title, xhtml_DfnType_style}

# xhtml_CodeType class attributes and methods
xhtml_CodeType_title: Property = Property(name="title", type=StringType)
xhtml_CodeType_class: Property = Property(name="class", type=StringType)
xhtml_CodeType_id: Property = Property(name="id", type=StringType)
xhtml_CodeType_style: Property = Property(name="style", type=StringType)
xhtml_CodeType.attributes={xhtml_CodeType_id, xhtml_CodeType_class, xhtml_CodeType_title, xhtml_CodeType_style}

# xhtml_QType class attributes and methods
xhtml_QType_cite1: Property = Property(name="cite1", type=StringType)
xhtml_QType_class: Property = Property(name="class", type=StringType)
xhtml_QType_id: Property = Property(name="id", type=StringType)
xhtml_QType_style: Property = Property(name="style", type=StringType)
xhtml_QType_title: Property = Property(name="title", type=StringType)
xhtml_QType.attributes={xhtml_QType_cite1, xhtml_QType_id, xhtml_QType_title, xhtml_QType_class, xhtml_QType_style}

# xhtml_SampType class attributes and methods
xhtml_SampType_class: Property = Property(name="class", type=StringType)
xhtml_SampType_id: Property = Property(name="id", type=StringType)
xhtml_SampType_style: Property = Property(name="style", type=StringType)
xhtml_SampType_title: Property = Property(name="title", type=StringType)
xhtml_SampType.attributes={xhtml_SampType_title, xhtml_SampType_class, xhtml_SampType_style, xhtml_SampType_id}

# xhtml_SupType class attributes and methods
xhtml_SupType_class: Property = Property(name="class", type=StringType)
xhtml_SupType_id: Property = Property(name="id", type=StringType)
xhtml_SupType_style: Property = Property(name="style", type=StringType)
xhtml_SupType_title: Property = Property(name="title", type=StringType)
xhtml_SupType.attributes={xhtml_SupType_id, xhtml_SupType_class, xhtml_SupType_title, xhtml_SupType_style}

# xhtml_InsType class attributes and methods
xhtml_InsType_cite1: Property = Property(name="cite1", type=StringType)
xhtml_InsType_class: Property = Property(name="class", type=StringType)
xhtml_InsType_datetime: Property = Property(name="datetime", type=StringType)
xhtml_InsType_id: Property = Property(name="id", type=StringType)
xhtml_InsType_style: Property = Property(name="style", type=StringType)
xhtml_InsType_title: Property = Property(name="title", type=StringType)
xhtml_InsType.attributes={xhtml_InsType_cite1, xhtml_InsType_title, xhtml_InsType_style, xhtml_InsType_id, xhtml_InsType_datetime, xhtml_InsType_class}

# xhtml_AcronymType class attributes and methods
xhtml_AcronymType_class: Property = Property(name="class", type=StringType)
xhtml_AcronymType_id: Property = Property(name="id", type=StringType)
xhtml_AcronymType_style: Property = Property(name="style", type=StringType)
xhtml_AcronymType_title: Property = Property(name="title", type=StringType)
xhtml_AcronymType.attributes={xhtml_AcronymType_id, xhtml_AcronymType_style, xhtml_AcronymType_title, xhtml_AcronymType_class}

# xhtml_SubType class attributes and methods
xhtml_SubType_id: Property = Property(name="id", type=StringType)
xhtml_SubType_style: Property = Property(name="style", type=StringType)
xhtml_SubType_title: Property = Property(name="title", type=StringType)
xhtml_SubType_class: Property = Property(name="class", type=StringType)
xhtml_SubType.attributes={xhtml_SubType_class, xhtml_SubType_title, xhtml_SubType_id, xhtml_SubType_style}

# xhtml_DelType class attributes and methods
xhtml_DelType_id: Property = Property(name="id", type=StringType)
xhtml_DelType_style: Property = Property(name="style", type=StringType)
xhtml_DelType_title: Property = Property(name="title", type=StringType)
xhtml_DelType_cite1: Property = Property(name="cite1", type=StringType)
xhtml_DelType_class: Property = Property(name="class", type=StringType)
xhtml_DelType_datetime: Property = Property(name="datetime", type=StringType)
xhtml_DelType.attributes={xhtml_DelType_datetime, xhtml_DelType_title, xhtml_DelType_id, xhtml_DelType_class, xhtml_DelType_cite1, xhtml_DelType_style}

# xhtml_AddressType class attributes and methods
xhtml_AddressType_class: Property = Property(name="class", type=StringType)
xhtml_AddressType_id: Property = Property(name="id", type=StringType)
xhtml_AddressType_style: Property = Property(name="style", type=StringType)
xhtml_AddressType_title: Property = Property(name="title", type=StringType)
xhtml_AddressType.attributes={xhtml_AddressType_id, xhtml_AddressType_class, xhtml_AddressType_title, xhtml_AddressType_style}

# xhtml_AType class attributes and methods
xhtml_AType_name: Property = Property(name="name", type=StringType)
xhtml_AType_rel: Property = Property(name="rel", type=StringType)
xhtml_AType_rev: Property = Property(name="rev", type=StringType)
xhtml_AType_shape: Property = Property(name="shape", type=StringType)
xhtml_AType_style: Property = Property(name="style", type=StringType)
xhtml_AType_title: Property = Property(name="title", type=StringType)
xhtml_AType_type: Property = Property(name="type", type=StringType)
xhtml_AType_charset: Property = Property(name="charset", type=StringType)
xhtml_AType_class: Property = Property(name="class", type=StringType)
xhtml_AType_coords: Property = Property(name="coords", type=StringType)
xhtml_AType_href: Property = Property(name="href", type=StringType)
xhtml_AType_hreflang: Property = Property(name="hreflang", type=StringType)
xhtml_AType_id: Property = Property(name="id", type=StringType)
xhtml_AType.attributes={xhtml_AType_hreflang, xhtml_AType_coords, xhtml_AType_shape, xhtml_AType_type, xhtml_AType_charset, xhtml_AType_style, xhtml_AType_name, xhtml_AType_rel, xhtml_AType_id, xhtml_AType_rev, xhtml_AType_href, xhtml_AType_title, xhtml_AType_class}

# AContent class attributes and methods

# xhtml_H2Type class attributes and methods
xhtml_H2Type_class: Property = Property(name="class", type=StringType)
xhtml_H2Type_id: Property = Property(name="id", type=StringType)
xhtml_H2Type_style: Property = Property(name="style", type=StringType)
xhtml_H2Type_title: Property = Property(name="title", type=StringType)
xhtml_H2Type.attributes={xhtml_H2Type_id, xhtml_H2Type_title, xhtml_H2Type_style, xhtml_H2Type_class}

# xhtml_H3Type class attributes and methods
xhtml_H3Type_id: Property = Property(name="id", type=StringType)
xhtml_H3Type_style: Property = Property(name="style", type=StringType)
xhtml_H3Type_title: Property = Property(name="title", type=StringType)
xhtml_H3Type_class: Property = Property(name="class", type=StringType)
xhtml_H3Type.attributes={xhtml_H3Type_class, xhtml_H3Type_title, xhtml_H3Type_id, xhtml_H3Type_style}

# xhtml_H4Type class attributes and methods
xhtml_H4Type_class: Property = Property(name="class", type=StringType)
xhtml_H4Type_id: Property = Property(name="id", type=StringType)
xhtml_H4Type_style: Property = Property(name="style", type=StringType)
xhtml_H4Type_title: Property = Property(name="title", type=StringType)
xhtml_H4Type.attributes={xhtml_H4Type_id, xhtml_H4Type_title, xhtml_H4Type_class, xhtml_H4Type_style}

# xhtml_H5Type class attributes and methods
xhtml_H5Type_class: Property = Property(name="class", type=StringType)
xhtml_H5Type_id: Property = Property(name="id", type=StringType)
xhtml_H5Type_style: Property = Property(name="style", type=StringType)
xhtml_H5Type_title: Property = Property(name="title", type=StringType)
xhtml_H5Type.attributes={xhtml_H5Type_style, xhtml_H5Type_title, xhtml_H5Type_id, xhtml_H5Type_class}

# xhtml_H6Type class attributes and methods
xhtml_H6Type_style: Property = Property(name="style", type=StringType)
xhtml_H6Type_title: Property = Property(name="title", type=StringType)
xhtml_H6Type_class: Property = Property(name="class", type=StringType)
xhtml_H6Type_id: Property = Property(name="id", type=StringType)
xhtml_H6Type.attributes={xhtml_H6Type_class, xhtml_H6Type_id, xhtml_H6Type_title, xhtml_H6Type_style}

# xhtml_Block class attributes and methods
xhtml_Block_group: Property = Property(name="group", type=StringType)
xhtml_Block.attributes={xhtml_Block_group}

# xhtml_PType class attributes and methods
xhtml_PType_class: Property = Property(name="class", type=StringType)
xhtml_PType_id: Property = Property(name="id", type=StringType)
xhtml_PType_style: Property = Property(name="style", type=StringType)
xhtml_PType_title: Property = Property(name="title", type=StringType)
xhtml_PType.attributes={xhtml_PType_style, xhtml_PType_title, xhtml_PType_class, xhtml_PType_id}

# xhtml_H1Type class attributes and methods
xhtml_H1Type_class: Property = Property(name="class", type=StringType)
xhtml_H1Type_id: Property = Property(name="id", type=StringType)
xhtml_H1Type_style: Property = Property(name="style", type=StringType)
xhtml_H1Type_title: Property = Property(name="title", type=StringType)
xhtml_H1Type.attributes={xhtml_H1Type_class, xhtml_H1Type_id, xhtml_H1Type_style, xhtml_H1Type_title}

# xhtml_DlType class attributes and methods
xhtml_DlType_style: Property = Property(name="style", type=StringType)
xhtml_DlType_title: Property = Property(name="title", type=StringType)
xhtml_DlType_group: Property = Property(name="group", type=StringType)
xhtml_DlType_class: Property = Property(name="class", type=StringType)
xhtml_DlType_id: Property = Property(name="id", type=StringType)
xhtml_DlType.attributes={xhtml_DlType_style, xhtml_DlType_title, xhtml_DlType_class, xhtml_DlType_group, xhtml_DlType_id}

# xhtml_PreType class attributes and methods
xhtml_PreType_class: Property = Property(name="class", type=StringType)
xhtml_PreType_id: Property = Property(name="id", type=StringType)
xhtml_PreType_style: Property = Property(name="style", type=StringType)
xhtml_PreType_title: Property = Property(name="title", type=StringType)
xhtml_PreType.attributes={xhtml_PreType_style, xhtml_PreType_class, xhtml_PreType_id, xhtml_PreType_title}

# xhtml_HrType class attributes and methods
xhtml_HrType_class: Property = Property(name="class", type=StringType)
xhtml_HrType_id: Property = Property(name="id", type=StringType)
xhtml_HrType_style: Property = Property(name="style", type=StringType)
xhtml_HrType_title: Property = Property(name="title", type=StringType)
xhtml_HrType.attributes={xhtml_HrType_title, xhtml_HrType_id, xhtml_HrType_class, xhtml_HrType_style}

# xhtml_BlockquoteType class attributes and methods
xhtml_BlockquoteType_cite: Property = Property(name="cite", type=StringType)
xhtml_BlockquoteType_class: Property = Property(name="class", type=StringType)
xhtml_BlockquoteType_id: Property = Property(name="id", type=StringType)
xhtml_BlockquoteType_style: Property = Property(name="style", type=StringType)
xhtml_BlockquoteType_title: Property = Property(name="title", type=StringType)
xhtml_BlockquoteType.attributes={xhtml_BlockquoteType_class, xhtml_BlockquoteType_title, xhtml_BlockquoteType_style, xhtml_BlockquoteType_id, xhtml_BlockquoteType_cite}

# xhtml_TableType class attributes and methods
xhtml_TableType_title: Property = Property(name="title", type=StringType)
xhtml_TableType_width: Property = Property(name="width", type=StringType)
xhtml_TableType_border: Property = Property(name="border", type=StringType)
xhtml_TableType_cellpadding: Property = Property(name="cellpadding", type=StringType)
xhtml_TableType_cellspacing: Property = Property(name="cellspacing", type=StringType)
xhtml_TableType_class: Property = Property(name="class", type=StringType)
xhtml_TableType_id: Property = Property(name="id", type=StringType)
xhtml_TableType_style: Property = Property(name="style", type=StringType)
xhtml_TableType_summary: Property = Property(name="summary", type=StringType)
xhtml_TableType.attributes={xhtml_TableType_cellspacing, xhtml_TableType_id, xhtml_TableType_cellpadding, xhtml_TableType_class, xhtml_TableType_summary, xhtml_TableType_width, xhtml_TableType_border, xhtml_TableType_style, xhtml_TableType_title}

# xhtml_DivType class attributes and methods
xhtml_DivType_class: Property = Property(name="class", type=StringType)
xhtml_DivType_id: Property = Property(name="id", type=StringType)
xhtml_DivType_style: Property = Property(name="style", type=StringType)
xhtml_DivType_title: Property = Property(name="title", type=StringType)
xhtml_DivType.attributes={xhtml_DivType_id, xhtml_DivType_title, xhtml_DivType_style, xhtml_DivType_class}

# xhtml_UlType class attributes and methods
xhtml_UlType_class: Property = Property(name="class", type=StringType)
xhtml_UlType_id: Property = Property(name="id", type=StringType)
xhtml_UlType_style: Property = Property(name="style", type=StringType)
xhtml_UlType_title: Property = Property(name="title", type=StringType)
xhtml_UlType.attributes={xhtml_UlType_style, xhtml_UlType_class, xhtml_UlType_title, xhtml_UlType_id}

# xhtml_OlType class attributes and methods
xhtml_OlType_title: Property = Property(name="title", type=StringType)
xhtml_OlType_class: Property = Property(name="class", type=StringType)
xhtml_OlType_id: Property = Property(name="id", type=StringType)
xhtml_OlType_style: Property = Property(name="style", type=StringType)
xhtml_OlType.attributes={xhtml_OlType_style, xhtml_OlType_title, xhtml_OlType_id, xhtml_OlType_class}

# Block class attributes and methods

# xhtml_BodyType class attributes and methods
xhtml_BodyType_class: Property = Property(name="class", type=StringType)
xhtml_BodyType_id: Property = Property(name="id", type=StringType)
xhtml_BodyType_style: Property = Property(name="style", type=StringType)
xhtml_BodyType_title: Property = Property(name="title", type=StringType)
xhtml_BodyType.attributes={xhtml_BodyType_title, xhtml_BodyType_class, xhtml_BodyType_style, xhtml_BodyType_id}

# xhtml_CaptionType class attributes and methods
xhtml_CaptionType_class: Property = Property(name="class", type=StringType)
xhtml_CaptionType_id: Property = Property(name="id", type=StringType)
xhtml_CaptionType_style: Property = Property(name="style", type=StringType)
xhtml_CaptionType_title: Property = Property(name="title", type=StringType)
xhtml_CaptionType.attributes={xhtml_CaptionType_id, xhtml_CaptionType_style, xhtml_CaptionType_title, xhtml_CaptionType_class}

# xhtml_ColgroupType class attributes and methods
xhtml_ColgroupType_align: Property = Property(name="align", type=StringType)
xhtml_ColgroupType_char: Property = Property(name="char", type=StringType)
xhtml_ColgroupType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_ColgroupType_class: Property = Property(name="class", type=StringType)
xhtml_ColgroupType_id: Property = Property(name="id", type=StringType)
xhtml_ColgroupType_span: Property = Property(name="span", type=StringType)
xhtml_ColgroupType_style: Property = Property(name="style", type=StringType)
xhtml_ColgroupType_title: Property = Property(name="title", type=StringType)
xhtml_ColgroupType_valign: Property = Property(name="valign", type=StringType)
xhtml_ColgroupType_width: Property = Property(name="width", type=StringType)
xhtml_ColgroupType.attributes={xhtml_ColgroupType_align, xhtml_ColgroupType_span, xhtml_ColgroupType_style, xhtml_ColgroupType_class, xhtml_ColgroupType_char, xhtml_ColgroupType_id, xhtml_ColgroupType_charoff, xhtml_ColgroupType_title, xhtml_ColgroupType_valign, xhtml_ColgroupType_width}

# xhtml_ColType class attributes and methods
xhtml_ColType_style: Property = Property(name="style", type=StringType)
xhtml_ColType_title: Property = Property(name="title", type=StringType)
xhtml_ColType_valign: Property = Property(name="valign", type=StringType)
xhtml_ColType_width: Property = Property(name="width", type=StringType)
xhtml_ColType_align: Property = Property(name="align", type=StringType)
xhtml_ColType_char: Property = Property(name="char", type=StringType)
xhtml_ColType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_ColType_class: Property = Property(name="class", type=StringType)
xhtml_ColType_id: Property = Property(name="id", type=StringType)
xhtml_ColType_span: Property = Property(name="span", type=StringType)
xhtml_ColType.attributes={xhtml_ColType_charoff, xhtml_ColType_valign, xhtml_ColType_char, xhtml_ColType_title, xhtml_ColType_width, xhtml_ColType_style, xhtml_ColType_id, xhtml_ColType_span, xhtml_ColType_align, xhtml_ColType_class}

# xhtml_DdType class attributes and methods
xhtml_DdType_class: Property = Property(name="class", type=StringType)
xhtml_DdType_id: Property = Property(name="id", type=StringType)
xhtml_DdType_style: Property = Property(name="style", type=StringType)
xhtml_DdType_title: Property = Property(name="title", type=StringType)
xhtml_DdType.attributes={xhtml_DdType_id, xhtml_DdType_class, xhtml_DdType_style, xhtml_DdType_title}

# Flow class attributes and methods

# xhtml_DocumentRoot class attributes and methods
xhtml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
xhtml_DocumentRoot.attributes={xhtml_DocumentRoot_mixed}

# xhtml_EStringToStringMapEntry class attributes and methods

# xhtml_DtType class attributes and methods
xhtml_DtType_class: Property = Property(name="class", type=StringType)
xhtml_DtType_id: Property = Property(name="id", type=StringType)
xhtml_DtType_style: Property = Property(name="style", type=StringType)
xhtml_DtType_title: Property = Property(name="title", type=StringType)
xhtml_DtType.attributes={xhtml_DtType_title, xhtml_DtType_class, xhtml_DtType_style, xhtml_DtType_id}

# xhtml_LiType class attributes and methods
xhtml_LiType_title: Property = Property(name="title", type=StringType)
xhtml_LiType_class: Property = Property(name="class", type=StringType)
xhtml_LiType_id: Property = Property(name="id", type=StringType)
xhtml_LiType_style: Property = Property(name="style", type=StringType)
xhtml_LiType.attributes={xhtml_LiType_class, xhtml_LiType_id, xhtml_LiType_style, xhtml_LiType_title}

# xhtml_HtmlType class attributes and methods
xhtml_HtmlType_id: Property = Property(name="id", type=StringType)
xhtml_HtmlType.attributes={xhtml_HtmlType_id}

# xhtml_ParamType class attributes and methods
xhtml_ParamType_id: Property = Property(name="id", type=StringType)
xhtml_ParamType_name: Property = Property(name="name", type=StringType)
xhtml_ParamType_type: Property = Property(name="type", type=StringType)
xhtml_ParamType_value: Property = Property(name="value", type=StringType)
xhtml_ParamType_valuetype: Property = Property(name="valuetype", type=StringType)
xhtml_ParamType.attributes={xhtml_ParamType_name, xhtml_ParamType_valuetype, xhtml_ParamType_value, xhtml_ParamType_type, xhtml_ParamType_id}

# xhtml_TfootType class attributes and methods
xhtml_TfootType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TfootType_class: Property = Property(name="class", type=StringType)
xhtml_TfootType_id: Property = Property(name="id", type=StringType)
xhtml_TfootType_align: Property = Property(name="align", type=StringType)
xhtml_TfootType_char: Property = Property(name="char", type=StringType)
xhtml_TfootType_style: Property = Property(name="style", type=StringType)
xhtml_TfootType_title: Property = Property(name="title", type=StringType)
xhtml_TfootType_valign: Property = Property(name="valign", type=StringType)
xhtml_TfootType.attributes={xhtml_TfootType_char, xhtml_TfootType_title, xhtml_TfootType_valign, xhtml_TfootType_class, xhtml_TfootType_charoff, xhtml_TfootType_style, xhtml_TfootType_align, xhtml_TfootType_id}

# xhtml_ThType class attributes and methods
xhtml_ThType_abbr1: Property = Property(name="abbr1", type=StringType)
xhtml_ThType_align: Property = Property(name="align", type=StringType)
xhtml_ThType_axis: Property = Property(name="axis", type=StringType)
xhtml_ThType_char: Property = Property(name="char", type=StringType)
xhtml_ThType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_ThType_class: Property = Property(name="class", type=StringType)
xhtml_ThType_colspan: Property = Property(name="colspan", type=StringType)
xhtml_ThType_headers: Property = Property(name="headers", type=StringType)
xhtml_ThType_id: Property = Property(name="id", type=StringType)
xhtml_ThType_rowspan: Property = Property(name="rowspan", type=StringType)
xhtml_ThType_scope: Property = Property(name="scope", type=StringType)
xhtml_ThType_style: Property = Property(name="style", type=StringType)
xhtml_ThType_title: Property = Property(name="title", type=StringType)
xhtml_ThType_valign: Property = Property(name="valign", type=StringType)
xhtml_ThType.attributes={xhtml_ThType_char, xhtml_ThType_id, xhtml_ThType_charoff, xhtml_ThType_scope, xhtml_ThType_style, xhtml_ThType_title, xhtml_ThType_align, xhtml_ThType_axis, xhtml_ThType_valign, xhtml_ThType_rowspan, xhtml_ThType_class, xhtml_ThType_headers, xhtml_ThType_abbr1, xhtml_ThType_colspan}

# xhtml_TheadType class attributes and methods
xhtml_TheadType_align: Property = Property(name="align", type=StringType)
xhtml_TheadType_char: Property = Property(name="char", type=StringType)
xhtml_TheadType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TheadType_class: Property = Property(name="class", type=StringType)
xhtml_TheadType_id: Property = Property(name="id", type=StringType)
xhtml_TheadType_style: Property = Property(name="style", type=StringType)
xhtml_TheadType_title: Property = Property(name="title", type=StringType)
xhtml_TheadType_valign: Property = Property(name="valign", type=StringType)
xhtml_TheadType.attributes={xhtml_TheadType_char, xhtml_TheadType_id, xhtml_TheadType_class, xhtml_TheadType_title, xhtml_TheadType_align, xhtml_TheadType_style, xhtml_TheadType_valign, xhtml_TheadType_charoff}

# xhtml_TrType class attributes and methods
xhtml_TrType_group: Property = Property(name="group", type=StringType)
xhtml_TrType_align: Property = Property(name="align", type=StringType)
xhtml_TrType_char: Property = Property(name="char", type=StringType)
xhtml_TrType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TrType_class: Property = Property(name="class", type=StringType)
xhtml_TrType_id: Property = Property(name="id", type=StringType)
xhtml_TrType_style: Property = Property(name="style", type=StringType)
xhtml_TrType_title: Property = Property(name="title", type=StringType)
xhtml_TrType_valign: Property = Property(name="valign", type=StringType)
xhtml_TrType.attributes={xhtml_TrType_class, xhtml_TrType_id, xhtml_TrType_title, xhtml_TrType_charoff, xhtml_TrType_style, xhtml_TrType_align, xhtml_TrType_char, xhtml_TrType_group, xhtml_TrType_valign}

# xhtml_TbodyType class attributes and methods
xhtml_TbodyType_align: Property = Property(name="align", type=StringType)
xhtml_TbodyType_char: Property = Property(name="char", type=StringType)
xhtml_TbodyType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TbodyType_class: Property = Property(name="class", type=StringType)
xhtml_TbodyType_id: Property = Property(name="id", type=StringType)
xhtml_TbodyType_style: Property = Property(name="style", type=StringType)
xhtml_TbodyType_title: Property = Property(name="title", type=StringType)
xhtml_TbodyType_valign: Property = Property(name="valign", type=StringType)
xhtml_TbodyType.attributes={xhtml_TbodyType_valign, xhtml_TbodyType_style, xhtml_TbodyType_align, xhtml_TbodyType_char, xhtml_TbodyType_class, xhtml_TbodyType_id, xhtml_TbodyType_charoff, xhtml_TbodyType_title}

# xhtml_TdType class attributes and methods
xhtml_TdType_char: Property = Property(name="char", type=StringType)
xhtml_TdType_charoff: Property = Property(name="charoff", type=StringType)
xhtml_TdType_class: Property = Property(name="class", type=StringType)
xhtml_TdType_colspan: Property = Property(name="colspan", type=StringType)
xhtml_TdType_abbr1: Property = Property(name="abbr1", type=StringType)
xhtml_TdType_align: Property = Property(name="align", type=StringType)
xhtml_TdType_axis: Property = Property(name="axis", type=StringType)
xhtml_TdType_headers: Property = Property(name="headers", type=StringType)
xhtml_TdType_id: Property = Property(name="id", type=StringType)
xhtml_TdType_rowspan: Property = Property(name="rowspan", type=StringType)
xhtml_TdType_scope: Property = Property(name="scope", type=StringType)
xhtml_TdType_style: Property = Property(name="style", type=StringType)
xhtml_TdType_title: Property = Property(name="title", type=StringType)
xhtml_TdType_valign: Property = Property(name="valign", type=StringType)
xhtml_TdType.attributes={xhtml_TdType_id, xhtml_TdType_abbr1, xhtml_TdType_align, xhtml_TdType_style, xhtml_TdType_char, xhtml_TdType_colspan, xhtml_TdType_title, xhtml_TdType_valign, xhtml_TdType_scope, xhtml_TdType_headers, xhtml_TdType_rowspan, xhtml_TdType_charoff, xhtml_TdType_axis, xhtml_TdType_class}

# xhtml_Flow class attributes and methods
xhtml_Flow_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Flow_group: Property = Property(name="group", type=StringType)
xhtml_Flow.attributes={xhtml_Flow_group, xhtml_Flow_mixed}

# xhtml_FormContent class attributes and methods
xhtml_FormContent_group: Property = Property(name="group", type=StringType)
xhtml_FormContent.attributes={xhtml_FormContent_group}

# xhtml_Inline class attributes and methods
xhtml_Inline_mixed: Property = Property(name="mixed", type=StringType)
xhtml_Inline_group: Property = Property(name="group", type=StringType)
xhtml_Inline.attributes={xhtml_Inline_mixed, xhtml_Inline_group}

# xhtml_PreContent class attributes and methods
xhtml_PreContent_mixed: Property = Property(name="mixed", type=StringType)
xhtml_PreContent_group: Property = Property(name="group", type=StringType)
xhtml_PreContent.attributes={xhtml_PreContent_mixed, xhtml_PreContent_group}

# PreContent class attributes and methods

# Relationships
object3: BinaryAssociation = BinaryAssociation(
    name="object3",
    ends={
        Property(name="xhtml_ObjectType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent4", type=xhtml_ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img5: BinaryAssociation = BinaryAssociation(
    name="img5",
    ends={
        Property(name="xhtml_ImgType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent6", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt7: BinaryAssociation = BinaryAssociation(
    name="tt7",
    ends={
        Property(name="xhtml_TtType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent8", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
strike19: BinaryAssociation = BinaryAssociation(
    name="strike19",
    ends={
        Property(name="xhtml_StrikeType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent20", type=xhtml_StrikeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em21: BinaryAssociation = BinaryAssociation(
    name="em21",
    ends={
        Property(name="xhtml_EmType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent22", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong23: BinaryAssociation = BinaryAssociation(
    name="strong23",
    ends={
        Property(name="xhtml_StrongType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent24", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i9: BinaryAssociation = BinaryAssociation(
    name="i9",
    ends={
        Property(name="xhtml_IType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent10", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b11: BinaryAssociation = BinaryAssociation(
    name="b11",
    ends={
        Property(name="xhtml_BType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent12", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big13: BinaryAssociation = BinaryAssociation(
    name="big13",
    ends={
        Property(name="xhtml_BigType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent14", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small15: BinaryAssociation = BinaryAssociation(
    name="small15",
    ends={
        Property(name="xhtml_SmallType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent16", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u17: BinaryAssociation = BinaryAssociation(
    name="u17",
    ends={
        Property(name="xhtml_UType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent18", type=xhtml_UType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd33: BinaryAssociation = BinaryAssociation(
    name="kbd33",
    ends={
        Property(name="xhtml_KbdType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent34", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var35: BinaryAssociation = BinaryAssociation(
    name="var35",
    ends={
        Property(name="xhtml_VarType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent36", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite37: BinaryAssociation = BinaryAssociation(
    name="cite37",
    ends={
        Property(name="xhtml_CiteType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent38", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn25: BinaryAssociation = BinaryAssociation(
    name="dfn25",
    ends={
        Property(name="xhtml_DfnType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent26", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code27: BinaryAssociation = BinaryAssociation(
    name="code27",
    ends={
        Property(name="xhtml_CodeType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent28", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q29: BinaryAssociation = BinaryAssociation(
    name="q29",
    ends={
        Property(name="xhtml_QType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent30", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp31: BinaryAssociation = BinaryAssociation(
    name="samp31",
    ends={
        Property(name="xhtml_SampType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent32", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub43: BinaryAssociation = BinaryAssociation(
    name="sub43",
    ends={
        Property(name="xhtml_SubType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent44", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup45: BinaryAssociation = BinaryAssociation(
    name="sup45",
    ends={
        Property(name="xhtml_SupType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent46", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins47: BinaryAssociation = BinaryAssociation(
    name="ins47",
    ends={
        Property(name="xhtml_InsType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent48", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr39: BinaryAssociation = BinaryAssociation(
    name="abbr39",
    ends={
        Property(name="xhtml_AbbrType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent40", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym41: BinaryAssociation = BinaryAssociation(
    name="acronym41",
    ends={
        Property(name="xhtml_AcronymType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent42", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del49: BinaryAssociation = BinaryAssociation(
    name="del49",
    ends={
        Property(name="xhtml_DelType", type=xhtml_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_AContent50", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h254: BinaryAssociation = BinaryAssociation(
    name="h254",
    ends={
        Property(name="xhtml_H2Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block55", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h356: BinaryAssociation = BinaryAssociation(
    name="h356",
    ends={
        Property(name="xhtml_H3Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block57", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h458: BinaryAssociation = BinaryAssociation(
    name="h458",
    ends={
        Property(name="xhtml_H4Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block59", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h560: BinaryAssociation = BinaryAssociation(
    name="h560",
    ends={
        Property(name="xhtml_H5Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block61", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h662: BinaryAssociation = BinaryAssociation(
    name="h662",
    ends={
        Property(name="xhtml_H6Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block63", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p51: BinaryAssociation = BinaryAssociation(
    name="p51",
    ends={
        Property(name="xhtml_PType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h152: BinaryAssociation = BinaryAssociation(
    name="h152",
    ends={
        Property(name="xhtml_H1Type", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block53", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl70: BinaryAssociation = BinaryAssociation(
    name="dl70",
    ends={
        Property(name="xhtml_DlType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block71", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre72: BinaryAssociation = BinaryAssociation(
    name="pre72",
    ends={
        Property(name="xhtml_PreType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block73", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr74: BinaryAssociation = BinaryAssociation(
    name="hr74",
    ends={
        Property(name="xhtml_HrType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block75", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote76: BinaryAssociation = BinaryAssociation(
    name="blockquote76",
    ends={
        Property(name="xhtml_BlockquoteType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block77", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address78: BinaryAssociation = BinaryAssociation(
    name="address78",
    ends={
        Property(name="xhtml_AddressType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block79", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div64: BinaryAssociation = BinaryAssociation(
    name="div64",
    ends={
        Property(name="xhtml_DivType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block65", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul66: BinaryAssociation = BinaryAssociation(
    name="ul66",
    ends={
        Property(name="xhtml_UlType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block67", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol68: BinaryAssociation = BinaryAssociation(
    name="ol68",
    ends={
        Property(name="xhtml_OlType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block69", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table80: BinaryAssociation = BinaryAssociation(
    name="table80",
    ends={
        Property(name="xhtml_TableType", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block81", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins82: BinaryAssociation = BinaryAssociation(
    name="ins82",
    ends={
        Property(name="xhtml_InsType84", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block83", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del85: BinaryAssociation = BinaryAssociation(
    name="del85",
    ends={
        Property(name="xhtml_DelType87", type=xhtml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Block86", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col88: BinaryAssociation = BinaryAssociation(
    name="col88",
    ends={
        Property(name="xhtml_ColType", type=xhtml_ColgroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ColgroupType", type=xhtml_ColType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap93: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap93",
    ends={
        Property(name="xhtml_EStringToStringMapEntry", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot", type=xhtml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation94: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation94",
    ends={
        Property(name="xhtml_EStringToStringMapEntry96", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot95", type=xhtml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a97: BinaryAssociation = BinaryAssociation(
    name="a97",
    ends={
        Property(name="xhtml_AType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot98", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr99: BinaryAssociation = BinaryAssociation(
    name="abbr99",
    ends={
        Property(name="xhtml_AbbrType101", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot100", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym102: BinaryAssociation = BinaryAssociation(
    name="acronym102",
    ends={
        Property(name="xhtml_AcronymType104", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot103", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dt89: BinaryAssociation = BinaryAssociation(
    name="dt89",
    ends={
        Property(name="xhtml_DtType", type=xhtml_DlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DlType90", type=xhtml_DtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dd91: BinaryAssociation = BinaryAssociation(
    name="dd91",
    ends={
        Property(name="xhtml_DdType", type=xhtml_DlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DlType92", type=xhtml_DdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big111: BinaryAssociation = BinaryAssociation(
    name="big111",
    ends={
        Property(name="xhtml_BigType113", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot112", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote114: BinaryAssociation = BinaryAssociation(
    name="blockquote114",
    ends={
        Property(name="xhtml_BlockquoteType116", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot115", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body117: BinaryAssociation = BinaryAssociation(
    name="body117",
    ends={
        Property(name="xhtml_BodyType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot118", type=xhtml_BodyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br119: BinaryAssociation = BinaryAssociation(
    name="br119",
    ends={
        Property(name="xhtml_BrType121", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot120", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caption122: BinaryAssociation = BinaryAssociation(
    name="caption122",
    ends={
        Property(name="xhtml_CaptionType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot123", type=xhtml_CaptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite124: BinaryAssociation = BinaryAssociation(
    name="cite124",
    ends={
        Property(name="xhtml_CiteType126", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot125", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address105: BinaryAssociation = BinaryAssociation(
    name="address105",
    ends={
        Property(name="xhtml_AddressType107", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot106", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b108: BinaryAssociation = BinaryAssociation(
    name="b108",
    ends={
        Property(name="xhtml_BType110", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot109", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dd136: BinaryAssociation = BinaryAssociation(
    name="dd136",
    ends={
        Property(name="xhtml_DdType138", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot137", type=xhtml_DdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del139: BinaryAssociation = BinaryAssociation(
    name="del139",
    ends={
        Property(name="xhtml_DelType141", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot140", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn142: BinaryAssociation = BinaryAssociation(
    name="dfn142",
    ends={
        Property(name="xhtml_DfnType144", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot143", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div145: BinaryAssociation = BinaryAssociation(
    name="div145",
    ends={
        Property(name="xhtml_DivType147", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot146", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code127: BinaryAssociation = BinaryAssociation(
    name="code127",
    ends={
        Property(name="xhtml_CodeType129", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot128", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col130: BinaryAssociation = BinaryAssociation(
    name="col130",
    ends={
        Property(name="xhtml_ColType132", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot131", type=xhtml_ColType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colgroup133: BinaryAssociation = BinaryAssociation(
    name="colgroup133",
    ends={
        Property(name="xhtml_ColgroupType135", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot134", type=xhtml_ColgroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2160: BinaryAssociation = BinaryAssociation(
    name="h2160",
    ends={
        Property(name="xhtml_H2Type162", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot161", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3163: BinaryAssociation = BinaryAssociation(
    name="h3163",
    ends={
        Property(name="xhtml_H3Type165", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot164", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4166: BinaryAssociation = BinaryAssociation(
    name="h4166",
    ends={
        Property(name="xhtml_H4Type168", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot167", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5169: BinaryAssociation = BinaryAssociation(
    name="h5169",
    ends={
        Property(name="xhtml_H5Type171", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot170", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6172: BinaryAssociation = BinaryAssociation(
    name="h6172",
    ends={
        Property(name="xhtml_H6Type174", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot173", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr175: BinaryAssociation = BinaryAssociation(
    name="hr175",
    ends={
        Property(name="xhtml_HrType177", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot176", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl148: BinaryAssociation = BinaryAssociation(
    name="dl148",
    ends={
        Property(name="xhtml_DlType150", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot149", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dt151: BinaryAssociation = BinaryAssociation(
    name="dt151",
    ends={
        Property(name="xhtml_DtType153", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot152", type=xhtml_DtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em154: BinaryAssociation = BinaryAssociation(
    name="em154",
    ends={
        Property(name="xhtml_EmType156", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot155", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1157: BinaryAssociation = BinaryAssociation(
    name="h1157",
    ends={
        Property(name="xhtml_H1Type159", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot158", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd189: BinaryAssociation = BinaryAssociation(
    name="kbd189",
    ends={
        Property(name="xhtml_KbdType191", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot190", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li192: BinaryAssociation = BinaryAssociation(
    name="li192",
    ends={
        Property(name="xhtml_LiType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot193", type=xhtml_LiType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object194: BinaryAssociation = BinaryAssociation(
    name="object194",
    ends={
        Property(name="xhtml_ObjectType196", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot195", type=xhtml_ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol197: BinaryAssociation = BinaryAssociation(
    name="ol197",
    ends={
        Property(name="xhtml_OlType199", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot198", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
html178: BinaryAssociation = BinaryAssociation(
    name="html178",
    ends={
        Property(name="xhtml_HtmlType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot179", type=xhtml_HtmlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i180: BinaryAssociation = BinaryAssociation(
    name="i180",
    ends={
        Property(name="xhtml_IType182", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot181", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img183: BinaryAssociation = BinaryAssociation(
    name="img183",
    ends={
        Property(name="xhtml_ImgType185", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot184", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins186: BinaryAssociation = BinaryAssociation(
    name="ins186",
    ends={
        Property(name="xhtml_InsType188", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot187", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre205: BinaryAssociation = BinaryAssociation(
    name="pre205",
    ends={
        Property(name="xhtml_DocumentRoot206", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xhtml_PreType207", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1))
    }
)
q208: BinaryAssociation = BinaryAssociation(
    name="q208",
    ends={
        Property(name="xhtml_QType210", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot209", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp211: BinaryAssociation = BinaryAssociation(
    name="samp211",
    ends={
        Property(name="xhtml_SampType213", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot212", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small214: BinaryAssociation = BinaryAssociation(
    name="small214",
    ends={
        Property(name="xhtml_SmallType216", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot215", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p200: BinaryAssociation = BinaryAssociation(
    name="p200",
    ends={
        Property(name="xhtml_PType202", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot201", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param203: BinaryAssociation = BinaryAssociation(
    name="param203",
    ends={
        Property(name="xhtml_ParamType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot204", type=xhtml_ParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strike220: BinaryAssociation = BinaryAssociation(
    name="strike220",
    ends={
        Property(name="xhtml_StrikeType222", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot221", type=xhtml_StrikeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong223: BinaryAssociation = BinaryAssociation(
    name="strong223",
    ends={
        Property(name="xhtml_StrongType225", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot224", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub226: BinaryAssociation = BinaryAssociation(
    name="sub226",
    ends={
        Property(name="xhtml_SubType228", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot227", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup229: BinaryAssociation = BinaryAssociation(
    name="sup229",
    ends={
        Property(name="xhtml_SupType231", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot230", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span217: BinaryAssociation = BinaryAssociation(
    name="span217",
    ends={
        Property(name="xhtml_SpanType219", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot218", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tfoot239: BinaryAssociation = BinaryAssociation(
    name="tfoot239",
    ends={
        Property(name="xhtml_TfootType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot240", type=xhtml_TfootType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
th241: BinaryAssociation = BinaryAssociation(
    name="th241",
    ends={
        Property(name="xhtml_ThType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot242", type=xhtml_ThType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead243: BinaryAssociation = BinaryAssociation(
    name="thead243",
    ends={
        Property(name="xhtml_TheadType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot244", type=xhtml_TheadType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr245: BinaryAssociation = BinaryAssociation(
    name="tr245",
    ends={
        Property(name="xhtml_TrType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot246", type=xhtml_TrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt247: BinaryAssociation = BinaryAssociation(
    name="tt247",
    ends={
        Property(name="xhtml_TtType249", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot248", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table232: BinaryAssociation = BinaryAssociation(
    name="table232",
    ends={
        Property(name="xhtml_TableType234", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot233", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tbody235: BinaryAssociation = BinaryAssociation(
    name="tbody235",
    ends={
        Property(name="xhtml_TbodyType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot236", type=xhtml_TbodyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
td237: BinaryAssociation = BinaryAssociation(
    name="td237",
    ends={
        Property(name="xhtml_TdType", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot238", type=xhtml_TdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var256: BinaryAssociation = BinaryAssociation(
    name="var256",
    ends={
        Property(name="xhtml_VarType258", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot257", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u250: BinaryAssociation = BinaryAssociation(
    name="u250",
    ends={
        Property(name="xhtml_UType252", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot251", type=xhtml_UType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul253: BinaryAssociation = BinaryAssociation(
    name="ul253",
    ends={
        Property(name="xhtml_UlType255", type=xhtml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_DocumentRoot254", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1261: BinaryAssociation = BinaryAssociation(
    name="h1261",
    ends={
        Property(name="xhtml_H1Type263", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow262", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2264: BinaryAssociation = BinaryAssociation(
    name="h2264",
    ends={
        Property(name="xhtml_H2Type266", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow265", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3267: BinaryAssociation = BinaryAssociation(
    name="h3267",
    ends={
        Property(name="xhtml_H3Type269", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow268", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4270: BinaryAssociation = BinaryAssociation(
    name="h4270",
    ends={
        Property(name="xhtml_H4Type272", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow271", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5273: BinaryAssociation = BinaryAssociation(
    name="h5273",
    ends={
        Property(name="xhtml_H5Type275", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow274", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6276: BinaryAssociation = BinaryAssociation(
    name="h6276",
    ends={
        Property(name="xhtml_H6Type278", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow277", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p259: BinaryAssociation = BinaryAssociation(
    name="p259",
    ends={
        Property(name="xhtml_PType260", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol285: BinaryAssociation = BinaryAssociation(
    name="ol285",
    ends={
        Property(name="xhtml_OlType287", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow286", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl288: BinaryAssociation = BinaryAssociation(
    name="dl288",
    ends={
        Property(name="xhtml_DlType290", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow289", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre291: BinaryAssociation = BinaryAssociation(
    name="pre291",
    ends={
        Property(name="xhtml_PreType293", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow292", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr294: BinaryAssociation = BinaryAssociation(
    name="hr294",
    ends={
        Property(name="xhtml_HrType296", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow295", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div279: BinaryAssociation = BinaryAssociation(
    name="div279",
    ends={
        Property(name="xhtml_DivType281", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow280", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul282: BinaryAssociation = BinaryAssociation(
    name="ul282",
    ends={
        Property(name="xhtml_UlType284", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow283", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a306: BinaryAssociation = BinaryAssociation(
    name="a306",
    ends={
        Property(name="xhtml_AType308", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow307", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br309: BinaryAssociation = BinaryAssociation(
    name="br309",
    ends={
        Property(name="xhtml_BrType311", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow310", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span312: BinaryAssociation = BinaryAssociation(
    name="span312",
    ends={
        Property(name="xhtml_SpanType314", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow313", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object315: BinaryAssociation = BinaryAssociation(
    name="object315",
    ends={
        Property(name="xhtml_ObjectType317", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow316", type=xhtml_ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img318: BinaryAssociation = BinaryAssociation(
    name="img318",
    ends={
        Property(name="xhtml_ImgType320", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow319", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote297: BinaryAssociation = BinaryAssociation(
    name="blockquote297",
    ends={
        Property(name="xhtml_BlockquoteType299", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow298", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address300: BinaryAssociation = BinaryAssociation(
    name="address300",
    ends={
        Property(name="xhtml_AddressType302", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow301", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table303: BinaryAssociation = BinaryAssociation(
    name="table303",
    ends={
        Property(name="xhtml_TableType305", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow304", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b327: BinaryAssociation = BinaryAssociation(
    name="b327",
    ends={
        Property(name="xhtml_BType329", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow328", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big330: BinaryAssociation = BinaryAssociation(
    name="big330",
    ends={
        Property(name="xhtml_BigType332", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow331", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small333: BinaryAssociation = BinaryAssociation(
    name="small333",
    ends={
        Property(name="xhtml_SmallType335", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow334", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u336: BinaryAssociation = BinaryAssociation(
    name="u336",
    ends={
        Property(name="xhtml_UType338", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow337", type=xhtml_UType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt321: BinaryAssociation = BinaryAssociation(
    name="tt321",
    ends={
        Property(name="xhtml_TtType323", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow322", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i324: BinaryAssociation = BinaryAssociation(
    name="i324",
    ends={
        Property(name="xhtml_IType326", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow325", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn348: BinaryAssociation = BinaryAssociation(
    name="dfn348",
    ends={
        Property(name="xhtml_DfnType350", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow349", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code351: BinaryAssociation = BinaryAssociation(
    name="code351",
    ends={
        Property(name="xhtml_CodeType353", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow352", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q354: BinaryAssociation = BinaryAssociation(
    name="q354",
    ends={
        Property(name="xhtml_QType356", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow355", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp357: BinaryAssociation = BinaryAssociation(
    name="samp357",
    ends={
        Property(name="xhtml_SampType359", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow358", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd360: BinaryAssociation = BinaryAssociation(
    name="kbd360",
    ends={
        Property(name="xhtml_KbdType362", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow361", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strike339: BinaryAssociation = BinaryAssociation(
    name="strike339",
    ends={
        Property(name="xhtml_StrikeType341", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow340", type=xhtml_StrikeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em342: BinaryAssociation = BinaryAssociation(
    name="em342",
    ends={
        Property(name="xhtml_EmType344", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow343", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong345: BinaryAssociation = BinaryAssociation(
    name="strong345",
    ends={
        Property(name="xhtml_StrongType347", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow346", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr369: BinaryAssociation = BinaryAssociation(
    name="abbr369",
    ends={
        Property(name="xhtml_AbbrType371", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow370", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym372: BinaryAssociation = BinaryAssociation(
    name="acronym372",
    ends={
        Property(name="xhtml_AcronymType374", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow373", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub375: BinaryAssociation = BinaryAssociation(
    name="sub375",
    ends={
        Property(name="xhtml_SubType377", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow376", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup378: BinaryAssociation = BinaryAssociation(
    name="sup378",
    ends={
        Property(name="xhtml_SupType380", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow379", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var363: BinaryAssociation = BinaryAssociation(
    name="var363",
    ends={
        Property(name="xhtml_VarType365", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow364", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite366: BinaryAssociation = BinaryAssociation(
    name="cite366",
    ends={
        Property(name="xhtml_CiteType368", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow367", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p387: BinaryAssociation = BinaryAssociation(
    name="p387",
    ends={
        Property(name="xhtml_PType388", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1389: BinaryAssociation = BinaryAssociation(
    name="h1389",
    ends={
        Property(name="xhtml_H1Type391", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent390", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2392: BinaryAssociation = BinaryAssociation(
    name="h2392",
    ends={
        Property(name="xhtml_H2Type394", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent393", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3395: BinaryAssociation = BinaryAssociation(
    name="h3395",
    ends={
        Property(name="xhtml_H3Type397", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent396", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4398: BinaryAssociation = BinaryAssociation(
    name="h4398",
    ends={
        Property(name="xhtml_H4Type400", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent399", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5401: BinaryAssociation = BinaryAssociation(
    name="h5401",
    ends={
        Property(name="xhtml_H5Type403", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent402", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins381: BinaryAssociation = BinaryAssociation(
    name="ins381",
    ends={
        Property(name="xhtml_InsType383", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow382", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del384: BinaryAssociation = BinaryAssociation(
    name="del384",
    ends={
        Property(name="xhtml_DelType386", type=xhtml_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Flow385", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol413: BinaryAssociation = BinaryAssociation(
    name="ol413",
    ends={
        Property(name="xhtml_OlType415", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent414", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl416: BinaryAssociation = BinaryAssociation(
    name="dl416",
    ends={
        Property(name="xhtml_DlType418", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent417", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre419: BinaryAssociation = BinaryAssociation(
    name="pre419",
    ends={
        Property(name="xhtml_PreType421", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent420", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr422: BinaryAssociation = BinaryAssociation(
    name="hr422",
    ends={
        Property(name="xhtml_HrType424", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent423", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote425: BinaryAssociation = BinaryAssociation(
    name="blockquote425",
    ends={
        Property(name="xhtml_BlockquoteType427", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent426", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6404: BinaryAssociation = BinaryAssociation(
    name="h6404",
    ends={
        Property(name="xhtml_H6Type406", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent405", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div407: BinaryAssociation = BinaryAssociation(
    name="div407",
    ends={
        Property(name="xhtml_DivType409", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent408", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul410: BinaryAssociation = BinaryAssociation(
    name="ul410",
    ends={
        Property(name="xhtml_UlType412", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent411", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del437: BinaryAssociation = BinaryAssociation(
    name="del437",
    ends={
        Property(name="xhtml_DelType439", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent438", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address428: BinaryAssociation = BinaryAssociation(
    name="address428",
    ends={
        Property(name="xhtml_AddressType430", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent429", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table431: BinaryAssociation = BinaryAssociation(
    name="table431",
    ends={
        Property(name="xhtml_TableType433", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent432", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins434: BinaryAssociation = BinaryAssociation(
    name="ins434",
    ends={
        Property(name="xhtml_InsType436", type=xhtml_FormContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_FormContent435", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body440: BinaryAssociation = BinaryAssociation(
    name="body440",
    ends={
        Property(name="xhtml_BodyType442", type=xhtml_HtmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_HtmlType441", type=xhtml_BodyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
a443: BinaryAssociation = BinaryAssociation(
    name="a443",
    ends={
        Property(name="xhtml_AType444", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img454: BinaryAssociation = BinaryAssociation(
    name="img454",
    ends={
        Property(name="xhtml_ImgType456", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline455", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt457: BinaryAssociation = BinaryAssociation(
    name="tt457",
    ends={
        Property(name="xhtml_TtType459", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline458", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i460: BinaryAssociation = BinaryAssociation(
    name="i460",
    ends={
        Property(name="xhtml_IType462", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline461", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b463: BinaryAssociation = BinaryAssociation(
    name="b463",
    ends={
        Property(name="xhtml_BType465", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline464", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br445: BinaryAssociation = BinaryAssociation(
    name="br445",
    ends={
        Property(name="xhtml_BrType447", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline446", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span448: BinaryAssociation = BinaryAssociation(
    name="span448",
    ends={
        Property(name="xhtml_SpanType450", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline449", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object451: BinaryAssociation = BinaryAssociation(
    name="object451",
    ends={
        Property(name="xhtml_ObjectType453", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline452", type=xhtml_ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u472: BinaryAssociation = BinaryAssociation(
    name="u472",
    ends={
        Property(name="xhtml_UType474", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline473", type=xhtml_UType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strike475: BinaryAssociation = BinaryAssociation(
    name="strike475",
    ends={
        Property(name="xhtml_StrikeType477", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline476", type=xhtml_StrikeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em478: BinaryAssociation = BinaryAssociation(
    name="em478",
    ends={
        Property(name="xhtml_EmType480", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline479", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong481: BinaryAssociation = BinaryAssociation(
    name="strong481",
    ends={
        Property(name="xhtml_StrongType483", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline482", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big466: BinaryAssociation = BinaryAssociation(
    name="big466",
    ends={
        Property(name="xhtml_BigType468", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline467", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small469: BinaryAssociation = BinaryAssociation(
    name="small469",
    ends={
        Property(name="xhtml_SmallType471", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline470", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp493: BinaryAssociation = BinaryAssociation(
    name="samp493",
    ends={
        Property(name="xhtml_SampType495", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline494", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd496: BinaryAssociation = BinaryAssociation(
    name="kbd496",
    ends={
        Property(name="xhtml_KbdType498", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline497", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var499: BinaryAssociation = BinaryAssociation(
    name="var499",
    ends={
        Property(name="xhtml_VarType501", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline500", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite502: BinaryAssociation = BinaryAssociation(
    name="cite502",
    ends={
        Property(name="xhtml_CiteType504", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline503", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn484: BinaryAssociation = BinaryAssociation(
    name="dfn484",
    ends={
        Property(name="xhtml_DfnType486", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline485", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code487: BinaryAssociation = BinaryAssociation(
    name="code487",
    ends={
        Property(name="xhtml_CodeType489", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline488", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q490: BinaryAssociation = BinaryAssociation(
    name="q490",
    ends={
        Property(name="xhtml_QType492", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline491", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub511: BinaryAssociation = BinaryAssociation(
    name="sub511",
    ends={
        Property(name="xhtml_SubType513", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline512", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup514: BinaryAssociation = BinaryAssociation(
    name="sup514",
    ends={
        Property(name="xhtml_SupType516", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline515", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins517: BinaryAssociation = BinaryAssociation(
    name="ins517",
    ends={
        Property(name="xhtml_InsType519", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline518", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del520: BinaryAssociation = BinaryAssociation(
    name="del520",
    ends={
        Property(name="xhtml_DelType522", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline521", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr505: BinaryAssociation = BinaryAssociation(
    name="abbr505",
    ends={
        Property(name="xhtml_AbbrType507", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline506", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym508: BinaryAssociation = BinaryAssociation(
    name="acronym508",
    ends={
        Property(name="xhtml_AcronymType510", type=xhtml_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_Inline509", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param523: BinaryAssociation = BinaryAssociation(
    name="param523",
    ends={
        Property(name="xhtml_ParamType525", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType524", type=xhtml_ParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1529: BinaryAssociation = BinaryAssociation(
    name="h1529",
    ends={
        Property(name="xhtml_H1Type531", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType530", type=xhtml_H1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2532: BinaryAssociation = BinaryAssociation(
    name="h2532",
    ends={
        Property(name="xhtml_H2Type534", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType533", type=xhtml_H2Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3535: BinaryAssociation = BinaryAssociation(
    name="h3535",
    ends={
        Property(name="xhtml_H3Type537", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType536", type=xhtml_H3Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p526: BinaryAssociation = BinaryAssociation(
    name="p526",
    ends={
        Property(name="xhtml_PType528", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType527", type=xhtml_PType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5541: BinaryAssociation = BinaryAssociation(
    name="h5541",
    ends={
        Property(name="xhtml_H5Type543", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType542", type=xhtml_H5Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4538: BinaryAssociation = BinaryAssociation(
    name="h4538",
    ends={
        Property(name="xhtml_H4Type540", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType539", type=xhtml_H4Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ol553: BinaryAssociation = BinaryAssociation(
    name="ol553",
    ends={
        Property(name="xhtml_OlType555", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType554", type=xhtml_OlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dl556: BinaryAssociation = BinaryAssociation(
    name="dl556",
    ends={
        Property(name="xhtml_DlType558", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType557", type=xhtml_DlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre559: BinaryAssociation = BinaryAssociation(
    name="pre559",
    ends={
        Property(name="xhtml_PreType561", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType560", type=xhtml_PreType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hr562: BinaryAssociation = BinaryAssociation(
    name="hr562",
    ends={
        Property(name="xhtml_HrType564", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType563", type=xhtml_HrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockquote565: BinaryAssociation = BinaryAssociation(
    name="blockquote565",
    ends={
        Property(name="xhtml_BlockquoteType567", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType566", type=xhtml_BlockquoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6544: BinaryAssociation = BinaryAssociation(
    name="h6544",
    ends={
        Property(name="xhtml_H6Type546", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType545", type=xhtml_H6Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
div547: BinaryAssociation = BinaryAssociation(
    name="div547",
    ends={
        Property(name="xhtml_DivType549", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType548", type=xhtml_DivType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ul550: BinaryAssociation = BinaryAssociation(
    name="ul550",
    ends={
        Property(name="xhtml_UlType552", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType551", type=xhtml_UlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br577: BinaryAssociation = BinaryAssociation(
    name="br577",
    ends={
        Property(name="xhtml_BrType579", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType578", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address568: BinaryAssociation = BinaryAssociation(
    name="address568",
    ends={
        Property(name="xhtml_AddressType570", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType569", type=xhtml_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table571: BinaryAssociation = BinaryAssociation(
    name="table571",
    ends={
        Property(name="xhtml_TableType573", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType572", type=xhtml_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a574: BinaryAssociation = BinaryAssociation(
    name="a574",
    ends={
        Property(name="xhtml_AType576", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType575", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
img586: BinaryAssociation = BinaryAssociation(
    name="img586",
    ends={
        Property(name="xhtml_ImgType588", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType587", type=xhtml_ImgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt589: BinaryAssociation = BinaryAssociation(
    name="tt589",
    ends={
        Property(name="xhtml_TtType591", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType590", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i592: BinaryAssociation = BinaryAssociation(
    name="i592",
    ends={
        Property(name="xhtml_IType594", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType593", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b595: BinaryAssociation = BinaryAssociation(
    name="b595",
    ends={
        Property(name="xhtml_BType597", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType596", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big598: BinaryAssociation = BinaryAssociation(
    name="big598",
    ends={
        Property(name="xhtml_BigType600", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType599", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span580: BinaryAssociation = BinaryAssociation(
    name="span580",
    ends={
        Property(name="xhtml_SpanType582", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType581", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object584: BinaryAssociation = BinaryAssociation(
    name="object584",
    ends={
        Property(name="xhtml_ObjectType585", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType583", type=xhtml_ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em610: BinaryAssociation = BinaryAssociation(
    name="em610",
    ends={
        Property(name="xhtml_EmType612", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType611", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong613: BinaryAssociation = BinaryAssociation(
    name="strong613",
    ends={
        Property(name="xhtml_StrongType615", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType614", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn616: BinaryAssociation = BinaryAssociation(
    name="dfn616",
    ends={
        Property(name="xhtml_DfnType618", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType617", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code619: BinaryAssociation = BinaryAssociation(
    name="code619",
    ends={
        Property(name="xhtml_CodeType621", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType620", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small601: BinaryAssociation = BinaryAssociation(
    name="small601",
    ends={
        Property(name="xhtml_SmallType603", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType602", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u604: BinaryAssociation = BinaryAssociation(
    name="u604",
    ends={
        Property(name="xhtml_UType606", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType605", type=xhtml_UType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strike607: BinaryAssociation = BinaryAssociation(
    name="strike607",
    ends={
        Property(name="xhtml_StrikeType609", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType608", type=xhtml_StrikeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var631: BinaryAssociation = BinaryAssociation(
    name="var631",
    ends={
        Property(name="xhtml_VarType633", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType632", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite634: BinaryAssociation = BinaryAssociation(
    name="cite634",
    ends={
        Property(name="xhtml_CiteType636", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType635", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr637: BinaryAssociation = BinaryAssociation(
    name="abbr637",
    ends={
        Property(name="xhtml_AbbrType639", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType638", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym640: BinaryAssociation = BinaryAssociation(
    name="acronym640",
    ends={
        Property(name="xhtml_AcronymType642", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType641", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q622: BinaryAssociation = BinaryAssociation(
    name="q622",
    ends={
        Property(name="xhtml_QType624", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType623", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp625: BinaryAssociation = BinaryAssociation(
    name="samp625",
    ends={
        Property(name="xhtml_SampType627", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType626", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd628: BinaryAssociation = BinaryAssociation(
    name="kbd628",
    ends={
        Property(name="xhtml_KbdType630", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType629", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup646: BinaryAssociation = BinaryAssociation(
    name="sup646",
    ends={
        Property(name="xhtml_SupType648", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType647", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins649: BinaryAssociation = BinaryAssociation(
    name="ins649",
    ends={
        Property(name="xhtml_InsType651", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType650", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del652: BinaryAssociation = BinaryAssociation(
    name="del652",
    ends={
        Property(name="xhtml_DelType654", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType653", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub643: BinaryAssociation = BinaryAssociation(
    name="sub643",
    ends={
        Property(name="xhtml_SubType645", type=xhtml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_ObjectType644", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li655: BinaryAssociation = BinaryAssociation(
    name="li655",
    ends={
        Property(name="xhtml_LiType657", type=xhtml_OlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_OlType656", type=xhtml_LiType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
i663: BinaryAssociation = BinaryAssociation(
    name="i663",
    ends={
        Property(name="xhtml_PreContent664", type=xhtml_IType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xhtml_IType665", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1))
    }
)
b666: BinaryAssociation = BinaryAssociation(
    name="b666",
    ends={
        Property(name="xhtml_BType668", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent667", type=xhtml_BType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
big669: BinaryAssociation = BinaryAssociation(
    name="big669",
    ends={
        Property(name="xhtml_BigType671", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent670", type=xhtml_BigType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
small672: BinaryAssociation = BinaryAssociation(
    name="small672",
    ends={
        Property(name="xhtml_SmallType674", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent673", type=xhtml_SmallType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u675: BinaryAssociation = BinaryAssociation(
    name="u675",
    ends={
        Property(name="xhtml_UType677", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent676", type=xhtml_UType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a658: BinaryAssociation = BinaryAssociation(
    name="a658",
    ends={
        Property(name="xhtml_AType659", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent", type=xhtml_AType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tt660: BinaryAssociation = BinaryAssociation(
    name="tt660",
    ends={
        Property(name="xhtml_TtType662", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent661", type=xhtml_TtType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfn687: BinaryAssociation = BinaryAssociation(
    name="dfn687",
    ends={
        Property(name="xhtml_DfnType689", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent688", type=xhtml_DfnType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code690: BinaryAssociation = BinaryAssociation(
    name="code690",
    ends={
        Property(name="xhtml_CodeType692", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent691", type=xhtml_CodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
q693: BinaryAssociation = BinaryAssociation(
    name="q693",
    ends={
        Property(name="xhtml_QType695", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent694", type=xhtml_QType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samp696: BinaryAssociation = BinaryAssociation(
    name="samp696",
    ends={
        Property(name="xhtml_SampType698", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent697", type=xhtml_SampType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbd699: BinaryAssociation = BinaryAssociation(
    name="kbd699",
    ends={
        Property(name="xhtml_KbdType701", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent700", type=xhtml_KbdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strike678: BinaryAssociation = BinaryAssociation(
    name="strike678",
    ends={
        Property(name="xhtml_StrikeType680", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent679", type=xhtml_StrikeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
em681: BinaryAssociation = BinaryAssociation(
    name="em681",
    ends={
        Property(name="xhtml_EmType683", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent682", type=xhtml_EmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strong684: BinaryAssociation = BinaryAssociation(
    name="strong684",
    ends={
        Property(name="xhtml_StrongType686", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent685", type=xhtml_StrongType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr708: BinaryAssociation = BinaryAssociation(
    name="abbr708",
    ends={
        Property(name="xhtml_AbbrType710", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent709", type=xhtml_AbbrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronym711: BinaryAssociation = BinaryAssociation(
    name="acronym711",
    ends={
        Property(name="xhtml_AcronymType713", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent712", type=xhtml_AcronymType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub714: BinaryAssociation = BinaryAssociation(
    name="sub714",
    ends={
        Property(name="xhtml_SubType716", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent715", type=xhtml_SubType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sup717: BinaryAssociation = BinaryAssociation(
    name="sup717",
    ends={
        Property(name="xhtml_SupType719", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent718", type=xhtml_SupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
br720: BinaryAssociation = BinaryAssociation(
    name="br720",
    ends={
        Property(name="xhtml_BrType722", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent721", type=xhtml_BrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span723: BinaryAssociation = BinaryAssociation(
    name="span723",
    ends={
        Property(name="xhtml_SpanType725", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent724", type=xhtml_SpanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var702: BinaryAssociation = BinaryAssociation(
    name="var702",
    ends={
        Property(name="xhtml_VarType704", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent703", type=xhtml_VarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ins726: BinaryAssociation = BinaryAssociation(
    name="ins726",
    ends={
        Property(name="xhtml_InsType728", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent727", type=xhtml_InsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite705: BinaryAssociation = BinaryAssociation(
    name="cite705",
    ends={
        Property(name="xhtml_CiteType707", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent706", type=xhtml_CiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
del729: BinaryAssociation = BinaryAssociation(
    name="del729",
    ends={
        Property(name="xhtml_DelType731", type=xhtml_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_PreContent730", type=xhtml_DelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colgroup738: BinaryAssociation = BinaryAssociation(
    name="colgroup738",
    ends={
        Property(name="xhtml_ColgroupType740", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType739", type=xhtml_ColgroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caption732: BinaryAssociation = BinaryAssociation(
    name="caption732",
    ends={
        Property(name="xhtml_CaptionType734", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType733", type=xhtml_CaptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col735: BinaryAssociation = BinaryAssociation(
    name="col735",
    ends={
        Property(name="xhtml_ColType737", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType736", type=xhtml_ColType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead741: BinaryAssociation = BinaryAssociation(
    name="thead741",
    ends={
        Property(name="xhtml_TheadType743", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType742", type=xhtml_TheadType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tfoot744: BinaryAssociation = BinaryAssociation(
    name="tfoot744",
    ends={
        Property(name="xhtml_TfootType746", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType745", type=xhtml_TfootType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbody747: BinaryAssociation = BinaryAssociation(
    name="tbody747",
    ends={
        Property(name="xhtml_TbodyType749", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType748", type=xhtml_TbodyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr750: BinaryAssociation = BinaryAssociation(
    name="tr750",
    ends={
        Property(name="xhtml_TrType752", type=xhtml_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TableType751", type=xhtml_TrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr753: BinaryAssociation = BinaryAssociation(
    name="tr753",
    ends={
        Property(name="xhtml_TrType755", type=xhtml_TbodyType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TbodyType754", type=xhtml_TrType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr756: BinaryAssociation = BinaryAssociation(
    name="tr756",
    ends={
        Property(name="xhtml_TrType758", type=xhtml_TfootType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TfootType757", type=xhtml_TrType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr759: BinaryAssociation = BinaryAssociation(
    name="tr759",
    ends={
        Property(name="xhtml_TrType761", type=xhtml_TheadType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TheadType760", type=xhtml_TrType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
th762: BinaryAssociation = BinaryAssociation(
    name="th762",
    ends={
        Property(name="xhtml_ThType764", type=xhtml_TrType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TrType763", type=xhtml_ThType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
td765: BinaryAssociation = BinaryAssociation(
    name="td765",
    ends={
        Property(name="xhtml_TdType767", type=xhtml_TrType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_TrType766", type=xhtml_TdType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li768: BinaryAssociation = BinaryAssociation(
    name="li768",
    ends={
        Property(name="xhtml_LiType770", type=xhtml_UlType, multiplicity=Multiplicity(1, 1)),
        Property(name="xhtml_UlType769", type=xhtml_LiType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_xhtml_AbbrType_Inline = Generalization(general=Inline, specific=xhtml_AbbrType)
gen_xhtml_AcronymType_Inline = Generalization(general=Inline, specific=xhtml_AcronymType)
gen_xhtml_AddressType_Inline = Generalization(general=Inline, specific=xhtml_AddressType)
gen_xhtml_BigType_Inline = Generalization(general=Inline, specific=xhtml_BigType)
gen_xhtml_AType_AContent = Generalization(general=AContent, specific=xhtml_AType)
gen_xhtml_BlockquoteType_Block = Generalization(general=Block, specific=xhtml_BlockquoteType)
gen_xhtml_BodyType_Block = Generalization(general=Block, specific=xhtml_BodyType)
gen_xhtml_CaptionType_Inline = Generalization(general=Inline, specific=xhtml_CaptionType)
gen_xhtml_CiteType_Inline = Generalization(general=Inline, specific=xhtml_CiteType)
gen_xhtml_BType_Inline = Generalization(general=Inline, specific=xhtml_BType)
gen_xhtml_CodeType_Inline = Generalization(general=Inline, specific=xhtml_CodeType)
gen_xhtml_DdType_Flow = Generalization(general=Flow, specific=xhtml_DdType)
gen_xhtml_DfnType_Inline = Generalization(general=Inline, specific=xhtml_DfnType)
gen_xhtml_DivType_Flow = Generalization(general=Flow, specific=xhtml_DivType)
gen_xhtml_DelType_Flow = Generalization(general=Flow, specific=xhtml_DelType)
gen_xhtml_DtType_Inline = Generalization(general=Inline, specific=xhtml_DtType)
gen_xhtml_EmType_Inline = Generalization(general=Inline, specific=xhtml_EmType)
gen_xhtml_H1Type_Inline = Generalization(general=Inline, specific=xhtml_H1Type)
gen_xhtml_H2Type_Inline = Generalization(general=Inline, specific=xhtml_H2Type)
gen_xhtml_H4Type_Inline = Generalization(general=Inline, specific=xhtml_H4Type)
gen_xhtml_H5Type_Inline = Generalization(general=Inline, specific=xhtml_H5Type)
gen_xhtml_H3Type_Inline = Generalization(general=Inline, specific=xhtml_H3Type)
gen_xhtml_H6Type_Inline = Generalization(general=Inline, specific=xhtml_H6Type)
gen_xhtml_InsType_Flow = Generalization(general=Flow, specific=xhtml_InsType)
gen_xhtml_IType_Inline = Generalization(general=Inline, specific=xhtml_IType)
gen_xhtml_KbdType_Inline = Generalization(general=Inline, specific=xhtml_KbdType)
gen_xhtml_LiType_Flow = Generalization(general=Flow, specific=xhtml_LiType)
gen_xhtml_PreType_PreContent = Generalization(general=PreContent, specific=xhtml_PreType)
gen_xhtml_SampType_Inline = Generalization(general=Inline, specific=xhtml_SampType)
gen_xhtml_PType_Inline = Generalization(general=Inline, specific=xhtml_PType)
gen_xhtml_QType_Inline = Generalization(general=Inline, specific=xhtml_QType)
gen_xhtml_SmallType_Inline = Generalization(general=Inline, specific=xhtml_SmallType)
gen_xhtml_SpanType_Inline = Generalization(general=Inline, specific=xhtml_SpanType)
gen_xhtml_StrikeType_Inline = Generalization(general=Inline, specific=xhtml_StrikeType)
gen_xhtml_StrongType_Inline = Generalization(general=Inline, specific=xhtml_StrongType)
gen_xhtml_SubType_Inline = Generalization(general=Inline, specific=xhtml_SubType)
gen_xhtml_SupType_Inline = Generalization(general=Inline, specific=xhtml_SupType)
gen_xhtml_TdType_Flow = Generalization(general=Flow, specific=xhtml_TdType)
gen_xhtml_ThType_Flow = Generalization(general=Flow, specific=xhtml_ThType)
gen_xhtml_TtType_Inline = Generalization(general=Inline, specific=xhtml_TtType)
gen_xhtml_UType_Inline = Generalization(general=Inline, specific=xhtml_UType)
gen_xhtml_VarType_Inline = Generalization(general=Inline, specific=xhtml_VarType)

# Domain Model
domain_model = DomainModel(
    name="xhtml",
    types={xhtml_AbbrType, Inline, xhtml_ObjectType, xhtml_ImgType, xhtml_TtType, xhtml_AContent, xhtml_BrType, xhtml_SpanType, xhtml_StrikeType, xhtml_EmType, xhtml_StrongType, xhtml_IType, xhtml_BType, xhtml_BigType, xhtml_SmallType, xhtml_UType, xhtml_KbdType, xhtml_VarType, xhtml_CiteType, xhtml_DfnType, xhtml_CodeType, xhtml_QType, xhtml_SampType, xhtml_SupType, xhtml_InsType, xhtml_AcronymType, xhtml_SubType, xhtml_DelType, xhtml_AddressType, xhtml_AType, AContent, xhtml_H2Type, xhtml_H3Type, xhtml_H4Type, xhtml_H5Type, xhtml_H6Type, xhtml_Block, xhtml_PType, xhtml_H1Type, xhtml_DlType, xhtml_PreType, xhtml_HrType, xhtml_BlockquoteType, xhtml_TableType, xhtml_DivType, xhtml_UlType, xhtml_OlType, Block, xhtml_BodyType, xhtml_CaptionType, xhtml_ColgroupType, xhtml_ColType, xhtml_DdType, Flow, xhtml_DocumentRoot, xhtml_EStringToStringMapEntry, xhtml_DtType, xhtml_LiType, xhtml_HtmlType, xhtml_ParamType, xhtml_TfootType, xhtml_ThType, xhtml_TheadType, xhtml_TrType, xhtml_TbodyType, xhtml_TdType, xhtml_Flow, xhtml_FormContent, xhtml_Inline, xhtml_PreContent, PreContent, AlignType, DeclareType, IsmapType, Scope, Shape, ValignType, ValuetypeType},
    associations={object3, img5, tt7, br0, span1, strike19, em21, strong23, i9, b11, big13, small15, u17, kbd33, var35, cite37, dfn25, code27, q29, samp31, sub43, sup45, ins47, abbr39, acronym41, del49, h254, h356, h458, h560, h662, p51, h152, dl70, pre72, hr74, blockquote76, address78, div64, ul66, ol68, table80, ins82, del85, col88, xMLNSPrefixMap93, xSISchemaLocation94, a97, abbr99, acronym102, dt89, dd91, big111, blockquote114, body117, br119, caption122, cite124, address105, b108, dd136, del139, dfn142, div145, code127, col130, colgroup133, h2160, h3163, h4166, h5169, h6172, hr175, dl148, dt151, em154, h1157, kbd189, li192, object194, ol197, html178, i180, img183, ins186, pre205, q208, samp211, small214, p200, param203, strike220, strong223, sub226, sup229, span217, tfoot239, th241, thead243, tr245, tt247, table232, tbody235, td237, var256, u250, ul253, h1261, h2264, h3267, h4270, h5273, h6276, p259, ol285, dl288, pre291, hr294, div279, ul282, a306, br309, span312, object315, img318, blockquote297, address300, table303, b327, big330, small333, u336, tt321, i324, dfn348, code351, q354, samp357, kbd360, strike339, em342, strong345, abbr369, acronym372, sub375, sup378, var363, cite366, p387, h1389, h2392, h3395, h4398, h5401, ins381, del384, ol413, dl416, pre419, hr422, blockquote425, h6404, div407, ul410, del437, address428, table431, ins434, body440, a443, img454, tt457, i460, b463, br445, span448, object451, u472, strike475, em478, strong481, big466, small469, samp493, kbd496, var499, cite502, dfn484, code487, q490, sub511, sup514, ins517, del520, abbr505, acronym508, param523, h1529, h2532, h3535, p526, h5541, h4538, ol553, dl556, pre559, hr562, blockquote565, h6544, div547, ul550, br577, address568, table571, a574, img586, tt589, i592, b595, big598, span580, object584, em610, strong613, dfn616, code619, small601, u604, strike607, var631, cite634, abbr637, acronym640, q622, samp625, kbd628, sup646, ins649, del652, sub643, li655, i663, b666, big669, small672, u675, a658, tt660, dfn687, code690, q693, samp696, kbd699, strike678, em681, strong684, abbr708, acronym711, sub714, sup717, br720, span723, var702, ins726, cite705, del729, colgroup738, caption732, col735, thead741, tfoot744, tbody747, tr750, tr753, tr756, tr759, th762, td765, li768},
    generalizations={gen_xhtml_AbbrType_Inline, gen_xhtml_AcronymType_Inline, gen_xhtml_AddressType_Inline, gen_xhtml_BigType_Inline, gen_xhtml_AType_AContent, gen_xhtml_BlockquoteType_Block, gen_xhtml_BodyType_Block, gen_xhtml_CaptionType_Inline, gen_xhtml_CiteType_Inline, gen_xhtml_BType_Inline, gen_xhtml_CodeType_Inline, gen_xhtml_DdType_Flow, gen_xhtml_DfnType_Inline, gen_xhtml_DivType_Flow, gen_xhtml_DelType_Flow, gen_xhtml_DtType_Inline, gen_xhtml_EmType_Inline, gen_xhtml_H1Type_Inline, gen_xhtml_H2Type_Inline, gen_xhtml_H4Type_Inline, gen_xhtml_H5Type_Inline, gen_xhtml_H3Type_Inline, gen_xhtml_H6Type_Inline, gen_xhtml_InsType_Flow, gen_xhtml_IType_Inline, gen_xhtml_KbdType_Inline, gen_xhtml_LiType_Flow, gen_xhtml_PreType_PreContent, gen_xhtml_SampType_Inline, gen_xhtml_PType_Inline, gen_xhtml_QType_Inline, gen_xhtml_SmallType_Inline, gen_xhtml_SpanType_Inline, gen_xhtml_StrikeType_Inline, gen_xhtml_StrongType_Inline, gen_xhtml_SubType_Inline, gen_xhtml_SupType_Inline, gen_xhtml_TdType_Flow, gen_xhtml_ThType_Flow, gen_xhtml_TtType_Inline, gen_xhtml_UType_Inline, gen_xhtml_VarType_Inline},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)