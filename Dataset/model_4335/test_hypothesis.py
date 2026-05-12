import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    qm_Result,
    qm_MeasureRankingEvaluationResult,
    EvaluationResult,
    qm_MultiMeasureEvaluationResult,
    qm_SingleMeasureEvaluationResult,
    MultiMeasureEvaluation,
    qm_WeightedSumMultiMeasureEvaluation,
    qm_Ranking,
    qm_MeasureEvaluation,
    FormBasedMeasureAggregation,
    qm_NumberMeanMeasureAggregation,
    qm_FindingsUnionMeasureAggregation,
    FactorAggregation,
    qm_WeightedSumFactorAggregation,
    LinearFunction,
    qm_LinearDecreasingFunction,
    qm_LinearIncreasingFunction,
    qm_FindingMessage,
    qm_DoubleInterval,
    MeasurementResult,
    qm_FindingsMeasurementResult,
    qm_NumberMeasurementResult,
    Result,
    qm_EvaluationResult,
    qm_MeasurementResult,
    qm_QualityModelResult,
    Instrument,
    qm_ToolBasedInstrument,
    MeasurementMethod,
    qm_Instrument,
    qm_Function,
    Function,
    qm_LinearFunction,
    Ranking,
    qm_FactorRanking,
    MeasureAggregation,
    qm_FormBasedMeasureAggregation,
    qm_TextAggregation,
    TextAggregation,
    qm_QIESLAggregation,
    Measure,
    qm_NormalizationMeasure,
    MeasureEvaluation,
    qm_MeasureRanking,
    FormBasedEvaluation,
    qm_FactorAggregation,
    qm_MultiMeasureEvaluation,
    qm_SingleMeasureEvaluation,
    Evaluation,
    qm_ManualEvaluation,
    qm_FormBasedEvaluation,
    qm_TextEvaluation,
    TextEvaluation,
    qm_QIESLEvaluation,
    CharacterizingElement,
    qm_Annotation,
    TaggedElement,
    qm_AnnotatedElement,
    DescribedElement,
    qm_NamedElement,
    AnnotatedElement,
    qm_Decomposition,
    qm_Impact,
    qm_MeasureRefinement,
    qm_FactorRefinement,
    qm_Measurement,
    qm_DescribedElement,
    qm_QualityModelElement,
    qm_Specialization,
    QualityModelElement,
    qm_TaggedElement,
    qm_AnnotationBase,
    NamedElement,
    qm_CharacterizingElement,
    qm_ManualInstrument,
    qm_Entity,
    qm_MeasureAggregation,
    qm_QualityModel,
    qm_Source,
    qm_Tag,
    qm_Tool,
    qm_MeasurementMethod,
    qm_Measure,
    qm_Evaluation,
    qm_Factor,
    Effect,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qm_result_is_not_abstract():
    assert not inspect.isabstract(qm_Result)


def test_qm_result_constructor_exists():
    assert callable(qm_Result.__init__)


def test_qm_result_constructor_args():
    sig = inspect.signature(qm_Result.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_qm_result_has_message():
    assert hasattr(qm_Result, "message")
    descriptor = None
    for klass in qm_Result.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_qm_measurerankingevaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm_MeasureRankingEvaluationResult)


def test_qm_measurerankingevaluationresult_constructor_exists():
    assert callable(qm_MeasureRankingEvaluationResult.__init__)


def test_qm_measurerankingevaluationresult_constructor_args():
    sig = inspect.signature(qm_MeasureRankingEvaluationResult.__init__)
    params = list(sig.parameters.keys())
    assert "ratioAffected" in params, "Missing parameter 'ratioAffected'"

def test_qm_measurerankingevaluationresult_has_ratioAffected():
    assert hasattr(qm_MeasureRankingEvaluationResult, "ratioAffected")
    descriptor = None
    for klass in qm_MeasureRankingEvaluationResult.__mro__:
        if "ratioAffected" in klass.__dict__:
            descriptor = klass.__dict__["ratioAffected"]
            break
    assert isinstance(descriptor, property)



def test_evaluationresult_is_not_abstract():
    assert not inspect.isabstract(EvaluationResult)


def test_evaluationresult_constructor_exists():
    assert callable(EvaluationResult.__init__)


def test_evaluationresult_constructor_args():
    sig = inspect.signature(EvaluationResult.__init__)
    params = list(sig.parameters.keys())



def test_qm_multimeasureevaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm_MultiMeasureEvaluationResult)


def test_qm_multimeasureevaluationresult_constructor_exists():
    assert callable(qm_MultiMeasureEvaluationResult.__init__)


def test_qm_multimeasureevaluationresult_constructor_args():
    sig = inspect.signature(qm_MultiMeasureEvaluationResult.__init__)
    params = list(sig.parameters.keys())



def test_qm_singlemeasureevaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm_SingleMeasureEvaluationResult)


def test_qm_singlemeasureevaluationresult_constructor_exists():
    assert callable(qm_SingleMeasureEvaluationResult.__init__)


def test_qm_singlemeasureevaluationresult_constructor_args():
    sig = inspect.signature(qm_SingleMeasureEvaluationResult.__init__)
    params = list(sig.parameters.keys())
    assert "ratioAffected" in params, "Missing parameter 'ratioAffected'"

def test_qm_singlemeasureevaluationresult_has_ratioAffected():
    assert hasattr(qm_SingleMeasureEvaluationResult, "ratioAffected")
    descriptor = None
    for klass in qm_SingleMeasureEvaluationResult.__mro__:
        if "ratioAffected" in klass.__dict__:
            descriptor = klass.__dict__["ratioAffected"]
            break
    assert isinstance(descriptor, property)



def test_multimeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(MultiMeasureEvaluation)


def test_multimeasureevaluation_constructor_exists():
    assert callable(MultiMeasureEvaluation.__init__)


def test_multimeasureevaluation_constructor_args():
    sig = inspect.signature(MultiMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_weightedsummultimeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_WeightedSumMultiMeasureEvaluation)


def test_qm_weightedsummultimeasureevaluation_constructor_exists():
    assert callable(qm_WeightedSumMultiMeasureEvaluation.__init__)


def test_qm_weightedsummultimeasureevaluation_constructor_args():
    sig = inspect.signature(qm_WeightedSumMultiMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_ranking_is_not_abstract():
    assert not inspect.isabstract(qm_Ranking)


def test_qm_ranking_constructor_exists():
    assert callable(qm_Ranking.__init__)


def test_qm_ranking_constructor_args():
    sig = inspect.signature(qm_Ranking.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_qm_ranking_has_weight():
    assert hasattr(qm_Ranking, "weight")
    descriptor = None
    for klass in qm_Ranking.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_qm_ranking_has_rank():
    assert hasattr(qm_Ranking, "rank")
    descriptor = None
    for klass in qm_Ranking.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_qm_measureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_MeasureEvaluation)


def test_qm_measureevaluation_constructor_exists():
    assert callable(qm_MeasureEvaluation.__init__)


def test_qm_measureevaluation_constructor_args():
    sig = inspect.signature(qm_MeasureEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"

def test_qm_measureevaluation_has_range():
    assert hasattr(qm_MeasureEvaluation, "range")
    descriptor = None
    for klass in qm_MeasureEvaluation.__mro__:
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



def test_qm_numbermeanmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm_NumberMeanMeasureAggregation)


def test_qm_numbermeanmeasureaggregation_constructor_exists():
    assert callable(qm_NumberMeanMeasureAggregation.__init__)


def test_qm_numbermeanmeasureaggregation_constructor_args():
    sig = inspect.signature(qm_NumberMeanMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm_findingsunionmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm_FindingsUnionMeasureAggregation)


def test_qm_findingsunionmeasureaggregation_constructor_exists():
    assert callable(qm_FindingsUnionMeasureAggregation.__init__)


def test_qm_findingsunionmeasureaggregation_constructor_args():
    sig = inspect.signature(qm_FindingsUnionMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_factoraggregation_is_not_abstract():
    assert not inspect.isabstract(FactorAggregation)


def test_factoraggregation_constructor_exists():
    assert callable(FactorAggregation.__init__)


def test_factoraggregation_constructor_args():
    sig = inspect.signature(FactorAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm_weightedsumfactoraggregation_is_not_abstract():
    assert not inspect.isabstract(qm_WeightedSumFactorAggregation)


def test_qm_weightedsumfactoraggregation_constructor_exists():
    assert callable(qm_WeightedSumFactorAggregation.__init__)


def test_qm_weightedsumfactoraggregation_constructor_args():
    sig = inspect.signature(qm_WeightedSumFactorAggregation.__init__)
    params = list(sig.parameters.keys())



def test_linearfunction_is_not_abstract():
    assert not inspect.isabstract(LinearFunction)


def test_linearfunction_constructor_exists():
    assert callable(LinearFunction.__init__)


def test_linearfunction_constructor_args():
    sig = inspect.signature(LinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_qm_lineardecreasingfunction_is_not_abstract():
    assert not inspect.isabstract(qm_LinearDecreasingFunction)


def test_qm_lineardecreasingfunction_constructor_exists():
    assert callable(qm_LinearDecreasingFunction.__init__)


def test_qm_lineardecreasingfunction_constructor_args():
    sig = inspect.signature(qm_LinearDecreasingFunction.__init__)
    params = list(sig.parameters.keys())



def test_qm_linearincreasingfunction_is_not_abstract():
    assert not inspect.isabstract(qm_LinearIncreasingFunction)


def test_qm_linearincreasingfunction_constructor_exists():
    assert callable(qm_LinearIncreasingFunction.__init__)


def test_qm_linearincreasingfunction_constructor_args():
    sig = inspect.signature(qm_LinearIncreasingFunction.__init__)
    params = list(sig.parameters.keys())



def test_qm_findingmessage_is_not_abstract():
    assert not inspect.isabstract(qm_FindingMessage)


def test_qm_findingmessage_constructor_exists():
    assert callable(qm_FindingMessage.__init__)


def test_qm_findingmessage_constructor_args():
    sig = inspect.signature(qm_FindingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "message" in params, "Missing parameter 'message'"

def test_qm_findingmessage_has_location():
    assert hasattr(qm_FindingMessage, "location")
    descriptor = None
    for klass in qm_FindingMessage.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_qm_findingmessage_has_message():
    assert hasattr(qm_FindingMessage, "message")
    descriptor = None
    for klass in qm_FindingMessage.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_qm_doubleinterval_is_not_abstract():
    assert not inspect.isabstract(qm_DoubleInterval)


def test_qm_doubleinterval_constructor_exists():
    assert callable(qm_DoubleInterval.__init__)


def test_qm_doubleinterval_constructor_args():
    sig = inspect.signature(qm_DoubleInterval.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_qm_doubleinterval_has_upper():
    assert hasattr(qm_DoubleInterval, "upper")
    descriptor = None
    for klass in qm_DoubleInterval.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_qm_doubleinterval_has_lower():
    assert hasattr(qm_DoubleInterval, "lower")
    descriptor = None
    for klass in qm_DoubleInterval.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_measurementresult_is_not_abstract():
    assert not inspect.isabstract(MeasurementResult)


def test_measurementresult_constructor_exists():
    assert callable(MeasurementResult.__init__)


def test_measurementresult_constructor_args():
    sig = inspect.signature(MeasurementResult.__init__)
    params = list(sig.parameters.keys())



def test_qm_findingsmeasurementresult_is_not_abstract():
    assert not inspect.isabstract(qm_FindingsMeasurementResult)


def test_qm_findingsmeasurementresult_constructor_exists():
    assert callable(qm_FindingsMeasurementResult.__init__)


def test_qm_findingsmeasurementresult_constructor_args():
    sig = inspect.signature(qm_FindingsMeasurementResult.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "findings" in params, "Missing parameter 'findings'"

def test_qm_findingsmeasurementresult_has_count():
    assert hasattr(qm_FindingsMeasurementResult, "count")
    descriptor = None
    for klass in qm_FindingsMeasurementResult.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_qm_findingsmeasurementresult_has_findings():
    assert hasattr(qm_FindingsMeasurementResult, "findings")
    descriptor = None
    for klass in qm_FindingsMeasurementResult.__mro__:
        if "findings" in klass.__dict__:
            descriptor = klass.__dict__["findings"]
            break
    assert isinstance(descriptor, property)



def test_qm_numbermeasurementresult_is_not_abstract():
    assert not inspect.isabstract(qm_NumberMeasurementResult)


def test_qm_numbermeasurementresult_constructor_exists():
    assert callable(qm_NumberMeasurementResult.__init__)


def test_qm_numbermeasurementresult_constructor_args():
    sig = inspect.signature(qm_NumberMeasurementResult.__init__)
    params = list(sig.parameters.keys())



def test_result_is_not_abstract():
    assert not inspect.isabstract(Result)


def test_result_constructor_exists():
    assert callable(Result.__init__)


def test_result_constructor_args():
    sig = inspect.signature(Result.__init__)
    params = list(sig.parameters.keys())



def test_qm_evaluationresult_is_not_abstract():
    assert not inspect.isabstract(qm_EvaluationResult)


def test_qm_evaluationresult_constructor_exists():
    assert callable(qm_EvaluationResult.__init__)


def test_qm_evaluationresult_constructor_args():
    sig = inspect.signature(qm_EvaluationResult.__init__)
    params = list(sig.parameters.keys())



def test_qm_measurementresult_is_not_abstract():
    assert not inspect.isabstract(qm_MeasurementResult)


def test_qm_measurementresult_constructor_exists():
    assert callable(qm_MeasurementResult.__init__)


def test_qm_measurementresult_constructor_args():
    sig = inspect.signature(qm_MeasurementResult.__init__)
    params = list(sig.parameters.keys())



def test_qm_qualitymodelresult_is_not_abstract():
    assert not inspect.isabstract(qm_QualityModelResult)


def test_qm_qualitymodelresult_constructor_exists():
    assert callable(qm_QualityModelResult.__init__)


def test_qm_qualitymodelresult_constructor_args():
    sig = inspect.signature(qm_QualityModelResult.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"
    assert "date" in params, "Missing parameter 'date'"

def test_qm_qualitymodelresult_has_system():
    assert hasattr(qm_QualityModelResult, "system")
    descriptor = None
    for klass in qm_QualityModelResult.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_qm_qualitymodelresult_has_date():
    assert hasattr(qm_QualityModelResult, "date")
    descriptor = None
    for klass in qm_QualityModelResult.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_instrument_is_not_abstract():
    assert not inspect.isabstract(Instrument)


def test_instrument_constructor_exists():
    assert callable(Instrument.__init__)


def test_instrument_constructor_args():
    sig = inspect.signature(Instrument.__init__)
    params = list(sig.parameters.keys())



def test_qm_toolbasedinstrument_is_not_abstract():
    assert not inspect.isabstract(qm_ToolBasedInstrument)


def test_qm_toolbasedinstrument_constructor_exists():
    assert callable(qm_ToolBasedInstrument.__init__)


def test_qm_toolbasedinstrument_constructor_args():
    sig = inspect.signature(qm_ToolBasedInstrument.__init__)
    params = list(sig.parameters.keys())
    assert "metric" in params, "Missing parameter 'metric'"

def test_qm_toolbasedinstrument_has_metric():
    assert hasattr(qm_ToolBasedInstrument, "metric")
    descriptor = None
    for klass in qm_ToolBasedInstrument.__mro__:
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



def test_qm_instrument_is_not_abstract():
    assert not inspect.isabstract(qm_Instrument)


def test_qm_instrument_constructor_exists():
    assert callable(qm_Instrument.__init__)


def test_qm_instrument_constructor_args():
    sig = inspect.signature(qm_Instrument.__init__)
    params = list(sig.parameters.keys())



def test_qm_function_is_not_abstract():
    assert not inspect.isabstract(qm_Function)


def test_qm_function_constructor_exists():
    assert callable(qm_Function.__init__)


def test_qm_function_constructor_args():
    sig = inspect.signature(qm_Function.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_qm_linearfunction_is_not_abstract():
    assert not inspect.isabstract(qm_LinearFunction)


def test_qm_linearfunction_constructor_exists():
    assert callable(qm_LinearFunction.__init__)


def test_qm_linearfunction_constructor_args():
    sig = inspect.signature(qm_LinearFunction.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_qm_linearfunction_has_upperBound():
    assert hasattr(qm_LinearFunction, "upperBound")
    descriptor = None
    for klass in qm_LinearFunction.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_qm_linearfunction_has_lowerBound():
    assert hasattr(qm_LinearFunction, "lowerBound")
    descriptor = None
    for klass in qm_LinearFunction.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_ranking_is_not_abstract():
    assert not inspect.isabstract(Ranking)


def test_ranking_constructor_exists():
    assert callable(Ranking.__init__)


def test_ranking_constructor_args():
    sig = inspect.signature(Ranking.__init__)
    params = list(sig.parameters.keys())



def test_qm_factorranking_is_not_abstract():
    assert not inspect.isabstract(qm_FactorRanking)


def test_qm_factorranking_constructor_exists():
    assert callable(qm_FactorRanking.__init__)


def test_qm_factorranking_constructor_args():
    sig = inspect.signature(qm_FactorRanking.__init__)
    params = list(sig.parameters.keys())



def test_measureaggregation_is_not_abstract():
    assert not inspect.isabstract(MeasureAggregation)


def test_measureaggregation_constructor_exists():
    assert callable(MeasureAggregation.__init__)


def test_measureaggregation_constructor_args():
    sig = inspect.signature(MeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm_formbasedmeasureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm_FormBasedMeasureAggregation)


def test_qm_formbasedmeasureaggregation_constructor_exists():
    assert callable(qm_FormBasedMeasureAggregation.__init__)


def test_qm_formbasedmeasureaggregation_constructor_args():
    sig = inspect.signature(qm_FormBasedMeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm_textaggregation_is_not_abstract():
    assert not inspect.isabstract(qm_TextAggregation)


def test_qm_textaggregation_constructor_exists():
    assert callable(qm_TextAggregation.__init__)


def test_qm_textaggregation_constructor_args():
    sig = inspect.signature(qm_TextAggregation.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_qm_textaggregation_has_specification():
    assert hasattr(qm_TextAggregation, "specification")
    descriptor = None
    for klass in qm_TextAggregation.__mro__:
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



def test_qm_qieslaggregation_is_not_abstract():
    assert not inspect.isabstract(qm_QIESLAggregation)


def test_qm_qieslaggregation_constructor_exists():
    assert callable(qm_QIESLAggregation.__init__)


def test_qm_qieslaggregation_constructor_args():
    sig = inspect.signature(qm_QIESLAggregation.__init__)
    params = list(sig.parameters.keys())



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_qm_normalizationmeasure_is_not_abstract():
    assert not inspect.isabstract(qm_NormalizationMeasure)


def test_qm_normalizationmeasure_constructor_exists():
    assert callable(qm_NormalizationMeasure.__init__)


def test_qm_normalizationmeasure_constructor_args():
    sig = inspect.signature(qm_NormalizationMeasure.__init__)
    params = list(sig.parameters.keys())



def test_measureevaluation_is_not_abstract():
    assert not inspect.isabstract(MeasureEvaluation)


def test_measureevaluation_constructor_exists():
    assert callable(MeasureEvaluation.__init__)


def test_measureevaluation_constructor_args():
    sig = inspect.signature(MeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_measureranking_is_not_abstract():
    assert not inspect.isabstract(qm_MeasureRanking)


def test_qm_measureranking_constructor_exists():
    assert callable(qm_MeasureRanking.__init__)


def test_qm_measureranking_constructor_args():
    sig = inspect.signature(qm_MeasureRanking.__init__)
    params = list(sig.parameters.keys())



def test_formbasedevaluation_is_not_abstract():
    assert not inspect.isabstract(FormBasedEvaluation)


def test_formbasedevaluation_constructor_exists():
    assert callable(FormBasedEvaluation.__init__)


def test_formbasedevaluation_constructor_args():
    sig = inspect.signature(FormBasedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_factoraggregation_is_not_abstract():
    assert not inspect.isabstract(qm_FactorAggregation)


def test_qm_factoraggregation_constructor_exists():
    assert callable(qm_FactorAggregation.__init__)


def test_qm_factoraggregation_constructor_args():
    sig = inspect.signature(qm_FactorAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm_multimeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_MultiMeasureEvaluation)


def test_qm_multimeasureevaluation_constructor_exists():
    assert callable(qm_MultiMeasureEvaluation.__init__)


def test_qm_multimeasureevaluation_constructor_args():
    sig = inspect.signature(qm_MultiMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_singlemeasureevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_SingleMeasureEvaluation)


def test_qm_singlemeasureevaluation_constructor_exists():
    assert callable(qm_SingleMeasureEvaluation.__init__)


def test_qm_singlemeasureevaluation_constructor_args():
    sig = inspect.signature(qm_SingleMeasureEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_is_not_abstract():
    assert not inspect.isabstract(Evaluation)


def test_evaluation_constructor_exists():
    assert callable(Evaluation.__init__)


def test_evaluation_constructor_args():
    sig = inspect.signature(Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_manualevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_ManualEvaluation)


def test_qm_manualevaluation_constructor_exists():
    assert callable(qm_ManualEvaluation.__init__)


def test_qm_manualevaluation_constructor_args():
    sig = inspect.signature(qm_ManualEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_formbasedevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_FormBasedEvaluation)


def test_qm_formbasedevaluation_constructor_exists():
    assert callable(qm_FormBasedEvaluation.__init__)


def test_qm_formbasedevaluation_constructor_args():
    sig = inspect.signature(qm_FormBasedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_qm_textevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_TextEvaluation)


def test_qm_textevaluation_constructor_exists():
    assert callable(qm_TextEvaluation.__init__)


def test_qm_textevaluation_constructor_args():
    sig = inspect.signature(qm_TextEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_qm_textevaluation_has_specification():
    assert hasattr(qm_TextEvaluation, "specification")
    descriptor = None
    for klass in qm_TextEvaluation.__mro__:
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



def test_qm_qieslevaluation_is_not_abstract():
    assert not inspect.isabstract(qm_QIESLEvaluation)


def test_qm_qieslevaluation_constructor_exists():
    assert callable(qm_QIESLEvaluation.__init__)


def test_qm_qieslevaluation_constructor_args():
    sig = inspect.signature(qm_QIESLEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_characterizingelement_is_not_abstract():
    assert not inspect.isabstract(CharacterizingElement)


def test_characterizingelement_constructor_exists():
    assert callable(CharacterizingElement.__init__)


def test_characterizingelement_constructor_args():
    sig = inspect.signature(CharacterizingElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_annotation_is_not_abstract():
    assert not inspect.isabstract(qm_Annotation)


def test_qm_annotation_constructor_exists():
    assert callable(qm_Annotation.__init__)


def test_qm_annotation_constructor_args():
    sig = inspect.signature(qm_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_qm_annotation_has_value():
    assert hasattr(qm_Annotation, "value")
    descriptor = None
    for klass in qm_Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_qm_annotation_has_key():
    assert hasattr(qm_Annotation, "key")
    descriptor = None
    for klass in qm_Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_taggedelement_is_not_abstract():
    assert not inspect.isabstract(TaggedElement)


def test_taggedelement_constructor_exists():
    assert callable(TaggedElement.__init__)


def test_taggedelement_constructor_args():
    sig = inspect.signature(TaggedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(qm_AnnotatedElement)


def test_qm_annotatedelement_constructor_exists():
    assert callable(qm_AnnotatedElement.__init__)


def test_qm_annotatedelement_constructor_args():
    sig = inspect.signature(qm_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_describedelement_is_not_abstract():
    assert not inspect.isabstract(DescribedElement)


def test_describedelement_constructor_exists():
    assert callable(DescribedElement.__init__)


def test_describedelement_constructor_args():
    sig = inspect.signature(DescribedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_namedelement_is_not_abstract():
    assert not inspect.isabstract(qm_NamedElement)


def test_qm_namedelement_constructor_exists():
    assert callable(qm_NamedElement.__init__)


def test_qm_namedelement_constructor_args():
    sig = inspect.signature(qm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "title" in params, "Missing parameter 'title'"

def test_qm_namedelement_has_name():
    assert hasattr(qm_NamedElement, "name")
    descriptor = None
    for klass in qm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qm_namedelement_has_title():
    assert hasattr(qm_NamedElement, "title")
    descriptor = None
    for klass in qm_NamedElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_decomposition_is_not_abstract():
    assert not inspect.isabstract(qm_Decomposition)


def test_qm_decomposition_constructor_exists():
    assert callable(qm_Decomposition.__init__)


def test_qm_decomposition_constructor_args():
    sig = inspect.signature(qm_Decomposition.__init__)
    params = list(sig.parameters.keys())



def test_qm_impact_is_not_abstract():
    assert not inspect.isabstract(qm_Impact)


def test_qm_impact_constructor_exists():
    assert callable(qm_Impact.__init__)


def test_qm_impact_constructor_args():
    sig = inspect.signature(qm_Impact.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "justification" in params, "Missing parameter 'justification'"

def test_qm_impact_has_effect():
    assert hasattr(qm_Impact, "effect")
    descriptor = None
    for klass in qm_Impact.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_qm_impact_has_justification():
    assert hasattr(qm_Impact, "justification")
    descriptor = None
    for klass in qm_Impact.__mro__:
        if "justification" in klass.__dict__:
            descriptor = klass.__dict__["justification"]
            break
    assert isinstance(descriptor, property)



def test_qm_measurerefinement_is_not_abstract():
    assert not inspect.isabstract(qm_MeasureRefinement)


def test_qm_measurerefinement_constructor_exists():
    assert callable(qm_MeasureRefinement.__init__)


def test_qm_measurerefinement_constructor_args():
    sig = inspect.signature(qm_MeasureRefinement.__init__)
    params = list(sig.parameters.keys())



def test_qm_factorrefinement_is_not_abstract():
    assert not inspect.isabstract(qm_FactorRefinement)


def test_qm_factorrefinement_constructor_exists():
    assert callable(qm_FactorRefinement.__init__)


def test_qm_factorrefinement_constructor_args():
    sig = inspect.signature(qm_FactorRefinement.__init__)
    params = list(sig.parameters.keys())



def test_qm_measurement_is_not_abstract():
    assert not inspect.isabstract(qm_Measurement)


def test_qm_measurement_constructor_exists():
    assert callable(qm_Measurement.__init__)


def test_qm_measurement_constructor_args():
    sig = inspect.signature(qm_Measurement.__init__)
    params = list(sig.parameters.keys())



def test_qm_describedelement_is_not_abstract():
    assert not inspect.isabstract(qm_DescribedElement)


def test_qm_describedelement_constructor_exists():
    assert callable(qm_DescribedElement.__init__)


def test_qm_describedelement_constructor_args():
    sig = inspect.signature(qm_DescribedElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_qm_describedelement_has_description():
    assert hasattr(qm_DescribedElement, "description")
    descriptor = None
    for klass in qm_DescribedElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_qm_qualitymodelelement_is_not_abstract():
    assert not inspect.isabstract(qm_QualityModelElement)


def test_qm_qualitymodelelement_constructor_exists():
    assert callable(qm_QualityModelElement.__init__)


def test_qm_qualitymodelelement_constructor_args():
    sig = inspect.signature(qm_QualityModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_qm_qualitymodelelement_has_qualifiedName():
    assert hasattr(qm_QualityModelElement, "qualifiedName")
    descriptor = None
    for klass in qm_QualityModelElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_qm_specialization_is_not_abstract():
    assert not inspect.isabstract(qm_Specialization)


def test_qm_specialization_constructor_exists():
    assert callable(qm_Specialization.__init__)


def test_qm_specialization_constructor_args():
    sig = inspect.signature(qm_Specialization.__init__)
    params = list(sig.parameters.keys())



def test_qualitymodelelement_is_not_abstract():
    assert not inspect.isabstract(QualityModelElement)


def test_qualitymodelelement_constructor_exists():
    assert callable(QualityModelElement.__init__)


def test_qualitymodelelement_constructor_args():
    sig = inspect.signature(QualityModelElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_taggedelement_is_not_abstract():
    assert not inspect.isabstract(qm_TaggedElement)


def test_qm_taggedelement_constructor_exists():
    assert callable(qm_TaggedElement.__init__)


def test_qm_taggedelement_constructor_args():
    sig = inspect.signature(qm_TaggedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_annotationbase_is_not_abstract():
    assert not inspect.isabstract(qm_AnnotationBase)


def test_qm_annotationbase_constructor_exists():
    assert callable(qm_AnnotationBase.__init__)


def test_qm_annotationbase_constructor_args():
    sig = inspect.signature(qm_AnnotationBase.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_characterizingelement_is_not_abstract():
    assert not inspect.isabstract(qm_CharacterizingElement)


def test_qm_characterizingelement_constructor_exists():
    assert callable(qm_CharacterizingElement.__init__)


def test_qm_characterizingelement_constructor_args():
    sig = inspect.signature(qm_CharacterizingElement.__init__)
    params = list(sig.parameters.keys())



def test_qm_manualinstrument_is_not_abstract():
    assert not inspect.isabstract(qm_ManualInstrument)


def test_qm_manualinstrument_constructor_exists():
    assert callable(qm_ManualInstrument.__init__)


def test_qm_manualinstrument_constructor_args():
    sig = inspect.signature(qm_ManualInstrument.__init__)
    params = list(sig.parameters.keys())



def test_qm_entity_is_not_abstract():
    assert not inspect.isabstract(qm_Entity)


def test_qm_entity_constructor_exists():
    assert callable(qm_Entity.__init__)


def test_qm_entity_constructor_args():
    sig = inspect.signature(qm_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "useCase" in params, "Missing parameter 'useCase'"
    assert "stakeholder" in params, "Missing parameter 'stakeholder'"

def test_qm_entity_has_useCase():
    assert hasattr(qm_Entity, "useCase")
    descriptor = None
    for klass in qm_Entity.__mro__:
        if "useCase" in klass.__dict__:
            descriptor = klass.__dict__["useCase"]
            break
    assert isinstance(descriptor, property)

def test_qm_entity_has_stakeholder():
    assert hasattr(qm_Entity, "stakeholder")
    descriptor = None
    for klass in qm_Entity.__mro__:
        if "stakeholder" in klass.__dict__:
            descriptor = klass.__dict__["stakeholder"]
            break
    assert isinstance(descriptor, property)



def test_qm_measureaggregation_is_not_abstract():
    assert not inspect.isabstract(qm_MeasureAggregation)


def test_qm_measureaggregation_constructor_exists():
    assert callable(qm_MeasureAggregation.__init__)


def test_qm_measureaggregation_constructor_args():
    sig = inspect.signature(qm_MeasureAggregation.__init__)
    params = list(sig.parameters.keys())



def test_qm_qualitymodel_is_not_abstract():
    assert not inspect.isabstract(qm_QualityModel)


def test_qm_qualitymodel_constructor_exists():
    assert callable(qm_QualityModel.__init__)


def test_qm_qualitymodel_constructor_args():
    sig = inspect.signature(qm_QualityModel.__init__)
    params = list(sig.parameters.keys())
    assert "schoolGradeBoundary6" in params, "Missing parameter 'schoolGradeBoundary6'"
    assert "schoolGradeBoundary4" in params, "Missing parameter 'schoolGradeBoundary4'"
    assert "schoolGradeBoundary5" in params, "Missing parameter 'schoolGradeBoundary5'"
    assert "schoolGradeBoundary2" in params, "Missing parameter 'schoolGradeBoundary2'"
    assert "schoolGradeBoundary3" in params, "Missing parameter 'schoolGradeBoundary3'"

def test_qm_qualitymodel_has_schoolGradeBoundary6():
    assert hasattr(qm_QualityModel, "schoolGradeBoundary6")
    descriptor = None
    for klass in qm_QualityModel.__mro__:
        if "schoolGradeBoundary6" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary6"]
            break
    assert isinstance(descriptor, property)

def test_qm_qualitymodel_has_schoolGradeBoundary4():
    assert hasattr(qm_QualityModel, "schoolGradeBoundary4")
    descriptor = None
    for klass in qm_QualityModel.__mro__:
        if "schoolGradeBoundary4" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary4"]
            break
    assert isinstance(descriptor, property)

def test_qm_qualitymodel_has_schoolGradeBoundary5():
    assert hasattr(qm_QualityModel, "schoolGradeBoundary5")
    descriptor = None
    for klass in qm_QualityModel.__mro__:
        if "schoolGradeBoundary5" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary5"]
            break
    assert isinstance(descriptor, property)

def test_qm_qualitymodel_has_schoolGradeBoundary2():
    assert hasattr(qm_QualityModel, "schoolGradeBoundary2")
    descriptor = None
    for klass in qm_QualityModel.__mro__:
        if "schoolGradeBoundary2" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary2"]
            break
    assert isinstance(descriptor, property)

def test_qm_qualitymodel_has_schoolGradeBoundary3():
    assert hasattr(qm_QualityModel, "schoolGradeBoundary3")
    descriptor = None
    for klass in qm_QualityModel.__mro__:
        if "schoolGradeBoundary3" in klass.__dict__:
            descriptor = klass.__dict__["schoolGradeBoundary3"]
            break
    assert isinstance(descriptor, property)



def test_qm_source_is_not_abstract():
    assert not inspect.isabstract(qm_Source)


def test_qm_source_constructor_exists():
    assert callable(qm_Source.__init__)


def test_qm_source_constructor_args():
    sig = inspect.signature(qm_Source.__init__)
    params = list(sig.parameters.keys())



def test_qm_tag_is_not_abstract():
    assert not inspect.isabstract(qm_Tag)


def test_qm_tag_constructor_exists():
    assert callable(qm_Tag.__init__)


def test_qm_tag_constructor_args():
    sig = inspect.signature(qm_Tag.__init__)
    params = list(sig.parameters.keys())



def test_qm_tool_is_not_abstract():
    assert not inspect.isabstract(qm_Tool)


def test_qm_tool_constructor_exists():
    assert callable(qm_Tool.__init__)


def test_qm_tool_constructor_args():
    sig = inspect.signature(qm_Tool.__init__)
    params = list(sig.parameters.keys())



def test_qm_measurementmethod_is_not_abstract():
    assert not inspect.isabstract(qm_MeasurementMethod)


def test_qm_measurementmethod_constructor_exists():
    assert callable(qm_MeasurementMethod.__init__)


def test_qm_measurementmethod_constructor_args():
    sig = inspect.signature(qm_MeasurementMethod.__init__)
    params = list(sig.parameters.keys())



def test_qm_measure_is_not_abstract():
    assert not inspect.isabstract(qm_Measure)


def test_qm_measure_constructor_exists():
    assert callable(qm_Measure.__init__)


def test_qm_measure_constructor_args():
    sig = inspect.signature(qm_Measure.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_qm_measure_has_type():
    assert hasattr(qm_Measure, "type")
    descriptor = None
    for klass in qm_Measure.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_qm_evaluation_is_not_abstract():
    assert not inspect.isabstract(qm_Evaluation)


def test_qm_evaluation_constructor_exists():
    assert callable(qm_Evaluation.__init__)


def test_qm_evaluation_constructor_args():
    sig = inspect.signature(qm_Evaluation.__init__)
    params = list(sig.parameters.keys())
    assert "maximumPoints" in params, "Missing parameter 'maximumPoints'"
    assert "completeness" in params, "Missing parameter 'completeness'"

def test_qm_evaluation_has_maximumPoints():
    assert hasattr(qm_Evaluation, "maximumPoints")
    descriptor = None
    for klass in qm_Evaluation.__mro__:
        if "maximumPoints" in klass.__dict__:
            descriptor = klass.__dict__["maximumPoints"]
            break
    assert isinstance(descriptor, property)

def test_qm_evaluation_has_completeness():
    assert hasattr(qm_Evaluation, "completeness")
    descriptor = None
    for klass in qm_Evaluation.__mro__:
        if "completeness" in klass.__dict__:
            descriptor = klass.__dict__["completeness"]
            break
    assert isinstance(descriptor, property)



def test_qm_factor_is_not_abstract():
    assert not inspect.isabstract(qm_Factor)


def test_qm_factor_constructor_exists():
    assert callable(qm_Factor.__init__)


def test_qm_factor_constructor_args():
    sig = inspect.signature(qm_Factor.__init__)
    params = list(sig.parameters.keys())

def test_effect_exists():
    # Check that the Enumeration exists
    assert Effect is not None

def test_effect_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Effect]
    expected_literals = [
        "POSITIVE",
        "NEGATIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Effect"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "FINDINGS",
        "NONE",
        "NUMBER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
qm_Result_strategy = st.builds(
    qm_Result,
    message=
        safe_text
)
qm_MeasureRankingEvaluationResult_strategy = st.builds(
    qm_MeasureRankingEvaluationResult,
    ratioAffected=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
EvaluationResult_strategy = st.builds(
    EvaluationResult,
)
qm_MultiMeasureEvaluationResult_strategy = st.builds(
    qm_MultiMeasureEvaluationResult,
)
qm_SingleMeasureEvaluationResult_strategy = st.builds(
    qm_SingleMeasureEvaluationResult,
    ratioAffected=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MultiMeasureEvaluation_strategy = st.builds(
    MultiMeasureEvaluation,
)
qm_WeightedSumMultiMeasureEvaluation_strategy = st.builds(
    qm_WeightedSumMultiMeasureEvaluation,
)
qm_Ranking_strategy = st.builds(
    qm_Ranking,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rank=
        st.integers()
)
qm_MeasureEvaluation_strategy = st.builds(
    qm_MeasureEvaluation,
    range=
        safe_text
)
FormBasedMeasureAggregation_strategy = st.builds(
    FormBasedMeasureAggregation,
)
qm_NumberMeanMeasureAggregation_strategy = st.builds(
    qm_NumberMeanMeasureAggregation,
)
qm_FindingsUnionMeasureAggregation_strategy = st.builds(
    qm_FindingsUnionMeasureAggregation,
)
FactorAggregation_strategy = st.builds(
    FactorAggregation,
)
qm_WeightedSumFactorAggregation_strategy = st.builds(
    qm_WeightedSumFactorAggregation,
)
LinearFunction_strategy = st.builds(
    LinearFunction,
)
qm_LinearDecreasingFunction_strategy = st.builds(
    qm_LinearDecreasingFunction,
)
qm_LinearIncreasingFunction_strategy = st.builds(
    qm_LinearIncreasingFunction,
)
qm_FindingMessage_strategy = st.builds(
    qm_FindingMessage,
    location=
        safe_text,
    message=
        safe_text
)
qm_DoubleInterval_strategy = st.builds(
    qm_DoubleInterval,
    upper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MeasurementResult_strategy = st.builds(
    MeasurementResult,
)
qm_FindingsMeasurementResult_strategy = st.builds(
    qm_FindingsMeasurementResult,
    count=
        st.integers(),
    findings=
        safe_text
)
qm_NumberMeasurementResult_strategy = st.builds(
    qm_NumberMeasurementResult,
)
Result_strategy = st.builds(
    Result,
)
qm_EvaluationResult_strategy = st.builds(
    qm_EvaluationResult,
)
qm_MeasurementResult_strategy = st.builds(
    qm_MeasurementResult,
)
qm_QualityModelResult_strategy = st.builds(
    qm_QualityModelResult,
    system=
        safe_text,
    date=
        st.dates()
)
Instrument_strategy = st.builds(
    Instrument,
)
qm_ToolBasedInstrument_strategy = st.builds(
    qm_ToolBasedInstrument,
    metric=
        safe_text
)
MeasurementMethod_strategy = st.builds(
    MeasurementMethod,
)
qm_Instrument_strategy = st.builds(
    qm_Instrument,
)
qm_Function_strategy = st.builds(
    qm_Function,
)
Function_strategy = st.builds(
    Function,
)
qm_LinearFunction_strategy = st.builds(
    qm_LinearFunction,
    upperBound=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lowerBound=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Ranking_strategy = st.builds(
    Ranking,
)
qm_FactorRanking_strategy = st.builds(
    qm_FactorRanking,
)
MeasureAggregation_strategy = st.builds(
    MeasureAggregation,
)
qm_FormBasedMeasureAggregation_strategy = st.builds(
    qm_FormBasedMeasureAggregation,
)
qm_TextAggregation_strategy = st.builds(
    qm_TextAggregation,
    specification=
        safe_text
)
TextAggregation_strategy = st.builds(
    TextAggregation,
)
qm_QIESLAggregation_strategy = st.builds(
    qm_QIESLAggregation,
)
Measure_strategy = st.builds(
    Measure,
)
qm_NormalizationMeasure_strategy = st.builds(
    qm_NormalizationMeasure,
)
MeasureEvaluation_strategy = st.builds(
    MeasureEvaluation,
)
qm_MeasureRanking_strategy = st.builds(
    qm_MeasureRanking,
)
FormBasedEvaluation_strategy = st.builds(
    FormBasedEvaluation,
)
qm_FactorAggregation_strategy = st.builds(
    qm_FactorAggregation,
)
qm_MultiMeasureEvaluation_strategy = st.builds(
    qm_MultiMeasureEvaluation,
)
qm_SingleMeasureEvaluation_strategy = st.builds(
    qm_SingleMeasureEvaluation,
)
Evaluation_strategy = st.builds(
    Evaluation,
)
qm_ManualEvaluation_strategy = st.builds(
    qm_ManualEvaluation,
)
qm_FormBasedEvaluation_strategy = st.builds(
    qm_FormBasedEvaluation,
)
qm_TextEvaluation_strategy = st.builds(
    qm_TextEvaluation,
    specification=
        safe_text
)
TextEvaluation_strategy = st.builds(
    TextEvaluation,
)
qm_QIESLEvaluation_strategy = st.builds(
    qm_QIESLEvaluation,
)
CharacterizingElement_strategy = st.builds(
    CharacterizingElement,
)
qm_Annotation_strategy = st.builds(
    qm_Annotation,
    value=
        safe_text,
    key=
        safe_text
)
TaggedElement_strategy = st.builds(
    TaggedElement,
)
qm_AnnotatedElement_strategy = st.builds(
    qm_AnnotatedElement,
)
DescribedElement_strategy = st.builds(
    DescribedElement,
)
qm_NamedElement_strategy = st.builds(
    qm_NamedElement,
    name=
        safe_text,
    title=
        safe_text
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
qm_Decomposition_strategy = st.builds(
    qm_Decomposition,
)
qm_Impact_strategy = st.builds(
    qm_Impact,
    effect=
        safe_text,
    justification=
        safe_text
)
qm_MeasureRefinement_strategy = st.builds(
    qm_MeasureRefinement,
)
qm_FactorRefinement_strategy = st.builds(
    qm_FactorRefinement,
)
qm_Measurement_strategy = st.builds(
    qm_Measurement,
)
qm_DescribedElement_strategy = st.builds(
    qm_DescribedElement,
    description=
        safe_text
)
qm_QualityModelElement_strategy = st.builds(
    qm_QualityModelElement,
    qualifiedName=
        safe_text
)
qm_Specialization_strategy = st.builds(
    qm_Specialization,
)
QualityModelElement_strategy = st.builds(
    QualityModelElement,
)
qm_TaggedElement_strategy = st.builds(
    qm_TaggedElement,
)
qm_AnnotationBase_strategy = st.builds(
    qm_AnnotationBase,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
qm_CharacterizingElement_strategy = st.builds(
    qm_CharacterizingElement,
)
qm_ManualInstrument_strategy = st.builds(
    qm_ManualInstrument,
)
qm_Entity_strategy = st.builds(
    qm_Entity,
    useCase=
        st.booleans(),
    stakeholder=
        st.booleans()
)
qm_MeasureAggregation_strategy = st.builds(
    qm_MeasureAggregation,
)
qm_QualityModel_strategy = st.builds(
    qm_QualityModel,
    schoolGradeBoundary6=
        safe_text,
    schoolGradeBoundary4=
        safe_text,
    schoolGradeBoundary5=
        safe_text,
    schoolGradeBoundary2=
        safe_text,
    schoolGradeBoundary3=
        safe_text
)
qm_Source_strategy = st.builds(
    qm_Source,
)
qm_Tag_strategy = st.builds(
    qm_Tag,
)
qm_Tool_strategy = st.builds(
    qm_Tool,
)
qm_MeasurementMethod_strategy = st.builds(
    qm_MeasurementMethod,
)
qm_Measure_strategy = st.builds(
    qm_Measure,
    type=
        safe_text
)
qm_Evaluation_strategy = st.builds(
    qm_Evaluation,
    maximumPoints=
        st.integers(),
    completeness=
        st.integers()
)
qm_Factor_strategy = st.builds(
    qm_Factor,
)

@given(instance=qm_Result_strategy)
@settings(max_examples=50)
def test_qm_result_instantiation(instance):
    assert isinstance(instance, qm_Result)



@given(instance=qm_Result_strategy)
def test_qm_result_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=qm_MeasureRankingEvaluationResult_strategy)
@settings(max_examples=50)
def test_qm_measurerankingevaluationresult_instantiation(instance):
    assert isinstance(instance, qm_MeasureRankingEvaluationResult)



@given(instance=qm_MeasureRankingEvaluationResult_strategy)
def test_qm_measurerankingevaluationresult_ratioAffected_setter(instance):
    original = instance.ratioAffected
    instance.ratioAffected = original
    assert instance.ratioAffected == original

@given(instance=EvaluationResult_strategy)
@settings(max_examples=50)
def test_evaluationresult_instantiation(instance):
    assert isinstance(instance, EvaluationResult)

@given(instance=qm_MultiMeasureEvaluationResult_strategy)
@settings(max_examples=50)
def test_qm_multimeasureevaluationresult_instantiation(instance):
    assert isinstance(instance, qm_MultiMeasureEvaluationResult)

@given(instance=qm_SingleMeasureEvaluationResult_strategy)
@settings(max_examples=50)
def test_qm_singlemeasureevaluationresult_instantiation(instance):
    assert isinstance(instance, qm_SingleMeasureEvaluationResult)



@given(instance=qm_SingleMeasureEvaluationResult_strategy)
def test_qm_singlemeasureevaluationresult_ratioAffected_setter(instance):
    original = instance.ratioAffected
    instance.ratioAffected = original
    assert instance.ratioAffected == original

@given(instance=MultiMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_multimeasureevaluation_instantiation(instance):
    assert isinstance(instance, MultiMeasureEvaluation)

@given(instance=qm_WeightedSumMultiMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm_weightedsummultimeasureevaluation_instantiation(instance):
    assert isinstance(instance, qm_WeightedSumMultiMeasureEvaluation)

@given(instance=qm_Ranking_strategy)
@settings(max_examples=50)
def test_qm_ranking_instantiation(instance):
    assert isinstance(instance, qm_Ranking)



@given(instance=qm_Ranking_strategy)
def test_qm_ranking_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=qm_Ranking_strategy)
def test_qm_ranking_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=qm_MeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm_measureevaluation_instantiation(instance):
    assert isinstance(instance, qm_MeasureEvaluation)



@given(instance=qm_MeasureEvaluation_strategy)
def test_qm_measureevaluation_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=FormBasedMeasureAggregation_strategy)
@settings(max_examples=50)
def test_formbasedmeasureaggregation_instantiation(instance):
    assert isinstance(instance, FormBasedMeasureAggregation)

@given(instance=qm_NumberMeanMeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm_numbermeanmeasureaggregation_instantiation(instance):
    assert isinstance(instance, qm_NumberMeanMeasureAggregation)

@given(instance=qm_FindingsUnionMeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm_findingsunionmeasureaggregation_instantiation(instance):
    assert isinstance(instance, qm_FindingsUnionMeasureAggregation)

@given(instance=FactorAggregation_strategy)
@settings(max_examples=50)
def test_factoraggregation_instantiation(instance):
    assert isinstance(instance, FactorAggregation)

@given(instance=qm_WeightedSumFactorAggregation_strategy)
@settings(max_examples=50)
def test_qm_weightedsumfactoraggregation_instantiation(instance):
    assert isinstance(instance, qm_WeightedSumFactorAggregation)

@given(instance=LinearFunction_strategy)
@settings(max_examples=50)
def test_linearfunction_instantiation(instance):
    assert isinstance(instance, LinearFunction)

@given(instance=qm_LinearDecreasingFunction_strategy)
@settings(max_examples=50)
def test_qm_lineardecreasingfunction_instantiation(instance):
    assert isinstance(instance, qm_LinearDecreasingFunction)

@given(instance=qm_LinearIncreasingFunction_strategy)
@settings(max_examples=50)
def test_qm_linearincreasingfunction_instantiation(instance):
    assert isinstance(instance, qm_LinearIncreasingFunction)

@given(instance=qm_FindingMessage_strategy)
@settings(max_examples=50)
def test_qm_findingmessage_instantiation(instance):
    assert isinstance(instance, qm_FindingMessage)



@given(instance=qm_FindingMessage_strategy)
def test_qm_findingmessage_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=qm_FindingMessage_strategy)
def test_qm_findingmessage_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=qm_DoubleInterval_strategy)
@settings(max_examples=50)
def test_qm_doubleinterval_instantiation(instance):
    assert isinstance(instance, qm_DoubleInterval)



@given(instance=qm_DoubleInterval_strategy)
def test_qm_doubleinterval_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=qm_DoubleInterval_strategy)
def test_qm_doubleinterval_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=MeasurementResult_strategy)
@settings(max_examples=50)
def test_measurementresult_instantiation(instance):
    assert isinstance(instance, MeasurementResult)

@given(instance=qm_FindingsMeasurementResult_strategy)
@settings(max_examples=50)
def test_qm_findingsmeasurementresult_instantiation(instance):
    assert isinstance(instance, qm_FindingsMeasurementResult)



@given(instance=qm_FindingsMeasurementResult_strategy)
def test_qm_findingsmeasurementresult_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=qm_FindingsMeasurementResult_strategy)
def test_qm_findingsmeasurementresult_findings_setter(instance):
    original = instance.findings
    instance.findings = original
    assert instance.findings == original

@given(instance=qm_NumberMeasurementResult_strategy)
@settings(max_examples=50)
def test_qm_numbermeasurementresult_instantiation(instance):
    assert isinstance(instance, qm_NumberMeasurementResult)

@given(instance=Result_strategy)
@settings(max_examples=50)
def test_result_instantiation(instance):
    assert isinstance(instance, Result)

@given(instance=qm_EvaluationResult_strategy)
@settings(max_examples=50)
def test_qm_evaluationresult_instantiation(instance):
    assert isinstance(instance, qm_EvaluationResult)

@given(instance=qm_MeasurementResult_strategy)
@settings(max_examples=50)
def test_qm_measurementresult_instantiation(instance):
    assert isinstance(instance, qm_MeasurementResult)

@given(instance=qm_QualityModelResult_strategy)
@settings(max_examples=50)
def test_qm_qualitymodelresult_instantiation(instance):
    assert isinstance(instance, qm_QualityModelResult)



@given(instance=qm_QualityModelResult_strategy)
def test_qm_qualitymodelresult_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=qm_QualityModelResult_strategy)
def test_qm_qualitymodelresult_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Instrument_strategy)
@settings(max_examples=50)
def test_instrument_instantiation(instance):
    assert isinstance(instance, Instrument)

@given(instance=qm_ToolBasedInstrument_strategy)
@settings(max_examples=50)
def test_qm_toolbasedinstrument_instantiation(instance):
    assert isinstance(instance, qm_ToolBasedInstrument)



@given(instance=qm_ToolBasedInstrument_strategy)
def test_qm_toolbasedinstrument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original

@given(instance=MeasurementMethod_strategy)
@settings(max_examples=50)
def test_measurementmethod_instantiation(instance):
    assert isinstance(instance, MeasurementMethod)

@given(instance=qm_Instrument_strategy)
@settings(max_examples=50)
def test_qm_instrument_instantiation(instance):
    assert isinstance(instance, qm_Instrument)

@given(instance=qm_Function_strategy)
@settings(max_examples=50)
def test_qm_function_instantiation(instance):
    assert isinstance(instance, qm_Function)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=qm_LinearFunction_strategy)
@settings(max_examples=50)
def test_qm_linearfunction_instantiation(instance):
    assert isinstance(instance, qm_LinearFunction)



@given(instance=qm_LinearFunction_strategy)
def test_qm_linearfunction_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=qm_LinearFunction_strategy)
def test_qm_linearfunction_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=Ranking_strategy)
@settings(max_examples=50)
def test_ranking_instantiation(instance):
    assert isinstance(instance, Ranking)

@given(instance=qm_FactorRanking_strategy)
@settings(max_examples=50)
def test_qm_factorranking_instantiation(instance):
    assert isinstance(instance, qm_FactorRanking)

@given(instance=MeasureAggregation_strategy)
@settings(max_examples=50)
def test_measureaggregation_instantiation(instance):
    assert isinstance(instance, MeasureAggregation)

@given(instance=qm_FormBasedMeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm_formbasedmeasureaggregation_instantiation(instance):
    assert isinstance(instance, qm_FormBasedMeasureAggregation)

@given(instance=qm_TextAggregation_strategy)
@settings(max_examples=50)
def test_qm_textaggregation_instantiation(instance):
    assert isinstance(instance, qm_TextAggregation)



@given(instance=qm_TextAggregation_strategy)
def test_qm_textaggregation_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=TextAggregation_strategy)
@settings(max_examples=50)
def test_textaggregation_instantiation(instance):
    assert isinstance(instance, TextAggregation)

@given(instance=qm_QIESLAggregation_strategy)
@settings(max_examples=50)
def test_qm_qieslaggregation_instantiation(instance):
    assert isinstance(instance, qm_QIESLAggregation)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=qm_NormalizationMeasure_strategy)
@settings(max_examples=50)
def test_qm_normalizationmeasure_instantiation(instance):
    assert isinstance(instance, qm_NormalizationMeasure)

@given(instance=MeasureEvaluation_strategy)
@settings(max_examples=50)
def test_measureevaluation_instantiation(instance):
    assert isinstance(instance, MeasureEvaluation)

@given(instance=qm_MeasureRanking_strategy)
@settings(max_examples=50)
def test_qm_measureranking_instantiation(instance):
    assert isinstance(instance, qm_MeasureRanking)

@given(instance=FormBasedEvaluation_strategy)
@settings(max_examples=50)
def test_formbasedevaluation_instantiation(instance):
    assert isinstance(instance, FormBasedEvaluation)

@given(instance=qm_FactorAggregation_strategy)
@settings(max_examples=50)
def test_qm_factoraggregation_instantiation(instance):
    assert isinstance(instance, qm_FactorAggregation)

@given(instance=qm_MultiMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm_multimeasureevaluation_instantiation(instance):
    assert isinstance(instance, qm_MultiMeasureEvaluation)

@given(instance=qm_SingleMeasureEvaluation_strategy)
@settings(max_examples=50)
def test_qm_singlemeasureevaluation_instantiation(instance):
    assert isinstance(instance, qm_SingleMeasureEvaluation)

@given(instance=Evaluation_strategy)
@settings(max_examples=50)
def test_evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)

@given(instance=qm_ManualEvaluation_strategy)
@settings(max_examples=50)
def test_qm_manualevaluation_instantiation(instance):
    assert isinstance(instance, qm_ManualEvaluation)

@given(instance=qm_FormBasedEvaluation_strategy)
@settings(max_examples=50)
def test_qm_formbasedevaluation_instantiation(instance):
    assert isinstance(instance, qm_FormBasedEvaluation)

@given(instance=qm_TextEvaluation_strategy)
@settings(max_examples=50)
def test_qm_textevaluation_instantiation(instance):
    assert isinstance(instance, qm_TextEvaluation)



@given(instance=qm_TextEvaluation_strategy)
def test_qm_textevaluation_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=TextEvaluation_strategy)
@settings(max_examples=50)
def test_textevaluation_instantiation(instance):
    assert isinstance(instance, TextEvaluation)

@given(instance=qm_QIESLEvaluation_strategy)
@settings(max_examples=50)
def test_qm_qieslevaluation_instantiation(instance):
    assert isinstance(instance, qm_QIESLEvaluation)

@given(instance=CharacterizingElement_strategy)
@settings(max_examples=50)
def test_characterizingelement_instantiation(instance):
    assert isinstance(instance, CharacterizingElement)

@given(instance=qm_Annotation_strategy)
@settings(max_examples=50)
def test_qm_annotation_instantiation(instance):
    assert isinstance(instance, qm_Annotation)



@given(instance=qm_Annotation_strategy)
def test_qm_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=qm_Annotation_strategy)
def test_qm_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=TaggedElement_strategy)
@settings(max_examples=50)
def test_taggedelement_instantiation(instance):
    assert isinstance(instance, TaggedElement)

@given(instance=qm_AnnotatedElement_strategy)
@settings(max_examples=50)
def test_qm_annotatedelement_instantiation(instance):
    assert isinstance(instance, qm_AnnotatedElement)

@given(instance=DescribedElement_strategy)
@settings(max_examples=50)
def test_describedelement_instantiation(instance):
    assert isinstance(instance, DescribedElement)

@given(instance=qm_NamedElement_strategy)
@settings(max_examples=50)
def test_qm_namedelement_instantiation(instance):
    assert isinstance(instance, qm_NamedElement)



@given(instance=qm_NamedElement_strategy)
def test_qm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=qm_NamedElement_strategy)
def test_qm_namedelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=qm_Decomposition_strategy)
@settings(max_examples=50)
def test_qm_decomposition_instantiation(instance):
    assert isinstance(instance, qm_Decomposition)

@given(instance=qm_Impact_strategy)
@settings(max_examples=50)
def test_qm_impact_instantiation(instance):
    assert isinstance(instance, qm_Impact)



@given(instance=qm_Impact_strategy)
def test_qm_impact_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=qm_Impact_strategy)
def test_qm_impact_justification_setter(instance):
    original = instance.justification
    instance.justification = original
    assert instance.justification == original

@given(instance=qm_MeasureRefinement_strategy)
@settings(max_examples=50)
def test_qm_measurerefinement_instantiation(instance):
    assert isinstance(instance, qm_MeasureRefinement)

@given(instance=qm_FactorRefinement_strategy)
@settings(max_examples=50)
def test_qm_factorrefinement_instantiation(instance):
    assert isinstance(instance, qm_FactorRefinement)

@given(instance=qm_Measurement_strategy)
@settings(max_examples=50)
def test_qm_measurement_instantiation(instance):
    assert isinstance(instance, qm_Measurement)

@given(instance=qm_DescribedElement_strategy)
@settings(max_examples=50)
def test_qm_describedelement_instantiation(instance):
    assert isinstance(instance, qm_DescribedElement)



@given(instance=qm_DescribedElement_strategy)
def test_qm_describedelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=qm_QualityModelElement_strategy)
@settings(max_examples=50)
def test_qm_qualitymodelelement_instantiation(instance):
    assert isinstance(instance, qm_QualityModelElement)



@given(instance=qm_QualityModelElement_strategy)
def test_qm_qualitymodelelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=qm_Specialization_strategy)
@settings(max_examples=50)
def test_qm_specialization_instantiation(instance):
    assert isinstance(instance, qm_Specialization)

@given(instance=QualityModelElement_strategy)
@settings(max_examples=50)
def test_qualitymodelelement_instantiation(instance):
    assert isinstance(instance, QualityModelElement)

@given(instance=qm_TaggedElement_strategy)
@settings(max_examples=50)
def test_qm_taggedelement_instantiation(instance):
    assert isinstance(instance, qm_TaggedElement)

@given(instance=qm_AnnotationBase_strategy)
@settings(max_examples=50)
def test_qm_annotationbase_instantiation(instance):
    assert isinstance(instance, qm_AnnotationBase)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=qm_CharacterizingElement_strategy)
@settings(max_examples=50)
def test_qm_characterizingelement_instantiation(instance):
    assert isinstance(instance, qm_CharacterizingElement)

@given(instance=qm_ManualInstrument_strategy)
@settings(max_examples=50)
def test_qm_manualinstrument_instantiation(instance):
    assert isinstance(instance, qm_ManualInstrument)

@given(instance=qm_Entity_strategy)
@settings(max_examples=50)
def test_qm_entity_instantiation(instance):
    assert isinstance(instance, qm_Entity)



@given(instance=qm_Entity_strategy)
def test_qm_entity_useCase_setter(instance):
    original = instance.useCase
    instance.useCase = original
    assert instance.useCase == original



@given(instance=qm_Entity_strategy)
def test_qm_entity_stakeholder_setter(instance):
    original = instance.stakeholder
    instance.stakeholder = original
    assert instance.stakeholder == original

@given(instance=qm_MeasureAggregation_strategy)
@settings(max_examples=50)
def test_qm_measureaggregation_instantiation(instance):
    assert isinstance(instance, qm_MeasureAggregation)

@given(instance=qm_QualityModel_strategy)
@settings(max_examples=50)
def test_qm_qualitymodel_instantiation(instance):
    assert isinstance(instance, qm_QualityModel)



@given(instance=qm_QualityModel_strategy)
def test_qm_qualitymodel_schoolGradeBoundary6_setter(instance):
    original = instance.schoolGradeBoundary6
    instance.schoolGradeBoundary6 = original
    assert instance.schoolGradeBoundary6 == original



@given(instance=qm_QualityModel_strategy)
def test_qm_qualitymodel_schoolGradeBoundary4_setter(instance):
    original = instance.schoolGradeBoundary4
    instance.schoolGradeBoundary4 = original
    assert instance.schoolGradeBoundary4 == original



@given(instance=qm_QualityModel_strategy)
def test_qm_qualitymodel_schoolGradeBoundary5_setter(instance):
    original = instance.schoolGradeBoundary5
    instance.schoolGradeBoundary5 = original
    assert instance.schoolGradeBoundary5 == original



@given(instance=qm_QualityModel_strategy)
def test_qm_qualitymodel_schoolGradeBoundary2_setter(instance):
    original = instance.schoolGradeBoundary2
    instance.schoolGradeBoundary2 = original
    assert instance.schoolGradeBoundary2 == original



@given(instance=qm_QualityModel_strategy)
def test_qm_qualitymodel_schoolGradeBoundary3_setter(instance):
    original = instance.schoolGradeBoundary3
    instance.schoolGradeBoundary3 = original
    assert instance.schoolGradeBoundary3 == original

@given(instance=qm_Source_strategy)
@settings(max_examples=50)
def test_qm_source_instantiation(instance):
    assert isinstance(instance, qm_Source)

@given(instance=qm_Tag_strategy)
@settings(max_examples=50)
def test_qm_tag_instantiation(instance):
    assert isinstance(instance, qm_Tag)

@given(instance=qm_Tool_strategy)
@settings(max_examples=50)
def test_qm_tool_instantiation(instance):
    assert isinstance(instance, qm_Tool)

@given(instance=qm_MeasurementMethod_strategy)
@settings(max_examples=50)
def test_qm_measurementmethod_instantiation(instance):
    assert isinstance(instance, qm_MeasurementMethod)

@given(instance=qm_Measure_strategy)
@settings(max_examples=50)
def test_qm_measure_instantiation(instance):
    assert isinstance(instance, qm_Measure)



@given(instance=qm_Measure_strategy)
def test_qm_measure_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=qm_Evaluation_strategy)
@settings(max_examples=50)
def test_qm_evaluation_instantiation(instance):
    assert isinstance(instance, qm_Evaluation)



@given(instance=qm_Evaluation_strategy)
def test_qm_evaluation_maximumPoints_setter(instance):
    original = instance.maximumPoints
    instance.maximumPoints = original
    assert instance.maximumPoints == original



@given(instance=qm_Evaluation_strategy)
def test_qm_evaluation_completeness_setter(instance):
    original = instance.completeness
    instance.completeness = original
    assert instance.completeness == original

@given(instance=qm_Factor_strategy)
@settings(max_examples=50)
def test_qm_factor_instantiation(instance):
    assert isinstance(instance, qm_Factor)
