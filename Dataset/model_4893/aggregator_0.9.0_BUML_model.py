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
AggregationType: Enumeration = Enumeration(
    name="AggregationType",
    literals={
            EnumerationLiteral(name="Stable"),
			EnumerationLiteral(name="Integration"),
			EnumerationLiteral(name="Nightly"),
			EnumerationLiteral(name="Maintenance"),
			EnumerationLiteral(name="Continuous"),
			EnumerationLiteral(name="Release")
    }
)

OperatingSystem: Enumeration = Enumeration(
    name="OperatingSystem",
    literals={
            EnumerationLiteral(name="Win32"),
			EnumerationLiteral(name="Linux"),
			EnumerationLiteral(name="MacOSX")
    }
)

WindowSystem: Enumeration = Enumeration(
    name="WindowSystem",
    literals={
            EnumerationLiteral(name="Win32"),
			EnumerationLiteral(name="GTK"),
			EnumerationLiteral(name="Carbon"),
			EnumerationLiteral(name="Cocoa")
    }
)

Architecture: Enumeration = Enumeration(
    name="Architecture",
    literals={
            EnumerationLiteral(name="X86"),
			EnumerationLiteral(name="PPC"),
			EnumerationLiteral(name="X86_64")
    }
)

PackedStrategy: Enumeration = Enumeration(
    name="PackedStrategy",
    literals={
            EnumerationLiteral(name="Copy"),
			EnumerationLiteral(name="Verify"),
			EnumerationLiteral(name="UnpackAsSibling"),
			EnumerationLiteral(name="Unpack"),
			EnumerationLiteral(name="Skip")
    }
)

InstallableUnitType: Enumeration = Enumeration(
    name="InstallableUnitType",
    literals={
            EnumerationLiteral(name="BUNDLE"),
			EnumerationLiteral(name="FEATURE"),
			EnumerationLiteral(name="PRODUCT"),
			EnumerationLiteral(name="CATEGORY"),
			EnumerationLiteral(name="FRAGMENT"),
			EnumerationLiteral(name="OTHER")
    }
)

StatusCode: Enumeration = Enumeration(
    name="StatusCode",
    literals={
            EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="BROKEN"),
			EnumerationLiteral(name="WAITING")
    }
)

# Classes
aggregator_MavenMapping = Class(name="aggregator::MavenMapping")
aggregator_MappedRepository = Class(name="aggregator::MappedRepository")
MetadataRepositoryReference = Class(name="MetadataRepositoryReference")
aggregator_Aggregator = Class(name="aggregator::Aggregator")
DescriptionProvider = Class(name="DescriptionProvider")
StatusProvider = Class(name="StatusProvider")
InfosProvider = Class(name="InfosProvider")
aggregator_Configuration = Class(name="aggregator::Configuration")
aggregator_Contribution = Class(name="aggregator::Contribution")
aggregator_Contact = Class(name="aggregator::Contact")
aggregator_CustomCategory = Class(name="aggregator::CustomCategory")
aggregator_MetadataRepositoryReference = Class(name="aggregator::MetadataRepositoryReference")
aggregator_Product = Class(name="aggregator::Product")
aggregator_Bundle = Class(name="aggregator::Bundle")
aggregator_Feature = Class(name="aggregator::Feature")
aggregator_Category = Class(name="aggregator::Category")
aggregator_MapRule = Class(name="aggregator::MapRule", is_abstract=True)
EnabledStatusProvider = Class(name="EnabledStatusProvider")
MappedUnit = Class(name="MappedUnit")
aggregator_ExclusionRule = Class(name="aggregator::ExclusionRule")
MapRule = Class(name="MapRule")
aggregator_ValidConfigurationsRule = Class(name="aggregator::ValidConfigurationsRule")
aggregator_MappedUnit = Class(name="aggregator::MappedUnit", is_abstract=True)
InstallableUnitReference = Class(name="InstallableUnitReference")
aggregator_Property = Class(name="aggregator::Property")
aggregator_EnabledStatusProvider = Class(name="aggregator::EnabledStatusProvider", is_abstract=True)
aggregator_InstallableUnitReference = Class(name="aggregator::InstallableUnitReference", is_abstract=True)
InstallableUnit = Class(name="InstallableUnit")
aggregator_StatusProvider = Class(name="aggregator::StatusProvider", is_abstract=True)
MetadataRepository = Class(name="MetadataRepository")
aggregator_Comparable = Class(name="aggregator::Comparable", is_abstract=True)
aggregator_LabelProvider = Class(name="aggregator::LabelProvider", is_abstract=True)
aggregator_DescriptionProvider = Class(name="aggregator::DescriptionProvider")
aggregator_MavenItem = Class(name="aggregator::MavenItem")
aggregator_ChildrenProvider = Class(name="aggregator::ChildrenProvider", is_abstract=True)
aggregator_Status = Class(name="aggregator::Status")
aggregator_InfosProvider = Class(name="aggregator::InfosProvider")
aggregator_p2_IArtifactKey = Class(name="aggregator::p2::IArtifactKey", is_abstract=True)
aggregator_p2_ICopyright = Class(name="aggregator::p2::ICopyright", is_abstract=True)
aggregator_p2_IInstallableUnit = Class(name="aggregator::p2::IInstallableUnit", is_abstract=True)
ITouchpointType = Class(name="ITouchpointType")
IUpdateDescriptor = Class(name="IUpdateDescriptor")
ILicense = Class(name="ILicense")
ICopyright = Class(name="ICopyright")
aggregator_p2_IInstallableUnitFragment = Class(name="aggregator::p2::IInstallableUnitFragment", is_abstract=True)
IInstallableUnit = Class(name="IInstallableUnit")
aggregator_p2_ILicense = Class(name="aggregator::p2::ILicense", is_abstract=True)
aggregator_p2_IProvidedCapability = Class(name="aggregator::p2::IProvidedCapability", is_abstract=True)
aggregator_p2_IRequiredCapability = Class(name="aggregator::p2::IRequiredCapability", is_abstract=True)
aggregator_p2_ITouchpointData = Class(name="aggregator::p2::ITouchpointData", is_abstract=True)
aggregator_p2_ITouchpointInstruction = Class(name="aggregator::p2::ITouchpointInstruction", is_abstract=True)
aggregator_p2_ITouchpointType = Class(name="aggregator::p2::ITouchpointType", is_abstract=True)
aggregator_p2_IUpdateDescriptor = Class(name="aggregator::p2::IUpdateDescriptor", is_abstract=True)
aggregator_p2_ArtifactKey = Class(name="aggregator::p2::ArtifactKey")
IArtifactKey = Class(name="IArtifactKey")
aggregator_p2_Copyright = Class(name="aggregator::p2::Copyright")
aggregator_p2_MetadataRepository = Class(name="aggregator::p2::MetadataRepository")
IMetadataRepository = Class(name="IMetadataRepository")
RepositoryReference = Class(name="RepositoryReference")
Property_ = Class(name="Property")
aggregator_p2_InstallableUnit = Class(name="aggregator::p2::InstallableUnit")
ProvidedCapability = Class(name="ProvidedCapability")
ArtifactKey = Class(name="ArtifactKey")
RequiredCapability = Class(name="RequiredCapability")
TouchpointData = Class(name="TouchpointData")
aggregator_p2_InstallableUnitFragment = Class(name="aggregator::p2::InstallableUnitFragment")
p2_InstallableUnit = Class(name="p2::InstallableUnit")
p2_IInstallableUnitFragment = Class(name="p2::IInstallableUnitFragment")
aggregator_p2_License = Class(name="aggregator::p2::License")
aggregator_p2_ProvidedCapability = Class(name="aggregator::p2::ProvidedCapability")
IProvidedCapability = Class(name="IProvidedCapability")
aggregator_p2_RequiredCapability = Class(name="aggregator::p2::RequiredCapability")
IRequiredCapability = Class(name="IRequiredCapability")
aggregator_p2_TouchpointData = Class(name="aggregator::p2::TouchpointData")
ITouchpointData = Class(name="ITouchpointData")
InstructionMap = Class(name="InstructionMap")
aggregator_p2_TouchpointInstruction = Class(name="aggregator::p2::TouchpointInstruction")
ITouchpointInstruction = Class(name="ITouchpointInstruction")
aggregator_p2_TouchpointType = Class(name="aggregator::p2::TouchpointType")
aggregator_p2_UpdateDescriptor = Class(name="aggregator::p2::UpdateDescriptor")
aggregator_p2_Property = Class(name="aggregator::p2::Property")
aggregator_p2_InstructionMap = Class(name="aggregator::p2::InstructionMap")
TouchpointInstruction = Class(name="TouchpointInstruction")
aggregator_p2_IQueryable = Class(name="aggregator::p2::IQueryable", is_abstract=True)
aggregator_p2_IMetadataRepository = Class(name="aggregator::p2::IMetadataRepository", is_abstract=True)
p2_IQueryable = Class(name="p2::IQueryable")
p2_IRepository = Class(name="p2::IRepository")
Miscellaneous = Class(name="Miscellaneous")
aggregator_p2_IRepository = Class(name="aggregator::p2::IRepository", is_abstract=True)
IAdaptable = Class(name="IAdaptable")
aggregator_p2_RepositoryReference = Class(name="aggregator::p2::RepositoryReference")
aggregator_p2_IAdaptable = Class(name="aggregator::p2::IAdaptable", is_abstract=True)
aggregator_p2view_MetadataRepositoryStructuredView = Class(name="aggregator::p2view::MetadataRepositoryStructuredView")
InstallableUnits = Class(name="InstallableUnits")
Properties = Class(name="Properties")
aggregator_p2view_InstallableUnits = Class(name="aggregator::p2view::InstallableUnits")
Categories = Class(name="Categories")
Features = Class(name="Features")
Products = Class(name="Products")
Bundles = Class(name="Bundles")
Fragments = Class(name="Fragments")
aggregator_p2view_Categories = Class(name="aggregator::p2view::Categories")
Category = Class(name="Category")
aggregator_p2view_Features = Class(name="aggregator::p2view::Features")
Feature = Class(name="Feature")
aggregator_p2view_Products = Class(name="aggregator::p2view::Products")
Product = Class(name="Product")
aggregator_p2view_Bundles = Class(name="aggregator::p2view::Bundles")
Bundle = Class(name="Bundle")
aggregator_p2view_Fragments = Class(name="aggregator::p2view::Fragments")
Fragment = Class(name="Fragment")
aggregator_p2view_Miscellaneous = Class(name="aggregator::p2view::Miscellaneous")
OtherIU = Class(name="OtherIU")
aggregator_p2view_IUPresentation = Class(name="aggregator::p2view::IUPresentation", is_abstract=True)
aggregator_p2view_IUPresentationWithDetails = Class(name="aggregator::p2view::IUPresentationWithDetails", is_abstract=True)
p2view_IUPresentation = Class(name="p2view::IUPresentation")
p2view_IUDetails = Class(name="p2view::IUDetails")
aggregator_p2view_Category = Class(name="aggregator::p2view::Category")
IUPresentation = Class(name="IUPresentation")
IUDetails = Class(name="IUDetails")
aggregator_p2view_Feature = Class(name="aggregator::p2view::Feature")
IUPresentationWithDetails = Class(name="IUPresentationWithDetails")
aggregator_p2view_Product = Class(name="aggregator::p2view::Product")
aggregator_p2view_Bundle = Class(name="aggregator::p2view::Bundle")
aggregator_p2view_Fragment = Class(name="aggregator::p2view::Fragment")
aggregator_p2view_OtherIU = Class(name="aggregator::p2view::OtherIU")
aggregator_p2view_Properties = Class(name="aggregator::p2view::Properties")
p2view_aggregator_Property = Class(name="p2view::aggregator::Property")
aggregator_p2view_RequiredCapabilities = Class(name="aggregator::p2view::RequiredCapabilities")
RequiredCapabilityWrapper = Class(name="RequiredCapabilityWrapper")
aggregator_p2view_ProvidedCapabilities = Class(name="aggregator::p2view::ProvidedCapabilities")
ProvidedCapabilityWrapper = Class(name="ProvidedCapabilityWrapper")
aggregator_p2view_Touchpoints = Class(name="aggregator::p2view::Touchpoints")
aggregator_p2view_IUDetails = Class(name="aggregator::p2view::IUDetails")
RequiredCapabilities = Class(name="RequiredCapabilities")
ProvidedCapabilities = Class(name="ProvidedCapabilities")
Touchpoints = Class(name="Touchpoints")
aggregator_p2view_RequiredCapabilityWrapper = Class(name="aggregator::p2view::RequiredCapabilityWrapper")
p2_IRequiredCapability = Class(name="p2::IRequiredCapability")
LabelProvider = Class(name="LabelProvider")
aggregator_p2view_ProvidedCapabilityWrapper = Class(name="aggregator::p2view::ProvidedCapabilityWrapper")
p2_IProvidedCapability = Class(name="p2::IProvidedCapability")

# aggregator_MavenMapping class attributes and methods
aggregator_MavenMapping_namePattern: Property = Property(name="namePattern", type=StringType)
aggregator_MavenMapping_groupId: Property = Property(name="groupId", type=StringType)
aggregator_MavenMapping_artifactId: Property = Property(name="artifactId", type=StringType)
aggregator_MavenMapping_m_map: Method = Method(name="map", parameters={Parameter(name='installableUnitID')}, type=StringType)
aggregator_MavenMapping.attributes={aggregator_MavenMapping_namePattern, aggregator_MavenMapping_groupId, aggregator_MavenMapping_artifactId}
aggregator_MavenMapping.methods={aggregator_MavenMapping_m_map}

# aggregator_MappedRepository class attributes and methods
aggregator_MappedRepository_mirrorArtifacts: Property = Property(name="mirrorArtifacts", type=BooleanType)
aggregator_MappedRepository_categoryPrefix: Property = Property(name="categoryPrefix", type=StringType)
aggregator_MappedRepository_m_getUnits: Method = Method(name="getUnits", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_MappedRepository_m_isMapExclusive: Method = Method(name="isMapExclusive", parameters={}, type=BooleanType)
aggregator_MappedRepository.attributes={aggregator_MappedRepository_mirrorArtifacts, aggregator_MappedRepository_categoryPrefix}
aggregator_MappedRepository.methods={aggregator_MappedRepository_m_getUnits, aggregator_MappedRepository_m_isMapExclusive}

# MetadataRepositoryReference class attributes and methods

# aggregator_Aggregator class attributes and methods
aggregator_Aggregator_label: Property = Property(name="label", type=StringType)
aggregator_Aggregator_buildRoot: Property = Property(name="buildRoot", type=StringType)
aggregator_Aggregator_packedStrategy: Property = Property(name="packedStrategy", type=StringType)
aggregator_Aggregator_sendmail: Property = Property(name="sendmail", type=BooleanType)
aggregator_Aggregator_type: Property = Property(name="type", type=StringType)
aggregator_Aggregator_mavenResult: Property = Property(name="mavenResult", type=BooleanType)
aggregator_Aggregator_m_getContributions: Method = Method(name="getContributions", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Aggregator_m_getValidationRepositories: Method = Method(name="getValidationRepositories", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Aggregator_m_getAllMetadataRepositoryReferences: Method = Method(name="getAllMetadataRepositoryReferences", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Aggregator.attributes={aggregator_Aggregator_packedStrategy, aggregator_Aggregator_type, aggregator_Aggregator_label, aggregator_Aggregator_buildRoot, aggregator_Aggregator_sendmail, aggregator_Aggregator_mavenResult}
aggregator_Aggregator.methods={aggregator_Aggregator_m_getContributions, aggregator_Aggregator_m_getValidationRepositories, aggregator_Aggregator_m_getAllMetadataRepositoryReferences}

# DescriptionProvider class attributes and methods

# StatusProvider class attributes and methods

# InfosProvider class attributes and methods

# aggregator_Configuration class attributes and methods
aggregator_Configuration_operatingSystem: Property = Property(name="operatingSystem", type=StringType)
aggregator_Configuration_windowSystem: Property = Property(name="windowSystem", type=StringType)
aggregator_Configuration_architecture: Property = Property(name="architecture", type=StringType)
aggregator_Configuration_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
aggregator_Configuration_m_getOSGiEnvironmentString: Method = Method(name="getOSGiEnvironmentString", parameters={}, type=StringType)
aggregator_Configuration.attributes={aggregator_Configuration_architecture, aggregator_Configuration_operatingSystem, aggregator_Configuration_windowSystem}
aggregator_Configuration.methods={aggregator_Configuration_m_getOSGiEnvironmentString, aggregator_Configuration_m_getName}

# aggregator_Contribution class attributes and methods
aggregator_Contribution_label: Property = Property(name="label", type=StringType)
aggregator_Contribution_m_getRepositories: Method = Method(name="getRepositories", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Contribution_m_getAllMavenMappings: Method = Method(name="getAllMavenMappings", parameters={}, type=StringType)
aggregator_Contribution.attributes={aggregator_Contribution_label}
aggregator_Contribution.methods={aggregator_Contribution_m_getAllMavenMappings, aggregator_Contribution_m_getRepositories}

# aggregator_Contact class attributes and methods
aggregator_Contact_name: Property = Property(name="name", type=StringType)
aggregator_Contact_email: Property = Property(name="email", type=StringType)
aggregator_Contact.attributes={aggregator_Contact_name, aggregator_Contact_email}

# aggregator_CustomCategory class attributes and methods
aggregator_CustomCategory_identifier: Property = Property(name="identifier", type=StringType)
aggregator_CustomCategory_label: Property = Property(name="label", type=StringType)
aggregator_CustomCategory_description: Property = Property(name="description", type=StringType)
aggregator_CustomCategory.attributes={aggregator_CustomCategory_identifier, aggregator_CustomCategory_label, aggregator_CustomCategory_description}

# aggregator_MetadataRepositoryReference class attributes and methods
aggregator_MetadataRepositoryReference_location: Property = Property(name="location", type=StringType)
aggregator_MetadataRepositoryReference_nature: Property = Property(name="nature", type=StringType)
aggregator_MetadataRepositoryReference_m_getAggregator: Method = Method(name="getAggregator", parameters={}, type=StringType)
aggregator_MetadataRepositoryReference_m_getMetadataRepository: Method = Method(name="getMetadataRepository", parameters={Parameter(name='forceResolve')}, type=StringType)
aggregator_MetadataRepositoryReference_m_isBranchEnabled: Method = Method(name="isBranchEnabled", parameters={}, type=BooleanType)
aggregator_MetadataRepositoryReference_m_getResolvedLocation: Method = Method(name="getResolvedLocation", parameters={}, type=StringType)
aggregator_MetadataRepositoryReference_m_startRepositoryLoad: Method = Method(name="startRepositoryLoad", parameters={Parameter(name='forceReload')})
aggregator_MetadataRepositoryReference_m_cancelRepositoryLoad: Method = Method(name="cancelRepositoryLoad", parameters={})
aggregator_MetadataRepositoryReference_m_onRepositoryLoad: Method = Method(name="onRepositoryLoad", parameters={})
aggregator_MetadataRepositoryReference.attributes={aggregator_MetadataRepositoryReference_location, aggregator_MetadataRepositoryReference_nature}
aggregator_MetadataRepositoryReference.methods={aggregator_MetadataRepositoryReference_m_onRepositoryLoad, aggregator_MetadataRepositoryReference_m_startRepositoryLoad, aggregator_MetadataRepositoryReference_m_cancelRepositoryLoad, aggregator_MetadataRepositoryReference_m_getMetadataRepository, aggregator_MetadataRepositoryReference_m_getResolvedLocation, aggregator_MetadataRepositoryReference_m_isBranchEnabled, aggregator_MetadataRepositoryReference_m_getAggregator}

# aggregator_Product class attributes and methods

# aggregator_Bundle class attributes and methods

# aggregator_Feature class attributes and methods

# aggregator_Category class attributes and methods
aggregator_Category_labelOverride: Property = Property(name="labelOverride", type=StringType)
aggregator_Category.attributes={aggregator_Category_labelOverride}

# aggregator_MapRule class attributes and methods

# EnabledStatusProvider class attributes and methods

# MappedUnit class attributes and methods

# aggregator_ExclusionRule class attributes and methods

# MapRule class attributes and methods

# aggregator_ValidConfigurationsRule class attributes and methods

# aggregator_MappedUnit class attributes and methods

# InstallableUnitReference class attributes and methods

# aggregator_Property class attributes and methods
aggregator_Property_key: Property = Property(name="key", type=StringType)
aggregator_Property_value: Property = Property(name="value", type=StringType)
aggregator_Property.attributes={aggregator_Property_value, aggregator_Property_key}

# aggregator_EnabledStatusProvider class attributes and methods
aggregator_EnabledStatusProvider_enabled: Property = Property(name="enabled", type=BooleanType)
aggregator_EnabledStatusProvider.attributes={aggregator_EnabledStatusProvider_enabled}

# aggregator_InstallableUnitReference class attributes and methods
aggregator_InstallableUnitReference_m_getInstallableUnit: Method = Method(name="getInstallableUnit", parameters={Parameter(name='forceResolve')}, type=StringType)
aggregator_InstallableUnitReference_m_isMappedRepositoryBroken: Method = Method(name="isMappedRepositoryBroken", parameters={}, type=BooleanType)
aggregator_InstallableUnitReference_m_isBranchEnabled: Method = Method(name="isBranchEnabled", parameters={}, type=BooleanType)
aggregator_InstallableUnitReference.methods={aggregator_InstallableUnitReference_m_getInstallableUnit, aggregator_InstallableUnitReference_m_isBranchEnabled, aggregator_InstallableUnitReference_m_isMappedRepositoryBroken}

# InstallableUnit class attributes and methods

# aggregator_StatusProvider class attributes and methods

# MetadataRepository class attributes and methods

# aggregator_Comparable class attributes and methods

# aggregator_LabelProvider class attributes and methods
aggregator_LabelProvider_label: Property = Property(name="label", type=StringType)
aggregator_LabelProvider.attributes={aggregator_LabelProvider_label}

# aggregator_DescriptionProvider class attributes and methods
aggregator_DescriptionProvider_description: Property = Property(name="description", type=StringType)
aggregator_DescriptionProvider.attributes={aggregator_DescriptionProvider_description}

# aggregator_MavenItem class attributes and methods
aggregator_MavenItem_groupId: Property = Property(name="groupId", type=StringType)
aggregator_MavenItem_artifactId: Property = Property(name="artifactId", type=StringType)
aggregator_MavenItem.attributes={aggregator_MavenItem_groupId, aggregator_MavenItem_artifactId}

# aggregator_ChildrenProvider class attributes and methods

# aggregator_Status class attributes and methods
aggregator_Status_message: Property = Property(name="message", type=StringType)
aggregator_Status_code: Property = Property(name="code", type=StringType)
aggregator_Status.attributes={aggregator_Status_code, aggregator_Status_message}

# aggregator_InfosProvider class attributes and methods
aggregator_InfosProvider_errors: Property = Property(name="errors", type=StringType)
aggregator_InfosProvider_warnings: Property = Property(name="warnings", type=StringType)
aggregator_InfosProvider_infos: Property = Property(name="infos", type=StringType)
aggregator_InfosProvider.attributes={aggregator_InfosProvider_infos, aggregator_InfosProvider_errors, aggregator_InfosProvider_warnings}

# aggregator_p2_IArtifactKey class attributes and methods
aggregator_p2_IArtifactKey_classifier: Property = Property(name="classifier", type=StringType)
aggregator_p2_IArtifactKey_id: Property = Property(name="id", type=StringType)
aggregator_p2_IArtifactKey_version: Property = Property(name="version", type=StringType)
aggregator_p2_IArtifactKey_m_toExternalForm: Method = Method(name="toExternalForm", parameters={}, type=StringType)
aggregator_p2_IArtifactKey.attributes={aggregator_p2_IArtifactKey_version, aggregator_p2_IArtifactKey_classifier, aggregator_p2_IArtifactKey_id}
aggregator_p2_IArtifactKey.methods={aggregator_p2_IArtifactKey_m_toExternalForm}

# aggregator_p2_ICopyright class attributes and methods
aggregator_p2_ICopyright_location: Property = Property(name="location", type=StringType)
aggregator_p2_ICopyright_body: Property = Property(name="body", type=StringType)
aggregator_p2_ICopyright.attributes={aggregator_p2_ICopyright_body, aggregator_p2_ICopyright_location}

# aggregator_p2_IInstallableUnit class attributes and methods
aggregator_p2_IInstallableUnit_filter: Property = Property(name="filter", type=StringType)
aggregator_p2_IInstallableUnit_id: Property = Property(name="id", type=StringType)
aggregator_p2_IInstallableUnit_version: Property = Property(name="version", type=StringType)
aggregator_p2_IInstallableUnit_resolved: Property = Property(name="resolved", type=BooleanType)
aggregator_p2_IInstallableUnit_singleton: Property = Property(name="singleton", type=BooleanType)
aggregator_p2_IInstallableUnit_m_getArtifacts: Method = Method(name="getArtifacts", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_getFragments: Method = Method(name="getFragments", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key')}, type=StringType)
aggregator_p2_IInstallableUnit_m_getProperties: Method = Method(name="getProperties", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_getMetaRequiredCapabilities: Method = Method(name="getMetaRequiredCapabilities", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_getRequiredCapabilities: Method = Method(name="getRequiredCapabilities", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_getProvidedCapabilities: Method = Method(name="getProvidedCapabilities", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_getTouchpointData: Method = Method(name="getTouchpointData", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit_m_isFragment: Method = Method(name="isFragment", parameters={}, type=BooleanType)
aggregator_p2_IInstallableUnit_m_satisfies: Method = Method(name="satisfies", parameters={Parameter(name='candidate')}, type=BooleanType)
aggregator_p2_IInstallableUnit_m_unresolved: Method = Method(name="unresolved", parameters={}, type=StringType)
aggregator_p2_IInstallableUnit.attributes={aggregator_p2_IInstallableUnit_version, aggregator_p2_IInstallableUnit_id, aggregator_p2_IInstallableUnit_resolved, aggregator_p2_IInstallableUnit_singleton, aggregator_p2_IInstallableUnit_filter}
aggregator_p2_IInstallableUnit.methods={aggregator_p2_IInstallableUnit_m_unresolved, aggregator_p2_IInstallableUnit_m_getTouchpointData, aggregator_p2_IInstallableUnit_m_getArtifacts, aggregator_p2_IInstallableUnit_m_isFragment, aggregator_p2_IInstallableUnit_m_satisfies, aggregator_p2_IInstallableUnit_m_getMetaRequiredCapabilities, aggregator_p2_IInstallableUnit_m_getProperties, aggregator_p2_IInstallableUnit_m_getFragments, aggregator_p2_IInstallableUnit_m_getRequiredCapabilities, aggregator_p2_IInstallableUnit_m_getProvidedCapabilities, aggregator_p2_IInstallableUnit_m_getProperty}

# ITouchpointType class attributes and methods

# IUpdateDescriptor class attributes and methods

# ILicense class attributes and methods

# ICopyright class attributes and methods

# aggregator_p2_IInstallableUnitFragment class attributes and methods
aggregator_p2_IInstallableUnitFragment_m_getHost: Method = Method(name="getHost", parameters={}, type=StringType)
aggregator_p2_IInstallableUnitFragment.methods={aggregator_p2_IInstallableUnitFragment_m_getHost}

# IInstallableUnit class attributes and methods

# aggregator_p2_ILicense class attributes and methods
aggregator_p2_ILicense_location: Property = Property(name="location", type=StringType)
aggregator_p2_ILicense_body: Property = Property(name="body", type=StringType)
aggregator_p2_ILicense_digest: Property = Property(name="digest", type=StringType)
aggregator_p2_ILicense.attributes={aggregator_p2_ILicense_digest, aggregator_p2_ILicense_body, aggregator_p2_ILicense_location}

# aggregator_p2_IProvidedCapability class attributes and methods
aggregator_p2_IProvidedCapability_name: Property = Property(name="name", type=StringType)
aggregator_p2_IProvidedCapability_namespace: Property = Property(name="namespace", type=StringType)
aggregator_p2_IProvidedCapability_version: Property = Property(name="version", type=StringType)
aggregator_p2_IProvidedCapability_m_satisfies: Method = Method(name="satisfies", parameters={Parameter(name='requirement')}, type=BooleanType)
aggregator_p2_IProvidedCapability.attributes={aggregator_p2_IProvidedCapability_name, aggregator_p2_IProvidedCapability_version, aggregator_p2_IProvidedCapability_namespace}
aggregator_p2_IProvidedCapability.methods={aggregator_p2_IProvidedCapability_m_satisfies}

# aggregator_p2_IRequiredCapability class attributes and methods
aggregator_p2_IRequiredCapability_filter: Property = Property(name="filter", type=StringType)
aggregator_p2_IRequiredCapability_name: Property = Property(name="name", type=StringType)
aggregator_p2_IRequiredCapability_namespace: Property = Property(name="namespace", type=StringType)
aggregator_p2_IRequiredCapability_range: Property = Property(name="range", type=StringType)
aggregator_p2_IRequiredCapability_negation: Property = Property(name="negation", type=BooleanType)
aggregator_p2_IRequiredCapability_selectorList: Property = Property(name="selectorList", type=StringType)
aggregator_p2_IRequiredCapability_multiple: Property = Property(name="multiple", type=BooleanType)
aggregator_p2_IRequiredCapability_optional: Property = Property(name="optional", type=BooleanType)
aggregator_p2_IRequiredCapability_greedy: Property = Property(name="greedy", type=BooleanType)
aggregator_p2_IRequiredCapability_m_getSelectors: Method = Method(name="getSelectors", parameters={}, type=StringType)
aggregator_p2_IRequiredCapability_m_setSelectors: Method = Method(name="setSelectors", parameters={Parameter(name='selectors')})
aggregator_p2_IRequiredCapability_m_satisfiedBy: Method = Method(name="satisfiedBy", parameters={Parameter(name='capability')}, type=BooleanType)
aggregator_p2_IRequiredCapability.attributes={aggregator_p2_IRequiredCapability_multiple, aggregator_p2_IRequiredCapability_selectorList, aggregator_p2_IRequiredCapability_negation, aggregator_p2_IRequiredCapability_optional, aggregator_p2_IRequiredCapability_greedy, aggregator_p2_IRequiredCapability_namespace, aggregator_p2_IRequiredCapability_range, aggregator_p2_IRequiredCapability_filter, aggregator_p2_IRequiredCapability_name}
aggregator_p2_IRequiredCapability.methods={aggregator_p2_IRequiredCapability_m_setSelectors, aggregator_p2_IRequiredCapability_m_getSelectors, aggregator_p2_IRequiredCapability_m_satisfiedBy}

# aggregator_p2_ITouchpointData class attributes and methods
aggregator_p2_ITouchpointData_m_getInstruction: Method = Method(name="getInstruction", parameters={Parameter(name='instructionKey')}, type=StringType)
aggregator_p2_ITouchpointData_m_getInstructions: Method = Method(name="getInstructions", parameters={}, type=StringType)
aggregator_p2_ITouchpointData.methods={aggregator_p2_ITouchpointData_m_getInstructions, aggregator_p2_ITouchpointData_m_getInstruction}

# aggregator_p2_ITouchpointInstruction class attributes and methods
aggregator_p2_ITouchpointInstruction_body: Property = Property(name="body", type=StringType)
aggregator_p2_ITouchpointInstruction_importAttribute: Property = Property(name="importAttribute", type=StringType)
aggregator_p2_ITouchpointInstruction.attributes={aggregator_p2_ITouchpointInstruction_importAttribute, aggregator_p2_ITouchpointInstruction_body}

# aggregator_p2_ITouchpointType class attributes and methods
aggregator_p2_ITouchpointType_id: Property = Property(name="id", type=StringType)
aggregator_p2_ITouchpointType_version: Property = Property(name="version", type=StringType)
aggregator_p2_ITouchpointType.attributes={aggregator_p2_ITouchpointType_version, aggregator_p2_ITouchpointType_id}

# aggregator_p2_IUpdateDescriptor class attributes and methods
aggregator_p2_IUpdateDescriptor_id: Property = Property(name="id", type=StringType)
aggregator_p2_IUpdateDescriptor_range: Property = Property(name="range", type=StringType)
aggregator_p2_IUpdateDescriptor_description: Property = Property(name="description", type=StringType)
aggregator_p2_IUpdateDescriptor_severity: Property = Property(name="severity", type=IntegerType)
aggregator_p2_IUpdateDescriptor_m_isUpdateOf: Method = Method(name="isUpdateOf", parameters={Parameter(name='iu')}, type=BooleanType)
aggregator_p2_IUpdateDescriptor.attributes={aggregator_p2_IUpdateDescriptor_severity, aggregator_p2_IUpdateDescriptor_range, aggregator_p2_IUpdateDescriptor_id, aggregator_p2_IUpdateDescriptor_description}
aggregator_p2_IUpdateDescriptor.methods={aggregator_p2_IUpdateDescriptor_m_isUpdateOf}

# aggregator_p2_ArtifactKey class attributes and methods

# IArtifactKey class attributes and methods

# aggregator_p2_Copyright class attributes and methods

# aggregator_p2_MetadataRepository class attributes and methods

# IMetadataRepository class attributes and methods

# RepositoryReference class attributes and methods

# Property class attributes and methods

# aggregator_p2_InstallableUnit class attributes and methods
aggregator_p2_InstallableUnit_m_compareTo: Method = Method(name="compareTo", parameters={Parameter(name='other')}, type=IntegerType)
aggregator_p2_InstallableUnit.methods={aggregator_p2_InstallableUnit_m_compareTo}

# ProvidedCapability class attributes and methods

# ArtifactKey class attributes and methods

# RequiredCapability class attributes and methods

# TouchpointData class attributes and methods

# aggregator_p2_InstallableUnitFragment class attributes and methods

# p2_InstallableUnit class attributes and methods

# p2_IInstallableUnitFragment class attributes and methods

# aggregator_p2_License class attributes and methods

# aggregator_p2_ProvidedCapability class attributes and methods

# IProvidedCapability class attributes and methods

# aggregator_p2_RequiredCapability class attributes and methods

# IRequiredCapability class attributes and methods

# aggregator_p2_TouchpointData class attributes and methods

# ITouchpointData class attributes and methods

# InstructionMap class attributes and methods

# aggregator_p2_TouchpointInstruction class attributes and methods

# ITouchpointInstruction class attributes and methods

# aggregator_p2_TouchpointType class attributes and methods

# aggregator_p2_UpdateDescriptor class attributes and methods

# aggregator_p2_Property class attributes and methods
aggregator_p2_Property_key: Property = Property(name="key", type=StringType)
aggregator_p2_Property_value: Property = Property(name="value", type=StringType)
aggregator_p2_Property.attributes={aggregator_p2_Property_key, aggregator_p2_Property_value}

# aggregator_p2_InstructionMap class attributes and methods
aggregator_p2_InstructionMap_key: Property = Property(name="key", type=StringType)
aggregator_p2_InstructionMap.attributes={aggregator_p2_InstructionMap_key}

# TouchpointInstruction class attributes and methods

# aggregator_p2_IQueryable class attributes and methods
aggregator_p2_IQueryable_m_query: Method = Method(name="query", parameters={Parameter(name='progress'), Parameter(name='collector'), Parameter(name='query')}, type=StringType)
aggregator_p2_IQueryable.methods={aggregator_p2_IQueryable_m_query}

# aggregator_p2_IMetadataRepository class attributes and methods
aggregator_p2_IMetadataRepository_m_removeInstallableUnits: Method = Method(name="removeInstallableUnits", parameters={Parameter(name='query'), Parameter(name='monitor')}, type=BooleanType)
aggregator_p2_IMetadataRepository_m_removeAll: Method = Method(name="removeAll", parameters={})
aggregator_p2_IMetadataRepository_m_addInstallableUnits: Method = Method(name="addInstallableUnits", parameters={Parameter(name='installableUnits')})
aggregator_p2_IMetadataRepository_m_addReference: Method = Method(name="addReference", parameters={Parameter(name='type'), Parameter(name='options'), Parameter(name='location'), Parameter(name='nickname')})
aggregator_p2_IMetadataRepository.methods={aggregator_p2_IMetadataRepository_m_addInstallableUnits, aggregator_p2_IMetadataRepository_m_removeAll, aggregator_p2_IMetadataRepository_m_removeInstallableUnits, aggregator_p2_IMetadataRepository_m_addReference}

# p2_IQueryable class attributes and methods

# p2_IRepository class attributes and methods

# Miscellaneous class attributes and methods

# aggregator_p2_IRepository class attributes and methods
aggregator_p2_IRepository_location: Property = Property(name="location", type=StringType)
aggregator_p2_IRepository_name: Property = Property(name="name", type=StringType)
aggregator_p2_IRepository_type: Property = Property(name="type", type=StringType)
aggregator_p2_IRepository_version: Property = Property(name="version", type=StringType)
aggregator_p2_IRepository_description: Property = Property(name="description", type=StringType)
aggregator_p2_IRepository_provider: Property = Property(name="provider", type=StringType)
aggregator_p2_IRepository_modifiable: Property = Property(name="modifiable", type=BooleanType)
aggregator_p2_IRepository_m_getProperties: Method = Method(name="getProperties", parameters={}, type=StringType)
aggregator_p2_IRepository_m_setProperty: Method = Method(name="setProperty", parameters={Parameter(name='value'), Parameter(name='key')}, type=StringType)
aggregator_p2_IRepository.attributes={aggregator_p2_IRepository_location, aggregator_p2_IRepository_description, aggregator_p2_IRepository_modifiable, aggregator_p2_IRepository_version, aggregator_p2_IRepository_name, aggregator_p2_IRepository_provider, aggregator_p2_IRepository_type}
aggregator_p2_IRepository.methods={aggregator_p2_IRepository_m_getProperties, aggregator_p2_IRepository_m_setProperty}

# IAdaptable class attributes and methods

# aggregator_p2_RepositoryReference class attributes and methods
aggregator_p2_RepositoryReference_location: Property = Property(name="location", type=StringType)
aggregator_p2_RepositoryReference_type: Property = Property(name="type", type=IntegerType)
aggregator_p2_RepositoryReference_options: Property = Property(name="options", type=IntegerType)
aggregator_p2_RepositoryReference_nickname: Property = Property(name="nickname", type=StringType)
aggregator_p2_RepositoryReference.attributes={aggregator_p2_RepositoryReference_options, aggregator_p2_RepositoryReference_nickname, aggregator_p2_RepositoryReference_type, aggregator_p2_RepositoryReference_location}

# aggregator_p2_IAdaptable class attributes and methods
aggregator_p2_IAdaptable_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
aggregator_p2_IAdaptable.methods={aggregator_p2_IAdaptable_m_getAdapter}

# aggregator_p2view_MetadataRepositoryStructuredView class attributes and methods
aggregator_p2view_MetadataRepositoryStructuredView_name: Property = Property(name="name", type=StringType)
aggregator_p2view_MetadataRepositoryStructuredView_loaded: Property = Property(name="loaded", type=BooleanType)
aggregator_p2view_MetadataRepositoryStructuredView.attributes={aggregator_p2view_MetadataRepositoryStructuredView_loaded, aggregator_p2view_MetadataRepositoryStructuredView_name}

# InstallableUnits class attributes and methods

# Properties class attributes and methods

# aggregator_p2view_InstallableUnits class attributes and methods
aggregator_p2view_InstallableUnits_m_getNotNullCategoryContainer: Method = Method(name="getNotNullCategoryContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullProductContainer: Method = Method(name="getNotNullProductContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullMiscellaneousContainer: Method = Method(name="getNotNullMiscellaneousContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits.methods={aggregator_p2view_InstallableUnits_m_getNotNullBundleContainer, aggregator_p2view_InstallableUnits_m_getNotNullFragmentContainer, aggregator_p2view_InstallableUnits_m_getNotNullFeatureContainer, aggregator_p2view_InstallableUnits_m_getNotNullCategoryContainer, aggregator_p2view_InstallableUnits_m_getNotNullProductContainer, aggregator_p2view_InstallableUnits_m_getNotNullMiscellaneousContainer}

# Categories class attributes and methods

# Features class attributes and methods

# Products class attributes and methods

# Bundles class attributes and methods

# Fragments class attributes and methods

# aggregator_p2view_Categories class attributes and methods

# Category class attributes and methods

# aggregator_p2view_Features class attributes and methods

# Feature class attributes and methods

# aggregator_p2view_Products class attributes and methods

# Product class attributes and methods

# aggregator_p2view_Bundles class attributes and methods

# Bundle class attributes and methods

# aggregator_p2view_Fragments class attributes and methods

# Fragment class attributes and methods

# aggregator_p2view_Miscellaneous class attributes and methods

# OtherIU class attributes and methods

# aggregator_p2view_IUPresentation class attributes and methods
aggregator_p2view_IUPresentation_id: Property = Property(name="id", type=StringType)
aggregator_p2view_IUPresentation_version: Property = Property(name="version", type=StringType)
aggregator_p2view_IUPresentation_name: Property = Property(name="name", type=StringType)
aggregator_p2view_IUPresentation_label: Property = Property(name="label", type=StringType)
aggregator_p2view_IUPresentation_description: Property = Property(name="description", type=StringType)
aggregator_p2view_IUPresentation_type: Property = Property(name="type", type=StringType)
aggregator_p2view_IUPresentation.attributes={aggregator_p2view_IUPresentation_type, aggregator_p2view_IUPresentation_version, aggregator_p2view_IUPresentation_label, aggregator_p2view_IUPresentation_name, aggregator_p2view_IUPresentation_id, aggregator_p2view_IUPresentation_description}

# aggregator_p2view_IUPresentationWithDetails class attributes and methods
aggregator_p2view_IUPresentationWithDetails_detailsResolved: Property = Property(name="detailsResolved", type=StringType)
aggregator_p2view_IUPresentationWithDetails.attributes={aggregator_p2view_IUPresentationWithDetails_detailsResolved}

# p2view_IUPresentation class attributes and methods

# p2view_IUDetails class attributes and methods

# aggregator_p2view_Category class attributes and methods
aggregator_p2view_Category_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullProductContainer: Method = Method(name="getNotNullProductContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullCategoryContainer: Method = Method(name="getNotNullCategoryContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_isNested: Method = Method(name="isNested", parameters={}, type=BooleanType)
aggregator_p2view_Category.methods={aggregator_p2view_Category_m_getNotNullProductContainer, aggregator_p2view_Category_m_getNotNullFeatureContainer, aggregator_p2view_Category_m_getNotNullFragmentContainer, aggregator_p2view_Category_m_isNested, aggregator_p2view_Category_m_getNotNullCategoryContainer, aggregator_p2view_Category_m_getNotNullBundleContainer}

# IUPresentation class attributes and methods

# IUDetails class attributes and methods

# aggregator_p2view_Feature class attributes and methods
aggregator_p2view_Feature_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_Feature_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_Feature_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_Feature.methods={aggregator_p2view_Feature_m_getNotNullFeatureContainer, aggregator_p2view_Feature_m_getNotNullBundleContainer, aggregator_p2view_Feature_m_getNotNullFragmentContainer}

# IUPresentationWithDetails class attributes and methods

# aggregator_p2view_Product class attributes and methods
aggregator_p2view_Product_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_Product_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_Product_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_Product.methods={aggregator_p2view_Product_m_getNotNullFragmentContainer, aggregator_p2view_Product_m_getNotNullBundleContainer, aggregator_p2view_Product_m_getNotNullFeatureContainer}

# aggregator_p2view_Bundle class attributes and methods

# aggregator_p2view_Fragment class attributes and methods

# aggregator_p2view_OtherIU class attributes and methods

# aggregator_p2view_Properties class attributes and methods

# p2view_aggregator_Property class attributes and methods

# aggregator_p2view_RequiredCapabilities class attributes and methods

# RequiredCapabilityWrapper class attributes and methods

# aggregator_p2view_ProvidedCapabilities class attributes and methods

# ProvidedCapabilityWrapper class attributes and methods

# aggregator_p2view_Touchpoints class attributes and methods

# aggregator_p2view_IUDetails class attributes and methods

# RequiredCapabilities class attributes and methods

# ProvidedCapabilities class attributes and methods

# Touchpoints class attributes and methods

# aggregator_p2view_RequiredCapabilityWrapper class attributes and methods

# p2_IRequiredCapability class attributes and methods

# LabelProvider class attributes and methods

# aggregator_p2view_ProvidedCapabilityWrapper class attributes and methods

# p2_IProvidedCapability class attributes and methods

# Relationships
mavenMappings10: BinaryAssociation = BinaryAssociation(
    name="mavenMappings10",
    ends={
        Property(name="aggregator_MavenMapping", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregator11", type=aggregator_MavenMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations0: BinaryAssociation = BinaryAssociation(
    name="configurations0",
    ends={
        Property(name="aggregator_Configuration", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregator", type=aggregator_Configuration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contributions1: BinaryAssociation = BinaryAssociation(
    name="contributions1",
    ends={
        Property(name="aggregator_Contribution", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregator2", type=aggregator_Contribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildmaster3: BinaryAssociation = BinaryAssociation(
    name="buildmaster3",
    ends={
        Property(name="aggregator_Contact", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregator4", type=aggregator_Contact, multiplicity=Multiplicity(0, 1))
    }
)
contacts5: BinaryAssociation = BinaryAssociation(
    name="contacts5",
    ends={
        Property(name="Contact", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator", type=aggregator_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customCategories6: BinaryAssociation = BinaryAssociation(
    name="customCategories6",
    ends={
        Property(name="aggregator_CustomCategory", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregator7", type=aggregator_CustomCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationRepositories8: BinaryAssociation = BinaryAssociation(
    name="validationRepositories8",
    ends={
        Property(name="aggregator_MetadataRepositoryReference", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregator9", type=aggregator_MetadataRepositoryReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories31: BinaryAssociation = BinaryAssociation(
    name="categories31",
    ends={
        Property(name="CustomCategory", type=aggregator_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=aggregator_CustomCategory, multiplicity=Multiplicity(0, 9999))
    }
)
products12: BinaryAssociation = BinaryAssociation(
    name="products12",
    ends={
        Property(name="aggregator_Product", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository", type=aggregator_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bundles13: BinaryAssociation = BinaryAssociation(
    name="bundles13",
    ends={
        Property(name="aggregator_Bundle", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository14", type=aggregator_Bundle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features15: BinaryAssociation = BinaryAssociation(
    name="features15",
    ends={
        Property(name="aggregator_Feature", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository16", type=aggregator_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories17: BinaryAssociation = BinaryAssociation(
    name="categories17",
    ends={
        Property(name="aggregator_Category", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository18", type=aggregator_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapRules19: BinaryAssociation = BinaryAssociation(
    name="mapRules19",
    ends={
        Property(name="aggregator_MapRule", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository20", type=aggregator_MapRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories21: BinaryAssociation = BinaryAssociation(
    name="repositories21",
    ends={
        Property(name="aggregator_MappedRepository23", type=aggregator_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Contribution22", type=aggregator_MappedRepository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contacts24: BinaryAssociation = BinaryAssociation(
    name="contacts24",
    ends={
        Property(name="aggregator_Contact26", type=aggregator_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Contribution25", type=aggregator_Contact, multiplicity=Multiplicity(0, 9999))
    }
)
mavenMappings27: BinaryAssociation = BinaryAssociation(
    name="mavenMappings27",
    ends={
        Property(name="aggregator_MavenMapping29", type=aggregator_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Contribution28", type=aggregator_MavenMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregator30: BinaryAssociation = BinaryAssociation(
    name="aggregator30",
    ends={
        Property(name="Aggregator", type=aggregator_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts", type=aggregator_Aggregator, multiplicity=Multiplicity(1, 1))
    }
)
validConfigurations32: BinaryAssociation = BinaryAssociation(
    name="validConfigurations32",
    ends={
        Property(name="aggregator_Configuration33", type=aggregator_MappedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedUnit", type=aggregator_Configuration, multiplicity=Multiplicity(0, 9999))
    }
)
features34: BinaryAssociation = BinaryAssociation(
    name="features34",
    ends={
        Property(name="Feature", type=aggregator_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="categories", type=aggregator_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
installableUnit35: BinaryAssociation = BinaryAssociation(
    name="installableUnit35",
    ends={
        Property(name="InstallableUnit", type=aggregator_InstallableUnitReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_InstallableUnitReference", type=InstallableUnit, multiplicity=Multiplicity(0, 1))
    }
)
validConfigurations36: BinaryAssociation = BinaryAssociation(
    name="validConfigurations36",
    ends={
        Property(name="aggregator_Configuration37", type=aggregator_ValidConfigurationsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_ValidConfigurationsRule", type=aggregator_Configuration, multiplicity=Multiplicity(0, 9999))
    }
)
metadataRepository38: BinaryAssociation = BinaryAssociation(
    name="metadataRepository38",
    ends={
        Property(name="MetadataRepository", type=aggregator_MetadataRepositoryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MetadataRepositoryReference39", type=MetadataRepository, multiplicity=Multiplicity(0, 1))
    }
)
status40: BinaryAssociation = BinaryAssociation(
    name="status40",
    ends={
        Property(name="aggregator_Status", type=aggregator_StatusProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_StatusProvider", type=aggregator_Status, multiplicity=Multiplicity(1, 1))
    }
)
touchpointType41: BinaryAssociation = BinaryAssociation(
    name="touchpointType41",
    ends={
        Property(name="ITouchpointType", type=aggregator_p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_IInstallableUnit", type=ITouchpointType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateDescriptor42: BinaryAssociation = BinaryAssociation(
    name="updateDescriptor42",
    ends={
        Property(name="IUpdateDescriptor", type=aggregator_p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_IInstallableUnit43", type=IUpdateDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
license44: BinaryAssociation = BinaryAssociation(
    name="license44",
    ends={
        Property(name="ILicense", type=aggregator_p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_IInstallableUnit45", type=ILicense, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
copyright46: BinaryAssociation = BinaryAssociation(
    name="copyright46",
    ends={
        Property(name="ICopyright", type=aggregator_p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_IInstallableUnit47", type=ICopyright, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
installableUnits48: BinaryAssociation = BinaryAssociation(
    name="installableUnits48",
    ends={
        Property(name="InstallableUnit49", type=aggregator_p2_MetadataRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_MetadataRepository", type=InstallableUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositoryReferences50: BinaryAssociation = BinaryAssociation(
    name="repositoryReferences50",
    ends={
        Property(name="RepositoryReference", type=aggregator_p2_MetadataRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_MetadataRepository51", type=RepositoryReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyMap52: BinaryAssociation = BinaryAssociation(
    name="propertyMap52",
    ends={
        Property(name="Property", type=aggregator_p2_MetadataRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_MetadataRepository53", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedCapabilityList55: BinaryAssociation = BinaryAssociation(
    name="providedCapabilityList55",
    ends={
        Property(name="ProvidedCapability", type=aggregator_p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnit56", type=ProvidedCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifactList54: BinaryAssociation = BinaryAssociation(
    name="artifactList54",
    ends={
        Property(name="ArtifactKey", type=aggregator_p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnit", type=ArtifactKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCapabilityList57: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilityList57",
    ends={
        Property(name="RequiredCapability", type=aggregator_p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnit58", type=RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaRequiredCapabilityList59: BinaryAssociation = BinaryAssociation(
    name="metaRequiredCapabilityList59",
    ends={
        Property(name="RequiredCapability61", type=aggregator_p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnit60", type=RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyMap62: BinaryAssociation = BinaryAssociation(
    name="propertyMap62",
    ends={
        Property(name="Property64", type=aggregator_p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnit63", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
touchpointDataList65: BinaryAssociation = BinaryAssociation(
    name="touchpointDataList65",
    ends={
        Property(name="TouchpointData", type=aggregator_p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnit66", type=TouchpointData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostList67: BinaryAssociation = BinaryAssociation(
    name="hostList67",
    ends={
        Property(name="RequiredCapability68", type=aggregator_p2_InstallableUnitFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstallableUnitFragment", type=RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructionMap69: BinaryAssociation = BinaryAssociation(
    name="instructionMap69",
    ends={
        Property(name="InstructionMap", type=aggregator_p2_TouchpointData, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_TouchpointData", type=InstructionMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value70: BinaryAssociation = BinaryAssociation(
    name="value70",
    ends={
        Property(name="TouchpointInstruction", type=aggregator_p2_InstructionMap, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2_InstructionMap", type=TouchpointInstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragmentContainer84: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer84",
    ends={
        Property(name="Fragments", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits85", type=Fragments, multiplicity=Multiplicity(0, 1))
    }
)
miscellaneousContainer86: BinaryAssociation = BinaryAssociation(
    name="miscellaneousContainer86",
    ends={
        Property(name="Miscellaneous", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits87", type=Miscellaneous, multiplicity=Multiplicity(0, 1))
    }
)
installableUnitList71: BinaryAssociation = BinaryAssociation(
    name="installableUnitList71",
    ends={
        Property(name="InstallableUnits", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView", type=InstallableUnits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties72: BinaryAssociation = BinaryAssociation(
    name="properties72",
    ends={
        Property(name="Properties", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView73", type=Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metadataRepository74: BinaryAssociation = BinaryAssociation(
    name="metadataRepository74",
    ends={
        Property(name="MetadataRepository76", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView75", type=MetadataRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
categoryContainer77: BinaryAssociation = BinaryAssociation(
    name="categoryContainer77",
    ends={
        Property(name="Categories", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits", type=Categories, multiplicity=Multiplicity(0, 1))
    }
)
featureContainer78: BinaryAssociation = BinaryAssociation(
    name="featureContainer78",
    ends={
        Property(name="Features", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits79", type=Features, multiplicity=Multiplicity(0, 1))
    }
)
productContainer80: BinaryAssociation = BinaryAssociation(
    name="productContainer80",
    ends={
        Property(name="Products", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits81", type=Products, multiplicity=Multiplicity(0, 1))
    }
)
bundleContainer82: BinaryAssociation = BinaryAssociation(
    name="bundleContainer82",
    ends={
        Property(name="Bundles", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits83", type=Bundles, multiplicity=Multiplicity(0, 1))
    }
)
categories88: BinaryAssociation = BinaryAssociation(
    name="categories88",
    ends={
        Property(name="Category", type=aggregator_p2view_Categories, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Categories", type=Category, multiplicity=Multiplicity(0, 9999))
    }
)
features89: BinaryAssociation = BinaryAssociation(
    name="features89",
    ends={
        Property(name="Feature90", type=aggregator_p2view_Features, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Features", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
products91: BinaryAssociation = BinaryAssociation(
    name="products91",
    ends={
        Property(name="Product", type=aggregator_p2view_Products, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Products", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
bundles92: BinaryAssociation = BinaryAssociation(
    name="bundles92",
    ends={
        Property(name="Bundle", type=aggregator_p2view_Bundles, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Bundles", type=Bundle, multiplicity=Multiplicity(0, 9999))
    }
)
fragments93: BinaryAssociation = BinaryAssociation(
    name="fragments93",
    ends={
        Property(name="Fragment", type=aggregator_p2view_Fragments, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Fragments", type=Fragment, multiplicity=Multiplicity(0, 9999))
    }
)
others94: BinaryAssociation = BinaryAssociation(
    name="others94",
    ends={
        Property(name="OtherIU", type=aggregator_p2view_Miscellaneous, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Miscellaneous", type=OtherIU, multiplicity=Multiplicity(0, 9999))
    }
)
installableUnit95: BinaryAssociation = BinaryAssociation(
    name="installableUnit95",
    ends={
        Property(name="InstallableUnit96", type=aggregator_p2view_IUPresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUPresentation", type=InstallableUnit, multiplicity=Multiplicity(0, 1))
    }
)
categoryContainer97: BinaryAssociation = BinaryAssociation(
    name="categoryContainer97",
    ends={
        Property(name="Categories98", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category", type=Categories, multiplicity=Multiplicity(0, 1))
    }
)
featureContainer99: BinaryAssociation = BinaryAssociation(
    name="featureContainer99",
    ends={
        Property(name="Features101", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category100", type=Features, multiplicity=Multiplicity(0, 1))
    }
)
productContainer102: BinaryAssociation = BinaryAssociation(
    name="productContainer102",
    ends={
        Property(name="Products104", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category103", type=Products, multiplicity=Multiplicity(0, 1))
    }
)
bundleContainer105: BinaryAssociation = BinaryAssociation(
    name="bundleContainer105",
    ends={
        Property(name="Bundles107", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category106", type=Bundles, multiplicity=Multiplicity(0, 1))
    }
)
fragmentContainer108: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer108",
    ends={
        Property(name="Fragments110", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category109", type=Fragments, multiplicity=Multiplicity(0, 1))
    }
)
iuDetails111: BinaryAssociation = BinaryAssociation(
    name="iuDetails111",
    ends={
        Property(name="IUDetails", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category112", type=IUDetails, multiplicity=Multiplicity(0, 1))
    }
)
featureContainer113: BinaryAssociation = BinaryAssociation(
    name="featureContainer113",
    ends={
        Property(name="Features114", type=aggregator_p2view_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Feature", type=Features, multiplicity=Multiplicity(0, 1))
    }
)
bundleContainer115: BinaryAssociation = BinaryAssociation(
    name="bundleContainer115",
    ends={
        Property(name="Bundles117", type=aggregator_p2view_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Feature116", type=Bundles, multiplicity=Multiplicity(0, 1))
    }
)
fragmentContainer118: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer118",
    ends={
        Property(name="Fragments120", type=aggregator_p2view_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Feature119", type=Fragments, multiplicity=Multiplicity(0, 1))
    }
)
featureContainer121: BinaryAssociation = BinaryAssociation(
    name="featureContainer121",
    ends={
        Property(name="Features122", type=aggregator_p2view_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Product", type=Features, multiplicity=Multiplicity(0, 1))
    }
)
bundleContainer123: BinaryAssociation = BinaryAssociation(
    name="bundleContainer123",
    ends={
        Property(name="Bundles125", type=aggregator_p2view_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Product124", type=Bundles, multiplicity=Multiplicity(0, 1))
    }
)
fragmentContainer126: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer126",
    ends={
        Property(name="Fragments128", type=aggregator_p2view_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Product127", type=Fragments, multiplicity=Multiplicity(0, 1))
    }
)
propertyList129: BinaryAssociation = BinaryAssociation(
    name="propertyList129",
    ends={
        Property(name="p2view_aggregator_Property", type=aggregator_p2view_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Properties", type=p2view_aggregator_Property, multiplicity=Multiplicity(0, 9999))
    }
)
requiredCapabilities130: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilities130",
    ends={
        Property(name="RequiredCapabilityWrapper", type=aggregator_p2view_RequiredCapabilities, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_RequiredCapabilities", type=RequiredCapabilityWrapper, multiplicity=Multiplicity(0, 9999))
    }
)
providedCapabilities131: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities131",
    ends={
        Property(name="ProvidedCapabilityWrapper", type=aggregator_p2view_ProvidedCapabilities, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_ProvidedCapabilities", type=ProvidedCapabilityWrapper, multiplicity=Multiplicity(0, 9999))
    }
)
touchpointType132: BinaryAssociation = BinaryAssociation(
    name="touchpointType132",
    ends={
        Property(name="ITouchpointType133", type=aggregator_p2view_Touchpoints, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Touchpoints", type=ITouchpointType, multiplicity=Multiplicity(0, 1))
    }
)
touchpointDataList134: BinaryAssociation = BinaryAssociation(
    name="touchpointDataList134",
    ends={
        Property(name="TouchpointData136", type=aggregator_p2view_Touchpoints, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Touchpoints135", type=TouchpointData, multiplicity=Multiplicity(0, 9999))
    }
)
requiredCapabilitiesContainer137: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilitiesContainer137",
    ends={
        Property(name="RequiredCapabilities", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails", type=RequiredCapabilities, multiplicity=Multiplicity(0, 1))
    }
)
providedCapabilitiesContainer138: BinaryAssociation = BinaryAssociation(
    name="providedCapabilitiesContainer138",
    ends={
        Property(name="ProvidedCapabilities", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails139", type=ProvidedCapabilities, multiplicity=Multiplicity(0, 1))
    }
)
propertiesContainer140: BinaryAssociation = BinaryAssociation(
    name="propertiesContainer140",
    ends={
        Property(name="Properties142", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails141", type=Properties, multiplicity=Multiplicity(0, 1))
    }
)
touchpointsContainer143: BinaryAssociation = BinaryAssociation(
    name="touchpointsContainer143",
    ends={
        Property(name="Touchpoints", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails144", type=Touchpoints, multiplicity=Multiplicity(0, 1))
    }
)
updateDescriptor145: BinaryAssociation = BinaryAssociation(
    name="updateDescriptor145",
    ends={
        Property(name="IUpdateDescriptor147", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails146", type=IUpdateDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
copyright148: BinaryAssociation = BinaryAssociation(
    name="copyright148",
    ends={
        Property(name="ICopyright150", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails149", type=ICopyright, multiplicity=Multiplicity(0, 1))
    }
)
license151: BinaryAssociation = BinaryAssociation(
    name="license151",
    ends={
        Property(name="ILicense153", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails152", type=ILicense, multiplicity=Multiplicity(0, 1))
    }
)
genuine154: BinaryAssociation = BinaryAssociation(
    name="genuine154",
    ends={
        Property(name="RequiredCapability155", type=aggregator_p2view_RequiredCapabilityWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_RequiredCapabilityWrapper", type=RequiredCapability, multiplicity=Multiplicity(1, 1))
    }
)
genuine156: BinaryAssociation = BinaryAssociation(
    name="genuine156",
    ends={
        Property(name="ProvidedCapability157", type=aggregator_p2view_ProvidedCapabilityWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_ProvidedCapabilityWrapper", type=ProvidedCapability, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_aggregator_MappedRepository_MetadataRepositoryReference = Generalization(general=MetadataRepositoryReference, specific=aggregator_MappedRepository)
gen_aggregator_MappedRepository_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_MappedRepository)
gen_aggregator_Aggregator_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_Aggregator)
gen_aggregator_Aggregator_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_Aggregator)
gen_aggregator_Aggregator_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_Aggregator)
gen_aggregator_Bundle_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Bundle)
gen_aggregator_Configuration_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_Configuration)
gen_aggregator_Contribution_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_Contribution)
gen_aggregator_Feature_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Feature)
gen_aggregator_ExclusionRule_MapRule = Generalization(general=MapRule, specific=aggregator_ExclusionRule)
gen_aggregator_ValidConfigurationsRule_MapRule = Generalization(general=MapRule, specific=aggregator_ValidConfigurationsRule)
gen_aggregator_MappedUnit_InstallableUnitReference = Generalization(general=InstallableUnitReference, specific=aggregator_MappedUnit)
gen_aggregator_MappedUnit_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_MappedUnit)
gen_aggregator_Product_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Product)
gen_aggregator_Category_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Category)
gen_aggregator_CustomCategory_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_CustomCategory)
gen_aggregator_CustomCategory_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_CustomCategory)
gen_aggregator_MapRule_InstallableUnitReference = Generalization(general=InstallableUnitReference, specific=aggregator_MapRule)
gen_aggregator_MapRule_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_MapRule)
gen_aggregator_InstallableUnitReference_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_InstallableUnitReference)
gen_aggregator_InstallableUnitReference_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_InstallableUnitReference)
gen_aggregator_MetadataRepositoryReference_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_MetadataRepositoryReference)
gen_aggregator_MetadataRepositoryReference_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_MetadataRepositoryReference)
gen_aggregator_MetadataRepositoryReference_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_MetadataRepositoryReference)
gen_aggregator_MavenMapping_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_MavenMapping)
gen_aggregator_MavenMapping_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_MavenMapping)
gen_aggregator_p2_IInstallableUnitFragment_IInstallableUnit = Generalization(general=IInstallableUnit, specific=aggregator_p2_IInstallableUnitFragment)
gen_aggregator_p2_ArtifactKey_IArtifactKey = Generalization(general=IArtifactKey, specific=aggregator_p2_ArtifactKey)
gen_aggregator_p2_Copyright_ICopyright = Generalization(general=ICopyright, specific=aggregator_p2_Copyright)
gen_aggregator_p2_MetadataRepository_IMetadataRepository = Generalization(general=IMetadataRepository, specific=aggregator_p2_MetadataRepository)
gen_aggregator_p2_InstallableUnit_IInstallableUnit = Generalization(general=IInstallableUnit, specific=aggregator_p2_InstallableUnit)
gen_aggregator_p2_InstallableUnitFragment_p2_InstallableUnit = Generalization(general=p2_InstallableUnit, specific=aggregator_p2_InstallableUnitFragment)
gen_aggregator_p2_InstallableUnitFragment_p2_IInstallableUnitFragment = Generalization(general=p2_IInstallableUnitFragment, specific=aggregator_p2_InstallableUnitFragment)
gen_aggregator_p2_License_ILicense = Generalization(general=ILicense, specific=aggregator_p2_License)
gen_aggregator_p2_ProvidedCapability_IProvidedCapability = Generalization(general=IProvidedCapability, specific=aggregator_p2_ProvidedCapability)
gen_aggregator_p2_RequiredCapability_IRequiredCapability = Generalization(general=IRequiredCapability, specific=aggregator_p2_RequiredCapability)
gen_aggregator_p2_TouchpointData_ITouchpointData = Generalization(general=ITouchpointData, specific=aggregator_p2_TouchpointData)
gen_aggregator_p2_TouchpointInstruction_ITouchpointInstruction = Generalization(general=ITouchpointInstruction, specific=aggregator_p2_TouchpointInstruction)
gen_aggregator_p2_TouchpointType_ITouchpointType = Generalization(general=ITouchpointType, specific=aggregator_p2_TouchpointType)
gen_aggregator_p2_UpdateDescriptor_IUpdateDescriptor = Generalization(general=IUpdateDescriptor, specific=aggregator_p2_UpdateDescriptor)
gen_aggregator_p2_IMetadataRepository_p2_IQueryable = Generalization(general=p2_IQueryable, specific=aggregator_p2_IMetadataRepository)
gen_aggregator_p2_IMetadataRepository_p2_IRepository = Generalization(general=p2_IRepository, specific=aggregator_p2_IMetadataRepository)
gen_aggregator_p2_IRepository_IAdaptable = Generalization(general=IAdaptable, specific=aggregator_p2_IRepository)
gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUPresentation = Generalization(general=p2view_IUPresentation, specific=aggregator_p2view_IUPresentationWithDetails)
gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUDetails = Generalization(general=p2view_IUDetails, specific=aggregator_p2view_IUPresentationWithDetails)
gen_aggregator_p2view_Category_IUPresentation = Generalization(general=IUPresentation, specific=aggregator_p2view_Category)
gen_aggregator_p2view_Feature_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_Feature)
gen_aggregator_p2view_Product_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_Product)
gen_aggregator_p2view_Bundle_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_Bundle)
gen_aggregator_p2view_Fragment_Bundle = Generalization(general=Bundle, specific=aggregator_p2view_Fragment)
gen_aggregator_p2view_OtherIU_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_OtherIU)
gen_aggregator_p2view_RequiredCapabilityWrapper_p2_IRequiredCapability = Generalization(general=p2_IRequiredCapability, specific=aggregator_p2view_RequiredCapabilityWrapper)
gen_aggregator_p2view_RequiredCapabilityWrapper_LabelProvider = Generalization(general=LabelProvider, specific=aggregator_p2view_RequiredCapabilityWrapper)
gen_aggregator_p2view_ProvidedCapabilityWrapper_p2_IProvidedCapability = Generalization(general=p2_IProvidedCapability, specific=aggregator_p2view_ProvidedCapabilityWrapper)
gen_aggregator_p2view_ProvidedCapabilityWrapper_LabelProvider = Generalization(general=LabelProvider, specific=aggregator_p2view_ProvidedCapabilityWrapper)

# Domain Model
domain_model = DomainModel(
    name="aggregator",
    types={aggregator_MavenMapping, aggregator_MappedRepository, MetadataRepositoryReference, aggregator_Aggregator, DescriptionProvider, StatusProvider, InfosProvider, aggregator_Configuration, aggregator_Contribution, aggregator_Contact, aggregator_CustomCategory, aggregator_MetadataRepositoryReference, aggregator_Product, aggregator_Bundle, aggregator_Feature, aggregator_Category, aggregator_MapRule, EnabledStatusProvider, MappedUnit, aggregator_ExclusionRule, MapRule, aggregator_ValidConfigurationsRule, aggregator_MappedUnit, InstallableUnitReference, aggregator_Property, aggregator_EnabledStatusProvider, aggregator_InstallableUnitReference, InstallableUnit, aggregator_StatusProvider, MetadataRepository, aggregator_Comparable, aggregator_LabelProvider, aggregator_DescriptionProvider, aggregator_MavenItem, aggregator_ChildrenProvider, aggregator_Status, aggregator_InfosProvider, aggregator_p2_IArtifactKey, aggregator_p2_ICopyright, aggregator_p2_IInstallableUnit, ITouchpointType, IUpdateDescriptor, ILicense, ICopyright, aggregator_p2_IInstallableUnitFragment, IInstallableUnit, aggregator_p2_ILicense, aggregator_p2_IProvidedCapability, aggregator_p2_IRequiredCapability, aggregator_p2_ITouchpointData, aggregator_p2_ITouchpointInstruction, aggregator_p2_ITouchpointType, aggregator_p2_IUpdateDescriptor, aggregator_p2_ArtifactKey, IArtifactKey, aggregator_p2_Copyright, aggregator_p2_MetadataRepository, IMetadataRepository, RepositoryReference, Property_, aggregator_p2_InstallableUnit, ProvidedCapability, ArtifactKey, RequiredCapability, TouchpointData, aggregator_p2_InstallableUnitFragment, p2_InstallableUnit, p2_IInstallableUnitFragment, aggregator_p2_License, aggregator_p2_ProvidedCapability, IProvidedCapability, aggregator_p2_RequiredCapability, IRequiredCapability, aggregator_p2_TouchpointData, ITouchpointData, InstructionMap, aggregator_p2_TouchpointInstruction, ITouchpointInstruction, aggregator_p2_TouchpointType, aggregator_p2_UpdateDescriptor, aggregator_p2_Property, aggregator_p2_InstructionMap, TouchpointInstruction, aggregator_p2_IQueryable, aggregator_p2_IMetadataRepository, p2_IQueryable, p2_IRepository, Miscellaneous, aggregator_p2_IRepository, IAdaptable, aggregator_p2_RepositoryReference, aggregator_p2_IAdaptable, aggregator_p2view_MetadataRepositoryStructuredView, InstallableUnits, Properties, aggregator_p2view_InstallableUnits, Categories, Features, Products, Bundles, Fragments, aggregator_p2view_Categories, Category, aggregator_p2view_Features, Feature, aggregator_p2view_Products, Product, aggregator_p2view_Bundles, Bundle, aggregator_p2view_Fragments, Fragment, aggregator_p2view_Miscellaneous, OtherIU, aggregator_p2view_IUPresentation, aggregator_p2view_IUPresentationWithDetails, p2view_IUPresentation, p2view_IUDetails, aggregator_p2view_Category, IUPresentation, IUDetails, aggregator_p2view_Feature, IUPresentationWithDetails, aggregator_p2view_Product, aggregator_p2view_Bundle, aggregator_p2view_Fragment, aggregator_p2view_OtherIU, aggregator_p2view_Properties, p2view_aggregator_Property, aggregator_p2view_RequiredCapabilities, RequiredCapabilityWrapper, aggregator_p2view_ProvidedCapabilities, ProvidedCapabilityWrapper, aggregator_p2view_Touchpoints, aggregator_p2view_IUDetails, RequiredCapabilities, ProvidedCapabilities, Touchpoints, aggregator_p2view_RequiredCapabilityWrapper, p2_IRequiredCapability, LabelProvider, aggregator_p2view_ProvidedCapabilityWrapper, p2_IProvidedCapability, AggregationType, OperatingSystem, WindowSystem, Architecture, PackedStrategy, InstallableUnitType, StatusCode},
    associations={mavenMappings10, configurations0, contributions1, buildmaster3, contacts5, customCategories6, validationRepositories8, categories31, products12, bundles13, features15, categories17, mapRules19, repositories21, contacts24, mavenMappings27, aggregator30, validConfigurations32, features34, installableUnit35, validConfigurations36, metadataRepository38, status40, touchpointType41, updateDescriptor42, license44, copyright46, installableUnits48, repositoryReferences50, propertyMap52, providedCapabilityList55, artifactList54, requiredCapabilityList57, metaRequiredCapabilityList59, propertyMap62, touchpointDataList65, hostList67, instructionMap69, value70, fragmentContainer84, miscellaneousContainer86, installableUnitList71, properties72, metadataRepository74, categoryContainer77, featureContainer78, productContainer80, bundleContainer82, categories88, features89, products91, bundles92, fragments93, others94, installableUnit95, categoryContainer97, featureContainer99, productContainer102, bundleContainer105, fragmentContainer108, iuDetails111, featureContainer113, bundleContainer115, fragmentContainer118, featureContainer121, bundleContainer123, fragmentContainer126, propertyList129, requiredCapabilities130, providedCapabilities131, touchpointType132, touchpointDataList134, requiredCapabilitiesContainer137, providedCapabilitiesContainer138, propertiesContainer140, touchpointsContainer143, updateDescriptor145, copyright148, license151, genuine154, genuine156},
    generalizations={gen_aggregator_MappedRepository_MetadataRepositoryReference, gen_aggregator_MappedRepository_DescriptionProvider, gen_aggregator_Aggregator_DescriptionProvider, gen_aggregator_Aggregator_StatusProvider, gen_aggregator_Aggregator_InfosProvider, gen_aggregator_Bundle_MappedUnit, gen_aggregator_Configuration_EnabledStatusProvider, gen_aggregator_Contribution_EnabledStatusProvider, gen_aggregator_Contribution_DescriptionProvider, gen_aggregator_Contribution_StatusProvider, gen_aggregator_Contribution_InfosProvider, gen_aggregator_Feature_MappedUnit, gen_aggregator_ExclusionRule_MapRule, gen_aggregator_ValidConfigurationsRule_MapRule, gen_aggregator_MappedUnit_InstallableUnitReference, gen_aggregator_MappedUnit_EnabledStatusProvider, gen_aggregator_Product_MappedUnit, gen_aggregator_Category_MappedUnit, gen_aggregator_CustomCategory_StatusProvider, gen_aggregator_CustomCategory_InfosProvider, gen_aggregator_MapRule_InstallableUnitReference, gen_aggregator_MapRule_DescriptionProvider, gen_aggregator_InstallableUnitReference_StatusProvider, gen_aggregator_InstallableUnitReference_InfosProvider, gen_aggregator_MetadataRepositoryReference_EnabledStatusProvider, gen_aggregator_MetadataRepositoryReference_StatusProvider, gen_aggregator_MetadataRepositoryReference_InfosProvider, gen_aggregator_MavenMapping_StatusProvider, gen_aggregator_MavenMapping_InfosProvider, gen_aggregator_p2_IInstallableUnitFragment_IInstallableUnit, gen_aggregator_p2_ArtifactKey_IArtifactKey, gen_aggregator_p2_Copyright_ICopyright, gen_aggregator_p2_MetadataRepository_IMetadataRepository, gen_aggregator_p2_InstallableUnit_IInstallableUnit, gen_aggregator_p2_InstallableUnitFragment_p2_InstallableUnit, gen_aggregator_p2_InstallableUnitFragment_p2_IInstallableUnitFragment, gen_aggregator_p2_License_ILicense, gen_aggregator_p2_ProvidedCapability_IProvidedCapability, gen_aggregator_p2_RequiredCapability_IRequiredCapability, gen_aggregator_p2_TouchpointData_ITouchpointData, gen_aggregator_p2_TouchpointInstruction_ITouchpointInstruction, gen_aggregator_p2_TouchpointType_ITouchpointType, gen_aggregator_p2_UpdateDescriptor_IUpdateDescriptor, gen_aggregator_p2_IMetadataRepository_p2_IQueryable, gen_aggregator_p2_IMetadataRepository_p2_IRepository, gen_aggregator_p2_IRepository_IAdaptable, gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUPresentation, gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUDetails, gen_aggregator_p2view_Category_IUPresentation, gen_aggregator_p2view_Feature_IUPresentationWithDetails, gen_aggregator_p2view_Product_IUPresentationWithDetails, gen_aggregator_p2view_Bundle_IUPresentationWithDetails, gen_aggregator_p2view_Fragment_Bundle, gen_aggregator_p2view_OtherIU_IUPresentationWithDetails, gen_aggregator_p2view_RequiredCapabilityWrapper_p2_IRequiredCapability, gen_aggregator_p2view_RequiredCapabilityWrapper_LabelProvider, gen_aggregator_p2view_ProvidedCapabilityWrapper_p2_IProvidedCapability, gen_aggregator_p2view_ProvidedCapabilityWrapper_LabelProvider},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)