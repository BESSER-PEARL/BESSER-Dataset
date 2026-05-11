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

ActionType: Enumeration = Enumeration(
    name="ActionType",
    literals={
            EnumerationLiteral(name="AUTOMATIC"),
			EnumerationLiteral(name="MANUAL"),
			EnumerationLiteral(name="FM")
    }
)

# Classes
Feature = Class(name="Feature")
Constraint = Class(name="Constraint")
spinefm_FMModel_Feature = Class(name="spinefm_FMModel_Feature")
Group = Class(name="Group")
spinefm_FMModel_Group = Class(name="spinefm_FMModel_Group")
spinefm_FMModel_FeatureModel = Class(name="spinefm_FMModel_FeatureModel")
DomainElement = Class(name="DomainElement")
DEAssociation = Class(name="DEAssociation")
spinefm_MSPLModel_DEAssociation = Class(name="spinefm_MSPLModel_DEAssociation")
RestrictionFunction = Class(name="RestrictionFunction")
DEAssociationEnd = Class(name="DEAssociationEnd")
spinefm_FMModel_Constraint = Class(name="spinefm_FMModel_Constraint")
spinefm_MSPLModel_MultipleSoftwareProductLine = Class(name="spinefm_MSPLModel_MultipleSoftwareProductLine")
spinefm_MSPLModel_DomainElement = Class(name="spinefm_MSPLModel_DomainElement")
FeatureModel = Class(name="FeatureModel")
spinefm_ConfigurationModel_Configuration = Class(name="spinefm_ConfigurationModel_Configuration")
spinefm_MSPLModel_MultiplicityElement = Class(name="spinefm_MSPLModel_MultiplicityElement")
spinefm_MSPLModel_DEAssociationEnd = Class(name="spinefm_MSPLModel_DEAssociationEnd")
MultiplicityElement = Class(name="MultiplicityElement")
Configuration = Class(name="Configuration")
spinefm_ConfigurationModel_CompositeConfiguration = Class(name="spinefm_ConfigurationModel_CompositeConfiguration")
ConfigurationProcessStep = Class(name="ConfigurationProcessStep")
Link = Class(name="Link")
ConfigurationState = Class(name="ConfigurationState")
spinefm_ConfigurationModel_Link = Class(name="spinefm_ConfigurationModel_Link")
Action = Class(name="Action")
MultipleSoftwareProductLine = Class(name="MultipleSoftwareProductLine")
spinefm_ProcessModel_ConfigurationProcessStep = Class(name="spinefm_ProcessModel_ConfigurationProcessStep")
CompositeConfiguration = Class(name="CompositeConfiguration")
spinefm_ProcessModel_LocalContext = Class(name="spinefm_ProcessModel_LocalContext")
spinefm_ProcessModel_ContextManager = Class(name="spinefm_ProcessModel_ContextManager")
Context = Class(name="Context")
spinefm_ProcessModel_Context = Class(name="spinefm_ProcessModel_Context", is_abstract=True)
spinefm_ProcessModel_GlobalContext = Class(name="spinefm_ProcessModel_GlobalContext")
spinefm_ActionModel_RestrictionFunction = Class(name="spinefm_ActionModel_RestrictionFunction")
Rule = Class(name="Rule")
spinefm_ActionModel_ConfigurationState = Class(name="spinefm_ActionModel_ConfigurationState")
GlobalContext = Class(name="GlobalContext")
LocalContext = Class(name="LocalContext")
spinefm_ProcessModel_DeletedContextInformations = Class(name="spinefm_ProcessModel_DeletedContextInformations")
spinefm_ActionModel_ActionSelect = Class(name="spinefm_ActionModel_ActionSelect")
spinefm_ActionModel_ActionDeselect = Class(name="spinefm_ActionModel_ActionDeselect")
spinefm_ActionModel_ActionAddCTConstraint = Class(name="spinefm_ActionModel_ActionAddCTConstraint")
spinefm_ActionModel_Rule = Class(name="spinefm_ActionModel_Rule")
spinefm_ActionModel_Action = Class(name="spinefm_ActionModel_Action", is_abstract=True)

# Feature class attributes and methods

# Constraint class attributes and methods

# spinefm_FMModel_Feature class attributes and methods
spinefm_FMModel_Feature_id: Property = Property(name="id", type=StringType)
spinefm_FMModel_Feature_name: Property = Property(name="name", type=StringType)
spinefm_FMModel_Feature_m_getAllChildrenFeatures: Method = Method(name="getAllChildrenFeatures", parameters={}, type=StringType)
spinefm_FMModel_Feature.attributes={spinefm_FMModel_Feature_name, spinefm_FMModel_Feature_id}
spinefm_FMModel_Feature.methods={spinefm_FMModel_Feature_m_getAllChildrenFeatures}

# Group class attributes and methods

# spinefm_FMModel_Group class attributes and methods
spinefm_FMModel_Group_state: Property = Property(name="state", type=StringType)
spinefm_FMModel_Group_m_getAllChildren: Method = Method(name="getAllChildren", parameters={}, type=StringType)
spinefm_FMModel_Group.attributes={spinefm_FMModel_Group_state}
spinefm_FMModel_Group.methods={spinefm_FMModel_Group_m_getAllChildren}

# spinefm_FMModel_FeatureModel class attributes and methods
spinefm_FMModel_FeatureModel_id: Property = Property(name="id", type=StringType)
spinefm_FMModel_FeatureModel_name: Property = Property(name="name", type=StringType)
spinefm_FMModel_FeatureModel_m_getStateFT: Method = Method(name="getStateFT", parameters={Parameter(name='spinefm_feature', type=StringType)}, type=StringType)
spinefm_FMModel_FeatureModel_m_getFeatureFromName: Method = Method(name="getFeatureFromName", parameters={Parameter(name='spinefm_name', type=StringType)}, type=StringType)
spinefm_FMModel_FeatureModel_m_addFeature: Method = Method(name="addFeature", parameters={Parameter(name='spinefm_state', type=StringType), Parameter(name='spinefm_name', type=StringType), Parameter(name='spinefm_feature', type=StringType)})
spinefm_FMModel_FeatureModel.attributes={spinefm_FMModel_FeatureModel_id, spinefm_FMModel_FeatureModel_name}
spinefm_FMModel_FeatureModel.methods={spinefm_FMModel_FeatureModel_m_getFeatureFromName, spinefm_FMModel_FeatureModel_m_getStateFT, spinefm_FMModel_FeatureModel_m_addFeature}

# DomainElement class attributes and methods

# DEAssociation class attributes and methods

# spinefm_MSPLModel_DEAssociation class attributes and methods
spinefm_MSPLModel_DEAssociation_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DEAssociation_m_computeActionsToDo: Method = Method(name="computeActionsToDo", parameters={Parameter(name='spinefm_CPSTarget', type=StringType), Parameter(name='spinefm_CPSSource', type=StringType)}, type=StringType)
spinefm_MSPLModel_DEAssociation_m_createAndAssociateInverseAssociation: Method = Method(name="createAndAssociateInverseAssociation", parameters={}, type=StringType)
spinefm_MSPLModel_DEAssociation.attributes={spinefm_MSPLModel_DEAssociation_id}
spinefm_MSPLModel_DEAssociation.methods={spinefm_MSPLModel_DEAssociation_m_createAndAssociateInverseAssociation, spinefm_MSPLModel_DEAssociation_m_computeActionsToDo}

# RestrictionFunction class attributes and methods

# DEAssociationEnd class attributes and methods

# spinefm_FMModel_Constraint class attributes and methods
spinefm_FMModel_Constraint_Rule: Property = Property(name="Rule", type=StringType)
spinefm_FMModel_Constraint.attributes={spinefm_FMModel_Constraint_Rule}

# spinefm_MSPLModel_MultipleSoftwareProductLine class attributes and methods
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getValidAssociationsForSourceAndTarget: Method = Method(name="getValidAssociationsForSourceAndTarget", parameters={Parameter(name='spinefm_target', type=StringType), Parameter(name='spinefm_source', type=StringType)}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine_m_getDomainElementByName: Method = Method(name="getDomainElementByName", parameters={Parameter(name='spinefm_name', type=StringType)}, type=StringType)
spinefm_MSPLModel_MultipleSoftwareProductLine.methods={spinefm_MSPLModel_MultipleSoftwareProductLine_m_getDomainElementByName, spinefm_MSPLModel_MultipleSoftwareProductLine_m_getValidAssociationsForSourceAndTarget}

# spinefm_MSPLModel_DomainElement class attributes and methods
spinefm_MSPLModel_DomainElement_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DomainElement_m_getSourcedAssociations: Method = Method(name="getSourcedAssociations", parameters={}, type=StringType)
spinefm_MSPLModel_DomainElement.attributes={spinefm_MSPLModel_DomainElement_id}
spinefm_MSPLModel_DomainElement.methods={spinefm_MSPLModel_DomainElement_m_getSourcedAssociations}

# FeatureModel class attributes and methods

# spinefm_ConfigurationModel_Configuration class attributes and methods
spinefm_ConfigurationModel_Configuration_id: Property = Property(name="id", type=StringType)
spinefm_ConfigurationModel_Configuration_description: Property = Property(name="description", type=StringType)
spinefm_ConfigurationModel_Configuration_m_canBeLinked: Method = Method(name="canBeLinked", parameters={Parameter(name='spinefm_association', type=StringType)}, type=BooleanType)
spinefm_ConfigurationModel_Configuration_m_getFeatureModel: Method = Method(name="getFeatureModel", parameters={}, type=StringType)
spinefm_ConfigurationModel_Configuration_m_getLinkedConfigurationsOfDomainElement: Method = Method(name="getLinkedConfigurationsOfDomainElement", parameters={Parameter(name='spinefm_de', type=StringType)}, type=StringType)
spinefm_ConfigurationModel_Configuration_m_isCompletlyLinked: Method = Method(name="isCompletlyLinked", parameters={}, type=BooleanType)
spinefm_ConfigurationModel_Configuration_m_getAllCPS: Method = Method(name="getAllCPS", parameters={}, type=StringType)
spinefm_ConfigurationModel_Configuration.attributes={spinefm_ConfigurationModel_Configuration_id, spinefm_ConfigurationModel_Configuration_description}
spinefm_ConfigurationModel_Configuration.methods={spinefm_ConfigurationModel_Configuration_m_canBeLinked, spinefm_ConfigurationModel_Configuration_m_getLinkedConfigurationsOfDomainElement, spinefm_ConfigurationModel_Configuration_m_getFeatureModel, spinefm_ConfigurationModel_Configuration_m_getAllCPS, spinefm_ConfigurationModel_Configuration_m_isCompletlyLinked}

# spinefm_MSPLModel_MultiplicityElement class attributes and methods
spinefm_MSPLModel_MultiplicityElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
spinefm_MSPLModel_MultiplicityElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
spinefm_MSPLModel_MultiplicityElement_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_MultiplicityElement_m_respectBoundaries: Method = Method(name="respectBoundaries", parameters={Parameter(name='spinefm_value', type=StringType)}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement_m_isExactlyOne: Method = Method(name="isExactlyOne", parameters={}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement_m_isLowerThanUpperBound: Method = Method(name="isLowerThanUpperBound", parameters={Parameter(name='spinefm_value', type=StringType)}, type=BooleanType)
spinefm_MSPLModel_MultiplicityElement.attributes={spinefm_MSPLModel_MultiplicityElement_id, spinefm_MSPLModel_MultiplicityElement_upperBound, spinefm_MSPLModel_MultiplicityElement_lowerBound}
spinefm_MSPLModel_MultiplicityElement.methods={spinefm_MSPLModel_MultiplicityElement_m_isLowerThanUpperBound, spinefm_MSPLModel_MultiplicityElement_m_respectBoundaries, spinefm_MSPLModel_MultiplicityElement_m_isExactlyOne}

# spinefm_MSPLModel_DEAssociationEnd class attributes and methods
spinefm_MSPLModel_DEAssociationEnd_id: Property = Property(name="id", type=StringType)
spinefm_MSPLModel_DEAssociationEnd.attributes={spinefm_MSPLModel_DEAssociationEnd_id}

# MultiplicityElement class attributes and methods

# Configuration class attributes and methods

# spinefm_ConfigurationModel_CompositeConfiguration class attributes and methods
spinefm_ConfigurationModel_CompositeConfiguration_name: Property = Property(name="name", type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_m_isValid: Method = Method(name="isValid", parameters={}, type=BooleanType)
spinefm_ConfigurationModel_CompositeConfiguration_m_addConfiguration: Method = Method(name="addConfiguration", parameters={Parameter(name='spinefm_conf', type=StringType)})
spinefm_ConfigurationModel_CompositeConfiguration_m_getConfigurationByName: Method = Method(name="getConfigurationByName", parameters={Parameter(name='spinefm_confName', type=StringType)}, type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration_m_createConfigurationLink: Method = Method(name="createConfigurationLink", parameters={Parameter(name='spinefm_asso', type=StringType), Parameter(name='spinefm_confSource', type=StringType), Parameter(name='spinefm_confTarget', type=StringType)})
spinefm_ConfigurationModel_CompositeConfiguration_m_getCompatibleConfigurations: Method = Method(name="getCompatibleConfigurations", parameters={Parameter(name='spinefm_confSource', type=StringType), Parameter(name='spinefm_asso', type=StringType)}, type=StringType)
spinefm_ConfigurationModel_CompositeConfiguration.attributes={spinefm_ConfigurationModel_CompositeConfiguration_name}
spinefm_ConfigurationModel_CompositeConfiguration.methods={spinefm_ConfigurationModel_CompositeConfiguration_m_getConfigurationByName, spinefm_ConfigurationModel_CompositeConfiguration_m_isValid, spinefm_ConfigurationModel_CompositeConfiguration_m_getCompatibleConfigurations, spinefm_ConfigurationModel_CompositeConfiguration_m_addConfiguration, spinefm_ConfigurationModel_CompositeConfiguration_m_createConfigurationLink}

# ConfigurationProcessStep class attributes and methods

# Link class attributes and methods

# ConfigurationState class attributes and methods

# spinefm_ConfigurationModel_Link class attributes and methods
spinefm_ConfigurationModel_Link_id: Property = Property(name="id", type=StringType)
spinefm_ConfigurationModel_Link_m_getAssociatedConfiguration: Method = Method(name="getAssociatedConfiguration", parameters={Parameter(name='spinefm_conf', type=StringType)}, type=StringType)
spinefm_ConfigurationModel_Link.attributes={spinefm_ConfigurationModel_Link_id}
spinefm_ConfigurationModel_Link.methods={spinefm_ConfigurationModel_Link_m_getAssociatedConfiguration}

# Action class attributes and methods

# MultipleSoftwareProductLine class attributes and methods

# spinefm_ProcessModel_ConfigurationProcessStep class attributes and methods
spinefm_ProcessModel_ConfigurationProcessStep_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_description: Property = Property(name="description", type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_userConfig: Property = Property(name="userConfig", type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_alreadyHaveAction: Method = Method(name="alreadyHaveAction", parameters={Parameter(name='spinefm_a', type=StringType)}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_getConfName: Method = Method(name="getConfName", parameters={}, type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_m_setFMA: Method = Method(name="setFMA", parameters={Parameter(name='spinefm_fma', type=StringType)})
spinefm_ProcessModel_ConfigurationProcessStep_m_apply: Method = Method(name="apply", parameters={}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_mergeWithExternalCPS: Method = Method(name="mergeWithExternalCPS", parameters={Parameter(name='spinefm_cps', type=StringType)})
spinefm_ProcessModel_ConfigurationProcessStep_m_isCompatibleWithConfiguration: Method = Method(name="isCompatibleWithConfiguration", parameters={Parameter(name='spinefm_conf', type=StringType)}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_isComplete: Method = Method(name="isComplete", parameters={}, type=BooleanType)
spinefm_ProcessModel_ConfigurationProcessStep_m_getState: Method = Method(name="getState", parameters={}, type=StringType)
spinefm_ProcessModel_ConfigurationProcessStep_m_addActionToDo: Method = Method(name="addActionToDo", parameters={Parameter(name='spinefm_a', type=StringType)})
spinefm_ProcessModel_ConfigurationProcessStep.attributes={spinefm_ProcessModel_ConfigurationProcessStep_userConfig, spinefm_ProcessModel_ConfigurationProcessStep_id, spinefm_ProcessModel_ConfigurationProcessStep_description}
spinefm_ProcessModel_ConfigurationProcessStep.methods={spinefm_ProcessModel_ConfigurationProcessStep_m_isComplete, spinefm_ProcessModel_ConfigurationProcessStep_m_addActionToDo, spinefm_ProcessModel_ConfigurationProcessStep_m_apply, spinefm_ProcessModel_ConfigurationProcessStep_m_isCompatibleWithConfiguration, spinefm_ProcessModel_ConfigurationProcessStep_m_mergeWithExternalCPS, spinefm_ProcessModel_ConfigurationProcessStep_m_getState, spinefm_ProcessModel_ConfigurationProcessStep_m_getConfName, spinefm_ProcessModel_ConfigurationProcessStep_m_setFMA, spinefm_ProcessModel_ConfigurationProcessStep_m_alreadyHaveAction}

# CompositeConfiguration class attributes and methods

# spinefm_ProcessModel_LocalContext class attributes and methods

# spinefm_ProcessModel_ContextManager class attributes and methods
spinefm_ProcessModel_ContextManager_m_propagate: Method = Method(name="propagate", parameters={Parameter(name='spinefm_CPS', type=StringType), Parameter(name='spinefm_context', type=StringType)})
spinefm_ProcessModel_ContextManager_m_setFMAdapter: Method = Method(name="setFMAdapter", parameters={Parameter(name='spinefm_fma', type=StringType)})
spinefm_ProcessModel_ContextManager_m_init: Method = Method(name="init", parameters={})
spinefm_ProcessModel_ContextManager_m_createNewContext: Method = Method(name="createNewContext", parameters={}, type=StringType)
spinefm_ProcessModel_ContextManager_m_getContextFromId: Method = Method(name="getContextFromId", parameters={Parameter(name='spinefm_id', type=StringType)}, type=StringType)
spinefm_ProcessModel_ContextManager_m_linkConfigurationsAndManageContexts: Method = Method(name="linkConfigurationsAndManageContexts", parameters={Parameter(name='spinefm_confTarget', type=StringType), Parameter(name='spinefm_confSource', type=StringType), Parameter(name='spinefm_association', type=StringType)}, type=StringType)
spinefm_ProcessModel_ContextManager_m_createNewContextCloningCPS: Method = Method(name="createNewContextCloningCPS", parameters={Parameter(name='spinefm_cps', type=StringType)}, type=StringType)
spinefm_ProcessModel_ContextManager.methods={spinefm_ProcessModel_ContextManager_m_linkConfigurationsAndManageContexts, spinefm_ProcessModel_ContextManager_m_createNewContext, spinefm_ProcessModel_ContextManager_m_setFMAdapter, spinefm_ProcessModel_ContextManager_m_propagate, spinefm_ProcessModel_ContextManager_m_init, spinefm_ProcessModel_ContextManager_m_getContextFromId, spinefm_ProcessModel_ContextManager_m_createNewContextCloningCPS}

# Context class attributes and methods

# spinefm_ProcessModel_Context class attributes and methods
spinefm_ProcessModel_Context_id: Property = Property(name="id", type=StringType)
spinefm_ProcessModel_Context_m_addCPS: Method = Method(name="addCPS", parameters={Parameter(name='spinefm_cps', type=StringType)})
spinefm_ProcessModel_Context_m_getCPSOfDE: Method = Method(name="getCPSOfDE", parameters={Parameter(name='spinefm_de', type=StringType)}, type=StringType)
spinefm_ProcessModel_Context_m_mergeExternalCPS: Method = Method(name="mergeExternalCPS", parameters={Parameter(name='spinefm_externalCPS', type=StringType)})
spinefm_ProcessModel_Context.attributes={spinefm_ProcessModel_Context_id}
spinefm_ProcessModel_Context.methods={spinefm_ProcessModel_Context_m_addCPS, spinefm_ProcessModel_Context_m_mergeExternalCPS, spinefm_ProcessModel_Context_m_getCPSOfDE}

# spinefm_ProcessModel_GlobalContext class attributes and methods

# spinefm_ActionModel_RestrictionFunction class attributes and methods
spinefm_ActionModel_RestrictionFunction_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_RestrictionFunction_m_createAndAssociateInverseRestFunc: Method = Method(name="createAndAssociateInverseRestFunc", parameters={}, type=StringType)
spinefm_ActionModel_RestrictionFunction.attributes={spinefm_ActionModel_RestrictionFunction_id}
spinefm_ActionModel_RestrictionFunction.methods={spinefm_ActionModel_RestrictionFunction_m_createAndAssociateInverseRestFunc}

# Rule class attributes and methods

# spinefm_ActionModel_ConfigurationState class attributes and methods
spinefm_ActionModel_ConfigurationState_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_ConfigurationState_m_isIncludedIn: Method = Method(name="isIncludedIn", parameters={Parameter(name='spinefm_otherState', type=StringType)}, type=BooleanType)
spinefm_ActionModel_ConfigurationState.attributes={spinefm_ActionModel_ConfigurationState_id}
spinefm_ActionModel_ConfigurationState.methods={spinefm_ActionModel_ConfigurationState_m_isIncludedIn}

# GlobalContext class attributes and methods

# LocalContext class attributes and methods

# spinefm_ProcessModel_DeletedContextInformations class attributes and methods
spinefm_ProcessModel_DeletedContextInformations_deletedContext: Property = Property(name="deletedContext", type=StringType)
spinefm_ProcessModel_DeletedContextInformations.attributes={spinefm_ProcessModel_DeletedContextInformations_deletedContext}

# spinefm_ActionModel_ActionSelect class attributes and methods

# spinefm_ActionModel_ActionDeselect class attributes and methods

# spinefm_ActionModel_ActionAddCTConstraint class attributes and methods

# spinefm_ActionModel_Rule class attributes and methods
spinefm_ActionModel_Rule_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_Rule_m_createInverseRule: Method = Method(name="createInverseRule", parameters={}, type=StringType)
spinefm_ActionModel_Rule.attributes={spinefm_ActionModel_Rule_id}
spinefm_ActionModel_Rule.methods={spinefm_ActionModel_Rule_m_createInverseRule}

# spinefm_ActionModel_Action class attributes and methods
spinefm_ActionModel_Action_id: Property = Property(name="id", type=StringType)
spinefm_ActionModel_Action_type: Property = Property(name="type", type=StringType)
spinefm_ActionModel_Action_m_isSameObject: Method = Method(name="isSameObject", parameters={Parameter(name='spinefm_o', type=StringType)}, type=BooleanType)
spinefm_ActionModel_Action_m_applyAction: Method = Method(name="applyAction", parameters={Parameter(name='spinefm_confName', type=StringType), Parameter(name='spinefm_fma', type=StringType)})
spinefm_ActionModel_Action.attributes={spinefm_ActionModel_Action_type, spinefm_ActionModel_Action_id}
spinefm_ActionModel_Action.methods={spinefm_ActionModel_Action_m_isSameObject, spinefm_ActionModel_Action_m_applyAction}

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
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="DEAssociationEnd14", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation13", type=DEAssociationEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inverse15: BinaryAssociation = BinaryAssociation(
    name="inverse15",
    ends={
        Property(name="DEAssociation17", type=spinefm_MSPLModel_DEAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociation16", type=DEAssociation, multiplicity=Multiplicity(1, 1))
    }
)
LinkMultiplicity18: BinaryAssociation = BinaryAssociation(
    name="LinkMultiplicity18",
    ends={
        Property(name="MultiplicityElement", type=spinefm_MSPLModel_DEAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_MSPLModel_DEAssociationEnd", type=MultiplicityElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source39: BinaryAssociation = BinaryAssociation(
    name="source39",
    ends={
        Property(name="Configuration", type=spinefm_ConfigurationModel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Link", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
relatedAssociation40: BinaryAssociation = BinaryAssociation(
    name="relatedAssociation40",
    ends={
        Property(name="DEAssociation42", type=spinefm_ConfigurationModel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Link41", type=DEAssociation, multiplicity=Multiplicity(1, 1))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="Configuration45", type=spinefm_ConfigurationModel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Link44", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
CPSRef29: BinaryAssociation = BinaryAssociation(
    name="CPSRef29",
    ends={
        Property(name="ConfigurationProcessStep", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 1))
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
domainElement33: BinaryAssociation = BinaryAssociation(
    name="domainElement33",
    ends={
        Property(name="DomainElement35", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration34", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
clonedCPS36: BinaryAssociation = BinaryAssociation(
    name="clonedCPS36",
    ends={
        Property(name="ConfigurationProcessStep38", type=spinefm_ConfigurationModel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_Configuration37", type=ConfigurationProcessStep, multiplicity=Multiplicity(0, 9999))
    }
)
actionsDone53: BinaryAssociation = BinaryAssociation(
    name="actionsDone53",
    ends={
        Property(name="Action", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep", type=Action, multiplicity=Multiplicity(0, 9999))
    }
)
domainElement54: BinaryAssociation = BinaryAssociation(
    name="domainElement54",
    ends={
        Property(name="DomainElement56", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep55", type=DomainElement, multiplicity=Multiplicity(1, 1))
    }
)
actionsToDo57: BinaryAssociation = BinaryAssociation(
    name="actionsToDo57",
    ends={
        Property(name="Action59", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep58", type=Action, multiplicity=Multiplicity(0, 9999))
    }
)
subConfigurations46: BinaryAssociation = BinaryAssociation(
    name="subConfigurations46",
    ends={
        Property(name="Configuration47", type=spinefm_ConfigurationModel_CompositeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_CompositeConfiguration", type=Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links48: BinaryAssociation = BinaryAssociation(
    name="links48",
    ends={
        Property(name="Link50", type=spinefm_ConfigurationModel_CompositeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_CompositeConfiguration49", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mspl51: BinaryAssociation = BinaryAssociation(
    name="mspl51",
    ends={
        Property(name="MultipleSoftwareProductLine", type=spinefm_ConfigurationModel_CompositeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ConfigurationModel_CompositeConfiguration52", type=MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1))
    }
)
configuration66: BinaryAssociation = BinaryAssociation(
    name="configuration66",
    ends={
        Property(name="CompositeConfiguration", type=spinefm_ProcessModel_GlobalContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_GlobalContext", type=CompositeConfiguration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configurations67: BinaryAssociation = BinaryAssociation(
    name="configurations67",
    ends={
        Property(name="Configuration68", type=spinefm_ProcessModel_LocalContext, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_LocalContext", type=Configuration, multiplicity=Multiplicity(1, 9999))
    }
)
context60: BinaryAssociation = BinaryAssociation(
    name="context60",
    ends={
        Property(name="Context", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ConfigurationProcessStep61", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
configuration62: BinaryAssociation = BinaryAssociation(
    name="configuration62",
    ends={
        Property(name="Configuration63", type=spinefm_ProcessModel_ConfigurationProcessStep, multiplicity=Multiplicity(1, 1)),
        Property(name="CPSRef", type=Configuration, multiplicity=Multiplicity(0, 1))
    }
)
CPS64: BinaryAssociation = BinaryAssociation(
    name="CPS64",
    ends={
        Property(name="ConfigurationProcessStep65", type=spinefm_ProcessModel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_Context", type=ConfigurationProcessStep, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rules77: BinaryAssociation = BinaryAssociation(
    name="rules77",
    ends={
        Property(name="Rule", type=spinefm_ActionModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_RestrictionFunction", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inverse78: BinaryAssociation = BinaryAssociation(
    name="inverse78",
    ends={
        Property(name="RestrictionFunction80", type=spinefm_ActionModel_RestrictionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_RestrictionFunction79", type=RestrictionFunction, multiplicity=Multiplicity(1, 1))
    }
)
mspl69: BinaryAssociation = BinaryAssociation(
    name="mspl69",
    ends={
        Property(name="MultipleSoftwareProductLine70", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager", type=MultipleSoftwareProductLine, multiplicity=Multiplicity(1, 1))
    }
)
globalContext71: BinaryAssociation = BinaryAssociation(
    name="globalContext71",
    ends={
        Property(name="GlobalContext", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager72", type=GlobalContext, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localContexts73: BinaryAssociation = BinaryAssociation(
    name="localContexts73",
    ends={
        Property(name="LocalContext", type=spinefm_ProcessModel_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_ContextManager74", type=LocalContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacedBy75: BinaryAssociation = BinaryAssociation(
    name="replacedBy75",
    ends={
        Property(name="Context76", type=spinefm_ProcessModel_DeletedContextInformations, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ProcessModel_DeletedContextInformations", type=Context, multiplicity=Multiplicity(0, 1))
    }
)
feature94: BinaryAssociation = BinaryAssociation(
    name="feature94",
    ends={
        Property(name="Feature95", type=spinefm_ActionModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Action", type=Feature, multiplicity=Multiplicity(0, 1))
    }
)
fm96: BinaryAssociation = BinaryAssociation(
    name="fm96",
    ends={
        Property(name="FeatureModel98", type=spinefm_ActionModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Action97", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
constraint99: BinaryAssociation = BinaryAssociation(
    name="constraint99",
    ends={
        Property(name="Constraint100", type=spinefm_ActionModel_ActionAddCTConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ActionAddCTConstraint", type=Constraint, multiplicity=Multiplicity(1, 1))
    }
)
selectedFeatures81: BinaryAssociation = BinaryAssociation(
    name="selectedFeatures81",
    ends={
        Property(name="Feature82", type=spinefm_ActionModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ConfigurationState", type=Feature, multiplicity=Multiplicity(1, 9999))
    }
)
deselectedFeatures83: BinaryAssociation = BinaryAssociation(
    name="deselectedFeatures83",
    ends={
        Property(name="Feature85", type=spinefm_ActionModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ConfigurationState84", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
fm86: BinaryAssociation = BinaryAssociation(
    name="fm86",
    ends={
        Property(name="FeatureModel88", type=spinefm_ActionModel_ConfigurationState, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_ConfigurationState87", type=FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
actions89: BinaryAssociation = BinaryAssociation(
    name="actions89",
    ends={
        Property(name="Action90", type=spinefm_ActionModel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Rule", type=Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state91: BinaryAssociation = BinaryAssociation(
    name="state91",
    ends={
        Property(name="ConfigurationState93", type=spinefm_ActionModel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spinefm_ActionModel_Rule92", type=ConfigurationState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_spinefm_ProcessModel_GlobalContext_Context = Generalization(general=Context, specific=spinefm_ProcessModel_GlobalContext)
gen_spinefm_ProcessModel_LocalContext_Context = Generalization(general=Context, specific=spinefm_ProcessModel_LocalContext)
gen_spinefm_ActionModel_ActionSelect_Action = Generalization(general=Action, specific=spinefm_ActionModel_ActionSelect)
gen_spinefm_ActionModel_ActionDeselect_Action = Generalization(general=Action, specific=spinefm_ActionModel_ActionDeselect)
gen_spinefm_ActionModel_ActionAddCTConstraint_Action = Generalization(general=Action, specific=spinefm_ActionModel_ActionAddCTConstraint)

# Domain Model
domain_model = DomainModel(
    name="spinefm",
    types={Feature, Constraint, spinefm_FMModel_Feature, Group, spinefm_FMModel_Group, spinefm_FMModel_FeatureModel, DomainElement, DEAssociation, spinefm_MSPLModel_DEAssociation, RestrictionFunction, DEAssociationEnd, spinefm_FMModel_Constraint, spinefm_MSPLModel_MultipleSoftwareProductLine, spinefm_MSPLModel_DomainElement, FeatureModel, spinefm_ConfigurationModel_Configuration, spinefm_MSPLModel_MultiplicityElement, spinefm_MSPLModel_DEAssociationEnd, MultiplicityElement, Configuration, spinefm_ConfigurationModel_CompositeConfiguration, ConfigurationProcessStep, Link, ConfigurationState, spinefm_ConfigurationModel_Link, Action, MultipleSoftwareProductLine, spinefm_ProcessModel_ConfigurationProcessStep, CompositeConfiguration, spinefm_ProcessModel_LocalContext, spinefm_ProcessModel_ContextManager, Context, spinefm_ProcessModel_Context, spinefm_ProcessModel_GlobalContext, spinefm_ActionModel_RestrictionFunction, Rule, spinefm_ActionModel_ConfigurationState, GlobalContext, LocalContext, spinefm_ProcessModel_DeletedContextInformations, spinefm_ActionModel_ActionSelect, spinefm_ActionModel_ActionDeselect, spinefm_ActionModel_ActionAddCTConstraint, spinefm_ActionModel_Rule, spinefm_ActionModel_Action, GroupState, ActionType},
    associations={root0, constraints1, children3, features4, domainElements6, associations7, restrictionFunction9, source10, apply_on19, MultiplicityElement22, refers_on24, belongs_to26, target12, inverse15, LinkMultiplicity18, source39, relatedAssociation40, target43, CPSRef29, belongs_to30, state31, domainElement33, clonedCPS36, actionsDone53, domainElement54, actionsToDo57, subConfigurations46, links48, mspl51, configuration66, configurations67, context60, configuration62, CPS64, rules77, inverse78, mspl69, globalContext71, localContexts73, replacedBy75, feature94, fm96, constraint99, selectedFeatures81, deselectedFeatures83, fm86, actions89, state91},
    generalizations={gen_spinefm_ProcessModel_GlobalContext_Context, gen_spinefm_ProcessModel_LocalContext_Context, gen_spinefm_ActionModel_ActionSelect_Action, gen_spinefm_ActionModel_ActionDeselect_Action, gen_spinefm_ActionModel_ActionAddCTConstraint_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)