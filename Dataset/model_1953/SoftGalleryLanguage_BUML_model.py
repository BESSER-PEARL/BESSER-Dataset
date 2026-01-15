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
softGalleryLanguage_Functionality = Class(name="softGalleryLanguage::Functionality")
softGalleryLanguage_ExceptionsDomain = Class(name="softGalleryLanguage::ExceptionsDomain")
softGalleryLanguage_Entities = Class(name="softGalleryLanguage::Entities")
softGalleryLanguage_AtributePhoto = Class(name="softGalleryLanguage::AtributePhoto")
softGalleryLanguage_AtributeAlbum = Class(name="softGalleryLanguage::AtributeAlbum")
softGalleryLanguage_Model = Class(name="softGalleryLanguage::Model")
softGalleryLanguage_EObject = Class(name="softGalleryLanguage::EObject")
softGalleryLanguage_Domain = Class(name="softGalleryLanguage::Domain")
softGalleryLanguage_Entity = Class(name="softGalleryLanguage::Entity")
softGalleryLanguage_AlbumManagement = Class(name="softGalleryLanguage::AlbumManagement")
softGalleryLanguage_PhotoActions = Class(name="softGalleryLanguage::PhotoActions")
softGalleryLanguage_LandingActions = Class(name="softGalleryLanguage::LandingActions")
softGalleryLanguage_ProfileManagementFunctions = Class(name="softGalleryLanguage::ProfileManagementFunctions")
softGalleryLanguage_AtributeUserDomain = Class(name="softGalleryLanguage::AtributeUserDomain")
softGalleryLanguage_Functionalities = Class(name="softGalleryLanguage::Functionalities")
softGalleryLanguage_ProfileManagement = Class(name="softGalleryLanguage::ProfileManagement")
softGalleryLanguage_AppAccess = Class(name="softGalleryLanguage::AppAccess")
softGalleryLanguage_PhotoActionsFunctions = Class(name="softGalleryLanguage::PhotoActionsFunctions")
softGalleryLanguage_LandingFunctions = Class(name="softGalleryLanguage::LandingFunctions")
softGalleryLanguage_ExceptionsType = Class(name="softGalleryLanguage::ExceptionsType")
softGalleryLanguage_AppAccessFunctions = Class(name="softGalleryLanguage::AppAccessFunctions")
softGalleryLanguage_AlbumManagementFunctions = Class(name="softGalleryLanguage::AlbumManagementFunctions")
softGalleryLanguage_Architecture = Class(name="softGalleryLanguage::Architecture")
softGalleryLanguage_NTiers = Class(name="softGalleryLanguage::NTiers")
softGalleryLanguage_Layer = Class(name="softGalleryLanguage::Layer")
softGalleryLanguage_PresentationLayer = Class(name="softGalleryLanguage::PresentationLayer")
softGalleryLanguage_PresentationContent = Class(name="softGalleryLanguage::PresentationContent")
softGalleryLanguage_PresentationSegments = Class(name="softGalleryLanguage::PresentationSegments")
softGalleryLanguage_BusinessLogicLayer = Class(name="softGalleryLanguage::BusinessLogicLayer")
softGalleryLanguage_PhotoException = Class(name="softGalleryLanguage::PhotoException")
softGalleryLanguage_AlbumException = Class(name="softGalleryLanguage::AlbumException")
softGalleryLanguage_UserException = Class(name="softGalleryLanguage::UserException")
softGalleryLanguage_SegmentStructure = Class(name="softGalleryLanguage::SegmentStructure")
softGalleryLanguage_SegmentStructureContent = Class(name="softGalleryLanguage::SegmentStructureContent")
softGalleryLanguage_DirectoryContent = Class(name="softGalleryLanguage::DirectoryContent")
softGalleryLanguage_Directories = Class(name="softGalleryLanguage::Directories")
softGalleryLanguage_MultipleFile = Class(name="softGalleryLanguage::MultipleFile")
softGalleryLanguage_SingleFile = Class(name="softGalleryLanguage::SingleFile")
softGalleryLanguage_LayerRelations = Class(name="softGalleryLanguage::LayerRelations")
softGalleryLanguage_BusinessLogicContent = Class(name="softGalleryLanguage::BusinessLogicContent")
softGalleryLanguage_BusinessLogicSegments = Class(name="softGalleryLanguage::BusinessLogicSegments")
softGalleryLanguage_ControllerSegmentElement = Class(name="softGalleryLanguage::ControllerSegmentElement")
softGalleryLanguage_SpecificationSegmentElement = Class(name="softGalleryLanguage::SpecificationSegmentElement")
softGalleryLanguage_CriteriaAttributeType = Class(name="softGalleryLanguage::CriteriaAttributeType")
softGalleryLanguage_DataPersistenceLayer = Class(name="softGalleryLanguage::DataPersistenceLayer")
softGalleryLanguage_DataPersistenceContent = Class(name="softGalleryLanguage::DataPersistenceContent")
softGalleryLanguage_DataPersistenceSegments = Class(name="softGalleryLanguage::DataPersistenceSegments")
softGalleryLanguage_NTierSource = Class(name="softGalleryLanguage::NTierSource")
softGalleryLanguage_NTierTarget = Class(name="softGalleryLanguage::NTierTarget")
softGalleryLanguage_NTiersRelations = Class(name="softGalleryLanguage::NTiersRelations")
softGalleryLanguage_Technology = Class(name="softGalleryLanguage::Technology")
softGalleryLanguage_Technologies = Class(name="softGalleryLanguage::Technologies")
softGalleryLanguage_Spring = Class(name="softGalleryLanguage::Spring")
softGalleryLanguage_React = Class(name="softGalleryLanguage::React")
softGalleryLanguage_LayerSource = Class(name="softGalleryLanguage::LayerSource")
softGalleryLanguage_LayerTarget = Class(name="softGalleryLanguage::LayerTarget")
softGalleryLanguage_ArchitectureComponents = Class(name="softGalleryLanguage::ArchitectureComponents")
softGalleryLanguage_FrontEnd = Class(name="softGalleryLanguage::FrontEnd")
softGalleryLanguage_BackEnd = Class(name="softGalleryLanguage::BackEnd")
softGalleryLanguage_PersistenceDataComponent = Class(name="softGalleryLanguage::PersistenceDataComponent")
softGalleryLanguage_NTiersConnections = Class(name="softGalleryLanguage::NTiersConnections")
softGalleryLanguage_NTierConnectionContent = Class(name="softGalleryLanguage::NTierConnectionContent")
softGalleryLanguage_SpringRepository = Class(name="softGalleryLanguage::SpringRepository")
softGalleryLanguage_SpringRepositories = Class(name="softGalleryLanguage::SpringRepositories")
softGalleryLanguage_SpringRepositoryAnnotation = Class(name="softGalleryLanguage::SpringRepositoryAnnotation")
softGalleryLanguage_RestController = Class(name="softGalleryLanguage::RestController")
softGalleryLanguage_Specification = Class(name="softGalleryLanguage::Specification")
softGalleryLanguage_Predicate = Class(name="softGalleryLanguage::Predicate")
softGalleryLanguage_SearchCriteria = Class(name="softGalleryLanguage::SearchCriteria")
softGalleryLanguage_PostgreSQL = Class(name="softGalleryLanguage::PostgreSQL")
softGalleryLanguage_AmazonWebServices = Class(name="softGalleryLanguage::AmazonWebServices")
softGalleryLanguage_SpringBootApplication = Class(name="softGalleryLanguage::SpringBootApplication")
softGalleryLanguage_Configuration = Class(name="softGalleryLanguage::Configuration")
softGalleryLanguage_EnableGlobalMethodSecurity = Class(name="softGalleryLanguage::EnableGlobalMethodSecurity")
softGalleryLanguage_EnableAuthorizationServer = Class(name="softGalleryLanguage::EnableAuthorizationServer")
softGalleryLanguage_EnableResourceServer = Class(name="softGalleryLanguage::EnableResourceServer")
softGalleryLanguage_EnableWebSecurity = Class(name="softGalleryLanguage::EnableWebSecurity")
softGalleryLanguage_SpringComponent = Class(name="softGalleryLanguage::SpringComponent")
softGalleryLanguage_OrderSpring = Class(name="softGalleryLanguage::OrderSpring")
softGalleryLanguage_GetMapping = Class(name="softGalleryLanguage::GetMapping")
softGalleryLanguage_PutMapping = Class(name="softGalleryLanguage::PutMapping")
softGalleryLanguage_DeleteMapping = Class(name="softGalleryLanguage::DeleteMapping")
softGalleryLanguage_ResponseParameterAnnotation = Class(name="softGalleryLanguage::ResponseParameterAnnotation")
softGalleryLanguage_ResponseParameterType = Class(name="softGalleryLanguage::ResponseParameterType")
softGalleryLanguage_ResponseParameterName = Class(name="softGalleryLanguage::ResponseParameterName")
softGalleryLanguage_ExceptionHandler = Class(name="softGalleryLanguage::ExceptionHandler")
softGalleryLanguage_ExceptionProcess = Class(name="softGalleryLanguage::ExceptionProcess")
softGalleryLanguage_Autowired = Class(name="softGalleryLanguage::Autowired")
softGalleryLanguage_ResponseEntity = Class(name="softGalleryLanguage::ResponseEntity")
softGalleryLanguage_MappingType = Class(name="softGalleryLanguage::MappingType")
softGalleryLanguage_ResponseParameter = Class(name="softGalleryLanguage::ResponseParameter")
softGalleryLanguage_RequestMapping = Class(name="softGalleryLanguage::RequestMapping")
MappingType = Class(name="MappingType")
softGalleryLanguage_RequestMappingValue = Class(name="softGalleryLanguage::RequestMappingValue")
softGalleryLanguage_RequestMappingMethod = Class(name="softGalleryLanguage::RequestMappingMethod")
softGalleryLanguage_RequestMappingProduces = Class(name="softGalleryLanguage::RequestMappingProduces")
softGalleryLanguage_PostMapping = Class(name="softGalleryLanguage::PostMapping")
softGalleryLanguage_StorageActionMember = Class(name="softGalleryLanguage::StorageActionMember")
softGalleryLanguage_StorageActionMemberType = Class(name="softGalleryLanguage::StorageActionMemberType")
softGalleryLanguage_StorageActionMemberName = Class(name="softGalleryLanguage::StorageActionMemberName")
softGalleryLanguage_ReactModules = Class(name="softGalleryLanguage::ReactModules")
softGalleryLanguage_ReactSubModules = Class(name="softGalleryLanguage::ReactSubModules")
softGalleryLanguage_ReactConfiguration = Class(name="softGalleryLanguage::ReactConfiguration")
softGalleryLanguage_ReactComponents = Class(name="softGalleryLanguage::ReactComponents")
softGalleryLanguage_ReactActions = Class(name="softGalleryLanguage::ReactActions")
softGalleryLanguage_SpringEntity = Class(name="softGalleryLanguage::SpringEntity")
softGalleryLanguage_SpringEntityAnnotationTypes = Class(name="softGalleryLanguage::SpringEntityAnnotationTypes")
softGalleryLanguage_StorageClient = Class(name="softGalleryLanguage::StorageClient")
softGalleryLanguage_StorageMember = Class(name="softGalleryLanguage::StorageMember")
softGalleryLanguage_StorageMemberType = Class(name="softGalleryLanguage::StorageMemberType")
softGalleryLanguage_StorageMemberAnnotation = Class(name="softGalleryLanguage::StorageMemberAnnotation")
softGalleryLanguage_StorageAction = Class(name="softGalleryLanguage::StorageAction")
softGalleryLanguage_StorageActionAnnotation = Class(name="softGalleryLanguage::StorageActionAnnotation")
softGalleryLanguage_StorageActionReturn = Class(name="softGalleryLanguage::StorageActionReturn")
softGalleryLanguage_PackageVersion = Class(name="softGalleryLanguage::PackageVersion")
softGalleryLanguage_DOMConfigurations = Class(name="softGalleryLanguage::DOMConfigurations")
softGalleryLanguage_ComponentsLogic = Class(name="softGalleryLanguage::ComponentsLogic")
softGalleryLanguage_ComponentsUI = Class(name="softGalleryLanguage::ComponentsUI")
softGalleryLanguage_ComponentsStyles = Class(name="softGalleryLanguage::ComponentsStyles")
softGalleryLanguage_LogicContent = Class(name="softGalleryLanguage::LogicContent")
softGalleryLanguage_ReactLibraries = Class(name="softGalleryLanguage::ReactLibraries")
softGalleryLanguage_ReactInfo = Class(name="softGalleryLanguage::ReactInfo")
softGalleryLanguage_ReactDependencies = Class(name="softGalleryLanguage::ReactDependencies")
softGalleryLanguage_ReactConfigurations = Class(name="softGalleryLanguage::ReactConfigurations")
softGalleryLanguage_ReactDependenciesRules = Class(name="softGalleryLanguage::ReactDependenciesRules")
softGalleryLanguage_ReactDependenciesSubRules = Class(name="softGalleryLanguage::ReactDependenciesSubRules")
softGalleryLanguage_SingleDependencies = Class(name="softGalleryLanguage::SingleDependencies")
softGalleryLanguage_PackageName = Class(name="softGalleryLanguage::PackageName")
softGalleryLanguage_ReactImports = Class(name="softGalleryLanguage::ReactImports")
softGalleryLanguage_ReactFunctions = Class(name="softGalleryLanguage::ReactFunctions")
softGalleryLanguage_Props = Class(name="softGalleryLanguage::Props")
softGalleryLanguage_ReactImportContent = Class(name="softGalleryLanguage::ReactImportContent")
softGalleryLanguage_ReactConstructor = Class(name="softGalleryLanguage::ReactConstructor")
softGalleryLanguage_ReactCoreFunctions = Class(name="softGalleryLanguage::ReactCoreFunctions")
softGalleryLanguage_LogicStructure = Class(name="softGalleryLanguage::LogicStructure")
softGalleryLanguage_ComponentClass = Class(name="softGalleryLanguage::ComponentClass")
softGalleryLanguage_UIContent = Class(name="softGalleryLanguage::UIContent")
softGalleryLanguage_ViewComponentCont = Class(name="softGalleryLanguage::ViewComponentCont")
softGalleryLanguage_SubcomponentCont = Class(name="softGalleryLanguage::SubcomponentCont")
softGalleryLanguage_ComponentsStylesContent = Class(name="softGalleryLanguage::ComponentsStylesContent")
softGalleryLanguage_StyleProperties = Class(name="softGalleryLanguage::StyleProperties")
softGalleryLanguage_StylePropertiesContent = Class(name="softGalleryLanguage::StylePropertiesContent")
softGalleryLanguage_ReactActionsContent = Class(name="softGalleryLanguage::ReactActionsContent")
softGalleryLanguage_ReactServicesRelation = Class(name="softGalleryLanguage::ReactServicesRelation")
softGalleryLanguage_ReactServicesType = Class(name="softGalleryLanguage::ReactServicesType")
softGalleryLanguage_ReactServiceContent = Class(name="softGalleryLanguage::ReactServiceContent")
softGalleryLanguage_State = Class(name="softGalleryLanguage::State")
softGalleryLanguage_CoreFunctionsDeclaration = Class(name="softGalleryLanguage::CoreFunctionsDeclaration")
softGalleryLanguage_StateContent = Class(name="softGalleryLanguage::StateContent")
softGalleryLanguage_PropsType = Class(name="softGalleryLanguage::PropsType")
softGalleryLanguage_ReactInformation = Class(name="softGalleryLanguage::ReactInformation")
softGalleryLanguage_Cluster = Class(name="softGalleryLanguage::Cluster")
softGalleryLanguage_Database = Class(name="softGalleryLanguage::Database")
softGalleryLanguage_Schema = Class(name="softGalleryLanguage::Schema")
softGalleryLanguage_ReactServiceContRequest = Class(name="softGalleryLanguage::ReactServiceContRequest")
softGalleryLanguage_ReactServiceRequestProps = Class(name="softGalleryLanguage::ReactServiceRequestProps")
softGalleryLanguage_ReactsRelationServ = Class(name="softGalleryLanguage::ReactsRelationServ")
softGalleryLanguage_ReactLibrary = Class(name="softGalleryLanguage::ReactLibrary")
softGalleryLanguage_DatatypeDB = Class(name="softGalleryLanguage::DatatypeDB")
softGalleryLanguage_Constraint = Class(name="softGalleryLanguage::Constraint")
softGalleryLanguage_Row = Class(name="softGalleryLanguage::Row")
softGalleryLanguage_Policy = Class(name="softGalleryLanguage::Policy")
softGalleryLanguage_Trigger = Class(name="softGalleryLanguage::Trigger")
softGalleryLanguage_Function = Class(name="softGalleryLanguage::Function")
softGalleryLanguage_PostgresUser = Class(name="softGalleryLanguage::PostgresUser")
softGalleryLanguage_Index_p = Class(name="softGalleryLanguage::Index::p")
softGalleryLanguage_ViewSchema = Class(name="softGalleryLanguage::ViewSchema")
softGalleryLanguage_Table_p = Class(name="softGalleryLanguage::Table::p")
softGalleryLanguage_ForeignKey = Class(name="softGalleryLanguage::ForeignKey")
softGalleryLanguage_ForeignKey_n = Class(name="softGalleryLanguage::ForeignKey::n")
softGalleryLanguage_ForeignKeyRef = Class(name="softGalleryLanguage::ForeignKeyRef")
softGalleryLanguage_RefTable_p = Class(name="softGalleryLanguage::RefTable::p")
softGalleryLanguage_ColumnP = Class(name="softGalleryLanguage::ColumnP")
softGalleryLanguage_PublicAccess = Class(name="softGalleryLanguage::PublicAccess")
softGalleryLanguage_ObjectsPublic = Class(name="softGalleryLanguage::ObjectsPublic")
softGalleryLanguage_BucketObjectsNotPublic = Class(name="softGalleryLanguage::BucketObjectsNotPublic")
softGalleryLanguage_OnlyAuthorized = Class(name="softGalleryLanguage::OnlyAuthorized")
softGalleryLanguage_AmazonFolder = Class(name="softGalleryLanguage::AmazonFolder")
softGalleryLanguage_AmazonFile = Class(name="softGalleryLanguage::AmazonFile")
softGalleryLanguage_Metadata = Class(name="softGalleryLanguage::Metadata")
softGalleryLanguage_AmazonElasticComputeCloud = Class(name="softGalleryLanguage::AmazonElasticComputeCloud")
softGalleryLanguage_Privilege = Class(name="softGalleryLanguage::Privilege")
softGalleryLanguage_Query = Class(name="softGalleryLanguage::Query")
softGalleryLanguage_Clause = Class(name="softGalleryLanguage::Clause")
softGalleryLanguage_AmazonSimpleStorageService = Class(name="softGalleryLanguage::AmazonSimpleStorageService")
softGalleryLanguage_BatchOperation = Class(name="softGalleryLanguage::BatchOperation")
softGalleryLanguage_Bucket = Class(name="softGalleryLanguage::Bucket")
softGalleryLanguage_BucketAccess = Class(name="softGalleryLanguage::BucketAccess")

# softGalleryLanguage_Functionality class attributes and methods

# softGalleryLanguage_ExceptionsDomain class attributes and methods

# softGalleryLanguage_Entities class attributes and methods
softGalleryLanguage_Entities_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Entities.attributes={softGalleryLanguage_Entities_name}

# softGalleryLanguage_AtributePhoto class attributes and methods
softGalleryLanguage_AtributePhoto_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AtributePhoto.attributes={softGalleryLanguage_AtributePhoto_name}

# softGalleryLanguage_AtributeAlbum class attributes and methods
softGalleryLanguage_AtributeAlbum_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AtributeAlbum.attributes={softGalleryLanguage_AtributeAlbum_name}

# softGalleryLanguage_Model class attributes and methods

# softGalleryLanguage_EObject class attributes and methods

# softGalleryLanguage_Domain class attributes and methods
softGalleryLanguage_Domain_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Domain.attributes={softGalleryLanguage_Domain_name}

# softGalleryLanguage_Entity class attributes and methods

# softGalleryLanguage_AlbumManagement class attributes and methods

# softGalleryLanguage_PhotoActions class attributes and methods

# softGalleryLanguage_LandingActions class attributes and methods

# softGalleryLanguage_ProfileManagementFunctions class attributes and methods
softGalleryLanguage_ProfileManagementFunctions_viewprofileName: Property = Property(name="viewprofileName", type=StringType)
softGalleryLanguage_ProfileManagementFunctions_editProfileName: Property = Property(name="editProfileName", type=StringType)
softGalleryLanguage_ProfileManagementFunctions.attributes={softGalleryLanguage_ProfileManagementFunctions_editProfileName, softGalleryLanguage_ProfileManagementFunctions_viewprofileName}

# softGalleryLanguage_AtributeUserDomain class attributes and methods
softGalleryLanguage_AtributeUserDomain_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AtributeUserDomain.attributes={softGalleryLanguage_AtributeUserDomain_name}

# softGalleryLanguage_Functionalities class attributes and methods

# softGalleryLanguage_ProfileManagement class attributes and methods

# softGalleryLanguage_AppAccess class attributes and methods

# softGalleryLanguage_PhotoActionsFunctions class attributes and methods
softGalleryLanguage_PhotoActionsFunctions_nameGenerico: Property = Property(name="nameGenerico", type=StringType)
softGalleryLanguage_PhotoActionsFunctions_namePhoto: Property = Property(name="namePhoto", type=StringType)
softGalleryLanguage_PhotoActionsFunctions_nameLoad: Property = Property(name="nameLoad", type=StringType)
softGalleryLanguage_PhotoActionsFunctions.attributes={softGalleryLanguage_PhotoActionsFunctions_nameLoad, softGalleryLanguage_PhotoActionsFunctions_nameGenerico, softGalleryLanguage_PhotoActionsFunctions_namePhoto}

# softGalleryLanguage_LandingFunctions class attributes and methods
softGalleryLanguage_LandingFunctions_nameCarouselName: Property = Property(name="nameCarouselName", type=StringType)
softGalleryLanguage_LandingFunctions_passPhotoName: Property = Property(name="passPhotoName", type=StringType)
softGalleryLanguage_LandingFunctions.attributes={softGalleryLanguage_LandingFunctions_nameCarouselName, softGalleryLanguage_LandingFunctions_passPhotoName}

# softGalleryLanguage_ExceptionsType class attributes and methods

# softGalleryLanguage_AppAccessFunctions class attributes and methods
softGalleryLanguage_AppAccessFunctions_loginName: Property = Property(name="loginName", type=StringType)
softGalleryLanguage_AppAccessFunctions_registerName: Property = Property(name="registerName", type=StringType)
softGalleryLanguage_AppAccessFunctions.attributes={softGalleryLanguage_AppAccessFunctions_registerName, softGalleryLanguage_AppAccessFunctions_loginName}

# softGalleryLanguage_AlbumManagementFunctions class attributes and methods
softGalleryLanguage_AlbumManagementFunctions_createdAlbName: Property = Property(name="createdAlbName", type=StringType)
softGalleryLanguage_AlbumManagementFunctions_selectAlbName: Property = Property(name="selectAlbName", type=StringType)
softGalleryLanguage_AlbumManagementFunctions.attributes={softGalleryLanguage_AlbumManagementFunctions_createdAlbName, softGalleryLanguage_AlbumManagementFunctions_selectAlbName}

# softGalleryLanguage_Architecture class attributes and methods

# softGalleryLanguage_NTiers class attributes and methods

# softGalleryLanguage_Layer class attributes and methods

# softGalleryLanguage_PresentationLayer class attributes and methods

# softGalleryLanguage_PresentationContent class attributes and methods

# softGalleryLanguage_PresentationSegments class attributes and methods
softGalleryLanguage_PresentationSegments_presentationSName: Property = Property(name="presentationSName", type=StringType)
softGalleryLanguage_PresentationSegments_presentationCName: Property = Property(name="presentationCName", type=StringType)
softGalleryLanguage_PresentationSegments_presentationAName: Property = Property(name="presentationAName", type=StringType)
softGalleryLanguage_PresentationSegments.attributes={softGalleryLanguage_PresentationSegments_presentationSName, softGalleryLanguage_PresentationSegments_presentationAName, softGalleryLanguage_PresentationSegments_presentationCName}

# softGalleryLanguage_BusinessLogicLayer class attributes and methods

# softGalleryLanguage_PhotoException class attributes and methods
softGalleryLanguage_PhotoException_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PhotoException.attributes={softGalleryLanguage_PhotoException_name}

# softGalleryLanguage_AlbumException class attributes and methods
softGalleryLanguage_AlbumException_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AlbumException.attributes={softGalleryLanguage_AlbumException_name}

# softGalleryLanguage_UserException class attributes and methods
softGalleryLanguage_UserException_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_UserException.attributes={softGalleryLanguage_UserException_name}

# softGalleryLanguage_SegmentStructure class attributes and methods

# softGalleryLanguage_SegmentStructureContent class attributes and methods
softGalleryLanguage_SegmentStructureContent_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SegmentStructureContent.attributes={softGalleryLanguage_SegmentStructureContent_name}

# softGalleryLanguage_DirectoryContent class attributes and methods
softGalleryLanguage_DirectoryContent_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_DirectoryContent.attributes={softGalleryLanguage_DirectoryContent_name}

# softGalleryLanguage_Directories class attributes and methods

# softGalleryLanguage_MultipleFile class attributes and methods
softGalleryLanguage_MultipleFile_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_MultipleFile.attributes={softGalleryLanguage_MultipleFile_name}

# softGalleryLanguage_SingleFile class attributes and methods
softGalleryLanguage_SingleFile_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SingleFile.attributes={softGalleryLanguage_SingleFile_name}

# softGalleryLanguage_LayerRelations class attributes and methods
softGalleryLanguage_LayerRelations_layerelations: Property = Property(name="layerelations", type=StringType)
softGalleryLanguage_LayerRelations_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_LayerRelations.attributes={softGalleryLanguage_LayerRelations_layerelations, softGalleryLanguage_LayerRelations_name}

# softGalleryLanguage_BusinessLogicContent class attributes and methods

# softGalleryLanguage_BusinessLogicSegments class attributes and methods
softGalleryLanguage_BusinessLogicSegments_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_BusinessLogicSegments.attributes={softGalleryLanguage_BusinessLogicSegments_name}

# softGalleryLanguage_ControllerSegmentElement class attributes and methods
softGalleryLanguage_ControllerSegmentElement_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ControllerSegmentElement.attributes={softGalleryLanguage_ControllerSegmentElement_name}

# softGalleryLanguage_SpecificationSegmentElement class attributes and methods
softGalleryLanguage_SpecificationSegmentElement_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SpecificationSegmentElement.attributes={softGalleryLanguage_SpecificationSegmentElement_name}

# softGalleryLanguage_CriteriaAttributeType class attributes and methods
softGalleryLanguage_CriteriaAttributeType_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_CriteriaAttributeType.attributes={softGalleryLanguage_CriteriaAttributeType_name}

# softGalleryLanguage_DataPersistenceLayer class attributes and methods

# softGalleryLanguage_DataPersistenceContent class attributes and methods

# softGalleryLanguage_DataPersistenceSegments class attributes and methods
softGalleryLanguage_DataPersistenceSegments_postSName: Property = Property(name="postSName", type=StringType)
softGalleryLanguage_DataPersistenceSegments_amazonSName: Property = Property(name="amazonSName", type=StringType)
softGalleryLanguage_DataPersistenceSegments.attributes={softGalleryLanguage_DataPersistenceSegments_amazonSName, softGalleryLanguage_DataPersistenceSegments_postSName}

# softGalleryLanguage_NTierSource class attributes and methods

# softGalleryLanguage_NTierTarget class attributes and methods

# softGalleryLanguage_NTiersRelations class attributes and methods
softGalleryLanguage_NTiersRelations_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_NTiersRelations.attributes={softGalleryLanguage_NTiersRelations_name}

# softGalleryLanguage_Technology class attributes and methods
softGalleryLanguage_Technology_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Technology.attributes={softGalleryLanguage_Technology_name}

# softGalleryLanguage_Technologies class attributes and methods

# softGalleryLanguage_Spring class attributes and methods
softGalleryLanguage_Spring_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Spring.attributes={softGalleryLanguage_Spring_name}

# softGalleryLanguage_React class attributes and methods
softGalleryLanguage_React_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_React.attributes={softGalleryLanguage_React_name}

# softGalleryLanguage_LayerSource class attributes and methods
softGalleryLanguage_LayerSource_layerelations: Property = Property(name="layerelations", type=StringType)
softGalleryLanguage_LayerSource.attributes={softGalleryLanguage_LayerSource_layerelations}

# softGalleryLanguage_LayerTarget class attributes and methods
softGalleryLanguage_LayerTarget_layerelations: Property = Property(name="layerelations", type=StringType)
softGalleryLanguage_LayerTarget.attributes={softGalleryLanguage_LayerTarget_layerelations}

# softGalleryLanguage_ArchitectureComponents class attributes and methods

# softGalleryLanguage_FrontEnd class attributes and methods
softGalleryLanguage_FrontEnd_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_FrontEnd.attributes={softGalleryLanguage_FrontEnd_name}

# softGalleryLanguage_BackEnd class attributes and methods
softGalleryLanguage_BackEnd_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_BackEnd.attributes={softGalleryLanguage_BackEnd_name}

# softGalleryLanguage_PersistenceDataComponent class attributes and methods
softGalleryLanguage_PersistenceDataComponent_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PersistenceDataComponent.attributes={softGalleryLanguage_PersistenceDataComponent_name}

# softGalleryLanguage_NTiersConnections class attributes and methods

# softGalleryLanguage_NTierConnectionContent class attributes and methods
softGalleryLanguage_NTierConnectionContent_nTierName: Property = Property(name="nTierName", type=StringType)
softGalleryLanguage_NTierConnectionContent_ntierconnection: Property = Property(name="ntierconnection", type=StringType)
softGalleryLanguage_NTierConnectionContent.attributes={softGalleryLanguage_NTierConnectionContent_nTierName, softGalleryLanguage_NTierConnectionContent_ntierconnection}

# softGalleryLanguage_SpringRepository class attributes and methods

# softGalleryLanguage_SpringRepositories class attributes and methods
softGalleryLanguage_SpringRepositories_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SpringRepositories.attributes={softGalleryLanguage_SpringRepositories_name}

# softGalleryLanguage_SpringRepositoryAnnotation class attributes and methods
softGalleryLanguage_SpringRepositoryAnnotation_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SpringRepositoryAnnotation.attributes={softGalleryLanguage_SpringRepositoryAnnotation_name}

# softGalleryLanguage_RestController class attributes and methods
softGalleryLanguage_RestController_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_RestController.attributes={softGalleryLanguage_RestController_name}

# softGalleryLanguage_Specification class attributes and methods

# softGalleryLanguage_Predicate class attributes and methods
softGalleryLanguage_Predicate_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Predicate.attributes={softGalleryLanguage_Predicate_name}

# softGalleryLanguage_SearchCriteria class attributes and methods
softGalleryLanguage_SearchCriteria_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SearchCriteria.attributes={softGalleryLanguage_SearchCriteria_name}

# softGalleryLanguage_PostgreSQL class attributes and methods
softGalleryLanguage_PostgreSQL_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PostgreSQL.attributes={softGalleryLanguage_PostgreSQL_name}

# softGalleryLanguage_AmazonWebServices class attributes and methods
softGalleryLanguage_AmazonWebServices_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AmazonWebServices.attributes={softGalleryLanguage_AmazonWebServices_name}

# softGalleryLanguage_SpringBootApplication class attributes and methods

# softGalleryLanguage_Configuration class attributes and methods

# softGalleryLanguage_EnableGlobalMethodSecurity class attributes and methods
softGalleryLanguage_EnableGlobalMethodSecurity_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_EnableGlobalMethodSecurity.attributes={softGalleryLanguage_EnableGlobalMethodSecurity_name}

# softGalleryLanguage_EnableAuthorizationServer class attributes and methods
softGalleryLanguage_EnableAuthorizationServer_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_EnableAuthorizationServer.attributes={softGalleryLanguage_EnableAuthorizationServer_name}

# softGalleryLanguage_EnableResourceServer class attributes and methods
softGalleryLanguage_EnableResourceServer_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_EnableResourceServer.attributes={softGalleryLanguage_EnableResourceServer_name}

# softGalleryLanguage_EnableWebSecurity class attributes and methods
softGalleryLanguage_EnableWebSecurity_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_EnableWebSecurity.attributes={softGalleryLanguage_EnableWebSecurity_name}

# softGalleryLanguage_SpringComponent class attributes and methods

# softGalleryLanguage_OrderSpring class attributes and methods
softGalleryLanguage_OrderSpring_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_OrderSpring.attributes={softGalleryLanguage_OrderSpring_name}

# softGalleryLanguage_GetMapping class attributes and methods
softGalleryLanguage_GetMapping_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_GetMapping.attributes={softGalleryLanguage_GetMapping_name}

# softGalleryLanguage_PutMapping class attributes and methods
softGalleryLanguage_PutMapping_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PutMapping.attributes={softGalleryLanguage_PutMapping_name}

# softGalleryLanguage_DeleteMapping class attributes and methods
softGalleryLanguage_DeleteMapping_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_DeleteMapping.attributes={softGalleryLanguage_DeleteMapping_name}

# softGalleryLanguage_ResponseParameterAnnotation class attributes and methods
softGalleryLanguage_ResponseParameterAnnotation_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ResponseParameterAnnotation.attributes={softGalleryLanguage_ResponseParameterAnnotation_name}

# softGalleryLanguage_ResponseParameterType class attributes and methods
softGalleryLanguage_ResponseParameterType_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ResponseParameterType.attributes={softGalleryLanguage_ResponseParameterType_name}

# softGalleryLanguage_ResponseParameterName class attributes and methods
softGalleryLanguage_ResponseParameterName_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ResponseParameterName.attributes={softGalleryLanguage_ResponseParameterName_name}

# softGalleryLanguage_ExceptionHandler class attributes and methods
softGalleryLanguage_ExceptionHandler_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ExceptionHandler.attributes={softGalleryLanguage_ExceptionHandler_name}

# softGalleryLanguage_ExceptionProcess class attributes and methods
softGalleryLanguage_ExceptionProcess_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ExceptionProcess.attributes={softGalleryLanguage_ExceptionProcess_name}

# softGalleryLanguage_Autowired class attributes and methods
softGalleryLanguage_Autowired_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Autowired.attributes={softGalleryLanguage_Autowired_name}

# softGalleryLanguage_ResponseEntity class attributes and methods
softGalleryLanguage_ResponseEntity_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ResponseEntity.attributes={softGalleryLanguage_ResponseEntity_name}

# softGalleryLanguage_MappingType class attributes and methods

# softGalleryLanguage_ResponseParameter class attributes and methods

# softGalleryLanguage_RequestMapping class attributes and methods

# MappingType class attributes and methods

# softGalleryLanguage_RequestMappingValue class attributes and methods
softGalleryLanguage_RequestMappingValue_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_RequestMappingValue.attributes={softGalleryLanguage_RequestMappingValue_name}

# softGalleryLanguage_RequestMappingMethod class attributes and methods
softGalleryLanguage_RequestMappingMethod_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_RequestMappingMethod.attributes={softGalleryLanguage_RequestMappingMethod_name}

# softGalleryLanguage_RequestMappingProduces class attributes and methods
softGalleryLanguage_RequestMappingProduces_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_RequestMappingProduces.attributes={softGalleryLanguage_RequestMappingProduces_name}

# softGalleryLanguage_PostMapping class attributes and methods
softGalleryLanguage_PostMapping_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PostMapping.attributes={softGalleryLanguage_PostMapping_name}

# softGalleryLanguage_StorageActionMember class attributes and methods

# softGalleryLanguage_StorageActionMemberType class attributes and methods
softGalleryLanguage_StorageActionMemberType_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageActionMemberType.attributes={softGalleryLanguage_StorageActionMemberType_name}

# softGalleryLanguage_StorageActionMemberName class attributes and methods
softGalleryLanguage_StorageActionMemberName_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageActionMemberName.attributes={softGalleryLanguage_StorageActionMemberName_name}

# softGalleryLanguage_ReactModules class attributes and methods

# softGalleryLanguage_ReactSubModules class attributes and methods

# softGalleryLanguage_ReactConfiguration class attributes and methods

# softGalleryLanguage_ReactComponents class attributes and methods

# softGalleryLanguage_ReactActions class attributes and methods

# softGalleryLanguage_SpringEntity class attributes and methods

# softGalleryLanguage_SpringEntityAnnotationTypes class attributes and methods
softGalleryLanguage_SpringEntityAnnotationTypes_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_SpringEntityAnnotationTypes.attributes={softGalleryLanguage_SpringEntityAnnotationTypes_name}

# softGalleryLanguage_StorageClient class attributes and methods
softGalleryLanguage_StorageClient_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageClient.attributes={softGalleryLanguage_StorageClient_name}

# softGalleryLanguage_StorageMember class attributes and methods
softGalleryLanguage_StorageMember_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageMember.attributes={softGalleryLanguage_StorageMember_name}

# softGalleryLanguage_StorageMemberType class attributes and methods
softGalleryLanguage_StorageMemberType_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageMemberType.attributes={softGalleryLanguage_StorageMemberType_name}

# softGalleryLanguage_StorageMemberAnnotation class attributes and methods
softGalleryLanguage_StorageMemberAnnotation_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageMemberAnnotation.attributes={softGalleryLanguage_StorageMemberAnnotation_name}

# softGalleryLanguage_StorageAction class attributes and methods
softGalleryLanguage_StorageAction_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageAction.attributes={softGalleryLanguage_StorageAction_name}

# softGalleryLanguage_StorageActionAnnotation class attributes and methods
softGalleryLanguage_StorageActionAnnotation_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageActionAnnotation.attributes={softGalleryLanguage_StorageActionAnnotation_name}

# softGalleryLanguage_StorageActionReturn class attributes and methods
softGalleryLanguage_StorageActionReturn_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_StorageActionReturn.attributes={softGalleryLanguage_StorageActionReturn_name}

# softGalleryLanguage_PackageVersion class attributes and methods
softGalleryLanguage_PackageVersion_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PackageVersion.attributes={softGalleryLanguage_PackageVersion_name}

# softGalleryLanguage_DOMConfigurations class attributes and methods
softGalleryLanguage_DOMConfigurations_elements: Property = Property(name="elements", type=StringType)
softGalleryLanguage_DOMConfigurations_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_DOMConfigurations.attributes={softGalleryLanguage_DOMConfigurations_name, softGalleryLanguage_DOMConfigurations_elements}

# softGalleryLanguage_ComponentsLogic class attributes and methods
softGalleryLanguage_ComponentsLogic_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ComponentsLogic.attributes={softGalleryLanguage_ComponentsLogic_name}

# softGalleryLanguage_ComponentsUI class attributes and methods
softGalleryLanguage_ComponentsUI_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ComponentsUI.attributes={softGalleryLanguage_ComponentsUI_name}

# softGalleryLanguage_ComponentsStyles class attributes and methods

# softGalleryLanguage_LogicContent class attributes and methods
softGalleryLanguage_LogicContent_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_LogicContent.attributes={softGalleryLanguage_LogicContent_name}

# softGalleryLanguage_ReactLibraries class attributes and methods

# softGalleryLanguage_ReactInfo class attributes and methods

# softGalleryLanguage_ReactDependencies class attributes and methods

# softGalleryLanguage_ReactConfigurations class attributes and methods
softGalleryLanguage_ReactConfigurations_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactConfigurations.attributes={softGalleryLanguage_ReactConfigurations_name}

# softGalleryLanguage_ReactDependenciesRules class attributes and methods
softGalleryLanguage_ReactDependenciesRules_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactDependenciesRules.attributes={softGalleryLanguage_ReactDependenciesRules_name}

# softGalleryLanguage_ReactDependenciesSubRules class attributes and methods

# softGalleryLanguage_SingleDependencies class attributes and methods

# softGalleryLanguage_PackageName class attributes and methods
softGalleryLanguage_PackageName_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PackageName.attributes={softGalleryLanguage_PackageName_name}

# softGalleryLanguage_ReactImports class attributes and methods

# softGalleryLanguage_ReactFunctions class attributes and methods
softGalleryLanguage_ReactFunctions_lifecycleclass: Property = Property(name="lifecycleclass", type=StringType)
softGalleryLanguage_ReactFunctions_renderclass: Property = Property(name="renderclass", type=StringType)
softGalleryLanguage_ReactFunctions.attributes={softGalleryLanguage_ReactFunctions_renderclass, softGalleryLanguage_ReactFunctions_lifecycleclass}

# softGalleryLanguage_Props class attributes and methods

# softGalleryLanguage_ReactImportContent class attributes and methods
softGalleryLanguage_ReactImportContent_impName: Property = Property(name="impName", type=StringType)
softGalleryLanguage_ReactImportContent.attributes={softGalleryLanguage_ReactImportContent_impName}

# softGalleryLanguage_ReactConstructor class attributes and methods

# softGalleryLanguage_ReactCoreFunctions class attributes and methods
softGalleryLanguage_ReactCoreFunctions_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactCoreFunctions.attributes={softGalleryLanguage_ReactCoreFunctions_name}

# softGalleryLanguage_LogicStructure class attributes and methods
softGalleryLanguage_LogicStructure_appComName: Property = Property(name="appComName", type=StringType)
softGalleryLanguage_LogicStructure_indexCompName: Property = Property(name="indexCompName", type=StringType)
softGalleryLanguage_LogicStructure.attributes={softGalleryLanguage_LogicStructure_indexCompName, softGalleryLanguage_LogicStructure_appComName}

# softGalleryLanguage_ComponentClass class attributes and methods

# softGalleryLanguage_UIContent class attributes and methods

# softGalleryLanguage_ViewComponentCont class attributes and methods
softGalleryLanguage_ViewComponentCont_nameView: Property = Property(name="nameView", type=StringType)
softGalleryLanguage_ViewComponentCont.attributes={softGalleryLanguage_ViewComponentCont_nameView}

# softGalleryLanguage_SubcomponentCont class attributes and methods
softGalleryLanguage_SubcomponentCont_nameSubComp: Property = Property(name="nameSubComp", type=StringType)
softGalleryLanguage_SubcomponentCont.attributes={softGalleryLanguage_SubcomponentCont_nameSubComp}

# softGalleryLanguage_ComponentsStylesContent class attributes and methods
softGalleryLanguage_ComponentsStylesContent_nameStyle: Property = Property(name="nameStyle", type=StringType)
softGalleryLanguage_ComponentsStylesContent.attributes={softGalleryLanguage_ComponentsStylesContent_nameStyle}

# softGalleryLanguage_StyleProperties class attributes and methods

# softGalleryLanguage_StylePropertiesContent class attributes and methods
softGalleryLanguage_StylePropertiesContent_propName: Property = Property(name="propName", type=StringType)
softGalleryLanguage_StylePropertiesContent.attributes={softGalleryLanguage_StylePropertiesContent_propName}

# softGalleryLanguage_ReactActionsContent class attributes and methods

# softGalleryLanguage_ReactServicesRelation class attributes and methods

# softGalleryLanguage_ReactServicesType class attributes and methods
softGalleryLanguage_ReactServicesType_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactServicesType.attributes={softGalleryLanguage_ReactServicesType_name}

# softGalleryLanguage_ReactServiceContent class attributes and methods
softGalleryLanguage_ReactServiceContent_functName: Property = Property(name="functName", type=StringType)
softGalleryLanguage_ReactServiceContent.attributes={softGalleryLanguage_ReactServiceContent_functName}

# softGalleryLanguage_State class attributes and methods

# softGalleryLanguage_CoreFunctionsDeclaration class attributes and methods
softGalleryLanguage_CoreFunctionsDeclaration_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_CoreFunctionsDeclaration.attributes={softGalleryLanguage_CoreFunctionsDeclaration_name}

# softGalleryLanguage_StateContent class attributes and methods
softGalleryLanguage_StateContent_stateName: Property = Property(name="stateName", type=StringType)
softGalleryLanguage_StateContent_componentdatatyp: Property = Property(name="componentdatatyp", type=StringType)
softGalleryLanguage_StateContent.attributes={softGalleryLanguage_StateContent_stateName, softGalleryLanguage_StateContent_componentdatatyp}

# softGalleryLanguage_PropsType class attributes and methods
softGalleryLanguage_PropsType_nameProps: Property = Property(name="nameProps", type=StringType)
softGalleryLanguage_PropsType_propsdatas: Property = Property(name="propsdatas", type=StringType)
softGalleryLanguage_PropsType.attributes={softGalleryLanguage_PropsType_propsdatas, softGalleryLanguage_PropsType_nameProps}

# softGalleryLanguage_ReactInformation class attributes and methods
softGalleryLanguage_ReactInformation_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactInformation.attributes={softGalleryLanguage_ReactInformation_name}

# softGalleryLanguage_Cluster class attributes and methods

# softGalleryLanguage_Database class attributes and methods
softGalleryLanguage_Database_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Database.attributes={softGalleryLanguage_Database_name}

# softGalleryLanguage_Schema class attributes and methods

# softGalleryLanguage_ReactServiceContRequest class attributes and methods

# softGalleryLanguage_ReactServiceRequestProps class attributes and methods
softGalleryLanguage_ReactServiceRequestProps_reqPropName: Property = Property(name="reqPropName", type=StringType)
softGalleryLanguage_ReactServiceRequestProps_reqPropDescription: Property = Property(name="reqPropDescription", type=StringType)
softGalleryLanguage_ReactServiceRequestProps.attributes={softGalleryLanguage_ReactServiceRequestProps_reqPropDescription, softGalleryLanguage_ReactServiceRequestProps_reqPropName}

# softGalleryLanguage_ReactsRelationServ class attributes and methods
softGalleryLanguage_ReactsRelationServ_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactsRelationServ.attributes={softGalleryLanguage_ReactsRelationServ_name}

# softGalleryLanguage_ReactLibrary class attributes and methods
softGalleryLanguage_ReactLibrary_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ReactLibrary.attributes={softGalleryLanguage_ReactLibrary_name}

# softGalleryLanguage_DatatypeDB class attributes and methods
softGalleryLanguage_DatatypeDB_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_DatatypeDB.attributes={softGalleryLanguage_DatatypeDB_name}

# softGalleryLanguage_Constraint class attributes and methods
softGalleryLanguage_Constraint_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Constraint.attributes={softGalleryLanguage_Constraint_name}

# softGalleryLanguage_Row class attributes and methods
softGalleryLanguage_Row_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Row.attributes={softGalleryLanguage_Row_name}

# softGalleryLanguage_Policy class attributes and methods
softGalleryLanguage_Policy_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Policy.attributes={softGalleryLanguage_Policy_name}

# softGalleryLanguage_Trigger class attributes and methods
softGalleryLanguage_Trigger_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Trigger.attributes={softGalleryLanguage_Trigger_name}

# softGalleryLanguage_Function class attributes and methods
softGalleryLanguage_Function_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Function.attributes={softGalleryLanguage_Function_name}

# softGalleryLanguage_PostgresUser class attributes and methods
softGalleryLanguage_PostgresUser_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PostgresUser.attributes={softGalleryLanguage_PostgresUser_name}

# softGalleryLanguage_Index_p class attributes and methods
softGalleryLanguage_Index_p_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Index_p.attributes={softGalleryLanguage_Index_p_name}

# softGalleryLanguage_ViewSchema class attributes and methods
softGalleryLanguage_ViewSchema_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ViewSchema.attributes={softGalleryLanguage_ViewSchema_name}

# softGalleryLanguage_Table_p class attributes and methods
softGalleryLanguage_Table_p_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Table_p.attributes={softGalleryLanguage_Table_p_name}

# softGalleryLanguage_ForeignKey class attributes and methods

# softGalleryLanguage_ForeignKey_n class attributes and methods
softGalleryLanguage_ForeignKey_n_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ForeignKey_n.attributes={softGalleryLanguage_ForeignKey_n_name}

# softGalleryLanguage_ForeignKeyRef class attributes and methods

# softGalleryLanguage_RefTable_p class attributes and methods
softGalleryLanguage_RefTable_p_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_RefTable_p.attributes={softGalleryLanguage_RefTable_p_name}

# softGalleryLanguage_ColumnP class attributes and methods
softGalleryLanguage_ColumnP_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ColumnP.attributes={softGalleryLanguage_ColumnP_name}

# softGalleryLanguage_PublicAccess class attributes and methods
softGalleryLanguage_PublicAccess_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_PublicAccess.attributes={softGalleryLanguage_PublicAccess_name}

# softGalleryLanguage_ObjectsPublic class attributes and methods
softGalleryLanguage_ObjectsPublic_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_ObjectsPublic.attributes={softGalleryLanguage_ObjectsPublic_name}

# softGalleryLanguage_BucketObjectsNotPublic class attributes and methods
softGalleryLanguage_BucketObjectsNotPublic_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_BucketObjectsNotPublic.attributes={softGalleryLanguage_BucketObjectsNotPublic_name}

# softGalleryLanguage_OnlyAuthorized class attributes and methods
softGalleryLanguage_OnlyAuthorized_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_OnlyAuthorized.attributes={softGalleryLanguage_OnlyAuthorized_name}

# softGalleryLanguage_AmazonFolder class attributes and methods
softGalleryLanguage_AmazonFolder_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AmazonFolder.attributes={softGalleryLanguage_AmazonFolder_name}

# softGalleryLanguage_AmazonFile class attributes and methods

# softGalleryLanguage_Metadata class attributes and methods
softGalleryLanguage_Metadata_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Metadata.attributes={softGalleryLanguage_Metadata_name}

# softGalleryLanguage_AmazonElasticComputeCloud class attributes and methods
softGalleryLanguage_AmazonElasticComputeCloud_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_AmazonElasticComputeCloud.attributes={softGalleryLanguage_AmazonElasticComputeCloud_name}

# softGalleryLanguage_Privilege class attributes and methods
softGalleryLanguage_Privilege_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Privilege.attributes={softGalleryLanguage_Privilege_name}

# softGalleryLanguage_Query class attributes and methods

# softGalleryLanguage_Clause class attributes and methods
softGalleryLanguage_Clause_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Clause.attributes={softGalleryLanguage_Clause_name}

# softGalleryLanguage_AmazonSimpleStorageService class attributes and methods

# softGalleryLanguage_BatchOperation class attributes and methods
softGalleryLanguage_BatchOperation_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_BatchOperation.attributes={softGalleryLanguage_BatchOperation_name}

# softGalleryLanguage_Bucket class attributes and methods
softGalleryLanguage_Bucket_name: Property = Property(name="name", type=StringType)
softGalleryLanguage_Bucket.attributes={softGalleryLanguage_Bucket_name}

# softGalleryLanguage_BucketAccess class attributes and methods

# Relationships
entityfuncs2: BinaryAssociation = BinaryAssociation(
    name="entityfuncs2",
    ends={
        Property(name="softGalleryLanguage_Functionality", type=softGalleryLanguage_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Domain3", type=softGalleryLanguage_Functionality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionsdomain4: BinaryAssociation = BinaryAssociation(
    name="exceptionsdomain4",
    ends={
        Property(name="softGalleryLanguage_ExceptionsDomain", type=softGalleryLanguage_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Domain5", type=softGalleryLanguage_ExceptionsDomain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements6: BinaryAssociation = BinaryAssociation(
    name="elements6",
    ends={
        Property(name="softGalleryLanguage_Entities", type=softGalleryLanguage_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Entity7", type=softGalleryLanguage_Entities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atributePhoto8: BinaryAssociation = BinaryAssociation(
    name="atributePhoto8",
    ends={
        Property(name="softGalleryLanguage_AtributePhoto", type=softGalleryLanguage_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Entities9", type=softGalleryLanguage_AtributePhoto, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atributeAlbum10: BinaryAssociation = BinaryAssociation(
    name="atributeAlbum10",
    ends={
        Property(name="softGalleryLanguage_AtributeAlbum", type=softGalleryLanguage_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Entities11", type=softGalleryLanguage_AtributeAlbum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="softGalleryLanguage_EObject", type=softGalleryLanguage_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Model", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entitydomain1: BinaryAssociation = BinaryAssociation(
    name="entitydomain1",
    ends={
        Property(name="softGalleryLanguage_Entity", type=softGalleryLanguage_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Domain", type=softGalleryLanguage_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="softGalleryLanguage_Functionalities19", type=softGalleryLanguage_AppAccess, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="softGalleryLanguage_AppAccess", type=softGalleryLanguage_Functionalities, multiplicity=Multiplicity(1, 1))
    }
)
items20: BinaryAssociation = BinaryAssociation(
    name="items20",
    ends={
        Property(name="softGalleryLanguage_AlbumManagement", type=softGalleryLanguage_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Functionalities21", type=softGalleryLanguage_AlbumManagement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources22: BinaryAssociation = BinaryAssociation(
    name="resources22",
    ends={
        Property(name="softGalleryLanguage_PhotoActions", type=softGalleryLanguage_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Functionalities23", type=softGalleryLanguage_PhotoActions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aditionals24: BinaryAssociation = BinaryAssociation(
    name="aditionals24",
    ends={
        Property(name="softGalleryLanguage_LandingActions", type=softGalleryLanguage_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Functionalities25", type=softGalleryLanguage_LandingActions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items26: BinaryAssociation = BinaryAssociation(
    name="items26",
    ends={
        Property(name="softGalleryLanguage_ProfileManagementFunctions", type=softGalleryLanguage_ProfileManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ProfileManagement27", type=softGalleryLanguage_ProfileManagementFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atributeUserDomain12: BinaryAssociation = BinaryAssociation(
    name="atributeUserDomain12",
    ends={
        Property(name="softGalleryLanguage_AtributeUserDomain", type=softGalleryLanguage_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Entities13", type=softGalleryLanguage_AtributeUserDomain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements14: BinaryAssociation = BinaryAssociation(
    name="elements14",
    ends={
        Property(name="softGalleryLanguage_Functionalities", type=softGalleryLanguage_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Functionality15", type=softGalleryLanguage_Functionalities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions16: BinaryAssociation = BinaryAssociation(
    name="functions16",
    ends={
        Property(name="softGalleryLanguage_ProfileManagement", type=softGalleryLanguage_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Functionalities17", type=softGalleryLanguage_ProfileManagement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items32: BinaryAssociation = BinaryAssociation(
    name="items32",
    ends={
        Property(name="softGalleryLanguage_PhotoActionsFunctions", type=softGalleryLanguage_PhotoActions, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_PhotoActions33", type=softGalleryLanguage_PhotoActionsFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items34: BinaryAssociation = BinaryAssociation(
    name="items34",
    ends={
        Property(name="softGalleryLanguage_LandingFunctions", type=softGalleryLanguage_LandingActions, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_LandingActions35", type=softGalleryLanguage_LandingFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items28: BinaryAssociation = BinaryAssociation(
    name="items28",
    ends={
        Property(name="softGalleryLanguage_AppAccessFunctions", type=softGalleryLanguage_AppAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_AppAccess29", type=softGalleryLanguage_AppAccessFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items30: BinaryAssociation = BinaryAssociation(
    name="items30",
    ends={
        Property(name="softGalleryLanguage_AlbumManagementFunctions", type=softGalleryLanguage_AlbumManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_AlbumManagement31", type=softGalleryLanguage_AlbumManagementFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements44: BinaryAssociation = BinaryAssociation(
    name="elements44",
    ends={
        Property(name="softGalleryLanguage_EObject45", type=softGalleryLanguage_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Architecture", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements46: BinaryAssociation = BinaryAssociation(
    name="elements46",
    ends={
        Property(name="softGalleryLanguage_EObject47", type=softGalleryLanguage_NTiers, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_NTiers", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layer48: BinaryAssociation = BinaryAssociation(
    name="layer48",
    ends={
        Property(name="softGalleryLanguage_EObject49", type=softGalleryLanguage_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Layer", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentationLayer50: BinaryAssociation = BinaryAssociation(
    name="presentationLayer50",
    ends={
        Property(name="softGalleryLanguage_EObject51", type=softGalleryLanguage_PresentationLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_PresentationLayer", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements52: BinaryAssociation = BinaryAssociation(
    name="elements52",
    ends={
        Property(name="softGalleryLanguage_PresentationSegments", type=softGalleryLanguage_PresentationContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_PresentationContent", type=softGalleryLanguage_PresentationSegments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessLogicLayer53: BinaryAssociation = BinaryAssociation(
    name="businessLogicLayer53",
    ends={
        Property(name="softGalleryLanguage_EObject54", type=softGalleryLanguage_BusinessLogicLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_BusinessLogicLayer", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionsType36: BinaryAssociation = BinaryAssociation(
    name="exceptionsType36",
    ends={
        Property(name="softGalleryLanguage_ExceptionsType", type=softGalleryLanguage_ExceptionsDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ExceptionsDomain37", type=softGalleryLanguage_ExceptionsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
photoException38: BinaryAssociation = BinaryAssociation(
    name="photoException38",
    ends={
        Property(name="softGalleryLanguage_PhotoException", type=softGalleryLanguage_ExceptionsType, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ExceptionsType39", type=softGalleryLanguage_PhotoException, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
albumException40: BinaryAssociation = BinaryAssociation(
    name="albumException40",
    ends={
        Property(name="softGalleryLanguage_AlbumException", type=softGalleryLanguage_ExceptionsType, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ExceptionsType41", type=softGalleryLanguage_AlbumException, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userException42: BinaryAssociation = BinaryAssociation(
    name="userException42",
    ends={
        Property(name="softGalleryLanguage_UserException", type=softGalleryLanguage_ExceptionsType, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ExceptionsType43", type=softGalleryLanguage_UserException, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements65: BinaryAssociation = BinaryAssociation(
    name="elements65",
    ends={
        Property(name="softGalleryLanguage_SegmentStructureContent", type=softGalleryLanguage_SegmentStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SegmentStructure", type=softGalleryLanguage_SegmentStructureContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements66: BinaryAssociation = BinaryAssociation(
    name="elements66",
    ends={
        Property(name="softGalleryLanguage_DirectoryContent", type=softGalleryLanguage_SegmentStructureContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SegmentStructureContent67", type=softGalleryLanguage_DirectoryContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directories68: BinaryAssociation = BinaryAssociation(
    name="directories68",
    ends={
        Property(name="softGalleryLanguage_EObject70", type=softGalleryLanguage_DirectoryContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_DirectoryContent69", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements71: BinaryAssociation = BinaryAssociation(
    name="elements71",
    ends={
        Property(name="softGalleryLanguage_MultipleFile", type=softGalleryLanguage_Directories, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Directories", type=softGalleryLanguage_MultipleFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessLogicSegments55: BinaryAssociation = BinaryAssociation(
    name="businessLogicSegments55",
    ends={
        Property(name="softGalleryLanguage_BusinessLogicSegments", type=softGalleryLanguage_BusinessLogicContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_BusinessLogicContent", type=softGalleryLanguage_BusinessLogicSegments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllerSegmentElement56: BinaryAssociation = BinaryAssociation(
    name="controllerSegmentElement56",
    ends={
        Property(name="softGalleryLanguage_ControllerSegmentElement", type=softGalleryLanguage_BusinessLogicSegments, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_BusinessLogicSegments57", type=softGalleryLanguage_ControllerSegmentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificationSegmentElement58: BinaryAssociation = BinaryAssociation(
    name="specificationSegmentElement58",
    ends={
        Property(name="softGalleryLanguage_SpecificationSegmentElement", type=softGalleryLanguage_BusinessLogicSegments, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_BusinessLogicSegments59", type=softGalleryLanguage_SpecificationSegmentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
criteriaAttributeType60: BinaryAssociation = BinaryAssociation(
    name="criteriaAttributeType60",
    ends={
        Property(name="softGalleryLanguage_CriteriaAttributeType", type=softGalleryLanguage_SpecificationSegmentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SpecificationSegmentElement61", type=softGalleryLanguage_CriteriaAttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements62: BinaryAssociation = BinaryAssociation(
    name="elements62",
    ends={
        Property(name="softGalleryLanguage_DataPersistenceContent", type=softGalleryLanguage_DataPersistenceLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_DataPersistenceLayer", type=softGalleryLanguage_DataPersistenceContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements63: BinaryAssociation = BinaryAssociation(
    name="elements63",
    ends={
        Property(name="softGalleryLanguage_DataPersistenceSegments", type=softGalleryLanguage_DataPersistenceContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_DataPersistenceContent64", type=softGalleryLanguage_DataPersistenceSegments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierorigin81: BinaryAssociation = BinaryAssociation(
    name="ntierorigin81",
    ends={
        Property(name="softGalleryLanguage_NTierSource", type=softGalleryLanguage_NTierConnectionContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_NTierConnectionContent82", type=softGalleryLanguage_NTierSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntiertarget83: BinaryAssociation = BinaryAssociation(
    name="ntiertarget83",
    ends={
        Property(name="softGalleryLanguage_NTierTarget", type=softGalleryLanguage_NTierConnectionContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_NTierConnectionContent84", type=softGalleryLanguage_NTierTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierconnection85: BinaryAssociation = BinaryAssociation(
    name="ntierconnection85",
    ends={
        Property(name="softGalleryLanguage_NTiersRelations", type=softGalleryLanguage_NTierSource, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_NTierSource86", type=softGalleryLanguage_NTiersRelations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierconnection87: BinaryAssociation = BinaryAssociation(
    name="ntierconnection87",
    ends={
        Property(name="softGalleryLanguage_NTiersRelations89", type=softGalleryLanguage_NTierTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_NTierTarget88", type=softGalleryLanguage_NTiersRelations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements90: BinaryAssociation = BinaryAssociation(
    name="elements90",
    ends={
        Property(name="softGalleryLanguage_Technologies", type=softGalleryLanguage_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Technology", type=softGalleryLanguage_Technologies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
techspring91: BinaryAssociation = BinaryAssociation(
    name="techspring91",
    ends={
        Property(name="softGalleryLanguage_Spring", type=softGalleryLanguage_Technologies, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Technologies92", type=softGalleryLanguage_Spring, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
techreact93: BinaryAssociation = BinaryAssociation(
    name="techreact93",
    ends={
        Property(name="softGalleryLanguage_React", type=softGalleryLanguage_Technologies, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Technologies94", type=softGalleryLanguage_React, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layerorigin72: BinaryAssociation = BinaryAssociation(
    name="layerorigin72",
    ends={
        Property(name="softGalleryLanguage_LayerSource", type=softGalleryLanguage_LayerRelations, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_LayerRelations", type=softGalleryLanguage_LayerSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layertarget73: BinaryAssociation = BinaryAssociation(
    name="layertarget73",
    ends={
        Property(name="softGalleryLanguage_LayerTarget", type=softGalleryLanguage_LayerRelations, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_LayerRelations74", type=softGalleryLanguage_LayerTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archFeComponent75: BinaryAssociation = BinaryAssociation(
    name="archFeComponent75",
    ends={
        Property(name="softGalleryLanguage_FrontEnd", type=softGalleryLanguage_ArchitectureComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ArchitectureComponents", type=softGalleryLanguage_FrontEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archBeComponent76: BinaryAssociation = BinaryAssociation(
    name="archBeComponent76",
    ends={
        Property(name="softGalleryLanguage_BackEnd", type=softGalleryLanguage_ArchitectureComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ArchitectureComponents77", type=softGalleryLanguage_BackEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archPdComponent78: BinaryAssociation = BinaryAssociation(
    name="archPdComponent78",
    ends={
        Property(name="softGalleryLanguage_PersistenceDataComponent", type=softGalleryLanguage_ArchitectureComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ArchitectureComponents79", type=softGalleryLanguage_PersistenceDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierconnections80: BinaryAssociation = BinaryAssociation(
    name="ntierconnections80",
    ends={
        Property(name="softGalleryLanguage_NTierConnectionContent", type=softGalleryLanguage_NTiersConnections, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_NTiersConnections", type=softGalleryLanguage_NTierConnectionContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements107: BinaryAssociation = BinaryAssociation(
    name="elements107",
    ends={
        Property(name="softGalleryLanguage_EObject108", type=softGalleryLanguage_SpringRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SpringRepository", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements109: BinaryAssociation = BinaryAssociation(
    name="elements109",
    ends={
        Property(name="softGalleryLanguage_EObject110", type=softGalleryLanguage_RestController, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_RestController", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements111: BinaryAssociation = BinaryAssociation(
    name="elements111",
    ends={
        Property(name="softGalleryLanguage_EObject112", type=softGalleryLanguage_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Specification", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
techpostgresql95: BinaryAssociation = BinaryAssociation(
    name="techpostgresql95",
    ends={
        Property(name="softGalleryLanguage_PostgreSQL", type=softGalleryLanguage_Technologies, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Technologies96", type=softGalleryLanguage_PostgreSQL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
techamazon97: BinaryAssociation = BinaryAssociation(
    name="techamazon97",
    ends={
        Property(name="softGalleryLanguage_AmazonWebServices", type=softGalleryLanguage_Technologies, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Technologies98", type=softGalleryLanguage_AmazonWebServices, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements99: BinaryAssociation = BinaryAssociation(
    name="elements99",
    ends={
        Property(name="softGalleryLanguage_SpringBootApplication", type=softGalleryLanguage_Spring, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Spring100", type=softGalleryLanguage_SpringBootApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements101: BinaryAssociation = BinaryAssociation(
    name="elements101",
    ends={
        Property(name="softGalleryLanguage_EObject103", type=softGalleryLanguage_SpringBootApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SpringBootApplication102", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements104: BinaryAssociation = BinaryAssociation(
    name="elements104",
    ends={
        Property(name="softGalleryLanguage_EObject105", type=softGalleryLanguage_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Configuration", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements106: BinaryAssociation = BinaryAssociation(
    name="elements106",
    ends={
        Property(name="softGalleryLanguage_OrderSpring", type=softGalleryLanguage_SpringComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SpringComponent", type=softGalleryLanguage_OrderSpring, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements121: BinaryAssociation = BinaryAssociation(
    name="elements121",
    ends={
        Property(name="softGalleryLanguage_EObject123", type=softGalleryLanguage_ResponseParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ResponseParameter122", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements124: BinaryAssociation = BinaryAssociation(
    name="elements124",
    ends={
        Property(name="softGalleryLanguage_ExceptionProcess", type=softGalleryLanguage_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ExceptionHandler", type=softGalleryLanguage_ExceptionProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type113: BinaryAssociation = BinaryAssociation(
    name="type113",
    ends={
        Property(name="softGalleryLanguage_MappingType", type=softGalleryLanguage_ResponseEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ResponseEntity", type=softGalleryLanguage_MappingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements114: BinaryAssociation = BinaryAssociation(
    name="elements114",
    ends={
        Property(name="softGalleryLanguage_ResponseParameter", type=softGalleryLanguage_ResponseEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ResponseEntity115", type=softGalleryLanguage_ResponseParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value116: BinaryAssociation = BinaryAssociation(
    name="value116",
    ends={
        Property(name="softGalleryLanguage_RequestMappingValue", type=softGalleryLanguage_RequestMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_RequestMapping", type=softGalleryLanguage_RequestMappingValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method117: BinaryAssociation = BinaryAssociation(
    name="method117",
    ends={
        Property(name="softGalleryLanguage_RequestMappingMethod", type=softGalleryLanguage_RequestMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_RequestMapping118", type=softGalleryLanguage_RequestMappingMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
produces119: BinaryAssociation = BinaryAssociation(
    name="produces119",
    ends={
        Property(name="softGalleryLanguage_RequestMappingProduces", type=softGalleryLanguage_RequestMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_RequestMapping120", type=softGalleryLanguage_RequestMappingProduces, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements132: BinaryAssociation = BinaryAssociation(
    name="elements132",
    ends={
        Property(name="softGalleryLanguage_EObject133", type=softGalleryLanguage_StorageActionMember, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_StorageActionMember", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reacts134: BinaryAssociation = BinaryAssociation(
    name="reacts134",
    ends={
        Property(name="softGalleryLanguage_ReactModules", type=softGalleryLanguage_React, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_React135", type=softGalleryLanguage_ReactModules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodules136: BinaryAssociation = BinaryAssociation(
    name="reactmodules136",
    ends={
        Property(name="softGalleryLanguage_ReactSubModules", type=softGalleryLanguage_ReactModules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactModules137", type=softGalleryLanguage_ReactSubModules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodulesconf138: BinaryAssociation = BinaryAssociation(
    name="reactmodulesconf138",
    ends={
        Property(name="softGalleryLanguage_ReactConfiguration", type=softGalleryLanguage_ReactSubModules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactSubModules139", type=softGalleryLanguage_ReactConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodulescomp140: BinaryAssociation = BinaryAssociation(
    name="reactmodulescomp140",
    ends={
        Property(name="softGalleryLanguage_ReactComponents", type=softGalleryLanguage_ReactSubModules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactSubModules141", type=softGalleryLanguage_ReactComponents, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodulesact142: BinaryAssociation = BinaryAssociation(
    name="reactmodulesact142",
    ends={
        Property(name="softGalleryLanguage_ReactActions", type=softGalleryLanguage_ReactSubModules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactSubModules143", type=softGalleryLanguage_ReactActions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
springEntityAnnotationTypes125: BinaryAssociation = BinaryAssociation(
    name="springEntityAnnotationTypes125",
    ends={
        Property(name="softGalleryLanguage_SpringEntityAnnotationTypes", type=softGalleryLanguage_SpringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SpringEntity", type=softGalleryLanguage_SpringEntityAnnotationTypes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements126: BinaryAssociation = BinaryAssociation(
    name="elements126",
    ends={
        Property(name="softGalleryLanguage_EObject127", type=softGalleryLanguage_StorageClient, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_StorageClient", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements128: BinaryAssociation = BinaryAssociation(
    name="elements128",
    ends={
        Property(name="softGalleryLanguage_EObject129", type=softGalleryLanguage_StorageMember, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_StorageMember", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements130: BinaryAssociation = BinaryAssociation(
    name="elements130",
    ends={
        Property(name="softGalleryLanguage_EObject131", type=softGalleryLanguage_StorageAction, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_StorageAction", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations161: BinaryAssociation = BinaryAssociation(
    name="configurations161",
    ends={
        Property(name="softGalleryLanguage_DOMConfigurations", type=softGalleryLanguage_ReactConfigurations, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactConfigurations162", type=softGalleryLanguage_DOMConfigurations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentslogic163: BinaryAssociation = BinaryAssociation(
    name="componentslogic163",
    ends={
        Property(name="softGalleryLanguage_ComponentsLogic", type=softGalleryLanguage_ReactComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactComponents164", type=softGalleryLanguage_ComponentsLogic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentsui165: BinaryAssociation = BinaryAssociation(
    name="componentsui165",
    ends={
        Property(name="softGalleryLanguage_ComponentsUI", type=softGalleryLanguage_ReactComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactComponents166", type=softGalleryLanguage_ComponentsUI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentstyle167: BinaryAssociation = BinaryAssociation(
    name="componentstyle167",
    ends={
        Property(name="softGalleryLanguage_ComponentsStyles", type=softGalleryLanguage_ReactComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactComponents168", type=softGalleryLanguage_ComponentsStyles, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logiccomponents169: BinaryAssociation = BinaryAssociation(
    name="logiccomponents169",
    ends={
        Property(name="softGalleryLanguage_LogicContent", type=softGalleryLanguage_ComponentsLogic, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentsLogic170", type=softGalleryLanguage_LogicContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmoduleslib144: BinaryAssociation = BinaryAssociation(
    name="reactmoduleslib144",
    ends={
        Property(name="softGalleryLanguage_ReactLibraries", type=softGalleryLanguage_ReactSubModules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactSubModules145", type=softGalleryLanguage_ReactLibraries, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodulesinf146: BinaryAssociation = BinaryAssociation(
    name="reactmodulesinf146",
    ends={
        Property(name="softGalleryLanguage_ReactInfo", type=softGalleryLanguage_ReactSubModules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactSubModules147", type=softGalleryLanguage_ReactInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies148: BinaryAssociation = BinaryAssociation(
    name="dependencies148",
    ends={
        Property(name="softGalleryLanguage_ReactDependencies", type=softGalleryLanguage_ReactConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactConfiguration149", type=softGalleryLanguage_ReactDependencies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations150: BinaryAssociation = BinaryAssociation(
    name="configurations150",
    ends={
        Property(name="softGalleryLanguage_ReactConfigurations", type=softGalleryLanguage_ReactConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactConfiguration151", type=softGalleryLanguage_ReactConfigurations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies152: BinaryAssociation = BinaryAssociation(
    name="dependencies152",
    ends={
        Property(name="softGalleryLanguage_ReactDependenciesRules", type=softGalleryLanguage_ReactDependencies, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactDependencies153", type=softGalleryLanguage_ReactDependenciesRules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies154: BinaryAssociation = BinaryAssociation(
    name="dependencies154",
    ends={
        Property(name="softGalleryLanguage_ReactDependenciesSubRules", type=softGalleryLanguage_ReactDependenciesRules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactDependenciesRules155", type=softGalleryLanguage_ReactDependenciesSubRules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies156: BinaryAssociation = BinaryAssociation(
    name="dependencies156",
    ends={
        Property(name="softGalleryLanguage_SingleDependencies", type=softGalleryLanguage_ReactDependenciesSubRules, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactDependenciesSubRules157", type=softGalleryLanguage_SingleDependencies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies158: BinaryAssociation = BinaryAssociation(
    name="dependencies158",
    ends={
        Property(name="softGalleryLanguage_EObject160", type=softGalleryLanguage_SingleDependencies, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SingleDependencies159", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uicontent184: BinaryAssociation = BinaryAssociation(
    name="uicontent184",
    ends={
        Property(name="softGalleryLanguage_ComponentClass186", type=softGalleryLanguage_SubcomponentCont, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_SubcomponentCont185", type=softGalleryLanguage_ComponentClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentclassimp187: BinaryAssociation = BinaryAssociation(
    name="componentclassimp187",
    ends={
        Property(name="softGalleryLanguage_ReactImports", type=softGalleryLanguage_ComponentClass, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentClass188", type=softGalleryLanguage_ReactImports, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentclassfunc189: BinaryAssociation = BinaryAssociation(
    name="componentclassfunc189",
    ends={
        Property(name="softGalleryLanguage_ReactFunctions", type=softGalleryLanguage_ComponentClass, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentClass190", type=softGalleryLanguage_ReactFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentclassprop191: BinaryAssociation = BinaryAssociation(
    name="componentclassprop191",
    ends={
        Property(name="softGalleryLanguage_Props", type=softGalleryLanguage_ComponentClass, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentClass192", type=softGalleryLanguage_Props, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactsimports193: BinaryAssociation = BinaryAssociation(
    name="reactsimports193",
    ends={
        Property(name="softGalleryLanguage_ReactImportContent", type=softGalleryLanguage_ReactImports, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactImports194", type=softGalleryLanguage_ReactImportContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactconstructors195: BinaryAssociation = BinaryAssociation(
    name="reactconstructors195",
    ends={
        Property(name="softGalleryLanguage_ReactConstructor", type=softGalleryLanguage_ReactFunctions, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactFunctions196", type=softGalleryLanguage_ReactConstructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactcorefuncs197: BinaryAssociation = BinaryAssociation(
    name="reactcorefuncs197",
    ends={
        Property(name="softGalleryLanguage_ReactCoreFunctions", type=softGalleryLanguage_ReactFunctions, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactFunctions198", type=softGalleryLanguage_ReactCoreFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logiccomponents171: BinaryAssociation = BinaryAssociation(
    name="logiccomponents171",
    ends={
        Property(name="softGalleryLanguage_LogicStructure", type=softGalleryLanguage_LogicContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_LogicContent172", type=softGalleryLanguage_LogicStructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logiccomponents173: BinaryAssociation = BinaryAssociation(
    name="logiccomponents173",
    ends={
        Property(name="softGalleryLanguage_ComponentClass", type=softGalleryLanguage_LogicStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_LogicStructure174", type=softGalleryLanguage_ComponentClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uicomponents175: BinaryAssociation = BinaryAssociation(
    name="uicomponents175",
    ends={
        Property(name="softGalleryLanguage_UIContent", type=softGalleryLanguage_ComponentsUI, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentsUI176", type=softGalleryLanguage_UIContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentcontent177: BinaryAssociation = BinaryAssociation(
    name="componentcontent177",
    ends={
        Property(name="softGalleryLanguage_ViewComponentCont", type=softGalleryLanguage_UIContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_UIContent178", type=softGalleryLanguage_ViewComponentCont, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subcomponentcontent179: BinaryAssociation = BinaryAssociation(
    name="subcomponentcontent179",
    ends={
        Property(name="softGalleryLanguage_SubcomponentCont", type=softGalleryLanguage_UIContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_UIContent180", type=softGalleryLanguage_SubcomponentCont, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uicontent181: BinaryAssociation = BinaryAssociation(
    name="uicontent181",
    ends={
        Property(name="softGalleryLanguage_ComponentClass183", type=softGalleryLanguage_ViewComponentCont, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ViewComponentCont182", type=softGalleryLanguage_ComponentClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stylescontents207: BinaryAssociation = BinaryAssociation(
    name="stylescontents207",
    ends={
        Property(name="softGalleryLanguage_ComponentsStylesContent", type=softGalleryLanguage_ComponentsStyles, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentsStyles208", type=softGalleryLanguage_ComponentsStylesContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stylecontent209: BinaryAssociation = BinaryAssociation(
    name="stylecontent209",
    ends={
        Property(name="softGalleryLanguage_StyleProperties", type=softGalleryLanguage_ComponentsStylesContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ComponentsStylesContent210", type=softGalleryLanguage_StyleProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stylespropscontents211: BinaryAssociation = BinaryAssociation(
    name="stylespropscontents211",
    ends={
        Property(name="softGalleryLanguage_StylePropertiesContent", type=softGalleryLanguage_StyleProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_StyleProperties212", type=softGalleryLanguage_StylePropertiesContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactactcontent213: BinaryAssociation = BinaryAssociation(
    name="reactactcontent213",
    ends={
        Property(name="softGalleryLanguage_ReactActionsContent", type=softGalleryLanguage_ReactActions, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactActions214", type=softGalleryLanguage_ReactActionsContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactrelcontent215: BinaryAssociation = BinaryAssociation(
    name="reactrelcontent215",
    ends={
        Property(name="softGalleryLanguage_ReactServicesRelation", type=softGalleryLanguage_ReactActionsContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactActionsContent216", type=softGalleryLanguage_ReactServicesRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactservcontent217: BinaryAssociation = BinaryAssociation(
    name="reactservcontent217",
    ends={
        Property(name="softGalleryLanguage_ReactServiceContent", type=softGalleryLanguage_ReactServicesType, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactServicesType", type=softGalleryLanguage_ReactServiceContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentstateclass199: BinaryAssociation = BinaryAssociation(
    name="componentstateclass199",
    ends={
        Property(name="softGalleryLanguage_State", type=softGalleryLanguage_ReactConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactConstructor200", type=softGalleryLanguage_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentfuncclass201: BinaryAssociation = BinaryAssociation(
    name="componentfuncclass201",
    ends={
        Property(name="softGalleryLanguage_CoreFunctionsDeclaration", type=softGalleryLanguage_ReactConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactConstructor202", type=softGalleryLanguage_CoreFunctionsDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statecontents203: BinaryAssociation = BinaryAssociation(
    name="statecontents203",
    ends={
        Property(name="softGalleryLanguage_StateContent", type=softGalleryLanguage_State, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_State204", type=softGalleryLanguage_StateContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propsconts205: BinaryAssociation = BinaryAssociation(
    name="propsconts205",
    ends={
        Property(name="softGalleryLanguage_PropsType", type=softGalleryLanguage_Props, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Props206", type=softGalleryLanguage_PropsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactinformation229: BinaryAssociation = BinaryAssociation(
    name="reactinformation229",
    ends={
        Property(name="softGalleryLanguage_ReactInformation", type=softGalleryLanguage_ReactInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactInfo230", type=softGalleryLanguage_ReactInformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements231: BinaryAssociation = BinaryAssociation(
    name="elements231",
    ends={
        Property(name="softGalleryLanguage_Cluster", type=softGalleryLanguage_PostgreSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_PostgreSQL232", type=softGalleryLanguage_Cluster, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements233: BinaryAssociation = BinaryAssociation(
    name="elements233",
    ends={
        Property(name="softGalleryLanguage_EObject235", type=softGalleryLanguage_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Cluster234", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements236: BinaryAssociation = BinaryAssociation(
    name="elements236",
    ends={
        Property(name="softGalleryLanguage_Schema", type=softGalleryLanguage_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Database", type=softGalleryLanguage_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements237: BinaryAssociation = BinaryAssociation(
    name="elements237",
    ends={
        Property(name="softGalleryLanguage_EObject239", type=softGalleryLanguage_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Schema238", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactservrequest218: BinaryAssociation = BinaryAssociation(
    name="reactservrequest218",
    ends={
        Property(name="softGalleryLanguage_ReactServiceContRequest", type=softGalleryLanguage_ReactServiceContent, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactServiceContent219", type=softGalleryLanguage_ReactServiceContRequest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactservrequestprops220: BinaryAssociation = BinaryAssociation(
    name="reactservrequestprops220",
    ends={
        Property(name="softGalleryLanguage_ReactServiceRequestProps", type=softGalleryLanguage_ReactServiceContRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactServiceContRequest221", type=softGalleryLanguage_ReactServiceRequestProps, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servicesrels222: BinaryAssociation = BinaryAssociation(
    name="servicesrels222",
    ends={
        Property(name="softGalleryLanguage_ReactsRelationServ", type=softGalleryLanguage_ReactServicesRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactServicesRelation223", type=softGalleryLanguage_ReactsRelationServ, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactrelationcontent224: BinaryAssociation = BinaryAssociation(
    name="reactrelationcontent224",
    ends={
        Property(name="softGalleryLanguage_ReactServicesType226", type=softGalleryLanguage_ReactsRelationServ, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactsRelationServ225", type=softGalleryLanguage_ReactServicesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactlibraries227: BinaryAssociation = BinaryAssociation(
    name="reactlibraries227",
    ends={
        Property(name="softGalleryLanguage_ReactLibrary", type=softGalleryLanguage_ReactLibraries, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ReactLibraries228", type=softGalleryLanguage_ReactLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements247: BinaryAssociation = BinaryAssociation(
    name="elements247",
    ends={
        Property(name="softGalleryLanguage_Policy", type=softGalleryLanguage_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Row", type=softGalleryLanguage_Policy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements248: BinaryAssociation = BinaryAssociation(
    name="elements248",
    ends={
        Property(name="softGalleryLanguage_EObject249", type=softGalleryLanguage_PostgresUser, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_PostgresUser", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements240: BinaryAssociation = BinaryAssociation(
    name="elements240",
    ends={
        Property(name="softGalleryLanguage_EObject241", type=softGalleryLanguage_Table_p, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Table_p", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements242: BinaryAssociation = BinaryAssociation(
    name="elements242",
    ends={
        Property(name="softGalleryLanguage_EObject243", type=softGalleryLanguage_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ForeignKey", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements244: BinaryAssociation = BinaryAssociation(
    name="elements244",
    ends={
        Property(name="softGalleryLanguage_RefTable_p", type=softGalleryLanguage_ForeignKeyRef, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ForeignKeyRef", type=softGalleryLanguage_RefTable_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements245: BinaryAssociation = BinaryAssociation(
    name="elements245",
    ends={
        Property(name="softGalleryLanguage_EObject246", type=softGalleryLanguage_ColumnP, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_ColumnP", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements258: BinaryAssociation = BinaryAssociation(
    name="elements258",
    ends={
        Property(name="softGalleryLanguage_BucketAccess", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="softGalleryLanguage_EObject259", type=softGalleryLanguage_BucketAccess, multiplicity=Multiplicity(1, 1))
    }
)
elements260: BinaryAssociation = BinaryAssociation(
    name="elements260",
    ends={
        Property(name="softGalleryLanguage_Metadata", type=softGalleryLanguage_AmazonFile, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_AmazonFile", type=softGalleryLanguage_Metadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements250: BinaryAssociation = BinaryAssociation(
    name="elements250",
    ends={
        Property(name="softGalleryLanguage_Clause", type=softGalleryLanguage_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Query", type=softGalleryLanguage_Clause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements251: BinaryAssociation = BinaryAssociation(
    name="elements251",
    ends={
        Property(name="softGalleryLanguage_EObject253", type=softGalleryLanguage_AmazonWebServices, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_AmazonWebServices252", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements254: BinaryAssociation = BinaryAssociation(
    name="elements254",
    ends={
        Property(name="softGalleryLanguage_EObject255", type=softGalleryLanguage_AmazonSimpleStorageService, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_AmazonSimpleStorageService", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements256: BinaryAssociation = BinaryAssociation(
    name="elements256",
    ends={
        Property(name="softGalleryLanguage_EObject257", type=softGalleryLanguage_Bucket, multiplicity=Multiplicity(1, 1)),
        Property(name="softGalleryLanguage_Bucket", type=softGalleryLanguage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_softGalleryLanguage_GetMapping_MappingType = Generalization(general=MappingType, specific=softGalleryLanguage_GetMapping)
gen_softGalleryLanguage_PutMapping_MappingType = Generalization(general=MappingType, specific=softGalleryLanguage_PutMapping)
gen_softGalleryLanguage_DeleteMapping_MappingType = Generalization(general=MappingType, specific=softGalleryLanguage_DeleteMapping)
gen_softGalleryLanguage_RequestMapping_MappingType = Generalization(general=MappingType, specific=softGalleryLanguage_RequestMapping)
gen_softGalleryLanguage_PostMapping_MappingType = Generalization(general=MappingType, specific=softGalleryLanguage_PostMapping)

# Domain Model
domain_model = DomainModel(
    name="softGalleryLanguage",
    types={softGalleryLanguage_Functionality, softGalleryLanguage_ExceptionsDomain, softGalleryLanguage_Entities, softGalleryLanguage_AtributePhoto, softGalleryLanguage_AtributeAlbum, softGalleryLanguage_Model, softGalleryLanguage_EObject, softGalleryLanguage_Domain, softGalleryLanguage_Entity, softGalleryLanguage_AlbumManagement, softGalleryLanguage_PhotoActions, softGalleryLanguage_LandingActions, softGalleryLanguage_ProfileManagementFunctions, softGalleryLanguage_AtributeUserDomain, softGalleryLanguage_Functionalities, softGalleryLanguage_ProfileManagement, softGalleryLanguage_AppAccess, softGalleryLanguage_PhotoActionsFunctions, softGalleryLanguage_LandingFunctions, softGalleryLanguage_ExceptionsType, softGalleryLanguage_AppAccessFunctions, softGalleryLanguage_AlbumManagementFunctions, softGalleryLanguage_Architecture, softGalleryLanguage_NTiers, softGalleryLanguage_Layer, softGalleryLanguage_PresentationLayer, softGalleryLanguage_PresentationContent, softGalleryLanguage_PresentationSegments, softGalleryLanguage_BusinessLogicLayer, softGalleryLanguage_PhotoException, softGalleryLanguage_AlbumException, softGalleryLanguage_UserException, softGalleryLanguage_SegmentStructure, softGalleryLanguage_SegmentStructureContent, softGalleryLanguage_DirectoryContent, softGalleryLanguage_Directories, softGalleryLanguage_MultipleFile, softGalleryLanguage_SingleFile, softGalleryLanguage_LayerRelations, softGalleryLanguage_BusinessLogicContent, softGalleryLanguage_BusinessLogicSegments, softGalleryLanguage_ControllerSegmentElement, softGalleryLanguage_SpecificationSegmentElement, softGalleryLanguage_CriteriaAttributeType, softGalleryLanguage_DataPersistenceLayer, softGalleryLanguage_DataPersistenceContent, softGalleryLanguage_DataPersistenceSegments, softGalleryLanguage_NTierSource, softGalleryLanguage_NTierTarget, softGalleryLanguage_NTiersRelations, softGalleryLanguage_Technology, softGalleryLanguage_Technologies, softGalleryLanguage_Spring, softGalleryLanguage_React, softGalleryLanguage_LayerSource, softGalleryLanguage_LayerTarget, softGalleryLanguage_ArchitectureComponents, softGalleryLanguage_FrontEnd, softGalleryLanguage_BackEnd, softGalleryLanguage_PersistenceDataComponent, softGalleryLanguage_NTiersConnections, softGalleryLanguage_NTierConnectionContent, softGalleryLanguage_SpringRepository, softGalleryLanguage_SpringRepositories, softGalleryLanguage_SpringRepositoryAnnotation, softGalleryLanguage_RestController, softGalleryLanguage_Specification, softGalleryLanguage_Predicate, softGalleryLanguage_SearchCriteria, softGalleryLanguage_PostgreSQL, softGalleryLanguage_AmazonWebServices, softGalleryLanguage_SpringBootApplication, softGalleryLanguage_Configuration, softGalleryLanguage_EnableGlobalMethodSecurity, softGalleryLanguage_EnableAuthorizationServer, softGalleryLanguage_EnableResourceServer, softGalleryLanguage_EnableWebSecurity, softGalleryLanguage_SpringComponent, softGalleryLanguage_OrderSpring, softGalleryLanguage_GetMapping, softGalleryLanguage_PutMapping, softGalleryLanguage_DeleteMapping, softGalleryLanguage_ResponseParameterAnnotation, softGalleryLanguage_ResponseParameterType, softGalleryLanguage_ResponseParameterName, softGalleryLanguage_ExceptionHandler, softGalleryLanguage_ExceptionProcess, softGalleryLanguage_Autowired, softGalleryLanguage_ResponseEntity, softGalleryLanguage_MappingType, softGalleryLanguage_ResponseParameter, softGalleryLanguage_RequestMapping, MappingType, softGalleryLanguage_RequestMappingValue, softGalleryLanguage_RequestMappingMethod, softGalleryLanguage_RequestMappingProduces, softGalleryLanguage_PostMapping, softGalleryLanguage_StorageActionMember, softGalleryLanguage_StorageActionMemberType, softGalleryLanguage_StorageActionMemberName, softGalleryLanguage_ReactModules, softGalleryLanguage_ReactSubModules, softGalleryLanguage_ReactConfiguration, softGalleryLanguage_ReactComponents, softGalleryLanguage_ReactActions, softGalleryLanguage_SpringEntity, softGalleryLanguage_SpringEntityAnnotationTypes, softGalleryLanguage_StorageClient, softGalleryLanguage_StorageMember, softGalleryLanguage_StorageMemberType, softGalleryLanguage_StorageMemberAnnotation, softGalleryLanguage_StorageAction, softGalleryLanguage_StorageActionAnnotation, softGalleryLanguage_StorageActionReturn, softGalleryLanguage_PackageVersion, softGalleryLanguage_DOMConfigurations, softGalleryLanguage_ComponentsLogic, softGalleryLanguage_ComponentsUI, softGalleryLanguage_ComponentsStyles, softGalleryLanguage_LogicContent, softGalleryLanguage_ReactLibraries, softGalleryLanguage_ReactInfo, softGalleryLanguage_ReactDependencies, softGalleryLanguage_ReactConfigurations, softGalleryLanguage_ReactDependenciesRules, softGalleryLanguage_ReactDependenciesSubRules, softGalleryLanguage_SingleDependencies, softGalleryLanguage_PackageName, softGalleryLanguage_ReactImports, softGalleryLanguage_ReactFunctions, softGalleryLanguage_Props, softGalleryLanguage_ReactImportContent, softGalleryLanguage_ReactConstructor, softGalleryLanguage_ReactCoreFunctions, softGalleryLanguage_LogicStructure, softGalleryLanguage_ComponentClass, softGalleryLanguage_UIContent, softGalleryLanguage_ViewComponentCont, softGalleryLanguage_SubcomponentCont, softGalleryLanguage_ComponentsStylesContent, softGalleryLanguage_StyleProperties, softGalleryLanguage_StylePropertiesContent, softGalleryLanguage_ReactActionsContent, softGalleryLanguage_ReactServicesRelation, softGalleryLanguage_ReactServicesType, softGalleryLanguage_ReactServiceContent, softGalleryLanguage_State, softGalleryLanguage_CoreFunctionsDeclaration, softGalleryLanguage_StateContent, softGalleryLanguage_PropsType, softGalleryLanguage_ReactInformation, softGalleryLanguage_Cluster, softGalleryLanguage_Database, softGalleryLanguage_Schema, softGalleryLanguage_ReactServiceContRequest, softGalleryLanguage_ReactServiceRequestProps, softGalleryLanguage_ReactsRelationServ, softGalleryLanguage_ReactLibrary, softGalleryLanguage_DatatypeDB, softGalleryLanguage_Constraint, softGalleryLanguage_Row, softGalleryLanguage_Policy, softGalleryLanguage_Trigger, softGalleryLanguage_Function, softGalleryLanguage_PostgresUser, softGalleryLanguage_Index_p, softGalleryLanguage_ViewSchema, softGalleryLanguage_Table_p, softGalleryLanguage_ForeignKey, softGalleryLanguage_ForeignKey_n, softGalleryLanguage_ForeignKeyRef, softGalleryLanguage_RefTable_p, softGalleryLanguage_ColumnP, softGalleryLanguage_PublicAccess, softGalleryLanguage_ObjectsPublic, softGalleryLanguage_BucketObjectsNotPublic, softGalleryLanguage_OnlyAuthorized, softGalleryLanguage_AmazonFolder, softGalleryLanguage_AmazonFile, softGalleryLanguage_Metadata, softGalleryLanguage_AmazonElasticComputeCloud, softGalleryLanguage_Privilege, softGalleryLanguage_Query, softGalleryLanguage_Clause, softGalleryLanguage_AmazonSimpleStorageService, softGalleryLanguage_BatchOperation, softGalleryLanguage_Bucket, softGalleryLanguage_BucketAccess},
    associations={entityfuncs2, exceptionsdomain4, elements6, atributePhoto8, atributeAlbum10, elements0, entitydomain1, elements18, items20, resources22, aditionals24, items26, atributeUserDomain12, elements14, functions16, items32, items34, items28, items30, elements44, elements46, layer48, presentationLayer50, elements52, businessLogicLayer53, exceptionsType36, photoException38, albumException40, userException42, elements65, elements66, directories68, elements71, businessLogicSegments55, controllerSegmentElement56, specificationSegmentElement58, criteriaAttributeType60, elements62, elements63, ntierorigin81, ntiertarget83, ntierconnection85, ntierconnection87, elements90, techspring91, techreact93, layerorigin72, layertarget73, archFeComponent75, archBeComponent76, archPdComponent78, ntierconnections80, elements107, elements109, elements111, techpostgresql95, techamazon97, elements99, elements101, elements104, elements106, elements121, elements124, type113, elements114, value116, method117, produces119, elements132, reacts134, reactmodules136, reactmodulesconf138, reactmodulescomp140, reactmodulesact142, springEntityAnnotationTypes125, elements126, elements128, elements130, configurations161, componentslogic163, componentsui165, componentstyle167, logiccomponents169, reactmoduleslib144, reactmodulesinf146, dependencies148, configurations150, dependencies152, dependencies154, dependencies156, dependencies158, uicontent184, componentclassimp187, componentclassfunc189, componentclassprop191, reactsimports193, reactconstructors195, reactcorefuncs197, logiccomponents171, logiccomponents173, uicomponents175, componentcontent177, subcomponentcontent179, uicontent181, stylescontents207, stylecontent209, stylespropscontents211, reactactcontent213, reactrelcontent215, reactservcontent217, componentstateclass199, componentfuncclass201, statecontents203, propsconts205, reactinformation229, elements231, elements233, elements236, elements237, reactservrequest218, reactservrequestprops220, servicesrels222, reactrelationcontent224, reactlibraries227, elements247, elements248, elements240, elements242, elements244, elements245, elements258, elements260, elements250, elements251, elements254, elements256},
    generalizations={gen_softGalleryLanguage_GetMapping_MappingType, gen_softGalleryLanguage_PutMapping_MappingType, gen_softGalleryLanguage_DeleteMapping_MappingType, gen_softGalleryLanguage_RequestMapping_MappingType, gen_softGalleryLanguage_PostMapping_MappingType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)