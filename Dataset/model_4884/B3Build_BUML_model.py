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
TriState: Enumeration = Enumeration(
    name="TriState",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="True"),
			EnumerationLiteral(name="False")
    }
)

MergeConflictStrategy: Enumeration = Enumeration(
    name="MergeConflictStrategy",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="UseWorkspace"),
			EnumerationLiteral(name="UseSCM"),
			EnumerationLiteral(name="Fail")
    }
)

BranchPointType: Enumeration = Enumeration(
    name="BranchPointType",
    literals={
            EnumerationLiteral(name="Latest"),
			EnumerationLiteral(name="Tag"),
			EnumerationLiteral(name="Timestamp"),
			EnumerationLiteral(name="Revision")
    }
)

# Classes
build_BPropertySet = Class(name="build::BPropertySet")
build_Synchronization = Class(name="build::Synchronization")
build_Repository = Class(name="build::Repository")
build_ContainerConfiguration = Class(name="build::ContainerConfiguration")
build_BuildUnit = Class(name="build::BuildUnit")
VersionedCapability = Class(name="VersionedCapability")
BFunctionContainer = Class(name="BFunctionContainer")
IRequiredCapabilityContainer = Class(name="IRequiredCapabilityContainer")
IProvidedCapabilityContainer = Class(name="IProvidedCapabilityContainer")
IVarName = Class(name="IVarName")
build_IBuilder = Class(name="build::IBuilder", is_abstract=True)
build_RequiredCapability = Class(name="build::RequiredCapability")
build_IType = Class(name="build::IType")
build_BConcern = Class(name="build::BConcern")
build_UnitParameterDeclaration = Class(name="build::UnitParameterDeclaration")
build_VersionedCapability = Class(name="build::VersionedCapability")
Capability = Class(name="Capability")
build_ConditionalPathVector = Class(name="build::ConditionalPathVector")
build_FirstFoundUnitProvider = Class(name="build::FirstFoundUnitProvider")
build_IBuildUnitContainer = Class(name="build::IBuildUnitContainer", is_abstract=True)
build_FragmentHost = Class(name="build::FragmentHost")
IFunction = Class(name="IFunction")
build_BExpression = Class(name="build::BExpression")
build_BuilderInput = Class(name="build::BuilderInput")
build_PathGroup = Class(name="build::PathGroup")
build_BuilderQuery = Class(name="build::BuilderQuery")
build_UnitProvider = Class(name="build::UnitProvider", is_abstract=True)
BExpression = Class(name="BExpression")
build_RepositoryUnitProvider = Class(name="build::RepositoryUnitProvider")
UnitProvider = Class(name="UnitProvider")
build_BuilderInputDecorator = Class(name="build::BuilderInputDecorator", is_abstract=True)
BuilderInput = Class(name="BuilderInput")
build_BuilderCall = Class(name="build::BuilderCall", is_abstract=True)
build_BParameterList = Class(name="build::BParameterList")
build_Capability = Class(name="build::Capability")
INamedValue = Class(name="INamedValue")
build_PathVector = Class(name="build::PathVector")
build_BNamePredicate = Class(name="build::BNamePredicate")
build_ImplementsPredicate = Class(name="build::ImplementsPredicate")
build_ProvidesPredicate = Class(name="build::ProvidesPredicate")
build_RepoOption = Class(name="build::RepoOption")
build_IBuildUnitRepository = Class(name="build::IBuildUnitRepository", is_abstract=True)
build_CompoundUnitProvider = Class(name="build::CompoundUnitProvider", is_abstract=True)
CompoundUnitProvider = Class(name="CompoundUnitProvider")
build_BestFoundUnitProvider = Class(name="build::BestFoundUnitProvider")
build_BuildConcernContext = Class(name="build::BuildConcernContext")
BConcernContext = Class(name="BConcernContext")
build_RequiresPredicate = Class(name="build::RequiresPredicate")
build_CapabilityPredicate = Class(name="build::CapabilityPredicate")
build_NameSpacePredicate = Class(name="build::NameSpacePredicate")
build_UnitNamePredicate = Class(name="build::UnitNamePredicate")
CapabilityPredicate = Class(name="CapabilityPredicate")
build_BuilderNamePredicate = Class(name="build::BuilderNamePredicate")
build_InputPredicate = Class(name="build::InputPredicate")
build_UnitConcernContext = Class(name="build::UnitConcernContext")
BuildConcernContext = Class(name="BuildConcernContext")
build_BuilderConcernContext = Class(name="build::BuilderConcernContext")
build_SourcePredicate = Class(name="build::SourcePredicate")
build_OutputPredicate = Class(name="build::OutputPredicate")
build_BParameterPredicate = Class(name="build::BParameterPredicate")
B3Function = Class(name="B3Function")
IBuilder = Class(name="IBuilder")
build_BuilderJava = Class(name="build::BuilderJava")
BJavaFunction = Class(name="BJavaFunction")
build_BuilderWrapper = Class(name="build::BuilderWrapper")
BFunctionWrapper = Class(name="BFunctionWrapper")
build_BeeModel = Class(name="build::BeeModel")
BChainedExpression = Class(name="BChainedExpression")
IBuildUnitContainer = Class(name="IBuildUnitContainer")
build_PathGroupPredicate = Class(name="build::PathGroupPredicate")
build_AliasedRequiredCapability = Class(name="build::AliasedRequiredCapability")
RequiredCapability = Class(name="RequiredCapability")
build_IRequiredCapabilityContainer = Class(name="build::IRequiredCapabilityContainer", is_abstract=True)
build_IProvidedCapabilityContainer = Class(name="build::IProvidedCapabilityContainer", is_abstract=True)
build_Builder = Class(name="build::Builder")
build_EffectiveUnitFacade = Class(name="build::EffectiveUnitFacade")
EffectiveFacade = Class(name="EffectiveFacade")
build_EffectiveCapabilityFacade = Class(name="build::EffectiveCapabilityFacade")
build_EffectiveRequirementFacade = Class(name="build::EffectiveRequirementFacade")
build_IFunction = Class(name="build::IFunction")
build_BeeHive = Class(name="build::BeeHive")
build_ResolutionInfo = Class(name="build::ResolutionInfo")
build_EffectiveFacade = Class(name="build::EffectiveFacade")
IEffectiveFacade = Class(name="IEffectiveFacade")
build_CompoundBuildUnitRepository = Class(name="build::CompoundBuildUnitRepository", is_abstract=True)
BuildUnitRepository = Class(name="BuildUnitRepository")
build_CompoundFirstFoundRepository = Class(name="build::CompoundFirstFoundRepository")
CompoundBuildUnitRepository = Class(name="CompoundBuildUnitRepository")
build_ExecutionStackRepository = Class(name="build::ExecutionStackRepository")
build_BeeModelRepository = Class(name="build::BeeModelRepository")
build_BuilderCallFacade = Class(name="build::BuilderCallFacade")
build_BuildSet = Class(name="build::BuildSet")
ITypedValueContainer = Class(name="ITypedValueContainer")
build_BuildResultContext = Class(name="build::BuildResultContext")
BInnerContext = Class(name="BInnerContext")
PathGroupPredicate = Class(name="PathGroupPredicate")
build_BuildUnitRepository = Class(name="build::BuildUnitRepository", is_abstract=True)
IBuildUnitRepository = Class(name="IBuildUnitRepository")
build_UnitResolutionInfo = Class(name="build::UnitResolutionInfo")
ResolutionInfo = Class(name="ResolutionInfo")
build_BExecutionContext = Class(name="build::BExecutionContext")
build_SwitchUnitProvider = Class(name="build::SwitchUnitProvider")
build_BSwitchExpression = Class(name="build::BSwitchExpression")
build_Branch = Class(name="build::Branch")
build_BuildCallOnSelectedRequirements = Class(name="build::BuildCallOnSelectedRequirements")
BuildCallMultiple = Class(name="BuildCallMultiple")
build_DelegatingUnitProvider = Class(name="build::DelegatingUnitProvider")
build_UnitRepositoryDescription = Class(name="build::UnitRepositoryDescription")
BParameterDeclaration = Class(name="BParameterDeclaration")
build_BuilderInputNameDecorator = Class(name="build::BuilderInputNameDecorator")
BuilderInputDecorator = Class(name="BuilderInputDecorator")
build_BuilderInputContextDecorator = Class(name="build::BuilderInputContextDecorator")
build_BWithExpression = Class(name="build::BWithExpression")
build_BuilderInputCondition = Class(name="build::BuilderInputCondition")
build_BuildCallMultiple = Class(name="build::BuildCallMultiple")
BuilderCall = Class(name="BuilderCall")
build_BuildCallSingle = Class(name="build::BuildCallSingle", is_abstract=True)
build_BuildCallOnDeclaredRequirement = Class(name="build::BuildCallOnDeclaredRequirement")
BuildCallSingle = Class(name="BuildCallSingle")
build_BuildCallOnReferencedRequirement = Class(name="build::BuildCallOnReferencedRequirement")
build_BuilderInputGroup = Class(name="build::BuilderInputGroup")
build_IEffectiveFacade = Class(name="build::IEffectiveFacade", is_abstract=True)
build_EffectiveBuilderCallFacade = Class(name="build::EffectiveBuilderCallFacade")
BuilderCallFacade = Class(name="BuilderCallFacade")

# build_BPropertySet class attributes and methods

# build_Synchronization class attributes and methods

# build_Repository class attributes and methods
build_Repository_name: Property = Property(name="name", type=StringType)
build_Repository_documentation: Property = Property(name="documentation", type=StringType)
build_Repository_handlerType: Property = Property(name="handlerType", type=StringType)
build_Repository.attributes={build_Repository_name, build_Repository_handlerType, build_Repository_documentation}

# build_ContainerConfiguration class attributes and methods
build_ContainerConfiguration_documentation: Property = Property(name="documentation", type=StringType)
build_ContainerConfiguration_name: Property = Property(name="name", type=StringType)
build_ContainerConfiguration.attributes={build_ContainerConfiguration_name, build_ContainerConfiguration_documentation}

# build_BuildUnit class attributes and methods
build_BuildUnit_documentation: Property = Property(name="documentation", type=StringType)
build_BuildUnit_executionMode: Property = Property(name="executionMode", type=StringType)
build_BuildUnit_sourceLocation: Property = Property(name="sourceLocation", type=StringType)
build_BuildUnit_outputLocation: Property = Property(name="outputLocation", type=StringType)
build_BuildUnit_platformFilter: Property = Property(name="platformFilter", type=StringType)
build_BuildUnit_m_getEffectiveFacade: Method = Method(name="getEffectiveFacade", parameters={Parameter(name='ctx')}, type=StringType)
build_BuildUnit_m_getUnitProvider: Method = Method(name="getUnitProvider", parameters={}, type=StringType)
build_BuildUnit.attributes={build_BuildUnit_sourceLocation, build_BuildUnit_documentation, build_BuildUnit_outputLocation, build_BuildUnit_executionMode, build_BuildUnit_platformFilter}
build_BuildUnit.methods={build_BuildUnit_m_getUnitProvider, build_BuildUnit_m_getEffectiveFacade}

# VersionedCapability class attributes and methods

# BFunctionContainer class attributes and methods

# IRequiredCapabilityContainer class attributes and methods

# IProvidedCapabilityContainer class attributes and methods

# IVarName class attributes and methods

# build_IBuilder class attributes and methods
build_IBuilder_unitType: Property = Property(name="unitType", type=StringType)
build_IBuilder.attributes={build_IBuilder_unitType}

# build_RequiredCapability class attributes and methods
build_RequiredCapability_versionRange: Property = Property(name="versionRange", type=StringType)
build_RequiredCapability_greedy: Property = Property(name="greedy", type=BooleanType)
build_RequiredCapability_max: Property = Property(name="max", type=IntegerType)
build_RequiredCapability_min: Property = Property(name="min", type=IntegerType)
build_RequiredCapability.attributes={build_RequiredCapability_max, build_RequiredCapability_min, build_RequiredCapability_versionRange, build_RequiredCapability_greedy}

# build_IType class attributes and methods

# build_BConcern class attributes and methods

# build_UnitParameterDeclaration class attributes and methods
build_UnitParameterDeclaration_m_hasCorrectState: Method = Method(name="hasCorrectState", parameters={Parameter(name='chain'), Parameter(name='map')}, type=BooleanType)
build_UnitParameterDeclaration.methods={build_UnitParameterDeclaration_m_hasCorrectState}

# build_VersionedCapability class attributes and methods
build_VersionedCapability_version: Property = Property(name="version", type=StringType)
build_VersionedCapability.attributes={build_VersionedCapability_version}

# Capability class attributes and methods

# build_ConditionalPathVector class attributes and methods

# build_FirstFoundUnitProvider class attributes and methods

# build_IBuildUnitContainer class attributes and methods

# build_FragmentHost class attributes and methods

# IFunction class attributes and methods

# build_BExpression class attributes and methods

# build_BuilderInput class attributes and methods

# build_PathGroup class attributes and methods

# build_BuilderQuery class attributes and methods

# build_UnitProvider class attributes and methods
build_UnitProvider_documentation: Property = Property(name="documentation", type=StringType)
build_UnitProvider_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='ctx'), Parameter(name='requiredCapability')}, type=StringType)
build_UnitProvider_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='effectiveRequirement')}, type=StringType)
build_UnitProvider.attributes={build_UnitProvider_documentation}
build_UnitProvider.methods={build_UnitProvider_m_resolve, build_UnitProvider_m_resolve}

# BExpression class attributes and methods

# build_RepositoryUnitProvider class attributes and methods

# UnitProvider class attributes and methods

# build_BuilderInputDecorator class attributes and methods

# BuilderInput class attributes and methods

# build_BuilderCall class attributes and methods
build_BuilderCall_builderName: Property = Property(name="builderName", type=StringType)
build_BuilderCall.attributes={build_BuilderCall_builderName}

# build_BParameterList class attributes and methods

# build_Capability class attributes and methods
build_Capability_nameSpace: Property = Property(name="nameSpace", type=StringType)
build_Capability_m_satisfies: Method = Method(name="satisfies", parameters={Parameter(name='requirement')}, type=BooleanType)
build_Capability.attributes={build_Capability_nameSpace}
build_Capability.methods={build_Capability_m_satisfies}

# INamedValue class attributes and methods

# build_PathVector class attributes and methods
build_PathVector_paths: Property = Property(name="paths", type=StringType)
build_PathVector_basePath: Property = Property(name="basePath", type=StringType)
build_PathVector_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='baseUri')}, type=StringType)
build_PathVector.attributes={build_PathVector_paths, build_PathVector_basePath}
build_PathVector.methods={build_PathVector_m_resolve}

# build_BNamePredicate class attributes and methods

# build_ImplementsPredicate class attributes and methods

# build_ProvidesPredicate class attributes and methods
build_ProvidesPredicate_m_matches: Method = Method(name="matches", parameters={Parameter(name='candidate')}, type=BooleanType)
build_ProvidesPredicate_m_matches: Method = Method(name="matches", parameters={Parameter(name='candidate')}, type=BooleanType)
build_ProvidesPredicate_m_removeMatching: Method = Method(name="removeMatching", parameters={Parameter(name='input')}, type=BooleanType)
build_ProvidesPredicate.methods={build_ProvidesPredicate_m_matches, build_ProvidesPredicate_m_matches, build_ProvidesPredicate_m_removeMatching}

# build_RepoOption class attributes and methods
build_RepoOption_name: Property = Property(name="name", type=StringType)
build_RepoOption.attributes={build_RepoOption_name}

# build_IBuildUnitRepository class attributes and methods

# build_CompoundUnitProvider class attributes and methods

# CompoundUnitProvider class attributes and methods

# build_BestFoundUnitProvider class attributes and methods

# build_BuildConcernContext class attributes and methods
build_BuildConcernContext_defaultPropertiesRemovals: Property = Property(name="defaultPropertiesRemovals", type=StringType)
build_BuildConcernContext.attributes={build_BuildConcernContext_defaultPropertiesRemovals}

# BConcernContext class attributes and methods

# build_RequiresPredicate class attributes and methods
build_RequiresPredicate_meta: Property = Property(name="meta", type=BooleanType)
build_RequiresPredicate_m_matches: Method = Method(name="matches", parameters={Parameter(name='candidate')}, type=BooleanType)
build_RequiresPredicate.attributes={build_RequiresPredicate_meta}
build_RequiresPredicate.methods={build_RequiresPredicate_m_matches}

# build_CapabilityPredicate class attributes and methods
build_CapabilityPredicate_versionRange: Property = Property(name="versionRange", type=StringType)
build_CapabilityPredicate_m_matches: Method = Method(name="matches", parameters={Parameter(name='candidate')}, type=BooleanType)
build_CapabilityPredicate_m_matches: Method = Method(name="matches", parameters={Parameter(name='candidate')}, type=BooleanType)
build_CapabilityPredicate_m_matches: Method = Method(name="matches", parameters={Parameter(name='candidate')}, type=BooleanType)
build_CapabilityPredicate.attributes={build_CapabilityPredicate_versionRange}
build_CapabilityPredicate.methods={build_CapabilityPredicate_m_matches, build_CapabilityPredicate_m_matches, build_CapabilityPredicate_m_matches}

# build_NameSpacePredicate class attributes and methods
build_NameSpacePredicate_nameSpace: Property = Property(name="nameSpace", type=StringType)
build_NameSpacePredicate.attributes={build_NameSpacePredicate_nameSpace}

# build_UnitNamePredicate class attributes and methods

# CapabilityPredicate class attributes and methods

# build_BuilderNamePredicate class attributes and methods

# build_InputPredicate class attributes and methods

# build_UnitConcernContext class attributes and methods
build_UnitConcernContext_sourceLocation: Property = Property(name="sourceLocation", type=StringType)
build_UnitConcernContext_outputLocation: Property = Property(name="outputLocation", type=StringType)
build_UnitConcernContext.attributes={build_UnitConcernContext_outputLocation, build_UnitConcernContext_sourceLocation}

# BuildConcernContext class attributes and methods

# build_BuilderConcernContext class attributes and methods
build_BuilderConcernContext_outputAnnotationsRemovals: Property = Property(name="outputAnnotationsRemovals", type=StringType)
build_BuilderConcernContext_varArgs: Property = Property(name="varArgs", type=BooleanType)
build_BuilderConcernContext_matchParameters: Property = Property(name="matchParameters", type=BooleanType)
build_BuilderConcernContext_removePreCondition: Property = Property(name="removePreCondition", type=BooleanType)
build_BuilderConcernContext_removePostCondition: Property = Property(name="removePostCondition", type=BooleanType)
build_BuilderConcernContext_removePostInputCondition: Property = Property(name="removePostInputCondition", type=BooleanType)
build_BuilderConcernContext_sourceAnnotationsRemovals: Property = Property(name="sourceAnnotationsRemovals", type=StringType)
build_BuilderConcernContext.attributes={build_BuilderConcernContext_removePostInputCondition, build_BuilderConcernContext_removePreCondition, build_BuilderConcernContext_outputAnnotationsRemovals, build_BuilderConcernContext_matchParameters, build_BuilderConcernContext_varArgs, build_BuilderConcernContext_sourceAnnotationsRemovals, build_BuilderConcernContext_removePostCondition}

# build_SourcePredicate class attributes and methods

# build_OutputPredicate class attributes and methods

# build_BParameterPredicate class attributes and methods

# B3Function class attributes and methods

# IBuilder class attributes and methods

# build_BuilderJava class attributes and methods

# BJavaFunction class attributes and methods

# build_BuilderWrapper class attributes and methods
build_BuilderWrapper_inputAdvised: Property = Property(name="inputAdvised", type=BooleanType)
build_BuilderWrapper_outputAdvised: Property = Property(name="outputAdvised", type=BooleanType)
build_BuilderWrapper_unitTypeAdvised: Property = Property(name="unitTypeAdvised", type=BooleanType)
build_BuilderWrapper_providesAdvised: Property = Property(name="providesAdvised", type=BooleanType)
build_BuilderWrapper_defaultPropertiesAdvised: Property = Property(name="defaultPropertiesAdvised", type=BooleanType)
build_BuilderWrapper_sourceAdvised: Property = Property(name="sourceAdvised", type=BooleanType)
build_BuilderWrapper.attributes={build_BuilderWrapper_sourceAdvised, build_BuilderWrapper_defaultPropertiesAdvised, build_BuilderWrapper_providesAdvised, build_BuilderWrapper_unitTypeAdvised, build_BuilderWrapper_inputAdvised, build_BuilderWrapper_outputAdvised}

# BFunctionWrapper class attributes and methods

# build_BeeModel class attributes and methods
build_BeeModel_m_getUnitProvider: Method = Method(name="getUnitProvider", parameters={}, type=StringType)
build_BeeModel.methods={build_BeeModel_m_getUnitProvider}

# BChainedExpression class attributes and methods

# IBuildUnitContainer class attributes and methods

# build_PathGroupPredicate class attributes and methods
build_PathGroupPredicate_m_removeMatching: Method = Method(name="removeMatching", parameters={Parameter(name='input')}, type=BooleanType)
build_PathGroupPredicate.methods={build_PathGroupPredicate_m_removeMatching}

# build_AliasedRequiredCapability class attributes and methods
build_AliasedRequiredCapability_alias: Property = Property(name="alias", type=StringType)
build_AliasedRequiredCapability.attributes={build_AliasedRequiredCapability_alias}

# RequiredCapability class attributes and methods

# build_IRequiredCapabilityContainer class attributes and methods

# build_IProvidedCapabilityContainer class attributes and methods

# build_Builder class attributes and methods

# build_EffectiveUnitFacade class attributes and methods

# EffectiveFacade class attributes and methods

# build_EffectiveCapabilityFacade class attributes and methods

# build_EffectiveRequirementFacade class attributes and methods

# build_IFunction class attributes and methods

# build_BeeHive class attributes and methods
build_BeeHive_resolutions: Property = Property(name="resolutions", type=StringType)
build_BeeHive_m_getResolvedCapabilityContainer: Method = Method(name="getResolvedCapabilityContainer", parameters={Parameter(name='requiredCapability')}, type=IProvidedCapabilityContainer)
build_BeeHive.attributes={build_BeeHive_resolutions}
build_BeeHive.methods={build_BeeHive_m_getResolvedCapabilityContainer}

# build_ResolutionInfo class attributes and methods
build_ResolutionInfo_status: Property = Property(name="status", type=StringType)
build_ResolutionInfo.attributes={build_ResolutionInfo_status}

# build_EffectiveFacade class attributes and methods

# IEffectiveFacade class attributes and methods

# build_CompoundBuildUnitRepository class attributes and methods

# BuildUnitRepository class attributes and methods

# build_CompoundFirstFoundRepository class attributes and methods

# CompoundBuildUnitRepository class attributes and methods

# build_ExecutionStackRepository class attributes and methods

# build_BeeModelRepository class attributes and methods

# build_BuilderCallFacade class attributes and methods
build_BuilderCallFacade_aliases: Property = Property(name="aliases", type=StringType)
build_BuilderCallFacade.attributes={build_BuilderCallFacade_aliases}

# build_BuildSet class attributes and methods
build_BuildSet_valueMap: Property = Property(name="valueMap", type=StringType)
build_BuildSet_pathIterator: Property = Property(name="pathIterator", type=StringType)
build_BuildSet_m_merge: Method = Method(name="merge", parameters={Parameter(name='buildResult')}, type=StringType)
build_BuildSet.attributes={build_BuildSet_pathIterator, build_BuildSet_valueMap}
build_BuildSet.methods={build_BuildSet_m_merge}

# ITypedValueContainer class attributes and methods

# build_BuildResultContext class attributes and methods

# BInnerContext class attributes and methods

# PathGroupPredicate class attributes and methods

# build_BuildUnitRepository class attributes and methods
build_BuildUnitRepository_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='repository'), Parameter(name='ctx'), Parameter(name='options')})
build_BuildUnitRepository_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='requiredCapability'), Parameter(name='options'), Parameter(name='ctx')}, type=StringType)
build_BuildUnitRepository.methods={build_BuildUnitRepository_m_resolve, build_BuildUnitRepository_m_initialize}

# IBuildUnitRepository class attributes and methods

# build_UnitResolutionInfo class attributes and methods

# ResolutionInfo class attributes and methods

# build_BExecutionContext class attributes and methods

# build_SwitchUnitProvider class attributes and methods

# build_BSwitchExpression class attributes and methods

# build_Branch class attributes and methods
build_Branch_name: Property = Property(name="name", type=StringType)
build_Branch_documentation: Property = Property(name="documentation", type=StringType)
build_Branch_branchPointType: Property = Property(name="branchPointType", type=StringType)
build_Branch_mergeStrategy: Property = Property(name="mergeStrategy", type=StringType)
build_Branch_checkout: Property = Property(name="checkout", type=StringType)
build_Branch_acceptDirty: Property = Property(name="acceptDirty", type=StringType)
build_Branch_update: Property = Property(name="update", type=StringType)
build_Branch_replace: Property = Property(name="replace", type=StringType)
build_Branch_m_getEffectiveAcceptDirty: Method = Method(name="getEffectiveAcceptDirty", parameters={}, type=BooleanType)
build_Branch_m_getEffectiveUpdate: Method = Method(name="getEffectiveUpdate", parameters={}, type=BooleanType)
build_Branch_m_getEffectiveReplace: Method = Method(name="getEffectiveReplace", parameters={}, type=BooleanType)
build_Branch_m_hasValidState: Method = Method(name="hasValidState", parameters={Parameter(name='chain'), Parameter(name='map')}, type=BooleanType)
build_Branch_m_getEffectiveMergeStrategy: Method = Method(name="getEffectiveMergeStrategy", parameters={}, type=StringType)
build_Branch_m_getEffectiveCheckout: Method = Method(name="getEffectiveCheckout", parameters={}, type=BooleanType)
build_Branch.attributes={build_Branch_name, build_Branch_checkout, build_Branch_branchPointType, build_Branch_documentation, build_Branch_replace, build_Branch_acceptDirty, build_Branch_update, build_Branch_mergeStrategy}
build_Branch.methods={build_Branch_m_hasValidState, build_Branch_m_getEffectiveAcceptDirty, build_Branch_m_getEffectiveUpdate, build_Branch_m_getEffectiveCheckout, build_Branch_m_getEffectiveMergeStrategy, build_Branch_m_getEffectiveReplace}

# build_BuildCallOnSelectedRequirements class attributes and methods

# BuildCallMultiple class attributes and methods

# build_DelegatingUnitProvider class attributes and methods

# build_UnitRepositoryDescription class attributes and methods
build_UnitRepositoryDescription_evaluatedOptions: Property = Property(name="evaluatedOptions", type=StringType)
build_UnitRepositoryDescription.attributes={build_UnitRepositoryDescription_evaluatedOptions}

# BParameterDeclaration class attributes and methods

# build_BuilderInputNameDecorator class attributes and methods

# BuilderInputDecorator class attributes and methods

# build_BuilderInputContextDecorator class attributes and methods

# build_BWithExpression class attributes and methods

# build_BuilderInputCondition class attributes and methods

# build_BuildCallMultiple class attributes and methods

# BuilderCall class attributes and methods

# build_BuildCallSingle class attributes and methods

# build_BuildCallOnDeclaredRequirement class attributes and methods

# BuildCallSingle class attributes and methods

# build_BuildCallOnReferencedRequirement class attributes and methods

# build_BuilderInputGroup class attributes and methods

# build_IEffectiveFacade class attributes and methods

# build_EffectiveBuilderCallFacade class attributes and methods

# BuilderCallFacade class attributes and methods

# Relationships
concerns5: BinaryAssociation = BinaryAssociation(
    name="concerns5",
    ends={
        Property(name="build_BuildUnit6", type=build_BConcern, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="build_BConcern", type=build_BuildUnit, multiplicity=Multiplicity(1, 1))
    }
)
defaultProperties7: BinaryAssociation = BinaryAssociation(
    name="defaultProperties7",
    ends={
        Property(name="build_BPropertySet", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit8", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronizations9: BinaryAssociation = BinaryAssociation(
    name="synchronizations9",
    ends={
        Property(name="build_Synchronization", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit10", type=build_Synchronization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories11: BinaryAssociation = BinaryAssociation(
    name="repositories11",
    ends={
        Property(name="build_Repository", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit12", type=build_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containers13: BinaryAssociation = BinaryAssociation(
    name="containers13",
    ends={
        Property(name="build_ContainerConfiguration", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit14", type=build_ContainerConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertySets15: BinaryAssociation = BinaryAssociation(
    name="propertySets15",
    ends={
        Property(name="build_BPropertySet17", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit16", type=build_BPropertySet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
builders0: BinaryAssociation = BinaryAssociation(
    name="builders0",
    ends={
        Property(name="build_IBuilder", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit", type=build_IBuilder, multiplicity=Multiplicity(0, 9999))
    }
)
metaRequiredCapabilities1: BinaryAssociation = BinaryAssociation(
    name="metaRequiredCapabilities1",
    ends={
        Property(name="build_RequiredCapability", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit2", type=build_RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements3: BinaryAssociation = BinaryAssociation(
    name="implements3",
    ends={
        Property(name="build_IType", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit4", type=build_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
explicitUnitType39: BinaryAssociation = BinaryAssociation(
    name="explicitUnitType39",
    ends={
        Property(name="build_UnitParameterDeclaration", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder40", type=build_UnitParameterDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source41: BinaryAssociation = BinaryAssociation(
    name="source41",
    ends={
        Property(name="build_PathGroup43", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder42", type=build_PathGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations44: BinaryAssociation = BinaryAssociation(
    name="annotations44",
    ends={
        Property(name="build_BPropertySet46", type=build_PathGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="build_PathGroup45", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathVectors47: BinaryAssociation = BinaryAssociation(
    name="pathVectors47",
    ends={
        Property(name="build_ConditionalPathVector", type=build_PathGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="build_PathGroup48", type=build_ConditionalPathVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers18: BinaryAssociation = BinaryAssociation(
    name="providers18",
    ends={
        Property(name="build_FirstFoundUnitProvider", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit19", type=build_FirstFoundUnitProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="build_IBuildUnitContainer", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit21", type=build_IBuildUnitContainer, multiplicity=Multiplicity(0, 1))
    }
)
fragmentHosts22: BinaryAssociation = BinaryAssociation(
    name="fragmentHosts22",
    ends={
        Property(name="build_FragmentHost", type=build_BuildUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildUnit23", type=build_FragmentHost, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondExpr24: BinaryAssociation = BinaryAssociation(
    name="postcondExpr24",
    ends={
        Property(name="build_BExpression", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder25", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
precondExpr26: BinaryAssociation = BinaryAssociation(
    name="precondExpr26",
    ends={
        Property(name="build_BExpression28", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder27", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input29: BinaryAssociation = BinaryAssociation(
    name="input29",
    ends={
        Property(name="build_BuilderInput", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder30", type=build_BuilderInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output31: BinaryAssociation = BinaryAssociation(
    name="output31",
    ends={
        Property(name="build_PathGroup", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder32", type=build_PathGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultProperties33: BinaryAssociation = BinaryAssociation(
    name="defaultProperties33",
    ends={
        Property(name="build_BPropertySet35", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder34", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postinputcondExpr36: BinaryAssociation = BinaryAssociation(
    name="postinputcondExpr36",
    ends={
        Property(name="build_BExpression38", type=build_IBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuilder37", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
builderQueries59: BinaryAssociation = BinaryAssociation(
    name="builderQueries59",
    ends={
        Property(name="build_BuilderQuery", type=build_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Synchronization60", type=build_BuilderQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository61: BinaryAssociation = BinaryAssociation(
    name="repository61",
    ends={
        Property(name="build_Repository62", type=build_RepositoryUnitProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="build_RepositoryUnitProvider", type=build_Repository, multiplicity=Multiplicity(0, 1))
    }
)
builderInput49: BinaryAssociation = BinaryAssociation(
    name="builderInput49",
    ends={
        Property(name="build_BuilderInput50", type=build_BuilderInputDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderInputDecorator", type=build_BuilderInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters51: BinaryAssociation = BinaryAssociation(
    name="parameters51",
    ends={
        Property(name="build_BParameterList", type=build_BuilderCall, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderCall", type=build_BParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr52: BinaryAssociation = BinaryAssociation(
    name="condExpr52",
    ends={
        Property(name="build_BExpression53", type=build_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Capability", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr54: BinaryAssociation = BinaryAssociation(
    name="condExpr54",
    ends={
        Property(name="build_BExpression56", type=build_ConditionalPathVector, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ConditionalPathVector55", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathVectors57: BinaryAssociation = BinaryAssociation(
    name="pathVectors57",
    ends={
        Property(name="build_PathVector", type=build_ConditionalPathVector, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ConditionalPathVector58", type=build_PathVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namePredicate77: BinaryAssociation = BinaryAssociation(
    name="namePredicate77",
    ends={
        Property(name="build_BNamePredicate", type=build_CapabilityPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_CapabilityPredicate78", type=build_BNamePredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpacePredicate79: BinaryAssociation = BinaryAssociation(
    name="nameSpacePredicate79",
    ends={
        Property(name="build_BNamePredicate81", type=build_CapabilityPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_CapabilityPredicate80", type=build_BNamePredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type82: BinaryAssociation = BinaryAssociation(
    name="type82",
    ends={
        Property(name="build_IType83", type=build_ImplementsPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ImplementsPredicate", type=build_IType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
options63: BinaryAssociation = BinaryAssociation(
    name="options63",
    ends={
        Property(name="build_RepoOption", type=build_RepositoryUnitProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="build_RepositoryUnitProvider64", type=build_RepoOption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildUnitRepository65: BinaryAssociation = BinaryAssociation(
    name="buildUnitRepository65",
    ends={
        Property(name="build_IBuildUnitRepository", type=build_RepositoryUnitProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="build_RepositoryUnitProvider66", type=build_IBuildUnitRepository, multiplicity=Multiplicity(0, 1))
    }
)
providers67: BinaryAssociation = BinaryAssociation(
    name="providers67",
    ends={
        Property(name="build_UnitProvider", type=build_CompoundUnitProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="build_CompoundUnitProvider", type=build_UnitProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
agentType68: BinaryAssociation = BinaryAssociation(
    name="agentType68",
    ends={
        Property(name="build_IType70", type=build_ContainerConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ContainerConfiguration69", type=build_IType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextBlock71: BinaryAssociation = BinaryAssociation(
    name="contextBlock71",
    ends={
        Property(name="build_BExpression73", type=build_ContainerConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ContainerConfiguration72", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultPropertiesAdditions74: BinaryAssociation = BinaryAssociation(
    name="defaultPropertiesAdditions74",
    ends={
        Property(name="build_BPropertySet75", type=build_BuildConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildConcernContext", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capabilityPredicate76: BinaryAssociation = BinaryAssociation(
    name="capabilityPredicate76",
    ends={
        Property(name="build_CapabilityPredicate", type=build_RequiresPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_RequiresPredicate", type=build_CapabilityPredicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requiredPredicatesRemovals103: BinaryAssociation = BinaryAssociation(
    name="requiredPredicatesRemovals103",
    ends={
        Property(name="build_CapabilityPredicate105", type=build_UnitConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitConcernContext104", type=build_CapabilityPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query106: BinaryAssociation = BinaryAssociation(
    name="query106",
    ends={
        Property(name="build_BExpression108", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext107", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputAdditions109: BinaryAssociation = BinaryAssociation(
    name="inputAdditions109",
    ends={
        Property(name="build_BuilderInput111", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext110", type=build_BuilderInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capabilityPredicate84: BinaryAssociation = BinaryAssociation(
    name="capabilityPredicate84",
    ends={
        Property(name="build_CapabilityPredicate85", type=build_ProvidesPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ProvidesPredicate", type=build_CapabilityPredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namePredicate86: BinaryAssociation = BinaryAssociation(
    name="namePredicate86",
    ends={
        Property(name="build_BNamePredicate87", type=build_BuilderNamePredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderNamePredicate", type=build_BNamePredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capabilityPredicate88: BinaryAssociation = BinaryAssociation(
    name="capabilityPredicate88",
    ends={
        Property(name="build_CapabilityPredicate89", type=build_InputPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_InputPredicate", type=build_CapabilityPredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
builderPredicate90: BinaryAssociation = BinaryAssociation(
    name="builderPredicate90",
    ends={
        Property(name="build_BNamePredicate92", type=build_InputPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_InputPredicate91", type=build_BNamePredicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
builderContexts93: BinaryAssociation = BinaryAssociation(
    name="builderContexts93",
    ends={
        Property(name="build_BuilderConcernContext", type=build_UnitConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitConcernContext", type=build_BuilderConcernContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query94: BinaryAssociation = BinaryAssociation(
    name="query94",
    ends={
        Property(name="build_BExpression96", type=build_UnitConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitConcernContext95", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiresRemovals97: BinaryAssociation = BinaryAssociation(
    name="requiresRemovals97",
    ends={
        Property(name="build_RequiresPredicate99", type=build_UnitConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitConcernContext98", type=build_RequiresPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providesRemovals100: BinaryAssociation = BinaryAssociation(
    name="providesRemovals100",
    ends={
        Property(name="build_ProvidesPredicate102", type=build_UnitConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitConcernContext101", type=build_ProvidesPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providesRemovals134: BinaryAssociation = BinaryAssociation(
    name="providesRemovals134",
    ends={
        Property(name="build_ProvidesPredicate136", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext135", type=build_ProvidesPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputAnnotationAdditions137: BinaryAssociation = BinaryAssociation(
    name="outputAnnotationAdditions137",
    ends={
        Property(name="build_BPropertySet139", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext138", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceRemovals140: BinaryAssociation = BinaryAssociation(
    name="sourceRemovals140",
    ends={
        Property(name="build_SourcePredicate", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext141", type=build_SourcePredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceAdditions142: BinaryAssociation = BinaryAssociation(
    name="sourceAdditions142",
    ends={
        Property(name="build_ConditionalPathVector144", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext143", type=build_ConditionalPathVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputRemovals112: BinaryAssociation = BinaryAssociation(
    name="inputRemovals112",
    ends={
        Property(name="build_InputPredicate114", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext113", type=build_InputPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputAdditions115: BinaryAssociation = BinaryAssociation(
    name="outputAdditions115",
    ends={
        Property(name="build_ConditionalPathVector117", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext116", type=build_ConditionalPathVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputRemovals118: BinaryAssociation = BinaryAssociation(
    name="outputRemovals118",
    ends={
        Property(name="build_OutputPredicate", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext119", type=build_OutputPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
funcExpr120: BinaryAssociation = BinaryAssociation(
    name="funcExpr120",
    ends={
        Property(name="build_BExpression122", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext121", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters123: BinaryAssociation = BinaryAssociation(
    name="parameters123",
    ends={
        Property(name="build_BParameterPredicate", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext124", type=build_BParameterPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondExpr125: BinaryAssociation = BinaryAssociation(
    name="precondExpr125",
    ends={
        Property(name="build_BExpression127", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext126", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postcondExpr128: BinaryAssociation = BinaryAssociation(
    name="postcondExpr128",
    ends={
        Property(name="build_BExpression130", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext129", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postinputcondExpr131: BinaryAssociation = BinaryAssociation(
    name="postinputcondExpr131",
    ends={
        Property(name="build_BExpression133", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext132", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceAnnotationAdditions145: BinaryAssociation = BinaryAssociation(
    name="sourceAnnotationAdditions145",
    ends={
        Property(name="build_BPropertySet147", type=build_BuilderConcernContext, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderConcernContext146", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathVector148: BinaryAssociation = BinaryAssociation(
    name="pathVector148",
    ends={
        Property(name="build_PathVector149", type=build_PathGroupPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_PathGroupPredicate", type=build_PathVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathPattern150: BinaryAssociation = BinaryAssociation(
    name="pathPattern150",
    ends={
        Property(name="build_BExpression152", type=build_PathGroupPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="build_PathGroupPredicate151", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredCapabilities153: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilities153",
    ends={
        Property(name="build_RequiredCapability154", type=build_IRequiredCapabilityContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IRequiredCapabilityContainer", type=build_RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredPredicates155: BinaryAssociation = BinaryAssociation(
    name="requiredPredicates155",
    ends={
        Property(name="build_CapabilityPredicate157", type=build_IRequiredCapabilityContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IRequiredCapabilityContainer156", type=build_CapabilityPredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedCapabilities158: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities158",
    ends={
        Property(name="build_Capability159", type=build_IProvidedCapabilityContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IProvidedCapabilityContainer", type=build_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
builderQueries160: BinaryAssociation = BinaryAssociation(
    name="builderQueries160",
    ends={
        Property(name="build_BExpression162", type=build_BuilderQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderQuery161", type=build_BExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
unitQuery163: BinaryAssociation = BinaryAssociation(
    name="unitQuery163",
    ends={
        Property(name="build_BExpression165", type=build_BuilderQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderQuery164", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit190: BinaryAssociation = BinaryAssociation(
    name="unit190",
    ends={
        Property(name="build_BuildUnit191", type=build_EffectiveUnitFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveUnitFacade", type=build_BuildUnit, multiplicity=Multiplicity(0, 1))
    }
)
providedCapabilities192: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities192",
    ends={
        Property(name="build_EffectiveCapabilityFacade", type=build_EffectiveUnitFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveUnitFacade193", type=build_EffectiveCapabilityFacade, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCapabilities194: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilities194",
    ends={
        Property(name="build_EffectiveRequirementFacade", type=build_EffectiveUnitFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveUnitFacade195", type=build_EffectiveRequirementFacade, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaRequiredCapabilities196: BinaryAssociation = BinaryAssociation(
    name="metaRequiredCapabilities196",
    ends={
        Property(name="build_EffectiveRequirementFacade198", type=build_EffectiveUnitFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveUnitFacade197", type=build_EffectiveRequirementFacade, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitRequiredCapabilities199: BinaryAssociation = BinaryAssociation(
    name="unitRequiredCapabilities199",
    ends={
        Property(name="build_EffectiveRequirementFacade201", type=build_EffectiveUnitFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveUnitFacade200", type=build_EffectiveRequirementFacade, multiplicity=Multiplicity(0, 9999))
    }
)
imports166: BinaryAssociation = BinaryAssociation(
    name="imports166",
    ends={
        Property(name="build_IType167", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel", type=build_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions168: BinaryAssociation = BinaryAssociation(
    name="functions168",
    ends={
        Property(name="build_IFunction", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel169", type=build_IFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concerns170: BinaryAssociation = BinaryAssociation(
    name="concerns170",
    ends={
        Property(name="build_BConcern172", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel171", type=build_BConcern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertySets173: BinaryAssociation = BinaryAssociation(
    name="propertySets173",
    ends={
        Property(name="build_BPropertySet175", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel174", type=build_BPropertySet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories176: BinaryAssociation = BinaryAssociation(
    name="repositories176",
    ends={
        Property(name="build_Repository178", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel177", type=build_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers179: BinaryAssociation = BinaryAssociation(
    name="providers179",
    ends={
        Property(name="build_FirstFoundUnitProvider181", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel180", type=build_FirstFoundUnitProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultProperties182: BinaryAssociation = BinaryAssociation(
    name="defaultProperties182",
    ends={
        Property(name="build_BPropertySet184", type=build_BeeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModel183", type=build_BPropertySet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
beeModels185: BinaryAssociation = BinaryAssociation(
    name="beeModels185",
    ends={
        Property(name="build_BeeModel186", type=build_BeeHive, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeHive", type=build_BeeModel, multiplicity=Multiplicity(0, 9999))
    }
)
parent188: BinaryAssociation = BinaryAssociation(
    name="parent188",
    ends={
        Property(name="build_BeeHive189", type=build_BeeHive, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeHive187", type=build_BeeHive, multiplicity=Multiplicity(0, 1))
    }
)
repositories215: BinaryAssociation = BinaryAssociation(
    name="repositories215",
    ends={
        Property(name="build_IBuildUnitRepository216", type=build_CompoundBuildUnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="build_CompoundBuildUnitRepository", type=build_IBuildUnitRepository, multiplicity=Multiplicity(0, 9999))
    }
)
requirement202: BinaryAssociation = BinaryAssociation(
    name="requirement202",
    ends={
        Property(name="build_RequiredCapability204", type=build_EffectiveRequirementFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveRequirementFacade203", type=build_RequiredCapability, multiplicity=Multiplicity(0, 1))
    }
)
providedCapability205: BinaryAssociation = BinaryAssociation(
    name="providedCapability205",
    ends={
        Property(name="build_Capability207", type=build_EffectiveCapabilityFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_EffectiveCapabilityFacade206", type=build_Capability, multiplicity=Multiplicity(0, 1))
    }
)
builderReference208: BinaryAssociation = BinaryAssociation(
    name="builderReference208",
    ends={
        Property(name="build_BuilderCall209", type=build_BuilderCallFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderCallFacade", type=build_BuilderCall, multiplicity=Multiplicity(0, 1))
    }
)
requiredCapability210: BinaryAssociation = BinaryAssociation(
    name="requiredCapability210",
    ends={
        Property(name="build_RequiredCapability212", type=build_BuilderCallFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderCallFacade211", type=build_RequiredCapability, multiplicity=Multiplicity(0, 1))
    }
)
pathVectors213: BinaryAssociation = BinaryAssociation(
    name="pathVectors213",
    ends={
        Property(name="build_PathVector214", type=build_BuildSet, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildSet", type=build_PathVector, multiplicity=Multiplicity(0, 9999))
    }
)
include235: BinaryAssociation = BinaryAssociation(
    name="include235",
    ends={
        Property(name="build_BNamePredicate237", type=build_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Branch236", type=build_BNamePredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclude238: BinaryAssociation = BinaryAssociation(
    name="exclude238",
    ends={
        Property(name="build_BNamePredicate240", type=build_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Branch239", type=build_BNamePredicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchPoint241: BinaryAssociation = BinaryAssociation(
    name="branchPoint241",
    ends={
        Property(name="build_BExpression243", type=build_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Branch242", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
beeModels217: BinaryAssociation = BinaryAssociation(
    name="beeModels217",
    ends={
        Property(name="build_BeeModel218", type=build_BeeModelRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BeeModelRepository", type=build_BeeModel, multiplicity=Multiplicity(0, 9999))
    }
)
unit219: BinaryAssociation = BinaryAssociation(
    name="unit219",
    ends={
        Property(name="build_BuildUnit220", type=build_UnitResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitResolutionInfo", type=build_BuildUnit, multiplicity=Multiplicity(0, 1))
    }
)
context221: BinaryAssociation = BinaryAssociation(
    name="context221",
    ends={
        Property(name="build_BExecutionContext", type=build_UnitResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitResolutionInfo222", type=build_BExecutionContext, multiplicity=Multiplicity(0, 1))
    }
)
repoSwitch223: BinaryAssociation = BinaryAssociation(
    name="repoSwitch223",
    ends={
        Property(name="build_BSwitchExpression", type=build_SwitchUnitProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="build_SwitchUnitProvider", type=build_BSwitchExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches224: BinaryAssociation = BinaryAssociation(
    name="branches224",
    ends={
        Property(name="build_Branch", type=build_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Repository225", type=build_Branch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options226: BinaryAssociation = BinaryAssociation(
    name="options226",
    ends={
        Property(name="build_RepoOption228", type=build_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Repository227", type=build_RepoOption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildUnitRepository229: BinaryAssociation = BinaryAssociation(
    name="buildUnitRepository229",
    ends={
        Property(name="build_IBuildUnitRepository231", type=build_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Repository230", type=build_IBuildUnitRepository, multiplicity=Multiplicity(0, 1))
    }
)
address232: BinaryAssociation = BinaryAssociation(
    name="address232",
    ends={
        Property(name="build_BExpression234", type=build_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Repository233", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredPredicate251: BinaryAssociation = BinaryAssociation(
    name="requiredPredicate251",
    ends={
        Property(name="build_CapabilityPredicate252", type=build_BuildCallOnSelectedRequirements, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildCallOnSelectedRequirements", type=build_CapabilityPredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delegate244: BinaryAssociation = BinaryAssociation(
    name="delegate244",
    ends={
        Property(name="build_UnitProvider245", type=build_DelegatingUnitProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="build_DelegatingUnitProvider", type=build_UnitProvider, multiplicity=Multiplicity(1, 1))
    }
)
expr246: BinaryAssociation = BinaryAssociation(
    name="expr246",
    ends={
        Property(name="build_BExpression248", type=build_RepoOption, multiplicity=Multiplicity(1, 1)),
        Property(name="build_RepoOption247", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hostRequirements267: BinaryAssociation = BinaryAssociation(
    name="hostRequirements267",
    ends={
        Property(name="build_RequiredCapability269", type=build_FragmentHost, multiplicity=Multiplicity(1, 1)),
        Property(name="build_FragmentHost268", type=build_RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository249: BinaryAssociation = BinaryAssociation(
    name="repository249",
    ends={
        Property(name="build_Repository250", type=build_UnitRepositoryDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="build_UnitRepositoryDescription", type=build_Repository, multiplicity=Multiplicity(0, 1))
    }
)
withExpr253: BinaryAssociation = BinaryAssociation(
    name="withExpr253",
    ends={
        Property(name="build_BWithExpression", type=build_BuilderInputContextDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderInputContextDecorator", type=build_BWithExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr254: BinaryAssociation = BinaryAssociation(
    name="condExpr254",
    ends={
        Property(name="build_BExpression255", type=build_BuilderInputCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuilderInputCondition", type=build_BExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredCapability256: BinaryAssociation = BinaryAssociation(
    name="requiredCapability256",
    ends={
        Property(name="build_RequiredCapability257", type=build_BuildCallSingle, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildCallSingle", type=build_RequiredCapability, multiplicity=Multiplicity(0, 1))
    }
)
requiredCapabilityDeclaration258: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilityDeclaration258",
    ends={
        Property(name="build_RequiredCapability259", type=build_BuildCallOnDeclaredRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildCallOnDeclaredRequirement", type=build_RequiredCapability, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredCapabilityReference260: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilityReference260",
    ends={
        Property(name="build_RequiredCapability261", type=build_BuildCallOnReferencedRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="build_BuildCallOnReferencedRequirement", type=build_RequiredCapability, multiplicity=Multiplicity(0, 1))
    }
)
context262: BinaryAssociation = BinaryAssociation(
    name="context262",
    ends={
        Property(name="build_BExecutionContext263", type=build_IEffectiveFacade, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IEffectiveFacade", type=build_BExecutionContext, multiplicity=Multiplicity(0, 1))
    }
)
buildUnits264: BinaryAssociation = BinaryAssociation(
    name="buildUnits264",
    ends={
        Property(name="build_BuildUnit266", type=build_IBuildUnitContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="build_IBuildUnitContainer265", type=build_BuildUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_build_BuildUnit_VersionedCapability = Generalization(general=VersionedCapability, specific=build_BuildUnit)
gen_build_BuildUnit_BFunctionContainer = Generalization(general=BFunctionContainer, specific=build_BuildUnit)
gen_build_BuildUnit_IRequiredCapabilityContainer = Generalization(general=IRequiredCapabilityContainer, specific=build_BuildUnit)
gen_build_BuildUnit_IProvidedCapabilityContainer = Generalization(general=IProvidedCapabilityContainer, specific=build_BuildUnit)
gen_build_BuildUnit_IVarName = Generalization(general=IVarName, specific=build_BuildUnit)
gen_build_VersionedCapability_Capability = Generalization(general=Capability, specific=build_VersionedCapability)
gen_build_IBuilder_IProvidedCapabilityContainer = Generalization(general=IProvidedCapabilityContainer, specific=build_IBuilder)
gen_build_IBuilder_IFunction = Generalization(general=IFunction, specific=build_IBuilder)
gen_build_UnitProvider_BExpression = Generalization(general=BExpression, specific=build_UnitProvider)
gen_build_RepositoryUnitProvider_UnitProvider = Generalization(general=UnitProvider, specific=build_RepositoryUnitProvider)
gen_build_BuilderInputDecorator_BuilderInput = Generalization(general=BuilderInput, specific=build_BuilderInputDecorator)
gen_build_BuilderCall_BuilderInput = Generalization(general=BuilderInput, specific=build_BuilderCall)
gen_build_Capability_INamedValue = Generalization(general=INamedValue, specific=build_Capability)
gen_build_RequiredCapability_Capability = Generalization(general=Capability, specific=build_RequiredCapability)
gen_build_ImplementsPredicate_BExpression = Generalization(general=BExpression, specific=build_ImplementsPredicate)
gen_build_ProvidesPredicate_BExpression = Generalization(general=BExpression, specific=build_ProvidesPredicate)
gen_build_CompoundUnitProvider_UnitProvider = Generalization(general=UnitProvider, specific=build_CompoundUnitProvider)
gen_build_FirstFoundUnitProvider_CompoundUnitProvider = Generalization(general=CompoundUnitProvider, specific=build_FirstFoundUnitProvider)
gen_build_BestFoundUnitProvider_CompoundUnitProvider = Generalization(general=CompoundUnitProvider, specific=build_BestFoundUnitProvider)
gen_build_BuildConcernContext_BConcernContext = Generalization(general=BConcernContext, specific=build_BuildConcernContext)
gen_build_BuildConcernContext_IProvidedCapabilityContainer = Generalization(general=IProvidedCapabilityContainer, specific=build_BuildConcernContext)
gen_build_RequiresPredicate_BExpression = Generalization(general=BExpression, specific=build_RequiresPredicate)
gen_build_CapabilityPredicate_BExpression = Generalization(general=BExpression, specific=build_CapabilityPredicate)
gen_build_BuilderConcernContext_BuildConcernContext = Generalization(general=BuildConcernContext, specific=build_BuilderConcernContext)
gen_build_UnitNamePredicate_CapabilityPredicate = Generalization(general=CapabilityPredicate, specific=build_UnitNamePredicate)
gen_build_BuilderNamePredicate_BExpression = Generalization(general=BExpression, specific=build_BuilderNamePredicate)
gen_build_InputPredicate_BExpression = Generalization(general=BExpression, specific=build_InputPredicate)
gen_build_UnitConcernContext_BuildConcernContext = Generalization(general=BuildConcernContext, specific=build_UnitConcernContext)
gen_build_UnitConcernContext_IRequiredCapabilityContainer = Generalization(general=IRequiredCapabilityContainer, specific=build_UnitConcernContext)
gen_build_Builder_B3Function = Generalization(general=B3Function, specific=build_Builder)
gen_build_Builder_IBuilder = Generalization(general=IBuilder, specific=build_Builder)
gen_build_BuilderJava_BJavaFunction = Generalization(general=BJavaFunction, specific=build_BuilderJava)
gen_build_BuilderJava_IBuilder = Generalization(general=IBuilder, specific=build_BuilderJava)
gen_build_BuilderWrapper_BFunctionWrapper = Generalization(general=BFunctionWrapper, specific=build_BuilderWrapper)
gen_build_BuilderWrapper_IBuilder = Generalization(general=IBuilder, specific=build_BuilderWrapper)
gen_build_BeeModel_BChainedExpression = Generalization(general=BChainedExpression, specific=build_BeeModel)
gen_build_BeeModel_IBuildUnitContainer = Generalization(general=IBuildUnitContainer, specific=build_BeeModel)
gen_build_PathGroupPredicate_BExpression = Generalization(general=BExpression, specific=build_PathGroupPredicate)
gen_build_AliasedRequiredCapability_RequiredCapability = Generalization(general=RequiredCapability, specific=build_AliasedRequiredCapability)
gen_build_EffectiveUnitFacade_EffectiveFacade = Generalization(general=EffectiveFacade, specific=build_EffectiveUnitFacade)
gen_build_EffectiveRequirementFacade_EffectiveFacade = Generalization(general=EffectiveFacade, specific=build_EffectiveRequirementFacade)
gen_build_EffectiveFacade_IEffectiveFacade = Generalization(general=IEffectiveFacade, specific=build_EffectiveFacade)
gen_build_CompoundBuildUnitRepository_BuildUnitRepository = Generalization(general=BuildUnitRepository, specific=build_CompoundBuildUnitRepository)
gen_build_CompoundFirstFoundRepository_CompoundBuildUnitRepository = Generalization(general=CompoundBuildUnitRepository, specific=build_CompoundFirstFoundRepository)
gen_build_ExecutionStackRepository_BuildUnitRepository = Generalization(general=BuildUnitRepository, specific=build_ExecutionStackRepository)
gen_build_BeeModelRepository_BuildUnitRepository = Generalization(general=BuildUnitRepository, specific=build_BeeModelRepository)
gen_build_EffectiveCapabilityFacade_EffectiveFacade = Generalization(general=EffectiveFacade, specific=build_EffectiveCapabilityFacade)
gen_build_BuildSet_ITypedValueContainer = Generalization(general=ITypedValueContainer, specific=build_BuildSet)
gen_build_BuildResultContext_BInnerContext = Generalization(general=BInnerContext, specific=build_BuildResultContext)
gen_build_OutputPredicate_PathGroupPredicate = Generalization(general=PathGroupPredicate, specific=build_OutputPredicate)
gen_build_SourcePredicate_PathGroupPredicate = Generalization(general=PathGroupPredicate, specific=build_SourcePredicate)
gen_build_BuildUnitRepository_IBuildUnitRepository = Generalization(general=IBuildUnitRepository, specific=build_BuildUnitRepository)
gen_build_UnitResolutionInfo_ResolutionInfo = Generalization(general=ResolutionInfo, specific=build_UnitResolutionInfo)
gen_build_SwitchUnitProvider_UnitProvider = Generalization(general=UnitProvider, specific=build_SwitchUnitProvider)
gen_build_Repository_BExpression = Generalization(general=BExpression, specific=build_Repository)
gen_build_BuildCallOnSelectedRequirements_BuildCallMultiple = Generalization(general=BuildCallMultiple, specific=build_BuildCallOnSelectedRequirements)
gen_build_DelegatingUnitProvider_UnitProvider = Generalization(general=UnitProvider, specific=build_DelegatingUnitProvider)
gen_build_UnitRepositoryDescription_BuildUnitRepository = Generalization(general=BuildUnitRepository, specific=build_UnitRepositoryDescription)
gen_build_UnitParameterDeclaration_BParameterDeclaration = Generalization(general=BParameterDeclaration, specific=build_UnitParameterDeclaration)
gen_build_BuilderInputNameDecorator_BuilderInputDecorator = Generalization(general=BuilderInputDecorator, specific=build_BuilderInputNameDecorator)
gen_build_BuilderInputNameDecorator_INamedValue = Generalization(general=INamedValue, specific=build_BuilderInputNameDecorator)
gen_build_BuilderInputContextDecorator_BuilderInputDecorator = Generalization(general=BuilderInputDecorator, specific=build_BuilderInputContextDecorator)
gen_build_BuilderInputCondition_BuilderInputDecorator = Generalization(general=BuilderInputDecorator, specific=build_BuilderInputCondition)
gen_build_BuildCallMultiple_BuilderCall = Generalization(general=BuilderCall, specific=build_BuildCallMultiple)
gen_build_BuildCallSingle_BuilderCall = Generalization(general=BuilderCall, specific=build_BuildCallSingle)
gen_build_BuildCallOnDeclaredRequirement_BuildCallSingle = Generalization(general=BuildCallSingle, specific=build_BuildCallOnDeclaredRequirement)
gen_build_BuildCallOnReferencedRequirement_BuildCallSingle = Generalization(general=BuildCallSingle, specific=build_BuildCallOnReferencedRequirement)
gen_build_BuilderInputGroup_BuilderInputDecorator = Generalization(general=BuilderInputDecorator, specific=build_BuilderInputGroup)
gen_build_EffectiveBuilderCallFacade_BuilderCallFacade = Generalization(general=BuilderCallFacade, specific=build_EffectiveBuilderCallFacade)
gen_build_EffectiveBuilderCallFacade_IEffectiveFacade = Generalization(general=IEffectiveFacade, specific=build_EffectiveBuilderCallFacade)

# Domain Model
domain_model = DomainModel(
    name="build",
    types={build_BPropertySet, build_Synchronization, build_Repository, build_ContainerConfiguration, build_BuildUnit, VersionedCapability, BFunctionContainer, IRequiredCapabilityContainer, IProvidedCapabilityContainer, IVarName, build_IBuilder, build_RequiredCapability, build_IType, build_BConcern, build_UnitParameterDeclaration, build_VersionedCapability, Capability, build_ConditionalPathVector, build_FirstFoundUnitProvider, build_IBuildUnitContainer, build_FragmentHost, IFunction, build_BExpression, build_BuilderInput, build_PathGroup, build_BuilderQuery, build_UnitProvider, BExpression, build_RepositoryUnitProvider, UnitProvider, build_BuilderInputDecorator, BuilderInput, build_BuilderCall, build_BParameterList, build_Capability, INamedValue, build_PathVector, build_BNamePredicate, build_ImplementsPredicate, build_ProvidesPredicate, build_RepoOption, build_IBuildUnitRepository, build_CompoundUnitProvider, CompoundUnitProvider, build_BestFoundUnitProvider, build_BuildConcernContext, BConcernContext, build_RequiresPredicate, build_CapabilityPredicate, build_NameSpacePredicate, build_UnitNamePredicate, CapabilityPredicate, build_BuilderNamePredicate, build_InputPredicate, build_UnitConcernContext, BuildConcernContext, build_BuilderConcernContext, build_SourcePredicate, build_OutputPredicate, build_BParameterPredicate, B3Function, IBuilder, build_BuilderJava, BJavaFunction, build_BuilderWrapper, BFunctionWrapper, build_BeeModel, BChainedExpression, IBuildUnitContainer, build_PathGroupPredicate, build_AliasedRequiredCapability, RequiredCapability, build_IRequiredCapabilityContainer, build_IProvidedCapabilityContainer, build_Builder, build_EffectiveUnitFacade, EffectiveFacade, build_EffectiveCapabilityFacade, build_EffectiveRequirementFacade, build_IFunction, build_BeeHive, build_ResolutionInfo, build_EffectiveFacade, IEffectiveFacade, build_CompoundBuildUnitRepository, BuildUnitRepository, build_CompoundFirstFoundRepository, CompoundBuildUnitRepository, build_ExecutionStackRepository, build_BeeModelRepository, build_BuilderCallFacade, build_BuildSet, ITypedValueContainer, build_BuildResultContext, BInnerContext, PathGroupPredicate, build_BuildUnitRepository, IBuildUnitRepository, build_UnitResolutionInfo, ResolutionInfo, build_BExecutionContext, build_SwitchUnitProvider, build_BSwitchExpression, build_Branch, build_BuildCallOnSelectedRequirements, BuildCallMultiple, build_DelegatingUnitProvider, build_UnitRepositoryDescription, BParameterDeclaration, build_BuilderInputNameDecorator, BuilderInputDecorator, build_BuilderInputContextDecorator, build_BWithExpression, build_BuilderInputCondition, build_BuildCallMultiple, BuilderCall, build_BuildCallSingle, build_BuildCallOnDeclaredRequirement, BuildCallSingle, build_BuildCallOnReferencedRequirement, build_BuilderInputGroup, build_IEffectiveFacade, build_EffectiveBuilderCallFacade, BuilderCallFacade, TriState, MergeConflictStrategy, BranchPointType},
    associations={concerns5, defaultProperties7, synchronizations9, repositories11, containers13, propertySets15, builders0, metaRequiredCapabilities1, implements3, explicitUnitType39, source41, annotations44, pathVectors47, providers18, parent20, fragmentHosts22, postcondExpr24, precondExpr26, input29, output31, defaultProperties33, postinputcondExpr36, builderQueries59, repository61, builderInput49, parameters51, condExpr52, condExpr54, pathVectors57, namePredicate77, nameSpacePredicate79, type82, options63, buildUnitRepository65, providers67, agentType68, contextBlock71, defaultPropertiesAdditions74, capabilityPredicate76, requiredPredicatesRemovals103, query106, inputAdditions109, capabilityPredicate84, namePredicate86, capabilityPredicate88, builderPredicate90, builderContexts93, query94, requiresRemovals97, providesRemovals100, providesRemovals134, outputAnnotationAdditions137, sourceRemovals140, sourceAdditions142, inputRemovals112, outputAdditions115, outputRemovals118, funcExpr120, parameters123, precondExpr125, postcondExpr128, postinputcondExpr131, sourceAnnotationAdditions145, pathVector148, pathPattern150, requiredCapabilities153, requiredPredicates155, providedCapabilities158, builderQueries160, unitQuery163, unit190, providedCapabilities192, requiredCapabilities194, metaRequiredCapabilities196, unitRequiredCapabilities199, imports166, functions168, concerns170, propertySets173, repositories176, providers179, defaultProperties182, beeModels185, parent188, repositories215, requirement202, providedCapability205, builderReference208, requiredCapability210, pathVectors213, include235, exclude238, branchPoint241, beeModels217, unit219, context221, repoSwitch223, branches224, options226, buildUnitRepository229, address232, requiredPredicate251, delegate244, expr246, hostRequirements267, repository249, withExpr253, condExpr254, requiredCapability256, requiredCapabilityDeclaration258, requiredCapabilityReference260, context262, buildUnits264},
    generalizations={gen_build_BuildUnit_VersionedCapability, gen_build_BuildUnit_BFunctionContainer, gen_build_BuildUnit_IRequiredCapabilityContainer, gen_build_BuildUnit_IProvidedCapabilityContainer, gen_build_BuildUnit_IVarName, gen_build_VersionedCapability_Capability, gen_build_IBuilder_IProvidedCapabilityContainer, gen_build_IBuilder_IFunction, gen_build_UnitProvider_BExpression, gen_build_RepositoryUnitProvider_UnitProvider, gen_build_BuilderInputDecorator_BuilderInput, gen_build_BuilderCall_BuilderInput, gen_build_Capability_INamedValue, gen_build_RequiredCapability_Capability, gen_build_ImplementsPredicate_BExpression, gen_build_ProvidesPredicate_BExpression, gen_build_CompoundUnitProvider_UnitProvider, gen_build_FirstFoundUnitProvider_CompoundUnitProvider, gen_build_BestFoundUnitProvider_CompoundUnitProvider, gen_build_BuildConcernContext_BConcernContext, gen_build_BuildConcernContext_IProvidedCapabilityContainer, gen_build_RequiresPredicate_BExpression, gen_build_CapabilityPredicate_BExpression, gen_build_BuilderConcernContext_BuildConcernContext, gen_build_UnitNamePredicate_CapabilityPredicate, gen_build_BuilderNamePredicate_BExpression, gen_build_InputPredicate_BExpression, gen_build_UnitConcernContext_BuildConcernContext, gen_build_UnitConcernContext_IRequiredCapabilityContainer, gen_build_Builder_B3Function, gen_build_Builder_IBuilder, gen_build_BuilderJava_BJavaFunction, gen_build_BuilderJava_IBuilder, gen_build_BuilderWrapper_BFunctionWrapper, gen_build_BuilderWrapper_IBuilder, gen_build_BeeModel_BChainedExpression, gen_build_BeeModel_IBuildUnitContainer, gen_build_PathGroupPredicate_BExpression, gen_build_AliasedRequiredCapability_RequiredCapability, gen_build_EffectiveUnitFacade_EffectiveFacade, gen_build_EffectiveRequirementFacade_EffectiveFacade, gen_build_EffectiveFacade_IEffectiveFacade, gen_build_CompoundBuildUnitRepository_BuildUnitRepository, gen_build_CompoundFirstFoundRepository_CompoundBuildUnitRepository, gen_build_ExecutionStackRepository_BuildUnitRepository, gen_build_BeeModelRepository_BuildUnitRepository, gen_build_EffectiveCapabilityFacade_EffectiveFacade, gen_build_BuildSet_ITypedValueContainer, gen_build_BuildResultContext_BInnerContext, gen_build_OutputPredicate_PathGroupPredicate, gen_build_SourcePredicate_PathGroupPredicate, gen_build_BuildUnitRepository_IBuildUnitRepository, gen_build_UnitResolutionInfo_ResolutionInfo, gen_build_SwitchUnitProvider_UnitProvider, gen_build_Repository_BExpression, gen_build_BuildCallOnSelectedRequirements_BuildCallMultiple, gen_build_DelegatingUnitProvider_UnitProvider, gen_build_UnitRepositoryDescription_BuildUnitRepository, gen_build_UnitParameterDeclaration_BParameterDeclaration, gen_build_BuilderInputNameDecorator_BuilderInputDecorator, gen_build_BuilderInputNameDecorator_INamedValue, gen_build_BuilderInputContextDecorator_BuilderInputDecorator, gen_build_BuilderInputCondition_BuilderInputDecorator, gen_build_BuildCallMultiple_BuilderCall, gen_build_BuildCallSingle_BuilderCall, gen_build_BuildCallOnDeclaredRequirement_BuildCallSingle, gen_build_BuildCallOnReferencedRequirement_BuildCallSingle, gen_build_BuilderInputGroup_BuilderInputDecorator, gen_build_EffectiveBuilderCallFacade_BuilderCallFacade, gen_build_EffectiveBuilderCallFacade_IEffectiveFacade},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)