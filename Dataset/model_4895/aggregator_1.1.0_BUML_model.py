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
OperatingSystem: Enumeration = Enumeration(
    name="OperatingSystem",
    literals={
            EnumerationLiteral(name="Win32"),
			EnumerationLiteral(name="Linux"),
			EnumerationLiteral(name="MacOSX"),
			EnumerationLiteral(name="AIX"),
			EnumerationLiteral(name="HPUX"),
			EnumerationLiteral(name="Solaris"),
			EnumerationLiteral(name="QNX")
    }
)

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

Architecture: Enumeration = Enumeration(
    name="Architecture",
    literals={
            EnumerationLiteral(name="X86"),
			EnumerationLiteral(name="PPC"),
			EnumerationLiteral(name="X86_64"),
			EnumerationLiteral(name="IA64"),
			EnumerationLiteral(name="IA64_32"),
			EnumerationLiteral(name="Sparc"),
			EnumerationLiteral(name="PPC64"),
			EnumerationLiteral(name="S390"),
			EnumerationLiteral(name="S390X")
    }
)

AvailableFrom: Enumeration = Enumeration(
    name="AvailableFrom",
    literals={
            EnumerationLiteral(name="REPOSITORY"),
			EnumerationLiteral(name="CONTRIBUTION"),
			EnumerationLiteral(name="VALIDATION_SET"),
			EnumerationLiteral(name="AGGREGATION")
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

StatusCode: Enumeration = Enumeration(
    name="StatusCode",
    literals={
            EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="BROKEN"),
			EnumerationLiteral(name="WAITING")
    }
)

VersionMatch: Enumeration = Enumeration(
    name="VersionMatch",
    literals={
            EnumerationLiteral(name="BELOW"),
			EnumerationLiteral(name="MATCHES"),
			EnumerationLiteral(name="ABOVE")
    }
)

WindowSystem: Enumeration = Enumeration(
    name="WindowSystem",
    literals={
            EnumerationLiteral(name="Win32"),
			EnumerationLiteral(name="GTK"),
			EnumerationLiteral(name="Carbon"),
			EnumerationLiteral(name="Cocoa"),
			EnumerationLiteral(name="Motif"),
			EnumerationLiteral(name="Photon")
    }
)

# Classes
aggregator_AvailableVersion = Class(name="aggregator::AvailableVersion")
aggregator_InstallableUnitRequest = Class(name="aggregator::InstallableUnitRequest", is_abstract=True)
aggregator_Aggregation = Class(name="aggregator::Aggregation")
DescriptionProvider = Class(name="DescriptionProvider")
StatusProvider = Class(name="StatusProvider")
InfosProvider = Class(name="InfosProvider")
aggregator_ValidationSet = Class(name="aggregator::ValidationSet")
aggregator_Configuration = Class(name="aggregator::Configuration")
aggregator_CustomCategory = Class(name="aggregator::CustomCategory")
aggregator_Contact = Class(name="aggregator::Contact")
aggregator_MavenMapping = Class(name="aggregator::MavenMapping")
aggregator_AvailableVersionsHeader = Class(name="aggregator::AvailableVersionsHeader")
aggregator_Bundle = Class(name="aggregator::Bundle")
MappedUnit = Class(name="MappedUnit")
aggregator_Category = Class(name="aggregator::Category")
aggregator_ChildrenProvider = Class(name="aggregator::ChildrenProvider", is_abstract=True)
EnabledStatusProvider = Class(name="EnabledStatusProvider")
aggregator_Contribution = Class(name="aggregator::Contribution")
IdentificationProvider = Class(name="IdentificationProvider")
aggregator_MappedRepository = Class(name="aggregator::MappedRepository")
aggregator_Feature = Class(name="aggregator::Feature")
aggregator_DescriptionProvider = Class(name="aggregator::DescriptionProvider")
aggregator_EnabledStatusProvider = Class(name="aggregator::EnabledStatusProvider", is_abstract=True)
aggregator_ExclusionRule = Class(name="aggregator::ExclusionRule")
MapRule = Class(name="MapRule")
aggregator_IdentificationProvider = Class(name="aggregator::IdentificationProvider", is_abstract=True)
aggregator_InfosProvider = Class(name="aggregator::InfosProvider")
aggregator_LabelProvider = Class(name="aggregator::LabelProvider", is_abstract=True)
MetadataRepositoryReference = Class(name="MetadataRepositoryReference")
aggregator_Product = Class(name="aggregator::Product")
aggregator_StatusProvider = Class(name="aggregator::StatusProvider", is_abstract=True)
aggregator_MapRule = Class(name="aggregator::MapRule", is_abstract=True)
aggregator_MappedUnit = Class(name="aggregator::MappedUnit", is_abstract=True)
InstallableUnitRequest = Class(name="InstallableUnitRequest")
aggregator_MavenItem = Class(name="aggregator::MavenItem")
aggregator_MetadataRepositoryReference = Class(name="aggregator::MetadataRepositoryReference")
aggregator_MetadataRepository = Class(name="aggregator::MetadataRepository")
aggregator_Property = Class(name="aggregator::Property")
aggregator_Status = Class(name="aggregator::Status")
aggregator_ValidConfigurationsRule = Class(name="aggregator::ValidConfigurationsRule")
IUDetails = Class(name="IUDetails")
aggregator_p2view_Bundle = Class(name="aggregator::p2view::Bundle")
IUPresentationWithDetails = Class(name="IUPresentationWithDetails")
aggregator_p2view_Bundles = Class(name="aggregator::p2view::Bundles")
Bundle = Class(name="Bundle")
aggregator_p2view_Category = Class(name="aggregator::p2view::Category")
IUPresentation = Class(name="IUPresentation")
Categories = Class(name="Categories")
Features = Class(name="Features")
Products = Class(name="Products")
Bundles = Class(name="Bundles")
Fragments = Class(name="Fragments")
aggregator_p2view_IUDetails = Class(name="aggregator::p2view::IUDetails")
Requirements = Class(name="Requirements")
aggregator_p2view_Categories = Class(name="aggregator::p2view::Categories")
Category = Class(name="Category")
aggregator_p2view_Feature = Class(name="aggregator::p2view::Feature")
aggregator_p2view_Features = Class(name="aggregator::p2view::Features")
Feature = Class(name="Feature")
aggregator_p2view_Fragment = Class(name="aggregator::p2view::Fragment")
aggregator_p2view_Fragments = Class(name="aggregator::p2view::Fragments")
Fragment = Class(name="Fragment")
aggregator_p2view_InstallableUnits = Class(name="aggregator::p2view::InstallableUnits")
Miscellaneous = Class(name="Miscellaneous")
ProvidedCapabilities = Class(name="ProvidedCapabilities")
Properties = Class(name="Properties")
Touchpoints = Class(name="Touchpoints")
p2view_aggregator_IUpdateDescriptor = Class(name="p2view::aggregator::IUpdateDescriptor")
p2view_aggregator_ICopyright = Class(name="p2view::aggregator::ICopyright")
Licenses = Class(name="Licenses")
aggregator_p2view_IUPresentation = Class(name="aggregator::p2view::IUPresentation", is_abstract=True)
p2view_aggregator_IInstallableUnit = Class(name="p2view::aggregator::IInstallableUnit")
aggregator_p2view_IUPresentationWithDetails = Class(name="aggregator::p2view::IUPresentationWithDetails", is_abstract=True)
p2view_IUPresentation = Class(name="p2view::IUPresentation")
p2view_IUDetails = Class(name="p2view::IUDetails")
aggregator_p2view_Licenses = Class(name="aggregator::p2view::Licenses")
p2view_aggregator_ILicense = Class(name="p2view::aggregator::ILicense")
aggregator_p2view_Requirements = Class(name="aggregator::p2view::Requirements")
aggregator_p2view_RepositoryBrowser = Class(name="aggregator::p2view::RepositoryBrowser")
RequirementWrapper = Class(name="RequirementWrapper")
MetadataRepositoryStructuredView = Class(name="MetadataRepositoryStructuredView")
aggregator_p2view_MetadataRepositoryStructuredView = Class(name="aggregator::p2view::MetadataRepositoryStructuredView")
aggregator_p2view_RequirementWrapper = Class(name="aggregator::p2view::RequirementWrapper")
IRequirement = Class(name="IRequirement")
InstallableUnits = Class(name="InstallableUnits")
p2view_aggregator_MetadataRepository = Class(name="p2view::aggregator::MetadataRepository")
RepositoryReferences = Class(name="RepositoryReferences")
aggregator_p2view_Miscellaneous = Class(name="aggregator::p2view::Miscellaneous")
OtherIU = Class(name="OtherIU")
aggregator_p2view_OtherIU = Class(name="aggregator::p2view::OtherIU")
aggregator_p2view_Product = Class(name="aggregator::p2view::Product")
aggregator_p2view_Products = Class(name="aggregator::p2view::Products")
Product = Class(name="Product")
aggregator_p2view_Properties = Class(name="aggregator::p2view::Properties")
p2view_aggregator_Property = Class(name="p2view::aggregator::Property")
aggregator_p2view_ProvidedCapabilities = Class(name="aggregator::p2view::ProvidedCapabilities")
ProvidedCapabilityWrapper = Class(name="ProvidedCapabilityWrapper")
aggregator_p2view_ProvidedCapabilityWrapper = Class(name="aggregator::p2view::ProvidedCapabilityWrapper")
IProvidedCapability = Class(name="IProvidedCapability")
LabelProvider = Class(name="LabelProvider")
p2view_aggregator_IProvidedCapability = Class(name="p2view::aggregator::IProvidedCapability")
aggregator_p2view_RepositoryReferences = Class(name="aggregator::p2view::RepositoryReferences")
p2view_aggregator_IRepositoryReference = Class(name="p2view::aggregator::IRepositoryReference")
p2view_aggregator_IRequirement = Class(name="p2view::aggregator::IRequirement")
aggregator_p2view_Touchpoints = Class(name="aggregator::p2view::Touchpoints")
p2view_aggregator_ITouchpointType = Class(name="p2view::aggregator::ITouchpointType")
p2view_aggregator_ITouchpointData = Class(name="p2view::aggregator::ITouchpointData")

# aggregator_AvailableVersion class attributes and methods
aggregator_AvailableVersion_versionMatch: Property = Property(name="versionMatch", type=StringType)
aggregator_AvailableVersion_version: Property = Property(name="version", type=StringType)
aggregator_AvailableVersion_filter: Property = Property(name="filter", type=StringType)
aggregator_AvailableVersion_availableFrom: Property = Property(name="availableFrom", type=StringType)
aggregator_AvailableVersion.attributes={aggregator_AvailableVersion_version, aggregator_AvailableVersion_filter, aggregator_AvailableVersion_versionMatch, aggregator_AvailableVersion_availableFrom}

# aggregator_InstallableUnitRequest class attributes and methods
aggregator_InstallableUnitRequest_name: Property = Property(name="name", type=StringType)
aggregator_InstallableUnitRequest_versionRange: Property = Property(name="versionRange", type=StringType)
aggregator_InstallableUnitRequest_m_isMappedRepositoryBroken: Method = Method(name="isMappedRepositoryBroken", parameters={}, type=BooleanType)
aggregator_InstallableUnitRequest_m_isBranchEnabled: Method = Method(name="isBranchEnabled", parameters={}, type=BooleanType)
aggregator_InstallableUnitRequest_m_resolveAsSingleton: Method = Method(name="resolveAsSingleton", parameters={}, type=StringType)
aggregator_InstallableUnitRequest_m_resolveAsSingleton: Method = Method(name="resolveAsSingleton", parameters={Parameter(name='forceResolve')}, type=StringType)
aggregator_InstallableUnitRequest_m_resolveAvailableVersions: Method = Method(name="resolveAvailableVersions", parameters={Parameter(name='updateOnly')})
aggregator_InstallableUnitRequest.attributes={aggregator_InstallableUnitRequest_versionRange, aggregator_InstallableUnitRequest_name}
aggregator_InstallableUnitRequest.methods={aggregator_InstallableUnitRequest_m_isBranchEnabled, aggregator_InstallableUnitRequest_m_resolveAsSingleton, aggregator_InstallableUnitRequest_m_resolveAvailableVersions, aggregator_InstallableUnitRequest_m_resolveAsSingleton, aggregator_InstallableUnitRequest_m_isMappedRepositoryBroken}

# aggregator_Aggregation class attributes and methods
aggregator_Aggregation_label: Property = Property(name="label", type=StringType)
aggregator_Aggregation_buildRoot: Property = Property(name="buildRoot", type=StringType)
aggregator_Aggregation_packedStrategy: Property = Property(name="packedStrategy", type=StringType)
aggregator_Aggregation_sendmail: Property = Property(name="sendmail", type=BooleanType)
aggregator_Aggregation_type: Property = Property(name="type", type=StringType)
aggregator_Aggregation_mavenResult: Property = Property(name="mavenResult", type=BooleanType)
aggregator_Aggregation_m_getAllMetadataRepositoryReferences: Method = Method(name="getAllMetadataRepositoryReferences", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Aggregation_m_getValidationSets: Method = Method(name="getValidationSets", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Aggregation_m_getAllContributions: Method = Method(name="getAllContributions", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Aggregation.attributes={aggregator_Aggregation_sendmail, aggregator_Aggregation_mavenResult, aggregator_Aggregation_packedStrategy, aggregator_Aggregation_buildRoot, aggregator_Aggregation_type, aggregator_Aggregation_label}
aggregator_Aggregation.methods={aggregator_Aggregation_m_getAllContributions, aggregator_Aggregation_m_getAllMetadataRepositoryReferences, aggregator_Aggregation_m_getValidationSets}

# DescriptionProvider class attributes and methods

# StatusProvider class attributes and methods

# InfosProvider class attributes and methods

# aggregator_ValidationSet class attributes and methods
aggregator_ValidationSet_abstract: Property = Property(name="abstract", type=BooleanType)
aggregator_ValidationSet_extension: Property = Property(name="extension", type=BooleanType)
aggregator_ValidationSet_label: Property = Property(name="label", type=StringType)
aggregator_ValidationSet_m_getAllValidationRepositories: Method = Method(name="getAllValidationRepositories", parameters={}, type=MetadataRepositoryReference)
aggregator_ValidationSet_m_getAllContributions: Method = Method(name="getAllContributions", parameters={}, type=StringType)
aggregator_ValidationSet_m_getDeclaredContributions: Method = Method(name="getDeclaredContributions", parameters={}, type=StringType)
aggregator_ValidationSet_m_getDeclaredValidationRepositories: Method = Method(name="getDeclaredValidationRepositories", parameters={}, type=MetadataRepositoryReference)
aggregator_ValidationSet_m_isExtensionOf: Method = Method(name="isExtensionOf", parameters={Parameter(name='validationSet')}, type=BooleanType)
aggregator_ValidationSet.attributes={aggregator_ValidationSet_abstract, aggregator_ValidationSet_label, aggregator_ValidationSet_extension}
aggregator_ValidationSet.methods={aggregator_ValidationSet_m_getDeclaredValidationRepositories, aggregator_ValidationSet_m_isExtensionOf, aggregator_ValidationSet_m_getAllValidationRepositories, aggregator_ValidationSet_m_getAllContributions, aggregator_ValidationSet_m_getDeclaredContributions}

# aggregator_Configuration class attributes and methods
aggregator_Configuration_operatingSystem: Property = Property(name="operatingSystem", type=StringType)
aggregator_Configuration_windowSystem: Property = Property(name="windowSystem", type=StringType)
aggregator_Configuration_architecture: Property = Property(name="architecture", type=StringType)
aggregator_Configuration_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
aggregator_Configuration_m_getOSGiEnvironmentString: Method = Method(name="getOSGiEnvironmentString", parameters={}, type=StringType)
aggregator_Configuration.attributes={aggregator_Configuration_architecture, aggregator_Configuration_operatingSystem, aggregator_Configuration_windowSystem}
aggregator_Configuration.methods={aggregator_Configuration_m_getName, aggregator_Configuration_m_getOSGiEnvironmentString}

# aggregator_CustomCategory class attributes and methods
aggregator_CustomCategory_identifier: Property = Property(name="identifier", type=StringType)
aggregator_CustomCategory_label: Property = Property(name="label", type=StringType)
aggregator_CustomCategory_description: Property = Property(name="description", type=StringType)
aggregator_CustomCategory.attributes={aggregator_CustomCategory_identifier, aggregator_CustomCategory_description, aggregator_CustomCategory_label}

# aggregator_Contact class attributes and methods
aggregator_Contact_name: Property = Property(name="name", type=StringType)
aggregator_Contact_email: Property = Property(name="email", type=StringType)
aggregator_Contact.attributes={aggregator_Contact_email, aggregator_Contact_name}

# aggregator_MavenMapping class attributes and methods
aggregator_MavenMapping_namePattern: Property = Property(name="namePattern", type=StringType)
aggregator_MavenMapping_groupId: Property = Property(name="groupId", type=StringType)
aggregator_MavenMapping_artifactId: Property = Property(name="artifactId", type=StringType)
aggregator_MavenMapping_m_map: Method = Method(name="map", parameters={Parameter(name='installableUnitID')}, type=StringType)
aggregator_MavenMapping.attributes={aggregator_MavenMapping_namePattern, aggregator_MavenMapping_groupId, aggregator_MavenMapping_artifactId}
aggregator_MavenMapping.methods={aggregator_MavenMapping_m_map}

# aggregator_AvailableVersionsHeader class attributes and methods

# aggregator_Bundle class attributes and methods

# MappedUnit class attributes and methods

# aggregator_Category class attributes and methods
aggregator_Category_labelOverride: Property = Property(name="labelOverride", type=StringType)
aggregator_Category.attributes={aggregator_Category_labelOverride}

# aggregator_ChildrenProvider class attributes and methods

# EnabledStatusProvider class attributes and methods

# aggregator_Contribution class attributes and methods
aggregator_Contribution_label: Property = Property(name="label", type=StringType)
aggregator_Contribution_m_getRepositories: Method = Method(name="getRepositories", parameters={Parameter(name='enabledOnly')}, type=StringType)
aggregator_Contribution_m_getAllMavenMappings: Method = Method(name="getAllMavenMappings", parameters={}, type=StringType)
aggregator_Contribution.attributes={aggregator_Contribution_label}
aggregator_Contribution.methods={aggregator_Contribution_m_getAllMavenMappings, aggregator_Contribution_m_getRepositories}

# IdentificationProvider class attributes and methods

# aggregator_MappedRepository class attributes and methods
aggregator_MappedRepository_mirrorArtifacts: Property = Property(name="mirrorArtifacts", type=BooleanType)
aggregator_MappedRepository_categoryPrefix: Property = Property(name="categoryPrefix", type=StringType)
aggregator_MappedRepository_m_getMapRules: Method = Method(name="getMapRules", parameters={Parameter(name='enabledOnly')}, type=MapRule)
aggregator_MappedRepository_m_getUnits: Method = Method(name="getUnits", parameters={Parameter(name='enabledOnly')}, type=MappedUnit)
aggregator_MappedRepository_m_isMapExclusive: Method = Method(name="isMapExclusive", parameters={}, type=BooleanType)
aggregator_MappedRepository.attributes={aggregator_MappedRepository_categoryPrefix, aggregator_MappedRepository_mirrorArtifacts}
aggregator_MappedRepository.methods={aggregator_MappedRepository_m_getMapRules, aggregator_MappedRepository_m_isMapExclusive, aggregator_MappedRepository_m_getUnits}

# aggregator_Feature class attributes and methods

# aggregator_DescriptionProvider class attributes and methods
aggregator_DescriptionProvider_description: Property = Property(name="description", type=StringType)
aggregator_DescriptionProvider.attributes={aggregator_DescriptionProvider_description}

# aggregator_EnabledStatusProvider class attributes and methods
aggregator_EnabledStatusProvider_branchEnabled: Property = Property(name="branchEnabled", type=BooleanType)
aggregator_EnabledStatusProvider_enabled: Property = Property(name="enabled", type=BooleanType)
aggregator_EnabledStatusProvider.attributes={aggregator_EnabledStatusProvider_branchEnabled, aggregator_EnabledStatusProvider_enabled}

# aggregator_ExclusionRule class attributes and methods

# MapRule class attributes and methods

# aggregator_IdentificationProvider class attributes and methods
aggregator_IdentificationProvider_m_getIdentification: Method = Method(name="getIdentification", parameters={}, type=StringType)
aggregator_IdentificationProvider.methods={aggregator_IdentificationProvider_m_getIdentification}

# aggregator_InfosProvider class attributes and methods
aggregator_InfosProvider_errors: Property = Property(name="errors", type=StringType)
aggregator_InfosProvider_warnings: Property = Property(name="warnings", type=StringType)
aggregator_InfosProvider_infos: Property = Property(name="infos", type=StringType)
aggregator_InfosProvider.attributes={aggregator_InfosProvider_warnings, aggregator_InfosProvider_errors, aggregator_InfosProvider_infos}

# aggregator_LabelProvider class attributes and methods
aggregator_LabelProvider_label: Property = Property(name="label", type=StringType)
aggregator_LabelProvider.attributes={aggregator_LabelProvider_label}

# MetadataRepositoryReference class attributes and methods

# aggregator_Product class attributes and methods

# aggregator_StatusProvider class attributes and methods

# aggregator_MapRule class attributes and methods

# aggregator_MappedUnit class attributes and methods
aggregator_MappedUnit_m_getRequirement: Method = Method(name="getRequirement", parameters={}, type=StringType)
aggregator_MappedUnit_m_getFilter: Method = Method(name="getFilter", parameters={})
aggregator_MappedUnit.methods={aggregator_MappedUnit_m_getRequirement, aggregator_MappedUnit_m_getFilter}

# InstallableUnitRequest class attributes and methods

# aggregator_MavenItem class attributes and methods
aggregator_MavenItem_groupId: Property = Property(name="groupId", type=StringType)
aggregator_MavenItem_artifactId: Property = Property(name="artifactId", type=StringType)
aggregator_MavenItem.attributes={aggregator_MavenItem_artifactId, aggregator_MavenItem_groupId}

# aggregator_MetadataRepositoryReference class attributes and methods
aggregator_MetadataRepositoryReference_location: Property = Property(name="location", type=StringType)
aggregator_MetadataRepositoryReference_nature: Property = Property(name="nature", type=StringType)
aggregator_MetadataRepositoryReference_m_getAggregation: Method = Method(name="getAggregation", parameters={}, type=StringType)
aggregator_MetadataRepositoryReference_m_isBranchEnabled: Method = Method(name="isBranchEnabled", parameters={}, type=BooleanType)
aggregator_MetadataRepositoryReference_m_getResolvedLocation: Method = Method(name="getResolvedLocation", parameters={}, type=StringType)
aggregator_MetadataRepositoryReference_m_startRepositoryLoad: Method = Method(name="startRepositoryLoad", parameters={Parameter(name='forceReload')})
aggregator_MetadataRepositoryReference_m_cancelRepositoryLoad: Method = Method(name="cancelRepositoryLoad", parameters={})
aggregator_MetadataRepositoryReference_m_onRepositoryLoad: Method = Method(name="onRepositoryLoad", parameters={})
aggregator_MetadataRepositoryReference.attributes={aggregator_MetadataRepositoryReference_nature, aggregator_MetadataRepositoryReference_location}
aggregator_MetadataRepositoryReference.methods={aggregator_MetadataRepositoryReference_m_onRepositoryLoad, aggregator_MetadataRepositoryReference_m_isBranchEnabled, aggregator_MetadataRepositoryReference_m_startRepositoryLoad, aggregator_MetadataRepositoryReference_m_getResolvedLocation, aggregator_MetadataRepositoryReference_m_getAggregation, aggregator_MetadataRepositoryReference_m_cancelRepositoryLoad}

# aggregator_MetadataRepository class attributes and methods

# aggregator_Property class attributes and methods
aggregator_Property_key: Property = Property(name="key", type=StringType)
aggregator_Property_value: Property = Property(name="value", type=StringType)
aggregator_Property.attributes={aggregator_Property_value, aggregator_Property_key}

# aggregator_Status class attributes and methods
aggregator_Status_code: Property = Property(name="code", type=StringType)
aggregator_Status_message: Property = Property(name="message", type=StringType)
aggregator_Status.attributes={aggregator_Status_code, aggregator_Status_message}

# aggregator_ValidConfigurationsRule class attributes and methods

# IUDetails class attributes and methods

# aggregator_p2view_Bundle class attributes and methods

# IUPresentationWithDetails class attributes and methods

# aggregator_p2view_Bundles class attributes and methods

# Bundle class attributes and methods

# aggregator_p2view_Category class attributes and methods
aggregator_p2view_Category_m_getNotNullCategoryContainer: Method = Method(name="getNotNullCategoryContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullProductContainer: Method = Method(name="getNotNullProductContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_Category_m_isNested: Method = Method(name="isNested", parameters={}, type=BooleanType)
aggregator_p2view_Category.methods={aggregator_p2view_Category_m_getNotNullBundleContainer, aggregator_p2view_Category_m_isNested, aggregator_p2view_Category_m_getNotNullProductContainer, aggregator_p2view_Category_m_getNotNullCategoryContainer, aggregator_p2view_Category_m_getNotNullFeatureContainer, aggregator_p2view_Category_m_getNotNullFragmentContainer}

# IUPresentation class attributes and methods

# Categories class attributes and methods

# Features class attributes and methods

# Products class attributes and methods

# Bundles class attributes and methods

# Fragments class attributes and methods

# aggregator_p2view_IUDetails class attributes and methods

# Requirements class attributes and methods

# aggregator_p2view_Categories class attributes and methods

# Category class attributes and methods

# aggregator_p2view_Feature class attributes and methods
aggregator_p2view_Feature_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_Feature_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_Feature_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_Feature.methods={aggregator_p2view_Feature_m_getNotNullFragmentContainer, aggregator_p2view_Feature_m_getNotNullFeatureContainer, aggregator_p2view_Feature_m_getNotNullBundleContainer}

# aggregator_p2view_Features class attributes and methods

# Feature class attributes and methods

# aggregator_p2view_Fragment class attributes and methods

# aggregator_p2view_Fragments class attributes and methods

# Fragment class attributes and methods

# aggregator_p2view_InstallableUnits class attributes and methods
aggregator_p2view_InstallableUnits_m_getNotNullCategoryContainer: Method = Method(name="getNotNullCategoryContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullProductContainer: Method = Method(name="getNotNullProductContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits_m_getNotNullMiscellaneousContainer: Method = Method(name="getNotNullMiscellaneousContainer", parameters={}, type=StringType)
aggregator_p2view_InstallableUnits.methods={aggregator_p2view_InstallableUnits_m_getNotNullFeatureContainer, aggregator_p2view_InstallableUnits_m_getNotNullMiscellaneousContainer, aggregator_p2view_InstallableUnits_m_getNotNullFragmentContainer, aggregator_p2view_InstallableUnits_m_getNotNullProductContainer, aggregator_p2view_InstallableUnits_m_getNotNullBundleContainer, aggregator_p2view_InstallableUnits_m_getNotNullCategoryContainer}

# Miscellaneous class attributes and methods

# ProvidedCapabilities class attributes and methods

# Properties class attributes and methods

# Touchpoints class attributes and methods

# p2view_aggregator_IUpdateDescriptor class attributes and methods

# p2view_aggregator_ICopyright class attributes and methods

# Licenses class attributes and methods

# aggregator_p2view_IUPresentation class attributes and methods
aggregator_p2view_IUPresentation_id: Property = Property(name="id", type=StringType)
aggregator_p2view_IUPresentation_version: Property = Property(name="version", type=StringType)
aggregator_p2view_IUPresentation_name: Property = Property(name="name", type=StringType)
aggregator_p2view_IUPresentation_label: Property = Property(name="label", type=StringType)
aggregator_p2view_IUPresentation_description: Property = Property(name="description", type=StringType)
aggregator_p2view_IUPresentation_type: Property = Property(name="type", type=StringType)
aggregator_p2view_IUPresentation_filter: Property = Property(name="filter", type=StringType)
aggregator_p2view_IUPresentation.attributes={aggregator_p2view_IUPresentation_type, aggregator_p2view_IUPresentation_label, aggregator_p2view_IUPresentation_name, aggregator_p2view_IUPresentation_filter, aggregator_p2view_IUPresentation_description, aggregator_p2view_IUPresentation_id, aggregator_p2view_IUPresentation_version}

# p2view_aggregator_IInstallableUnit class attributes and methods

# aggregator_p2view_IUPresentationWithDetails class attributes and methods
aggregator_p2view_IUPresentationWithDetails_detailsResolved: Property = Property(name="detailsResolved", type=StringType)
aggregator_p2view_IUPresentationWithDetails.attributes={aggregator_p2view_IUPresentationWithDetails_detailsResolved}

# p2view_IUPresentation class attributes and methods

# p2view_IUDetails class attributes and methods

# aggregator_p2view_Licenses class attributes and methods

# p2view_aggregator_ILicense class attributes and methods

# aggregator_p2view_Requirements class attributes and methods

# aggregator_p2view_RepositoryBrowser class attributes and methods
aggregator_p2view_RepositoryBrowser_loading: Property = Property(name="loading", type=BooleanType)
aggregator_p2view_RepositoryBrowser.attributes={aggregator_p2view_RepositoryBrowser_loading}

# RequirementWrapper class attributes and methods

# MetadataRepositoryStructuredView class attributes and methods

# aggregator_p2view_MetadataRepositoryStructuredView class attributes and methods
aggregator_p2view_MetadataRepositoryStructuredView_name: Property = Property(name="name", type=StringType)
aggregator_p2view_MetadataRepositoryStructuredView_loaded: Property = Property(name="loaded", type=BooleanType)
aggregator_p2view_MetadataRepositoryStructuredView_location: Property = Property(name="location", type=StringType)
aggregator_p2view_MetadataRepositoryStructuredView.attributes={aggregator_p2view_MetadataRepositoryStructuredView_location, aggregator_p2view_MetadataRepositoryStructuredView_name, aggregator_p2view_MetadataRepositoryStructuredView_loaded}

# aggregator_p2view_RequirementWrapper class attributes and methods

# IRequirement class attributes and methods

# InstallableUnits class attributes and methods

# p2view_aggregator_MetadataRepository class attributes and methods

# RepositoryReferences class attributes and methods

# aggregator_p2view_Miscellaneous class attributes and methods

# OtherIU class attributes and methods

# aggregator_p2view_OtherIU class attributes and methods

# aggregator_p2view_Product class attributes and methods
aggregator_p2view_Product_m_getNotNullFeatureContainer: Method = Method(name="getNotNullFeatureContainer", parameters={}, type=StringType)
aggregator_p2view_Product_m_getNotNullBundleContainer: Method = Method(name="getNotNullBundleContainer", parameters={}, type=StringType)
aggregator_p2view_Product_m_getNotNullFragmentContainer: Method = Method(name="getNotNullFragmentContainer", parameters={}, type=StringType)
aggregator_p2view_Product.methods={aggregator_p2view_Product_m_getNotNullFeatureContainer, aggregator_p2view_Product_m_getNotNullBundleContainer, aggregator_p2view_Product_m_getNotNullFragmentContainer}

# aggregator_p2view_Products class attributes and methods

# Product class attributes and methods

# aggregator_p2view_Properties class attributes and methods

# p2view_aggregator_Property class attributes and methods

# aggregator_p2view_ProvidedCapabilities class attributes and methods

# ProvidedCapabilityWrapper class attributes and methods

# aggregator_p2view_ProvidedCapabilityWrapper class attributes and methods

# IProvidedCapability class attributes and methods

# LabelProvider class attributes and methods

# p2view_aggregator_IProvidedCapability class attributes and methods

# aggregator_p2view_RepositoryReferences class attributes and methods

# p2view_aggregator_IRepositoryReference class attributes and methods

# p2view_aggregator_IRequirement class attributes and methods

# aggregator_p2view_Touchpoints class attributes and methods

# p2view_aggregator_ITouchpointType class attributes and methods

# p2view_aggregator_ITouchpointData class attributes and methods

# Relationships
availableVersions10: BinaryAssociation = BinaryAssociation(
    name="availableVersions10",
    ends={
        Property(name="aggregator_AvailableVersion", type=aggregator_AvailableVersionsHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_AvailableVersionsHeader", type=aggregator_AvailableVersion, multiplicity=Multiplicity(0, 9999))
    }
)
installableUnitRequest11: BinaryAssociation = BinaryAssociation(
    name="installableUnitRequest11",
    ends={
        Property(name="InstallableUnitRequest", type=aggregator_AvailableVersionsHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="availableVersionsHeader", type=aggregator_InstallableUnitRequest, multiplicity=Multiplicity(1, 1))
    }
)
validationSets0: BinaryAssociation = BinaryAssociation(
    name="validationSets0",
    ends={
        Property(name="aggregator_ValidationSet", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregation", type=aggregator_ValidationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations1: BinaryAssociation = BinaryAssociation(
    name="configurations1",
    ends={
        Property(name="aggregator_Configuration", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregation2", type=aggregator_Configuration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customCategories3: BinaryAssociation = BinaryAssociation(
    name="customCategories3",
    ends={
        Property(name="aggregator_CustomCategory", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregation4", type=aggregator_CustomCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contacts5: BinaryAssociation = BinaryAssociation(
    name="contacts5",
    ends={
        Property(name="Contact", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregation", type=aggregator_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildmaster6: BinaryAssociation = BinaryAssociation(
    name="buildmaster6",
    ends={
        Property(name="aggregator_Contact", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregation7", type=aggregator_Contact, multiplicity=Multiplicity(0, 1))
    }
)
mavenMappings8: BinaryAssociation = BinaryAssociation(
    name="mavenMappings8",
    ends={
        Property(name="aggregator_MavenMapping", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Aggregation9", type=aggregator_MavenMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregation12: BinaryAssociation = BinaryAssociation(
    name="aggregation12",
    ends={
        Property(name="Aggregation", type=aggregator_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts", type=aggregator_Aggregation, multiplicity=Multiplicity(1, 1))
    }
)
repositories13: BinaryAssociation = BinaryAssociation(
    name="repositories13",
    ends={
        Property(name="aggregator_MappedRepository", type=aggregator_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Contribution", type=aggregator_MappedRepository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contacts14: BinaryAssociation = BinaryAssociation(
    name="contacts14",
    ends={
        Property(name="aggregator_Contact16", type=aggregator_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Contribution15", type=aggregator_Contact, multiplicity=Multiplicity(0, 9999))
    }
)
mavenMappings17: BinaryAssociation = BinaryAssociation(
    name="mavenMappings17",
    ends={
        Property(name="aggregator_MavenMapping19", type=aggregator_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_Contribution18", type=aggregator_MavenMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories20: BinaryAssociation = BinaryAssociation(
    name="categories20",
    ends={
        Property(name="CustomCategory", type=aggregator_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=aggregator_CustomCategory, multiplicity=Multiplicity(0, 9999))
    }
)
products25: BinaryAssociation = BinaryAssociation(
    name="products25",
    ends={
        Property(name="aggregator_Product", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository26", type=aggregator_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bundles27: BinaryAssociation = BinaryAssociation(
    name="bundles27",
    ends={
        Property(name="aggregator_Bundle", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository28", type=aggregator_Bundle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features29: BinaryAssociation = BinaryAssociation(
    name="features29",
    ends={
        Property(name="aggregator_Feature", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository30", type=aggregator_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features21: BinaryAssociation = BinaryAssociation(
    name="features21",
    ends={
        Property(name="Feature", type=aggregator_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="categories", type=aggregator_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
availableVersionsHeader22: BinaryAssociation = BinaryAssociation(
    name="availableVersionsHeader22",
    ends={
        Property(name="AvailableVersionsHeader", type=aggregator_InstallableUnitRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="installableUnitRequest", type=aggregator_AvailableVersionsHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
availableVersions23: BinaryAssociation = BinaryAssociation(
    name="availableVersions23",
    ends={
        Property(name="aggregator_AvailableVersion24", type=aggregator_InstallableUnitRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_InstallableUnitRequest", type=aggregator_AvailableVersion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
status38: BinaryAssociation = BinaryAssociation(
    name="status38",
    ends={
        Property(name="aggregator_Status", type=aggregator_StatusProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_StatusProvider", type=aggregator_Status, multiplicity=Multiplicity(1, 1))
    }
)
categories31: BinaryAssociation = BinaryAssociation(
    name="categories31",
    ends={
        Property(name="aggregator_Category", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository32", type=aggregator_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapRules33: BinaryAssociation = BinaryAssociation(
    name="mapRules33",
    ends={
        Property(name="aggregator_MapRule", type=aggregator_MappedRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedRepository34", type=aggregator_MapRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validConfigurations35: BinaryAssociation = BinaryAssociation(
    name="validConfigurations35",
    ends={
        Property(name="aggregator_Configuration36", type=aggregator_MappedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MappedUnit", type=aggregator_Configuration, multiplicity=Multiplicity(0, 9999))
    }
)
metadataRepository37: BinaryAssociation = BinaryAssociation(
    name="metadataRepository37",
    ends={
        Property(name="aggregator_MetadataRepository", type=aggregator_MetadataRepositoryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_MetadataRepositoryReference", type=aggregator_MetadataRepository, multiplicity=Multiplicity(0, 1))
    }
)
contributions39: BinaryAssociation = BinaryAssociation(
    name="contributions39",
    ends={
        Property(name="aggregator_Contribution41", type=aggregator_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_ValidationSet40", type=aggregator_Contribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationRepositories42: BinaryAssociation = BinaryAssociation(
    name="validationRepositories42",
    ends={
        Property(name="aggregator_MetadataRepositoryReference44", type=aggregator_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_ValidationSet43", type=aggregator_MetadataRepositoryReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends46: BinaryAssociation = BinaryAssociation(
    name="extends46",
    ends={
        Property(name="aggregator_ValidationSet47", type=aggregator_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_ValidationSet45", type=aggregator_ValidationSet, multiplicity=Multiplicity(0, 9999))
    }
)
validConfigurations48: BinaryAssociation = BinaryAssociation(
    name="validConfigurations48",
    ends={
        Property(name="aggregator_Configuration49", type=aggregator_ValidConfigurationsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_ValidConfigurationsRule", type=aggregator_Configuration, multiplicity=Multiplicity(0, 9999))
    }
)
fragmentContainer58: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer58",
    ends={
        Property(name="Fragments", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category59", type=Fragments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iuDetails60: BinaryAssociation = BinaryAssociation(
    name="iuDetails60",
    ends={
        Property(name="IUDetails", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category61", type=IUDetails, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bundles50: BinaryAssociation = BinaryAssociation(
    name="bundles50",
    ends={
        Property(name="Bundle", type=aggregator_p2view_Bundles, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Bundles", type=Bundle, multiplicity=Multiplicity(0, 9999))
    }
)
categoryContainer51: BinaryAssociation = BinaryAssociation(
    name="categoryContainer51",
    ends={
        Property(name="Categories", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category", type=Categories, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureContainer52: BinaryAssociation = BinaryAssociation(
    name="featureContainer52",
    ends={
        Property(name="Features", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category53", type=Features, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
productContainer54: BinaryAssociation = BinaryAssociation(
    name="productContainer54",
    ends={
        Property(name="Products", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category55", type=Products, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bundleContainer56: BinaryAssociation = BinaryAssociation(
    name="bundleContainer56",
    ends={
        Property(name="Bundles", type=aggregator_p2view_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Category57", type=Bundles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
miscellaneousContainer90: BinaryAssociation = BinaryAssociation(
    name="miscellaneousContainer90",
    ends={
        Property(name="Miscellaneous", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits91", type=Miscellaneous, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requirementsContainer92: BinaryAssociation = BinaryAssociation(
    name="requirementsContainer92",
    ends={
        Property(name="Requirements", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails", type=Requirements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
categories62: BinaryAssociation = BinaryAssociation(
    name="categories62",
    ends={
        Property(name="Category", type=aggregator_p2view_Categories, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Categories", type=Category, multiplicity=Multiplicity(0, 9999))
    }
)
featureContainer63: BinaryAssociation = BinaryAssociation(
    name="featureContainer63",
    ends={
        Property(name="Features64", type=aggregator_p2view_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Feature", type=Features, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bundleContainer65: BinaryAssociation = BinaryAssociation(
    name="bundleContainer65",
    ends={
        Property(name="Bundles67", type=aggregator_p2view_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Feature66", type=Bundles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragmentContainer68: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer68",
    ends={
        Property(name="Fragments70", type=aggregator_p2view_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Feature69", type=Fragments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features71: BinaryAssociation = BinaryAssociation(
    name="features71",
    ends={
        Property(name="Feature72", type=aggregator_p2view_Features, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Features", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
fragments73: BinaryAssociation = BinaryAssociation(
    name="fragments73",
    ends={
        Property(name="Fragment", type=aggregator_p2view_Fragments, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Fragments", type=Fragment, multiplicity=Multiplicity(0, 9999))
    }
)
allIUs74: BinaryAssociation = BinaryAssociation(
    name="allIUs74",
    ends={
        Property(name="IUPresentation", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits", type=IUPresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryContainer75: BinaryAssociation = BinaryAssociation(
    name="categoryContainer75",
    ends={
        Property(name="Categories77", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits76", type=Categories, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureContainer78: BinaryAssociation = BinaryAssociation(
    name="featureContainer78",
    ends={
        Property(name="Features80", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits79", type=Features, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
productContainer81: BinaryAssociation = BinaryAssociation(
    name="productContainer81",
    ends={
        Property(name="Products83", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits82", type=Products, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bundleContainer84: BinaryAssociation = BinaryAssociation(
    name="bundleContainer84",
    ends={
        Property(name="Bundles86", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits85", type=Bundles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragmentContainer87: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer87",
    ends={
        Property(name="Fragments89", type=aggregator_p2view_InstallableUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_InstallableUnits88", type=Fragments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
providedCapabilitiesContainer93: BinaryAssociation = BinaryAssociation(
    name="providedCapabilitiesContainer93",
    ends={
        Property(name="ProvidedCapabilities", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails94", type=ProvidedCapabilities, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertiesContainer95: BinaryAssociation = BinaryAssociation(
    name="propertiesContainer95",
    ends={
        Property(name="Properties", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails96", type=Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
touchpointsContainer97: BinaryAssociation = BinaryAssociation(
    name="touchpointsContainer97",
    ends={
        Property(name="Touchpoints", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails98", type=Touchpoints, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateDescriptor99: BinaryAssociation = BinaryAssociation(
    name="updateDescriptor99",
    ends={
        Property(name="p2view_aggregator_IUpdateDescriptor", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails100", type=p2view_aggregator_IUpdateDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
copyright101: BinaryAssociation = BinaryAssociation(
    name="copyright101",
    ends={
        Property(name="p2view_aggregator_ICopyright", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails102", type=p2view_aggregator_ICopyright, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
licensesContainer103: BinaryAssociation = BinaryAssociation(
    name="licensesContainer103",
    ends={
        Property(name="Licenses", type=aggregator_p2view_IUDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUDetails104", type=Licenses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
installableUnit105: BinaryAssociation = BinaryAssociation(
    name="installableUnit105",
    ends={
        Property(name="p2view_aggregator_IInstallableUnit", type=aggregator_p2view_IUPresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_IUPresentation", type=p2view_aggregator_IInstallableUnit, multiplicity=Multiplicity(0, 1))
    }
)
licenses106: BinaryAssociation = BinaryAssociation(
    name="licenses106",
    ends={
        Property(name="p2view_aggregator_ILicense", type=aggregator_p2view_Licenses, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Licenses", type=p2view_aggregator_ILicense, multiplicity=Multiplicity(0, 9999))
    }
)
requirements130: BinaryAssociation = BinaryAssociation(
    name="requirements130",
    ends={
        Property(name="RequirementWrapper", type=aggregator_p2view_Requirements, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Requirements", type=RequirementWrapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories107: BinaryAssociation = BinaryAssociation(
    name="repositories107",
    ends={
        Property(name="MetadataRepositoryStructuredView", type=aggregator_p2view_RepositoryBrowser, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_RepositoryBrowser", type=MetadataRepositoryStructuredView, multiplicity=Multiplicity(0, 9999))
    }
)
installableUnitList108: BinaryAssociation = BinaryAssociation(
    name="installableUnitList108",
    ends={
        Property(name="InstallableUnits", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView", type=InstallableUnits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties109: BinaryAssociation = BinaryAssociation(
    name="properties109",
    ends={
        Property(name="Properties111", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView110", type=Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metadataRepository112: BinaryAssociation = BinaryAssociation(
    name="metadataRepository112",
    ends={
        Property(name="p2view_aggregator_MetadataRepository", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView113", type=p2view_aggregator_MetadataRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
repositoryReferences114: BinaryAssociation = BinaryAssociation(
    name="repositoryReferences114",
    ends={
        Property(name="RepositoryReferences", type=aggregator_p2view_MetadataRepositoryStructuredView, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_MetadataRepositoryStructuredView115", type=RepositoryReferences, multiplicity=Multiplicity(0, 1))
    }
)
others116: BinaryAssociation = BinaryAssociation(
    name="others116",
    ends={
        Property(name="OtherIU", type=aggregator_p2view_Miscellaneous, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Miscellaneous", type=OtherIU, multiplicity=Multiplicity(0, 9999))
    }
)
featureContainer117: BinaryAssociation = BinaryAssociation(
    name="featureContainer117",
    ends={
        Property(name="Features118", type=aggregator_p2view_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Product", type=Features, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bundleContainer119: BinaryAssociation = BinaryAssociation(
    name="bundleContainer119",
    ends={
        Property(name="Bundles121", type=aggregator_p2view_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Product120", type=Bundles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragmentContainer122: BinaryAssociation = BinaryAssociation(
    name="fragmentContainer122",
    ends={
        Property(name="Fragments124", type=aggregator_p2view_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Product123", type=Fragments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
products125: BinaryAssociation = BinaryAssociation(
    name="products125",
    ends={
        Property(name="Product", type=aggregator_p2view_Products, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Products", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
propertyList126: BinaryAssociation = BinaryAssociation(
    name="propertyList126",
    ends={
        Property(name="p2view_aggregator_Property", type=aggregator_p2view_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Properties", type=p2view_aggregator_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedCapabilities127: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities127",
    ends={
        Property(name="ProvidedCapabilityWrapper", type=aggregator_p2view_ProvidedCapabilities, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_ProvidedCapabilities", type=ProvidedCapabilityWrapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genuine128: BinaryAssociation = BinaryAssociation(
    name="genuine128",
    ends={
        Property(name="p2view_aggregator_IProvidedCapability", type=aggregator_p2view_ProvidedCapabilityWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_ProvidedCapabilityWrapper", type=p2view_aggregator_IProvidedCapability, multiplicity=Multiplicity(1, 1))
    }
)
repositoryReferences129: BinaryAssociation = BinaryAssociation(
    name="repositoryReferences129",
    ends={
        Property(name="p2view_aggregator_IRepositoryReference", type=aggregator_p2view_RepositoryReferences, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_RepositoryReferences", type=p2view_aggregator_IRepositoryReference, multiplicity=Multiplicity(0, 9999))
    }
)
genuine131: BinaryAssociation = BinaryAssociation(
    name="genuine131",
    ends={
        Property(name="p2view_aggregator_IRequirement", type=aggregator_p2view_RequirementWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_RequirementWrapper", type=p2view_aggregator_IRequirement, multiplicity=Multiplicity(1, 1))
    }
)
touchpointType132: BinaryAssociation = BinaryAssociation(
    name="touchpointType132",
    ends={
        Property(name="p2view_aggregator_ITouchpointType", type=aggregator_p2view_Touchpoints, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Touchpoints", type=p2view_aggregator_ITouchpointType, multiplicity=Multiplicity(0, 1))
    }
)
touchpointDataList133: BinaryAssociation = BinaryAssociation(
    name="touchpointDataList133",
    ends={
        Property(name="p2view_aggregator_ITouchpointData", type=aggregator_p2view_Touchpoints, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregator_p2view_Touchpoints134", type=p2view_aggregator_ITouchpointData, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_aggregator_Aggregation_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_Aggregation)
gen_aggregator_Aggregation_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_Aggregation)
gen_aggregator_Aggregation_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_Aggregation)
gen_aggregator_CustomCategory_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_CustomCategory)
gen_aggregator_CustomCategory_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_CustomCategory)
gen_aggregator_Bundle_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Bundle)
gen_aggregator_Category_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Category)
gen_aggregator_Configuration_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_Configuration)
gen_aggregator_Contribution_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_Contribution)
gen_aggregator_Contribution_IdentificationProvider = Generalization(general=IdentificationProvider, specific=aggregator_Contribution)
gen_aggregator_Feature_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Feature)
gen_aggregator_ExclusionRule_MapRule = Generalization(general=MapRule, specific=aggregator_ExclusionRule)
gen_aggregator_InstallableUnitRequest_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_InstallableUnitRequest)
gen_aggregator_InstallableUnitRequest_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_InstallableUnitRequest)
gen_aggregator_InstallableUnitRequest_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_InstallableUnitRequest)
gen_aggregator_MappedRepository_MetadataRepositoryReference = Generalization(general=MetadataRepositoryReference, specific=aggregator_MappedRepository)
gen_aggregator_MappedRepository_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_MappedRepository)
gen_aggregator_MappedRepository_IdentificationProvider = Generalization(general=IdentificationProvider, specific=aggregator_MappedRepository)
gen_aggregator_MappedUnit_InstallableUnitRequest = Generalization(general=InstallableUnitRequest, specific=aggregator_MappedUnit)
gen_aggregator_MappedUnit_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_MappedUnit)
gen_aggregator_MappedUnit_IdentificationProvider = Generalization(general=IdentificationProvider, specific=aggregator_MappedUnit)
gen_aggregator_MapRule_InstallableUnitRequest = Generalization(general=InstallableUnitRequest, specific=aggregator_MapRule)
gen_aggregator_MapRule_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_MapRule)
gen_aggregator_MapRule_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_MapRule)
gen_aggregator_MavenMapping_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_MavenMapping)
gen_aggregator_MavenMapping_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_MavenMapping)
gen_aggregator_MetadataRepositoryReference_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_MetadataRepositoryReference)
gen_aggregator_MetadataRepositoryReference_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_MetadataRepositoryReference)
gen_aggregator_MetadataRepositoryReference_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_MetadataRepositoryReference)
gen_aggregator_Product_MappedUnit = Generalization(general=MappedUnit, specific=aggregator_Product)
gen_aggregator_ValidationSet_EnabledStatusProvider = Generalization(general=EnabledStatusProvider, specific=aggregator_ValidationSet)
gen_aggregator_ValidationSet_DescriptionProvider = Generalization(general=DescriptionProvider, specific=aggregator_ValidationSet)
gen_aggregator_ValidationSet_StatusProvider = Generalization(general=StatusProvider, specific=aggregator_ValidationSet)
gen_aggregator_ValidationSet_InfosProvider = Generalization(general=InfosProvider, specific=aggregator_ValidationSet)
gen_aggregator_ValidationSet_IdentificationProvider = Generalization(general=IdentificationProvider, specific=aggregator_ValidationSet)
gen_aggregator_ValidConfigurationsRule_MapRule = Generalization(general=MapRule, specific=aggregator_ValidConfigurationsRule)
gen_aggregator_p2view_Bundle_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_Bundle)
gen_aggregator_p2view_Category_IUPresentation = Generalization(general=IUPresentation, specific=aggregator_p2view_Category)
gen_aggregator_p2view_Feature_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_Feature)
gen_aggregator_p2view_Fragment_Bundle = Generalization(general=Bundle, specific=aggregator_p2view_Fragment)
gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUPresentation = Generalization(general=p2view_IUPresentation, specific=aggregator_p2view_IUPresentationWithDetails)
gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUDetails = Generalization(general=p2view_IUDetails, specific=aggregator_p2view_IUPresentationWithDetails)
gen_aggregator_p2view_RequirementWrapper_IRequirement = Generalization(general=IRequirement, specific=aggregator_p2view_RequirementWrapper)
gen_aggregator_p2view_RequirementWrapper_LabelProvider = Generalization(general=LabelProvider, specific=aggregator_p2view_RequirementWrapper)
gen_aggregator_p2view_OtherIU_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_OtherIU)
gen_aggregator_p2view_Product_IUPresentationWithDetails = Generalization(general=IUPresentationWithDetails, specific=aggregator_p2view_Product)
gen_aggregator_p2view_ProvidedCapabilityWrapper_IProvidedCapability = Generalization(general=IProvidedCapability, specific=aggregator_p2view_ProvidedCapabilityWrapper)
gen_aggregator_p2view_ProvidedCapabilityWrapper_LabelProvider = Generalization(general=LabelProvider, specific=aggregator_p2view_ProvidedCapabilityWrapper)

# Domain Model
domain_model = DomainModel(
    name="aggregator",
    types={aggregator_AvailableVersion, aggregator_InstallableUnitRequest, aggregator_Aggregation, DescriptionProvider, StatusProvider, InfosProvider, aggregator_ValidationSet, aggregator_Configuration, aggregator_CustomCategory, aggregator_Contact, aggregator_MavenMapping, aggregator_AvailableVersionsHeader, aggregator_Bundle, MappedUnit, aggregator_Category, aggregator_ChildrenProvider, EnabledStatusProvider, aggregator_Contribution, IdentificationProvider, aggregator_MappedRepository, aggregator_Feature, aggregator_DescriptionProvider, aggregator_EnabledStatusProvider, aggregator_ExclusionRule, MapRule, aggregator_IdentificationProvider, aggregator_InfosProvider, aggregator_LabelProvider, MetadataRepositoryReference, aggregator_Product, aggregator_StatusProvider, aggregator_MapRule, aggregator_MappedUnit, InstallableUnitRequest, aggregator_MavenItem, aggregator_MetadataRepositoryReference, aggregator_MetadataRepository, aggregator_Property, aggregator_Status, aggregator_ValidConfigurationsRule, IUDetails, aggregator_p2view_Bundle, IUPresentationWithDetails, aggregator_p2view_Bundles, Bundle, aggregator_p2view_Category, IUPresentation, Categories, Features, Products, Bundles, Fragments, aggregator_p2view_IUDetails, Requirements, aggregator_p2view_Categories, Category, aggregator_p2view_Feature, aggregator_p2view_Features, Feature, aggregator_p2view_Fragment, aggregator_p2view_Fragments, Fragment, aggregator_p2view_InstallableUnits, Miscellaneous, ProvidedCapabilities, Properties, Touchpoints, p2view_aggregator_IUpdateDescriptor, p2view_aggregator_ICopyright, Licenses, aggregator_p2view_IUPresentation, p2view_aggregator_IInstallableUnit, aggregator_p2view_IUPresentationWithDetails, p2view_IUPresentation, p2view_IUDetails, aggregator_p2view_Licenses, p2view_aggregator_ILicense, aggregator_p2view_Requirements, aggregator_p2view_RepositoryBrowser, RequirementWrapper, MetadataRepositoryStructuredView, aggregator_p2view_MetadataRepositoryStructuredView, aggregator_p2view_RequirementWrapper, IRequirement, InstallableUnits, p2view_aggregator_MetadataRepository, RepositoryReferences, aggregator_p2view_Miscellaneous, OtherIU, aggregator_p2view_OtherIU, aggregator_p2view_Product, aggregator_p2view_Products, Product, aggregator_p2view_Properties, p2view_aggregator_Property, aggregator_p2view_ProvidedCapabilities, ProvidedCapabilityWrapper, aggregator_p2view_ProvidedCapabilityWrapper, IProvidedCapability, LabelProvider, p2view_aggregator_IProvidedCapability, aggregator_p2view_RepositoryReferences, p2view_aggregator_IRepositoryReference, p2view_aggregator_IRequirement, aggregator_p2view_Touchpoints, p2view_aggregator_ITouchpointType, p2view_aggregator_ITouchpointData, OperatingSystem, AggregationType, Architecture, AvailableFrom, InstallableUnitType, PackedStrategy, StatusCode, VersionMatch, WindowSystem},
    associations={availableVersions10, installableUnitRequest11, validationSets0, configurations1, customCategories3, contacts5, buildmaster6, mavenMappings8, aggregation12, repositories13, contacts14, mavenMappings17, categories20, products25, bundles27, features29, features21, availableVersionsHeader22, availableVersions23, status38, categories31, mapRules33, validConfigurations35, metadataRepository37, contributions39, validationRepositories42, extends46, validConfigurations48, fragmentContainer58, iuDetails60, bundles50, categoryContainer51, featureContainer52, productContainer54, bundleContainer56, miscellaneousContainer90, requirementsContainer92, categories62, featureContainer63, bundleContainer65, fragmentContainer68, features71, fragments73, allIUs74, categoryContainer75, featureContainer78, productContainer81, bundleContainer84, fragmentContainer87, providedCapabilitiesContainer93, propertiesContainer95, touchpointsContainer97, updateDescriptor99, copyright101, licensesContainer103, installableUnit105, licenses106, requirements130, repositories107, installableUnitList108, properties109, metadataRepository112, repositoryReferences114, others116, featureContainer117, bundleContainer119, fragmentContainer122, products125, propertyList126, providedCapabilities127, genuine128, repositoryReferences129, genuine131, touchpointType132, touchpointDataList133},
    generalizations={gen_aggregator_Aggregation_DescriptionProvider, gen_aggregator_Aggregation_StatusProvider, gen_aggregator_Aggregation_InfosProvider, gen_aggregator_CustomCategory_StatusProvider, gen_aggregator_CustomCategory_InfosProvider, gen_aggregator_Bundle_MappedUnit, gen_aggregator_Category_MappedUnit, gen_aggregator_Configuration_EnabledStatusProvider, gen_aggregator_Contribution_EnabledStatusProvider, gen_aggregator_Contribution_DescriptionProvider, gen_aggregator_Contribution_StatusProvider, gen_aggregator_Contribution_InfosProvider, gen_aggregator_Contribution_IdentificationProvider, gen_aggregator_Feature_MappedUnit, gen_aggregator_ExclusionRule_MapRule, gen_aggregator_InstallableUnitRequest_StatusProvider, gen_aggregator_InstallableUnitRequest_InfosProvider, gen_aggregator_InstallableUnitRequest_DescriptionProvider, gen_aggregator_MappedRepository_MetadataRepositoryReference, gen_aggregator_MappedRepository_DescriptionProvider, gen_aggregator_MappedRepository_IdentificationProvider, gen_aggregator_MappedUnit_InstallableUnitRequest, gen_aggregator_MappedUnit_EnabledStatusProvider, gen_aggregator_MappedUnit_IdentificationProvider, gen_aggregator_MapRule_InstallableUnitRequest, gen_aggregator_MapRule_DescriptionProvider, gen_aggregator_MapRule_EnabledStatusProvider, gen_aggregator_MavenMapping_StatusProvider, gen_aggregator_MavenMapping_InfosProvider, gen_aggregator_MetadataRepositoryReference_EnabledStatusProvider, gen_aggregator_MetadataRepositoryReference_StatusProvider, gen_aggregator_MetadataRepositoryReference_InfosProvider, gen_aggregator_Product_MappedUnit, gen_aggregator_ValidationSet_EnabledStatusProvider, gen_aggregator_ValidationSet_DescriptionProvider, gen_aggregator_ValidationSet_StatusProvider, gen_aggregator_ValidationSet_InfosProvider, gen_aggregator_ValidationSet_IdentificationProvider, gen_aggregator_ValidConfigurationsRule_MapRule, gen_aggregator_p2view_Bundle_IUPresentationWithDetails, gen_aggregator_p2view_Category_IUPresentation, gen_aggregator_p2view_Feature_IUPresentationWithDetails, gen_aggregator_p2view_Fragment_Bundle, gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUPresentation, gen_aggregator_p2view_IUPresentationWithDetails_p2view_IUDetails, gen_aggregator_p2view_RequirementWrapper_IRequirement, gen_aggregator_p2view_RequirementWrapper_LabelProvider, gen_aggregator_p2view_OtherIU_IUPresentationWithDetails, gen_aggregator_p2view_Product_IUPresentationWithDetails, gen_aggregator_p2view_ProvidedCapabilityWrapper_IProvidedCapability, gen_aggregator_p2view_ProvidedCapabilityWrapper_LabelProvider},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)