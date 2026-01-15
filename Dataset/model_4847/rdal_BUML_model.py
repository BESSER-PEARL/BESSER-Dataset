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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="In"),
			EnumerationLiteral(name="Out"),
			EnumerationLiteral(name="InOut")
    }
)

RiskKind: Enumeration = Enumeration(
    name="RiskKind",
    literals={
            EnumerationLiteral(name="High"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Low")
    }
)

VerificationMethod: Enumeration = Enumeration(
    name="VerificationMethod",
    literals={
            EnumerationLiteral(name="Analysis"),
			EnumerationLiteral(name="Demonstration"),
			EnumerationLiteral(name="Inspection"),
			EnumerationLiteral(name="Test")
    }
)

AssumptionType: Enumeration = Enumeration(
    name="AssumptionType",
    literals={
            EnumerationLiteral(name="Organizational"),
			EnumerationLiteral(name="Managerial"),
			EnumerationLiteral(name="Technical")
    }
)

AgregationType: Enumeration = Enumeration(
    name="AgregationType",
    literals={
            EnumerationLiteral(name="Composition"),
			EnumerationLiteral(name="Alternative")
    }
)

VariableType: Enumeration = Enumeration(
    name="VariableType",
    literals={
            EnumerationLiteral(name="Monitored"),
			EnumerationLiteral(name="Controlled"),
			EnumerationLiteral(name="Both")
    }
)

ContainerType: Enumeration = Enumeration(
    name="ContainerType",
    literals={
            EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Or")
    }
)

# Classes
core_IdentifiedElement = Class(name="core::IdentifiedElement", is_abstract=True)
core_Rationale = Class(name="core::Rationale")
core_Actor = Class(name="core::Actor")
core_Expression = Class(name="core::Expression")
core_ContractualElement = Class(name="core::ContractualElement", is_abstract=True)
IdentifiedElement = Class(name="IdentifiedElement")
core_Uncertainty = Class(name="core::Uncertainty")
core_StakeHolder = Class(name="core::StakeHolder")
core_EObject = Class(name="core::EObject")
core_Category = Class(name="core::Category")
core_ReferencedModelElements = Class(name="core::ReferencedModelElements", is_abstract=True)
core_Goal = Class(name="core::Goal")
core_SystemContext = Class(name="core::SystemContext")
core_Variable = Class(name="core::Variable")
core_VerifiableElement = Class(name="core::VerifiableElement", is_abstract=True)
ContractualElement = Class(name="ContractualElement")
core_Specification = Class(name="core::Specification")
VerifiableElement = Class(name="VerifiableElement")
core_SystemOverview = Class(name="core::SystemOverview")
core_RequirementsGroup = Class(name="core::RequirementsGroup")
core_VerificationActivity = Class(name="core::VerificationActivity")
core_Conflict = Class(name="core::Conflict")
core_ConstraintLanguagesSpecification = Class(name="core::ConstraintLanguagesSpecification")
core_AbstractRequirement = Class(name="core::AbstractRequirement", is_abstract=True)
core_Interaction = Class(name="core::Interaction")
Actor = Class(name="Actor")
core_Requirement = Class(name="core::Requirement")
AbstractRequirement = Class(name="AbstractRequirement")
core_Assumption = Class(name="core::Assumption")
core_RequirementsContainer = Class(name="core::RequirementsContainer")
ModelElementReference = Class(name="ModelElementReference")
RequirementsCoverageData = Class(name="RequirementsCoverageData")
core_RequirementsCoverageData = Class(name="core::RequirementsCoverageData")
core_RefExpressionCollectedModelElements = Class(name="core::RefExpressionCollectedModelElements")
ReferencedModelElements = Class(name="ReferencedModelElements")
core_FormalLanguageExpression = Class(name="core::FormalLanguageExpression")
core_RefUserSelectedModelElements = Class(name="core::RefUserSelectedModelElements")
core_ModelElementReference = Class(name="core::ModelElementReference")
core_Trace = Class(name="core::Trace")
core_TraceModelElementReference = Class(name="core::TraceModelElementReference")
core_RefDerivedModelElements = Class(name="core::RefDerivedModelElements")

# core_IdentifiedElement class attributes and methods
core_IdentifiedElement_id: Property = Property(name="id", type=StringType)
core_IdentifiedElement_name: Property = Property(name="name", type=StringType)
core_IdentifiedElement_description: Property = Property(name="description", type=StringType)
core_IdentifiedElement.attributes={core_IdentifiedElement_name, core_IdentifiedElement_description, core_IdentifiedElement_id}

# core_Rationale class attributes and methods

# core_Actor class attributes and methods
core_Actor_address: Property = Property(name="address", type=StringType)
core_Actor_email: Property = Property(name="email", type=StringType)
core_Actor_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
core_Actor.attributes={core_Actor_email, core_Actor_address, core_Actor_phoneNumber}

# core_Expression class attributes and methods

# core_ContractualElement class attributes and methods
core_ContractualElement_droppingReason: Property = Property(name="droppingReason", type=StringType)
core_ContractualElement_satisfactionLevel: Property = Property(name="satisfactionLevel", type=StringType)
core_ContractualElement_timeCriticality: Property = Property(name="timeCriticality", type=StringType)
core_ContractualElement_sources: Property = Property(name="sources", type=StringType)
core_ContractualElement_originDate: Property = Property(name="originDate", type=StringType)
core_ContractualElement_scheduleDate: Property = Property(name="scheduleDate", type=StringType)
core_ContractualElement_dropped: Property = Property(name="dropped", type=BooleanType)
core_ContractualElement.attributes={core_ContractualElement_scheduleDate, core_ContractualElement_droppingReason, core_ContractualElement_timeCriticality, core_ContractualElement_originDate, core_ContractualElement_dropped, core_ContractualElement_satisfactionLevel, core_ContractualElement_sources}

# IdentifiedElement class attributes and methods

# core_Uncertainty class attributes and methods
core_Uncertainty_volatility: Property = Property(name="volatility", type=StringType)
core_Uncertainty_costsImpact: Property = Property(name="costsImpact", type=StringType)
core_Uncertainty_scheduleImpact: Property = Property(name="scheduleImpact", type=StringType)
core_Uncertainty_precedence: Property = Property(name="precedence", type=StringType)
core_Uncertainty_riskIndex: Property = Property(name="riskIndex", type=StringType)
core_Uncertainty_propRiskIndex: Property = Property(name="propRiskIndex", type=StringType)
core_Uncertainty_maturityIndex: Property = Property(name="maturityIndex", type=StringType)
core_Uncertainty.attributes={core_Uncertainty_volatility, core_Uncertainty_riskIndex, core_Uncertainty_maturityIndex, core_Uncertainty_propRiskIndex, core_Uncertainty_scheduleImpact, core_Uncertainty_precedence, core_Uncertainty_costsImpact}

# core_StakeHolder class attributes and methods

# core_EObject class attributes and methods

# core_Category class attributes and methods

# core_ReferencedModelElements class attributes and methods
core_ReferencedModelElements_agregationType: Property = Property(name="agregationType", type=StringType)
core_ReferencedModelElements.attributes={core_ReferencedModelElements_agregationType}

# core_Goal class attributes and methods
core_Goal_priority: Property = Property(name="priority", type=StringType)
core_Goal.attributes={core_Goal_priority}

# core_SystemContext class attributes and methods

# core_Variable class attributes and methods
core_Variable_type: Property = Property(name="type", type=StringType)
core_Variable.attributes={core_Variable_type}

# core_VerifiableElement class attributes and methods
core_VerifiableElement_verified: Property = Property(name="verified", type=StringType)
core_VerifiableElement.attributes={core_VerifiableElement_verified}

# ContractualElement class attributes and methods

# core_Specification class attributes and methods
core_Specification_version: Property = Property(name="version", type=StringType)
core_Specification.attributes={core_Specification_version}

# VerifiableElement class attributes and methods

# core_SystemOverview class attributes and methods
core_SystemOverview_purpose: Property = Property(name="purpose", type=StringType)
core_SystemOverview_capabilities: Property = Property(name="capabilities", type=StringType)
core_SystemOverview.attributes={core_SystemOverview_purpose, core_SystemOverview_capabilities}

# core_RequirementsGroup class attributes and methods

# core_VerificationActivity class attributes and methods
core_VerificationActivity_verificationMethod: Property = Property(name="verificationMethod", type=StringType)
core_VerificationActivity_passed: Property = Property(name="passed", type=BooleanType)
core_VerificationActivity.attributes={core_VerificationActivity_passed, core_VerificationActivity_verificationMethod}

# core_Conflict class attributes and methods
core_Conflict_degree: Property = Property(name="degree", type=StringType)
core_Conflict.attributes={core_Conflict_degree}

# core_ConstraintLanguagesSpecification class attributes and methods

# core_AbstractRequirement class attributes and methods
core_AbstractRequirement_risk: Property = Property(name="risk", type=StringType)
core_AbstractRequirement.attributes={core_AbstractRequirement_risk}

# core_Interaction class attributes and methods
core_Interaction_direction: Property = Property(name="direction", type=StringType)
core_Interaction.attributes={core_Interaction_direction}

# Actor class attributes and methods

# core_Requirement class attributes and methods

# AbstractRequirement class attributes and methods

# core_Assumption class attributes and methods
core_Assumption_type: Property = Property(name="type", type=StringType)
core_Assumption.attributes={core_Assumption_type}

# core_RequirementsContainer class attributes and methods
core_RequirementsContainer_type: Property = Property(name="type", type=StringType)
core_RequirementsContainer.attributes={core_RequirementsContainer_type}

# ModelElementReference class attributes and methods

# RequirementsCoverageData class attributes and methods

# core_RequirementsCoverageData class attributes and methods
core_RequirementsCoverageData_nbRequirements: Property = Property(name="nbRequirements", type=IntegerType)
core_RequirementsCoverageData_verificationLevel: Property = Property(name="verificationLevel", type=StringType)
core_RequirementsCoverageData.attributes={core_RequirementsCoverageData_verificationLevel, core_RequirementsCoverageData_nbRequirements}

# core_RefExpressionCollectedModelElements class attributes and methods

# ReferencedModelElements class attributes and methods

# core_FormalLanguageExpression class attributes and methods

# core_RefUserSelectedModelElements class attributes and methods

# core_ModelElementReference class attributes and methods
core_ModelElementReference_weight: Property = Property(name="weight", type=StringType)
core_ModelElementReference_verifies: Property = Property(name="verifies", type=StringType)
core_ModelElementReference_satisfactionLevel: Property = Property(name="satisfactionLevel", type=StringType)
core_ModelElementReference_reason: Property = Property(name="reason", type=StringType)
core_ModelElementReference.attributes={core_ModelElementReference_satisfactionLevel, core_ModelElementReference_reason, core_ModelElementReference_verifies, core_ModelElementReference_weight}

# core_Trace class attributes and methods
core_Trace_m_modelElementReference: Method = Method(name="modelElementReference", parameters={Parameter(name='modelElement')}, type=StringType)
core_Trace.methods={core_Trace_m_modelElementReference}

# core_TraceModelElementReference class attributes and methods
core_TraceModelElementReference_container: Property = Property(name="container", type=BooleanType)
core_TraceModelElementReference_m_merge: Method = Method(name="merge", parameters={Parameter(name='modelElementReference')})
core_TraceModelElementReference.attributes={core_TraceModelElementReference_container}
core_TraceModelElementReference.methods={core_TraceModelElementReference_m_merge}

# core_RefDerivedModelElements class attributes and methods

# Relationships
rationales17: BinaryAssociation = BinaryAssociation(
    name="rationales17",
    ends={
        Property(name="Rationale", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contract", type=core_Rationale, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contactInformation18: BinaryAssociation = BinaryAssociation(
    name="contactInformation18",
    ends={
        Property(name="core_Actor", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement19", type=core_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="core_Expression", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement21", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition22: BinaryAssociation = BinaryAssociation(
    name="condition22",
    ends={
        Property(name="core_Expression24", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement23", type=core_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modes25: BinaryAssociation = BinaryAssociation(
    name="modes25",
    ends={
        Property(name="core_EObject27", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement26", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
changeUncertainty0: BinaryAssociation = BinaryAssociation(
    name="changeUncertainty0",
    ends={
        Property(name="core_Uncertainty", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement", type=core_Uncertainty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stakeholders1: BinaryAssociation = BinaryAssociation(
    name="stakeholders1",
    ends={
        Property(name="StakeHolder", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contractualElements", type=core_StakeHolder, multiplicity=Multiplicity(0, 9999))
    }
)
evolvedTo3: BinaryAssociation = BinaryAssociation(
    name="evolvedTo3",
    ends={
        Property(name="core_ContractualElement4", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement2", type=core_ContractualElement, multiplicity=Multiplicity(0, 9999))
    }
)
tracedTo5: BinaryAssociation = BinaryAssociation(
    name="tracedTo5",
    ends={
        Property(name="core_EObject", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement6", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
category7: BinaryAssociation = BinaryAssociation(
    name="category7",
    ends={
        Property(name="core_Category", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement8", type=core_Category, multiplicity=Multiplicity(0, 1))
    }
)
satisfiedBy9: BinaryAssociation = BinaryAssociation(
    name="satisfiedBy9",
    ends={
        Property(name="core_ReferencedModelElements", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement10", type=core_ReferencedModelElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
agents11: BinaryAssociation = BinaryAssociation(
    name="agents11",
    ends={
        Property(name="core_EObject13", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement12", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
derivedFrom14: BinaryAssociation = BinaryAssociation(
    name="derivedFrom14",
    ends={
        Property(name="core_EObject16", type=core_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ContractualElement15", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
goals45: BinaryAssociation = BinaryAssociation(
    name="goals45",
    ends={
        Property(name="core_Goal", type=core_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemOverview46", type=core_Goal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
systemToBe47: BinaryAssociation = BinaryAssociation(
    name="systemToBe47",
    ends={
        Property(name="core_EObject49", type=core_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemOverview48", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
contexts50: BinaryAssociation = BinaryAssociation(
    name="contexts50",
    ends={
        Property(name="core_SystemContext", type=core_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemOverview51", type=core_SystemContext, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
systemBoundary52: BinaryAssociation = BinaryAssociation(
    name="systemBoundary52",
    ends={
        Property(name="core_Variable", type=core_SystemOverview, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemOverview53", type=core_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
globalSystem54: BinaryAssociation = BinaryAssociation(
    name="globalSystem54",
    ends={
        Property(name="core_EObject56", type=core_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemContext55", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
actors57: BinaryAssociation = BinaryAssociation(
    name="actors57",
    ends={
        Property(name="core_Actor59", type=core_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemContext58", type=core_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
actors28: BinaryAssociation = BinaryAssociation(
    name="actors28",
    ends={
        Property(name="core_Actor29", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification", type=core_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systOverview30: BinaryAssociation = BinaryAssociation(
    name="systOverview30",
    ends={
        Property(name="core_SystemOverview", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification31", type=core_SystemOverview, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requirementGroups32: BinaryAssociation = BinaryAssociation(
    name="requirementGroups32",
    ends={
        Property(name="RequirementsGroup", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=core_RequirementsGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
verificationActivities33: BinaryAssociation = BinaryAssociation(
    name="verificationActivities33",
    ends={
        Property(name="core_VerificationActivity", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification34", type=core_VerificationActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conflicts35: BinaryAssociation = BinaryAssociation(
    name="conflicts35",
    ends={
        Property(name="core_Conflict", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification36", type=core_Conflict, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraintLanguagesSpecification37: BinaryAssociation = BinaryAssociation(
    name="constraintLanguagesSpecification37",
    ends={
        Property(name="core_ConstraintLanguagesSpecification", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification38", type=core_ConstraintLanguagesSpecification, multiplicity=Multiplicity(1, 1))
    }
)
specifies39: BinaryAssociation = BinaryAssociation(
    name="specifies39",
    ends={
        Property(name="core_EObject41", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification40", type=core_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
primaryActors42: BinaryAssociation = BinaryAssociation(
    name="primaryActors42",
    ends={
        Property(name="core_EObject44", type=core_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Specification43", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
rationales77: BinaryAssociation = BinaryAssociation(
    name="rationales77",
    ends={
        Property(name="core_Rationale", type=core_StakeHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="core_StakeHolder", type=core_Rationale, multiplicity=Multiplicity(0, 9999))
    }
)
requirements78: BinaryAssociation = BinaryAssociation(
    name="requirements78",
    ends={
        Property(name="AbstractRequirement", type=core_RequirementsGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=core_AbstractRequirement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specification79: BinaryAssociation = BinaryAssociation(
    name="specification79",
    ends={
        Property(name="Specification", type=core_RequirementsGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementGroups", type=core_Specification, multiplicity=Multiplicity(1, 1))
    }
)
systemBoundary60: BinaryAssociation = BinaryAssociation(
    name="systemBoundary60",
    ends={
        Property(name="core_Variable62", type=core_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemContext61", type=core_Variable, multiplicity=Multiplicity(1, 9999))
    }
)
systemModes63: BinaryAssociation = BinaryAssociation(
    name="systemModes63",
    ends={
        Property(name="core_EObject65", type=core_SystemContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_SystemContext64", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
images66: BinaryAssociation = BinaryAssociation(
    name="images66",
    ends={
        Property(name="core_EObject68", type=core_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Actor67", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
interactions69: BinaryAssociation = BinaryAssociation(
    name="interactions69",
    ends={
        Property(name="core_Interaction", type=core_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Actor70", type=core_Interaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity71: BinaryAssociation = BinaryAssociation(
    name="entity71",
    ends={
        Property(name="core_EObject73", type=core_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Interaction72", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
conflicts74: BinaryAssociation = BinaryAssociation(
    name="conflicts74",
    ends={
        Property(name="Conflict", type=core_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goals", type=core_Conflict, multiplicity=Multiplicity(0, 9999))
    }
)
goals75: BinaryAssociation = BinaryAssociation(
    name="goals75",
    ends={
        Property(name="Goal", type=core_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflicts", type=core_Goal, multiplicity=Multiplicity(2, 2))
    }
)
contractualElements76: BinaryAssociation = BinaryAssociation(
    name="contractualElements76",
    ends={
        Property(name="ContractualElement", type=core_StakeHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="stakeholders", type=core_ContractualElement, multiplicity=Multiplicity(1, 9999))
    }
)
requirement105: BinaryAssociation = BinaryAssociation(
    name="requirement105",
    ends={
        Property(name="AbstractRequirement106", type=core_VerificationActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="verifiedBy", type=core_AbstractRequirement, multiplicity=Multiplicity(0, 1))
    }
)
externalRef107: BinaryAssociation = BinaryAssociation(
    name="externalRef107",
    ends={
        Property(name="core_EObject109", type=core_VerificationActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="core_VerificationActivity108", type=core_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="core_Expression112", type=core_VerificationActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="core_VerificationActivity111", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containedRequirements81: BinaryAssociation = BinaryAssociation(
    name="containedRequirements81",
    ends={
        Property(name="core_AbstractRequirement", type=core_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_AbstractRequirement80", type=core_AbstractRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
verifiedBy82: BinaryAssociation = BinaryAssociation(
    name="verifiedBy82",
    ends={
        Property(name="VerificationActivity", type=core_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement", type=core_VerificationActivity, multiplicity=Multiplicity(0, 9999))
    }
)
group83: BinaryAssociation = BinaryAssociation(
    name="group83",
    ends={
        Property(name="RequirementsGroup84", type=core_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements", type=core_RequirementsGroup, multiplicity=Multiplicity(1, 1))
    }
)
assignedVariable85: BinaryAssociation = BinaryAssociation(
    name="assignedVariable85",
    ends={
        Property(name="core_Variable87", type=core_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_AbstractRequirement86", type=core_Variable, multiplicity=Multiplicity(0, 1))
    }
)
conditionVariables88: BinaryAssociation = BinaryAssociation(
    name="conditionVariables88",
    ends={
        Property(name="core_Variable90", type=core_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_AbstractRequirement89", type=core_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
refinedBY92: BinaryAssociation = BinaryAssociation(
    name="refinedBY92",
    ends={
        Property(name="core_Requirement", type=core_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Requirement91", type=core_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
assumptions93: BinaryAssociation = BinaryAssociation(
    name="assumptions93",
    ends={
        Property(name="Assumption", type=core_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements94", type=core_Assumption, multiplicity=Multiplicity(0, 9999))
    }
)
imageAssumption95: BinaryAssociation = BinaryAssociation(
    name="imageAssumption95",
    ends={
        Property(name="Assumption96", type=core_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="imageRequirement", type=core_Assumption, multiplicity=Multiplicity(0, 1))
    }
)
derivations98: BinaryAssociation = BinaryAssociation(
    name="derivations98",
    ends={
        Property(name="core_Requirement99", type=core_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Requirement97", type=core_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
subRequirements100: BinaryAssociation = BinaryAssociation(
    name="subRequirements100",
    ends={
        Property(name="core_RequirementsContainer", type=core_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Requirement101", type=core_RequirementsContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requirements102: BinaryAssociation = BinaryAssociation(
    name="requirements102",
    ends={
        Property(name="Requirement", type=core_Assumption, multiplicity=Multiplicity(1, 1)),
        Property(name="assumptions", type=core_Requirement, multiplicity=Multiplicity(0, 1))
    }
)
imageRequirement103: BinaryAssociation = BinaryAssociation(
    name="imageRequirement103",
    ends={
        Property(name="Requirement104", type=core_Assumption, multiplicity=Multiplicity(1, 1)),
        Property(name="imageAssumption", type=core_Requirement, multiplicity=Multiplicity(0, 1))
    }
)
feature120: BinaryAssociation = BinaryAssociation(
    name="feature120",
    ends={
        Property(name="core_EObject122", type=core_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Variable121", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
queryExpression113: BinaryAssociation = BinaryAssociation(
    name="queryExpression113",
    ends={
        Property(name="core_FormalLanguageExpression", type=core_RefExpressionCollectedModelElements, multiplicity=Multiplicity(1, 1)),
        Property(name="core_RefExpressionCollectedModelElements", type=core_FormalLanguageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelElementReferences114: BinaryAssociation = BinaryAssociation(
    name="modelElementReferences114",
    ends={
        Property(name="ModelElementReference", type=core_ReferencedModelElements, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=core_ModelElementReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElement115: BinaryAssociation = BinaryAssociation(
    name="modelElement115",
    ends={
        Property(name="core_EObject116", type=core_ModelElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ModelElementReference", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
parent117: BinaryAssociation = BinaryAssociation(
    name="parent117",
    ends={
        Property(name="ReferencedModelElements", type=core_ModelElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElementReferences", type=core_ReferencedModelElements, multiplicity=Multiplicity(1, 1))
    }
)
specifications118: BinaryAssociation = BinaryAssociation(
    name="specifications118",
    ends={
        Property(name="core_Specification119", type=core_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Trace", type=core_Specification, multiplicity=Multiplicity(0, 9999))
    }
)
contract123: BinaryAssociation = BinaryAssociation(
    name="contract123",
    ends={
        Property(name="ContractualElement124", type=core_Rationale, multiplicity=Multiplicity(1, 1)),
        Property(name="rationales", type=core_ContractualElement, multiplicity=Multiplicity(1, 1))
    }
)
requirement125: BinaryAssociation = BinaryAssociation(
    name="requirement125",
    ends={
        Property(name="core_Requirement127", type=core_RequirementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="core_RequirementsContainer126", type=core_Requirement, multiplicity=Multiplicity(0, 1))
    }
)
requirements128: BinaryAssociation = BinaryAssociation(
    name="requirements128",
    ends={
        Property(name="core_Requirement130", type=core_RequirementsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="core_RequirementsContainer129", type=core_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_core_Uncertainty_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_Uncertainty)
gen_core_ContractualElement_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_ContractualElement)
gen_core_SystemContext_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_SystemContext)
gen_core_VerifiableElement_ContractualElement = Generalization(general=ContractualElement, specific=core_VerifiableElement)
gen_core_Specification_VerifiableElement = Generalization(general=VerifiableElement, specific=core_Specification)
gen_core_SystemOverview_ContractualElement = Generalization(general=ContractualElement, specific=core_SystemOverview)
gen_core_RequirementsGroup_VerifiableElement = Generalization(general=VerifiableElement, specific=core_RequirementsGroup)
gen_core_AbstractRequirement_VerifiableElement = Generalization(general=VerifiableElement, specific=core_AbstractRequirement)
gen_core_Actor_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_Actor)
gen_core_Interaction_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_Interaction)
gen_core_Goal_ContractualElement = Generalization(general=ContractualElement, specific=core_Goal)
gen_core_Conflict_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_Conflict)
gen_core_StakeHolder_Actor = Generalization(general=Actor, specific=core_StakeHolder)
gen_core_VerificationActivity_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_VerificationActivity)
gen_core_Requirement_AbstractRequirement = Generalization(general=AbstractRequirement, specific=core_Requirement)
gen_core_Assumption_AbstractRequirement = Generalization(general=AbstractRequirement, specific=core_Assumption)
gen_core_TraceModelElementReference_ModelElementReference = Generalization(general=ModelElementReference, specific=core_TraceModelElementReference)
gen_core_TraceModelElementReference_RequirementsCoverageData = Generalization(general=RequirementsCoverageData, specific=core_TraceModelElementReference)
gen_core_RequirementsCoverageData_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_RequirementsCoverageData)
gen_core_Variable_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_Variable)
gen_core_RefExpressionCollectedModelElements_ReferencedModelElements = Generalization(general=ReferencedModelElements, specific=core_RefExpressionCollectedModelElements)
gen_core_RefUserSelectedModelElements_ReferencedModelElements = Generalization(general=ReferencedModelElements, specific=core_RefUserSelectedModelElements)
gen_core_ReferencedModelElements_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_ReferencedModelElements)
gen_core_ModelElementReference_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_ModelElementReference)
gen_core_Trace_ReferencedModelElements = Generalization(general=ReferencedModelElements, specific=core_Trace)
gen_core_RefDerivedModelElements_ReferencedModelElements = Generalization(general=ReferencedModelElements, specific=core_RefDerivedModelElements)
gen_core_Rationale_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_Rationale)
gen_core_RequirementsContainer_IdentifiedElement = Generalization(general=IdentifiedElement, specific=core_RequirementsContainer)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_IdentifiedElement, core_Rationale, core_Actor, core_Expression, core_ContractualElement, IdentifiedElement, core_Uncertainty, core_StakeHolder, core_EObject, core_Category, core_ReferencedModelElements, core_Goal, core_SystemContext, core_Variable, core_VerifiableElement, ContractualElement, core_Specification, VerifiableElement, core_SystemOverview, core_RequirementsGroup, core_VerificationActivity, core_Conflict, core_ConstraintLanguagesSpecification, core_AbstractRequirement, core_Interaction, Actor, core_Requirement, AbstractRequirement, core_Assumption, core_RequirementsContainer, ModelElementReference, RequirementsCoverageData, core_RequirementsCoverageData, core_RefExpressionCollectedModelElements, ReferencedModelElements, core_FormalLanguageExpression, core_RefUserSelectedModelElements, core_ModelElementReference, core_Trace, core_TraceModelElementReference, core_RefDerivedModelElements, Direction, RiskKind, VerificationMethod, AssumptionType, AgregationType, VariableType, ContainerType},
    associations={rationales17, contactInformation18, expression20, condition22, modes25, changeUncertainty0, stakeholders1, evolvedTo3, tracedTo5, category7, satisfiedBy9, agents11, derivedFrom14, goals45, systemToBe47, contexts50, systemBoundary52, globalSystem54, actors57, actors28, systOverview30, requirementGroups32, verificationActivities33, conflicts35, constraintLanguagesSpecification37, specifies39, primaryActors42, rationales77, requirements78, specification79, systemBoundary60, systemModes63, images66, interactions69, entity71, conflicts74, goals75, contractualElements76, requirement105, externalRef107, expression110, containedRequirements81, verifiedBy82, group83, assignedVariable85, conditionVariables88, refinedBY92, assumptions93, imageAssumption95, derivations98, subRequirements100, requirements102, imageRequirement103, feature120, queryExpression113, modelElementReferences114, modelElement115, parent117, specifications118, contract123, requirement125, requirements128},
    generalizations={gen_core_Uncertainty_IdentifiedElement, gen_core_ContractualElement_IdentifiedElement, gen_core_SystemContext_IdentifiedElement, gen_core_VerifiableElement_ContractualElement, gen_core_Specification_VerifiableElement, gen_core_SystemOverview_ContractualElement, gen_core_RequirementsGroup_VerifiableElement, gen_core_AbstractRequirement_VerifiableElement, gen_core_Actor_IdentifiedElement, gen_core_Interaction_IdentifiedElement, gen_core_Goal_ContractualElement, gen_core_Conflict_IdentifiedElement, gen_core_StakeHolder_Actor, gen_core_VerificationActivity_IdentifiedElement, gen_core_Requirement_AbstractRequirement, gen_core_Assumption_AbstractRequirement, gen_core_TraceModelElementReference_ModelElementReference, gen_core_TraceModelElementReference_RequirementsCoverageData, gen_core_RequirementsCoverageData_IdentifiedElement, gen_core_Variable_IdentifiedElement, gen_core_RefExpressionCollectedModelElements_ReferencedModelElements, gen_core_RefUserSelectedModelElements_ReferencedModelElements, gen_core_ReferencedModelElements_IdentifiedElement, gen_core_ModelElementReference_IdentifiedElement, gen_core_Trace_ReferencedModelElements, gen_core_RefDerivedModelElements_ReferencedModelElements, gen_core_Rationale_IdentifiedElement, gen_core_RequirementsContainer_IdentifiedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)