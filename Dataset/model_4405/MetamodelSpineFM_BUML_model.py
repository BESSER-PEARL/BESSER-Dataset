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
GroupState: Enumeration = Enumeration(
    name="GroupState",
    literals={
            EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="OPTIONAL"),
			EnumerationLiteral(name="ALTERNATIVE"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="MUTEX")
    }
)

ActionMode: Enumeration = Enumeration(
    name="ActionMode",
    literals={
            EnumerationLiteral(name="AUTOMATIC"),
			EnumerationLiteral(name="MANUAL"),
			EnumerationLiteral(name="FM")
    }
)

CPSStatus: Enumeration = Enumeration(
    name="CPSStatus",
    literals={
            EnumerationLiteral(name="PartiallyConfigured"),
			EnumerationLiteral(name="Configured"),
			EnumerationLiteral(name="Unconfigurable")
    }
)

# Classes
spinefm_FMModel_FeatureModel = Class(name="spinefm::FMModel::FeatureModel")
Feature = Class(name="Feature")
Constraint = Class(name="Constraint")
spinefm_FMModel_Feature = Class(name="spinefm::FMModel::Feature")
spinefm_MSPLModel_MultipleSoftwareProductLine = Class(name="spinefm::MSPLModel::MultipleSoftwareProductLine")
DomainElement = Class(name="DomainElement")
DEAssociation = Class(name="DEAssociation")
spinefm_MSPLModel_DEAssociation = Class(name="spinefm::MSPLModel::DEAssociation")
Group = Class(name="Group")
spinefm_FMModel_Group = Class(name="spinefm::FMModel::Group")
spinefm_FMModel_Constraint = Class(name="spinefm::FMModel::Constraint")
spinefm_MSPLModel_DomainElement = Class(name="spinefm::MSPLModel::DomainElement")
FeatureModel = Class(name="FeatureModel")
spinefm_ConfigurationModel_Configuration = Class(name="spinefm::ConfigurationModel::Configuration")
RestrictionFunction = Class(name="RestrictionFunction")
DEAssociationEnd = Class(name="DEAssociationEnd")
spinefm_MSPLModel_MultiplicityElement = Class(name="spinefm::MSPLModel::MultiplicityElement")
spinefm_MSPLModel_DEAssociationEnd = Class(name="spinefm::MSPLModel::DEAssociationEnd")
MultiplicityElement = Class(name="MultiplicityElement")
spinefm_ConfigurationModel_CompositeConfiguration = Class(name="spinefm::ConfigurationModel::CompositeConfiguration")
MultipleSoftwareProductLine = Class(name="MultipleSoftwareProductLine")
spinefm_ProcessModel_ConfigurationProcessStep = Class(name="spinefm::ProcessModel::ConfigurationProcessStep")
ConfigurationProcessStep = Class(name="ConfigurationProcessStep")
Link = Class(name="Link")
ConfigurationState = Class(name="ConfigurationState")
spinefm_ConfigurationModel_Link = Class(name="spinefm::ConfigurationModel::Link")
Configuration = Class(name="Configuration")
SystemActionModel_ActionOnFM = Class(name="SystemActionModel::ActionOnFM")
spinefm_ProcessModel_Context = Class(name="spinefm::ProcessModel::Context", is_abstract=True)
Context = Class(name="Context")
spinefm_ProcessModel_LocalContext = Class(name="spinefm::ProcessModel::LocalContext")
spinefm_ProcessModel_ContextManager = Class(name="spinefm::ProcessModel::ContextManager")
spinefm_ProcessModel_GlobalContext = Class(name="spinefm::ProcessModel::GlobalContext")
CompositeConfiguration = Class(name="CompositeConfiguration")
spinefm_SystemActionModel_SystemAction = Class(name="spinefm::SystemActionModel::SystemAction", is_abstract=True)
Step = Class(name="Step")
GlobalContext = Class(name="GlobalContext")
LocalContext = Class(name="LocalContext")
Past = Class(name="Past")
spinefm_ProcessModel_DeletedContextInformations = Class(name="spinefm::ProcessModel::DeletedContextInformations")
spinefm_SystemActionModel_ActionMoveConfiguration = Class(name="spinefm::SystemActionModel::ActionMoveConfiguration")
spinefm_SystemActionModel_ActionDeleteContext = Class(name="spinefm::SystemActionModel::ActionDeleteContext")
spinefm_SystemActionModel_ActionOnFM = Class(name="spinefm::SystemActionModel::ActionOnFM", is_abstract=True)
spinefm_SystemActionModel_ActionCreateConfiguration = Class(name="spinefm::SystemActionModel::ActionCreateConfiguration")
SystemAction = Class(name="SystemAction")
spinefm_SystemActionModel_ActionLink = Class(name="spinefm::SystemActionModel::ActionLink")
ContextManager = Class(name="ContextManager")
spinefm_SystemActionModel_ActionCreateContext = Class(name="spinefm::SystemActionModel::ActionCreateContext")
spinefm_SystemActionModel_ActionRenameConfig = Class(name="spinefm::SystemActionModel::ActionRenameConfig")
spinefm_SystemActionModel_ActionRenameProduct = Class(name="spinefm::SystemActionModel::ActionRenameProduct")
spinefm_SystemActionModel_ActionSetProductDescription = Class(name="spinefm::SystemActionModel::ActionSetProductDescription")
spinefm_UserActionModel_UserSelect = Class(name="spinefm::UserActionModel::UserSelect")
UserAction = Class(name="UserAction")
spinefm_UserActionModel_UserAction = Class(name="spinefm::UserActionModel::UserAction", is_abstract=True)
spinefm_SystemActionModel_ActionSelect = Class(name="spinefm::SystemActionModel::ActionSelect")
ActionOnFM = Class(name="ActionOnFM")
spinefm_SystemActionModel_ActionDeselect = Class(name="spinefm::SystemActionModel::ActionDeselect")
spinefm_SystemActionModel_ActionAddCTConstraint = Class(name="spinefm::SystemActionModel::ActionAddCTConstraint")
spinefm_SystemActionModel_ActionAbstractRename = Class(name="spinefm::SystemActionModel::ActionAbstractRename")
spinefm_SystemActionModel_ActionRenameCPS = Class(name="spinefm::SystemActionModel::ActionRenameCPS")
ActionAbstractRename = Class(name="ActionAbstractRename")
spinefm_UserActionModel_UserLinkConfiguration = Class(name="spinefm::UserActionModel::UserLinkConfiguration")
spinefm_UserActionModel_UserInit = Class(name="spinefm::UserActionModel::UserInit")
spinefm_UserActionModel_UserGenerate = Class(name="spinefm::UserActionModel::UserGenerate")
spinefm_UserActionModel_UserSavePast = Class(name="spinefm::UserActionModel::UserSavePast")
spinefm_UserActionModel_UserRenameElement = Class(name="spinefm::UserActionModel::UserRenameElement")
spinefm_UserActionModel_UserCloneContext = Class(name="spinefm::UserActionModel::UserCloneContext")
spinefm_HistoryModel_Step = Class(name="spinefm::HistoryModel::Step")
UserActionModel_spinefm_EObject = Class(name="UserActionModel::spinefm::EObject")
spinefm_UserActionModel_UserCreateContext = Class(name="spinefm::UserActionModel::UserCreateContext")
spinefm_UserActionModel_UserDeselect = Class(name="spinefm::UserActionModel::UserDeselect")
spinefm_UserActionModel_UserPropagate = Class(name="spinefm::UserActionModel::UserPropagate")
spinefm_UserActionModel_UserValidConfiguration = Class(name="spinefm::UserActionModel::UserValidConfiguration")
spinefm_RFModel_RestrictionFunction = Class(name="spinefm::RFModel::RestrictionFunction")
Rule = Class(name="Rule")
UserActionModel_UserAction = Class(name="UserActionModel::UserAction")
SystemActionModel_SystemAction = Class(name="SystemActionModel::SystemAction")
spinefm_HistoryModel_Past = Class(name="spinefm::HistoryModel::Past")
spinefm_RFModel_ConfigurationState = Class(name="spinefm::RFModel::ConfigurationState")
spinefm_RFModel_Rule = Class(name="spinefm::RFModel::Rule")

# spinefm_FMModel_FeatureModel class attributes and methods
spinefm_FMModel_FeatureModel_id: Property = Property(name="id", type=StringType)
spinefm_FMModel_FeatureModel_name: Property = Property(name="name", type=StringType)
spinefm_FMModel_FeatureModel_m_getStateFT: Method = Method(name="getStateFT", parameters={Parameter(name='feature')}, type=StringType)
spinefm_FMModel_FeatureModel_m_getFeatureFromName: Method = Method(name="getFeatureFromName", parameters={Parameter(name='name')}, type=StringType)
spinefm_FMModel_FeatureModel_m_addFeature: Method = Method(name="addFeature", parameters={Parameter(name='feature'), Parameter(name='state'), Parameter(name='name')})
spinefm_FMModel_FeatureModel.attributes={spinefm_FMModel_FeatureModel_id, spinefm_FMModel_FeatureModel_name}
spinefm_FMModel_FeatureModel.methods={spinefm_FMModel_FeatureModel_m_getFeatureFromName, spinefm_FMModel_FeatureModel_m_getStateFT, spinefm_FMModel_FeatureModel_m_addFeature}

# Feature class attributes and methods

# Constraint class attributes and methods

# spinefm_FMModel_Feature class attributes and methods
spinefm_FMModel_Feature_id: Property = Property(name="id", type=StringType)
spinefm_FMModel_Feature_name: Property = Property(name="name", type=StringType)
spinefm_FMModel_Feature_m_getAllChildrenFeatures: Method = Method(name="getAllChildrenFeatures", parameters={}, type=StringType)
spinefm_FMModel_Feature.attributes={spinefm_FMModel_Feature_id, spinefm_FMModel_Feature_name}
spinefm_FMModel_Feature.methods={spinefm_FMModel_Feature_m_getAllChildrenFeatures}

# spinefm_MSPLModel_MultipleSoftwareProductLine class attributes and methods
spinefm_MSPLModel_MultipleSoftwareProductLine_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getDomainElementByName: Method = Method(name="getDomainElementByName", parameters={Parameter(name='name')}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getValidAssociationsForDEs: Method = Method(name="getValidAssociationsForDEs", parameters={Parameter(name='target'), Parameter(name='source')}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getAssociationByName: Method = Method(name="getAssociationByName", parameters={Parameter(name='assoName')}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine.attributes={spinefm_MSPLModel_MultipleSoftwareProductLine_id}
spinefm_MSPLModel_MultipleSoftwareProductLine.methods={spinefm_MSPLModel_MultipleSoftwareProductLine_m_getValidAssociationsForDEs, spinefm_MSPLModel_MultipleSoftwareProductLine_m_getDomainElementByName, spinefm_MSPLModel_MultipleSoftwareProductLine_m_getAssociationByName}

# DomainElement class attributes and methods

# DEAssociation class attributes and methods

# spinefm_MSPLModel_DEAssociation class attributes and methods
spinefm_MSPLModel_DEAssociation_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DEAssociation_m_computeActionsToDo: Method = Method(name="computeActionsToDo", parameters={Parameter(name='CPSSource'), Parameter(name='CPSTarget')}, type=StringType)
spinefm_MSPLModel_DEAssociation_m_createAndAssociateInverseAssociation: Method = Method(name="createAndAssociateInverseAssociation", parameters={})
spinefm_MSPLModel_DEAssociation_m_isLinkBetweenDEs: Method = Method(name="isLinkBetweenDEs", parameters={Parameter(name='secondExtremity'), Parameter(name='firstExtremity')}, type=BooleanType)
spinefm_MSPLModel_DEAssociation_m_getOppositeExtremity: Method = Method(name="getOppositeExtremity", parameters={Parameter(name='source')}, type=StringType)
spinefm_MSPLModel_DEAssociation_m_getExtremityOfDE: Method = Method(name="getExtremityOfDE", parameters={Parameter(name='de')}, type=StringType)
spinefm_MSPLModel_DEAssociation.attributes={spinefm_MSPLModel_DEAssociation_id}
spinefm_MSPLModel_DEAssociation.methods={spinefm_MSPLModel_DEAssociation_m_getExtremityOfDE, spinefm_MSPLModel_DEAssociation_m_createAndAssociateInverseAssociation, spinefm_MSPLModel_DEAssociation_m_isLinkBetweenDEs, spinefm_MSPLModel_DEAssociation_m_computeActionsToDo, spinefm_MSPLModel_DEAssociation_m_getOppositeExtremity}

# Group class attributes and methods

# spinefm_FMModel_Group class attributes and methods
spinefm_FMModel_Group_state: Property = Property(name="state", type=StringType)
spinefm_FMModel_Group_m_getAllChildren: Method = Method(name="getAllChildren", parameters={}, type=StringType)
spinefm_FMModel_Group.attributes={spinefm_FMModel_Group_state}
spinefm_FMModel_Group.methods={spinefm_FMModel_Group_m_getAllChildren}

# spinefm_FMModel_Constraint class attributes and methods
spinefm_FMModel_Constraint_Rule: Property = Property(name="Rule", type=StringType)
spinefm_FMModel_Constraint.attributes={spinefm_FMModel_Constraint_Rule}

# spinefm_MSPLModel_DomainElement class attributes and methods
spinefm_MSPLModel_DomainElement_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DomainElement.attributes={spinefm_MSPLModel_DomainElement_id}

# FeatureModel class attributes and methods

# spinefm_ConfigurationModel_Configuration class attributes and methods
spinefm_ConfigurationModel_Configuration_id: Property = Property(name="id", type=StringType)
spinefm_ConfigurationModel_Configuration_description: Property = Property(name="description", type=StringType)
spinefm_ConfigurationModel_Configuration_m_canBeLinked: Method = Method(name="canBeLinked", parameters={Parameter(name='association')}, type=BooleanType)
spinefm_ConfigurationModel_Configuration_m_getFeatureModel: Method = Method(name="getFeatureModel", parameters={}, type=StringType)
spinefm_ConfigurationModel_Configuration_m_getLinkedConfigurationsOfDomainElement: Method = Method(name="getLinkedConfigurationsOfDomainElement", parameters={Parameter(name='de')}, type=StringType)
spinefm_ConfigurationModel_Configuration_m_isCompletlyLinked: Method = Method(name="isCompletlyLinked", parameters={}, type=BooleanType)
spinefm_ConfigurationModel_Configuration_m_getAllCPS: Method = Method(name="getAllCPS", parameters={}, type=StringType)
spinefm_ConfigurationModel_Configuration.attributes={spinefm_ConfigurationModel_Configuration_description, spinefm_ConfigurationModel_Configuration_id}
spinefm_ConfigurationModel_Configuration.methods={spinefm_ConfigurationModel_Configuration_m_canBeLinked, spinefm_ConfigurationModel_Configuration_m_isCompletlyLinked, spinefm_ConfigurationModel_Configuration_m_getAllCPS, spinefm_ConfigurationModel_Configuration_m_getLinkedConfigurationsOfDomainElement, spinefm_ConfigurationModel_Configuration_m_getFeatureModel}

# RestrictionFunction class attributes and methods

# DEAssociationEnd class attributes and methods

# spinefm_MSPLModel_MultiplicityElement class attributes and methods
spinefm_MSPLModel_MultiplicityElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
spinefm_MSPLModel_MultiplicityElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
spinefm_MSPLModel_MultiplicityElement_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_MultiplicityElement_m_respectBoundaries: Method = Method(name="respectBoundaries", parameters={Parameter(name='value')}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement_m_isExactlyOne: Method = Method(name="isExactlyOne", parameters={}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement_m_isLowerThanUpperBound: Method = Method(name="isLowerThanUpperBound", parameters={Parameter(name='value')}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement.attributes={spinefm_MSPLModel_MultiplicityElement_id, spinefm_MSPLModel_MultiplicityElement_upperBound, spinefm_MSPLModel_MultiplicityElement_lowerBound}
spinefm_MSPLModel_MultiplicityElement.methods={spinefm_MSPLModel_MultiplicityElement_m_respectBoundaries, spinefm_MSPLModel_MultiplicityElement_m_isExactlyOne, spinefm_MSPLModel_MultiplicityElement_m_isLowerThanUpperBound}

# spinefm_MSPLModel_DEAssociationEnd class attributes and methods
spinefm_MSPLModel_DEAssociationEnd_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DEAssociationEnd.attributes={spinefm_MSPLModel_DEAssociationEnd_id}

# MultiplicityElement class attributes and methods

# spinefm_ConfigurationModel_CompositeConfiguration class attributes and methods
spinefm_ConfigurationModel_CompositeConfiguration_name: Property = Property(name="name", type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_description: Property = Property(name="description", type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_m_isValid: Method = Method(name="isValid", parameters={}, type=BooleanType)
spinefm_ConfigurationModel_CompositeConfiguration_m_addConfiguration: Method = Method(name="addConfiguration", parameters={Parameter(name='conf')})
spinefm_ConfigurationModel_CompositeConfiguration_m_getConfigurationByName: Method = Method(name="getConfigurationByName", parameters={Parameter(name='confName')}, type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_m_createConfigurationLink: Method = Method(name="createConfigurationLink", parameters={Parameter(name='confTarget'), Parameter(name='confSource'), Parameter(name='asso')})
spinefm_ConfigurationModel_CompositeConfiguration_m_getCompatibleConfigurations: Method = Method(name="getCompatibleConfigurations", parameters={Parameter(name='confSource'), Parameter(name='asso')}, type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration.attributes={spinefm_ConfigurationModel_CompositeConfiguration_description, spinefm_ConfigurationModel_CompositeConfiguration_name}
spinefm_ConfigurationModel_CompositeConfiguration.methods={spinefm_ConfigurationModel_CompositeConfiguration_m_getCompatibleConfigurations, spinefm_ConfigurationModel_CompositeConfiguration_m_isValid, spinefm_ConfigurationModel_CompositeConfiguration_m_createConfigurationLink, spinefm_ConfigurationModel_CompositeConfiguration_m_getConfigurationByName, spinefm_ConfigurationModel_CompositeConfiguration_m_addConfiguration}

# MultipleSoftwareProductLine class attributes and methods

# spinefm_ProcessModel_ConfigurationProcessStep class attributes and methods
spinefm_ProcessModel_ConfigurationProcessStep_userConfig: Property = Property(name="userConfig", type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_history: Property = Property(name="history", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_status: Property = Property(name="status", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_description: Property = Property(name="description", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_m_isComplete: Method = Method(name="isComplete", parameters={}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_alreadyHaveAction: Method = Method(name="alreadyHaveAction", parameters={Parameter(name='a')}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_getConfName: Method = Method(name="getConfName", parameters={}, type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_m_setFMA: Method = Method(name="setFMA", parameters={Parameter(name='step'), Parameter(name='fma')})
spinefm_ProcessModel_ConfigurationProcessStep_m_isMergeableWithCPS: Method = Method(name="isMergeableWithCPS", parameters={Parameter(name='cps')}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_mergeWithExternalCPS: Method = Method(name="mergeWithExternalCPS", parameters={Parameter(name='confCPS'), Parameter(name='step'), Parameter(name='cm')})
spinefm_ProcessModel_ConfigurationProcessStep_m_captureImplicitActions: Method = Method(name="captureImplicitActions", parameters={Parameter(name='step'), Parameter(name='aof')})
spinefm_ProcessModel_ConfigurationProcessStep_m_recordActionDone: Method = Method(name="recordActionDone", parameters={Parameter(name='feature'), Parameter(name='aof')})
spinefm_ProcessModel_ConfigurationProcessStep_m_setFeatureUnselected: Method = Method(name="setFeatureUnselected", parameters={Parameter(name='feature')})
spinefm_ProcessModel_ConfigurationProcessStep.attributes={spinefm_ProcessModel_ConfigurationProcessStep_status, spinefm_ProcessModel_ConfigurationProcessStep_userConfig, spinefm_ProcessModel_ConfigurationProcessStep_history, spinefm_ProcessModel_ConfigurationProcessStep_description, spinefm_ProcessModel_ConfigurationProcessStep_id}
spinefm_ProcessModel_ConfigurationProcessStep.methods={spinefm_ProcessModel_ConfigurationProcessStep_m_setFMA, spinefm_ProcessModel_ConfigurationProcessStep_m_getConfName, spinefm_ProcessModel_ConfigurationProcessStep_m_captureImplicitActions, spinefm_ProcessModel_ConfigurationProcessStep_m_isComplete, spinefm_ProcessModel_ConfigurationProcessStep_m_recordActionDone, spinefm_ProcessModel_ConfigurationProcessStep_m_setFeatureUnselected, spinefm_ProcessModel_ConfigurationProcessStep_m_isMergeableWithCPS, spinefm_ProcessModel_ConfigurationProcessStep_m_mergeWithExternalCPS, spinefm_ProcessModel_ConfigurationProcessStep_m_alreadyHaveAction}

# ConfigurationProcessStep class attributes and methods

# Link class attributes and methods

# ConfigurationState class attributes and methods

# spinefm_ConfigurationModel_Link class attributes and methods
spinefm_ConfigurationModel_Link_id: Property = Property(name="id", type=StringType)
spinefm_ConfigurationModel_Link_m_getAssociatedConfiguration: Method = Method(name="getAssociatedConfiguration", parameters={Parameter(name='conf')}, type=StringType)
spinefm_ConfigurationModel_Link.attributes={spinefm_ConfigurationModel_Link_id}
spinefm_ConfigurationModel_Link.methods={spinefm_ConfigurationModel_Link_m_getAssociatedConfiguration}

# Configuration class attributes and methods

# SystemActionModel_ActionOnFM class attributes and methods

# spinefm_ProcessModel_Context class attributes and methods
spinefm_ProcessModel_Context_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_Context_m_addCPS: Method = Method(name="addCPS", parameters={Parameter(name='cps')})
spinefm_ProcessModel_Context_m_getCPSOfDE: Method = Method(name="getCPSOfDE", parameters={Parameter(name='de')}, type=StringType)
spinefm_ProcessModel_Context_m_mergeExternalCPS: Method = Method(name="mergeExternalCPS", parameters={Parameter(name='cm'), Parameter(name='step'), Parameter(name='externalCPS')})
spinefm_ProcessModel_Context.attributes={spinefm_ProcessModel_Context_id}
spinefm_ProcessModel_Context.methods={spinefm_ProcessModel_Context_m_getCPSOfDE, spinefm_ProcessModel_Context_m_addCPS, spinefm_ProcessModel_Context_m_mergeExternalCPS}

# Context class attributes and methods

# spinefm_ProcessModel_LocalContext class attributes and methods

# spinefm_ProcessModel_ContextManager class attributes and methods
spinefm_ProcessModel_ContextManager_fma: Property = Property(name="fma", type=StringType)
spinefm_ProcessModel_ContextManager_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_ContextManager_m_propagate: Method = Method(name="propagate", parameters={Parameter(name='CPS'), Parameter(name='step'), Parameter(name='context')})
spinefm_ProcessModel_ContextManager_m_init: Method = Method(name="init", parameters={Parameter(name='step')})
spinefm_ProcessModel_ContextManager_m_createNewContext: Method = Method(name="createNewContext", parameters={Parameter(name='step')}, type=StringType)
spinefm_ProcessModel_ContextManager_m_getContextFromId: Method = Method(name="getContextFromId", parameters={Parameter(name='id')}, type=StringType)
spinefm_ProcessModel_ContextManager_m_cloningExistingContext: Method = Method(name="cloningExistingContext", parameters={Parameter(name='contextSource')}, type=StringType)
spinefm_ProcessModel_ContextManager_m_removeContext: Method = Method(name="removeContext", parameters={Parameter(name='context')})
spinefm_ProcessModel_ContextManager_m_restoreContext: Method = Method(name="restoreContext", parameters={Parameter(name='context')})
spinefm_ProcessModel_ContextManager_m_getCPSFromId: Method = Method(name="getCPSFromId", parameters={Parameter(name='id')}, type=StringType)
spinefm_ProcessModel_ContextManager.attributes={spinefm_ProcessModel_ContextManager_id, spinefm_ProcessModel_ContextManager_fma}
spinefm_ProcessModel_ContextManager.methods={spinefm_ProcessModel_ContextManager_m_cloningExistingContext, spinefm_ProcessModel_ContextManager_m_createNewContext, spinefm_ProcessModel_ContextManager_m_restoreContext, spinefm_ProcessModel_ContextManager_m_getContextFromId, spinefm_ProcessModel_ContextManager_m_propagate, spinefm_ProcessModel_ContextManager_m_getCPSFromId, spinefm_ProcessModel_ContextManager_m_init, spinefm_ProcessModel_ContextManager_m_removeContext}

# spinefm_ProcessModel_GlobalContext class attributes and methods

# CompositeConfiguration class attributes and methods

# spinefm_SystemActionModel_SystemAction class attributes and methods
spinefm_SystemActionModel_SystemAction_cpsHistory: Property = Property(name="cpsHistory", type=StringType)
spinefm_SystemActionModel_SystemAction_type: Property = Property(name="type", type=StringType)
spinefm_SystemActionModel_SystemAction_m_apply: Method = Method(name="apply", parameters={})
spinefm_SystemActionModel_SystemAction_m_isSameObject: Method = Method(name="isSameObject", parameters={Parameter(name='o')}, type=BooleanType)
spinefm_SystemActionModel_SystemAction_m_undo: Method = Method(name="undo", parameters={})
spinefm_SystemActionModel_SystemAction.attributes={spinefm_SystemActionModel_SystemAction_cpsHistory, spinefm_SystemActionModel_SystemAction_type}
spinefm_SystemActionModel_SystemAction.methods={spinefm_SystemActionModel_SystemAction_m_isSameObject, spinefm_SystemActionModel_SystemAction_m_apply, spinefm_SystemActionModel_SystemAction_m_undo}

# Step class attributes and methods

# GlobalContext class attributes and methods

# LocalContext class attributes and methods

# Past class attributes and methods

# spinefm_ProcessModel_DeletedContextInformations class attributes and methods
spinefm_ProcessModel_DeletedContextInformations_deletedContext: Property = Property(name="deletedContext", type=StringType)
spinefm_ProcessModel_DeletedContextInformations.attributes={spinefm_ProcessModel_DeletedContextInformations_deletedContext}

# spinefm_SystemActionModel_ActionMoveConfiguration class attributes and methods

# spinefm_SystemActionModel_ActionDeleteContext class attributes and methods

# spinefm_SystemActionModel_ActionOnFM class attributes and methods
spinefm_SystemActionModel_ActionOnFM_fma: Property = Property(name="fma", type=StringType)
spinefm_SystemActionModel_ActionOnFM_m_cloneAction: Method = Method(name="cloneAction", parameters={}, type=StringType)
spinefm_SystemActionModel_ActionOnFM.attributes={spinefm_SystemActionModel_ActionOnFM_fma}
spinefm_SystemActionModel_ActionOnFM.methods={spinefm_SystemActionModel_ActionOnFM_m_cloneAction}

# spinefm_SystemActionModel_ActionCreateConfiguration class attributes and methods

# SystemAction class attributes and methods

# spinefm_SystemActionModel_ActionLink class attributes and methods

# ContextManager class attributes and methods

# spinefm_SystemActionModel_ActionCreateContext class attributes and methods

# spinefm_SystemActionModel_ActionRenameConfig class attributes and methods

# spinefm_SystemActionModel_ActionRenameProduct class attributes and methods

# spinefm_SystemActionModel_ActionSetProductDescription class attributes and methods

# spinefm_UserActionModel_UserSelect class attributes and methods
spinefm_UserActionModel_UserSelect_domainElementName: Property = Property(name="domainElementName", type=StringType)
spinefm_UserActionModel_UserSelect_contextID: Property = Property(name="contextID", type=StringType)
spinefm_UserActionModel_UserSelect_featureName: Property = Property(name="featureName", type=StringType)
spinefm_UserActionModel_UserSelect.attributes={spinefm_UserActionModel_UserSelect_contextID, spinefm_UserActionModel_UserSelect_featureName, spinefm_UserActionModel_UserSelect_domainElementName}

# UserAction class attributes and methods

# spinefm_UserActionModel_UserAction class attributes and methods
spinefm_UserActionModel_UserAction_type: Property = Property(name="type", type=StringType)
spinefm_UserActionModel_UserAction_m_apply: Method = Method(name="apply", parameters={})
spinefm_UserActionModel_UserAction_m_initManualAction: Method = Method(name="initManualAction", parameters={Parameter(name='contextManager')})
spinefm_UserActionModel_UserAction_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
spinefm_UserActionModel_UserAction_m_cloneActionWithStringAttributes: Method = Method(name="cloneActionWithStringAttributes", parameters={}, type=StringType)
spinefm_UserActionModel_UserAction_m_precondition: Method = Method(name="precondition", parameters={}, type=StringType)
spinefm_UserActionModel_UserAction_m_postcondition: Method = Method(name="postcondition", parameters={})
spinefm_UserActionModel_UserAction_m_transformContextNameToSave: Method = Method(name="transformContextNameToSave", parameters={Parameter(name='contextID')}, type=StringType)
spinefm_UserActionModel_UserAction.attributes={spinefm_UserActionModel_UserAction_type}
spinefm_UserActionModel_UserAction.methods={spinefm_UserActionModel_UserAction_m_transformContextNameToSave, spinefm_UserActionModel_UserAction_m_getDescription, spinefm_UserActionModel_UserAction_m_postcondition, spinefm_UserActionModel_UserAction_m_initManualAction, spinefm_UserActionModel_UserAction_m_cloneActionWithStringAttributes, spinefm_UserActionModel_UserAction_m_apply, spinefm_UserActionModel_UserAction_m_precondition}

# spinefm_SystemActionModel_ActionSelect class attributes and methods

# ActionOnFM class attributes and methods

# spinefm_SystemActionModel_ActionDeselect class attributes and methods

# spinefm_SystemActionModel_ActionAddCTConstraint class attributes and methods

# spinefm_SystemActionModel_ActionAbstractRename class attributes and methods
spinefm_SystemActionModel_ActionAbstractRename_oldName: Property = Property(name="oldName", type=StringType)
spinefm_SystemActionModel_ActionAbstractRename_newName: Property = Property(name="newName", type=StringType)
spinefm_SystemActionModel_ActionAbstractRename.attributes={spinefm_SystemActionModel_ActionAbstractRename_oldName, spinefm_SystemActionModel_ActionAbstractRename_newName}

# spinefm_SystemActionModel_ActionRenameCPS class attributes and methods

# ActionAbstractRename class attributes and methods

# spinefm_UserActionModel_UserLinkConfiguration class attributes and methods
spinefm_UserActionModel_UserLinkConfiguration_confSourceName: Property = Property(name="confSourceName", type=StringType)
spinefm_UserActionModel_UserLinkConfiguration_confTargetName: Property = Property(name="confTargetName", type=StringType)
spinefm_UserActionModel_UserLinkConfiguration_assoName: Property = Property(name="assoName", type=StringType)
spinefm_UserActionModel_UserLinkConfiguration.attributes={spinefm_UserActionModel_UserLinkConfiguration_assoName, spinefm_UserActionModel_UserLinkConfiguration_confSourceName, spinefm_UserActionModel_UserLinkConfiguration_confTargetName}

# spinefm_UserActionModel_UserInit class attributes and methods
spinefm_UserActionModel_UserInit_filePath: Property = Property(name="filePath", type=StringType)
spinefm_UserActionModel_UserInit_pastPath: Property = Property(name="pastPath", type=StringType)
spinefm_UserActionModel_UserInit_confDescription: Property = Property(name="confDescription", type=StringType)
spinefm_UserActionModel_UserInit.attributes={spinefm_UserActionModel_UserInit_confDescription, spinefm_UserActionModel_UserInit_pastPath, spinefm_UserActionModel_UserInit_filePath}

# spinefm_UserActionModel_UserGenerate class attributes and methods
spinefm_UserActionModel_UserGenerate_path: Property = Property(name="path", type=StringType)
spinefm_UserActionModel_UserGenerate.attributes={spinefm_UserActionModel_UserGenerate_path}

# spinefm_UserActionModel_UserSavePast class attributes and methods
spinefm_UserActionModel_UserSavePast_destPath: Property = Property(name="destPath", type=StringType)
spinefm_UserActionModel_UserSavePast.attributes={spinefm_UserActionModel_UserSavePast_destPath}

# spinefm_UserActionModel_UserRenameElement class attributes and methods
spinefm_UserActionModel_UserRenameElement_name: Property = Property(name="name", type=StringType)
spinefm_UserActionModel_UserRenameElement_elementType: Property = Property(name="elementType", type=StringType)
spinefm_UserActionModel_UserRenameElement_elementID: Property = Property(name="elementID", type=StringType)
spinefm_UserActionModel_UserRenameElement.attributes={spinefm_UserActionModel_UserRenameElement_elementType, spinefm_UserActionModel_UserRenameElement_name, spinefm_UserActionModel_UserRenameElement_elementID}

# spinefm_UserActionModel_UserCloneContext class attributes and methods
spinefm_UserActionModel_UserCloneContext_contextID: Property = Property(name="contextID", type=StringType)
spinefm_UserActionModel_UserCloneContext.attributes={spinefm_UserActionModel_UserCloneContext_contextID}

# spinefm_HistoryModel_Step class attributes and methods
spinefm_HistoryModel_Step_id: Property = Property(name="id", type=StringType)
spinefm_HistoryModel_Step_m_undoActions: Method = Method(name="undoActions", parameters={})
spinefm_HistoryModel_Step_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
spinefm_HistoryModel_Step_m_cloneStepWithoutSystemActions: Method = Method(name="cloneStepWithoutSystemActions", parameters={}, type=StringType)
spinefm_HistoryModel_Step.attributes={spinefm_HistoryModel_Step_id}
spinefm_HistoryModel_Step.methods={spinefm_HistoryModel_Step_m_undoActions, spinefm_HistoryModel_Step_m_cloneStepWithoutSystemActions, spinefm_HistoryModel_Step_m_getDescription}

# UserActionModel_spinefm_EObject class attributes and methods

# spinefm_UserActionModel_UserCreateContext class attributes and methods

# spinefm_UserActionModel_UserDeselect class attributes and methods
spinefm_UserActionModel_UserDeselect_domainElementName: Property = Property(name="domainElementName", type=StringType)
spinefm_UserActionModel_UserDeselect_contextID: Property = Property(name="contextID", type=StringType)
spinefm_UserActionModel_UserDeselect_featureName: Property = Property(name="featureName", type=StringType)
spinefm_UserActionModel_UserDeselect.attributes={spinefm_UserActionModel_UserDeselect_featureName, spinefm_UserActionModel_UserDeselect_contextID, spinefm_UserActionModel_UserDeselect_domainElementName}

# spinefm_UserActionModel_UserPropagate class attributes and methods
spinefm_UserActionModel_UserPropagate_domainElementName: Property = Property(name="domainElementName", type=StringType)
spinefm_UserActionModel_UserPropagate_contextID: Property = Property(name="contextID", type=StringType)
spinefm_UserActionModel_UserPropagate.attributes={spinefm_UserActionModel_UserPropagate_domainElementName, spinefm_UserActionModel_UserPropagate_contextID}

# spinefm_UserActionModel_UserValidConfiguration class attributes and methods
spinefm_UserActionModel_UserValidConfiguration_domainElementName: Property = Property(name="domainElementName", type=StringType)
spinefm_UserActionModel_UserValidConfiguration_contextID: Property = Property(name="contextID", type=StringType)
spinefm_UserActionModel_UserValidConfiguration.attributes={spinefm_UserActionModel_UserValidConfiguration_domainElementName, spinefm_UserActionModel_UserValidConfiguration_contextID}

# spinefm_RFModel_RestrictionFunction class attributes and methods
spinefm_RFModel_RestrictionFunction_id: Property = Property(name="id", type=StringType)
spinefm_RFModel_RestrictionFunction_m_createAndAssociateInverseRestFunc: Method = Method(name="createAndAssociateInverseRestFunc", parameters={}, type=StringType)
spinefm_RFModel_RestrictionFunction.attributes={spinefm_RFModel_RestrictionFunction_id}
spinefm_RFModel_RestrictionFunction.methods={spinefm_RFModel_RestrictionFunction_m_createAndAssociateInverseRestFunc}

# Rule class attributes and methods

# UserActionModel_UserAction class attributes and methods

# SystemActionModel_SystemAction class attributes and methods

# spinefm_HistoryModel_Past class attributes and methods
spinefm_HistoryModel_Past_modelPath: Property = Property(name="modelPath", type=StringType)
spinefm_HistoryModel_Past_description: Property = Property(name="description", type=StringType)
spinefm_HistoryModel_Past_id: Property = Property(name="id", type=StringType)
spinefm_HistoryModel_Past_rootPath: Property = Property(name="rootPath", type=StringType)
spinefm_HistoryModel_Past_m_createStep: Method = Method(name="createStep", parameters={Parameter(name='action')}, type=StringType)
spinefm_HistoryModel_Past_m_undoLastAction: Method = Method(name="undoLastAction", parameters={})
spinefm_HistoryModel_Past_m_clonePastWithoutSystemActions: Method = Method(name="clonePastWithoutSystemActions", parameters={}, type=StringType)
spinefm_HistoryModel_Past_m_undoAction: Method = Method(name="undoAction", parameters={Parameter(name='step')})
spinefm_HistoryModel_Past_m_getStepFromId: Method = Method(name="getStepFromId", parameters={Parameter(name='stepId')}, type=StringType)
spinefm_HistoryModel_Past.attributes={spinefm_HistoryModel_Past_id, spinefm_HistoryModel_Past_rootPath, spinefm_HistoryModel_Past_modelPath, spinefm_HistoryModel_Past_description}
spinefm_HistoryModel_Past.methods={spinefm_HistoryModel_Past_m_createStep, spinefm_HistoryModel_Past_m_undoAction, spinefm_HistoryModel_Past_m_getStepFromId, spinefm_HistoryModel_Past_m_clonePastWithoutSystemActions, spinefm_HistoryModel_Past_m_undoLastAction}

# spinefm_RFModel_ConfigurationState class attributes and methods
spinefm_RFModel_ConfigurationState_id: Property = Property(name="id", type=StringType)
spinefm_RFModel_ConfigurationState_m_isIncludedIn: Method = Method(name="isIncludedIn", parameters={Parameter(name='otherState')}, type=BooleanType)
spinefm_RFModel_ConfigurationState.attributes={spinefm_RFModel_ConfigurationState_id}
spinefm_RFModel_ConfigurationState.methods={spinefm_RFModel_ConfigurationState_m_isIncludedIn}

# spinefm_RFModel_Rule class attributes and methods
spinefm_RFModel_Rule_id: Property = Property(name="id", type=StringType)
spinefm_RFModel_Rule_m_createInverseRule: Method = Method(name="createInverseRule", parameters={}, type=StringType)
spinefm_RFModel_Rule.attributes={spinefm_RFModel_Rule_id}
spinefm_RFModel_Rule.methods={spinefm_RFModel_Rule_m_createInverseRule}

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="Feature", type=spinefm_FMModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_FMModel_FeatureModel", type=Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="Constraint", type=spinefm_FMModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_FMModel_FeatureModel2", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domainElements6: BinaryAssociation = BinaryAssociation(
    name="domainElements6",
    ends={
        Property(name="DomainElement", type=spinefm_MSPLModel_MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_MultipleSoftwareProductLine", type=DomainElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
associations7: BinaryAssociation = BinaryAssociation(
    name="associations7",
    ends={
        Property(name="DEAssociation", type=spinefm_MSPLModel_MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_MultipleSoftwareProductLine8", type=DEAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Group", type=spinefm_FMModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_FMModel_Feature", type=Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features4: BinaryAssociation = BinaryAssociation(
    name="features4",
    ends={
        Property(name="Feature5", type=spinefm_FMModel_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_FMModel_Group", type=Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
MultiplicityElement16: BinaryAssociation = BinaryAssociation(
    name="MultiplicityElement16",
    ends={
        Property(name="MultiplicityElement17", type=spinefm_MSPLModel_DomainElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DomainElement", type=MultiplicityElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refers_on18: BinaryAssociation = BinaryAssociation(
    name="refers_on18",
    ends={
        Property(name="FeatureModel", type=spinefm_MSPLModel_DomainElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DomainElement19", type=FeatureModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
belongs_to20: BinaryAssociation = BinaryAssociation(
    name="belongs_to20",
    ends={
        Property(name="DEAssociation22", type=spinefm_MSPLModel_DomainElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DomainElement21", type=DEAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
restrictionFunction9: BinaryAssociation = BinaryAssociation(
    name="restrictionFunction9",
    ends={
        Property(name="RestrictionFunction", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation", type=RestrictionFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extremity10: BinaryAssociation = BinaryAssociation(
    name="extremity10",
    ends={
        Property(name="DEAssociationEnd", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation11", type=DEAssociationEnd, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
LinkMultiplicity12: BinaryAssociation = BinaryAssociation(
    name="LinkMultiplicity12",
    ends={
        Property(name="MultiplicityElement", type=spinefm_MSPLModel_DEAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociationEnd", type=MultiplicityElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
apply_on13: BinaryAssociation = BinaryAssociation(
    name="apply_on13",
    ends={
        Property(name="DomainElement15", type=spinefm_MSPLModel_DEAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociationEnd14", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
target37: BinaryAssociation = BinaryAssociation(
    name="target37",
    ends={
        Property(name="Configuration39", type=spinefm_ConfigurationModel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Link38", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
subConfigurations40: BinaryAssociation = BinaryAssociation(
    name="subConfigurations40",
    ends={
        Property(name="Configuration41", type=spinefm_ConfigurationModel_CompositeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_CompositeConfiguration", type=Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links42: BinaryAssociation = BinaryAssociation(
    name="links42",
    ends={
        Property(name="Link44", type=spinefm_ConfigurationModel_CompositeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_CompositeConfiguration43", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mspl45: BinaryAssociation = BinaryAssociation(
    name="mspl45",
    ends={
        Property(name="MultipleSoftwareProductLine", type=spinefm_ConfigurationModel_CompositeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_CompositeConfiguration46", type=MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1))
    }
)
CPSRef23: BinaryAssociation = BinaryAssociation(
    name="CPSRef23",
    ends={
        Property(name="ProcessModel", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="ConfigurationProcessStep", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
belongs_to24: BinaryAssociation = BinaryAssociation(
    name="belongs_to24",
    ends={
        Property(name="Link", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration", type=Link, multiplicity=Multiplicity(0, 9999))
    }
)
state25: BinaryAssociation = BinaryAssociation(
    name="state25",
    ends={
        Property(name="ConfigurationState", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration26", type=ConfigurationState, multiplicity=Multiplicity(1, 1))
    }
)
domainElement27: BinaryAssociation = BinaryAssociation(
    name="domainElement27",
    ends={
        Property(name="DomainElement29", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration28", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
clonedCPS30: BinaryAssociation = BinaryAssociation(
    name="clonedCPS30",
    ends={
        Property(name="ConfigurationProcessStep32", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration31", type=ConfigurationProcessStep, multiplicity=Multiplicity(0, 9999))
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="Configuration", type=spinefm_ConfigurationModel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Link", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
relatedAssociation34: BinaryAssociation = BinaryAssociation(
    name="relatedAssociation34",
    ends={
        Property(name="DEAssociation36", type=spinefm_ConfigurationModel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Link35", type=DEAssociation, multiplicity=Multiplicity(1, 1))
    }
)
configuration51: BinaryAssociation = BinaryAssociation(
    name="configuration51",
    ends={
        Property(name="ConfigurationModel", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="Configuration52", type=Configuration, multiplicity=Multiplicity(0, 1))
    }
)
state53: BinaryAssociation = BinaryAssociation(
    name="state53",
    ends={
        Property(name="ConfigurationState55", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep54", type=ConfigurationState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actionsDone56: BinaryAssociation = BinaryAssociation(
    name="actionsDone56",
    ends={
        Property(name="SystemActionModel_ActionOnFM", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep57", type=SystemActionModel_ActionOnFM, multiplicity=Multiplicity(0, 9999))
    }
)
domainElement47: BinaryAssociation = BinaryAssociation(
    name="domainElement47",
    ends={
        Property(name="DomainElement48", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
context49: BinaryAssociation = BinaryAssociation(
    name="context49",
    ends={
        Property(name="Context", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep50", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
configuration60: BinaryAssociation = BinaryAssociation(
    name="configuration60",
    ends={
        Property(name="spinefm_ProcessModel_GlobalContext", type=CompositeConfiguration, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CompositeConfiguration", type=spinefm_ProcessModel_GlobalContext, multiplicity=Multiplicity(1, 1))
    }
)
configurations61: BinaryAssociation = BinaryAssociation(
    name="configurations61",
    ends={
        Property(name="Configuration62", type=spinefm_ProcessModel_LocalContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_LocalContext", type=Configuration, multiplicity=Multiplicity(1, 9999))
    }
)
CPS58: BinaryAssociation = BinaryAssociation(
    name="CPS58",
    ends={
        Property(name="ConfigurationProcessStep59", type=spinefm_ProcessModel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_Context", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
step73: BinaryAssociation = BinaryAssociation(
    name="step73",
    ends={
        Property(name="HistoryModel", type=spinefm_SystemActionModel_SystemAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Step", type=Step, multiplicity=Multiplicity(1, 1))
    }
)
mspl63: BinaryAssociation = BinaryAssociation(
    name="mspl63",
    ends={
        Property(name="MultipleSoftwareProductLine64", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager", type=MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1))
    }
)
globalContext65: BinaryAssociation = BinaryAssociation(
    name="globalContext65",
    ends={
        Property(name="GlobalContext", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager66", type=GlobalContext, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localContexts67: BinaryAssociation = BinaryAssociation(
    name="localContexts67",
    ends={
        Property(name="LocalContext", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager68", type=LocalContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
past69: BinaryAssociation = BinaryAssociation(
    name="past69",
    ends={
        Property(name="Past", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager70", type=Past, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replacedBy71: BinaryAssociation = BinaryAssociation(
    name="replacedBy71",
    ends={
        Property(name="Context72", type=spinefm_ProcessModel_DeletedContextInformations, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_DeletedContextInformations", type=Context, multiplicity=Multiplicity(0, 1))
    }
)
contextManager92: BinaryAssociation = BinaryAssociation(
    name="contextManager92",
    ends={
        Property(name="spinefm_SystemActionModel_ActionCreateContext", type=ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ContextManager93", type=spinefm_SystemActionModel_ActionCreateContext, multiplicity=Multiplicity(1, 1))
    }
)
context94: BinaryAssociation = BinaryAssociation(
    name="context94",
    ends={
        Property(name="Context96", type=spinefm_SystemActionModel_ActionCreateContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionCreateContext95", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
configuration97: BinaryAssociation = BinaryAssociation(
    name="configuration97",
    ends={
        Property(name="Configuration98", type=spinefm_SystemActionModel_ActionMoveConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionMoveConfiguration", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
cpsSource99: BinaryAssociation = BinaryAssociation(
    name="cpsSource99",
    ends={
        Property(name="ConfigurationProcessStep101", type=spinefm_SystemActionModel_ActionMoveConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionMoveConfiguration100", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
cpsTarget102: BinaryAssociation = BinaryAssociation(
    name="cpsTarget102",
    ends={
        Property(name="ConfigurationProcessStep104", type=spinefm_SystemActionModel_ActionMoveConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionMoveConfiguration103", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
contextManager105: BinaryAssociation = BinaryAssociation(
    name="contextManager105",
    ends={
        Property(name="ContextManager106", type=spinefm_SystemActionModel_ActionDeleteContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionDeleteContext", type=ContextManager, multiplicity=Multiplicity(1, 1))
    }
)
context107: BinaryAssociation = BinaryAssociation(
    name="context107",
    ends={
        Property(name="Context109", type=spinefm_SystemActionModel_ActionDeleteContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionDeleteContext108", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
fm110: BinaryAssociation = BinaryAssociation(
    name="fm110",
    ends={
        Property(name="FeatureModel111", type=spinefm_SystemActionModel_ActionOnFM, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionOnFM", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
cps112: BinaryAssociation = BinaryAssociation(
    name="cps112",
    ends={
        Property(name="ConfigurationProcessStep114", type=spinefm_SystemActionModel_ActionOnFM, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionOnFM113", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
cps74: BinaryAssociation = BinaryAssociation(
    name="cps74",
    ends={
        Property(name="ConfigurationProcessStep75", type=spinefm_SystemActionModel_ActionCreateConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionCreateConfiguration", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
compconf76: BinaryAssociation = BinaryAssociation(
    name="compconf76",
    ends={
        Property(name="CompositeConfiguration78", type=spinefm_SystemActionModel_ActionCreateConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionCreateConfiguration77", type=CompositeConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
confSource79: BinaryAssociation = BinaryAssociation(
    name="confSource79",
    ends={
        Property(name="Configuration80", type=spinefm_SystemActionModel_ActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionLink", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
confTarget81: BinaryAssociation = BinaryAssociation(
    name="confTarget81",
    ends={
        Property(name="Configuration83", type=spinefm_SystemActionModel_ActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionLink82", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
asso84: BinaryAssociation = BinaryAssociation(
    name="asso84",
    ends={
        Property(name="DEAssociation86", type=spinefm_SystemActionModel_ActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionLink85", type=DEAssociation, multiplicity=Multiplicity(1, 1))
    }
)
link87: BinaryAssociation = BinaryAssociation(
    name="link87",
    ends={
        Property(name="Link89", type=spinefm_SystemActionModel_ActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionLink88", type=Link, multiplicity=Multiplicity(1, 1))
    }
)
contextManager90: BinaryAssociation = BinaryAssociation(
    name="contextManager90",
    ends={
        Property(name="ContextManager", type=spinefm_SystemActionModel_ActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionLink91", type=ContextManager, multiplicity=Multiplicity(1, 1))
    }
)
config123: BinaryAssociation = BinaryAssociation(
    name="config123",
    ends={
        Property(name="Configuration124", type=spinefm_SystemActionModel_ActionRenameConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionRenameConfig", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
product125: BinaryAssociation = BinaryAssociation(
    name="product125",
    ends={
        Property(name="CompositeConfiguration126", type=spinefm_SystemActionModel_ActionRenameProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionRenameProduct", type=CompositeConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
product127: BinaryAssociation = BinaryAssociation(
    name="product127",
    ends={
        Property(name="CompositeConfiguration128", type=spinefm_SystemActionModel_ActionSetProductDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionSetProductDescription", type=CompositeConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
feature115: BinaryAssociation = BinaryAssociation(
    name="feature115",
    ends={
        Property(name="Feature116", type=spinefm_SystemActionModel_ActionSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionSelect", type=Feature, multiplicity=Multiplicity(1, 1))
    }
)
feature117: BinaryAssociation = BinaryAssociation(
    name="feature117",
    ends={
        Property(name="Feature118", type=spinefm_SystemActionModel_ActionDeselect, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionDeselect", type=Feature, multiplicity=Multiplicity(1, 1))
    }
)
constraint119: BinaryAssociation = BinaryAssociation(
    name="constraint119",
    ends={
        Property(name="Constraint120", type=spinefm_SystemActionModel_ActionAddCTConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionAddCTConstraint", type=Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cps121: BinaryAssociation = BinaryAssociation(
    name="cps121",
    ends={
        Property(name="ConfigurationProcessStep122", type=spinefm_SystemActionModel_ActionRenameCPS, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_SystemActionModel_ActionRenameCPS", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
step129: BinaryAssociation = BinaryAssociation(
    name="step129",
    ends={
        Property(name="HistoryModel131", type=spinefm_UserActionModel_UserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Step130", type=Step, multiplicity=Multiplicity(0, 1))
    }
)
contextManager132: BinaryAssociation = BinaryAssociation(
    name="contextManager132",
    ends={
        Property(name="ContextManager133", type=spinefm_UserActionModel_UserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_UserActionModel_UserAction", type=ContextManager, multiplicity=Multiplicity(1, 1))
    }
)
result134: BinaryAssociation = BinaryAssociation(
    name="result134",
    ends={
        Property(name="UserActionModel_spinefm_EObject", type=spinefm_UserActionModel_UserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_UserActionModel_UserAction135", type=UserActionModel_spinefm_EObject, multiplicity=Multiplicity(1, 1))
    }
)
rules144: BinaryAssociation = BinaryAssociation(
    name="rules144",
    ends={
        Property(name="Rule", type=spinefm_RFModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_RestrictionFunction", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inverse145: BinaryAssociation = BinaryAssociation(
    name="inverse145",
    ends={
        Property(name="RestrictionFunction147", type=spinefm_RFModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_RestrictionFunction146", type=RestrictionFunction, multiplicity=Multiplicity(1, 1))
    }
)
source148: BinaryAssociation = BinaryAssociation(
    name="source148",
    ends={
        Property(name="DomainElement150", type=spinefm_RFModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_RestrictionFunction149", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
launchingAction136: BinaryAssociation = BinaryAssociation(
    name="launchingAction136",
    ends={
        Property(name="ActionModel", type=spinefm_HistoryModel_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="UserActionModel", type=UserActionModel_UserAction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
launchedActions137: BinaryAssociation = BinaryAssociation(
    name="launchedActions137",
    ends={
        Property(name="ActionModel138", type=spinefm_HistoryModel_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="SystemActionModel", type=SystemActionModel_SystemAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps139: BinaryAssociation = BinaryAssociation(
    name="steps139",
    ends={
        Property(name="Step140", type=spinefm_HistoryModel_Past, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_HistoryModel_Past", type=Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deletedContext141: BinaryAssociation = BinaryAssociation(
    name="deletedContext141",
    ends={
        Property(name="LocalContext143", type=spinefm_HistoryModel_Past, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_HistoryModel_Past142", type=LocalContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target151: BinaryAssociation = BinaryAssociation(
    name="target151",
    ends={
        Property(name="DomainElement153", type=spinefm_RFModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_RestrictionFunction152", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
selectedFeatures154: BinaryAssociation = BinaryAssociation(
    name="selectedFeatures154",
    ends={
        Property(name="Feature155", type=spinefm_RFModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_ConfigurationState", type=Feature, multiplicity=Multiplicity(1, 9999))
    }
)
deselectedFeatures156: BinaryAssociation = BinaryAssociation(
    name="deselectedFeatures156",
    ends={
        Property(name="Feature158", type=spinefm_RFModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_ConfigurationState157", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
fm159: BinaryAssociation = BinaryAssociation(
    name="fm159",
    ends={
        Property(name="FeatureModel161", type=spinefm_RFModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_ConfigurationState160", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
action162: BinaryAssociation = BinaryAssociation(
    name="action162",
    ends={
        Property(name="SystemActionModel_ActionOnFM163", type=spinefm_RFModel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_Rule", type=SystemActionModel_ActionOnFM, multiplicity=Multiplicity(1, 1))
    }
)
state164: BinaryAssociation = BinaryAssociation(
    name="state164",
    ends={
        Property(name="ConfigurationState166", type=spinefm_RFModel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_RFModel_Rule165", type=ConfigurationState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_spinefm_ProcessModel_LocalContext_Context = Generalization(general=Context, specific=spinefm_ProcessModel_LocalContext)
gen_spinefm_ProcessModel_GlobalContext_Context = Generalization(general=Context, specific=spinefm_ProcessModel_GlobalContext)
gen_spinefm_SystemActionModel_ActionMoveConfiguration_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionMoveConfiguration)
gen_spinefm_SystemActionModel_ActionDeleteContext_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionDeleteContext)
gen_spinefm_SystemActionModel_ActionOnFM_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionOnFM)
gen_spinefm_SystemActionModel_ActionCreateConfiguration_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionCreateConfiguration)
gen_spinefm_SystemActionModel_ActionLink_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionLink)
gen_spinefm_SystemActionModel_ActionCreateContext_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionCreateContext)
gen_spinefm_SystemActionModel_ActionRenameConfig_ActionAbstractRename = Generalization(general=ActionAbstractRename, specific=spinefm_SystemActionModel_ActionRenameConfig)
gen_spinefm_SystemActionModel_ActionRenameProduct_ActionAbstractRename = Generalization(general=ActionAbstractRename, specific=spinefm_SystemActionModel_ActionRenameProduct)
gen_spinefm_SystemActionModel_ActionSetProductDescription_ActionAbstractRename = Generalization(general=ActionAbstractRename, specific=spinefm_SystemActionModel_ActionSetProductDescription)
gen_spinefm_UserActionModel_UserSelect_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserSelect)
gen_spinefm_SystemActionModel_ActionSelect_ActionOnFM = Generalization(general=ActionOnFM, specific=spinefm_SystemActionModel_ActionSelect)
gen_spinefm_SystemActionModel_ActionDeselect_ActionOnFM = Generalization(general=ActionOnFM, specific=spinefm_SystemActionModel_ActionDeselect)
gen_spinefm_SystemActionModel_ActionAddCTConstraint_ActionOnFM = Generalization(general=ActionOnFM, specific=spinefm_SystemActionModel_ActionAddCTConstraint)
gen_spinefm_SystemActionModel_ActionAbstractRename_SystemAction = Generalization(general=SystemAction, specific=spinefm_SystemActionModel_ActionAbstractRename)
gen_spinefm_SystemActionModel_ActionRenameCPS_ActionAbstractRename = Generalization(general=ActionAbstractRename, specific=spinefm_SystemActionModel_ActionRenameCPS)
gen_spinefm_UserActionModel_UserLinkConfiguration_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserLinkConfiguration)
gen_spinefm_UserActionModel_UserInit_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserInit)
gen_spinefm_UserActionModel_UserGenerate_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserGenerate)
gen_spinefm_UserActionModel_UserSavePast_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserSavePast)
gen_spinefm_UserActionModel_UserRenameElement_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserRenameElement)
gen_spinefm_UserActionModel_UserCloneContext_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserCloneContext)
gen_spinefm_UserActionModel_UserCreateContext_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserCreateContext)
gen_spinefm_UserActionModel_UserDeselect_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserDeselect)
gen_spinefm_UserActionModel_UserPropagate_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserPropagate)
gen_spinefm_UserActionModel_UserValidConfiguration_UserAction = Generalization(general=UserAction, specific=spinefm_UserActionModel_UserValidConfiguration)

# Domain Model
domain_model = DomainModel(
    name="spinefm",
    types={spinefm_FMModel_FeatureModel, Feature, Constraint, spinefm_FMModel_Feature, spinefm_MSPLModel_MultipleSoftwareProductLine, DomainElement, DEAssociation, spinefm_MSPLModel_DEAssociation, Group, spinefm_FMModel_Group, spinefm_FMModel_Constraint, spinefm_MSPLModel_DomainElement, FeatureModel, spinefm_ConfigurationModel_Configuration, RestrictionFunction, DEAssociationEnd, spinefm_MSPLModel_MultiplicityElement, spinefm_MSPLModel_DEAssociationEnd, MultiplicityElement, spinefm_ConfigurationModel_CompositeConfiguration, MultipleSoftwareProductLine, spinefm_ProcessModel_ConfigurationProcessStep, ConfigurationProcessStep, Link, ConfigurationState, spinefm_ConfigurationModel_Link, Configuration, SystemActionModel_ActionOnFM, spinefm_ProcessModel_Context, Context, spinefm_ProcessModel_LocalContext, spinefm_ProcessModel_ContextManager, spinefm_ProcessModel_GlobalContext, CompositeConfiguration, spinefm_SystemActionModel_SystemAction, Step, GlobalContext, LocalContext, Past, spinefm_ProcessModel_DeletedContextInformations, spinefm_SystemActionModel_ActionMoveConfiguration, spinefm_SystemActionModel_ActionDeleteContext, spinefm_SystemActionModel_ActionOnFM, spinefm_SystemActionModel_ActionCreateConfiguration, SystemAction, spinefm_SystemActionModel_ActionLink, ContextManager, spinefm_SystemActionModel_ActionCreateContext, spinefm_SystemActionModel_ActionRenameConfig, spinefm_SystemActionModel_ActionRenameProduct, spinefm_SystemActionModel_ActionSetProductDescription, spinefm_UserActionModel_UserSelect, UserAction, spinefm_UserActionModel_UserAction, spinefm_SystemActionModel_ActionSelect, ActionOnFM, spinefm_SystemActionModel_ActionDeselect, spinefm_SystemActionModel_ActionAddCTConstraint, spinefm_SystemActionModel_ActionAbstractRename, spinefm_SystemActionModel_ActionRenameCPS, ActionAbstractRename, spinefm_UserActionModel_UserLinkConfiguration, spinefm_UserActionModel_UserInit, spinefm_UserActionModel_UserGenerate, spinefm_UserActionModel_UserSavePast, spinefm_UserActionModel_UserRenameElement, spinefm_UserActionModel_UserCloneContext, spinefm_HistoryModel_Step, UserActionModel_spinefm_EObject, spinefm_UserActionModel_UserCreateContext, spinefm_UserActionModel_UserDeselect, spinefm_UserActionModel_UserPropagate, spinefm_UserActionModel_UserValidConfiguration, spinefm_RFModel_RestrictionFunction, Rule, UserActionModel_UserAction, SystemActionModel_SystemAction, spinefm_HistoryModel_Past, spinefm_RFModel_ConfigurationState, spinefm_RFModel_Rule, GroupState, ActionMode, CPSStatus},
    associations={root0, constraints1, domainElements6, associations7, children3, features4, MultiplicityElement16, refers_on18, belongs_to20, restrictionFunction9, extremity10, LinkMultiplicity12, apply_on13, target37, subConfigurations40, links42, mspl45, CPSRef23, belongs_to24, state25, domainElement27, clonedCPS30, source33, relatedAssociation34, configuration51, state53, actionsDone56, domainElement47, context49, configuration60, configurations61, CPS58, step73, mspl63, globalContext65, localContexts67, past69, replacedBy71, contextManager92, context94, configuration97, cpsSource99, cpsTarget102, contextManager105, context107, fm110, cps112, cps74, compconf76, confSource79, confTarget81, asso84, link87, contextManager90, config123, product125, product127, feature115, feature117, constraint119, cps121, step129, contextManager132, result134, rules144, inverse145, source148, launchingAction136, launchedActions137, steps139, deletedContext141, target151, selectedFeatures154, deselectedFeatures156, fm159, action162, state164},
    generalizations={gen_spinefm_ProcessModel_LocalContext_Context, gen_spinefm_ProcessModel_GlobalContext_Context, gen_spinefm_SystemActionModel_ActionMoveConfiguration_SystemAction, gen_spinefm_SystemActionModel_ActionDeleteContext_SystemAction, gen_spinefm_SystemActionModel_ActionOnFM_SystemAction, gen_spinefm_SystemActionModel_ActionCreateConfiguration_SystemAction, gen_spinefm_SystemActionModel_ActionLink_SystemAction, gen_spinefm_SystemActionModel_ActionCreateContext_SystemAction, gen_spinefm_SystemActionModel_ActionRenameConfig_ActionAbstractRename, gen_spinefm_SystemActionModel_ActionRenameProduct_ActionAbstractRename, gen_spinefm_SystemActionModel_ActionSetProductDescription_ActionAbstractRename, gen_spinefm_UserActionModel_UserSelect_UserAction, gen_spinefm_SystemActionModel_ActionSelect_ActionOnFM, gen_spinefm_SystemActionModel_ActionDeselect_ActionOnFM, gen_spinefm_SystemActionModel_ActionAddCTConstraint_ActionOnFM, gen_spinefm_SystemActionModel_ActionAbstractRename_SystemAction, gen_spinefm_SystemActionModel_ActionRenameCPS_ActionAbstractRename, gen_spinefm_UserActionModel_UserLinkConfiguration_UserAction, gen_spinefm_UserActionModel_UserInit_UserAction, gen_spinefm_UserActionModel_UserGenerate_UserAction, gen_spinefm_UserActionModel_UserSavePast_UserAction, gen_spinefm_UserActionModel_UserRenameElement_UserAction, gen_spinefm_UserActionModel_UserCloneContext_UserAction, gen_spinefm_UserActionModel_UserCreateContext_UserAction, gen_spinefm_UserActionModel_UserDeselect_UserAction, gen_spinefm_UserActionModel_UserPropagate_UserAction, gen_spinefm_UserActionModel_UserValidConfiguration_UserAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)