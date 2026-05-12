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
reqSpec_ReqSpec = Class(name="reqSpec_ReqSpec")
reqSpec_EObject = Class(name="reqSpec_EObject")
reqSpec_GlobalConstants = Class(name="reqSpec_GlobalConstants")
reqSpec_ComponentClassifier = Class(name="reqSpec_ComponentClassifier")
reqSpec_NamedElement = Class(name="reqSpec_NamedElement")
reqSpec_Category = Class(name="reqSpec_Category")
reqSpec_Description = Class(name="reqSpec_Description")
reqSpec_WhenCondition = Class(name="reqSpec_WhenCondition")
reqSpec_Rationale = Class(name="reqSpec_Rationale")
reqSpec_AVariableDeclaration = Class(name="reqSpec_AVariableDeclaration")
reqSpec_ContractualElement = Class(name="reqSpec_ContractualElement")
reqSpec_ExternalDocument = Class(name="reqSpec_ExternalDocument")
reqSpec_Goal = Class(name="reqSpec_Goal")
reqSpec_ReqRoot = Class(name="reqSpec_ReqRoot")
reqSpec_StakeholderGoals = Class(name="reqSpec_StakeholderGoals")
ReqRoot = Class(name="ReqRoot")
reqSpec_Uncertainty = Class(name="reqSpec_Uncertainty")
reqSpec_Requirement = Class(name="reqSpec_Requirement")
reqSpec_ReqDocument = Class(name="reqSpec_ReqDocument")
reqSpec_DocumentSection = Class(name="reqSpec_DocumentSection")
reqSpec_RequirementSet = Class(name="reqSpec_RequirementSet")
ContractualElement = Class(name="ContractualElement")
reqSpec_Stakeholder = Class(name="reqSpec_Stakeholder")
reqSpec_ReqPredicate = Class(name="reqSpec_ReqPredicate")
reqSpec_IncludeGlobalRequirement = Class(name="reqSpec_IncludeGlobalRequirement")
reqSpec_Mode = Class(name="reqSpec_Mode")
reqSpec_ErrorBehaviorState = Class(name="reqSpec_ErrorBehaviorState")
reqSpec_PropertyExpression = Class(name="reqSpec_PropertyExpression")
reqSpec_ValuePredicate = Class(name="reqSpec_ValuePredicate")
reqSpec_DesiredValue = Class(name="reqSpec_DesiredValue")
reqSpec_AVariableReference = Class(name="reqSpec_AVariableReference")
reqSpec_InformalPredicate = Class(name="reqSpec_InformalPredicate")
ReqPredicate = Class(name="ReqPredicate")
reqSpec_Predicate = Class(name="reqSpec_Predicate")
reqSpec_SystemRequirementSet = Class(name="reqSpec_SystemRequirementSet")
RequirementSet = Class(name="RequirementSet")
reqSpec_GlobalRequirementSet = Class(name="reqSpec_GlobalRequirementSet")

# reqSpec_ReqSpec class attributes and methods

# reqSpec_EObject class attributes and methods

# reqSpec_GlobalConstants class attributes and methods
reqSpec_GlobalConstants_name: Property = Property(name="name", type=StringType)
reqSpec_GlobalConstants.attributes={reqSpec_GlobalConstants_name}

# reqSpec_ComponentClassifier class attributes and methods

# reqSpec_NamedElement class attributes and methods

# reqSpec_Category class attributes and methods

# reqSpec_Description class attributes and methods

# reqSpec_WhenCondition class attributes and methods

# reqSpec_Rationale class attributes and methods

# reqSpec_AVariableDeclaration class attributes and methods

# reqSpec_ContractualElement class attributes and methods
reqSpec_ContractualElement_name: Property = Property(name="name", type=StringType)
reqSpec_ContractualElement_title: Property = Property(name="title", type=StringType)
reqSpec_ContractualElement_targetDescription: Property = Property(name="targetDescription", type=StringType)
reqSpec_ContractualElement_dropped: Property = Property(name="dropped", type=BooleanType)
reqSpec_ContractualElement_dropRationale: Property = Property(name="dropRationale", type=StringType)
reqSpec_ContractualElement_issues: Property = Property(name="issues", type=StringType)
reqSpec_ContractualElement.attributes={reqSpec_ContractualElement_dropRationale, reqSpec_ContractualElement_title, reqSpec_ContractualElement_dropped, reqSpec_ContractualElement_issues, reqSpec_ContractualElement_targetDescription, reqSpec_ContractualElement_name}

# reqSpec_ExternalDocument class attributes and methods
reqSpec_ExternalDocument_docReference: Property = Property(name="docReference", type=StringType)
reqSpec_ExternalDocument_docFragment: Property = Property(name="docFragment", type=StringType)
reqSpec_ExternalDocument.attributes={reqSpec_ExternalDocument_docFragment, reqSpec_ExternalDocument_docReference}

# reqSpec_Goal class attributes and methods

# reqSpec_ReqRoot class attributes and methods
reqSpec_ReqRoot_name: Property = Property(name="name", type=StringType)
reqSpec_ReqRoot_title: Property = Property(name="title", type=StringType)
reqSpec_ReqRoot_issues: Property = Property(name="issues", type=StringType)
reqSpec_ReqRoot.attributes={reqSpec_ReqRoot_title, reqSpec_ReqRoot_issues, reqSpec_ReqRoot_name}

# reqSpec_StakeholderGoals class attributes and methods
reqSpec_StakeholderGoals_componentCategory: Property = Property(name="componentCategory", type=StringType)
reqSpec_StakeholderGoals.attributes={reqSpec_StakeholderGoals_componentCategory}

# ReqRoot class attributes and methods

# reqSpec_Uncertainty class attributes and methods

# reqSpec_Requirement class attributes and methods
reqSpec_Requirement_exceptionText: Property = Property(name="exceptionText", type=StringType)
reqSpec_Requirement_componentCategory: Property = Property(name="componentCategory", type=StringType)
reqSpec_Requirement_connections: Property = Property(name="connections", type=BooleanType)
reqSpec_Requirement.attributes={reqSpec_Requirement_connections, reqSpec_Requirement_componentCategory, reqSpec_Requirement_exceptionText}

# reqSpec_ReqDocument class attributes and methods

# reqSpec_DocumentSection class attributes and methods
reqSpec_DocumentSection_label: Property = Property(name="label", type=StringType)
reqSpec_DocumentSection_title: Property = Property(name="title", type=StringType)
reqSpec_DocumentSection.attributes={reqSpec_DocumentSection_label, reqSpec_DocumentSection_title}

# reqSpec_RequirementSet class attributes and methods

# ContractualElement class attributes and methods

# reqSpec_Stakeholder class attributes and methods

# reqSpec_ReqPredicate class attributes and methods

# reqSpec_IncludeGlobalRequirement class attributes and methods
reqSpec_IncludeGlobalRequirement_componentCategory: Property = Property(name="componentCategory", type=StringType)
reqSpec_IncludeGlobalRequirement_self: Property = Property(name="self", type=BooleanType)
reqSpec_IncludeGlobalRequirement.attributes={reqSpec_IncludeGlobalRequirement_self, reqSpec_IncludeGlobalRequirement_componentCategory}

# reqSpec_Mode class attributes and methods

# reqSpec_ErrorBehaviorState class attributes and methods

# reqSpec_PropertyExpression class attributes and methods

# reqSpec_ValuePredicate class attributes and methods

# reqSpec_DesiredValue class attributes and methods
reqSpec_DesiredValue_upto: Property = Property(name="upto", type=BooleanType)
reqSpec_DesiredValue.attributes={reqSpec_DesiredValue_upto}

# reqSpec_AVariableReference class attributes and methods

# reqSpec_InformalPredicate class attributes and methods
reqSpec_InformalPredicate_description: Property = Property(name="description", type=StringType)
reqSpec_InformalPredicate.attributes={reqSpec_InformalPredicate_description}

# ReqPredicate class attributes and methods

# reqSpec_Predicate class attributes and methods

# reqSpec_SystemRequirementSet class attributes and methods

# RequirementSet class attributes and methods

# reqSpec_GlobalRequirementSet class attributes and methods

# Relationships
parts0: BinaryAssociation = BinaryAssociation(
    name="parts0",
    ends={
        Property(name="reqSpec_EObject", type=reqSpec_ReqSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ReqSpec", type=reqSpec_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target2: BinaryAssociation = BinaryAssociation(
    name="target2",
    ends={
        Property(name="reqSpec_ComponentClassifier", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement", type=reqSpec_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
targetElement3: BinaryAssociation = BinaryAssociation(
    name="targetElement3",
    ends={
        Property(name="reqSpec_NamedElement", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement4", type=reqSpec_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
category5: BinaryAssociation = BinaryAssociation(
    name="category5",
    ends={
        Property(name="reqSpec_Category", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement6", type=reqSpec_Category, multiplicity=Multiplicity(0, 9999))
    }
)
description7: BinaryAssociation = BinaryAssociation(
    name="description7",
    ends={
        Property(name="reqSpec_Description", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement8", type=reqSpec_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants9: BinaryAssociation = BinaryAssociation(
    name="constants9",
    ends={
        Property(name="reqSpec_AVariableDeclaration11", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement10", type=reqSpec_AVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whencondition12: BinaryAssociation = BinaryAssociation(
    name="whencondition12",
    ends={
        Property(name="reqSpec_WhenCondition", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement13", type=reqSpec_WhenCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rationale14: BinaryAssociation = BinaryAssociation(
    name="rationale14",
    ends={
        Property(name="reqSpec_Rationale", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement15", type=reqSpec_Rationale, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants1: BinaryAssociation = BinaryAssociation(
    name="constants1",
    ends={
        Property(name="reqSpec_AVariableDeclaration", type=reqSpec_GlobalConstants, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_GlobalConstants", type=reqSpec_AVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docReference20: BinaryAssociation = BinaryAssociation(
    name="docReference20",
    ends={
        Property(name="reqSpec_ExternalDocument", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement21", type=reqSpec_ExternalDocument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goalReference22: BinaryAssociation = BinaryAssociation(
    name="goalReference22",
    ends={
        Property(name="reqSpec_Goal", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement23", type=reqSpec_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
description24: BinaryAssociation = BinaryAssociation(
    name="description24",
    ends={
        Property(name="reqSpec_Description25", type=reqSpec_ReqRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ReqRoot", type=reqSpec_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docReference26: BinaryAssociation = BinaryAssociation(
    name="docReference26",
    ends={
        Property(name="reqSpec_ExternalDocument28", type=reqSpec_ReqRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ReqRoot27", type=reqSpec_ExternalDocument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeUncertainty16: BinaryAssociation = BinaryAssociation(
    name="changeUncertainty16",
    ends={
        Property(name="reqSpec_Uncertainty", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement17", type=reqSpec_Uncertainty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants34: BinaryAssociation = BinaryAssociation(
    name="constants34",
    ends={
        Property(name="reqSpec_StakeholderGoals35", type=reqSpec_AVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="reqSpec_AVariableDeclaration36", type=reqSpec_StakeholderGoals, multiplicity=Multiplicity(1, 1))
    }
)
evolvesReference18: BinaryAssociation = BinaryAssociation(
    name="evolvesReference18",
    ends={
        Property(name="reqSpec_Requirement", type=reqSpec_ContractualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ContractualElement19", type=reqSpec_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
goals37: BinaryAssociation = BinaryAssociation(
    name="goals37",
    ends={
        Property(name="reqSpec_Goal39", type=reqSpec_StakeholderGoals, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_StakeholderGoals38", type=reqSpec_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content40: BinaryAssociation = BinaryAssociation(
    name="content40",
    ends={
        Property(name="reqSpec_EObject41", type=reqSpec_ReqDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ReqDocument", type=reqSpec_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description42: BinaryAssociation = BinaryAssociation(
    name="description42",
    ends={
        Property(name="reqSpec_Description43", type=reqSpec_DocumentSection, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_DocumentSection", type=reqSpec_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content44: BinaryAssociation = BinaryAssociation(
    name="content44",
    ends={
        Property(name="reqSpec_EObject46", type=reqSpec_DocumentSection, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_DocumentSection45", type=reqSpec_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importConstants47: BinaryAssociation = BinaryAssociation(
    name="importConstants47",
    ends={
        Property(name="reqSpec_GlobalConstants48", type=reqSpec_RequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_RequirementSet", type=reqSpec_GlobalConstants, multiplicity=Multiplicity(0, 9999))
    }
)
constants49: BinaryAssociation = BinaryAssociation(
    name="constants49",
    ends={
        Property(name="reqSpec_AVariableDeclaration51", type=reqSpec_RequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_RequirementSet50", type=reqSpec_AVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="reqSpec_ComponentClassifier30", type=reqSpec_StakeholderGoals, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_StakeholderGoals", type=reqSpec_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
importConstants31: BinaryAssociation = BinaryAssociation(
    name="importConstants31",
    ends={
        Property(name="reqSpec_GlobalConstants33", type=reqSpec_StakeholderGoals, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_StakeholderGoals32", type=reqSpec_GlobalConstants, multiplicity=Multiplicity(0, 9999))
    }
)
refinesReference62: BinaryAssociation = BinaryAssociation(
    name="refinesReference62",
    ends={
        Property(name="reqSpec_Goal63", type=reqSpec_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Goal61", type=reqSpec_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
conflictsReference65: BinaryAssociation = BinaryAssociation(
    name="conflictsReference65",
    ends={
        Property(name="reqSpec_Goal66", type=reqSpec_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Goal64", type=reqSpec_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
stakeholderReference67: BinaryAssociation = BinaryAssociation(
    name="stakeholderReference67",
    ends={
        Property(name="reqSpec_Stakeholder", type=reqSpec_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Goal68", type=reqSpec_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
computes69: BinaryAssociation = BinaryAssociation(
    name="computes69",
    ends={
        Property(name="reqSpec_AVariableDeclaration71", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement70", type=reqSpec_AVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predicate72: BinaryAssociation = BinaryAssociation(
    name="predicate72",
    ends={
        Property(name="reqSpec_ReqPredicate", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement73", type=reqSpec_ReqPredicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception74: BinaryAssociation = BinaryAssociation(
    name="exception74",
    ends={
        Property(name="reqSpec_EObject76", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement75", type=reqSpec_EObject, multiplicity=Multiplicity(0, 1))
    }
)
refinesReference78: BinaryAssociation = BinaryAssociation(
    name="refinesReference78",
    ends={
        Property(name="reqSpec_Requirement79", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement77", type=reqSpec_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
computes52: BinaryAssociation = BinaryAssociation(
    name="computes52",
    ends={
        Property(name="reqSpec_AVariableDeclaration54", type=reqSpec_RequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_RequirementSet53", type=reqSpec_AVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirements55: BinaryAssociation = BinaryAssociation(
    name="requirements55",
    ends={
        Property(name="reqSpec_Requirement57", type=reqSpec_RequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_RequirementSet56", type=reqSpec_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stakeholderGoals58: BinaryAssociation = BinaryAssociation(
    name="stakeholderGoals58",
    ends={
        Property(name="reqSpec_ReqRoot60", type=reqSpec_RequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_RequirementSet59", type=reqSpec_ReqRoot, multiplicity=Multiplicity(0, 9999))
    }
)
developmentStakeholder86: BinaryAssociation = BinaryAssociation(
    name="developmentStakeholder86",
    ends={
        Property(name="reqSpec_Stakeholder88", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement87", type=reqSpec_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
requirementReference90: BinaryAssociation = BinaryAssociation(
    name="requirementReference90",
    ends={
        Property(name="reqSpec_Requirement91", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement89", type=reqSpec_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
include92: BinaryAssociation = BinaryAssociation(
    name="include92",
    ends={
        Property(name="reqSpec_EObject93", type=reqSpec_IncludeGlobalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_IncludeGlobalRequirement", type=reqSpec_EObject, multiplicity=Multiplicity(0, 1))
    }
)
inMode94: BinaryAssociation = BinaryAssociation(
    name="inMode94",
    ends={
        Property(name="reqSpec_Mode", type=reqSpec_WhenCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_WhenCondition95", type=reqSpec_Mode, multiplicity=Multiplicity(0, 9999))
    }
)
inErrorState96: BinaryAssociation = BinaryAssociation(
    name="inErrorState96",
    ends={
        Property(name="reqSpec_ErrorBehaviorState", type=reqSpec_WhenCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_WhenCondition97", type=reqSpec_ErrorBehaviorState, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesReference81: BinaryAssociation = BinaryAssociation(
    name="decomposesReference81",
    ends={
        Property(name="reqSpec_Requirement82", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement80", type=reqSpec_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
inheritsReference84: BinaryAssociation = BinaryAssociation(
    name="inheritsReference84",
    ends={
        Property(name="reqSpec_Requirement85", type=reqSpec_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Requirement83", type=reqSpec_Requirement, multiplicity=Multiplicity(0, 1))
    }
)
xpression102: BinaryAssociation = BinaryAssociation(
    name="xpression102",
    ends={
        Property(name="reqSpec_PropertyExpression103", type=reqSpec_ValuePredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ValuePredicate", type=reqSpec_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
desiredValue104: BinaryAssociation = BinaryAssociation(
    name="desiredValue104",
    ends={
        Property(name="reqSpec_DesiredValue", type=reqSpec_ValuePredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_ValuePredicate105", type=reqSpec_DesiredValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition98: BinaryAssociation = BinaryAssociation(
    name="condition98",
    ends={
        Property(name="reqSpec_PropertyExpression", type=reqSpec_WhenCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_WhenCondition99", type=reqSpec_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
desired106: BinaryAssociation = BinaryAssociation(
    name="desired106",
    ends={
        Property(name="reqSpec_AVariableReference", type=reqSpec_DesiredValue, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_DesiredValue107", type=reqSpec_AVariableReference, multiplicity=Multiplicity(0, 1))
    }
)
xpression100: BinaryAssociation = BinaryAssociation(
    name="xpression100",
    ends={
        Property(name="reqSpec_PropertyExpression101", type=reqSpec_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_Predicate", type=reqSpec_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value108: BinaryAssociation = BinaryAssociation(
    name="value108",
    ends={
        Property(name="reqSpec_PropertyExpression110", type=reqSpec_DesiredValue, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_DesiredValue109", type=reqSpec_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target111: BinaryAssociation = BinaryAssociation(
    name="target111",
    ends={
        Property(name="reqSpec_ComponentClassifier112", type=reqSpec_SystemRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_SystemRequirementSet", type=reqSpec_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
include113: BinaryAssociation = BinaryAssociation(
    name="include113",
    ends={
        Property(name="reqSpec_IncludeGlobalRequirement115", type=reqSpec_SystemRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reqSpec_SystemRequirementSet114", type=reqSpec_IncludeGlobalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_reqSpec_StakeholderGoals_ReqRoot = Generalization(general=ReqRoot, specific=reqSpec_StakeholderGoals)
gen_reqSpec_ReqDocument_ReqRoot = Generalization(general=ReqRoot, specific=reqSpec_ReqDocument)
gen_reqSpec_RequirementSet_ReqRoot = Generalization(general=ReqRoot, specific=reqSpec_RequirementSet)
gen_reqSpec_Goal_ContractualElement = Generalization(general=ContractualElement, specific=reqSpec_Goal)
gen_reqSpec_Requirement_ContractualElement = Generalization(general=ContractualElement, specific=reqSpec_Requirement)
gen_reqSpec_ValuePredicate_ReqPredicate = Generalization(general=ReqPredicate, specific=reqSpec_ValuePredicate)
gen_reqSpec_InformalPredicate_ReqPredicate = Generalization(general=ReqPredicate, specific=reqSpec_InformalPredicate)
gen_reqSpec_Predicate_ReqPredicate = Generalization(general=ReqPredicate, specific=reqSpec_Predicate)
gen_reqSpec_SystemRequirementSet_RequirementSet = Generalization(general=RequirementSet, specific=reqSpec_SystemRequirementSet)
gen_reqSpec_GlobalRequirementSet_RequirementSet = Generalization(general=RequirementSet, specific=reqSpec_GlobalRequirementSet)

# Domain Model
domain_model = DomainModel(
    name="reqSpec",
    types={reqSpec_ReqSpec, reqSpec_EObject, reqSpec_GlobalConstants, reqSpec_ComponentClassifier, reqSpec_NamedElement, reqSpec_Category, reqSpec_Description, reqSpec_WhenCondition, reqSpec_Rationale, reqSpec_AVariableDeclaration, reqSpec_ContractualElement, reqSpec_ExternalDocument, reqSpec_Goal, reqSpec_ReqRoot, reqSpec_StakeholderGoals, ReqRoot, reqSpec_Uncertainty, reqSpec_Requirement, reqSpec_ReqDocument, reqSpec_DocumentSection, reqSpec_RequirementSet, ContractualElement, reqSpec_Stakeholder, reqSpec_ReqPredicate, reqSpec_IncludeGlobalRequirement, reqSpec_Mode, reqSpec_ErrorBehaviorState, reqSpec_PropertyExpression, reqSpec_ValuePredicate, reqSpec_DesiredValue, reqSpec_AVariableReference, reqSpec_InformalPredicate, ReqPredicate, reqSpec_Predicate, reqSpec_SystemRequirementSet, RequirementSet, reqSpec_GlobalRequirementSet},
    associations={parts0, target2, targetElement3, category5, description7, constants9, whencondition12, rationale14, constants1, docReference20, goalReference22, description24, docReference26, changeUncertainty16, constants34, evolvesReference18, goals37, content40, description42, content44, importConstants47, constants49, target29, importConstants31, refinesReference62, conflictsReference65, stakeholderReference67, computes69, predicate72, exception74, refinesReference78, computes52, requirements55, stakeholderGoals58, developmentStakeholder86, requirementReference90, include92, inMode94, inErrorState96, decomposesReference81, inheritsReference84, xpression102, desiredValue104, condition98, desired106, xpression100, value108, target111, include113},
    generalizations={gen_reqSpec_StakeholderGoals_ReqRoot, gen_reqSpec_ReqDocument_ReqRoot, gen_reqSpec_RequirementSet_ReqRoot, gen_reqSpec_Goal_ContractualElement, gen_reqSpec_Requirement_ContractualElement, gen_reqSpec_ValuePredicate_ReqPredicate, gen_reqSpec_InformalPredicate_ReqPredicate, gen_reqSpec_Predicate_ReqPredicate, gen_reqSpec_SystemRequirementSet_RequirementSet, gen_reqSpec_GlobalRequirementSet_RequirementSet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)