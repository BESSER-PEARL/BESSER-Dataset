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
TWEvol: Enumeration = Enumeration(
    name="TWEvol",
    literals={
            EnumerationLiteral(name="twFinal"),
			EnumerationLiteral(name="twTransient"),
			EnumerationLiteral(name="twMutable"),
			EnumerationLiteral(name="twImmutable")
    }
)

TWUpdateKind: Enumeration = Enumeration(
    name="TWUpdateKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="merge"),
			EnumerationLiteral(name="compute")
    }
)

TWCommitKind: Enumeration = Enumeration(
    name="TWCommitKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="conflict"),
			EnumerationLiteral(name="reconcile")
    }
)

PositionEnum: Enumeration = Enumeration(
    name="PositionEnum",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="defaultpos")
    }
)

TWDestEvol: Enumeration = Enumeration(
    name="TWDestEvol",
    literals={
            EnumerationLiteral(name="mutable"),
			EnumerationLiteral(name="immutable"),
			EnumerationLiteral(name="effective"),
			EnumerationLiteral(name="finalDest"),
			EnumerationLiteral(name="branch")
    }
)

# Classes
ccore_WCListener = Class(name="ccore::WCListener", is_abstract=True)
ccore_TypeDefinition = Class(name="ccore::TypeDefinition", is_abstract=True)
Item = Class(name="Item")
EClass = Class(name="EClass")
ccore_Attribute = Class(name="ccore::Attribute", is_abstract=True)
ccore_Field = Class(name="ccore::Field")
ccore_Page = Class(name="ccore::Page")
ccore_UIValidator = Class(name="ccore::UIValidator")
ccore_GroupOfAttributes = Class(name="ccore::GroupOfAttributes")
ccore_EClass = Class(name="ccore::EClass")
ccore_ExtentedType = Class(name="ccore::ExtentedType")
TypeDefinition = Class(name="TypeDefinition")
ccore_ItemType = Class(name="ccore::ItemType")
ccore_KeyDefinition = Class(name="ccore::KeyDefinition")
ccore_ContentItemType = Class(name="ccore::ContentItemType", is_abstract=True)
ccore_ExporterType = Class(name="ccore::ExporterType")
ccore_ComposerType = Class(name="ccore::ComposerType")
ccore_Cadse = Class(name="ccore::Cadse")
EPackage = Class(name="EPackage")
ccore_EPackage = Class(name="ccore::EPackage")
ccore_BindingDesc = Class(name="ccore::BindingDesc")
ccore_Item = Class(name="ccore::Item")
ENamedElement = Class(name="ENamedElement")
DBObject = Class(name="DBObject")
ccore_ContentItem = Class(name="ccore::ContentItem")
ccore_Exporter = Class(name="ccore::Exporter")
ccore_Composer = Class(name="ccore::Composer")
EAttribute = Class(name="EAttribute")
ccore_ViewLinkType = Class(name="ccore::ViewLinkType")
ccore_ViewDescription = Class(name="ccore::ViewDescription")
ccore_EStructuralFeature = Class(name="ccore::EStructuralFeature")
ItemType = Class(name="ItemType")
ccore_GenInformation = Class(name="ccore::GenInformation")
ccore_ViewItemType = Class(name="ccore::ViewItemType")
ccore_Display = Class(name="ccore::Display")
RuntimeItem = Class(name="RuntimeItem")
ccore_InteractionController = Class(name="ccore::InteractionController")
ccore_ModelController = Class(name="ccore::ModelController")
ccore_Enum = Class(name="ccore::Enum")
ccore_StringAttribute = Class(name="ccore::StringAttribute")
Attribute = Class(name="Attribute")
ccore_BooleanAttribute = Class(name="ccore::BooleanAttribute")
ccore_IntegerAttribute = Class(name="ccore::IntegerAttribute")
ccore_LongAttribute = Class(name="ccore::LongAttribute")
ccore_DateAttribute = Class(name="ccore::DateAttribute")
ccore_UUIDAttribute = Class(name="ccore::UUIDAttribute")
ccore_DoubleAttribute = Class(name="ccore::DoubleAttribute")
ccore_TimeAttribute = Class(name="ccore::TimeAttribute")
LongAttribute = Class(name="LongAttribute")
ccore_UnresolvedAttributeType = Class(name="ccore::UnresolvedAttributeType", is_abstract=True)
ccore_BindExt = Class(name="ccore::BindExt")
BindingDesc = Class(name="BindingDesc")
ccore_DynamicActions = Class(name="ccore::DynamicActions")
ccore_ActionExtItemType = Class(name="ccore::ActionExtItemType")
ccore_Menu = Class(name="ccore::Menu")
ccore_MenuAbstract = Class(name="ccore::MenuAbstract", is_abstract=True)
ccore_RuntimeItem = Class(name="ccore::RuntimeItem")
ccore_EnumType = Class(name="ccore::EnumType")
ccore_LinkType = Class(name="ccore::LinkType")
EReference = Class(name="EReference")
ccore_ExportedContent = Class(name="ccore::ExportedContent")
ccore_GroupExtItem = Class(name="ccore::GroupExtItem")
ccore_MenuAction = Class(name="ccore::MenuAction")
ccore_MenuGroup = Class(name="ccore::MenuGroup")
ccore_ComposerLink = Class(name="ccore::ComposerLink")
EEnum = Class(name="EEnum")
ccore_EEnum = Class(name="ccore::EEnum")
ccore_ComputedString = Class(name="ccore::ComputedString", is_abstract=True)
ccore_View = Class(name="ccore::View")
ccore_ExtItem = Class(name="ccore::ExtItem", is_abstract=True)
ccore_ViewModel = Class(name="ccore::ViewModel")
RuntimeItemType = Class(name="RuntimeItemType")
ccore_RuntimeItemType = Class(name="ccore::RuntimeItemType")
ccore_DBObject = Class(name="ccore::DBObject")

# ccore_WCListener class attributes and methods

# ccore_TypeDefinition class attributes and methods
ccore_TypeDefinition_idRuntime: Property = Property(name="idRuntime", type=StringType)
ccore_TypeDefinition.attributes={ccore_TypeDefinition_idRuntime}

# Item class attributes and methods

# EClass class attributes and methods

# ccore_Attribute class attributes and methods
ccore_Attribute_isList: Property = Property(name="isList", type=BooleanType)
ccore_Attribute_require: Property = Property(name="require", type=BooleanType)
ccore_Attribute_cannotBeUndefined: Property = Property(name="cannotBeUndefined", type=BooleanType)
ccore_Attribute_natif: Property = Property(name="natif", type=BooleanType)
ccore_Attribute__final: Property = Property(name="_final", type=BooleanType)
ccore_Attribute_mustBeInitialized: Property = Property(name="mustBeInitialized", type=BooleanType)
ccore_Attribute_tWRevSpecific: Property = Property(name="tWRevSpecific", type=BooleanType)
ccore_Attribute_tWEvol: Property = Property(name="tWEvol", type=StringType)
ccore_Attribute_tWUpdateKind: Property = Property(name="tWUpdateKind", type=StringType)
ccore_Attribute_tWCommitKind: Property = Property(name="tWCommitKind", type=StringType)
ccore_Attribute_devGenerated: Property = Property(name="devGenerated", type=BooleanType)
ccore_Attribute_idRuntime: Property = Property(name="idRuntime", type=StringType)
ccore_Attribute_hiddenInComputedPages: Property = Property(name="hiddenInComputedPages", type=BooleanType)
ccore_Attribute.attributes={ccore_Attribute_cannotBeUndefined, ccore_Attribute_tWEvol, ccore_Attribute__final, ccore_Attribute_tWUpdateKind, ccore_Attribute_devGenerated, ccore_Attribute_idRuntime, ccore_Attribute_mustBeInitialized, ccore_Attribute_require, ccore_Attribute_natif, ccore_Attribute_tWRevSpecific, ccore_Attribute_hiddenInComputedPages, ccore_Attribute_isList, ccore_Attribute_tWCommitKind}

# ccore_Field class attributes and methods
ccore_Field_label: Property = Property(name="label", type=StringType)
ccore_Field_position: Property = Property(name="position", type=StringType)
ccore_Field_editable: Property = Property(name="editable", type=BooleanType)
ccore_Field.attributes={ccore_Field_label, ccore_Field_editable, ccore_Field_position}

# ccore_Page class attributes and methods
ccore_Page_title: Property = Property(name="title", type=StringType)
ccore_Page_description: Property = Property(name="description", type=StringType)
ccore_Page_label: Property = Property(name="label", type=StringType)
ccore_Page_idRuntime: Property = Property(name="idRuntime", type=StringType)
ccore_Page.attributes={ccore_Page_description, ccore_Page_title, ccore_Page_idRuntime, ccore_Page_label}

# ccore_UIValidator class attributes and methods

# ccore_GroupOfAttributes class attributes and methods
ccore_GroupOfAttributes_column: Property = Property(name="column", type=IntegerType)
ccore_GroupOfAttributes.attributes={ccore_GroupOfAttributes_column}

# ccore_EClass class attributes and methods

# ccore_ExtentedType class attributes and methods

# TypeDefinition class attributes and methods

# ccore_ItemType class attributes and methods
ccore_ItemType_hasUniqueName: Property = Property(name="hasUniqueName", type=BooleanType)
ccore_ItemType_isMetaItemType: Property = Property(name="isMetaItemType", type=BooleanType)
ccore_ItemType_isInstanceHidden: Property = Property(name="isInstanceHidden", type=BooleanType)
ccore_ItemType_overwriteDefaultPages: Property = Property(name="overwriteDefaultPages", type=BooleanType)
ccore_ItemType_icon: Property = Property(name="icon", type=StringType)
ccore_ItemType_itemFactoryClass: Property = Property(name="itemFactoryClass", type=StringType)
ccore_ItemType_hasContent: Property = Property(name="hasContent", type=BooleanType)
ccore_ItemType_isRootElement: Property = Property(name="isRootElement", type=BooleanType)
ccore_ItemType_isInstanceAbstract: Property = Property(name="isInstanceAbstract", type=BooleanType)
ccore_ItemType_hasShortName: Property = Property(name="hasShortName", type=BooleanType)
ccore_ItemType_itemManagerClass: Property = Property(name="itemManagerClass", type=StringType)
ccore_ItemType_packageName: Property = Property(name="packageName", type=StringType)
ccore_ItemType_customManager: Property = Property(name="customManager", type=BooleanType)
ccore_ItemType_managerClass: Property = Property(name="managerClass", type=StringType)
ccore_ItemType_qualifiedNameTemplate: Property = Property(name="qualifiedNameTemplate", type=StringType)
ccore_ItemType_messageErrorId: Property = Property(name="messageErrorId", type=StringType)
ccore_ItemType_validateNameRe: Property = Property(name="validateNameRe", type=StringType)
ccore_ItemType_displayNameTemplate: Property = Property(name="displayNameTemplate", type=StringType)
ccore_ItemType_humanName: Property = Property(name="humanName", type=StringType)
ccore_ItemType.attributes={ccore_ItemType_isRootElement, ccore_ItemType_hasUniqueName, ccore_ItemType_isMetaItemType, ccore_ItemType_customManager, ccore_ItemType_validateNameRe, ccore_ItemType_packageName, ccore_ItemType_itemFactoryClass, ccore_ItemType_icon, ccore_ItemType_isInstanceHidden, ccore_ItemType_isInstanceAbstract, ccore_ItemType_displayNameTemplate, ccore_ItemType_messageErrorId, ccore_ItemType_managerClass, ccore_ItemType_overwriteDefaultPages, ccore_ItemType_hasShortName, ccore_ItemType_hasContent, ccore_ItemType_itemManagerClass, ccore_ItemType_humanName, ccore_ItemType_qualifiedNameTemplate}

# ccore_KeyDefinition class attributes and methods

# ccore_ContentItemType class attributes and methods
ccore_ContentItemType_extendsClass: Property = Property(name="extendsClass", type=BooleanType)
ccore_ContentItemType.attributes={ccore_ContentItemType_extendsClass}

# ccore_ExporterType class attributes and methods

# ccore_ComposerType class attributes and methods

# ccore_Cadse class attributes and methods
ccore_Cadse_itemRepoURL: Property = Property(name="itemRepoURL", type=StringType)
ccore_Cadse_idDefinition: Property = Property(name="idDefinition", type=StringType)
ccore_Cadse_description: Property = Property(name="description", type=StringType)
ccore_Cadse_defaultContentRepoURL: Property = Property(name="defaultContentRepoURL", type=StringType)
ccore_Cadse_executed: Property = Property(name="executed", type=BooleanType)
ccore_Cadse_itemRepoLogin: Property = Property(name="itemRepoLogin", type=StringType)
ccore_Cadse_itemRepoPasswd: Property = Property(name="itemRepoPasswd", type=StringType)
ccore_Cadse.attributes={ccore_Cadse_itemRepoURL, ccore_Cadse_description, ccore_Cadse_itemRepoPasswd, ccore_Cadse_executed, ccore_Cadse_itemRepoLogin, ccore_Cadse_defaultContentRepoURL, ccore_Cadse_idDefinition}

# EPackage class attributes and methods

# ccore_EPackage class attributes and methods

# ccore_BindingDesc class attributes and methods

# ccore_Item class attributes and methods
ccore_Item_committedBy: Property = Property(name="committedBy", type=StringType)
ccore_Item_displayName: Property = Property(name="displayName", type=StringType)
ccore_Item_itemHidden: Property = Property(name="itemHidden", type=BooleanType)
ccore_Item_itemReadonly: Property = Property(name="itemReadonly", type=BooleanType)
ccore_Item_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
ccore_Item_twRequireNewRev: Property = Property(name="twRequireNewRev", type=BooleanType)
ccore_Item_twVersion: Property = Property(name="twVersion", type=IntegerType)
ccore_Item_twRevModified: Property = Property(name="twRevModified", type=BooleanType)
ccore_Item_twCommittedDate: Property = Property(name="twCommittedDate", type=StringType)
ccore_Item_isvalid: Property = Property(name="isvalid", type=BooleanType)
ccore_Item.attributes={ccore_Item_twRevModified, ccore_Item_displayName, ccore_Item_qualifiedName, ccore_Item_twCommittedDate, ccore_Item_twRequireNewRev, ccore_Item_itemReadonly, ccore_Item_isvalid, ccore_Item_itemHidden, ccore_Item_committedBy, ccore_Item_twVersion}

# ENamedElement class attributes and methods

# DBObject class attributes and methods

# ccore_ContentItem class attributes and methods

# ccore_Exporter class attributes and methods
ccore_Exporter_types: Property = Property(name="types", type=StringType)
ccore_Exporter.attributes={ccore_Exporter_types}

# ccore_Composer class attributes and methods
ccore_Composer_types: Property = Property(name="types", type=StringType)
ccore_Composer.attributes={ccore_Composer_types}

# EAttribute class attributes and methods

# ccore_ViewLinkType class attributes and methods
ccore_ViewLinkType_canCreateItem: Property = Property(name="canCreateItem", type=BooleanType)
ccore_ViewLinkType_canCreateLink: Property = Property(name="canCreateLink", type=BooleanType)
ccore_ViewLinkType_displayCreate: Property = Property(name="displayCreate", type=StringType)
ccore_ViewLinkType_aggregation: Property = Property(name="aggregation", type=BooleanType)
ccore_ViewLinkType.attributes={ccore_ViewLinkType_aggregation, ccore_ViewLinkType_canCreateItem, ccore_ViewLinkType_canCreateLink, ccore_ViewLinkType_displayCreate}

# ccore_ViewDescription class attributes and methods

# ccore_EStructuralFeature class attributes and methods

# ItemType class attributes and methods

# ccore_GenInformation class attributes and methods
ccore_GenInformation_cSTName: Property = Property(name="cSTName", type=StringType)
ccore_GenInformation.attributes={ccore_GenInformation_cSTName}

# ccore_ViewItemType class attributes and methods
ccore_ViewItemType_ref: Property = Property(name="ref", type=BooleanType)
ccore_ViewItemType_isRootElement: Property = Property(name="isRootElement", type=BooleanType)
ccore_ViewItemType.attributes={ccore_ViewItemType_isRootElement, ccore_ViewItemType_ref}

# ccore_Display class attributes and methods
ccore_Display_extendsIC: Property = Property(name="extendsIC", type=BooleanType)
ccore_Display_extendsMC: Property = Property(name="extendsMC", type=BooleanType)
ccore_Display_extendsUI: Property = Property(name="extendsUI", type=BooleanType)
ccore_Display.attributes={ccore_Display_extendsIC, ccore_Display_extendsMC, ccore_Display_extendsUI}

# RuntimeItem class attributes and methods

# ccore_InteractionController class attributes and methods

# ccore_ModelController class attributes and methods

# ccore_Enum class attributes and methods
ccore_Enum_enumClazz: Property = Property(name="enumClazz", type=StringType)
ccore_Enum_values: Property = Property(name="values", type=StringType)
ccore_Enum.attributes={ccore_Enum_enumClazz, ccore_Enum_values}

# ccore_StringAttribute class attributes and methods
ccore_StringAttribute_notEmpty: Property = Property(name="notEmpty", type=BooleanType)
ccore_StringAttribute.attributes={ccore_StringAttribute_notEmpty}

# Attribute class attributes and methods

# ccore_BooleanAttribute class attributes and methods

# ccore_IntegerAttribute class attributes and methods

# ccore_LongAttribute class attributes and methods

# ccore_DateAttribute class attributes and methods

# ccore_UUIDAttribute class attributes and methods

# ccore_DoubleAttribute class attributes and methods

# ccore_TimeAttribute class attributes and methods
ccore_TimeAttribute_initWithTheCurrentTime: Property = Property(name="initWithTheCurrentTime", type=BooleanType)
ccore_TimeAttribute.attributes={ccore_TimeAttribute_initWithTheCurrentTime}

# LongAttribute class attributes and methods

# ccore_UnresolvedAttributeType class attributes and methods

# ccore_BindExt class attributes and methods

# BindingDesc class attributes and methods

# ccore_DynamicActions class attributes and methods

# ccore_ActionExtItemType class attributes and methods

# ccore_Menu class attributes and methods

# ccore_MenuAbstract class attributes and methods
ccore_MenuAbstract_label: Property = Property(name="label", type=StringType)
ccore_MenuAbstract_icon: Property = Property(name="icon", type=StringType)
ccore_MenuAbstract_path: Property = Property(name="path", type=StringType)
ccore_MenuAbstract.attributes={ccore_MenuAbstract_path, ccore_MenuAbstract_icon, ccore_MenuAbstract_label}

# ccore_RuntimeItem class attributes and methods
ccore_RuntimeItem_className: Property = Property(name="className", type=StringType)
ccore_RuntimeItem_extendsClass: Property = Property(name="extendsClass", type=BooleanType)
ccore_RuntimeItem.attributes={ccore_RuntimeItem_extendsClass, ccore_RuntimeItem_className}

# ccore_EnumType class attributes and methods
ccore_EnumType_mustBeGenerated: Property = Property(name="mustBeGenerated", type=BooleanType)
ccore_EnumType_javaClass: Property = Property(name="javaClass", type=StringType)
ccore_EnumType_values: Property = Property(name="values", type=StringType)
ccore_EnumType.attributes={ccore_EnumType_values, ccore_EnumType_javaClass, ccore_EnumType_mustBeGenerated}

# ccore_LinkType class attributes and methods
ccore_LinkType_annotation: Property = Property(name="annotation", type=BooleanType)
ccore_LinkType_aggregation: Property = Property(name="aggregation", type=BooleanType)
ccore_LinkType_composition: Property = Property(name="composition", type=BooleanType)
ccore_LinkType_selection: Property = Property(name="selection", type=StringType)
ccore_LinkType_mapping: Property = Property(name="mapping", type=BooleanType)
ccore_LinkType_linkManager: Property = Property(name="linkManager", type=StringType)
ccore_LinkType_twDestEvol: Property = Property(name="twDestEvol", type=StringType)
ccore_LinkType_twCoupled: Property = Property(name="twCoupled", type=BooleanType)
ccore_LinkType_hidden: Property = Property(name="hidden", type=BooleanType)
ccore_LinkType_min: Property = Property(name="min", type=IntegerType)
ccore_LinkType_max: Property = Property(name="max", type=IntegerType)
ccore_LinkType_kind: Property = Property(name="kind", type=IntegerType)
ccore_LinkType_group: Property = Property(name="group", type=BooleanType)
ccore_LinkType.attributes={ccore_LinkType_group, ccore_LinkType_mapping, ccore_LinkType_max, ccore_LinkType_twDestEvol, ccore_LinkType_linkManager, ccore_LinkType_min, ccore_LinkType_kind, ccore_LinkType_aggregation, ccore_LinkType_selection, ccore_LinkType_hidden, ccore_LinkType_annotation, ccore_LinkType_composition, ccore_LinkType_twCoupled}

# EReference class attributes and methods

# ccore_ExportedContent class attributes and methods
ccore_ExportedContent_m_hasChildren: Method = Method(name="hasChildren", parameters={}, type=BooleanType)
ccore_ExportedContent.methods={ccore_ExportedContent_m_hasChildren}

# ccore_GroupExtItem class attributes and methods

# ccore_MenuAction class attributes and methods

# ccore_MenuGroup class attributes and methods

# ccore_ComposerLink class attributes and methods

# EEnum class attributes and methods

# ccore_EEnum class attributes and methods

# ccore_ComputedString class attributes and methods
ccore_ComputedString_expression: Property = Property(name="expression", type=StringType)
ccore_ComputedString.attributes={ccore_ComputedString_expression}

# ccore_View class attributes and methods
ccore_View_icon: Property = Property(name="icon", type=StringType)
ccore_View.attributes={ccore_View_icon}

# ccore_ExtItem class attributes and methods

# ccore_ViewModel class attributes and methods

# RuntimeItemType class attributes and methods

# ccore_RuntimeItemType class attributes and methods

# ccore_DBObject class attributes and methods
ccore_DBObject_uuid_lsb: Property = Property(name="uuid_lsb", type=StringType)
ccore_DBObject_objectId: Property = Property(name="objectId", type=IntegerType)
ccore_DBObject_uuid_msb: Property = Property(name="uuid_msb", type=StringType)
ccore_DBObject.attributes={ccore_DBObject_uuid_lsb, ccore_DBObject_uuid_msb, ccore_DBObject_objectId}

# Relationships
wcListeners18: BinaryAssociation = BinaryAssociation(
    name="wcListeners18",
    ends={
        Property(name="ccore_WCListener", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType19", type=ccore_WCListener, multiplicity=Multiplicity(0, 9999))
    }
)
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="ccore_Attribute", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition", type=ccore_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields1: BinaryAssociation = BinaryAssociation(
    name="fields1",
    ends={
        Property(name="ccore_Field", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition2", type=ccore_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creationPages3: BinaryAssociation = BinaryAssociation(
    name="creationPages3",
    ends={
        Property(name="ccore_Page", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition4", type=ccore_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validators5: BinaryAssociation = BinaryAssociation(
    name="validators5",
    ends={
        Property(name="ccore_UIValidator", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition6", type=ccore_UIValidator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modificationPages7: BinaryAssociation = BinaryAssociation(
    name="modificationPages7",
    ends={
        Property(name="ccore_Page9", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition8", type=ccore_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goupsOfAttributes10: BinaryAssociation = BinaryAssociation(
    name="goupsOfAttributes10",
    ends={
        Property(name="ccore_GroupOfAttributes", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition11", type=ccore_GroupOfAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refEClass12: BinaryAssociation = BinaryAssociation(
    name="refEClass12",
    ends={
        Property(name="ccore_EClass", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_TypeDefinition13", type=ccore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
exendsItemTypes14: BinaryAssociation = BinaryAssociation(
    name="exendsItemTypes14",
    ends={
        Property(name="ccore_ItemType", type=ccore_ExtentedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ExtentedType", type=ccore_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
superType16: BinaryAssociation = BinaryAssociation(
    name="superType16",
    ends={
        Property(name="ccore_ItemType17", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType15", type=ccore_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
itemTypes39: BinaryAssociation = BinaryAssociation(
    name="itemTypes39",
    ends={
        Property(name="ccore_ItemType41", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse40", type=ccore_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
keys42: BinaryAssociation = BinaryAssociation(
    name="keys42",
    ends={
        Property(name="ccore_KeyDefinition44", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse43", type=ccore_KeyDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subTypes21: BinaryAssociation = BinaryAssociation(
    name="subTypes21",
    ends={
        Property(name="ccore_ItemType22", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType20", type=ccore_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
extendedBy23: BinaryAssociation = BinaryAssociation(
    name="extendedBy23",
    ends={
        Property(name="ccore_ExtentedType25", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType24", type=ccore_ExtentedType, multiplicity=Multiplicity(0, 9999))
    }
)
keyDefinition26: BinaryAssociation = BinaryAssociation(
    name="keyDefinition26",
    ends={
        Property(name="ccore_KeyDefinition", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType27", type=ccore_KeyDefinition, multiplicity=Multiplicity(0, 1))
    }
)
contentModel28: BinaryAssociation = BinaryAssociation(
    name="contentModel28",
    ends={
        Property(name="ccore_ContentItemType", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType29", type=ccore_ContentItemType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exporterTypes30: BinaryAssociation = BinaryAssociation(
    name="exporterTypes30",
    ends={
        Property(name="ccore_ExporterType", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType31", type=ccore_ExporterType, multiplicity=Multiplicity(0, 9999))
    }
)
composerTypes32: BinaryAssociation = BinaryAssociation(
    name="composerTypes32",
    ends={
        Property(name="ccore_ComposerType", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType33", type=ccore_ComposerType, multiplicity=Multiplicity(0, 9999))
    }
)
contentItemTypes34: BinaryAssociation = BinaryAssociation(
    name="contentItemTypes34",
    ends={
        Property(name="ccore_ContentItemType36", type=ccore_ItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ItemType35", type=ccore_ContentItemType, multiplicity=Multiplicity(0, 9999))
    }
)
extendsCadse38: BinaryAssociation = BinaryAssociation(
    name="extendsCadse38",
    ends={
        Property(name="ccore_Cadse", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse37", type=ccore_Cadse, multiplicity=Multiplicity(0, 9999))
    }
)
parent58: BinaryAssociation = BinaryAssociation(
    name="parent58",
    ends={
        Property(name="ccore_Item59", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Item57", type=ccore_Item, multiplicity=Multiplicity(0, 1))
    }
)
modifiedAttributes60: BinaryAssociation = BinaryAssociation(
    name="modifiedAttributes60",
    ends={
        Property(name="ccore_Attribute62", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Item61", type=ccore_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
extendedTypes45: BinaryAssociation = BinaryAssociation(
    name="extendedTypes45",
    ends={
        Property(name="ccore_ExtentedType47", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse46", type=ccore_ExtentedType, multiplicity=Multiplicity(0, 9999))
    }
)
refEPackage48: BinaryAssociation = BinaryAssociation(
    name="refEPackage48",
    ends={
        Property(name="ccore_EPackage", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse49", type=ccore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
binding50: BinaryAssociation = BinaryAssociation(
    name="binding50",
    ends={
        Property(name="ccore_BindingDesc", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse51", type=ccore_BindingDesc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemContents52: BinaryAssociation = BinaryAssociation(
    name="itemContents52",
    ends={
        Property(name="ccore_Item", type=ccore_Cadse, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Cadse53", type=ccore_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instanceOf54: BinaryAssociation = BinaryAssociation(
    name="instanceOf54",
    ends={
        Property(name="ccore_ItemType56", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Item55", type=ccore_ItemType, multiplicity=Multiplicity(1, 9999))
    }
)
contents63: BinaryAssociation = BinaryAssociation(
    name="contents63",
    ends={
        Property(name="ContentItem", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerItem", type=ccore_ContentItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cadse64: BinaryAssociation = BinaryAssociation(
    name="cadse64",
    ends={
        Property(name="ccore_Cadse66", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Item65", type=ccore_Cadse, multiplicity=Multiplicity(1, 1))
    }
)
exporters67: BinaryAssociation = BinaryAssociation(
    name="exporters67",
    ends={
        Property(name="Exporter", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerItem68", type=ccore_Exporter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composers69: BinaryAssociation = BinaryAssociation(
    name="composers69",
    ends={
        Property(name="Composer", type=ccore_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerItem70", type=ccore_Composer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemType79: BinaryAssociation = BinaryAssociation(
    name="itemType79",
    ends={
        Property(name="ccore_ItemType80", type=ccore_ViewItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ViewItemType", type=ccore_ItemType, multiplicity=Multiplicity(1, 1))
    }
)
viewLinkTypes81: BinaryAssociation = BinaryAssociation(
    name="viewLinkTypes81",
    ends={
        Property(name="ccore_ViewLinkType", type=ccore_ViewItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ViewItemType82", type=ccore_ViewLinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootTypes83: BinaryAssociation = BinaryAssociation(
    name="rootTypes83",
    ends={
        Property(name="ccore_TypeDefinition84", type=ccore_ViewDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ViewDescription", type=ccore_TypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
wcListens71: BinaryAssociation = BinaryAssociation(
    name="wcListens71",
    ends={
        Property(name="ccore_WCListener73", type=ccore_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Attribute72", type=ccore_WCListener, multiplicity=Multiplicity(0, 9999))
    }
)
keys74: BinaryAssociation = BinaryAssociation(
    name="keys74",
    ends={
        Property(name="ccore_EStructuralFeature", type=ccore_KeyDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_KeyDefinition75", type=ccore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
parentKey77: BinaryAssociation = BinaryAssociation(
    name="parentKey77",
    ends={
        Property(name="ccore_KeyDefinition78", type=ccore_KeyDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_KeyDefinition76", type=ccore_KeyDefinition, multiplicity=Multiplicity(0, 1))
    }
)
overwrite94: BinaryAssociation = BinaryAssociation(
    name="overwrite94",
    ends={
        Property(name="ccore_UIValidator95", type=ccore_UIValidator, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_UIValidator93", type=ccore_UIValidator, multiplicity=Multiplicity(0, 9999))
    }
)
listenAttributes96: BinaryAssociation = BinaryAssociation(
    name="listenAttributes96",
    ends={
        Property(name="ccore_Attribute98", type=ccore_UIValidator, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_UIValidator97", type=ccore_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
refItemType85: BinaryAssociation = BinaryAssociation(
    name="refItemType85",
    ends={
        Property(name="ccore_ItemType86", type=ccore_BindExt, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_BindExt", type=ccore_ItemType, multiplicity=Multiplicity(1, 1))
    }
)
refExt87: BinaryAssociation = BinaryAssociation(
    name="refExt87",
    ends={
        Property(name="ccore_ExtentedType89", type=ccore_BindExt, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_BindExt88", type=ccore_ExtentedType, multiplicity=Multiplicity(1, 1))
    }
)
actionsModel90: BinaryAssociation = BinaryAssociation(
    name="actionsModel90",
    ends={
        Property(name="ccore_Menu", type=ccore_ActionExtItemType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ActionExtItemType", type=ccore_Menu, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children91: BinaryAssociation = BinaryAssociation(
    name="children91",
    ends={
        Property(name="ccore_MenuAbstract", type=ccore_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Menu92", type=ccore_MenuAbstract, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute111: BinaryAssociation = BinaryAssociation(
    name="attribute111",
    ends={
        Property(name="ccore_Attribute113", type=ccore_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Field112", type=ccore_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
ic114: BinaryAssociation = BinaryAssociation(
    name="ic114",
    ends={
        Property(name="ccore_InteractionController", type=ccore_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Field115", type=ccore_InteractionController, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mc116: BinaryAssociation = BinaryAssociation(
    name="mc116",
    ends={
        Property(name="ccore_ModelController", type=ccore_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Field117", type=ccore_ModelController, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ui118: BinaryAssociation = BinaryAssociation(
    name="ui118",
    ends={
        Property(name="ccore_Display", type=ccore_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Field119", type=ccore_Display, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumType99: BinaryAssociation = BinaryAssociation(
    name="enumType99",
    ends={
        Property(name="ccore_EnumType", type=ccore_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Enum", type=ccore_EnumType, multiplicity=Multiplicity(0, 1))
    }
)
destination100: BinaryAssociation = BinaryAssociation(
    name="destination100",
    ends={
        Property(name="ccore_TypeDefinition101", type=ccore_LinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_LinkType", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
source102: BinaryAssociation = BinaryAssociation(
    name="source102",
    ends={
        Property(name="ccore_TypeDefinition104", type=ccore_LinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_LinkType103", type=ccore_TypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
listenItemTypes105: BinaryAssociation = BinaryAssociation(
    name="listenItemTypes105",
    ends={
        Property(name="ccore_ItemType107", type=ccore_WCListener, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_WCListener106", type=ccore_ItemType, multiplicity=Multiplicity(0, 9999))
    }
)
listenAttributeDefinitions108: BinaryAssociation = BinaryAssociation(
    name="listenAttributeDefinitions108",
    ends={
        Property(name="ccore_Attribute110", type=ccore_WCListener, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_WCListener109", type=ccore_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
members137: BinaryAssociation = BinaryAssociation(
    name="members137",
    ends={
        Property(name="ccore_Item138", type=ccore_GroupExtItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_GroupExtItem", type=ccore_Item, multiplicity=Multiplicity(0, 9999))
    }
)
memberOf139: BinaryAssociation = BinaryAssociation(
    name="memberOf139",
    ends={
        Property(name="ccore_Item141", type=ccore_GroupExtItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_GroupExtItem140", type=ccore_Item, multiplicity=Multiplicity(0, 1))
    }
)
composerLinks142: BinaryAssociation = BinaryAssociation(
    name="composerLinks142",
    ends={
        Property(name="ccore_LinkType143", type=ccore_Composer, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Composer", type=ccore_LinkType, multiplicity=Multiplicity(0, 9999))
    }
)
links144: BinaryAssociation = BinaryAssociation(
    name="links144",
    ends={
        Property(name="ccore_ComposerLink", type=ccore_Composer, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Composer145", type=ccore_ComposerLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes120: BinaryAssociation = BinaryAssociation(
    name="attributes120",
    ends={
        Property(name="ccore_Attribute122", type=ccore_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Page121", type=ccore_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overwrite124: BinaryAssociation = BinaryAssociation(
    name="overwrite124",
    ends={
        Property(name="ccore_Page125", type=ccore_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_Page123", type=ccore_Page, multiplicity=Multiplicity(0, 9999))
    }
)
refEnum126: BinaryAssociation = BinaryAssociation(
    name="refEnum126",
    ends={
        Property(name="ccore_EEnum", type=ccore_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_EnumType127", type=ccore_EEnum, multiplicity=Multiplicity(1, 1))
    }
)
attributes128: BinaryAssociation = BinaryAssociation(
    name="attributes128",
    ends={
        Property(name="ccore_Attribute130", type=ccore_GroupOfAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_GroupOfAttributes129", type=ccore_Attribute, multiplicity=Multiplicity(1, 9999))
    }
)
superGroup132: BinaryAssociation = BinaryAssociation(
    name="superGroup132",
    ends={
        Property(name="ccore_GroupOfAttributes133", type=ccore_GroupOfAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_GroupOfAttributes131", type=ccore_GroupOfAttributes, multiplicity=Multiplicity(0, 1))
    }
)
linkType134: BinaryAssociation = BinaryAssociation(
    name="linkType134",
    ends={
        Property(name="ccore_LinkType136", type=ccore_ViewLinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ViewLinkType135", type=ccore_LinkType, multiplicity=Multiplicity(1, 1))
    }
)
ownerItem146: BinaryAssociation = BinaryAssociation(
    name="ownerItem146",
    ends={
        Property(name="Item", type=ccore_Composer, multiplicity=Multiplicity(1, 1)),
        Property(name="composers", type=ccore_Item, multiplicity=Multiplicity(0, 1))
    }
)
ownerItem147: BinaryAssociation = BinaryAssociation(
    name="ownerItem147",
    ends={
        Property(name="Item148", type=ccore_Exporter, multiplicity=Multiplicity(1, 1)),
        Property(name="exporters", type=ccore_Item, multiplicity=Multiplicity(1, 1))
    }
)
ownerItem149: BinaryAssociation = BinaryAssociation(
    name="ownerItem149",
    ends={
        Property(name="Item150", type=ccore_ContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=ccore_Item, multiplicity=Multiplicity(0, 1))
    }
)
children152: BinaryAssociation = BinaryAssociation(
    name="children152",
    ends={
        Property(name="ccore_ContentItem", type=ccore_ContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ContentItem151", type=ccore_ContentItem, multiplicity=Multiplicity(0, 9999))
    }
)
exporters153: BinaryAssociation = BinaryAssociation(
    name="exporters153",
    ends={
        Property(name="ccore_Exporter", type=ccore_ComposerLink, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ComposerLink154", type=ccore_Exporter, multiplicity=Multiplicity(0, 9999))
    }
)
link155: BinaryAssociation = BinaryAssociation(
    name="link155",
    ends={
        Property(name="ccore_LinkType157", type=ccore_ComposerLink, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ComposerLink156", type=ccore_LinkType, multiplicity=Multiplicity(1, 1))
    }
)
viewItemTypes158: BinaryAssociation = BinaryAssociation(
    name="viewItemTypes158",
    ends={
        Property(name="ccore_ViewItemType159", type=ccore_View, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_View", type=ccore_ViewItemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views160: BinaryAssociation = BinaryAssociation(
    name="views160",
    ends={
        Property(name="ccore_View161", type=ccore_ViewModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_ViewModel", type=ccore_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source162: BinaryAssociation = BinaryAssociation(
    name="source162",
    ends={
        Property(name="ccore_Item164", type=ccore_BindingDesc, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_BindingDesc163", type=ccore_Item, multiplicity=Multiplicity(1, 1))
    }
)
dest165: BinaryAssociation = BinaryAssociation(
    name="dest165",
    ends={
        Property(name="ccore_Item167", type=ccore_BindingDesc, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_BindingDesc166", type=ccore_Item, multiplicity=Multiplicity(1, 1))
    }
)
typeBinding168: BinaryAssociation = BinaryAssociation(
    name="typeBinding168",
    ends={
        Property(name="ccore_LinkType170", type=ccore_BindingDesc, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_BindingDesc169", type=ccore_LinkType, multiplicity=Multiplicity(1, 1))
    }
)
mainItemType171: BinaryAssociation = BinaryAssociation(
    name="mainItemType171",
    ends={
        Property(name="ccore_ItemType172", type=ccore_DBObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ccore_DBObject", type=ccore_ItemType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ccore_TypeDefinition_Item = Generalization(general=Item, specific=ccore_TypeDefinition)
gen_ccore_TypeDefinition_EClass = Generalization(general=EClass, specific=ccore_TypeDefinition)
gen_ccore_ExtentedType_TypeDefinition = Generalization(general=TypeDefinition, specific=ccore_ExtentedType)
gen_ccore_ItemType_TypeDefinition = Generalization(general=TypeDefinition, specific=ccore_ItemType)
gen_ccore_Cadse_Item = Generalization(general=Item, specific=ccore_Cadse)
gen_ccore_Cadse_EPackage = Generalization(general=EPackage, specific=ccore_Cadse)
gen_ccore_Item_ENamedElement = Generalization(general=ENamedElement, specific=ccore_Item)
gen_ccore_Item_DBObject = Generalization(general=DBObject, specific=ccore_Item)
gen_ccore_Attribute_Item = Generalization(general=Item, specific=ccore_Attribute)
gen_ccore_Attribute_EAttribute = Generalization(general=EAttribute, specific=ccore_Attribute)
gen_ccore_KeyDefinition_Item = Generalization(general=Item, specific=ccore_KeyDefinition)
gen_ccore_ContentItemType_ItemType = Generalization(general=ItemType, specific=ccore_ContentItemType)
gen_ccore_Display_RuntimeItem = Generalization(general=RuntimeItem, specific=ccore_Display)
gen_ccore_InteractionController_RuntimeItem = Generalization(general=RuntimeItem, specific=ccore_InteractionController)
gen_ccore_ModelController_RuntimeItem = Generalization(general=RuntimeItem, specific=ccore_ModelController)
gen_ccore_Enum_Attribute = Generalization(general=Attribute, specific=ccore_Enum)
gen_ccore_StringAttribute_Attribute = Generalization(general=Attribute, specific=ccore_StringAttribute)
gen_ccore_BooleanAttribute_Attribute = Generalization(general=Attribute, specific=ccore_BooleanAttribute)
gen_ccore_IntegerAttribute_Attribute = Generalization(general=Attribute, specific=ccore_IntegerAttribute)
gen_ccore_LongAttribute_Attribute = Generalization(general=Attribute, specific=ccore_LongAttribute)
gen_ccore_DateAttribute_Attribute = Generalization(general=Attribute, specific=ccore_DateAttribute)
gen_ccore_UUIDAttribute_Attribute = Generalization(general=Attribute, specific=ccore_UUIDAttribute)
gen_ccore_DoubleAttribute_Attribute = Generalization(general=Attribute, specific=ccore_DoubleAttribute)
gen_ccore_TimeAttribute_LongAttribute = Generalization(general=LongAttribute, specific=ccore_TimeAttribute)
gen_ccore_BindExt_BindingDesc = Generalization(general=BindingDesc, specific=ccore_BindExt)
gen_ccore_RuntimeItem_Item = Generalization(general=Item, specific=ccore_RuntimeItem)
gen_ccore_Field_Item = Generalization(general=Item, specific=ccore_Field)
gen_ccore_LinkType_EReference = Generalization(general=EReference, specific=ccore_LinkType)
gen_ccore_LinkType_Attribute = Generalization(general=Attribute, specific=ccore_LinkType)
gen_ccore_Composer_RuntimeItem = Generalization(general=RuntimeItem, specific=ccore_Composer)
gen_ccore_EnumType_EEnum = Generalization(general=EEnum, specific=ccore_EnumType)
gen_ccore_Exporter_RuntimeItem = Generalization(general=RuntimeItem, specific=ccore_Exporter)
gen_ccore_ComposerType_RuntimeItemType = Generalization(general=RuntimeItemType, specific=ccore_ComposerType)
gen_ccore_ExporterType_RuntimeItemType = Generalization(general=RuntimeItemType, specific=ccore_ExporterType)
gen_ccore_RuntimeItemType_ItemType = Generalization(general=ItemType, specific=ccore_RuntimeItemType)
gen_ccore_BindingDesc_DBObject = Generalization(general=DBObject, specific=ccore_BindingDesc)

# Domain Model
domain_model = DomainModel(
    name="ccore",
    types={ccore_WCListener, ccore_TypeDefinition, Item, EClass, ccore_Attribute, ccore_Field, ccore_Page, ccore_UIValidator, ccore_GroupOfAttributes, ccore_EClass, ccore_ExtentedType, TypeDefinition, ccore_ItemType, ccore_KeyDefinition, ccore_ContentItemType, ccore_ExporterType, ccore_ComposerType, ccore_Cadse, EPackage, ccore_EPackage, ccore_BindingDesc, ccore_Item, ENamedElement, DBObject, ccore_ContentItem, ccore_Exporter, ccore_Composer, EAttribute, ccore_ViewLinkType, ccore_ViewDescription, ccore_EStructuralFeature, ItemType, ccore_GenInformation, ccore_ViewItemType, ccore_Display, RuntimeItem, ccore_InteractionController, ccore_ModelController, ccore_Enum, ccore_StringAttribute, Attribute, ccore_BooleanAttribute, ccore_IntegerAttribute, ccore_LongAttribute, ccore_DateAttribute, ccore_UUIDAttribute, ccore_DoubleAttribute, ccore_TimeAttribute, LongAttribute, ccore_UnresolvedAttributeType, ccore_BindExt, BindingDesc, ccore_DynamicActions, ccore_ActionExtItemType, ccore_Menu, ccore_MenuAbstract, ccore_RuntimeItem, ccore_EnumType, ccore_LinkType, EReference, ccore_ExportedContent, ccore_GroupExtItem, ccore_MenuAction, ccore_MenuGroup, ccore_ComposerLink, EEnum, ccore_EEnum, ccore_ComputedString, ccore_View, ccore_ExtItem, ccore_ViewModel, RuntimeItemType, ccore_RuntimeItemType, ccore_DBObject, TWEvol, TWUpdateKind, TWCommitKind, PositionEnum, TWDestEvol},
    associations={wcListeners18, attributes0, fields1, creationPages3, validators5, modificationPages7, goupsOfAttributes10, refEClass12, exendsItemTypes14, superType16, itemTypes39, keys42, subTypes21, extendedBy23, keyDefinition26, contentModel28, exporterTypes30, composerTypes32, contentItemTypes34, extendsCadse38, parent58, modifiedAttributes60, extendedTypes45, refEPackage48, binding50, itemContents52, instanceOf54, contents63, cadse64, exporters67, composers69, itemType79, viewLinkTypes81, rootTypes83, wcListens71, keys74, parentKey77, overwrite94, listenAttributes96, refItemType85, refExt87, actionsModel90, children91, attribute111, ic114, mc116, ui118, enumType99, destination100, source102, listenItemTypes105, listenAttributeDefinitions108, members137, memberOf139, composerLinks142, links144, attributes120, overwrite124, refEnum126, attributes128, superGroup132, linkType134, ownerItem146, ownerItem147, ownerItem149, children152, exporters153, link155, viewItemTypes158, views160, source162, dest165, typeBinding168, mainItemType171},
    generalizations={gen_ccore_TypeDefinition_Item, gen_ccore_TypeDefinition_EClass, gen_ccore_ExtentedType_TypeDefinition, gen_ccore_ItemType_TypeDefinition, gen_ccore_Cadse_Item, gen_ccore_Cadse_EPackage, gen_ccore_Item_ENamedElement, gen_ccore_Item_DBObject, gen_ccore_Attribute_Item, gen_ccore_Attribute_EAttribute, gen_ccore_KeyDefinition_Item, gen_ccore_ContentItemType_ItemType, gen_ccore_Display_RuntimeItem, gen_ccore_InteractionController_RuntimeItem, gen_ccore_ModelController_RuntimeItem, gen_ccore_Enum_Attribute, gen_ccore_StringAttribute_Attribute, gen_ccore_BooleanAttribute_Attribute, gen_ccore_IntegerAttribute_Attribute, gen_ccore_LongAttribute_Attribute, gen_ccore_DateAttribute_Attribute, gen_ccore_UUIDAttribute_Attribute, gen_ccore_DoubleAttribute_Attribute, gen_ccore_TimeAttribute_LongAttribute, gen_ccore_BindExt_BindingDesc, gen_ccore_RuntimeItem_Item, gen_ccore_Field_Item, gen_ccore_LinkType_EReference, gen_ccore_LinkType_Attribute, gen_ccore_Composer_RuntimeItem, gen_ccore_EnumType_EEnum, gen_ccore_Exporter_RuntimeItem, gen_ccore_ComposerType_RuntimeItemType, gen_ccore_ExporterType_RuntimeItemType, gen_ccore_RuntimeItemType_ItemType, gen_ccore_BindingDesc_DBObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)