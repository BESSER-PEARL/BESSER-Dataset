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
GoalType: Enumeration = Enumeration(
    name="GoalType",
    literals={
            EnumerationLiteral(name="BUSINESS_GOAL"),
			EnumerationLiteral(name="PRODUCT_GOAL"),
			EnumerationLiteral(name="CUSTOMER_GOAL"),
			EnumerationLiteral(name="END_USER_GOAL")
    }
)

GoalReferenceType: Enumeration = Enumeration(
    name="GoalReferenceType",
    literals={
            EnumerationLiteral(name="PLUS_PLUS"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="MINUS_MINUS")
    }
)

# Classes
Goal = Class(name="Goal")
urml_URMLDiagram = Class(name="urml_URMLDiagram")
MEDiagram = Class(name="MEDiagram")
urml_StakeholderRole = Class(name="urml_StakeholderRole")
NonDomainElement = Class(name="NonDomainElement")
urml_SetEntry = Class(name="urml_SetEntry")
urml_UrmlModelElement = Class(name="urml_UrmlModelElement", is_abstract=True)
UnicaseModelElement = Class(name="UnicaseModelElement")
urml_Stakeholder = Class(name="urml_Stakeholder")
UrmlModelElement = Class(name="UrmlModelElement")
urml_UrmlProjectSettings = Class(name="urml_UrmlProjectSettings")
urml_goal_Goal = Class(name="urml_goal_Goal")
goal_urml_Stakeholder = Class(name="goal_urml_Stakeholder")
urml_EClass = Class(name="urml_EClass")
urml_EStructuralFeature = Class(name="urml_EStructuralFeature")
urml_PhaseSetEntry = Class(name="urml_PhaseSetEntry")
urml_Phase = Class(name="urml_Phase")
urml_goal_GoalReference = Class(name="urml_goal_GoalReference")
AssociationClassElement = Class(name="AssociationClassElement")
AbstractFeature = Class(name="AbstractFeature")
ApplicationDomainUseCase = Class(name="ApplicationDomainUseCase")
GoalReference = Class(name="GoalReference")
FunctionalRequirement = Class(name="FunctionalRequirement")
urml_requirement_NonFunctionalRequirement = Class(name="urml_requirement_NonFunctionalRequirement")
urml_requirement_Requirement = Class(name="urml_requirement_Requirement", is_abstract=True)
Mitigation = Class(name="Mitigation")
Service = Class(name="Service")
urml_requirement_FunctionalRequirement = Class(name="urml_requirement_FunctionalRequirement")
Requirement = Class(name="Requirement")
urml_usecase_SolutionDomainUseCase = Class(name="urml_usecase_SolutionDomainUseCase")
urml_usecase_Actor = Class(name="urml_usecase_Actor")
Asset = Class(name="Asset")
urml_service_Service = Class(name="urml_service_Service")
NonFunctionalRequirement = Class(name="NonFunctionalRequirement")
urml_usecase_UseCase = Class(name="urml_usecase_UseCase", is_abstract=True)
Step = Class(name="Step")
Actor = Class(name="Actor")
urml_usecase_ApplicationDomainUseCase = Class(name="urml_usecase_ApplicationDomainUseCase")
UseCase = Class(name="UseCase")
urml_danger_Mitigation = Class(name="urml_danger_Mitigation", is_abstract=True)
urml_danger_Asset = Class(name="urml_danger_Asset", is_abstract=True)
Danger = Class(name="Danger")
urml_danger_Danger = Class(name="urml_danger_Danger")
urml_danger_ProceduralMitigation = Class(name="urml_danger_ProceduralMitigation")
urml_feature_AbstractFeature = Class(name="urml_feature_AbstractFeature", is_abstract=True)
SolutionDomainUseCase = Class(name="SolutionDomainUseCase")
urml_feature_VariationPointInstance = Class(name="urml_feature_VariationPointInstance")
VariationPoint = Class(name="VariationPoint")
VariationPointInstance = Class(name="VariationPointInstance")
urml_feature_Feature = Class(name="urml_feature_Feature")
Product = Class(name="Product")
urml_feature_VariationPoint = Class(name="urml_feature_VariationPoint")
urml_feature_Product = Class(name="urml_feature_Product")
Feature = Class(name="Feature")

# Goal class attributes and methods

# urml_URMLDiagram class attributes and methods

# MEDiagram class attributes and methods

# urml_StakeholderRole class attributes and methods

# NonDomainElement class attributes and methods

# urml_SetEntry class attributes and methods

# urml_UrmlModelElement class attributes and methods
urml_UrmlModelElement_reviewed: Property = Property(name="reviewed", type=BooleanType)
urml_UrmlModelElement.attributes={urml_UrmlModelElement_reviewed}

# UnicaseModelElement class attributes and methods

# urml_Stakeholder class attributes and methods

# UrmlModelElement class attributes and methods

# urml_UrmlProjectSettings class attributes and methods

# urml_goal_Goal class attributes and methods
urml_goal_Goal_soft: Property = Property(name="soft", type=BooleanType)
urml_goal_Goal_type: Property = Property(name="type", type=StringType)
urml_goal_Goal.attributes={urml_goal_Goal_soft, urml_goal_Goal_type}

# goal_urml_Stakeholder class attributes and methods

# urml_EClass class attributes and methods

# urml_EStructuralFeature class attributes and methods

# urml_PhaseSetEntry class attributes and methods

# urml_Phase class attributes and methods

# urml_goal_GoalReference class attributes and methods
urml_goal_GoalReference_weight: Property = Property(name="weight", type=StringType)
urml_goal_GoalReference.attributes={urml_goal_GoalReference_weight}

# AssociationClassElement class attributes and methods

# AbstractFeature class attributes and methods

# ApplicationDomainUseCase class attributes and methods

# GoalReference class attributes and methods

# FunctionalRequirement class attributes and methods

# urml_requirement_NonFunctionalRequirement class attributes and methods

# urml_requirement_Requirement class attributes and methods
urml_requirement_Requirement_terminal: Property = Property(name="terminal", type=BooleanType)
urml_requirement_Requirement.attributes={urml_requirement_Requirement_terminal}

# Mitigation class attributes and methods

# Service class attributes and methods

# urml_requirement_FunctionalRequirement class attributes and methods

# Requirement class attributes and methods

# urml_usecase_SolutionDomainUseCase class attributes and methods

# urml_usecase_Actor class attributes and methods

# Asset class attributes and methods

# urml_service_Service class attributes and methods

# NonFunctionalRequirement class attributes and methods

# urml_usecase_UseCase class attributes and methods

# Step class attributes and methods

# Actor class attributes and methods

# urml_usecase_ApplicationDomainUseCase class attributes and methods

# UseCase class attributes and methods

# urml_danger_Mitigation class attributes and methods

# urml_danger_Asset class attributes and methods

# Danger class attributes and methods

# urml_danger_Danger class attributes and methods

# urml_danger_ProceduralMitigation class attributes and methods
urml_danger_ProceduralMitigation_mitigationProcedure: Property = Property(name="mitigationProcedure", type=StringType)
urml_danger_ProceduralMitigation.attributes={urml_danger_ProceduralMitigation_mitigationProcedure}

# urml_feature_AbstractFeature class attributes and methods

# SolutionDomainUseCase class attributes and methods

# urml_feature_VariationPointInstance class attributes and methods

# VariationPoint class attributes and methods

# VariationPointInstance class attributes and methods

# urml_feature_Feature class attributes and methods

# Product class attributes and methods

# urml_feature_VariationPoint class attributes and methods
urml_feature_VariationPoint_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
urml_feature_VariationPoint.attributes={urml_feature_VariationPoint_multiplicity}

# urml_feature_Product class attributes and methods

# Feature class attributes and methods

# Relationships
goals2: BinaryAssociation = BinaryAssociation(
    name="goals2",
    ends={
        Property(name="Goal", type=urml_Stakeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="stakeholders", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
reviewSet3: BinaryAssociation = BinaryAssociation(
    name="reviewSet3",
    ends={
        Property(name="urml_SetEntry", type=urml_StakeholderRole, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_StakeholderRole", type=urml_SetEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filterSet4: BinaryAssociation = BinaryAssociation(
    name="filterSet4",
    ends={
        Property(name="urml_SetEntry6", type=urml_StakeholderRole, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_StakeholderRole5", type=urml_SetEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="urml_UrmlModelElement", type=urml_UrmlModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_UrmlModelElement0", type=urml_UrmlModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
activePhase18: BinaryAssociation = BinaryAssociation(
    name="activePhase18",
    ends={
        Property(name="urml_Phase19", type=urml_UrmlProjectSettings, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_UrmlProjectSettings", type=urml_Phase, multiplicity=Multiplicity(0, 1))
    }
)
stakeholders20: BinaryAssociation = BinaryAssociation(
    name="stakeholders20",
    ends={
        Property(name="Stakeholder", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goals", type=goal_urml_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
key7: BinaryAssociation = BinaryAssociation(
    name="key7",
    ends={
        Property(name="urml_EClass", type=urml_SetEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_SetEntry8", type=urml_EClass, multiplicity=Multiplicity(0, 1))
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="urml_EStructuralFeature", type=urml_SetEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_SetEntry10", type=urml_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
key11: BinaryAssociation = BinaryAssociation(
    name="key11",
    ends={
        Property(name="urml_EClass12", type=urml_PhaseSetEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_PhaseSetEntry", type=urml_EClass, multiplicity=Multiplicity(0, 1))
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="urml_EClass15", type=urml_PhaseSetEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_PhaseSetEntry14", type=urml_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
allowedAssociations16: BinaryAssociation = BinaryAssociation(
    name="allowedAssociations16",
    ends={
        Property(name="urml_PhaseSetEntry17", type=urml_Phase, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_Phase", type=urml_PhaseSetEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
influencedGoals29: BinaryAssociation = BinaryAssociation(
    name="influencedGoals29",
    ends={
        Property(name="GoalReference30", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=GoalReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source31: BinaryAssociation = BinaryAssociation(
    name="source31",
    ends={
        Property(name="Goal32", type=urml_goal_GoalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="influencedGoals", type=Goal, multiplicity=Multiplicity(0, 1))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="Goal34", type=urml_goal_GoalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="influencingGoals", type=Goal, multiplicity=Multiplicity(0, 1))
    }
)
realizedFeatures21: BinaryAssociation = BinaryAssociation(
    name="realizedFeatures21",
    ends={
        Property(name="AbstractFeature", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goals22", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
detailingUseCases23: BinaryAssociation = BinaryAssociation(
    name="detailingUseCases23",
    ends={
        Property(name="ApplicationDomainUseCase", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="detailedGoal", type=ApplicationDomainUseCase, multiplicity=Multiplicity(0, 1))
    }
)
subGoals24: BinaryAssociation = BinaryAssociation(
    name="subGoals24",
    ends={
        Property(name="Goal25", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGoal", type=Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGoal26: BinaryAssociation = BinaryAssociation(
    name="parentGoal26",
    ends={
        Property(name="Goal27", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="subGoals", type=Goal, multiplicity=Multiplicity(0, 1))
    }
)
influencingGoals28: BinaryAssociation = BinaryAssociation(
    name="influencingGoals28",
    ends={
        Property(name="GoalReference", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=GoalReference, multiplicity=Multiplicity(0, 9999))
    }
)
detailedFeatures36: BinaryAssociation = BinaryAssociation(
    name="detailedFeatures36",
    ends={
        Property(name="AbstractFeature37", type=urml_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="detailingFunctionalRequirements", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
subFunctionalRequirements38: BinaryAssociation = BinaryAssociation(
    name="subFunctionalRequirements38",
    ends={
        Property(name="FunctionalRequirement", type=urml_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFunctionalRequirement", type=FunctionalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentFunctionalRequirement39: BinaryAssociation = BinaryAssociation(
    name="parentFunctionalRequirement39",
    ends={
        Property(name="FunctionalRequirement40", type=urml_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="subFunctionalRequirements", type=FunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
constrainedFeatures41: BinaryAssociation = BinaryAssociation(
    name="constrainedFeatures41",
    ends={
        Property(name="AbstractFeature42", type=urml_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainingNonFunctionalRequirements", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
implementingServices35: BinaryAssociation = BinaryAssociation(
    name="implementingServices35",
    ends={
        Property(name="Service", type=urml_requirement_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="satisfiedRequirements", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
detailedFeature50: BinaryAssociation = BinaryAssociation(
    name="detailedFeature50",
    ends={
        Property(name="AbstractFeature52", type=urml_usecase_SolutionDomainUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="detailingUseCases51", type=AbstractFeature, multiplicity=Multiplicity(0, 1))
    }
)
useCases53: BinaryAssociation = BinaryAssociation(
    name="useCases53",
    ends={
        Property(name="UseCase", type=urml_usecase_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
subNonFunctionalRequirements43: BinaryAssociation = BinaryAssociation(
    name="subNonFunctionalRequirements43",
    ends={
        Property(name="NonFunctionalRequirement", type=urml_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNonFunctionalRequirement", type=NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNonFunctionalRequirement44: BinaryAssociation = BinaryAssociation(
    name="parentNonFunctionalRequirement44",
    ends={
        Property(name="NonFunctionalRequirement45", type=urml_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="subNonFunctionalRequirements", type=NonFunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
steps46: BinaryAssociation = BinaryAssociation(
    name="steps46",
    ends={
        Property(name="Step", type=urml_usecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_usecase_UseCase", type=Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors47: BinaryAssociation = BinaryAssociation(
    name="actors47",
    ends={
        Property(name="Actor", type=urml_usecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases", type=Actor, multiplicity=Multiplicity(0, 9999))
    }
)
detailedGoal48: BinaryAssociation = BinaryAssociation(
    name="detailedGoal48",
    ends={
        Property(name="Goal49", type=urml_usecase_ApplicationDomainUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="detailingUseCases", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
triggeringAssets62: BinaryAssociation = BinaryAssociation(
    name="triggeringAssets62",
    ends={
        Property(name="Asset", type=urml_danger_Danger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeredDangers", type=Asset, multiplicity=Multiplicity(0, 9999))
    }
)
harmedAssets63: BinaryAssociation = BinaryAssociation(
    name="harmedAssets63",
    ends={
        Property(name="Asset64", type=urml_danger_Danger, multiplicity=Multiplicity(1, 1)),
        Property(name="harmingDangers", type=Asset, multiplicity=Multiplicity(0, 9999))
    }
)
mitigations65: BinaryAssociation = BinaryAssociation(
    name="mitigations65",
    ends={
        Property(name="Mitigation", type=urml_danger_Danger, multiplicity=Multiplicity(1, 1)),
        Property(name="mitigatedDangers", type=Mitigation, multiplicity=Multiplicity(0, 9999))
    }
)
mitigatedDangers66: BinaryAssociation = BinaryAssociation(
    name="mitigatedDangers66",
    ends={
        Property(name="Danger67", type=urml_danger_Mitigation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitigations", type=Danger, multiplicity=Multiplicity(0, 9999))
    }
)
satisfiedRequirements54: BinaryAssociation = BinaryAssociation(
    name="satisfiedRequirements54",
    ends={
        Property(name="Requirement", type=urml_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingServices", type=Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
parentService55: BinaryAssociation = BinaryAssociation(
    name="parentService55",
    ends={
        Property(name="Service56", type=urml_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="subServices", type=Service, multiplicity=Multiplicity(0, 1))
    }
)
subServices57: BinaryAssociation = BinaryAssociation(
    name="subServices57",
    ends={
        Property(name="Service58", type=urml_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="parentService", type=Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggeredDangers59: BinaryAssociation = BinaryAssociation(
    name="triggeredDangers59",
    ends={
        Property(name="Danger", type=urml_danger_Asset, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeringAssets", type=Danger, multiplicity=Multiplicity(0, 9999))
    }
)
harmingDangers60: BinaryAssociation = BinaryAssociation(
    name="harmingDangers60",
    ends={
        Property(name="Danger61", type=urml_danger_Asset, multiplicity=Multiplicity(1, 1)),
        Property(name="harmedAssets", type=Danger, multiplicity=Multiplicity(0, 9999))
    }
)
parentFeature75: BinaryAssociation = BinaryAssociation(
    name="parentFeature75",
    ends={
        Property(name="AbstractFeature76", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="subFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 1))
    }
)
subFeatures77: BinaryAssociation = BinaryAssociation(
    name="subFeatures77",
    ends={
        Property(name="AbstractFeature78", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFeature", type=AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
excludingFeatures79: BinaryAssociation = BinaryAssociation(
    name="excludingFeatures79",
    ends={
        Property(name="AbstractFeature80", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="excludedFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
excludedFeatures81: BinaryAssociation = BinaryAssociation(
    name="excludedFeatures81",
    ends={
        Property(name="AbstractFeature82", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="excludingFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
goals68: BinaryAssociation = BinaryAssociation(
    name="goals68",
    ends={
        Property(name="Goal69", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedFeatures", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
detailingFunctionalRequirements70: BinaryAssociation = BinaryAssociation(
    name="detailingFunctionalRequirements70",
    ends={
        Property(name="FunctionalRequirement71", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="detailedFeatures", type=FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
constrainingNonFunctionalRequirements72: BinaryAssociation = BinaryAssociation(
    name="constrainingNonFunctionalRequirements72",
    ends={
        Property(name="NonFunctionalRequirement73", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedFeatures", type=NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
detailingUseCases74: BinaryAssociation = BinaryAssociation(
    name="detailingUseCases74",
    ends={
        Property(name="SolutionDomainUseCase", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="detailedFeature", type=SolutionDomainUseCase, multiplicity=Multiplicity(0, 9999))
    }
)
optionalSubFeatures90: BinaryAssociation = BinaryAssociation(
    name="optionalSubFeatures90",
    ends={
        Property(name="AbstractFeature91", type=urml_feature_VariationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalParentVariationPoint", type=AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances92: BinaryAssociation = BinaryAssociation(
    name="instances92",
    ends={
        Property(name="VariationPointInstance93", type=urml_feature_VariationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="variationPoint", type=VariationPointInstance, multiplicity=Multiplicity(0, 9999))
    }
)
variationPoint94: BinaryAssociation = BinaryAssociation(
    name="variationPoint94",
    ends={
        Property(name="VariationPoint95", type=urml_feature_VariationPointInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=VariationPoint, multiplicity=Multiplicity(0, 1))
    }
)
requiringFeatures83: BinaryAssociation = BinaryAssociation(
    name="requiringFeatures83",
    ends={
        Property(name="AbstractFeature84", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
requiredFeatures85: BinaryAssociation = BinaryAssociation(
    name="requiredFeatures85",
    ends={
        Property(name="AbstractFeature86", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
optionalParentVariationPoint87: BinaryAssociation = BinaryAssociation(
    name="optionalParentVariationPoint87",
    ends={
        Property(name="VariationPoint", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalSubFeatures", type=VariationPoint, multiplicity=Multiplicity(0, 1))
    }
)
variationPointInstances88: BinaryAssociation = BinaryAssociation(
    name="variationPointInstances88",
    ends={
        Property(name="VariationPointInstance", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="selectedFeatures", type=VariationPointInstance, multiplicity=Multiplicity(0, 9999))
    }
)
products89: BinaryAssociation = BinaryAssociation(
    name="products89",
    ends={
        Property(name="Product", type=urml_feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
products96: BinaryAssociation = BinaryAssociation(
    name="products96",
    ends={
        Property(name="Product97", type=urml_feature_VariationPointInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="variationPointInstances", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
selectedFeatures98: BinaryAssociation = BinaryAssociation(
    name="selectedFeatures98",
    ends={
        Property(name="AbstractFeature100", type=urml_feature_VariationPointInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="variationPointInstances99", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
variationPointInstances101: BinaryAssociation = BinaryAssociation(
    name="variationPointInstances101",
    ends={
        Property(name="VariationPointInstance102", type=urml_feature_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="products", type=VariationPointInstance, multiplicity=Multiplicity(0, 9999))
    }
)
features103: BinaryAssociation = BinaryAssociation(
    name="features103",
    ends={
        Property(name="Feature", type=urml_feature_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="products104", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_urml_URMLDiagram_MEDiagram = Generalization(general=MEDiagram, specific=urml_URMLDiagram)
gen_urml_StakeholderRole_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=urml_StakeholderRole)
gen_urml_StakeholderRole_NonDomainElement = Generalization(general=NonDomainElement, specific=urml_StakeholderRole)
gen_urml_UrmlModelElement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=urml_UrmlModelElement)
gen_urml_Stakeholder_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_Stakeholder)
gen_urml_UrmlProjectSettings_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=urml_UrmlProjectSettings)
gen_urml_UrmlProjectSettings_NonDomainElement = Generalization(general=NonDomainElement, specific=urml_UrmlProjectSettings)
gen_urml_goal_Goal_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_goal_Goal)
gen_urml_Phase_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=urml_Phase)
gen_urml_Phase_NonDomainElement = Generalization(general=NonDomainElement, specific=urml_Phase)
gen_urml_goal_GoalReference_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_goal_GoalReference)
gen_urml_goal_GoalReference_AssociationClassElement = Generalization(general=AssociationClassElement, specific=urml_goal_GoalReference)
gen_urml_requirement_NonFunctionalRequirement_Requirement = Generalization(general=Requirement, specific=urml_requirement_NonFunctionalRequirement)
gen_urml_requirement_Requirement_Mitigation = Generalization(general=Mitigation, specific=urml_requirement_Requirement)
gen_urml_requirement_FunctionalRequirement_Requirement = Generalization(general=Requirement, specific=urml_requirement_FunctionalRequirement)
gen_urml_usecase_SolutionDomainUseCase_UseCase = Generalization(general=UseCase, specific=urml_usecase_SolutionDomainUseCase)
gen_urml_usecase_Actor_Asset = Generalization(general=Asset, specific=urml_usecase_Actor)
gen_urml_service_Service_Asset = Generalization(general=Asset, specific=urml_service_Service)
gen_urml_usecase_UseCase_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_usecase_UseCase)
gen_urml_usecase_ApplicationDomainUseCase_UseCase = Generalization(general=UseCase, specific=urml_usecase_ApplicationDomainUseCase)
gen_urml_danger_Mitigation_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_danger_Mitigation)
gen_urml_danger_Asset_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_danger_Asset)
gen_urml_danger_Danger_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_danger_Danger)
gen_urml_danger_ProceduralMitigation_Mitigation = Generalization(general=Mitigation, specific=urml_danger_ProceduralMitigation)
gen_urml_feature_AbstractFeature_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_feature_AbstractFeature)
gen_urml_feature_VariationPoint_AbstractFeature = Generalization(general=AbstractFeature, specific=urml_feature_VariationPoint)
gen_urml_feature_VariationPointInstance_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_feature_VariationPointInstance)
gen_urml_feature_Feature_AbstractFeature = Generalization(general=AbstractFeature, specific=urml_feature_Feature)
gen_urml_feature_Product_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_feature_Product)

# Domain Model
domain_model = DomainModel(
    name="urml",
    types={Goal, urml_URMLDiagram, MEDiagram, urml_StakeholderRole, NonDomainElement, urml_SetEntry, urml_UrmlModelElement, UnicaseModelElement, urml_Stakeholder, UrmlModelElement, urml_UrmlProjectSettings, urml_goal_Goal, goal_urml_Stakeholder, urml_EClass, urml_EStructuralFeature, urml_PhaseSetEntry, urml_Phase, urml_goal_GoalReference, AssociationClassElement, AbstractFeature, ApplicationDomainUseCase, GoalReference, FunctionalRequirement, urml_requirement_NonFunctionalRequirement, urml_requirement_Requirement, Mitigation, Service, urml_requirement_FunctionalRequirement, Requirement, urml_usecase_SolutionDomainUseCase, urml_usecase_Actor, Asset, urml_service_Service, NonFunctionalRequirement, urml_usecase_UseCase, Step, Actor, urml_usecase_ApplicationDomainUseCase, UseCase, urml_danger_Mitigation, urml_danger_Asset, Danger, urml_danger_Danger, urml_danger_ProceduralMitigation, urml_feature_AbstractFeature, SolutionDomainUseCase, urml_feature_VariationPointInstance, VariationPoint, VariationPointInstance, urml_feature_Feature, Product, urml_feature_VariationPoint, urml_feature_Product, Feature, GoalType, GoalReferenceType},
    associations={goals2, reviewSet3, filterSet4, associations1, activePhase18, stakeholders20, key7, value9, key11, value13, allowedAssociations16, influencedGoals29, source31, target33, realizedFeatures21, detailingUseCases23, subGoals24, parentGoal26, influencingGoals28, detailedFeatures36, subFunctionalRequirements38, parentFunctionalRequirement39, constrainedFeatures41, implementingServices35, detailedFeature50, useCases53, subNonFunctionalRequirements43, parentNonFunctionalRequirement44, steps46, actors47, detailedGoal48, triggeringAssets62, harmedAssets63, mitigations65, mitigatedDangers66, satisfiedRequirements54, parentService55, subServices57, triggeredDangers59, harmingDangers60, parentFeature75, subFeatures77, excludingFeatures79, excludedFeatures81, goals68, detailingFunctionalRequirements70, constrainingNonFunctionalRequirements72, detailingUseCases74, optionalSubFeatures90, instances92, variationPoint94, requiringFeatures83, requiredFeatures85, optionalParentVariationPoint87, variationPointInstances88, products89, products96, selectedFeatures98, variationPointInstances101, features103},
    generalizations={gen_urml_URMLDiagram_MEDiagram, gen_urml_StakeholderRole_UnicaseModelElement, gen_urml_StakeholderRole_NonDomainElement, gen_urml_UrmlModelElement_UnicaseModelElement, gen_urml_Stakeholder_UrmlModelElement, gen_urml_UrmlProjectSettings_UnicaseModelElement, gen_urml_UrmlProjectSettings_NonDomainElement, gen_urml_goal_Goal_UrmlModelElement, gen_urml_Phase_UnicaseModelElement, gen_urml_Phase_NonDomainElement, gen_urml_goal_GoalReference_UrmlModelElement, gen_urml_goal_GoalReference_AssociationClassElement, gen_urml_requirement_NonFunctionalRequirement_Requirement, gen_urml_requirement_Requirement_Mitigation, gen_urml_requirement_FunctionalRequirement_Requirement, gen_urml_usecase_SolutionDomainUseCase_UseCase, gen_urml_usecase_Actor_Asset, gen_urml_service_Service_Asset, gen_urml_usecase_UseCase_UrmlModelElement, gen_urml_usecase_ApplicationDomainUseCase_UseCase, gen_urml_danger_Mitigation_UrmlModelElement, gen_urml_danger_Asset_UrmlModelElement, gen_urml_danger_Danger_UrmlModelElement, gen_urml_danger_ProceduralMitigation_Mitigation, gen_urml_feature_AbstractFeature_UrmlModelElement, gen_urml_feature_VariationPoint_AbstractFeature, gen_urml_feature_VariationPointInstance_UrmlModelElement, gen_urml_feature_Feature_AbstractFeature, gen_urml_feature_Product_UrmlModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)