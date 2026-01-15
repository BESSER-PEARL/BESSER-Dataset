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
Docbook_AbstractType = Class(name="Docbook::AbstractType")
Docbook_ParaType = Class(name="Docbook::ParaType")
Docbook_AddressType = Class(name="Docbook::AddressType")
Docbook_ArgType = Class(name="Docbook::ArgType")
Docbook_OptionType = Class(name="Docbook::OptionType")
Docbook_ReplaceableType = Class(name="Docbook::ReplaceableType")
Docbook_OtheraddrType = Class(name="Docbook::OtheraddrType")
Docbook_AuthorinitialsType = Class(name="Docbook::AuthorinitialsType")
Docbook_AuthorType = Class(name="Docbook::AuthorType")
Docbook_PersonnameType = Class(name="Docbook::PersonnameType")
Docbook_InfoType = Class(name="Docbook::InfoType")
Docbook_BookType = Class(name="Docbook::BookType")
Docbook_PrefaceType = Class(name="Docbook::PrefaceType")
Docbook_ChapterType = Class(name="Docbook::ChapterType")
Docbook_ReferenceType = Class(name="Docbook::ReferenceType")
Docbook_NoteType = Class(name="Docbook::NoteType")
Docbook_SectionType = Class(name="Docbook::SectionType")
Docbook_ColspecType = Class(name="Docbook::ColspecType")
Docbook_TitleType = Class(name="Docbook::TitleType")
Docbook_ConfgroupType = Class(name="Docbook::ConfgroupType")
Docbook_CmdsynopsisType = Class(name="Docbook::CmdsynopsisType")
Docbook_CommandType = Class(name="Docbook::CommandType")
Docbook_CopyrightType = Class(name="Docbook::CopyrightType")
Docbook_EStringToStringMapEntry = Class(name="Docbook::EStringToStringMapEntry")
Docbook_DateType = Class(name="Docbook::DateType")
Docbook_DocumentRoot = Class(name="Docbook::DocumentRoot")
Docbook_EmphasisType = Class(name="Docbook::EmphasisType")
Docbook_EntryType = Class(name="Docbook::EntryType")
Docbook_FootnoteType = Class(name="Docbook::FootnoteType")
Docbook_ImagedataType = Class(name="Docbook::ImagedataType")
Docbook_ImageobjectType = Class(name="Docbook::ImageobjectType")
Docbook_FigureType = Class(name="Docbook::FigureType")
Docbook_ItemizedlistType = Class(name="Docbook::ItemizedlistType")
Docbook_KeywordsetType = Class(name="Docbook::KeywordsetType")
Docbook_ImportantType = Class(name="Docbook::ImportantType")
Docbook_InformaltableType = Class(name="Docbook::InformaltableType")
Docbook_ListitemType = Class(name="Docbook::ListitemType")
Docbook_LiteralType = Class(name="Docbook::LiteralType")
Docbook_MediaobjectType = Class(name="Docbook::MediaobjectType")
Docbook_LinkType = Class(name="Docbook::LinkType")
Docbook_OrderedlistType = Class(name="Docbook::OrderedlistType")
Docbook_ProgramlistingType = Class(name="Docbook::ProgramlistingType")
Docbook_PhraseType = Class(name="Docbook::PhraseType")
Docbook_RowType = Class(name="Docbook::RowType")
Docbook_PublisherType = Class(name="Docbook::PublisherType")
Docbook_TableType = Class(name="Docbook::TableType")
Docbook_TbodyType = Class(name="Docbook::TbodyType")
Docbook_TipType = Class(name="Docbook::TipType")
Docbook_TgroupType = Class(name="Docbook::TgroupType")
Docbook_TheadType = Class(name="Docbook::TheadType")
Docbook_UlinkType = Class(name="Docbook::UlinkType")
Docbook_EnvarType = Class(name="Docbook::EnvarType")
Docbook_ExampleType = Class(name="Docbook::ExampleType")
Docbook_FirstnameType = Class(name="Docbook::FirstnameType")
Docbook_FileNameType = Class(name="Docbook::FileNameType")
Docbook_FunctionType = Class(name="Docbook::FunctionType")
Docbook_FuncprototypeType = Class(name="Docbook::FuncprototypeType")
Docbook_ParamdefType = Class(name="Docbook::ParamdefType")
Docbook_FuncdefType = Class(name="Docbook::FuncdefType")
Docbook_FuncsynopsisType = Class(name="Docbook::FuncsynopsisType")
Docbook_SubtitleType = Class(name="Docbook::SubtitleType")
Docbook_RevhistoryType = Class(name="Docbook::RevhistoryType")
Docbook_LegalNoticeType = Class(name="Docbook::LegalNoticeType")
ItemizedlistType = Class(name="ItemizedlistType")
Docbook_ParameterType = Class(name="Docbook::ParameterType")
Docbook_SurnameType = Class(name="Docbook::SurnameType")
Docbook_VariableListType = Class(name="Docbook::VariableListType")
Docbook_RefMetaType = Class(name="Docbook::RefMetaType")
Docbook_RefNameDivType = Class(name="Docbook::RefNameDivType")
Docbook_RefSynopsisDivType = Class(name="Docbook::RefSynopsisDivType")
Docbook_RefSect1Type = Class(name="Docbook::RefSect1Type")
Docbook_RefEntryType = Class(name="Docbook::RefEntryType")
Docbook_RefEntryTitleType = Class(name="Docbook::RefEntryTitleType")
Docbook_SegmentedListType = Class(name="Docbook::SegmentedListType")
Docbook_RevisionType = Class(name="Docbook::RevisionType")
Docbook_RevdescriptionType = Class(name="Docbook::RevdescriptionType")
Docbook_RevnumberType = Class(name="Docbook::RevnumberType")
Docbook_SegListItemType = Class(name="Docbook::SegListItemType")
Docbook_SegType = Class(name="Docbook::SegType")
Docbook_TermType = Class(name="Docbook::TermType")
Docbook_VarListEntryType = Class(name="Docbook::VarListEntryType")

# Docbook_AbstractType class attributes and methods

# Docbook_ParaType class attributes and methods
Docbook_ParaType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ParaType_group: Property = Property(name="group", type=StringType)
Docbook_ParaType_role: Property = Property(name="role", type=StringType)
Docbook_ParaType_id: Property = Property(name="id", type=StringType)
Docbook_ParaType.attributes={Docbook_ParaType_id, Docbook_ParaType_role, Docbook_ParaType_group, Docbook_ParaType_mixed}

# Docbook_AddressType class attributes and methods
Docbook_AddressType_state: Property = Property(name="state", type=StringType)
Docbook_AddressType_email: Property = Property(name="email", type=StringType)
Docbook_AddressType_format: Property = Property(name="format", type=StringType)
Docbook_AddressType.attributes={Docbook_AddressType_state, Docbook_AddressType_email, Docbook_AddressType_format}

# Docbook_ArgType class attributes and methods
Docbook_ArgType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ArgType_choice: Property = Property(name="choice", type=StringType)
Docbook_ArgType_rep: Property = Property(name="rep", type=StringType)
Docbook_ArgType.attributes={Docbook_ArgType_mixed, Docbook_ArgType_choice, Docbook_ArgType_rep}

# Docbook_OptionType class attributes and methods
Docbook_OptionType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_OptionType.attributes={Docbook_OptionType_mixed}

# Docbook_ReplaceableType class attributes and methods
Docbook_ReplaceableType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ReplaceableType.attributes={Docbook_ReplaceableType_mixed}

# Docbook_OtheraddrType class attributes and methods

# Docbook_AuthorinitialsType class attributes and methods
Docbook_AuthorinitialsType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_AuthorinitialsType.attributes={Docbook_AuthorinitialsType_mixed}

# Docbook_AuthorType class attributes and methods
Docbook_AuthorType_contrib: Property = Property(name="contrib", type=StringType)
Docbook_AuthorType.attributes={Docbook_AuthorType_contrib}

# Docbook_PersonnameType class attributes and methods

# Docbook_InfoType class attributes and methods
Docbook_InfoType_pubdate: Property = Property(name="pubdate", type=StringType)
Docbook_InfoType_bibliomisc: Property = Property(name="bibliomisc", type=StringType)
Docbook_InfoType_date: Property = Property(name="date", type=StringType)
Docbook_InfoType_group: Property = Property(name="group", type=StringType)
Docbook_InfoType_releaseinfo: Property = Property(name="releaseinfo", type=StringType)
Docbook_InfoType_productname: Property = Property(name="productname", type=StringType)
Docbook_InfoType.attributes={Docbook_InfoType_group, Docbook_InfoType_releaseinfo, Docbook_InfoType_productname, Docbook_InfoType_pubdate, Docbook_InfoType_date, Docbook_InfoType_bibliomisc}

# Docbook_BookType class attributes and methods
Docbook_BookType_lang: Property = Property(name="lang", type=StringType)
Docbook_BookType_version: Property = Property(name="version", type=StringType)
Docbook_BookType_label: Property = Property(name="label", type=StringType)
Docbook_BookType.attributes={Docbook_BookType_lang, Docbook_BookType_label, Docbook_BookType_version}

# Docbook_PrefaceType class attributes and methods

# Docbook_ChapterType class attributes and methods
Docbook_ChapterType_annotations: Property = Property(name="annotations", type=StringType)
Docbook_ChapterType.attributes={Docbook_ChapterType_annotations}

# Docbook_ReferenceType class attributes and methods
Docbook_ReferenceType_version: Property = Property(name="version", type=StringType)
Docbook_ReferenceType.attributes={Docbook_ReferenceType_version}

# Docbook_NoteType class attributes and methods
Docbook_NoteType_group: Property = Property(name="group", type=StringType)
Docbook_NoteType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_NoteType.attributes={Docbook_NoteType_group, Docbook_NoteType_mixed}

# Docbook_SectionType class attributes and methods
Docbook_SectionType_group: Property = Property(name="group", type=StringType)
Docbook_SectionType_caution: Property = Property(name="caution", type=StringType)
Docbook_SectionType_warning: Property = Property(name="warning", type=StringType)
Docbook_SectionType_annotations: Property = Property(name="annotations", type=StringType)
Docbook_SectionType.attributes={Docbook_SectionType_annotations, Docbook_SectionType_caution, Docbook_SectionType_group, Docbook_SectionType_warning}

# Docbook_ColspecType class attributes and methods
Docbook_ColspecType_colname: Property = Property(name="colname", type=StringType)
Docbook_ColspecType_colwidth: Property = Property(name="colwidth", type=StringType)
Docbook_ColspecType.attributes={Docbook_ColspecType_colname, Docbook_ColspecType_colwidth}

# Docbook_TitleType class attributes and methods
Docbook_TitleType_group: Property = Property(name="group", type=StringType)
Docbook_TitleType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_TitleType.attributes={Docbook_TitleType_group, Docbook_TitleType_mixed}

# Docbook_ConfgroupType class attributes and methods
Docbook_ConfgroupType_conftitle: Property = Property(name="conftitle", type=StringType)
Docbook_ConfgroupType_confnum: Property = Property(name="confnum", type=StringType)
Docbook_ConfgroupType_confsponsor: Property = Property(name="confsponsor", type=StringType)
Docbook_ConfgroupType.attributes={Docbook_ConfgroupType_conftitle, Docbook_ConfgroupType_confsponsor, Docbook_ConfgroupType_confnum}

# Docbook_CmdsynopsisType class attributes and methods

# Docbook_CommandType class attributes and methods
Docbook_CommandType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_CommandType.attributes={Docbook_CommandType_mixed}

# Docbook_CopyrightType class attributes and methods
Docbook_CopyrightType_group: Property = Property(name="group", type=StringType)
Docbook_CopyrightType_year: Property = Property(name="year", type=StringType)
Docbook_CopyrightType_holder: Property = Property(name="holder", type=StringType)
Docbook_CopyrightType.attributes={Docbook_CopyrightType_group, Docbook_CopyrightType_holder, Docbook_CopyrightType_year}

# Docbook_EStringToStringMapEntry class attributes and methods

# Docbook_DateType class attributes and methods
Docbook_DateType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_DateType.attributes={Docbook_DateType_mixed}

# Docbook_DocumentRoot class attributes and methods
Docbook_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
Docbook_DocumentRoot_bibliomisc: Property = Property(name="bibliomisc", type=StringType)
Docbook_DocumentRoot_confnum: Property = Property(name="confnum", type=StringType)
Docbook_DocumentRoot_caution: Property = Property(name="caution", type=StringType)
Docbook_DocumentRoot_date: Property = Property(name="date", type=StringType)
Docbook_DocumentRoot_confsponsor: Property = Property(name="confsponsor", type=StringType)
Docbook_DocumentRoot_conftitle: Property = Property(name="conftitle", type=StringType)
Docbook_DocumentRoot_firstname: Property = Property(name="firstname", type=StringType)
Docbook_DocumentRoot_keyword: Property = Property(name="keyword", type=StringType)
Docbook_DocumentRoot_pubdate: Property = Property(name="pubdate", type=StringType)
Docbook_DocumentRoot_publishername: Property = Property(name="publishername", type=StringType)
Docbook_DocumentRoot_state: Property = Property(name="state", type=StringType)
Docbook_DocumentRoot_subtitle: Property = Property(name="subtitle", type=StringType)
Docbook_DocumentRoot_superscript: Property = Property(name="superscript", type=StringType)
Docbook_DocumentRoot_warning: Property = Property(name="warning", type=StringType)
Docbook_DocumentRoot.attributes={Docbook_DocumentRoot_mixed, Docbook_DocumentRoot_firstname, Docbook_DocumentRoot_publishername, Docbook_DocumentRoot_caution, Docbook_DocumentRoot_subtitle, Docbook_DocumentRoot_keyword, Docbook_DocumentRoot_superscript, Docbook_DocumentRoot_confsponsor, Docbook_DocumentRoot_pubdate, Docbook_DocumentRoot_confnum, Docbook_DocumentRoot_date, Docbook_DocumentRoot_warning, Docbook_DocumentRoot_bibliomisc, Docbook_DocumentRoot_conftitle, Docbook_DocumentRoot_state}

# Docbook_EmphasisType class attributes and methods
Docbook_EmphasisType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_EmphasisType_role: Property = Property(name="role", type=StringType)
Docbook_EmphasisType.attributes={Docbook_EmphasisType_role, Docbook_EmphasisType_mixed}

# Docbook_EntryType class attributes and methods
Docbook_EntryType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_EntryType_valign: Property = Property(name="valign", type=StringType)
Docbook_EntryType_align: Property = Property(name="align", type=StringType)
Docbook_EntryType_morerows: Property = Property(name="morerows", type=StringType)
Docbook_EntryType_nameend: Property = Property(name="nameend", type=StringType)
Docbook_EntryType_namest: Property = Property(name="namest", type=StringType)
Docbook_EntryType.attributes={Docbook_EntryType_mixed, Docbook_EntryType_align, Docbook_EntryType_nameend, Docbook_EntryType_namest, Docbook_EntryType_valign, Docbook_EntryType_morerows}

# Docbook_FootnoteType class attributes and methods
Docbook_FootnoteType_id: Property = Property(name="id", type=StringType)
Docbook_FootnoteType.attributes={Docbook_FootnoteType_id}

# Docbook_ImagedataType class attributes and methods
Docbook_ImagedataType_depth: Property = Property(name="depth", type=StringType)
Docbook_ImagedataType_fileref: Property = Property(name="fileref", type=StringType)
Docbook_ImagedataType_width: Property = Property(name="width", type=StringType)
Docbook_ImagedataType_align: Property = Property(name="align", type=StringType)
Docbook_ImagedataType_scale: Property = Property(name="scale", type=StringType)
Docbook_ImagedataType.attributes={Docbook_ImagedataType_depth, Docbook_ImagedataType_align, Docbook_ImagedataType_scale, Docbook_ImagedataType_width, Docbook_ImagedataType_fileref}

# Docbook_ImageobjectType class attributes and methods

# Docbook_FigureType class attributes and methods
Docbook_FigureType_float: Property = Property(name="float", type=StringType)
Docbook_FigureType_id: Property = Property(name="id", type=StringType)
Docbook_FigureType.attributes={Docbook_FigureType_float, Docbook_FigureType_id}

# Docbook_ItemizedlistType class attributes and methods

# Docbook_KeywordsetType class attributes and methods
Docbook_KeywordsetType_keyword: Property = Property(name="keyword", type=StringType)
Docbook_KeywordsetType.attributes={Docbook_KeywordsetType_keyword}

# Docbook_ImportantType class attributes and methods
Docbook_ImportantType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ImportantType_group: Property = Property(name="group", type=StringType)
Docbook_ImportantType.attributes={Docbook_ImportantType_group, Docbook_ImportantType_mixed}

# Docbook_InformaltableType class attributes and methods

# Docbook_ListitemType class attributes and methods

# Docbook_LiteralType class attributes and methods
Docbook_LiteralType_value: Property = Property(name="value", type=StringType)
Docbook_LiteralType_moreinfo: Property = Property(name="moreinfo", type=StringType)
Docbook_LiteralType.attributes={Docbook_LiteralType_moreinfo, Docbook_LiteralType_value}

# Docbook_MediaobjectType class attributes and methods

# Docbook_LinkType class attributes and methods
Docbook_LinkType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_LinkType_value: Property = Property(name="value", type=StringType)
Docbook_LinkType_linkend: Property = Property(name="linkend", type=StringType)
Docbook_LinkType.attributes={Docbook_LinkType_mixed, Docbook_LinkType_linkend, Docbook_LinkType_value}

# Docbook_OrderedlistType class attributes and methods
Docbook_OrderedlistType_inheritnum: Property = Property(name="inheritnum", type=StringType)
Docbook_OrderedlistType_continuation: Property = Property(name="continuation", type=StringType)
Docbook_OrderedlistType.attributes={Docbook_OrderedlistType_continuation, Docbook_OrderedlistType_inheritnum}

# Docbook_ProgramlistingType class attributes and methods
Docbook_ProgramlistingType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ProgramlistingType_group: Property = Property(name="group", type=StringType)
Docbook_ProgramlistingType_format: Property = Property(name="format", type=StringType)
Docbook_ProgramlistingType_language: Property = Property(name="language", type=StringType)
Docbook_ProgramlistingType_linenumbering: Property = Property(name="linenumbering", type=StringType)
Docbook_ProgramlistingType_superscript: Property = Property(name="superscript", type=StringType)
Docbook_ProgramlistingType.attributes={Docbook_ProgramlistingType_linenumbering, Docbook_ProgramlistingType_format, Docbook_ProgramlistingType_superscript, Docbook_ProgramlistingType_mixed, Docbook_ProgramlistingType_language, Docbook_ProgramlistingType_group}

# Docbook_PhraseType class attributes and methods
Docbook_PhraseType_id: Property = Property(name="id", type=StringType)
Docbook_PhraseType.attributes={Docbook_PhraseType_id}

# Docbook_RowType class attributes and methods

# Docbook_PublisherType class attributes and methods
Docbook_PublisherType_publishername: Property = Property(name="publishername", type=StringType)
Docbook_PublisherType.attributes={Docbook_PublisherType_publishername}

# Docbook_TableType class attributes and methods
Docbook_TableType_id: Property = Property(name="id", type=StringType)
Docbook_TableType.attributes={Docbook_TableType_id}

# Docbook_TbodyType class attributes and methods

# Docbook_TipType class attributes and methods
Docbook_TipType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_TipType.attributes={Docbook_TipType_mixed}

# Docbook_TgroupType class attributes and methods
Docbook_TgroupType_colseq: Property = Property(name="colseq", type=StringType)
Docbook_TgroupType_rowseq: Property = Property(name="rowseq", type=StringType)
Docbook_TgroupType_cols: Property = Property(name="cols", type=StringType)
Docbook_TgroupType_align: Property = Property(name="align", type=StringType)
Docbook_TgroupType.attributes={Docbook_TgroupType_cols, Docbook_TgroupType_rowseq, Docbook_TgroupType_colseq, Docbook_TgroupType_align}

# Docbook_TheadType class attributes and methods

# Docbook_UlinkType class attributes and methods
Docbook_UlinkType_type: Property = Property(name="type", type=StringType)
Docbook_UlinkType_url: Property = Property(name="url", type=StringType)
Docbook_UlinkType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_UlinkType.attributes={Docbook_UlinkType_type, Docbook_UlinkType_url, Docbook_UlinkType_mixed}

# Docbook_EnvarType class attributes and methods
Docbook_EnvarType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_EnvarType.attributes={Docbook_EnvarType_mixed}

# Docbook_ExampleType class attributes and methods
Docbook_ExampleType_id: Property = Property(name="id", type=StringType)
Docbook_ExampleType.attributes={Docbook_ExampleType_id}

# Docbook_FirstnameType class attributes and methods
Docbook_FirstnameType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_FirstnameType.attributes={Docbook_FirstnameType_mixed}

# Docbook_FileNameType class attributes and methods
Docbook_FileNameType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_FileNameType.attributes={Docbook_FileNameType_mixed}

# Docbook_FunctionType class attributes and methods
Docbook_FunctionType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_FunctionType.attributes={Docbook_FunctionType_mixed}

# Docbook_FuncprototypeType class attributes and methods

# Docbook_ParamdefType class attributes and methods
Docbook_ParamdefType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ParamdefType.attributes={Docbook_ParamdefType_mixed}

# Docbook_FuncdefType class attributes and methods
Docbook_FuncdefType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_FuncdefType.attributes={Docbook_FuncdefType_mixed}

# Docbook_FuncsynopsisType class attributes and methods

# Docbook_SubtitleType class attributes and methods
Docbook_SubtitleType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_SubtitleType_group: Property = Property(name="group", type=StringType)
Docbook_SubtitleType.attributes={Docbook_SubtitleType_mixed, Docbook_SubtitleType_group}

# Docbook_RevhistoryType class attributes and methods

# Docbook_LegalNoticeType class attributes and methods
Docbook_LegalNoticeType_group: Property = Property(name="group", type=StringType)
Docbook_LegalNoticeType.attributes={Docbook_LegalNoticeType_group}

# ItemizedlistType class attributes and methods

# Docbook_ParameterType class attributes and methods
Docbook_ParameterType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_ParameterType.attributes={Docbook_ParameterType_mixed}

# Docbook_SurnameType class attributes and methods
Docbook_SurnameType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_SurnameType.attributes={Docbook_SurnameType_mixed}

# Docbook_VariableListType class attributes and methods

# Docbook_RefMetaType class attributes and methods
Docbook_RefMetaType_manvolnum: Property = Property(name="manvolnum", type=StringType)
Docbook_RefMetaType.attributes={Docbook_RefMetaType_manvolnum}

# Docbook_RefNameDivType class attributes and methods
Docbook_RefNameDivType_refname: Property = Property(name="refname", type=StringType)
Docbook_RefNameDivType_refpurpose: Property = Property(name="refpurpose", type=StringType)
Docbook_RefNameDivType_refclass: Property = Property(name="refclass", type=StringType)
Docbook_RefNameDivType.attributes={Docbook_RefNameDivType_refname, Docbook_RefNameDivType_refpurpose, Docbook_RefNameDivType_refclass}

# Docbook_RefSynopsisDivType class attributes and methods

# Docbook_RefSect1Type class attributes and methods
Docbook_RefSect1Type_group: Property = Property(name="group", type=StringType)
Docbook_RefSect1Type_id: Property = Property(name="id", type=StringType)
Docbook_RefSect1Type.attributes={Docbook_RefSect1Type_id, Docbook_RefSect1Type_group}

# Docbook_RefEntryType class attributes and methods
Docbook_RefEntryType_version: Property = Property(name="version", type=StringType)
Docbook_RefEntryType.attributes={Docbook_RefEntryType_version}

# Docbook_RefEntryTitleType class attributes and methods
Docbook_RefEntryTitleType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_RefEntryTitleType.attributes={Docbook_RefEntryTitleType_mixed}

# Docbook_SegmentedListType class attributes and methods
Docbook_SegmentedListType_group: Property = Property(name="group", type=StringType)
Docbook_SegmentedListType_segtitle: Property = Property(name="segtitle", type=StringType)
Docbook_SegmentedListType.attributes={Docbook_SegmentedListType_group, Docbook_SegmentedListType_segtitle}

# Docbook_RevisionType class attributes and methods

# Docbook_RevdescriptionType class attributes and methods
Docbook_RevdescriptionType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_RevdescriptionType.attributes={Docbook_RevdescriptionType_mixed}

# Docbook_RevnumberType class attributes and methods
Docbook_RevnumberType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_RevnumberType.attributes={Docbook_RevnumberType_mixed}

# Docbook_SegListItemType class attributes and methods

# Docbook_SegType class attributes and methods
Docbook_SegType_group: Property = Property(name="group", type=StringType)
Docbook_SegType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_SegType_errorcode: Property = Property(name="errorcode", type=StringType)
Docbook_SegType_errortext: Property = Property(name="errortext", type=StringType)
Docbook_SegType.attributes={Docbook_SegType_mixed, Docbook_SegType_group, Docbook_SegType_errorcode, Docbook_SegType_errortext}

# Docbook_TermType class attributes and methods
Docbook_TermType_mixed: Property = Property(name="mixed", type=StringType)
Docbook_TermType.attributes={Docbook_TermType_mixed}

# Docbook_VarListEntryType class attributes and methods
Docbook_VarListEntryType_spacing: Property = Property(name="spacing", type=StringType)
Docbook_VarListEntryType_termlength: Property = Property(name="termlength", type=StringType)
Docbook_VarListEntryType.attributes={Docbook_VarListEntryType_termlength, Docbook_VarListEntryType_spacing}

# Relationships
para0: BinaryAssociation = BinaryAssociation(
    name="para0",
    ends={
        Property(name="Docbook_ParaType", type=Docbook_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_AbstractType", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
option2: BinaryAssociation = BinaryAssociation(
    name="option2",
    ends={
        Property(name="Docbook_OptionType", type=Docbook_ArgType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ArgType", type=Docbook_OptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
otheraddr1: BinaryAssociation = BinaryAssociation(
    name="otheraddr1",
    ends={
        Property(name="Docbook_OtheraddrType", type=Docbook_AddressType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_AddressType", type=Docbook_OtheraddrType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
personname5: BinaryAssociation = BinaryAssociation(
    name="personname5",
    ends={
        Property(name="Docbook_PersonnameType", type=Docbook_AuthorType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_AuthorType", type=Docbook_PersonnameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replaceable3: BinaryAssociation = BinaryAssociation(
    name="replaceable3",
    ends={
        Property(name="Docbook_ReplaceableType", type=Docbook_ArgType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ArgType4", type=Docbook_ReplaceableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
info9: BinaryAssociation = BinaryAssociation(
    name="info9",
    ends={
        Property(name="Docbook_InfoType", type=Docbook_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_BookType", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
address6: BinaryAssociation = BinaryAssociation(
    name="address6",
    ends={
        Property(name="Docbook_AddressType8", type=Docbook_AuthorType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_AuthorType7", type=Docbook_AddressType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference14: BinaryAssociation = BinaryAssociation(
    name="reference14",
    ends={
        Property(name="Docbook_BookType15", type=Docbook_ReferenceType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Docbook_ReferenceType", type=Docbook_BookType, multiplicity=Multiplicity(1, 1))
    }
)
preface10: BinaryAssociation = BinaryAssociation(
    name="preface10",
    ends={
        Property(name="Docbook_PrefaceType", type=Docbook_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_BookType11", type=Docbook_PrefaceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
chapter12: BinaryAssociation = BinaryAssociation(
    name="chapter12",
    ends={
        Property(name="Docbook_ChapterType", type=Docbook_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_BookType13", type=Docbook_ChapterType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
note21: BinaryAssociation = BinaryAssociation(
    name="note21",
    ends={
        Property(name="Docbook_NoteType", type=Docbook_ChapterType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ChapterType22", type=Docbook_NoteType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
section23: BinaryAssociation = BinaryAssociation(
    name="section23",
    ends={
        Property(name="Docbook_SectionType", type=Docbook_ChapterType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ChapterType24", type=Docbook_SectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title16: BinaryAssociation = BinaryAssociation(
    name="title16",
    ends={
        Property(name="Docbook_TitleType", type=Docbook_ChapterType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ChapterType17", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
para18: BinaryAssociation = BinaryAssociation(
    name="para18",
    ends={
        Property(name="Docbook_ParaType20", type=Docbook_ChapterType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ChapterType19", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg26: BinaryAssociation = BinaryAssociation(
    name="arg26",
    ends={
        Property(name="Docbook_ArgType28", type=Docbook_CmdsynopsisType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_CmdsynopsisType27", type=Docbook_ArgType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
command25: BinaryAssociation = BinaryAssociation(
    name="command25",
    ends={
        Property(name="Docbook_CommandType", type=Docbook_CmdsynopsisType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_CmdsynopsisType", type=Docbook_CommandType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap29: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap29",
    ends={
        Property(name="Docbook_EStringToStringMapEntry", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot", type=Docbook_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation30: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation30",
    ends={
        Property(name="Docbook_EStringToStringMapEntry32", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot31", type=Docbook_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book42: BinaryAssociation = BinaryAssociation(
    name="book42",
    ends={
        Property(name="Docbook_BookType44", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot43", type=Docbook_BookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstract33: BinaryAssociation = BinaryAssociation(
    name="abstract33",
    ends={
        Property(name="Docbook_AbstractType35", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot34", type=Docbook_AbstractType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address36: BinaryAssociation = BinaryAssociation(
    name="address36",
    ends={
        Property(name="Docbook_AddressType38", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot37", type=Docbook_AddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author39: BinaryAssociation = BinaryAssociation(
    name="author39",
    ends={
        Property(name="Docbook_AuthorType41", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot40", type=Docbook_AuthorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colspec51: BinaryAssociation = BinaryAssociation(
    name="colspec51",
    ends={
        Property(name="Docbook_ColspecType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot52", type=Docbook_ColspecType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
confgroup53: BinaryAssociation = BinaryAssociation(
    name="confgroup53",
    ends={
        Property(name="Docbook_ConfgroupType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot54", type=Docbook_ConfgroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
info45: BinaryAssociation = BinaryAssociation(
    name="info45",
    ends={
        Property(name="Docbook_InfoType47", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot46", type=Docbook_InfoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chapter48: BinaryAssociation = BinaryAssociation(
    name="chapter48",
    ends={
        Property(name="Docbook_ChapterType50", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot49", type=Docbook_ChapterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emphasis55: BinaryAssociation = BinaryAssociation(
    name="emphasis55",
    ends={
        Property(name="Docbook_EmphasisType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot56", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry57: BinaryAssociation = BinaryAssociation(
    name="entry57",
    ends={
        Property(name="Docbook_EntryType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot58", type=Docbook_EntryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
footnote61: BinaryAssociation = BinaryAssociation(
    name="footnote61",
    ends={
        Property(name="Docbook_FootnoteType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot62", type=Docbook_FootnoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imagedata63: BinaryAssociation = BinaryAssociation(
    name="imagedata63",
    ends={
        Property(name="Docbook_ImagedataType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot64", type=Docbook_ImagedataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imageobject65: BinaryAssociation = BinaryAssociation(
    name="imageobject65",
    ends={
        Property(name="Docbook_ImageobjectType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot66", type=Docbook_ImageobjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure59: BinaryAssociation = BinaryAssociation(
    name="figure59",
    ends={
        Property(name="Docbook_FigureType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot60", type=Docbook_FigureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemizedlist71: BinaryAssociation = BinaryAssociation(
    name="itemizedlist71",
    ends={
        Property(name="Docbook_ItemizedlistType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot72", type=Docbook_ItemizedlistType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
important67: BinaryAssociation = BinaryAssociation(
    name="important67",
    ends={
        Property(name="Docbook_ImportantType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot68", type=Docbook_ImportantType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informaltable69: BinaryAssociation = BinaryAssociation(
    name="informaltable69",
    ends={
        Property(name="Docbook_InformaltableType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot70", type=Docbook_InformaltableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listitem77: BinaryAssociation = BinaryAssociation(
    name="listitem77",
    ends={
        Property(name="Docbook_ListitemType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot78", type=Docbook_ListitemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal79: BinaryAssociation = BinaryAssociation(
    name="literal79",
    ends={
        Property(name="Docbook_LiteralType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot80", type=Docbook_LiteralType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediaobject81: BinaryAssociation = BinaryAssociation(
    name="mediaobject81",
    ends={
        Property(name="Docbook_MediaobjectType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot82", type=Docbook_MediaobjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keywordset73: BinaryAssociation = BinaryAssociation(
    name="keywordset73",
    ends={
        Property(name="Docbook_KeywordsetType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot74", type=Docbook_KeywordsetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
link75: BinaryAssociation = BinaryAssociation(
    name="link75",
    ends={
        Property(name="Docbook_LinkType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot76", type=Docbook_LinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderedlist86: BinaryAssociation = BinaryAssociation(
    name="orderedlist86",
    ends={
        Property(name="Docbook_OrderedlistType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot87", type=Docbook_OrderedlistType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
otheraddr88: BinaryAssociation = BinaryAssociation(
    name="otheraddr88",
    ends={
        Property(name="Docbook_OtheraddrType90", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot89", type=Docbook_OtheraddrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
note83: BinaryAssociation = BinaryAssociation(
    name="note83",
    ends={
        Property(name="Docbook_NoteType85", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot84", type=Docbook_NoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preface96: BinaryAssociation = BinaryAssociation(
    name="preface96",
    ends={
        Property(name="Docbook_PrefaceType98", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot97", type=Docbook_PrefaceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programlisting99: BinaryAssociation = BinaryAssociation(
    name="programlisting99",
    ends={
        Property(name="Docbook_ProgramlistingType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot100", type=Docbook_ProgramlistingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
para91: BinaryAssociation = BinaryAssociation(
    name="para91",
    ends={
        Property(name="Docbook_ParaType93", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot92", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phrase94: BinaryAssociation = BinaryAssociation(
    name="phrase94",
    ends={
        Property(name="Docbook_PhraseType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot95", type=Docbook_PhraseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row103: BinaryAssociation = BinaryAssociation(
    name="row103",
    ends={
        Property(name="Docbook_RowType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot104", type=Docbook_RowType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section105: BinaryAssociation = BinaryAssociation(
    name="section105",
    ends={
        Property(name="Docbook_SectionType107", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot106", type=Docbook_SectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publisher101: BinaryAssociation = BinaryAssociation(
    name="publisher101",
    ends={
        Property(name="Docbook_PublisherType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot102", type=Docbook_PublisherType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table108: BinaryAssociation = BinaryAssociation(
    name="table108",
    ends={
        Property(name="Docbook_TableType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot109", type=Docbook_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tbody110: BinaryAssociation = BinaryAssociation(
    name="tbody110",
    ends={
        Property(name="Docbook_TbodyType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot111", type=Docbook_TbodyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tip116: BinaryAssociation = BinaryAssociation(
    name="tip116",
    ends={
        Property(name="Docbook_TipType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot117", type=Docbook_TipType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title118: BinaryAssociation = BinaryAssociation(
    name="title118",
    ends={
        Property(name="Docbook_TitleType120", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot119", type=Docbook_TitleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tgroup112: BinaryAssociation = BinaryAssociation(
    name="tgroup112",
    ends={
        Property(name="Docbook_TgroupType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot113", type=Docbook_TgroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead114: BinaryAssociation = BinaryAssociation(
    name="thead114",
    ends={
        Property(name="Docbook_TheadType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot115", type=Docbook_TheadType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emphasis124: BinaryAssociation = BinaryAssociation(
    name="emphasis124",
    ends={
        Property(name="Docbook_EmphasisType125", type=Docbook_EmphasisType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_EmphasisType123", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ulink121: BinaryAssociation = BinaryAssociation(
    name="ulink121",
    ends={
        Property(name="Docbook_UlinkType", type=Docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_DocumentRoot122", type=Docbook_UlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediaobject129: BinaryAssociation = BinaryAssociation(
    name="mediaobject129",
    ends={
        Property(name="Docbook_MediaobjectType131", type=Docbook_EntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_EntryType130", type=Docbook_MediaobjectType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
para132: BinaryAssociation = BinaryAssociation(
    name="para132",
    ends={
        Property(name="Docbook_ParaType134", type=Docbook_EntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_EntryType133", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programlisting126: BinaryAssociation = BinaryAssociation(
    name="programlisting126",
    ends={
        Property(name="Docbook_ProgramlistingType128", type=Docbook_EntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_EntryType127", type=Docbook_ProgramlistingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replaceable135: BinaryAssociation = BinaryAssociation(
    name="replaceable135",
    ends={
        Property(name="Docbook_ReplaceableType136", type=Docbook_EnvarType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_EnvarType", type=Docbook_ReplaceableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title142: BinaryAssociation = BinaryAssociation(
    name="title142",
    ends={
        Property(name="Docbook_TitleType144", type=Docbook_FigureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FigureType143", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mediaobject145: BinaryAssociation = BinaryAssociation(
    name="mediaobject145",
    ends={
        Property(name="Docbook_MediaobjectType147", type=Docbook_FigureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FigureType146", type=Docbook_MediaobjectType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
title137: BinaryAssociation = BinaryAssociation(
    name="title137",
    ends={
        Property(name="Docbook_TitleType138", type=Docbook_ExampleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ExampleType", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
programlisting139: BinaryAssociation = BinaryAssociation(
    name="programlisting139",
    ends={
        Property(name="Docbook_ProgramlistingType141", type=Docbook_ExampleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ExampleType140", type=Docbook_ProgramlistingType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replaceable148: BinaryAssociation = BinaryAssociation(
    name="replaceable148",
    ends={
        Property(name="Docbook_ReplaceableType149", type=Docbook_FileNameType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FileNameType", type=Docbook_ReplaceableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
para150: BinaryAssociation = BinaryAssociation(
    name="para150",
    ends={
        Property(name="Docbook_ParaType152", type=Docbook_FootnoteType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FootnoteType151", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function153: BinaryAssociation = BinaryAssociation(
    name="function153",
    ends={
        Property(name="Docbook_FunctionType", type=Docbook_FuncdefType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FuncdefType", type=Docbook_FunctionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
funcdef154: BinaryAssociation = BinaryAssociation(
    name="funcdef154",
    ends={
        Property(name="Docbook_FuncdefType155", type=Docbook_FuncprototypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FuncprototypeType", type=Docbook_FuncdefType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
paramdef156: BinaryAssociation = BinaryAssociation(
    name="paramdef156",
    ends={
        Property(name="Docbook_ParamdefType", type=Docbook_FuncprototypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FuncprototypeType157", type=Docbook_ParamdefType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
funcprototype158: BinaryAssociation = BinaryAssociation(
    name="funcprototype158",
    ends={
        Property(name="Docbook_FuncprototypeType159", type=Docbook_FuncsynopsisType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_FuncsynopsisType", type=Docbook_FuncprototypeType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
emphasis163: BinaryAssociation = BinaryAssociation(
    name="emphasis163",
    ends={
        Property(name="Docbook_EmphasisType165", type=Docbook_ImportantType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ImportantType164", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imagedata160: BinaryAssociation = BinaryAssociation(
    name="imagedata160",
    ends={
        Property(name="Docbook_ImagedataType162", type=Docbook_ImageobjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ImageobjectType161", type=Docbook_ImagedataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tgroup169: BinaryAssociation = BinaryAssociation(
    name="tgroup169",
    ends={
        Property(name="Docbook_InformaltableType170", type=Docbook_TgroupType, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Docbook_TgroupType171", type=Docbook_InformaltableType, multiplicity=Multiplicity(1, 1))
    }
)
author172: BinaryAssociation = BinaryAssociation(
    name="author172",
    ends={
        Property(name="Docbook_AuthorType174", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType173", type=Docbook_AuthorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ulink166: BinaryAssociation = BinaryAssociation(
    name="ulink166",
    ends={
        Property(name="Docbook_UlinkType168", type=Docbook_ImportantType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ImportantType167", type=Docbook_UlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keywordset180: BinaryAssociation = BinaryAssociation(
    name="keywordset180",
    ends={
        Property(name="Docbook_KeywordsetType182", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType181", type=Docbook_KeywordsetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title175: BinaryAssociation = BinaryAssociation(
    name="title175",
    ends={
        Property(name="Docbook_TitleType177", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType176", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subtitle178: BinaryAssociation = BinaryAssociation(
    name="subtitle178",
    ends={
        Property(name="Docbook_SubtitleType", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType179", type=Docbook_SubtitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
confgroup189: BinaryAssociation = BinaryAssociation(
    name="confgroup189",
    ends={
        Property(name="Docbook_ConfgroupType191", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType190", type=Docbook_ConfgroupType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
revhistory192: BinaryAssociation = BinaryAssociation(
    name="revhistory192",
    ends={
        Property(name="Docbook_RevhistoryType", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType193", type=Docbook_RevhistoryType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copyright194: BinaryAssociation = BinaryAssociation(
    name="copyright194",
    ends={
        Property(name="Docbook_CopyrightType", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType195", type=Docbook_CopyrightType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abstract183: BinaryAssociation = BinaryAssociation(
    name="abstract183",
    ends={
        Property(name="Docbook_AbstractType185", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType184", type=Docbook_AbstractType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
publisher186: BinaryAssociation = BinaryAssociation(
    name="publisher186",
    ends={
        Property(name="Docbook_PublisherType188", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType187", type=Docbook_PublisherType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listitem198: BinaryAssociation = BinaryAssociation(
    name="listitem198",
    ends={
        Property(name="Docbook_ListitemType200", type=Docbook_ItemizedlistType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ItemizedlistType199", type=Docbook_ListitemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
legalnotice196: BinaryAssociation = BinaryAssociation(
    name="legalnotice196",
    ends={
        Property(name="Docbook_LegalNoticeType", type=Docbook_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_InfoType197", type=Docbook_LegalNoticeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
title201: BinaryAssociation = BinaryAssociation(
    name="title201",
    ends={
        Property(name="Docbook_TitleType203", type=Docbook_LegalNoticeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_LegalNoticeType202", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
revhistory204: BinaryAssociation = BinaryAssociation(
    name="revhistory204",
    ends={
        Property(name="Docbook_RevhistoryType206", type=Docbook_LegalNoticeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_LegalNoticeType205", type=Docbook_RevhistoryType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
para207: BinaryAssociation = BinaryAssociation(
    name="para207",
    ends={
        Property(name="Docbook_ParaType209", type=Docbook_LegalNoticeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_LegalNoticeType208", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
para213: BinaryAssociation = BinaryAssociation(
    name="para213",
    ends={
        Property(name="Docbook_ParaType215", type=Docbook_ListitemType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ListitemType214", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderedlist210: BinaryAssociation = BinaryAssociation(
    name="orderedlist210",
    ends={
        Property(name="Docbook_OrderedlistType212", type=Docbook_LegalNoticeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_LegalNoticeType211", type=Docbook_OrderedlistType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imageobject219: BinaryAssociation = BinaryAssociation(
    name="imageobject219",
    ends={
        Property(name="Docbook_ImageobjectType221", type=Docbook_MediaobjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_MediaobjectType220", type=Docbook_ImageobjectType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemizedlist216: BinaryAssociation = BinaryAssociation(
    name="itemizedlist216",
    ends={
        Property(name="Docbook_ItemizedlistType218", type=Docbook_ListitemType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ListitemType217", type=Docbook_ItemizedlistType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal222: BinaryAssociation = BinaryAssociation(
    name="literal222",
    ends={
        Property(name="Docbook_LiteralType224", type=Docbook_NoteType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_NoteType223", type=Docbook_LiteralType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ulink225: BinaryAssociation = BinaryAssociation(
    name="ulink225",
    ends={
        Property(name="Docbook_UlinkType227", type=Docbook_NoteType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_NoteType226", type=Docbook_UlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ulink231: BinaryAssociation = BinaryAssociation(
    name="ulink231",
    ends={
        Property(name="Docbook_UlinkType233", type=Docbook_OtheraddrType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_OtheraddrType232", type=Docbook_UlinkType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replaceable228: BinaryAssociation = BinaryAssociation(
    name="replaceable228",
    ends={
        Property(name="Docbook_ReplaceableType230", type=Docbook_OptionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_OptionType229", type=Docbook_ReplaceableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter234: BinaryAssociation = BinaryAssociation(
    name="parameter234",
    ends={
        Property(name="Docbook_ParameterType", type=Docbook_ParamdefType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParamdefType235", type=Docbook_ParameterType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
emphasis236: BinaryAssociation = BinaryAssociation(
    name="emphasis236",
    ends={
        Property(name="Docbook_EmphasisType238", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType237", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal239: BinaryAssociation = BinaryAssociation(
    name="literal239",
    ends={
        Property(name="Docbook_LiteralType241", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType240", type=Docbook_LiteralType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
link248: BinaryAssociation = BinaryAssociation(
    name="link248",
    ends={
        Property(name="Docbook_LinkType250", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType249", type=Docbook_LinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ulink242: BinaryAssociation = BinaryAssociation(
    name="ulink242",
    ends={
        Property(name="Docbook_UlinkType244", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType243", type=Docbook_UlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
footnote245: BinaryAssociation = BinaryAssociation(
    name="footnote245",
    ends={
        Property(name="Docbook_FootnoteType247", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType246", type=Docbook_FootnoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstname256: BinaryAssociation = BinaryAssociation(
    name="firstname256",
    ends={
        Property(name="Docbook_FirstnameType", type=Docbook_PersonnameType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PersonnameType257", type=Docbook_FirstnameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
surname258: BinaryAssociation = BinaryAssociation(
    name="surname258",
    ends={
        Property(name="Docbook_SurnameType", type=Docbook_PersonnameType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PersonnameType259", type=Docbook_SurnameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
itemizedlist251: BinaryAssociation = BinaryAssociation(
    name="itemizedlist251",
    ends={
        Property(name="Docbook_ItemizedlistType253", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType252", type=Docbook_ItemizedlistType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablelist254: BinaryAssociation = BinaryAssociation(
    name="variablelist254",
    ends={
        Property(name="Docbook_VariableListType", type=Docbook_ParaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ParaType255", type=Docbook_VariableListType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title260: BinaryAssociation = BinaryAssociation(
    name="title260",
    ends={
        Property(name="Docbook_TitleType262", type=Docbook_PrefaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PrefaceType261", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
para263: BinaryAssociation = BinaryAssociation(
    name="para263",
    ends={
        Property(name="Docbook_ParaType265", type=Docbook_PrefaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PrefaceType264", type=Docbook_ParaType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
important266: BinaryAssociation = BinaryAssociation(
    name="important266",
    ends={
        Property(name="Docbook_ImportantType268", type=Docbook_PrefaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PrefaceType267", type=Docbook_ImportantType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
emphasis272: BinaryAssociation = BinaryAssociation(
    name="emphasis272",
    ends={
        Property(name="Docbook_EmphasisType274", type=Docbook_ProgramlistingType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ProgramlistingType273", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tip269: BinaryAssociation = BinaryAssociation(
    name="tip269",
    ends={
        Property(name="Docbook_TipType271", type=Docbook_PrefaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PrefaceType270", type=Docbook_TipType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
phrase275: BinaryAssociation = BinaryAssociation(
    name="phrase275",
    ends={
        Property(name="Docbook_PhraseType277", type=Docbook_ProgramlistingType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ProgramlistingType276", type=Docbook_PhraseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refmeta283: BinaryAssociation = BinaryAssociation(
    name="refmeta283",
    ends={
        Property(name="Docbook_RefMetaType", type=Docbook_RefEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefEntryType284", type=Docbook_RefMetaType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refnamediv285: BinaryAssociation = BinaryAssociation(
    name="refnamediv285",
    ends={
        Property(name="Docbook_RefNameDivType", type=Docbook_RefEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefEntryType286", type=Docbook_RefNameDivType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refsynopsisdiv287: BinaryAssociation = BinaryAssociation(
    name="refsynopsisdiv287",
    ends={
        Property(name="Docbook_RefSynopsisDivType", type=Docbook_RefEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefEntryType288", type=Docbook_RefSynopsisDivType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refsect1289: BinaryAssociation = BinaryAssociation(
    name="refsect1289",
    ends={
        Property(name="Docbook_RefSect1Type", type=Docbook_RefEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefEntryType290", type=Docbook_RefSect1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address278: BinaryAssociation = BinaryAssociation(
    name="address278",
    ends={
        Property(name="Docbook_AddressType280", type=Docbook_PublisherType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_PublisherType279", type=Docbook_AddressType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
info281: BinaryAssociation = BinaryAssociation(
    name="info281",
    ends={
        Property(name="Docbook_InfoType282", type=Docbook_RefEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefEntryType", type=Docbook_InfoType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
info291: BinaryAssociation = BinaryAssociation(
    name="info291",
    ends={
        Property(name="Docbook_InfoType293", type=Docbook_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ReferenceType292", type=Docbook_InfoType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title294: BinaryAssociation = BinaryAssociation(
    name="title294",
    ends={
        Property(name="Docbook_TitleType296", type=Docbook_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ReferenceType295", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refentrytitle300: BinaryAssociation = BinaryAssociation(
    name="refentrytitle300",
    ends={
        Property(name="Docbook_RefEntryTitleType", type=Docbook_RefMetaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefMetaType301", type=Docbook_RefEntryTitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refentry297: BinaryAssociation = BinaryAssociation(
    name="refentry297",
    ends={
        Property(name="Docbook_RefEntryType299", type=Docbook_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_ReferenceType298", type=Docbook_RefEntryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title302: BinaryAssociation = BinaryAssociation(
    name="title302",
    ends={
        Property(name="Docbook_TitleType304", type=Docbook_RefSect1Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefSect1Type303", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
para305: BinaryAssociation = BinaryAssociation(
    name="para305",
    ends={
        Property(name="Docbook_ParaType307", type=Docbook_RefSect1Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefSect1Type306", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablelist308: BinaryAssociation = BinaryAssociation(
    name="variablelist308",
    ends={
        Property(name="Docbook_VariableListType310", type=Docbook_RefSect1Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefSect1Type309", type=Docbook_VariableListType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segmentedlist311: BinaryAssociation = BinaryAssociation(
    name="segmentedlist311",
    ends={
        Property(name="Docbook_SegmentedListType", type=Docbook_RefSect1Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefSect1Type312", type=Docbook_SegmentedListType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
para319: BinaryAssociation = BinaryAssociation(
    name="para319",
    ends={
        Property(name="Docbook_ParaType320", type=Docbook_RevdescriptionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RevdescriptionType", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmdsynopsis313: BinaryAssociation = BinaryAssociation(
    name="cmdsynopsis313",
    ends={
        Property(name="Docbook_CmdsynopsisType315", type=Docbook_RefSynopsisDivType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefSynopsisDivType314", type=Docbook_CmdsynopsisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revision321: BinaryAssociation = BinaryAssociation(
    name="revision321",
    ends={
        Property(name="Docbook_RevisionType", type=Docbook_RevhistoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RevhistoryType322", type=Docbook_RevisionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
funcsynopsis316: BinaryAssociation = BinaryAssociation(
    name="funcsynopsis316",
    ends={
        Property(name="Docbook_FuncsynopsisType318", type=Docbook_RefSynopsisDivType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RefSynopsisDivType317", type=Docbook_FuncsynopsisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
date325: BinaryAssociation = BinaryAssociation(
    name="date325",
    ends={
        Property(name="Docbook_RevisionType326", type=Docbook_DateType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Docbook_DateType", type=Docbook_RevisionType, multiplicity=Multiplicity(1, 1))
    }
)
authorinitials327: BinaryAssociation = BinaryAssociation(
    name="authorinitials327",
    ends={
        Property(name="Docbook_AuthorinitialsType", type=Docbook_RevisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RevisionType328", type=Docbook_AuthorinitialsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
revdescription329: BinaryAssociation = BinaryAssociation(
    name="revdescription329",
    ends={
        Property(name="Docbook_RevdescriptionType331", type=Docbook_RevisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RevisionType330", type=Docbook_RevdescriptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
revnumber323: BinaryAssociation = BinaryAssociation(
    name="revnumber323",
    ends={
        Property(name="Docbook_RevnumberType", type=Docbook_RevisionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RevisionType324", type=Docbook_RevnumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry335: BinaryAssociation = BinaryAssociation(
    name="entry335",
    ends={
        Property(name="Docbook_EntryType337", type=Docbook_RowType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RowType336", type=Docbook_EntryType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ulink332: BinaryAssociation = BinaryAssociation(
    name="ulink332",
    ends={
        Property(name="Docbook_UlinkType334", type=Docbook_RevnumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_RevnumberType333", type=Docbook_UlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemizedlist338: BinaryAssociation = BinaryAssociation(
    name="itemizedlist338",
    ends={
        Property(name="Docbook_ItemizedlistType340", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType339", type=Docbook_ItemizedlistType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
para347: BinaryAssociation = BinaryAssociation(
    name="para347",
    ends={
        Property(name="Docbook_ParaType349", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType348", type=Docbook_ParaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediaobject341: BinaryAssociation = BinaryAssociation(
    name="mediaobject341",
    ends={
        Property(name="Docbook_MediaobjectType343", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType342", type=Docbook_MediaobjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
note344: BinaryAssociation = BinaryAssociation(
    name="note344",
    ends={
        Property(name="Docbook_NoteType346", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType345", type=Docbook_NoteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section354: BinaryAssociation = BinaryAssociation(
    name="section354",
    ends={
        Property(name="Docbook_SectionType355", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType353", type=Docbook_SectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programlisting350: BinaryAssociation = BinaryAssociation(
    name="programlisting350",
    ends={
        Property(name="Docbook_ProgramlistingType352", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType351", type=Docbook_ProgramlistingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informaltable362: BinaryAssociation = BinaryAssociation(
    name="informaltable362",
    ends={
        Property(name="Docbook_InformaltableType364", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType363", type=Docbook_InformaltableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderedlist365: BinaryAssociation = BinaryAssociation(
    name="orderedlist365",
    ends={
        Property(name="Docbook_OrderedlistType367", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType366", type=Docbook_OrderedlistType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title356: BinaryAssociation = BinaryAssociation(
    name="title356",
    ends={
        Property(name="Docbook_TitleType358", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType357", type=Docbook_TitleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure359: BinaryAssociation = BinaryAssociation(
    name="figure359",
    ends={
        Property(name="Docbook_FigureType361", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType360", type=Docbook_FigureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tip371: BinaryAssociation = BinaryAssociation(
    name="tip371",
    ends={
        Property(name="Docbook_TipType373", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType372", type=Docbook_TipType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
funcsynopsis374: BinaryAssociation = BinaryAssociation(
    name="funcsynopsis374",
    ends={
        Property(name="Docbook_FuncsynopsisType376", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType375", type=Docbook_FuncsynopsisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table368: BinaryAssociation = BinaryAssociation(
    name="table368",
    ends={
        Property(name="Docbook_TableType370", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType369", type=Docbook_TableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seg383: BinaryAssociation = BinaryAssociation(
    name="seg383",
    ends={
        Property(name="Docbook_SegType", type=Docbook_SegListItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SegListItemType", type=Docbook_SegType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
example377: BinaryAssociation = BinaryAssociation(
    name="example377",
    ends={
        Property(name="Docbook_ExampleType379", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType378", type=Docbook_ExampleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cmdsynopsis380: BinaryAssociation = BinaryAssociation(
    name="cmdsynopsis380",
    ends={
        Property(name="Docbook_CmdsynopsisType382", type=Docbook_SectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SectionType381", type=Docbook_CmdsynopsisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seglistitem384: BinaryAssociation = BinaryAssociation(
    name="seglistitem384",
    ends={
        Property(name="Docbook_SegListItemType386", type=Docbook_SegmentedListType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SegmentedListType385", type=Docbook_SegListItemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phrase390: BinaryAssociation = BinaryAssociation(
    name="phrase390",
    ends={
        Property(name="Docbook_PhraseType392", type=Docbook_SubtitleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SubtitleType391", type=Docbook_PhraseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emphasis387: BinaryAssociation = BinaryAssociation(
    name="emphasis387",
    ends={
        Property(name="Docbook_EmphasisType389", type=Docbook_SubtitleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_SubtitleType388", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emphasis399: BinaryAssociation = BinaryAssociation(
    name="emphasis399",
    ends={
        Property(name="Docbook_EmphasisType400", type=Docbook_TermType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TermType", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title393: BinaryAssociation = BinaryAssociation(
    name="title393",
    ends={
        Property(name="Docbook_TitleType395", type=Docbook_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TableType394", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tgroup396: BinaryAssociation = BinaryAssociation(
    name="tgroup396",
    ends={
        Property(name="Docbook_TgroupType398", type=Docbook_TableType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TableType397", type=Docbook_TgroupType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
row410: BinaryAssociation = BinaryAssociation(
    name="row410",
    ends={
        Property(name="Docbook_RowType412", type=Docbook_TbodyType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TbodyType411", type=Docbook_RowType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
colspec413: BinaryAssociation = BinaryAssociation(
    name="colspec413",
    ends={
        Property(name="Docbook_ColspecType415", type=Docbook_TgroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TgroupType414", type=Docbook_ColspecType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
option401: BinaryAssociation = BinaryAssociation(
    name="option401",
    ends={
        Property(name="Docbook_OptionType403", type=Docbook_TermType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TermType402", type=Docbook_OptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filename404: BinaryAssociation = BinaryAssociation(
    name="filename404",
    ends={
        Property(name="Docbook_FileNameType406", type=Docbook_TermType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TermType405", type=Docbook_FileNameType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
envar407: BinaryAssociation = BinaryAssociation(
    name="envar407",
    ends={
        Property(name="Docbook_EnvarType409", type=Docbook_TermType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TermType408", type=Docbook_EnvarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thead416: BinaryAssociation = BinaryAssociation(
    name="thead416",
    ends={
        Property(name="Docbook_TheadType418", type=Docbook_TgroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TgroupType417", type=Docbook_TheadType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbody419: BinaryAssociation = BinaryAssociation(
    name="tbody419",
    ends={
        Property(name="Docbook_TbodyType421", type=Docbook_TgroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TgroupType420", type=Docbook_TbodyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
row422: BinaryAssociation = BinaryAssociation(
    name="row422",
    ends={
        Property(name="Docbook_RowType424", type=Docbook_TheadType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TheadType423", type=Docbook_RowType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
emphasis428: BinaryAssociation = BinaryAssociation(
    name="emphasis428",
    ends={
        Property(name="Docbook_EmphasisType430", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TitleType429", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phrase431: BinaryAssociation = BinaryAssociation(
    name="phrase431",
    ends={
        Property(name="Docbook_PhraseType433", type=Docbook_TitleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TitleType432", type=Docbook_PhraseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ulink425: BinaryAssociation = BinaryAssociation(
    name="ulink425",
    ends={
        Property(name="Docbook_UlinkType427", type=Docbook_TipType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_TipType426", type=Docbook_UlinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emphasis434: BinaryAssociation = BinaryAssociation(
    name="emphasis434",
    ends={
        Property(name="Docbook_EmphasisType436", type=Docbook_UlinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_UlinkType435", type=Docbook_EmphasisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varlistentry437: BinaryAssociation = BinaryAssociation(
    name="varlistentry437",
    ends={
        Property(name="Docbook_VarListEntryType", type=Docbook_VariableListType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_VariableListType438", type=Docbook_VarListEntryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term439: BinaryAssociation = BinaryAssociation(
    name="term439",
    ends={
        Property(name="Docbook_TermType441", type=Docbook_VarListEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_VarListEntryType440", type=Docbook_TermType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
listitem442: BinaryAssociation = BinaryAssociation(
    name="listitem442",
    ends={
        Property(name="Docbook_ListitemType444", type=Docbook_VarListEntryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Docbook_VarListEntryType443", type=Docbook_ListitemType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Docbook_OrderedlistType_ItemizedlistType = Generalization(general=ItemizedlistType, specific=Docbook_OrderedlistType)

# Domain Model
domain_model = DomainModel(
    name="Docbook",
    types={Docbook_AbstractType, Docbook_ParaType, Docbook_AddressType, Docbook_ArgType, Docbook_OptionType, Docbook_ReplaceableType, Docbook_OtheraddrType, Docbook_AuthorinitialsType, Docbook_AuthorType, Docbook_PersonnameType, Docbook_InfoType, Docbook_BookType, Docbook_PrefaceType, Docbook_ChapterType, Docbook_ReferenceType, Docbook_NoteType, Docbook_SectionType, Docbook_ColspecType, Docbook_TitleType, Docbook_ConfgroupType, Docbook_CmdsynopsisType, Docbook_CommandType, Docbook_CopyrightType, Docbook_EStringToStringMapEntry, Docbook_DateType, Docbook_DocumentRoot, Docbook_EmphasisType, Docbook_EntryType, Docbook_FootnoteType, Docbook_ImagedataType, Docbook_ImageobjectType, Docbook_FigureType, Docbook_ItemizedlistType, Docbook_KeywordsetType, Docbook_ImportantType, Docbook_InformaltableType, Docbook_ListitemType, Docbook_LiteralType, Docbook_MediaobjectType, Docbook_LinkType, Docbook_OrderedlistType, Docbook_ProgramlistingType, Docbook_PhraseType, Docbook_RowType, Docbook_PublisherType, Docbook_TableType, Docbook_TbodyType, Docbook_TipType, Docbook_TgroupType, Docbook_TheadType, Docbook_UlinkType, Docbook_EnvarType, Docbook_ExampleType, Docbook_FirstnameType, Docbook_FileNameType, Docbook_FunctionType, Docbook_FuncprototypeType, Docbook_ParamdefType, Docbook_FuncdefType, Docbook_FuncsynopsisType, Docbook_SubtitleType, Docbook_RevhistoryType, Docbook_LegalNoticeType, ItemizedlistType, Docbook_ParameterType, Docbook_SurnameType, Docbook_VariableListType, Docbook_RefMetaType, Docbook_RefNameDivType, Docbook_RefSynopsisDivType, Docbook_RefSect1Type, Docbook_RefEntryType, Docbook_RefEntryTitleType, Docbook_SegmentedListType, Docbook_RevisionType, Docbook_RevdescriptionType, Docbook_RevnumberType, Docbook_SegListItemType, Docbook_SegType, Docbook_TermType, Docbook_VarListEntryType},
    associations={para0, option2, otheraddr1, personname5, replaceable3, info9, address6, reference14, preface10, chapter12, note21, section23, title16, para18, arg26, command25, xMLNSPrefixMap29, xSISchemaLocation30, book42, abstract33, address36, author39, colspec51, confgroup53, info45, chapter48, emphasis55, entry57, footnote61, imagedata63, imageobject65, figure59, itemizedlist71, important67, informaltable69, listitem77, literal79, mediaobject81, keywordset73, link75, orderedlist86, otheraddr88, note83, preface96, programlisting99, para91, phrase94, row103, section105, publisher101, table108, tbody110, tip116, title118, tgroup112, thead114, emphasis124, ulink121, mediaobject129, para132, programlisting126, replaceable135, title142, mediaobject145, title137, programlisting139, replaceable148, para150, function153, funcdef154, paramdef156, funcprototype158, emphasis163, imagedata160, tgroup169, author172, ulink166, keywordset180, title175, subtitle178, confgroup189, revhistory192, copyright194, abstract183, publisher186, listitem198, legalnotice196, title201, revhistory204, para207, para213, orderedlist210, imageobject219, itemizedlist216, literal222, ulink225, ulink231, replaceable228, parameter234, emphasis236, literal239, link248, ulink242, footnote245, firstname256, surname258, itemizedlist251, variablelist254, title260, para263, important266, emphasis272, tip269, phrase275, refmeta283, refnamediv285, refsynopsisdiv287, refsect1289, address278, info281, info291, title294, refentrytitle300, refentry297, title302, para305, variablelist308, segmentedlist311, para319, cmdsynopsis313, revision321, funcsynopsis316, date325, authorinitials327, revdescription329, revnumber323, entry335, ulink332, itemizedlist338, para347, mediaobject341, note344, section354, programlisting350, informaltable362, orderedlist365, title356, figure359, tip371, funcsynopsis374, table368, seg383, example377, cmdsynopsis380, seglistitem384, phrase390, emphasis387, emphasis399, title393, tgroup396, row410, colspec413, option401, filename404, envar407, thead416, tbody419, row422, emphasis428, phrase431, ulink425, emphasis434, varlistentry437, term439, listitem442},
    generalizations={gen_Docbook_OrderedlistType_ItemizedlistType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)