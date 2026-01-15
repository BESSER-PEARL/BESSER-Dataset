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
Effect: Enumeration = Enumeration(
    name="Effect",
    literals={
            EnumerationLiteral(name="NEGATIVE"),
			EnumerationLiteral(name="POSITIVE")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="FINDINGS"),
			EnumerationLiteral(name="NUMBER")
    }
)

# Classes
qm_QualityModel = Class(name="qm::QualityModel")
NamedElement = Class(name="NamedElement")
qm_Evaluation = Class(name="qm::Evaluation", is_abstract=True)
qm_Measure = Class(name="qm::Measure")
qm_MeasurementMethod = Class(name="qm::MeasurementMethod", is_abstract=True)
qm_Tool = Class(name="qm::Tool")
qm_Tag = Class(name="qm::Tag")
qm_Source = Class(name="qm::Source")
qm_QualityModelElement = Class(name="qm::QualityModelElement", is_abstract=True)
qm_DescribedElement = Class(name="qm::DescribedElement", is_abstract=True)
AnnotatedElement = Class(name="AnnotatedElement")
qm_Entity = Class(name="qm::Entity")
qm_NamedElement = Class(name="qm::NamedElement", is_abstract=True)
DescribedElement = Class(name="DescribedElement")
qm_Factor = Class(name="qm::Factor")
qm_Annotation = Class(name="qm::Annotation")
qm_AnnotationBase = Class(name="qm::AnnotationBase", is_abstract=True)
qm_TaggedElement = Class(name="qm::TaggedElement", is_abstract=True)
QualityModelElement = Class(name="QualityModelElement")
qm_Specialization = Class(name="qm::Specialization")
qm_Decomposition = Class(name="qm::Decomposition")
qm_AnnotatedElement = Class(name="qm::AnnotatedElement", is_abstract=True)
TaggedElement = Class(name="TaggedElement")
qm_CharacterizingElement = Class(name="qm::CharacterizingElement", is_abstract=True)
CharacterizingElement = Class(name="CharacterizingElement")
qm_Impact = Class(name="qm::Impact")
qm_FactorRefinement = Class(name="qm::FactorRefinement")
qm_Measurement = Class(name="qm::Measurement")
qm_MeasureRefinement = Class(name="qm::MeasureRefinement")
qm_MeasureAggregation = Class(name="qm::MeasureAggregation", is_abstract=True)
MeasurementMethod = Class(name="MeasurementMethod")
qm_Instrument = Class(name="qm::Instrument", is_abstract=True)
qm_ManualInstrument = Class(name="qm::ManualInstrument")
Instrument = Class(name="Instrument")
qm_ToolBasedInstrument = Class(name="qm::ToolBasedInstrument")
qm_QIESLEvaluation = Class(name="qm::QIESLEvaluation")
TextEvaluation = Class(name="TextEvaluation")
qm_TextEvaluation = Class(name="qm::TextEvaluation")
Evaluation = Class(name="Evaluation")
qm_FormBasedEvaluation = Class(name="qm::FormBasedEvaluation", is_abstract=True)
qm_SingleMeasureEvaluation = Class(name="qm::SingleMeasureEvaluation")
FormBasedEvaluation = Class(name="FormBasedEvaluation")
MeasureEvaluation = Class(name="MeasureEvaluation")
qm_FactorAggregation = Class(name="qm::FactorAggregation", is_abstract=True)
qm_NormalizationMeasure = Class(name="qm::NormalizationMeasure")
Measure = Class(name="Measure")
qm_QIESLAggregation = Class(name="qm::QIESLAggregation")
TextAggregation = Class(name="TextAggregation")
qm_TextAggregation = Class(name="qm::TextAggregation")
MeasureAggregation = Class(name="MeasureAggregation")
qm_Function = Class(name="qm::Function", is_abstract=True)
qm_LinearIncreasingFunction = Class(name="qm::LinearIncreasingFunction")
LinearFunction = Class(name="LinearFunction")
qm_LinearDecreasingFunction = Class(name="qm::LinearDecreasingFunction")
qm_WeightedSumFactorAggregation = Class(name="qm::WeightedSumFactorAggregation")
FactorAggregation = Class(name="FactorAggregation")
qm_FindingsUnionMeasureAggregation = Class(name="qm::FindingsUnionMeasureAggregation")
FormBasedMeasureAggregation = Class(name="FormBasedMeasureAggregation")
qm_NumberMeanMeasureAggregation = Class(name="qm::NumberMeanMeasureAggregation")
qm_ManualEvaluation = Class(name="qm::ManualEvaluation")
qm_MeasureEvaluation = Class(name="qm::MeasureEvaluation", is_abstract=True)
qm_Ranking = Class(name="qm::Ranking", is_abstract=True)
qm_MultiMeasureEvaluation = Class(name="qm::MultiMeasureEvaluation", is_abstract=True)
qm_WeightedSumMultiMeasureEvaluation = Class(name="qm::WeightedSumMultiMeasureEvaluation")
MultiMeasureEvaluation = Class(name="MultiMeasureEvaluation")
qm_MeasureRanking = Class(name="qm::MeasureRanking")
qm_QualityModelResult = Class(name="qm::QualityModelResult")
qm_MeasurementResult = Class(name="qm::MeasurementResult", is_abstract=True)
qm_EvaluationResult = Class(name="qm::EvaluationResult")
qm_FormBasedMeasureAggregation = Class(name="qm::FormBasedMeasureAggregation", is_abstract=True)
qm_FactorRanking = Class(name="qm::FactorRanking")
Ranking = Class(name="Ranking")
qm_LinearFunction = Class(name="qm::LinearFunction", is_abstract=True)
Function = Class(name="Function")
qm_DoubleInterval = Class(name="qm::DoubleInterval")
qm_FindingsMeasurementResult = Class(name="qm::FindingsMeasurementResult")
qm_FindingMessage = Class(name="qm::FindingMessage")
qm_SingleMeasureEvaluationResult = Class(name="qm::SingleMeasureEvaluationResult")
EvaluationResult = Class(name="EvaluationResult")
qm_MultiMeasureEvaluationResult = Class(name="qm::MultiMeasureEvaluationResult")
qm_MeasureRankingEvaluationResult = Class(name="qm::MeasureRankingEvaluationResult")
qm_Result = Class(name="qm::Result", is_abstract=True)
Result = Class(name="Result")
qm_NumberMeasurementResult = Class(name="qm::NumberMeasurementResult")
MeasurementResult = Class(name="MeasurementResult")

# qm_QualityModel class attributes and methods
qm_QualityModel_schoolGradeBoundary2: Property = Property(name="schoolGradeBoundary2", type=StringType)
qm_QualityModel_schoolGradeBoundary3: Property = Property(name="schoolGradeBoundary3", type=StringType)
qm_QualityModel_schoolGradeBoundary4: Property = Property(name="schoolGradeBoundary4", type=StringType)
qm_QualityModel_schoolGradeBoundary5: Property = Property(name="schoolGradeBoundary5", type=StringType)
qm_QualityModel_schoolGradeBoundary6: Property = Property(name="schoolGradeBoundary6", type=StringType)
qm_QualityModel.attributes={qm_QualityModel_schoolGradeBoundary6, qm_QualityModel_schoolGradeBoundary5, qm_QualityModel_schoolGradeBoundary2, qm_QualityModel_schoolGradeBoundary4, qm_QualityModel_schoolGradeBoundary3}

# NamedElement class attributes and methods

# qm_Evaluation class attributes and methods
qm_Evaluation_maximumPoints: Property = Property(name="maximumPoints", type=IntegerType)
qm_Evaluation_completeness: Property = Property(name="completeness", type=IntegerType)
qm_Evaluation.attributes={qm_Evaluation_maximumPoints, qm_Evaluation_completeness}

# qm_Measure class attributes and methods
qm_Measure_type: Property = Property(name="type", type=StringType)
qm_Measure.attributes={qm_Measure_type}

# qm_MeasurementMethod class attributes and methods

# qm_Tool class attributes and methods

# qm_Tag class attributes and methods

# qm_Source class attributes and methods

# qm_QualityModelElement class attributes and methods
qm_QualityModelElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
qm_QualityModelElement.attributes={qm_QualityModelElement_qualifiedName}

# qm_DescribedElement class attributes and methods
qm_DescribedElement_description: Property = Property(name="description", type=StringType)
qm_DescribedElement.attributes={qm_DescribedElement_description}

# AnnotatedElement class attributes and methods

# qm_Entity class attributes and methods
qm_Entity_stakeholder: Property = Property(name="stakeholder", type=BooleanType)
qm_Entity_useCase: Property = Property(name="useCase", type=BooleanType)
qm_Entity.attributes={qm_Entity_useCase, qm_Entity_stakeholder}

# qm_NamedElement class attributes and methods
qm_NamedElement_name: Property = Property(name="name", type=StringType)
qm_NamedElement_title: Property = Property(name="title", type=StringType)
qm_NamedElement.attributes={qm_NamedElement_title, qm_NamedElement_name}

# DescribedElement class attributes and methods

# qm_Factor class attributes and methods

# qm_Annotation class attributes and methods
qm_Annotation_key: Property = Property(name="key", type=StringType)
qm_Annotation_value: Property = Property(name="value", type=StringType)
qm_Annotation.attributes={qm_Annotation_key, qm_Annotation_value}

# qm_AnnotationBase class attributes and methods

# qm_TaggedElement class attributes and methods

# QualityModelElement class attributes and methods

# qm_Specialization class attributes and methods

# qm_Decomposition class attributes and methods

# qm_AnnotatedElement class attributes and methods

# TaggedElement class attributes and methods

# qm_CharacterizingElement class attributes and methods

# CharacterizingElement class attributes and methods

# qm_Impact class attributes and methods
qm_Impact_justification: Property = Property(name="justification", type=StringType)
qm_Impact_effect: Property = Property(name="effect", type=StringType)
qm_Impact.attributes={qm_Impact_justification, qm_Impact_effect}

# qm_FactorRefinement class attributes and methods

# qm_Measurement class attributes and methods

# qm_MeasureRefinement class attributes and methods

# qm_MeasureAggregation class attributes and methods

# MeasurementMethod class attributes and methods

# qm_Instrument class attributes and methods

# qm_ManualInstrument class attributes and methods

# Instrument class attributes and methods

# qm_ToolBasedInstrument class attributes and methods
qm_ToolBasedInstrument_metric: Property = Property(name="metric", type=StringType)
qm_ToolBasedInstrument.attributes={qm_ToolBasedInstrument_metric}

# qm_QIESLEvaluation class attributes and methods

# TextEvaluation class attributes and methods

# qm_TextEvaluation class attributes and methods
qm_TextEvaluation_specification: Property = Property(name="specification", type=StringType)
qm_TextEvaluation.attributes={qm_TextEvaluation_specification}

# Evaluation class attributes and methods

# qm_FormBasedEvaluation class attributes and methods

# qm_SingleMeasureEvaluation class attributes and methods

# FormBasedEvaluation class attributes and methods

# MeasureEvaluation class attributes and methods

# qm_FactorAggregation class attributes and methods

# qm_NormalizationMeasure class attributes and methods

# Measure class attributes and methods

# qm_QIESLAggregation class attributes and methods

# TextAggregation class attributes and methods

# qm_TextAggregation class attributes and methods
qm_TextAggregation_specification: Property = Property(name="specification", type=StringType)
qm_TextAggregation.attributes={qm_TextAggregation_specification}

# MeasureAggregation class attributes and methods

# qm_Function class attributes and methods

# qm_LinearIncreasingFunction class attributes and methods

# LinearFunction class attributes and methods

# qm_LinearDecreasingFunction class attributes and methods

# qm_WeightedSumFactorAggregation class attributes and methods

# FactorAggregation class attributes and methods

# qm_FindingsUnionMeasureAggregation class attributes and methods

# FormBasedMeasureAggregation class attributes and methods

# qm_NumberMeanMeasureAggregation class attributes and methods

# qm_ManualEvaluation class attributes and methods

# qm_MeasureEvaluation class attributes and methods
qm_MeasureEvaluation_range: Property = Property(name="range", type=StringType)
qm_MeasureEvaluation.attributes={qm_MeasureEvaluation_range}

# qm_Ranking class attributes and methods
qm_Ranking_rank: Property = Property(name="rank", type=IntegerType)
qm_Ranking_weight: Property = Property(name="weight", type=FloatType)
qm_Ranking.attributes={qm_Ranking_rank, qm_Ranking_weight}

# qm_MultiMeasureEvaluation class attributes and methods

# qm_WeightedSumMultiMeasureEvaluation class attributes and methods

# MultiMeasureEvaluation class attributes and methods

# qm_MeasureRanking class attributes and methods

# qm_QualityModelResult class attributes and methods
qm_QualityModelResult_system: Property = Property(name="system", type=StringType)
qm_QualityModelResult_date: Property = Property(name="date", type=DateType)
qm_QualityModelResult.attributes={qm_QualityModelResult_system, qm_QualityModelResult_date}

# qm_MeasurementResult class attributes and methods

# qm_EvaluationResult class attributes and methods

# qm_FormBasedMeasureAggregation class attributes and methods

# qm_FactorRanking class attributes and methods

# Ranking class attributes and methods

# qm_LinearFunction class attributes and methods
qm_LinearFunction_lowerBound: Property = Property(name="lowerBound", type=FloatType)
qm_LinearFunction_upperBound: Property = Property(name="upperBound", type=FloatType)
qm_LinearFunction.attributes={qm_LinearFunction_upperBound, qm_LinearFunction_lowerBound}

# Function class attributes and methods

# qm_DoubleInterval class attributes and methods
qm_DoubleInterval_lower: Property = Property(name="lower", type=FloatType)
qm_DoubleInterval_upper: Property = Property(name="upper", type=FloatType)
qm_DoubleInterval.attributes={qm_DoubleInterval_upper, qm_DoubleInterval_lower}

# qm_FindingsMeasurementResult class attributes and methods
qm_FindingsMeasurementResult_count: Property = Property(name="count", type=IntegerType)
qm_FindingsMeasurementResult_findings: Property = Property(name="findings", type=StringType)
qm_FindingsMeasurementResult.attributes={qm_FindingsMeasurementResult_findings, qm_FindingsMeasurementResult_count}

# qm_FindingMessage class attributes and methods
qm_FindingMessage_message: Property = Property(name="message", type=StringType)
qm_FindingMessage_location: Property = Property(name="location", type=StringType)
qm_FindingMessage.attributes={qm_FindingMessage_location, qm_FindingMessage_message}

# qm_SingleMeasureEvaluationResult class attributes and methods
qm_SingleMeasureEvaluationResult_ratioAffected: Property = Property(name="ratioAffected", type=FloatType)
qm_SingleMeasureEvaluationResult.attributes={qm_SingleMeasureEvaluationResult_ratioAffected}

# EvaluationResult class attributes and methods

# qm_MultiMeasureEvaluationResult class attributes and methods

# qm_MeasureRankingEvaluationResult class attributes and methods
qm_MeasureRankingEvaluationResult_ratioAffected: Property = Property(name="ratioAffected", type=FloatType)
qm_MeasureRankingEvaluationResult.attributes={qm_MeasureRankingEvaluationResult_ratioAffected}

# qm_Result class attributes and methods
qm_Result_message: Property = Property(name="message", type=StringType)
qm_Result.attributes={qm_Result_message}

# Result class attributes and methods

# qm_NumberMeasurementResult class attributes and methods

# MeasurementResult class attributes and methods

# Relationships
evaluations3: BinaryAssociation = BinaryAssociation(
    name="evaluations3",
    ends={
        Property(name="Evaluation", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel4", type=qm_Evaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measures5: BinaryAssociation = BinaryAssociation(
    name="measures5",
    ends={
        Property(name="Measure", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel6", type=qm_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurementMethods7: BinaryAssociation = BinaryAssociation(
    name="measurementMethods7",
    ends={
        Property(name="MeasurementMethod", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel8", type=qm_MeasurementMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools9: BinaryAssociation = BinaryAssociation(
    name="tools9",
    ends={
        Property(name="Tool", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel10", type=qm_Tool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags11: BinaryAssociation = BinaryAssociation(
    name="tags11",
    ends={
        Property(name="Tag", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel12", type=qm_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources13: BinaryAssociation = BinaryAssociation(
    name="sources13",
    ends={
        Property(name="Source", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel14", type=qm_Source, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requires16: BinaryAssociation = BinaryAssociation(
    name="requires16",
    ends={
        Property(name="qm_QualityModel", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_QualityModel15", type=qm_QualityModel, multiplicity=Multiplicity(0, 9999))
    }
)
originatesFrom17: BinaryAssociation = BinaryAssociation(
    name="originatesFrom17",
    ends={
        Property(name="qm_Source", type=qm_QualityModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_QualityModelElement", type=qm_Source, multiplicity=Multiplicity(0, 9999))
    }
)
qualityModel18: BinaryAssociation = BinaryAssociation(
    name="qualityModel18",
    ends={
        Property(name="QualityModel", type=qm_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="Entity", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel", type=qm_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors1: BinaryAssociation = BinaryAssociation(
    name="factors1",
    ends={
        Property(name="Factor", type=qm_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qualityModel2", type=qm_Factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations19: BinaryAssociation = BinaryAssociation(
    name="annotations19",
    ends={
        Property(name="qm_Annotation", type=qm_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_AnnotatedElement", type=qm_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
advancedAnnotations20: BinaryAssociation = BinaryAssociation(
    name="advancedAnnotations20",
    ends={
        Property(name="qm_AnnotationBase", type=qm_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_AnnotatedElement21", type=qm_AnnotationBase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualityModel22: BinaryAssociation = BinaryAssociation(
    name="qualityModel22",
    ends={
        Property(name="QualityModel23", type=qm_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tags", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
taggedBy24: BinaryAssociation = BinaryAssociation(
    name="taggedBy24",
    ends={
        Property(name="qm_Tag", type=qm_TaggedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_TaggedElement", type=qm_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
isA25: BinaryAssociation = BinaryAssociation(
    name="isA25",
    ends={
        Property(name="Specialization", type=qm_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=qm_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isADirect27: BinaryAssociation = BinaryAssociation(
    name="isADirect27",
    ends={
        Property(name="qm_Entity", type=qm_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Entity26", type=qm_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
partOf28: BinaryAssociation = BinaryAssociation(
    name="partOf28",
    ends={
        Property(name="Decomposition", type=qm_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="child29", type=qm_Decomposition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partOfDirect31: BinaryAssociation = BinaryAssociation(
    name="partOfDirect31",
    ends={
        Property(name="qm_Entity32", type=qm_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Entity30", type=qm_Entity, multiplicity=Multiplicity(0, 1))
    }
)
qualityModel33: BinaryAssociation = BinaryAssociation(
    name="qualityModel33",
    ends={
        Property(name="QualityModel34", type=qm_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
parent39: BinaryAssociation = BinaryAssociation(
    name="parent39",
    ends={
        Property(name="qm_Entity40", type=qm_Decomposition, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Decomposition", type=qm_Entity, multiplicity=Multiplicity(1, 1))
    }
)
child41: BinaryAssociation = BinaryAssociation(
    name="child41",
    ends={
        Property(name="Entity42", type=qm_Decomposition, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf", type=qm_Entity, multiplicity=Multiplicity(1, 1))
    }
)
characterizes43: BinaryAssociation = BinaryAssociation(
    name="characterizes43",
    ends={
        Property(name="qm_Entity44", type=qm_CharacterizingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_CharacterizingElement", type=qm_Entity, multiplicity=Multiplicity(0, 1))
    }
)
influences45: BinaryAssociation = BinaryAssociation(
    name="influences45",
    ends={
        Property(name="Impact", type=qm_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=qm_Impact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
influencesDirect47: BinaryAssociation = BinaryAssociation(
    name="influencesDirect47",
    ends={
        Property(name="qm_Factor", type=qm_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Factor46", type=qm_Factor, multiplicity=Multiplicity(0, 9999))
    }
)
refines48: BinaryAssociation = BinaryAssociation(
    name="refines48",
    ends={
        Property(name="FactorRefinement", type=qm_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="child49", type=qm_FactorRefinement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinesDirect51: BinaryAssociation = BinaryAssociation(
    name="refinesDirect51",
    ends={
        Property(name="qm_Factor52", type=qm_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Factor50", type=qm_Factor, multiplicity=Multiplicity(0, 9999))
    }
)
qualityModel53: BinaryAssociation = BinaryAssociation(
    name="qualityModel53",
    ends={
        Property(name="QualityModel54", type=qm_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="factors", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
source55: BinaryAssociation = BinaryAssociation(
    name="source55",
    ends={
        Property(name="Factor56", type=qm_Impact, multiplicity=Multiplicity(1, 1)),
        Property(name="influences", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
target57: BinaryAssociation = BinaryAssociation(
    name="target57",
    ends={
        Property(name="qm_Factor58", type=qm_Impact, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Impact", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
parent35: BinaryAssociation = BinaryAssociation(
    name="parent35",
    ends={
        Property(name="qm_Entity36", type=qm_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Specialization", type=qm_Entity, multiplicity=Multiplicity(1, 1))
    }
)
child37: BinaryAssociation = BinaryAssociation(
    name="child37",
    ends={
        Property(name="Entity38", type=qm_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="isA", type=qm_Entity, multiplicity=Multiplicity(1, 1))
    }
)
evaluates59: BinaryAssociation = BinaryAssociation(
    name="evaluates59",
    ends={
        Property(name="qm_Factor60", type=qm_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Evaluation", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
qualityModel61: BinaryAssociation = BinaryAssociation(
    name="qualityModel61",
    ends={
        Property(name="QualityModel62", type=qm_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluations", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
child63: BinaryAssociation = BinaryAssociation(
    name="child63",
    ends={
        Property(name="Factor64", type=qm_FactorRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="refines", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
parent65: BinaryAssociation = BinaryAssociation(
    name="parent65",
    ends={
        Property(name="qm_Factor66", type=qm_FactorRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_FactorRefinement", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
parent67: BinaryAssociation = BinaryAssociation(
    name="parent67",
    ends={
        Property(name="qm_Factor68", type=qm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Measurement", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
child69: BinaryAssociation = BinaryAssociation(
    name="child69",
    ends={
        Property(name="Measure70", type=qm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="measures", type=qm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
parent71: BinaryAssociation = BinaryAssociation(
    name="parent71",
    ends={
        Property(name="qm_Measure", type=qm_MeasureRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasureRefinement", type=qm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
child72: BinaryAssociation = BinaryAssociation(
    name="child72",
    ends={
        Property(name="Measure74", type=qm_MeasureRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="refines73", type=qm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
measures75: BinaryAssociation = BinaryAssociation(
    name="measures75",
    ends={
        Property(name="Measurement", type=qm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="child76", type=qm_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measuresDirect77: BinaryAssociation = BinaryAssociation(
    name="measuresDirect77",
    ends={
        Property(name="qm_Factor79", type=qm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Measure78", type=qm_Factor, multiplicity=Multiplicity(0, 9999))
    }
)
determines88: BinaryAssociation = BinaryAssociation(
    name="determines88",
    ends={
        Property(name="qm_Measure89", type=qm_MeasurementMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasurementMethod", type=qm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
qualityModel90: BinaryAssociation = BinaryAssociation(
    name="qualityModel90",
    ends={
        Property(name="QualityModel91", type=qm_MeasurementMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="measurementMethods", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
tool92: BinaryAssociation = BinaryAssociation(
    name="tool92",
    ends={
        Property(name="qm_Tool", type=qm_ToolBasedInstrument, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_ToolBasedInstrument", type=qm_Tool, multiplicity=Multiplicity(1, 1))
    }
)
qualityModel93: BinaryAssociation = BinaryAssociation(
    name="qualityModel93",
    ends={
        Property(name="QualityModel94", type=qm_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="tools", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
qualityModel80: BinaryAssociation = BinaryAssociation(
    name="qualityModel80",
    ends={
        Property(name="QualityModel82", type=qm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="measures81", type=qm_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
refines83: BinaryAssociation = BinaryAssociation(
    name="refines83",
    ends={
        Property(name="MeasureRefinement", type=qm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="child84", type=qm_MeasureRefinement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinesDirect86: BinaryAssociation = BinaryAssociation(
    name="refinesDirect86",
    ends={
        Property(name="qm_Measure87", type=qm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_Measure85", type=qm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
rankings97: BinaryAssociation = BinaryAssociation(
    name="rankings97",
    ends={
        Property(name="qm_FactorRanking98", type=qm_WeightedSumFactorAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_WeightedSumFactorAggregation", type=qm_FactorRanking, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
measure99: BinaryAssociation = BinaryAssociation(
    name="measure99",
    ends={
        Property(name="qm_Measure100", type=qm_MeasureEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasureEvaluation", type=qm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
normlizationMeasure101: BinaryAssociation = BinaryAssociation(
    name="normlizationMeasure101",
    ends={
        Property(name="qm_NormalizationMeasure", type=qm_MeasureEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasureEvaluation102", type=qm_NormalizationMeasure, multiplicity=Multiplicity(0, 1))
    }
)
function103: BinaryAssociation = BinaryAssociation(
    name="function103",
    ends={
        Property(name="qm_Function", type=qm_MeasureEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasureEvaluation104", type=qm_Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rankings105: BinaryAssociation = BinaryAssociation(
    name="rankings105",
    ends={
        Property(name="qm_MeasureRanking", type=qm_WeightedSumMultiMeasureEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_WeightedSumMultiMeasureEvaluation", type=qm_MeasureRanking, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
measurementResults106: BinaryAssociation = BinaryAssociation(
    name="measurementResults106",
    ends={
        Property(name="qm_MeasurementResult", type=qm_QualityModelResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_QualityModelResult", type=qm_MeasurementResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factor95: BinaryAssociation = BinaryAssociation(
    name="factor95",
    ends={
        Property(name="qm_Factor96", type=qm_FactorRanking, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_FactorRanking", type=qm_Factor, multiplicity=Multiplicity(1, 1))
    }
)
value112: BinaryAssociation = BinaryAssociation(
    name="value112",
    ends={
        Property(name="qm_DoubleInterval", type=qm_NumberMeasurementResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_NumberMeasurementResult", type=qm_DoubleInterval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
findingMessages113: BinaryAssociation = BinaryAssociation(
    name="findingMessages113",
    ends={
        Property(name="qm_FindingMessage", type=qm_FindingsMeasurementResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_FindingsMeasurementResult", type=qm_FindingMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value114: BinaryAssociation = BinaryAssociation(
    name="value114",
    ends={
        Property(name="qm_DoubleInterval116", type=qm_EvaluationResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_EvaluationResult115", type=qm_DoubleInterval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultsFrom117: BinaryAssociation = BinaryAssociation(
    name="resultsFrom117",
    ends={
        Property(name="qm_Evaluation119", type=qm_EvaluationResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_EvaluationResult118", type=qm_Evaluation, multiplicity=Multiplicity(1, 1))
    }
)
evaluationResults120: BinaryAssociation = BinaryAssociation(
    name="evaluationResults120",
    ends={
        Property(name="qm_MeasureRankingEvaluationResult", type=qm_MultiMeasureEvaluationResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MultiMeasureEvaluationResult", type=qm_MeasureRankingEvaluationResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value121: BinaryAssociation = BinaryAssociation(
    name="value121",
    ends={
        Property(name="qm_DoubleInterval123", type=qm_MeasureRankingEvaluationResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasureRankingEvaluationResult122", type=qm_DoubleInterval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultsFrom124: BinaryAssociation = BinaryAssociation(
    name="resultsFrom124",
    ends={
        Property(name="qm_MeasureRanking126", type=qm_MeasureRankingEvaluationResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasureRankingEvaluationResult125", type=qm_MeasureRanking, multiplicity=Multiplicity(1, 1))
    }
)
evaluationResults107: BinaryAssociation = BinaryAssociation(
    name="evaluationResults107",
    ends={
        Property(name="qm_EvaluationResult", type=qm_QualityModelResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_QualityModelResult108", type=qm_EvaluationResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultsFrom109: BinaryAssociation = BinaryAssociation(
    name="resultsFrom109",
    ends={
        Property(name="qm_MeasurementMethod111", type=qm_MeasurementResult, multiplicity=Multiplicity(1, 1)),
        Property(name="qm_MeasurementResult110", type=qm_MeasurementMethod, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_qm_Source_NamedElement = Generalization(general=NamedElement, specific=qm_Source)
gen_qm_DescribedElement_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_DescribedElement)
gen_qm_QualityModel_NamedElement = Generalization(general=NamedElement, specific=qm_QualityModel)
gen_qm_NamedElement_DescribedElement = Generalization(general=DescribedElement, specific=qm_NamedElement)
gen_qm_Tag_NamedElement = Generalization(general=NamedElement, specific=qm_Tag)
gen_qm_TaggedElement_QualityModelElement = Generalization(general=QualityModelElement, specific=qm_TaggedElement)
gen_qm_Entity_NamedElement = Generalization(general=NamedElement, specific=qm_Entity)
gen_qm_AnnotatedElement_TaggedElement = Generalization(general=TaggedElement, specific=qm_AnnotatedElement)
gen_qm_CharacterizingElement_NamedElement = Generalization(general=NamedElement, specific=qm_CharacterizingElement)
gen_qm_Factor_CharacterizingElement = Generalization(general=CharacterizingElement, specific=qm_Factor)
gen_qm_Impact_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_Impact)
gen_qm_Specialization_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_Specialization)
gen_qm_Decomposition_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_Decomposition)
gen_qm_Evaluation_NamedElement = Generalization(general=NamedElement, specific=qm_Evaluation)
gen_qm_FactorRefinement_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_FactorRefinement)
gen_qm_Measurement_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_Measurement)
gen_qm_MeasureRefinement_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_MeasureRefinement)
gen_qm_Measure_CharacterizingElement = Generalization(general=CharacterizingElement, specific=qm_Measure)
gen_qm_MeasurementMethod_AnnotatedElement = Generalization(general=AnnotatedElement, specific=qm_MeasurementMethod)
gen_qm_MeasureAggregation_MeasurementMethod = Generalization(general=MeasurementMethod, specific=qm_MeasureAggregation)
gen_qm_MeasureAggregation_NamedElement = Generalization(general=NamedElement, specific=qm_MeasureAggregation)
gen_qm_Instrument_MeasurementMethod = Generalization(general=MeasurementMethod, specific=qm_Instrument)
gen_qm_ManualInstrument_Instrument = Generalization(general=Instrument, specific=qm_ManualInstrument)
gen_qm_ManualInstrument_NamedElement = Generalization(general=NamedElement, specific=qm_ManualInstrument)
gen_qm_ToolBasedInstrument_Instrument = Generalization(general=Instrument, specific=qm_ToolBasedInstrument)
gen_qm_Tool_NamedElement = Generalization(general=NamedElement, specific=qm_Tool)
gen_qm_QIESLEvaluation_TextEvaluation = Generalization(general=TextEvaluation, specific=qm_QIESLEvaluation)
gen_qm_TextEvaluation_Evaluation = Generalization(general=Evaluation, specific=qm_TextEvaluation)
gen_qm_FormBasedEvaluation_Evaluation = Generalization(general=Evaluation, specific=qm_FormBasedEvaluation)
gen_qm_SingleMeasureEvaluation_FormBasedEvaluation = Generalization(general=FormBasedEvaluation, specific=qm_SingleMeasureEvaluation)
gen_qm_SingleMeasureEvaluation_MeasureEvaluation = Generalization(general=MeasureEvaluation, specific=qm_SingleMeasureEvaluation)
gen_qm_FactorAggregation_FormBasedEvaluation = Generalization(general=FormBasedEvaluation, specific=qm_FactorAggregation)
gen_qm_NormalizationMeasure_Measure = Generalization(general=Measure, specific=qm_NormalizationMeasure)
gen_qm_QIESLAggregation_TextAggregation = Generalization(general=TextAggregation, specific=qm_QIESLAggregation)
gen_qm_TextAggregation_MeasureAggregation = Generalization(general=MeasureAggregation, specific=qm_TextAggregation)
gen_qm_LinearIncreasingFunction_LinearFunction = Generalization(general=LinearFunction, specific=qm_LinearIncreasingFunction)
gen_qm_LinearDecreasingFunction_LinearFunction = Generalization(general=LinearFunction, specific=qm_LinearDecreasingFunction)
gen_qm_WeightedSumFactorAggregation_FactorAggregation = Generalization(general=FactorAggregation, specific=qm_WeightedSumFactorAggregation)
gen_qm_FindingsUnionMeasureAggregation_FormBasedMeasureAggregation = Generalization(general=FormBasedMeasureAggregation, specific=qm_FindingsUnionMeasureAggregation)
gen_qm_NumberMeanMeasureAggregation_FormBasedMeasureAggregation = Generalization(general=FormBasedMeasureAggregation, specific=qm_NumberMeanMeasureAggregation)
gen_qm_ManualEvaluation_Evaluation = Generalization(general=Evaluation, specific=qm_ManualEvaluation)
gen_qm_MultiMeasureEvaluation_FormBasedEvaluation = Generalization(general=FormBasedEvaluation, specific=qm_MultiMeasureEvaluation)
gen_qm_WeightedSumMultiMeasureEvaluation_MultiMeasureEvaluation = Generalization(general=MultiMeasureEvaluation, specific=qm_WeightedSumMultiMeasureEvaluation)
gen_qm_MeasureRanking_MeasureEvaluation = Generalization(general=MeasureEvaluation, specific=qm_MeasureRanking)
gen_qm_MeasureRanking_Ranking = Generalization(general=Ranking, specific=qm_MeasureRanking)
gen_qm_FormBasedMeasureAggregation_MeasureAggregation = Generalization(general=MeasureAggregation, specific=qm_FormBasedMeasureAggregation)
gen_qm_FactorRanking_Ranking = Generalization(general=Ranking, specific=qm_FactorRanking)
gen_qm_LinearFunction_Function = Generalization(general=Function, specific=qm_LinearFunction)
gen_qm_FindingsMeasurementResult_MeasurementResult = Generalization(general=MeasurementResult, specific=qm_FindingsMeasurementResult)
gen_qm_EvaluationResult_Result = Generalization(general=Result, specific=qm_EvaluationResult)
gen_qm_SingleMeasureEvaluationResult_EvaluationResult = Generalization(general=EvaluationResult, specific=qm_SingleMeasureEvaluationResult)
gen_qm_MultiMeasureEvaluationResult_EvaluationResult = Generalization(general=EvaluationResult, specific=qm_MultiMeasureEvaluationResult)
gen_qm_MeasurementResult_Result = Generalization(general=Result, specific=qm_MeasurementResult)
gen_qm_NumberMeasurementResult_MeasurementResult = Generalization(general=MeasurementResult, specific=qm_NumberMeasurementResult)

# Domain Model
domain_model = DomainModel(
    name="qm",
    types={qm_QualityModel, NamedElement, qm_Evaluation, qm_Measure, qm_MeasurementMethod, qm_Tool, qm_Tag, qm_Source, qm_QualityModelElement, qm_DescribedElement, AnnotatedElement, qm_Entity, qm_NamedElement, DescribedElement, qm_Factor, qm_Annotation, qm_AnnotationBase, qm_TaggedElement, QualityModelElement, qm_Specialization, qm_Decomposition, qm_AnnotatedElement, TaggedElement, qm_CharacterizingElement, CharacterizingElement, qm_Impact, qm_FactorRefinement, qm_Measurement, qm_MeasureRefinement, qm_MeasureAggregation, MeasurementMethod, qm_Instrument, qm_ManualInstrument, Instrument, qm_ToolBasedInstrument, qm_QIESLEvaluation, TextEvaluation, qm_TextEvaluation, Evaluation, qm_FormBasedEvaluation, qm_SingleMeasureEvaluation, FormBasedEvaluation, MeasureEvaluation, qm_FactorAggregation, qm_NormalizationMeasure, Measure, qm_QIESLAggregation, TextAggregation, qm_TextAggregation, MeasureAggregation, qm_Function, qm_LinearIncreasingFunction, LinearFunction, qm_LinearDecreasingFunction, qm_WeightedSumFactorAggregation, FactorAggregation, qm_FindingsUnionMeasureAggregation, FormBasedMeasureAggregation, qm_NumberMeanMeasureAggregation, qm_ManualEvaluation, qm_MeasureEvaluation, qm_Ranking, qm_MultiMeasureEvaluation, qm_WeightedSumMultiMeasureEvaluation, MultiMeasureEvaluation, qm_MeasureRanking, qm_QualityModelResult, qm_MeasurementResult, qm_EvaluationResult, qm_FormBasedMeasureAggregation, qm_FactorRanking, Ranking, qm_LinearFunction, Function, qm_DoubleInterval, qm_FindingsMeasurementResult, qm_FindingMessage, qm_SingleMeasureEvaluationResult, EvaluationResult, qm_MultiMeasureEvaluationResult, qm_MeasureRankingEvaluationResult, qm_Result, Result, qm_NumberMeasurementResult, MeasurementResult, Effect, Type},
    associations={evaluations3, measures5, measurementMethods7, tools9, tags11, sources13, requires16, originatesFrom17, qualityModel18, entities0, factors1, annotations19, advancedAnnotations20, qualityModel22, taggedBy24, isA25, isADirect27, partOf28, partOfDirect31, qualityModel33, parent39, child41, characterizes43, influences45, influencesDirect47, refines48, refinesDirect51, qualityModel53, source55, target57, parent35, child37, evaluates59, qualityModel61, child63, parent65, parent67, child69, parent71, child72, measures75, measuresDirect77, determines88, qualityModel90, tool92, qualityModel93, qualityModel80, refines83, refinesDirect86, rankings97, measure99, normlizationMeasure101, function103, rankings105, measurementResults106, factor95, value112, findingMessages113, value114, resultsFrom117, evaluationResults120, value121, resultsFrom124, evaluationResults107, resultsFrom109},
    generalizations={gen_qm_Source_NamedElement, gen_qm_DescribedElement_AnnotatedElement, gen_qm_QualityModel_NamedElement, gen_qm_NamedElement_DescribedElement, gen_qm_Tag_NamedElement, gen_qm_TaggedElement_QualityModelElement, gen_qm_Entity_NamedElement, gen_qm_AnnotatedElement_TaggedElement, gen_qm_CharacterizingElement_NamedElement, gen_qm_Factor_CharacterizingElement, gen_qm_Impact_AnnotatedElement, gen_qm_Specialization_AnnotatedElement, gen_qm_Decomposition_AnnotatedElement, gen_qm_Evaluation_NamedElement, gen_qm_FactorRefinement_AnnotatedElement, gen_qm_Measurement_AnnotatedElement, gen_qm_MeasureRefinement_AnnotatedElement, gen_qm_Measure_CharacterizingElement, gen_qm_MeasurementMethod_AnnotatedElement, gen_qm_MeasureAggregation_MeasurementMethod, gen_qm_MeasureAggregation_NamedElement, gen_qm_Instrument_MeasurementMethod, gen_qm_ManualInstrument_Instrument, gen_qm_ManualInstrument_NamedElement, gen_qm_ToolBasedInstrument_Instrument, gen_qm_Tool_NamedElement, gen_qm_QIESLEvaluation_TextEvaluation, gen_qm_TextEvaluation_Evaluation, gen_qm_FormBasedEvaluation_Evaluation, gen_qm_SingleMeasureEvaluation_FormBasedEvaluation, gen_qm_SingleMeasureEvaluation_MeasureEvaluation, gen_qm_FactorAggregation_FormBasedEvaluation, gen_qm_NormalizationMeasure_Measure, gen_qm_QIESLAggregation_TextAggregation, gen_qm_TextAggregation_MeasureAggregation, gen_qm_LinearIncreasingFunction_LinearFunction, gen_qm_LinearDecreasingFunction_LinearFunction, gen_qm_WeightedSumFactorAggregation_FactorAggregation, gen_qm_FindingsUnionMeasureAggregation_FormBasedMeasureAggregation, gen_qm_NumberMeanMeasureAggregation_FormBasedMeasureAggregation, gen_qm_ManualEvaluation_Evaluation, gen_qm_MultiMeasureEvaluation_FormBasedEvaluation, gen_qm_WeightedSumMultiMeasureEvaluation_MultiMeasureEvaluation, gen_qm_MeasureRanking_MeasureEvaluation, gen_qm_MeasureRanking_Ranking, gen_qm_FormBasedMeasureAggregation_MeasureAggregation, gen_qm_FactorRanking_Ranking, gen_qm_LinearFunction_Function, gen_qm_FindingsMeasurementResult_MeasurementResult, gen_qm_EvaluationResult_Result, gen_qm_SingleMeasureEvaluationResult_EvaluationResult, gen_qm_MultiMeasureEvaluationResult_EvaluationResult, gen_qm_MeasurementResult_Result, gen_qm_NumberMeasurementResult_MeasurementResult},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)