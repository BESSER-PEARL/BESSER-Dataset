import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    qm::Result,
    qm::MeasureRankingEvaluationResult,
    qm::FindingMessage,
    qm::DoubleInterval,
    MeasurementResult,
    qm::FindingsMeasurementResult,
    qm::NumberMeasurementResult,
    Result,
    qm::EvaluationResult,
    qm::MeasurementResult,
    qm::QualityModelResult,
    MultiMeasureEvaluation,
    qm::WeightedSumMultiMeasureEvaluation,
    qm::Ranking,
    qm::MeasureEvaluation,
    FormBasedMeasureAggregation,
    qm::NumberMeanMeasureAggregation,
    qm::FindingsUnionMeasureAggregation,
    FactorAggregation,
    qm::WeightedSumFactorAggregation,
    LinearFunction,
    qm::LinearDecreasingFunction,
    qm::LinearIncreasingFunction,
    qm::Function,
    Function,
    qm::LinearFunction,
    Ranking,
    qm::FactorRanking,
    MeasureAggregation,
    qm::FormBasedMeasureAggregation,
    qm::TextAggregation,
    TextAggregation,
    qm::QIESLAggregation,
    Measure,
    qm::NormalizationMeasure,
    MeasureEvaluation,
    qm::MeasureRanking,
    FormBasedEvaluation,
    qm::SingleMeasureEvaluation,
    qm::FactorAggregation,
    qm::MultiMeasureEvaluation,
    Evaluation,
    qm::FormBasedEvaluation,
    qm::ManualEvaluation,
    qm::TextEvaluation,
    TextEvaluation,
    qm::QIESLEvaluation,
    Instrument,
    qm::ToolBasedInstrument,
    MeasurementMethod,
    qm::Instrument,
    CharacterizingElement,
    QualityModelElement,
    qm::TaggedElement,
    qm::AnnotationBase,
    qm::Annotation,
    TaggedElement,
    qm::AnnotatedElement,
    qm::QualityModelElement,
    DescribedElement,
    qm::NamedElement,
    AnnotatedElement,
    qm::Decomposition,
    qm::Measurement,
    qm::MeasureRefinement,
    qm::FactorRefinement,
    qm::Impact,
    qm::Specialization,
    qm::DescribedElement,
    NamedElement,
    qm::MeasureAggregation,
    qm::ManualInstrument,
    qm::CharacterizingElement,
    qm::QualityModel,
    qm::Source,
    qm::Tag,
    qm::Tool,
    qm::MeasurementMethod,
    qm::Measure,
    qm::Evaluation,
    qm::Factor,
    qm::Entity,
    EvaluationResult,
    qm::MultiMeasureEvaluationResult,
    qm::SingleMeasureEvaluationResult,
    Type,
    Effect,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qm::result_is_not_abstract():
    assert not inspect.isabstract(qm::Result)


def test_qm::result_constructor_exists():
    assert callable(qm::Result.__init__)


def test_qm::result_constructor_args():
    sig = inspect.signature(qm::Result.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_qm::result_has_message():
    assert hasattr(qm::Result, "message")
    descriptor = None
    for klass in qm::Result.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_qm::measurerankingevaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm::MeasureRankingEvaluationResult)


def test_qm::measurerankingevaluationresult_constructor_exists():
    assert callable(qm::MeasureRankingEvaluationResult.__init__)


def test_qm::measurerankingevaluationresult_constructor_args():
    sig = inspect.signature(qm::MeasureRankingEvaluationResult.__init__)
    params = list(sig.parameters.keys())
    assert "ratioAffected" in params, "Missing parameter 'ratioAffected'"

def test_qm::measurerankingevaluationresult_has_ratioAffected():
    assert hasattr(qm::MeasureRankingEvaluationResult, "ratioAffected")
    descriptor = None
    for klass in qm::MeasureRankingEvaluationResult.__mro__:
        if "ratioAffected" in klass.__dict__:
            descriptor = klass.__dict__["ratioAffected"]
            break
    assert isinstance(descriptor, property)



def test_qm::findingmessage_is_not_abstract():
    assert not inspect.isabstract(qm::FindingMessage)


def test_qm::findingmessage_constructor_exists():
    assert callable(qm::FindingMessage.__init__)


def test_qm::findingmessage_constructor_args():
    sig = inspect.signature(qm::FindingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "location" in params, "Missing parameter 'location'"

def test_qm::findingmessage_has_message():
    assert hasattr(qm::FindingMessage, "message")
    descriptor = None
    for klass in qm::FindingMessage.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_qm::findingmessage_has_location():
    assert hasattr(qm::FindingMessage, "location")
    descriptor = None
    for klass in qm::FindingMessage.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_qm::doubleinterval_is_not_abstract():
    assert not inspect.isabstract(qm::DoubleInterval)


def test_qm::doubleinterval_constructor_exists():
    assert callable(qm::DoubleInterval.__init__)


def test_qm::doubleinterval_constructor_args():
    sig = inspect.signature(qm::DoubleInterval.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_qm::doubleinterval_has_lower():
    assert hasattr(qm::DoubleInterval, "lower")
    descriptor = None
    for klass in qm::DoubleInterval.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_qm::doubleinterval_has_upper():
    assert hasattr(qm::DoubleInterval, "upper")
    descriptor = None
    for klass in qm::DoubleInterval.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_measurementresult_is_not_abstract():
    assert not inspect.isabstract(MeasurementResult)


def test_measurementresult_constructor_exists():
    assert callable(MeasurementResult.__init__)


def test_measurementresult_constructor_args():
    sig = inspect.signature(MeasurementResult.__init__)
    params = list(sig.parameters.keys())



def test_qm::findingsmeasurementresult_is_not_abstract():
    assert not inspect.isabstract(qm::FindingsMeasurementResult)


def test_qm::findingsmeasurementresult_constructor_exists():
    assert callable(qm::FindingsMeasurementResult.__init__)


def test_qm::findingsmeasurementresult_constructor_args():
    sig = inspect.signature(qm::FindingsMeasurementResult.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "findings" in params, "Missing parameter 'findings'"

def test_qm::findingsmeasurementresult_has_count():
    assert hasattr(qm::FindingsMeasurementResult, "count")
    descriptor = None
    for klass in qm::FindingsMeasurementResult.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_qm::findingsmeasurementresult_has_findings():
    assert hasattr(qm::FindingsMeasurementResult, "findings")
    descriptor = None
    for klass in qm::FindingsMeasurementResult.__mro__:
        if "findings" in klass.__dict__:
            descriptor = klass.__dict__["findings"]
            break
    assert isinstance(descriptor, property)



def test_qm::numbermeasurementresult_is_not_abstract():
    assert not inspect.isabstract(qm::NumberMeasurementResult)


def test_qm::numbermeasurementresult_constructor_exists():
    assert callable(qm::NumberMeasurementResult.__init__)


def test_qm::numbermeasurementresult_constructor_args():
    sig = inspect.signature(qm::NumberMeasurementResult.__init__)
    params = list(sig.parameters.keys())



def test_result_is_not_abstract():
    assert not inspect.isabstract(Result)


def test_result_constructor_exists():
    assert callable(Result.__init__)


def test_result_constructor_args():
    sig = inspect.signature(Result.__init__)
    params = list(sig.parameters.keys())



def test_qm::evaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm::EvaluationResult)


def test_qm::evaluationresult_constructor_exists():
    assert callable(qm::EvaluationResult.__init__)


def test_qm::evaluationresult_constructor_args():
    sig = inspect.signature(qm::EvaluationResult.__init__)
    params = list(sig.parameters.keys())



def test_qm::measurementresult_is_not_abstract():
    assert not inspect.isabstract(qm::MeasurementResult)


def test_qm::measurementresult_constructor_exists():
    assert callable(qm::MeasurementResult.__init__)


def test_qm::measurementresult_constructor_args():
    sig = inspect.signature(qm::MeasurementResult.__init__)
    params = list(sig.parameters.keys())



def test_qm::qualitymodelresult_is_not_abstract():
    assert not inspect.isabstract(qm::QualityModelResult)


def test_qm::qualitymodelresult_constructor_exists():
    assert callable(qm::QualityModelResult.__init__)


def test_qm::qualitymodelresult_constructor_args():
    sig = inspect.signature(qm::QualityModelResult.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "system" in params, "Missing parameter 'system'"

def test_qm::qualitymodelresult_has_date():
    assert hasattr(qm::QualityModelResult, "date")
    descriptor = None
    for klass in qm::QualityModelResult.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_qm::qualitymodelresult_has_system():
    assert hasattr(qm::QualityModelResult, "system")
    descriptor = None
    for klass in qm::QualityModelResult.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_multimeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(MultiMeasureEvaluation)


def test_multimeasureevaluation_constructor_exists():
    assert callable(MultiMeasureEvaluation.__init__)


def test_multimeasureevaluation_constructor_args():
    sig = inspect.signature(MultiMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::weightedsummultimeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::WeightedSumMultiMeasureEvaluation)


def test_qm::weightedsummultimeasureevaluation_constructor_exists():
    assert callable(qm::WeightedSumMultiMeasureEvaluation.__init__)


def test_qm::weightedsummultimeasureevaluation_constructor_args():
    sig = inspect.signature(qm::WeightedSumMultiMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::ranking_is_not_abstract():
    assert not inspect.isabstract(qm::Ranking)


def test_qm::ranking_constructor_exists():
    assert callable(qm::Ranking.__init__)


def test_qm::ranking_constructor_args():
    sig = inspect.signature(qm::Ranking.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_qm::ranking_has_weight():
    assert hasattr(qm::Ranking, "weight")
    descriptor = None
    for klass in qm::Ranking.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_qm::ranking_has_rank():
    assert hasattr(qm::Ranking, "rank")
    descriptor = None
    for klass in qm::Ranking.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_qm::measureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::MeasureEvaluation)


def test_qm::measureevaluation_constructor_exists():
    assert callable(qm::MeasureEvaluation.__init__)


def test_qm::measureevaluation_constructor_args():
    sig = inspect.signature(qm::MeasureEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"

def test_qm::measureevaluation_has_range():
    assert hasattr(qm::MeasureEvaluation, "range")
    descriptor = None
    for klass in qm::MeasureEvaluation.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_formbasedmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(FormBasedMeasureAggregation)


def test_formbasedmeasureaggregation_constructor_exists():
    assert callable(FormBasedMeasureAggregation.__init__)


def test_formbasedmeasureaggregation_constructor_args():
    sig = inspect.signature(FormBasedMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::numbermeanmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm::NumberMeanMeasureAggregation)


def test_qm::numbermeanmeasureaggregation_constructor_exists():
    assert callable(qm::NumberMeanMeasureAggregation.__init__)


def test_qm::numbermeanmeasureaggregation_constructor_args():
    sig = inspect.signature(qm::NumberMeanMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::findingsunionmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm::FindingsUnionMeasureAggregation)


def test_qm::findingsunionmeasureaggregation_constructor_exists():
    assert callable(qm::FindingsUnionMeasureAggregation.__init__)


def test_qm::findingsunionmeasureaggregation_constructor_args():
    sig = inspect.signature(qm::FindingsUnionMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_factoraggregation_is_not_abstract():
    assert not inspect.isabstract(FactorAggregation)


def test_factoraggregation_constructor_exists():
    assert callable(FactorAggregation.__init__)


def test_factoraggregation_constructor_args():
    sig = inspect.signature(FactorAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::weightedsumfactoraggregation_is_not_abstract():
    assert not inspect.isabstract(qm::WeightedSumFactorAggregation)


def test_qm::weightedsumfactoraggregation_constructor_exists():
    assert callable(qm::WeightedSumFactorAggregation.__init__)


def test_qm::weightedsumfactoraggregation_constructor_args():
    sig = inspect.signature(qm::WeightedSumFactorAggregation.__init__)
    params = list(sig.parameters.keys())



def test_linearfunction_is_not_abstract():
    assert not inspect.isabstract(LinearFunction)


def test_linearfunction_constructor_exists():
    assert callable(LinearFunction.__init__)


def test_linearfunction_constructor_args():
    sig = inspect.signature(LinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_qm::lineardecreasingfunction_is_not_abstract():
    assert not inspect.isabstract(qm::LinearDecreasingFunction)


def test_qm::lineardecreasingfunction_constructor_exists():
    assert callable(qm::LinearDecreasingFunction.__init__)


def test_qm::lineardecreasingfunction_constructor_args():
    sig = inspect.signature(qm::LinearDecreasingFunction.__init__)
    params = list(sig.parameters.keys())



def test_qm::linearincreasingfunction_is_not_abstract():
    assert not inspect.isabstract(qm::LinearIncreasingFunction)


def test_qm::linearincreasingfunction_constructor_exists():
    assert callable(qm::LinearIncreasingFunction.__init__)


def test_qm::linearincreasingfunction_constructor_args():
    sig = inspect.signature(qm::LinearIncreasingFunction.__init__)
    params = list(sig.parameters.keys())



def test_qm::function_is_not_abstract():
    assert not inspect.isabstract(qm::Function)


def test_qm::function_constructor_exists():
    assert callable(qm::Function.__init__)


def test_qm::function_constructor_args():
    sig = inspect.signature(qm::Function.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_qm::linearfunction_is_not_abstract():
    assert not inspect.isabstract(qm::LinearFunction)


def test_qm::linearfunction_constructor_exists():
    assert callable(qm::LinearFunction.__init__)


def test_qm::linearfunction_constructor_args():
    sig = inspect.signature(qm::LinearFunction.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_qm::linearfunction_has_lowerBound():
    assert hasattr(qm::LinearFunction, "lowerBound")
    descriptor = None
    for klass in qm::LinearFunction.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_qm::linearfunction_has_upperBound():
    assert hasattr(qm::LinearFunction, "upperBound")
    descriptor = None
    for klass in qm::LinearFunction.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_ranking_is_not_abstract():
    assert not inspect.isabstract(Ranking)


def test_ranking_constructor_exists():
    assert callable(Ranking.__init__)


def test_ranking_constructor_args():
    sig = inspect.signature(Ranking.__init__)
    params = list(sig.parameters.keys())



def test_qm::factorranking_is_not_abstract():
    assert not inspect.isabstract(qm::FactorRanking)


def test_qm::factorranking_constructor_exists():
    assert callable(qm::FactorRanking.__init__)


def test_qm::factorranking_constructor_args():
    sig = inspect.signature(qm::FactorRanking.__init__)
    params = list(sig.parameters.keys())



def test_measureaggregation_is_not_abstract():
    assert not inspect.isabstract(MeasureAggregation)


def test_measureaggregation_constructor_exists():
    assert callable(MeasureAggregation.__init__)


def test_measureaggregation_constructor_args():
    sig = inspect.signature(MeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::formbasedmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm::FormBasedMeasureAggregation)


def test_qm::formbasedmeasureaggregation_constructor_exists():
    assert callable(qm::FormBasedMeasureAggregation.__init__)


def test_qm::formbasedmeasureaggregation_constructor_args():
    sig = inspect.signature(qm::FormBasedMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::textaggregation_is_not_abstract():
    assert not inspect.isabstract(qm::TextAggregation)


def test_qm::textaggregation_constructor_exists():
    assert callable(qm::TextAggregation.__init__)


def test_qm::textaggregation_constructor_args():
    sig = inspect.signature(qm::TextAggregation.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_qm::textaggregation_has_specification():
    assert hasattr(qm::TextAggregation, "specification")
    descriptor = None
    for klass in qm::TextAggregation.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_textaggregation_is_not_abstract():
    assert not inspect.isabstract(TextAggregation)


def test_textaggregation_constructor_exists():
    assert callable(TextAggregation.__init__)


def test_textaggregation_constructor_args():
    sig = inspect.signature(TextAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::qieslaggregation_is_not_abstract():
    assert not inspect.isabstract(qm::QIESLAggregation)


def test_qm::qieslaggregation_constructor_exists():
    assert callable(qm::QIESLAggregation.__init__)


def test_qm::qieslaggregation_constructor_args():
    sig = inspect.signature(qm::QIESLAggregation.__init__)
    params = list(sig.parameters.keys())



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_qm::normalizationmeasure_is_not_abstract():
    assert not inspect.isabstract(qm::NormalizationMeasure)


def test_qm::normalizationmeasure_constructor_exists():
    assert callable(qm::NormalizationMeasure.__init__)


def test_qm::normalizationmeasure_constructor_args():
    sig = inspect.signature(qm::NormalizationMeasure.__init__)
    params = list(sig.parameters.keys())



def test_measureevaluation_is_not_abstract():
    assert not inspect.isabstract(MeasureEvaluation)


def test_measureevaluation_constructor_exists():
    assert callable(MeasureEvaluation.__init__)


def test_measureevaluation_constructor_args():
    sig = inspect.signature(MeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::measureranking_is_not_abstract():
    assert not inspect.isabstract(qm::MeasureRanking)


def test_qm::measureranking_constructor_exists():
    assert callable(qm::MeasureRanking.__init__)


def test_qm::measureranking_constructor_args():
    sig = inspect.signature(qm::MeasureRanking.__init__)
    params = list(sig.parameters.keys())



def test_formbasedevaluation_is_not_abstract():
    assert not inspect.isabstract(FormBasedEvaluation)


def test_formbasedevaluation_constructor_exists():
    assert callable(FormBasedEvaluation.__init__)


def test_formbasedevaluation_constructor_args():
    sig = inspect.signature(FormBasedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::singlemeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::SingleMeasureEvaluation)


def test_qm::singlemeasureevaluation_constructor_exists():
    assert callable(qm::SingleMeasureEvaluation.__init__)


def test_qm::singlemeasureevaluation_constructor_args():
    sig = inspect.signature(qm::SingleMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::factoraggregation_is_not_abstract():
    assert not inspect.isabstract(qm::FactorAggregation)


def test_qm::factoraggregation_constructor_exists():
    assert callable(qm::FactorAggregation.__init__)


def test_qm::factoraggregation_constructor_args():
    sig = inspect.signature(qm::FactorAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::multimeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::MultiMeasureEvaluation)


def test_qm::multimeasureevaluation_constructor_exists():
    assert callable(qm::MultiMeasureEvaluation.__init__)


def test_qm::multimeasureevaluation_constructor_args():
    sig = inspect.signature(qm::MultiMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_is_not_abstract():
    assert not inspect.isabstract(Evaluation)


def test_evaluation_constructor_exists():
    assert callable(Evaluation.__init__)


def test_evaluation_constructor_args():
    sig = inspect.signature(Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::formbasedevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::FormBasedEvaluation)


def test_qm::formbasedevaluation_constructor_exists():
    assert callable(qm::FormBasedEvaluation.__init__)


def test_qm::formbasedevaluation_constructor_args():
    sig = inspect.signature(qm::FormBasedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::manualevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::ManualEvaluation)


def test_qm::manualevaluation_constructor_exists():
    assert callable(qm::ManualEvaluation.__init__)


def test_qm::manualevaluation_constructor_args():
    sig = inspect.signature(qm::ManualEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::textevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::TextEvaluation)


def test_qm::textevaluation_constructor_exists():
    assert callable(qm::TextEvaluation.__init__)


def test_qm::textevaluation_constructor_args():
    sig = inspect.signature(qm::TextEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_qm::textevaluation_has_specification():
    assert hasattr(qm::TextEvaluation, "specification")
    descriptor = None
    for klass in qm::TextEvaluation.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_textevaluation_is_not_abstract():
    assert not inspect.isabstract(TextEvaluation)


def test_textevaluation_constructor_exists():
    assert callable(TextEvaluation.__init__)


def test_textevaluation_constructor_args():
    sig = inspect.signature(TextEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm::qieslevaluation_is_not_abstract():
    assert not inspect.isabstract(qm::QIESLEvaluation)


def test_qm::qieslevaluation_constructor_exists():
    assert callable(qm::QIESLEvaluation.__init__)


def test_qm::qieslevaluation_constructor_args():
    sig = inspect.signature(qm::QIESLEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_instrument_is_not_abstract():
    assert not inspect.isabstract(Instrument)


def test_instrument_constructor_exists():
    assert callable(Instrument.__init__)


def test_instrument_constructor_args():
    sig = inspect.signature(Instrument.__init__)
    params = list(sig.parameters.keys())



def test_qm::toolbasedinstrument_is_not_abstract():
    assert not inspect.isabstract(qm::ToolBasedInstrument)


def test_qm::toolbasedinstrument_constructor_exists():
    assert callable(qm::ToolBasedInstrument.__init__)


def test_qm::toolbasedinstrument_constructor_args():
    sig = inspect.signature(qm::ToolBasedInstrument.__init__)
    params = list(sig.parameters.keys())
    assert "metric" in params, "Missing parameter 'metric'"

def test_qm::toolbasedinstrument_has_metric():
    assert hasattr(qm::ToolBasedInstrument, "metric")
    descriptor = None
    for klass in qm::ToolBasedInstrument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)



def test_measurementmethod_is_not_abstract():
    assert not inspect.isabstract(MeasurementMethod)


def test_measurementmethod_constructor_exists():
    assert callable(MeasurementMethod.__init__)


def test_measurementmethod_constructor_args():
    sig = inspect.signature(MeasurementMethod.__init__)
    params = list(sig.parameters.keys())



def test_qm::instrument_is_not_abstract():
    assert not inspect.isabstract(qm::Instrument)


def test_qm::instrument_constructor_exists():
    assert callable(qm::Instrument.__init__)


def test_qm::instrument_constructor_args():
    sig = inspect.signature(qm::Instrument.__init__)
    params = list(sig.parameters.keys())



def test_characterizingelement_is_not_abstract():
    assert not inspect.isabstract(CharacterizingElement)


def test_characterizingelement_constructor_exists():
    assert callable(CharacterizingElement.__init__)


def test_characterizingelement_constructor_args():
    sig = inspect.signature(CharacterizingElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymodelelement_is_not_abstract():
    assert not inspect.isabstract(QualityModelElement)


def test_qualitymodelelement_constructor_exists():
    assert callable(QualityModelElement.__init__)


def test_qualitymodelelement_constructor_args():
    sig = inspect.signature(QualityModelElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::taggedelement_is_not_abstract():
    assert not inspect.isabstract(qm::TaggedElement)


def test_qm::taggedelement_constructor_exists():
    assert callable(qm::TaggedElement.__init__)


def test_qm::taggedelement_constructor_args():
    sig = inspect.signature(qm::TaggedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::annotationbase_is_not_abstract():
    assert not inspect.isabstract(qm::AnnotationBase)


def test_qm::annotationbase_constructor_exists():
    assert callable(qm::AnnotationBase.__init__)


def test_qm::annotationbase_constructor_args():
    sig = inspect.signature(qm::AnnotationBase.__init__)
    params = list(sig.parameters.keys())



def test_qm::annotation_is_not_abstract():
    assert not inspect.isabstract(qm::Annotation)


def test_qm::annotation_constructor_exists():
    assert callable(qm::Annotation.__init__)


def test_qm::annotation_constructor_args():
    sig = inspect.signature(qm::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_qm::annotation_has_key():
    assert hasattr(qm::Annotation, "key")
    descriptor = None
    for klass in qm::Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_qm::annotation_has_value():
    assert hasattr(qm::Annotation, "value")
    descriptor = None
    for klass in qm::Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_taggedelement_is_not_abstract():
    assert not inspect.isabstract(TaggedElement)


def test_taggedelement_constructor_exists():
    assert callable(TaggedElement.__init__)


def test_taggedelement_constructor_args():
    sig = inspect.signature(TaggedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::annotatedelement_is_not_abstract():
    assert not inspect.isabstract(qm::AnnotatedElement)


def test_qm::annotatedelement_constructor_exists():
    assert callable(qm::AnnotatedElement.__init__)


def test_qm::annotatedelement_constructor_args():
    sig = inspect.signature(qm::AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::qualitymodelelement_is_not_abstract():
    assert not inspect.isabstract(qm::QualityModelElement)


def test_qm::qualitymodelelement_constructor_exists():
    assert callable(qm::QualityModelElement.__init__)


def test_qm::qualitymodelelement_constructor_args():
    sig = inspect.signature(qm::QualityModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_qm::qualitymodelelement_has_qualifiedName():
    assert hasattr(qm::QualityModelElement, "qualifiedName")
    descriptor = None
    for klass in qm::QualityModelElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_describedelement_is_not_abstract():
    assert not inspect.isabstract(DescribedElement)


def test_describedelement_constructor_exists():
    assert callable(DescribedElement.__init__)


def test_describedelement_constructor_args():
    sig = inspect.signature(DescribedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::namedelement_is_not_abstract():
    assert not inspect.isabstract(qm::NamedElement)


def test_qm::namedelement_constructor_exists():
    assert callable(qm::NamedElement.__init__)


def test_qm::namedelement_constructor_args():
    sig = inspect.signature(qm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"

def test_qm::namedelement_has_title():
    assert hasattr(qm::NamedElement, "title")
    descriptor = None
    for klass in qm::NamedElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_qm::namedelement_has_name():
    assert hasattr(qm::NamedElement, "name")
    descriptor = None
    for klass in qm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::decomposition_is_not_abstract():
    assert not inspect.isabstract(qm::Decomposition)


def test_qm::decomposition_constructor_exists():
    assert callable(qm::Decomposition.__init__)


def test_qm::decomposition_constructor_args():
    sig = inspect.signature(qm::Decomposition.__init__)
    params = list(sig.parameters.keys())



def test_qm::measurement_is_not_abstract():
    assert not inspect.isabstract(qm::Measurement)


def test_qm::measurement_constructor_exists():
    assert callable(qm::Measurement.__init__)


def test_qm::measurement_constructor_args():
    sig = inspect.signature(qm::Measurement.__init__)
    params = list(sig.parameters.keys())



def test_qm::measurerefinement_is_not_abstract():
    assert not inspect.isabstract(qm::MeasureRefinement)


def test_qm::measurerefinement_constructor_exists():
    assert callable(qm::MeasureRefinement.__init__)


def test_qm::measurerefinement_constructor_args():
    sig = inspect.signature(qm::MeasureRefinement.__init__)
    params = list(sig.parameters.keys())



def test_qm::factorrefinement_is_not_abstract():
    assert not inspect.isabstract(qm::FactorRefinement)


def test_qm::factorrefinement_constructor_exists():
    assert callable(qm::FactorRefinement.__init__)


def test_qm::factorrefinement_constructor_args():
    sig = inspect.signature(qm::FactorRefinement.__init__)
    params = list(sig.parameters.keys())



def test_qm::impact_is_not_abstract():
    assert not inspect.isabstract(qm::Impact)


def test_qm::impact_constructor_exists():
    assert callable(qm::Impact.__init__)


def test_qm::impact_constructor_args():
    sig = inspect.signature(qm::Impact.__init__)
    params = list(sig.parameters.keys())
    assert "justification" in params, "Missing parameter 'justification'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_qm::impact_has_justification():
    assert hasattr(qm::Impact, "justification")
    descriptor = None
    for klass in qm::Impact.__mro__:
        if "justification" in klass.__dict__:
            descriptor = klass.__dict__["justification"]
            break
    assert isinstance(descriptor, property)

def test_qm::impact_has_effect():
    assert hasattr(qm::Impact, "effect")
    descriptor = None
    for klass in qm::Impact.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_qm::specialization_is_not_abstract():
    assert not inspect.isabstract(qm::Specialization)


def test_qm::specialization_constructor_exists():
    assert callable(qm::Specialization.__init__)


def test_qm::specialization_constructor_args():
    sig = inspect.signature(qm::Specialization.__init__)
    params = list(sig.parameters.keys())



def test_qm::describedelement_is_not_abstract():
    assert not inspect.isabstract(qm::DescribedElement)


def test_qm::describedelement_constructor_exists():
    assert callable(qm::DescribedElement.__init__)


def test_qm::describedelement_constructor_args():
    sig = inspect.signature(qm::DescribedElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_qm::describedelement_has_description():
    assert hasattr(qm::DescribedElement, "description")
    descriptor = None
    for klass in qm::DescribedElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::measureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm::MeasureAggregation)


def test_qm::measureaggregation_constructor_exists():
    assert callable(qm::MeasureAggregation.__init__)


def test_qm::measureaggregation_constructor_args():
    sig = inspect.signature(qm::MeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm::manualinstrument_is_not_abstract():
    assert not inspect.isabstract(qm::ManualInstrument)


def test_qm::manualinstrument_constructor_exists():
    assert callable(qm::ManualInstrument.__init__)


def test_qm::manualinstrument_constructor_args():
    sig = inspect.signature(qm::ManualInstrument.__init__)
    params = list(sig.parameters.keys())



def test_qm::characterizingelement_is_not_abstract():
    assert not inspect.isabstract(qm::CharacterizingElement)


def test_qm::characterizingelement_constructor_exists():
    assert callable(qm::CharacterizingElement.__init__)


def test_qm::characterizingelement_constructor_args():
    sig = inspect.signature(qm::CharacterizingElement.__init__)
    params = list(sig.parameters.keys())



def test_qm::qualitymodel_is_not_abstract():
    assert not inspect.isabstract(qm::QualityModel)


def test_qm::qualitymodel_constructor_exists():
    assert callable(qm::QualityModel.__init__)


def test_qm::qualitymodel_constructor_args():
    sig = inspect.signature(qm::QualityModel.__init__)
    params = list(sig.parameters.keys())
    assert "schoolGradeBoundary2" in params, "Missing parameter 'schoolGradeBoundary2'"
    assert "schoolGradeBoundary6" in params, "Missing parameter 'schoolGradeBoundary6'"
    assert "schoolGradeBoundary3" in params, "Missing parameter 'schoolGradeBoundary3'"
    assert "schoolGradeBoundary5" in params, "Missing parameter 'schoolGradeBoundary5'"
    assert "schoolGradeBoundary4" in params, "Missing parameter 'schoolGradeBoundary4'"

def test_qm::qualitymodel_has_schoolGradeBoundary2():
    assert hasattr(qm::QualityModel, "schoolGradeBoundary2")
    descriptor = None
    for klass in qm::QualityModel.__mro__:
        if "schoolGradeBoundary2" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary2"]
            break
    assert isinstance(descriptor, property)

def test_qm::qualitymodel_has_schoolGradeBoundary6():
    assert hasattr(qm::QualityModel, "schoolGradeBoundary6")
    descriptor = None
    for klass in qm::QualityModel.__mro__:
        if "schoolGradeBoundary6" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary6"]
            break
    assert isinstance(descriptor, property)

def test_qm::qualitymodel_has_schoolGradeBoundary3():
    assert hasattr(qm::QualityModel, "schoolGradeBoundary3")
    descriptor = None
    for klass in qm::QualityModel.__mro__:
        if "schoolGradeBoundary3" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary3"]
            break
    assert isinstance(descriptor, property)

def test_qm::qualitymodel_has_schoolGradeBoundary5():
    assert hasattr(qm::QualityModel, "schoolGradeBoundary5")
    descriptor = None
    for klass in qm::QualityModel.__mro__:
        if "schoolGradeBoundary5" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary5"]
            break
    assert isinstance(descriptor, property)

def test_qm::qualitymodel_has_schoolGradeBoundary4():
    assert hasattr(qm::QualityModel, "schoolGradeBoundary4")
    descriptor = None
    for klass in qm::QualityModel.__mro__:
        if "schoolGradeBoundary4" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary4"]
            break
    assert isinstance(descriptor, property)



def test_qm::source_is_not_abstract():
    assert not inspect.isabstract(qm::Source)


def test_qm::source_constructor_exists():
    assert callable(qm::Source.__init__)


def test_qm::source_constructor_args():
    sig = inspect.signature(qm::Source.__init__)
    params = list(sig.parameters.keys())



def test_qm::tag_is_not_abstract():
    assert not inspect.isabstract(qm::Tag)


def test_qm::tag_constructor_exists():
    assert callable(qm::Tag.__init__)


def test_qm::tag_constructor_args():
    sig = inspect.signature(qm::Tag.__init__)
    params = list(sig.parameters.keys())



def test_qm::tool_is_not_abstract():
    assert not inspect.isabstract(qm::Tool)


def test_qm::tool_constructor_exists():
    assert callable(qm::Tool.__init__)


def test_qm::tool_constructor_args():
    sig = inspect.signature(qm::Tool.__init__)
    params = list(sig.parameters.keys())



def test_qm::measurementmethod_is_not_abstract():
    assert not inspect.isabstract(qm::MeasurementMethod)


def test_qm::measurementmethod_constructor_exists():
    assert callable(qm::MeasurementMethod.__init__)


def test_qm::measurementmethod_constructor_args():
    sig = inspect.signature(qm::MeasurementMethod.__init__)
    params = list(sig.parameters.keys())



def test_qm::measure_is_not_abstract():
    assert not inspect.isabstract(qm::Measure)


def test_qm::measure_constructor_exists():
    assert callable(qm::Measure.__init__)


def test_qm::measure_constructor_args():
    sig = inspect.signature(qm::Measure.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_qm::measure_has_type():
    assert hasattr(qm::Measure, "type")
    descriptor = None
    for klass in qm::Measure.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_qm::evaluation_is_not_abstract():
    assert not inspect.isabstract(qm::Evaluation)


def test_qm::evaluation_constructor_exists():
    assert callable(qm::Evaluation.__init__)


def test_qm::evaluation_constructor_args():
    sig = inspect.signature(qm::Evaluation.__init__)
    params = list(sig.parameters.keys())
    assert "completeness" in params, "Missing parameter 'completeness'"
    assert "maximumPoints" in params, "Missing parameter 'maximumPoints'"

def test_qm::evaluation_has_completeness():
    assert hasattr(qm::Evaluation, "completeness")
    descriptor = None
    for klass in qm::Evaluation.__mro__:
        if "completeness" in klass.__dict__:
            descriptor = klass.__dict__["completeness"]
            break
    assert isinstance(descriptor, property)

def test_qm::evaluation_has_maximumPoints():
    assert hasattr(qm::Evaluation, "maximumPoints")
    descriptor = None
    for klass in qm::Evaluation.__mro__:
        if "maximumPoints" in klass.__dict__:
            descriptor = klass.__dict__["maximumPoints"]
            break
    assert isinstance(descriptor, property)



def test_qm::factor_is_not_abstract():
    assert not inspect.isabstract(qm::Factor)


def test_qm::factor_constructor_exists():
    assert callable(qm::Factor.__init__)


def test_qm::factor_constructor_args():
    sig = inspect.signature(qm::Factor.__init__)
    params = list(sig.parameters.keys())



def test_qm::entity_is_not_abstract():
    assert not inspect.isabstract(qm::Entity)


def test_qm::entity_constructor_exists():
    assert callable(qm::Entity.__init__)


def test_qm::entity_constructor_args():
    sig = inspect.signature(qm::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "useCase" in params, "Missing parameter 'useCase'"
    assert "stakeholder" in params, "Missing parameter 'stakeholder'"

def test_qm::entity_has_useCase():
    assert hasattr(qm::Entity, "useCase")
    descriptor = None
    for klass in qm::Entity.__mro__:
        if "useCase" in klass.__dict__:
            descriptor = klass.__dict__["useCase"]
            break
    assert isinstance(descriptor, property)

def test_qm::entity_has_stakeholder():
    assert hasattr(qm::Entity, "stakeholder")
    descriptor = None
    for klass in qm::Entity.__mro__:
        if "stakeholder" in klass.__dict__:
            descriptor = klass.__dict__["stakeholder"]
            break
    assert isinstance(descriptor, property)



def test_evaluationresult_is_not_abstract():
    assert not inspect.isabstract(EvaluationResult)


def test_evaluationresult_constructor_exists():
    assert callable(EvaluationResult.__init__)


def test_evaluationresult_constructor_args():
    sig = inspect.signature(EvaluationResult.__init__)
    params = list(sig.parameters.keys())



def test_qm::multimeasureevaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm::MultiMeasureEvaluationResult)


def test_qm::multimeasureevaluationresult_constructor_exists():
    assert callable(qm::MultiMeasureEvaluationResult.__init__)


def test_qm::multimeasureevaluationresult_constructor_args():
    sig = inspect.signature(qm::MultiMeasureEvaluationResult.__init__)
    params = list(sig.parameters.keys())



def test_qm::singlemeasureevaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm::SingleMeasureEvaluationResult)


def test_qm::singlemeasureevaluationresult_constructor_exists():
    assert callable(qm::SingleMeasureEvaluationResult.__init__)


def test_qm::singlemeasureevaluationresult_constructor_args():
    sig = inspect.signature(qm::SingleMeasureEvaluationResult.__init__)
    params = list(sig.parameters.keys())
    assert "ratioAffected" in params, "Missing parameter 'ratioAffected'"

def test_qm::singlemeasureevaluationresult_has_ratioAffected():
    assert hasattr(qm::SingleMeasureEvaluationResult, "ratioAffected")
    descriptor = None
    for klass in qm::SingleMeasureEvaluationResult.__mro__:
        if "ratioAffected" in klass.__dict__:
            descriptor = klass.__dict__["ratioAffected"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "NUMBER",
        "NONE",
        "FINDINGS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_effect_exists():
    # Check that the Enumeration exists
    assert Effect is not None

def test_effect_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Effect]
    expected_literals = [
        "NEGATIVE",
        "POSITIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Effect"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
qm::Result_strategy = st.builds(
    qm::Result,
    message=
        safe_text
)
qm::MeasureRankingEvaluationResult_strategy = st.builds(
    qm::MeasureRankingEvaluationResult,
    ratioAffected=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
qm::FindingMessage_strategy = st.builds(
    qm::FindingMessage,
    message=
        safe_text,
    location=
        safe_text
)
qm::DoubleInterval_strategy = st.builds(
    qm::DoubleInterval,
    lower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    upper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MeasurementResult_strategy = st.builds(
    MeasurementResult,
)
qm::FindingsMeasurementResult_strategy = st.builds(
    qm::FindingsMeasurementResult,
    count=
        st.integers(),
    findings=
        safe_text
)
qm::NumberMeasurementResult_strategy = st.builds(
    qm::NumberMeasurementResult,
)
Result_strategy = st.builds(
    Result,
)
qm::EvaluationResult_strategy = st.builds(
    qm::EvaluationResult,
)
qm::MeasurementResult_strategy = st.builds(
    qm::MeasurementResult,
)
qm::QualityModelResult_strategy = st.builds(
    qm::QualityModelResult,
    date=
        st.dates(),
    system=
        safe_text
)
MultiMeasureEvaluation_strategy = st.builds(
    MultiMeasureEvaluation,
)
qm::WeightedSumMultiMeasureEvaluation_strategy = st.builds(
    qm::WeightedSumMultiMeasureEvaluation,
)
qm::Ranking_strategy = st.builds(
    qm::Ranking,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rank=
        st.integers()
)
qm::MeasureEvaluation_strategy = st.builds(
    qm::MeasureEvaluation,
    range=
        safe_text
)
FormBasedMeasureAggregation_strategy = st.builds(
    FormBasedMeasureAggregation,
)
qm::NumberMeanMeasureAggregation_strategy = st.builds(
    qm::NumberMeanMeasureAggregation,
)
qm::FindingsUnionMeasureAggregation_strategy = st.builds(
    qm::FindingsUnionMeasureAggregation,
)
FactorAggregation_strategy = st.builds(
    FactorAggregation,
)
qm::WeightedSumFactorAggregation_strategy = st.builds(
    qm::WeightedSumFactorAggregation,
)
LinearFunction_strategy = st.builds(
    LinearFunction,
)
qm::LinearDecreasingFunction_strategy = st.builds(
    qm::LinearDecreasingFunction,
)
qm::LinearIncreasingFunction_strategy = st.builds(
    qm::LinearIncreasingFunction,
)
qm::Function_strategy = st.builds(
    qm::Function,
)
Function_strategy = st.builds(
    Function,
)
qm::LinearFunction_strategy = st.builds(
    qm::LinearFunction,
    lowerBound=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    upperBound=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Ranking_strategy = st.builds(
    Ranking,
)
qm::FactorRanking_strategy = st.builds(
    qm::FactorRanking,
)
MeasureAggregation_strategy = st.builds(
    MeasureAggregation,
)
qm::FormBasedMeasureAggregation_strategy = st.builds(
    qm::FormBasedMeasureAggregation,
)
qm::TextAggregation_strategy = st.builds(
    qm::TextAggregation,
    specification=
        safe_text
)
TextAggregation_strategy = st.builds(
    TextAggregation,
)
qm::QIESLAggregation_strategy = st.builds(
    qm::QIESLAggregation,
)
Measure_strategy = st.builds(
    Measure,
)
qm::NormalizationMeasure_strategy = st.builds(
    qm::NormalizationMeasure,
)
MeasureEvaluation_strategy = st.builds(
    MeasureEvaluation,
)
qm::MeasureRanking_strategy = st.builds(
    qm::MeasureRanking,
)
FormBasedEvaluation_strategy = st.builds(
    FormBasedEvaluation,
)
qm::SingleMeasureEvaluation_strategy = st.builds(
    qm::SingleMeasureEvaluation,
)
qm::FactorAggregation_strategy = st.builds(
    qm::FactorAggregation,
)
qm::MultiMeasureEvaluation_strategy = st.builds(
    qm::MultiMeasureEvaluation,
)
Evaluation_strategy = st.builds(
    Evaluation,
)
qm::FormBasedEvaluation_strategy = st.builds(
    qm::FormBasedEvaluation,
)
qm::ManualEvaluation_strategy = st.builds(
    qm::ManualEvaluation,
)
qm::TextEvaluation_strategy = st.builds(
    qm::TextEvaluation,
    specification=
        safe_text
)
TextEvaluation_strategy = st.builds(
    TextEvaluation,
)
qm::QIESLEvaluation_strategy = st.builds(
    qm::QIESLEvaluation,
)
Instrument_strategy = st.builds(
    Instrument,
)
qm::ToolBasedInstrument_strategy = st.builds(
    qm::ToolBasedInstrument,
    metric=
        safe_text
)
MeasurementMethod_strategy = st.builds(
    MeasurementMethod,
)
qm::Instrument_strategy = st.builds(
    qm::Instrument,
)
CharacterizingElement_strategy = st.builds(
    CharacterizingElement,
)
QualityModelElement_strategy = st.builds(
    QualityModelElement,
)
qm::TaggedElement_strategy = st.builds(
    qm::TaggedElement,
)
qm::AnnotationBase_strategy = st.builds(
    qm::AnnotationBase,
)
qm::Annotation_strategy = st.builds(
    qm::Annotation,
    key=
        safe_text,
    value=
        safe_text
)
TaggedElement_strategy = st.builds(
    TaggedElement,
)
qm::AnnotatedElement_strategy = st.builds(
    qm::AnnotatedElement,
)
qm::QualityModelElement_strategy = st.builds(
    qm::QualityModelElement,
    qualifiedName=
        safe_text
)
DescribedElement_strategy = st.builds(
    DescribedElement,
)
qm::NamedElement_strategy = st.builds(
    qm::NamedElement,
    title=
        safe_text,
    name=
        safe_text
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
qm::Decomposition_strategy = st.builds(
    qm::Decomposition,
)
qm::Measurement_strategy = st.builds(
    qm::Measurement,
)
qm::MeasureRefinement_strategy = st.builds(
    qm::MeasureRefinement,
)
qm::FactorRefinement_strategy = st.builds(
    qm::FactorRefinement,
)
qm::Impact_strategy = st.builds(
    qm::Impact,
    justification=
        safe_text,
    effect=
        safe_text
)
qm::Specialization_strategy = st.builds(
    qm::Specialization,
)
qm::DescribedElement_strategy = st.builds(
    qm::DescribedElement,
    description=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
qm::MeasureAggregation_strategy = st.builds(
    qm::MeasureAggregation,
)
qm::ManualInstrument_strategy = st.builds(
    qm::ManualInstrument,
)
qm::CharacterizingElement_strategy = st.builds(
    qm::CharacterizingElement,
)
qm::QualityModel_strategy = st.builds(
    qm::QualityModel,
    schoolGradeBoundary2=
        safe_text,
    schoolGradeBoundary6=
        safe_text,
    schoolGradeBoundary3=
        safe_text,
    schoolGradeBoundary5=
        safe_text,
    schoolGradeBoundary4=
        safe_text
)
qm::Source_strategy = st.builds(
    qm::Source,
)
qm::Tag_strategy = st.builds(
    qm::Tag,
)
qm::Tool_strategy = st.builds(
    qm::Tool,
)
qm::MeasurementMethod_strategy = st.builds(
    qm::MeasurementMethod,
)
qm::Measure_strategy = st.builds(
    qm::Measure,
    type=
        safe_text
)
qm::Evaluation_strategy = st.builds(
    qm::Evaluation,
    completeness=
        st.integers(),
    maximumPoints=
        st.integers()
)
qm::Factor_strategy = st.builds(
    qm::Factor,
)
qm::Entity_strategy = st.builds(
    qm::Entity,
    useCase=
        st.booleans(),
    stakeholder=
        st.booleans()
)
EvaluationResult_strategy = st.builds(
    EvaluationResult,
)
qm::MultiMeasureEvaluationResult_strategy = st.builds(
    qm::MultiMeasureEvaluationResult,
)
qm::SingleMeasureEvaluationResult_strategy = st.builds(
    qm::SingleMeasureEvaluationResult,
    ratioAffected=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=qm::Result_strategy)
@settings(max_examples=50)
def test_qm::result_instantiation(instance):
    assert isinstance(instance, qm::Result)

@given(instance=qm::Result_strategy)
def test_qm::result_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=qm::Result_strategy)
def test_qm::result_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=qm::MeasureRankingEvaluationResult_strategy)
@settings(max_examples=50)
def test_qm::measurerankingevaluationresult_instantiation(instance):
    assert isinstance(instance, qm::MeasureRankingEvaluationResult)

@given(instance=qm::MeasureRankingEvaluationResult_strategy)
def test_qm::measurerankingevaluationresult_ratioAffected_type(instance):
    assert isinstance(instance.ratioAffected, float)


@given(instance=qm::MeasureRankingEvaluationResult_strategy)
def test_qm::measurerankingevaluationresult_ratioAffected_setter(instance):
    original = instance.ratioAffected
    instance.ratioAffected = original
    assert instance.ratioAffected == original

@given(instance=qm::FindingMessage_strategy)
@settings(max_examples=50)
def test_qm::findingmessage_instantiation(instance):
    assert isinstance(instance, qm::FindingMessage)

@given(instance=qm::FindingMessage_strategy)
def test_qm::findingmessage_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=qm::FindingMessage_strategy)
def test_qm::findingmessage_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=qm::FindingMessage_strategy)
def test_qm::findingmessage_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=qm::FindingMessage_strategy)
def test_qm::findingmessage_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=qm::DoubleInterval_strategy)
@settings(max_examples=50)
def test_qm::doubleinterval_instantiation(instance):
    assert isinstance(instance, qm::DoubleInterval)

@given(instance=qm::DoubleInterval_strategy)
def test_qm::doubleinterval_lower_type(instance):
    assert isinstance(instance.lower, float)


@given(instance=qm::DoubleInterval_strategy)
def test_qm::doubleinterval_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=qm::DoubleInterval_strategy)
def test_qm::doubleinterval_upper_type(instance):
    assert isinstance(instance.upper, float)


@given(instance=qm::DoubleInterval_strategy)
def test_qm::doubleinterval_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=MeasurementResult_strategy)
@settings(max_examples=50)
def test_measurementresult_instantiation(instance):
    assert isinstance(instance, MeasurementResult)

@given(instance=qm::FindingsMeasurementResult_strategy)
@settings(max_examples=50)
def test_qm::findingsmeasurementresult_instantiation(instance):
    assert isinstance(instance, qm::FindingsMeasurementResult)

@given(instance=qm::FindingsMeasurementResult_strategy)
def test_qm::findingsmeasurementresult_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=qm::FindingsMeasurementResult_strategy)
def test_qm::findingsmeasurementresult_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=qm::FindingsMeasurementResult_strategy)
def test_qm::findingsmeasurementresult_findings_type(instance):
    assert isinstance(instance.findings, str)


@given(instance=qm::FindingsMeasurementResult_strategy)
def test_qm::findingsmeasurementresult_findings_setter(instance):
    original = instance.findings
    instance.findings = original
    assert instance.findings == original

@given(instance=qm::NumberMeasurementResult_strategy)
@settings(max_examples=50)
def test_qm::numbermeasurementresult_instantiation(instance):
    assert isinstance(instance, qm::NumberMeasurementResult)

@given(instance=Result_strategy)
@settings(max_examples=50)
def test_result_instantiation(instance):
    assert isinstance(instance, Result)

@given(instance=qm::EvaluationResult_strategy)
@settings(max_examples=50)
def test_qm::evaluationresult_instantiation(instance):
    assert isinstance(instance, qm::EvaluationResult)

@given(instance=qm::MeasurementResult_strategy)
@settings(max_examples=50)
def test_qm::measurementresult_instantiation(instance):
    assert isinstance(instance, qm::MeasurementResult)

@given(instance=qm::QualityModelResult_strategy)
@settings(max_examples=50)
def test_qm::qualitymodelresult_instantiation(instance):
    assert isinstance(instance, qm::QualityModelResult)

@given(instance=qm::QualityModelResult_strategy)
def test_qm::qualitymodelresult_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=qm::QualityModelResult_strategy)
def test_qm::qualitymodelresult_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=qm::QualityModelResult_strategy)
def test_qm::qualitymodelresult_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=qm::QualityModelResult_strategy)
def test_qm::qualitymodelresult_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=MultiMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_multimeasureevaluation_instantiation(instance):
    assert isinstance(instance, MultiMeasureEvaluation)

@given(instance=qm::WeightedSumMultiMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm::weightedsummultimeasureevaluation_instantiation(instance):
    assert isinstance(instance, qm::WeightedSumMultiMeasureEvaluation)

@given(instance=qm::Ranking_strategy)
@settings(max_examples=50)
def test_qm::ranking_instantiation(instance):
    assert isinstance(instance, qm::Ranking)

@given(instance=qm::Ranking_strategy)
def test_qm::ranking_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=qm::Ranking_strategy)
def test_qm::ranking_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=qm::Ranking_strategy)
def test_qm::ranking_rank_type(instance):
    assert isinstance(instance.rank, int)


@given(instance=qm::Ranking_strategy)
def test_qm::ranking_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=qm::MeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm::measureevaluation_instantiation(instance):
    assert isinstance(instance, qm::MeasureEvaluation)

@given(instance=qm::MeasureEvaluation_strategy)
def test_qm::measureevaluation_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=qm::MeasureEvaluation_strategy)
def test_qm::measureevaluation_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=FormBasedMeasureAggregation_strategy)
@settings(max_examples=50)
def test_formbasedmeasureaggregation_instantiation(instance):
    assert isinstance(instance, FormBasedMeasureAggregation)

@given(instance=qm::NumberMeanMeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm::numbermeanmeasureaggregation_instantiation(instance):
    assert isinstance(instance, qm::NumberMeanMeasureAggregation)

@given(instance=qm::FindingsUnionMeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm::findingsunionmeasureaggregation_instantiation(instance):
    assert isinstance(instance, qm::FindingsUnionMeasureAggregation)

@given(instance=FactorAggregation_strategy)
@settings(max_examples=50)
def test_factoraggregation_instantiation(instance):
    assert isinstance(instance, FactorAggregation)

@given(instance=qm::WeightedSumFactorAggregation_strategy)
@settings(max_examples=50)
def test_qm::weightedsumfactoraggregation_instantiation(instance):
    assert isinstance(instance, qm::WeightedSumFactorAggregation)

@given(instance=LinearFunction_strategy)
@settings(max_examples=50)
def test_linearfunction_instantiation(instance):
    assert isinstance(instance, LinearFunction)

@given(instance=qm::LinearDecreasingFunction_strategy)
@settings(max_examples=50)
def test_qm::lineardecreasingfunction_instantiation(instance):
    assert isinstance(instance, qm::LinearDecreasingFunction)

@given(instance=qm::LinearIncreasingFunction_strategy)
@settings(max_examples=50)
def test_qm::linearincreasingfunction_instantiation(instance):
    assert isinstance(instance, qm::LinearIncreasingFunction)

@given(instance=qm::Function_strategy)
@settings(max_examples=50)
def test_qm::function_instantiation(instance):
    assert isinstance(instance, qm::Function)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=qm::LinearFunction_strategy)
@settings(max_examples=50)
def test_qm::linearfunction_instantiation(instance):
    assert isinstance(instance, qm::LinearFunction)

@given(instance=qm::LinearFunction_strategy)
def test_qm::linearfunction_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, float)


@given(instance=qm::LinearFunction_strategy)
def test_qm::linearfunction_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=qm::LinearFunction_strategy)
def test_qm::linearfunction_upperBound_type(instance):
    assert isinstance(instance.upperBound, float)


@given(instance=qm::LinearFunction_strategy)
def test_qm::linearfunction_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=Ranking_strategy)
@settings(max_examples=50)
def test_ranking_instantiation(instance):
    assert isinstance(instance, Ranking)

@given(instance=qm::FactorRanking_strategy)
@settings(max_examples=50)
def test_qm::factorranking_instantiation(instance):
    assert isinstance(instance, qm::FactorRanking)

@given(instance=MeasureAggregation_strategy)
@settings(max_examples=50)
def test_measureaggregation_instantiation(instance):
    assert isinstance(instance, MeasureAggregation)

@given(instance=qm::FormBasedMeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm::formbasedmeasureaggregation_instantiation(instance):
    assert isinstance(instance, qm::FormBasedMeasureAggregation)

@given(instance=qm::TextAggregation_strategy)
@settings(max_examples=50)
def test_qm::textaggregation_instantiation(instance):
    assert isinstance(instance, qm::TextAggregation)

@given(instance=qm::TextAggregation_strategy)
def test_qm::textaggregation_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=qm::TextAggregation_strategy)
def test_qm::textaggregation_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=TextAggregation_strategy)
@settings(max_examples=50)
def test_textaggregation_instantiation(instance):
    assert isinstance(instance, TextAggregation)

@given(instance=qm::QIESLAggregation_strategy)
@settings(max_examples=50)
def test_qm::qieslaggregation_instantiation(instance):
    assert isinstance(instance, qm::QIESLAggregation)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=qm::NormalizationMeasure_strategy)
@settings(max_examples=50)
def test_qm::normalizationmeasure_instantiation(instance):
    assert isinstance(instance, qm::NormalizationMeasure)

@given(instance=MeasureEvaluation_strategy)
@settings(max_examples=50)
def test_measureevaluation_instantiation(instance):
    assert isinstance(instance, MeasureEvaluation)

@given(instance=qm::MeasureRanking_strategy)
@settings(max_examples=50)
def test_qm::measureranking_instantiation(instance):
    assert isinstance(instance, qm::MeasureRanking)

@given(instance=FormBasedEvaluation_strategy)
@settings(max_examples=50)
def test_formbasedevaluation_instantiation(instance):
    assert isinstance(instance, FormBasedEvaluation)

@given(instance=qm::SingleMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm::singlemeasureevaluation_instantiation(instance):
    assert isinstance(instance, qm::SingleMeasureEvaluation)

@given(instance=qm::FactorAggregation_strategy)
@settings(max_examples=50)
def test_qm::factoraggregation_instantiation(instance):
    assert isinstance(instance, qm::FactorAggregation)

@given(instance=qm::MultiMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm::multimeasureevaluation_instantiation(instance):
    assert isinstance(instance, qm::MultiMeasureEvaluation)

@given(instance=Evaluation_strategy)
@settings(max_examples=50)
def test_evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)

@given(instance=qm::FormBasedEvaluation_strategy)
@settings(max_examples=50)
def test_qm::formbasedevaluation_instantiation(instance):
    assert isinstance(instance, qm::FormBasedEvaluation)

@given(instance=qm::ManualEvaluation_strategy)
@settings(max_examples=50)
def test_qm::manualevaluation_instantiation(instance):
    assert isinstance(instance, qm::ManualEvaluation)

@given(instance=qm::TextEvaluation_strategy)
@settings(max_examples=50)
def test_qm::textevaluation_instantiation(instance):
    assert isinstance(instance, qm::TextEvaluation)

@given(instance=qm::TextEvaluation_strategy)
def test_qm::textevaluation_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=qm::TextEvaluation_strategy)
def test_qm::textevaluation_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=TextEvaluation_strategy)
@settings(max_examples=50)
def test_textevaluation_instantiation(instance):
    assert isinstance(instance, TextEvaluation)

@given(instance=qm::QIESLEvaluation_strategy)
@settings(max_examples=50)
def test_qm::qieslevaluation_instantiation(instance):
    assert isinstance(instance, qm::QIESLEvaluation)

@given(instance=Instrument_strategy)
@settings(max_examples=50)
def test_instrument_instantiation(instance):
    assert isinstance(instance, Instrument)

@given(instance=qm::ToolBasedInstrument_strategy)
@settings(max_examples=50)
def test_qm::toolbasedinstrument_instantiation(instance):
    assert isinstance(instance, qm::ToolBasedInstrument)

@given(instance=qm::ToolBasedInstrument_strategy)
def test_qm::toolbasedinstrument_metric_type(instance):
    assert isinstance(instance.metric, str)


@given(instance=qm::ToolBasedInstrument_strategy)
def test_qm::toolbasedinstrument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original

@given(instance=MeasurementMethod_strategy)
@settings(max_examples=50)
def test_measurementmethod_instantiation(instance):
    assert isinstance(instance, MeasurementMethod)

@given(instance=qm::Instrument_strategy)
@settings(max_examples=50)
def test_qm::instrument_instantiation(instance):
    assert isinstance(instance, qm::Instrument)

@given(instance=CharacterizingElement_strategy)
@settings(max_examples=50)
def test_characterizingelement_instantiation(instance):
    assert isinstance(instance, CharacterizingElement)

@given(instance=QualityModelElement_strategy)
@settings(max_examples=50)
def test_qualitymodelelement_instantiation(instance):
    assert isinstance(instance, QualityModelElement)

@given(instance=qm::TaggedElement_strategy)
@settings(max_examples=50)
def test_qm::taggedelement_instantiation(instance):
    assert isinstance(instance, qm::TaggedElement)

@given(instance=qm::AnnotationBase_strategy)
@settings(max_examples=50)
def test_qm::annotationbase_instantiation(instance):
    assert isinstance(instance, qm::AnnotationBase)

@given(instance=qm::Annotation_strategy)
@settings(max_examples=50)
def test_qm::annotation_instantiation(instance):
    assert isinstance(instance, qm::Annotation)

@given(instance=qm::Annotation_strategy)
def test_qm::annotation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=qm::Annotation_strategy)
def test_qm::annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=qm::Annotation_strategy)
def test_qm::annotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=qm::Annotation_strategy)
def test_qm::annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TaggedElement_strategy)
@settings(max_examples=50)
def test_taggedelement_instantiation(instance):
    assert isinstance(instance, TaggedElement)

@given(instance=qm::AnnotatedElement_strategy)
@settings(max_examples=50)
def test_qm::annotatedelement_instantiation(instance):
    assert isinstance(instance, qm::AnnotatedElement)

@given(instance=qm::QualityModelElement_strategy)
@settings(max_examples=50)
def test_qm::qualitymodelelement_instantiation(instance):
    assert isinstance(instance, qm::QualityModelElement)

@given(instance=qm::QualityModelElement_strategy)
def test_qm::qualitymodelelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=qm::QualityModelElement_strategy)
def test_qm::qualitymodelelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=DescribedElement_strategy)
@settings(max_examples=50)
def test_describedelement_instantiation(instance):
    assert isinstance(instance, DescribedElement)

@given(instance=qm::NamedElement_strategy)
@settings(max_examples=50)
def test_qm::namedelement_instantiation(instance):
    assert isinstance(instance, qm::NamedElement)

@given(instance=qm::NamedElement_strategy)
def test_qm::namedelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=qm::NamedElement_strategy)
def test_qm::namedelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=qm::NamedElement_strategy)
def test_qm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=qm::NamedElement_strategy)
def test_qm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=qm::Decomposition_strategy)
@settings(max_examples=50)
def test_qm::decomposition_instantiation(instance):
    assert isinstance(instance, qm::Decomposition)

@given(instance=qm::Measurement_strategy)
@settings(max_examples=50)
def test_qm::measurement_instantiation(instance):
    assert isinstance(instance, qm::Measurement)

@given(instance=qm::MeasureRefinement_strategy)
@settings(max_examples=50)
def test_qm::measurerefinement_instantiation(instance):
    assert isinstance(instance, qm::MeasureRefinement)

@given(instance=qm::FactorRefinement_strategy)
@settings(max_examples=50)
def test_qm::factorrefinement_instantiation(instance):
    assert isinstance(instance, qm::FactorRefinement)

@given(instance=qm::Impact_strategy)
@settings(max_examples=50)
def test_qm::impact_instantiation(instance):
    assert isinstance(instance, qm::Impact)

@given(instance=qm::Impact_strategy)
def test_qm::impact_justification_type(instance):
    assert isinstance(instance.justification, str)


@given(instance=qm::Impact_strategy)
def test_qm::impact_justification_setter(instance):
    original = instance.justification
    instance.justification = original
    assert instance.justification == original

@given(instance=qm::Impact_strategy)
def test_qm::impact_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=qm::Impact_strategy)
def test_qm::impact_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=qm::Specialization_strategy)
@settings(max_examples=50)
def test_qm::specialization_instantiation(instance):
    assert isinstance(instance, qm::Specialization)

@given(instance=qm::DescribedElement_strategy)
@settings(max_examples=50)
def test_qm::describedelement_instantiation(instance):
    assert isinstance(instance, qm::DescribedElement)

@given(instance=qm::DescribedElement_strategy)
def test_qm::describedelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=qm::DescribedElement_strategy)
def test_qm::describedelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=qm::MeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm::measureaggregation_instantiation(instance):
    assert isinstance(instance, qm::MeasureAggregation)

@given(instance=qm::ManualInstrument_strategy)
@settings(max_examples=50)
def test_qm::manualinstrument_instantiation(instance):
    assert isinstance(instance, qm::ManualInstrument)

@given(instance=qm::CharacterizingElement_strategy)
@settings(max_examples=50)
def test_qm::characterizingelement_instantiation(instance):
    assert isinstance(instance, qm::CharacterizingElement)

@given(instance=qm::QualityModel_strategy)
@settings(max_examples=50)
def test_qm::qualitymodel_instantiation(instance):
    assert isinstance(instance, qm::QualityModel)

@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary2_type(instance):
    assert isinstance(instance.schoolGradeBoundary2, str)


@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary2_setter(instance):
    original = instance.schoolGradeBoundary2
    instance.schoolGradeBoundary2 = original
    assert instance.schoolGradeBoundary2 == original

@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary6_type(instance):
    assert isinstance(instance.schoolGradeBoundary6, str)


@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary6_setter(instance):
    original = instance.schoolGradeBoundary6
    instance.schoolGradeBoundary6 = original
    assert instance.schoolGradeBoundary6 == original

@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary3_type(instance):
    assert isinstance(instance.schoolGradeBoundary3, str)


@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary3_setter(instance):
    original = instance.schoolGradeBoundary3
    instance.schoolGradeBoundary3 = original
    assert instance.schoolGradeBoundary3 == original

@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary5_type(instance):
    assert isinstance(instance.schoolGradeBoundary5, str)


@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary5_setter(instance):
    original = instance.schoolGradeBoundary5
    instance.schoolGradeBoundary5 = original
    assert instance.schoolGradeBoundary5 == original

@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary4_type(instance):
    assert isinstance(instance.schoolGradeBoundary4, str)


@given(instance=qm::QualityModel_strategy)
def test_qm::qualitymodel_schoolGradeBoundary4_setter(instance):
    original = instance.schoolGradeBoundary4
    instance.schoolGradeBoundary4 = original
    assert instance.schoolGradeBoundary4 == original

@given(instance=qm::Source_strategy)
@settings(max_examples=50)
def test_qm::source_instantiation(instance):
    assert isinstance(instance, qm::Source)

@given(instance=qm::Tag_strategy)
@settings(max_examples=50)
def test_qm::tag_instantiation(instance):
    assert isinstance(instance, qm::Tag)

@given(instance=qm::Tool_strategy)
@settings(max_examples=50)
def test_qm::tool_instantiation(instance):
    assert isinstance(instance, qm::Tool)

@given(instance=qm::MeasurementMethod_strategy)
@settings(max_examples=50)
def test_qm::measurementmethod_instantiation(instance):
    assert isinstance(instance, qm::MeasurementMethod)

@given(instance=qm::Measure_strategy)
@settings(max_examples=50)
def test_qm::measure_instantiation(instance):
    assert isinstance(instance, qm::Measure)

@given(instance=qm::Measure_strategy)
def test_qm::measure_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=qm::Measure_strategy)
def test_qm::measure_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=qm::Evaluation_strategy)
@settings(max_examples=50)
def test_qm::evaluation_instantiation(instance):
    assert isinstance(instance, qm::Evaluation)

@given(instance=qm::Evaluation_strategy)
def test_qm::evaluation_completeness_type(instance):
    assert isinstance(instance.completeness, int)


@given(instance=qm::Evaluation_strategy)
def test_qm::evaluation_completeness_setter(instance):
    original = instance.completeness
    instance.completeness = original
    assert instance.completeness == original

@given(instance=qm::Evaluation_strategy)
def test_qm::evaluation_maximumPoints_type(instance):
    assert isinstance(instance.maximumPoints, int)


@given(instance=qm::Evaluation_strategy)
def test_qm::evaluation_maximumPoints_setter(instance):
    original = instance.maximumPoints
    instance.maximumPoints = original
    assert instance.maximumPoints == original

@given(instance=qm::Factor_strategy)
@settings(max_examples=50)
def test_qm::factor_instantiation(instance):
    assert isinstance(instance, qm::Factor)

@given(instance=qm::Entity_strategy)
@settings(max_examples=50)
def test_qm::entity_instantiation(instance):
    assert isinstance(instance, qm::Entity)

@given(instance=qm::Entity_strategy)
def test_qm::entity_useCase_type(instance):
    assert isinstance(instance.useCase, bool)


@given(instance=qm::Entity_strategy)
def test_qm::entity_useCase_setter(instance):
    original = instance.useCase
    instance.useCase = original
    assert instance.useCase == original

@given(instance=qm::Entity_strategy)
def test_qm::entity_stakeholder_type(instance):
    assert isinstance(instance.stakeholder, bool)


@given(instance=qm::Entity_strategy)
def test_qm::entity_stakeholder_setter(instance):
    original = instance.stakeholder
    instance.stakeholder = original
    assert instance.stakeholder == original

@given(instance=EvaluationResult_strategy)
@settings(max_examples=50)
def test_evaluationresult_instantiation(instance):
    assert isinstance(instance, EvaluationResult)

@given(instance=qm::MultiMeasureEvaluationResult_strategy)
@settings(max_examples=50)
def test_qm::multimeasureevaluationresult_instantiation(instance):
    assert isinstance(instance, qm::MultiMeasureEvaluationResult)

@given(instance=qm::SingleMeasureEvaluationResult_strategy)
@settings(max_examples=50)
def test_qm::singlemeasureevaluationresult_instantiation(instance):
    assert isinstance(instance, qm::SingleMeasureEvaluationResult)

@given(instance=qm::SingleMeasureEvaluationResult_strategy)
def test_qm::singlemeasureevaluationresult_ratioAffected_type(instance):
    assert isinstance(instance.ratioAffected, float)


@given(instance=qm::SingleMeasureEvaluationResult_strategy)
def test_qm::singlemeasureevaluationresult_ratioAffected_setter(instance):
    original = instance.ratioAffected
    instance.ratioAffected = original
    assert instance.ratioAffected == original
