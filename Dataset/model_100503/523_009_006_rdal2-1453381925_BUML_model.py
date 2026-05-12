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
InteractionVariableType: Enumeration = Enumeration(
    name="InteractionVariableType",
    literals={
            EnumerationLiteral(name="Monitorable"),
			EnumerationLiteral(name="Controllable")
    }
)

AggregationType: Enumeration = Enumeration(
    name="AggregationType",
    literals={
            EnumerationLiteral(name="Composition"),
			EnumerationLiteral(name="Alternative")
    }
)

Modality: Enumeration = Enumeration(
    name="Modality",
    literals={
            EnumerationLiteral(name="Maximum"),
			EnumerationLiteral(name="Minimum")
    }
)

# Classes
rdal_IdentifiedElement = Class(name="rdal_IdentifiedElement", is_abstract=True)
rdal_UserProperty = Class(name="rdal_UserProperty")
rdal_ElementRefinement = Class(name="rdal_ElementRefinement", is_abstract=True)
IdentifiedElement = Class(name="IdentifiedElement")
rdal_RefineableElement = Class(name="rdal_RefineableElement", is_abstract=True)
rdal_SubElementReference = Class(name="rdal_SubElementReference", is_abstract=True)
rdal_RequirementRefinement = Class(name="rdal_RequirementRefinement")
ElementRefinement = Class(name="ElementRefinement")
SatisfiableElement = Class(name="SatisfiableElement")
VerifiableElement = Class(name="VerifiableElement")
rdal_SubRequirementReference = Class(name="rdal_SubRequirementReference")
rdal_AbstractRequirement = Class(name="rdal_AbstractRequirement", is_abstract=True)
rdal_Stakeholder = Class(name="rdal_Stakeholder")
rdal_GoalRefinement = Class(name="rdal_GoalRefinement")
rdal_SubGoalReference = Class(name="rdal_SubGoalReference")
rdal_AbstractGoal = Class(name="rdal_AbstractGoal", is_abstract=True)
rdal_TraceableToDesignElementsElement = Class(name="rdal_TraceableToDesignElementsElement", is_abstract=True)
rdal_ReferencedDesignElements = Class(name="rdal_ReferencedDesignElements", is_abstract=True)
rdal_Specification = Class(name="rdal_Specification")
rdal_AbstractContractualElement = Class(name="rdal_AbstractContractualElement", is_abstract=True)
TraceableToDesignElementsElement = Class(name="TraceableToDesignElementsElement")
rdal_Rationale = Class(name="rdal_Rationale")
rdal_ContactInformation = Class(name="rdal_ContactInformation")
rdal_Uncertainty = Class(name="rdal_Uncertainty")
rdal_TextualContractualElement = Class(name="rdal_TextualContractualElement", is_abstract=True)
AbstractContractualElement = Class(name="AbstractContractualElement")
rdal_Expression = Class(name="rdal_Expression")
rdal_Category = Class(name="rdal_Category")
rdal_SystemOverview = Class(name="rdal_SystemOverview")
rdal_SatisfiableElement = Class(name="rdal_SatisfiableElement", is_abstract=True)
rdal_VerifiableElement = Class(name="rdal_VerifiableElement", is_abstract=True)
rdal_RdalOrgPackage = Class(name="rdal_RdalOrgPackage", is_abstract=True)
rdal_Conflict = Class(name="rdal_Conflict")
rdal_ConstraintLanguagesSpec = Class(name="rdal_ConstraintLanguagesSpec")
rdal_ActorReference = Class(name="rdal_ActorReference")
rdal_EObject = Class(name="rdal_EObject")
rdal_NonFunctionalProperty = Class(name="rdal_NonFunctionalProperty")
rdal_GoalsPackage = Class(name="rdal_GoalsPackage")
rdal_RequirementsPackage = Class(name="rdal_RequirementsPackage")
RdalOrgPackage = Class(name="RdalOrgPackage")
rdal_InteractionVariable = Class(name="rdal_InteractionVariable")
rdal_Capability = Class(name="rdal_Capability")
rdal_SystemContext = Class(name="rdal_SystemContext")
rdal_Variable = Class(name="rdal_Variable")
Variable = Class(name="Variable")
rdal_Requirement = Class(name="rdal_Requirement")
AbstractRequirement = Class(name="AbstractRequirement")
TextualContractualElement = Class(name="TextualContractualElement")
rdal_VerificationActivity = Class(name="rdal_VerificationActivity")
rdal_NonFunctionalGoal = Class(name="rdal_NonFunctionalGoal")
RefineableElement = Class(name="RefineableElement")
rdal_Assumption = Class(name="rdal_Assumption")
rdal_SystemFunctionGoal = Class(name="rdal_SystemFunctionGoal")
AbstractGoal = Class(name="AbstractGoal")
rdal_QualityObjective = Class(name="rdal_QualityObjective")
NonFunctionalGoal = Class(name="NonFunctionalGoal")
rdal_Sensitivity = Class(name="rdal_Sensitivity")
rdal_DesignElementReference = Class(name="rdal_DesignElementReference")
rdal_VerifiableDesignElementRef = Class(name="rdal_VerifiableDesignElementRef")
DesignElementReference = Class(name="DesignElementReference")
rdal_SatisfiableDesignElementRef = Class(name="rdal_SatisfiableDesignElementRef")
rdal_PrioritizedSatDesignElementRef = Class(name="rdal_PrioritizedSatDesignElementRef")
SatisfiableDesignElementRef = Class(name="SatisfiableDesignElementRef")
rdal_SystOverviewDesignElemRef = Class(name="rdal_SystOverviewDesignElemRef")
rdal_SystContextDesignElemRef = Class(name="rdal_SystContextDesignElemRef")
rdal_RefManuallySelectedDesignElements = Class(name="rdal_RefManuallySelectedDesignElements")
ReferencedDesignElements = Class(name="ReferencedDesignElements")
rdal_RefQueryCollectedDesignElements = Class(name="rdal_RefQueryCollectedDesignElements")
rdal_FormalLanguageExpression = Class(name="rdal_FormalLanguageExpression")
rdal_TraceDesignElementRef = Class(name="rdal_TraceDesignElementRef")
RequirementsCoverageData = Class(name="RequirementsCoverageData")
rdal_Trace = Class(name="rdal_Trace")
rdal_RequirementsCoverageData = Class(name="rdal_RequirementsCoverageData")
SubElementReference = Class(name="SubElementReference")

# rdal_IdentifiedElement class attributes and methods
rdal_IdentifiedElement_name: Property = Property(name="name", type=StringType)
rdal_IdentifiedElement_id: Property = Property(name="id", type=StringType)
rdal_IdentifiedElement_description: Property = Property(name="description", type=StringType)
rdal_IdentifiedElement.attributes={rdal_IdentifiedElement_description, rdal_IdentifiedElement_name, rdal_IdentifiedElement_id}

# rdal_UserProperty class attributes and methods
rdal_UserProperty_value: Property = Property(name="value", type=StringType)
rdal_UserProperty_name: Property = Property(name="name", type=StringType)
rdal_UserProperty.attributes={rdal_UserProperty_value, rdal_UserProperty_name}

# rdal_ElementRefinement class attributes and methods
rdal_ElementRefinement_subElementRefEntries: Property = Property(name="subElementRefEntries", type=StringType)
rdal_ElementRefinement_refinedElementEntries: Property = Property(name="refinedElementEntries", type=StringType)
rdal_ElementRefinement.attributes={rdal_ElementRefinement_refinedElementEntries, rdal_ElementRefinement_subElementRefEntries}

# IdentifiedElement class attributes and methods

# rdal_RefineableElement class attributes and methods

# rdal_SubElementReference class attributes and methods
rdal_SubElementReference_weight: Property = Property(name="weight", type=StringType)
rdal_SubElementReference_referencedElementEntries: Property = Property(name="referencedElementEntries", type=StringType)
rdal_SubElementReference.attributes={rdal_SubElementReference_weight, rdal_SubElementReference_referencedElementEntries}

# rdal_RequirementRefinement class attributes and methods

# ElementRefinement class attributes and methods

# SatisfiableElement class attributes and methods

# VerifiableElement class attributes and methods

# rdal_SubRequirementReference class attributes and methods

# rdal_AbstractRequirement class attributes and methods
rdal_AbstractRequirement_risk: Property = Property(name="risk", type=StringType)
rdal_AbstractRequirement.attributes={rdal_AbstractRequirement_risk}

# rdal_Stakeholder class attributes and methods

# rdal_GoalRefinement class attributes and methods

# rdal_SubGoalReference class attributes and methods

# rdal_AbstractGoal class attributes and methods

# rdal_TraceableToDesignElementsElement class attributes and methods

# rdal_ReferencedDesignElements class attributes and methods
rdal_ReferencedDesignElements_agregationType: Property = Property(name="agregationType", type=StringType)
rdal_ReferencedDesignElements.attributes={rdal_ReferencedDesignElements_agregationType}

# rdal_Specification class attributes and methods
rdal_Specification_version: Property = Property(name="version", type=StringType)
rdal_Specification.attributes={rdal_Specification_version}

# rdal_AbstractContractualElement class attributes and methods
rdal_AbstractContractualElement_originDate: Property = Property(name="originDate", type=StringType)
rdal_AbstractContractualElement_scheduleDate: Property = Property(name="scheduleDate", type=StringType)
rdal_AbstractContractualElement_sources: Property = Property(name="sources", type=StringType)
rdal_AbstractContractualElement_dropped: Property = Property(name="dropped", type=BooleanType)
rdal_AbstractContractualElement.attributes={rdal_AbstractContractualElement_dropped, rdal_AbstractContractualElement_scheduleDate, rdal_AbstractContractualElement_originDate, rdal_AbstractContractualElement_sources}

# TraceableToDesignElementsElement class attributes and methods

# rdal_Rationale class attributes and methods

# rdal_ContactInformation class attributes and methods
rdal_ContactInformation_address: Property = Property(name="address", type=StringType)
rdal_ContactInformation_email: Property = Property(name="email", type=StringType)
rdal_ContactInformation_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
rdal_ContactInformation_country: Property = Property(name="country", type=StringType)
rdal_ContactInformation.attributes={rdal_ContactInformation_phoneNumber, rdal_ContactInformation_address, rdal_ContactInformation_email, rdal_ContactInformation_country}

# rdal_Uncertainty class attributes and methods
rdal_Uncertainty_volatility: Property = Property(name="volatility", type=StringType)
rdal_Uncertainty_costsImpact: Property = Property(name="costsImpact", type=StringType)
rdal_Uncertainty_scheduleImpact: Property = Property(name="scheduleImpact", type=StringType)
rdal_Uncertainty_timeCriticality: Property = Property(name="timeCriticality", type=StringType)
rdal_Uncertainty_familiarity: Property = Property(name="familiarity", type=StringType)
rdal_Uncertainty_riskIndex: Property = Property(name="riskIndex", type=StringType)
rdal_Uncertainty_propRiskIndex: Property = Property(name="propRiskIndex", type=StringType)
rdal_Uncertainty_maturityIndex: Property = Property(name="maturityIndex", type=StringType)
rdal_Uncertainty.attributes={rdal_Uncertainty_scheduleImpact, rdal_Uncertainty_riskIndex, rdal_Uncertainty_familiarity, rdal_Uncertainty_costsImpact, rdal_Uncertainty_volatility, rdal_Uncertainty_maturityIndex, rdal_Uncertainty_propRiskIndex, rdal_Uncertainty_timeCriticality}

# rdal_TextualContractualElement class attributes and methods
rdal_TextualContractualElement_priority: Property = Property(name="priority", type=StringType)
rdal_TextualContractualElement.attributes={rdal_TextualContractualElement_priority}

# AbstractContractualElement class attributes and methods

# rdal_Expression class attributes and methods

# rdal_Category class attributes and methods

# rdal_SystemOverview class attributes and methods
rdal_SystemOverview_purpose: Property = Property(name="purpose", type=StringType)
rdal_SystemOverview.attributes={rdal_SystemOverview_purpose}

# rdal_SatisfiableElement class attributes and methods
rdal_SatisfiableElement_satisfactionLevel: Property = Property(name="satisfactionLevel", type=StringType)
rdal_SatisfiableElement.attributes={rdal_SatisfiableElement_satisfactionLevel}

# rdal_VerifiableElement class attributes and methods
rdal_VerifiableElement_verified: Property = Property(name="verified", type=StringType)
rdal_VerifiableElement.attributes={rdal_VerifiableElement_verified}

# rdal_RdalOrgPackage class attributes and methods
rdal_RdalOrgPackage_contractualElementEntries: Property = Property(name="contractualElementEntries", type=StringType)
rdal_RdalOrgPackage_refinementEntries: Property = Property(name="refinementEntries", type=StringType)
rdal_RdalOrgPackage.attributes={rdal_RdalOrgPackage_contractualElementEntries, rdal_RdalOrgPackage_refinementEntries}

# rdal_Conflict class attributes and methods
rdal_Conflict_degree: Property = Property(name="degree", type=StringType)
rdal_Conflict.attributes={rdal_Conflict_degree}

# rdal_ConstraintLanguagesSpec class attributes and methods

# rdal_ActorReference class attributes and methods

# rdal_EObject class attributes and methods

# rdal_NonFunctionalProperty class attributes and methods

# rdal_GoalsPackage class attributes and methods

# rdal_RequirementsPackage class attributes and methods

# RdalOrgPackage class attributes and methods

# rdal_InteractionVariable class attributes and methods
rdal_InteractionVariable_type: Property = Property(name="type", type=StringType)
rdal_InteractionVariable_neglected: Property = Property(name="neglected", type=BooleanType)
rdal_InteractionVariable.attributes={rdal_InteractionVariable_neglected, rdal_InteractionVariable_type}

# rdal_Capability class attributes and methods

# rdal_SystemContext class attributes and methods

# rdal_Variable class attributes and methods

# Variable class attributes and methods

# rdal_Requirement class attributes and methods

# AbstractRequirement class attributes and methods

# TextualContractualElement class attributes and methods

# rdal_VerificationActivity class attributes and methods
rdal_VerificationActivity_passed: Property = Property(name="passed", type=BooleanType)
rdal_VerificationActivity.attributes={rdal_VerificationActivity_passed}

# rdal_NonFunctionalGoal class attributes and methods

# RefineableElement class attributes and methods

# rdal_Assumption class attributes and methods

# rdal_SystemFunctionGoal class attributes and methods

# AbstractGoal class attributes and methods

# rdal_QualityObjective class attributes and methods
rdal_QualityObjective_modality: Property = Property(name="modality", type=StringType)
rdal_QualityObjective_bound: Property = Property(name="bound", type=FloatType)
rdal_QualityObjective.attributes={rdal_QualityObjective_bound, rdal_QualityObjective_modality}

# NonFunctionalGoal class attributes and methods

# rdal_Sensitivity class attributes and methods

# rdal_DesignElementReference class attributes and methods
rdal_DesignElementReference_evaluationResult: Property = Property(name="evaluationResult", type=StringType)
rdal_DesignElementReference.attributes={rdal_DesignElementReference_evaluationResult}

# rdal_VerifiableDesignElementRef class attributes and methods

# DesignElementReference class attributes and methods

# rdal_SatisfiableDesignElementRef class attributes and methods

# rdal_PrioritizedSatDesignElementRef class attributes and methods
rdal_PrioritizedSatDesignElementRef_priority: Property = Property(name="priority", type=StringType)
rdal_PrioritizedSatDesignElementRef_weight: Property = Property(name="weight", type=StringType)
rdal_PrioritizedSatDesignElementRef.attributes={rdal_PrioritizedSatDesignElementRef_weight, rdal_PrioritizedSatDesignElementRef_priority}

# SatisfiableDesignElementRef class attributes and methods

# rdal_SystOverviewDesignElemRef class attributes and methods

# rdal_SystContextDesignElemRef class attributes and methods

# rdal_RefManuallySelectedDesignElements class attributes and methods

# ReferencedDesignElements class attributes and methods

# rdal_RefQueryCollectedDesignElements class attributes and methods

# rdal_FormalLanguageExpression class attributes and methods

# rdal_TraceDesignElementRef class attributes and methods
rdal_TraceDesignElementRef_container: Property = Property(name="container", type=BooleanType)
rdal_TraceDesignElementRef_m_merge: Method = Method(name="merge", parameters={Parameter(name='rdal_modelElementReference', type=StringType)})
rdal_TraceDesignElementRef.attributes={rdal_TraceDesignElementRef_container}
rdal_TraceDesignElementRef.methods={rdal_TraceDesignElementRef_m_merge}

# RequirementsCoverageData class attributes and methods

# rdal_Trace class attributes and methods
rdal_Trace_m_modelElementReference: Method = Method(name="modelElementReference", parameters={Parameter(name='rdal_modelElement', type=StringType)}, type=StringType)
rdal_Trace.methods={rdal_Trace_m_modelElementReference}

# rdal_RequirementsCoverageData class attributes and methods
rdal_RequirementsCoverageData_nbRequirements: Property = Property(name="nbRequirements", type=IntegerType)
rdal_RequirementsCoverageData_verificationLevel: Property = Property(name="verificationLevel", type=StringType)
rdal_RequirementsCoverageData.attributes={rdal_RequirementsCoverageData_verificationLevel, rdal_RequirementsCoverageData_nbRequirements}

# SubElementReference class attributes and methods

# Relationships
ownedUserProperties0: BinaryAssociation = BinaryAssociation(
    name="ownedUserProperties0",
    ends={
        Property(name="rdal_UserProperty", type=rdal_IdentifiedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_IdentifiedElement", type=rdal_UserProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinedRequirement10: BinaryAssociation = BinaryAssociation(
    name="refinedRequirement10",
    ends={
        Property(name="rdal_AbstractRequirement12", type=rdal_RequirementRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RequirementRefinement11", type=rdal_AbstractRequirement, multiplicity=Multiplicity(1, 1))
    }
)
subElements1: BinaryAssociation = BinaryAssociation(
    name="subElements1",
    ends={
        Property(name="rdal_RefineableElement", type=rdal_ElementRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_ElementRefinement", type=rdal_RefineableElement, multiplicity=Multiplicity(1, 9999))
    }
)
ownedSubElementRefs2: BinaryAssociation = BinaryAssociation(
    name="ownedSubElementRefs2",
    ends={
        Property(name="rdal_SubElementReference", type=rdal_ElementRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_ElementRefinement3", type=rdal_SubElementReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinedElement4: BinaryAssociation = BinaryAssociation(
    name="refinedElement4",
    ends={
        Property(name="rdal_RefineableElement6", type=rdal_ElementRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_ElementRefinement5", type=rdal_RefineableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubRequirementRefs7: BinaryAssociation = BinaryAssociation(
    name="ownedSubRequirementRefs7",
    ends={
        Property(name="rdal_SubRequirementReference", type=rdal_RequirementRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RequirementRefinement", type=rdal_SubRequirementReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subRequirements8: BinaryAssociation = BinaryAssociation(
    name="subRequirements8",
    ends={
        Property(name="rdal_AbstractRequirement", type=rdal_RequirementRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RequirementRefinement9", type=rdal_AbstractRequirement, multiplicity=Multiplicity(1, 9999))
    }
)
stakeholders22: BinaryAssociation = BinaryAssociation(
    name="stakeholders22",
    ends={
        Property(name="rdal_Stakeholder", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_AbstractContractualElement", type=rdal_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSubGoalRefs13: BinaryAssociation = BinaryAssociation(
    name="ownedSubGoalRefs13",
    ends={
        Property(name="rdal_SubGoalReference", type=rdal_GoalRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_GoalRefinement", type=rdal_SubGoalReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subGoals14: BinaryAssociation = BinaryAssociation(
    name="subGoals14",
    ends={
        Property(name="rdal_AbstractGoal", type=rdal_GoalRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_GoalRefinement15", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 9999))
    }
)
refinedGoal16: BinaryAssociation = BinaryAssociation(
    name="refinedGoal16",
    ends={
        Property(name="rdal_AbstractGoal18", type=rdal_GoalRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_GoalRefinement17", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 1))
    }
)
ownedReferencedDesignElements19: BinaryAssociation = BinaryAssociation(
    name="ownedReferencedDesignElements19",
    ends={
        Property(name="rdal_ReferencedDesignElements", type=rdal_TraceableToDesignElementsElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_TraceableToDesignElementsElement", type=rdal_ReferencedDesignElements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification20: BinaryAssociation = BinaryAssociation(
    name="specification20",
    ends={
        Property(name="rdal_Specification", type=rdal_TraceableToDesignElementsElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_TraceableToDesignElementsElement21", type=rdal_Specification, multiplicity=Multiplicity(1, 1))
    }
)
ownedRationales23: BinaryAssociation = BinaryAssociation(
    name="ownedRationales23",
    ends={
        Property(name="rdal_Rationale", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_AbstractContractualElement24", type=rdal_Rationale, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contactInformation25: BinaryAssociation = BinaryAssociation(
    name="contactInformation25",
    ends={
        Property(name="rdal_ContactInformation", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_AbstractContractualElement26", type=rdal_ContactInformation, multiplicity=Multiplicity(0, 9999))
    }
)
evolvedTo28: BinaryAssociation = BinaryAssociation(
    name="evolvedTo28",
    ends={
        Property(name="rdal_AbstractContractualElement29", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_AbstractContractualElement27", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedDroppingReasons30: BinaryAssociation = BinaryAssociation(
    name="ownedDroppingReasons30",
    ends={
        Property(name="rdal_Rationale32", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_AbstractContractualElement31", type=rdal_Rationale, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeUncertainty33: BinaryAssociation = BinaryAssociation(
    name="changeUncertainty33",
    ends={
        Property(name="rdal_Uncertainty", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_AbstractContractualElement34", type=rdal_Uncertainty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contactInformation35: BinaryAssociation = BinaryAssociation(
    name="contactInformation35",
    ends={
        Property(name="rdal_ContactInformation37", type=rdal_Stakeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Stakeholder36", type=rdal_ContactInformation, multiplicity=Multiplicity(1, 9999))
    }
)
stakeholders38: BinaryAssociation = BinaryAssociation(
    name="stakeholders38",
    ends={
        Property(name="rdal_Stakeholder40", type=rdal_Rationale, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Rationale39", type=rdal_Stakeholder, multiplicity=Multiplicity(1, 9999))
    }
)
ownedExpression41: BinaryAssociation = BinaryAssociation(
    name="ownedExpression41",
    ends={
        Property(name="rdal_Expression", type=rdal_TextualContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_TextualContractualElement", type=rdal_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedCondition42: BinaryAssociation = BinaryAssociation(
    name="ownedCondition42",
    ends={
        Property(name="rdal_Expression44", type=rdal_TextualContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_TextualContractualElement43", type=rdal_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivedFrom46: BinaryAssociation = BinaryAssociation(
    name="derivedFrom46",
    ends={
        Property(name="rdal_TextualContractualElement47", type=rdal_TextualContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_TextualContractualElement45", type=rdal_TextualContractualElement, multiplicity=Multiplicity(0, 9999))
    }
)
category48: BinaryAssociation = BinaryAssociation(
    name="category48",
    ends={
        Property(name="rdal_Category", type=rdal_TextualContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_TextualContractualElement49", type=rdal_Category, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackages50: BinaryAssociation = BinaryAssociation(
    name="ownedPackages50",
    ends={
        Property(name="RdalOrgPackage", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedContactInformation51: BinaryAssociation = BinaryAssociation(
    name="ownedContactInformation51",
    ends={
        Property(name="rdal_ContactInformation53", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification52", type=rdal_ContactInformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConflicts54: BinaryAssociation = BinaryAssociation(
    name="ownedConflicts54",
    ends={
        Property(name="rdal_Conflict", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification55", type=rdal_Conflict, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent74: BinaryAssociation = BinaryAssociation(
    name="parent74",
    ends={
        Property(name="RdalOrgPackage75", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="subPackages", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(0, 1))
    }
)
ownedSystOverview56: BinaryAssociation = BinaryAssociation(
    name="ownedSystOverview56",
    ends={
        Property(name="rdal_SystemOverview", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification57", type=rdal_SystemOverview, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraintLanguagesSpec58: BinaryAssociation = BinaryAssociation(
    name="constraintLanguagesSpec58",
    ends={
        Property(name="rdal_ConstraintLanguagesSpec", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification59", type=rdal_ConstraintLanguagesSpec, multiplicity=Multiplicity(0, 1))
    }
)
ownedActorReferences60: BinaryAssociation = BinaryAssociation(
    name="ownedActorReferences60",
    ends={
        Property(name="rdal_ActorReference", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification61", type=rdal_ActorReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryActors62: BinaryAssociation = BinaryAssociation(
    name="primaryActors62",
    ends={
        Property(name="rdal_EObject", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification63", type=rdal_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
ownedNonFuncProperties64: BinaryAssociation = BinaryAssociation(
    name="ownedNonFuncProperties64",
    ends={
        Property(name="rdal_NonFunctionalProperty", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification65", type=rdal_NonFunctionalProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStakeholders66: BinaryAssociation = BinaryAssociation(
    name="ownedStakeholders66",
    ends={
        Property(name="rdal_Stakeholder68", type=rdal_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Specification67", type=rdal_Stakeholder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification69: BinaryAssociation = BinaryAssociation(
    name="specification69",
    ends={
        Property(name="Specification", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=rdal_Specification, multiplicity=Multiplicity(1, 1))
    }
)
subPackages71: BinaryAssociation = BinaryAssociation(
    name="subPackages71",
    ends={
        Property(name="RdalOrgPackage72", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRefinements76: BinaryAssociation = BinaryAssociation(
    name="ownedRefinements76",
    ends={
        Property(name="rdal_ElementRefinement77", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RdalOrgPackage", type=rdal_ElementRefinement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedContractualElements78: BinaryAssociation = BinaryAssociation(
    name="ownedContractualElements78",
    ends={
        Property(name="rdal_TextualContractualElement80", type=rdal_RdalOrgPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RdalOrgPackage79", type=rdal_TextualContractualElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedRequirements81: BinaryAssociation = BinaryAssociation(
    name="ownedRequirements81",
    ends={
        Property(name="AbstractRequirement", type=rdal_RequirementsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=rdal_AbstractRequirement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
functionUsedIn82: BinaryAssociation = BinaryAssociation(
    name="functionUsedIn82",
    ends={
        Property(name="rdal_EObject83", type=rdal_RequirementsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RequirementsPackage", type=rdal_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ownedRequirementsRefinements84: BinaryAssociation = BinaryAssociation(
    name="ownedRequirementsRefinements84",
    ends={
        Property(name="rdal_RequirementRefinement86", type=rdal_RequirementsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_RequirementsPackage85", type=rdal_RequirementRefinement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemBoundary100: BinaryAssociation = BinaryAssociation(
    name="ownedSystemBoundary100",
    ends={
        Property(name="rdal_InteractionVariable", type=rdal_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemOverview101", type=rdal_InteractionVariable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedGoals87: BinaryAssociation = BinaryAssociation(
    name="ownedGoals87",
    ends={
        Property(name="AbstractGoal", type=rdal_GoalsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package88", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedGoalRefinements89: BinaryAssociation = BinaryAssociation(
    name="ownedGoalRefinements89",
    ends={
        Property(name="rdal_GoalRefinement90", type=rdal_GoalsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_GoalsPackage", type=rdal_GoalRefinement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedCapabilities91: BinaryAssociation = BinaryAssociation(
    name="ownedCapabilities91",
    ends={
        Property(name="rdal_Capability", type=rdal_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemOverview92", type=rdal_Capability, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
globalSystem93: BinaryAssociation = BinaryAssociation(
    name="globalSystem93",
    ends={
        Property(name="rdal_EObject95", type=rdal_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemOverview94", type=rdal_EObject, multiplicity=Multiplicity(1, 1))
    }
)
systemToBe96: BinaryAssociation = BinaryAssociation(
    name="systemToBe96",
    ends={
        Property(name="rdal_EObject98", type=rdal_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemOverview97", type=rdal_EObject, multiplicity=Multiplicity(1, 1))
    }
)
ownedContexts99: BinaryAssociation = BinaryAssociation(
    name="ownedContexts99",
    ends={
        Property(name="SystemContext", type=rdal_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="systemOverview", type=rdal_SystemContext, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
globalSystemContext102: BinaryAssociation = BinaryAssociation(
    name="globalSystemContext102",
    ends={
        Property(name="rdal_EObject103", type=rdal_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemContext", type=rdal_EObject, multiplicity=Multiplicity(1, 1))
    }
)
systemContextBoundary104: BinaryAssociation = BinaryAssociation(
    name="systemContextBoundary104",
    ends={
        Property(name="rdal_InteractionVariable106", type=rdal_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemContext105", type=rdal_InteractionVariable, multiplicity=Multiplicity(1, 9999))
    }
)
actors107: BinaryAssociation = BinaryAssociation(
    name="actors107",
    ends={
        Property(name="rdal_ActorReference109", type=rdal_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemContext108", type=rdal_ActorReference, multiplicity=Multiplicity(0, 9999))
    }
)
systemOverview110: BinaryAssociation = BinaryAssociation(
    name="systemOverview110",
    ends={
        Property(name="SystemOverview", type=rdal_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedContexts", type=rdal_SystemOverview, multiplicity=Multiplicity(0, 1))
    }
)
designVariable111: BinaryAssociation = BinaryAssociation(
    name="designVariable111",
    ends={
        Property(name="rdal_EObject112", type=rdal_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Variable", type=rdal_EObject, multiplicity=Multiplicity(1, 1))
    }
)
referencedActors113: BinaryAssociation = BinaryAssociation(
    name="referencedActors113",
    ends={
        Property(name="rdal_EObject115", type=rdal_ActorReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_ActorReference114", type=rdal_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
ownedVerifiedBy116: BinaryAssociation = BinaryAssociation(
    name="ownedVerifiedBy116",
    ends={
        Property(name="VerificationActivity", type=rdal_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements", type=rdal_VerificationActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package117: BinaryAssociation = BinaryAssociation(
    name="package117",
    ends={
        Property(name="RequirementsPackage", type=rdal_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRequirements", type=rdal_RequirementsPackage, multiplicity=Multiplicity(1, 1))
    }
)
externalRefs118: BinaryAssociation = BinaryAssociation(
    name="externalRefs118",
    ends={
        Property(name="rdal_EObject119", type=rdal_VerificationActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_VerificationActivity", type=rdal_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
requirements120: BinaryAssociation = BinaryAssociation(
    name="requirements120",
    ends={
        Property(name="AbstractRequirement121", type=rdal_VerificationActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedVerifiedBy", type=rdal_AbstractRequirement, multiplicity=Multiplicity(0, 1))
    }
)
category122: BinaryAssociation = BinaryAssociation(
    name="category122",
    ends={
        Property(name="rdal_Category124", type=rdal_VerificationActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_VerificationActivity123", type=rdal_Category, multiplicity=Multiplicity(0, 1))
    }
)
imageAssumptions125: BinaryAssociation = BinaryAssociation(
    name="imageAssumptions125",
    ends={
        Property(name="Assumption", type=rdal_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="imageRequirement", type=rdal_Assumption, multiplicity=Multiplicity(0, 9999))
    }
)
functionUsedIn126: BinaryAssociation = BinaryAssociation(
    name="functionUsedIn126",
    ends={
        Property(name="rdal_EObject127", type=rdal_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Requirement", type=rdal_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
imageRequirement128: BinaryAssociation = BinaryAssociation(
    name="imageRequirement128",
    ends={
        Property(name="Requirement", type=rdal_Assumption, multiplicity=Multiplicity(1, 1)),
        Property(name="imageAssumptions", type=rdal_Requirement, multiplicity=Multiplicity(0, 1))
    }
)
imageAssumptions130: BinaryAssociation = BinaryAssociation(
    name="imageAssumptions130",
    ends={
        Property(name="rdal_Assumption", type=rdal_Assumption, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Assumption129", type=rdal_Assumption, multiplicity=Multiplicity(0, 9999))
    }
)
conflicts131: BinaryAssociation = BinaryAssociation(
    name="conflicts131",
    ends={
        Property(name="Conflict", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=rdal_Conflict, multiplicity=Multiplicity(0, 9999))
    }
)
package132: BinaryAssociation = BinaryAssociation(
    name="package132",
    ends={
        Property(name="GoalsPackage", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedGoals", type=rdal_GoalsPackage, multiplicity=Multiplicity(1, 1))
    }
)
useCases133: BinaryAssociation = BinaryAssociation(
    name="useCases133",
    ends={
        Property(name="rdal_EObject134", type=rdal_SystemFunctionGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SystemFunctionGoal", type=rdal_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
property135: BinaryAssociation = BinaryAssociation(
    name="property135",
    ends={
        Property(name="rdal_NonFunctionalProperty136", type=rdal_QualityObjective, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_QualityObjective", type=rdal_NonFunctionalProperty, multiplicity=Multiplicity(1, 1))
    }
)
ownedSensitivity137: BinaryAssociation = BinaryAssociation(
    name="ownedSensitivity137",
    ends={
        Property(name="rdal_Sensitivity", type=rdal_QualityObjective, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_QualityObjective138", type=rdal_Sensitivity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
goal139: BinaryAssociation = BinaryAssociation(
    name="goal139",
    ends={
        Property(name="AbstractGoal140", type=rdal_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflicts", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 1))
    }
)
contractualElement141: BinaryAssociation = BinaryAssociation(
    name="contractualElement141",
    ends={
        Property(name="rdal_AbstractContractualElement143", type=rdal_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Conflict142", type=rdal_AbstractContractualElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedDesignElementRefs144: BinaryAssociation = BinaryAssociation(
    name="ownedDesignElementRefs144",
    ends={
        Property(name="DesignElementReference", type=rdal_ReferencedDesignElements, multiplicity=Multiplicity(1, 1)),
        Property(name="parent145", type=rdal_DesignElementReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
queryExpression152: BinaryAssociation = BinaryAssociation(
    name="queryExpression152",
    ends={
        Property(name="rdal_RefQueryCollectedDesignElements", type=rdal_FormalLanguageExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="rdal_FormalLanguageExpression", type=rdal_RefQueryCollectedDesignElements, multiplicity=Multiplicity(1, 1))
    }
)
designElement146: BinaryAssociation = BinaryAssociation(
    name="designElement146",
    ends={
        Property(name="rdal_EObject147", type=rdal_DesignElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_DesignElementReference", type=rdal_EObject, multiplicity=Multiplicity(1, 1))
    }
)
parent148: BinaryAssociation = BinaryAssociation(
    name="parent148",
    ends={
        Property(name="ReferencedDesignElements", type=rdal_DesignElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedDesignElementRefs", type=rdal_ReferencedDesignElements, multiplicity=Multiplicity(1, 1))
    }
)
parentTraceableElement149: BinaryAssociation = BinaryAssociation(
    name="parentTraceableElement149",
    ends={
        Property(name="rdal_TraceableToDesignElementsElement151", type=rdal_DesignElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_DesignElementReference150", type=rdal_TraceableToDesignElementsElement, multiplicity=Multiplicity(1, 1))
    }
)
specifications153: BinaryAssociation = BinaryAssociation(
    name="specifications153",
    ends={
        Property(name="rdal_Specification154", type=rdal_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_Trace", type=rdal_Specification, multiplicity=Multiplicity(0, 9999))
    }
)
designProperty155: BinaryAssociation = BinaryAssociation(
    name="designProperty155",
    ends={
        Property(name="rdal_EObject157", type=rdal_NonFunctionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_NonFunctionalProperty156", type=rdal_EObject, multiplicity=Multiplicity(0, 1))
    }
)
referencedElement158: BinaryAssociation = BinaryAssociation(
    name="referencedElement158",
    ends={
        Property(name="rdal_RefineableElement160", type=rdal_SubElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SubElementReference159", type=rdal_RefineableElement, multiplicity=Multiplicity(1, 1))
    }
)
requirement161: BinaryAssociation = BinaryAssociation(
    name="requirement161",
    ends={
        Property(name="rdal_AbstractRequirement163", type=rdal_SubRequirementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SubRequirementReference162", type=rdal_AbstractRequirement, multiplicity=Multiplicity(1, 1))
    }
)
goal164: BinaryAssociation = BinaryAssociation(
    name="goal164",
    ends={
        Property(name="rdal_AbstractGoal166", type=rdal_SubGoalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rdal_SubGoalReference165", type=rdal_AbstractGoal, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdal_ElementRefinement_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_ElementRefinement)
gen_rdal_RequirementRefinement_ElementRefinement = Generalization(general=ElementRefinement, specific=rdal_RequirementRefinement)
gen_rdal_RequirementRefinement_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_RequirementRefinement)
gen_rdal_RequirementRefinement_VerifiableElement = Generalization(general=VerifiableElement, specific=rdal_RequirementRefinement)
gen_rdal_GoalRefinement_ElementRefinement = Generalization(general=ElementRefinement, specific=rdal_GoalRefinement)
gen_rdal_GoalRefinement_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_GoalRefinement)
gen_rdal_TraceableToDesignElementsElement_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_TraceableToDesignElementsElement)
gen_rdal_AbstractContractualElement_TraceableToDesignElementsElement = Generalization(general=TraceableToDesignElementsElement, specific=rdal_AbstractContractualElement)
gen_rdal_ContactInformation_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_ContactInformation)
gen_rdal_Uncertainty_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_Uncertainty)
gen_rdal_Stakeholder_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_Stakeholder)
gen_rdal_Rationale_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_Rationale)
gen_rdal_TextualContractualElement_AbstractContractualElement = Generalization(general=AbstractContractualElement, specific=rdal_TextualContractualElement)
gen_rdal_Specification_AbstractContractualElement = Generalization(general=AbstractContractualElement, specific=rdal_Specification)
gen_rdal_Specification_VerifiableElement = Generalization(general=VerifiableElement, specific=rdal_Specification)
gen_rdal_Specification_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_Specification)
gen_rdal_RdalOrgPackage_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_RdalOrgPackage)
gen_rdal_GoalsPackage_RdalOrgPackage = Generalization(general=RdalOrgPackage, specific=rdal_GoalsPackage)
gen_rdal_GoalsPackage_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_GoalsPackage)
gen_rdal_RequirementsPackage_RdalOrgPackage = Generalization(general=RdalOrgPackage, specific=rdal_RequirementsPackage)
gen_rdal_RequirementsPackage_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_RequirementsPackage)
gen_rdal_RequirementsPackage_VerifiableElement = Generalization(general=VerifiableElement, specific=rdal_RequirementsPackage)
gen_rdal_SystemOverview_AbstractContractualElement = Generalization(general=AbstractContractualElement, specific=rdal_SystemOverview)
gen_rdal_ActorReference_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_ActorReference)
gen_rdal_Capability_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_Capability)
gen_rdal_SystemContext_AbstractContractualElement = Generalization(general=AbstractContractualElement, specific=rdal_SystemContext)
gen_rdal_Variable_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_Variable)
gen_rdal_InteractionVariable_Variable = Generalization(general=Variable, specific=rdal_InteractionVariable)
gen_rdal_Requirement_AbstractRequirement = Generalization(general=AbstractRequirement, specific=rdal_Requirement)
gen_rdal_AbstractRequirement_TextualContractualElement = Generalization(general=TextualContractualElement, specific=rdal_AbstractRequirement)
gen_rdal_AbstractRequirement_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_AbstractRequirement)
gen_rdal_AbstractRequirement_VerifiableElement = Generalization(general=VerifiableElement, specific=rdal_AbstractRequirement)
gen_rdal_VerificationActivity_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_VerificationActivity)
gen_rdal_NonFunctionalGoal_AbstractGoal = Generalization(general=AbstractGoal, specific=rdal_NonFunctionalGoal)
gen_rdal_Requirement_RefineableElement = Generalization(general=RefineableElement, specific=rdal_Requirement)
gen_rdal_Assumption_AbstractRequirement = Generalization(general=AbstractRequirement, specific=rdal_Assumption)
gen_rdal_AbstractGoal_TextualContractualElement = Generalization(general=TextualContractualElement, specific=rdal_AbstractGoal)
gen_rdal_AbstractGoal_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_AbstractGoal)
gen_rdal_AbstractGoal_RefineableElement = Generalization(general=RefineableElement, specific=rdal_AbstractGoal)
gen_rdal_SystemFunctionGoal_AbstractGoal = Generalization(general=AbstractGoal, specific=rdal_SystemFunctionGoal)
gen_rdal_DesignElementReference_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_DesignElementReference)
gen_rdal_QualityObjective_NonFunctionalGoal = Generalization(general=NonFunctionalGoal, specific=rdal_QualityObjective)
gen_rdal_Conflict_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_Conflict)
gen_rdal_ReferencedDesignElements_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_ReferencedDesignElements)
gen_rdal_VerifiableDesignElementRef_DesignElementReference = Generalization(general=DesignElementReference, specific=rdal_VerifiableDesignElementRef)
gen_rdal_VerifiableDesignElementRef_VerifiableElement = Generalization(general=VerifiableElement, specific=rdal_VerifiableDesignElementRef)
gen_rdal_SatisfiableDesignElementRef_DesignElementReference = Generalization(general=DesignElementReference, specific=rdal_SatisfiableDesignElementRef)
gen_rdal_SatisfiableDesignElementRef_SatisfiableElement = Generalization(general=SatisfiableElement, specific=rdal_SatisfiableDesignElementRef)
gen_rdal_PrioritizedSatDesignElementRef_SatisfiableDesignElementRef = Generalization(general=SatisfiableDesignElementRef, specific=rdal_PrioritizedSatDesignElementRef)
gen_rdal_SystOverviewDesignElemRef_DesignElementReference = Generalization(general=DesignElementReference, specific=rdal_SystOverviewDesignElemRef)
gen_rdal_SystContextDesignElemRef_DesignElementReference = Generalization(general=DesignElementReference, specific=rdal_SystContextDesignElemRef)
gen_rdal_RefManuallySelectedDesignElements_ReferencedDesignElements = Generalization(general=ReferencedDesignElements, specific=rdal_RefManuallySelectedDesignElements)
gen_rdal_RefQueryCollectedDesignElements_ReferencedDesignElements = Generalization(general=ReferencedDesignElements, specific=rdal_RefQueryCollectedDesignElements)
gen_rdal_Sensitivity_TraceableToDesignElementsElement = Generalization(general=TraceableToDesignElementsElement, specific=rdal_Sensitivity)
gen_rdal_TraceDesignElementRef_DesignElementReference = Generalization(general=DesignElementReference, specific=rdal_TraceDesignElementRef)
gen_rdal_TraceDesignElementRef_RequirementsCoverageData = Generalization(general=RequirementsCoverageData, specific=rdal_TraceDesignElementRef)
gen_rdal_TraceDesignElementRef_VerifiableElement = Generalization(general=VerifiableElement, specific=rdal_TraceDesignElementRef)
gen_rdal_Trace_ReferencedDesignElements = Generalization(general=ReferencedDesignElements, specific=rdal_Trace)
gen_rdal_RequirementsCoverageData_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_RequirementsCoverageData)
gen_rdal_NonFunctionalProperty_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_NonFunctionalProperty)
gen_rdal_SubElementReference_IdentifiedElement = Generalization(general=IdentifiedElement, specific=rdal_SubElementReference)
gen_rdal_SubRequirementReference_SubElementReference = Generalization(general=SubElementReference, specific=rdal_SubRequirementReference)
gen_rdal_SubGoalReference_SubElementReference = Generalization(general=SubElementReference, specific=rdal_SubGoalReference)

# Domain Model
domain_model = DomainModel(
    name="rdal",
    types={rdal_IdentifiedElement, rdal_UserProperty, rdal_ElementRefinement, IdentifiedElement, rdal_RefineableElement, rdal_SubElementReference, rdal_RequirementRefinement, ElementRefinement, SatisfiableElement, VerifiableElement, rdal_SubRequirementReference, rdal_AbstractRequirement, rdal_Stakeholder, rdal_GoalRefinement, rdal_SubGoalReference, rdal_AbstractGoal, rdal_TraceableToDesignElementsElement, rdal_ReferencedDesignElements, rdal_Specification, rdal_AbstractContractualElement, TraceableToDesignElementsElement, rdal_Rationale, rdal_ContactInformation, rdal_Uncertainty, rdal_TextualContractualElement, AbstractContractualElement, rdal_Expression, rdal_Category, rdal_SystemOverview, rdal_SatisfiableElement, rdal_VerifiableElement, rdal_RdalOrgPackage, rdal_Conflict, rdal_ConstraintLanguagesSpec, rdal_ActorReference, rdal_EObject, rdal_NonFunctionalProperty, rdal_GoalsPackage, rdal_RequirementsPackage, RdalOrgPackage, rdal_InteractionVariable, rdal_Capability, rdal_SystemContext, rdal_Variable, Variable, rdal_Requirement, AbstractRequirement, TextualContractualElement, rdal_VerificationActivity, rdal_NonFunctionalGoal, RefineableElement, rdal_Assumption, rdal_SystemFunctionGoal, AbstractGoal, rdal_QualityObjective, NonFunctionalGoal, rdal_Sensitivity, rdal_DesignElementReference, rdal_VerifiableDesignElementRef, DesignElementReference, rdal_SatisfiableDesignElementRef, rdal_PrioritizedSatDesignElementRef, SatisfiableDesignElementRef, rdal_SystOverviewDesignElemRef, rdal_SystContextDesignElemRef, rdal_RefManuallySelectedDesignElements, ReferencedDesignElements, rdal_RefQueryCollectedDesignElements, rdal_FormalLanguageExpression, rdal_TraceDesignElementRef, RequirementsCoverageData, rdal_Trace, rdal_RequirementsCoverageData, SubElementReference, InteractionVariableType, AggregationType, Modality},
    associations={ownedUserProperties0, refinedRequirement10, subElements1, ownedSubElementRefs2, refinedElement4, ownedSubRequirementRefs7, subRequirements8, stakeholders22, ownedSubGoalRefs13, subGoals14, refinedGoal16, ownedReferencedDesignElements19, specification20, ownedRationales23, contactInformation25, evolvedTo28, ownedDroppingReasons30, changeUncertainty33, contactInformation35, stakeholders38, ownedExpression41, ownedCondition42, derivedFrom46, category48, ownedPackages50, ownedContactInformation51, ownedConflicts54, parent74, ownedSystOverview56, constraintLanguagesSpec58, ownedActorReferences60, primaryActors62, ownedNonFuncProperties64, ownedStakeholders66, specification69, subPackages71, ownedRefinements76, ownedContractualElements78, ownedRequirements81, functionUsedIn82, ownedRequirementsRefinements84, ownedSystemBoundary100, ownedGoals87, ownedGoalRefinements89, ownedCapabilities91, globalSystem93, systemToBe96, ownedContexts99, globalSystemContext102, systemContextBoundary104, actors107, systemOverview110, designVariable111, referencedActors113, ownedVerifiedBy116, package117, externalRefs118, requirements120, category122, imageAssumptions125, functionUsedIn126, imageRequirement128, imageAssumptions130, conflicts131, package132, useCases133, property135, ownedSensitivity137, goal139, contractualElement141, ownedDesignElementRefs144, queryExpression152, designElement146, parent148, parentTraceableElement149, specifications153, designProperty155, referencedElement158, requirement161, goal164},
    generalizations={gen_rdal_ElementRefinement_IdentifiedElement, gen_rdal_RequirementRefinement_ElementRefinement, gen_rdal_RequirementRefinement_SatisfiableElement, gen_rdal_RequirementRefinement_VerifiableElement, gen_rdal_GoalRefinement_ElementRefinement, gen_rdal_GoalRefinement_SatisfiableElement, gen_rdal_TraceableToDesignElementsElement_IdentifiedElement, gen_rdal_AbstractContractualElement_TraceableToDesignElementsElement, gen_rdal_ContactInformation_IdentifiedElement, gen_rdal_Uncertainty_IdentifiedElement, gen_rdal_Stakeholder_IdentifiedElement, gen_rdal_Rationale_IdentifiedElement, gen_rdal_TextualContractualElement_AbstractContractualElement, gen_rdal_Specification_AbstractContractualElement, gen_rdal_Specification_VerifiableElement, gen_rdal_Specification_SatisfiableElement, gen_rdal_RdalOrgPackage_IdentifiedElement, gen_rdal_GoalsPackage_RdalOrgPackage, gen_rdal_GoalsPackage_SatisfiableElement, gen_rdal_RequirementsPackage_RdalOrgPackage, gen_rdal_RequirementsPackage_SatisfiableElement, gen_rdal_RequirementsPackage_VerifiableElement, gen_rdal_SystemOverview_AbstractContractualElement, gen_rdal_ActorReference_IdentifiedElement, gen_rdal_Capability_IdentifiedElement, gen_rdal_SystemContext_AbstractContractualElement, gen_rdal_Variable_IdentifiedElement, gen_rdal_InteractionVariable_Variable, gen_rdal_Requirement_AbstractRequirement, gen_rdal_AbstractRequirement_TextualContractualElement, gen_rdal_AbstractRequirement_SatisfiableElement, gen_rdal_AbstractRequirement_VerifiableElement, gen_rdal_VerificationActivity_IdentifiedElement, gen_rdal_NonFunctionalGoal_AbstractGoal, gen_rdal_Requirement_RefineableElement, gen_rdal_Assumption_AbstractRequirement, gen_rdal_AbstractGoal_TextualContractualElement, gen_rdal_AbstractGoal_SatisfiableElement, gen_rdal_AbstractGoal_RefineableElement, gen_rdal_SystemFunctionGoal_AbstractGoal, gen_rdal_DesignElementReference_IdentifiedElement, gen_rdal_QualityObjective_NonFunctionalGoal, gen_rdal_Conflict_IdentifiedElement, gen_rdal_ReferencedDesignElements_IdentifiedElement, gen_rdal_VerifiableDesignElementRef_DesignElementReference, gen_rdal_VerifiableDesignElementRef_VerifiableElement, gen_rdal_SatisfiableDesignElementRef_DesignElementReference, gen_rdal_SatisfiableDesignElementRef_SatisfiableElement, gen_rdal_PrioritizedSatDesignElementRef_SatisfiableDesignElementRef, gen_rdal_SystOverviewDesignElemRef_DesignElementReference, gen_rdal_SystContextDesignElemRef_DesignElementReference, gen_rdal_RefManuallySelectedDesignElements_ReferencedDesignElements, gen_rdal_RefQueryCollectedDesignElements_ReferencedDesignElements, gen_rdal_Sensitivity_TraceableToDesignElementsElement, gen_rdal_TraceDesignElementRef_DesignElementReference, gen_rdal_TraceDesignElementRef_RequirementsCoverageData, gen_rdal_TraceDesignElementRef_VerifiableElement, gen_rdal_Trace_ReferencedDesignElements, gen_rdal_RequirementsCoverageData_IdentifiedElement, gen_rdal_NonFunctionalProperty_IdentifiedElement, gen_rdal_SubElementReference_IdentifiedElement, gen_rdal_SubRequirementReference_SubElementReference, gen_rdal_SubGoalReference_SubElementReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)