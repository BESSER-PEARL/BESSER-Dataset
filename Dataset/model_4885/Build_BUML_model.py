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
Disposition: Enumeration = Enumeration(
    name="Disposition",
    literals={
            EnumerationLiteral(name="required"),
			EnumerationLiteral(name="desired"),
			EnumerationLiteral(name="unbiassed"),
			EnumerationLiteral(name="undesired"),
			EnumerationLiteral(name="rejected")
    }
)

ConflictResolution: Enumeration = Enumeration(
    name="ConflictResolution",
    literals={
            EnumerationLiteral(name="keep"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="replace"),
			EnumerationLiteral(name="fail")
    }
)

SplitStyle: Enumeration = Enumeration(
    name="SplitStyle",
    literals={
            EnumerationLiteral(name="unquoted"),
			EnumerationLiteral(name="quoted"),
			EnumerationLiteral(name="groups")
    }
)

FilterAdviceOperation: Enumeration = Enumeration(
    name="FilterAdviceOperation",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="REPLACE")
    }
)

# Classes
build_IBuildUnit = Class(name="build::IBuildUnit", is_abstract=True)
ICapability = Class(name="ICapability")
PropertyScope = Class(name="PropertyScope")
IGenericUnit = Class(name="IGenericUnit")
build_IBuildPart = Class(name="build::IBuildPart", is_abstract=True)
build_IRequiredCapability = Class(name="build::IRequiredCapability", is_abstract=True)
build_ICapability = Class(name="build::ICapability", is_abstract=True)
build_PartCapability = Class(name="build::PartCapability")
build_IProvidedCapability = Class(name="build::IProvidedCapability", is_abstract=True)
build_IArtifactsPart = Class(name="build::IArtifactsPart", is_abstract=True)
IBuildPart = Class(name="IBuildPart")
build_IPathGroup = Class(name="build::IPathGroup", is_abstract=True)
build_IActionPart = Class(name="build::IActionPart", is_abstract=True)
IClosurePart = Class(name="IClosurePart")
build_IActionResult = Class(name="build::IActionResult", is_abstract=True)
build_IUpToDatePolicy = Class(name="build::IUpToDatePolicy", is_abstract=True)
build_IClosure = Class(name="build::IClosure", is_abstract=True)
IPrerequisites = Class(name="IPrerequisites")
IAdvise = Class(name="IAdvise")
build_IPrerequisites = Class(name="build::IPrerequisites", is_abstract=True)
build_IRequirement = Class(name="build::IRequirement", is_abstract=True)
build_IPartGroup = Class(name="build::IPartGroup", is_abstract=True)
build_PartRequirement = Class(name="build::PartRequirement")
IRequirement = Class(name="IRequirement")
build_IProducedPart = Class(name="build::IProducedPart", is_abstract=True)
build_IResultingParts = Class(name="build::IResultingParts", is_abstract=True)
IActionResult = Class(name="IActionResult")
build_IClosurePart = Class(name="build::IClosurePart", is_abstract=True)
IClosure = Class(name="IClosure")
build_Requirement = Class(name="build::Requirement")
build_ResultingPathGroup = Class(name="build::ResultingPathGroup")
build_StringProperties = Class(name="build::StringProperties")
build_PropertyScope = Class(name="build::PropertyScope", is_abstract=True)
build_IGenericUnit = Class(name="build::IGenericUnit", is_abstract=True)
build_context_IBuildContext = Class(name="build::context::IBuildContext", is_abstract=True)
IUnitRequest = Class(name="IUnitRequest")
IResolution = Class(name="IResolution")
context_build_IBuildUnit = Class(name="context::build::IBuildUnit")
IResolver = Class(name="IResolver")
build_context_IResolution = Class(name="build::context::IResolution", is_abstract=True)
context_build_IRequiredCapability = Class(name="context::build::IRequiredCapability")
context_build_ICapability = Class(name="context::build::ICapability")
ImportOptions = Class(name="ImportOptions")
build_context_ResolutionOptions = Class(name="build::context::ResolutionOptions", is_abstract=True)
build_context_ImportOptions = Class(name="build::context::ImportOptions", is_abstract=True)
IMaterializer = Class(name="IMaterializer")
build_resolver_BestChoice = Class(name="build::resolver::BestChoice")
build_resolver_IMetaDataTranslatorFactory = Class(name="build::resolver::IMetaDataTranslatorFactory", is_abstract=True)
build_runtime_BuildRuntime = Class(name="build::runtime::BuildRuntime")
UpToDateExtension = Class(name="UpToDateExtension")
MaterializerExtension = Class(name="MaterializerExtension")
MetaDataTranslatorFactoryExtension = Class(name="MetaDataTranslatorFactoryExtension")
ResolverExtension = Class(name="ResolverExtension")
build_runtime_UpToDateExtension = Class(name="build::runtime::UpToDateExtension")
IHumanSelectable = Class(name="IHumanSelectable")
runtime_build_IUpToDatePolicy = Class(name="runtime::build::IUpToDatePolicy")
build_runtime_IHumanSelectable = Class(name="build::runtime::IHumanSelectable", is_abstract=True)
IExtension = Class(name="IExtension")
build_runtime_MaterializerExtension = Class(name="build::runtime::MaterializerExtension")
build_runtime_MetaDataTranslatorFactoryExtension = Class(name="build::runtime::MetaDataTranslatorFactoryExtension")
IMetaDataTranslatorFactory = Class(name="IMetaDataTranslatorFactory")
build_runtime_ResolverExtension = Class(name="build::runtime::ResolverExtension")
build_runtime_IExtension = Class(name="build::runtime::IExtension", is_abstract=True)
build_resolver_IResolver = Class(name="build::resolver::IResolver", is_abstract=True)
IExpr = Class(name="IExpr")
build_resolver_IResourceMap = Class(name="build::resolver::IResourceMap", is_abstract=True)
build_resolver_ILocation = Class(name="build::resolver::ILocation", is_abstract=True)
build_resolver_ResolverGroup = Class(name="build::resolver::ResolverGroup", is_abstract=True)
build_resolver_FirstChoice = Class(name="build::resolver::FirstChoice")
ResolverGroup = Class(name="ResolverGroup")
build_properties_ToUpper = Class(name="build::properties::ToUpper")
build_properties_toLower = Class(name="build::properties::toLower")
build_properties_replace = Class(name="build::properties::replace")
build_resolver_IMetaDataTranslator = Class(name="build::resolver::IMetaDataTranslator", is_abstract=True)
build_resolver_IEFSBasedAccess = Class(name="build::resolver::IEFSBasedAccess", is_abstract=True)
build_resolver_DefaultResolver = Class(name="build::resolver::DefaultResolver", is_abstract=True)
IMetaDataTranslator = Class(name="IMetaDataTranslator")
build_resolver_WorspaceResolver = Class(name="build::resolver::WorspaceResolver")
EFSResolver = Class(name="EFSResolver")
build_resolver_EFSResolver = Class(name="build::resolver::EFSResolver")
resolver_DefaultResolver = Class(name="resolver::DefaultResolver")
resolver_IEFSBasedAccess = Class(name="resolver::IEFSBasedAccess")
build_resolver_P2Resolver = Class(name="build::resolver::P2Resolver")
build_resolver_IResolutionContext = Class(name="build::resolver::IResolutionContext", is_abstract=True)
build_materializer_IMaterializer = Class(name="build::materializer::IMaterializer", is_abstract=True)
build_materializer_FileSystemMaterializer = Class(name="build::materializer::FileSystemMaterializer")
build_materializer_P2Materializer = Class(name="build::materializer::P2Materializer")
build_materializer_WorkspaceMaterializer = Class(name="build::materializer::WorkspaceMaterializer")
build_properties_IExpr = Class(name="build::properties::IExpr", is_abstract=True)
build_properties_Literal = Class(name="build::properties::Literal")
build_properties_IFunction = Class(name="build::properties::IFunction", is_abstract=True)
build_properties_PropertyRef = Class(name="build::properties::PropertyRef")
IFunction = Class(name="IFunction")
build_properties_Format = Class(name="build::properties::Format")
build_command_BooleanAdvice = Class(name="build::command::BooleanAdvice")
build_command_UnsetAdvice = Class(name="build::command::UnsetAdvice")
build_command_NewInstanceAdvice = Class(name="build::command::NewInstanceAdvice")
AdviceGroup = Class(name="AdviceGroup")
Match = Class(name="Match")
build_properties_Match = Class(name="build::properties::Match")
build_properties_Split = Class(name="build::properties::Split")
build_command_IUnitRequest = Class(name="build::command::IUnitRequest", is_abstract=True)
ResolutionOptions = Class(name="ResolutionOptions")
build_command_BuildUnitCommand = Class(name="build::command::BuildUnitCommand", is_abstract=True)
command_build_PropertyScope = Class(name="command::build::PropertyScope")
build_command_IAdvise = Class(name="build::command::IAdvise", is_abstract=True)
ContextNodeSelector = Class(name="ContextNodeSelector")
build_command_ImportCommand = Class(name="build::command::ImportCommand")
BuildUnitCommand = Class(name="BuildUnitCommand")
build_command_PropertyAdvice = Class(name="build::command::PropertyAdvice")
build_command_ContextNodeSelector = Class(name="build::command::ContextNodeSelector", is_abstract=True)
build_command_StringAdvice = Class(name="build::command::StringAdvice")
build_command_VersionAdvice = Class(name="build::command::VersionAdvice")
build_command_VersionRangeAdvice = Class(name="build::command::VersionRangeAdvice")
build_command_InvokeCommand = Class(name="build::command::InvokeCommand")
build_command_FilterAdvice = Class(name="build::command::FilterAdvice")
IFilter = Class(name="IFilter")
build_command_AdviceGroup = Class(name="build::command::AdviceGroup")
build_filter_IFilter = Class(name="build::filter::IFilter", is_abstract=True)
build_filter_OSGiBasedFilter = Class(name="build::filter::OSGiBasedFilter")
build_filter_AndFilter = Class(name="build::filter::AndFilter")
FilterGroup = Class(name="FilterGroup")
build_filter_OrFilter = Class(name="build::filter::OrFilter")
build_filter_FilterGroup = Class(name="build::filter::FilterGroup")
build_filter_RegexpFilter = Class(name="build::filter::RegexpFilter")
SinglePropertyFilter = Class(name="SinglePropertyFilter")
build_filter_SinglePropertyFilter = Class(name="build::filter::SinglePropertyFilter")
build_filter_SimplePatternFIlter = Class(name="build::filter::SimplePatternFIlter")

# build_IBuildUnit class attributes and methods
build_IBuildUnit_filter: Property = Property(name="filter", type=StringType)
build_IBuildUnit_circularityAllowed: Property = Property(name="circularityAllowed", type=BooleanType)
build_IBuildUnit_instanceLocation: Property = Property(name="instanceLocation", type=StringType)
build_IBuildUnit.attributes={build_IBuildUnit_instanceLocation, build_IBuildUnit_circularityAllowed, build_IBuildUnit_filter}

# ICapability class attributes and methods

# PropertyScope class attributes and methods

# IGenericUnit class attributes and methods

# build_IBuildPart class attributes and methods
build_IBuildPart_name: Property = Property(name="name", type=StringType)
build_IBuildPart.attributes={build_IBuildPart_name}

# build_IRequiredCapability class attributes and methods
build_IRequiredCapability_namespace: Property = Property(name="namespace", type=StringType)
build_IRequiredCapability_name: Property = Property(name="name", type=StringType)
build_IRequiredCapability_range: Property = Property(name="range", type=StringType)
build_IRequiredCapability_filter: Property = Property(name="filter", type=StringType)
build_IRequiredCapability.attributes={build_IRequiredCapability_name, build_IRequiredCapability_filter, build_IRequiredCapability_namespace, build_IRequiredCapability_range}

# build_ICapability class attributes and methods
build_ICapability_namespace: Property = Property(name="namespace", type=StringType)
build_ICapability_name: Property = Property(name="name", type=StringType)
build_ICapability_version: Property = Property(name="version", type=StringType)
build_ICapability_m_satisfies: Method = Method(name="satisfies", parameters={Parameter(name='required')}, type=BooleanType)
build_ICapability.attributes={build_ICapability_name, build_ICapability_version, build_ICapability_namespace}
build_ICapability.methods={build_ICapability_m_satisfies}

# build_PartCapability class attributes and methods

# build_IProvidedCapability class attributes and methods

# build_IArtifactsPart class attributes and methods

# IBuildPart class attributes and methods

# build_IPathGroup class attributes and methods
build_IPathGroup_basePath: Property = Property(name="basePath", type=StringType)
build_IPathGroup_paths: Property = Property(name="paths", type=StringType)
build_IPathGroup.attributes={build_IPathGroup_basePath, build_IPathGroup_paths}

# build_IActionPart class attributes and methods

# IClosurePart class attributes and methods

# build_IActionResult class attributes and methods

# build_IUpToDatePolicy class attributes and methods

# build_IClosure class attributes and methods
build_IClosure_executeOnce: Property = Property(name="executeOnce", type=BooleanType)
build_IClosure.attributes={build_IClosure_executeOnce}

# IPrerequisites class attributes and methods

# IAdvise class attributes and methods

# build_IPrerequisites class attributes and methods
build_IPrerequisites_alias: Property = Property(name="alias", type=StringType)
build_IPrerequisites_rebasePath: Property = Property(name="rebasePath", type=StringType)
build_IPrerequisites.attributes={build_IPrerequisites_rebasePath, build_IPrerequisites_alias}

# build_IRequirement class attributes and methods
build_IRequirement_memberName: Property = Property(name="memberName", type=StringType)
build_IRequirement_alias: Property = Property(name="alias", type=StringType)
build_IRequirement_contributor: Property = Property(name="contributor", type=BooleanType)
build_IRequirement_filter: Property = Property(name="filter", type=StringType)
build_IRequirement_includePattern: Property = Property(name="includePattern", type=StringType)
build_IRequirement_excludePattern: Property = Property(name="excludePattern", type=StringType)
build_IRequirement.attributes={build_IRequirement_memberName, build_IRequirement_includePattern, build_IRequirement_alias, build_IRequirement_filter, build_IRequirement_excludePattern, build_IRequirement_contributor}

# build_IPartGroup class attributes and methods

# build_PartRequirement class attributes and methods

# IRequirement class attributes and methods

# build_IProducedPart class attributes and methods

# build_IResultingParts class attributes and methods

# IActionResult class attributes and methods

# build_IClosurePart class attributes and methods

# IClosure class attributes and methods

# build_Requirement class attributes and methods

# build_ResultingPathGroup class attributes and methods

# build_StringProperties class attributes and methods
build_StringProperties_key: Property = Property(name="key", type=StringType)
build_StringProperties_value: Property = Property(name="value", type=StringType)
build_StringProperties_immutable: Property = Property(name="immutable", type=BooleanType)
build_StringProperties.attributes={build_StringProperties_key, build_StringProperties_immutable, build_StringProperties_value}

# build_PropertyScope class attributes and methods
build_PropertyScope_unsetProperties: Property = Property(name="unsetProperties", type=StringType)
build_PropertyScope.attributes={build_PropertyScope_unsetProperties}

# build_IGenericUnit class attributes and methods

# build_context_IBuildContext class attributes and methods

# IUnitRequest class attributes and methods

# IResolution class attributes and methods

# context_build_IBuildUnit class attributes and methods

# IResolver class attributes and methods

# build_context_IResolution class attributes and methods

# context_build_IRequiredCapability class attributes and methods

# context_build_ICapability class attributes and methods

# ImportOptions class attributes and methods

# build_context_ResolutionOptions class attributes and methods
build_context_ResolutionOptions_source: Property = Property(name="source", type=StringType)
build_context_ResolutionOptions_mutable: Property = Property(name="mutable", type=StringType)
build_context_ResolutionOptions_branchTagPath: Property = Property(name="branchTagPath", type=StringType)
build_context_ResolutionOptions_timestamp: Property = Property(name="timestamp", type=StringType)
build_context_ResolutionOptions_revision: Property = Property(name="revision", type=StringType)
build_context_ResolutionOptions_resolverFilter: Property = Property(name="resolverFilter", type=StringType)
build_context_ResolutionOptions_filterGroups: Property = Property(name="filterGroups", type=BooleanType)
build_context_ResolutionOptions_overlayPath: Property = Property(name="overlayPath", type=StringType)
build_context_ResolutionOptions_includeParts: Property = Property(name="includeParts", type=StringType)
build_context_ResolutionOptions_excludeParts: Property = Property(name="excludeParts", type=StringType)
build_context_ResolutionOptions_prune: Property = Property(name="prune", type=BooleanType)
build_context_ResolutionOptions.attributes={build_context_ResolutionOptions_includeParts, build_context_ResolutionOptions_overlayPath, build_context_ResolutionOptions_revision, build_context_ResolutionOptions_excludeParts, build_context_ResolutionOptions_filterGroups, build_context_ResolutionOptions_prune, build_context_ResolutionOptions_resolverFilter, build_context_ResolutionOptions_mutable, build_context_ResolutionOptions_timestamp, build_context_ResolutionOptions_source, build_context_ResolutionOptions_branchTagPath}

# build_context_ImportOptions class attributes and methods
build_context_ImportOptions_suffix: Property = Property(name="suffix", type=StringType)
build_context_ImportOptions_location: Property = Property(name="location", type=StringType)
build_context_ImportOptions_conflictResolution: Property = Property(name="conflictResolution", type=StringType)
build_context_ImportOptions_resourcePath: Property = Property(name="resourcePath", type=StringType)
build_context_ImportOptions_unpack: Property = Property(name="unpack", type=BooleanType)
build_context_ImportOptions_expand: Property = Property(name="expand", type=BooleanType)
build_context_ImportOptions.attributes={build_context_ImportOptions_location, build_context_ImportOptions_expand, build_context_ImportOptions_unpack, build_context_ImportOptions_conflictResolution, build_context_ImportOptions_suffix, build_context_ImportOptions_resourcePath}

# IMaterializer class attributes and methods

# build_resolver_BestChoice class attributes and methods

# build_resolver_IMetaDataTranslatorFactory class attributes and methods
build_resolver_IMetaDataTranslatorFactory_m_getTranslator: Method = Method(name="getTranslator", parameters={Parameter(name='resolver'), Parameter(name='nameSpace')}, type=StringType)
build_resolver_IMetaDataTranslatorFactory.methods={build_resolver_IMetaDataTranslatorFactory_m_getTranslator}

# build_runtime_BuildRuntime class attributes and methods

# UpToDateExtension class attributes and methods

# MaterializerExtension class attributes and methods

# MetaDataTranslatorFactoryExtension class attributes and methods

# ResolverExtension class attributes and methods

# build_runtime_UpToDateExtension class attributes and methods

# IHumanSelectable class attributes and methods

# runtime_build_IUpToDatePolicy class attributes and methods

# build_runtime_IHumanSelectable class attributes and methods
build_runtime_IHumanSelectable_label: Property = Property(name="label", type=StringType)
build_runtime_IHumanSelectable_typeName: Property = Property(name="typeName", type=StringType)
build_runtime_IHumanSelectable.attributes={build_runtime_IHumanSelectable_typeName, build_runtime_IHumanSelectable_label}

# IExtension class attributes and methods

# build_runtime_MaterializerExtension class attributes and methods

# build_runtime_MetaDataTranslatorFactoryExtension class attributes and methods

# IMetaDataTranslatorFactory class attributes and methods

# build_runtime_ResolverExtension class attributes and methods

# build_runtime_IExtension class attributes and methods

# build_resolver_IResolver class attributes and methods
build_resolver_IResolver_failOnError: Property = Property(name="failOnError", type=BooleanType)
build_resolver_IResolver_filter: Property = Property(name="filter", type=StringType)
build_resolver_IResolver_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='IResolutionContext')}, type=StringType)
build_resolver_IResolver.attributes={build_resolver_IResolver_filter, build_resolver_IResolver_failOnError}
build_resolver_IResolver.methods={build_resolver_IResolver_m_resolve}

# IExpr class attributes and methods

# build_resolver_IResourceMap class attributes and methods
build_resolver_IResourceMap_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='request')}, type=StringType)
build_resolver_IResourceMap.methods={build_resolver_IResourceMap_m_lookup}

# build_resolver_ILocation class attributes and methods

# build_resolver_ResolverGroup class attributes and methods

# build_resolver_FirstChoice class attributes and methods

# ResolverGroup class attributes and methods

# build_properties_ToUpper class attributes and methods

# build_properties_toLower class attributes and methods

# build_properties_replace class attributes and methods

# build_resolver_IMetaDataTranslator class attributes and methods
build_resolver_IMetaDataTranslator_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='resolver')}, type=StringType)
build_resolver_IMetaDataTranslator.methods={build_resolver_IMetaDataTranslator_m_resolve}

# build_resolver_IEFSBasedAccess class attributes and methods
build_resolver_IEFSBasedAccess_m_getFileStore: Method = Method(name="getFileStore", parameters={}, type=StringType)
build_resolver_IEFSBasedAccess.methods={build_resolver_IEFSBasedAccess_m_getFileStore}

# build_resolver_DefaultResolver class attributes and methods

# IMetaDataTranslator class attributes and methods

# build_resolver_WorspaceResolver class attributes and methods

# EFSResolver class attributes and methods

# build_resolver_EFSResolver class attributes and methods

# resolver_DefaultResolver class attributes and methods

# resolver_IEFSBasedAccess class attributes and methods

# build_resolver_P2Resolver class attributes and methods
build_resolver_P2Resolver_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='IResolutionContext')}, type=StringType)
build_resolver_P2Resolver.methods={build_resolver_P2Resolver_m_resolve}

# build_resolver_IResolutionContext class attributes and methods

# build_materializer_IMaterializer class attributes and methods

# build_materializer_FileSystemMaterializer class attributes and methods

# build_materializer_P2Materializer class attributes and methods

# build_materializer_WorkspaceMaterializer class attributes and methods

# build_properties_IExpr class attributes and methods
build_properties_IExpr_m_eval: Method = Method(name="eval", parameters={Parameter(name='scope')}, type=StringType)
build_properties_IExpr.methods={build_properties_IExpr_m_eval}

# build_properties_Literal class attributes and methods
build_properties_Literal_value: Property = Property(name="value", type=StringType)
build_properties_Literal.attributes={build_properties_Literal_value}

# build_properties_IFunction class attributes and methods

# build_properties_PropertyRef class attributes and methods

# IFunction class attributes and methods

# build_properties_Format class attributes and methods
build_properties_Format_formatString: Property = Property(name="formatString", type=StringType)
build_properties_Format.attributes={build_properties_Format_formatString}

# build_command_BooleanAdvice class attributes and methods
build_command_BooleanAdvice_value: Property = Property(name="value", type=BooleanType)
build_command_BooleanAdvice.attributes={build_command_BooleanAdvice_value}

# build_command_UnsetAdvice class attributes and methods

# build_command_NewInstanceAdvice class attributes and methods
build_command_NewInstanceAdvice_clazz: Property = Property(name="clazz", type=StringType)
build_command_NewInstanceAdvice.attributes={build_command_NewInstanceAdvice_clazz}

# AdviceGroup class attributes and methods

# Match class attributes and methods

# build_properties_Match class attributes and methods
build_properties_Match_pattern: Property = Property(name="pattern", type=StringType)
build_properties_Match_replacement: Property = Property(name="replacement", type=StringType)
build_properties_Match_quotePattern: Property = Property(name="quotePattern", type=BooleanType)
build_properties_Match.attributes={build_properties_Match_pattern, build_properties_Match_replacement, build_properties_Match_quotePattern}

# build_properties_Split class attributes and methods
build_properties_Split_pattern: Property = Property(name="pattern", type=StringType)
build_properties_Split_style: Property = Property(name="style", type=StringType)
build_properties_Split_limit: Property = Property(name="limit", type=IntegerType)
build_properties_Split.attributes={build_properties_Split_pattern, build_properties_Split_limit, build_properties_Split_style}

# build_command_IUnitRequest class attributes and methods
build_command_IUnitRequest_name: Property = Property(name="name", type=StringType)
build_command_IUnitRequest_nameSpace: Property = Property(name="nameSpace", type=StringType)
build_command_IUnitRequest_range: Property = Property(name="range", type=StringType)
build_command_IUnitRequest.attributes={build_command_IUnitRequest_range, build_command_IUnitRequest_name, build_command_IUnitRequest_nameSpace}

# ResolutionOptions class attributes and methods

# build_command_BuildUnitCommand class attributes and methods

# command_build_PropertyScope class attributes and methods

# build_command_IAdvise class attributes and methods

# ContextNodeSelector class attributes and methods

# build_command_ImportCommand class attributes and methods

# BuildUnitCommand class attributes and methods

# build_command_PropertyAdvice class attributes and methods

# build_command_ContextNodeSelector class attributes and methods

# build_command_StringAdvice class attributes and methods
build_command_StringAdvice_value: Property = Property(name="value", type=StringType)
build_command_StringAdvice.attributes={build_command_StringAdvice_value}

# build_command_VersionAdvice class attributes and methods
build_command_VersionAdvice_version: Property = Property(name="version", type=StringType)
build_command_VersionAdvice.attributes={build_command_VersionAdvice_version}

# build_command_VersionRangeAdvice class attributes and methods
build_command_VersionRangeAdvice_versionRange: Property = Property(name="versionRange", type=StringType)
build_command_VersionRangeAdvice.attributes={build_command_VersionRangeAdvice_versionRange}

# build_command_InvokeCommand class attributes and methods
build_command_InvokeCommand_action: Property = Property(name="action", type=StringType)
build_command_InvokeCommand.attributes={build_command_InvokeCommand_action}

# build_command_FilterAdvice class attributes and methods
build_command_FilterAdvice_filterOp: Property = Property(name="filterOp", type=StringType)
build_command_FilterAdvice.attributes={build_command_FilterAdvice_filterOp}

# IFilter class attributes and methods

# build_command_AdviceGroup class attributes and methods

# build_filter_IFilter class attributes and methods
build_filter_IFilter_m_match: Method = Method(name="match", parameters={Parameter(name='matched'), Parameter(name='properties')}, type=BooleanType)
build_filter_IFilter.methods={build_filter_IFilter_m_match}

# build_filter_OSGiBasedFilter class attributes and methods

# build_filter_AndFilter class attributes and methods

# FilterGroup class attributes and methods

# build_filter_OrFilter class attributes and methods

# build_filter_FilterGroup class attributes and methods

# build_filter_RegexpFilter class attributes and methods

# SinglePropertyFilter class attributes and methods

# build_filter_SinglePropertyFilter class attributes and methods
build_filter_SinglePropertyFilter_property: Property = Property(name="property", type=StringType)
build_filter_SinglePropertyFilter.attributes={build_filter_SinglePropertyFilter_property}

# build_filter_SimplePatternFIlter class attributes and methods

# Relationships
parts0: BinaryAssociation = BinaryAssociation(
    name="parts0",
    ends={
        Property(name="IBuildPart", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="buildUnit", type=build_IBuildPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCapabilities1: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilities1",
    ends={
        Property(name="build_IRequiredCapability", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnit", type=build_IRequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaRequiredCapabilities2: BinaryAssociation = BinaryAssociation(
    name="metaRequiredCapabilities2",
    ends={
        Property(name="build_IRequiredCapability4", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnit3", type=build_IRequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allRequiredCapabilities5: BinaryAssociation = BinaryAssociation(
    name="allRequiredCapabilities5",
    ends={
        Property(name="build_IRequiredCapability7", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnit6", type=build_IRequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedCapabilities8: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities8",
    ends={
        Property(name="build_ICapability", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnit9", type=build_ICapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selfCapability11: BinaryAssociation = BinaryAssociation(
    name="selfCapability11",
    ends={
        Property(name="build_IBuildUnit12", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnit10", type=build_IBuildUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partCapabilities13: BinaryAssociation = BinaryAssociation(
    name="partCapabilities13",
    ends={
        Property(name="build_PartCapability", type=build_IBuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnit14", type=build_PartCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publishedCapabilities15: BinaryAssociation = BinaryAssociation(
    name="publishedCapabilities15",
    ends={
        Property(name="PartCapability", type=build_IBuildPart, multiplicity=Multiplicity(1, 1)),
        Property(name="buildPart", type=build_PartCapability, multiplicity=Multiplicity(0, 9999))
    }
)
buildUnit16: BinaryAssociation = BinaryAssociation(
    name="buildUnit16",
    ends={
        Property(name="IBuildUnit", type=build_IBuildPart, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=build_IBuildUnit, multiplicity=Multiplicity(0, 1))
    }
)
paths17: BinaryAssociation = BinaryAssociation(
    name="paths17",
    ends={
        Property(name="build_IPathGroup", type=build_IArtifactsPart, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IArtifactsPart", type=build_IPathGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
produces18: BinaryAssociation = BinaryAssociation(
    name="produces18",
    ends={
        Property(name="IActionResult", type=build_IActionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="producedBy", type=build_IActionResult, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upToDatePolicy19: BinaryAssociation = BinaryAssociation(
    name="upToDatePolicy19",
    ends={
        Property(name="build_IUpToDatePolicy", type=build_IActionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IActionPart", type=build_IUpToDatePolicy, multiplicity=Multiplicity(0, 1))
    }
)
advice20: BinaryAssociation = BinaryAssociation(
    name="advice20",
    ends={
        Property(name="IAdvise", type=build_IClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IClosure", type=IAdvise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredParts21: BinaryAssociation = BinaryAssociation(
    name="requiredParts21",
    ends={
        Property(name="build_IRequirement", type=build_IPrerequisites, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IPrerequisites", type=build_IRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredPart22: BinaryAssociation = BinaryAssociation(
    name="requiredPart22",
    ends={
        Property(name="build_IBuildPart", type=build_PartRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="build_PartRequirement", type=build_IBuildPart, multiplicity=Multiplicity(1, 1))
    }
)
producedBy23: BinaryAssociation = BinaryAssociation(
    name="producedBy23",
    ends={
        Property(name="IActionPart", type=build_IActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="produces", type=build_IActionPart, multiplicity=Multiplicity(1, 1))
    }
)
paths24: BinaryAssociation = BinaryAssociation(
    name="paths24",
    ends={
        Property(name="build_IPathGroup25", type=build_IProducedPart, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IProducedPart", type=build_IPathGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
producedBy26: BinaryAssociation = BinaryAssociation(
    name="producedBy26",
    ends={
        Property(name="IResultingParts", type=build_IProducedPart, multiplicity=Multiplicity(1, 1)),
        Property(name="producedParts", type=build_IResultingParts, multiplicity=Multiplicity(1, 1))
    }
)
producedParts27: BinaryAssociation = BinaryAssociation(
    name="producedParts27",
    ends={
        Property(name="IProducedPart", type=build_IResultingParts, multiplicity=Multiplicity(1, 1)),
        Property(name="producedBy28", type=build_IProducedPart, multiplicity=Multiplicity(0, 9999))
    }
)
requiredCapability29: BinaryAssociation = BinaryAssociation(
    name="requiredCapability29",
    ends={
        Property(name="build_IRequiredCapability30", type=build_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Requirement", type=build_IRequiredCapability, multiplicity=Multiplicity(1, 1))
    }
)
paths31: BinaryAssociation = BinaryAssociation(
    name="paths31",
    ends={
        Property(name="build_IPathGroup32", type=build_ResultingPathGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ResultingPathGroup", type=build_IPathGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buildPart33: BinaryAssociation = BinaryAssociation(
    name="buildPart33",
    ends={
        Property(name="IBuildPart34", type=build_PartCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="publishedCapabilities", type=build_IBuildPart, multiplicity=Multiplicity(1, 1))
    }
)
properties35: BinaryAssociation = BinaryAssociation(
    name="properties35",
    ends={
        Property(name="build_StringProperties", type=build_PropertyScope, multiplicity=Multiplicity(1, 1)),
        Property(name="build_PropertyScope", type=build_StringProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
self36: BinaryAssociation = BinaryAssociation(
    name="self36",
    ends={
        Property(name="build_IPathGroup37", type=build_IGenericUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IGenericUnit", type=build_IPathGroup, multiplicity=Multiplicity(1, 1))
    }
)
requests38: BinaryAssociation = BinaryAssociation(
    name="requests38",
    ends={
        Property(name="IUnitRequest", type=build_context_IBuildContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IBuildContext", type=IUnitRequest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolutions39: BinaryAssociation = BinaryAssociation(
    name="resolutions39",
    ends={
        Property(name="IResolution", type=build_context_IBuildContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IBuildContext40", type=IResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units41: BinaryAssociation = BinaryAssociation(
    name="units41",
    ends={
        Property(name="context_build_IBuildUnit", type=build_context_IBuildContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IBuildContext42", type=context_build_IBuildUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
advice43: BinaryAssociation = BinaryAssociation(
    name="advice43",
    ends={
        Property(name="IAdvise45", type=build_context_IBuildContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IBuildContext44", type=IAdvise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolver46: BinaryAssociation = BinaryAssociation(
    name="resolver46",
    ends={
        Property(name="IResolver", type=build_context_IBuildContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IBuildContext47", type=IResolver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolves48: BinaryAssociation = BinaryAssociation(
    name="resolves48",
    ends={
        Property(name="context_build_IRequiredCapability", type=build_context_IResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IResolution", type=context_build_IRequiredCapability, multiplicity=Multiplicity(1, 1))
    }
)
resolution49: BinaryAssociation = BinaryAssociation(
    name="resolution49",
    ends={
        Property(name="context_build_ICapability", type=build_context_IResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IResolution50", type=context_build_ICapability, multiplicity=Multiplicity(0, 1))
    }
)
subResolutions51: BinaryAssociation = BinaryAssociation(
    name="subResolutions51",
    ends={
        Property(name="IResolution53", type=build_context_IResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IResolution52", type=IResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options54: BinaryAssociation = BinaryAssociation(
    name="options54",
    ends={
        Property(name="ImportOptions", type=build_context_IResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_IResolution55", type=ImportOptions, multiplicity=Multiplicity(0, 1))
    }
)
materializer56: BinaryAssociation = BinaryAssociation(
    name="materializer56",
    ends={
        Property(name="IMaterializer", type=build_context_ImportOptions, multiplicity=Multiplicity(1, 1)),
        Property(name="build_context_ImportOptions", type=IMaterializer, multiplicity=Multiplicity(0, 1))
    }
)
upToDatePolicies57: BinaryAssociation = BinaryAssociation(
    name="upToDatePolicies57",
    ends={
        Property(name="UpToDateExtension", type=build_runtime_BuildRuntime, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_BuildRuntime", type=UpToDateExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
materializers58: BinaryAssociation = BinaryAssociation(
    name="materializers58",
    ends={
        Property(name="MaterializerExtension", type=build_runtime_BuildRuntime, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_BuildRuntime59", type=MaterializerExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitTypes60: BinaryAssociation = BinaryAssociation(
    name="unitTypes60",
    ends={
        Property(name="MetaDataTranslatorFactoryExtension", type=build_runtime_BuildRuntime, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_BuildRuntime61", type=MetaDataTranslatorFactoryExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvers62: BinaryAssociation = BinaryAssociation(
    name="resolvers62",
    ends={
        Property(name="ResolverExtension", type=build_runtime_BuildRuntime, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_BuildRuntime63", type=ResolverExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance64: BinaryAssociation = BinaryAssociation(
    name="instance64",
    ends={
        Property(name="runtime_build_IUpToDatePolicy", type=build_runtime_UpToDateExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_UpToDateExtension", type=runtime_build_IUpToDatePolicy, multiplicity=Multiplicity(1, 1))
    }
)
instance65: BinaryAssociation = BinaryAssociation(
    name="instance65",
    ends={
        Property(name="IMaterializer66", type=build_runtime_MaterializerExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_MaterializerExtension", type=IMaterializer, multiplicity=Multiplicity(1, 1))
    }
)
instance67: BinaryAssociation = BinaryAssociation(
    name="instance67",
    ends={
        Property(name="IMetaDataTranslatorFactory", type=build_runtime_MetaDataTranslatorFactoryExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_MetaDataTranslatorFactoryExtension", type=IMetaDataTranslatorFactory, multiplicity=Multiplicity(0, 1))
    }
)
instance68: BinaryAssociation = BinaryAssociation(
    name="instance68",
    ends={
        Property(name="IResolver69", type=build_runtime_ResolverExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="build_runtime_ResolverExtension", type=IResolver, multiplicity=Multiplicity(1, 1))
    }
)
location70: BinaryAssociation = BinaryAssociation(
    name="location70",
    ends={
        Property(name="IExpr", type=build_resolver_IResolver, multiplicity=Multiplicity(1, 1)),
        Property(name="build_resolver_IResolver", type=IExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolvers71: BinaryAssociation = BinaryAssociation(
    name="resolvers71",
    ends={
        Property(name="IResolver72", type=build_resolver_ResolverGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="build_resolver_ResolverGroup", type=IResolver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translator73: BinaryAssociation = BinaryAssociation(
    name="translator73",
    ends={
        Property(name="IMetaDataTranslator", type=build_resolver_DefaultResolver, multiplicity=Multiplicity(1, 1)),
        Property(name="build_resolver_DefaultResolver", type=IMetaDataTranslator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operands74: BinaryAssociation = BinaryAssociation(
    name="operands74",
    ends={
        Property(name="IExpr75", type=build_properties_IFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="build_properties_IFunction", type=IExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matchers76: BinaryAssociation = BinaryAssociation(
    name="matchers76",
    ends={
        Property(name="Match", type=build_properties_replace, multiplicity=Multiplicity(1, 1)),
        Property(name="build_properties_replace", type=Match, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options77: BinaryAssociation = BinaryAssociation(
    name="options77",
    ends={
        Property(name="ResolutionOptions", type=build_command_IUnitRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_IUnitRequest", type=ResolutionOptions, multiplicity=Multiplicity(0, 1))
    }
)
requests78: BinaryAssociation = BinaryAssociation(
    name="requests78",
    ends={
        Property(name="IUnitRequest79", type=build_command_BuildUnitCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_BuildUnitCommand", type=IUnitRequest, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties80: BinaryAssociation = BinaryAssociation(
    name="properties80",
    ends={
        Property(name="command_build_PropertyScope", type=build_command_BuildUnitCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_BuildUnitCommand81", type=command_build_PropertyScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolver82: BinaryAssociation = BinaryAssociation(
    name="resolver82",
    ends={
        Property(name="IResolver84", type=build_command_BuildUnitCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_BuildUnitCommand83", type=IResolver, multiplicity=Multiplicity(0, 1))
    }
)
advice85: BinaryAssociation = BinaryAssociation(
    name="advice85",
    ends={
        Property(name="IAdvise87", type=build_command_BuildUnitCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_BuildUnitCommand86", type=IAdvise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selector88: BinaryAssociation = BinaryAssociation(
    name="selector88",
    ends={
        Property(name="ContextNodeSelector", type=build_command_IAdvise, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_IAdvise", type=ContextNodeSelector, multiplicity=Multiplicity(0, 1))
    }
)
properties89: BinaryAssociation = BinaryAssociation(
    name="properties89",
    ends={
        Property(name="command_build_PropertyScope90", type=build_command_PropertyAdvice, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_PropertyAdvice", type=command_build_PropertyScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remove91: BinaryAssociation = BinaryAssociation(
    name="remove91",
    ends={
        Property(name="IFilter", type=build_command_FilterAdvice, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_FilterAdvice", type=IFilter, multiplicity=Multiplicity(0, 1))
    }
)
add92: BinaryAssociation = BinaryAssociation(
    name="add92",
    ends={
        Property(name="IFilter94", type=build_command_FilterAdvice, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_FilterAdvice93", type=IFilter, multiplicity=Multiplicity(0, 1))
    }
)
advice95: BinaryAssociation = BinaryAssociation(
    name="advice95",
    ends={
        Property(name="IAdvise96", type=build_command_AdviceGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="build_command_AdviceGroup", type=IAdvise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters97: BinaryAssociation = BinaryAssociation(
    name="filters97",
    ends={
        Property(name="IFilter98", type=build_filter_FilterGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="build_filter_FilterGroup", type=IFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_build_IBuildUnit_ICapability = Generalization(general=ICapability, specific=build_IBuildUnit)
gen_build_IBuildUnit_PropertyScope = Generalization(general=PropertyScope, specific=build_IBuildUnit)
gen_build_IBuildUnit_IGenericUnit = Generalization(general=IGenericUnit, specific=build_IBuildUnit)
gen_build_IArtifactsPart_IBuildPart = Generalization(general=IBuildPart, specific=build_IArtifactsPart)
gen_build_IActionPart_IClosurePart = Generalization(general=IClosurePart, specific=build_IActionPart)
gen_build_IClosure_IPrerequisites = Generalization(general=IPrerequisites, specific=build_IClosure)
gen_build_IClosure_PropertyScope = Generalization(general=PropertyScope, specific=build_IClosure)
gen_build_IPrerequisites_IBuildPart = Generalization(general=IBuildPart, specific=build_IPrerequisites)
gen_build_IPartGroup_IClosurePart = Generalization(general=IClosurePart, specific=build_IPartGroup)
gen_build_PartRequirement_IRequirement = Generalization(general=IRequirement, specific=build_PartRequirement)
gen_build_IResultingParts_IActionResult = Generalization(general=IActionResult, specific=build_IResultingParts)
gen_build_IClosurePart_IClosure = Generalization(general=IClosure, specific=build_IClosurePart)
gen_build_IClosurePart_IBuildPart = Generalization(general=IBuildPart, specific=build_IClosurePart)
gen_build_Requirement_IRequirement = Generalization(general=IRequirement, specific=build_Requirement)
gen_build_ResultingPathGroup_IActionResult = Generalization(general=IActionResult, specific=build_ResultingPathGroup)
gen_build_PartCapability_ICapability = Generalization(general=ICapability, specific=build_PartCapability)
gen_build_IProducedPart_IClosurePart = Generalization(general=IClosurePart, specific=build_IProducedPart)
gen_build_resolver_BestChoice_ResolverGroup = Generalization(general=ResolverGroup, specific=build_resolver_BestChoice)
gen_build_runtime_UpToDateExtension_IHumanSelectable = Generalization(general=IHumanSelectable, specific=build_runtime_UpToDateExtension)
gen_build_runtime_IHumanSelectable_IExtension = Generalization(general=IExtension, specific=build_runtime_IHumanSelectable)
gen_build_runtime_MaterializerExtension_IHumanSelectable = Generalization(general=IHumanSelectable, specific=build_runtime_MaterializerExtension)
gen_build_runtime_MetaDataTranslatorFactoryExtension_IExtension = Generalization(general=IExtension, specific=build_runtime_MetaDataTranslatorFactoryExtension)
gen_build_runtime_ResolverExtension_IHumanSelectable = Generalization(general=IHumanSelectable, specific=build_runtime_ResolverExtension)
gen_build_resolver_ResolverGroup_IResolver = Generalization(general=IResolver, specific=build_resolver_ResolverGroup)
gen_build_resolver_FirstChoice_ResolverGroup = Generalization(general=ResolverGroup, specific=build_resolver_FirstChoice)
gen_build_properties_ToUpper_IFunction = Generalization(general=IFunction, specific=build_properties_ToUpper)
gen_build_properties_toLower_IFunction = Generalization(general=IFunction, specific=build_properties_toLower)
gen_build_properties_replace_IFunction = Generalization(general=IFunction, specific=build_properties_replace)
gen_build_resolver_DefaultResolver_IResolver = Generalization(general=IResolver, specific=build_resolver_DefaultResolver)
gen_build_resolver_WorspaceResolver_EFSResolver = Generalization(general=EFSResolver, specific=build_resolver_WorspaceResolver)
gen_build_resolver_EFSResolver_resolver_DefaultResolver = Generalization(general=resolver_DefaultResolver, specific=build_resolver_EFSResolver)
gen_build_resolver_EFSResolver_resolver_IEFSBasedAccess = Generalization(general=resolver_IEFSBasedAccess, specific=build_resolver_EFSResolver)
gen_build_resolver_P2Resolver_IResolver = Generalization(general=IResolver, specific=build_resolver_P2Resolver)
gen_build_materializer_FileSystemMaterializer_IMaterializer = Generalization(general=IMaterializer, specific=build_materializer_FileSystemMaterializer)
gen_build_materializer_P2Materializer_IMaterializer = Generalization(general=IMaterializer, specific=build_materializer_P2Materializer)
gen_build_materializer_WorkspaceMaterializer_IMaterializer = Generalization(general=IMaterializer, specific=build_materializer_WorkspaceMaterializer)
gen_build_properties_Literal_IExpr = Generalization(general=IExpr, specific=build_properties_Literal)
gen_build_properties_IFunction_IExpr = Generalization(general=IExpr, specific=build_properties_IFunction)
gen_build_properties_PropertyRef_IFunction = Generalization(general=IFunction, specific=build_properties_PropertyRef)
gen_build_properties_Format_IFunction = Generalization(general=IFunction, specific=build_properties_Format)
gen_build_command_BooleanAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_BooleanAdvice)
gen_build_command_UnsetAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_UnsetAdvice)
gen_build_command_NewInstanceAdvice_AdviceGroup = Generalization(general=AdviceGroup, specific=build_command_NewInstanceAdvice)
gen_build_properties_Split_IFunction = Generalization(general=IFunction, specific=build_properties_Split)
gen_build_command_ImportCommand_BuildUnitCommand = Generalization(general=BuildUnitCommand, specific=build_command_ImportCommand)
gen_build_command_PropertyAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_PropertyAdvice)
gen_build_command_StringAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_StringAdvice)
gen_build_command_VersionAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_VersionAdvice)
gen_build_command_VersionRangeAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_VersionRangeAdvice)
gen_build_command_InvokeCommand_BuildUnitCommand = Generalization(general=BuildUnitCommand, specific=build_command_InvokeCommand)
gen_build_command_FilterAdvice_IAdvise = Generalization(general=IAdvise, specific=build_command_FilterAdvice)
gen_build_filter_OSGiBasedFilter_IFilter = Generalization(general=IFilter, specific=build_filter_OSGiBasedFilter)
gen_build_filter_AndFilter_FilterGroup = Generalization(general=FilterGroup, specific=build_filter_AndFilter)
gen_build_filter_OrFilter_FilterGroup = Generalization(general=FilterGroup, specific=build_filter_OrFilter)
gen_build_filter_FilterGroup_IFilter = Generalization(general=IFilter, specific=build_filter_FilterGroup)
gen_build_filter_RegexpFilter_SinglePropertyFilter = Generalization(general=SinglePropertyFilter, specific=build_filter_RegexpFilter)
gen_build_filter_SinglePropertyFilter_IFilter = Generalization(general=IFilter, specific=build_filter_SinglePropertyFilter)
gen_build_filter_SimplePatternFIlter_SinglePropertyFilter = Generalization(general=SinglePropertyFilter, specific=build_filter_SimplePatternFIlter)

# Domain Model
domain_model = DomainModel(
    name="build",
    types={build_IBuildUnit, ICapability, PropertyScope, IGenericUnit, build_IBuildPart, build_IRequiredCapability, build_ICapability, build_PartCapability, build_IProvidedCapability, build_IArtifactsPart, IBuildPart, build_IPathGroup, build_IActionPart, IClosurePart, build_IActionResult, build_IUpToDatePolicy, build_IClosure, IPrerequisites, IAdvise, build_IPrerequisites, build_IRequirement, build_IPartGroup, build_PartRequirement, IRequirement, build_IProducedPart, build_IResultingParts, IActionResult, build_IClosurePart, IClosure, build_Requirement, build_ResultingPathGroup, build_StringProperties, build_PropertyScope, build_IGenericUnit, build_context_IBuildContext, IUnitRequest, IResolution, context_build_IBuildUnit, IResolver, build_context_IResolution, context_build_IRequiredCapability, context_build_ICapability, ImportOptions, build_context_ResolutionOptions, build_context_ImportOptions, IMaterializer, build_resolver_BestChoice, build_resolver_IMetaDataTranslatorFactory, build_runtime_BuildRuntime, UpToDateExtension, MaterializerExtension, MetaDataTranslatorFactoryExtension, ResolverExtension, build_runtime_UpToDateExtension, IHumanSelectable, runtime_build_IUpToDatePolicy, build_runtime_IHumanSelectable, IExtension, build_runtime_MaterializerExtension, build_runtime_MetaDataTranslatorFactoryExtension, IMetaDataTranslatorFactory, build_runtime_ResolverExtension, build_runtime_IExtension, build_resolver_IResolver, IExpr, build_resolver_IResourceMap, build_resolver_ILocation, build_resolver_ResolverGroup, build_resolver_FirstChoice, ResolverGroup, build_properties_ToUpper, build_properties_toLower, build_properties_replace, build_resolver_IMetaDataTranslator, build_resolver_IEFSBasedAccess, build_resolver_DefaultResolver, IMetaDataTranslator, build_resolver_WorspaceResolver, EFSResolver, build_resolver_EFSResolver, resolver_DefaultResolver, resolver_IEFSBasedAccess, build_resolver_P2Resolver, build_resolver_IResolutionContext, build_materializer_IMaterializer, build_materializer_FileSystemMaterializer, build_materializer_P2Materializer, build_materializer_WorkspaceMaterializer, build_properties_IExpr, build_properties_Literal, build_properties_IFunction, build_properties_PropertyRef, IFunction, build_properties_Format, build_command_BooleanAdvice, build_command_UnsetAdvice, build_command_NewInstanceAdvice, AdviceGroup, Match, build_properties_Match, build_properties_Split, build_command_IUnitRequest, ResolutionOptions, build_command_BuildUnitCommand, command_build_PropertyScope, build_command_IAdvise, ContextNodeSelector, build_command_ImportCommand, BuildUnitCommand, build_command_PropertyAdvice, build_command_ContextNodeSelector, build_command_StringAdvice, build_command_VersionAdvice, build_command_VersionRangeAdvice, build_command_InvokeCommand, build_command_FilterAdvice, IFilter, build_command_AdviceGroup, build_filter_IFilter, build_filter_OSGiBasedFilter, build_filter_AndFilter, FilterGroup, build_filter_OrFilter, build_filter_FilterGroup, build_filter_RegexpFilter, SinglePropertyFilter, build_filter_SinglePropertyFilter, build_filter_SimplePatternFIlter, Disposition, ConflictResolution, SplitStyle, FilterAdviceOperation},
    associations={parts0, requiredCapabilities1, metaRequiredCapabilities2, allRequiredCapabilities5, providedCapabilities8, selfCapability11, partCapabilities13, publishedCapabilities15, buildUnit16, paths17, produces18, upToDatePolicy19, advice20, requiredParts21, requiredPart22, producedBy23, paths24, producedBy26, producedParts27, requiredCapability29, paths31, buildPart33, properties35, self36, requests38, resolutions39, units41, advice43, resolver46, resolves48, resolution49, subResolutions51, options54, materializer56, upToDatePolicies57, materializers58, unitTypes60, resolvers62, instance64, instance65, instance67, instance68, location70, resolvers71, translator73, operands74, matchers76, options77, requests78, properties80, resolver82, advice85, selector88, properties89, remove91, add92, advice95, filters97},
    generalizations={gen_build_IBuildUnit_ICapability, gen_build_IBuildUnit_PropertyScope, gen_build_IBuildUnit_IGenericUnit, gen_build_IArtifactsPart_IBuildPart, gen_build_IActionPart_IClosurePart, gen_build_IClosure_IPrerequisites, gen_build_IClosure_PropertyScope, gen_build_IPrerequisites_IBuildPart, gen_build_IPartGroup_IClosurePart, gen_build_PartRequirement_IRequirement, gen_build_IResultingParts_IActionResult, gen_build_IClosurePart_IClosure, gen_build_IClosurePart_IBuildPart, gen_build_Requirement_IRequirement, gen_build_ResultingPathGroup_IActionResult, gen_build_PartCapability_ICapability, gen_build_IProducedPart_IClosurePart, gen_build_resolver_BestChoice_ResolverGroup, gen_build_runtime_UpToDateExtension_IHumanSelectable, gen_build_runtime_IHumanSelectable_IExtension, gen_build_runtime_MaterializerExtension_IHumanSelectable, gen_build_runtime_MetaDataTranslatorFactoryExtension_IExtension, gen_build_runtime_ResolverExtension_IHumanSelectable, gen_build_resolver_ResolverGroup_IResolver, gen_build_resolver_FirstChoice_ResolverGroup, gen_build_properties_ToUpper_IFunction, gen_build_properties_toLower_IFunction, gen_build_properties_replace_IFunction, gen_build_resolver_DefaultResolver_IResolver, gen_build_resolver_WorspaceResolver_EFSResolver, gen_build_resolver_EFSResolver_resolver_DefaultResolver, gen_build_resolver_EFSResolver_resolver_IEFSBasedAccess, gen_build_resolver_P2Resolver_IResolver, gen_build_materializer_FileSystemMaterializer_IMaterializer, gen_build_materializer_P2Materializer_IMaterializer, gen_build_materializer_WorkspaceMaterializer_IMaterializer, gen_build_properties_Literal_IExpr, gen_build_properties_IFunction_IExpr, gen_build_properties_PropertyRef_IFunction, gen_build_properties_Format_IFunction, gen_build_command_BooleanAdvice_IAdvise, gen_build_command_UnsetAdvice_IAdvise, gen_build_command_NewInstanceAdvice_AdviceGroup, gen_build_properties_Split_IFunction, gen_build_command_ImportCommand_BuildUnitCommand, gen_build_command_PropertyAdvice_IAdvise, gen_build_command_StringAdvice_IAdvise, gen_build_command_VersionAdvice_IAdvise, gen_build_command_VersionRangeAdvice_IAdvise, gen_build_command_InvokeCommand_BuildUnitCommand, gen_build_command_FilterAdvice_IAdvise, gen_build_filter_OSGiBasedFilter_IFilter, gen_build_filter_AndFilter_FilterGroup, gen_build_filter_OrFilter_FilterGroup, gen_build_filter_FilterGroup_IFilter, gen_build_filter_RegexpFilter_SinglePropertyFilter, gen_build_filter_SinglePropertyFilter_IFilter, gen_build_filter_SimplePatternFIlter_SinglePropertyFilter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)