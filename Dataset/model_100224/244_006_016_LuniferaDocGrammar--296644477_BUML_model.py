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
DocType: Enumeration = Enumeration(
    name="DocType",
    literals={
            EnumerationLiteral(name="BPM_TASK"),
			EnumerationLiteral(name="VAACLIPSE_VIEW"),
			EnumerationLiteral(name="UI"),
			EnumerationLiteral(name="ENTITY"),
			EnumerationLiteral(name="DTO"),
			EnumerationLiteral(name="BPM_PROCESS")
    }
)

# Classes
luniferadoc_NamedDocument = Class(name="luniferadoc_NamedDocument", is_abstract=True)
luniferadoc_DocumentInclude = Class(name="luniferadoc_DocumentInclude")
LuniferaDocDocument = Class(name="LuniferaDocDocument")
luniferadoc_document_EntityDescription = Class(name="luniferadoc_document_EntityDescription")
RichString = Class(name="RichString")
luniferadoc_document_EntityFields = Class(name="luniferadoc_document_EntityFields")
EntityField = Class(name="EntityField")
luniferadoc_document_EntityField = Class(name="luniferadoc_document_EntityField")
luniferadoc_document_LuniferaDocDocument = Class(name="luniferadoc_document_LuniferaDocDocument", is_abstract=True)
NamedDocument = Class(name="NamedDocument")
luniferadoc_document_EntityDocument = Class(name="luniferadoc_document_EntityDocument")
EntityDescription = Class(name="EntityDescription")
EntityFields = Class(name="EntityFields")
DTOProperties = Class(name="DTOProperties")
luniferadoc_document_DTODescription = Class(name="luniferadoc_document_DTODescription")
luniferadoc_document_DTOProperties = Class(name="luniferadoc_document_DTOProperties")
DTOProperty = Class(name="DTOProperty")
luniferadoc_document_DTODocument = Class(name="luniferadoc_document_DTODocument")
DTODescription = Class(name="DTODescription")
luniferadoc_document_BPMHumanTaskDocument = Class(name="luniferadoc_document_BPMHumanTaskDocument")
BPMHumanTaskDescription = Class(name="BPMHumanTaskDescription")
luniferadoc_document_BPMHumanTaskDescription = Class(name="luniferadoc_document_BPMHumanTaskDescription")
luniferadoc_document_DTOProperty = Class(name="luniferadoc_document_DTOProperty")
luniferadoc_document_BPMProcessDocument = Class(name="luniferadoc_document_BPMProcessDocument")
BPMProcessDescription = Class(name="BPMProcessDescription")
luniferadoc_document_BPMProcessDescription = Class(name="luniferadoc_document_BPMProcessDescription")
UIDescription = Class(name="UIDescription")
luniferadoc_document_UIDescription = Class(name="luniferadoc_document_UIDescription")
luniferadoc_document_GeneralDocument = Class(name="luniferadoc_document_GeneralDocument")
LuniferaDocLayout = Class(name="LuniferaDocLayout")
document_luniferadoc_DocumentInclude = Class(name="document_luniferadoc_DocumentInclude")
luniferadoc_document_VaaclipseViewDocument = Class(name="luniferadoc_document_VaaclipseViewDocument")
VaaclipseViewDescription = Class(name="VaaclipseViewDescription")
luniferadoc_document_VaaclipseViewDescription = Class(name="luniferadoc_document_VaaclipseViewDescription")
luniferadoc_document_UIDocument = Class(name="luniferadoc_document_UIDocument")
luniferadoc_document_BPMProcessLayout = Class(name="luniferadoc_document_BPMProcessLayout")
luniferadoc_document_BPMHumanTaskLayout = Class(name="luniferadoc_document_BPMHumanTaskLayout")
luniferadoc_document_VaaclipseViewLayout = Class(name="luniferadoc_document_VaaclipseViewLayout")
luniferadoc_document_UILayout = Class(name="luniferadoc_document_UILayout")
luniferadoc_richstring_RichStringElseIf = Class(name="luniferadoc_richstring_RichStringElseIf")
richstring_luniferadoc_XExpression = Class(name="richstring_luniferadoc_XExpression")
luniferadoc_document_LuniferaDocLayout = Class(name="luniferadoc_document_LuniferaDocLayout", is_abstract=True)
document_luniferadoc_XImportDeclaration = Class(name="document_luniferadoc_XImportDeclaration")
luniferadoc_document_EntityLayout = Class(name="luniferadoc_document_EntityLayout")
luniferadoc_document_DTOLayout = Class(name="luniferadoc_document_DTOLayout")
luniferadoc_richstring_RichStringIf = Class(name="luniferadoc_richstring_RichStringIf")
XExpression = Class(name="XExpression")
luniferadoc_richstring_RichString = Class(name="luniferadoc_richstring_RichString")
XBlockExpression = Class(name="XBlockExpression")
luniferadoc_richstring_RichStringLiteral = Class(name="luniferadoc_richstring_RichStringLiteral")
XStringLiteral = Class(name="XStringLiteral")
luniferadoc_richstring_RichStringForLoop = Class(name="luniferadoc_richstring_RichStringForLoop")
XForLoopExpression = Class(name="XForLoopExpression")
luniferadoc_richstring_RichStringExample = Class(name="luniferadoc_richstring_RichStringExample")
RichStringMarkup = Class(name="RichStringMarkup")
luniferadoc_richstring_RichStringH1 = Class(name="luniferadoc_richstring_RichStringH1")
luniferadoc_richstring_RichStringH2 = Class(name="luniferadoc_richstring_RichStringH2")
luniferadoc_richstring_RichStringH3 = Class(name="luniferadoc_richstring_RichStringH3")
luniferadoc_richstring_RichStringH4 = Class(name="luniferadoc_richstring_RichStringH4")
RichStringElseIf = Class(name="RichStringElseIf")
luniferadoc_richstring_RichStringMarkup = Class(name="luniferadoc_richstring_RichStringMarkup")
luniferadoc_richstring_RichStringRef = Class(name="luniferadoc_richstring_RichStringRef")
luniferadoc_richstring_RichStringBold = Class(name="luniferadoc_richstring_RichStringBold")
luniferadoc_richstring_RichStringH5 = Class(name="luniferadoc_richstring_RichStringH5")
luniferadoc_richstring_RichStringH6 = Class(name="luniferadoc_richstring_RichStringH6")
luniferadoc_richstring_RichStringChapter = Class(name="luniferadoc_richstring_RichStringChapter")
luniferadoc_richstring_RichStringSection = Class(name="luniferadoc_richstring_RichStringSection")
luniferadoc_richstring_RichStringSubsection = Class(name="luniferadoc_richstring_RichStringSubsection")
luniferadoc_richstring_RichStringURL = Class(name="luniferadoc_richstring_RichStringURL")
luniferadoc_richstring_RichStringMailto = Class(name="luniferadoc_richstring_RichStringMailto")
luniferadoc_richstring_RichStringSkype = Class(name="luniferadoc_richstring_RichStringSkype")
luniferadoc_richstring_RichStringUnderline = Class(name="luniferadoc_richstring_RichStringUnderline")
luniferadoc_richstring_RichStringItalic = Class(name="luniferadoc_richstring_RichStringItalic")
luniferadoc_richstring_RichStringImg = Class(name="luniferadoc_richstring_RichStringImg")
luniferadoc_richstring_RichStringTable = Class(name="luniferadoc_richstring_RichStringTable")
RichStringTableRow = Class(name="RichStringTableRow")
luniferadoc_richstring_RichStringMovie = Class(name="luniferadoc_richstring_RichStringMovie")
luniferadoc_richstring_RichStringCode = Class(name="luniferadoc_richstring_RichStringCode")
luniferadoc_richstring_RichStringTableData = Class(name="luniferadoc_richstring_RichStringTableData")
luniferadoc_richstring_RichStringOpenView = Class(name="luniferadoc_richstring_RichStringOpenView")
luniferadoc_richstring_RichStringStartProcess = Class(name="luniferadoc_richstring_RichStringStartProcess")
luniferadoc_richstring_RichStringEntityRef = Class(name="luniferadoc_richstring_RichStringEntityRef")
luniferadoc_richstring_RichStringTableRow = Class(name="luniferadoc_richstring_RichStringTableRow")
RichStringTableData = Class(name="RichStringTableData")
BPMHumanTaskDocument = Class(name="BPMHumanTaskDocument")
luniferadoc_richstring_RichStringViewRef = Class(name="luniferadoc_richstring_RichStringViewRef")
VaaclipseViewDocument = Class(name="VaaclipseViewDocument")
luniferadoc_richstring_RichStringUIRef = Class(name="luniferadoc_richstring_RichStringUIRef")
UIDocument = Class(name="UIDocument")
EntityDocument = Class(name="EntityDocument")
luniferadoc_richstring_RichStringDTORef = Class(name="luniferadoc_richstring_RichStringDTORef")
DTODocument = Class(name="DTODocument")
luniferadoc_richstring_RichStringProcessRef = Class(name="luniferadoc_richstring_RichStringProcessRef")
BPMProcessDocument = Class(name="BPMProcessDocument")
luniferadoc_richstring_RichStringTaskRef = Class(name="luniferadoc_richstring_RichStringTaskRef")
luniferadoc_richstring_RichStringListElement = Class(name="luniferadoc_richstring_RichStringListElement")
luniferadoc_richstring_RichStringSpan = Class(name="luniferadoc_richstring_RichStringSpan")
luniferadoc_richstring_RichStringList = Class(name="luniferadoc_richstring_RichStringList")
RichStringListElement = Class(name="RichStringListElement")
luniferadoc_richstring_RichStringOrderedList = Class(name="luniferadoc_richstring_RichStringOrderedList")

# luniferadoc_NamedDocument class attributes and methods
luniferadoc_NamedDocument_name: Property = Property(name="name", type=StringType)
luniferadoc_NamedDocument.attributes={luniferadoc_NamedDocument_name}

# luniferadoc_DocumentInclude class attributes and methods
luniferadoc_DocumentInclude_varName: Property = Property(name="varName", type=StringType)
luniferadoc_DocumentInclude.attributes={luniferadoc_DocumentInclude_varName}

# LuniferaDocDocument class attributes and methods

# luniferadoc_document_EntityDescription class attributes and methods

# RichString class attributes and methods

# luniferadoc_document_EntityFields class attributes and methods

# EntityField class attributes and methods

# luniferadoc_document_EntityField class attributes and methods
luniferadoc_document_EntityField_name: Property = Property(name="name", type=StringType)
luniferadoc_document_EntityField_type: Property = Property(name="type", type=StringType)
luniferadoc_document_EntityField_length: Property = Property(name="length", type=IntegerType)
luniferadoc_document_EntityField_pk: Property = Property(name="pk", type=BooleanType)
luniferadoc_document_EntityField_nullable: Property = Property(name="nullable", type=BooleanType)
luniferadoc_document_EntityField.attributes={luniferadoc_document_EntityField_pk, luniferadoc_document_EntityField_nullable, luniferadoc_document_EntityField_name, luniferadoc_document_EntityField_type, luniferadoc_document_EntityField_length}

# luniferadoc_document_LuniferaDocDocument class attributes and methods

# NamedDocument class attributes and methods

# luniferadoc_document_EntityDocument class attributes and methods
luniferadoc_document_EntityDocument_entityClass: Property = Property(name="entityClass", type=StringType)
luniferadoc_document_EntityDocument.attributes={luniferadoc_document_EntityDocument_entityClass}

# EntityDescription class attributes and methods

# EntityFields class attributes and methods

# DTOProperties class attributes and methods

# luniferadoc_document_DTODescription class attributes and methods

# luniferadoc_document_DTOProperties class attributes and methods

# DTOProperty class attributes and methods

# luniferadoc_document_DTODocument class attributes and methods
luniferadoc_document_DTODocument_dtoClass: Property = Property(name="dtoClass", type=StringType)
luniferadoc_document_DTODocument.attributes={luniferadoc_document_DTODocument_dtoClass}

# DTODescription class attributes and methods

# luniferadoc_document_BPMHumanTaskDocument class attributes and methods
luniferadoc_document_BPMHumanTaskDocument_task: Property = Property(name="task", type=StringType)
luniferadoc_document_BPMHumanTaskDocument.attributes={luniferadoc_document_BPMHumanTaskDocument_task}

# BPMHumanTaskDescription class attributes and methods

# luniferadoc_document_BPMHumanTaskDescription class attributes and methods

# luniferadoc_document_DTOProperty class attributes and methods
luniferadoc_document_DTOProperty_name: Property = Property(name="name", type=StringType)
luniferadoc_document_DTOProperty.attributes={luniferadoc_document_DTOProperty_name}

# luniferadoc_document_BPMProcessDocument class attributes and methods
luniferadoc_document_BPMProcessDocument_process: Property = Property(name="process", type=StringType)
luniferadoc_document_BPMProcessDocument.attributes={luniferadoc_document_BPMProcessDocument_process}

# BPMProcessDescription class attributes and methods

# luniferadoc_document_BPMProcessDescription class attributes and methods

# UIDescription class attributes and methods

# luniferadoc_document_UIDescription class attributes and methods

# luniferadoc_document_GeneralDocument class attributes and methods

# LuniferaDocLayout class attributes and methods

# document_luniferadoc_DocumentInclude class attributes and methods

# luniferadoc_document_VaaclipseViewDocument class attributes and methods
luniferadoc_document_VaaclipseViewDocument_view: Property = Property(name="view", type=StringType)
luniferadoc_document_VaaclipseViewDocument.attributes={luniferadoc_document_VaaclipseViewDocument_view}

# VaaclipseViewDescription class attributes and methods

# luniferadoc_document_VaaclipseViewDescription class attributes and methods

# luniferadoc_document_UIDocument class attributes and methods
luniferadoc_document_UIDocument_ui: Property = Property(name="ui", type=StringType)
luniferadoc_document_UIDocument.attributes={luniferadoc_document_UIDocument_ui}

# luniferadoc_document_BPMProcessLayout class attributes and methods

# luniferadoc_document_BPMHumanTaskLayout class attributes and methods

# luniferadoc_document_VaaclipseViewLayout class attributes and methods

# luniferadoc_document_UILayout class attributes and methods

# luniferadoc_richstring_RichStringElseIf class attributes and methods

# richstring_luniferadoc_XExpression class attributes and methods

# luniferadoc_document_LuniferaDocLayout class attributes and methods

# document_luniferadoc_XImportDeclaration class attributes and methods

# luniferadoc_document_EntityLayout class attributes and methods

# luniferadoc_document_DTOLayout class attributes and methods

# luniferadoc_richstring_RichStringIf class attributes and methods

# XExpression class attributes and methods

# luniferadoc_richstring_RichString class attributes and methods

# XBlockExpression class attributes and methods

# luniferadoc_richstring_RichStringLiteral class attributes and methods

# XStringLiteral class attributes and methods

# luniferadoc_richstring_RichStringForLoop class attributes and methods

# XForLoopExpression class attributes and methods

# luniferadoc_richstring_RichStringExample class attributes and methods

# RichStringMarkup class attributes and methods

# luniferadoc_richstring_RichStringH1 class attributes and methods

# luniferadoc_richstring_RichStringH2 class attributes and methods

# luniferadoc_richstring_RichStringH3 class attributes and methods

# luniferadoc_richstring_RichStringH4 class attributes and methods

# RichStringElseIf class attributes and methods

# luniferadoc_richstring_RichStringMarkup class attributes and methods
luniferadoc_richstring_RichStringMarkup_id: Property = Property(name="id", type=StringType)
luniferadoc_richstring_RichStringMarkup_styleClass: Property = Property(name="styleClass", type=StringType)
luniferadoc_richstring_RichStringMarkup.attributes={luniferadoc_richstring_RichStringMarkup_id, luniferadoc_richstring_RichStringMarkup_styleClass}

# luniferadoc_richstring_RichStringRef class attributes and methods
luniferadoc_richstring_RichStringRef_refId: Property = Property(name="refId", type=StringType)
luniferadoc_richstring_RichStringRef.attributes={luniferadoc_richstring_RichStringRef_refId}

# luniferadoc_richstring_RichStringBold class attributes and methods

# luniferadoc_richstring_RichStringH5 class attributes and methods

# luniferadoc_richstring_RichStringH6 class attributes and methods

# luniferadoc_richstring_RichStringChapter class attributes and methods
luniferadoc_richstring_RichStringChapter_name: Property = Property(name="name", type=StringType)
luniferadoc_richstring_RichStringChapter.attributes={luniferadoc_richstring_RichStringChapter_name}

# luniferadoc_richstring_RichStringSection class attributes and methods
luniferadoc_richstring_RichStringSection_name: Property = Property(name="name", type=StringType)
luniferadoc_richstring_RichStringSection.attributes={luniferadoc_richstring_RichStringSection_name}

# luniferadoc_richstring_RichStringSubsection class attributes and methods
luniferadoc_richstring_RichStringSubsection_name: Property = Property(name="name", type=StringType)
luniferadoc_richstring_RichStringSubsection.attributes={luniferadoc_richstring_RichStringSubsection_name}

# luniferadoc_richstring_RichStringURL class attributes and methods
luniferadoc_richstring_RichStringURL_location: Property = Property(name="location", type=StringType)
luniferadoc_richstring_RichStringURL.attributes={luniferadoc_richstring_RichStringURL_location}

# luniferadoc_richstring_RichStringMailto class attributes and methods
luniferadoc_richstring_RichStringMailto_email: Property = Property(name="email", type=StringType)
luniferadoc_richstring_RichStringMailto.attributes={luniferadoc_richstring_RichStringMailto_email}

# luniferadoc_richstring_RichStringSkype class attributes and methods
luniferadoc_richstring_RichStringSkype_target: Property = Property(name="target", type=StringType)
luniferadoc_richstring_RichStringSkype.attributes={luniferadoc_richstring_RichStringSkype_target}

# luniferadoc_richstring_RichStringUnderline class attributes and methods

# luniferadoc_richstring_RichStringItalic class attributes and methods

# luniferadoc_richstring_RichStringImg class attributes and methods
luniferadoc_richstring_RichStringImg_src: Property = Property(name="src", type=StringType)
luniferadoc_richstring_RichStringImg_alt: Property = Property(name="alt", type=StringType)
luniferadoc_richstring_RichStringImg_width: Property = Property(name="width", type=StringType)
luniferadoc_richstring_RichStringImg_height: Property = Property(name="height", type=StringType)
luniferadoc_richstring_RichStringImg.attributes={luniferadoc_richstring_RichStringImg_height, luniferadoc_richstring_RichStringImg_width, luniferadoc_richstring_RichStringImg_alt, luniferadoc_richstring_RichStringImg_src}

# luniferadoc_richstring_RichStringTable class attributes and methods

# RichStringTableRow class attributes and methods

# luniferadoc_richstring_RichStringMovie class attributes and methods
luniferadoc_richstring_RichStringMovie_src: Property = Property(name="src", type=StringType)
luniferadoc_richstring_RichStringMovie_width: Property = Property(name="width", type=StringType)
luniferadoc_richstring_RichStringMovie_height: Property = Property(name="height", type=StringType)
luniferadoc_richstring_RichStringMovie_type: Property = Property(name="type", type=StringType)
luniferadoc_richstring_RichStringMovie.attributes={luniferadoc_richstring_RichStringMovie_type, luniferadoc_richstring_RichStringMovie_width, luniferadoc_richstring_RichStringMovie_height, luniferadoc_richstring_RichStringMovie_src}

# luniferadoc_richstring_RichStringCode class attributes and methods
luniferadoc_richstring_RichStringCode_lang: Property = Property(name="lang", type=StringType)
luniferadoc_richstring_RichStringCode.attributes={luniferadoc_richstring_RichStringCode_lang}

# luniferadoc_richstring_RichStringTableData class attributes and methods

# luniferadoc_richstring_RichStringOpenView class attributes and methods
luniferadoc_richstring_RichStringOpenView_viewId: Property = Property(name="viewId", type=StringType)
luniferadoc_richstring_RichStringOpenView.attributes={luniferadoc_richstring_RichStringOpenView_viewId}

# luniferadoc_richstring_RichStringStartProcess class attributes and methods
luniferadoc_richstring_RichStringStartProcess_processId: Property = Property(name="processId", type=StringType)
luniferadoc_richstring_RichStringStartProcess.attributes={luniferadoc_richstring_RichStringStartProcess_processId}

# luniferadoc_richstring_RichStringEntityRef class attributes and methods

# luniferadoc_richstring_RichStringTableRow class attributes and methods

# RichStringTableData class attributes and methods

# BPMHumanTaskDocument class attributes and methods

# luniferadoc_richstring_RichStringViewRef class attributes and methods

# VaaclipseViewDocument class attributes and methods

# luniferadoc_richstring_RichStringUIRef class attributes and methods

# UIDocument class attributes and methods

# EntityDocument class attributes and methods

# luniferadoc_richstring_RichStringDTORef class attributes and methods

# DTODocument class attributes and methods

# luniferadoc_richstring_RichStringProcessRef class attributes and methods

# BPMProcessDocument class attributes and methods

# luniferadoc_richstring_RichStringTaskRef class attributes and methods

# luniferadoc_richstring_RichStringListElement class attributes and methods

# luniferadoc_richstring_RichStringSpan class attributes and methods

# luniferadoc_richstring_RichStringList class attributes and methods

# RichStringListElement class attributes and methods

# luniferadoc_richstring_RichStringOrderedList class attributes and methods

# Relationships
include0: BinaryAssociation = BinaryAssociation(
    name="include0",
    ends={
        Property(name="LuniferaDocDocument", type=luniferadoc_DocumentInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_DocumentInclude", type=LuniferaDocDocument, multiplicity=Multiplicity(0, 1))
    }
)
content4: BinaryAssociation = BinaryAssociation(
    name="content4",
    ends={
        Property(name="RichString", type=luniferadoc_document_EntityDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_EntityDescription", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields5: BinaryAssociation = BinaryAssociation(
    name="fields5",
    ends={
        Property(name="EntityField", type=luniferadoc_document_EntityFields, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_EntityFields", type=EntityField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description1: BinaryAssociation = BinaryAssociation(
    name="description1",
    ends={
        Property(name="EntityDescription", type=luniferadoc_document_EntityDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_EntityDocument", type=EntityDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields2: BinaryAssociation = BinaryAssociation(
    name="fields2",
    ends={
        Property(name="EntityFields", type=luniferadoc_document_EntityDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_EntityDocument3", type=EntityFields, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="DTOProperties", type=luniferadoc_document_DTODocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_DTODocument10", type=DTOProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content11: BinaryAssociation = BinaryAssociation(
    name="content11",
    ends={
        Property(name="RichString12", type=luniferadoc_document_DTODescription, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_DTODescription", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties13: BinaryAssociation = BinaryAssociation(
    name="properties13",
    ends={
        Property(name="DTOProperty", type=luniferadoc_document_DTOProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_DTOProperties", type=DTOProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description6: BinaryAssociation = BinaryAssociation(
    name="description6",
    ends={
        Property(name="RichString7", type=luniferadoc_document_EntityField, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_EntityField", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description8: BinaryAssociation = BinaryAssociation(
    name="description8",
    ends={
        Property(name="DTODescription", type=luniferadoc_document_DTODocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_DTODocument", type=DTODescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content17: BinaryAssociation = BinaryAssociation(
    name="content17",
    ends={
        Property(name="luniferadoc_document_BPMProcessDescription", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="RichString18", type=luniferadoc_document_BPMProcessDescription, multiplicity=Multiplicity(1, 1))
    }
)
description19: BinaryAssociation = BinaryAssociation(
    name="description19",
    ends={
        Property(name="BPMHumanTaskDescription", type=luniferadoc_document_BPMHumanTaskDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_BPMHumanTaskDocument", type=BPMHumanTaskDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description14: BinaryAssociation = BinaryAssociation(
    name="description14",
    ends={
        Property(name="RichString15", type=luniferadoc_document_DTOProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_DTOProperty", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description16: BinaryAssociation = BinaryAssociation(
    name="description16",
    ends={
        Property(name="BPMProcessDescription", type=luniferadoc_document_BPMProcessDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_BPMProcessDocument", type=BPMProcessDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description25: BinaryAssociation = BinaryAssociation(
    name="description25",
    ends={
        Property(name="UIDescription", type=luniferadoc_document_UIDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_UIDocument", type=UIDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content26: BinaryAssociation = BinaryAssociation(
    name="content26",
    ends={
        Property(name="RichString27", type=luniferadoc_document_UIDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_UIDescription", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content20: BinaryAssociation = BinaryAssociation(
    name="content20",
    ends={
        Property(name="RichString21", type=luniferadoc_document_BPMHumanTaskDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_BPMHumanTaskDescription", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description22: BinaryAssociation = BinaryAssociation(
    name="description22",
    ends={
        Property(name="VaaclipseViewDescription", type=luniferadoc_document_VaaclipseViewDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_VaaclipseViewDocument", type=VaaclipseViewDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content23: BinaryAssociation = BinaryAssociation(
    name="content23",
    ends={
        Property(name="RichString24", type=luniferadoc_document_VaaclipseViewDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_VaaclipseViewDescription", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_33: BinaryAssociation = BinaryAssociation(
    name="if_33",
    ends={
        Property(name="richstring_luniferadoc_XExpression", type=luniferadoc_richstring_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringElseIf", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
includes28: BinaryAssociation = BinaryAssociation(
    name="includes28",
    ends={
        Property(name="document_luniferadoc_DocumentInclude", type=luniferadoc_document_GeneralDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_GeneralDocument", type=document_luniferadoc_DocumentInclude, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content29: BinaryAssociation = BinaryAssociation(
    name="content29",
    ends={
        Property(name="RichString30", type=luniferadoc_document_LuniferaDocLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_LuniferaDocLayout", type=RichString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports31: BinaryAssociation = BinaryAssociation(
    name="imports31",
    ends={
        Property(name="document_luniferadoc_XImportDeclaration", type=luniferadoc_document_LuniferaDocLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_document_LuniferaDocLayout32", type=document_luniferadoc_XImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
after42: BinaryAssociation = BinaryAssociation(
    name="after42",
    ends={
        Property(name="richstring_luniferadoc_XExpression44", type=luniferadoc_richstring_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringForLoop43", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_45: BinaryAssociation = BinaryAssociation(
    name="if_45",
    ends={
        Property(name="richstring_luniferadoc_XExpression46", type=luniferadoc_richstring_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringIf", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then47: BinaryAssociation = BinaryAssociation(
    name="then47",
    ends={
        Property(name="richstring_luniferadoc_XExpression49", type=luniferadoc_richstring_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringIf48", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then34: BinaryAssociation = BinaryAssociation(
    name="then34",
    ends={
        Property(name="richstring_luniferadoc_XExpression36", type=luniferadoc_richstring_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringElseIf35", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before37: BinaryAssociation = BinaryAssociation(
    name="before37",
    ends={
        Property(name="richstring_luniferadoc_XExpression38", type=luniferadoc_richstring_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringForLoop", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
separator39: BinaryAssociation = BinaryAssociation(
    name="separator39",
    ends={
        Property(name="richstring_luniferadoc_XExpression41", type=luniferadoc_richstring_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringForLoop40", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfs50: BinaryAssociation = BinaryAssociation(
    name="elseIfs50",
    ends={
        Property(name="RichStringElseIf", type=luniferadoc_richstring_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringIf51", type=RichStringElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else_52: BinaryAssociation = BinaryAssociation(
    name="else_52",
    ends={
        Property(name="richstring_luniferadoc_XExpression54", type=luniferadoc_richstring_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringIf53", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="richstring_luniferadoc_XExpression56", type=luniferadoc_richstring_RichStringMarkup, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringMarkup", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text57: BinaryAssociation = BinaryAssociation(
    name="text57",
    ends={
        Property(name="richstring_luniferadoc_XExpression58", type=luniferadoc_richstring_RichStringURL, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringURL", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content61: BinaryAssociation = BinaryAssociation(
    name="content61",
    ends={
        Property(name="richstring_luniferadoc_XExpression62", type=luniferadoc_richstring_RichStringMailto, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringMailto", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content63: BinaryAssociation = BinaryAssociation(
    name="content63",
    ends={
        Property(name="richstring_luniferadoc_XExpression64", type=luniferadoc_richstring_RichStringSkype, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringSkype", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content59: BinaryAssociation = BinaryAssociation(
    name="content59",
    ends={
        Property(name="richstring_luniferadoc_XExpression60", type=luniferadoc_richstring_RichStringImg, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringImg", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content67: BinaryAssociation = BinaryAssociation(
    name="content67",
    ends={
        Property(name="richstring_luniferadoc_XExpression68", type=luniferadoc_richstring_RichStringCode, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringCode", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows69: BinaryAssociation = BinaryAssociation(
    name="rows69",
    ends={
        Property(name="RichStringTableRow", type=luniferadoc_richstring_RichStringTable, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringTable", type=RichStringTableRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content65: BinaryAssociation = BinaryAssociation(
    name="content65",
    ends={
        Property(name="richstring_luniferadoc_XExpression66", type=luniferadoc_richstring_RichStringMovie, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringMovie", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions70: BinaryAssociation = BinaryAssociation(
    name="expressions70",
    ends={
        Property(name="richstring_luniferadoc_XExpression72", type=luniferadoc_richstring_RichStringTable, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringTable71", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns73: BinaryAssociation = BinaryAssociation(
    name="columns73",
    ends={
        Property(name="RichStringTableData", type=luniferadoc_richstring_RichStringTableRow, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringTableRow", type=RichStringTableData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions74: BinaryAssociation = BinaryAssociation(
    name="expressions74",
    ends={
        Property(name="richstring_luniferadoc_XExpression76", type=luniferadoc_richstring_RichStringTableRow, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringTableRow75", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskDoc80: BinaryAssociation = BinaryAssociation(
    name="taskDoc80",
    ends={
        Property(name="BPMHumanTaskDocument", type=luniferadoc_richstring_RichStringTaskRef, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringTaskRef", type=BPMHumanTaskDocument, multiplicity=Multiplicity(0, 1))
    }
)
viewDoc81: BinaryAssociation = BinaryAssociation(
    name="viewDoc81",
    ends={
        Property(name="VaaclipseViewDocument", type=luniferadoc_richstring_RichStringViewRef, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringViewRef", type=VaaclipseViewDocument, multiplicity=Multiplicity(0, 1))
    }
)
entityDoc77: BinaryAssociation = BinaryAssociation(
    name="entityDoc77",
    ends={
        Property(name="EntityDocument", type=luniferadoc_richstring_RichStringEntityRef, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringEntityRef", type=EntityDocument, multiplicity=Multiplicity(0, 1))
    }
)
dtoDoc78: BinaryAssociation = BinaryAssociation(
    name="dtoDoc78",
    ends={
        Property(name="DTODocument", type=luniferadoc_richstring_RichStringDTORef, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringDTORef", type=DTODocument, multiplicity=Multiplicity(0, 1))
    }
)
processDoc79: BinaryAssociation = BinaryAssociation(
    name="processDoc79",
    ends={
        Property(name="BPMProcessDocument", type=luniferadoc_richstring_RichStringProcessRef, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringProcessRef", type=BPMProcessDocument, multiplicity=Multiplicity(0, 1))
    }
)
elements87: BinaryAssociation = BinaryAssociation(
    name="elements87",
    ends={
        Property(name="RichStringListElement88", type=luniferadoc_richstring_RichStringOrderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringOrderedList", type=RichStringListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions89: BinaryAssociation = BinaryAssociation(
    name="expressions89",
    ends={
        Property(name="richstring_luniferadoc_XExpression91", type=luniferadoc_richstring_RichStringOrderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringOrderedList90", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uiDoc82: BinaryAssociation = BinaryAssociation(
    name="uiDoc82",
    ends={
        Property(name="UIDocument", type=luniferadoc_richstring_RichStringUIRef, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringUIRef", type=UIDocument, multiplicity=Multiplicity(0, 1))
    }
)
elements83: BinaryAssociation = BinaryAssociation(
    name="elements83",
    ends={
        Property(name="RichStringListElement", type=luniferadoc_richstring_RichStringList, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringList", type=RichStringListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions84: BinaryAssociation = BinaryAssociation(
    name="expressions84",
    ends={
        Property(name="richstring_luniferadoc_XExpression86", type=luniferadoc_richstring_RichStringList, multiplicity=Multiplicity(1, 1)),
        Property(name="luniferadoc_richstring_RichStringList85", type=richstring_luniferadoc_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_luniferadoc_document_LuniferaDocDocument_NamedDocument = Generalization(general=NamedDocument, specific=luniferadoc_document_LuniferaDocDocument)
gen_luniferadoc_document_EntityDocument_LuniferaDocDocument = Generalization(general=LuniferaDocDocument, specific=luniferadoc_document_EntityDocument)
gen_luniferadoc_document_DTODocument_LuniferaDocDocument = Generalization(general=LuniferaDocDocument, specific=luniferadoc_document_DTODocument)
gen_luniferadoc_document_BPMHumanTaskDocument_LuniferaDocDocument = Generalization(general=LuniferaDocDocument, specific=luniferadoc_document_BPMHumanTaskDocument)
gen_luniferadoc_document_BPMProcessDocument_LuniferaDocDocument = Generalization(general=LuniferaDocDocument, specific=luniferadoc_document_BPMProcessDocument)
gen_luniferadoc_document_GeneralDocument_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_GeneralDocument)
gen_luniferadoc_document_VaaclipseViewDocument_LuniferaDocDocument = Generalization(general=LuniferaDocDocument, specific=luniferadoc_document_VaaclipseViewDocument)
gen_luniferadoc_document_UIDocument_LuniferaDocDocument = Generalization(general=LuniferaDocDocument, specific=luniferadoc_document_UIDocument)
gen_luniferadoc_document_BPMProcessLayout_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_BPMProcessLayout)
gen_luniferadoc_document_BPMHumanTaskLayout_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_BPMHumanTaskLayout)
gen_luniferadoc_document_VaaclipseViewLayout_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_VaaclipseViewLayout)
gen_luniferadoc_document_UILayout_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_UILayout)
gen_luniferadoc_document_LuniferaDocLayout_NamedDocument = Generalization(general=NamedDocument, specific=luniferadoc_document_LuniferaDocLayout)
gen_luniferadoc_document_EntityLayout_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_EntityLayout)
gen_luniferadoc_document_DTOLayout_LuniferaDocLayout = Generalization(general=LuniferaDocLayout, specific=luniferadoc_document_DTOLayout)
gen_luniferadoc_richstring_RichStringIf_XExpression = Generalization(general=XExpression, specific=luniferadoc_richstring_RichStringIf)
gen_luniferadoc_richstring_RichString_XBlockExpression = Generalization(general=XBlockExpression, specific=luniferadoc_richstring_RichString)
gen_luniferadoc_richstring_RichStringLiteral_XStringLiteral = Generalization(general=XStringLiteral, specific=luniferadoc_richstring_RichStringLiteral)
gen_luniferadoc_richstring_RichStringForLoop_XForLoopExpression = Generalization(general=XForLoopExpression, specific=luniferadoc_richstring_RichStringForLoop)
gen_luniferadoc_richstring_RichStringExample_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringExample)
gen_luniferadoc_richstring_RichStringH1_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringH1)
gen_luniferadoc_richstring_RichStringH2_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringH2)
gen_luniferadoc_richstring_RichStringH3_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringH3)
gen_luniferadoc_richstring_RichStringH4_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringH4)
gen_luniferadoc_richstring_RichStringMarkup_XExpression = Generalization(general=XExpression, specific=luniferadoc_richstring_RichStringMarkup)
gen_luniferadoc_richstring_RichStringURL_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringURL)
gen_luniferadoc_richstring_RichStringRef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringRef)
gen_luniferadoc_richstring_RichStringBold_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringBold)
gen_luniferadoc_richstring_RichStringH5_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringH5)
gen_luniferadoc_richstring_RichStringH6_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringH6)
gen_luniferadoc_richstring_RichStringChapter_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringChapter)
gen_luniferadoc_richstring_RichStringSection_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringSection)
gen_luniferadoc_richstring_RichStringSubsection_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringSubsection)
gen_luniferadoc_richstring_RichStringMailto_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringMailto)
gen_luniferadoc_richstring_RichStringSkype_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringSkype)
gen_luniferadoc_richstring_RichStringUnderline_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringUnderline)
gen_luniferadoc_richstring_RichStringItalic_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringItalic)
gen_luniferadoc_richstring_RichStringImg_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringImg)
gen_luniferadoc_richstring_RichStringTable_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringTable)
gen_luniferadoc_richstring_RichStringMovie_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringMovie)
gen_luniferadoc_richstring_RichStringCode_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringCode)
gen_luniferadoc_richstring_RichStringTableData_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringTableData)
gen_luniferadoc_richstring_RichStringOpenView_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringOpenView)
gen_luniferadoc_richstring_RichStringStartProcess_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringStartProcess)
gen_luniferadoc_richstring_RichStringEntityRef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringEntityRef)
gen_luniferadoc_richstring_RichStringTableRow_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringTableRow)
gen_luniferadoc_richstring_RichStringViewRef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringViewRef)
gen_luniferadoc_richstring_RichStringUIRef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringUIRef)
gen_luniferadoc_richstring_RichStringDTORef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringDTORef)
gen_luniferadoc_richstring_RichStringProcessRef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringProcessRef)
gen_luniferadoc_richstring_RichStringTaskRef_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringTaskRef)
gen_luniferadoc_richstring_RichStringListElement_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringListElement)
gen_luniferadoc_richstring_RichStringSpan_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringSpan)
gen_luniferadoc_richstring_RichStringList_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringList)
gen_luniferadoc_richstring_RichStringOrderedList_RichStringMarkup = Generalization(general=RichStringMarkup, specific=luniferadoc_richstring_RichStringOrderedList)

# Domain Model
domain_model = DomainModel(
    name="luniferadoc",
    types={luniferadoc_NamedDocument, luniferadoc_DocumentInclude, LuniferaDocDocument, luniferadoc_document_EntityDescription, RichString, luniferadoc_document_EntityFields, EntityField, luniferadoc_document_EntityField, luniferadoc_document_LuniferaDocDocument, NamedDocument, luniferadoc_document_EntityDocument, EntityDescription, EntityFields, DTOProperties, luniferadoc_document_DTODescription, luniferadoc_document_DTOProperties, DTOProperty, luniferadoc_document_DTODocument, DTODescription, luniferadoc_document_BPMHumanTaskDocument, BPMHumanTaskDescription, luniferadoc_document_BPMHumanTaskDescription, luniferadoc_document_DTOProperty, luniferadoc_document_BPMProcessDocument, BPMProcessDescription, luniferadoc_document_BPMProcessDescription, UIDescription, luniferadoc_document_UIDescription, luniferadoc_document_GeneralDocument, LuniferaDocLayout, document_luniferadoc_DocumentInclude, luniferadoc_document_VaaclipseViewDocument, VaaclipseViewDescription, luniferadoc_document_VaaclipseViewDescription, luniferadoc_document_UIDocument, luniferadoc_document_BPMProcessLayout, luniferadoc_document_BPMHumanTaskLayout, luniferadoc_document_VaaclipseViewLayout, luniferadoc_document_UILayout, luniferadoc_richstring_RichStringElseIf, richstring_luniferadoc_XExpression, luniferadoc_document_LuniferaDocLayout, document_luniferadoc_XImportDeclaration, luniferadoc_document_EntityLayout, luniferadoc_document_DTOLayout, luniferadoc_richstring_RichStringIf, XExpression, luniferadoc_richstring_RichString, XBlockExpression, luniferadoc_richstring_RichStringLiteral, XStringLiteral, luniferadoc_richstring_RichStringForLoop, XForLoopExpression, luniferadoc_richstring_RichStringExample, RichStringMarkup, luniferadoc_richstring_RichStringH1, luniferadoc_richstring_RichStringH2, luniferadoc_richstring_RichStringH3, luniferadoc_richstring_RichStringH4, RichStringElseIf, luniferadoc_richstring_RichStringMarkup, luniferadoc_richstring_RichStringRef, luniferadoc_richstring_RichStringBold, luniferadoc_richstring_RichStringH5, luniferadoc_richstring_RichStringH6, luniferadoc_richstring_RichStringChapter, luniferadoc_richstring_RichStringSection, luniferadoc_richstring_RichStringSubsection, luniferadoc_richstring_RichStringURL, luniferadoc_richstring_RichStringMailto, luniferadoc_richstring_RichStringSkype, luniferadoc_richstring_RichStringUnderline, luniferadoc_richstring_RichStringItalic, luniferadoc_richstring_RichStringImg, luniferadoc_richstring_RichStringTable, RichStringTableRow, luniferadoc_richstring_RichStringMovie, luniferadoc_richstring_RichStringCode, luniferadoc_richstring_RichStringTableData, luniferadoc_richstring_RichStringOpenView, luniferadoc_richstring_RichStringStartProcess, luniferadoc_richstring_RichStringEntityRef, luniferadoc_richstring_RichStringTableRow, RichStringTableData, BPMHumanTaskDocument, luniferadoc_richstring_RichStringViewRef, VaaclipseViewDocument, luniferadoc_richstring_RichStringUIRef, UIDocument, EntityDocument, luniferadoc_richstring_RichStringDTORef, DTODocument, luniferadoc_richstring_RichStringProcessRef, BPMProcessDocument, luniferadoc_richstring_RichStringTaskRef, luniferadoc_richstring_RichStringListElement, luniferadoc_richstring_RichStringSpan, luniferadoc_richstring_RichStringList, RichStringListElement, luniferadoc_richstring_RichStringOrderedList, DocType},
    associations={include0, content4, fields5, description1, fields2, properties9, content11, properties13, description6, description8, content17, description19, description14, description16, description25, content26, content20, description22, content23, if_33, includes28, content29, imports31, after42, if_45, then47, then34, before37, separator39, elseIfs50, else_52, expression55, text57, content61, content63, content59, content67, rows69, content65, expressions70, columns73, expressions74, taskDoc80, viewDoc81, entityDoc77, dtoDoc78, processDoc79, elements87, expressions89, uiDoc82, elements83, expressions84},
    generalizations={gen_luniferadoc_document_LuniferaDocDocument_NamedDocument, gen_luniferadoc_document_EntityDocument_LuniferaDocDocument, gen_luniferadoc_document_DTODocument_LuniferaDocDocument, gen_luniferadoc_document_BPMHumanTaskDocument_LuniferaDocDocument, gen_luniferadoc_document_BPMProcessDocument_LuniferaDocDocument, gen_luniferadoc_document_GeneralDocument_LuniferaDocLayout, gen_luniferadoc_document_VaaclipseViewDocument_LuniferaDocDocument, gen_luniferadoc_document_UIDocument_LuniferaDocDocument, gen_luniferadoc_document_BPMProcessLayout_LuniferaDocLayout, gen_luniferadoc_document_BPMHumanTaskLayout_LuniferaDocLayout, gen_luniferadoc_document_VaaclipseViewLayout_LuniferaDocLayout, gen_luniferadoc_document_UILayout_LuniferaDocLayout, gen_luniferadoc_document_LuniferaDocLayout_NamedDocument, gen_luniferadoc_document_EntityLayout_LuniferaDocLayout, gen_luniferadoc_document_DTOLayout_LuniferaDocLayout, gen_luniferadoc_richstring_RichStringIf_XExpression, gen_luniferadoc_richstring_RichString_XBlockExpression, gen_luniferadoc_richstring_RichStringLiteral_XStringLiteral, gen_luniferadoc_richstring_RichStringForLoop_XForLoopExpression, gen_luniferadoc_richstring_RichStringExample_RichStringMarkup, gen_luniferadoc_richstring_RichStringH1_RichStringMarkup, gen_luniferadoc_richstring_RichStringH2_RichStringMarkup, gen_luniferadoc_richstring_RichStringH3_RichStringMarkup, gen_luniferadoc_richstring_RichStringH4_RichStringMarkup, gen_luniferadoc_richstring_RichStringMarkup_XExpression, gen_luniferadoc_richstring_RichStringURL_RichStringMarkup, gen_luniferadoc_richstring_RichStringRef_RichStringMarkup, gen_luniferadoc_richstring_RichStringBold_RichStringMarkup, gen_luniferadoc_richstring_RichStringH5_RichStringMarkup, gen_luniferadoc_richstring_RichStringH6_RichStringMarkup, gen_luniferadoc_richstring_RichStringChapter_RichStringMarkup, gen_luniferadoc_richstring_RichStringSection_RichStringMarkup, gen_luniferadoc_richstring_RichStringSubsection_RichStringMarkup, gen_luniferadoc_richstring_RichStringMailto_RichStringMarkup, gen_luniferadoc_richstring_RichStringSkype_RichStringMarkup, gen_luniferadoc_richstring_RichStringUnderline_RichStringMarkup, gen_luniferadoc_richstring_RichStringItalic_RichStringMarkup, gen_luniferadoc_richstring_RichStringImg_RichStringMarkup, gen_luniferadoc_richstring_RichStringTable_RichStringMarkup, gen_luniferadoc_richstring_RichStringMovie_RichStringMarkup, gen_luniferadoc_richstring_RichStringCode_RichStringMarkup, gen_luniferadoc_richstring_RichStringTableData_RichStringMarkup, gen_luniferadoc_richstring_RichStringOpenView_RichStringMarkup, gen_luniferadoc_richstring_RichStringStartProcess_RichStringMarkup, gen_luniferadoc_richstring_RichStringEntityRef_RichStringMarkup, gen_luniferadoc_richstring_RichStringTableRow_RichStringMarkup, gen_luniferadoc_richstring_RichStringViewRef_RichStringMarkup, gen_luniferadoc_richstring_RichStringUIRef_RichStringMarkup, gen_luniferadoc_richstring_RichStringDTORef_RichStringMarkup, gen_luniferadoc_richstring_RichStringProcessRef_RichStringMarkup, gen_luniferadoc_richstring_RichStringTaskRef_RichStringMarkup, gen_luniferadoc_richstring_RichStringListElement_RichStringMarkup, gen_luniferadoc_richstring_RichStringSpan_RichStringMarkup, gen_luniferadoc_richstring_RichStringList_RichStringMarkup, gen_luniferadoc_richstring_RichStringOrderedList_RichStringMarkup},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)