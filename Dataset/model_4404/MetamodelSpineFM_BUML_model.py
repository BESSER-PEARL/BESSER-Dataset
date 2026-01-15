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

# Classes
spinefm_FMModel_Feature = Class(name="spinefm::FMModel::Feature")
spinefm_FMModel_FeatureModel = Class(name="spinefm::FMModel::FeatureModel")
Feature = Class(name="Feature")
Constraint = Class(name="Constraint")
Group = Class(name="Group")
spinefm_FMModel_Group = Class(name="spinefm::FMModel::Group")
spinefm_FMModel_Constraint = Class(name="spinefm::FMModel::Constraint")
spinefm_MSPLModel_MultipleSoftwareProductLine = Class(name="spinefm::MSPLModel::MultipleSoftwareProductLine")
DomainElement = Class(name="DomainElement")
DEAssociation = Class(name="DEAssociation")
spinefm_MSPLModel_DEAssociation = Class(name="spinefm::MSPLModel::DEAssociation")
RestrictionFunction = Class(name="RestrictionFunction")
DEAssociationEnd = Class(name="DEAssociationEnd")
spinefm_MSPLModel_MultiplicityElement = Class(name="spinefm::MSPLModel::MultiplicityElement")
spinefm_MSPLModel_DEAssociationEnd = Class(name="spinefm::MSPLModel::DEAssociationEnd")
MultiplicityElement = Class(name="MultiplicityElement")
spinefm_MSPLModel_DomainElement = Class(name="spinefm::MSPLModel::DomainElement")
FeatureModel = Class(name="FeatureModel")
spinefm_ConfigurationModel_Configuration = Class(name="spinefm::ConfigurationModel::Configuration")
ConfigurationProcessStep = Class(name="ConfigurationProcessStep")
Link = Class(name="Link")
ConfigurationState = Class(name="ConfigurationState")
spinefm_ConfigurationModel_Link = Class(name="spinefm::ConfigurationModel::Link")
Configuration = Class(name="Configuration")
spinefm_ConfigurationModel_CompositeConfiguration = Class(name="spinefm::ConfigurationModel::CompositeConfiguration")
spinefm_ProcessModel_LocalContext = Class(name="spinefm::ProcessModel::LocalContext")
spinefm_ProcessModel_ConfigurationProcessStep = Class(name="spinefm::ProcessModel::ConfigurationProcessStep")
Action = Class(name="Action")
Context = Class(name="Context")
spinefm_ProcessModel_Context = Class(name="spinefm::ProcessModel::Context", is_abstract=True)
spinefm_ProcessModel_GlobalContext = Class(name="spinefm::ProcessModel::GlobalContext")
CompositeConfiguration = Class(name="CompositeConfiguration")
spinefm_ActionModel_ConfigurationState = Class(name="spinefm::ActionModel::ConfigurationState")
spinefm_ProcessModel_ContextManager = Class(name="spinefm::ProcessModel::ContextManager")
MultipleSoftwareProductLine = Class(name="MultipleSoftwareProductLine")
GlobalContext = Class(name="GlobalContext")
LocalContext = Class(name="LocalContext")
spinefm_ProcessModel_DeletedContextInformations = Class(name="spinefm::ProcessModel::DeletedContextInformations")
spinefm_ActionModel_RestrictionFunction = Class(name="spinefm::ActionModel::RestrictionFunction")
Rule = Class(name="Rule")
spinefm_ActionModel_Rule = Class(name="spinefm::ActionModel::Rule")
spinefm_ActionModel_Action = Class(name="spinefm::ActionModel::Action", is_abstract=True)
spinefm_ActionModel_ActionSelect = Class(name="spinefm::ActionModel::ActionSelect")
spinefm_ActionModel_ActionDeselect = Class(name="spinefm::ActionModel::ActionDeselect")
spinefm_ActionModel_ActionAddCTConstraint = Class(name="spinefm::ActionModel::ActionAddCTConstraint")

# spinefm_FMModel_Feature class attributes and methods
spinefm_FMModel_Feature_id: Property = Property(name="id", type=StringType)
spinefm_FMModel_Feature_name: Property = Property(name="name", type=StringType)
spinefm_FMModel_Feature_m_getAllChildrenFeatures: Method = Method(name="getAllChildrenFeatures", parameters={}, type=StringType)
spinefm_FMModel_Feature.attributes={spinefm_FMModel_Feature_id, spinefm_FMModel_Feature_name}
spinefm_FMModel_Feature.methods={spinefm_FMModel_Feature_m_getAllChildrenFeatures}

# spinefm_FMModel_FeatureModel class attributes and methods
spinefm_FMModel_FeatureModel_id: Property = Property(name="id", type=StringType)
spinefm_FMModel_FeatureModel_name: Property = Property(name="name", type=StringType)
spinefm_FMModel_FeatureModel_m_getStateFT: Method = Method(name="getStateFT", parameters={Parameter(name='feature')}, type=StringType)
spinefm_FMModel_FeatureModel_m_getFeatureFromName: Method = Method(name="getFeatureFromName", parameters={Parameter(name='name')}, type=StringType)
spinefm_FMModel_FeatureModel_m_addFeature: Method = Method(name="addFeature", parameters={Parameter(name='feature'), Parameter(name='name'), Parameter(name='state')})
spinefm_FMModel_FeatureModel.attributes={spinefm_FMModel_FeatureModel_id, spinefm_FMModel_FeatureModel_name}
spinefm_FMModel_FeatureModel.methods={spinefm_FMModel_FeatureModel_m_getFeatureFromName, spinefm_FMModel_FeatureModel_m_addFeature, spinefm_FMModel_FeatureModel_m_getStateFT}

# Feature class attributes and methods

# Constraint class attributes and methods

# Group class attributes and methods

# spinefm_FMModel_Group class attributes and methods
spinefm_FMModel_Group_state: Property = Property(name="state", type=StringType)
spinefm_FMModel_Group_m_getAllChildren: Method = Method(name="getAllChildren", parameters={}, type=StringType)
spinefm_FMModel_Group.attributes={spinefm_FMModel_Group_state}
spinefm_FMModel_Group.methods={spinefm_FMModel_Group_m_getAllChildren}

# spinefm_FMModel_Constraint class attributes and methods
spinefm_FMModel_Constraint_Rule: Property = Property(name="Rule", type=StringType)
spinefm_FMModel_Constraint.attributes={spinefm_FMModel_Constraint_Rule}

# spinefm_MSPLModel_MultipleSoftwareProductLine class attributes and methods
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getDomainElementByName: Method = Method(name="getDomainElementByName", parameters={Parameter(name='name')}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getValidAssociationsForSourceAndTarget: Method = Method(name="getValidAssociationsForSourceAndTarget", parameters={Parameter(name='target'), Parameter(name='source')}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine.methods={spinefm_MSPLModel_MultipleSoftwareProductLine_m_getDomainElementByName, spinefm_MSPLModel_MultipleSoftwareProductLine_m_getValidAssociationsForSourceAndTarget}

# DomainElement class attributes and methods

# DEAssociation class attributes and methods

# spinefm_MSPLModel_DEAssociation class attributes and methods
spinefm_MSPLModel_DEAssociation_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DEAssociation_m_computeActionsToDo: Method = Method(name="computeActionsToDo", parameters={Parameter(name='CPSSource'), Parameter(name='CPSTarget')}, type=StringType)
spinefm_MSPLModel_DEAssociation_m_createAndAssociateInverseAssociation: Method = Method(name="createAndAssociateInverseAssociation", parameters={}, type=StringType)
spinefm_MSPLModel_DEAssociation.attributes={spinefm_MSPLModel_DEAssociation_id}
spinefm_MSPLModel_DEAssociation.methods={spinefm_MSPLModel_DEAssociation_m_createAndAssociateInverseAssociation, spinefm_MSPLModel_DEAssociation_m_computeActionsToDo}

# RestrictionFunction class attributes and methods

# DEAssociationEnd class attributes and methods

# spinefm_MSPLModel_MultiplicityElement class attributes and methods
spinefm_MSPLModel_MultiplicityElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
spinefm_MSPLModel_MultiplicityElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
spinefm_MSPLModel_MultiplicityElement_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_MultiplicityElement_m_respectBoundaries: Method = Method(name="respectBoundaries", parameters={Parameter(name='value')}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement_m_isExactlyOne: Method = Method(name="isExactlyOne", parameters={}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement_m_isLowerThanUpperBound: Method = Method(name="isLowerThanUpperBound", parameters={Parameter(name='value')}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement.attributes={spinefm_MSPLModel_MultiplicityElement_upperBound, spinefm_MSPLModel_MultiplicityElement_lowerBound, spinefm_MSPLModel_MultiplicityElement_id}
spinefm_MSPLModel_MultiplicityElement.methods={spinefm_MSPLModel_MultiplicityElement_m_isExactlyOne, spinefm_MSPLModel_MultiplicityElement_m_isLowerThanUpperBound, spinefm_MSPLModel_MultiplicityElement_m_respectBoundaries}

# spinefm_MSPLModel_DEAssociationEnd class attributes and methods
spinefm_MSPLModel_DEAssociationEnd_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DEAssociationEnd.attributes={spinefm_MSPLModel_DEAssociationEnd_id}

# MultiplicityElement class attributes and methods

# spinefm_MSPLModel_DomainElement class attributes and methods
spinefm_MSPLModel_DomainElement_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DomainElement_m_getSourcedAssociations: Method = Method(name="getSourcedAssociations", parameters={}, type=StringType)
spinefm_MSPLModel_DomainElement.attributes={spinefm_MSPLModel_DomainElement_id}
spinefm_MSPLModel_DomainElement.methods={spinefm_MSPLModel_DomainElement_m_getSourcedAssociations}

# FeatureModel class attributes and methods

# spinefm_ConfigurationModel_Configuration class attributes and methods
spinefm_ConfigurationModel_Configuration_id: Property = Property(name="id", type=StringType)
spinefm_ConfigurationModel_Configuration_description: Property = Property(name="description", type=StringType)
spinefm_ConfigurationModel_Configuration_m_getFeatureModel: Method = Method(name="getFeatureModel", parameters={}, type=StringType)
spinefm_ConfigurationModel_Configuration_m_getLinkedConfigurationsOfDomainElement: Method = Method(name="getLinkedConfigurationsOfDomainElement", parameters={Parameter(name='de')}, type=StringType)
spinefm_ConfigurationModel_Configuration_m_canBeLinked: Method = Method(name="canBeLinked", parameters={Parameter(name='association')}, type=BooleanType)
spinefm_ConfigurationModel_Configuration_m_isCompletlyLinked: Method = Method(name="isCompletlyLinked", parameters={}, type=BooleanType)
spinefm_ConfigurationModel_Configuration.attributes={spinefm_ConfigurationModel_Configuration_description, spinefm_ConfigurationModel_Configuration_id}
spinefm_ConfigurationModel_Configuration.methods={spinefm_ConfigurationModel_Configuration_m_getLinkedConfigurationsOfDomainElement, spinefm_ConfigurationModel_Configuration_m_canBeLinked, spinefm_ConfigurationModel_Configuration_m_isCompletlyLinked, spinefm_ConfigurationModel_Configuration_m_getFeatureModel}

# ConfigurationProcessStep class attributes and methods

# Link class attributes and methods

# ConfigurationState class attributes and methods

# spinefm_ConfigurationModel_Link class attributes and methods
spinefm_ConfigurationModel_Link_id: Property = Property(name="id", type=StringType)
spinefm_ConfigurationModel_Link_m_getAssociatedConfiguration: Method = Method(name="getAssociatedConfiguration", parameters={Parameter(name='conf')}, type=StringType)
spinefm_ConfigurationModel_Link.attributes={spinefm_ConfigurationModel_Link_id}
spinefm_ConfigurationModel_Link.methods={spinefm_ConfigurationModel_Link_m_getAssociatedConfiguration}

# Configuration class attributes and methods

# spinefm_ConfigurationModel_CompositeConfiguration class attributes and methods
spinefm_ConfigurationModel_CompositeConfiguration_name: Property = Property(name="name", type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_m_isValid: Method = Method(name="isValid", parameters={}, type=BooleanType)
spinefm_ConfigurationModel_CompositeConfiguration_m_addConfiguration: Method = Method(name="addConfiguration", parameters={Parameter(name='conf')})
spinefm_ConfigurationModel_CompositeConfiguration_m_getConfigurationByName: Method = Method(name="getConfigurationByName", parameters={Parameter(name='confName')}, type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_m_createConfigurationLink: Method = Method(name="createConfigurationLink", parameters={Parameter(name='confTarget'), Parameter(name='asso'), Parameter(name='confSource')})
spinefm_ConfigurationModel_CompositeConfiguration_m_getCompatibleConfigurations: Method = Method(name="getCompatibleConfigurations", parameters={Parameter(name='asso'), Parameter(name='confSource')}, type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration.attributes={spinefm_ConfigurationModel_CompositeConfiguration_name}
spinefm_ConfigurationModel_CompositeConfiguration.methods={spinefm_ConfigurationModel_CompositeConfiguration_m_addConfiguration, spinefm_ConfigurationModel_CompositeConfiguration_m_getConfigurationByName, spinefm_ConfigurationModel_CompositeConfiguration_m_isValid, spinefm_ConfigurationModel_CompositeConfiguration_m_createConfigurationLink, spinefm_ConfigurationModel_CompositeConfiguration_m_getCompatibleConfigurations}

# spinefm_ProcessModel_LocalContext class attributes and methods

# spinefm_ProcessModel_ConfigurationProcessStep class attributes and methods
spinefm_ProcessModel_ConfigurationProcessStep_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_description: Property = Property(name="description", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_userConfig: Property = Property(name="userConfig", type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_isComplete: Method = Method(name="isComplete", parameters={}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_getState: Method = Method(name="getState", parameters={}, type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_m_addActionToDo: Method = Method(name="addActionToDo", parameters={Parameter(name='a')})
spinefm_ProcessModel_ConfigurationProcessStep_m_alreadyHaveAction: Method = Method(name="alreadyHaveAction", parameters={Parameter(name='a')}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_getConfName: Method = Method(name="getConfName", parameters={}, type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_m_setFMA: Method = Method(name="setFMA", parameters={Parameter(name='fma')})
spinefm_ProcessModel_ConfigurationProcessStep_m_apply: Method = Method(name="apply", parameters={}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_mergeWithExternalCPS: Method = Method(name="mergeWithExternalCPS", parameters={Parameter(name='cps')})
spinefm_ProcessModel_ConfigurationProcessStep_m_isCompatibleWithConfiguration: Method = Method(name="isCompatibleWithConfiguration", parameters={Parameter(name='conf')}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep.attributes={spinefm_ProcessModel_ConfigurationProcessStep_description, spinefm_ProcessModel_ConfigurationProcessStep_userConfig, spinefm_ProcessModel_ConfigurationProcessStep_id}
spinefm_ProcessModel_ConfigurationProcessStep.methods={spinefm_ProcessModel_ConfigurationProcessStep_m_setFMA, spinefm_ProcessModel_ConfigurationProcessStep_m_mergeWithExternalCPS, spinefm_ProcessModel_ConfigurationProcessStep_m_getState, spinefm_ProcessModel_ConfigurationProcessStep_m_alreadyHaveAction, spinefm_ProcessModel_ConfigurationProcessStep_m_apply, spinefm_ProcessModel_ConfigurationProcessStep_m_isComplete, spinefm_ProcessModel_ConfigurationProcessStep_m_addActionToDo, spinefm_ProcessModel_ConfigurationProcessStep_m_isCompatibleWithConfiguration, spinefm_ProcessModel_ConfigurationProcessStep_m_getConfName}

# Action class attributes and methods

# Context class attributes and methods

# spinefm_ProcessModel_Context class attributes and methods
spinefm_ProcessModel_Context_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_Context_m_addCPS: Method = Method(name="addCPS", parameters={Parameter(name='cps')})
spinefm_ProcessModel_Context_m_getCPSOfDE: Method = Method(name="getCPSOfDE", parameters={Parameter(name='de')}, type=StringType)
spinefm_ProcessModel_Context_m_mergeExternalCPS: Method = Method(name="mergeExternalCPS", parameters={Parameter(name='externalCPS')})
spinefm_ProcessModel_Context.attributes={spinefm_ProcessModel_Context_id}
spinefm_ProcessModel_Context.methods={spinefm_ProcessModel_Context_m_getCPSOfDE, spinefm_ProcessModel_Context_m_mergeExternalCPS, spinefm_ProcessModel_Context_m_addCPS}

# spinefm_ProcessModel_GlobalContext class attributes and methods

# CompositeConfiguration class attributes and methods

# spinefm_ActionModel_ConfigurationState class attributes and methods
spinefm_ActionModel_ConfigurationState_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_ConfigurationState_m_isIncludedIn: Method = Method(name="isIncludedIn", parameters={Parameter(name='otherState')}, type=BooleanType)
spinefm_ActionModel_ConfigurationState.attributes={spinefm_ActionModel_ConfigurationState_id}
spinefm_ActionModel_ConfigurationState.methods={spinefm_ActionModel_ConfigurationState_m_isIncludedIn}

# spinefm_ProcessModel_ContextManager class attributes and methods
spinefm_ProcessModel_ContextManager_m_propagate: Method = Method(name="propagate", parameters={Parameter(name='CPS'), Parameter(name='context')})
spinefm_ProcessModel_ContextManager_m_setFMAdapter: Method = Method(name="setFMAdapter", parameters={Parameter(name='fma')})
spinefm_ProcessModel_ContextManager_m_init: Method = Method(name="init", parameters={})
spinefm_ProcessModel_ContextManager_m_createNewContext: Method = Method(name="createNewContext", parameters={}, type=StringType)
spinefm_ProcessModel_ContextManager_m_getContextFromId: Method = Method(name="getContextFromId", parameters={Parameter(name='id')}, type=StringType)
spinefm_ProcessModel_ContextManager_m_linkConfigurationsAndManageContexts: Method = Method(name="linkConfigurationsAndManageContexts", parameters={Parameter(name='association'), Parameter(name='confTarget'), Parameter(name='confSource')}, type=StringType)
spinefm_ProcessModel_ContextManager.methods={spinefm_ProcessModel_ContextManager_m_linkConfigurationsAndManageContexts, spinefm_ProcessModel_ContextManager_m_setFMAdapter, spinefm_ProcessModel_ContextManager_m_createNewContext, spinefm_ProcessModel_ContextManager_m_getContextFromId, spinefm_ProcessModel_ContextManager_m_init, spinefm_ProcessModel_ContextManager_m_propagate}

# MultipleSoftwareProductLine class attributes and methods

# GlobalContext class attributes and methods

# LocalContext class attributes and methods

# spinefm_ProcessModel_DeletedContextInformations class attributes and methods
spinefm_ProcessModel_DeletedContextInformations_deletedContext: Property = Property(name="deletedContext", type=StringType)
spinefm_ProcessModel_DeletedContextInformations.attributes={spinefm_ProcessModel_DeletedContextInformations_deletedContext}

# spinefm_ActionModel_RestrictionFunction class attributes and methods
spinefm_ActionModel_RestrictionFunction_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_RestrictionFunction_m_createAndAssociateInverseRestFunc: Method = Method(name="createAndAssociateInverseRestFunc", parameters={}, type=StringType)
spinefm_ActionModel_RestrictionFunction.attributes={spinefm_ActionModel_RestrictionFunction_id}
spinefm_ActionModel_RestrictionFunction.methods={spinefm_ActionModel_RestrictionFunction_m_createAndAssociateInverseRestFunc}

# Rule class attributes and methods

# spinefm_ActionModel_Rule class attributes and methods
spinefm_ActionModel_Rule_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_Rule_m_createInverseRule: Method = Method(name="createInverseRule", parameters={}, type=StringType)
spinefm_ActionModel_Rule.attributes={spinefm_ActionModel_Rule_id}
spinefm_ActionModel_Rule.methods={spinefm_ActionModel_Rule_m_createInverseRule}

# spinefm_ActionModel_Action class attributes and methods
spinefm_ActionModel_Action_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_Action_m_applyAction: Method = Method(name="applyAction", parameters={Parameter(name='fma'), Parameter(name='confName')})
spinefm_ActionModel_Action_m_isSameObject: Method = Method(name="isSameObject", parameters={Parameter(name='o')}, type=BooleanType)
spinefm_ActionModel_Action.attributes={spinefm_ActionModel_Action_id}
spinefm_ActionModel_Action.methods={spinefm_ActionModel_Action_m_isSameObject, spinefm_ActionModel_Action_m_applyAction}

# spinefm_ActionModel_ActionSelect class attributes and methods

# spinefm_ActionModel_ActionDeselect class attributes and methods

# spinefm_ActionModel_ActionAddCTConstraint class attributes and methods

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
inverse15: BinaryAssociation = BinaryAssociation(
    name="inverse15",
    ends={
        Property(name="DEAssociation17", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation16", type=DEAssociation, multiplicity=Multiplicity(1, 1))
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
restrictionFunction9: BinaryAssociation = BinaryAssociation(
    name="restrictionFunction9",
    ends={
        Property(name="RestrictionFunction", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation", type=RestrictionFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="DEAssociationEnd", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation11", type=DEAssociationEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="DEAssociationEnd14", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation13", type=DEAssociationEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LinkMultiplicity18: BinaryAssociation = BinaryAssociation(
    name="LinkMultiplicity18",
    ends={
        Property(name="MultiplicityElement", type=spinefm_MSPLModel_DEAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociationEnd", type=MultiplicityElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
apply_on19: BinaryAssociation = BinaryAssociation(
    name="apply_on19",
    ends={
        Property(name="DomainElement21", type=spinefm_MSPLModel_DEAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociationEnd20", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
MultiplicityElement22: BinaryAssociation = BinaryAssociation(
    name="MultiplicityElement22",
    ends={
        Property(name="MultiplicityElement23", type=spinefm_MSPLModel_DomainElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DomainElement", type=MultiplicityElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refers_on24: BinaryAssociation = BinaryAssociation(
    name="refers_on24",
    ends={
        Property(name="FeatureModel", type=spinefm_MSPLModel_DomainElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DomainElement25", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
belongs_to26: BinaryAssociation = BinaryAssociation(
    name="belongs_to26",
    ends={
        Property(name="DEAssociation28", type=spinefm_MSPLModel_DomainElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DomainElement27", type=DEAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
CPS29: BinaryAssociation = BinaryAssociation(
    name="CPS29",
    ends={
        Property(name="ProcessModel", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="ConfigurationProcessStep", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
    }
)
belongs_to30: BinaryAssociation = BinaryAssociation(
    name="belongs_to30",
    ends={
        Property(name="Link", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration", type=Link, multiplicity=Multiplicity(0, 9999))
    }
)
state31: BinaryAssociation = BinaryAssociation(
    name="state31",
    ends={
        Property(name="ConfigurationState", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration32", type=ConfigurationState, multiplicity=Multiplicity(1, 1), is_composite=True)
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
actionsDone45: BinaryAssociation = BinaryAssociation(
    name="actionsDone45",
    ends={
        Property(name="Action", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep", type=Action, multiplicity=Multiplicity(0, 9999))
    }
)
domainElement46: BinaryAssociation = BinaryAssociation(
    name="domainElement46",
    ends={
        Property(name="DomainElement48", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep47", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
actionsToDo49: BinaryAssociation = BinaryAssociation(
    name="actionsToDo49",
    ends={
        Property(name="Action51", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep50", type=Action, multiplicity=Multiplicity(0, 9999))
    }
)
context52: BinaryAssociation = BinaryAssociation(
    name="context52",
    ends={
        Property(name="Context", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep53", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
configuration54: BinaryAssociation = BinaryAssociation(
    name="configuration54",
    ends={
        Property(name="ConfigurationModel", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="Configuration55", type=Configuration, multiplicity=Multiplicity(0, 1))
    }
)
CPS56: BinaryAssociation = BinaryAssociation(
    name="CPS56",
    ends={
        Property(name="ConfigurationProcessStep57", type=spinefm_ProcessModel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_Context", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
configuration58: BinaryAssociation = BinaryAssociation(
    name="configuration58",
    ends={
        Property(name="CompositeConfiguration", type=spinefm_ProcessModel_GlobalContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_GlobalContext", type=CompositeConfiguration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configurations59: BinaryAssociation = BinaryAssociation(
    name="configurations59",
    ends={
        Property(name="Configuration60", type=spinefm_ProcessModel_LocalContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_LocalContext", type=Configuration, multiplicity=Multiplicity(1, 9999))
    }
)
mspl61: BinaryAssociation = BinaryAssociation(
    name="mspl61",
    ends={
        Property(name="MultipleSoftwareProductLine", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager", type=MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1))
    }
)
globalContext62: BinaryAssociation = BinaryAssociation(
    name="globalContext62",
    ends={
        Property(name="GlobalContext", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager63", type=GlobalContext, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localContexts64: BinaryAssociation = BinaryAssociation(
    name="localContexts64",
    ends={
        Property(name="LocalContext", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager65", type=LocalContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacedBy66: BinaryAssociation = BinaryAssociation(
    name="replacedBy66",
    ends={
        Property(name="Context67", type=spinefm_ProcessModel_DeletedContextInformations, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_DeletedContextInformations", type=Context, multiplicity=Multiplicity(0, 1))
    }
)
rules68: BinaryAssociation = BinaryAssociation(
    name="rules68",
    ends={
        Property(name="Rule", type=spinefm_ActionModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_RestrictionFunction", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inverse69: BinaryAssociation = BinaryAssociation(
    name="inverse69",
    ends={
        Property(name="RestrictionFunction71", type=spinefm_ActionModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_RestrictionFunction70", type=RestrictionFunction, multiplicity=Multiplicity(1, 1))
    }
)
selectedFeatures72: BinaryAssociation = BinaryAssociation(
    name="selectedFeatures72",
    ends={
        Property(name="Feature73", type=spinefm_ActionModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ConfigurationState", type=Feature, multiplicity=Multiplicity(1, 9999))
    }
)
deselectedFeatures74: BinaryAssociation = BinaryAssociation(
    name="deselectedFeatures74",
    ends={
        Property(name="Feature76", type=spinefm_ActionModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ConfigurationState75", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
fm77: BinaryAssociation = BinaryAssociation(
    name="fm77",
    ends={
        Property(name="FeatureModel79", type=spinefm_ActionModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ConfigurationState78", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
actions80: BinaryAssociation = BinaryAssociation(
    name="actions80",
    ends={
        Property(name="Action81", type=spinefm_ActionModel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Rule", type=Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state82: BinaryAssociation = BinaryAssociation(
    name="state82",
    ends={
        Property(name="ConfigurationState84", type=spinefm_ActionModel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Rule83", type=ConfigurationState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature85: BinaryAssociation = BinaryAssociation(
    name="feature85",
    ends={
        Property(name="Feature86", type=spinefm_ActionModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Action", type=Feature, multiplicity=Multiplicity(0, 1))
    }
)
fm87: BinaryAssociation = BinaryAssociation(
    name="fm87",
    ends={
        Property(name="FeatureModel89", type=spinefm_ActionModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Action88", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
constraint90: BinaryAssociation = BinaryAssociation(
    name="constraint90",
    ends={
        Property(name="Constraint91", type=spinefm_ActionModel_ActionAddCTConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ActionAddCTConstraint", type=Constraint, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_spinefm_ProcessModel_LocalContext_Context = Generalization(general=Context, specific=spinefm_ProcessModel_LocalContext)
gen_spinefm_ProcessModel_GlobalContext_Context = Generalization(general=Context, specific=spinefm_ProcessModel_GlobalContext)
gen_spinefm_ActionModel_ActionSelect_Action = Generalization(general=Action, specific=spinefm_ActionModel_ActionSelect)
gen_spinefm_ActionModel_ActionDeselect_Action = Generalization(general=Action, specific=spinefm_ActionModel_ActionDeselect)
gen_spinefm_ActionModel_ActionAddCTConstraint_Action = Generalization(general=Action, specific=spinefm_ActionModel_ActionAddCTConstraint)

# Domain Model
domain_model = DomainModel(
    name="spinefm",
    types={spinefm_FMModel_Feature, spinefm_FMModel_FeatureModel, Feature, Constraint, Group, spinefm_FMModel_Group, spinefm_FMModel_Constraint, spinefm_MSPLModel_MultipleSoftwareProductLine, DomainElement, DEAssociation, spinefm_MSPLModel_DEAssociation, RestrictionFunction, DEAssociationEnd, spinefm_MSPLModel_MultiplicityElement, spinefm_MSPLModel_DEAssociationEnd, MultiplicityElement, spinefm_MSPLModel_DomainElement, FeatureModel, spinefm_ConfigurationModel_Configuration, ConfigurationProcessStep, Link, ConfigurationState, spinefm_ConfigurationModel_Link, Configuration, spinefm_ConfigurationModel_CompositeConfiguration, spinefm_ProcessModel_LocalContext, spinefm_ProcessModel_ConfigurationProcessStep, Action, Context, spinefm_ProcessModel_Context, spinefm_ProcessModel_GlobalContext, CompositeConfiguration, spinefm_ActionModel_ConfigurationState, spinefm_ProcessModel_ContextManager, MultipleSoftwareProductLine, GlobalContext, LocalContext, spinefm_ProcessModel_DeletedContextInformations, spinefm_ActionModel_RestrictionFunction, Rule, spinefm_ActionModel_Rule, spinefm_ActionModel_Action, spinefm_ActionModel_ActionSelect, spinefm_ActionModel_ActionDeselect, spinefm_ActionModel_ActionAddCTConstraint, GroupState},
    associations={root0, constraints1, inverse15, children3, features4, domainElements6, associations7, restrictionFunction9, source10, target12, LinkMultiplicity18, apply_on19, MultiplicityElement22, refers_on24, belongs_to26, CPS29, belongs_to30, state31, source33, relatedAssociation34, target37, subConfigurations40, links42, actionsDone45, domainElement46, actionsToDo49, context52, configuration54, CPS56, configuration58, configurations59, mspl61, globalContext62, localContexts64, replacedBy66, rules68, inverse69, selectedFeatures72, deselectedFeatures74, fm77, actions80, state82, feature85, fm87, constraint90},
    generalizations={gen_spinefm_ProcessModel_LocalContext_Context, gen_spinefm_ProcessModel_GlobalContext_Context, gen_spinefm_ActionModel_ActionSelect_Action, gen_spinefm_ActionModel_ActionDeselect_Action, gen_spinefm_ActionModel_ActionAddCTConstraint_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)