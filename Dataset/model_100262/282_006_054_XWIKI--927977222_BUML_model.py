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
xwiki_Attachment = Class(name="xwiki_Attachment")
LinkCollection = Class(name="LinkCollection")
xwiki_AttachmentsType = Class(name="xwiki_AttachmentsType")
xwiki_Attribute = Class(name="xwiki_Attribute")
xwiki_Class = Class(name="xwiki_Class")
xwiki_Property = Class(name="xwiki_Property")
xwiki_ClassesType = Class(name="xwiki_ClassesType")
xwiki_Comment = Class(name="xwiki_Comment")
xwiki_CommentsType = Class(name="xwiki_CommentsType")
xwiki_DocumentRoot = Class(name="xwiki_DocumentRoot")
xwiki_EStringToStringMapEntry = Class(name="xwiki_EStringToStringMapEntry")
xwiki_ObjectSummary = Class(name="xwiki_ObjectSummary")
xwiki_HistoryType = Class(name="xwiki_HistoryType")
xwiki_Object = Class(name="xwiki_Object")
xwiki_ObjectsType = Class(name="xwiki_ObjectsType")
xwiki_SpacesType = Class(name="xwiki_SpacesType")
xwiki_Page = Class(name="xwiki_Page")
xwiki_PagesType = Class(name="xwiki_PagesType")
xwiki_PropertiesType = Class(name="xwiki_PropertiesType")
xwiki_SearchResult = Class(name="xwiki_SearchResult")
xwiki_SearchResultsType = Class(name="xwiki_SearchResultsType")
xwiki_Space = Class(name="xwiki_Space")
xwiki_Syntaxes = Class(name="xwiki_Syntaxes")
xwiki_Tag = Class(name="xwiki_Tag")
xwiki_TagsType = Class(name="xwiki_TagsType")
xwiki_Translations = Class(name="xwiki_Translations")
xwiki_Wiki = Class(name="xwiki_Wiki")
xwiki_WikisType = Class(name="xwiki_WikisType")
xwiki_XWiki = Class(name="xwiki_XWiki")
xwiki_HistorySummary = Class(name="xwiki_HistorySummary")
xwiki_Link = Class(name="xwiki_Link")
xwiki_LinkCollection = Class(name="xwiki_LinkCollection")
ObjectSummary = Class(name="ObjectSummary")
PageSummary = Class(name="PageSummary")
xwiki_PageSummary = Class(name="xwiki_PageSummary")
xwiki_Translation = Class(name="xwiki_Translation")

# xwiki_Attachment class attributes and methods
xwiki_Attachment_version: Property = Property(name="version", type=StringType)
xwiki_Attachment_pageId: Property = Property(name="pageId", type=StringType)
xwiki_Attachment_pageVersion: Property = Property(name="pageVersion", type=StringType)
xwiki_Attachment_mimeType: Property = Property(name="mimeType", type=StringType)
xwiki_Attachment_author: Property = Property(name="author", type=StringType)
xwiki_Attachment_authorName: Property = Property(name="authorName", type=StringType)
xwiki_Attachment_date: Property = Property(name="date", type=StringType)
xwiki_Attachment_xwikiRelativeUrl: Property = Property(name="xwikiRelativeUrl", type=StringType)
xwiki_Attachment_xwikiAbsoluteUrl: Property = Property(name="xwikiAbsoluteUrl", type=StringType)
xwiki_Attachment_id: Property = Property(name="id", type=StringType)
xwiki_Attachment_name: Property = Property(name="name", type=StringType)
xwiki_Attachment_size: Property = Property(name="size", type=StringType)
xwiki_Attachment.attributes={xwiki_Attachment_size, xwiki_Attachment_author, xwiki_Attachment_xwikiRelativeUrl, xwiki_Attachment_pageVersion, xwiki_Attachment_date, xwiki_Attachment_mimeType, xwiki_Attachment_xwikiAbsoluteUrl, xwiki_Attachment_pageId, xwiki_Attachment_authorName, xwiki_Attachment_name, xwiki_Attachment_version, xwiki_Attachment_id}

# LinkCollection class attributes and methods

# xwiki_AttachmentsType class attributes and methods

# xwiki_Attribute class attributes and methods
xwiki_Attribute_name: Property = Property(name="name", type=StringType)
xwiki_Attribute_value: Property = Property(name="value", type=StringType)
xwiki_Attribute.attributes={xwiki_Attribute_value, xwiki_Attribute_name}

# xwiki_Class class attributes and methods
xwiki_Class_id: Property = Property(name="id", type=StringType)
xwiki_Class_name: Property = Property(name="name", type=StringType)
xwiki_Class.attributes={xwiki_Class_id, xwiki_Class_name}

# xwiki_Property class attributes and methods
xwiki_Property_value: Property = Property(name="value", type=StringType)
xwiki_Property_name: Property = Property(name="name", type=StringType)
xwiki_Property_type: Property = Property(name="type", type=StringType)
xwiki_Property.attributes={xwiki_Property_type, xwiki_Property_name, xwiki_Property_value}

# xwiki_ClassesType class attributes and methods

# xwiki_Comment class attributes and methods
xwiki_Comment_id: Property = Property(name="id", type=StringType)
xwiki_Comment_pageId: Property = Property(name="pageId", type=StringType)
xwiki_Comment_author: Property = Property(name="author", type=StringType)
xwiki_Comment_authorName: Property = Property(name="authorName", type=StringType)
xwiki_Comment_date: Property = Property(name="date", type=StringType)
xwiki_Comment_highlight: Property = Property(name="highlight", type=StringType)
xwiki_Comment_text: Property = Property(name="text", type=StringType)
xwiki_Comment_replyTo: Property = Property(name="replyTo", type=StringType)
xwiki_Comment.attributes={xwiki_Comment_authorName, xwiki_Comment_id, xwiki_Comment_highlight, xwiki_Comment_replyTo, xwiki_Comment_pageId, xwiki_Comment_author, xwiki_Comment_date, xwiki_Comment_text}

# xwiki_CommentsType class attributes and methods

# xwiki_DocumentRoot class attributes and methods
xwiki_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
xwiki_DocumentRoot.attributes={xwiki_DocumentRoot_mixed}

# xwiki_EStringToStringMapEntry class attributes and methods

# xwiki_ObjectSummary class attributes and methods
xwiki_ObjectSummary_id: Property = Property(name="id", type=StringType)
xwiki_ObjectSummary_headline: Property = Property(name="headline", type=StringType)
xwiki_ObjectSummary_guid: Property = Property(name="guid", type=StringType)
xwiki_ObjectSummary_pageId: Property = Property(name="pageId", type=StringType)
xwiki_ObjectSummary_pageVersion: Property = Property(name="pageVersion", type=StringType)
xwiki_ObjectSummary_wiki: Property = Property(name="wiki", type=StringType)
xwiki_ObjectSummary_space: Property = Property(name="space", type=StringType)
xwiki_ObjectSummary_pageName: Property = Property(name="pageName", type=StringType)
xwiki_ObjectSummary_pageAuthor: Property = Property(name="pageAuthor", type=StringType)
xwiki_ObjectSummary_pageAuthorName: Property = Property(name="pageAuthorName", type=StringType)
xwiki_ObjectSummary_className: Property = Property(name="className", type=StringType)
xwiki_ObjectSummary_number: Property = Property(name="number", type=StringType)
xwiki_ObjectSummary.attributes={xwiki_ObjectSummary_headline, xwiki_ObjectSummary_pageAuthorName, xwiki_ObjectSummary_pageId, xwiki_ObjectSummary_pageName, xwiki_ObjectSummary_id, xwiki_ObjectSummary_className, xwiki_ObjectSummary_number, xwiki_ObjectSummary_guid, xwiki_ObjectSummary_wiki, xwiki_ObjectSummary_pageAuthor, xwiki_ObjectSummary_space, xwiki_ObjectSummary_pageVersion}

# xwiki_HistoryType class attributes and methods

# xwiki_Object class attributes and methods

# xwiki_ObjectsType class attributes and methods

# xwiki_SpacesType class attributes and methods

# xwiki_Page class attributes and methods
xwiki_Page_content: Property = Property(name="content", type=StringType)
xwiki_Page_language: Property = Property(name="language", type=StringType)
xwiki_Page_majorVersion: Property = Property(name="majorVersion", type=StringType)
xwiki_Page_minorVersion: Property = Property(name="minorVersion", type=StringType)
xwiki_Page_created: Property = Property(name="created", type=StringType)
xwiki_Page_creator: Property = Property(name="creator", type=StringType)
xwiki_Page_creatorName: Property = Property(name="creatorName", type=StringType)
xwiki_Page_modified: Property = Property(name="modified", type=StringType)
xwiki_Page_modifier: Property = Property(name="modifier", type=StringType)
xwiki_Page_modifierName: Property = Property(name="modifierName", type=StringType)
xwiki_Page_comment: Property = Property(name="comment", type=StringType)
xwiki_Page.attributes={xwiki_Page_comment, xwiki_Page_modifier, xwiki_Page_created, xwiki_Page_majorVersion, xwiki_Page_modified, xwiki_Page_creatorName, xwiki_Page_language, xwiki_Page_minorVersion, xwiki_Page_content, xwiki_Page_modifierName, xwiki_Page_creator}

# xwiki_PagesType class attributes and methods

# xwiki_PropertiesType class attributes and methods

# xwiki_SearchResult class attributes and methods
xwiki_SearchResult_type: Property = Property(name="type", type=StringType)
xwiki_SearchResult_id: Property = Property(name="id", type=StringType)
xwiki_SearchResult_pageFullName: Property = Property(name="pageFullName", type=StringType)
xwiki_SearchResult_title: Property = Property(name="title", type=StringType)
xwiki_SearchResult_wiki: Property = Property(name="wiki", type=StringType)
xwiki_SearchResult_space: Property = Property(name="space", type=StringType)
xwiki_SearchResult_pageName: Property = Property(name="pageName", type=StringType)
xwiki_SearchResult_modified: Property = Property(name="modified", type=StringType)
xwiki_SearchResult_author: Property = Property(name="author", type=StringType)
xwiki_SearchResult_authorName: Property = Property(name="authorName", type=StringType)
xwiki_SearchResult_version: Property = Property(name="version", type=StringType)
xwiki_SearchResult_language: Property = Property(name="language", type=StringType)
xwiki_SearchResult_className: Property = Property(name="className", type=StringType)
xwiki_SearchResult_objectNumber: Property = Property(name="objectNumber", type=StringType)
xwiki_SearchResult_filename: Property = Property(name="filename", type=StringType)
xwiki_SearchResult_score: Property = Property(name="score", type=StringType)
xwiki_SearchResult.attributes={xwiki_SearchResult_title, xwiki_SearchResult_modified, xwiki_SearchResult_pageName, xwiki_SearchResult_author, xwiki_SearchResult_objectNumber, xwiki_SearchResult_space, xwiki_SearchResult_id, xwiki_SearchResult_authorName, xwiki_SearchResult_pageFullName, xwiki_SearchResult_language, xwiki_SearchResult_score, xwiki_SearchResult_className, xwiki_SearchResult_type, xwiki_SearchResult_version, xwiki_SearchResult_wiki, xwiki_SearchResult_filename}

# xwiki_SearchResultsType class attributes and methods
xwiki_SearchResultsType_template: Property = Property(name="template", type=StringType)
xwiki_SearchResultsType.attributes={xwiki_SearchResultsType_template}

# xwiki_Space class attributes and methods
xwiki_Space_id: Property = Property(name="id", type=StringType)
xwiki_Space_wiki: Property = Property(name="wiki", type=StringType)
xwiki_Space_name: Property = Property(name="name", type=StringType)
xwiki_Space_home: Property = Property(name="home", type=StringType)
xwiki_Space_xwikiRelativeUrl: Property = Property(name="xwikiRelativeUrl", type=StringType)
xwiki_Space_xwikiAbsoluteUrl: Property = Property(name="xwikiAbsoluteUrl", type=StringType)
xwiki_Space.attributes={xwiki_Space_xwikiRelativeUrl, xwiki_Space_name, xwiki_Space_home, xwiki_Space_id, xwiki_Space_xwikiAbsoluteUrl, xwiki_Space_wiki}

# xwiki_Syntaxes class attributes and methods
xwiki_Syntaxes_syntax: Property = Property(name="syntax", type=StringType)
xwiki_Syntaxes.attributes={xwiki_Syntaxes_syntax}

# xwiki_Tag class attributes and methods
xwiki_Tag_name: Property = Property(name="name", type=StringType)
xwiki_Tag.attributes={xwiki_Tag_name}

# xwiki_TagsType class attributes and methods

# xwiki_Translations class attributes and methods
xwiki_Translations_default: Property = Property(name="default", type=StringType)
xwiki_Translations.attributes={xwiki_Translations_default}

# xwiki_Wiki class attributes and methods
xwiki_Wiki_id: Property = Property(name="id", type=StringType)
xwiki_Wiki_name: Property = Property(name="name", type=StringType)
xwiki_Wiki_description: Property = Property(name="description", type=StringType)
xwiki_Wiki_owner: Property = Property(name="owner", type=StringType)
xwiki_Wiki.attributes={xwiki_Wiki_owner, xwiki_Wiki_id, xwiki_Wiki_description, xwiki_Wiki_name}

# xwiki_WikisType class attributes and methods

# xwiki_XWiki class attributes and methods
xwiki_XWiki_version: Property = Property(name="version", type=StringType)
xwiki_XWiki.attributes={xwiki_XWiki_version}

# xwiki_HistorySummary class attributes and methods
xwiki_HistorySummary_pageId: Property = Property(name="pageId", type=StringType)
xwiki_HistorySummary_wiki: Property = Property(name="wiki", type=StringType)
xwiki_HistorySummary_space: Property = Property(name="space", type=StringType)
xwiki_HistorySummary_name: Property = Property(name="name", type=StringType)
xwiki_HistorySummary_version: Property = Property(name="version", type=StringType)
xwiki_HistorySummary_majorVersion: Property = Property(name="majorVersion", type=StringType)
xwiki_HistorySummary_minorVersion: Property = Property(name="minorVersion", type=StringType)
xwiki_HistorySummary_modified: Property = Property(name="modified", type=StringType)
xwiki_HistorySummary_modifier: Property = Property(name="modifier", type=StringType)
xwiki_HistorySummary_modifierName: Property = Property(name="modifierName", type=StringType)
xwiki_HistorySummary_language: Property = Property(name="language", type=StringType)
xwiki_HistorySummary_comment: Property = Property(name="comment", type=StringType)
xwiki_HistorySummary.attributes={xwiki_HistorySummary_space, xwiki_HistorySummary_minorVersion, xwiki_HistorySummary_modifier, xwiki_HistorySummary_wiki, xwiki_HistorySummary_name, xwiki_HistorySummary_version, xwiki_HistorySummary_comment, xwiki_HistorySummary_pageId, xwiki_HistorySummary_majorVersion, xwiki_HistorySummary_modified, xwiki_HistorySummary_language, xwiki_HistorySummary_modifierName}

# xwiki_Link class attributes and methods
xwiki_Link_href: Property = Property(name="href", type=StringType)
xwiki_Link_hrefLang: Property = Property(name="hrefLang", type=StringType)
xwiki_Link_rel: Property = Property(name="rel", type=StringType)
xwiki_Link_type: Property = Property(name="type", type=StringType)
xwiki_Link.attributes={xwiki_Link_hrefLang, xwiki_Link_href, xwiki_Link_type, xwiki_Link_rel}

# xwiki_LinkCollection class attributes and methods

# ObjectSummary class attributes and methods

# PageSummary class attributes and methods

# xwiki_PageSummary class attributes and methods
xwiki_PageSummary_version: Property = Property(name="version", type=StringType)
xwiki_PageSummary_id: Property = Property(name="id", type=StringType)
xwiki_PageSummary_fullName: Property = Property(name="fullName", type=StringType)
xwiki_PageSummary_wiki: Property = Property(name="wiki", type=StringType)
xwiki_PageSummary_space: Property = Property(name="space", type=StringType)
xwiki_PageSummary_name: Property = Property(name="name", type=StringType)
xwiki_PageSummary_title: Property = Property(name="title", type=StringType)
xwiki_PageSummary_parent: Property = Property(name="parent", type=StringType)
xwiki_PageSummary_parentId: Property = Property(name="parentId", type=StringType)
xwiki_PageSummary_syntax: Property = Property(name="syntax", type=StringType)
xwiki_PageSummary_author: Property = Property(name="author", type=StringType)
xwiki_PageSummary_authorName: Property = Property(name="authorName", type=StringType)
xwiki_PageSummary_xwikiRelativeUrl: Property = Property(name="xwikiRelativeUrl", type=StringType)
xwiki_PageSummary_xwikiAbsoluteUrl: Property = Property(name="xwikiAbsoluteUrl", type=StringType)
xwiki_PageSummary.attributes={xwiki_PageSummary_name, xwiki_PageSummary_author, xwiki_PageSummary_xwikiRelativeUrl, xwiki_PageSummary_authorName, xwiki_PageSummary_space, xwiki_PageSummary_id, xwiki_PageSummary_parent, xwiki_PageSummary_fullName, xwiki_PageSummary_version, xwiki_PageSummary_wiki, xwiki_PageSummary_xwikiAbsoluteUrl, xwiki_PageSummary_title, xwiki_PageSummary_parentId, xwiki_PageSummary_syntax}

# xwiki_Translation class attributes and methods
xwiki_Translation_language: Property = Property(name="language", type=StringType)
xwiki_Translation.attributes={xwiki_Translation_language}

# Relationships
attachment0: BinaryAssociation = BinaryAssociation(
    name="attachment0",
    ends={
        Property(name="xwiki_Attachment", type=xwiki_AttachmentsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_AttachmentsType", type=xwiki_Attachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property1: BinaryAssociation = BinaryAssociation(
    name="property1",
    ends={
        Property(name="xwiki_Property", type=xwiki_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_Class", type=xwiki_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_2: BinaryAssociation = BinaryAssociation(
    name="class_2",
    ends={
        Property(name="xwiki_Class3", type=xwiki_ClassesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_ClassesType", type=xwiki_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachment9: BinaryAssociation = BinaryAssociation(
    name="attachment9",
    ends={
        Property(name="xwiki_Attachment11", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot10", type=xwiki_Attachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comment4: BinaryAssociation = BinaryAssociation(
    name="comment4",
    ends={
        Property(name="xwiki_Comment", type=xwiki_CommentsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_CommentsType", type=xwiki_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap5: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap5",
    ends={
        Property(name="xwiki_EStringToStringMapEntry", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot", type=xwiki_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation6: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation6",
    ends={
        Property(name="xwiki_EStringToStringMapEntry8", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot7", type=xwiki_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachments12: BinaryAssociation = BinaryAssociation(
    name="attachments12",
    ends={
        Property(name="xwiki_AttachmentsType14", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot13", type=xwiki_AttachmentsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_15: BinaryAssociation = BinaryAssociation(
    name="class_15",
    ends={
        Property(name="xwiki_Class17", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot16", type=xwiki_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes18: BinaryAssociation = BinaryAssociation(
    name="classes18",
    ends={
        Property(name="xwiki_ClassesType20", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot19", type=xwiki_ClassesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comment21: BinaryAssociation = BinaryAssociation(
    name="comment21",
    ends={
        Property(name="xwiki_Comment23", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot22", type=xwiki_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments24: BinaryAssociation = BinaryAssociation(
    name="comments24",
    ends={
        Property(name="xwiki_CommentsType26", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot25", type=xwiki_CommentsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history27: BinaryAssociation = BinaryAssociation(
    name="history27",
    ends={
        Property(name="xwiki_HistoryType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot28", type=xwiki_HistoryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object29: BinaryAssociation = BinaryAssociation(
    name="object29",
    ends={
        Property(name="xwiki_Object", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot30", type=xwiki_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects31: BinaryAssociation = BinaryAssociation(
    name="objects31",
    ends={
        Property(name="xwiki_ObjectsType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot32", type=xwiki_ObjectsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spaces50: BinaryAssociation = BinaryAssociation(
    name="spaces50",
    ends={
        Property(name="xwiki_SpacesType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot51", type=xwiki_SpacesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectSummary33: BinaryAssociation = BinaryAssociation(
    name="objectSummary33",
    ends={
        Property(name="xwiki_ObjectSummary", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot34", type=xwiki_ObjectSummary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page35: BinaryAssociation = BinaryAssociation(
    name="page35",
    ends={
        Property(name="xwiki_Page", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot36", type=xwiki_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages37: BinaryAssociation = BinaryAssociation(
    name="pages37",
    ends={
        Property(name="xwiki_PagesType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot38", type=xwiki_PagesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties39: BinaryAssociation = BinaryAssociation(
    name="properties39",
    ends={
        Property(name="xwiki_PropertiesType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot40", type=xwiki_PropertiesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property41: BinaryAssociation = BinaryAssociation(
    name="property41",
    ends={
        Property(name="xwiki_Property43", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot42", type=xwiki_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
searchResult44: BinaryAssociation = BinaryAssociation(
    name="searchResult44",
    ends={
        Property(name="xwiki_SearchResult", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot45", type=xwiki_SearchResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
searchResults46: BinaryAssociation = BinaryAssociation(
    name="searchResults46",
    ends={
        Property(name="xwiki_SearchResultsType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot47", type=xwiki_SearchResultsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
space48: BinaryAssociation = BinaryAssociation(
    name="space48",
    ends={
        Property(name="xwiki_Space", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot49", type=xwiki_Space, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
syntaxes52: BinaryAssociation = BinaryAssociation(
    name="syntaxes52",
    ends={
        Property(name="xwiki_Syntaxes", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot53", type=xwiki_Syntaxes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag54: BinaryAssociation = BinaryAssociation(
    name="tag54",
    ends={
        Property(name="xwiki_Tag", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot55", type=xwiki_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags56: BinaryAssociation = BinaryAssociation(
    name="tags56",
    ends={
        Property(name="xwiki_TagsType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot57", type=xwiki_TagsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translations58: BinaryAssociation = BinaryAssociation(
    name="translations58",
    ends={
        Property(name="xwiki_Translations", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot59", type=xwiki_Translations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wiki60: BinaryAssociation = BinaryAssociation(
    name="wiki60",
    ends={
        Property(name="xwiki_Wiki", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot61", type=xwiki_Wiki, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wikis62: BinaryAssociation = BinaryAssociation(
    name="wikis62",
    ends={
        Property(name="xwiki_WikisType", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot63", type=xwiki_WikisType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xwiki64: BinaryAssociation = BinaryAssociation(
    name="xwiki64",
    ends={
        Property(name="xwiki_XWiki", type=xwiki_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_DocumentRoot65", type=xwiki_XWiki, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
historySummary66: BinaryAssociation = BinaryAssociation(
    name="historySummary66",
    ends={
        Property(name="xwiki_HistoryType67", type=xwiki_HistorySummary, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xwiki_HistorySummary", type=xwiki_HistoryType, multiplicity=Multiplicity(1, 1))
    }
)
link68: BinaryAssociation = BinaryAssociation(
    name="link68",
    ends={
        Property(name="xwiki_Link", type=xwiki_LinkCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_LinkCollection", type=xwiki_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property69: BinaryAssociation = BinaryAssociation(
    name="property69",
    ends={
        Property(name="xwiki_Property71", type=xwiki_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_Object70", type=xwiki_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectSummary72: BinaryAssociation = BinaryAssociation(
    name="objectSummary72",
    ends={
        Property(name="xwiki_ObjectSummary74", type=xwiki_ObjectsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_ObjectsType73", type=xwiki_ObjectSummary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageSummary75: BinaryAssociation = BinaryAssociation(
    name="pageSummary75",
    ends={
        Property(name="xwiki_PageSummary", type=xwiki_PagesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_PagesType76", type=xwiki_PageSummary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translations77: BinaryAssociation = BinaryAssociation(
    name="translations77",
    ends={
        Property(name="xwiki_Translations79", type=xwiki_PageSummary, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_PageSummary78", type=xwiki_Translations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property80: BinaryAssociation = BinaryAssociation(
    name="property80",
    ends={
        Property(name="xwiki_Property82", type=xwiki_PropertiesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_PropertiesType81", type=xwiki_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute83: BinaryAssociation = BinaryAssociation(
    name="attribute83",
    ends={
        Property(name="xwiki_Attribute", type=xwiki_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_Property84", type=xwiki_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object85: BinaryAssociation = BinaryAssociation(
    name="object85",
    ends={
        Property(name="xwiki_Object87", type=xwiki_SearchResult, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_SearchResult86", type=xwiki_Object, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
space91: BinaryAssociation = BinaryAssociation(
    name="space91",
    ends={
        Property(name="xwiki_Space93", type=xwiki_SpacesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_SpacesType92", type=xwiki_Space, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
searchResult88: BinaryAssociation = BinaryAssociation(
    name="searchResult88",
    ends={
        Property(name="xwiki_SearchResult90", type=xwiki_SearchResultsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_SearchResultsType89", type=xwiki_SearchResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translation97: BinaryAssociation = BinaryAssociation(
    name="translation97",
    ends={
        Property(name="xwiki_Translation", type=xwiki_Translations, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_Translations98", type=xwiki_Translation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag94: BinaryAssociation = BinaryAssociation(
    name="tag94",
    ends={
        Property(name="xwiki_Tag96", type=xwiki_TagsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_TagsType95", type=xwiki_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
syntaxes102: BinaryAssociation = BinaryAssociation(
    name="syntaxes102",
    ends={
        Property(name="xwiki_Syntaxes104", type=xwiki_XWiki, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_XWiki103", type=xwiki_Syntaxes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
wiki99: BinaryAssociation = BinaryAssociation(
    name="wiki99",
    ends={
        Property(name="xwiki_Wiki101", type=xwiki_WikisType, multiplicity=Multiplicity(1, 1)),
        Property(name="xwiki_WikisType100", type=xwiki_Wiki, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_xwiki_Attachment_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Attachment)
gen_xwiki_AttachmentsType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_AttachmentsType)
gen_xwiki_Attribute_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Attribute)
gen_xwiki_Class_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Class)
gen_xwiki_ClassesType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_ClassesType)
gen_xwiki_Comment_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Comment)
gen_xwiki_CommentsType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_CommentsType)
gen_xwiki_HistorySummary_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_HistorySummary)
gen_xwiki_HistoryType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_HistoryType)
gen_xwiki_Object_ObjectSummary = Generalization(general=ObjectSummary, specific=xwiki_Object)
gen_xwiki_ObjectsType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_ObjectsType)
gen_xwiki_ObjectSummary_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_ObjectSummary)
gen_xwiki_Page_PageSummary = Generalization(general=PageSummary, specific=xwiki_Page)
gen_xwiki_PagesType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_PagesType)
gen_xwiki_PageSummary_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_PageSummary)
gen_xwiki_PropertiesType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_PropertiesType)
gen_xwiki_Property_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Property)
gen_xwiki_SearchResult_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_SearchResult)
gen_xwiki_SearchResultsType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_SearchResultsType)
gen_xwiki_Space_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Space)
gen_xwiki_SpacesType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_SpacesType)
gen_xwiki_Syntaxes_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Syntaxes)
gen_xwiki_Tag_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Tag)
gen_xwiki_TagsType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_TagsType)
gen_xwiki_Translation_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Translation)
gen_xwiki_Translations_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Translations)
gen_xwiki_Wiki_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_Wiki)
gen_xwiki_WikisType_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_WikisType)
gen_xwiki_XWiki_LinkCollection = Generalization(general=LinkCollection, specific=xwiki_XWiki)

# Domain Model
domain_model = DomainModel(
    name="xwiki",
    types={xwiki_Attachment, LinkCollection, xwiki_AttachmentsType, xwiki_Attribute, xwiki_Class, xwiki_Property, xwiki_ClassesType, xwiki_Comment, xwiki_CommentsType, xwiki_DocumentRoot, xwiki_EStringToStringMapEntry, xwiki_ObjectSummary, xwiki_HistoryType, xwiki_Object, xwiki_ObjectsType, xwiki_SpacesType, xwiki_Page, xwiki_PagesType, xwiki_PropertiesType, xwiki_SearchResult, xwiki_SearchResultsType, xwiki_Space, xwiki_Syntaxes, xwiki_Tag, xwiki_TagsType, xwiki_Translations, xwiki_Wiki, xwiki_WikisType, xwiki_XWiki, xwiki_HistorySummary, xwiki_Link, xwiki_LinkCollection, ObjectSummary, PageSummary, xwiki_PageSummary, xwiki_Translation},
    associations={attachment0, property1, class_2, attachment9, comment4, xMLNSPrefixMap5, xSISchemaLocation6, attachments12, class_15, classes18, comment21, comments24, history27, object29, objects31, spaces50, objectSummary33, page35, pages37, properties39, property41, searchResult44, searchResults46, space48, syntaxes52, tag54, tags56, translations58, wiki60, wikis62, xwiki64, historySummary66, link68, property69, objectSummary72, pageSummary75, translations77, property80, attribute83, object85, space91, searchResult88, translation97, tag94, syntaxes102, wiki99},
    generalizations={gen_xwiki_Attachment_LinkCollection, gen_xwiki_AttachmentsType_LinkCollection, gen_xwiki_Attribute_LinkCollection, gen_xwiki_Class_LinkCollection, gen_xwiki_ClassesType_LinkCollection, gen_xwiki_Comment_LinkCollection, gen_xwiki_CommentsType_LinkCollection, gen_xwiki_HistorySummary_LinkCollection, gen_xwiki_HistoryType_LinkCollection, gen_xwiki_Object_ObjectSummary, gen_xwiki_ObjectsType_LinkCollection, gen_xwiki_ObjectSummary_LinkCollection, gen_xwiki_Page_PageSummary, gen_xwiki_PagesType_LinkCollection, gen_xwiki_PageSummary_LinkCollection, gen_xwiki_PropertiesType_LinkCollection, gen_xwiki_Property_LinkCollection, gen_xwiki_SearchResult_LinkCollection, gen_xwiki_SearchResultsType_LinkCollection, gen_xwiki_Space_LinkCollection, gen_xwiki_SpacesType_LinkCollection, gen_xwiki_Syntaxes_LinkCollection, gen_xwiki_Tag_LinkCollection, gen_xwiki_TagsType_LinkCollection, gen_xwiki_Translation_LinkCollection, gen_xwiki_Translations_LinkCollection, gen_xwiki_Wiki_LinkCollection, gen_xwiki_WikisType_LinkCollection, gen_xwiki_XWiki_LinkCollection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)