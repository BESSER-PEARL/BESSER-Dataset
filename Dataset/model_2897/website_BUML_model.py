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
DatabaseTechnologies: Enumeration = Enumeration(
    name="DatabaseTechnologies",
    literals={
            EnumerationLiteral(name="MySql"),
			EnumerationLiteral(name="Oracle")
    }
)

OrmTechnologies: Enumeration = Enumeration(
    name="OrmTechnologies",
    literals={
            EnumerationLiteral(name="JPA"),
			EnumerationLiteral(name="DataMapper"),
			EnumerationLiteral(name="Idiorm"),
			EnumerationLiteral(name="Kohana"),
			EnumerationLiteral(name="DoctrineORM"),
			EnumerationLiteral(name="DoctrineODM")
    }
)

FrameworkTechnologies: Enumeration = Enumeration(
    name="FrameworkTechnologies",
    literals={
            EnumerationLiteral(name="JSF"),
			EnumerationLiteral(name="CakePHP"),
			EnumerationLiteral(name="CodeIgniter"),
			EnumerationLiteral(name="Kohana"),
			EnumerationLiteral(name="Laravel"),
			EnumerationLiteral(name="Symfony")
    }
)

InputTechnologies: Enumeration = Enumeration(
    name="InputTechnologies",
    literals={
            EnumerationLiteral(name="Html"),
			EnumerationLiteral(name="jQueryUI")
    }
)

AjaxTechnologies: Enumeration = Enumeration(
    name="AjaxTechnologies",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="jQuery"),
			EnumerationLiteral(name="AngularJS")
    }
)

AuthenticationKeyTypes: Enumeration = Enumeration(
    name="AuthenticationKeyTypes",
    literals={
            EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="ScreenName"),
			EnumerationLiteral(name="Username")
    }
)

Cardinality: Enumeration = Enumeration(
    name="Cardinality",
    literals={
            EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Required"),
			EnumerationLiteral(name="Many")
    }
)

isHasChoices: Enumeration = Enumeration(
    name="isHasChoices",
    literals={
            EnumerationLiteral(name="isA"),
			EnumerationLiteral(name="hasA")
    }
)

DateDetails: Enumeration = Enumeration(
    name="DateDetails",
    literals={
            EnumerationLiteral(name="DateOnly"),
			EnumerationLiteral(name="TimeOnly"),
			EnumerationLiteral(name="DateAndTime")
    }
)

OperationResultTypes: Enumeration = Enumeration(
    name="OperationResultTypes",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="File")
    }
)

PageTopMenuOptions: Enumeration = Enumeration(
    name="PageTopMenuOptions",
    literals={
            EnumerationLiteral(name="NeverInclude"),
			EnumerationLiteral(name="AlwaysInclude"),
			EnumerationLiteral(name="IncludeWhenAuthenticated")
    }
)

CollectionDisplayOptions: Enumeration = Enumeration(
    name="CollectionDisplayOptions",
    literals={
            EnumerationLiteral(name="LineDirection"),
			EnumerationLiteral(name="PageDirection")
    }
)

IndexDisplayOption: Enumeration = Enumeration(
    name="IndexDisplayOption",
    literals={
            EnumerationLiteral(name="Grid"),
			EnumerationLiteral(name="PageDirection"),
			EnumerationLiteral(name="LineDirection")
    }
)

# Classes
website_Classifier = Class(name="website::Classifier", is_abstract=True)
website_Service = Class(name="website::Service")
website_WebGenModel = Class(name="website::WebGenModel")
website_WebsiteProperties = Class(name="website::WebsiteProperties")
website_Page = Class(name="website::Page")
website_Menu = Class(name="website::Menu", is_abstract=True)
website_EntityOrView = Class(name="website::EntityOrView", is_abstract=True)
website_ImageManipulation = Class(name="website::ImageManipulation")
website_Authentication = Class(name="website::Authentication", is_abstract=True)
website_RegistrationUnit = Class(name="website::RegistrationUnit")
website_LoginUnit = Class(name="website::LoginUnit")
website_ForgottenPasswordUnit = Class(name="website::ForgottenPasswordUnit")
website_Attribute = Class(name="website::Attribute", is_abstract=True)
website_LocalAuthenticationSystem = Class(name="website::LocalAuthenticationSystem")
Authentication = Class(name="Authentication")
website_ModelLabel = Class(name="website::ModelLabel")
website_CasAuthentication = Class(name="website::CasAuthentication")
website_NamedElement = Class(name="website::NamedElement", is_abstract=True)
website_NamedDisplayElement = Class(name="website::NamedDisplayElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
NamedDisplayElement = Class(name="NamedDisplayElement")
website_DataType = Class(name="website::DataType")
Classifier = Class(name="Classifier")
website_EnumerationType = Class(name="website::EnumerationType")
DataType = Class(name="DataType")
website_EnumerationLiteral = Class(name="website::EnumerationLiteral")
website_Feature = Class(name="website::Feature", is_abstract=True)
Feature = Class(name="Feature")
Label = Class(name="Label")
website_Association = Class(name="website::Association", is_abstract=True)
website_EntityFeature = Class(name="website::EntityFeature", is_abstract=True)
website_Expression = Class(name="website::Expression")
website_EncapsulatedAssociation = Class(name="website::EncapsulatedAssociation")
website_Label = Class(name="website::Label", is_abstract=True)
website_ModelLabelFeature = Class(name="website::ModelLabelFeature", is_abstract=True)
website_ModelLabelAttribute = Class(name="website::ModelLabelAttribute")
ModelLabelFeature = Class(name="ModelLabelFeature")
website_ModelLabelAssociation = Class(name="website::ModelLabelAssociation")
website_EntityAssociation = Class(name="website::EntityAssociation", is_abstract=True)
website_Entity = Class(name="website::Entity")
EntityOrView = Class(name="EntityOrView")
website_ResourceAttribute = Class(name="website::ResourceAttribute", is_abstract=True)
website_EntityAttribute = Class(name="website::EntityAttribute", is_abstract=True)
EntityFeature = Class(name="EntityFeature")
Attribute = Class(name="Attribute")
website_DataTypeAttribute = Class(name="website::DataTypeAttribute")
EntityAttribute = Class(name="EntityAttribute")
website_DateAttribute = Class(name="website::DateAttribute")
website_UrlAttribute = Class(name="website::UrlAttribute")
website_PathElement = Class(name="website::PathElement", is_abstract=True)
website_StaticPathElement = Class(name="website::StaticPathElement")
PathElement = Class(name="PathElement")
website_DatePathElement = Class(name="website::DatePathElement")
website_FileAttribute = Class(name="website::FileAttribute")
ResourceAttribute = Class(name="ResourceAttribute")
website_ImageAttribute = Class(name="website::ImageAttribute")
website_LocationAttribute = Class(name="website::LocationAttribute")
Association = Class(name="Association")
website_AssociationKey = Class(name="website::AssociationKey")
website_AssociationWithoutContainment = Class(name="website::AssociationWithoutContainment")
EntityAssociation = Class(name="EntityAssociation")
website_AssociationWithContainment = Class(name="website::AssociationWithContainment")
website_View = Class(name="website::View")
website_ViewFeature = Class(name="website::ViewFeature", is_abstract=True)
website_EncapsulatedFeature = Class(name="website::EncapsulatedFeature")
ViewFeature = Class(name="ViewFeature")
website_EncapsulatedAttribute = Class(name="website::EncapsulatedAttribute")
EncapsulatedFeature = Class(name="EncapsulatedFeature")
website_ViewAssociation = Class(name="website::ViewAssociation")
website_Selection = Class(name="website::Selection")
website_BusinessOperation = Class(name="website::BusinessOperation")
website_SelectionParameter = Class(name="website::SelectionParameter")
website_Predicate = Class(name="website::Predicate")
website_Order = Class(name="website::Order")
website_ImageFilter = Class(name="website::ImageFilter", is_abstract=True)
website_ThumbnailFilter = Class(name="website::ThumbnailFilter")
ImageFilter = Class(name="ImageFilter")
UnitContainer = Class(name="UnitContainer")
website_PageLink = Class(name="website::PageLink")
website_MenuEntry = Class(name="website::MenuEntry", is_abstract=True)
website_StaticMenu = Class(name="website::StaticMenu")
Menu = Class(name="Menu")
website_ActionMenuEntry = Class(name="website::ActionMenuEntry")
MenuEntry = Class(name="MenuEntry")
website_ContentUnit = Class(name="website::ContentUnit", is_abstract=True)
website_Query = Class(name="website::Query")
website_EditStaticTextMenuEntry = Class(name="website::EditStaticTextMenuEntry")
website_DynamicMenu = Class(name="website::DynamicMenu")
website_MenuFeature = Class(name="website::MenuFeature")
website_Filter = Class(name="website::Filter")
website_FilterParameter = Class(name="website::FilterParameter")
website_UnitField = Class(name="website::UnitField", is_abstract=True)
website_UnitSupportAction = Class(name="website::UnitSupportAction")
website_QueryParameter = Class(name="website::QueryParameter")
website_UnitContainer = Class(name="website::UnitContainer", is_abstract=True)
website_StaticUnit = Class(name="website::StaticUnit")
ContentUnit = Class(name="ContentUnit")
website_CreateSitemapUnit = Class(name="website::CreateSitemapUnit")
website_DynamicUnit = Class(name="website::DynamicUnit", is_abstract=True)
website_UnitFeature = Class(name="website::UnitFeature", is_abstract=True)
UnitField = Class(name="UnitField")
InlineActionContainer = Class(name="InlineActionContainer")
website_UnitAssociation = Class(name="website::UnitAssociation")
AssociationReference = Class(name="AssociationReference")
website_UnitElement = Class(name="website::UnitElement")
UnitFeature = Class(name="UnitFeature")
website_DataTypeField = Class(name="website::DataTypeField")
InterfaceField = Class(name="InterfaceField")
website_DateField = Class(name="website::DateField")
website_CaptchaField = Class(name="website::CaptchaField")
website_AssociationReference = Class(name="website::AssociationReference", is_abstract=True)
website_ChildPath = Class(name="website::ChildPath", is_abstract=True)
website_InterfaceField = Class(name="website::InterfaceField", is_abstract=True)
SelectableUnit = Class(name="SelectableUnit")
website_EditUnit = Class(name="website::EditUnit", is_abstract=True)
DynamicUnit = Class(name="DynamicUnit")
SingletonUnit = Class(name="SingletonUnit")
website_SelectableUnit = Class(name="website::SelectableUnit", is_abstract=True)
website_SingletonUnit = Class(name="website::SingletonUnit", is_abstract=True)
website_CollectionUnit = Class(name="website::CollectionUnit", is_abstract=True)
website_UpdateUnit = Class(name="website::UpdateUnit")
website_MapUnit = Class(name="website::MapUnit")
website_DataUnit = Class(name="website::DataUnit", is_abstract=True)
website_DetailsUnit = Class(name="website::DetailsUnit")
DataUnit = Class(name="DataUnit")
website_CreateUnit = Class(name="website::CreateUnit")
EditUnit = Class(name="EditUnit")
website_CreateUpdateUnit = Class(name="website::CreateUpdateUnit")
website_SearchUnit = Class(name="website::SearchUnit")
ControlUnit = Class(name="ControlUnit")
website_ImageUnit = Class(name="website::ImageUnit", is_abstract=True)
website_FeaturePath = Class(name="website::FeaturePath", is_abstract=True)
website_FeaturePathAttribute = Class(name="website::FeaturePathAttribute")
FeaturePath = Class(name="FeaturePath")
website_FeaturePathAssociation = Class(name="website::FeaturePathAssociation")
website_IndexUnit = Class(name="website::IndexUnit")
CollectionUnit = Class(name="CollectionUnit")
website_ControlUnit = Class(name="website::ControlUnit", is_abstract=True)
ChildPath = Class(name="ChildPath")
website_ChildPathAssociation = Class(name="website::ChildPathAssociation")
website_ImageIndexUnit = Class(name="website::ImageIndexUnit")
ImageUnit = Class(name="ImageUnit")
website_SliderUnit = Class(name="website::SliderUnit")
website_GalleryUnit = Class(name="website::GalleryUnit")
website_ChildPathAttribute = Class(name="website::ChildPathAttribute")
website_AuthenticationUnit = Class(name="website::AuthenticationUnit", is_abstract=True)
AuthenticationUnit = Class(name="AuthenticationUnit")
website_InlineActionContainer = Class(name="website::InlineActionContainer", is_abstract=True)
website_InlineAction = Class(name="website::InlineAction", is_abstract=True)
website_DeleteAction = Class(name="website::DeleteAction")
website_FeatureSupportAction = Class(name="website::FeatureSupportAction")
website_ModelReference = Class(name="website::ModelReference")
Path = Class(name="Path")
website_FeatureReference = Class(name="website::FeatureReference")
website_RouteParameterReference = Class(name="website::RouteParameterReference")
website_ParameterReference = Class(name="website::ParameterReference")
website_CurrentUserReference = Class(name="website::CurrentUserReference")
website_SelectAction = Class(name="website::SelectAction")
InlineAction = Class(name="InlineAction")

# website_Classifier class attributes and methods

# website_Service class attributes and methods

# website_WebGenModel class attributes and methods

# website_WebsiteProperties class attributes and methods
website_WebsiteProperties_databaseTechnology: Property = Property(name="databaseTechnology", type=StringType)
website_WebsiteProperties_databasePrefix: Property = Property(name="databasePrefix", type=StringType)
website_WebsiteProperties_databaseHost: Property = Property(name="databaseHost", type=StringType)
website_WebsiteProperties_databaseName: Property = Property(name="databaseName", type=StringType)
website_WebsiteProperties_databasePort: Property = Property(name="databasePort", type=StringType)
website_WebsiteProperties_databaseUsername: Property = Property(name="databaseUsername", type=StringType)
website_WebsiteProperties_databasePassword: Property = Property(name="databasePassword", type=StringType)
website_WebsiteProperties_siteTitle: Property = Property(name="siteTitle", type=StringType)
website_WebsiteProperties_developmentVersion: Property = Property(name="developmentVersion", type=BooleanType)
website_WebsiteProperties_baseURL: Property = Property(name="baseURL", type=StringType)
website_WebsiteProperties_rewriteURLs: Property = Property(name="rewriteURLs", type=BooleanType)
website_WebsiteProperties_webmasterEmail: Property = Property(name="webmasterEmail", type=StringType)
website_WebsiteProperties_copyrightText: Property = Property(name="copyrightText", type=StringType)
website_WebsiteProperties_metaDescription: Property = Property(name="metaDescription", type=StringType)
website_WebsiteProperties_projectName: Property = Property(name="projectName", type=StringType)
website_WebsiteProperties_testProjectName: Property = Property(name="testProjectName", type=StringType)
website_WebsiteProperties_defaultDateFormat: Property = Property(name="defaultDateFormat", type=StringType)
website_WebsiteProperties_defaultTimeFormat: Property = Property(name="defaultTimeFormat", type=StringType)
website_WebsiteProperties_defaultDateTimeFormat: Property = Property(name="defaultDateTimeFormat", type=StringType)
website_WebsiteProperties_defaultMaximumUploadSize: Property = Property(name="defaultMaximumUploadSize", type=IntegerType)
website_WebsiteProperties_ormTechnology: Property = Property(name="ormTechnology", type=StringType)
website_WebsiteProperties_timestampCreation: Property = Property(name="timestampCreation", type=BooleanType)
website_WebsiteProperties_timestampUpdates: Property = Property(name="timestampUpdates", type=BooleanType)
website_WebsiteProperties_frameworkTechnology: Property = Property(name="frameworkTechnology", type=StringType)
website_WebsiteProperties_inputTechnology: Property = Property(name="inputTechnology", type=StringType)
website_WebsiteProperties_ajaxTechnology: Property = Property(name="ajaxTechnology", type=StringType)
website_WebsiteProperties_captchaSiteKey: Property = Property(name="captchaSiteKey", type=StringType)
website_WebsiteProperties_captchaSecretKey: Property = Property(name="captchaSecretKey", type=StringType)
website_WebsiteProperties_textEditorURL: Property = Property(name="textEditorURL", type=StringType)
website_WebsiteProperties_responsiveTopMenu: Property = Property(name="responsiveTopMenu", type=BooleanType)
website_WebsiteProperties_topNavigationId: Property = Property(name="topNavigationId", type=StringType)
website_WebsiteProperties_siteTemplate: Property = Property(name="siteTemplate", type=StringType)
website_WebsiteProperties_staticUnitsEditable: Property = Property(name="staticUnitsEditable", type=BooleanType)
website_WebsiteProperties.attributes={website_WebsiteProperties_siteTitle, website_WebsiteProperties_databasePrefix, website_WebsiteProperties_textEditorURL, website_WebsiteProperties_testProjectName, website_WebsiteProperties_webmasterEmail, website_WebsiteProperties_timestampCreation, website_WebsiteProperties_databasePort, website_WebsiteProperties_ormTechnology, website_WebsiteProperties_captchaSiteKey, website_WebsiteProperties_captchaSecretKey, website_WebsiteProperties_projectName, website_WebsiteProperties_staticUnitsEditable, website_WebsiteProperties_timestampUpdates, website_WebsiteProperties_databaseHost, website_WebsiteProperties_defaultDateTimeFormat, website_WebsiteProperties_copyrightText, website_WebsiteProperties_defaultDateFormat, website_WebsiteProperties_developmentVersion, website_WebsiteProperties_rewriteURLs, website_WebsiteProperties_databaseTechnology, website_WebsiteProperties_siteTemplate, website_WebsiteProperties_databaseName, website_WebsiteProperties_ajaxTechnology, website_WebsiteProperties_databaseUsername, website_WebsiteProperties_metaDescription, website_WebsiteProperties_topNavigationId, website_WebsiteProperties_defaultTimeFormat, website_WebsiteProperties_defaultMaximumUploadSize, website_WebsiteProperties_inputTechnology, website_WebsiteProperties_databasePassword, website_WebsiteProperties_frameworkTechnology, website_WebsiteProperties_baseURL, website_WebsiteProperties_responsiveTopMenu}

# website_Page class attributes and methods
website_Page_authenticated: Property = Property(name="authenticated", type=BooleanType)
website_Page_uriElement: Property = Property(name="uriElement", type=StringType)
website_Page_topMenuOption: Property = Property(name="topMenuOption", type=StringType)
website_Page_topMenuRank: Property = Property(name="topMenuRank", type=IntegerType)
website_Page_navigationLabel: Property = Property(name="navigationLabel", type=StringType)
website_Page_styleClass: Property = Property(name="styleClass", type=StringType)
website_Page.attributes={website_Page_uriElement, website_Page_navigationLabel, website_Page_authenticated, website_Page_topMenuRank, website_Page_topMenuOption, website_Page_styleClass}

# website_Menu class attributes and methods
website_Menu_omitCaption: Property = Property(name="omitCaption", type=BooleanType)
website_Menu_captionClass: Property = Property(name="captionClass", type=StringType)
website_Menu_styleClass: Property = Property(name="styleClass", type=StringType)
website_Menu_layoutClass: Property = Property(name="layoutClass", type=StringType)
website_Menu.attributes={website_Menu_styleClass, website_Menu_captionClass, website_Menu_omitCaption, website_Menu_layoutClass}

# website_EntityOrView class attributes and methods
website_EntityOrView_singletonName: Property = Property(name="singletonName", type=StringType)
website_EntityOrView_pluralisedName: Property = Property(name="pluralisedName", type=StringType)
website_EntityOrView_tableName: Property = Property(name="tableName", type=StringType)
website_EntityOrView_autoKeyName: Property = Property(name="autoKeyName", type=StringType)
website_EntityOrView_autoKeyPersistentType: Property = Property(name="autoKeyPersistentType", type=StringType)
website_EntityOrView_autoKeyGenerationStrategy: Property = Property(name="autoKeyGenerationStrategy", type=StringType)
website_EntityOrView_serializationExcludeAll: Property = Property(name="serializationExcludeAll", type=BooleanType)
website_EntityOrView_implementsUserInterface: Property = Property(name="implementsUserInterface", type=BooleanType)
website_EntityOrView.attributes={website_EntityOrView_autoKeyName, website_EntityOrView_serializationExcludeAll, website_EntityOrView_tableName, website_EntityOrView_implementsUserInterface, website_EntityOrView_autoKeyPersistentType, website_EntityOrView_autoKeyGenerationStrategy, website_EntityOrView_singletonName, website_EntityOrView_pluralisedName}

# website_ImageManipulation class attributes and methods
website_ImageManipulation_jpegQuality: Property = Property(name="jpegQuality", type=IntegerType)
website_ImageManipulation.attributes={website_ImageManipulation_jpegQuality}

# website_Authentication class attributes and methods
website_Authentication_loginLabel: Property = Property(name="loginLabel", type=StringType)
website_Authentication_logoutLabel: Property = Property(name="logoutLabel", type=StringType)
website_Authentication.attributes={website_Authentication_logoutLabel, website_Authentication_loginLabel}

# website_RegistrationUnit class attributes and methods
website_RegistrationUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_RegistrationUnit.attributes={website_RegistrationUnit_styleClass}

# website_LoginUnit class attributes and methods
website_LoginUnit_logoutUriElement: Property = Property(name="logoutUriElement", type=StringType)
website_LoginUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_LoginUnit.attributes={website_LoginUnit_styleClass, website_LoginUnit_logoutUriElement}

# website_ForgottenPasswordUnit class attributes and methods
website_ForgottenPasswordUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_ForgottenPasswordUnit.attributes={website_ForgottenPasswordUnit_styleClass}

# website_Attribute class attributes and methods
website_Attribute_placeholder: Property = Property(name="placeholder", type=StringType)
website_Attribute_validationPattern: Property = Property(name="validationPattern", type=StringType)
website_Attribute_inputClass: Property = Property(name="inputClass", type=StringType)
website_Attribute.attributes={website_Attribute_validationPattern, website_Attribute_inputClass, website_Attribute_placeholder}

# website_LocalAuthenticationSystem class attributes and methods
website_LocalAuthenticationSystem_useEmailActivation: Property = Property(name="useEmailActivation", type=BooleanType)
website_LocalAuthenticationSystem_sendWelcomeEmail: Property = Property(name="sendWelcomeEmail", type=BooleanType)
website_LocalAuthenticationSystem_authenticationKey: Property = Property(name="authenticationKey", type=StringType)
website_LocalAuthenticationSystem_useCaptcha: Property = Property(name="useCaptcha", type=BooleanType)
website_LocalAuthenticationSystem_allowRememberMe: Property = Property(name="allowRememberMe", type=BooleanType)
website_LocalAuthenticationSystem_allowSelfRegistration: Property = Property(name="allowSelfRegistration", type=BooleanType)
website_LocalAuthenticationSystem_trackLoginAttempts: Property = Property(name="trackLoginAttempts", type=BooleanType)
website_LocalAuthenticationSystem.attributes={website_LocalAuthenticationSystem_allowRememberMe, website_LocalAuthenticationSystem_trackLoginAttempts, website_LocalAuthenticationSystem_sendWelcomeEmail, website_LocalAuthenticationSystem_useEmailActivation, website_LocalAuthenticationSystem_authenticationKey, website_LocalAuthenticationSystem_allowSelfRegistration, website_LocalAuthenticationSystem_useCaptcha}

# Authentication class attributes and methods

# website_ModelLabel class attributes and methods
website_ModelLabel_format: Property = Property(name="format", type=StringType)
website_ModelLabel.attributes={website_ModelLabel_format}

# website_CasAuthentication class attributes and methods

# website_NamedElement class attributes and methods
website_NamedElement_name: Property = Property(name="name", type=StringType)
website_NamedElement.attributes={website_NamedElement_name}

# website_NamedDisplayElement class attributes and methods
website_NamedDisplayElement_displayLabel: Property = Property(name="displayLabel", type=StringType)
website_NamedDisplayElement.attributes={website_NamedDisplayElement_displayLabel}

# NamedElement class attributes and methods

# NamedDisplayElement class attributes and methods

# website_DataType class attributes and methods
website_DataType_persistentType: Property = Property(name="persistentType", type=StringType)
website_DataType_ormType: Property = Property(name="ormType", type=StringType)
website_DataType_interfaceType: Property = Property(name="interfaceType", type=StringType)
website_DataType_placeholder: Property = Property(name="placeholder", type=StringType)
website_DataType_validationPattern: Property = Property(name="validationPattern", type=StringType)
website_DataType.attributes={website_DataType_persistentType, website_DataType_ormType, website_DataType_placeholder, website_DataType_interfaceType, website_DataType_validationPattern}

# Classifier class attributes and methods

# website_EnumerationType class attributes and methods

# DataType class attributes and methods

# website_EnumerationLiteral class attributes and methods

# website_Feature class attributes and methods
website_Feature_serializationExpose: Property = Property(name="serializationExpose", type=BooleanType)
website_Feature_headerClass: Property = Property(name="headerClass", type=StringType)
website_Feature_displayClass: Property = Property(name="displayClass", type=StringType)
website_Feature_footerClass: Property = Property(name="footerClass", type=StringType)
website_Feature_title: Property = Property(name="title", type=StringType)
website_Feature_collectionAllowAdd: Property = Property(name="collectionAllowAdd", type=BooleanType)
website_Feature_collectionAllowRemove: Property = Property(name="collectionAllowRemove", type=BooleanType)
website_Feature_nullDisplayValue: Property = Property(name="nullDisplayValue", type=StringType)
website_Feature_encodeUriKey: Property = Property(name="encodeUriKey", type=BooleanType)
website_Feature_serializationGroups: Property = Property(name="serializationGroups", type=StringType)
website_Feature.attributes={website_Feature_encodeUriKey, website_Feature_displayClass, website_Feature_headerClass, website_Feature_serializationExpose, website_Feature_footerClass, website_Feature_collectionAllowRemove, website_Feature_serializationGroups, website_Feature_collectionAllowAdd, website_Feature_nullDisplayValue, website_Feature_title}

# Feature class attributes and methods

# Label class attributes and methods

# website_Association class attributes and methods
website_Association_pseudo: Property = Property(name="pseudo", type=BooleanType)
website_Association_inputClass: Property = Property(name="inputClass", type=StringType)
website_Association_serializationMaxDepth: Property = Property(name="serializationMaxDepth", type=IntegerType)
website_Association.attributes={website_Association_serializationMaxDepth, website_Association_inputClass, website_Association_pseudo}

# website_EntityFeature class attributes and methods
website_EntityFeature_cardinality: Property = Property(name="cardinality", type=StringType)
website_EntityFeature_unique: Property = Property(name="unique", type=BooleanType)
website_EntityFeature_ordered: Property = Property(name="ordered", type=BooleanType)
website_EntityFeature_booleanIsHasChoice: Property = Property(name="booleanIsHasChoice", type=StringType)
website_EntityFeature_singletonName: Property = Property(name="singletonName", type=StringType)
website_EntityFeature_pluralisedName: Property = Property(name="pluralisedName", type=StringType)
website_EntityFeature_columnName: Property = Property(name="columnName", type=StringType)
website_EntityFeature.attributes={website_EntityFeature_singletonName, website_EntityFeature_unique, website_EntityFeature_columnName, website_EntityFeature_booleanIsHasChoice, website_EntityFeature_pluralisedName, website_EntityFeature_ordered, website_EntityFeature_cardinality}

# website_Expression class attributes and methods

# website_EncapsulatedAssociation class attributes and methods
website_EncapsulatedAssociation_name: Property = Property(name="name", type=StringType)
website_EncapsulatedAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
website_EncapsulatedAssociation_cardinality: Property = Property(name="cardinality", type=StringType)
website_EncapsulatedAssociation.attributes={website_EncapsulatedAssociation_name, website_EncapsulatedAssociation_isSourceAssociation, website_EncapsulatedAssociation_cardinality}

# website_Label class attributes and methods

# website_ModelLabelFeature class attributes and methods

# website_ModelLabelAttribute class attributes and methods
website_ModelLabelAttribute_dateFormat: Property = Property(name="dateFormat", type=StringType)
website_ModelLabelAttribute.attributes={website_ModelLabelAttribute_dateFormat}

# ModelLabelFeature class attributes and methods

# website_ModelLabelAssociation class attributes and methods
website_ModelLabelAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
website_ModelLabelAssociation.attributes={website_ModelLabelAssociation_isSourceAssociation}

# website_EntityAssociation class attributes and methods
website_EntityAssociation_bidirectional: Property = Property(name="bidirectional", type=BooleanType)
website_EntityAssociation_pivotTableName: Property = Property(name="pivotTableName", type=StringType)
website_EntityAssociation_targetFeatureName: Property = Property(name="targetFeatureName", type=StringType)
website_EntityAssociation_targetPrimaryKey: Property = Property(name="targetPrimaryKey", type=BooleanType)
website_EntityAssociation_targetDisplayLabel: Property = Property(name="targetDisplayLabel", type=StringType)
website_EntityAssociation_targetHeaderClass: Property = Property(name="targetHeaderClass", type=StringType)
website_EntityAssociation_targetInputClass: Property = Property(name="targetInputClass", type=StringType)
website_EntityAssociation_targetDisplayClass: Property = Property(name="targetDisplayClass", type=StringType)
website_EntityAssociation_targetFooterClass: Property = Property(name="targetFooterClass", type=StringType)
website_EntityAssociation.attributes={website_EntityAssociation_targetDisplayLabel, website_EntityAssociation_targetPrimaryKey, website_EntityAssociation_pivotTableName, website_EntityAssociation_bidirectional, website_EntityAssociation_targetFooterClass, website_EntityAssociation_targetFeatureName, website_EntityAssociation_targetDisplayClass, website_EntityAssociation_targetHeaderClass, website_EntityAssociation_targetInputClass}

# website_Entity class attributes and methods

# EntityOrView class attributes and methods

# website_ResourceAttribute class attributes and methods
website_ResourceAttribute_maximumUploadSize: Property = Property(name="maximumUploadSize", type=IntegerType)
website_ResourceAttribute_validUploadMimeTypes: Property = Property(name="validUploadMimeTypes", type=StringType)
website_ResourceAttribute_validUploadExtensions: Property = Property(name="validUploadExtensions", type=StringType)
website_ResourceAttribute_uploadsWithinWebsite: Property = Property(name="uploadsWithinWebsite", type=BooleanType)
website_ResourceAttribute.attributes={website_ResourceAttribute_validUploadMimeTypes, website_ResourceAttribute_validUploadExtensions, website_ResourceAttribute_uploadsWithinWebsite, website_ResourceAttribute_maximumUploadSize}

# website_EntityAttribute class attributes and methods
website_EntityAttribute_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
website_EntityAttribute_containerUnique: Property = Property(name="containerUnique", type=BooleanType)
website_EntityAttribute_persistentType: Property = Property(name="persistentType", type=StringType)
website_EntityAttribute_ormType: Property = Property(name="ormType", type=StringType)
website_EntityAttribute_interfaceType: Property = Property(name="interfaceType", type=StringType)
website_EntityAttribute.attributes={website_EntityAttribute_primaryKey, website_EntityAttribute_ormType, website_EntityAttribute_persistentType, website_EntityAttribute_containerUnique, website_EntityAttribute_interfaceType}

# EntityFeature class attributes and methods

# Attribute class attributes and methods

# website_DataTypeAttribute class attributes and methods
website_DataTypeAttribute_obfuscateFormFields: Property = Property(name="obfuscateFormFields", type=BooleanType)
website_DataTypeAttribute_caseInsensitive: Property = Property(name="caseInsensitive", type=BooleanType)
website_DataTypeAttribute_encrypt: Property = Property(name="encrypt", type=BooleanType)
website_DataTypeAttribute.attributes={website_DataTypeAttribute_encrypt, website_DataTypeAttribute_obfuscateFormFields, website_DataTypeAttribute_caseInsensitive}

# EntityAttribute class attributes and methods

# website_DateAttribute class attributes and methods
website_DateAttribute_details: Property = Property(name="details", type=StringType)
website_DateAttribute_format: Property = Property(name="format", type=StringType)
website_DateAttribute.attributes={website_DateAttribute_format, website_DateAttribute_details}

# website_UrlAttribute class attributes and methods
website_UrlAttribute_displayValue: Property = Property(name="displayValue", type=StringType)
website_UrlAttribute.attributes={website_UrlAttribute_displayValue}

# website_PathElement class attributes and methods

# website_StaticPathElement class attributes and methods
website_StaticPathElement_element: Property = Property(name="element", type=StringType)
website_StaticPathElement.attributes={website_StaticPathElement_element}

# PathElement class attributes and methods

# website_DatePathElement class attributes and methods
website_DatePathElement_format: Property = Property(name="format", type=StringType)
website_DatePathElement.attributes={website_DatePathElement_format}

# website_FileAttribute class attributes and methods

# ResourceAttribute class attributes and methods

# website_ImageAttribute class attributes and methods

# website_LocationAttribute class attributes and methods

# Association class attributes and methods

# website_AssociationKey class attributes and methods
website_AssociationKey_targetColumnName: Property = Property(name="targetColumnName", type=StringType)
website_AssociationKey.attributes={website_AssociationKey_targetColumnName}

# website_AssociationWithoutContainment class attributes and methods
website_AssociationWithoutContainment_targetCardinality: Property = Property(name="targetCardinality", type=StringType)
website_AssociationWithoutContainment_targetUnique: Property = Property(name="targetUnique", type=BooleanType)
website_AssociationWithoutContainment.attributes={website_AssociationWithoutContainment_targetCardinality, website_AssociationWithoutContainment_targetUnique}

# EntityAssociation class attributes and methods

# website_AssociationWithContainment class attributes and methods
website_AssociationWithContainment_sourceVisible: Property = Property(name="sourceVisible", type=BooleanType)
website_AssociationWithContainment.attributes={website_AssociationWithContainment_sourceVisible}

# website_View class attributes and methods

# website_ViewFeature class attributes and methods

# website_EncapsulatedFeature class attributes and methods
website_EncapsulatedFeature_displayLabel: Property = Property(name="displayLabel", type=StringType)
website_EncapsulatedFeature_alias: Property = Property(name="alias", type=StringType)
website_EncapsulatedFeature_columnName: Property = Property(name="columnName", type=StringType)
website_EncapsulatedFeature.attributes={website_EncapsulatedFeature_alias, website_EncapsulatedFeature_displayLabel, website_EncapsulatedFeature_columnName}

# ViewFeature class attributes and methods

# website_EncapsulatedAttribute class attributes and methods
website_EncapsulatedAttribute_name: Property = Property(name="name", type=StringType)
website_EncapsulatedAttribute_cardinality: Property = Property(name="cardinality", type=StringType)
website_EncapsulatedAttribute.attributes={website_EncapsulatedAttribute_cardinality, website_EncapsulatedAttribute_name}

# EncapsulatedFeature class attributes and methods

# website_ViewAssociation class attributes and methods
website_ViewAssociation_cardinality: Property = Property(name="cardinality", type=StringType)
website_ViewAssociation.attributes={website_ViewAssociation_cardinality}

# website_Selection class attributes and methods
website_Selection_distinct: Property = Property(name="distinct", type=BooleanType)
website_Selection_limit: Property = Property(name="limit", type=IntegerType)
website_Selection_selected: Property = Property(name="selected", type=BooleanType)
website_Selection.attributes={website_Selection_selected, website_Selection_distinct, website_Selection_limit}

# website_BusinessOperation class attributes and methods
website_BusinessOperation_resultType: Property = Property(name="resultType", type=StringType)
website_BusinessOperation_resultMimeType: Property = Property(name="resultMimeType", type=StringType)
website_BusinessOperation.attributes={website_BusinessOperation_resultType, website_BusinessOperation_resultMimeType}

# website_SelectionParameter class attributes and methods
website_SelectionParameter_optional: Property = Property(name="optional", type=BooleanType)
website_SelectionParameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
website_SelectionParameter.attributes={website_SelectionParameter_defaultValue, website_SelectionParameter_optional}

# website_Predicate class attributes and methods

# website_Order class attributes and methods

# website_ImageFilter class attributes and methods

# website_ThumbnailFilter class attributes and methods
website_ThumbnailFilter_width: Property = Property(name="width", type=IntegerType)
website_ThumbnailFilter_height: Property = Property(name="height", type=IntegerType)
website_ThumbnailFilter.attributes={website_ThumbnailFilter_height, website_ThumbnailFilter_width}

# ImageFilter class attributes and methods

# UnitContainer class attributes and methods

# website_PageLink class attributes and methods

# website_MenuEntry class attributes and methods
website_MenuEntry_requiresRole: Property = Property(name="requiresRole", type=StringType)
website_MenuEntry.attributes={website_MenuEntry_requiresRole}

# website_StaticMenu class attributes and methods

# Menu class attributes and methods

# website_ActionMenuEntry class attributes and methods

# MenuEntry class attributes and methods

# website_ContentUnit class attributes and methods
website_ContentUnit_createDefaultUriElement: Property = Property(name="createDefaultUriElement", type=BooleanType)
website_ContentUnit_requiresRole: Property = Property(name="requiresRole", type=StringType)
website_ContentUnit_purposeSummary: Property = Property(name="purposeSummary", type=StringType)
website_ContentUnit_uriElement: Property = Property(name="uriElement", type=StringType)
website_ContentUnit_alternative: Property = Property(name="alternative", type=StringType)
website_ContentUnit_omitCaption: Property = Property(name="omitCaption", type=BooleanType)
website_ContentUnit_captionClass: Property = Property(name="captionClass", type=StringType)
website_ContentUnit.attributes={website_ContentUnit_createDefaultUriElement, website_ContentUnit_omitCaption, website_ContentUnit_captionClass, website_ContentUnit_uriElement, website_ContentUnit_alternative, website_ContentUnit_purposeSummary, website_ContentUnit_requiresRole}

# website_Query class attributes and methods

# website_EditStaticTextMenuEntry class attributes and methods

# website_DynamicMenu class attributes and methods

# website_MenuFeature class attributes and methods

# website_Filter class attributes and methods

# website_FilterParameter class attributes and methods
website_FilterParameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
website_FilterParameter_placeholder: Property = Property(name="placeholder", type=StringType)
website_FilterParameter.attributes={website_FilterParameter_placeholder, website_FilterParameter_defaultValue}

# website_UnitField class attributes and methods
website_UnitField_title: Property = Property(name="title", type=StringType)
website_UnitField_collectionDisplayOption: Property = Property(name="collectionDisplayOption", type=StringType)
website_UnitField_collectionAllowAdd: Property = Property(name="collectionAllowAdd", type=BooleanType)
website_UnitField_collectionAllowRemove: Property = Property(name="collectionAllowRemove", type=BooleanType)
website_UnitField_maximumDisplaySize: Property = Property(name="maximumDisplaySize", type=IntegerType)
website_UnitField_dateFormat: Property = Property(name="dateFormat", type=StringType)
website_UnitField.attributes={website_UnitField_maximumDisplaySize, website_UnitField_collectionAllowAdd, website_UnitField_dateFormat, website_UnitField_collectionDisplayOption, website_UnitField_title, website_UnitField_collectionAllowRemove}

# website_UnitSupportAction class attributes and methods
website_UnitSupportAction_disable: Property = Property(name="disable", type=BooleanType)
website_UnitSupportAction_confirmMessage: Property = Property(name="confirmMessage", type=StringType)
website_UnitSupportAction.attributes={website_UnitSupportAction_confirmMessage, website_UnitSupportAction_disable}

# website_QueryParameter class attributes and methods
website_QueryParameter_value: Property = Property(name="value", type=StringType)
website_QueryParameter.attributes={website_QueryParameter_value}

# website_UnitContainer class attributes and methods

# website_StaticUnit class attributes and methods
website_StaticUnit_content: Property = Property(name="content", type=StringType)
website_StaticUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_StaticUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_StaticUnit.attributes={website_StaticUnit_styleClass, website_StaticUnit_contentClass, website_StaticUnit_content}

# ContentUnit class attributes and methods

# website_CreateSitemapUnit class attributes and methods
website_CreateSitemapUnit_deployedURL: Property = Property(name="deployedURL", type=StringType)
website_CreateSitemapUnit_filename: Property = Property(name="filename", type=StringType)
website_CreateSitemapUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_CreateSitemapUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_CreateSitemapUnit.attributes={website_CreateSitemapUnit_filename, website_CreateSitemapUnit_styleClass, website_CreateSitemapUnit_contentClass, website_CreateSitemapUnit_deployedURL}

# website_DynamicUnit class attributes and methods
website_DynamicUnit_header: Property = Property(name="header", type=StringType)
website_DynamicUnit_footer: Property = Property(name="footer", type=StringType)
website_DynamicUnit_headerClass: Property = Property(name="headerClass", type=StringType)
website_DynamicUnit_controlClass: Property = Property(name="controlClass", type=StringType)
website_DynamicUnit_footerClass: Property = Property(name="footerClass", type=StringType)
website_DynamicUnit_errorClass: Property = Property(name="errorClass", type=StringType)
website_DynamicUnit.attributes={website_DynamicUnit_footer, website_DynamicUnit_header, website_DynamicUnit_footerClass, website_DynamicUnit_controlClass, website_DynamicUnit_errorClass, website_DynamicUnit_headerClass}

# website_UnitFeature class attributes and methods
website_UnitFeature_onlyDisplayWhenNotEmpty: Property = Property(name="onlyDisplayWhenNotEmpty", type=BooleanType)
website_UnitFeature_displayLabel: Property = Property(name="displayLabel", type=StringType)
website_UnitFeature_required: Property = Property(name="required", type=BooleanType)
website_UnitFeature_nullDisplayValue: Property = Property(name="nullDisplayValue", type=StringType)
website_UnitFeature_footer: Property = Property(name="footer", type=StringType)
website_UnitFeature_autofocus: Property = Property(name="autofocus", type=BooleanType)
website_UnitFeature_headerClass: Property = Property(name="headerClass", type=StringType)
website_UnitFeature_inputClass: Property = Property(name="inputClass", type=StringType)
website_UnitFeature_displayClass: Property = Property(name="displayClass", type=StringType)
website_UnitFeature_footerClass: Property = Property(name="footerClass", type=StringType)
website_UnitFeature.attributes={website_UnitFeature_required, website_UnitFeature_footerClass, website_UnitFeature_footer, website_UnitFeature_headerClass, website_UnitFeature_displayClass, website_UnitFeature_nullDisplayValue, website_UnitFeature_autofocus, website_UnitFeature_inputClass, website_UnitFeature_onlyDisplayWhenNotEmpty, website_UnitFeature_displayLabel}

# UnitField class attributes and methods

# InlineActionContainer class attributes and methods

# website_UnitAssociation class attributes and methods
website_UnitAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
website_UnitAssociation.attributes={website_UnitAssociation_isSourceAssociation}

# AssociationReference class attributes and methods

# website_UnitElement class attributes and methods
website_UnitElement_name: Property = Property(name="name", type=StringType)
website_UnitElement_obfuscateFormFields: Property = Property(name="obfuscateFormFields", type=BooleanType)
website_UnitElement_placeholder: Property = Property(name="placeholder", type=StringType)
website_UnitElement_validationPattern: Property = Property(name="validationPattern", type=StringType)
website_UnitElement.attributes={website_UnitElement_placeholder, website_UnitElement_obfuscateFormFields, website_UnitElement_validationPattern, website_UnitElement_name}

# UnitFeature class attributes and methods

# website_DataTypeField class attributes and methods
website_DataTypeField_obfuscateFormFields: Property = Property(name="obfuscateFormFields", type=BooleanType)
website_DataTypeField_encrypt: Property = Property(name="encrypt", type=BooleanType)
website_DataTypeField_interfaceType: Property = Property(name="interfaceType", type=StringType)
website_DataTypeField.attributes={website_DataTypeField_interfaceType, website_DataTypeField_encrypt, website_DataTypeField_obfuscateFormFields}

# InterfaceField class attributes and methods

# website_DateField class attributes and methods
website_DateField_details: Property = Property(name="details", type=StringType)
website_DateField_format: Property = Property(name="format", type=StringType)
website_DateField.attributes={website_DateField_details, website_DateField_format}

# website_CaptchaField class attributes and methods

# website_AssociationReference class attributes and methods
website_AssociationReference_name: Property = Property(name="name", type=StringType)
website_AssociationReference.attributes={website_AssociationReference_name}

# website_ChildPath class attributes and methods

# website_InterfaceField class attributes and methods
website_InterfaceField_inputClass: Property = Property(name="inputClass", type=StringType)
website_InterfaceField_placeholder: Property = Property(name="placeholder", type=StringType)
website_InterfaceField_validationPattern: Property = Property(name="validationPattern", type=StringType)
website_InterfaceField_required: Property = Property(name="required", type=BooleanType)
website_InterfaceField_defaultValue: Property = Property(name="defaultValue", type=StringType)
website_InterfaceField.attributes={website_InterfaceField_required, website_InterfaceField_defaultValue, website_InterfaceField_inputClass, website_InterfaceField_validationPattern, website_InterfaceField_placeholder}

# SelectableUnit class attributes and methods

# website_EditUnit class attributes and methods
website_EditUnit_confirmLabel: Property = Property(name="confirmLabel", type=StringType)
website_EditUnit_cancelLabel: Property = Property(name="cancelLabel", type=StringType)
website_EditUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_EditUnit_customiseValues: Property = Property(name="customiseValues", type=BooleanType)
website_EditUnit.attributes={website_EditUnit_confirmLabel, website_EditUnit_customiseValues, website_EditUnit_contentClass, website_EditUnit_cancelLabel}

# DynamicUnit class attributes and methods

# SingletonUnit class attributes and methods

# website_SelectableUnit class attributes and methods

# website_SingletonUnit class attributes and methods

# website_CollectionUnit class attributes and methods
website_CollectionUnit_emptyMessage: Property = Property(name="emptyMessage", type=StringType)
website_CollectionUnit_defaultPaginationSize: Property = Property(name="defaultPaginationSize", type=IntegerType)
website_CollectionUnit_nextNpages: Property = Property(name="nextNpages", type=IntegerType)
website_CollectionUnit_previousNpages: Property = Property(name="previousNpages", type=IntegerType)
website_CollectionUnit_nextPageLabel: Property = Property(name="nextPageLabel", type=StringType)
website_CollectionUnit_previousPageLabel: Property = Property(name="previousPageLabel", type=StringType)
website_CollectionUnit_useDisabledPageLinks: Property = Property(name="useDisabledPageLinks", type=BooleanType)
website_CollectionUnit_useFirstLastPageLinks: Property = Property(name="useFirstLastPageLinks", type=BooleanType)
website_CollectionUnit_firstPageLabel: Property = Property(name="firstPageLabel", type=StringType)
website_CollectionUnit_lastPageLabel: Property = Property(name="lastPageLabel", type=StringType)
website_CollectionUnit.attributes={website_CollectionUnit_previousNpages, website_CollectionUnit_useDisabledPageLinks, website_CollectionUnit_nextPageLabel, website_CollectionUnit_nextNpages, website_CollectionUnit_useFirstLastPageLinks, website_CollectionUnit_firstPageLabel, website_CollectionUnit_previousPageLabel, website_CollectionUnit_lastPageLabel, website_CollectionUnit_defaultPaginationSize, website_CollectionUnit_emptyMessage}

# website_UpdateUnit class attributes and methods
website_UpdateUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_UpdateUnit.attributes={website_UpdateUnit_styleClass}

# website_MapUnit class attributes and methods
website_MapUnit_readOnly: Property = Property(name="readOnly", type=BooleanType)
website_MapUnit_defaultZoomLevel: Property = Property(name="defaultZoomLevel", type=IntegerType)
website_MapUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_MapUnit.attributes={website_MapUnit_defaultZoomLevel, website_MapUnit_readOnly, website_MapUnit_styleClass}

# website_DataUnit class attributes and methods

# website_DetailsUnit class attributes and methods
website_DetailsUnit_onlyDisplayWhenNotEmpty: Property = Property(name="onlyDisplayWhenNotEmpty", type=BooleanType)
website_DetailsUnit_omitFieldLabels: Property = Property(name="omitFieldLabels", type=BooleanType)
website_DetailsUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_DetailsUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_DetailsUnit.attributes={website_DetailsUnit_omitFieldLabels, website_DetailsUnit_onlyDisplayWhenNotEmpty, website_DetailsUnit_styleClass, website_DetailsUnit_contentClass}

# DataUnit class attributes and methods

# website_CreateUnit class attributes and methods
website_CreateUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_CreateUnit.attributes={website_CreateUnit_styleClass}

# EditUnit class attributes and methods

# website_CreateUpdateUnit class attributes and methods
website_CreateUpdateUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_CreateUpdateUnit_createUriElement: Property = Property(name="createUriElement", type=StringType)
website_CreateUpdateUnit_clearLabel: Property = Property(name="clearLabel", type=StringType)
website_CreateUpdateUnit.attributes={website_CreateUpdateUnit_styleClass, website_CreateUpdateUnit_createUriElement, website_CreateUpdateUnit_clearLabel}

# website_SearchUnit class attributes and methods
website_SearchUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_SearchUnit.attributes={website_SearchUnit_styleClass}

# ControlUnit class attributes and methods

# website_ImageUnit class attributes and methods
website_ImageUnit_missingImagePath: Property = Property(name="missingImagePath", type=StringType)
website_ImageUnit_showTime: Property = Property(name="showTime", type=IntegerType)
website_ImageUnit_transitionTime: Property = Property(name="transitionTime", type=IntegerType)
website_ImageUnit.attributes={website_ImageUnit_missingImagePath, website_ImageUnit_transitionTime, website_ImageUnit_showTime}

# website_FeaturePath class attributes and methods

# website_FeaturePathAttribute class attributes and methods
website_FeaturePathAttribute_name: Property = Property(name="name", type=StringType)
website_FeaturePathAttribute.attributes={website_FeaturePathAttribute_name}

# FeaturePath class attributes and methods

# website_FeaturePathAssociation class attributes and methods
website_FeaturePathAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
website_FeaturePathAssociation.attributes={website_FeaturePathAssociation_isSourceAssociation}

# website_IndexUnit class attributes and methods
website_IndexUnit_displayOption: Property = Property(name="displayOption", type=StringType)
website_IndexUnit_omitColumnLabels: Property = Property(name="omitColumnLabels", type=BooleanType)
website_IndexUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_IndexUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_IndexUnit_rowClasses: Property = Property(name="rowClasses", type=StringType)
website_IndexUnit.attributes={website_IndexUnit_styleClass, website_IndexUnit_rowClasses, website_IndexUnit_omitColumnLabels, website_IndexUnit_displayOption, website_IndexUnit_contentClass}

# CollectionUnit class attributes and methods

# website_ControlUnit class attributes and methods
website_ControlUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_ControlUnit_submitLabel: Property = Property(name="submitLabel", type=StringType)
website_ControlUnit_cancelLabel: Property = Property(name="cancelLabel", type=StringType)
website_ControlUnit.attributes={website_ControlUnit_cancelLabel, website_ControlUnit_submitLabel, website_ControlUnit_contentClass}

# ChildPath class attributes and methods

# website_ChildPathAssociation class attributes and methods
website_ChildPathAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
website_ChildPathAssociation.attributes={website_ChildPathAssociation_isSourceAssociation}

# website_ImageIndexUnit class attributes and methods
website_ImageIndexUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_ImageIndexUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_ImageIndexUnit.attributes={website_ImageIndexUnit_contentClass, website_ImageIndexUnit_styleClass}

# ImageUnit class attributes and methods

# website_SliderUnit class attributes and methods
website_SliderUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_SliderUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_SliderUnit.attributes={website_SliderUnit_styleClass, website_SliderUnit_contentClass}

# website_GalleryUnit class attributes and methods
website_GalleryUnit_styleClass: Property = Property(name="styleClass", type=StringType)
website_GalleryUnit_contentClass: Property = Property(name="contentClass", type=StringType)
website_GalleryUnit.attributes={website_GalleryUnit_styleClass, website_GalleryUnit_contentClass}

# website_ChildPathAttribute class attributes and methods
website_ChildPathAttribute_name: Property = Property(name="name", type=StringType)
website_ChildPathAttribute.attributes={website_ChildPathAttribute_name}

# website_AuthenticationUnit class attributes and methods

# AuthenticationUnit class attributes and methods

# website_InlineActionContainer class attributes and methods

# website_InlineAction class attributes and methods
website_InlineAction_disable: Property = Property(name="disable", type=BooleanType)
website_InlineAction_requiresRole: Property = Property(name="requiresRole", type=StringType)
website_InlineAction_header: Property = Property(name="header", type=StringType)
website_InlineAction_footer: Property = Property(name="footer", type=StringType)
website_InlineAction_headerClass: Property = Property(name="headerClass", type=StringType)
website_InlineAction_footerClass: Property = Property(name="footerClass", type=StringType)
website_InlineAction.attributes={website_InlineAction_requiresRole, website_InlineAction_disable, website_InlineAction_footer, website_InlineAction_footerClass, website_InlineAction_header, website_InlineAction_headerClass}

# website_DeleteAction class attributes and methods
website_DeleteAction_confirmMessage: Property = Property(name="confirmMessage", type=StringType)
website_DeleteAction_uriElement: Property = Property(name="uriElement", type=StringType)
website_DeleteAction.attributes={website_DeleteAction_confirmMessage, website_DeleteAction_uriElement}

# website_FeatureSupportAction class attributes and methods
website_FeatureSupportAction_confirmMessage: Property = Property(name="confirmMessage", type=StringType)
website_FeatureSupportAction_uriElement: Property = Property(name="uriElement", type=StringType)
website_FeatureSupportAction_fileExtension: Property = Property(name="fileExtension", type=StringType)
website_FeatureSupportAction.attributes={website_FeatureSupportAction_fileExtension, website_FeatureSupportAction_uriElement, website_FeatureSupportAction_confirmMessage}

# website_ModelReference class attributes and methods

# Path class attributes and methods

# website_FeatureReference class attributes and methods
website_FeatureReference_name: Property = Property(name="name", type=StringType)
website_FeatureReference.attributes={website_FeatureReference_name}

# website_RouteParameterReference class attributes and methods
website_RouteParameterReference_name: Property = Property(name="name", type=StringType)
website_RouteParameterReference.attributes={website_RouteParameterReference_name}

# website_ParameterReference class attributes and methods
website_ParameterReference_name: Property = Property(name="name", type=StringType)
website_ParameterReference.attributes={website_ParameterReference_name}

# website_CurrentUserReference class attributes and methods

# website_SelectAction class attributes and methods

# InlineAction class attributes and methods

# Relationships
classifiers1: BinaryAssociation = BinaryAssociation(
    name="classifiers1",
    ends={
        Property(name="website_Classifier", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel2", type=website_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services3: BinaryAssociation = BinaryAssociation(
    name="services3",
    ends={
        Property(name="website_Service", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel4", type=website_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
websiteProperties0: BinaryAssociation = BinaryAssociation(
    name="websiteProperties0",
    ends={
        Property(name="website_WebsiteProperties", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel", type=website_WebsiteProperties, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pages5: BinaryAssociation = BinaryAssociation(
    name="pages5",
    ends={
        Property(name="website_Page", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel6", type=website_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menus7: BinaryAssociation = BinaryAssociation(
    name="menus7",
    ends={
        Property(name="website_Menu", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel8", type=website_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowTypeCustomisation9: BinaryAssociation = BinaryAssociation(
    name="allowTypeCustomisation9",
    ends={
        Property(name="website_EntityOrView", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel10", type=website_EntityOrView, multiplicity=Multiplicity(0, 9999))
    }
)
imageManipulations11: BinaryAssociation = BinaryAssociation(
    name="imageManipulations11",
    ends={
        Property(name="website_ImageManipulation", type=website_WebGenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebGenModel12", type=website_ImageManipulation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authentication13: BinaryAssociation = BinaryAssociation(
    name="authentication13",
    ends={
        Property(name="Authentication", type=website_WebsiteProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="authenticates", type=website_Authentication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
registrationUnit24: BinaryAssociation = BinaryAssociation(
    name="registrationUnit24",
    ends={
        Property(name="website_RegistrationUnit", type=website_LocalAuthenticationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="website_LocalAuthenticationSystem25", type=website_RegistrationUnit, multiplicity=Multiplicity(0, 1))
    }
)
loginUnit26: BinaryAssociation = BinaryAssociation(
    name="loginUnit26",
    ends={
        Property(name="website_LoginUnit", type=website_LocalAuthenticationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="website_LocalAuthenticationSystem27", type=website_LoginUnit, multiplicity=Multiplicity(0, 1))
    }
)
sideMenu14: BinaryAssociation = BinaryAssociation(
    name="sideMenu14",
    ends={
        Property(name="website_Menu16", type=website_WebsiteProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="website_WebsiteProperties15", type=website_Menu, multiplicity=Multiplicity(0, 1))
    }
)
authenticates17: BinaryAssociation = BinaryAssociation(
    name="authenticates17",
    ends={
        Property(name="WebsiteProperties", type=website_Authentication, multiplicity=Multiplicity(1, 1)),
        Property(name="authentication", type=website_WebsiteProperties, multiplicity=Multiplicity(1, 1))
    }
)
user18: BinaryAssociation = BinaryAssociation(
    name="user18",
    ends={
        Property(name="website_EntityOrView19", type=website_Authentication, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Authentication", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
userKey20: BinaryAssociation = BinaryAssociation(
    name="userKey20",
    ends={
        Property(name="website_Attribute", type=website_Authentication, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Authentication21", type=website_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
authentication22: BinaryAssociation = BinaryAssociation(
    name="authentication22",
    ends={
        Property(name="website_EntityOrView23", type=website_LocalAuthenticationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="website_LocalAuthenticationSystem", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
labels40: BinaryAssociation = BinaryAssociation(
    name="labels40",
    ends={
        Property(name="ModelLabel", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="labelFor", type=website_ModelLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features41: BinaryAssociation = BinaryAssociation(
    name="features41",
    ends={
        Property(name="website_Feature43", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView42", type=website_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
forgottenPasswordUnit28: BinaryAssociation = BinaryAssociation(
    name="forgottenPasswordUnit28",
    ends={
        Property(name="website_ForgottenPasswordUnit", type=website_LocalAuthenticationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="website_LocalAuthenticationSystem29", type=website_ForgottenPasswordUnit, multiplicity=Multiplicity(0, 1))
    }
)
enumerations30: BinaryAssociation = BinaryAssociation(
    name="enumerations30",
    ends={
        Property(name="website_EnumerationLiteral", type=website_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EnumerationType", type=website_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys31: BinaryAssociation = BinaryAssociation(
    name="keys31",
    ends={
        Property(name="website_Feature", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView32", type=website_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
unique33: BinaryAssociation = BinaryAssociation(
    name="unique33",
    ends={
        Property(name="website_Feature35", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView34", type=website_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
containerUnique36: BinaryAssociation = BinaryAssociation(
    name="containerUnique36",
    ends={
        Property(name="website_Feature38", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView37", type=website_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
servedBy39: BinaryAssociation = BinaryAssociation(
    name="servedBy39",
    ends={
        Property(name="Service", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="serves", type=website_Service, multiplicity=Multiplicity(0, 9999))
    }
)
allFeatures44: BinaryAssociation = BinaryAssociation(
    name="allFeatures44",
    ends={
        Property(name="website_Feature46", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView45", type=website_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attributes47: BinaryAssociation = BinaryAssociation(
    name="attributes47",
    ends={
        Property(name="website_Attribute49", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView48", type=website_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
associations50: BinaryAssociation = BinaryAssociation(
    name="associations50",
    ends={
        Property(name="website_Association", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView51", type=website_Association, multiplicity=Multiplicity(0, 9999))
    }
)
allAssociations52: BinaryAssociation = BinaryAssociation(
    name="allAssociations52",
    ends={
        Property(name="website_Association54", type=website_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EntityOrView53", type=website_Association, multiplicity=Multiplicity(0, 9999))
    }
)
entityFeatures73: BinaryAssociation = BinaryAssociation(
    name="entityFeatures73",
    ends={
        Property(name="EntityFeature", type=website_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf74", type=website_EntityFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnds75: BinaryAssociation = BinaryAssociation(
    name="associationEnds75",
    ends={
        Property(name="EntityAssociation", type=website_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="targetEntity", type=website_EntityAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue55: BinaryAssociation = BinaryAssociation(
    name="defaultValue55",
    ends={
        Property(name="website_Expression", type=website_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Attribute56", type=website_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
encapsulatedBy57: BinaryAssociation = BinaryAssociation(
    name="encapsulatedBy57",
    ends={
        Property(name="EncapsulatedAssociation", type=website_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
sourceEntityX58: BinaryAssociation = BinaryAssociation(
    name="sourceEntityX58",
    ends={
        Property(name="website_EntityOrView60", type=website_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Association59", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
targetEntityX61: BinaryAssociation = BinaryAssociation(
    name="targetEntityX61",
    ends={
        Property(name="website_EntityOrView63", type=website_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Association62", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
labelFor64: BinaryAssociation = BinaryAssociation(
    name="labelFor64",
    ends={
        Property(name="EntityOrView", type=website_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
features65: BinaryAssociation = BinaryAssociation(
    name="features65",
    ends={
        Property(name="ModelLabelFeature", type=website_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf", type=website_ModelLabelFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partOf66: BinaryAssociation = BinaryAssociation(
    name="partOf66",
    ends={
        Property(name="ModelLabel67", type=website_ModelLabelFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=website_ModelLabel, multiplicity=Multiplicity(1, 1))
    }
)
attribute68: BinaryAssociation = BinaryAssociation(
    name="attribute68",
    ends={
        Property(name="website_Attribute69", type=website_ModelLabelAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ModelLabelAttribute", type=website_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
association70: BinaryAssociation = BinaryAssociation(
    name="association70",
    ends={
        Property(name="website_EntityAssociation", type=website_ModelLabelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ModelLabelAssociation", type=website_EntityAssociation, multiplicity=Multiplicity(1, 1))
    }
)
dynamicLabel71: BinaryAssociation = BinaryAssociation(
    name="dynamicLabel71",
    ends={
        Property(name="website_ModelLabel", type=website_ModelLabelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ModelLabelAssociation72", type=website_ModelLabel, multiplicity=Multiplicity(0, 1))
    }
)
partOf76: BinaryAssociation = BinaryAssociation(
    name="partOf76",
    ends={
        Property(name="Entity", type=website_EntityFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="entityFeatures", type=website_Entity, multiplicity=Multiplicity(1, 1))
    }
)
dataType77: BinaryAssociation = BinaryAssociation(
    name="dataType77",
    ends={
        Property(name="website_DataType", type=website_DataTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DataTypeAttribute", type=website_DataType, multiplicity=Multiplicity(1, 1))
    }
)
sourceFeature84: BinaryAssociation = BinaryAssociation(
    name="sourceFeature84",
    ends={
        Property(name="website_EntityFeature", type=website_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="website_AssociationKey", type=website_EntityFeature, multiplicity=Multiplicity(1, 1))
    }
)
targetFeature85: BinaryAssociation = BinaryAssociation(
    name="targetFeature85",
    ends={
        Property(name="website_EntityFeature87", type=website_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="website_AssociationKey86", type=website_EntityFeature, multiplicity=Multiplicity(0, 1))
    }
)
uploadPath78: BinaryAssociation = BinaryAssociation(
    name="uploadPath78",
    ends={
        Property(name="website_PathElement", type=website_ResourceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ResourceAttribute", type=website_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys79: BinaryAssociation = BinaryAssociation(
    name="keys79",
    ends={
        Property(name="AssociationKey", type=website_EntityAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="keyFor", type=website_AssociationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetEntity80: BinaryAssociation = BinaryAssociation(
    name="targetEntity80",
    ends={
        Property(name="Entity81", type=website_EntityAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnds", type=website_Entity, multiplicity=Multiplicity(1, 1))
    }
)
keyFor82: BinaryAssociation = BinaryAssociation(
    name="keyFor82",
    ends={
        Property(name="EntityAssociation83", type=website_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=website_EntityAssociation, multiplicity=Multiplicity(1, 1))
    }
)
targetEntity100: BinaryAssociation = BinaryAssociation(
    name="targetEntity100",
    ends={
        Property(name="website_Entity102", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EncapsulatedAssociation101", type=website_Entity, multiplicity=Multiplicity(1, 1))
    }
)
encapsulates88: BinaryAssociation = BinaryAssociation(
    name="encapsulates88",
    ends={
        Property(name="website_EntityOrView89", type=website_View, multiplicity=Multiplicity(1, 1)),
        Property(name="website_View", type=website_EntityOrView, multiplicity=Multiplicity(0, 9999))
    }
)
viewFeatures90: BinaryAssociation = BinaryAssociation(
    name="viewFeatures90",
    ends={
        Property(name="ViewFeature", type=website_View, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf91", type=website_ViewFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partOf92: BinaryAssociation = BinaryAssociation(
    name="partOf92",
    ends={
        Property(name="View", type=website_ViewFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="viewFeatures", type=website_View, multiplicity=Multiplicity(1, 1))
    }
)
attribute93: BinaryAssociation = BinaryAssociation(
    name="attribute93",
    ends={
        Property(name="website_Attribute94", type=website_EncapsulatedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EncapsulatedAttribute", type=website_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
association95: BinaryAssociation = BinaryAssociation(
    name="association95",
    ends={
        Property(name="Association", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatedBy", type=website_Association, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedTarget97: BinaryAssociation = BinaryAssociation(
    name="encapsulatedTarget97",
    ends={
        Property(name="website_EncapsulatedAssociation", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EncapsulatedAssociation96", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
sourceEntity98: BinaryAssociation = BinaryAssociation(
    name="sourceEntity98",
    ends={
        Property(name="website_Entity", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EncapsulatedAssociation99", type=website_Entity, multiplicity=Multiplicity(1, 1))
    }
)
uses124: BinaryAssociation = BinaryAssociation(
    name="uses124",
    ends={
        Property(name="website_Service126", type=website_BusinessOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_BusinessOperation125", type=website_Service, multiplicity=Multiplicity(0, 9999))
    }
)
opposite103: BinaryAssociation = BinaryAssociation(
    name="opposite103",
    ends={
        Property(name="website_EncapsulatedAssociation104", type=website_ViewAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ViewAssociation", type=website_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1))
    }
)
serves105: BinaryAssociation = BinaryAssociation(
    name="serves105",
    ends={
        Property(name="EntityOrView106", type=website_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servedBy", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
selections107: BinaryAssociation = BinaryAssociation(
    name="selections107",
    ends={
        Property(name="Selection", type=website_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="usedBy", type=website_Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations108: BinaryAssociation = BinaryAssociation(
    name="operations108",
    ends={
        Property(name="website_BusinessOperation", type=website_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Service109", type=website_BusinessOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedBy110: BinaryAssociation = BinaryAssociation(
    name="usedBy110",
    ends={
        Property(name="Service111", type=website_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="selections", type=website_Service, multiplicity=Multiplicity(1, 1))
    }
)
fields112: BinaryAssociation = BinaryAssociation(
    name="fields112",
    ends={
        Property(name="website_Feature113", type=website_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Selection", type=website_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
parameters114: BinaryAssociation = BinaryAssociation(
    name="parameters114",
    ends={
        Property(name="SelectionParameter", type=website_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="formalFor", type=website_SelectionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joins115: BinaryAssociation = BinaryAssociation(
    name="joins115",
    ends={
        Property(name="website_Association117", type=website_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Selection116", type=website_Association, multiplicity=Multiplicity(0, 9999))
    }
)
filter118: BinaryAssociation = BinaryAssociation(
    name="filter118",
    ends={
        Property(name="website_Predicate", type=website_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Selection119", type=website_Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering120: BinaryAssociation = BinaryAssociation(
    name="ordering120",
    ends={
        Property(name="website_Order", type=website_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Selection121", type=website_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalFor122: BinaryAssociation = BinaryAssociation(
    name="formalFor122",
    ends={
        Property(name="Selection123", type=website_SelectionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=website_Selection, multiplicity=Multiplicity(1, 1))
    }
)
entries136: BinaryAssociation = BinaryAssociation(
    name="entries136",
    ends={
        Property(name="MenuEntry", type=website_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf137", type=website_MenuEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters127: BinaryAssociation = BinaryAssociation(
    name="filters127",
    ends={
        Property(name="website_ImageFilter", type=website_ImageManipulation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ImageManipulation128", type=website_ImageFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentPage129: BinaryAssociation = BinaryAssociation(
    name="parentPage129",
    ends={
        Property(name="website_PageLink", type=website_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Page130", type=website_PageLink, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childPages131: BinaryAssociation = BinaryAssociation(
    name="childPages131",
    ends={
        Property(name="PageLink", type=website_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="targetPage", type=website_PageLink, multiplicity=Multiplicity(0, 9999))
    }
)
sideMenu132: BinaryAssociation = BinaryAssociation(
    name="sideMenu132",
    ends={
        Property(name="website_Menu134", type=website_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Page133", type=website_Menu, multiplicity=Multiplicity(0, 1))
    }
)
targetPage135: BinaryAssociation = BinaryAssociation(
    name="targetPage135",
    ends={
        Property(name="Page", type=website_PageLink, multiplicity=Multiplicity(1, 1)),
        Property(name="childPages", type=website_Page, multiplicity=Multiplicity(1, 1))
    }
)
formal155: BinaryAssociation = BinaryAssociation(
    name="formal155",
    ends={
        Property(name="website_FilterParameter", type=website_SelectionParameter, multiplicity=Multiplicity(0, 1)),
        Property(name="website_SelectionParameter", type=website_FilterParameter, multiplicity=Multiplicity(1, 1))
    }
)
dataType156: BinaryAssociation = BinaryAssociation(
    name="dataType156",
    ends={
        Property(name="website_DataType158", type=website_FilterParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="website_FilterParameter157", type=website_DataType, multiplicity=Multiplicity(0, 1))
    }
)
partOf138: BinaryAssociation = BinaryAssociation(
    name="partOf138",
    ends={
        Property(name="Menu", type=website_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=website_Menu, multiplicity=Multiplicity(1, 1))
    }
)
destination139: BinaryAssociation = BinaryAssociation(
    name="destination139",
    ends={
        Property(name="website_ContentUnit", type=website_ActionMenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ActionMenuEntry", type=website_ContentUnit, multiplicity=Multiplicity(1, 1))
    }
)
query140: BinaryAssociation = BinaryAssociation(
    name="query140",
    ends={
        Property(name="website_Query", type=website_ActionMenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ActionMenuEntry141", type=website_Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityOrView142: BinaryAssociation = BinaryAssociation(
    name="entityOrView142",
    ends={
        Property(name="website_EntityOrView143", type=website_DynamicMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DynamicMenu", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
selection144: BinaryAssociation = BinaryAssociation(
    name="selection144",
    ends={
        Property(name="website_Selection146", type=website_DynamicMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DynamicMenu145", type=website_Selection, multiplicity=Multiplicity(1, 1))
    }
)
title147: BinaryAssociation = BinaryAssociation(
    name="title147",
    ends={
        Property(name="website_Label", type=website_DynamicMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DynamicMenu148", type=website_Label, multiplicity=Multiplicity(0, 1))
    }
)
parameters149: BinaryAssociation = BinaryAssociation(
    name="parameters149",
    ends={
        Property(name="FilterParameter", type=website_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf150", type=website_FilterParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection151: BinaryAssociation = BinaryAssociation(
    name="selection151",
    ends={
        Property(name="website_Selection152", type=website_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Filter", type=website_Selection, multiplicity=Multiplicity(0, 1))
    }
)
partOf153: BinaryAssociation = BinaryAssociation(
    name="partOf153",
    ends={
        Property(name="Filter", type=website_FilterParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters154", type=website_Filter, multiplicity=Multiplicity(0, 1))
    }
)
displayFields171: BinaryAssociation = BinaryAssociation(
    name="displayFields171",
    ends={
        Property(name="UnitField", type=website_DynamicUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="displayedOn172", type=website_UnitField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportActions173: BinaryAssociation = BinaryAssociation(
    name="supportActions173",
    ends={
        Property(name="website_UnitSupportAction", type=website_DynamicUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DynamicUnit174", type=website_UnitSupportAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter159: BinaryAssociation = BinaryAssociation(
    name="filter159",
    ends={
        Property(name="website_Filter161", type=website_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Query160", type=website_Filter, multiplicity=Multiplicity(1, 1))
    }
)
parameters162: BinaryAssociation = BinaryAssociation(
    name="parameters162",
    ends={
        Property(name="website_QueryParameter", type=website_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="website_Query163", type=website_QueryParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formal164: BinaryAssociation = BinaryAssociation(
    name="formal164",
    ends={
        Property(name="website_FilterParameter166", type=website_QueryParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="website_QueryParameter165", type=website_FilterParameter, multiplicity=Multiplicity(1, 1))
    }
)
units167: BinaryAssociation = BinaryAssociation(
    name="units167",
    ends={
        Property(name="ContentUnit", type=website_UnitContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="displayedOn", type=website_ContentUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
displayedOn168: BinaryAssociation = BinaryAssociation(
    name="displayedOn168",
    ends={
        Property(name="UnitContainer", type=website_ContentUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="units", type=website_UnitContainer, multiplicity=Multiplicity(1, 1))
    }
)
entities169: BinaryAssociation = BinaryAssociation(
    name="entities169",
    ends={
        Property(name="website_EntityOrView170", type=website_DynamicUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DynamicUnit", type=website_EntityOrView, multiplicity=Multiplicity(0, 9999))
    }
)
displayedOn175: BinaryAssociation = BinaryAssociation(
    name="displayedOn175",
    ends={
        Property(name="DynamicUnit", type=website_UnitField, multiplicity=Multiplicity(1, 1)),
        Property(name="displayFields", type=website_DynamicUnit, multiplicity=Multiplicity(1, 1))
    }
)
attribute178: BinaryAssociation = BinaryAssociation(
    name="attribute178",
    ends={
        Property(name="website_Attribute179", type=website_UnitElement, multiplicity=Multiplicity(1, 1)),
        Property(name="website_UnitElement", type=website_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue180: BinaryAssociation = BinaryAssociation(
    name="defaultValue180",
    ends={
        Property(name="website_Expression182", type=website_UnitElement, multiplicity=Multiplicity(1, 1)),
        Property(name="website_UnitElement181", type=website_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceEntity183: BinaryAssociation = BinaryAssociation(
    name="sourceEntity183",
    ends={
        Property(name="website_EntityOrView184", type=website_UnitAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_UnitAssociation", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
targetEntity185: BinaryAssociation = BinaryAssociation(
    name="targetEntity185",
    ends={
        Property(name="website_EntityOrView187", type=website_UnitAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_UnitAssociation186", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
selection188: BinaryAssociation = BinaryAssociation(
    name="selection188",
    ends={
        Property(name="website_Selection190", type=website_UnitAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_UnitAssociation189", type=website_Selection, multiplicity=Multiplicity(0, 1))
    }
)
forcedValue176: BinaryAssociation = BinaryAssociation(
    name="forcedValue176",
    ends={
        Property(name="website_Expression177", type=website_UnitFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="website_UnitFeature", type=website_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataType199: BinaryAssociation = BinaryAssociation(
    name="dataType199",
    ends={
        Property(name="website_DataType200", type=website_DataTypeField, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DataTypeField", type=website_DataType, multiplicity=Multiplicity(1, 1))
    }
)
association191: BinaryAssociation = BinaryAssociation(
    name="association191",
    ends={
        Property(name="website_Association192", type=website_AssociationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_AssociationReference", type=website_Association, multiplicity=Multiplicity(1, 1))
    }
)
valueDisplay193: BinaryAssociation = BinaryAssociation(
    name="valueDisplay193",
    ends={
        Property(name="website_Label195", type=website_AssociationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_AssociationReference194", type=website_Label, multiplicity=Multiplicity(0, 1))
    }
)
childFeature196: BinaryAssociation = BinaryAssociation(
    name="childFeature196",
    ends={
        Property(name="ChildPath", type=website_AssociationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf197", type=website_ChildPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mustMatch198: BinaryAssociation = BinaryAssociation(
    name="mustMatch198",
    ends={
        Property(name="website_UnitField", type=website_InterfaceField, multiplicity=Multiplicity(1, 1)),
        Property(name="website_InterfaceField", type=website_UnitField, multiplicity=Multiplicity(0, 1))
    }
)
contentType205: BinaryAssociation = BinaryAssociation(
    name="contentType205",
    ends={
        Property(name="website_EntityOrView206", type=website_CollectionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_CollectionUnit", type=website_EntityOrView, multiplicity=Multiplicity(1, 9999))
    }
)
containingFeature207: BinaryAssociation = BinaryAssociation(
    name="containingFeature207",
    ends={
        Property(name="website_Feature209", type=website_CollectionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_CollectionUnit208", type=website_Feature, multiplicity=Multiplicity(0, 1))
    }
)
selection210: BinaryAssociation = BinaryAssociation(
    name="selection210",
    ends={
        Property(name="website_Selection212", type=website_CollectionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_CollectionUnit211", type=website_Selection, multiplicity=Multiplicity(0, 1))
    }
)
filters213: BinaryAssociation = BinaryAssociation(
    name="filters213",
    ends={
        Property(name="website_Filter215", type=website_CollectionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_CollectionUnit214", type=website_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pagination216: BinaryAssociation = BinaryAssociation(
    name="pagination216",
    ends={
        Property(name="website_Filter218", type=website_CollectionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_CollectionUnit217", type=website_Filter, multiplicity=Multiplicity(0, 1))
    }
)
defaultSelection219: BinaryAssociation = BinaryAssociation(
    name="defaultSelection219",
    ends={
        Property(name="website_Selection220", type=website_EditUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EditUnit", type=website_Selection, multiplicity=Multiplicity(0, 1))
    }
)
title221: BinaryAssociation = BinaryAssociation(
    name="title221",
    ends={
        Property(name="website_Label223", type=website_EditUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EditUnit222", type=website_Label, multiplicity=Multiplicity(0, 1))
    }
)
enableWhen224: BinaryAssociation = BinaryAssociation(
    name="enableWhen224",
    ends={
        Property(name="website_Predicate226", type=website_EditUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EditUnit225", type=website_Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectionType201: BinaryAssociation = BinaryAssociation(
    name="selectionType201",
    ends={
        Property(name="website_EntityOrView202", type=website_SelectableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_SelectableUnit", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
contentType203: BinaryAssociation = BinaryAssociation(
    name="contentType203",
    ends={
        Property(name="website_EntityOrView204", type=website_SingletonUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_SingletonUnit", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
location233: BinaryAssociation = BinaryAssociation(
    name="location233",
    ends={
        Property(name="website_LocationAttribute", type=website_MapUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_MapUnit", type=website_LocationAttribute, multiplicity=Multiplicity(1, 1))
    }
)
placeName234: BinaryAssociation = BinaryAssociation(
    name="placeName234",
    ends={
        Property(name="website_Attribute236", type=website_MapUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_MapUnit235", type=website_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
defaultSelection237: BinaryAssociation = BinaryAssociation(
    name="defaultSelection237",
    ends={
        Property(name="website_Selection238", type=website_DataUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DataUnit", type=website_Selection, multiplicity=Multiplicity(0, 1))
    }
)
title239: BinaryAssociation = BinaryAssociation(
    name="title239",
    ends={
        Property(name="website_Label241", type=website_DataUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DataUnit240", type=website_Label, multiplicity=Multiplicity(0, 1))
    }
)
confirmDestination227: BinaryAssociation = BinaryAssociation(
    name="confirmDestination227",
    ends={
        Property(name="website_Page229", type=website_EditUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EditUnit228", type=website_Page, multiplicity=Multiplicity(0, 1))
    }
)
cancelDestination230: BinaryAssociation = BinaryAssociation(
    name="cancelDestination230",
    ends={
        Property(name="website_Page232", type=website_EditUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_EditUnit231", type=website_Page, multiplicity=Multiplicity(0, 1))
    }
)
resultsDestination244: BinaryAssociation = BinaryAssociation(
    name="resultsDestination244",
    ends={
        Property(name="website_IndexUnit", type=website_SearchUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_SearchUnit", type=website_IndexUnit, multiplicity=Multiplicity(1, 1))
    }
)
defaultSelection245: BinaryAssociation = BinaryAssociation(
    name="defaultSelection245",
    ends={
        Property(name="website_Selection246", type=website_ImageUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ImageUnit", type=website_Selection, multiplicity=Multiplicity(0, 1))
    }
)
imagePathFeature247: BinaryAssociation = BinaryAssociation(
    name="imagePathFeature247",
    ends={
        Property(name="website_FeaturePath", type=website_ImageUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ImageUnit248", type=website_FeaturePath, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
titleFeature249: BinaryAssociation = BinaryAssociation(
    name="titleFeature249",
    ends={
        Property(name="website_FeaturePath251", type=website_ImageUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ImageUnit250", type=website_FeaturePath, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imageFilter252: BinaryAssociation = BinaryAssociation(
    name="imageFilter252",
    ends={
        Property(name="website_ImageManipulation254", type=website_ImageUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ImageUnit253", type=website_ImageManipulation, multiplicity=Multiplicity(1, 1))
    }
)
attribute255: BinaryAssociation = BinaryAssociation(
    name="attribute255",
    ends={
        Property(name="website_Attribute256", type=website_FeaturePathAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_FeaturePathAttribute", type=website_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
cancelDestination242: BinaryAssociation = BinaryAssociation(
    name="cancelDestination242",
    ends={
        Property(name="website_Page243", type=website_ControlUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ControlUnit", type=website_Page, multiplicity=Multiplicity(0, 1))
    }
)
attribute263: BinaryAssociation = BinaryAssociation(
    name="attribute263",
    ends={
        Property(name="website_Attribute264", type=website_ChildPathAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ChildPathAttribute", type=website_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
sourceEntity265: BinaryAssociation = BinaryAssociation(
    name="sourceEntity265",
    ends={
        Property(name="website_EntityOrView266", type=website_ChildPathAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ChildPathAssociation", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
targetEntity267: BinaryAssociation = BinaryAssociation(
    name="targetEntity267",
    ends={
        Property(name="website_EntityOrView269", type=website_ChildPathAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ChildPathAssociation268", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
sourceEntity257: BinaryAssociation = BinaryAssociation(
    name="sourceEntity257",
    ends={
        Property(name="website_EntityOrView258", type=website_FeaturePathAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_FeaturePathAssociation", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
targetEntity259: BinaryAssociation = BinaryAssociation(
    name="targetEntity259",
    ends={
        Property(name="website_EntityOrView261", type=website_FeaturePathAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="website_FeaturePathAssociation260", type=website_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
partOf262: BinaryAssociation = BinaryAssociation(
    name="partOf262",
    ends={
        Property(name="AssociationReference", type=website_ChildPath, multiplicity=Multiplicity(1, 1)),
        Property(name="childFeature", type=website_AssociationReference, multiplicity=Multiplicity(0, 1))
    }
)
actions272: BinaryAssociation = BinaryAssociation(
    name="actions272",
    ends={
        Property(name="InlineAction", type=website_InlineActionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="usedBy273", type=website_InlineAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedBy274: BinaryAssociation = BinaryAssociation(
    name="usedBy274",
    ends={
        Property(name="InlineActionContainer", type=website_InlineAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions", type=website_InlineActionContainer, multiplicity=Multiplicity(1, 1))
    }
)
enableWhen275: BinaryAssociation = BinaryAssociation(
    name="enableWhen275",
    ends={
        Property(name="website_Predicate276", type=website_InlineAction, multiplicity=Multiplicity(1, 1)),
        Property(name="website_InlineAction", type=website_Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayWhen277: BinaryAssociation = BinaryAssociation(
    name="displayWhen277",
    ends={
        Property(name="website_Predicate279", type=website_InlineAction, multiplicity=Multiplicity(1, 1)),
        Property(name="website_InlineAction278", type=website_Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fullSizeFilter270: BinaryAssociation = BinaryAssociation(
    name="fullSizeFilter270",
    ends={
        Property(name="website_ImageManipulation271", type=website_GalleryUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="website_GalleryUnit", type=website_ImageManipulation, multiplicity=Multiplicity(0, 1))
    }
)
destination282: BinaryAssociation = BinaryAssociation(
    name="destination282",
    ends={
        Property(name="website_Page283", type=website_DeleteAction, multiplicity=Multiplicity(1, 1)),
        Property(name="website_DeleteAction", type=website_Page, multiplicity=Multiplicity(0, 1))
    }
)
operation284: BinaryAssociation = BinaryAssociation(
    name="operation284",
    ends={
        Property(name="website_BusinessOperation285", type=website_FeatureSupportAction, multiplicity=Multiplicity(1, 1)),
        Property(name="website_FeatureSupportAction", type=website_BusinessOperation, multiplicity=Multiplicity(1, 1))
    }
)
unit286: BinaryAssociation = BinaryAssociation(
    name="unit286",
    ends={
        Property(name="website_DynamicUnit287", type=website_ModelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ModelReference", type=website_DynamicUnit, multiplicity=Multiplicity(1, 1))
    }
)
feature288: BinaryAssociation = BinaryAssociation(
    name="feature288",
    ends={
        Property(name="website_Feature289", type=website_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_FeatureReference", type=website_Feature, multiplicity=Multiplicity(1, 1))
    }
)
parameter290: BinaryAssociation = BinaryAssociation(
    name="parameter290",
    ends={
        Property(name="website_Attribute291", type=website_RouteParameterReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_RouteParameterReference", type=website_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
parameter292: BinaryAssociation = BinaryAssociation(
    name="parameter292",
    ends={
        Property(name="website_SelectionParameter293", type=website_ParameterReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_ParameterReference", type=website_SelectionParameter, multiplicity=Multiplicity(1, 1))
    }
)
userModel294: BinaryAssociation = BinaryAssociation(
    name="userModel294",
    ends={
        Property(name="website_EntityOrView295", type=website_CurrentUserReference, multiplicity=Multiplicity(1, 1)),
        Property(name="website_CurrentUserReference", type=website_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
target280: BinaryAssociation = BinaryAssociation(
    name="target280",
    ends={
        Property(name="website_SelectableUnit281", type=website_SelectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="website_SelectAction", type=website_SelectableUnit, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_website_LocalAuthenticationSystem_Authentication = Generalization(general=Authentication, specific=website_LocalAuthenticationSystem)
gen_website_CasAuthentication_Authentication = Generalization(general=Authentication, specific=website_CasAuthentication)
gen_website_NamedDisplayElement_NamedElement = Generalization(general=NamedElement, specific=website_NamedDisplayElement)
gen_website_Classifier_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_Classifier)
gen_website_DataType_Classifier = Generalization(general=Classifier, specific=website_DataType)
gen_website_EnumerationType_DataType = Generalization(general=DataType, specific=website_EnumerationType)
gen_website_EnumerationLiteral_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_EnumerationLiteral)
gen_website_EntityOrView_Classifier = Generalization(general=Classifier, specific=website_EntityOrView)
gen_website_Attribute_Feature = Generalization(general=Feature, specific=website_Attribute)
gen_website_Attribute_Label = Generalization(general=Label, specific=website_Attribute)
gen_website_Association_Feature = Generalization(general=Feature, specific=website_Association)
gen_website_ModelLabel_NamedElement = Generalization(general=NamedElement, specific=website_ModelLabel)
gen_website_ModelLabel_Label = Generalization(general=Label, specific=website_ModelLabel)
gen_website_ModelLabelAttribute_ModelLabelFeature = Generalization(general=ModelLabelFeature, specific=website_ModelLabelAttribute)
gen_website_ModelLabelAssociation_ModelLabelFeature = Generalization(general=ModelLabelFeature, specific=website_ModelLabelAssociation)
gen_website_Entity_EntityOrView = Generalization(general=EntityOrView, specific=website_Entity)
gen_website_ResourceAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=website_ResourceAttribute)
gen_website_EntityFeature_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_EntityFeature)
gen_website_EntityFeature_Feature = Generalization(general=Feature, specific=website_EntityFeature)
gen_website_EntityAttribute_EntityFeature = Generalization(general=EntityFeature, specific=website_EntityAttribute)
gen_website_EntityAttribute_Attribute = Generalization(general=Attribute, specific=website_EntityAttribute)
gen_website_DataTypeAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=website_DataTypeAttribute)
gen_website_DateAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=website_DateAttribute)
gen_website_UrlAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=website_UrlAttribute)
gen_website_StaticPathElement_PathElement = Generalization(general=PathElement, specific=website_StaticPathElement)
gen_website_DatePathElement_PathElement = Generalization(general=PathElement, specific=website_DatePathElement)
gen_website_FileAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=website_FileAttribute)
gen_website_ImageAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=website_ImageAttribute)
gen_website_LocationAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=website_LocationAttribute)
gen_website_EntityAssociation_EntityFeature = Generalization(general=EntityFeature, specific=website_EntityAssociation)
gen_website_EntityAssociation_Association = Generalization(general=Association, specific=website_EntityAssociation)
gen_website_AssociationWithoutContainment_EntityAssociation = Generalization(general=EntityAssociation, specific=website_AssociationWithoutContainment)
gen_website_AssociationWithContainment_EntityAssociation = Generalization(general=EntityAssociation, specific=website_AssociationWithContainment)
gen_website_View_EntityOrView = Generalization(general=EntityOrView, specific=website_View)
gen_website_ViewFeature_Feature = Generalization(general=Feature, specific=website_ViewFeature)
gen_website_EncapsulatedFeature_ViewFeature = Generalization(general=ViewFeature, specific=website_EncapsulatedFeature)
gen_website_EncapsulatedAttribute_EncapsulatedFeature = Generalization(general=EncapsulatedFeature, specific=website_EncapsulatedAttribute)
gen_website_EncapsulatedAttribute_Attribute = Generalization(general=Attribute, specific=website_EncapsulatedAttribute)
gen_website_EncapsulatedAssociation_EncapsulatedFeature = Generalization(general=EncapsulatedFeature, specific=website_EncapsulatedAssociation)
gen_website_EncapsulatedAssociation_Association = Generalization(general=Association, specific=website_EncapsulatedAssociation)
gen_website_BusinessOperation_NamedElement = Generalization(general=NamedElement, specific=website_BusinessOperation)
gen_website_ViewAssociation_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_ViewAssociation)
gen_website_ViewAssociation_ViewFeature = Generalization(general=ViewFeature, specific=website_ViewAssociation)
gen_website_ViewAssociation_Association = Generalization(general=Association, specific=website_ViewAssociation)
gen_website_Service_NamedElement = Generalization(general=NamedElement, specific=website_Service)
gen_website_Selection_NamedElement = Generalization(general=NamedElement, specific=website_Selection)
gen_website_SelectionParameter_NamedElement = Generalization(general=NamedElement, specific=website_SelectionParameter)
gen_website_ImageManipulation_NamedElement = Generalization(general=NamedElement, specific=website_ImageManipulation)
gen_website_ThumbnailFilter_ImageFilter = Generalization(general=ImageFilter, specific=website_ThumbnailFilter)
gen_website_Page_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_Page)
gen_website_Page_UnitContainer = Generalization(general=UnitContainer, specific=website_Page)
gen_website_Menu_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_Menu)
gen_website_StaticMenu_Menu = Generalization(general=Menu, specific=website_StaticMenu)
gen_website_ActionMenuEntry_MenuEntry = Generalization(general=MenuEntry, specific=website_ActionMenuEntry)
gen_website_ActionMenuEntry_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_ActionMenuEntry)
gen_website_EditStaticTextMenuEntry_MenuEntry = Generalization(general=MenuEntry, specific=website_EditStaticTextMenuEntry)
gen_website_EditStaticTextMenuEntry_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_EditStaticTextMenuEntry)
gen_website_DynamicMenu_Menu = Generalization(general=Menu, specific=website_DynamicMenu)
gen_website_MenuFeature_MenuEntry = Generalization(general=MenuEntry, specific=website_MenuFeature)
gen_website_Filter_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_Filter)
gen_website_FilterParameter_NamedElement = Generalization(general=NamedElement, specific=website_FilterParameter)
gen_website_ContentUnit_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_ContentUnit)
gen_website_StaticUnit_ContentUnit = Generalization(general=ContentUnit, specific=website_StaticUnit)
gen_website_CreateSitemapUnit_ContentUnit = Generalization(general=ContentUnit, specific=website_CreateSitemapUnit)
gen_website_DynamicUnit_ContentUnit = Generalization(general=ContentUnit, specific=website_DynamicUnit)
gen_website_UnitFeature_UnitField = Generalization(general=UnitField, specific=website_UnitFeature)
gen_website_UnitFeature_InlineActionContainer = Generalization(general=InlineActionContainer, specific=website_UnitFeature)
gen_website_UnitAssociation_UnitFeature = Generalization(general=UnitFeature, specific=website_UnitAssociation)
gen_website_UnitAssociation_UnitContainer = Generalization(general=UnitContainer, specific=website_UnitAssociation)
gen_website_UnitAssociation_AssociationReference = Generalization(general=AssociationReference, specific=website_UnitAssociation)
gen_website_UnitElement_UnitFeature = Generalization(general=UnitFeature, specific=website_UnitElement)
gen_website_DataTypeField_InterfaceField = Generalization(general=InterfaceField, specific=website_DataTypeField)
gen_website_DateField_InterfaceField = Generalization(general=InterfaceField, specific=website_DateField)
gen_website_CaptchaField_InterfaceField = Generalization(general=InterfaceField, specific=website_CaptchaField)
gen_website_UnitSupportAction_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_UnitSupportAction)
gen_website_InterfaceField_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_InterfaceField)
gen_website_InterfaceField_UnitField = Generalization(general=UnitField, specific=website_InterfaceField)
gen_website_CollectionUnit_SelectableUnit = Generalization(general=SelectableUnit, specific=website_CollectionUnit)
gen_website_EditUnit_DynamicUnit = Generalization(general=DynamicUnit, specific=website_EditUnit)
gen_website_EditUnit_SingletonUnit = Generalization(general=SingletonUnit, specific=website_EditUnit)
gen_website_UpdateUnit_EditUnit = Generalization(general=EditUnit, specific=website_UpdateUnit)
gen_website_UpdateUnit_SelectableUnit = Generalization(general=SelectableUnit, specific=website_UpdateUnit)
gen_website_MapUnit_EditUnit = Generalization(general=EditUnit, specific=website_MapUnit)
gen_website_MapUnit_SelectableUnit = Generalization(general=SelectableUnit, specific=website_MapUnit)
gen_website_DataUnit_DynamicUnit = Generalization(general=DynamicUnit, specific=website_DataUnit)
gen_website_DetailsUnit_DataUnit = Generalization(general=DataUnit, specific=website_DetailsUnit)
gen_website_DetailsUnit_SingletonUnit = Generalization(general=SingletonUnit, specific=website_DetailsUnit)
gen_website_DetailsUnit_SelectableUnit = Generalization(general=SelectableUnit, specific=website_DetailsUnit)
gen_website_CreateUnit_EditUnit = Generalization(general=EditUnit, specific=website_CreateUnit)
gen_website_CreateUpdateUnit_EditUnit = Generalization(general=EditUnit, specific=website_CreateUpdateUnit)
gen_website_CreateUpdateUnit_SelectableUnit = Generalization(general=SelectableUnit, specific=website_CreateUpdateUnit)
gen_website_SearchUnit_ControlUnit = Generalization(general=ControlUnit, specific=website_SearchUnit)
gen_website_ImageUnit_DynamicUnit = Generalization(general=DynamicUnit, specific=website_ImageUnit)
gen_website_ImageUnit_CollectionUnit = Generalization(general=CollectionUnit, specific=website_ImageUnit)
gen_website_FeaturePathAttribute_FeaturePath = Generalization(general=FeaturePath, specific=website_FeaturePathAttribute)
gen_website_IndexUnit_DataUnit = Generalization(general=DataUnit, specific=website_IndexUnit)
gen_website_IndexUnit_CollectionUnit = Generalization(general=CollectionUnit, specific=website_IndexUnit)
gen_website_IndexUnit_InlineActionContainer = Generalization(general=InlineActionContainer, specific=website_IndexUnit)
gen_website_ControlUnit_DynamicUnit = Generalization(general=DynamicUnit, specific=website_ControlUnit)
gen_website_ChildPathAttribute_ChildPath = Generalization(general=ChildPath, specific=website_ChildPathAttribute)
gen_website_ChildPathAssociation_ChildPath = Generalization(general=ChildPath, specific=website_ChildPathAssociation)
gen_website_ChildPathAssociation_AssociationReference = Generalization(general=AssociationReference, specific=website_ChildPathAssociation)
gen_website_ImageIndexUnit_ImageUnit = Generalization(general=ImageUnit, specific=website_ImageIndexUnit)
gen_website_ImageIndexUnit_InlineActionContainer = Generalization(general=InlineActionContainer, specific=website_ImageIndexUnit)
gen_website_SliderUnit_ImageUnit = Generalization(general=ImageUnit, specific=website_SliderUnit)
gen_website_GalleryUnit_ImageUnit = Generalization(general=ImageUnit, specific=website_GalleryUnit)
gen_website_FeaturePathAssociation_FeaturePath = Generalization(general=FeaturePath, specific=website_FeaturePathAssociation)
gen_website_FeaturePathAssociation_AssociationReference = Generalization(general=AssociationReference, specific=website_FeaturePathAssociation)
gen_website_RegistrationUnit_AuthenticationUnit = Generalization(general=AuthenticationUnit, specific=website_RegistrationUnit)
gen_website_RegistrationUnit_ControlUnit = Generalization(general=ControlUnit, specific=website_RegistrationUnit)
gen_website_LoginUnit_AuthenticationUnit = Generalization(general=AuthenticationUnit, specific=website_LoginUnit)
gen_website_LoginUnit_ControlUnit = Generalization(general=ControlUnit, specific=website_LoginUnit)
gen_website_ForgottenPasswordUnit_AuthenticationUnit = Generalization(general=AuthenticationUnit, specific=website_ForgottenPasswordUnit)
gen_website_ForgottenPasswordUnit_ControlUnit = Generalization(general=ControlUnit, specific=website_ForgottenPasswordUnit)
gen_website_InlineAction_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=website_InlineAction)
gen_website_DeleteAction_InlineAction = Generalization(general=InlineAction, specific=website_DeleteAction)
gen_website_FeatureSupportAction_InlineAction = Generalization(general=InlineAction, specific=website_FeatureSupportAction)
gen_website_ModelReference_Path = Generalization(general=Path, specific=website_ModelReference)
gen_website_FeatureReference_Path = Generalization(general=Path, specific=website_FeatureReference)
gen_website_RouteParameterReference_Path = Generalization(general=Path, specific=website_RouteParameterReference)
gen_website_ParameterReference_Path = Generalization(general=Path, specific=website_ParameterReference)
gen_website_CurrentUserReference_Path = Generalization(general=Path, specific=website_CurrentUserReference)
gen_website_SelectAction_InlineAction = Generalization(general=InlineAction, specific=website_SelectAction)

# Domain Model
domain_model = DomainModel(
    name="website",
    types={website_Classifier, website_Service, website_WebGenModel, website_WebsiteProperties, website_Page, website_Menu, website_EntityOrView, website_ImageManipulation, website_Authentication, website_RegistrationUnit, website_LoginUnit, website_ForgottenPasswordUnit, website_Attribute, website_LocalAuthenticationSystem, Authentication, website_ModelLabel, website_CasAuthentication, website_NamedElement, website_NamedDisplayElement, NamedElement, NamedDisplayElement, website_DataType, Classifier, website_EnumerationType, DataType, website_EnumerationLiteral, website_Feature, Feature, Label, website_Association, website_EntityFeature, website_Expression, website_EncapsulatedAssociation, website_Label, website_ModelLabelFeature, website_ModelLabelAttribute, ModelLabelFeature, website_ModelLabelAssociation, website_EntityAssociation, website_Entity, EntityOrView, website_ResourceAttribute, website_EntityAttribute, EntityFeature, Attribute, website_DataTypeAttribute, EntityAttribute, website_DateAttribute, website_UrlAttribute, website_PathElement, website_StaticPathElement, PathElement, website_DatePathElement, website_FileAttribute, ResourceAttribute, website_ImageAttribute, website_LocationAttribute, Association, website_AssociationKey, website_AssociationWithoutContainment, EntityAssociation, website_AssociationWithContainment, website_View, website_ViewFeature, website_EncapsulatedFeature, ViewFeature, website_EncapsulatedAttribute, EncapsulatedFeature, website_ViewAssociation, website_Selection, website_BusinessOperation, website_SelectionParameter, website_Predicate, website_Order, website_ImageFilter, website_ThumbnailFilter, ImageFilter, UnitContainer, website_PageLink, website_MenuEntry, website_StaticMenu, Menu, website_ActionMenuEntry, MenuEntry, website_ContentUnit, website_Query, website_EditStaticTextMenuEntry, website_DynamicMenu, website_MenuFeature, website_Filter, website_FilterParameter, website_UnitField, website_UnitSupportAction, website_QueryParameter, website_UnitContainer, website_StaticUnit, ContentUnit, website_CreateSitemapUnit, website_DynamicUnit, website_UnitFeature, UnitField, InlineActionContainer, website_UnitAssociation, AssociationReference, website_UnitElement, UnitFeature, website_DataTypeField, InterfaceField, website_DateField, website_CaptchaField, website_AssociationReference, website_ChildPath, website_InterfaceField, SelectableUnit, website_EditUnit, DynamicUnit, SingletonUnit, website_SelectableUnit, website_SingletonUnit, website_CollectionUnit, website_UpdateUnit, website_MapUnit, website_DataUnit, website_DetailsUnit, DataUnit, website_CreateUnit, EditUnit, website_CreateUpdateUnit, website_SearchUnit, ControlUnit, website_ImageUnit, website_FeaturePath, website_FeaturePathAttribute, FeaturePath, website_FeaturePathAssociation, website_IndexUnit, CollectionUnit, website_ControlUnit, ChildPath, website_ChildPathAssociation, website_ImageIndexUnit, ImageUnit, website_SliderUnit, website_GalleryUnit, website_ChildPathAttribute, website_AuthenticationUnit, AuthenticationUnit, website_InlineActionContainer, website_InlineAction, website_DeleteAction, website_FeatureSupportAction, website_ModelReference, Path, website_FeatureReference, website_RouteParameterReference, website_ParameterReference, website_CurrentUserReference, website_SelectAction, InlineAction, DatabaseTechnologies, OrmTechnologies, FrameworkTechnologies, InputTechnologies, AjaxTechnologies, AuthenticationKeyTypes, Cardinality, isHasChoices, DateDetails, OperationResultTypes, PageTopMenuOptions, CollectionDisplayOptions, IndexDisplayOption},
    associations={classifiers1, services3, websiteProperties0, pages5, menus7, allowTypeCustomisation9, imageManipulations11, authentication13, registrationUnit24, loginUnit26, sideMenu14, authenticates17, user18, userKey20, authentication22, labels40, features41, forgottenPasswordUnit28, enumerations30, keys31, unique33, containerUnique36, servedBy39, allFeatures44, attributes47, associations50, allAssociations52, entityFeatures73, associationEnds75, defaultValue55, encapsulatedBy57, sourceEntityX58, targetEntityX61, labelFor64, features65, partOf66, attribute68, association70, dynamicLabel71, partOf76, dataType77, sourceFeature84, targetFeature85, uploadPath78, keys79, targetEntity80, keyFor82, targetEntity100, encapsulates88, viewFeatures90, partOf92, attribute93, association95, encapsulatedTarget97, sourceEntity98, uses124, opposite103, serves105, selections107, operations108, usedBy110, fields112, parameters114, joins115, filter118, ordering120, formalFor122, entries136, filters127, parentPage129, childPages131, sideMenu132, targetPage135, formal155, dataType156, partOf138, destination139, query140, entityOrView142, selection144, title147, parameters149, selection151, partOf153, displayFields171, supportActions173, filter159, parameters162, formal164, units167, displayedOn168, entities169, displayedOn175, attribute178, defaultValue180, sourceEntity183, targetEntity185, selection188, forcedValue176, dataType199, association191, valueDisplay193, childFeature196, mustMatch198, contentType205, containingFeature207, selection210, filters213, pagination216, defaultSelection219, title221, enableWhen224, selectionType201, contentType203, location233, placeName234, defaultSelection237, title239, confirmDestination227, cancelDestination230, resultsDestination244, defaultSelection245, imagePathFeature247, titleFeature249, imageFilter252, attribute255, cancelDestination242, attribute263, sourceEntity265, targetEntity267, sourceEntity257, targetEntity259, partOf262, actions272, usedBy274, enableWhen275, displayWhen277, fullSizeFilter270, destination282, operation284, unit286, feature288, parameter290, parameter292, userModel294, target280},
    generalizations={gen_website_LocalAuthenticationSystem_Authentication, gen_website_CasAuthentication_Authentication, gen_website_NamedDisplayElement_NamedElement, gen_website_Classifier_NamedDisplayElement, gen_website_DataType_Classifier, gen_website_EnumerationType_DataType, gen_website_EnumerationLiteral_NamedDisplayElement, gen_website_EntityOrView_Classifier, gen_website_Attribute_Feature, gen_website_Attribute_Label, gen_website_Association_Feature, gen_website_ModelLabel_NamedElement, gen_website_ModelLabel_Label, gen_website_ModelLabelAttribute_ModelLabelFeature, gen_website_ModelLabelAssociation_ModelLabelFeature, gen_website_Entity_EntityOrView, gen_website_ResourceAttribute_EntityAttribute, gen_website_EntityFeature_NamedDisplayElement, gen_website_EntityFeature_Feature, gen_website_EntityAttribute_EntityFeature, gen_website_EntityAttribute_Attribute, gen_website_DataTypeAttribute_EntityAttribute, gen_website_DateAttribute_EntityAttribute, gen_website_UrlAttribute_EntityAttribute, gen_website_StaticPathElement_PathElement, gen_website_DatePathElement_PathElement, gen_website_FileAttribute_ResourceAttribute, gen_website_ImageAttribute_ResourceAttribute, gen_website_LocationAttribute_EntityAttribute, gen_website_EntityAssociation_EntityFeature, gen_website_EntityAssociation_Association, gen_website_AssociationWithoutContainment_EntityAssociation, gen_website_AssociationWithContainment_EntityAssociation, gen_website_View_EntityOrView, gen_website_ViewFeature_Feature, gen_website_EncapsulatedFeature_ViewFeature, gen_website_EncapsulatedAttribute_EncapsulatedFeature, gen_website_EncapsulatedAttribute_Attribute, gen_website_EncapsulatedAssociation_EncapsulatedFeature, gen_website_EncapsulatedAssociation_Association, gen_website_BusinessOperation_NamedElement, gen_website_ViewAssociation_NamedDisplayElement, gen_website_ViewAssociation_ViewFeature, gen_website_ViewAssociation_Association, gen_website_Service_NamedElement, gen_website_Selection_NamedElement, gen_website_SelectionParameter_NamedElement, gen_website_ImageManipulation_NamedElement, gen_website_ThumbnailFilter_ImageFilter, gen_website_Page_NamedDisplayElement, gen_website_Page_UnitContainer, gen_website_Menu_NamedDisplayElement, gen_website_StaticMenu_Menu, gen_website_ActionMenuEntry_MenuEntry, gen_website_ActionMenuEntry_NamedDisplayElement, gen_website_EditStaticTextMenuEntry_MenuEntry, gen_website_EditStaticTextMenuEntry_NamedDisplayElement, gen_website_DynamicMenu_Menu, gen_website_MenuFeature_MenuEntry, gen_website_Filter_NamedDisplayElement, gen_website_FilterParameter_NamedElement, gen_website_ContentUnit_NamedDisplayElement, gen_website_StaticUnit_ContentUnit, gen_website_CreateSitemapUnit_ContentUnit, gen_website_DynamicUnit_ContentUnit, gen_website_UnitFeature_UnitField, gen_website_UnitFeature_InlineActionContainer, gen_website_UnitAssociation_UnitFeature, gen_website_UnitAssociation_UnitContainer, gen_website_UnitAssociation_AssociationReference, gen_website_UnitElement_UnitFeature, gen_website_DataTypeField_InterfaceField, gen_website_DateField_InterfaceField, gen_website_CaptchaField_InterfaceField, gen_website_UnitSupportAction_NamedDisplayElement, gen_website_InterfaceField_NamedDisplayElement, gen_website_InterfaceField_UnitField, gen_website_CollectionUnit_SelectableUnit, gen_website_EditUnit_DynamicUnit, gen_website_EditUnit_SingletonUnit, gen_website_UpdateUnit_EditUnit, gen_website_UpdateUnit_SelectableUnit, gen_website_MapUnit_EditUnit, gen_website_MapUnit_SelectableUnit, gen_website_DataUnit_DynamicUnit, gen_website_DetailsUnit_DataUnit, gen_website_DetailsUnit_SingletonUnit, gen_website_DetailsUnit_SelectableUnit, gen_website_CreateUnit_EditUnit, gen_website_CreateUpdateUnit_EditUnit, gen_website_CreateUpdateUnit_SelectableUnit, gen_website_SearchUnit_ControlUnit, gen_website_ImageUnit_DynamicUnit, gen_website_ImageUnit_CollectionUnit, gen_website_FeaturePathAttribute_FeaturePath, gen_website_IndexUnit_DataUnit, gen_website_IndexUnit_CollectionUnit, gen_website_IndexUnit_InlineActionContainer, gen_website_ControlUnit_DynamicUnit, gen_website_ChildPathAttribute_ChildPath, gen_website_ChildPathAssociation_ChildPath, gen_website_ChildPathAssociation_AssociationReference, gen_website_ImageIndexUnit_ImageUnit, gen_website_ImageIndexUnit_InlineActionContainer, gen_website_SliderUnit_ImageUnit, gen_website_GalleryUnit_ImageUnit, gen_website_FeaturePathAssociation_FeaturePath, gen_website_FeaturePathAssociation_AssociationReference, gen_website_RegistrationUnit_AuthenticationUnit, gen_website_RegistrationUnit_ControlUnit, gen_website_LoginUnit_AuthenticationUnit, gen_website_LoginUnit_ControlUnit, gen_website_ForgottenPasswordUnit_AuthenticationUnit, gen_website_ForgottenPasswordUnit_ControlUnit, gen_website_InlineAction_NamedDisplayElement, gen_website_DeleteAction_InlineAction, gen_website_FeatureSupportAction_InlineAction, gen_website_ModelReference_Path, gen_website_FeatureReference_Path, gen_website_RouteParameterReference_Path, gen_website_ParameterReference_Path, gen_website_CurrentUserReference_Path, gen_website_SelectAction_InlineAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)