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
PlatformLayers: Enumeration = Enumeration(
    name="PlatformLayers",
    literals={
            EnumerationLiteral(name="ServiceLayer"),
			EnumerationLiteral(name="UILayer")
    }
)

Comparator: Enumeration = Enumeration(
    name="Comparator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="GEQ"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LEQ")
    }
)

Order: Enumeration = Enumeration(
    name="Order",
    literals={
            EnumerationLiteral(name="ASC"),
			EnumerationLiteral(name="DESC")
    }
)

RelationType: Enumeration = Enumeration(
    name="RelationType",
    literals={
            EnumerationLiteral(name="One2One"),
			EnumerationLiteral(name="One2Many"),
			EnumerationLiteral(name="Many2Many")
    }
)

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="Top"),
			EnumerationLiteral(name="Bottom"),
			EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right")
    }
)

# Classes
domain_Domain = Class(name="domain::Domain")
domain_DomainArtifacts = Class(name="domain::DomainArtifacts")
domain_DomainTypes = Class(name="domain::DomainTypes")
domain_DomainApplications = Class(name="domain::DomainApplications")
domain_EObject = Class(name="domain::EObject")
domain_GenerationHint = Class(name="domain::GenerationHint")
domain_Secured = Class(name="domain::Secured")
domain_GrantAccess = Class(name="domain::GrantAccess")
domain_DomainApplication = Class(name="domain::DomainApplication")
domain_Role = Class(name="domain::Role")
HTMLLayerHolder = Class(name="HTMLLayerHolder")
domain_HTMLLayerHolder = Class(name="domain::HTMLLayerHolder")
domain_Categorized = Class(name="domain::Categorized")
domain_Classifier = Class(name="domain::Classifier")
domain_DomainArtifact = Class(name="domain::DomainArtifact")
domain_TypesRepository = Class(name="domain::TypesRepository")
domain_Application = Class(name="domain::Application")
domain_Artifacts = Class(name="domain::Artifacts")
domain_EJBService = Class(name="domain::EJBService")
domain_ContinuousIintegration = Class(name="domain::ContinuousIintegration")
domain_Artifact = Class(name="domain::Artifact")
domain_ORMEntity = Class(name="domain::ORMEntity")
DomainArtifact = Class(name="DomainArtifact")
domain_JPAService = Class(name="domain::JPAService")
domain_ConfigVariable = Class(name="domain::ConfigVariable")
domain_ConfigHash = Class(name="domain::ConfigHash")
domain_ModelQuery = Class(name="domain::ModelQuery")
domain_Specifier = Class(name="domain::Specifier")
domain_QueryParameter = Class(name="domain::QueryParameter")
domain_ApplicationRecipes = Class(name="domain::ApplicationRecipes")
domain_ApplicationMappers = Class(name="domain::ApplicationMappers")
domain_ApplicationUILayer = Class(name="domain::ApplicationUILayer")
domain_ApplicationInfrastructureLayer = Class(name="domain::ApplicationInfrastructureLayer")
domain_ApplicationStyle = Class(name="domain::ApplicationStyle")
domain_Option = Class(name="domain::Option")
domain_Messages = Class(name="domain::Messages")
domain_ApplicationRole = Class(name="domain::ApplicationRole")
domain_ApplicationMessages = Class(name="domain::ApplicationMessages")
domain_StylesPackage = Class(name="domain::StylesPackage")
domain_Roles = Class(name="domain::Roles")
domain_ApplicationUIPackage = Class(name="domain::ApplicationUIPackage")
domain_Styles = Class(name="domain::Styles")
domain_ApplicationRecipe = Class(name="domain::ApplicationRecipe")
domain_Recipes = Class(name="domain::Recipes")
domain_UIPackage = Class(name="domain::UIPackage")
domain_ApplicationMapper = Class(name="domain::ApplicationMapper")
domain_Mappers = Class(name="domain::Mappers")
domain_MethodPointer = Class(name="domain::MethodPointer")
TypePointer = Class(name="TypePointer")
domain_Operation = Class(name="domain::Operation")
domain_MessageLibrary = Class(name="domain::MessageLibrary")
domain_Language = Class(name="domain::Language")
Categorized = Class(name="Categorized")
domain_LanguageRef = Class(name="domain::LanguageRef")
domain_Message = Class(name="domain::Message")
domain_Translation = Class(name="domain::Translation")
domain_Group = Class(name="domain::Group")
domain_StyleLibrary = Class(name="domain::StyleLibrary")
domain_StyleSet = Class(name="domain::StyleSet")
domain_Mapper = Class(name="domain::Mapper")
domain_JavaScriptMapper = Class(name="domain::JavaScriptMapper")
domain_CSSMapper = Class(name="domain::CSSMapper")
domain_TypeMapper = Class(name="domain::TypeMapper")
Mapper = Class(name="Mapper")
domain_JavaMapper = Class(name="domain::JavaMapper")
TypeMapper = Class(name="TypeMapper")
domain_RoleMapper = Class(name="domain::RoleMapper")
domain_Recipe = Class(name="domain::Recipe")
domain_Configuration = Class(name="domain::Configuration")
domain_DeploymentSequence = Class(name="domain::DeploymentSequence")
domain_ConfigExtension = Class(name="domain::ConfigExtension")
domain_DeploymentComponents = Class(name="domain::DeploymentComponents")
domain_Infrastructure = Class(name="domain::Infrastructure")
domain_ModelMapper = Class(name="domain::ModelMapper")
domain_DeploymentComponent = Class(name="domain::DeploymentComponent")
domain_DeploymentStarStep = Class(name="domain::DeploymentStarStep")
UsingMappers = Class(name="UsingMappers")
domain_UsingMappers = Class(name="domain::UsingMappers")
domain_Ingredient = Class(name="domain::Ingredient")
domain_Component = Class(name="domain::Component")
domain_JavaComponent = Class(name="domain::JavaComponent")
Component = Class(name="Component")
domain_Property = Class(name="domain::Property")
domain_HashProperty = Class(name="domain::HashProperty")
ArtifactRef = Class(name="ArtifactRef")
domain_MappingSpecifier = Class(name="domain::MappingSpecifier")
domain_Query = Class(name="domain::Query")
domain_KeyValuePair = Class(name="domain::KeyValuePair")
domain_QueryVariable = Class(name="domain::QueryVariable")
domain_TypePointer = Class(name="domain::TypePointer")
domain_Package = Class(name="domain::Package")
domain_TypeElement = Class(name="domain::TypeElement")
domain_TypeDefinition = Class(name="domain::TypeDefinition")
domain_ArtifactRef = Class(name="domain::ArtifactRef")
domain_References = Class(name="domain::References")
RelationShip = Class(name="RelationShip")
domain_Generalization = Class(name="domain::Generalization")
domain_RelationShip = Class(name="domain::RelationShip")
domain_Link = Class(name="domain::Link")
domain_Attribute = Class(name="domain::Attribute")
domain_Primitive = Class(name="domain::Primitive")
TypeElement = Class(name="TypeElement")
domain_Assosiation = Class(name="domain::Assosiation")
domain_TypeReference = Class(name="domain::TypeReference")
domain_Type = Class(name="domain::Type")
Secured = Class(name="Secured")
domain_Parameter = Class(name="domain::Parameter")
domain_ReturnValue = Class(name="domain::ReturnValue")
domain_Enumarator = Class(name="domain::Enumarator")
domain_EnumAttribute = Class(name="domain::EnumAttribute")
domain_Types = Class(name="domain::Types")
domain_Form = Class(name="domain::Form")
domain_FormView = Class(name="domain::FormView")
domain_Views = Class(name="domain::Views")
domain_FormDataControls = Class(name="domain::FormDataControls")
domain_FormParameter = Class(name="domain::FormParameter")
domain_TabPagesInheritance = Class(name="domain::TabPagesInheritance")
domain_MenuDefinition = Class(name="domain::MenuDefinition")
domain_Orderable = Class(name="domain::Orderable")
domain_MultiLangLabel = Class(name="domain::MultiLangLabel")
domain_Context = Class(name="domain::Context")
domain_CanvasFrame = Class(name="domain::CanvasFrame")
domain_ViewInheritance = Class(name="domain::ViewInheritance")
domain_ViewElement = Class(name="domain::ViewElement")
domain_DefaultCavas = Class(name="domain::DefaultCavas")
NickNamed = Class(name="NickNamed")
domain_PopupCanvas = Class(name="domain::PopupCanvas")
CanvasFrame = Class(name="CanvasFrame")
ViewPortHolder = Class(name="ViewPortHolder")
DefaultCavas = Class(name="DefaultCavas")
MultiLangLabel = Class(name="MultiLangLabel")
FlexFields = Class(name="FlexFields")
StyleElement = Class(name="StyleElement")
domain_ViewPortHolder = Class(name="domain::ViewPortHolder")
domain_Window = Class(name="domain::Window")
domain_MenuView = Class(name="domain::MenuView")
domain_Canvas = Class(name="domain::Canvas")
domain_TabPage = Class(name="domain::TabPage")
Orderable = Class(name="Orderable")
domain_ViewPort = Class(name="domain::ViewPort")
ViewElement = Class(name="ViewElement")
domain_ViewPortTrigger = Class(name="domain::ViewPortTrigger")
domain_ViewArea = Class(name="domain::ViewArea")
domain_TabCanvas = Class(name="domain::TabCanvas")
domain_CanvasView = Class(name="domain::CanvasView")
Trigger = Class(name="Trigger")
domain_Controls = Class(name="domain::Controls")
domain_LayerHolder = Class(name="domain::LayerHolder")
domain_LinkToMessage = Class(name="domain::LinkToMessage")
domain_InputElement = Class(name="domain::InputElement")
domain_MessageElement = Class(name="domain::MessageElement")
domain_LinkToLabel = Class(name="domain::LinkToLabel")
domain_ChildrenHolder = Class(name="domain::ChildrenHolder")
domain_Uielement = Class(name="domain::Uielement")
domain_ContextParameter = Class(name="domain::ContextParameter")
domain_ContextValue = Class(name="domain::ContextValue")
domain_ExpressionPart = Class(name="domain::ExpressionPart")
domain_Label = Class(name="domain::Label")
domain_ContextParameters = Class(name="domain::ContextParameters")
ContextValue = Class(name="ContextValue")
ContextParameters = Class(name="ContextParameters")
domain_StyleElement = Class(name="domain::StyleElement")
domain_StyleClass = Class(name="domain::StyleClass")
domain_NickNamed = Class(name="domain::NickNamed")
Context = Class(name="Context")
domain_EnabledUIItem = Class(name="domain::EnabledUIItem")
EnabledUIItem = Class(name="EnabledUIItem")
MenuHolder = Class(name="MenuHolder")
domain_AreaRef = Class(name="domain::AreaRef")
domain_FlexFields = Class(name="domain::FlexFields")
domain_FlexField = Class(name="domain::FlexField")
domain_Formatable = Class(name="domain::Formatable")
domain_SourcesPointer = Class(name="domain::SourcesPointer")
Uielement = Class(name="Uielement")
domain_DataControl = Class(name="domain::DataControl")
domain_Selection = Class(name="domain::Selection")
domain_ItemIcon = Class(name="domain::ItemIcon")
domain_OptionSelection = Class(name="domain::OptionSelection")
InputElement = Class(name="InputElement")
ChildrenHolder = Class(name="ChildrenHolder")
domain_InputText = Class(name="domain::InputText")
Formatable = Class(name="Formatable")
domain_Password = Class(name="domain::Password")
SourcesPointer = Class(name="SourcesPointer")
domain_CheckBox = Class(name="domain::CheckBox")
domain_DropDownSelection = Class(name="domain::DropDownSelection")
OptionSelection = Class(name="OptionSelection")
domain_Image = Class(name="domain::Image")
domain_Date = Class(name="domain::Date")
domain_Button = Class(name="domain::Button")
ItemIcon = Class(name="ItemIcon")
domain_OutputText = Class(name="domain::OutputText")
domain_Table = Class(name="domain::Table")
domain_Menu = Class(name="domain::Menu")
domain_Tree = Class(name="domain::Tree")
domain_Column = Class(name="domain::Column")
domain_Dependency = Class(name="domain::Dependency")
domain_Trigger = Class(name="domain::Trigger")
MethodPointer = Class(name="MethodPointer")
domain_PREFormTrigger = Class(name="domain::PREFormTrigger")
domain_PREQueryTrigger = Class(name="domain::PREQueryTrigger")
domain_POSTQueryTrigger = Class(name="domain::POSTQueryTrigger")
domain_PREInsertTrigger = Class(name="domain::PREInsertTrigger")
domain_Root = Class(name="domain::Root")
domain_Relation = Class(name="domain::Relation")
domain_POSTCreateTrigger = Class(name="domain::POSTCreateTrigger")
domain_PREUpdateTrigger = Class(name="domain::PREUpdateTrigger")
domain_ProxiesList = Class(name="domain::ProxiesList")
domain_CreateTrigger = Class(name="domain::CreateTrigger")
ProxiesList = Class(name="ProxiesList")
domain_PREDeleteTrigger = Class(name="domain::PREDeleteTrigger")
domain_InsertTrigger = Class(name="domain::InsertTrigger")
domain_UpdateTrigger = Class(name="domain::UpdateTrigger")
domain_DeleteTrigger = Class(name="domain::DeleteTrigger")
domain_SearchTrigger = Class(name="domain::SearchTrigger")
domain_FormVariable = Class(name="domain::FormVariable")
domain_ArtificialField = Class(name="domain::ArtificialField")
domain_Orders = Class(name="domain::Orders")
domain_OrderBy = Class(name="domain::OrderBy")
domain_EnterpriseInfrastructure = Class(name="domain::EnterpriseInfrastructure")
domain_Datacenter = Class(name="domain::Datacenter")
domain_InfrastructureConnection = Class(name="domain::InfrastructureConnection")
domain_Subsystem = Class(name="domain::Subsystem")
domain_InfrastructureLayer = Class(name="domain::InfrastructureLayer")
domain_Server = Class(name="domain::Server")
InfrastructureComponent = Class(name="InfrastructureComponent")
domain_Router = Class(name="domain::Router")
domain_Hub = Class(name="domain::Hub")
domain_Storage = Class(name="domain::Storage")
domain_InfrastructureComponent = Class(name="domain::InfrastructureComponent")
domain_MenuFolder = Class(name="domain::MenuFolder")
domain_MenuHolder = Class(name="domain::MenuHolder")
domain_MenuExtensionRef = Class(name="domain::MenuExtensionRef")
domain_MenuElement = Class(name="domain::MenuElement")
domain_ServerClaster = Class(name="domain::ServerClaster")
domain_MenuExtensionPoint = Class(name="domain::MenuExtensionPoint")
MenuExtensionRef = Class(name="MenuExtensionRef")
domain_SubMenu = Class(name="domain::SubMenu")
domain_MenuSeparator = Class(name="domain::MenuSeparator")
domain_MenuItem = Class(name="domain::MenuItem")
MenuElement = Class(name="MenuElement")

# domain_Domain class attributes and methods
domain_Domain_uid: Property = Property(name="uid", type=StringType)
domain_Domain.attributes={domain_Domain_uid}

# domain_DomainArtifacts class attributes and methods
domain_DomainArtifacts_uid: Property = Property(name="uid", type=StringType)
domain_DomainArtifacts_name: Property = Property(name="name", type=StringType)
domain_DomainArtifacts.attributes={domain_DomainArtifacts_uid, domain_DomainArtifacts_name}

# domain_DomainTypes class attributes and methods
domain_DomainTypes_uid: Property = Property(name="uid", type=StringType)
domain_DomainTypes_name: Property = Property(name="name", type=StringType)
domain_DomainTypes.attributes={domain_DomainTypes_name, domain_DomainTypes_uid}

# domain_DomainApplications class attributes and methods
domain_DomainApplications_uid: Property = Property(name="uid", type=StringType)
domain_DomainApplications_name: Property = Property(name="name", type=StringType)
domain_DomainApplications.attributes={domain_DomainApplications_uid, domain_DomainApplications_name}

# domain_EObject class attributes and methods

# domain_GenerationHint class attributes and methods
domain_GenerationHint_uid: Property = Property(name="uid", type=StringType)
domain_GenerationHint_name: Property = Property(name="name", type=StringType)
domain_GenerationHint_applyedClass: Property = Property(name="applyedClass", type=StringType)
domain_GenerationHint.attributes={domain_GenerationHint_uid, domain_GenerationHint_name, domain_GenerationHint_applyedClass}

# domain_Secured class attributes and methods

# domain_GrantAccess class attributes and methods
domain_GrantAccess_uid: Property = Property(name="uid", type=StringType)
domain_GrantAccess.attributes={domain_GrantAccess_uid}

# domain_DomainApplication class attributes and methods
domain_DomainApplication_uid: Property = Property(name="uid", type=StringType)
domain_DomainApplication_name: Property = Property(name="name", type=StringType)
domain_DomainApplication.attributes={domain_DomainApplication_uid, domain_DomainApplication_name}

# domain_Role class attributes and methods
domain_Role_uid: Property = Property(name="uid", type=StringType)
domain_Role_name: Property = Property(name="name", type=StringType)
domain_Role.attributes={domain_Role_uid, domain_Role_name}

# HTMLLayerHolder class attributes and methods

# domain_HTMLLayerHolder class attributes and methods
domain_HTMLLayerHolder_columns: Property = Property(name="columns", type=IntegerType)
domain_HTMLLayerHolder.attributes={domain_HTMLLayerHolder_columns}

# domain_Categorized class attributes and methods

# domain_Classifier class attributes and methods
domain_Classifier_uid: Property = Property(name="uid", type=StringType)
domain_Classifier_details: Property = Property(name="details", type=StringType)
domain_Classifier.attributes={domain_Classifier_uid, domain_Classifier_details}

# domain_DomainArtifact class attributes and methods
domain_DomainArtifact_uid: Property = Property(name="uid", type=StringType)
domain_DomainArtifact_name: Property = Property(name="name", type=StringType)
domain_DomainArtifact.attributes={domain_DomainArtifact_uid, domain_DomainArtifact_name}

# domain_TypesRepository class attributes and methods
domain_TypesRepository_uid: Property = Property(name="uid", type=StringType)
domain_TypesRepository.attributes={domain_TypesRepository_uid}

# domain_Application class attributes and methods
domain_Application_uid: Property = Property(name="uid", type=StringType)
domain_Application.attributes={domain_Application_uid}

# domain_Artifacts class attributes and methods
domain_Artifacts_uid: Property = Property(name="uid", type=StringType)
domain_Artifacts.attributes={domain_Artifacts_uid}

# domain_EJBService class attributes and methods

# domain_ContinuousIintegration class attributes and methods

# domain_Artifact class attributes and methods
domain_Artifact_name: Property = Property(name="name", type=StringType)
domain_Artifact_description: Property = Property(name="description", type=StringType)
domain_Artifact_uid: Property = Property(name="uid", type=StringType)
domain_Artifact_template: Property = Property(name="template", type=StringType)
domain_Artifact.attributes={domain_Artifact_template, domain_Artifact_uid, domain_Artifact_name, domain_Artifact_description}

# domain_ORMEntity class attributes and methods

# DomainArtifact class attributes and methods

# domain_JPAService class attributes and methods

# domain_ConfigVariable class attributes and methods
domain_ConfigVariable_uid: Property = Property(name="uid", type=StringType)
domain_ConfigVariable_name: Property = Property(name="name", type=StringType)
domain_ConfigVariable.attributes={domain_ConfigVariable_uid, domain_ConfigVariable_name}

# domain_ConfigHash class attributes and methods
domain_ConfigHash_uid: Property = Property(name="uid", type=StringType)
domain_ConfigHash_name: Property = Property(name="name", type=StringType)
domain_ConfigHash.attributes={domain_ConfigHash_name, domain_ConfigHash_uid}

# domain_ModelQuery class attributes and methods
domain_ModelQuery_uid: Property = Property(name="uid", type=StringType)
domain_ModelQuery_name: Property = Property(name="name", type=StringType)
domain_ModelQuery_query: Property = Property(name="query", type=StringType)
domain_ModelQuery.attributes={domain_ModelQuery_uid, domain_ModelQuery_query, domain_ModelQuery_name}

# domain_Specifier class attributes and methods
domain_Specifier_uid: Property = Property(name="uid", type=StringType)
domain_Specifier_name: Property = Property(name="name", type=StringType)
domain_Specifier.attributes={domain_Specifier_name, domain_Specifier_uid}

# domain_QueryParameter class attributes and methods
domain_QueryParameter_uid: Property = Property(name="uid", type=StringType)
domain_QueryParameter_name: Property = Property(name="name", type=StringType)
domain_QueryParameter.attributes={domain_QueryParameter_uid, domain_QueryParameter_name}

# domain_ApplicationRecipes class attributes and methods
domain_ApplicationRecipes_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationRecipes_name: Property = Property(name="name", type=StringType)
domain_ApplicationRecipes.attributes={domain_ApplicationRecipes_name, domain_ApplicationRecipes_uid}

# domain_ApplicationMappers class attributes and methods
domain_ApplicationMappers_name: Property = Property(name="name", type=StringType)
domain_ApplicationMappers_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationMappers.attributes={domain_ApplicationMappers_name, domain_ApplicationMappers_uid}

# domain_ApplicationUILayer class attributes and methods
domain_ApplicationUILayer_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationUILayer_name: Property = Property(name="name", type=StringType)
domain_ApplicationUILayer.attributes={domain_ApplicationUILayer_uid, domain_ApplicationUILayer_name}

# domain_ApplicationInfrastructureLayer class attributes and methods
domain_ApplicationInfrastructureLayer_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationInfrastructureLayer_name: Property = Property(name="name", type=StringType)
domain_ApplicationInfrastructureLayer.attributes={domain_ApplicationInfrastructureLayer_uid, domain_ApplicationInfrastructureLayer_name}

# domain_ApplicationStyle class attributes and methods
domain_ApplicationStyle_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationStyle_name: Property = Property(name="name", type=StringType)
domain_ApplicationStyle.attributes={domain_ApplicationStyle_name, domain_ApplicationStyle_uid}

# domain_Option class attributes and methods
domain_Option_uid: Property = Property(name="uid", type=StringType)
domain_Option_value: Property = Property(name="value", type=StringType)
domain_Option.attributes={domain_Option_value, domain_Option_uid}

# domain_Messages class attributes and methods
domain_Messages_uid: Property = Property(name="uid", type=StringType)
domain_Messages.attributes={domain_Messages_uid}

# domain_ApplicationRole class attributes and methods
domain_ApplicationRole_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationRole_name: Property = Property(name="name", type=StringType)
domain_ApplicationRole.attributes={domain_ApplicationRole_name, domain_ApplicationRole_uid}

# domain_ApplicationMessages class attributes and methods
domain_ApplicationMessages_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationMessages_name: Property = Property(name="name", type=StringType)
domain_ApplicationMessages.attributes={domain_ApplicationMessages_name, domain_ApplicationMessages_uid}

# domain_StylesPackage class attributes and methods
domain_StylesPackage_uid: Property = Property(name="uid", type=StringType)
domain_StylesPackage_name: Property = Property(name="name", type=StringType)
domain_StylesPackage.attributes={domain_StylesPackage_name, domain_StylesPackage_uid}

# domain_Roles class attributes and methods
domain_Roles_uid: Property = Property(name="uid", type=StringType)
domain_Roles.attributes={domain_Roles_uid}

# domain_ApplicationUIPackage class attributes and methods
domain_ApplicationUIPackage_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationUIPackage_name: Property = Property(name="name", type=StringType)
domain_ApplicationUIPackage.attributes={domain_ApplicationUIPackage_name, domain_ApplicationUIPackage_uid}

# domain_Styles class attributes and methods
domain_Styles_uid: Property = Property(name="uid", type=StringType)
domain_Styles.attributes={domain_Styles_uid}

# domain_ApplicationRecipe class attributes and methods
domain_ApplicationRecipe_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationRecipe_name: Property = Property(name="name", type=StringType)
domain_ApplicationRecipe.attributes={domain_ApplicationRecipe_uid, domain_ApplicationRecipe_name}

# domain_Recipes class attributes and methods
domain_Recipes_uid: Property = Property(name="uid", type=StringType)
domain_Recipes.attributes={domain_Recipes_uid}

# domain_UIPackage class attributes and methods
domain_UIPackage_uid: Property = Property(name="uid", type=StringType)
domain_UIPackage.attributes={domain_UIPackage_uid}

# domain_ApplicationMapper class attributes and methods
domain_ApplicationMapper_uid: Property = Property(name="uid", type=StringType)
domain_ApplicationMapper_name: Property = Property(name="name", type=StringType)
domain_ApplicationMapper.attributes={domain_ApplicationMapper_name, domain_ApplicationMapper_uid}

# domain_Mappers class attributes and methods
domain_Mappers_uid: Property = Property(name="uid", type=StringType)
domain_Mappers.attributes={domain_Mappers_uid}

# domain_MethodPointer class attributes and methods
domain_MethodPointer_fakeMethod: Property = Property(name="fakeMethod", type=StringType)
domain_MethodPointer.attributes={domain_MethodPointer_fakeMethod}

# TypePointer class attributes and methods

# domain_Operation class attributes and methods
domain_Operation_uid: Property = Property(name="uid", type=StringType)
domain_Operation_name: Property = Property(name="name", type=StringType)
domain_Operation.attributes={domain_Operation_name, domain_Operation_uid}

# domain_MessageLibrary class attributes and methods
domain_MessageLibrary_uid: Property = Property(name="uid", type=StringType)
domain_MessageLibrary_name: Property = Property(name="name", type=StringType)
domain_MessageLibrary.attributes={domain_MessageLibrary_name, domain_MessageLibrary_uid}

# domain_Language class attributes and methods
domain_Language_uid: Property = Property(name="uid", type=StringType)
domain_Language_lang: Property = Property(name="lang", type=StringType)
domain_Language_code: Property = Property(name="code", type=StringType)
domain_Language_defaultLang: Property = Property(name="defaultLang", type=BooleanType)
domain_Language.attributes={domain_Language_code, domain_Language_defaultLang, domain_Language_lang, domain_Language_uid}

# Categorized class attributes and methods

# domain_LanguageRef class attributes and methods
domain_LanguageRef_uid: Property = Property(name="uid", type=StringType)
domain_LanguageRef.attributes={domain_LanguageRef_uid}

# domain_Message class attributes and methods
domain_Message_uid: Property = Property(name="uid", type=StringType)
domain_Message_name: Property = Property(name="name", type=StringType)
domain_Message.attributes={domain_Message_name, domain_Message_uid}

# domain_Translation class attributes and methods
domain_Translation_uid: Property = Property(name="uid", type=StringType)
domain_Translation_translation: Property = Property(name="translation", type=StringType)
domain_Translation.attributes={domain_Translation_uid, domain_Translation_translation}

# domain_Group class attributes and methods
domain_Group_uid: Property = Property(name="uid", type=StringType)
domain_Group_name: Property = Property(name="name", type=StringType)
domain_Group.attributes={domain_Group_uid, domain_Group_name}

# domain_StyleLibrary class attributes and methods
domain_StyleLibrary_uid: Property = Property(name="uid", type=StringType)
domain_StyleLibrary_name: Property = Property(name="name", type=StringType)
domain_StyleLibrary.attributes={domain_StyleLibrary_uid, domain_StyleLibrary_name}

# domain_StyleSet class attributes and methods
domain_StyleSet_uid: Property = Property(name="uid", type=StringType)
domain_StyleSet_name: Property = Property(name="name", type=StringType)
domain_StyleSet.attributes={domain_StyleSet_name, domain_StyleSet_uid}

# domain_Mapper class attributes and methods
domain_Mapper_uid: Property = Property(name="uid", type=StringType)
domain_Mapper_serviceLayer: Property = Property(name="serviceLayer", type=BooleanType)
domain_Mapper_uiLayer: Property = Property(name="uiLayer", type=BooleanType)
domain_Mapper.attributes={domain_Mapper_uiLayer, domain_Mapper_serviceLayer, domain_Mapper_uid}

# domain_JavaScriptMapper class attributes and methods
domain_JavaScriptMapper_libraryUrl: Property = Property(name="libraryUrl", type=StringType)
domain_JavaScriptMapper.attributes={domain_JavaScriptMapper_libraryUrl}

# domain_CSSMapper class attributes and methods
domain_CSSMapper_fakePackageName: Property = Property(name="fakePackageName", type=StringType)
domain_CSSMapper_fakeTypeName: Property = Property(name="fakeTypeName", type=StringType)
domain_CSSMapper_libraryUrl: Property = Property(name="libraryUrl", type=StringType)
domain_CSSMapper.attributes={domain_CSSMapper_libraryUrl, domain_CSSMapper_fakeTypeName, domain_CSSMapper_fakePackageName}

# domain_TypeMapper class attributes and methods

# Mapper class attributes and methods

# domain_JavaMapper class attributes and methods
domain_JavaMapper_mappedToPackageName: Property = Property(name="mappedToPackageName", type=StringType)
domain_JavaMapper_mappedToClassName: Property = Property(name="mappedToClassName", type=StringType)
domain_JavaMapper_artifactId: Property = Property(name="artifactId", type=StringType)
domain_JavaMapper_groupId: Property = Property(name="groupId", type=StringType)
domain_JavaMapper_version: Property = Property(name="version", type=StringType)
domain_JavaMapper_libraryName: Property = Property(name="libraryName", type=StringType)
domain_JavaMapper_artifactType: Property = Property(name="artifactType", type=StringType)
domain_JavaMapper.attributes={domain_JavaMapper_mappedToClassName, domain_JavaMapper_artifactId, domain_JavaMapper_libraryName, domain_JavaMapper_artifactType, domain_JavaMapper_groupId, domain_JavaMapper_version, domain_JavaMapper_mappedToPackageName}

# TypeMapper class attributes and methods

# domain_RoleMapper class attributes and methods
domain_RoleMapper_localRoleName: Property = Property(name="localRoleName", type=StringType)
domain_RoleMapper_globalRoleName: Property = Property(name="globalRoleName", type=StringType)
domain_RoleMapper_fakeRoleName: Property = Property(name="fakeRoleName", type=StringType)
domain_RoleMapper.attributes={domain_RoleMapper_fakeRoleName, domain_RoleMapper_localRoleName, domain_RoleMapper_globalRoleName}

# domain_Recipe class attributes and methods
domain_Recipe_uid: Property = Property(name="uid", type=StringType)
domain_Recipe_name: Property = Property(name="name", type=StringType)
domain_Recipe.attributes={domain_Recipe_name, domain_Recipe_uid}

# domain_Configuration class attributes and methods
domain_Configuration_uid: Property = Property(name="uid", type=StringType)
domain_Configuration_name: Property = Property(name="name", type=StringType)
domain_Configuration.attributes={domain_Configuration_name, domain_Configuration_uid}

# domain_DeploymentSequence class attributes and methods
domain_DeploymentSequence_uid: Property = Property(name="uid", type=StringType)
domain_DeploymentSequence_name: Property = Property(name="name", type=StringType)
domain_DeploymentSequence.attributes={domain_DeploymentSequence_name, domain_DeploymentSequence_uid}

# domain_ConfigExtension class attributes and methods
domain_ConfigExtension_uid: Property = Property(name="uid", type=StringType)
domain_ConfigExtension.attributes={domain_ConfigExtension_uid}

# domain_DeploymentComponents class attributes and methods
domain_DeploymentComponents_uid: Property = Property(name="uid", type=StringType)
domain_DeploymentComponents.attributes={domain_DeploymentComponents_uid}

# domain_Infrastructure class attributes and methods
domain_Infrastructure_uid: Property = Property(name="uid", type=StringType)
domain_Infrastructure_name: Property = Property(name="name", type=StringType)
domain_Infrastructure.attributes={domain_Infrastructure_uid, domain_Infrastructure_name}

# domain_ModelMapper class attributes and methods
domain_ModelMapper_name: Property = Property(name="name", type=StringType)
domain_ModelMapper_artifactRoot: Property = Property(name="artifactRoot", type=StringType)
domain_ModelMapper_artifactExecutionString: Property = Property(name="artifactExecutionString", type=StringType)
domain_ModelMapper.attributes={domain_ModelMapper_name, domain_ModelMapper_artifactRoot, domain_ModelMapper_artifactExecutionString}

# domain_DeploymentComponent class attributes and methods
domain_DeploymentComponent_uid: Property = Property(name="uid", type=StringType)
domain_DeploymentComponent_name: Property = Property(name="name", type=StringType)
domain_DeploymentComponent.attributes={domain_DeploymentComponent_uid, domain_DeploymentComponent_name}

# domain_DeploymentStarStep class attributes and methods
domain_DeploymentStarStep_uid: Property = Property(name="uid", type=StringType)
domain_DeploymentStarStep_name: Property = Property(name="name", type=StringType)
domain_DeploymentStarStep.attributes={domain_DeploymentStarStep_uid, domain_DeploymentStarStep_name}

# UsingMappers class attributes and methods

# domain_UsingMappers class attributes and methods

# domain_Ingredient class attributes and methods
domain_Ingredient_name: Property = Property(name="name", type=StringType)
domain_Ingredient_layer: Property = Property(name="layer", type=StringType)
domain_Ingredient_uid: Property = Property(name="uid", type=StringType)
domain_Ingredient.attributes={domain_Ingredient_layer, domain_Ingredient_name, domain_Ingredient_uid}

# domain_Component class attributes and methods
domain_Component_uid: Property = Property(name="uid", type=StringType)
domain_Component_name: Property = Property(name="name", type=StringType)
domain_Component_componentRoot: Property = Property(name="componentRoot", type=StringType)
domain_Component.attributes={domain_Component_uid, domain_Component_name, domain_Component_componentRoot}

# domain_JavaComponent class attributes and methods
domain_JavaComponent_artifactId: Property = Property(name="artifactId", type=StringType)
domain_JavaComponent_groupId: Property = Property(name="groupId", type=StringType)
domain_JavaComponent_version: Property = Property(name="version", type=StringType)
domain_JavaComponent_basePackage: Property = Property(name="basePackage", type=StringType)
domain_JavaComponent.attributes={domain_JavaComponent_artifactId, domain_JavaComponent_groupId, domain_JavaComponent_version, domain_JavaComponent_basePackage}

# Component class attributes and methods

# domain_Property class attributes and methods
domain_Property_uid: Property = Property(name="uid", type=StringType)
domain_Property_value: Property = Property(name="value", type=StringType)
domain_Property_fakeName: Property = Property(name="fakeName", type=StringType)
domain_Property.attributes={domain_Property_value, domain_Property_uid, domain_Property_fakeName}

# domain_HashProperty class attributes and methods
domain_HashProperty_uid: Property = Property(name="uid", type=StringType)
domain_HashProperty_fakeName: Property = Property(name="fakeName", type=StringType)
domain_HashProperty.attributes={domain_HashProperty_fakeName, domain_HashProperty_uid}

# ArtifactRef class attributes and methods

# domain_MappingSpecifier class attributes and methods
domain_MappingSpecifier_uid: Property = Property(name="uid", type=StringType)
domain_MappingSpecifier.attributes={domain_MappingSpecifier_uid}

# domain_Query class attributes and methods
domain_Query_uid: Property = Property(name="uid", type=StringType)
domain_Query_name: Property = Property(name="name", type=StringType)
domain_Query.attributes={domain_Query_name, domain_Query_uid}

# domain_KeyValuePair class attributes and methods
domain_KeyValuePair_uid: Property = Property(name="uid", type=StringType)
domain_KeyValuePair_key: Property = Property(name="key", type=StringType)
domain_KeyValuePair_value: Property = Property(name="value", type=StringType)
domain_KeyValuePair.attributes={domain_KeyValuePair_key, domain_KeyValuePair_value, domain_KeyValuePair_uid}

# domain_QueryVariable class attributes and methods
domain_QueryVariable_uid: Property = Property(name="uid", type=StringType)
domain_QueryVariable_value: Property = Property(name="value", type=StringType)
domain_QueryVariable.attributes={domain_QueryVariable_value, domain_QueryVariable_uid}

# domain_TypePointer class attributes and methods
domain_TypePointer_fakePackageName: Property = Property(name="fakePackageName", type=StringType)
domain_TypePointer_fakeTypeName: Property = Property(name="fakeTypeName", type=StringType)
domain_TypePointer.attributes={domain_TypePointer_fakeTypeName, domain_TypePointer_fakePackageName}

# domain_Package class attributes and methods
domain_Package_uid: Property = Property(name="uid", type=StringType)
domain_Package_name: Property = Property(name="name", type=StringType)
domain_Package.attributes={domain_Package_name, domain_Package_uid}

# domain_TypeElement class attributes and methods
domain_TypeElement_uid: Property = Property(name="uid", type=StringType)
domain_TypeElement_name: Property = Property(name="name", type=StringType)
domain_TypeElement.attributes={domain_TypeElement_uid, domain_TypeElement_name}

# domain_TypeDefinition class attributes and methods
domain_TypeDefinition_uid: Property = Property(name="uid", type=StringType)
domain_TypeDefinition.attributes={domain_TypeDefinition_uid}

# domain_ArtifactRef class attributes and methods
domain_ArtifactRef_uid: Property = Property(name="uid", type=StringType)
domain_ArtifactRef.attributes={domain_ArtifactRef_uid}

# domain_References class attributes and methods

# RelationShip class attributes and methods

# domain_Generalization class attributes and methods

# domain_RelationShip class attributes and methods
domain_RelationShip_uid: Property = Property(name="uid", type=StringType)
domain_RelationShip.attributes={domain_RelationShip_uid}

# domain_Link class attributes and methods
domain_Link_uid: Property = Property(name="uid", type=StringType)
domain_Link.attributes={domain_Link_uid}

# domain_Attribute class attributes and methods
domain_Attribute_uid: Property = Property(name="uid", type=StringType)
domain_Attribute_name: Property = Property(name="name", type=StringType)
domain_Attribute_pk: Property = Property(name="pk", type=BooleanType)
domain_Attribute.attributes={domain_Attribute_uid, domain_Attribute_name, domain_Attribute_pk}

# domain_Primitive class attributes and methods

# TypeElement class attributes and methods

# domain_Assosiation class attributes and methods
domain_Assosiation_type: Property = Property(name="type", type=StringType)
domain_Assosiation.attributes={domain_Assosiation_type}

# domain_TypeReference class attributes and methods

# domain_Type class attributes and methods

# Secured class attributes and methods

# domain_Parameter class attributes and methods
domain_Parameter_uid: Property = Property(name="uid", type=StringType)
domain_Parameter_name: Property = Property(name="name", type=StringType)
domain_Parameter_order: Property = Property(name="order", type=IntegerType)
domain_Parameter.attributes={domain_Parameter_order, domain_Parameter_name, domain_Parameter_uid}

# domain_ReturnValue class attributes and methods
domain_ReturnValue_uid: Property = Property(name="uid", type=StringType)
domain_ReturnValue.attributes={domain_ReturnValue_uid}

# domain_Enumarator class attributes and methods

# domain_EnumAttribute class attributes and methods
domain_EnumAttribute_uid: Property = Property(name="uid", type=StringType)
domain_EnumAttribute_name: Property = Property(name="name", type=StringType)
domain_EnumAttribute_value: Property = Property(name="value", type=StringType)
domain_EnumAttribute.attributes={domain_EnumAttribute_value, domain_EnumAttribute_uid, domain_EnumAttribute_name}

# domain_Types class attributes and methods
domain_Types_uid: Property = Property(name="uid", type=StringType)
domain_Types_name: Property = Property(name="name", type=StringType)
domain_Types.attributes={domain_Types_uid, domain_Types_name}

# domain_Form class attributes and methods
domain_Form_uid: Property = Property(name="uid", type=StringType)
domain_Form_name: Property = Property(name="name", type=StringType)
domain_Form.attributes={domain_Form_name, domain_Form_uid}

# domain_FormView class attributes and methods
domain_FormView_uid: Property = Property(name="uid", type=StringType)
domain_FormView_name: Property = Property(name="name", type=StringType)
domain_FormView.attributes={domain_FormView_uid, domain_FormView_name}

# domain_Views class attributes and methods
domain_Views_uid: Property = Property(name="uid", type=StringType)
domain_Views.attributes={domain_Views_uid}

# domain_FormDataControls class attributes and methods
domain_FormDataControls_uid: Property = Property(name="uid", type=StringType)
domain_FormDataControls_name: Property = Property(name="name", type=StringType)
domain_FormDataControls.attributes={domain_FormDataControls_uid, domain_FormDataControls_name}

# domain_FormParameter class attributes and methods
domain_FormParameter_uid: Property = Property(name="uid", type=StringType)
domain_FormParameter_name: Property = Property(name="name", type=StringType)
domain_FormParameter.attributes={domain_FormParameter_name, domain_FormParameter_uid}

# domain_TabPagesInheritance class attributes and methods
domain_TabPagesInheritance_uid: Property = Property(name="uid", type=StringType)
domain_TabPagesInheritance.attributes={domain_TabPagesInheritance_uid}

# domain_MenuDefinition class attributes and methods
domain_MenuDefinition_uid: Property = Property(name="uid", type=StringType)
domain_MenuDefinition_name: Property = Property(name="name", type=StringType)
domain_MenuDefinition.attributes={domain_MenuDefinition_name, domain_MenuDefinition_uid}

# domain_Orderable class attributes and methods
domain_Orderable_order: Property = Property(name="order", type=IntegerType)
domain_Orderable.attributes={domain_Orderable_order}

# domain_MultiLangLabel class attributes and methods

# domain_Context class attributes and methods

# domain_CanvasFrame class attributes and methods
domain_CanvasFrame_uid: Property = Property(name="uid", type=StringType)
domain_CanvasFrame_name: Property = Property(name="name", type=StringType)
domain_CanvasFrame.attributes={domain_CanvasFrame_name, domain_CanvasFrame_uid}

# domain_ViewInheritance class attributes and methods
domain_ViewInheritance_uid: Property = Property(name="uid", type=StringType)
domain_ViewInheritance.attributes={domain_ViewInheritance_uid}

# domain_ViewElement class attributes and methods

# domain_DefaultCavas class attributes and methods
domain_DefaultCavas_defaultCanvas: Property = Property(name="defaultCanvas", type=BooleanType)
domain_DefaultCavas.attributes={domain_DefaultCavas_defaultCanvas}

# NickNamed class attributes and methods

# domain_PopupCanvas class attributes and methods
domain_PopupCanvas_modal: Property = Property(name="modal", type=BooleanType)
domain_PopupCanvas.attributes={domain_PopupCanvas_modal}

# CanvasFrame class attributes and methods

# ViewPortHolder class attributes and methods

# DefaultCavas class attributes and methods

# MultiLangLabel class attributes and methods

# FlexFields class attributes and methods

# StyleElement class attributes and methods

# domain_ViewPortHolder class attributes and methods

# domain_Window class attributes and methods

# domain_MenuView class attributes and methods
domain_MenuView_uid: Property = Property(name="uid", type=StringType)
domain_MenuView.attributes={domain_MenuView_uid}

# domain_Canvas class attributes and methods

# domain_TabPage class attributes and methods

# Orderable class attributes and methods

# domain_ViewPort class attributes and methods
domain_ViewPort_uid: Property = Property(name="uid", type=StringType)
domain_ViewPort_name: Property = Property(name="name", type=StringType)
domain_ViewPort.attributes={domain_ViewPort_uid, domain_ViewPort_name}

# ViewElement class attributes and methods

# domain_ViewPortTrigger class attributes and methods
domain_ViewPortTrigger_uid: Property = Property(name="uid", type=StringType)
domain_ViewPortTrigger.attributes={domain_ViewPortTrigger_uid}

# domain_ViewArea class attributes and methods
domain_ViewArea_uid: Property = Property(name="uid", type=StringType)
domain_ViewArea_name: Property = Property(name="name", type=StringType)
domain_ViewArea.attributes={domain_ViewArea_name, domain_ViewArea_uid}

# domain_TabCanvas class attributes and methods
domain_TabCanvas_orientation: Property = Property(name="orientation", type=StringType)
domain_TabCanvas.attributes={domain_TabCanvas_orientation}

# domain_CanvasView class attributes and methods
domain_CanvasView_uid: Property = Property(name="uid", type=StringType)
domain_CanvasView.attributes={domain_CanvasView_uid}

# Trigger class attributes and methods

# domain_Controls class attributes and methods
domain_Controls_uid: Property = Property(name="uid", type=StringType)
domain_Controls.attributes={domain_Controls_uid}

# domain_LayerHolder class attributes and methods

# domain_LinkToMessage class attributes and methods
domain_LinkToMessage_uid: Property = Property(name="uid", type=StringType)
domain_LinkToMessage.attributes={domain_LinkToMessage_uid}

# domain_InputElement class attributes and methods

# domain_MessageElement class attributes and methods
domain_MessageElement_label: Property = Property(name="label", type=StringType)
domain_MessageElement.attributes={domain_MessageElement_label}

# domain_LinkToLabel class attributes and methods
domain_LinkToLabel_uid: Property = Property(name="uid", type=StringType)
domain_LinkToLabel.attributes={domain_LinkToLabel_uid}

# domain_ChildrenHolder class attributes and methods

# domain_Uielement class attributes and methods
domain_Uielement_uid: Property = Property(name="uid", type=StringType)
domain_Uielement.attributes={domain_Uielement_uid}

# domain_ContextParameter class attributes and methods
domain_ContextParameter_uid: Property = Property(name="uid", type=StringType)
domain_ContextParameter_operation: Property = Property(name="operation", type=StringType)
domain_ContextParameter.attributes={domain_ContextParameter_operation, domain_ContextParameter_uid}

# domain_ContextValue class attributes and methods
domain_ContextValue_uid: Property = Property(name="uid", type=StringType)
domain_ContextValue_constant: Property = Property(name="constant", type=BooleanType)
domain_ContextValue_value: Property = Property(name="value", type=StringType)
domain_ContextValue.attributes={domain_ContextValue_value, domain_ContextValue_constant, domain_ContextValue_uid}

# domain_ExpressionPart class attributes and methods
domain_ExpressionPart_order: Property = Property(name="order", type=IntegerType)
domain_ExpressionPart_expressionType: Property = Property(name="expressionType", type=StringType)
domain_ExpressionPart_uid: Property = Property(name="uid", type=StringType)
domain_ExpressionPart.attributes={domain_ExpressionPart_order, domain_ExpressionPart_expressionType, domain_ExpressionPart_uid}

# domain_Label class attributes and methods
domain_Label_label: Property = Property(name="label", type=StringType)
domain_Label.attributes={domain_Label_label}

# domain_ContextParameters class attributes and methods

# ContextValue class attributes and methods

# ContextParameters class attributes and methods

# domain_StyleElement class attributes and methods

# domain_StyleClass class attributes and methods

# domain_NickNamed class attributes and methods
domain_NickNamed_nickname: Property = Property(name="nickname", type=StringType)
domain_NickNamed.attributes={domain_NickNamed_nickname}

# Context class attributes and methods

# domain_EnabledUIItem class attributes and methods

# EnabledUIItem class attributes and methods

# MenuHolder class attributes and methods

# domain_AreaRef class attributes and methods
domain_AreaRef_group: Property = Property(name="group", type=IntegerType)
domain_AreaRef.attributes={domain_AreaRef_group}

# domain_FlexFields class attributes and methods

# domain_FlexField class attributes and methods

# domain_Formatable class attributes and methods
domain_Formatable_format: Property = Property(name="format", type=StringType)
domain_Formatable.attributes={domain_Formatable_format}

# domain_SourcesPointer class attributes and methods

# Uielement class attributes and methods

# domain_DataControl class attributes and methods
domain_DataControl_uid: Property = Property(name="uid", type=StringType)
domain_DataControl_name: Property = Property(name="name", type=StringType)
domain_DataControl.attributes={domain_DataControl_uid, domain_DataControl_name}

# domain_Selection class attributes and methods

# domain_ItemIcon class attributes and methods

# domain_OptionSelection class attributes and methods

# InputElement class attributes and methods

# ChildrenHolder class attributes and methods

# domain_InputText class attributes and methods

# Formatable class attributes and methods

# domain_Password class attributes and methods

# SourcesPointer class attributes and methods

# domain_CheckBox class attributes and methods

# domain_DropDownSelection class attributes and methods
domain_DropDownSelection_initialOptionValue: Property = Property(name="initialOptionValue", type=StringType)
domain_DropDownSelection.attributes={domain_DropDownSelection_initialOptionValue}

# OptionSelection class attributes and methods

# domain_Image class attributes and methods

# domain_Date class attributes and methods

# domain_Button class attributes and methods
domain_Button_label: Property = Property(name="label", type=StringType)
domain_Button.attributes={domain_Button_label}

# ItemIcon class attributes and methods

# domain_OutputText class attributes and methods

# domain_Table class attributes and methods
domain_Table_label: Property = Property(name="label", type=StringType)
domain_Table_rowNumber: Property = Property(name="rowNumber", type=IntegerType)
domain_Table.attributes={domain_Table_label, domain_Table_rowNumber}

# domain_Menu class attributes and methods
domain_Menu_fakeName: Property = Property(name="fakeName", type=StringType)
domain_Menu.attributes={domain_Menu_fakeName}

# domain_Tree class attributes and methods
domain_Tree_label: Property = Property(name="label", type=StringType)
domain_Tree.attributes={domain_Tree_label}

# domain_Column class attributes and methods
domain_Column_label: Property = Property(name="label", type=StringType)
domain_Column_uid: Property = Property(name="uid", type=StringType)
domain_Column.attributes={domain_Column_uid, domain_Column_label}

# domain_Dependency class attributes and methods
domain_Dependency_uid: Property = Property(name="uid", type=StringType)
domain_Dependency_name: Property = Property(name="name", type=StringType)
domain_Dependency.attributes={domain_Dependency_uid, domain_Dependency_name}

# domain_Trigger class attributes and methods

# MethodPointer class attributes and methods

# domain_PREFormTrigger class attributes and methods
domain_PREFormTrigger_uid: Property = Property(name="uid", type=StringType)
domain_PREFormTrigger.attributes={domain_PREFormTrigger_uid}

# domain_PREQueryTrigger class attributes and methods
domain_PREQueryTrigger_uid: Property = Property(name="uid", type=StringType)
domain_PREQueryTrigger.attributes={domain_PREQueryTrigger_uid}

# domain_POSTQueryTrigger class attributes and methods
domain_POSTQueryTrigger_uid: Property = Property(name="uid", type=StringType)
domain_POSTQueryTrigger.attributes={domain_POSTQueryTrigger_uid}

# domain_PREInsertTrigger class attributes and methods
domain_PREInsertTrigger_uid: Property = Property(name="uid", type=StringType)
domain_PREInsertTrigger.attributes={domain_PREInsertTrigger_uid}

# domain_Root class attributes and methods
domain_Root_uid: Property = Property(name="uid", type=StringType)
domain_Root_name: Property = Property(name="name", type=StringType)
domain_Root.attributes={domain_Root_uid, domain_Root_name}

# domain_Relation class attributes and methods
domain_Relation_uid: Property = Property(name="uid", type=StringType)
domain_Relation_name: Property = Property(name="name", type=StringType)
domain_Relation_isTree: Property = Property(name="isTree", type=BooleanType)
domain_Relation.attributes={domain_Relation_name, domain_Relation_isTree, domain_Relation_uid}

# domain_POSTCreateTrigger class attributes and methods
domain_POSTCreateTrigger_uid: Property = Property(name="uid", type=StringType)
domain_POSTCreateTrigger.attributes={domain_POSTCreateTrigger_uid}

# domain_PREUpdateTrigger class attributes and methods
domain_PREUpdateTrigger_uid: Property = Property(name="uid", type=StringType)
domain_PREUpdateTrigger.attributes={domain_PREUpdateTrigger_uid}

# domain_ProxiesList class attributes and methods

# domain_CreateTrigger class attributes and methods
domain_CreateTrigger_uid: Property = Property(name="uid", type=StringType)
domain_CreateTrigger.attributes={domain_CreateTrigger_uid}

# ProxiesList class attributes and methods

# domain_PREDeleteTrigger class attributes and methods
domain_PREDeleteTrigger_uid: Property = Property(name="uid", type=StringType)
domain_PREDeleteTrigger.attributes={domain_PREDeleteTrigger_uid}

# domain_InsertTrigger class attributes and methods
domain_InsertTrigger_uid: Property = Property(name="uid", type=StringType)
domain_InsertTrigger.attributes={domain_InsertTrigger_uid}

# domain_UpdateTrigger class attributes and methods
domain_UpdateTrigger_uid: Property = Property(name="uid", type=StringType)
domain_UpdateTrigger.attributes={domain_UpdateTrigger_uid}

# domain_DeleteTrigger class attributes and methods
domain_DeleteTrigger_uid: Property = Property(name="uid", type=StringType)
domain_DeleteTrigger.attributes={domain_DeleteTrigger_uid}

# domain_SearchTrigger class attributes and methods
domain_SearchTrigger_uid: Property = Property(name="uid", type=StringType)
domain_SearchTrigger.attributes={domain_SearchTrigger_uid}

# domain_FormVariable class attributes and methods
domain_FormVariable_uid: Property = Property(name="uid", type=StringType)
domain_FormVariable_name: Property = Property(name="name", type=StringType)
domain_FormVariable.attributes={domain_FormVariable_uid, domain_FormVariable_name}

# domain_ArtificialField class attributes and methods
domain_ArtificialField_uid: Property = Property(name="uid", type=StringType)
domain_ArtificialField_name: Property = Property(name="name", type=StringType)
domain_ArtificialField.attributes={domain_ArtificialField_name, domain_ArtificialField_uid}

# domain_Orders class attributes and methods
domain_Orders_uid: Property = Property(name="uid", type=StringType)
domain_Orders.attributes={domain_Orders_uid}

# domain_OrderBy class attributes and methods
domain_OrderBy_uid: Property = Property(name="uid", type=StringType)
domain_OrderBy_order: Property = Property(name="order", type=StringType)
domain_OrderBy.attributes={domain_OrderBy_uid, domain_OrderBy_order}

# domain_EnterpriseInfrastructure class attributes and methods
domain_EnterpriseInfrastructure_uid: Property = Property(name="uid", type=StringType)
domain_EnterpriseInfrastructure.attributes={domain_EnterpriseInfrastructure_uid}

# domain_Datacenter class attributes and methods
domain_Datacenter_name: Property = Property(name="name", type=StringType)
domain_Datacenter_uid: Property = Property(name="uid", type=StringType)
domain_Datacenter.attributes={domain_Datacenter_name, domain_Datacenter_uid}

# domain_InfrastructureConnection class attributes and methods
domain_InfrastructureConnection_uid: Property = Property(name="uid", type=StringType)
domain_InfrastructureConnection.attributes={domain_InfrastructureConnection_uid}

# domain_Subsystem class attributes and methods
domain_Subsystem_uid: Property = Property(name="uid", type=StringType)
domain_Subsystem_name: Property = Property(name="name", type=StringType)
domain_Subsystem.attributes={domain_Subsystem_uid, domain_Subsystem_name}

# domain_InfrastructureLayer class attributes and methods
domain_InfrastructureLayer_uid: Property = Property(name="uid", type=StringType)
domain_InfrastructureLayer_name: Property = Property(name="name", type=StringType)
domain_InfrastructureLayer.attributes={domain_InfrastructureLayer_name, domain_InfrastructureLayer_uid}

# domain_Server class attributes and methods

# InfrastructureComponent class attributes and methods

# domain_Router class attributes and methods

# domain_Hub class attributes and methods

# domain_Storage class attributes and methods

# domain_InfrastructureComponent class attributes and methods
domain_InfrastructureComponent_uid: Property = Property(name="uid", type=StringType)
domain_InfrastructureComponent_name: Property = Property(name="name", type=StringType)
domain_InfrastructureComponent.attributes={domain_InfrastructureComponent_name, domain_InfrastructureComponent_uid}

# domain_MenuFolder class attributes and methods
domain_MenuFolder_uid: Property = Property(name="uid", type=StringType)
domain_MenuFolder_name: Property = Property(name="name", type=StringType)
domain_MenuFolder_extensionPoint: Property = Property(name="extensionPoint", type=BooleanType)
domain_MenuFolder.attributes={domain_MenuFolder_name, domain_MenuFolder_uid, domain_MenuFolder_extensionPoint}

# domain_MenuHolder class attributes and methods

# domain_MenuExtensionRef class attributes and methods

# domain_MenuElement class attributes and methods
domain_MenuElement_uid: Property = Property(name="uid", type=StringType)
domain_MenuElement_name: Property = Property(name="name", type=StringType)
domain_MenuElement.attributes={domain_MenuElement_name, domain_MenuElement_uid}

# domain_ServerClaster class attributes and methods

# domain_MenuExtensionPoint class attributes and methods

# MenuExtensionRef class attributes and methods

# domain_SubMenu class attributes and methods

# domain_MenuSeparator class attributes and methods

# domain_MenuItem class attributes and methods

# MenuElement class attributes and methods

# Relationships
domainArtifacts0: BinaryAssociation = BinaryAssociation(
    name="domainArtifacts0",
    ends={
        Property(name="DomainArtifacts", type=domain_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=domain_DomainArtifacts, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domainTypes1: BinaryAssociation = BinaryAssociation(
    name="domainTypes1",
    ends={
        Property(name="DomainTypes", type=domain_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="parent2", type=domain_DomainTypes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domainApplications3: BinaryAssociation = BinaryAssociation(
    name="domainApplications3",
    ends={
        Property(name="DomainApplications", type=domain_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="parent4", type=domain_DomainApplications, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
any5: BinaryAssociation = BinaryAssociation(
    name="any5",
    ends={
        Property(name="domain_EObject", type=domain_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Domain", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hint7: BinaryAssociation = BinaryAssociation(
    name="hint7",
    ends={
        Property(name="domain_GenerationHint", type=domain_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Classifier8", type=domain_GenerationHint, multiplicity=Multiplicity(0, 1))
    }
)
grants9: BinaryAssociation = BinaryAssociation(
    name="grants9",
    ends={
        Property(name="domain_GrantAccess", type=domain_Secured, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Secured", type=domain_GrantAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationRef10: BinaryAssociation = BinaryAssociation(
    name="applicationRef10",
    ends={
        Property(name="domain_DomainApplication", type=domain_GrantAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_GrantAccess11", type=domain_DomainApplication, multiplicity=Multiplicity(0, 1))
    }
)
roleRef12: BinaryAssociation = BinaryAssociation(
    name="roleRef12",
    ends={
        Property(name="domain_Role", type=domain_GrantAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_GrantAccess13", type=domain_Role, multiplicity=Multiplicity(0, 1))
    }
)
classifiers6: BinaryAssociation = BinaryAssociation(
    name="classifiers6",
    ends={
        Property(name="domain_Classifier", type=domain_Categorized, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Categorized", type=domain_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domainArtifact15: BinaryAssociation = BinaryAssociation(
    name="domainArtifact15",
    ends={
        Property(name="DomainArtifact", type=domain_DomainArtifacts, multiplicity=Multiplicity(1, 1)),
        Property(name="parent16", type=domain_DomainArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typesrepository17: BinaryAssociation = BinaryAssociation(
    name="typesrepository17",
    ends={
        Property(name="TypesRepository", type=domain_DomainTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="parent18", type=domain_TypesRepository, multiplicity=Multiplicity(0, 1))
    }
)
parent19: BinaryAssociation = BinaryAssociation(
    name="parent19",
    ends={
        Property(name="Domain20", type=domain_DomainTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="domainTypes", type=domain_Domain, multiplicity=Multiplicity(0, 1))
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="Domain", type=domain_DomainArtifacts, multiplicity=Multiplicity(1, 1)),
        Property(name="domainArtifacts", type=domain_Domain, multiplicity=Multiplicity(0, 1))
    }
)
application25: BinaryAssociation = BinaryAssociation(
    name="application25",
    ends={
        Property(name="Application", type=domain_DomainApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="parent26", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
parent27: BinaryAssociation = BinaryAssociation(
    name="parent27",
    ends={
        Property(name="DomainApplications28", type=domain_DomainApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="applications", type=domain_DomainApplications, multiplicity=Multiplicity(0, 1))
    }
)
parent29: BinaryAssociation = BinaryAssociation(
    name="parent29",
    ends={
        Property(name="DomainArtifacts30", type=domain_DomainArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="domainArtifact", type=domain_DomainArtifacts, multiplicity=Multiplicity(0, 1))
    }
)
artifact31: BinaryAssociation = BinaryAssociation(
    name="artifact31",
    ends={
        Property(name="Artifacts", type=domain_DomainArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="parent32", type=domain_Artifacts, multiplicity=Multiplicity(0, 1))
    }
)
applications21: BinaryAssociation = BinaryAssociation(
    name="applications21",
    ends={
        Property(name="DomainApplication", type=domain_DomainApplications, multiplicity=Multiplicity(1, 1)),
        Property(name="parent22", type=domain_DomainApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent23: BinaryAssociation = BinaryAssociation(
    name="parent23",
    ends={
        Property(name="Domain24", type=domain_DomainApplications, multiplicity=Multiplicity(1, 1)),
        Property(name="domainApplications", type=domain_Domain, multiplicity=Multiplicity(0, 1))
    }
)
artifacts33: BinaryAssociation = BinaryAssociation(
    name="artifacts33",
    ends={
        Property(name="Artifact", type=domain_Artifacts, multiplicity=Multiplicity(1, 1)),
        Property(name="parent34", type=domain_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent35: BinaryAssociation = BinaryAssociation(
    name="parent35",
    ends={
        Property(name="DomainArtifact36", type=domain_Artifacts, multiplicity=Multiplicity(1, 1)),
        Property(name="artifact", type=domain_DomainArtifact, multiplicity=Multiplicity(0, 1))
    }
)
any37: BinaryAssociation = BinaryAssociation(
    name="any37",
    ends={
        Property(name="domain_EObject38", type=domain_Artifacts, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Artifacts", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent39: BinaryAssociation = BinaryAssociation(
    name="parent39",
    ends={
        Property(name="Artifacts40", type=domain_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="artifacts", type=domain_Artifacts, multiplicity=Multiplicity(0, 1))
    }
)
configVariables41: BinaryAssociation = BinaryAssociation(
    name="configVariables41",
    ends={
        Property(name="ConfigVariable", type=domain_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="parent42", type=domain_ConfigVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configHashes43: BinaryAssociation = BinaryAssociation(
    name="configHashes43",
    ends={
        Property(name="ConfigHash", type=domain_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="parent44", type=domain_ConfigHash, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelQuery45: BinaryAssociation = BinaryAssociation(
    name="modelQuery45",
    ends={
        Property(name="ModelQuery", type=domain_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="parent46", type=domain_ModelQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiers47: BinaryAssociation = BinaryAssociation(
    name="specifiers47",
    ends={
        Property(name="Specifier", type=domain_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="parent48", type=domain_Specifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="Artifact52", type=domain_ConfigVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="configVariables", type=domain_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
hints49: BinaryAssociation = BinaryAssociation(
    name="hints49",
    ends={
        Property(name="domain_GenerationHint50", type=domain_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Artifact", type=domain_GenerationHint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent55: BinaryAssociation = BinaryAssociation(
    name="parent55",
    ends={
        Property(name="Artifact56", type=domain_ModelQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="modelQuery", type=domain_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
parameters57: BinaryAssociation = BinaryAssociation(
    name="parameters57",
    ends={
        Property(name="QueryParameter", type=domain_ModelQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="parent58", type=domain_QueryParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent59: BinaryAssociation = BinaryAssociation(
    name="parent59",
    ends={
        Property(name="ModelQuery60", type=domain_QueryParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=domain_ModelQuery, multiplicity=Multiplicity(0, 1))
    }
)
parent53: BinaryAssociation = BinaryAssociation(
    name="parent53",
    ends={
        Property(name="Artifact54", type=domain_ConfigHash, multiplicity=Multiplicity(1, 1)),
        Property(name="configHashes", type=domain_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
parent65: BinaryAssociation = BinaryAssociation(
    name="parent65",
    ends={
        Property(name="Specifier66", type=domain_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="options", type=domain_Specifier, multiplicity=Multiplicity(0, 1))
    }
)
applicationRecipes67: BinaryAssociation = BinaryAssociation(
    name="applicationRecipes67",
    ends={
        Property(name="ApplicationRecipes", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent68", type=domain_ApplicationRecipes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationMappers69: BinaryAssociation = BinaryAssociation(
    name="applicationMappers69",
    ends={
        Property(name="ApplicationMappers", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent70", type=domain_ApplicationMappers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationUILayer71: BinaryAssociation = BinaryAssociation(
    name="applicationUILayer71",
    ends={
        Property(name="ApplicationUILayer", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent72", type=domain_ApplicationUILayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationInfrastructureLayer73: BinaryAssociation = BinaryAssociation(
    name="applicationInfrastructureLayer73",
    ends={
        Property(name="ApplicationInfrastructureLayer", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent74", type=domain_ApplicationInfrastructureLayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent61: BinaryAssociation = BinaryAssociation(
    name="parent61",
    ends={
        Property(name="Artifact62", type=domain_Specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiers", type=domain_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
options63: BinaryAssociation = BinaryAssociation(
    name="options63",
    ends={
        Property(name="Option", type=domain_Specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="parent64", type=domain_Option, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent81: BinaryAssociation = BinaryAssociation(
    name="parent81",
    ends={
        Property(name="DomainApplication82", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application", type=domain_DomainApplication, multiplicity=Multiplicity(0, 1))
    }
)
any83: BinaryAssociation = BinaryAssociation(
    name="any83",
    ends={
        Property(name="domain_EObject84", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Application", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent85: BinaryAssociation = BinaryAssociation(
    name="parent85",
    ends={
        Property(name="Application86", type=domain_ApplicationMessages, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationMessages", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
messages87: BinaryAssociation = BinaryAssociation(
    name="messages87",
    ends={
        Property(name="Messages", type=domain_ApplicationMessages, multiplicity=Multiplicity(1, 1)),
        Property(name="parent88", type=domain_Messages, multiplicity=Multiplicity(0, 1))
    }
)
applicationStyle75: BinaryAssociation = BinaryAssociation(
    name="applicationStyle75",
    ends={
        Property(name="ApplicationStyle", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent76", type=domain_ApplicationStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationRole77: BinaryAssociation = BinaryAssociation(
    name="applicationRole77",
    ends={
        Property(name="ApplicationRole", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent78", type=domain_ApplicationRole, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applicationMessages79: BinaryAssociation = BinaryAssociation(
    name="applicationMessages79",
    ends={
        Property(name="ApplicationMessages", type=domain_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="parent80", type=domain_ApplicationMessages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles91: BinaryAssociation = BinaryAssociation(
    name="roles91",
    ends={
        Property(name="parent92", type=domain_Roles, multiplicity=Multiplicity(0, 1)),
        Property(name="Roles", type=domain_ApplicationRole, multiplicity=Multiplicity(1, 1))
    }
)
parent93: BinaryAssociation = BinaryAssociation(
    name="parent93",
    ends={
        Property(name="Application94", type=domain_ApplicationStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationStyle", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
stylesPackage95: BinaryAssociation = BinaryAssociation(
    name="stylesPackage95",
    ends={
        Property(name="StylesPackage", type=domain_ApplicationStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="parent96", type=domain_StylesPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent89: BinaryAssociation = BinaryAssociation(
    name="parent89",
    ends={
        Property(name="Application90", type=domain_ApplicationRole, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationRole", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
parent101: BinaryAssociation = BinaryAssociation(
    name="parent101",
    ends={
        Property(name="Application102", type=domain_ApplicationUILayer, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationUILayer", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
applicationUIPackages103: BinaryAssociation = BinaryAssociation(
    name="applicationUIPackages103",
    ends={
        Property(name="ApplicationUIPackage", type=domain_ApplicationUILayer, multiplicity=Multiplicity(1, 1)),
        Property(name="parent104", type=domain_ApplicationUIPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent97: BinaryAssociation = BinaryAssociation(
    name="parent97",
    ends={
        Property(name="ApplicationStyle98", type=domain_StylesPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesPackage", type=domain_ApplicationStyle, multiplicity=Multiplicity(0, 1))
    }
)
styles99: BinaryAssociation = BinaryAssociation(
    name="styles99",
    ends={
        Property(name="Styles", type=domain_StylesPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parent100", type=domain_Styles, multiplicity=Multiplicity(0, 1))
    }
)
parent109: BinaryAssociation = BinaryAssociation(
    name="parent109",
    ends={
        Property(name="Application110", type=domain_ApplicationRecipes, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationRecipes", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
recipes111: BinaryAssociation = BinaryAssociation(
    name="recipes111",
    ends={
        Property(name="ApplicationRecipe", type=domain_ApplicationRecipes, multiplicity=Multiplicity(1, 1)),
        Property(name="parent112", type=domain_ApplicationRecipe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recipes113: BinaryAssociation = BinaryAssociation(
    name="recipes113",
    ends={
        Property(name="Recipes", type=domain_ApplicationRecipe, multiplicity=Multiplicity(1, 1)),
        Property(name="parent114", type=domain_Recipes, multiplicity=Multiplicity(0, 1))
    }
)
parent115: BinaryAssociation = BinaryAssociation(
    name="parent115",
    ends={
        Property(name="ApplicationRecipes116", type=domain_ApplicationRecipe, multiplicity=Multiplicity(1, 1)),
        Property(name="recipes", type=domain_ApplicationRecipes, multiplicity=Multiplicity(0, 1))
    }
)
parent105: BinaryAssociation = BinaryAssociation(
    name="parent105",
    ends={
        Property(name="ApplicationUILayer106", type=domain_ApplicationUIPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationUIPackages", type=domain_ApplicationUILayer, multiplicity=Multiplicity(0, 1))
    }
)
uipackage107: BinaryAssociation = BinaryAssociation(
    name="uipackage107",
    ends={
        Property(name="UIPackage", type=domain_ApplicationUIPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parent108", type=domain_UIPackage, multiplicity=Multiplicity(0, 1))
    }
)
parent117: BinaryAssociation = BinaryAssociation(
    name="parent117",
    ends={
        Property(name="Application118", type=domain_ApplicationMappers, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationMappers", type=domain_Application, multiplicity=Multiplicity(0, 1))
    }
)
mappers119: BinaryAssociation = BinaryAssociation(
    name="mappers119",
    ends={
        Property(name="ApplicationMapper", type=domain_ApplicationMappers, multiplicity=Multiplicity(1, 1)),
        Property(name="parent120", type=domain_ApplicationMapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapper121: BinaryAssociation = BinaryAssociation(
    name="mapper121",
    ends={
        Property(name="Mappers", type=domain_ApplicationMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="parent122", type=domain_Mappers, multiplicity=Multiplicity(0, 1))
    }
)
parent123: BinaryAssociation = BinaryAssociation(
    name="parent123",
    ends={
        Property(name="ApplicationMappers124", type=domain_ApplicationMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="mappers", type=domain_ApplicationMappers, multiplicity=Multiplicity(0, 1))
    }
)
methodRef125: BinaryAssociation = BinaryAssociation(
    name="methodRef125",
    ends={
        Property(name="domain_Operation", type=domain_MethodPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MethodPointer", type=domain_Operation, multiplicity=Multiplicity(0, 1))
    }
)
parent126: BinaryAssociation = BinaryAssociation(
    name="parent126",
    ends={
        Property(name="ApplicationMessages127", type=domain_Messages, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=domain_ApplicationMessages, multiplicity=Multiplicity(0, 1))
    }
)
messageLibraries128: BinaryAssociation = BinaryAssociation(
    name="messageLibraries128",
    ends={
        Property(name="domain_MessageLibrary", type=domain_Messages, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Messages", type=domain_MessageLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
languages129: BinaryAssociation = BinaryAssociation(
    name="languages129",
    ends={
        Property(name="domain_Language", type=domain_Messages, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Messages130", type=domain_Language, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any131: BinaryAssociation = BinaryAssociation(
    name="any131",
    ends={
        Property(name="domain_EObject133", type=domain_Messages, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Messages132", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
libLanguages134: BinaryAssociation = BinaryAssociation(
    name="libLanguages134",
    ends={
        Property(name="domain_LanguageRef", type=domain_MessageLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MessageLibrary135", type=domain_LanguageRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages136: BinaryAssociation = BinaryAssociation(
    name="messages136",
    ends={
        Property(name="domain_Message", type=domain_MessageLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MessageLibrary137", type=domain_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lang138: BinaryAssociation = BinaryAssociation(
    name="lang138",
    ends={
        Property(name="domain_Language140", type=domain_LanguageRef, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_LanguageRef139", type=domain_Language, multiplicity=Multiplicity(0, 1))
    }
)
translatioins141: BinaryAssociation = BinaryAssociation(
    name="translatioins141",
    ends={
        Property(name="domain_Translation", type=domain_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Message142", type=domain_Translation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lang143: BinaryAssociation = BinaryAssociation(
    name="lang143",
    ends={
        Property(name="domain_LanguageRef145", type=domain_Translation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Translation144", type=domain_LanguageRef, multiplicity=Multiplicity(0, 1))
    }
)
parent146: BinaryAssociation = BinaryAssociation(
    name="parent146",
    ends={
        Property(name="ApplicationRole147", type=domain_Roles, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=domain_ApplicationRole, multiplicity=Multiplicity(0, 1))
    }
)
roles148: BinaryAssociation = BinaryAssociation(
    name="roles148",
    ends={
        Property(name="domain_Role149", type=domain_Roles, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Roles", type=domain_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups150: BinaryAssociation = BinaryAssociation(
    name="groups150",
    ends={
        Property(name="domain_Group", type=domain_Roles, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Roles151", type=domain_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any152: BinaryAssociation = BinaryAssociation(
    name="any152",
    ends={
        Property(name="domain_EObject154", type=domain_Roles, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Roles153", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
group2Role158: BinaryAssociation = BinaryAssociation(
    name="group2Role158",
    ends={
        Property(name="domain_Role160", type=domain_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Group159", type=domain_Role, multiplicity=Multiplicity(0, 9999))
    }
)
parent161: BinaryAssociation = BinaryAssociation(
    name="parent161",
    ends={
        Property(name="StylesPackage162", type=domain_Styles, multiplicity=Multiplicity(1, 1)),
        Property(name="styles", type=domain_StylesPackage, multiplicity=Multiplicity(0, 1))
    }
)
libraries163: BinaryAssociation = BinaryAssociation(
    name="libraries163",
    ends={
        Property(name="domain_StyleLibrary", type=domain_Styles, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Styles", type=domain_StyleLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any164: BinaryAssociation = BinaryAssociation(
    name="any164",
    ends={
        Property(name="domain_EObject166", type=domain_Styles, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Styles165", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
group2Group156: BinaryAssociation = BinaryAssociation(
    name="group2Group156",
    ends={
        Property(name="domain_Group157", type=domain_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Group155", type=domain_Group, multiplicity=Multiplicity(0, 9999))
    }
)
mappers169: BinaryAssociation = BinaryAssociation(
    name="mappers169",
    ends={
        Property(name="Mapper", type=domain_Mappers, multiplicity=Multiplicity(1, 1)),
        Property(name="parent170", type=domain_Mapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent171: BinaryAssociation = BinaryAssociation(
    name="parent171",
    ends={
        Property(name="ApplicationMapper172", type=domain_Mappers, multiplicity=Multiplicity(1, 1)),
        Property(name="mapper", type=domain_ApplicationMapper, multiplicity=Multiplicity(0, 1))
    }
)
any173: BinaryAssociation = BinaryAssociation(
    name="any173",
    ends={
        Property(name="domain_EObject174", type=domain_Mappers, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Mappers", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent175: BinaryAssociation = BinaryAssociation(
    name="parent175",
    ends={
        Property(name="Mappers177", type=domain_Mapper, multiplicity=Multiplicity(1, 1)),
        Property(name="mappers176", type=domain_Mappers, multiplicity=Multiplicity(0, 1))
    }
)
styles167: BinaryAssociation = BinaryAssociation(
    name="styles167",
    ends={
        Property(name="domain_StyleSet", type=domain_StyleLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_StyleLibrary168", type=domain_StyleSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role182: BinaryAssociation = BinaryAssociation(
    name="role182",
    ends={
        Property(name="domain_EObject183", type=domain_RoleMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_RoleMapper", type=domain_EObject, multiplicity=Multiplicity(0, 1))
    }
)
recipe184: BinaryAssociation = BinaryAssociation(
    name="recipe184",
    ends={
        Property(name="Recipe", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="parent185", type=domain_Recipe, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stylePackage178: BinaryAssociation = BinaryAssociation(
    name="stylePackage178",
    ends={
        Property(name="domain_StylesPackage", type=domain_CSSMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_CSSMapper", type=domain_StylesPackage, multiplicity=Multiplicity(0, 1))
    }
)
styleLibrary179: BinaryAssociation = BinaryAssociation(
    name="styleLibrary179",
    ends={
        Property(name="domain_StyleLibrary181", type=domain_CSSMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_CSSMapper180", type=domain_StyleLibrary, multiplicity=Multiplicity(0, 1))
    }
)
deployment192: BinaryAssociation = BinaryAssociation(
    name="deployment192",
    ends={
        Property(name="domain_DeploymentSequence", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Recipes193", type=domain_DeploymentSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configExtension194: BinaryAssociation = BinaryAssociation(
    name="configExtension194",
    ends={
        Property(name="domain_ConfigExtension", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Recipes195", type=domain_ConfigExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any196: BinaryAssociation = BinaryAssociation(
    name="any196",
    ends={
        Property(name="domain_EObject198", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Recipes197", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deploymentComponents199: BinaryAssociation = BinaryAssociation(
    name="deploymentComponents199",
    ends={
        Property(name="domain_DeploymentComponents", type=domain_DeploymentSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentSequence200", type=domain_DeploymentComponents, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configurations186: BinaryAssociation = BinaryAssociation(
    name="configurations186",
    ends={
        Property(name="domain_Configuration", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Recipes", type=domain_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructures187: BinaryAssociation = BinaryAssociation(
    name="infrastructures187",
    ends={
        Property(name="domain_Infrastructure", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Recipes188", type=domain_Infrastructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent189: BinaryAssociation = BinaryAssociation(
    name="parent189",
    ends={
        Property(name="ApplicationRecipe191", type=domain_Recipes, multiplicity=Multiplicity(1, 1)),
        Property(name="recipes190", type=domain_ApplicationRecipe, multiplicity=Multiplicity(0, 1))
    }
)
any205: BinaryAssociation = BinaryAssociation(
    name="any205",
    ends={
        Property(name="domain_EObject207", type=domain_DeploymentComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentComponents206", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapper208: BinaryAssociation = BinaryAssociation(
    name="mapper208",
    ends={
        Property(name="domain_ModelMapper", type=domain_DeploymentComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentComponent209", type=domain_ModelMapper, multiplicity=Multiplicity(0, 1))
    }
)
deploymentComponentLink211: BinaryAssociation = BinaryAssociation(
    name="deploymentComponentLink211",
    ends={
        Property(name="domain_DeploymentComponent212", type=domain_DeploymentComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentComponent210", type=domain_DeploymentComponent, multiplicity=Multiplicity(0, 1))
    }
)
deplymentStep201: BinaryAssociation = BinaryAssociation(
    name="deplymentStep201",
    ends={
        Property(name="domain_DeploymentComponent", type=domain_DeploymentComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentComponents202", type=domain_DeploymentComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startSeq203: BinaryAssociation = BinaryAssociation(
    name="startSeq203",
    ends={
        Property(name="domain_DeploymentStarStep", type=domain_DeploymentComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentComponents204", type=domain_DeploymentStarStep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappers216: BinaryAssociation = BinaryAssociation(
    name="mappers216",
    ends={
        Property(name="domain_ApplicationMapper", type=domain_UsingMappers, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_UsingMappers", type=domain_ApplicationMapper, multiplicity=Multiplicity(0, 9999))
    }
)
firstStep213: BinaryAssociation = BinaryAssociation(
    name="firstStep213",
    ends={
        Property(name="domain_DeploymentComponent215", type=domain_DeploymentStarStep, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DeploymentStarStep214", type=domain_DeploymentComponent, multiplicity=Multiplicity(0, 1))
    }
)
infrastructures221: BinaryAssociation = BinaryAssociation(
    name="infrastructures221",
    ends={
        Property(name="Infrastructure", type=domain_Recipe, multiplicity=Multiplicity(1, 1)),
        Property(name="recipe222", type=domain_Infrastructure, multiplicity=Multiplicity(0, 9999))
    }
)
deployment223: BinaryAssociation = BinaryAssociation(
    name="deployment223",
    ends={
        Property(name="domain_DeploymentSequence224", type=domain_Recipe, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Recipe", type=domain_DeploymentSequence, multiplicity=Multiplicity(0, 1))
    }
)
source225: BinaryAssociation = BinaryAssociation(
    name="source225",
    ends={
        Property(name="domain_Configuration227", type=domain_ConfigExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ConfigExtension226", type=domain_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
parent217: BinaryAssociation = BinaryAssociation(
    name="parent217",
    ends={
        Property(name="Recipes218", type=domain_Recipe, multiplicity=Multiplicity(1, 1)),
        Property(name="recipe", type=domain_Recipes, multiplicity=Multiplicity(0, 1))
    }
)
ingredients219: BinaryAssociation = BinaryAssociation(
    name="ingredients219",
    ends={
        Property(name="Ingredient", type=domain_Recipe, multiplicity=Multiplicity(1, 1)),
        Property(name="parent220", type=domain_Ingredient, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent231: BinaryAssociation = BinaryAssociation(
    name="parent231",
    ends={
        Property(name="Recipe232", type=domain_Ingredient, multiplicity=Multiplicity(1, 1)),
        Property(name="ingredients", type=domain_Recipe, multiplicity=Multiplicity(0, 1))
    }
)
components233: BinaryAssociation = BinaryAssociation(
    name="components233",
    ends={
        Property(name="Component", type=domain_Ingredient, multiplicity=Multiplicity(1, 1)),
        Property(name="parent234", type=domain_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent235: BinaryAssociation = BinaryAssociation(
    name="parent235",
    ends={
        Property(name="Ingredient236", type=domain_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=domain_Ingredient, multiplicity=Multiplicity(0, 1))
    }
)
mappers237: BinaryAssociation = BinaryAssociation(
    name="mappers237",
    ends={
        Property(name="ModelMapper", type=domain_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="parent238", type=domain_ModelMapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target228: BinaryAssociation = BinaryAssociation(
    name="target228",
    ends={
        Property(name="domain_Configuration230", type=domain_ConfigExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ConfigExtension229", type=domain_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
recipe239: BinaryAssociation = BinaryAssociation(
    name="recipe239",
    ends={
        Property(name="Recipe240", type=domain_Infrastructure, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructures", type=domain_Recipe, multiplicity=Multiplicity(0, 1))
    }
)
recipeConfig241: BinaryAssociation = BinaryAssociation(
    name="recipeConfig241",
    ends={
        Property(name="Configuration", type=domain_Infrastructure, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructure", type=domain_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
infrastructure242: BinaryAssociation = BinaryAssociation(
    name="infrastructure242",
    ends={
        Property(name="Infrastructure243", type=domain_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="recipeConfig", type=domain_Infrastructure, multiplicity=Multiplicity(0, 1))
    }
)
properties244: BinaryAssociation = BinaryAssociation(
    name="properties244",
    ends={
        Property(name="domain_Property", type=domain_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Configuration245", type=domain_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hashProperties246: BinaryAssociation = BinaryAssociation(
    name="hashProperties246",
    ends={
        Property(name="domain_HashProperty", type=domain_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Configuration247", type=domain_HashProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent248: BinaryAssociation = BinaryAssociation(
    name="parent248",
    ends={
        Property(name="Component250", type=domain_ModelMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="mappers249", type=domain_Component, multiplicity=Multiplicity(0, 1))
    }
)
specifiers251: BinaryAssociation = BinaryAssociation(
    name="specifiers251",
    ends={
        Property(name="domain_MappingSpecifier", type=domain_ModelMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ModelMapper252", type=domain_MappingSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
confVarRef255: BinaryAssociation = BinaryAssociation(
    name="confVarRef255",
    ends={
        Property(name="domain_ConfigVariable", type=domain_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Property256", type=domain_ConfigVariable, multiplicity=Multiplicity(0, 1))
    }
)
confHashRef257: BinaryAssociation = BinaryAssociation(
    name="confHashRef257",
    ends={
        Property(name="domain_ConfigHash", type=domain_HashProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_HashProperty258", type=domain_ConfigHash, multiplicity=Multiplicity(0, 1))
    }
)
hash259: BinaryAssociation = BinaryAssociation(
    name="hash259",
    ends={
        Property(name="domain_KeyValuePair", type=domain_HashProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_HashProperty260", type=domain_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries253: BinaryAssociation = BinaryAssociation(
    name="queries253",
    ends={
        Property(name="domain_Query", type=domain_ModelMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ModelMapper254", type=domain_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifierRef261: BinaryAssociation = BinaryAssociation(
    name="specifierRef261",
    ends={
        Property(name="domain_Specifier", type=domain_MappingSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MappingSpecifier262", type=domain_Specifier, multiplicity=Multiplicity(0, 1))
    }
)
valueRef263: BinaryAssociation = BinaryAssociation(
    name="valueRef263",
    ends={
        Property(name="domain_Option", type=domain_MappingSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MappingSpecifier264", type=domain_Option, multiplicity=Multiplicity(0, 1))
    }
)
modelQuery265: BinaryAssociation = BinaryAssociation(
    name="modelQuery265",
    ends={
        Property(name="domain_ModelQuery", type=domain_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Query266", type=domain_ModelQuery, multiplicity=Multiplicity(0, 1))
    }
)
queryRef267: BinaryAssociation = BinaryAssociation(
    name="queryRef267",
    ends={
        Property(name="domain_ModelQuery269", type=domain_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Query268", type=domain_ModelQuery, multiplicity=Multiplicity(0, 1))
    }
)
variables270: BinaryAssociation = BinaryAssociation(
    name="variables270",
    ends={
        Property(name="domain_QueryVariable", type=domain_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Query271", type=domain_QueryVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domainArtifactRef274: BinaryAssociation = BinaryAssociation(
    name="domainArtifactRef274",
    ends={
        Property(name="domain_DomainArtifact", type=domain_ArtifactRef, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ArtifactRef", type=domain_DomainArtifact, multiplicity=Multiplicity(0, 1))
    }
)
artifactRef275: BinaryAssociation = BinaryAssociation(
    name="artifactRef275",
    ends={
        Property(name="domain_Artifact277", type=domain_ArtifactRef, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ArtifactRef276", type=domain_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
packageRef278: BinaryAssociation = BinaryAssociation(
    name="packageRef278",
    ends={
        Property(name="domain_Package", type=domain_TypePointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TypePointer", type=domain_Package, multiplicity=Multiplicity(0, 1))
    }
)
typeRef279: BinaryAssociation = BinaryAssociation(
    name="typeRef279",
    ends={
        Property(name="domain_TypeElement", type=domain_TypePointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TypePointer280", type=domain_TypeElement, multiplicity=Multiplicity(0, 1))
    }
)
types281: BinaryAssociation = BinaryAssociation(
    name="types281",
    ends={
        Property(name="TypeElement", type=domain_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parent282", type=domain_TypeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent283: BinaryAssociation = BinaryAssociation(
    name="parent283",
    ends={
        Property(name="Package", type=domain_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="typedefinition", type=domain_Package, multiplicity=Multiplicity(0, 1))
    }
)
queryParamRef272: BinaryAssociation = BinaryAssociation(
    name="queryParamRef272",
    ends={
        Property(name="domain_QueryParameter", type=domain_QueryVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_QueryVariable273", type=domain_QueryParameter, multiplicity=Multiplicity(0, 1))
    }
)
any285: BinaryAssociation = BinaryAssociation(
    name="any285",
    ends={
        Property(name="domain_EObject287", type=domain_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TypeDefinition286", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source288: BinaryAssociation = BinaryAssociation(
    name="source288",
    ends={
        Property(name="domain_TypeElement290", type=domain_RelationShip, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_RelationShip289", type=domain_TypeElement, multiplicity=Multiplicity(0, 1))
    }
)
target291: BinaryAssociation = BinaryAssociation(
    name="target291",
    ends={
        Property(name="domain_TypeElement293", type=domain_RelationShip, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_RelationShip292", type=domain_TypeElement, multiplicity=Multiplicity(0, 1))
    }
)
relationShips284: BinaryAssociation = BinaryAssociation(
    name="relationShips284",
    ends={
        Property(name="domain_RelationShip", type=domain_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TypeDefinition", type=domain_RelationShip, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links294: BinaryAssociation = BinaryAssociation(
    name="links294",
    ends={
        Property(name="domain_Link", type=domain_Assosiation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Assosiation", type=domain_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceProperty295: BinaryAssociation = BinaryAssociation(
    name="sourceProperty295",
    ends={
        Property(name="domain_Attribute", type=domain_Assosiation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Assosiation296", type=domain_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
targetProperty297: BinaryAssociation = BinaryAssociation(
    name="targetProperty297",
    ends={
        Property(name="domain_Attribute299", type=domain_Assosiation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Assosiation298", type=domain_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
many2manyHelper300: BinaryAssociation = BinaryAssociation(
    name="many2manyHelper300",
    ends={
        Property(name="domain_TypePointer302", type=domain_Assosiation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Assosiation301", type=domain_TypePointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent303: BinaryAssociation = BinaryAssociation(
    name="parent303",
    ends={
        Property(name="TypeDefinition", type=domain_TypeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=domain_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
attributes304: BinaryAssociation = BinaryAssociation(
    name="attributes304",
    ends={
        Property(name="Attribute", type=domain_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="parent305", type=domain_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations306: BinaryAssociation = BinaryAssociation(
    name="operations306",
    ends={
        Property(name="Operation", type=domain_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="parent307", type=domain_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent309: BinaryAssociation = BinaryAssociation(
    name="parent309",
    ends={
        Property(name="Type310", type=domain_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=domain_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters311: BinaryAssociation = BinaryAssociation(
    name="parameters311",
    ends={
        Property(name="Parameter", type=domain_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent312", type=domain_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue313: BinaryAssociation = BinaryAssociation(
    name="returnValue313",
    ends={
        Property(name="domain_ReturnValue", type=domain_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Operation314", type=domain_ReturnValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent308: BinaryAssociation = BinaryAssociation(
    name="parent308",
    ends={
        Property(name="Type", type=domain_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=domain_Type, multiplicity=Multiplicity(0, 1))
    }
)
values318: BinaryAssociation = BinaryAssociation(
    name="values318",
    ends={
        Property(name="EnumAttribute", type=domain_Enumarator, multiplicity=Multiplicity(1, 1)),
        Property(name="parent319", type=domain_EnumAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent320: BinaryAssociation = BinaryAssociation(
    name="parent320",
    ends={
        Property(name="Enumarator", type=domain_EnumAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="values", type=domain_Enumarator, multiplicity=Multiplicity(0, 1))
    }
)
parent315: BinaryAssociation = BinaryAssociation(
    name="parent315",
    ends={
        Property(name="Operation317", type=domain_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters316", type=domain_Operation, multiplicity=Multiplicity(0, 1))
    }
)
any325: BinaryAssociation = BinaryAssociation(
    name="any325",
    ends={
        Property(name="domain_EObject326", type=domain_TypesRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TypesRepository", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent327: BinaryAssociation = BinaryAssociation(
    name="parent327",
    ends={
        Property(name="TypesRepository328", type=domain_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="typeDefinition", type=domain_TypesRepository, multiplicity=Multiplicity(0, 1))
    }
)
packages329: BinaryAssociation = BinaryAssociation(
    name="packages329",
    ends={
        Property(name="Package331", type=domain_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="parent330", type=domain_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinition321: BinaryAssociation = BinaryAssociation(
    name="typeDefinition321",
    ends={
        Property(name="Types", type=domain_TypesRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="parent322", type=domain_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent323: BinaryAssociation = BinaryAssociation(
    name="parent323",
    ends={
        Property(name="DomainTypes324", type=domain_TypesRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="typesrepository", type=domain_DomainTypes, multiplicity=Multiplicity(0, 1))
    }
)
parent337: BinaryAssociation = BinaryAssociation(
    name="parent337",
    ends={
        Property(name="ApplicationUIPackage338", type=domain_UIPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uipackage", type=domain_ApplicationUIPackage, multiplicity=Multiplicity(0, 1))
    }
)
forms339: BinaryAssociation = BinaryAssociation(
    name="forms339",
    ends={
        Property(name="domain_Form", type=domain_UIPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_UIPackage", type=domain_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any340: BinaryAssociation = BinaryAssociation(
    name="any340",
    ends={
        Property(name="domain_EObject342", type=domain_UIPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_UIPackage341", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view343: BinaryAssociation = BinaryAssociation(
    name="view343",
    ends={
        Property(name="domain_FormView", type=domain_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Form344", type=domain_FormView, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typedefinition332: BinaryAssociation = BinaryAssociation(
    name="typedefinition332",
    ends={
        Property(name="TypeDefinition334", type=domain_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="parent333", type=domain_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
parent335: BinaryAssociation = BinaryAssociation(
    name="parent335",
    ends={
        Property(name="Types336", type=domain_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=domain_Types, multiplicity=Multiplicity(0, 1))
    }
)
view349: BinaryAssociation = BinaryAssociation(
    name="view349",
    ends={
        Property(name="Views", type=domain_FormView, multiplicity=Multiplicity(1, 1)),
        Property(name="parent350", type=domain_Views, multiplicity=Multiplicity(0, 1))
    }
)
datacontrols345: BinaryAssociation = BinaryAssociation(
    name="datacontrols345",
    ends={
        Property(name="domain_FormDataControls", type=domain_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Form346", type=domain_FormDataControls, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters347: BinaryAssociation = BinaryAssociation(
    name="parameters347",
    ends={
        Property(name="domain_FormParameter", type=domain_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Form348", type=domain_FormParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tabPagesInheritances355: BinaryAssociation = BinaryAssociation(
    name="tabPagesInheritances355",
    ends={
        Property(name="domain_TabPagesInheritance", type=domain_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Views356", type=domain_TabPagesInheritance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menus357: BinaryAssociation = BinaryAssociation(
    name="menus357",
    ends={
        Property(name="domain_MenuDefinition", type=domain_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Views358", type=domain_MenuDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any359: BinaryAssociation = BinaryAssociation(
    name="any359",
    ends={
        Property(name="domain_EObject361", type=domain_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Views360", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiLangLabel362: BinaryAssociation = BinaryAssociation(
    name="multiLangLabel362",
    ends={
        Property(name="domain_Context", type=domain_MultiLangLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MultiLangLabel", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent351: BinaryAssociation = BinaryAssociation(
    name="parent351",
    ends={
        Property(name="FormView", type=domain_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="view", type=domain_FormView, multiplicity=Multiplicity(0, 1))
    }
)
canvases352: BinaryAssociation = BinaryAssociation(
    name="canvases352",
    ends={
        Property(name="domain_CanvasFrame", type=domain_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Views", type=domain_CanvasFrame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewInheritances353: BinaryAssociation = BinaryAssociation(
    name="viewInheritances353",
    ends={
        Property(name="domain_ViewInheritance", type=domain_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Views354", type=domain_ViewInheritance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewElement363: BinaryAssociation = BinaryAssociation(
    name="viewElement363",
    ends={
        Property(name="domain_ViewElement", type=domain_ViewPortHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ViewPortHolder", type=domain_ViewElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menuView364: BinaryAssociation = BinaryAssociation(
    name="menuView364",
    ends={
        Property(name="MenuView", type=domain_MenuDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parent365", type=domain_MenuView, multiplicity=Multiplicity(0, 1))
    }
)
viewPortTrigger366: BinaryAssociation = BinaryAssociation(
    name="viewPortTrigger366",
    ends={
        Property(name="domain_ViewPortTrigger", type=domain_ViewPort, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ViewPort", type=domain_ViewPortTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
canvasView367: BinaryAssociation = BinaryAssociation(
    name="canvasView367",
    ends={
        Property(name="CanvasView", type=domain_ViewArea, multiplicity=Multiplicity(1, 1)),
        Property(name="parent368", type=domain_CanvasView, multiplicity=Multiplicity(0, 1))
    }
)
source369: BinaryAssociation = BinaryAssociation(
    name="source369",
    ends={
        Property(name="domain_ViewPort371", type=domain_ViewInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ViewInheritance370", type=domain_ViewPort, multiplicity=Multiplicity(0, 1))
    }
)
target372: BinaryAssociation = BinaryAssociation(
    name="target372",
    ends={
        Property(name="domain_CanvasFrame374", type=domain_ViewInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ViewInheritance373", type=domain_CanvasFrame, multiplicity=Multiplicity(0, 1))
    }
)
source375: BinaryAssociation = BinaryAssociation(
    name="source375",
    ends={
        Property(name="domain_TabCanvas", type=domain_TabPagesInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TabPagesInheritance376", type=domain_TabCanvas, multiplicity=Multiplicity(0, 1))
    }
)
target377: BinaryAssociation = BinaryAssociation(
    name="target377",
    ends={
        Property(name="domain_TabPage", type=domain_TabPagesInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_TabPagesInheritance378", type=domain_TabPage, multiplicity=Multiplicity(0, 1))
    }
)
formControl379: BinaryAssociation = BinaryAssociation(
    name="formControl379",
    ends={
        Property(name="Controls", type=domain_FormDataControls, multiplicity=Multiplicity(1, 1)),
        Property(name="parent380", type=domain_Controls, multiplicity=Multiplicity(0, 1))
    }
)
parent381: BinaryAssociation = BinaryAssociation(
    name="parent381",
    ends={
        Property(name="ViewArea", type=domain_CanvasView, multiplicity=Multiplicity(1, 1)),
        Property(name="canvasView", type=domain_ViewArea, multiplicity=Multiplicity(0, 1))
    }
)
linkToMessages385: BinaryAssociation = BinaryAssociation(
    name="linkToMessages385",
    ends={
        Property(name="domain_LinkToMessage", type=domain_CanvasView, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_CanvasView386", type=domain_LinkToMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any387: BinaryAssociation = BinaryAssociation(
    name="any387",
    ends={
        Property(name="domain_EObject389", type=domain_CanvasView, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_CanvasView388", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source390: BinaryAssociation = BinaryAssociation(
    name="source390",
    ends={
        Property(name="domain_InputElement", type=domain_LinkToMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_LinkToMessage391", type=domain_InputElement, multiplicity=Multiplicity(0, 1))
    }
)
target392: BinaryAssociation = BinaryAssociation(
    name="target392",
    ends={
        Property(name="domain_MessageElement", type=domain_LinkToMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_LinkToMessage393", type=domain_MessageElement, multiplicity=Multiplicity(0, 1))
    }
)
baseCanvas382: BinaryAssociation = BinaryAssociation(
    name="baseCanvas382",
    ends={
        Property(name="domain_LayerHolder", type=domain_CanvasView, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_CanvasView", type=domain_LayerHolder, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkToLabels383: BinaryAssociation = BinaryAssociation(
    name="linkToLabels383",
    ends={
        Property(name="domain_LinkToLabel", type=domain_CanvasView, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_CanvasView384", type=domain_LinkToLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target397: BinaryAssociation = BinaryAssociation(
    name="target397",
    ends={
        Property(name="domain_Label", type=domain_LinkToLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_LinkToLabel398", type=domain_Label, multiplicity=Multiplicity(0, 1))
    }
)
children399: BinaryAssociation = BinaryAssociation(
    name="children399",
    ends={
        Property(name="domain_Uielement", type=domain_ChildrenHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ChildrenHolder", type=domain_Uielement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refObj400: BinaryAssociation = BinaryAssociation(
    name="refObj400",
    ends={
        Property(name="domain_EObject401", type=domain_ContextParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ContextParameter", type=domain_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value402: BinaryAssociation = BinaryAssociation(
    name="value402",
    ends={
        Property(name="domain_ContextValue", type=domain_ContextParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ContextParameter403", type=domain_ContextValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression404: BinaryAssociation = BinaryAssociation(
    name="expression404",
    ends={
        Property(name="domain_ExpressionPart", type=domain_ContextValue, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ContextValue405", type=domain_ExpressionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source394: BinaryAssociation = BinaryAssociation(
    name="source394",
    ends={
        Property(name="domain_InputElement396", type=domain_LinkToLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_LinkToLabel395", type=domain_InputElement, multiplicity=Multiplicity(0, 1))
    }
)
objRef406: BinaryAssociation = BinaryAssociation(
    name="objRef406",
    ends={
        Property(name="domain_ExpressionPart407", type=domain_EObject, multiplicity=Multiplicity(0, 1)),
        Property(name="domain_EObject408", type=domain_ExpressionPart, multiplicity=Multiplicity(1, 1))
    }
)
parameters409: BinaryAssociation = BinaryAssociation(
    name="parameters409",
    ends={
        Property(name="domain_ContextParameter410", type=domain_ContextParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ContextParameters", type=domain_ContextParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style411: BinaryAssociation = BinaryAssociation(
    name="style411",
    ends={
        Property(name="domain_Context412", type=domain_StyleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_StyleElement", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styleClass413: BinaryAssociation = BinaryAssociation(
    name="styleClass413",
    ends={
        Property(name="domain_StyleClass", type=domain_StyleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_StyleElement414", type=domain_StyleClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier415: BinaryAssociation = BinaryAssociation(
    name="classifier415",
    ends={
        Property(name="domain_Classifier417", type=domain_StyleClass, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_StyleClass416", type=domain_Classifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields418: BinaryAssociation = BinaryAssociation(
    name="fields418",
    ends={
        Property(name="domain_FlexField", type=domain_FlexFields, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_FlexFields", type=domain_FlexField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enabled419: BinaryAssociation = BinaryAssociation(
    name="enabled419",
    ends={
        Property(name="domain_Context420", type=domain_EnabledUIItem, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_EnabledUIItem", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
required421: BinaryAssociation = BinaryAssociation(
    name="required421",
    ends={
        Property(name="domain_Context423", type=domain_Uielement, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Uielement422", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readOnly424: BinaryAssociation = BinaryAssociation(
    name="readOnly424",
    ends={
        Property(name="domain_Context426", type=domain_Uielement, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Uielement425", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
icon429: BinaryAssociation = BinaryAssociation(
    name="icon429",
    ends={
        Property(name="domain_Context430", type=domain_ItemIcon, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ItemIcon", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
area431: BinaryAssociation = BinaryAssociation(
    name="area431",
    ends={
        Property(name="domain_NickNamed", type=domain_AreaRef, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_AreaRef432", type=domain_NickNamed, multiplicity=Multiplicity(0, 1))
    }
)
sourcePointer433: BinaryAssociation = BinaryAssociation(
    name="sourcePointer433",
    ends={
        Property(name="domain_DataControl", type=domain_SourcesPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_SourcesPointer", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
valuePointer434: BinaryAssociation = BinaryAssociation(
    name="valuePointer434",
    ends={
        Property(name="domain_EObject436", type=domain_SourcesPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_SourcesPointer435", type=domain_EObject, multiplicity=Multiplicity(0, 1))
    }
)
sourceCast437: BinaryAssociation = BinaryAssociation(
    name="sourceCast437",
    ends={
        Property(name="domain_Type", type=domain_SourcesPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_SourcesPointer438", type=domain_Type, multiplicity=Multiplicity(0, 1))
    }
)
refreshAreas427: BinaryAssociation = BinaryAssociation(
    name="refreshAreas427",
    ends={
        Property(name="domain_AreaRef", type=domain_Uielement, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Uielement428", type=domain_AreaRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
displayOptionPointer442: BinaryAssociation = BinaryAssociation(
    name="displayOptionPointer442",
    ends={
        Property(name="domain_EObject443", type=domain_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Selection", type=domain_EObject, multiplicity=Multiplicity(0, 1))
    }
)
valueOptionPointer444: BinaryAssociation = BinaryAssociation(
    name="valueOptionPointer444",
    ends={
        Property(name="domain_EObject446", type=domain_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Selection445", type=domain_EObject, multiplicity=Multiplicity(0, 1))
    }
)
optionPointer447: BinaryAssociation = BinaryAssociation(
    name="optionPointer447",
    ends={
        Property(name="domain_DataControl448", type=domain_OptionSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_OptionSelection", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
optionCast449: BinaryAssociation = BinaryAssociation(
    name="optionCast449",
    ends={
        Property(name="domain_Type451", type=domain_OptionSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_OptionSelection450", type=domain_Type, multiplicity=Multiplicity(0, 1))
    }
)
optionCastDataControl452: BinaryAssociation = BinaryAssociation(
    name="optionCastDataControl452",
    ends={
        Property(name="domain_DataControl454", type=domain_OptionSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_OptionSelection453", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
sourceCastDataControl439: BinaryAssociation = BinaryAssociation(
    name="sourceCastDataControl439",
    ends={
        Property(name="domain_DataControl441", type=domain_SourcesPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_SourcesPointer440", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
selection455: BinaryAssociation = BinaryAssociation(
    name="selection455",
    ends={
        Property(name="domain_Selection456", type=domain_DropDownSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DropDownSelection", type=domain_Selection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOptionMessage457: BinaryAssociation = BinaryAssociation(
    name="initialOptionMessage457",
    ends={
        Property(name="domain_Context459", type=domain_DropDownSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DropDownSelection458", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element460: BinaryAssociation = BinaryAssociation(
    name="element460",
    ends={
        Property(name="domain_Uielement461", type=domain_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Column", type=domain_Uielement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cols462: BinaryAssociation = BinaryAssociation(
    name="cols462",
    ends={
        Property(name="domain_Column463", type=domain_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Table", type=domain_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image464: BinaryAssociation = BinaryAssociation(
    name="image464",
    ends={
        Property(name="domain_Context465", type=domain_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Tree", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cols466: BinaryAssociation = BinaryAssociation(
    name="cols466",
    ends={
        Property(name="domain_Column468", type=domain_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Tree467", type=domain_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations473: BinaryAssociation = BinaryAssociation(
    name="relations473",
    ends={
        Property(name="domain_Relation", type=domain_Controls, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Controls474", type=domain_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies475: BinaryAssociation = BinaryAssociation(
    name="dependencies475",
    ends={
        Property(name="domain_Dependency", type=domain_Controls, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Controls476", type=domain_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any477: BinaryAssociation = BinaryAssociation(
    name="any477",
    ends={
        Property(name="domain_EObject479", type=domain_Controls, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Controls478", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent469: BinaryAssociation = BinaryAssociation(
    name="parent469",
    ends={
        Property(name="FormDataControls", type=domain_Controls, multiplicity=Multiplicity(1, 1)),
        Property(name="formControl", type=domain_FormDataControls, multiplicity=Multiplicity(0, 1))
    }
)
root470: BinaryAssociation = BinaryAssociation(
    name="root470",
    ends={
        Property(name="domain_Root", type=domain_Controls, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Controls", type=domain_Root, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controls471: BinaryAssociation = BinaryAssociation(
    name="controls471",
    ends={
        Property(name="DataControl", type=domain_Controls, multiplicity=Multiplicity(1, 1)),
        Property(name="parent472", type=domain_DataControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typePointers480: BinaryAssociation = BinaryAssociation(
    name="typePointers480",
    ends={
        Property(name="domain_TypePointer481", type=domain_ProxiesList, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ProxiesList", type=domain_TypePointer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preFormTrigger482: BinaryAssociation = BinaryAssociation(
    name="preFormTrigger482",
    ends={
        Property(name="domain_PREFormTrigger", type=domain_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Root483", type=domain_PREFormTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables484: BinaryAssociation = BinaryAssociation(
    name="variables484",
    ends={
        Property(name="domain_FormVariable", type=domain_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Root485", type=domain_FormVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paramRef486: BinaryAssociation = BinaryAssociation(
    name="paramRef486",
    ends={
        Property(name="domain_FormParameter488", type=domain_FormVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_FormVariable487", type=domain_FormParameter, multiplicity=Multiplicity(0, 1))
    }
)
baseTypeRef489: BinaryAssociation = BinaryAssociation(
    name="baseTypeRef489",
    ends={
        Property(name="domain_TypePointer491", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl490", type=domain_TypePointer, multiplicity=Multiplicity(0, 1))
    }
)
parent495: BinaryAssociation = BinaryAssociation(
    name="parent495",
    ends={
        Property(name="Controls496", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="controls", type=domain_Controls, multiplicity=Multiplicity(0, 1))
    }
)
preQueryTrigger497: BinaryAssociation = BinaryAssociation(
    name="preQueryTrigger497",
    ends={
        Property(name="domain_PREQueryTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl498", type=domain_PREQueryTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postQueryTrigger499: BinaryAssociation = BinaryAssociation(
    name="postQueryTrigger499",
    ends={
        Property(name="domain_POSTQueryTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl500", type=domain_POSTQueryTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preInsertTrigger501: BinaryAssociation = BinaryAssociation(
    name="preInsertTrigger501",
    ends={
        Property(name="domain_PREInsertTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl502", type=domain_PREInsertTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preDeleteTrigger503: BinaryAssociation = BinaryAssociation(
    name="preDeleteTrigger503",
    ends={
        Property(name="domain_PREDeleteTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl504", type=domain_PREDeleteTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseType492: BinaryAssociation = BinaryAssociation(
    name="baseType492",
    ends={
        Property(name="domain_TypePointer494", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl493", type=domain_TypePointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preUpdateTrigger507: BinaryAssociation = BinaryAssociation(
    name="preUpdateTrigger507",
    ends={
        Property(name="domain_PREUpdateTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl508", type=domain_PREUpdateTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
create509: BinaryAssociation = BinaryAssociation(
    name="create509",
    ends={
        Property(name="domain_CreateTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl510", type=domain_CreateTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insert511: BinaryAssociation = BinaryAssociation(
    name="insert511",
    ends={
        Property(name="domain_InsertTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl512", type=domain_InsertTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
update513: BinaryAssociation = BinaryAssociation(
    name="update513",
    ends={
        Property(name="domain_UpdateTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl514", type=domain_UpdateTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remove515: BinaryAssociation = BinaryAssociation(
    name="remove515",
    ends={
        Property(name="domain_DeleteTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl516", type=domain_DeleteTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postCreateTrigger505: BinaryAssociation = BinaryAssociation(
    name="postCreateTrigger505",
    ends={
        Property(name="domain_POSTCreateTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl506", type=domain_POSTCreateTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
artificialFields519: BinaryAssociation = BinaryAssociation(
    name="artificialFields519",
    ends={
        Property(name="ArtificialField", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="parent520", type=domain_ArtificialField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultSearch521: BinaryAssociation = BinaryAssociation(
    name="defaultSearch521",
    ends={
        Property(name="domain_ContextParameters523", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl522", type=domain_ContextParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultOrderBy524: BinaryAssociation = BinaryAssociation(
    name="defaultOrderBy524",
    ends={
        Property(name="domain_Orders", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl525", type=domain_Orders, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderRules526: BinaryAssociation = BinaryAssociation(
    name="orderRules526",
    ends={
        Property(name="domain_OrderBy", type=domain_Orders, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Orders527", type=domain_OrderBy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refObj528: BinaryAssociation = BinaryAssociation(
    name="refObj528",
    ends={
        Property(name="domain_EObject530", type=domain_OrderBy, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_OrderBy529", type=domain_EObject, multiplicity=Multiplicity(0, 1))
    }
)
search517: BinaryAssociation = BinaryAssociation(
    name="search517",
    ends={
        Property(name="domain_SearchTrigger", type=domain_DataControl, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_DataControl518", type=domain_SearchTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
master531: BinaryAssociation = BinaryAssociation(
    name="master531",
    ends={
        Property(name="domain_DataControl533", type=domain_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Relation532", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
detail534: BinaryAssociation = BinaryAssociation(
    name="detail534",
    ends={
        Property(name="domain_DataControl536", type=domain_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Relation535", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
links537: BinaryAssociation = BinaryAssociation(
    name="links537",
    ends={
        Property(name="domain_Link539", type=domain_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Relation538", type=domain_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
detail543: BinaryAssociation = BinaryAssociation(
    name="detail543",
    ends={
        Property(name="domain_Dependency544", type=domain_DataControl, multiplicity=Multiplicity(0, 1)),
        Property(name="domain_DataControl545", type=domain_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
parent546: BinaryAssociation = BinaryAssociation(
    name="parent546",
    ends={
        Property(name="DataControl547", type=domain_ArtificialField, multiplicity=Multiplicity(1, 1)),
        Property(name="artificialFields", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
masterField548: BinaryAssociation = BinaryAssociation(
    name="masterField548",
    ends={
        Property(name="domain_Attribute550", type=domain_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Link549", type=domain_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
detailField551: BinaryAssociation = BinaryAssociation(
    name="detailField551",
    ends={
        Property(name="domain_Attribute553", type=domain_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Link552", type=domain_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
master540: BinaryAssociation = BinaryAssociation(
    name="master540",
    ends={
        Property(name="domain_DataControl542", type=domain_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_Dependency541", type=domain_DataControl, multiplicity=Multiplicity(0, 1))
    }
)
parent554: BinaryAssociation = BinaryAssociation(
    name="parent554",
    ends={
        Property(name="applicationInfrastructureLayer", type=domain_Application, multiplicity=Multiplicity(0, 1)),
        Property(name="Application555", type=domain_ApplicationInfrastructureLayer, multiplicity=Multiplicity(1, 1))
    }
)
infarastructure556: BinaryAssociation = BinaryAssociation(
    name="infarastructure556",
    ends={
        Property(name="EnterpriseInfrastructure", type=domain_ApplicationInfrastructureLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="parent557", type=domain_EnterpriseInfrastructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent558: BinaryAssociation = BinaryAssociation(
    name="parent558",
    ends={
        Property(name="ApplicationInfrastructureLayer559", type=domain_EnterpriseInfrastructure, multiplicity=Multiplicity(1, 1)),
        Property(name="infarastructure", type=domain_ApplicationInfrastructureLayer, multiplicity=Multiplicity(0, 1))
    }
)
datacenters560: BinaryAssociation = BinaryAssociation(
    name="datacenters560",
    ends={
        Property(name="Datacenter", type=domain_EnterpriseInfrastructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parent561", type=domain_Datacenter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureConnections562: BinaryAssociation = BinaryAssociation(
    name="infrastructureConnections562",
    ends={
        Property(name="domain_InfrastructureConnection", type=domain_EnterpriseInfrastructure, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_EnterpriseInfrastructure", type=domain_InfrastructureConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any563: BinaryAssociation = BinaryAssociation(
    name="any563",
    ends={
        Property(name="domain_EObject565", type=domain_EnterpriseInfrastructure, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_EnterpriseInfrastructure564", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent566: BinaryAssociation = BinaryAssociation(
    name="parent566",
    ends={
        Property(name="datacenters", type=domain_EnterpriseInfrastructure, multiplicity=Multiplicity(0, 1)),
        Property(name="EnterpriseInfrastructure567", type=domain_Datacenter, multiplicity=Multiplicity(1, 1))
    }
)
subsystems568: BinaryAssociation = BinaryAssociation(
    name="subsystems568",
    ends={
        Property(name="Subsystem", type=domain_Datacenter, multiplicity=Multiplicity(1, 1)),
        Property(name="parent569", type=domain_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent570: BinaryAssociation = BinaryAssociation(
    name="parent570",
    ends={
        Property(name="Datacenter571", type=domain_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="subsystems", type=domain_Datacenter, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureLayer572: BinaryAssociation = BinaryAssociation(
    name="infrastructureLayer572",
    ends={
        Property(name="InfrastructureLayer", type=domain_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="parent573", type=domain_InfrastructureLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
master578: BinaryAssociation = BinaryAssociation(
    name="master578",
    ends={
        Property(name="domain_InfrastructureComponent", type=domain_InfrastructureConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_InfrastructureConnection579", type=domain_InfrastructureComponent, multiplicity=Multiplicity(0, 1))
    }
)
detail580: BinaryAssociation = BinaryAssociation(
    name="detail580",
    ends={
        Property(name="domain_InfrastructureComponent582", type=domain_InfrastructureConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_InfrastructureConnection581", type=domain_InfrastructureComponent, multiplicity=Multiplicity(0, 1))
    }
)
parent583: BinaryAssociation = BinaryAssociation(
    name="parent583",
    ends={
        Property(name="InfrastructureLayer584", type=domain_InfrastructureComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureComponent", type=domain_InfrastructureLayer, multiplicity=Multiplicity(0, 1))
    }
)
parent574: BinaryAssociation = BinaryAssociation(
    name="parent574",
    ends={
        Property(name="Subsystem575", type=domain_InfrastructureLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureLayer", type=domain_Subsystem, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureComponent576: BinaryAssociation = BinaryAssociation(
    name="infrastructureComponent576",
    ends={
        Property(name="InfrastructureComponent", type=domain_InfrastructureLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="parent577", type=domain_InfrastructureComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent586: BinaryAssociation = BinaryAssociation(
    name="parent586",
    ends={
        Property(name="MenuDefinition", type=domain_MenuView, multiplicity=Multiplicity(1, 1)),
        Property(name="menuView", type=domain_MenuDefinition, multiplicity=Multiplicity(0, 1))
    }
)
menuFolders587: BinaryAssociation = BinaryAssociation(
    name="menuFolders587",
    ends={
        Property(name="domain_MenuFolder", type=domain_MenuView, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuView", type=domain_MenuFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
any588: BinaryAssociation = BinaryAssociation(
    name="any588",
    ends={
        Property(name="domain_EObject590", type=domain_MenuView, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuView589", type=domain_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
menu591: BinaryAssociation = BinaryAssociation(
    name="menu591",
    ends={
        Property(name="domain_MenuFolder592", type=domain_MenuHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuHolder", type=domain_MenuFolder, multiplicity=Multiplicity(0, 1))
    }
)
extensionRef593: BinaryAssociation = BinaryAssociation(
    name="extensionRef593",
    ends={
        Property(name="domain_MenuFolder594", type=domain_MenuExtensionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuExtensionRef", type=domain_MenuFolder, multiplicity=Multiplicity(0, 1))
    }
)
menuElements595: BinaryAssociation = BinaryAssociation(
    name="menuElements595",
    ends={
        Property(name="domain_MenuElement", type=domain_MenuFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuFolder596", type=domain_MenuElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servers585: BinaryAssociation = BinaryAssociation(
    name="servers585",
    ends={
        Property(name="domain_Server", type=domain_ServerClaster, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_ServerClaster", type=domain_Server, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition597: BinaryAssociation = BinaryAssociation(
    name="transition597",
    ends={
        Property(name="domain_Context598", type=domain_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuItem", type=domain_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refreshAreas599: BinaryAssociation = BinaryAssociation(
    name="refreshAreas599",
    ends={
        Property(name="domain_AreaRef601", type=domain_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_MenuItem600", type=domain_AreaRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toSubmenu602: BinaryAssociation = BinaryAssociation(
    name="toSubmenu602",
    ends={
        Property(name="domain_MenuFolder603", type=domain_SubMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="domain_SubMenu", type=domain_MenuFolder, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_domain_DomainArtifacts_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_DomainArtifacts)
gen_domain_DomainApplications_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_DomainApplications)
gen_domain_JPAService_DomainArtifact = Generalization(general=DomainArtifact, specific=domain_JPAService)
gen_domain_EJBService_DomainArtifact = Generalization(general=DomainArtifact, specific=domain_EJBService)
gen_domain_ContinuousIintegration_DomainArtifact = Generalization(general=DomainArtifact, specific=domain_ContinuousIintegration)
gen_domain_ORMEntity_DomainArtifact = Generalization(general=DomainArtifact, specific=domain_ORMEntity)
gen_domain_ApplicationStyle_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_ApplicationStyle)
gen_domain_ApplicationUILayer_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_ApplicationUILayer)
gen_domain_ApplicationMappers_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_ApplicationMappers)
gen_domain_ApplicationRecipes_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_ApplicationRecipes)
gen_domain_MethodPointer_TypePointer = Generalization(general=TypePointer, specific=domain_MethodPointer)
gen_domain_MessageLibrary_Categorized = Generalization(general=Categorized, specific=domain_MessageLibrary)
gen_domain_JavaScriptMapper_TypeMapper = Generalization(general=TypeMapper, specific=domain_JavaScriptMapper)
gen_domain_CSSMapper_Mapper = Generalization(general=Mapper, specific=domain_CSSMapper)
gen_domain_TypeMapper_Mapper = Generalization(general=Mapper, specific=domain_TypeMapper)
gen_domain_TypeMapper_TypePointer = Generalization(general=TypePointer, specific=domain_TypeMapper)
gen_domain_JavaMapper_TypeMapper = Generalization(general=TypeMapper, specific=domain_JavaMapper)
gen_domain_RoleMapper_Mapper = Generalization(general=Mapper, specific=domain_RoleMapper)
gen_domain_Recipe_UsingMappers = Generalization(general=UsingMappers, specific=domain_Recipe)
gen_domain_Component_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Component)
gen_domain_Ingredient_UsingMappers = Generalization(general=UsingMappers, specific=domain_Ingredient)
gen_domain_Ingredient_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Ingredient)
gen_domain_JavaComponent_Component = Generalization(general=Component, specific=domain_JavaComponent)
gen_domain_ModelMapper_ArtifactRef = Generalization(general=ArtifactRef, specific=domain_ModelMapper)
gen_domain_RelationShip_Categorized = Generalization(general=Categorized, specific=domain_RelationShip)
gen_domain_References_RelationShip = Generalization(general=RelationShip, specific=domain_References)
gen_domain_Generalization_RelationShip = Generalization(general=RelationShip, specific=domain_Generalization)
gen_domain_Primitive_TypeElement = Generalization(general=TypeElement, specific=domain_Primitive)
gen_domain_Assosiation_RelationShip = Generalization(general=RelationShip, specific=domain_Assosiation)
gen_domain_TypeReference_TypeElement = Generalization(general=TypeElement, specific=domain_TypeReference)
gen_domain_TypeReference_TypePointer = Generalization(general=TypePointer, specific=domain_TypeReference)
gen_domain_Attribute_TypePointer = Generalization(general=TypePointer, specific=domain_Attribute)
gen_domain_Attribute_Categorized = Generalization(general=Categorized, specific=domain_Attribute)
gen_domain_Type_TypeElement = Generalization(general=TypeElement, specific=domain_Type)
gen_domain_Type_Categorized = Generalization(general=Categorized, specific=domain_Type)
gen_domain_Operation_Secured = Generalization(general=Secured, specific=domain_Operation)
gen_domain_Operation_Categorized = Generalization(general=Categorized, specific=domain_Operation)
gen_domain_Parameter_TypePointer = Generalization(general=TypePointer, specific=domain_Parameter)
gen_domain_Enumarator_TypeElement = Generalization(general=TypeElement, specific=domain_Enumarator)
gen_domain_ReturnValue_TypePointer = Generalization(general=TypePointer, specific=domain_ReturnValue)
gen_domain_Types_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Types)
gen_domain_FormParameter_TypePointer = Generalization(general=TypePointer, specific=domain_FormParameter)
gen_domain_ViewPortHolder_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_ViewPortHolder)
gen_domain_ViewElement_StyleElement = Generalization(general=StyleElement, specific=domain_ViewElement)
gen_domain_ViewElement_Categorized = Generalization(general=Categorized, specific=domain_ViewElement)
gen_domain_ViewElement_NickNamed = Generalization(general=NickNamed, specific=domain_ViewElement)
gen_domain_PopupCanvas_CanvasFrame = Generalization(general=CanvasFrame, specific=domain_PopupCanvas)
gen_domain_PopupCanvas_ViewPortHolder = Generalization(general=ViewPortHolder, specific=domain_PopupCanvas)
gen_domain_PopupCanvas_DefaultCavas = Generalization(general=DefaultCavas, specific=domain_PopupCanvas)
gen_domain_PopupCanvas_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_PopupCanvas)
gen_domain_PopupCanvas_Categorized = Generalization(general=Categorized, specific=domain_PopupCanvas)
gen_domain_PopupCanvas_FlexFields = Generalization(general=FlexFields, specific=domain_PopupCanvas)
gen_domain_CanvasFrame_StyleElement = Generalization(general=StyleElement, specific=domain_CanvasFrame)
gen_domain_Window_CanvasFrame = Generalization(general=CanvasFrame, specific=domain_Window)
gen_domain_Window_ViewPortHolder = Generalization(general=ViewPortHolder, specific=domain_Window)
gen_domain_Window_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Window)
gen_domain_Window_Categorized = Generalization(general=Categorized, specific=domain_Window)
gen_domain_Window_Secured = Generalization(general=Secured, specific=domain_Window)
gen_domain_MenuDefinition_StyleElement = Generalization(general=StyleElement, specific=domain_MenuDefinition)
gen_domain_MenuDefinition_Categorized = Generalization(general=Categorized, specific=domain_MenuDefinition)
gen_domain_Canvas_CanvasFrame = Generalization(general=CanvasFrame, specific=domain_Canvas)
gen_domain_Canvas_ViewPortHolder = Generalization(general=ViewPortHolder, specific=domain_Canvas)
gen_domain_Canvas_DefaultCavas = Generalization(general=DefaultCavas, specific=domain_Canvas)
gen_domain_Canvas_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Canvas)
gen_domain_Canvas_Categorized = Generalization(general=Categorized, specific=domain_Canvas)
gen_domain_TabPage_CanvasFrame = Generalization(general=CanvasFrame, specific=domain_TabPage)
gen_domain_TabPage_ViewPortHolder = Generalization(general=ViewPortHolder, specific=domain_TabPage)
gen_domain_TabPage_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_TabPage)
gen_domain_TabPage_Categorized = Generalization(general=Categorized, specific=domain_TabPage)
gen_domain_TabPage_Orderable = Generalization(general=Orderable, specific=domain_TabPage)
gen_domain_ViewPort_ViewElement = Generalization(general=ViewElement, specific=domain_ViewPort)
gen_domain_ViewPort_Orderable = Generalization(general=Orderable, specific=domain_ViewPort)
gen_domain_ViewArea_ViewElement = Generalization(general=ViewElement, specific=domain_ViewArea)
gen_domain_ViewArea_Orderable = Generalization(general=Orderable, specific=domain_ViewArea)
gen_domain_TabCanvas_CanvasFrame = Generalization(general=CanvasFrame, specific=domain_TabCanvas)
gen_domain_TabCanvas_DefaultCavas = Generalization(general=DefaultCavas, specific=domain_TabCanvas)
gen_domain_TabCanvas_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_TabCanvas)
gen_domain_TabCanvas_Categorized = Generalization(general=Categorized, specific=domain_TabCanvas)
gen_domain_ViewPortTrigger_Trigger = Generalization(general=Trigger, specific=domain_ViewPortTrigger)
gen_domain_Context_ContextValue = Generalization(general=ContextValue, specific=domain_Context)
gen_domain_Context_ContextParameters = Generalization(general=ContextParameters, specific=domain_Context)
gen_domain_StyleClass_ContextValue = Generalization(general=ContextValue, specific=domain_StyleClass)
gen_domain_FlexField_Context = Generalization(general=Context, specific=domain_FlexField)
gen_domain_FlexField_Categorized = Generalization(general=Categorized, specific=domain_FlexField)
gen_domain_Uielement_StyleElement = Generalization(general=StyleElement, specific=domain_Uielement)
gen_domain_Uielement_NickNamed = Generalization(general=NickNamed, specific=domain_Uielement)
gen_domain_Uielement_Categorized = Generalization(general=Categorized, specific=domain_Uielement)
gen_domain_Uielement_Orderable = Generalization(general=Orderable, specific=domain_Uielement)
gen_domain_Uielement_EnabledUIItem = Generalization(general=EnabledUIItem, specific=domain_Uielement)
gen_domain_Uielement_FlexFields = Generalization(general=FlexFields, specific=domain_Uielement)
gen_domain_Uielement_MenuHolder = Generalization(general=MenuHolder, specific=domain_Uielement)
gen_domain_SourcesPointer_Uielement = Generalization(general=Uielement, specific=domain_SourcesPointer)
gen_domain_Selection_StyleElement = Generalization(general=StyleElement, specific=domain_Selection)
gen_domain_OptionSelection_InputElement = Generalization(general=InputElement, specific=domain_OptionSelection)
gen_domain_LayerHolder_Uielement = Generalization(general=Uielement, specific=domain_LayerHolder)
gen_domain_LayerHolder_ChildrenHolder = Generalization(general=ChildrenHolder, specific=domain_LayerHolder)
gen_domain_LayerHolder_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_LayerHolder)
gen_domain_InputText_InputElement = Generalization(general=InputElement, specific=domain_InputText)
gen_domain_InputText_Formatable = Generalization(general=Formatable, specific=domain_InputText)
gen_domain_Password_InputElement = Generalization(general=InputElement, specific=domain_Password)
gen_domain_Password_Formatable = Generalization(general=Formatable, specific=domain_Password)
gen_domain_Label_Uielement = Generalization(general=Uielement, specific=domain_Label)
gen_domain_Label_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Label)
gen_domain_InputElement_SourcesPointer = Generalization(general=SourcesPointer, specific=domain_InputElement)
gen_domain_OutputText_Formatable = Generalization(general=Formatable, specific=domain_OutputText)
gen_domain_CheckBox_InputElement = Generalization(general=InputElement, specific=domain_CheckBox)
gen_domain_DropDownSelection_OptionSelection = Generalization(general=OptionSelection, specific=domain_DropDownSelection)
gen_domain_Image_InputElement = Generalization(general=InputElement, specific=domain_Image)
gen_domain_Date_InputElement = Generalization(general=InputElement, specific=domain_Date)
gen_domain_Date_Formatable = Generalization(general=Formatable, specific=domain_Date)
gen_domain_Button_Uielement = Generalization(general=Uielement, specific=domain_Button)
gen_domain_Button_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Button)
gen_domain_Button_ItemIcon = Generalization(general=ItemIcon, specific=domain_Button)
gen_domain_MessageElement_Uielement = Generalization(general=Uielement, specific=domain_MessageElement)
gen_domain_MessageElement_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_MessageElement)
gen_domain_OutputText_InputElement = Generalization(general=InputElement, specific=domain_OutputText)
gen_domain_Table_SourcesPointer = Generalization(general=SourcesPointer, specific=domain_Table)
gen_domain_Table_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Table)
gen_domain_Table_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Table)
gen_domain_Menu_Uielement = Generalization(general=Uielement, specific=domain_Menu)
gen_domain_Tree_SourcesPointer = Generalization(general=SourcesPointer, specific=domain_Tree)
gen_domain_Tree_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Tree)
gen_domain_Tree_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Tree)
gen_domain_Column_StyleElement = Generalization(general=StyleElement, specific=domain_Column)
gen_domain_Column_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_Column)
gen_domain_Column_Categorized = Generalization(general=Categorized, specific=domain_Column)
gen_domain_Column_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Column)
gen_domain_Column_Orderable = Generalization(general=Orderable, specific=domain_Column)
gen_domain_Trigger_MethodPointer = Generalization(general=MethodPointer, specific=domain_Trigger)
gen_domain_Trigger_ContextParameters = Generalization(general=ContextParameters, specific=domain_Trigger)
gen_domain_PREFormTrigger_Trigger = Generalization(general=Trigger, specific=domain_PREFormTrigger)
gen_domain_PREQueryTrigger_Trigger = Generalization(general=Trigger, specific=domain_PREQueryTrigger)
gen_domain_POSTQueryTrigger_Trigger = Generalization(general=Trigger, specific=domain_POSTQueryTrigger)
gen_domain_PREInsertTrigger_Trigger = Generalization(general=Trigger, specific=domain_PREInsertTrigger)
gen_domain_POSTCreateTrigger_Trigger = Generalization(general=Trigger, specific=domain_POSTCreateTrigger)
gen_domain_PREUpdateTrigger_Trigger = Generalization(general=Trigger, specific=domain_PREUpdateTrigger)
gen_domain_CreateTrigger_Trigger = Generalization(general=Trigger, specific=domain_CreateTrigger)
gen_domain_CreateTrigger_ProxiesList = Generalization(general=ProxiesList, specific=domain_CreateTrigger)
gen_domain_PREDeleteTrigger_Trigger = Generalization(general=Trigger, specific=domain_PREDeleteTrigger)
gen_domain_InsertTrigger_Trigger = Generalization(general=Trigger, specific=domain_InsertTrigger)
gen_domain_InsertTrigger_ProxiesList = Generalization(general=ProxiesList, specific=domain_InsertTrigger)
gen_domain_UpdateTrigger_Trigger = Generalization(general=Trigger, specific=domain_UpdateTrigger)
gen_domain_UpdateTrigger_ProxiesList = Generalization(general=ProxiesList, specific=domain_UpdateTrigger)
gen_domain_DeleteTrigger_Trigger = Generalization(general=Trigger, specific=domain_DeleteTrigger)
gen_domain_DeleteTrigger_ProxiesList = Generalization(general=ProxiesList, specific=domain_DeleteTrigger)
gen_domain_SearchTrigger_Trigger = Generalization(general=Trigger, specific=domain_SearchTrigger)
gen_domain_FormVariable_TypePointer = Generalization(general=TypePointer, specific=domain_FormVariable)
gen_domain_SearchTrigger_ProxiesList = Generalization(general=ProxiesList, specific=domain_SearchTrigger)
gen_domain_ArtificialField_TypePointer = Generalization(general=TypePointer, specific=domain_ArtificialField)
gen_domain_Datacenter_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_Datacenter)
gen_domain_Server_InfrastructureComponent = Generalization(general=InfrastructureComponent, specific=domain_Server)
gen_domain_Router_InfrastructureComponent = Generalization(general=InfrastructureComponent, specific=domain_Router)
gen_domain_Hub_InfrastructureComponent = Generalization(general=InfrastructureComponent, specific=domain_Hub)
gen_domain_Storage_InfrastructureComponent = Generalization(general=InfrastructureComponent, specific=domain_Storage)
gen_domain_MenuElement_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_MenuElement)
gen_domain_MenuElement_StyleElement = Generalization(general=StyleElement, specific=domain_MenuElement)
gen_domain_MenuElement_Categorized = Generalization(general=Categorized, specific=domain_MenuElement)
gen_domain_MenuElement_EnabledUIItem = Generalization(general=EnabledUIItem, specific=domain_MenuElement)
gen_domain_MenuElement_Orderable = Generalization(general=Orderable, specific=domain_MenuElement)
gen_domain_MenuFolder_HTMLLayerHolder = Generalization(general=HTMLLayerHolder, specific=domain_MenuFolder)
gen_domain_MenuFolder_EnabledUIItem = Generalization(general=EnabledUIItem, specific=domain_MenuFolder)
gen_domain_MenuFolder_Categorized = Generalization(general=Categorized, specific=domain_MenuFolder)
gen_domain_MenuFolder_StyleElement = Generalization(general=StyleElement, specific=domain_MenuFolder)
gen_domain_MenuFolder_MultiLangLabel = Generalization(general=MultiLangLabel, specific=domain_MenuFolder)
gen_domain_MenuFolder_ItemIcon = Generalization(general=ItemIcon, specific=domain_MenuFolder)
gen_domain_ServerClaster_InfrastructureComponent = Generalization(general=InfrastructureComponent, specific=domain_ServerClaster)
gen_domain_MenuExtensionPoint_MenuElement = Generalization(general=MenuElement, specific=domain_MenuExtensionPoint)
gen_domain_MenuExtensionPoint_MenuExtensionRef = Generalization(general=MenuExtensionRef, specific=domain_MenuExtensionPoint)
gen_domain_SubMenu_MenuElement = Generalization(general=MenuElement, specific=domain_SubMenu)
gen_domain_SubMenu_ItemIcon = Generalization(general=ItemIcon, specific=domain_SubMenu)
gen_domain_MenuSeparator_MenuElement = Generalization(general=MenuElement, specific=domain_MenuSeparator)
gen_domain_MenuItem_MenuElement = Generalization(general=MenuElement, specific=domain_MenuItem)
gen_domain_MenuItem_ItemIcon = Generalization(general=ItemIcon, specific=domain_MenuItem)
gen_domain_MenuItem_FlexFields = Generalization(general=FlexFields, specific=domain_MenuItem)

# Domain Model
domain_model = DomainModel(
    name="domain",
    types={domain_Domain, domain_DomainArtifacts, domain_DomainTypes, domain_DomainApplications, domain_EObject, domain_GenerationHint, domain_Secured, domain_GrantAccess, domain_DomainApplication, domain_Role, HTMLLayerHolder, domain_HTMLLayerHolder, domain_Categorized, domain_Classifier, domain_DomainArtifact, domain_TypesRepository, domain_Application, domain_Artifacts, domain_EJBService, domain_ContinuousIintegration, domain_Artifact, domain_ORMEntity, DomainArtifact, domain_JPAService, domain_ConfigVariable, domain_ConfigHash, domain_ModelQuery, domain_Specifier, domain_QueryParameter, domain_ApplicationRecipes, domain_ApplicationMappers, domain_ApplicationUILayer, domain_ApplicationInfrastructureLayer, domain_ApplicationStyle, domain_Option, domain_Messages, domain_ApplicationRole, domain_ApplicationMessages, domain_StylesPackage, domain_Roles, domain_ApplicationUIPackage, domain_Styles, domain_ApplicationRecipe, domain_Recipes, domain_UIPackage, domain_ApplicationMapper, domain_Mappers, domain_MethodPointer, TypePointer, domain_Operation, domain_MessageLibrary, domain_Language, Categorized, domain_LanguageRef, domain_Message, domain_Translation, domain_Group, domain_StyleLibrary, domain_StyleSet, domain_Mapper, domain_JavaScriptMapper, domain_CSSMapper, domain_TypeMapper, Mapper, domain_JavaMapper, TypeMapper, domain_RoleMapper, domain_Recipe, domain_Configuration, domain_DeploymentSequence, domain_ConfigExtension, domain_DeploymentComponents, domain_Infrastructure, domain_ModelMapper, domain_DeploymentComponent, domain_DeploymentStarStep, UsingMappers, domain_UsingMappers, domain_Ingredient, domain_Component, domain_JavaComponent, Component, domain_Property, domain_HashProperty, ArtifactRef, domain_MappingSpecifier, domain_Query, domain_KeyValuePair, domain_QueryVariable, domain_TypePointer, domain_Package, domain_TypeElement, domain_TypeDefinition, domain_ArtifactRef, domain_References, RelationShip, domain_Generalization, domain_RelationShip, domain_Link, domain_Attribute, domain_Primitive, TypeElement, domain_Assosiation, domain_TypeReference, domain_Type, Secured, domain_Parameter, domain_ReturnValue, domain_Enumarator, domain_EnumAttribute, domain_Types, domain_Form, domain_FormView, domain_Views, domain_FormDataControls, domain_FormParameter, domain_TabPagesInheritance, domain_MenuDefinition, domain_Orderable, domain_MultiLangLabel, domain_Context, domain_CanvasFrame, domain_ViewInheritance, domain_ViewElement, domain_DefaultCavas, NickNamed, domain_PopupCanvas, CanvasFrame, ViewPortHolder, DefaultCavas, MultiLangLabel, FlexFields, StyleElement, domain_ViewPortHolder, domain_Window, domain_MenuView, domain_Canvas, domain_TabPage, Orderable, domain_ViewPort, ViewElement, domain_ViewPortTrigger, domain_ViewArea, domain_TabCanvas, domain_CanvasView, Trigger, domain_Controls, domain_LayerHolder, domain_LinkToMessage, domain_InputElement, domain_MessageElement, domain_LinkToLabel, domain_ChildrenHolder, domain_Uielement, domain_ContextParameter, domain_ContextValue, domain_ExpressionPart, domain_Label, domain_ContextParameters, ContextValue, ContextParameters, domain_StyleElement, domain_StyleClass, domain_NickNamed, Context, domain_EnabledUIItem, EnabledUIItem, MenuHolder, domain_AreaRef, domain_FlexFields, domain_FlexField, domain_Formatable, domain_SourcesPointer, Uielement, domain_DataControl, domain_Selection, domain_ItemIcon, domain_OptionSelection, InputElement, ChildrenHolder, domain_InputText, Formatable, domain_Password, SourcesPointer, domain_CheckBox, domain_DropDownSelection, OptionSelection, domain_Image, domain_Date, domain_Button, ItemIcon, domain_OutputText, domain_Table, domain_Menu, domain_Tree, domain_Column, domain_Dependency, domain_Trigger, MethodPointer, domain_PREFormTrigger, domain_PREQueryTrigger, domain_POSTQueryTrigger, domain_PREInsertTrigger, domain_Root, domain_Relation, domain_POSTCreateTrigger, domain_PREUpdateTrigger, domain_ProxiesList, domain_CreateTrigger, ProxiesList, domain_PREDeleteTrigger, domain_InsertTrigger, domain_UpdateTrigger, domain_DeleteTrigger, domain_SearchTrigger, domain_FormVariable, domain_ArtificialField, domain_Orders, domain_OrderBy, domain_EnterpriseInfrastructure, domain_Datacenter, domain_InfrastructureConnection, domain_Subsystem, domain_InfrastructureLayer, domain_Server, InfrastructureComponent, domain_Router, domain_Hub, domain_Storage, domain_InfrastructureComponent, domain_MenuFolder, domain_MenuHolder, domain_MenuExtensionRef, domain_MenuElement, domain_ServerClaster, domain_MenuExtensionPoint, MenuExtensionRef, domain_SubMenu, domain_MenuSeparator, domain_MenuItem, MenuElement, PlatformLayers, Comparator, Order, RelationType, Orientation},
    associations={domainArtifacts0, domainTypes1, domainApplications3, any5, hint7, grants9, applicationRef10, roleRef12, classifiers6, domainArtifact15, typesrepository17, parent19, parent14, application25, parent27, parent29, artifact31, applications21, parent23, artifacts33, parent35, any37, parent39, configVariables41, configHashes43, modelQuery45, specifiers47, parent51, hints49, parent55, parameters57, parent59, parent53, parent65, applicationRecipes67, applicationMappers69, applicationUILayer71, applicationInfrastructureLayer73, parent61, options63, parent81, any83, parent85, messages87, applicationStyle75, applicationRole77, applicationMessages79, roles91, parent93, stylesPackage95, parent89, parent101, applicationUIPackages103, parent97, styles99, parent109, recipes111, recipes113, parent115, parent105, uipackage107, parent117, mappers119, mapper121, parent123, methodRef125, parent126, messageLibraries128, languages129, any131, libLanguages134, messages136, lang138, translatioins141, lang143, parent146, roles148, groups150, any152, group2Role158, parent161, libraries163, any164, group2Group156, mappers169, parent171, any173, parent175, styles167, role182, recipe184, stylePackage178, styleLibrary179, deployment192, configExtension194, any196, deploymentComponents199, configurations186, infrastructures187, parent189, any205, mapper208, deploymentComponentLink211, deplymentStep201, startSeq203, mappers216, firstStep213, infrastructures221, deployment223, source225, parent217, ingredients219, parent231, components233, parent235, mappers237, target228, recipe239, recipeConfig241, infrastructure242, properties244, hashProperties246, parent248, specifiers251, confVarRef255, confHashRef257, hash259, queries253, specifierRef261, valueRef263, modelQuery265, queryRef267, variables270, domainArtifactRef274, artifactRef275, packageRef278, typeRef279, types281, parent283, queryParamRef272, any285, source288, target291, relationShips284, links294, sourceProperty295, targetProperty297, many2manyHelper300, parent303, attributes304, operations306, parent309, parameters311, returnValue313, parent308, values318, parent320, parent315, any325, parent327, packages329, typeDefinition321, parent323, parent337, forms339, any340, view343, typedefinition332, parent335, view349, datacontrols345, parameters347, tabPagesInheritances355, menus357, any359, multiLangLabel362, parent351, canvases352, viewInheritances353, viewElement363, menuView364, viewPortTrigger366, canvasView367, source369, target372, source375, target377, formControl379, parent381, linkToMessages385, any387, source390, target392, baseCanvas382, linkToLabels383, target397, children399, refObj400, value402, expression404, source394, objRef406, parameters409, style411, styleClass413, classifier415, fields418, enabled419, required421, readOnly424, icon429, area431, sourcePointer433, valuePointer434, sourceCast437, refreshAreas427, displayOptionPointer442, valueOptionPointer444, optionPointer447, optionCast449, optionCastDataControl452, sourceCastDataControl439, selection455, initialOptionMessage457, element460, cols462, image464, cols466, relations473, dependencies475, any477, parent469, root470, controls471, typePointers480, preFormTrigger482, variables484, paramRef486, baseTypeRef489, parent495, preQueryTrigger497, postQueryTrigger499, preInsertTrigger501, preDeleteTrigger503, baseType492, preUpdateTrigger507, create509, insert511, update513, remove515, postCreateTrigger505, artificialFields519, defaultSearch521, defaultOrderBy524, orderRules526, refObj528, search517, master531, detail534, links537, detail543, parent546, masterField548, detailField551, master540, parent554, infarastructure556, parent558, datacenters560, infrastructureConnections562, any563, parent566, subsystems568, parent570, infrastructureLayer572, master578, detail580, parent583, parent574, infrastructureComponent576, parent586, menuFolders587, any588, menu591, extensionRef593, menuElements595, servers585, transition597, refreshAreas599, toSubmenu602},
    generalizations={gen_domain_DomainArtifacts_HTMLLayerHolder, gen_domain_DomainApplications_HTMLLayerHolder, gen_domain_JPAService_DomainArtifact, gen_domain_EJBService_DomainArtifact, gen_domain_ContinuousIintegration_DomainArtifact, gen_domain_ORMEntity_DomainArtifact, gen_domain_ApplicationStyle_HTMLLayerHolder, gen_domain_ApplicationUILayer_HTMLLayerHolder, gen_domain_ApplicationMappers_HTMLLayerHolder, gen_domain_ApplicationRecipes_HTMLLayerHolder, gen_domain_MethodPointer_TypePointer, gen_domain_MessageLibrary_Categorized, gen_domain_JavaScriptMapper_TypeMapper, gen_domain_CSSMapper_Mapper, gen_domain_TypeMapper_Mapper, gen_domain_TypeMapper_TypePointer, gen_domain_JavaMapper_TypeMapper, gen_domain_RoleMapper_Mapper, gen_domain_Recipe_UsingMappers, gen_domain_Component_HTMLLayerHolder, gen_domain_Ingredient_UsingMappers, gen_domain_Ingredient_HTMLLayerHolder, gen_domain_JavaComponent_Component, gen_domain_ModelMapper_ArtifactRef, gen_domain_RelationShip_Categorized, gen_domain_References_RelationShip, gen_domain_Generalization_RelationShip, gen_domain_Primitive_TypeElement, gen_domain_Assosiation_RelationShip, gen_domain_TypeReference_TypeElement, gen_domain_TypeReference_TypePointer, gen_domain_Attribute_TypePointer, gen_domain_Attribute_Categorized, gen_domain_Type_TypeElement, gen_domain_Type_Categorized, gen_domain_Operation_Secured, gen_domain_Operation_Categorized, gen_domain_Parameter_TypePointer, gen_domain_Enumarator_TypeElement, gen_domain_ReturnValue_TypePointer, gen_domain_Types_HTMLLayerHolder, gen_domain_FormParameter_TypePointer, gen_domain_ViewPortHolder_HTMLLayerHolder, gen_domain_ViewElement_StyleElement, gen_domain_ViewElement_Categorized, gen_domain_ViewElement_NickNamed, gen_domain_PopupCanvas_CanvasFrame, gen_domain_PopupCanvas_ViewPortHolder, gen_domain_PopupCanvas_DefaultCavas, gen_domain_PopupCanvas_MultiLangLabel, gen_domain_PopupCanvas_Categorized, gen_domain_PopupCanvas_FlexFields, gen_domain_CanvasFrame_StyleElement, gen_domain_Window_CanvasFrame, gen_domain_Window_ViewPortHolder, gen_domain_Window_MultiLangLabel, gen_domain_Window_Categorized, gen_domain_Window_Secured, gen_domain_MenuDefinition_StyleElement, gen_domain_MenuDefinition_Categorized, gen_domain_Canvas_CanvasFrame, gen_domain_Canvas_ViewPortHolder, gen_domain_Canvas_DefaultCavas, gen_domain_Canvas_MultiLangLabel, gen_domain_Canvas_Categorized, gen_domain_TabPage_CanvasFrame, gen_domain_TabPage_ViewPortHolder, gen_domain_TabPage_MultiLangLabel, gen_domain_TabPage_Categorized, gen_domain_TabPage_Orderable, gen_domain_ViewPort_ViewElement, gen_domain_ViewPort_Orderable, gen_domain_ViewArea_ViewElement, gen_domain_ViewArea_Orderable, gen_domain_TabCanvas_CanvasFrame, gen_domain_TabCanvas_DefaultCavas, gen_domain_TabCanvas_MultiLangLabel, gen_domain_TabCanvas_Categorized, gen_domain_ViewPortTrigger_Trigger, gen_domain_Context_ContextValue, gen_domain_Context_ContextParameters, gen_domain_StyleClass_ContextValue, gen_domain_FlexField_Context, gen_domain_FlexField_Categorized, gen_domain_Uielement_StyleElement, gen_domain_Uielement_NickNamed, gen_domain_Uielement_Categorized, gen_domain_Uielement_Orderable, gen_domain_Uielement_EnabledUIItem, gen_domain_Uielement_FlexFields, gen_domain_Uielement_MenuHolder, gen_domain_SourcesPointer_Uielement, gen_domain_Selection_StyleElement, gen_domain_OptionSelection_InputElement, gen_domain_LayerHolder_Uielement, gen_domain_LayerHolder_ChildrenHolder, gen_domain_LayerHolder_HTMLLayerHolder, gen_domain_InputText_InputElement, gen_domain_InputText_Formatable, gen_domain_Password_InputElement, gen_domain_Password_Formatable, gen_domain_Label_Uielement, gen_domain_Label_MultiLangLabel, gen_domain_InputElement_SourcesPointer, gen_domain_OutputText_Formatable, gen_domain_CheckBox_InputElement, gen_domain_DropDownSelection_OptionSelection, gen_domain_Image_InputElement, gen_domain_Date_InputElement, gen_domain_Date_Formatable, gen_domain_Button_Uielement, gen_domain_Button_MultiLangLabel, gen_domain_Button_ItemIcon, gen_domain_MessageElement_Uielement, gen_domain_MessageElement_MultiLangLabel, gen_domain_OutputText_InputElement, gen_domain_Table_SourcesPointer, gen_domain_Table_HTMLLayerHolder, gen_domain_Table_MultiLangLabel, gen_domain_Menu_Uielement, gen_domain_Tree_SourcesPointer, gen_domain_Tree_HTMLLayerHolder, gen_domain_Tree_MultiLangLabel, gen_domain_Column_StyleElement, gen_domain_Column_MultiLangLabel, gen_domain_Column_Categorized, gen_domain_Column_HTMLLayerHolder, gen_domain_Column_Orderable, gen_domain_Trigger_MethodPointer, gen_domain_Trigger_ContextParameters, gen_domain_PREFormTrigger_Trigger, gen_domain_PREQueryTrigger_Trigger, gen_domain_POSTQueryTrigger_Trigger, gen_domain_PREInsertTrigger_Trigger, gen_domain_POSTCreateTrigger_Trigger, gen_domain_PREUpdateTrigger_Trigger, gen_domain_CreateTrigger_Trigger, gen_domain_CreateTrigger_ProxiesList, gen_domain_PREDeleteTrigger_Trigger, gen_domain_InsertTrigger_Trigger, gen_domain_InsertTrigger_ProxiesList, gen_domain_UpdateTrigger_Trigger, gen_domain_UpdateTrigger_ProxiesList, gen_domain_DeleteTrigger_Trigger, gen_domain_DeleteTrigger_ProxiesList, gen_domain_SearchTrigger_Trigger, gen_domain_FormVariable_TypePointer, gen_domain_SearchTrigger_ProxiesList, gen_domain_ArtificialField_TypePointer, gen_domain_Datacenter_HTMLLayerHolder, gen_domain_Server_InfrastructureComponent, gen_domain_Router_InfrastructureComponent, gen_domain_Hub_InfrastructureComponent, gen_domain_Storage_InfrastructureComponent, gen_domain_MenuElement_MultiLangLabel, gen_domain_MenuElement_StyleElement, gen_domain_MenuElement_Categorized, gen_domain_MenuElement_EnabledUIItem, gen_domain_MenuElement_Orderable, gen_domain_MenuFolder_HTMLLayerHolder, gen_domain_MenuFolder_EnabledUIItem, gen_domain_MenuFolder_Categorized, gen_domain_MenuFolder_StyleElement, gen_domain_MenuFolder_MultiLangLabel, gen_domain_MenuFolder_ItemIcon, gen_domain_ServerClaster_InfrastructureComponent, gen_domain_MenuExtensionPoint_MenuElement, gen_domain_MenuExtensionPoint_MenuExtensionRef, gen_domain_SubMenu_MenuElement, gen_domain_SubMenu_ItemIcon, gen_domain_MenuSeparator_MenuElement, gen_domain_MenuItem_MenuElement, gen_domain_MenuItem_ItemIcon, gen_domain_MenuItem_FlexFields},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)