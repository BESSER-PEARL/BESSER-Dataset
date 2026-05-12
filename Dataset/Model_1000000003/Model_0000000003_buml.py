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
EvaluationStatus: Enumeration = Enumeration(
    name="EvaluationStatus",
    literals={
            EnumerationLiteral(name="Archived"),
			EnumerationLiteral(name="Pending"),
			EnumerationLiteral(name="Processing"),
			EnumerationLiteral(name="Custom"),
			EnumerationLiteral(name="Done")
    }
)

ProjectStatus: Enumeration = Enumeration(
    name="ProjectStatus",
    literals={
            EnumerationLiteral(name="Archived"),
			EnumerationLiteral(name="Created"),
			EnumerationLiteral(name="Pending"),
			EnumerationLiteral(name="Ready"),
			EnumerationLiteral(name="Closed")
    }
)

DatasetType: Enumeration = Enumeration(
    name="DatasetType",
    literals={
            EnumerationLiteral(name="Training"),
			EnumerationLiteral(name="Test"),
			EnumerationLiteral(name="Validation")
    }
)

LicensingType: Enumeration = Enumeration(
    name="LicensingType",
    literals={
            EnumerationLiteral(name="Open_Source"),
			EnumerationLiteral(name="Proprietary")
    }
)

VerificationType: Enumeration = Enumeration(
    name="VerificationType",
    literals={
            EnumerationLiteral(name="Case_1"),
			EnumerationLiteral(name="Case_2"),
			EnumerationLiteral(name="Case_3")
    }
)

TagsVerificationTarget: Enumeration = Enumeration(
    name="TagsVerificationTarget",
    literals={
            EnumerationLiteral(name="Transparency"),
			EnumerationLiteral(name="Accountability"),
			EnumerationLiteral(name="Risk_management"),
			EnumerationLiteral(name="Human_Agency_and_Oversight"),
			EnumerationLiteral(name="Technical_Robustness__and_Saftey"),
			EnumerationLiteral(name="Privacy_and_Data_Governance"),
			EnumerationLiteral(name="Diversity_Nondiscrimination_and_Fairness"),
			EnumerationLiteral(name="Societal_and_enviornmanetal_wellbeing")
    }
)

TagsSector: Enumeration = Enumeration(
    name="TagsSector",
    literals={
            EnumerationLiteral(name="Agriculture"),
			EnumerationLiteral(name="Defence"),
			EnumerationLiteral(name="Health"),
			EnumerationLiteral(name="Competition"),
			EnumerationLiteral(name="Environment"),
			EnumerationLiteral(name="Economz"),
			EnumerationLiteral(name="Education"),
			EnumerationLiteral(name="Trade"),
			EnumerationLiteral(name="Innovation"),
			EnumerationLiteral(name="Inclusive_development"),
			EnumerationLiteral(name="Investment")
    }
)

TagsTargetSystem: Enumeration = Enumeration(
    name="TagsTargetSystem",
    literals={
            EnumerationLiteral(name="Computer_Vision"),
			EnumerationLiteral(name="Natural_Language_Processing"),
			EnumerationLiteral(name="Audio"),
			EnumerationLiteral(name="Multimodal"),
			EnumerationLiteral(name="Knowledge_and_Retrival"),
			EnumerationLiteral(name="Decision_and_Optimization"),
			EnumerationLiteral(name="Recommendation_and_Personalization"),
			EnumerationLiteral(name="Predictive_and_Analytical_AI"),
			EnumerationLiteral(name="Tabular_and_Structured_Data"),
			EnumerationLiteral(name="Reinforcement_Learning_and_Control"),
			EnumerationLiteral(name="Agents_and_Agentic_Systems"),
			EnumerationLiteral(name="AI_Safety_and_Governance"),
			EnumerationLiteral(name="Emerging_Other")
    }
)

# Classes
Project = Class(name="Project")
Dataset = Class(name="Dataset")
Datashape = Class(name="Datashape")
Feature = Class(name="Feature")
MetricCategory = Class(name="MetricCategory")
Configuration = Class(name="Configuration")
Metric = Class(name="Metric")
ConfParam = Class(name="ConfParam")
AssessmentElement = Class(name="AssessmentElement", is_abstract=True)
Element = Class(name="Element")
Tool = Class(name="Tool")
LegalRequirement = Class(name="LegalRequirement")
Measure = Class(name="Measure")
Observation = Class(name="Observation")
Evaluation = Class(name="Evaluation")
Direct = Class(name="Direct")
Derived = Class(name="Derived")
AISystem = Class(name="AISystem")

# Project class attributes and methods
Project_name: Property = Property(name="name", type=StringType)
Project_status: Property = Property(name="status", type=ProjectStatus)
Project.attributes={Project_name, Project_status}

# Dataset class attributes and methods
Dataset_source: Property = Property(name="source", type=StringType)
Dataset_version: Property = Property(name="version", type=StringType)
Dataset_licensing: Property = Property(name="licensing", type=LicensingType)
Dataset_dataset_type: Property = Property(name="dataset_type", type=DatasetType)
Dataset.attributes={Dataset_dataset_type, Dataset_licensing, Dataset_source, Dataset_version}

# Datashape class attributes and methods
Datashape_accepted_target_values: Property = Property(name="accepted_target_values", type=StringType)
Datashape.attributes={Datashape_accepted_target_values}

# Feature class attributes and methods
Feature_feature_type: Property = Property(name="feature_type", type=StringType)
Feature_min_value: Property = Property(name="min_value", type=FloatType)
Feature_max_value: Property = Property(name="max_value", type=FloatType)
Feature.attributes={Feature_feature_type, Feature_max_value, Feature_min_value}

# MetricCategory class attributes and methods

# Configuration class attributes and methods

# Metric class attributes and methods

# ConfParam class attributes and methods
ConfParam_param_type: Property = Property(name="param_type", type=StringType)
ConfParam_value: Property = Property(name="value", type=StringType)
ConfParam.attributes={ConfParam_param_type, ConfParam_value}

# AssessmentElement class attributes and methods
AssessmentElement_name: Property = Property(name="name", type=StringType)
AssessmentElement_description: Property = Property(name="description", type=StringType)
AssessmentElement.attributes={AssessmentElement_description, AssessmentElement_name}

# Element class attributes and methods

# Tool class attributes and methods
Tool_licensing: Property = Property(name="licensing", type=LicensingType)
Tool_verification_type: Property = Property(name="verification_type", type=VerificationType)
Tool_provider: Property = Property(name="provider", type=StringType)
Tool_project: Property = Property(name="project", type=StringType)
Tool_branch: Property = Property(name="branch", type=StringType)
Tool_version: Property = Property(name="version", type=StringType)
Tool_project_maturity: Property = Property(name="project_maturity", type=StringType)
Tool_scientific_reference: Property = Property(name="scientific_reference", type=StringType)
Tool_verification_targets: Property = Property(name="verification_targets", type=TagsVerificationTarget)
Tool_sector: Property = Property(name="sector", type=TagsSector)
Tool_target_system: Property = Property(name="target_system", type=TagsTargetSystem)
Tool_target_legal_requirements: Property = Property(name="target_legal_requirements", type=StringType)
Tool.attributes={Tool_branch, Tool_licensing, Tool_project, Tool_project_maturity, Tool_provider, Tool_scientific_reference, Tool_sector, Tool_target_legal_requirements, Tool_target_system, Tool_verification_targets, Tool_verification_type, Tool_version}

# LegalRequirement class attributes and methods
LegalRequirement_legal_ref: Property = Property(name="legal_ref", type=StringType)
LegalRequirement_standard: Property = Property(name="standard", type=StringType)
LegalRequirement_principle: Property = Property(name="principle", type=StringType)
LegalRequirement.attributes={LegalRequirement_legal_ref, LegalRequirement_principle, LegalRequirement_standard}

# Measure class attributes and methods
Measure_value: Property = Property(name="value", type=StringType)
Measure_error: Property = Property(name="error", type=StringType)
Measure_uncertainty: Property = Property(name="uncertainty", type=FloatType)
Measure_unit: Property = Property(name="unit", type=StringType)
Measure.attributes={Measure_error, Measure_uncertainty, Measure_unit, Measure_value}

# Observation class attributes and methods
Observation_observer: Property = Property(name="observer", type=StringType)
Observation_whenObserved: Property = Property(name="whenObserved", type=DateTimeType)
Observation.attributes={Observation_observer, Observation_whenObserved}

# Evaluation class attributes and methods
Evaluation_status: Property = Property(name="status", type=EvaluationStatus)
Evaluation.attributes={Evaluation_status}

# Direct class attributes and methods

# Derived class attributes and methods
Derived_expression: Property = Property(name="expression", type=StringType)
Derived.attributes={Derived_expression}

# AISystem class attributes and methods
AISystem_settings: Property = Property(name="settings", type=StringType)
AISystem_data: Property = Property(name="data", type=StringType)
AISystem_source: Property = Property(name="source", type=StringType)
AISystem_licensing: Property = Property(name="licensing", type=LicensingType)
AISystem_version: Property = Property(name="version", type=StringType)
AISystem.attributes={AISystem_data, AISystem_licensing, AISystem_settings, AISystem_source, AISystem_version}

# Relationships
MetricCategory_Metric: BinaryAssociation = BinaryAssociation(
    name="MetricCategory_Metric",
    ends={
        Property(name="category", type=MetricCategory, multiplicity=Multiplicity(0, 9999)),
        Property(name="metrics", type=Metric, multiplicity=Multiplicity(0, 9999))
    }
)
Measure_Element: BinaryAssociation = BinaryAssociation(
    name="Measure_Element",
    ends={
        Property(name="measure", type=Measure, multiplicity=Multiplicity(0, 9999)),
        Property(name="measurand", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
Measure_Metric: BinaryAssociation = BinaryAssociation(
    name="Measure_Metric",
    ends={
        Property(name="measures", type=Measure, multiplicity=Multiplicity(0, 9999)),
        Property(name="metric", type=Metric, multiplicity=Multiplicity(1, 1))
    }
)
Measure_Observation: BinaryAssociation = BinaryAssociation(
    name="Measure_Observation",
    ends={
        Property(name="measures", type=Measure, multiplicity=Multiplicity(0, 9999)),
        Property(name="observation", type=Observation, multiplicity=Multiplicity(1, 1))
    }
)
Datashape_Feature: BinaryAssociation = BinaryAssociation(
    name="Datashape_Feature",
    ends={
        Property(name="date", type=Datashape, multiplicity=Multiplicity(0, 9999)),
        Property(name="f_date", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
ConfParam_Configuration: BinaryAssociation = BinaryAssociation(
    name="ConfParam_Configuration",
    ends={
        Property(name="params", type=ConfParam, multiplicity=Multiplicity(0, 9999)),
        Property(name="conf", type=Configuration, multiplicity=Multiplicity(1, 1))
    }
)
Datashape_Feature_1: BinaryAssociation = BinaryAssociation(
    name="Datashape_Feature_1",
    ends={
        Property(name="features", type=Datashape, multiplicity=Multiplicity(1, 1)),
        Property(name="f_features", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
Evaluation_Observation: BinaryAssociation = BinaryAssociation(
    name="Evaluation_Observation",
    ends={
        Property(name="eval", type=Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="observations", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
Derived_Metric: BinaryAssociation = BinaryAssociation(
    name="Derived_Metric",
    ends={
        Property(name="derivedBy", type=Derived, multiplicity=Multiplicity(0, 9999)),
        Property(name="baseMetric", type=Metric, multiplicity=Multiplicity(1, 9999))
    }
)
Configuration_Evaluation: BinaryAssociation = BinaryAssociation(
    name="Configuration_Evaluation",
    ends={
        Property(name="config", type=Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="eval", type=Evaluation, multiplicity=Multiplicity(0, 9999))
    }
)
Project_Evaluation: BinaryAssociation = BinaryAssociation(
    name="Project_Evaluation",
    ends={
        Property(name="project", type=Project, multiplicity=Multiplicity(1, 1)),
        Property(name="eval", type=Evaluation, multiplicity=Multiplicity(0, 9999))
    }
)
Project_Element: BinaryAssociation = BinaryAssociation(
    name="Project_Element",
    ends={
        Property(name="project", type=Project, multiplicity=Multiplicity(0, 1)),
        Property(name="involves", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
evaluates_eval: BinaryAssociation = BinaryAssociation(
    name="evaluates_eval",
    ends={
        Property(name="evalu", type=Evaluation, multiplicity=Multiplicity(0, 9999)),
        Property(name="evaluates", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
Evaluation_Element: BinaryAssociation = BinaryAssociation(
    name="Evaluation_Element",
    ends={
        Property(name="eval", type=Evaluation, multiplicity=Multiplicity(0, 9999)),
        Property(name="ref", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
AISystem_Dataset: BinaryAssociation = BinaryAssociation(
    name="AISystem_Dataset",
    ends={
        Property(name="models", type=AISystem, multiplicity=Multiplicity(0, 9999)),
        Property(name="dataset", type=Dataset, multiplicity=Multiplicity(1, 9999))
    }
)
Tool_Observation: BinaryAssociation = BinaryAssociation(
    name="Tool_Observation",
    ends={
        Property(name="tool", type=Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="observation_1", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
Datashape_Dataset: BinaryAssociation = BinaryAssociation(
    name="Datashape_Dataset",
    ends={
        Property(name="datashape", type=Datashape, multiplicity=Multiplicity(1, 1)),
        Property(name="dataset_1", type=Dataset, multiplicity=Multiplicity(0, 9999))
    }
)
Dataset_Observation: BinaryAssociation = BinaryAssociation(
    name="Dataset_Observation",
    ends={
        Property(name="dataset", type=Dataset, multiplicity=Multiplicity(1, 1)),
        Property(name="observation_2", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
LegalRequirement_Project: BinaryAssociation = BinaryAssociation(
    name="LegalRequirement_Project",
    ends={
        Property(name="legal_requirements", type=LegalRequirement, multiplicity=Multiplicity(0, 9999)),
        Property(name="project_1", type=Project, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_MetricCategory_AssessmentElement = Generalization(general=AssessmentElement, specific=MetricCategory)
gen_Metric_AssessmentElement = Generalization(general=AssessmentElement, specific=Metric)
gen_Observation_AssessmentElement = Generalization(general=AssessmentElement, specific=Observation)
gen_Direct_Metric = Generalization(general=Metric, specific=Direct)
gen_Derived_Metric = Generalization(general=Metric, specific=Derived)
gen_AISystem_Element = Generalization(general=Element, specific=AISystem)
gen_Element_AssessmentElement = Generalization(general=AssessmentElement, specific=Element)
gen_Configuration_AssessmentElement = Generalization(general=AssessmentElement, specific=Configuration)
gen_ConfParam_AssessmentElement = Generalization(general=AssessmentElement, specific=ConfParam)
gen_Dataset_Element = Generalization(general=Element, specific=Dataset)
gen_Feature_Element = Generalization(general=Element, specific=Feature)
gen_Tool_AssessmentElement = Generalization(general=AssessmentElement, specific=Tool)

# Domain Model
domain_model = DomainModel(
    name="AI_Sandbox",
    types={Project, Dataset, Datashape, Feature, MetricCategory, Configuration, Metric, ConfParam, AssessmentElement, Element, Tool, LegalRequirement, Measure, Observation, Evaluation, Direct, Derived, AISystem, EvaluationStatus, ProjectStatus, DatasetType, LicensingType, VerificationType, TagsVerificationTarget, TagsSector, TagsTargetSystem},
    associations={MetricCategory_Metric, Measure_Element, Measure_Metric, Measure_Observation, Datashape_Feature, ConfParam_Configuration, Datashape_Feature_1, Evaluation_Observation, Derived_Metric, Configuration_Evaluation, Project_Evaluation, Project_Element, evaluates_eval, Evaluation_Element, AISystem_Dataset, Tool_Observation, Datashape_Dataset, Dataset_Observation, LegalRequirement_Project},
    generalizations={gen_MetricCategory_AssessmentElement, gen_Metric_AssessmentElement, gen_Observation_AssessmentElement, gen_Direct_Metric, gen_Derived_Metric, gen_AISystem_Element, gen_Element_AssessmentElement, gen_Configuration_AssessmentElement, gen_ConfParam_AssessmentElement, gen_Dataset_Element, gen_Feature_Element, gen_Tool_AssessmentElement},
    metadata=None
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="New project")
project = Project(
    name="skillset_match",
    models=[domain_model],
    owner="User",
    metadata=metadata
)
