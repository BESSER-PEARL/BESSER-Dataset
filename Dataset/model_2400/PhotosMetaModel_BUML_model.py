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
PhotosMetaModel_Functionalities = Class(name="PhotosMetaModel::Functionalities")
PhotosMetaModel_Entities = Class(name="PhotosMetaModel::Entities")
PhotosMetaModel_SoftGallery = Class(name="PhotosMetaModel::SoftGallery")
PhotosMetaModel_Domain = Class(name="PhotosMetaModel::Domain")
PhotosMetaModel_Architecture = Class(name="PhotosMetaModel::Architecture")
PhotosMetaModel_Technology = Class(name="PhotosMetaModel::Technology")
PhotosMetaModel_Entity = Class(name="PhotosMetaModel::Entity")
PhotosMetaModel_NTier = Class(name="PhotosMetaModel::NTier")
PhotosMetaModel_Spring = Class(name="PhotosMetaModel::Spring")
PhotosMetaModel_PostgreSQL = Class(name="PhotosMetaModel::PostgreSQL")
PhotosMetaModel_React = Class(name="PhotosMetaModel::React")
PhotosMetaModel_AmazonWebServices = Class(name="PhotosMetaModel::AmazonWebServices")
PhotosMetaModel_SpringBootApplication = Class(name="PhotosMetaModel::SpringBootApplication")
PhotosMetaModel_Modules = Class(name="PhotosMetaModel::Modules")
PhotosMetaModel_Repository = Class(name="PhotosMetaModel::Repository")
PhotosMetaModel_RestController = Class(name="PhotosMetaModel::RestController")
PhotosMetaModel_RequestMapping = Class(name="PhotosMetaModel::RequestMapping")
PhotosMetaModel_ExceptionHandler = Class(name="PhotosMetaModel::ExceptionHandler")
PhotosMetaModel_Autowired = Class(name="PhotosMetaModel::Autowired")
PhotosMetaModel_Specification = Class(name="PhotosMetaModel::Specification")
PhotosMetaModel_GetMapping = Class(name="PhotosMetaModel::GetMapping")
PhotosMetaModel_PutMapping = Class(name="PhotosMetaModel::PutMapping")
PhotosMetaModel_Component = Class(name="PhotosMetaModel::Component")
PhotosMetaModel_Configuration = Class(name="PhotosMetaModel::Configuration")
PhotosMetaModel_RequestPart = Class(name="PhotosMetaModel::RequestPart")
PhotosMetaModel_PostMapping = Class(name="PhotosMetaModel::PostMapping")
RequestMapping = Class(name="RequestMapping")
PhotosMetaModel_GeneratedValue = Class(name="PhotosMetaModel::GeneratedValue")
PhotosMetaModel_Exception = Class(name="PhotosMetaModel::Exception")
PhotosMetaModel_DeleteMapping = Class(name="PhotosMetaModel::DeleteMapping")
PhotosMetaModel_Table_s = Class(name="PhotosMetaModel::Table::s")
PhotosMetaModel_NamedNativeQuery = Class(name="PhotosMetaModel::NamedNativeQuery")
PhotosMetaModel_Column_s = Class(name="PhotosMetaModel::Column::s")
PhotosMetaModel_Id = Class(name="PhotosMetaModel::Id")
PhotosMetaModel_EnableWebSecurity = Class(name="PhotosMetaModel::EnableWebSecurity")
PhotosMetaModel_EnableResourceServer = Class(name="PhotosMetaModel::EnableResourceServer")
PhotosMetaModel_Column_p = Class(name="PhotosMetaModel::Column::p")
PhotosMetaModel_Constraint = Class(name="PhotosMetaModel::Constraint")
PhotosMetaModel_DataType = Class(name="PhotosMetaModel::DataType")
PhotosMetaModel_SearchCriteria = Class(name="PhotosMetaModel::SearchCriteria")
PhotosMetaModel_Predicate = Class(name="PhotosMetaModel::Predicate")
PhotosMetaModel_Bean = Class(name="PhotosMetaModel::Bean")
PhotosMetaModel_ForeignKey = Class(name="PhotosMetaModel::ForeignKey")
PhotosMetaModel_EnableAuthorizationServer = Class(name="PhotosMetaModel::EnableAuthorizationServer")
PhotosMetaModel_EnableGlobalMethodSecurity = Class(name="PhotosMetaModel::EnableGlobalMethodSecurity")
PhotosMetaModel_Order_s = Class(name="PhotosMetaModel::Order::s")
PhotosMetaModel_Cluster = Class(name="PhotosMetaModel::Cluster")
PhotosMetaModel_Query = Class(name="PhotosMetaModel::Query")
PhotosMetaModel_Clause = Class(name="PhotosMetaModel::Clause")
PhotosMetaModel_Function_p = Class(name="PhotosMetaModel::Function::p")
PhotosMetaModel_Database = Class(name="PhotosMetaModel::Database")
PhotosMetaModel_Table_p = Class(name="PhotosMetaModel::Table::p")
PhotosMetaModel_Trigger = Class(name="PhotosMetaModel::Trigger")
PhotosMetaModel_View = Class(name="PhotosMetaModel::View")
PhotosMetaModel_Index_p = Class(name="PhotosMetaModel::Index::p")
PhotosMetaModel_Row = Class(name="PhotosMetaModel::Row")
PhotosMetaModel_User_p = Class(name="PhotosMetaModel::User::p")
PhotosMetaModel_Scheme = Class(name="PhotosMetaModel::Scheme")
PhotosMetaModel_Privilege = Class(name="PhotosMetaModel::Privilege")
PhotosMetaModel_Policy = Class(name="PhotosMetaModel::Policy")
PhotosMetaModel_Column = Class(name="PhotosMetaModel::Column")
PhotosMetaModel_AlbumManagement = Class(name="PhotosMetaModel::AlbumManagement")
PhotosMetaModel_PhotoActions = Class(name="PhotosMetaModel::PhotoActions")
PhotosMetaModel_Index = Class(name="PhotosMetaModel::Index")
PhotosMetaModel_User_d = Class(name="PhotosMetaModel::User::d")
Entities = Class(name="Entities")
PhotosMetaModel_AppAccess = Class(name="PhotosMetaModel::AppAccess")
Functionalities = Class(name="Functionalities")
PhotosMetaModel_ProfileManagement = Class(name="PhotosMetaModel::ProfileManagement")
PhotosMetaModel_Layer = Class(name="PhotosMetaModel::Layer")
PhotosMetaModel_Photo = Class(name="PhotosMetaModel::Photo")
PhotosMetaModel_Album = Class(name="PhotosMetaModel::Album")
PhotosMetaModel_AmazonSimpleStorageService = Class(name="PhotosMetaModel::AmazonSimpleStorageService")
PhotosMetaModel_AmazonElasticComputeCloud = Class(name="PhotosMetaModel::AmazonElasticComputeCloud")
PhotosMetaModel_Connection = Class(name="PhotosMetaModel::Connection")
PhotosMetaModel_AmazonS3API = Class(name="PhotosMetaModel::AmazonS3API")
PhotosMetaModel_Relation = Class(name="PhotosMetaModel::Relation")
PhotosMetaModel_REST = Class(name="PhotosMetaModel::REST")
Connection = Class(name="Connection")
PhotosMetaModel_PostgreSQLConnection = Class(name="PhotosMetaModel::PostgreSQLConnection")
PhotosMetaModel_AllowedToUse = Class(name="PhotosMetaModel::AllowedToUse")
Relation = Class(name="Relation")
PhotosMetaModel_SegmentStructure = Class(name="PhotosMetaModel::SegmentStructure")
PhotosMetaModel_Presentation = Class(name="PhotosMetaModel::Presentation")
Layer = Class(name="Layer")
PhotosMetaModel_PresentationSegment = Class(name="PhotosMetaModel::PresentationSegment")
PhotosMetaModel_BusinessLogic = Class(name="PhotosMetaModel::BusinessLogic")
PhotosMetaModel_BusinessLogicSegment = Class(name="PhotosMetaModel::BusinessLogicSegment")
PhotosMetaModel_Data = Class(name="PhotosMetaModel::Data")
PhotosMetaModel_DataSegment = Class(name="PhotosMetaModel::DataSegment")
PhotosMetaModel_AmazonS3Storage = Class(name="PhotosMetaModel::AmazonS3Storage")
PhotosMetaModel_Components = Class(name="PhotosMetaModel::Components")
Modules = Class(name="Modules")
PhotosMetaModel_ReactClasses = Class(name="PhotosMetaModel::ReactClasses")
PhotosMetaModel_View_a = Class(name="PhotosMetaModel::View::a")
PresentationSegment = Class(name="PresentationSegment")
PhotosMetaModel_Component_a = Class(name="PhotosMetaModel::Component::a")
PhotosMetaModel_Action_a = Class(name="PhotosMetaModel::Action::a")
PhotosMetaModel_Controller_a = Class(name="PhotosMetaModel::Controller::a")
BusinessLogicSegment = Class(name="BusinessLogicSegment")
PhotosMetaModel_Model_a = Class(name="PhotosMetaModel::Model::a")
PhotosMetaModel_Repository_a = Class(name="PhotosMetaModel::Repository::a")
PhotosMetaModel_Security_a = Class(name="PhotosMetaModel::Security::a")
PhotosMetaModel_PostgreSQL_a = Class(name="PhotosMetaModel::PostgreSQL::a")
DataSegment = Class(name="DataSegment")
PhotosMetaModel_Access = Class(name="PhotosMetaModel::Access")
PhotosMetaModel_File_a = Class(name="PhotosMetaModel::File::a")
PhotosMetaModel_ReactFunctions = Class(name="PhotosMetaModel::ReactFunctions")
PhotosMetaModel_Render = Class(name="PhotosMetaModel::Render")
ReactFunctions = Class(name="ReactFunctions")
PhotosMetaModel_Constructor = Class(name="PhotosMetaModel::Constructor")
PhotosMetaModel_LifeCycle = Class(name="PhotosMetaModel::LifeCycle")
PhotosMetaModel_Bucket = Class(name="PhotosMetaModel::Bucket")
PhotosMetaModel_BatchOperation = Class(name="PhotosMetaModel::BatchOperation")
PhotosMetaModel_MetaData = Class(name="PhotosMetaModel::MetaData")
PhotosMetaModel_Folder_a = Class(name="PhotosMetaModel::Folder::a")
PhotosMetaModel_Public = Class(name="PhotosMetaModel::Public")
Access = Class(name="Access")
PhotosMetaModel_ObjectsPublic = Class(name="PhotosMetaModel::ObjectsPublic")
PhotosMetaModel_BucketObjectsNotPublic = Class(name="PhotosMetaModel::BucketObjectsNotPublic")
PhotosMetaModel_OnlyAuthorized = Class(name="PhotosMetaModel::OnlyAuthorized")
PhotosMetaModel_UI = Class(name="PhotosMetaModel::UI")
PhotosMetaModel_Props = Class(name="PhotosMetaModel::Props")
PhotosMetaModel_ReactConfiguration = Class(name="PhotosMetaModel::ReactConfiguration")
PhotosMetaModel_ReactDOM = Class(name="PhotosMetaModel::ReactDOM")
ReactConfiguration = Class(name="ReactConfiguration")
PhotosMetaModel_Dependencies = Class(name="PhotosMetaModel::Dependencies")
PhotosMetaModel_Logic = Class(name="PhotosMetaModel::Logic")
Components = Class(name="Components")
UI = Class(name="UI")
PhotosMetaModel_Subcomponents = Class(name="PhotosMetaModel::Subcomponents")
PhotosMetaModel_Actions = Class(name="PhotosMetaModel::Actions")
PhotosMetaModel_Request = Class(name="PhotosMetaModel::Request")
Actions = Class(name="Actions")
PhotosMetaModel_Services = Class(name="PhotosMetaModel::Services")
PhotosMetaModel_State = Class(name="PhotosMetaModel::State")
PhotosMetaModel_CoreFunctions = Class(name="PhotosMetaModel::CoreFunctions")
PhotosMetaModel_Router = Class(name="PhotosMetaModel::Router")
Logic = Class(name="Logic")
PhotosMetaModel_Structure = Class(name="PhotosMetaModel::Structure")
PhotosMetaModel_ViewComponents = Class(name="PhotosMetaModel::ViewComponents")
PhotosMetaModel_Directories = Class(name="PhotosMetaModel::Directories")
PhotosMetaModel_Files = Class(name="PhotosMetaModel::Files")
PhotosMetaModel_Libraries = Class(name="PhotosMetaModel::Libraries")
PhotosMetaModel_Information = Class(name="PhotosMetaModel::Information")

# PhotosMetaModel_Functionalities class attributes and methods

# PhotosMetaModel_Entities class attributes and methods
PhotosMetaModel_Entities_id: Property = Property(name="id", type=StringType)
PhotosMetaModel_Entities.attributes={PhotosMetaModel_Entities_id}

# PhotosMetaModel_SoftGallery class attributes and methods

# PhotosMetaModel_Domain class attributes and methods

# PhotosMetaModel_Architecture class attributes and methods

# PhotosMetaModel_Technology class attributes and methods

# PhotosMetaModel_Entity class attributes and methods

# PhotosMetaModel_NTier class attributes and methods

# PhotosMetaModel_Spring class attributes and methods

# PhotosMetaModel_PostgreSQL class attributes and methods

# PhotosMetaModel_React class attributes and methods

# PhotosMetaModel_AmazonWebServices class attributes and methods

# PhotosMetaModel_SpringBootApplication class attributes and methods

# PhotosMetaModel_Modules class attributes and methods
PhotosMetaModel_Modules_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Modules.attributes={PhotosMetaModel_Modules_name}

# PhotosMetaModel_Repository class attributes and methods

# PhotosMetaModel_RestController class attributes and methods
PhotosMetaModel_RestController_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_RestController.attributes={PhotosMetaModel_RestController_name}

# PhotosMetaModel_RequestMapping class attributes and methods

# PhotosMetaModel_ExceptionHandler class attributes and methods

# PhotosMetaModel_Autowired class attributes and methods

# PhotosMetaModel_Specification class attributes and methods

# PhotosMetaModel_GetMapping class attributes and methods

# PhotosMetaModel_PutMapping class attributes and methods

# PhotosMetaModel_Component class attributes and methods

# PhotosMetaModel_Configuration class attributes and methods

# PhotosMetaModel_RequestPart class attributes and methods

# PhotosMetaModel_PostMapping class attributes and methods

# RequestMapping class attributes and methods

# PhotosMetaModel_GeneratedValue class attributes and methods

# PhotosMetaModel_Exception class attributes and methods

# PhotosMetaModel_DeleteMapping class attributes and methods

# PhotosMetaModel_Table_s class attributes and methods
PhotosMetaModel_Table_s_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Table_s.attributes={PhotosMetaModel_Table_s_name}

# PhotosMetaModel_NamedNativeQuery class attributes and methods

# PhotosMetaModel_Column_s class attributes and methods
PhotosMetaModel_Column_s_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Column_s.attributes={PhotosMetaModel_Column_s_name}

# PhotosMetaModel_Id class attributes and methods

# PhotosMetaModel_EnableWebSecurity class attributes and methods

# PhotosMetaModel_EnableResourceServer class attributes and methods

# PhotosMetaModel_Column_p class attributes and methods
PhotosMetaModel_Column_p_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Column_p.attributes={PhotosMetaModel_Column_p_name}

# PhotosMetaModel_Constraint class attributes and methods

# PhotosMetaModel_DataType class attributes and methods
PhotosMetaModel_DataType_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_DataType.attributes={PhotosMetaModel_DataType_name}

# PhotosMetaModel_SearchCriteria class attributes and methods

# PhotosMetaModel_Predicate class attributes and methods

# PhotosMetaModel_Bean class attributes and methods

# PhotosMetaModel_ForeignKey class attributes and methods

# PhotosMetaModel_EnableAuthorizationServer class attributes and methods

# PhotosMetaModel_EnableGlobalMethodSecurity class attributes and methods

# PhotosMetaModel_Order_s class attributes and methods

# PhotosMetaModel_Cluster class attributes and methods

# PhotosMetaModel_Query class attributes and methods

# PhotosMetaModel_Clause class attributes and methods

# PhotosMetaModel_Function_p class attributes and methods

# PhotosMetaModel_Database class attributes and methods
PhotosMetaModel_Database_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Database.attributes={PhotosMetaModel_Database_name}

# PhotosMetaModel_Table_p class attributes and methods
PhotosMetaModel_Table_p_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Table_p.attributes={PhotosMetaModel_Table_p_name}

# PhotosMetaModel_Trigger class attributes and methods

# PhotosMetaModel_View class attributes and methods

# PhotosMetaModel_Index_p class attributes and methods

# PhotosMetaModel_Row class attributes and methods
PhotosMetaModel_Row_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Row.attributes={PhotosMetaModel_Row_name}

# PhotosMetaModel_User_p class attributes and methods
PhotosMetaModel_User_p_username: Property = Property(name="username", type=StringType)
PhotosMetaModel_User_p_password: Property = Property(name="password", type=StringType)
PhotosMetaModel_User_p.attributes={PhotosMetaModel_User_p_username, PhotosMetaModel_User_p_password}

# PhotosMetaModel_Scheme class attributes and methods
PhotosMetaModel_Scheme_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Scheme.attributes={PhotosMetaModel_Scheme_name}

# PhotosMetaModel_Privilege class attributes and methods

# PhotosMetaModel_Policy class attributes and methods

# PhotosMetaModel_Column class attributes and methods

# PhotosMetaModel_AlbumManagement class attributes and methods

# PhotosMetaModel_PhotoActions class attributes and methods

# PhotosMetaModel_Index class attributes and methods

# PhotosMetaModel_User_d class attributes and methods
PhotosMetaModel_User_d_first_name: Property = Property(name="first_name", type=StringType)
PhotosMetaModel_User_d_last_name: Property = Property(name="last_name", type=StringType)
PhotosMetaModel_User_d_profile_description: Property = Property(name="profile_description", type=StringType)
PhotosMetaModel_User_d_username: Property = Property(name="username", type=StringType)
PhotosMetaModel_User_d_password: Property = Property(name="password", type=StringType)
PhotosMetaModel_User_d_email: Property = Property(name="email", type=StringType)
PhotosMetaModel_User_d.attributes={PhotosMetaModel_User_d_password, PhotosMetaModel_User_d_last_name, PhotosMetaModel_User_d_first_name, PhotosMetaModel_User_d_profile_description, PhotosMetaModel_User_d_email, PhotosMetaModel_User_d_username}

# Entities class attributes and methods

# PhotosMetaModel_AppAccess class attributes and methods

# Functionalities class attributes and methods

# PhotosMetaModel_ProfileManagement class attributes and methods

# PhotosMetaModel_Layer class attributes and methods

# PhotosMetaModel_Photo class attributes and methods
PhotosMetaModel_Photo_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Photo.attributes={PhotosMetaModel_Photo_name}

# PhotosMetaModel_Album class attributes and methods
PhotosMetaModel_Album_url: Property = Property(name="url", type=StringType)
PhotosMetaModel_Album_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Album.attributes={PhotosMetaModel_Album_url, PhotosMetaModel_Album_name}

# PhotosMetaModel_AmazonSimpleStorageService class attributes and methods

# PhotosMetaModel_AmazonElasticComputeCloud class attributes and methods

# PhotosMetaModel_Connection class attributes and methods

# PhotosMetaModel_AmazonS3API class attributes and methods
PhotosMetaModel_AmazonS3API_endpointUrl: Property = Property(name="endpointUrl", type=StringType)
PhotosMetaModel_AmazonS3API_accessKey: Property = Property(name="accessKey", type=StringType)
PhotosMetaModel_AmazonS3API_secretKey: Property = Property(name="secretKey", type=StringType)
PhotosMetaModel_AmazonS3API_bucketName: Property = Property(name="bucketName", type=StringType)
PhotosMetaModel_AmazonS3API.attributes={PhotosMetaModel_AmazonS3API_bucketName, PhotosMetaModel_AmazonS3API_accessKey, PhotosMetaModel_AmazonS3API_endpointUrl, PhotosMetaModel_AmazonS3API_secretKey}

# PhotosMetaModel_Relation class attributes and methods

# PhotosMetaModel_REST class attributes and methods

# Connection class attributes and methods

# PhotosMetaModel_PostgreSQLConnection class attributes and methods
PhotosMetaModel_PostgreSQLConnection_port: Property = Property(name="port", type=IntegerType)
PhotosMetaModel_PostgreSQLConnection_username: Property = Property(name="username", type=StringType)
PhotosMetaModel_PostgreSQLConnection_password: Property = Property(name="password", type=StringType)
PhotosMetaModel_PostgreSQLConnection_url: Property = Property(name="url", type=StringType)
PhotosMetaModel_PostgreSQLConnection.attributes={PhotosMetaModel_PostgreSQLConnection_port, PhotosMetaModel_PostgreSQLConnection_url, PhotosMetaModel_PostgreSQLConnection_username, PhotosMetaModel_PostgreSQLConnection_password}

# PhotosMetaModel_AllowedToUse class attributes and methods

# Relation class attributes and methods

# PhotosMetaModel_SegmentStructure class attributes and methods
PhotosMetaModel_SegmentStructure_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_SegmentStructure.attributes={PhotosMetaModel_SegmentStructure_name}

# PhotosMetaModel_Presentation class attributes and methods

# Layer class attributes and methods

# PhotosMetaModel_PresentationSegment class attributes and methods

# PhotosMetaModel_BusinessLogic class attributes and methods

# PhotosMetaModel_BusinessLogicSegment class attributes and methods

# PhotosMetaModel_Data class attributes and methods

# PhotosMetaModel_DataSegment class attributes and methods

# PhotosMetaModel_AmazonS3Storage class attributes and methods

# PhotosMetaModel_Components class attributes and methods

# Modules class attributes and methods

# PhotosMetaModel_ReactClasses class attributes and methods

# PhotosMetaModel_View_a class attributes and methods

# PresentationSegment class attributes and methods

# PhotosMetaModel_Component_a class attributes and methods

# PhotosMetaModel_Action_a class attributes and methods

# PhotosMetaModel_Controller_a class attributes and methods

# BusinessLogicSegment class attributes and methods

# PhotosMetaModel_Model_a class attributes and methods

# PhotosMetaModel_Repository_a class attributes and methods

# PhotosMetaModel_Security_a class attributes and methods

# PhotosMetaModel_PostgreSQL_a class attributes and methods

# DataSegment class attributes and methods

# PhotosMetaModel_Access class attributes and methods

# PhotosMetaModel_File_a class attributes and methods
PhotosMetaModel_File_a_Onwer: Property = Property(name="Onwer", type=StringType)
PhotosMetaModel_File_a_size: Property = Property(name="size", type=StringType)
PhotosMetaModel_File_a_ObjectURL: Property = Property(name="ObjectURL", type=StringType)
PhotosMetaModel_File_a.attributes={PhotosMetaModel_File_a_Onwer, PhotosMetaModel_File_a_size, PhotosMetaModel_File_a_ObjectURL}

# PhotosMetaModel_ReactFunctions class attributes and methods
PhotosMetaModel_ReactFunctions_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_ReactFunctions.attributes={PhotosMetaModel_ReactFunctions_name}

# PhotosMetaModel_Render class attributes and methods

# ReactFunctions class attributes and methods

# PhotosMetaModel_Constructor class attributes and methods

# PhotosMetaModel_LifeCycle class attributes and methods

# PhotosMetaModel_Bucket class attributes and methods
PhotosMetaModel_Bucket_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Bucket.attributes={PhotosMetaModel_Bucket_name}

# PhotosMetaModel_BatchOperation class attributes and methods

# PhotosMetaModel_MetaData class attributes and methods

# PhotosMetaModel_Folder_a class attributes and methods
PhotosMetaModel_Folder_a_name: Property = Property(name="name", type=StringType)
PhotosMetaModel_Folder_a.attributes={PhotosMetaModel_Folder_a_name}

# PhotosMetaModel_Public class attributes and methods

# Access class attributes and methods

# PhotosMetaModel_ObjectsPublic class attributes and methods

# PhotosMetaModel_BucketObjectsNotPublic class attributes and methods

# PhotosMetaModel_OnlyAuthorized class attributes and methods

# PhotosMetaModel_UI class attributes and methods

# PhotosMetaModel_Props class attributes and methods
PhotosMetaModel_Props_type: Property = Property(name="type", type=StringType)
PhotosMetaModel_Props_dataType: Property = Property(name="dataType", type=StringType)
PhotosMetaModel_Props.attributes={PhotosMetaModel_Props_type, PhotosMetaModel_Props_dataType}

# PhotosMetaModel_ReactConfiguration class attributes and methods

# PhotosMetaModel_ReactDOM class attributes and methods
PhotosMetaModel_ReactDOM_isRoute: Property = Property(name="isRoute", type=StringType)
PhotosMetaModel_ReactDOM_isConstant: Property = Property(name="isConstant", type=StringType)
PhotosMetaModel_ReactDOM_isStruct: Property = Property(name="isStruct", type=StringType)
PhotosMetaModel_ReactDOM.attributes={PhotosMetaModel_ReactDOM_isRoute, PhotosMetaModel_ReactDOM_isStruct, PhotosMetaModel_ReactDOM_isConstant}

# ReactConfiguration class attributes and methods

# PhotosMetaModel_Dependencies class attributes and methods

# PhotosMetaModel_Logic class attributes and methods

# Components class attributes and methods

# UI class attributes and methods

# PhotosMetaModel_Subcomponents class attributes and methods

# PhotosMetaModel_Actions class attributes and methods

# PhotosMetaModel_Request class attributes and methods

# Actions class attributes and methods

# PhotosMetaModel_Services class attributes and methods

# PhotosMetaModel_State class attributes and methods
PhotosMetaModel_State_active: Property = Property(name="active", type=StringType)
PhotosMetaModel_State.attributes={PhotosMetaModel_State_active}

# PhotosMetaModel_CoreFunctions class attributes and methods

# PhotosMetaModel_Router class attributes and methods

# Logic class attributes and methods

# PhotosMetaModel_Structure class attributes and methods

# PhotosMetaModel_ViewComponents class attributes and methods

# PhotosMetaModel_Directories class attributes and methods

# PhotosMetaModel_Files class attributes and methods
PhotosMetaModel_Files_type: Property = Property(name="type", type=StringType)
PhotosMetaModel_Files_extension: Property = Property(name="extension", type=StringType)
PhotosMetaModel_Files.attributes={PhotosMetaModel_Files_extension, PhotosMetaModel_Files_type}

# PhotosMetaModel_Libraries class attributes and methods
PhotosMetaModel_Libraries_type: Property = Property(name="type", type=StringType)
PhotosMetaModel_Libraries.attributes={PhotosMetaModel_Libraries_type}

# PhotosMetaModel_Information class attributes and methods
PhotosMetaModel_Information_fileType: Property = Property(name="fileType", type=StringType)
PhotosMetaModel_Information.attributes={PhotosMetaModel_Information_fileType}

# Relationships
functionalities5: BinaryAssociation = BinaryAssociation(
    name="functionalities5",
    ends={
        Property(name="PhotosMetaModel_Functionalities", type=PhotosMetaModel_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Domain6", type=PhotosMetaModel_Functionalities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities7: BinaryAssociation = BinaryAssociation(
    name="entities7",
    ends={
        Property(name="PhotosMetaModel_Entities", type=PhotosMetaModel_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Domain8", type=PhotosMetaModel_Entities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain0: BinaryAssociation = BinaryAssociation(
    name="domain0",
    ends={
        Property(name="PhotosMetaModel_Domain", type=PhotosMetaModel_SoftGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SoftGallery", type=PhotosMetaModel_Domain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
architecture1: BinaryAssociation = BinaryAssociation(
    name="architecture1",
    ends={
        Property(name="PhotosMetaModel_Architecture", type=PhotosMetaModel_SoftGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SoftGallery2", type=PhotosMetaModel_Architecture, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
technology3: BinaryAssociation = BinaryAssociation(
    name="technology3",
    ends={
        Property(name="PhotosMetaModel_Technology", type=PhotosMetaModel_SoftGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SoftGallery4", type=PhotosMetaModel_Technology, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repository30: BinaryAssociation = BinaryAssociation(
    name="repository30",
    ends={
        Property(name="PhotosMetaModel_Repository", type=PhotosMetaModel_SpringBootApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SpringBootApplication31", type=PhotosMetaModel_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restcontroller32: BinaryAssociation = BinaryAssociation(
    name="restcontroller32",
    ends={
        Property(name="PhotosMetaModel_RestController34", type=PhotosMetaModel_SpringBootApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SpringBootApplication33", type=PhotosMetaModel_RestController, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntier9: BinaryAssociation = BinaryAssociation(
    name="ntier9",
    ends={
        Property(name="PhotosMetaModel_NTier", type=PhotosMetaModel_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Architecture10", type=PhotosMetaModel_NTier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spring11: BinaryAssociation = BinaryAssociation(
    name="spring11",
    ends={
        Property(name="PhotosMetaModel_Spring", type=PhotosMetaModel_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Technology12", type=PhotosMetaModel_Spring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postgresql13: BinaryAssociation = BinaryAssociation(
    name="postgresql13",
    ends={
        Property(name="PhotosMetaModel_PostgreSQL", type=PhotosMetaModel_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Technology14", type=PhotosMetaModel_PostgreSQL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
react15: BinaryAssociation = BinaryAssociation(
    name="react15",
    ends={
        Property(name="PhotosMetaModel_React", type=PhotosMetaModel_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Technology16", type=PhotosMetaModel_React, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
amazonwebservices17: BinaryAssociation = BinaryAssociation(
    name="amazonwebservices17",
    ends={
        Property(name="PhotosMetaModel_AmazonWebServices", type=PhotosMetaModel_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Technology18", type=PhotosMetaModel_AmazonWebServices, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
springbootapplication19: BinaryAssociation = BinaryAssociation(
    name="springbootapplication19",
    ends={
        Property(name="PhotosMetaModel_SpringBootApplication", type=PhotosMetaModel_Spring, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Spring20", type=PhotosMetaModel_SpringBootApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules21: BinaryAssociation = BinaryAssociation(
    name="modules21",
    ends={
        Property(name="PhotosMetaModel_Modules", type=PhotosMetaModel_React, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_React22", type=PhotosMetaModel_Modules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requestmapping23: BinaryAssociation = BinaryAssociation(
    name="requestmapping23",
    ends={
        Property(name="PhotosMetaModel_RequestMapping", type=PhotosMetaModel_RestController, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_RestController", type=PhotosMetaModel_RequestMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionhandler24: BinaryAssociation = BinaryAssociation(
    name="exceptionhandler24",
    ends={
        Property(name="PhotosMetaModel_ExceptionHandler", type=PhotosMetaModel_RestController, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_RestController25", type=PhotosMetaModel_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
autowired26: BinaryAssociation = BinaryAssociation(
    name="autowired26",
    ends={
        Property(name="PhotosMetaModel_Autowired", type=PhotosMetaModel_RestController, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_RestController27", type=PhotosMetaModel_Autowired, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification28: BinaryAssociation = BinaryAssociation(
    name="specification28",
    ends={
        Property(name="PhotosMetaModel_Specification", type=PhotosMetaModel_RestController, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_RestController29", type=PhotosMetaModel_Specification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity35: BinaryAssociation = BinaryAssociation(
    name="entity35",
    ends={
        Property(name="PhotosMetaModel_Entity", type=PhotosMetaModel_SpringBootApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SpringBootApplication36", type=PhotosMetaModel_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component37: BinaryAssociation = BinaryAssociation(
    name="component37",
    ends={
        Property(name="PhotosMetaModel_Component", type=PhotosMetaModel_SpringBootApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SpringBootApplication38", type=PhotosMetaModel_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration39: BinaryAssociation = BinaryAssociation(
    name="configuration39",
    ends={
        Property(name="PhotosMetaModel_Configuration", type=PhotosMetaModel_SpringBootApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SpringBootApplication40", type=PhotosMetaModel_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requestpart41: BinaryAssociation = BinaryAssociation(
    name="requestpart41",
    ends={
        Property(name="PhotosMetaModel_RequestPart", type=PhotosMetaModel_RequestMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_RequestMapping42", type=PhotosMetaModel_RequestPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generatedvalue53: BinaryAssociation = BinaryAssociation(
    name="generatedvalue53",
    ends={
        Property(name="PhotosMetaModel_GeneratedValue", type=PhotosMetaModel_Id, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Id54", type=PhotosMetaModel_GeneratedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception43: BinaryAssociation = BinaryAssociation(
    name="exception43",
    ends={
        Property(name="PhotosMetaModel_Exception", type=PhotosMetaModel_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_ExceptionHandler44", type=PhotosMetaModel_Exception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table45: BinaryAssociation = BinaryAssociation(
    name="table45",
    ends={
        Property(name="PhotosMetaModel_Table_s", type=PhotosMetaModel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Entity46", type=PhotosMetaModel_Table_s, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namednativequery47: BinaryAssociation = BinaryAssociation(
    name="namednativequery47",
    ends={
        Property(name="PhotosMetaModel_NamedNativeQuery", type=PhotosMetaModel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Entity48", type=PhotosMetaModel_NamedNativeQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column_s49: BinaryAssociation = BinaryAssociation(
    name="column_s49",
    ends={
        Property(name="PhotosMetaModel_Column_s", type=PhotosMetaModel_Table_s, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_s50", type=PhotosMetaModel_Column_s, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id51: BinaryAssociation = BinaryAssociation(
    name="id51",
    ends={
        Property(name="PhotosMetaModel_Id", type=PhotosMetaModel_Table_s, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_s52", type=PhotosMetaModel_Id, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enablewebsecurity64: BinaryAssociation = BinaryAssociation(
    name="enablewebsecurity64",
    ends={
        Property(name="PhotosMetaModel_EnableWebSecurity", type=PhotosMetaModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Configuration65", type=PhotosMetaModel_EnableWebSecurity, multiplicity=Multiplicity(0, 1))
    }
)
constraint55: BinaryAssociation = BinaryAssociation(
    name="constraint55",
    ends={
        Property(name="PhotosMetaModel_Constraint", type=PhotosMetaModel_Column_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Column_p", type=PhotosMetaModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype56: BinaryAssociation = BinaryAssociation(
    name="datatype56",
    ends={
        Property(name="PhotosMetaModel_DataType", type=PhotosMetaModel_Column_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Column_p57", type=PhotosMetaModel_DataType, multiplicity=Multiplicity(0, 1))
    }
)
searchcriteria58: BinaryAssociation = BinaryAssociation(
    name="searchcriteria58",
    ends={
        Property(name="PhotosMetaModel_SearchCriteria", type=PhotosMetaModel_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Specification59", type=PhotosMetaModel_SearchCriteria, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification60: BinaryAssociation = BinaryAssociation(
    name="specification60",
    ends={
        Property(name="PhotosMetaModel_Specification61", type=PhotosMetaModel_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Predicate", type=PhotosMetaModel_Specification, multiplicity=Multiplicity(0, 1))
    }
)
bean62: BinaryAssociation = BinaryAssociation(
    name="bean62",
    ends={
        Property(name="PhotosMetaModel_Bean", type=PhotosMetaModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Configuration63", type=PhotosMetaModel_Bean, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause76: BinaryAssociation = BinaryAssociation(
    name="clause76",
    ends={
        Property(name="PhotosMetaModel_Query", type=PhotosMetaModel_Clause, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PhotosMetaModel_Clause", type=PhotosMetaModel_Query, multiplicity=Multiplicity(1, 1))
    }
)
enableresourceserver66: BinaryAssociation = BinaryAssociation(
    name="enableresourceserver66",
    ends={
        Property(name="PhotosMetaModel_EnableResourceServer", type=PhotosMetaModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Configuration67", type=PhotosMetaModel_EnableResourceServer, multiplicity=Multiplicity(0, 1))
    }
)
enableauthorizationserver68: BinaryAssociation = BinaryAssociation(
    name="enableauthorizationserver68",
    ends={
        Property(name="PhotosMetaModel_EnableAuthorizationServer", type=PhotosMetaModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Configuration69", type=PhotosMetaModel_EnableAuthorizationServer, multiplicity=Multiplicity(0, 1))
    }
)
enableglobalmethodsecurity70: BinaryAssociation = BinaryAssociation(
    name="enableglobalmethodsecurity70",
    ends={
        Property(name="PhotosMetaModel_EnableGlobalMethodSecurity", type=PhotosMetaModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Configuration71", type=PhotosMetaModel_EnableGlobalMethodSecurity, multiplicity=Multiplicity(0, 1))
    }
)
order72: BinaryAssociation = BinaryAssociation(
    name="order72",
    ends={
        Property(name="PhotosMetaModel_Order_s", type=PhotosMetaModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Component73", type=PhotosMetaModel_Order_s, multiplicity=Multiplicity(0, 1))
    }
)
cluster74: BinaryAssociation = BinaryAssociation(
    name="cluster74",
    ends={
        Property(name="PhotosMetaModel_Cluster", type=PhotosMetaModel_PostgreSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_PostgreSQL75", type=PhotosMetaModel_Cluster, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column77: BinaryAssociation = BinaryAssociation(
    name="column77",
    ends={
        Property(name="PhotosMetaModel_Column_p78", type=PhotosMetaModel_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_ForeignKey", type=PhotosMetaModel_Column_p, multiplicity=Multiplicity(0, 1))
    }
)
reference79: BinaryAssociation = BinaryAssociation(
    name="reference79",
    ends={
        Property(name="PhotosMetaModel_Table_p", type=PhotosMetaModel_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_ForeignKey80", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(0, 1))
    }
)
column81: BinaryAssociation = BinaryAssociation(
    name="column81",
    ends={
        Property(name="PhotosMetaModel_Column_p83", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_p82", type=PhotosMetaModel_Column_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row84: BinaryAssociation = BinaryAssociation(
    name="row84",
    ends={
        Property(name="PhotosMetaModel_Row", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_p85", type=PhotosMetaModel_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignkey86: BinaryAssociation = BinaryAssociation(
    name="foreignkey86",
    ends={
        Property(name="PhotosMetaModel_ForeignKey88", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_p87", type=PhotosMetaModel_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey89: BinaryAssociation = BinaryAssociation(
    name="primaryKey89",
    ends={
        Property(name="PhotosMetaModel_Column_p91", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_p90", type=PhotosMetaModel_Column_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inherit93: BinaryAssociation = BinaryAssociation(
    name="inherit93",
    ends={
        Property(name="PhotosMetaModel_Table_p94", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Table_p92", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(0, 1))
    }
)
execute107: BinaryAssociation = BinaryAssociation(
    name="execute107",
    ends={
        Property(name="PhotosMetaModel_Query108", type=PhotosMetaModel_User_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_User_p", type=PhotosMetaModel_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scheme95: BinaryAssociation = BinaryAssociation(
    name="scheme95",
    ends={
        Property(name="PhotosMetaModel_Scheme", type=PhotosMetaModel_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Database", type=PhotosMetaModel_Scheme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table_postgresql96: BinaryAssociation = BinaryAssociation(
    name="table_postgresql96",
    ends={
        Property(name="PhotosMetaModel_Table_p98", type=PhotosMetaModel_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Scheme97", type=PhotosMetaModel_Table_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view_postgresql99: BinaryAssociation = BinaryAssociation(
    name="view_postgresql99",
    ends={
        Property(name="PhotosMetaModel_View", type=PhotosMetaModel_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Scheme100", type=PhotosMetaModel_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index101: BinaryAssociation = BinaryAssociation(
    name="index101",
    ends={
        Property(name="PhotosMetaModel_Index_p", type=PhotosMetaModel_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Scheme102", type=PhotosMetaModel_Index_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger103: BinaryAssociation = BinaryAssociation(
    name="trigger103",
    ends={
        Property(name="PhotosMetaModel_Trigger", type=PhotosMetaModel_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Scheme104", type=PhotosMetaModel_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
storedprocedure105: BinaryAssociation = BinaryAssociation(
    name="storedprocedure105",
    ends={
        Property(name="PhotosMetaModel_Function_p", type=PhotosMetaModel_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Scheme106", type=PhotosMetaModel_Function_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint121: BinaryAssociation = BinaryAssociation(
    name="constraint121",
    ends={
        Property(name="PhotosMetaModel_Column122", type=PhotosMetaModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PhotosMetaModel_Constraint123", type=PhotosMetaModel_Column, multiplicity=Multiplicity(1, 1))
    }
)
privilege109: BinaryAssociation = BinaryAssociation(
    name="privilege109",
    ends={
        Property(name="PhotosMetaModel_Privilege", type=PhotosMetaModel_User_p, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_User_p110", type=PhotosMetaModel_Privilege, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database111: BinaryAssociation = BinaryAssociation(
    name="database111",
    ends={
        Property(name="PhotosMetaModel_Database113", type=PhotosMetaModel_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Cluster112", type=PhotosMetaModel_Database, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user_p114: BinaryAssociation = BinaryAssociation(
    name="user_p114",
    ends={
        Property(name="PhotosMetaModel_User_p116", type=PhotosMetaModel_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Cluster115", type=PhotosMetaModel_User_p, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
policy117: BinaryAssociation = BinaryAssociation(
    name="policy117",
    ends={
        Property(name="PhotosMetaModel_Policy", type=PhotosMetaModel_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Row118", type=PhotosMetaModel_Policy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype119: BinaryAssociation = BinaryAssociation(
    name="datatype119",
    ends={
        Property(name="PhotosMetaModel_DataType120", type=PhotosMetaModel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Column", type=PhotosMetaModel_DataType, multiplicity=Multiplicity(0, 1))
    }
)
functionalities124: BinaryAssociation = BinaryAssociation(
    name="functionalities124",
    ends={
        Property(name="PhotosMetaModel_Functionalities125", type=PhotosMetaModel_User_d, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_User_d", type=PhotosMetaModel_Functionalities, multiplicity=Multiplicity(0, 1))
    }
)
connection135: BinaryAssociation = BinaryAssociation(
    name="connection135",
    ends={
        Property(name="PhotosMetaModel_Connection", type=PhotosMetaModel_NTier, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_NTier136", type=PhotosMetaModel_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
albummanagement126: BinaryAssociation = BinaryAssociation(
    name="albummanagement126",
    ends={
        Property(name="PhotosMetaModel_AlbumManagement", type=PhotosMetaModel_PhotoActions, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_PhotoActions", type=PhotosMetaModel_AlbumManagement, multiplicity=Multiplicity(0, 1))
    }
)
photoactions127: BinaryAssociation = BinaryAssociation(
    name="photoactions127",
    ends={
        Property(name="PhotosMetaModel_PhotoActions128", type=PhotosMetaModel_Photo, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Photo", type=PhotosMetaModel_PhotoActions, multiplicity=Multiplicity(0, 1))
    }
)
albummanagement129: BinaryAssociation = BinaryAssociation(
    name="albummanagement129",
    ends={
        Property(name="PhotosMetaModel_AlbumManagement130", type=PhotosMetaModel_Album, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Album", type=PhotosMetaModel_AlbumManagement, multiplicity=Multiplicity(0, 1))
    }
)
amazonsimplestorageservice131: BinaryAssociation = BinaryAssociation(
    name="amazonsimplestorageservice131",
    ends={
        Property(name="PhotosMetaModel_AmazonSimpleStorageService", type=PhotosMetaModel_AmazonWebServices, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_AmazonWebServices132", type=PhotosMetaModel_AmazonSimpleStorageService, multiplicity=Multiplicity(0, 1))
    }
)
amazonelasticcomputecloud133: BinaryAssociation = BinaryAssociation(
    name="amazonelasticcomputecloud133",
    ends={
        Property(name="PhotosMetaModel_AmazonElasticComputeCloud", type=PhotosMetaModel_AmazonWebServices, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_AmazonWebServices134", type=PhotosMetaModel_AmazonElasticComputeCloud, multiplicity=Multiplicity(0, 1))
    }
)
layer137: BinaryAssociation = BinaryAssociation(
    name="layer137",
    ends={
        Property(name="PhotosMetaModel_Layer", type=PhotosMetaModel_NTier, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_NTier138", type=PhotosMetaModel_Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation139: BinaryAssociation = BinaryAssociation(
    name="relation139",
    ends={
        Property(name="PhotosMetaModel_Relation", type=PhotosMetaModel_NTier, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_NTier140", type=PhotosMetaModel_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceLayer141: BinaryAssociation = BinaryAssociation(
    name="sourceLayer141",
    ends={
        Property(name="PhotosMetaModel_Layer143", type=PhotosMetaModel_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Connection142", type=PhotosMetaModel_Layer, multiplicity=Multiplicity(0, 1))
    }
)
targetLayer144: BinaryAssociation = BinaryAssociation(
    name="targetLayer144",
    ends={
        Property(name="PhotosMetaModel_Layer146", type=PhotosMetaModel_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Connection145", type=PhotosMetaModel_Layer, multiplicity=Multiplicity(0, 1))
    }
)
sourceLayer147: BinaryAssociation = BinaryAssociation(
    name="sourceLayer147",
    ends={
        Property(name="PhotosMetaModel_Layer149", type=PhotosMetaModel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Relation148", type=PhotosMetaModel_Layer, multiplicity=Multiplicity(0, 1))
    }
)
targetLayer150: BinaryAssociation = BinaryAssociation(
    name="targetLayer150",
    ends={
        Property(name="PhotosMetaModel_Layer152", type=PhotosMetaModel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Relation151", type=PhotosMetaModel_Layer, multiplicity=Multiplicity(0, 1))
    }
)
segmentstructure156: BinaryAssociation = BinaryAssociation(
    name="segmentstructure156",
    ends={
        Property(name="PhotosMetaModel_SegmentStructure", type=PhotosMetaModel_PresentationSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_PresentationSegment157", type=PhotosMetaModel_SegmentStructure, multiplicity=Multiplicity(0, 1))
    }
)
segmentstructure158: BinaryAssociation = BinaryAssociation(
    name="segmentstructure158",
    ends={
        Property(name="PhotosMetaModel_SegmentStructure160", type=PhotosMetaModel_BusinessLogicSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_BusinessLogicSegment159", type=PhotosMetaModel_SegmentStructure, multiplicity=Multiplicity(0, 1))
    }
)
presentationLayer153: BinaryAssociation = BinaryAssociation(
    name="presentationLayer153",
    ends={
        Property(name="PhotosMetaModel_PresentationSegment", type=PhotosMetaModel_Presentation, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Presentation", type=PhotosMetaModel_PresentationSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BusinessLogicSegment154: BinaryAssociation = BinaryAssociation(
    name="BusinessLogicSegment154",
    ends={
        Property(name="PhotosMetaModel_BusinessLogicSegment", type=PhotosMetaModel_BusinessLogic, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_BusinessLogic", type=PhotosMetaModel_BusinessLogicSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataSegment155: BinaryAssociation = BinaryAssociation(
    name="dataSegment155",
    ends={
        Property(name="PhotosMetaModel_DataSegment", type=PhotosMetaModel_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Data", type=PhotosMetaModel_DataSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactclasses164: BinaryAssociation = BinaryAssociation(
    name="reactclasses164",
    ends={
        Property(name="PhotosMetaModel_ReactClasses", type=PhotosMetaModel_Components, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Components", type=PhotosMetaModel_ReactClasses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segmentstructure161: BinaryAssociation = BinaryAssociation(
    name="segmentstructure161",
    ends={
        Property(name="PhotosMetaModel_SegmentStructure163", type=PhotosMetaModel_DataSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_DataSegment162", type=PhotosMetaModel_SegmentStructure, multiplicity=Multiplicity(0, 1))
    }
)
access172: BinaryAssociation = BinaryAssociation(
    name="access172",
    ends={
        Property(name="PhotosMetaModel_Access", type=PhotosMetaModel_Bucket, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Bucket173", type=PhotosMetaModel_Access, multiplicity=Multiplicity(0, 1))
    }
)
file_a174: BinaryAssociation = BinaryAssociation(
    name="file_a174",
    ends={
        Property(name="PhotosMetaModel_File_a", type=PhotosMetaModel_Bucket, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Bucket175", type=PhotosMetaModel_File_a, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules165: BinaryAssociation = BinaryAssociation(
    name="modules165",
    ends={
        Property(name="PhotosMetaModel_Modules167", type=PhotosMetaModel_Components, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Components166", type=PhotosMetaModel_Modules, multiplicity=Multiplicity(0, 1))
    }
)
bucket168: BinaryAssociation = BinaryAssociation(
    name="bucket168",
    ends={
        Property(name="PhotosMetaModel_Bucket", type=PhotosMetaModel_AmazonSimpleStorageService, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_AmazonSimpleStorageService169", type=PhotosMetaModel_Bucket, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
batchoperation170: BinaryAssociation = BinaryAssociation(
    name="batchoperation170",
    ends={
        Property(name="PhotosMetaModel_BatchOperation", type=PhotosMetaModel_AmazonSimpleStorageService, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_AmazonSimpleStorageService171", type=PhotosMetaModel_BatchOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata178: BinaryAssociation = BinaryAssociation(
    name="metadata178",
    ends={
        Property(name="PhotosMetaModel_MetaData", type=PhotosMetaModel_File_a, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_File_a179", type=PhotosMetaModel_MetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
folder_a176: BinaryAssociation = BinaryAssociation(
    name="folder_a176",
    ends={
        Property(name="PhotosMetaModel_Folder_a", type=PhotosMetaModel_Bucket, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Bucket177", type=PhotosMetaModel_Folder_a, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactfunctions183: BinaryAssociation = BinaryAssociation(
    name="reactfunctions183",
    ends={
        Property(name="PhotosMetaModel_ReactFunctions", type=PhotosMetaModel_ReactClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_ReactClasses184", type=PhotosMetaModel_ReactFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
props185: BinaryAssociation = BinaryAssociation(
    name="props185",
    ends={
        Property(name="PhotosMetaModel_Props", type=PhotosMetaModel_ReactClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_ReactClasses186", type=PhotosMetaModel_Props, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
file_a180: BinaryAssociation = BinaryAssociation(
    name="file_a180",
    ends={
        Property(name="PhotosMetaModel_File_a182", type=PhotosMetaModel_Folder_a, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Folder_a181", type=PhotosMetaModel_File_a, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state187: BinaryAssociation = BinaryAssociation(
    name="state187",
    ends={
        Property(name="PhotosMetaModel_State", type=PhotosMetaModel_ReactClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_ReactClasses188", type=PhotosMetaModel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
corefunctions190: BinaryAssociation = BinaryAssociation(
    name="corefunctions190",
    ends={
        Property(name="PhotosMetaModel_CoreFunctions", type=PhotosMetaModel_CoreFunctions, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_CoreFunctions189", type=PhotosMetaModel_CoreFunctions, multiplicity=Multiplicity(0, 1))
    }
)
directories192: BinaryAssociation = BinaryAssociation(
    name="directories192",
    ends={
        Property(name="PhotosMetaModel_Directories", type=PhotosMetaModel_SegmentStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SegmentStructure193", type=PhotosMetaModel_Directories, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files194: BinaryAssociation = BinaryAssociation(
    name="files194",
    ends={
        Property(name="PhotosMetaModel_Files", type=PhotosMetaModel_SegmentStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_SegmentStructure195", type=PhotosMetaModel_Files, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
request191: BinaryAssociation = BinaryAssociation(
    name="request191",
    ends={
        Property(name="PhotosMetaModel_Request", type=PhotosMetaModel_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Services", type=PhotosMetaModel_Request, multiplicity=Multiplicity(0, 1))
    }
)
files196: BinaryAssociation = BinaryAssociation(
    name="files196",
    ends={
        Property(name="PhotosMetaModel_Files198", type=PhotosMetaModel_Directories, multiplicity=Multiplicity(1, 1)),
        Property(name="PhotosMetaModel_Directories197", type=PhotosMetaModel_Files, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_PhotosMetaModel_GetMapping_RequestMapping = Generalization(general=RequestMapping, specific=PhotosMetaModel_GetMapping)
gen_PhotosMetaModel_PutMapping_RequestMapping = Generalization(general=RequestMapping, specific=PhotosMetaModel_PutMapping)
gen_PhotosMetaModel_PostMapping_RequestMapping = Generalization(general=RequestMapping, specific=PhotosMetaModel_PostMapping)
gen_PhotosMetaModel_DeleteMapping_RequestMapping = Generalization(general=RequestMapping, specific=PhotosMetaModel_DeleteMapping)
gen_PhotosMetaModel_AlbumManagement_Functionalities = Generalization(general=Functionalities, specific=PhotosMetaModel_AlbumManagement)
gen_PhotosMetaModel_PhotoActions_Functionalities = Generalization(general=Functionalities, specific=PhotosMetaModel_PhotoActions)
gen_PhotosMetaModel_User_d_Entities = Generalization(general=Entities, specific=PhotosMetaModel_User_d)
gen_PhotosMetaModel_AppAccess_Functionalities = Generalization(general=Functionalities, specific=PhotosMetaModel_AppAccess)
gen_PhotosMetaModel_ProfileManagement_Functionalities = Generalization(general=Functionalities, specific=PhotosMetaModel_ProfileManagement)
gen_PhotosMetaModel_Photo_Entities = Generalization(general=Entities, specific=PhotosMetaModel_Photo)
gen_PhotosMetaModel_Album_Entities = Generalization(general=Entities, specific=PhotosMetaModel_Album)
gen_PhotosMetaModel_AmazonS3API_Connection = Generalization(general=Connection, specific=PhotosMetaModel_AmazonS3API)
gen_PhotosMetaModel_REST_Connection = Generalization(general=Connection, specific=PhotosMetaModel_REST)
gen_PhotosMetaModel_PostgreSQLConnection_Connection = Generalization(general=Connection, specific=PhotosMetaModel_PostgreSQLConnection)
gen_PhotosMetaModel_AllowedToUse_Relation = Generalization(general=Relation, specific=PhotosMetaModel_AllowedToUse)
gen_PhotosMetaModel_Presentation_Layer = Generalization(general=Layer, specific=PhotosMetaModel_Presentation)
gen_PhotosMetaModel_BusinessLogic_Layer = Generalization(general=Layer, specific=PhotosMetaModel_BusinessLogic)
gen_PhotosMetaModel_Data_Layer = Generalization(general=Layer, specific=PhotosMetaModel_Data)
gen_PhotosMetaModel_AmazonS3Storage_DataSegment = Generalization(general=DataSegment, specific=PhotosMetaModel_AmazonS3Storage)
gen_PhotosMetaModel_Components_Modules = Generalization(general=Modules, specific=PhotosMetaModel_Components)
gen_PhotosMetaModel_View_a_PresentationSegment = Generalization(general=PresentationSegment, specific=PhotosMetaModel_View_a)
gen_PhotosMetaModel_Component_a_PresentationSegment = Generalization(general=PresentationSegment, specific=PhotosMetaModel_Component_a)
gen_PhotosMetaModel_Action_a_PresentationSegment = Generalization(general=PresentationSegment, specific=PhotosMetaModel_Action_a)
gen_PhotosMetaModel_Controller_a_BusinessLogicSegment = Generalization(general=BusinessLogicSegment, specific=PhotosMetaModel_Controller_a)
gen_PhotosMetaModel_Model_a_BusinessLogicSegment = Generalization(general=BusinessLogicSegment, specific=PhotosMetaModel_Model_a)
gen_PhotosMetaModel_Repository_a_BusinessLogicSegment = Generalization(general=BusinessLogicSegment, specific=PhotosMetaModel_Repository_a)
gen_PhotosMetaModel_Security_a_BusinessLogicSegment = Generalization(general=BusinessLogicSegment, specific=PhotosMetaModel_Security_a)
gen_PhotosMetaModel_PostgreSQL_a_DataSegment = Generalization(general=DataSegment, specific=PhotosMetaModel_PostgreSQL_a)
gen_PhotosMetaModel_Render_ReactFunctions = Generalization(general=ReactFunctions, specific=PhotosMetaModel_Render)
gen_PhotosMetaModel_Constructor_ReactFunctions = Generalization(general=ReactFunctions, specific=PhotosMetaModel_Constructor)
gen_PhotosMetaModel_LifeCycle_ReactFunctions = Generalization(general=ReactFunctions, specific=PhotosMetaModel_LifeCycle)
gen_PhotosMetaModel_Public_Access = Generalization(general=Access, specific=PhotosMetaModel_Public)
gen_PhotosMetaModel_ObjectsPublic_Access = Generalization(general=Access, specific=PhotosMetaModel_ObjectsPublic)
gen_PhotosMetaModel_BucketObjectsNotPublic_Access = Generalization(general=Access, specific=PhotosMetaModel_BucketObjectsNotPublic)
gen_PhotosMetaModel_OnlyAuthorized_Access = Generalization(general=Access, specific=PhotosMetaModel_OnlyAuthorized)
gen_PhotosMetaModel_UI_Components = Generalization(general=Components, specific=PhotosMetaModel_UI)
gen_PhotosMetaModel_ReactConfiguration_Modules = Generalization(general=Modules, specific=PhotosMetaModel_ReactConfiguration)
gen_PhotosMetaModel_ReactDOM_ReactConfiguration = Generalization(general=ReactConfiguration, specific=PhotosMetaModel_ReactDOM)
gen_PhotosMetaModel_Dependencies_ReactConfiguration = Generalization(general=ReactConfiguration, specific=PhotosMetaModel_Dependencies)
gen_PhotosMetaModel_Logic_Components = Generalization(general=Components, specific=PhotosMetaModel_Logic)
gen_PhotosMetaModel_ViewComponents_UI = Generalization(general=UI, specific=PhotosMetaModel_ViewComponents)
gen_PhotosMetaModel_Subcomponents_UI = Generalization(general=UI, specific=PhotosMetaModel_Subcomponents)
gen_PhotosMetaModel_Actions_Modules = Generalization(general=Modules, specific=PhotosMetaModel_Actions)
gen_PhotosMetaModel_Request_Actions = Generalization(general=Actions, specific=PhotosMetaModel_Request)
gen_PhotosMetaModel_Services_Actions = Generalization(general=Actions, specific=PhotosMetaModel_Services)
gen_PhotosMetaModel_CoreFunctions_ReactFunctions = Generalization(general=ReactFunctions, specific=PhotosMetaModel_CoreFunctions)
gen_PhotosMetaModel_Router_Logic = Generalization(general=Logic, specific=PhotosMetaModel_Router)
gen_PhotosMetaModel_Structure_Logic = Generalization(general=Logic, specific=PhotosMetaModel_Structure)
gen_PhotosMetaModel_Libraries_Modules = Generalization(general=Modules, specific=PhotosMetaModel_Libraries)
gen_PhotosMetaModel_Information_Modules = Generalization(general=Modules, specific=PhotosMetaModel_Information)

# Domain Model
domain_model = DomainModel(
    name="PhotosMetaModel",
    types={PhotosMetaModel_Functionalities, PhotosMetaModel_Entities, PhotosMetaModel_SoftGallery, PhotosMetaModel_Domain, PhotosMetaModel_Architecture, PhotosMetaModel_Technology, PhotosMetaModel_Entity, PhotosMetaModel_NTier, PhotosMetaModel_Spring, PhotosMetaModel_PostgreSQL, PhotosMetaModel_React, PhotosMetaModel_AmazonWebServices, PhotosMetaModel_SpringBootApplication, PhotosMetaModel_Modules, PhotosMetaModel_Repository, PhotosMetaModel_RestController, PhotosMetaModel_RequestMapping, PhotosMetaModel_ExceptionHandler, PhotosMetaModel_Autowired, PhotosMetaModel_Specification, PhotosMetaModel_GetMapping, PhotosMetaModel_PutMapping, PhotosMetaModel_Component, PhotosMetaModel_Configuration, PhotosMetaModel_RequestPart, PhotosMetaModel_PostMapping, RequestMapping, PhotosMetaModel_GeneratedValue, PhotosMetaModel_Exception, PhotosMetaModel_DeleteMapping, PhotosMetaModel_Table_s, PhotosMetaModel_NamedNativeQuery, PhotosMetaModel_Column_s, PhotosMetaModel_Id, PhotosMetaModel_EnableWebSecurity, PhotosMetaModel_EnableResourceServer, PhotosMetaModel_Column_p, PhotosMetaModel_Constraint, PhotosMetaModel_DataType, PhotosMetaModel_SearchCriteria, PhotosMetaModel_Predicate, PhotosMetaModel_Bean, PhotosMetaModel_ForeignKey, PhotosMetaModel_EnableAuthorizationServer, PhotosMetaModel_EnableGlobalMethodSecurity, PhotosMetaModel_Order_s, PhotosMetaModel_Cluster, PhotosMetaModel_Query, PhotosMetaModel_Clause, PhotosMetaModel_Function_p, PhotosMetaModel_Database, PhotosMetaModel_Table_p, PhotosMetaModel_Trigger, PhotosMetaModel_View, PhotosMetaModel_Index_p, PhotosMetaModel_Row, PhotosMetaModel_User_p, PhotosMetaModel_Scheme, PhotosMetaModel_Privilege, PhotosMetaModel_Policy, PhotosMetaModel_Column, PhotosMetaModel_AlbumManagement, PhotosMetaModel_PhotoActions, PhotosMetaModel_Index, PhotosMetaModel_User_d, Entities, PhotosMetaModel_AppAccess, Functionalities, PhotosMetaModel_ProfileManagement, PhotosMetaModel_Layer, PhotosMetaModel_Photo, PhotosMetaModel_Album, PhotosMetaModel_AmazonSimpleStorageService, PhotosMetaModel_AmazonElasticComputeCloud, PhotosMetaModel_Connection, PhotosMetaModel_AmazonS3API, PhotosMetaModel_Relation, PhotosMetaModel_REST, Connection, PhotosMetaModel_PostgreSQLConnection, PhotosMetaModel_AllowedToUse, Relation, PhotosMetaModel_SegmentStructure, PhotosMetaModel_Presentation, Layer, PhotosMetaModel_PresentationSegment, PhotosMetaModel_BusinessLogic, PhotosMetaModel_BusinessLogicSegment, PhotosMetaModel_Data, PhotosMetaModel_DataSegment, PhotosMetaModel_AmazonS3Storage, PhotosMetaModel_Components, Modules, PhotosMetaModel_ReactClasses, PhotosMetaModel_View_a, PresentationSegment, PhotosMetaModel_Component_a, PhotosMetaModel_Action_a, PhotosMetaModel_Controller_a, BusinessLogicSegment, PhotosMetaModel_Model_a, PhotosMetaModel_Repository_a, PhotosMetaModel_Security_a, PhotosMetaModel_PostgreSQL_a, DataSegment, PhotosMetaModel_Access, PhotosMetaModel_File_a, PhotosMetaModel_ReactFunctions, PhotosMetaModel_Render, ReactFunctions, PhotosMetaModel_Constructor, PhotosMetaModel_LifeCycle, PhotosMetaModel_Bucket, PhotosMetaModel_BatchOperation, PhotosMetaModel_MetaData, PhotosMetaModel_Folder_a, PhotosMetaModel_Public, Access, PhotosMetaModel_ObjectsPublic, PhotosMetaModel_BucketObjectsNotPublic, PhotosMetaModel_OnlyAuthorized, PhotosMetaModel_UI, PhotosMetaModel_Props, PhotosMetaModel_ReactConfiguration, PhotosMetaModel_ReactDOM, ReactConfiguration, PhotosMetaModel_Dependencies, PhotosMetaModel_Logic, Components, UI, PhotosMetaModel_Subcomponents, PhotosMetaModel_Actions, PhotosMetaModel_Request, Actions, PhotosMetaModel_Services, PhotosMetaModel_State, PhotosMetaModel_CoreFunctions, PhotosMetaModel_Router, Logic, PhotosMetaModel_Structure, PhotosMetaModel_ViewComponents, PhotosMetaModel_Directories, PhotosMetaModel_Files, PhotosMetaModel_Libraries, PhotosMetaModel_Information},
    associations={functionalities5, entities7, domain0, architecture1, technology3, repository30, restcontroller32, ntier9, spring11, postgresql13, react15, amazonwebservices17, springbootapplication19, modules21, requestmapping23, exceptionhandler24, autowired26, specification28, entity35, component37, configuration39, requestpart41, generatedvalue53, exception43, table45, namednativequery47, column_s49, id51, enablewebsecurity64, constraint55, datatype56, searchcriteria58, specification60, bean62, clause76, enableresourceserver66, enableauthorizationserver68, enableglobalmethodsecurity70, order72, cluster74, column77, reference79, column81, row84, foreignkey86, primaryKey89, inherit93, execute107, scheme95, table_postgresql96, view_postgresql99, index101, trigger103, storedprocedure105, constraint121, privilege109, database111, user_p114, policy117, datatype119, functionalities124, connection135, albummanagement126, photoactions127, albummanagement129, amazonsimplestorageservice131, amazonelasticcomputecloud133, layer137, relation139, sourceLayer141, targetLayer144, sourceLayer147, targetLayer150, segmentstructure156, segmentstructure158, presentationLayer153, BusinessLogicSegment154, dataSegment155, reactclasses164, segmentstructure161, access172, file_a174, modules165, bucket168, batchoperation170, metadata178, folder_a176, reactfunctions183, props185, file_a180, state187, corefunctions190, directories192, files194, request191, files196},
    generalizations={gen_PhotosMetaModel_GetMapping_RequestMapping, gen_PhotosMetaModel_PutMapping_RequestMapping, gen_PhotosMetaModel_PostMapping_RequestMapping, gen_PhotosMetaModel_DeleteMapping_RequestMapping, gen_PhotosMetaModel_AlbumManagement_Functionalities, gen_PhotosMetaModel_PhotoActions_Functionalities, gen_PhotosMetaModel_User_d_Entities, gen_PhotosMetaModel_AppAccess_Functionalities, gen_PhotosMetaModel_ProfileManagement_Functionalities, gen_PhotosMetaModel_Photo_Entities, gen_PhotosMetaModel_Album_Entities, gen_PhotosMetaModel_AmazonS3API_Connection, gen_PhotosMetaModel_REST_Connection, gen_PhotosMetaModel_PostgreSQLConnection_Connection, gen_PhotosMetaModel_AllowedToUse_Relation, gen_PhotosMetaModel_Presentation_Layer, gen_PhotosMetaModel_BusinessLogic_Layer, gen_PhotosMetaModel_Data_Layer, gen_PhotosMetaModel_AmazonS3Storage_DataSegment, gen_PhotosMetaModel_Components_Modules, gen_PhotosMetaModel_View_a_PresentationSegment, gen_PhotosMetaModel_Component_a_PresentationSegment, gen_PhotosMetaModel_Action_a_PresentationSegment, gen_PhotosMetaModel_Controller_a_BusinessLogicSegment, gen_PhotosMetaModel_Model_a_BusinessLogicSegment, gen_PhotosMetaModel_Repository_a_BusinessLogicSegment, gen_PhotosMetaModel_Security_a_BusinessLogicSegment, gen_PhotosMetaModel_PostgreSQL_a_DataSegment, gen_PhotosMetaModel_Render_ReactFunctions, gen_PhotosMetaModel_Constructor_ReactFunctions, gen_PhotosMetaModel_LifeCycle_ReactFunctions, gen_PhotosMetaModel_Public_Access, gen_PhotosMetaModel_ObjectsPublic_Access, gen_PhotosMetaModel_BucketObjectsNotPublic_Access, gen_PhotosMetaModel_OnlyAuthorized_Access, gen_PhotosMetaModel_UI_Components, gen_PhotosMetaModel_ReactConfiguration_Modules, gen_PhotosMetaModel_ReactDOM_ReactConfiguration, gen_PhotosMetaModel_Dependencies_ReactConfiguration, gen_PhotosMetaModel_Logic_Components, gen_PhotosMetaModel_ViewComponents_UI, gen_PhotosMetaModel_Subcomponents_UI, gen_PhotosMetaModel_Actions_Modules, gen_PhotosMetaModel_Request_Actions, gen_PhotosMetaModel_Services_Actions, gen_PhotosMetaModel_CoreFunctions_ReactFunctions, gen_PhotosMetaModel_Router_Logic, gen_PhotosMetaModel_Structure_Logic, gen_PhotosMetaModel_Libraries_Modules, gen_PhotosMetaModel_Information_Modules},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)