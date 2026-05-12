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
UrmlModelElement = Class(name="UrmlModelElement")
Goal = Class(name="Goal")
urml_URMLDiagram = Class(name="urml_URMLDiagram")
MEDiagram = Class(name="MEDiagram")
urml_goal_Goal = Class(name="urml_goal_Goal")
urml_UrmlModelElement = Class(name="urml_UrmlModelElement", is_abstract=True)
UnicaseModelElement = Class(name="UnicaseModelElement")
urml_Stakeholder = Class(name="urml_Stakeholder")
urml_goal_GoalReference = Class(name="urml_goal_GoalReference")
AssociationClassElement = Class(name="AssociationClassElement")
goal_urml_Stakeholder = Class(name="goal_urml_Stakeholder")
AbstractFeature = Class(name="AbstractFeature")
ApplicationDomainUseCase = Class(name="ApplicationDomainUseCase")
GoalReference = Class(name="GoalReference")
urml_requirement_FunctionalRequirement = Class(name="urml_requirement_FunctionalRequirement")
Requirement = Class(name="Requirement")
FunctionalRequirement = Class(name="FunctionalRequirement")
urml_requirement_Requirement = Class(name="urml_requirement_Requirement", is_abstract=True)
Mitigation = Class(name="Mitigation")
Service = Class(name="Service")
urml_usecase_ApplicationDomainUseCase = Class(name="urml_usecase_ApplicationDomainUseCase")
UseCase = Class(name="UseCase")
urml_usecase_SolutionDomainUseCase = Class(name="urml_usecase_SolutionDomainUseCase")
urml_requirement_NonFunctionalRequirement = Class(name="urml_requirement_NonFunctionalRequirement")
NonFunctionalRequirement = Class(name="NonFunctionalRequirement")
urml_usecase_UseCase = Class(name="urml_usecase_UseCase", is_abstract=True)
Step = Class(name="Step")
Actor = Class(name="Actor")
urml_danger_Danger = Class(name="urml_danger_Danger")
urml_usecase_Actor = Class(name="urml_usecase_Actor")
Asset = Class(name="Asset")
urml_service_Service = Class(name="urml_service_Service")
urml_danger_Asset = Class(name="urml_danger_Asset", is_abstract=True)
Danger = Class(name="Danger")
SolutionDomainUseCase = Class(name="SolutionDomainUseCase")
urml_danger_Mitigation = Class(name="urml_danger_Mitigation", is_abstract=True)
urml_danger_ProceduralMitigation = Class(name="urml_danger_ProceduralMitigation")
urml_feature_AbstractFeature = Class(name="urml_feature_AbstractFeature", is_abstract=True)
urml_feature_Feature = Class(name="urml_feature_Feature")
Product = Class(name="Product")
urml_feature_VariationPoint = Class(name="urml_feature_VariationPoint")
VariationPoint = Class(name="VariationPoint")
VariationPointInstance = Class(name="VariationPointInstance")
Feature = Class(name="Feature")
urml_feature_VariationPointInstance = Class(name="urml_feature_VariationPointInstance")
urml_feature_Product = Class(name="urml_feature_Product")

# UrmlModelElement class attributes and methods

# Goal class attributes and methods

# urml_URMLDiagram class attributes and methods

# MEDiagram class attributes and methods

# urml_goal_Goal class attributes and methods
urml_goal_Goal_soft: Property = Property(name="soft", type=BooleanType)
urml_goal_Goal_type: Property = Property(name="type", type=StringType)
urml_goal_Goal.attributes={urml_goal_Goal_type, urml_goal_Goal_soft}

# urml_UrmlModelElement class attributes and methods

# UnicaseModelElement class attributes and methods

# urml_Stakeholder class attributes and methods

# urml_goal_GoalReference class attributes and methods
urml_goal_GoalReference_weight: Property = Property(name="weight", type=StringType)
urml_goal_GoalReference.attributes={urml_goal_GoalReference_weight}

# AssociationClassElement class attributes and methods

# goal_urml_Stakeholder class attributes and methods

# AbstractFeature class attributes and methods

# ApplicationDomainUseCase class attributes and methods

# GoalReference class attributes and methods

# urml_requirement_FunctionalRequirement class attributes and methods

# Requirement class attributes and methods

# FunctionalRequirement class attributes and methods

# urml_requirement_Requirement class attributes and methods
urml_requirement_Requirement_terminal: Property = Property(name="terminal", type=BooleanType)
urml_requirement_Requirement.attributes={urml_requirement_Requirement_terminal}

# Mitigation class attributes and methods

# Service class attributes and methods

# urml_usecase_ApplicationDomainUseCase class attributes and methods

# UseCase class attributes and methods

# urml_usecase_SolutionDomainUseCase class attributes and methods

# urml_requirement_NonFunctionalRequirement class attributes and methods

# NonFunctionalRequirement class attributes and methods

# urml_usecase_UseCase class attributes and methods

# Step class attributes and methods

# Actor class attributes and methods

# urml_danger_Danger class attributes and methods

# urml_usecase_Actor class attributes and methods

# Asset class attributes and methods

# urml_service_Service class attributes and methods

# urml_danger_Asset class attributes and methods

# Danger class attributes and methods

# SolutionDomainUseCase class attributes and methods

# urml_danger_Mitigation class attributes and methods

# urml_danger_ProceduralMitigation class attributes and methods
urml_danger_ProceduralMitigation_mitigationProcedure: Property = Property(name="mitigationProcedure", type=StringType)
urml_danger_ProceduralMitigation.attributes={urml_danger_ProceduralMitigation_mitigationProcedure}

# urml_feature_AbstractFeature class attributes and methods

# urml_feature_Feature class attributes and methods

# Product class attributes and methods

# urml_feature_VariationPoint class attributes and methods
urml_feature_VariationPoint_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
urml_feature_VariationPoint.attributes={urml_feature_VariationPoint_multiplicity}

# VariationPoint class attributes and methods

# VariationPointInstance class attributes and methods

# Feature class attributes and methods

# urml_feature_VariationPointInstance class attributes and methods

# urml_feature_Product class attributes and methods

# Relationships
goals0: BinaryAssociation = BinaryAssociation(
    name="goals0",
    ends={
        Property(name="Goal", type=urml_Stakeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="stakeholders", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
influencedGoals10: BinaryAssociation = BinaryAssociation(
    name="influencedGoals10",
    ends={
        Property(name="GoalReference11", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=GoalReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="Goal13", type=urml_goal_GoalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="influencedGoals", type=Goal, multiplicity=Multiplicity(0, 1))
    }
)
stakeholders1: BinaryAssociation = BinaryAssociation(
    name="stakeholders1",
    ends={
        Property(name="Stakeholder", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goals", type=goal_urml_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
realizedFeatures2: BinaryAssociation = BinaryAssociation(
    name="realizedFeatures2",
    ends={
        Property(name="AbstractFeature", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goals3", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
detailingUseCases4: BinaryAssociation = BinaryAssociation(
    name="detailingUseCases4",
    ends={
        Property(name="ApplicationDomainUseCase", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="detailedGoal", type=ApplicationDomainUseCase, multiplicity=Multiplicity(0, 1))
    }
)
subGoals5: BinaryAssociation = BinaryAssociation(
    name="subGoals5",
    ends={
        Property(name="Goal6", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGoal", type=Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGoal7: BinaryAssociation = BinaryAssociation(
    name="parentGoal7",
    ends={
        Property(name="Goal8", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="subGoals", type=Goal, multiplicity=Multiplicity(0, 1))
    }
)
influencingGoals9: BinaryAssociation = BinaryAssociation(
    name="influencingGoals9",
    ends={
        Property(name="GoalReference", type=urml_goal_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=GoalReference, multiplicity=Multiplicity(0, 9999))
    }
)
detailedFeatures17: BinaryAssociation = BinaryAssociation(
    name="detailedFeatures17",
    ends={
        Property(name="AbstractFeature18", type=urml_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="detailingFunctionalRequirements", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
subFunctionalRequirements19: BinaryAssociation = BinaryAssociation(
    name="subFunctionalRequirements19",
    ends={
        Property(name="FunctionalRequirement", type=urml_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFunctionalRequirement", type=FunctionalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="Goal15", type=urml_goal_GoalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="influencingGoals", type=Goal, multiplicity=Multiplicity(0, 1))
    }
)
implementingServices16: BinaryAssociation = BinaryAssociation(
    name="implementingServices16",
    ends={
        Property(name="Service", type=urml_requirement_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="satisfiedRequirements", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
actors28: BinaryAssociation = BinaryAssociation(
    name="actors28",
    ends={
        Property(name="useCases", type=Actor, multiplicity=Multiplicity(0, 9999)),
        Property(name="Actor", type=urml_usecase_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
detailedGoal29: BinaryAssociation = BinaryAssociation(
    name="detailedGoal29",
    ends={
        Property(name="Goal30", type=urml_usecase_ApplicationDomainUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="detailingUseCases", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
detailedFeature31: BinaryAssociation = BinaryAssociation(
    name="detailedFeature31",
    ends={
        Property(name="AbstractFeature33", type=urml_usecase_SolutionDomainUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="detailingUseCases32", type=AbstractFeature, multiplicity=Multiplicity(0, 1))
    }
)
parentFunctionalRequirement20: BinaryAssociation = BinaryAssociation(
    name="parentFunctionalRequirement20",
    ends={
        Property(name="FunctionalRequirement21", type=urml_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="subFunctionalRequirements", type=FunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
constrainedFeatures22: BinaryAssociation = BinaryAssociation(
    name="constrainedFeatures22",
    ends={
        Property(name="AbstractFeature23", type=urml_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainingNonFunctionalRequirements", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
subNonFunctionalRequirements24: BinaryAssociation = BinaryAssociation(
    name="subNonFunctionalRequirements24",
    ends={
        Property(name="NonFunctionalRequirement", type=urml_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNonFunctionalRequirement", type=NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNonFunctionalRequirement25: BinaryAssociation = BinaryAssociation(
    name="parentNonFunctionalRequirement25",
    ends={
        Property(name="NonFunctionalRequirement26", type=urml_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="subNonFunctionalRequirements", type=NonFunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
steps27: BinaryAssociation = BinaryAssociation(
    name="steps27",
    ends={
        Property(name="Step", type=urml_usecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="urml_usecase_UseCase", type=Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggeredDangers40: BinaryAssociation = BinaryAssociation(
    name="triggeredDangers40",
    ends={
        Property(name="Danger", type=urml_danger_Asset, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeringAssets", type=Danger, multiplicity=Multiplicity(0, 9999))
    }
)
harmingDangers41: BinaryAssociation = BinaryAssociation(
    name="harmingDangers41",
    ends={
        Property(name="Danger42", type=urml_danger_Asset, multiplicity=Multiplicity(1, 1)),
        Property(name="harmedAssets", type=Danger, multiplicity=Multiplicity(0, 9999))
    }
)
triggeringAssets43: BinaryAssociation = BinaryAssociation(
    name="triggeringAssets43",
    ends={
        Property(name="Asset", type=urml_danger_Danger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeredDangers", type=Asset, multiplicity=Multiplicity(0, 9999))
    }
)
useCases34: BinaryAssociation = BinaryAssociation(
    name="useCases34",
    ends={
        Property(name="UseCase", type=urml_usecase_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
satisfiedRequirements35: BinaryAssociation = BinaryAssociation(
    name="satisfiedRequirements35",
    ends={
        Property(name="Requirement", type=urml_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingServices", type=Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
parentService36: BinaryAssociation = BinaryAssociation(
    name="parentService36",
    ends={
        Property(name="Service37", type=urml_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="subServices", type=Service, multiplicity=Multiplicity(0, 1))
    }
)
subServices38: BinaryAssociation = BinaryAssociation(
    name="subServices38",
    ends={
        Property(name="Service39", type=urml_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="parentService", type=Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainingNonFunctionalRequirements53: BinaryAssociation = BinaryAssociation(
    name="constrainingNonFunctionalRequirements53",
    ends={
        Property(name="NonFunctionalRequirement54", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedFeatures", type=NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
detailingUseCases55: BinaryAssociation = BinaryAssociation(
    name="detailingUseCases55",
    ends={
        Property(name="SolutionDomainUseCase", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="detailedFeature", type=SolutionDomainUseCase, multiplicity=Multiplicity(0, 9999))
    }
)
parentFeature56: BinaryAssociation = BinaryAssociation(
    name="parentFeature56",
    ends={
        Property(name="AbstractFeature57", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="subFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 1))
    }
)
harmedAssets44: BinaryAssociation = BinaryAssociation(
    name="harmedAssets44",
    ends={
        Property(name="Asset45", type=urml_danger_Danger, multiplicity=Multiplicity(1, 1)),
        Property(name="harmingDangers", type=Asset, multiplicity=Multiplicity(0, 9999))
    }
)
mitigations46: BinaryAssociation = BinaryAssociation(
    name="mitigations46",
    ends={
        Property(name="Mitigation", type=urml_danger_Danger, multiplicity=Multiplicity(1, 1)),
        Property(name="mitigatedDangers", type=Mitigation, multiplicity=Multiplicity(0, 9999))
    }
)
mitigatedDangers47: BinaryAssociation = BinaryAssociation(
    name="mitigatedDangers47",
    ends={
        Property(name="Danger48", type=urml_danger_Mitigation, multiplicity=Multiplicity(1, 1)),
        Property(name="mitigations", type=Danger, multiplicity=Multiplicity(0, 9999))
    }
)
goals49: BinaryAssociation = BinaryAssociation(
    name="goals49",
    ends={
        Property(name="Goal50", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedFeatures", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)
detailingFunctionalRequirements51: BinaryAssociation = BinaryAssociation(
    name="detailingFunctionalRequirements51",
    ends={
        Property(name="FunctionalRequirement52", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="detailedFeatures", type=FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
products70: BinaryAssociation = BinaryAssociation(
    name="products70",
    ends={
        Property(name="Product", type=urml_feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
optionalSubFeatures71: BinaryAssociation = BinaryAssociation(
    name="optionalSubFeatures71",
    ends={
        Property(name="AbstractFeature72", type=urml_feature_VariationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalParentVariationPoint", type=AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFeatures58: BinaryAssociation = BinaryAssociation(
    name="subFeatures58",
    ends={
        Property(name="AbstractFeature59", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFeature", type=AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
excludingFeatures60: BinaryAssociation = BinaryAssociation(
    name="excludingFeatures60",
    ends={
        Property(name="AbstractFeature61", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="excludedFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
excludedFeatures62: BinaryAssociation = BinaryAssociation(
    name="excludedFeatures62",
    ends={
        Property(name="AbstractFeature63", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="excludingFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
requiringFeatures64: BinaryAssociation = BinaryAssociation(
    name="requiringFeatures64",
    ends={
        Property(name="AbstractFeature65", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
requiredFeatures66: BinaryAssociation = BinaryAssociation(
    name="requiredFeatures66",
    ends={
        Property(name="AbstractFeature67", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringFeatures", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
optionalParentVariationPoint68: BinaryAssociation = BinaryAssociation(
    name="optionalParentVariationPoint68",
    ends={
        Property(name="VariationPoint", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalSubFeatures", type=VariationPoint, multiplicity=Multiplicity(0, 1))
    }
)
variationPointInstances69: BinaryAssociation = BinaryAssociation(
    name="variationPointInstances69",
    ends={
        Property(name="VariationPointInstance", type=urml_feature_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="selectedFeatures", type=VariationPointInstance, multiplicity=Multiplicity(0, 9999))
    }
)
features84: BinaryAssociation = BinaryAssociation(
    name="features84",
    ends={
        Property(name="Feature", type=urml_feature_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="products85", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
instances73: BinaryAssociation = BinaryAssociation(
    name="instances73",
    ends={
        Property(name="VariationPointInstance74", type=urml_feature_VariationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="variationPoint", type=VariationPointInstance, multiplicity=Multiplicity(0, 9999))
    }
)
variationPoint75: BinaryAssociation = BinaryAssociation(
    name="variationPoint75",
    ends={
        Property(name="VariationPoint76", type=urml_feature_VariationPointInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=VariationPoint, multiplicity=Multiplicity(0, 1))
    }
)
products77: BinaryAssociation = BinaryAssociation(
    name="products77",
    ends={
        Property(name="Product78", type=urml_feature_VariationPointInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="variationPointInstances", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
selectedFeatures79: BinaryAssociation = BinaryAssociation(
    name="selectedFeatures79",
    ends={
        Property(name="AbstractFeature81", type=urml_feature_VariationPointInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="variationPointInstances80", type=AbstractFeature, multiplicity=Multiplicity(0, 9999))
    }
)
variationPointInstances82: BinaryAssociation = BinaryAssociation(
    name="variationPointInstances82",
    ends={
        Property(name="VariationPointInstance83", type=urml_feature_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="products", type=VariationPointInstance, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_urml_Stakeholder_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_Stakeholder)
gen_urml_URMLDiagram_MEDiagram = Generalization(general=MEDiagram, specific=urml_URMLDiagram)
gen_urml_UrmlModelElement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=urml_UrmlModelElement)
gen_urml_goal_GoalReference_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_goal_GoalReference)
gen_urml_goal_GoalReference_AssociationClassElement = Generalization(general=AssociationClassElement, specific=urml_goal_GoalReference)
gen_urml_goal_Goal_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_goal_Goal)
gen_urml_requirement_FunctionalRequirement_Requirement = Generalization(general=Requirement, specific=urml_requirement_FunctionalRequirement)
gen_urml_requirement_Requirement_Mitigation = Generalization(general=Mitigation, specific=urml_requirement_Requirement)
gen_urml_usecase_ApplicationDomainUseCase_UseCase = Generalization(general=UseCase, specific=urml_usecase_ApplicationDomainUseCase)
gen_urml_usecase_SolutionDomainUseCase_UseCase = Generalization(general=UseCase, specific=urml_usecase_SolutionDomainUseCase)
gen_urml_requirement_NonFunctionalRequirement_Requirement = Generalization(general=Requirement, specific=urml_requirement_NonFunctionalRequirement)
gen_urml_usecase_UseCase_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_usecase_UseCase)
gen_urml_danger_Danger_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_danger_Danger)
gen_urml_usecase_Actor_Asset = Generalization(general=Asset, specific=urml_usecase_Actor)
gen_urml_service_Service_Asset = Generalization(general=Asset, specific=urml_service_Service)
gen_urml_danger_Asset_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_danger_Asset)
gen_urml_danger_Mitigation_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_danger_Mitigation)
gen_urml_danger_ProceduralMitigation_Mitigation = Generalization(general=Mitigation, specific=urml_danger_ProceduralMitigation)
gen_urml_feature_AbstractFeature_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_feature_AbstractFeature)
gen_urml_feature_Feature_AbstractFeature = Generalization(general=AbstractFeature, specific=urml_feature_Feature)
gen_urml_feature_VariationPoint_AbstractFeature = Generalization(general=AbstractFeature, specific=urml_feature_VariationPoint)
gen_urml_feature_VariationPointInstance_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_feature_VariationPointInstance)
gen_urml_feature_Product_UrmlModelElement = Generalization(general=UrmlModelElement, specific=urml_feature_Product)

# Domain Model
domain_model = DomainModel(
    name="urml",
    types={UrmlModelElement, Goal, urml_URMLDiagram, MEDiagram, urml_goal_Goal, urml_UrmlModelElement, UnicaseModelElement, urml_Stakeholder, urml_goal_GoalReference, AssociationClassElement, goal_urml_Stakeholder, AbstractFeature, ApplicationDomainUseCase, GoalReference, urml_requirement_FunctionalRequirement, Requirement, FunctionalRequirement, urml_requirement_Requirement, Mitigation, Service, urml_usecase_ApplicationDomainUseCase, UseCase, urml_usecase_SolutionDomainUseCase, urml_requirement_NonFunctionalRequirement, NonFunctionalRequirement, urml_usecase_UseCase, Step, Actor, urml_danger_Danger, urml_usecase_Actor, Asset, urml_service_Service, urml_danger_Asset, Danger, SolutionDomainUseCase, urml_danger_Mitigation, urml_danger_ProceduralMitigation, urml_feature_AbstractFeature, urml_feature_Feature, Product, urml_feature_VariationPoint, VariationPoint, VariationPointInstance, Feature, urml_feature_VariationPointInstance, urml_feature_Product, GoalType, GoalReferenceType},
    associations={goals0, influencedGoals10, source12, stakeholders1, realizedFeatures2, detailingUseCases4, subGoals5, parentGoal7, influencingGoals9, detailedFeatures17, subFunctionalRequirements19, target14, implementingServices16, actors28, detailedGoal29, detailedFeature31, parentFunctionalRequirement20, constrainedFeatures22, subNonFunctionalRequirements24, parentNonFunctionalRequirement25, steps27, triggeredDangers40, harmingDangers41, triggeringAssets43, useCases34, satisfiedRequirements35, parentService36, subServices38, constrainingNonFunctionalRequirements53, detailingUseCases55, parentFeature56, harmedAssets44, mitigations46, mitigatedDangers47, goals49, detailingFunctionalRequirements51, products70, optionalSubFeatures71, subFeatures58, excludingFeatures60, excludedFeatures62, requiringFeatures64, requiredFeatures66, optionalParentVariationPoint68, variationPointInstances69, features84, instances73, variationPoint75, products77, selectedFeatures79, variationPointInstances82},
    generalizations={gen_urml_Stakeholder_UrmlModelElement, gen_urml_URMLDiagram_MEDiagram, gen_urml_UrmlModelElement_UnicaseModelElement, gen_urml_goal_GoalReference_UrmlModelElement, gen_urml_goal_GoalReference_AssociationClassElement, gen_urml_goal_Goal_UrmlModelElement, gen_urml_requirement_FunctionalRequirement_Requirement, gen_urml_requirement_Requirement_Mitigation, gen_urml_usecase_ApplicationDomainUseCase_UseCase, gen_urml_usecase_SolutionDomainUseCase_UseCase, gen_urml_requirement_NonFunctionalRequirement_Requirement, gen_urml_usecase_UseCase_UrmlModelElement, gen_urml_danger_Danger_UrmlModelElement, gen_urml_usecase_Actor_Asset, gen_urml_service_Service_Asset, gen_urml_danger_Asset_UrmlModelElement, gen_urml_danger_Mitigation_UrmlModelElement, gen_urml_danger_ProceduralMitigation_Mitigation, gen_urml_feature_AbstractFeature_UrmlModelElement, gen_urml_feature_Feature_AbstractFeature, gen_urml_feature_VariationPoint_AbstractFeature, gen_urml_feature_VariationPointInstance_UrmlModelElement, gen_urml_feature_Product_UrmlModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)