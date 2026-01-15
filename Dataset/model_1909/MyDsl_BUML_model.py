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
myDsl_Entities = Class(name="myDsl::Entities")
myDsl_Model = Class(name="myDsl::Model")
myDsl_EObject = Class(name="myDsl::EObject")
myDsl_Domain = Class(name="myDsl::Domain")
myDsl_Entity = Class(name="myDsl::Entity")
myDsl_AppAccess = Class(name="myDsl::AppAccess")
myDsl_AlbumManagement = Class(name="myDsl::AlbumManagement")
myDsl_PhotoActions = Class(name="myDsl::PhotoActions")
myDsl_Photo = Class(name="myDsl::Photo")
myDsl_Album = Class(name="myDsl::Album")
myDsl_UserDomain = Class(name="myDsl::UserDomain")
myDsl_Functionality = Class(name="myDsl::Functionality")
myDsl_Functionalities = Class(name="myDsl::Functionalities")
myDsl_ProfileManagement = Class(name="myDsl::ProfileManagement")
myDsl_LandingActions = Class(name="myDsl::LandingActions")
myDsl_ProfileManagementFunctions = Class(name="myDsl::ProfileManagementFunctions")
myDsl_AppAccessFunctions = Class(name="myDsl::AppAccessFunctions")
myDsl_AlbumManagementFunctions = Class(name="myDsl::AlbumManagementFunctions")
myDsl_PhotoActionsFunctions = Class(name="myDsl::PhotoActionsFunctions")
myDsl_LandingFunctions = Class(name="myDsl::LandingFunctions")
myDsl_DomainConnection = Class(name="myDsl::DomainConnection")
myDsl_DomainRelations = Class(name="myDsl::DomainRelations")
myDsl_PresentationLayer = Class(name="myDsl::PresentationLayer")
myDsl_Architecture = Class(name="myDsl::Architecture")
myDsl_NTiers = Class(name="myDsl::NTiers")
myDsl_Layer = Class(name="myDsl::Layer")
myDsl_SegmentStructure = Class(name="myDsl::SegmentStructure")
myDsl_SegmentStructureContent = Class(name="myDsl::SegmentStructureContent")
myDsl_PresentationContent = Class(name="myDsl::PresentationContent")
myDsl_PresentationSegments = Class(name="myDsl::PresentationSegments")
myDsl_BusinessLogicLayer = Class(name="myDsl::BusinessLogicLayer")
myDsl_BusinessLogicContent = Class(name="myDsl::BusinessLogicContent")
myDsl_BusinessLogicSegments = Class(name="myDsl::BusinessLogicSegments")
myDsl_DataPersistenceLayer = Class(name="myDsl::DataPersistenceLayer")
myDsl_DataPersistenceContent = Class(name="myDsl::DataPersistenceContent")
myDsl_DataPersistenceSegments = Class(name="myDsl::DataPersistenceSegments")
myDsl_LayerSource = Class(name="myDsl::LayerSource")
myDsl_DirectoryContent = Class(name="myDsl::DirectoryContent")
myDsl_Directories = Class(name="myDsl::Directories")
myDsl_MultipleFile = Class(name="myDsl::MultipleFile")
myDsl_SingleFile = Class(name="myDsl::SingleFile")
myDsl_LayerRelations = Class(name="myDsl::LayerRelations")
myDsl_NTierSource = Class(name="myDsl::NTierSource")
myDsl_LayerTarget = Class(name="myDsl::LayerTarget")
myDsl_ArchitectureComponents = Class(name="myDsl::ArchitectureComponents")
myDsl_FrontEnd = Class(name="myDsl::FrontEnd")
myDsl_BackEnd = Class(name="myDsl::BackEnd")
myDsl_PersistenceDataComponent = Class(name="myDsl::PersistenceDataComponent")
myDsl_NTiersConnections = Class(name="myDsl::NTiersConnections")
myDsl_NTierTarget = Class(name="myDsl::NTierTarget")
myDsl_ReactSubModules = Class(name="myDsl::ReactSubModules")
myDsl_NTiersRelations = Class(name="myDsl::NTiersRelations")
myDsl_Technology = Class(name="myDsl::Technology")
myDsl_Technologies = Class(name="myDsl::Technologies")
myDsl_React = Class(name="myDsl::React")
myDsl_ReactModules = Class(name="myDsl::ReactModules")
myDsl_SingleDependencies = Class(name="myDsl::SingleDependencies")
myDsl_ReactConfiguration = Class(name="myDsl::ReactConfiguration")
myDsl_ReactDependencies = Class(name="myDsl::ReactDependencies")
myDsl_ReactConfigurations = Class(name="myDsl::ReactConfigurations")
myDsl_ReactDependenciesRules = Class(name="myDsl::ReactDependenciesRules")
myDsl_ReactDependenciesSubRules = Class(name="myDsl::ReactDependenciesSubRules")
myDsl_LogicContent = Class(name="myDsl::LogicContent")
myDsl_PackageName = Class(name="myDsl::PackageName")
myDsl_PackageVersion = Class(name="myDsl::PackageVersion")
myDsl_DOMConfigurations = Class(name="myDsl::DOMConfigurations")
myDsl_ReactComponents = Class(name="myDsl::ReactComponents")
myDsl_ComponentsLogic = Class(name="myDsl::ComponentsLogic")
myDsl_ComponentsUI = Class(name="myDsl::ComponentsUI")
myDsl_ReactFunctions = Class(name="myDsl::ReactFunctions")
myDsl_LogicStructure = Class(name="myDsl::LogicStructure")
myDsl_ComponentClass = Class(name="myDsl::ComponentClass")
myDsl_UIContent = Class(name="myDsl::UIContent")
myDsl_ReactServicesRelation = Class(name="myDsl::ReactServicesRelation")
myDsl_ReactConstructor = Class(name="myDsl::ReactConstructor")
myDsl_State = Class(name="myDsl::State")
myDsl_CoreFunctionsDeclaration = Class(name="myDsl::CoreFunctionsDeclaration")
myDsl_Props = Class(name="myDsl::Props")
myDsl_ReactCoreFunctions = Class(name="myDsl::ReactCoreFunctions")
myDsl_ReactActions = Class(name="myDsl::ReactActions")
myDsl_ReactActionsContent = Class(name="myDsl::ReactActionsContent")
myDsl_AmazonWebServices = Class(name="myDsl::AmazonWebServices")
myDsl_ReactServicesType = Class(name="myDsl::ReactServicesType")
myDsl_ReactLibraries = Class(name="myDsl::ReactLibraries")
myDsl_ReactLibrary = Class(name="myDsl::ReactLibrary")
myDsl_ReactInfo = Class(name="myDsl::ReactInfo")
myDsl_ReactInformation = Class(name="myDsl::ReactInformation")
myDsl_Spring = Class(name="myDsl::Spring")
myDsl_PostgreSQL = Class(name="myDsl::PostgreSQL")

# myDsl_Entities class attributes and methods

# myDsl_Model class attributes and methods

# myDsl_EObject class attributes and methods

# myDsl_Domain class attributes and methods
myDsl_Domain_name: Property = Property(name="name", type=StringType)
myDsl_Domain.attributes={myDsl_Domain_name}

# myDsl_Entity class attributes and methods

# myDsl_AppAccess class attributes and methods

# myDsl_AlbumManagement class attributes and methods

# myDsl_PhotoActions class attributes and methods

# myDsl_Photo class attributes and methods
myDsl_Photo_name: Property = Property(name="name", type=StringType)
myDsl_Photo.attributes={myDsl_Photo_name}

# myDsl_Album class attributes and methods
myDsl_Album_name: Property = Property(name="name", type=StringType)
myDsl_Album.attributes={myDsl_Album_name}

# myDsl_UserDomain class attributes and methods
myDsl_UserDomain_name: Property = Property(name="name", type=StringType)
myDsl_UserDomain.attributes={myDsl_UserDomain_name}

# myDsl_Functionality class attributes and methods

# myDsl_Functionalities class attributes and methods

# myDsl_ProfileManagement class attributes and methods

# myDsl_LandingActions class attributes and methods

# myDsl_ProfileManagementFunctions class attributes and methods
myDsl_ProfileManagementFunctions_name: Property = Property(name="name", type=StringType)
myDsl_ProfileManagementFunctions.attributes={myDsl_ProfileManagementFunctions_name}

# myDsl_AppAccessFunctions class attributes and methods
myDsl_AppAccessFunctions_name: Property = Property(name="name", type=StringType)
myDsl_AppAccessFunctions.attributes={myDsl_AppAccessFunctions_name}

# myDsl_AlbumManagementFunctions class attributes and methods
myDsl_AlbumManagementFunctions_name: Property = Property(name="name", type=StringType)
myDsl_AlbumManagementFunctions.attributes={myDsl_AlbumManagementFunctions_name}

# myDsl_PhotoActionsFunctions class attributes and methods
myDsl_PhotoActionsFunctions_name: Property = Property(name="name", type=StringType)
myDsl_PhotoActionsFunctions.attributes={myDsl_PhotoActionsFunctions_name}

# myDsl_LandingFunctions class attributes and methods
myDsl_LandingFunctions_name: Property = Property(name="name", type=StringType)
myDsl_LandingFunctions.attributes={myDsl_LandingFunctions_name}

# myDsl_DomainConnection class attributes and methods

# myDsl_DomainRelations class attributes and methods
myDsl_DomainRelations_name: Property = Property(name="name", type=StringType)
myDsl_DomainRelations.attributes={myDsl_DomainRelations_name}

# myDsl_PresentationLayer class attributes and methods

# myDsl_Architecture class attributes and methods

# myDsl_NTiers class attributes and methods

# myDsl_Layer class attributes and methods

# myDsl_SegmentStructure class attributes and methods

# myDsl_SegmentStructureContent class attributes and methods
myDsl_SegmentStructureContent_name: Property = Property(name="name", type=StringType)
myDsl_SegmentStructureContent.attributes={myDsl_SegmentStructureContent_name}

# myDsl_PresentationContent class attributes and methods

# myDsl_PresentationSegments class attributes and methods
myDsl_PresentationSegments_name: Property = Property(name="name", type=StringType)
myDsl_PresentationSegments.attributes={myDsl_PresentationSegments_name}

# myDsl_BusinessLogicLayer class attributes and methods

# myDsl_BusinessLogicContent class attributes and methods

# myDsl_BusinessLogicSegments class attributes and methods
myDsl_BusinessLogicSegments_name: Property = Property(name="name", type=StringType)
myDsl_BusinessLogicSegments.attributes={myDsl_BusinessLogicSegments_name}

# myDsl_DataPersistenceLayer class attributes and methods

# myDsl_DataPersistenceContent class attributes and methods

# myDsl_DataPersistenceSegments class attributes and methods
myDsl_DataPersistenceSegments_name: Property = Property(name="name", type=StringType)
myDsl_DataPersistenceSegments.attributes={myDsl_DataPersistenceSegments_name}

# myDsl_LayerSource class attributes and methods
myDsl_LayerSource_layerelations: Property = Property(name="layerelations", type=StringType)
myDsl_LayerSource.attributes={myDsl_LayerSource_layerelations}

# myDsl_DirectoryContent class attributes and methods
myDsl_DirectoryContent_name: Property = Property(name="name", type=StringType)
myDsl_DirectoryContent.attributes={myDsl_DirectoryContent_name}

# myDsl_Directories class attributes and methods

# myDsl_MultipleFile class attributes and methods
myDsl_MultipleFile_name: Property = Property(name="name", type=StringType)
myDsl_MultipleFile.attributes={myDsl_MultipleFile_name}

# myDsl_SingleFile class attributes and methods
myDsl_SingleFile_name: Property = Property(name="name", type=StringType)
myDsl_SingleFile.attributes={myDsl_SingleFile_name}

# myDsl_LayerRelations class attributes and methods
myDsl_LayerRelations_name: Property = Property(name="name", type=StringType)
myDsl_LayerRelations_layerelations: Property = Property(name="layerelations", type=StringType)
myDsl_LayerRelations.attributes={myDsl_LayerRelations_layerelations, myDsl_LayerRelations_name}

# myDsl_NTierSource class attributes and methods

# myDsl_LayerTarget class attributes and methods
myDsl_LayerTarget_layerelations: Property = Property(name="layerelations", type=StringType)
myDsl_LayerTarget.attributes={myDsl_LayerTarget_layerelations}

# myDsl_ArchitectureComponents class attributes and methods

# myDsl_FrontEnd class attributes and methods
myDsl_FrontEnd_name: Property = Property(name="name", type=StringType)
myDsl_FrontEnd.attributes={myDsl_FrontEnd_name}

# myDsl_BackEnd class attributes and methods
myDsl_BackEnd_name: Property = Property(name="name", type=StringType)
myDsl_BackEnd.attributes={myDsl_BackEnd_name}

# myDsl_PersistenceDataComponent class attributes and methods
myDsl_PersistenceDataComponent_name: Property = Property(name="name", type=StringType)
myDsl_PersistenceDataComponent.attributes={myDsl_PersistenceDataComponent_name}

# myDsl_NTiersConnections class attributes and methods
myDsl_NTiersConnections_ntierconnection: Property = Property(name="ntierconnection", type=StringType)
myDsl_NTiersConnections_name: Property = Property(name="name", type=StringType)
myDsl_NTiersConnections.attributes={myDsl_NTiersConnections_name, myDsl_NTiersConnections_ntierconnection}

# myDsl_NTierTarget class attributes and methods

# myDsl_ReactSubModules class attributes and methods

# myDsl_NTiersRelations class attributes and methods
myDsl_NTiersRelations_name: Property = Property(name="name", type=StringType)
myDsl_NTiersRelations.attributes={myDsl_NTiersRelations_name}

# myDsl_Technology class attributes and methods
myDsl_Technology_name: Property = Property(name="name", type=StringType)
myDsl_Technology.attributes={myDsl_Technology_name}

# myDsl_Technologies class attributes and methods

# myDsl_React class attributes and methods
myDsl_React_name: Property = Property(name="name", type=StringType)
myDsl_React.attributes={myDsl_React_name}

# myDsl_ReactModules class attributes and methods

# myDsl_SingleDependencies class attributes and methods

# myDsl_ReactConfiguration class attributes and methods

# myDsl_ReactDependencies class attributes and methods

# myDsl_ReactConfigurations class attributes and methods
myDsl_ReactConfigurations_name: Property = Property(name="name", type=StringType)
myDsl_ReactConfigurations.attributes={myDsl_ReactConfigurations_name}

# myDsl_ReactDependenciesRules class attributes and methods
myDsl_ReactDependenciesRules_name: Property = Property(name="name", type=StringType)
myDsl_ReactDependenciesRules.attributes={myDsl_ReactDependenciesRules_name}

# myDsl_ReactDependenciesSubRules class attributes and methods

# myDsl_LogicContent class attributes and methods
myDsl_LogicContent_name: Property = Property(name="name", type=StringType)
myDsl_LogicContent.attributes={myDsl_LogicContent_name}

# myDsl_PackageName class attributes and methods
myDsl_PackageName_name: Property = Property(name="name", type=StringType)
myDsl_PackageName.attributes={myDsl_PackageName_name}

# myDsl_PackageVersion class attributes and methods
myDsl_PackageVersion_name: Property = Property(name="name", type=StringType)
myDsl_PackageVersion.attributes={myDsl_PackageVersion_name}

# myDsl_DOMConfigurations class attributes and methods
myDsl_DOMConfigurations_elements: Property = Property(name="elements", type=StringType)
myDsl_DOMConfigurations_name: Property = Property(name="name", type=StringType)
myDsl_DOMConfigurations.attributes={myDsl_DOMConfigurations_name, myDsl_DOMConfigurations_elements}

# myDsl_ReactComponents class attributes and methods

# myDsl_ComponentsLogic class attributes and methods
myDsl_ComponentsLogic_name: Property = Property(name="name", type=StringType)
myDsl_ComponentsLogic.attributes={myDsl_ComponentsLogic_name}

# myDsl_ComponentsUI class attributes and methods
myDsl_ComponentsUI_name: Property = Property(name="name", type=StringType)
myDsl_ComponentsUI.attributes={myDsl_ComponentsUI_name}

# myDsl_ReactFunctions class attributes and methods
myDsl_ReactFunctions_lifecycleclass: Property = Property(name="lifecycleclass", type=StringType)
myDsl_ReactFunctions_renderclass: Property = Property(name="renderclass", type=StringType)
myDsl_ReactFunctions.attributes={myDsl_ReactFunctions_renderclass, myDsl_ReactFunctions_lifecycleclass}

# myDsl_LogicStructure class attributes and methods
myDsl_LogicStructure_name: Property = Property(name="name", type=StringType)
myDsl_LogicStructure.attributes={myDsl_LogicStructure_name}

# myDsl_ComponentClass class attributes and methods

# myDsl_UIContent class attributes and methods
myDsl_UIContent_name: Property = Property(name="name", type=StringType)
myDsl_UIContent.attributes={myDsl_UIContent_name}

# myDsl_ReactServicesRelation class attributes and methods
myDsl_ReactServicesRelation_name: Property = Property(name="name", type=StringType)
myDsl_ReactServicesRelation.attributes={myDsl_ReactServicesRelation_name}

# myDsl_ReactConstructor class attributes and methods

# myDsl_State class attributes and methods
myDsl_State_name: Property = Property(name="name", type=StringType)
myDsl_State_componentclass: Property = Property(name="componentclass", type=StringType)
myDsl_State.attributes={myDsl_State_name, myDsl_State_componentclass}

# myDsl_CoreFunctionsDeclaration class attributes and methods
myDsl_CoreFunctionsDeclaration_name: Property = Property(name="name", type=StringType)
myDsl_CoreFunctionsDeclaration.attributes={myDsl_CoreFunctionsDeclaration_name}

# myDsl_Props class attributes and methods
myDsl_Props_name: Property = Property(name="name", type=StringType)
myDsl_Props_componentclass: Property = Property(name="componentclass", type=StringType)
myDsl_Props.attributes={myDsl_Props_name, myDsl_Props_componentclass}

# myDsl_ReactCoreFunctions class attributes and methods
myDsl_ReactCoreFunctions_name: Property = Property(name="name", type=StringType)
myDsl_ReactCoreFunctions.attributes={myDsl_ReactCoreFunctions_name}

# myDsl_ReactActions class attributes and methods

# myDsl_ReactActionsContent class attributes and methods

# myDsl_AmazonWebServices class attributes and methods
myDsl_AmazonWebServices_name: Property = Property(name="name", type=StringType)
myDsl_AmazonWebServices.attributes={myDsl_AmazonWebServices_name}

# myDsl_ReactServicesType class attributes and methods
myDsl_ReactServicesType_name: Property = Property(name="name", type=StringType)
myDsl_ReactServicesType.attributes={myDsl_ReactServicesType_name}

# myDsl_ReactLibraries class attributes and methods

# myDsl_ReactLibrary class attributes and methods
myDsl_ReactLibrary_name: Property = Property(name="name", type=StringType)
myDsl_ReactLibrary.attributes={myDsl_ReactLibrary_name}

# myDsl_ReactInfo class attributes and methods

# myDsl_ReactInformation class attributes and methods
myDsl_ReactInformation_name: Property = Property(name="name", type=StringType)
myDsl_ReactInformation.attributes={myDsl_ReactInformation_name}

# myDsl_Spring class attributes and methods
myDsl_Spring_name: Property = Property(name="name", type=StringType)
myDsl_Spring.attributes={myDsl_Spring_name}

# myDsl_PostgreSQL class attributes and methods
myDsl_PostgreSQL_name: Property = Property(name="name", type=StringType)
myDsl_PostgreSQL.attributes={myDsl_PostgreSQL_name}

# Relationships
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="myDsl_Entities", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity", type=myDsl_Entities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="myDsl_EObject6", type=myDsl_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entities5", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_EObject", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="myDsl_EObject2", type=myDsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Domain", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="myDsl_AppAccess", type=myDsl_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionalities11", type=myDsl_AppAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items12: BinaryAssociation = BinaryAssociation(
    name="items12",
    ends={
        Property(name="myDsl_AlbumManagement", type=myDsl_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionalities13", type=myDsl_AlbumManagement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements7: BinaryAssociation = BinaryAssociation(
    name="elements7",
    ends={
        Property(name="myDsl_Functionalities", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality", type=myDsl_Functionalities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions8: BinaryAssociation = BinaryAssociation(
    name="functions8",
    ends={
        Property(name="myDsl_ProfileManagement", type=myDsl_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionalities9", type=myDsl_ProfileManagement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items22: BinaryAssociation = BinaryAssociation(
    name="items22",
    ends={
        Property(name="myDsl_AlbumManagementFunctions", type=myDsl_AlbumManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AlbumManagement23", type=myDsl_AlbumManagementFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources14: BinaryAssociation = BinaryAssociation(
    name="resources14",
    ends={
        Property(name="myDsl_PhotoActions", type=myDsl_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionalities15", type=myDsl_PhotoActions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aditionals16: BinaryAssociation = BinaryAssociation(
    name="aditionals16",
    ends={
        Property(name="myDsl_LandingActions", type=myDsl_Functionalities, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionalities17", type=myDsl_LandingActions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="myDsl_ProfileManagementFunctions", type=myDsl_ProfileManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ProfileManagement19", type=myDsl_ProfileManagementFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items20: BinaryAssociation = BinaryAssociation(
    name="items20",
    ends={
        Property(name="myDsl_AppAccessFunctions", type=myDsl_AppAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AppAccess21", type=myDsl_AppAccessFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements29: BinaryAssociation = BinaryAssociation(
    name="elements29",
    ends={
        Property(name="myDsl_DomainRelations30", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="myDsl_EObject31", type=myDsl_DomainRelations, multiplicity=Multiplicity(1, 1))
    }
)
items24: BinaryAssociation = BinaryAssociation(
    name="items24",
    ends={
        Property(name="myDsl_PhotoActionsFunctions", type=myDsl_PhotoActions, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PhotoActions25", type=myDsl_PhotoActionsFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items26: BinaryAssociation = BinaryAssociation(
    name="items26",
    ends={
        Property(name="myDsl_LandingFunctions", type=myDsl_LandingActions, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LandingActions27", type=myDsl_LandingFunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements28: BinaryAssociation = BinaryAssociation(
    name="elements28",
    ends={
        Property(name="myDsl_DomainRelations", type=myDsl_DomainConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DomainConnection", type=myDsl_DomainRelations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements38: BinaryAssociation = BinaryAssociation(
    name="elements38",
    ends={
        Property(name="myDsl_EObject39", type=myDsl_PresentationLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PresentationLayer", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements32: BinaryAssociation = BinaryAssociation(
    name="elements32",
    ends={
        Property(name="myDsl_EObject33", type=myDsl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Architecture", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements34: BinaryAssociation = BinaryAssociation(
    name="elements34",
    ends={
        Property(name="myDsl_EObject35", type=myDsl_NTiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NTiers", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements36: BinaryAssociation = BinaryAssociation(
    name="elements36",
    ends={
        Property(name="myDsl_EObject37", type=myDsl_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Layer", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements47: BinaryAssociation = BinaryAssociation(
    name="elements47",
    ends={
        Property(name="myDsl_SegmentStructureContent", type=myDsl_SegmentStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SegmentStructure", type=myDsl_SegmentStructureContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements40: BinaryAssociation = BinaryAssociation(
    name="elements40",
    ends={
        Property(name="myDsl_PresentationSegments", type=myDsl_PresentationContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PresentationContent", type=myDsl_PresentationSegments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements41: BinaryAssociation = BinaryAssociation(
    name="elements41",
    ends={
        Property(name="myDsl_EObject42", type=myDsl_BusinessLogicLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BusinessLogicLayer", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements43: BinaryAssociation = BinaryAssociation(
    name="elements43",
    ends={
        Property(name="myDsl_BusinessLogicSegments", type=myDsl_BusinessLogicContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BusinessLogicContent", type=myDsl_BusinessLogicSegments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements44: BinaryAssociation = BinaryAssociation(
    name="elements44",
    ends={
        Property(name="myDsl_DataPersistenceContent", type=myDsl_DataPersistenceLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataPersistenceLayer", type=myDsl_DataPersistenceContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements45: BinaryAssociation = BinaryAssociation(
    name="elements45",
    ends={
        Property(name="myDsl_DataPersistenceSegments", type=myDsl_DataPersistenceContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataPersistenceContent46", type=myDsl_DataPersistenceSegments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layerorigin54: BinaryAssociation = BinaryAssociation(
    name="layerorigin54",
    ends={
        Property(name="myDsl_LayerSource", type=myDsl_LayerRelations, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LayerRelations", type=myDsl_LayerSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements48: BinaryAssociation = BinaryAssociation(
    name="elements48",
    ends={
        Property(name="myDsl_DirectoryContent", type=myDsl_SegmentStructureContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SegmentStructureContent49", type=myDsl_DirectoryContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements50: BinaryAssociation = BinaryAssociation(
    name="elements50",
    ends={
        Property(name="myDsl_EObject52", type=myDsl_DirectoryContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DirectoryContent51", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements53: BinaryAssociation = BinaryAssociation(
    name="elements53",
    ends={
        Property(name="myDsl_MultipleFile", type=myDsl_Directories, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Directories", type=myDsl_MultipleFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierorigin59: BinaryAssociation = BinaryAssociation(
    name="ntierorigin59",
    ends={
        Property(name="myDsl_NTierSource", type=myDsl_NTiersConnections, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NTiersConnections", type=myDsl_NTierSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layertarget55: BinaryAssociation = BinaryAssociation(
    name="layertarget55",
    ends={
        Property(name="myDsl_LayerTarget", type=myDsl_LayerRelations, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LayerRelations56", type=myDsl_LayerTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archcomponent57: BinaryAssociation = BinaryAssociation(
    name="archcomponent57",
    ends={
        Property(name="myDsl_EObject58", type=myDsl_ArchitectureComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArchitectureComponents", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reacts71: BinaryAssociation = BinaryAssociation(
    name="reacts71",
    ends={
        Property(name="myDsl_ReactModules", type=myDsl_React, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_React", type=myDsl_ReactModules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntiertarget60: BinaryAssociation = BinaryAssociation(
    name="ntiertarget60",
    ends={
        Property(name="myDsl_NTierTarget", type=myDsl_NTiersConnections, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NTiersConnections61", type=myDsl_NTierTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodules72: BinaryAssociation = BinaryAssociation(
    name="reactmodules72",
    ends={
        Property(name="myDsl_ReactSubModules", type=myDsl_ReactModules, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactModules73", type=myDsl_ReactSubModules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierconnection62: BinaryAssociation = BinaryAssociation(
    name="ntierconnection62",
    ends={
        Property(name="myDsl_NTiersRelations", type=myDsl_NTierSource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NTierSource63", type=myDsl_NTiersRelations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ntierconnection64: BinaryAssociation = BinaryAssociation(
    name="ntierconnection64",
    ends={
        Property(name="myDsl_NTiersRelations66", type=myDsl_NTierTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NTierTarget65", type=myDsl_NTiersRelations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements67: BinaryAssociation = BinaryAssociation(
    name="elements67",
    ends={
        Property(name="myDsl_Technologies", type=myDsl_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Technology", type=myDsl_Technologies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors68: BinaryAssociation = BinaryAssociation(
    name="factors68",
    ends={
        Property(name="myDsl_EObject70", type=myDsl_Technologies, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Technologies69", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies84: BinaryAssociation = BinaryAssociation(
    name="dependencies84",
    ends={
        Property(name="myDsl_SingleDependencies", type=myDsl_ReactDependenciesSubRules, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactDependenciesSubRules85", type=myDsl_SingleDependencies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies86: BinaryAssociation = BinaryAssociation(
    name="dependencies86",
    ends={
        Property(name="myDsl_EObject88", type=myDsl_SingleDependencies, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SingleDependencies87", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactmodules74: BinaryAssociation = BinaryAssociation(
    name="reactmodules74",
    ends={
        Property(name="myDsl_EObject76", type=myDsl_ReactSubModules, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactSubModules75", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies77: BinaryAssociation = BinaryAssociation(
    name="dependencies77",
    ends={
        Property(name="myDsl_ReactDependencies", type=myDsl_ReactConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactConfiguration", type=myDsl_ReactDependencies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations78: BinaryAssociation = BinaryAssociation(
    name="configurations78",
    ends={
        Property(name="myDsl_ReactConfigurations", type=myDsl_ReactConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactConfiguration79", type=myDsl_ReactConfigurations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies80: BinaryAssociation = BinaryAssociation(
    name="dependencies80",
    ends={
        Property(name="myDsl_ReactDependenciesRules", type=myDsl_ReactDependencies, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactDependencies81", type=myDsl_ReactDependenciesRules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies82: BinaryAssociation = BinaryAssociation(
    name="dependencies82",
    ends={
        Property(name="myDsl_ReactDependenciesSubRules", type=myDsl_ReactDependenciesRules, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactDependenciesRules83", type=myDsl_ReactDependenciesSubRules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logiccomponents94: BinaryAssociation = BinaryAssociation(
    name="logiccomponents94",
    ends={
        Property(name="myDsl_LogicContent", type=myDsl_ComponentsLogic, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ComponentsLogic95", type=myDsl_LogicContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations89: BinaryAssociation = BinaryAssociation(
    name="configurations89",
    ends={
        Property(name="myDsl_DOMConfigurations", type=myDsl_ReactConfigurations, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactConfigurations90", type=myDsl_DOMConfigurations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentslogic91: BinaryAssociation = BinaryAssociation(
    name="componentslogic91",
    ends={
        Property(name="myDsl_ComponentsLogic", type=myDsl_ReactComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactComponents", type=myDsl_ComponentsLogic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentsui92: BinaryAssociation = BinaryAssociation(
    name="componentsui92",
    ends={
        Property(name="myDsl_ComponentsUI", type=myDsl_ReactComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactComponents93", type=myDsl_ComponentsUI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentclass108: BinaryAssociation = BinaryAssociation(
    name="componentclass108",
    ends={
        Property(name="myDsl_EObject109", type=myDsl_ReactFunctions, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactFunctions", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logiccomponents96: BinaryAssociation = BinaryAssociation(
    name="logiccomponents96",
    ends={
        Property(name="myDsl_LogicStructure", type=myDsl_LogicContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LogicContent97", type=myDsl_LogicStructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logiccomponents98: BinaryAssociation = BinaryAssociation(
    name="logiccomponents98",
    ends={
        Property(name="myDsl_ComponentClass", type=myDsl_LogicStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LogicStructure99", type=myDsl_ComponentClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uicomponents100: BinaryAssociation = BinaryAssociation(
    name="uicomponents100",
    ends={
        Property(name="myDsl_UIContent", type=myDsl_ComponentsUI, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ComponentsUI101", type=myDsl_UIContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uicontent102: BinaryAssociation = BinaryAssociation(
    name="uicontent102",
    ends={
        Property(name="myDsl_ComponentClass104", type=myDsl_UIContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_UIContent103", type=myDsl_ComponentClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentclass105: BinaryAssociation = BinaryAssociation(
    name="componentclass105",
    ends={
        Property(name="myDsl_EObject107", type=myDsl_ComponentClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ComponentClass106", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactrelcontent113: BinaryAssociation = BinaryAssociation(
    name="reactrelcontent113",
    ends={
        Property(name="myDsl_ReactServicesRelation", type=myDsl_ReactActionsContent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactActionsContent114", type=myDsl_ReactServicesRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentclass110: BinaryAssociation = BinaryAssociation(
    name="componentclass110",
    ends={
        Property(name="myDsl_EObject111", type=myDsl_ReactConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactConstructor", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactactcontent112: BinaryAssociation = BinaryAssociation(
    name="reactactcontent112",
    ends={
        Property(name="myDsl_ReactActionsContent", type=myDsl_ReactActions, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactActions", type=myDsl_ReactActionsContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactrelationcontent115: BinaryAssociation = BinaryAssociation(
    name="reactrelationcontent115",
    ends={
        Property(name="myDsl_ReactServicesType", type=myDsl_ReactServicesRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactServicesRelation116", type=myDsl_ReactServicesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactlibraries117: BinaryAssociation = BinaryAssociation(
    name="reactlibraries117",
    ends={
        Property(name="myDsl_ReactLibrary", type=myDsl_ReactLibraries, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactLibraries", type=myDsl_ReactLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reactinformation118: BinaryAssociation = BinaryAssociation(
    name="reactinformation118",
    ends={
        Property(name="myDsl_ReactInformation", type=myDsl_ReactInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactInfo", type=myDsl_ReactInformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Entities, myDsl_Model, myDsl_EObject, myDsl_Domain, myDsl_Entity, myDsl_AppAccess, myDsl_AlbumManagement, myDsl_PhotoActions, myDsl_Photo, myDsl_Album, myDsl_UserDomain, myDsl_Functionality, myDsl_Functionalities, myDsl_ProfileManagement, myDsl_LandingActions, myDsl_ProfileManagementFunctions, myDsl_AppAccessFunctions, myDsl_AlbumManagementFunctions, myDsl_PhotoActionsFunctions, myDsl_LandingFunctions, myDsl_DomainConnection, myDsl_DomainRelations, myDsl_PresentationLayer, myDsl_Architecture, myDsl_NTiers, myDsl_Layer, myDsl_SegmentStructure, myDsl_SegmentStructureContent, myDsl_PresentationContent, myDsl_PresentationSegments, myDsl_BusinessLogicLayer, myDsl_BusinessLogicContent, myDsl_BusinessLogicSegments, myDsl_DataPersistenceLayer, myDsl_DataPersistenceContent, myDsl_DataPersistenceSegments, myDsl_LayerSource, myDsl_DirectoryContent, myDsl_Directories, myDsl_MultipleFile, myDsl_SingleFile, myDsl_LayerRelations, myDsl_NTierSource, myDsl_LayerTarget, myDsl_ArchitectureComponents, myDsl_FrontEnd, myDsl_BackEnd, myDsl_PersistenceDataComponent, myDsl_NTiersConnections, myDsl_NTierTarget, myDsl_ReactSubModules, myDsl_NTiersRelations, myDsl_Technology, myDsl_Technologies, myDsl_React, myDsl_ReactModules, myDsl_SingleDependencies, myDsl_ReactConfiguration, myDsl_ReactDependencies, myDsl_ReactConfigurations, myDsl_ReactDependenciesRules, myDsl_ReactDependenciesSubRules, myDsl_LogicContent, myDsl_PackageName, myDsl_PackageVersion, myDsl_DOMConfigurations, myDsl_ReactComponents, myDsl_ComponentsLogic, myDsl_ComponentsUI, myDsl_ReactFunctions, myDsl_LogicStructure, myDsl_ComponentClass, myDsl_UIContent, myDsl_ReactServicesRelation, myDsl_ReactConstructor, myDsl_State, myDsl_CoreFunctionsDeclaration, myDsl_Props, myDsl_ReactCoreFunctions, myDsl_ReactActions, myDsl_ReactActionsContent, myDsl_AmazonWebServices, myDsl_ReactServicesType, myDsl_ReactLibraries, myDsl_ReactLibrary, myDsl_ReactInfo, myDsl_ReactInformation, myDsl_Spring, myDsl_PostgreSQL},
    associations={elements3, elements4, elements0, elements1, elements10, items12, elements7, functions8, items22, resources14, aditionals16, items18, items20, elements29, items24, items26, elements28, elements38, elements32, elements34, elements36, elements47, elements40, elements41, elements43, elements44, elements45, layerorigin54, elements48, elements50, elements53, ntierorigin59, layertarget55, archcomponent57, reacts71, ntiertarget60, reactmodules72, ntierconnection62, ntierconnection64, elements67, factors68, dependencies84, dependencies86, reactmodules74, dependencies77, configurations78, dependencies80, dependencies82, logiccomponents94, configurations89, componentslogic91, componentsui92, componentclass108, logiccomponents96, logiccomponents98, uicomponents100, uicontent102, componentclass105, reactrelcontent113, componentclass110, reactactcontent112, reactrelationcontent115, reactlibraries117, reactinformation118},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)