import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UnitOfMeasure,
    smm_CountingUnit,
    smm_SmmElement,
    BaseMeasurementRelationship,
    smm_ScaledBaseMeasurementRelationship,
    BinaryMeasurement,
    smm_RatioMeasurement,
    BinaryMeasure,
    smm_RatioMeasure,
    Interval,
    smm_RankingInterval,
    smm_GradeInterval,
    BaseMeasureRelationship,
    smm_ScaledBaseMeasureRelationship,
    smm_EObject,
    smm_RescaledMeasurementRelationship,
    Measurement,
    smm_DimensionalMeasurement,
    smm_RescaledMeasureRelationship,
    Measure,
    smm_GradeMeasure,
    smm_DimensionalMeasure,
    smm_GradeMeasurement,
    MeasurementRelationship,
    smm_RefinementMeasurementRelationship,
    smm_BaseMeasurementRelationship,
    smm_EquivalentMeasurementRelationship,
    MeasureRelationship,
    smm_RefinementMeasureRelationship,
    smm_BaseMeasureRelationship,
    smm_EquivalentMeasureRelationship,
    DimensionalMeasurement,
    smm_RankingMeasurement,
    smm_RescaledMeasurement,
    smm_NamedMeasurement,
    smm_DirectMeasurement,
    smm_BinaryMeasurement,
    DimensionalMeasure,
    smm_RankingMeasure,
    smm_DirectMeasure,
    smm_RescaledMeasure,
    smm_NamedMeasure,
    smm_BinaryMeasure,
    ScaledBaseMeasurementRelationship,
    smm_BaseNMeasurementRelationship,
    smm_Base2MeasurementRelationship,
    smm_RankingMeasurementRelationship,
    smm_GradeMeasurementRelationship,
    smm_Base1MeasurementRelationship,
    ScaledBaseMeasureRelationship,
    smm_GradeMeasureRelationship,
    smm_RankingMeasureRelationship,
    smm_BaseNMeasureRelationship,
    smm_Base2MeasureRelationship,
    smm_Base1MeasureRelationship,
    smm_CollectiveMeasurement,
    smm_CollectiveMeasure,
    AbstractMeasureElement,
    smm_OCLOperation,
    smm_Scope,
    smm_UnitOfMeasure,
    smm_MeasureCategory,
    smm_Operation,
    smm_Measure,
    smm_Characteristic,
    SmmRelationship,
    smm_MeasureRelationship,
    smm_MeasurementRelationship,
    smm_CategoryRelationship,
    SmmElement,
    smm_Attribute,
    smm_Argument,
    smm_SmmModel,
    smm_MeasureLibrary,
    smm_Annotation,
    smm_Observation,
    smm_ObservedMeasure,
    smm_Interval,
    smm_ObservationScope,
    smm_Measurement,
    smm_SmmRelationship,
    smm_AbstractMeasureElement,
    Influence,
    Accumulator,
    BinaryFunctor,
    ScaleOfMeasurement,
    MeasurementScale,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unitofmeasure_is_not_abstract():
    assert not inspect.isabstract(UnitOfMeasure)


def test_unitofmeasure_constructor_exists():
    assert callable(UnitOfMeasure.__init__)


def test_unitofmeasure_constructor_args():
    sig = inspect.signature(UnitOfMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_countingunit_is_not_abstract():
    assert not inspect.isabstract(smm_CountingUnit)


def test_smm_countingunit_constructor_exists():
    assert callable(smm_CountingUnit.__init__)


def test_smm_countingunit_constructor_args():
    sig = inspect.signature(smm_CountingUnit.__init__)
    params = list(sig.parameters.keys())



def test_smm_smmelement_is_not_abstract():
    assert not inspect.isabstract(smm_SmmElement)


def test_smm_smmelement_constructor_exists():
    assert callable(smm_SmmElement.__init__)


def test_smm_smmelement_constructor_args():
    sig = inspect.signature(smm_SmmElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "shortDescription" in params, "Missing parameter 'shortDescription'"
    assert "name" in params, "Missing parameter 'name'"

def test_smm_smmelement_has_description():
    assert hasattr(smm_SmmElement, "description")
    descriptor = None
    for klass in smm_SmmElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_smm_smmelement_has_shortDescription():
    assert hasattr(smm_SmmElement, "shortDescription")
    descriptor = None
    for klass in smm_SmmElement.__mro__:
        if "shortDescription" in klass.__dict__:
            descriptor = klass.__dict__["shortDescription"]
            break
    assert isinstance(descriptor, property)

def test_smm_smmelement_has_name():
    assert hasattr(smm_SmmElement, "name")
    descriptor = None
    for klass in smm_SmmElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(BaseMeasurementRelationship)


def test_basemeasurementrelationship_constructor_exists():
    assert callable(BaseMeasurementRelationship.__init__)


def test_basemeasurementrelationship_constructor_args():
    sig = inspect.signature(BaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_scaledbasemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_ScaledBaseMeasurementRelationship)


def test_smm_scaledbasemeasurementrelationship_constructor_exists():
    assert callable(smm_ScaledBaseMeasurementRelationship.__init__)


def test_smm_scaledbasemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_ScaledBaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_binarymeasurement_is_not_abstract():
    assert not inspect.isabstract(BinaryMeasurement)


def test_binarymeasurement_constructor_exists():
    assert callable(BinaryMeasurement.__init__)


def test_binarymeasurement_constructor_args():
    sig = inspect.signature(BinaryMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_ratiomeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_RatioMeasurement)


def test_smm_ratiomeasurement_constructor_exists():
    assert callable(smm_RatioMeasurement.__init__)


def test_smm_ratiomeasurement_constructor_args():
    sig = inspect.signature(smm_RatioMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_binarymeasure_is_not_abstract():
    assert not inspect.isabstract(BinaryMeasure)


def test_binarymeasure_constructor_exists():
    assert callable(BinaryMeasure.__init__)


def test_binarymeasure_constructor_args():
    sig = inspect.signature(BinaryMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_ratiomeasure_is_not_abstract():
    assert not inspect.isabstract(smm_RatioMeasure)


def test_smm_ratiomeasure_constructor_exists():
    assert callable(smm_RatioMeasure.__init__)


def test_smm_ratiomeasure_constructor_args():
    sig = inspect.signature(smm_RatioMeasure.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankinginterval_is_not_abstract():
    assert not inspect.isabstract(smm_RankingInterval)


def test_smm_rankinginterval_constructor_exists():
    assert callable(smm_RankingInterval.__init__)


def test_smm_rankinginterval_constructor_args():
    sig = inspect.signature(smm_RankingInterval.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smm_rankinginterval_has_value():
    assert hasattr(smm_RankingInterval, "value")
    descriptor = None
    for klass in smm_RankingInterval.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm_gradeinterval_is_not_abstract():
    assert not inspect.isabstract(smm_GradeInterval)


def test_smm_gradeinterval_constructor_exists():
    assert callable(smm_GradeInterval.__init__)


def test_smm_gradeinterval_constructor_args():
    sig = inspect.signature(smm_GradeInterval.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_smm_gradeinterval_has_symbol():
    assert hasattr(smm_GradeInterval, "symbol")
    descriptor = None
    for klass in smm_GradeInterval.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_basemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(BaseMeasureRelationship)


def test_basemeasurerelationship_constructor_exists():
    assert callable(BaseMeasureRelationship.__init__)


def test_basemeasurerelationship_constructor_args():
    sig = inspect.signature(BaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_scaledbasemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_ScaledBaseMeasureRelationship)


def test_smm_scaledbasemeasurerelationship_constructor_exists():
    assert callable(smm_ScaledBaseMeasureRelationship.__init__)


def test_smm_scaledbasemeasurerelationship_constructor_args():
    sig = inspect.signature(smm_ScaledBaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_eobject_is_not_abstract():
    assert not inspect.isabstract(smm_EObject)


def test_smm_eobject_constructor_exists():
    assert callable(smm_EObject.__init__)


def test_smm_eobject_constructor_args():
    sig = inspect.signature(smm_EObject.__init__)
    params = list(sig.parameters.keys())



def test_smm_rescaledmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RescaledMeasurementRelationship)


def test_smm_rescaledmeasurementrelationship_constructor_exists():
    assert callable(smm_RescaledMeasurementRelationship.__init__)


def test_smm_rescaledmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RescaledMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measurement_is_not_abstract():
    assert not inspect.isabstract(Measurement)


def test_measurement_constructor_exists():
    assert callable(Measurement.__init__)


def test_measurement_constructor_args():
    sig = inspect.signature(Measurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_dimensionalmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_DimensionalMeasurement)


def test_smm_dimensionalmeasurement_constructor_exists():
    assert callable(smm_DimensionalMeasurement.__init__)


def test_smm_dimensionalmeasurement_constructor_args():
    sig = inspect.signature(smm_DimensionalMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smm_dimensionalmeasurement_has_value():
    assert hasattr(smm_DimensionalMeasurement, "value")
    descriptor = None
    for klass in smm_DimensionalMeasurement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm_rescaledmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RescaledMeasureRelationship)


def test_smm_rescaledmeasurerelationship_constructor_exists():
    assert callable(smm_RescaledMeasureRelationship.__init__)


def test_smm_rescaledmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RescaledMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_smm_grademeasure_is_not_abstract():
    assert not inspect.isabstract(smm_GradeMeasure)


def test_smm_grademeasure_constructor_exists():
    assert callable(smm_GradeMeasure.__init__)


def test_smm_grademeasure_constructor_args():
    sig = inspect.signature(smm_GradeMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_DimensionalMeasure)


def test_smm_dimensionalmeasure_constructor_exists():
    assert callable(smm_DimensionalMeasure.__init__)


def test_smm_dimensionalmeasure_constructor_args():
    sig = inspect.signature(smm_DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"

def test_smm_dimensionalmeasure_has_formula():
    assert hasattr(smm_DimensionalMeasure, "formula")
    descriptor = None
    for klass in smm_DimensionalMeasure.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_smm_grademeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_GradeMeasurement)


def test_smm_grademeasurement_constructor_exists():
    assert callable(smm_GradeMeasurement.__init__)


def test_smm_grademeasurement_constructor_args():
    sig = inspect.signature(smm_GradeMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm_grademeasurement_has_value():
    assert hasattr(smm_GradeMeasurement, "value")
    descriptor = None
    for klass in smm_GradeMeasurement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smm_grademeasurement_has_isBaseSupplied():
    assert hasattr(smm_GradeMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm_GradeMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(MeasurementRelationship)


def test_measurementrelationship_constructor_exists():
    assert callable(MeasurementRelationship.__init__)


def test_measurementrelationship_constructor_args():
    sig = inspect.signature(MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_refinementmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RefinementMeasurementRelationship)


def test_smm_refinementmeasurementrelationship_constructor_exists():
    assert callable(smm_RefinementMeasurementRelationship.__init__)


def test_smm_refinementmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RefinementMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_basemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_BaseMeasurementRelationship)


def test_smm_basemeasurementrelationship_constructor_exists():
    assert callable(smm_BaseMeasurementRelationship.__init__)


def test_smm_basemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_BaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_equivalentmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_EquivalentMeasurementRelationship)


def test_smm_equivalentmeasurementrelationship_constructor_exists():
    assert callable(smm_EquivalentMeasurementRelationship.__init__)


def test_smm_equivalentmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_EquivalentMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measurerelationship_is_not_abstract():
    assert not inspect.isabstract(MeasureRelationship)


def test_measurerelationship_constructor_exists():
    assert callable(MeasureRelationship.__init__)


def test_measurerelationship_constructor_args():
    sig = inspect.signature(MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_refinementmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RefinementMeasureRelationship)


def test_smm_refinementmeasurerelationship_constructor_exists():
    assert callable(smm_RefinementMeasureRelationship.__init__)


def test_smm_refinementmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RefinementMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_basemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_BaseMeasureRelationship)


def test_smm_basemeasurerelationship_constructor_exists():
    assert callable(smm_BaseMeasureRelationship.__init__)


def test_smm_basemeasurerelationship_constructor_args():
    sig = inspect.signature(smm_BaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_equivalentmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_EquivalentMeasureRelationship)


def test_smm_equivalentmeasurerelationship_constructor_exists():
    assert callable(smm_EquivalentMeasureRelationship.__init__)


def test_smm_equivalentmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_EquivalentMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_dimensionalmeasurement_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasurement)


def test_dimensionalmeasurement_constructor_exists():
    assert callable(DimensionalMeasurement.__init__)


def test_dimensionalmeasurement_constructor_args():
    sig = inspect.signature(DimensionalMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankingmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_RankingMeasurement)


def test_smm_rankingmeasurement_constructor_exists():
    assert callable(smm_RankingMeasurement.__init__)


def test_smm_rankingmeasurement_constructor_args():
    sig = inspect.signature(smm_RankingMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm_rankingmeasurement_has_isBaseSupplied():
    assert hasattr(smm_RankingMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm_RankingMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm_rescaledmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_RescaledMeasurement)


def test_smm_rescaledmeasurement_constructor_exists():
    assert callable(smm_RescaledMeasurement.__init__)


def test_smm_rescaledmeasurement_constructor_args():
    sig = inspect.signature(smm_RescaledMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm_rescaledmeasurement_has_isBaseSupplied():
    assert hasattr(smm_RescaledMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm_RescaledMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm_namedmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_NamedMeasurement)


def test_smm_namedmeasurement_constructor_exists():
    assert callable(smm_NamedMeasurement.__init__)


def test_smm_namedmeasurement_constructor_args():
    sig = inspect.signature(smm_NamedMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_directmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_DirectMeasurement)


def test_smm_directmeasurement_constructor_exists():
    assert callable(smm_DirectMeasurement.__init__)


def test_smm_directmeasurement_constructor_args():
    sig = inspect.signature(smm_DirectMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_binarymeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_BinaryMeasurement)


def test_smm_binarymeasurement_constructor_exists():
    assert callable(smm_BinaryMeasurement.__init__)


def test_smm_binarymeasurement_constructor_args():
    sig = inspect.signature(smm_BinaryMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm_binarymeasurement_has_isBaseSupplied():
    assert hasattr(smm_BinaryMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm_BinaryMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasure)


def test_dimensionalmeasure_constructor_exists():
    assert callable(DimensionalMeasure.__init__)


def test_dimensionalmeasure_constructor_args():
    sig = inspect.signature(DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankingmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_RankingMeasure)


def test_smm_rankingmeasure_constructor_exists():
    assert callable(smm_RankingMeasure.__init__)


def test_smm_rankingmeasure_constructor_args():
    sig = inspect.signature(smm_RankingMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_directmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_DirectMeasure)


def test_smm_directmeasure_constructor_exists():
    assert callable(smm_DirectMeasure.__init__)


def test_smm_directmeasure_constructor_args():
    sig = inspect.signature(smm_DirectMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_rescaledmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_RescaledMeasure)


def test_smm_rescaledmeasure_constructor_exists():
    assert callable(smm_RescaledMeasure.__init__)


def test_smm_rescaledmeasure_constructor_args():
    sig = inspect.signature(smm_RescaledMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "multiplier" in params, "Missing parameter 'multiplier'"
    assert "operationFirst" in params, "Missing parameter 'operationFirst'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_smm_rescaledmeasure_has_multiplier():
    assert hasattr(smm_RescaledMeasure, "multiplier")
    descriptor = None
    for klass in smm_RescaledMeasure.__mro__:
        if "multiplier" in klass.__dict__:
            descriptor = klass.__dict__["multiplier"]
            break
    assert isinstance(descriptor, property)

def test_smm_rescaledmeasure_has_operationFirst():
    assert hasattr(smm_RescaledMeasure, "operationFirst")
    descriptor = None
    for klass in smm_RescaledMeasure.__mro__:
        if "operationFirst" in klass.__dict__:
            descriptor = klass.__dict__["operationFirst"]
            break
    assert isinstance(descriptor, property)

def test_smm_rescaledmeasure_has_offset():
    assert hasattr(smm_RescaledMeasure, "offset")
    descriptor = None
    for klass in smm_RescaledMeasure.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_smm_namedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_NamedMeasure)


def test_smm_namedmeasure_constructor_exists():
    assert callable(smm_NamedMeasure.__init__)


def test_smm_namedmeasure_constructor_args():
    sig = inspect.signature(smm_NamedMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_binarymeasure_is_not_abstract():
    assert not inspect.isabstract(smm_BinaryMeasure)


def test_smm_binarymeasure_constructor_exists():
    assert callable(smm_BinaryMeasure.__init__)


def test_smm_binarymeasure_constructor_args():
    sig = inspect.signature(smm_BinaryMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "functor" in params, "Missing parameter 'functor'"

def test_smm_binarymeasure_has_functor():
    assert hasattr(smm_BinaryMeasure, "functor")
    descriptor = None
    for klass in smm_BinaryMeasure.__mro__:
        if "functor" in klass.__dict__:
            descriptor = klass.__dict__["functor"]
            break
    assert isinstance(descriptor, property)



def test_scaledbasemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(ScaledBaseMeasurementRelationship)


def test_scaledbasemeasurementrelationship_constructor_exists():
    assert callable(ScaledBaseMeasurementRelationship.__init__)


def test_scaledbasemeasurementrelationship_constructor_args():
    sig = inspect.signature(ScaledBaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_basenmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_BaseNMeasurementRelationship)


def test_smm_basenmeasurementrelationship_constructor_exists():
    assert callable(smm_BaseNMeasurementRelationship.__init__)


def test_smm_basenmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_BaseNMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_base2measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_Base2MeasurementRelationship)


def test_smm_base2measurementrelationship_constructor_exists():
    assert callable(smm_Base2MeasurementRelationship.__init__)


def test_smm_base2measurementrelationship_constructor_args():
    sig = inspect.signature(smm_Base2MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankingmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RankingMeasurementRelationship)


def test_smm_rankingmeasurementrelationship_constructor_exists():
    assert callable(smm_RankingMeasurementRelationship.__init__)


def test_smm_rankingmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RankingMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_grademeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_GradeMeasurementRelationship)


def test_smm_grademeasurementrelationship_constructor_exists():
    assert callable(smm_GradeMeasurementRelationship.__init__)


def test_smm_grademeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_GradeMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_base1measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_Base1MeasurementRelationship)


def test_smm_base1measurementrelationship_constructor_exists():
    assert callable(smm_Base1MeasurementRelationship.__init__)


def test_smm_base1measurementrelationship_constructor_args():
    sig = inspect.signature(smm_Base1MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_scaledbasemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(ScaledBaseMeasureRelationship)


def test_scaledbasemeasurerelationship_constructor_exists():
    assert callable(ScaledBaseMeasureRelationship.__init__)


def test_scaledbasemeasurerelationship_constructor_args():
    sig = inspect.signature(ScaledBaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_grademeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_GradeMeasureRelationship)


def test_smm_grademeasurerelationship_constructor_exists():
    assert callable(smm_GradeMeasureRelationship.__init__)


def test_smm_grademeasurerelationship_constructor_args():
    sig = inspect.signature(smm_GradeMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankingmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RankingMeasureRelationship)


def test_smm_rankingmeasurerelationship_constructor_exists():
    assert callable(smm_RankingMeasureRelationship.__init__)


def test_smm_rankingmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RankingMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_basenmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_BaseNMeasureRelationship)


def test_smm_basenmeasurerelationship_constructor_exists():
    assert callable(smm_BaseNMeasureRelationship.__init__)


def test_smm_basenmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_BaseNMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_base2measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_Base2MeasureRelationship)


def test_smm_base2measurerelationship_constructor_exists():
    assert callable(smm_Base2MeasureRelationship.__init__)


def test_smm_base2measurerelationship_constructor_args():
    sig = inspect.signature(smm_Base2MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_base1measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_Base1MeasureRelationship)


def test_smm_base1measurerelationship_constructor_exists():
    assert callable(smm_Base1MeasureRelationship.__init__)


def test_smm_base1measurerelationship_constructor_args():
    sig = inspect.signature(smm_Base1MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_collectivemeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_CollectiveMeasurement)


def test_smm_collectivemeasurement_constructor_exists():
    assert callable(smm_CollectiveMeasurement.__init__)


def test_smm_collectivemeasurement_constructor_args():
    sig = inspect.signature(smm_CollectiveMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm_collectivemeasurement_has_isBaseSupplied():
    assert hasattr(smm_CollectiveMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm_CollectiveMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm_collectivemeasure_is_not_abstract():
    assert not inspect.isabstract(smm_CollectiveMeasure)


def test_smm_collectivemeasure_constructor_exists():
    assert callable(smm_CollectiveMeasure.__init__)


def test_smm_collectivemeasure_constructor_args():
    sig = inspect.signature(smm_CollectiveMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "accumulator" in params, "Missing parameter 'accumulator'"

def test_smm_collectivemeasure_has_accumulator():
    assert hasattr(smm_CollectiveMeasure, "accumulator")
    descriptor = None
    for klass in smm_CollectiveMeasure.__mro__:
        if "accumulator" in klass.__dict__:
            descriptor = klass.__dict__["accumulator"]
            break
    assert isinstance(descriptor, property)



def test_abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(AbstractMeasureElement)


def test_abstractmeasureelement_constructor_exists():
    assert callable(AbstractMeasureElement.__init__)


def test_abstractmeasureelement_constructor_args():
    sig = inspect.signature(AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())



def test_smm_ocloperation_is_not_abstract():
    assert not inspect.isabstract(smm_OCLOperation)


def test_smm_ocloperation_constructor_exists():
    assert callable(smm_OCLOperation.__init__)


def test_smm_ocloperation_constructor_args():
    sig = inspect.signature(smm_OCLOperation.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "context" in params, "Missing parameter 'context'"

def test_smm_ocloperation_has_body():
    assert hasattr(smm_OCLOperation, "body")
    descriptor = None
    for klass in smm_OCLOperation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_smm_ocloperation_has_context():
    assert hasattr(smm_OCLOperation, "context")
    descriptor = None
    for klass in smm_OCLOperation.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_smm_scope_is_not_abstract():
    assert not inspect.isabstract(smm_Scope)


def test_smm_scope_constructor_exists():
    assert callable(smm_Scope.__init__)


def test_smm_scope_constructor_args():
    sig = inspect.signature(smm_Scope.__init__)
    params = list(sig.parameters.keys())



def test_smm_unitofmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_UnitOfMeasure)


def test_smm_unitofmeasure_constructor_exists():
    assert callable(smm_UnitOfMeasure.__init__)


def test_smm_unitofmeasure_constructor_args():
    sig = inspect.signature(smm_UnitOfMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_measurecategory_is_not_abstract():
    assert not inspect.isabstract(smm_MeasureCategory)


def test_smm_measurecategory_constructor_exists():
    assert callable(smm_MeasureCategory.__init__)


def test_smm_measurecategory_constructor_args():
    sig = inspect.signature(smm_MeasureCategory.__init__)
    params = list(sig.parameters.keys())



def test_smm_operation_is_not_abstract():
    assert not inspect.isabstract(smm_Operation)


def test_smm_operation_constructor_exists():
    assert callable(smm_Operation.__init__)


def test_smm_operation_constructor_args():
    sig = inspect.signature(smm_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_smm_operation_has_body():
    assert hasattr(smm_Operation, "body")
    descriptor = None
    for klass in smm_Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_smm_operation_has_language():
    assert hasattr(smm_Operation, "language")
    descriptor = None
    for klass in smm_Operation.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_smm_measure_is_not_abstract():
    assert not inspect.isabstract(smm_Measure)


def test_smm_measure_constructor_exists():
    assert callable(smm_Measure.__init__)


def test_smm_measure_constructor_args():
    sig = inspect.signature(smm_Measure.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "measureLabelFormat" in params, "Missing parameter 'measureLabelFormat'"
    assert "measurementLabelFormat" in params, "Missing parameter 'measurementLabelFormat'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "customScale" in params, "Missing parameter 'customScale'"
    assert "source" in params, "Missing parameter 'source'"

def test_smm_measure_has_visible():
    assert hasattr(smm_Measure, "visible")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_smm_measure_has_measureLabelFormat():
    assert hasattr(smm_Measure, "measureLabelFormat")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "measureLabelFormat" in klass.__dict__:
            descriptor = klass.__dict__["measureLabelFormat"]
            break
    assert isinstance(descriptor, property)

def test_smm_measure_has_measurementLabelFormat():
    assert hasattr(smm_Measure, "measurementLabelFormat")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "measurementLabelFormat" in klass.__dict__:
            descriptor = klass.__dict__["measurementLabelFormat"]
            break
    assert isinstance(descriptor, property)

def test_smm_measure_has_scale():
    assert hasattr(smm_Measure, "scale")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_smm_measure_has_customScale():
    assert hasattr(smm_Measure, "customScale")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "customScale" in klass.__dict__:
            descriptor = klass.__dict__["customScale"]
            break
    assert isinstance(descriptor, property)

def test_smm_measure_has_source():
    assert hasattr(smm_Measure, "source")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_smm_characteristic_is_not_abstract():
    assert not inspect.isabstract(smm_Characteristic)


def test_smm_characteristic_constructor_exists():
    assert callable(smm_Characteristic.__init__)


def test_smm_characteristic_constructor_args():
    sig = inspect.signature(smm_Characteristic.__init__)
    params = list(sig.parameters.keys())



def test_smmrelationship_is_not_abstract():
    assert not inspect.isabstract(SmmRelationship)


def test_smmrelationship_constructor_exists():
    assert callable(SmmRelationship.__init__)


def test_smmrelationship_constructor_args():
    sig = inspect.signature(SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_MeasureRelationship)


def test_smm_measurerelationship_constructor_exists():
    assert callable(smm_MeasureRelationship.__init__)


def test_smm_measurerelationship_constructor_args():
    sig = inspect.signature(smm_MeasureRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "influence" in params, "Missing parameter 'influence'"

def test_smm_measurerelationship_has_influence():
    assert hasattr(smm_MeasureRelationship, "influence")
    descriptor = None
    for klass in smm_MeasureRelationship.__mro__:
        if "influence" in klass.__dict__:
            descriptor = klass.__dict__["influence"]
            break
    assert isinstance(descriptor, property)



def test_smm_measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_MeasurementRelationship)


def test_smm_measurementrelationship_constructor_exists():
    assert callable(smm_MeasurementRelationship.__init__)


def test_smm_measurementrelationship_constructor_args():
    sig = inspect.signature(smm_MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_categoryrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_CategoryRelationship)


def test_smm_categoryrelationship_constructor_exists():
    assert callable(smm_CategoryRelationship.__init__)


def test_smm_categoryrelationship_constructor_args():
    sig = inspect.signature(smm_CategoryRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smmelement_is_not_abstract():
    assert not inspect.isabstract(SmmElement)


def test_smmelement_constructor_exists():
    assert callable(SmmElement.__init__)


def test_smmelement_constructor_args():
    sig = inspect.signature(SmmElement.__init__)
    params = list(sig.parameters.keys())



def test_smm_attribute_is_not_abstract():
    assert not inspect.isabstract(smm_Attribute)


def test_smm_attribute_constructor_exists():
    assert callable(smm_Attribute.__init__)


def test_smm_attribute_constructor_args():
    sig = inspect.signature(smm_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_smm_attribute_has_value():
    assert hasattr(smm_Attribute, "value")
    descriptor = None
    for klass in smm_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smm_attribute_has_tag():
    assert hasattr(smm_Attribute, "tag")
    descriptor = None
    for klass in smm_Attribute.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_smm_argument_is_not_abstract():
    assert not inspect.isabstract(smm_Argument)


def test_smm_argument_constructor_exists():
    assert callable(smm_Argument.__init__)


def test_smm_argument_constructor_args():
    sig = inspect.signature(smm_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_smm_argument_has_value():
    assert hasattr(smm_Argument, "value")
    descriptor = None
    for klass in smm_Argument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smm_argument_has_Type():
    assert hasattr(smm_Argument, "Type")
    descriptor = None
    for klass in smm_Argument.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_smm_smmmodel_is_not_abstract():
    assert not inspect.isabstract(smm_SmmModel)


def test_smm_smmmodel_constructor_exists():
    assert callable(smm_SmmModel.__init__)


def test_smm_smmmodel_constructor_args():
    sig = inspect.signature(smm_SmmModel.__init__)
    params = list(sig.parameters.keys())



def test_smm_measurelibrary_is_not_abstract():
    assert not inspect.isabstract(smm_MeasureLibrary)


def test_smm_measurelibrary_constructor_exists():
    assert callable(smm_MeasureLibrary.__init__)


def test_smm_measurelibrary_constructor_args():
    sig = inspect.signature(smm_MeasureLibrary.__init__)
    params = list(sig.parameters.keys())



def test_smm_annotation_is_not_abstract():
    assert not inspect.isabstract(smm_Annotation)


def test_smm_annotation_constructor_exists():
    assert callable(smm_Annotation.__init__)


def test_smm_annotation_constructor_args():
    sig = inspect.signature(smm_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_smm_annotation_has_text():
    assert hasattr(smm_Annotation, "text")
    descriptor = None
    for klass in smm_Annotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_smm_observation_is_not_abstract():
    assert not inspect.isabstract(smm_Observation)


def test_smm_observation_constructor_exists():
    assert callable(smm_Observation.__init__)


def test_smm_observation_constructor_args():
    sig = inspect.signature(smm_Observation.__init__)
    params = list(sig.parameters.keys())
    assert "whenObserved" in params, "Missing parameter 'whenObserved'"
    assert "observer" in params, "Missing parameter 'observer'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_smm_observation_has_whenObserved():
    assert hasattr(smm_Observation, "whenObserved")
    descriptor = None
    for klass in smm_Observation.__mro__:
        if "whenObserved" in klass.__dict__:
            descriptor = klass.__dict__["whenObserved"]
            break
    assert isinstance(descriptor, property)

def test_smm_observation_has_observer():
    assert hasattr(smm_Observation, "observer")
    descriptor = None
    for klass in smm_Observation.__mro__:
        if "observer" in klass.__dict__:
            descriptor = klass.__dict__["observer"]
            break
    assert isinstance(descriptor, property)

def test_smm_observation_has_tool():
    assert hasattr(smm_Observation, "tool")
    descriptor = None
    for klass in smm_Observation.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_smm_observedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_ObservedMeasure)


def test_smm_observedmeasure_constructor_exists():
    assert callable(smm_ObservedMeasure.__init__)


def test_smm_observedmeasure_constructor_args():
    sig = inspect.signature(smm_ObservedMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_interval_is_not_abstract():
    assert not inspect.isabstract(smm_Interval)


def test_smm_interval_constructor_exists():
    assert callable(smm_Interval.__init__)


def test_smm_interval_constructor_args():
    sig = inspect.signature(smm_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "maximumOpen" in params, "Missing parameter 'maximumOpen'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "minimumOpen" in params, "Missing parameter 'minimumOpen'"

def test_smm_interval_has_maximumOpen():
    assert hasattr(smm_Interval, "maximumOpen")
    descriptor = None
    for klass in smm_Interval.__mro__:
        if "maximumOpen" in klass.__dict__:
            descriptor = klass.__dict__["maximumOpen"]
            break
    assert isinstance(descriptor, property)

def test_smm_interval_has_maximum():
    assert hasattr(smm_Interval, "maximum")
    descriptor = None
    for klass in smm_Interval.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_smm_interval_has_minimum():
    assert hasattr(smm_Interval, "minimum")
    descriptor = None
    for klass in smm_Interval.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_smm_interval_has_minimumOpen():
    assert hasattr(smm_Interval, "minimumOpen")
    descriptor = None
    for klass in smm_Interval.__mro__:
        if "minimumOpen" in klass.__dict__:
            descriptor = klass.__dict__["minimumOpen"]
            break
    assert isinstance(descriptor, property)



def test_smm_observationscope_is_not_abstract():
    assert not inspect.isabstract(smm_ObservationScope)


def test_smm_observationscope_constructor_exists():
    assert callable(smm_ObservationScope.__init__)


def test_smm_observationscope_constructor_args():
    sig = inspect.signature(smm_ObservationScope.__init__)
    params = list(sig.parameters.keys())
    assert "scopeUri" in params, "Missing parameter 'scopeUri'"

def test_smm_observationscope_has_scopeUri():
    assert hasattr(smm_ObservationScope, "scopeUri")
    descriptor = None
    for klass in smm_ObservationScope.__mro__:
        if "scopeUri" in klass.__dict__:
            descriptor = klass.__dict__["scopeUri"]
            break
    assert isinstance(descriptor, property)



def test_smm_measurement_is_not_abstract():
    assert not inspect.isabstract(smm_Measurement)


def test_smm_measurement_constructor_exists():
    assert callable(smm_Measurement.__init__)


def test_smm_measurement_constructor_args():
    sig = inspect.signature(smm_Measurement.__init__)
    params = list(sig.parameters.keys())
    assert "breakValue" in params, "Missing parameter 'breakValue'"
    assert "error" in params, "Missing parameter 'error'"

def test_smm_measurement_has_breakValue():
    assert hasattr(smm_Measurement, "breakValue")
    descriptor = None
    for klass in smm_Measurement.__mro__:
        if "breakValue" in klass.__dict__:
            descriptor = klass.__dict__["breakValue"]
            break
    assert isinstance(descriptor, property)

def test_smm_measurement_has_error():
    assert hasattr(smm_Measurement, "error")
    descriptor = None
    for klass in smm_Measurement.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)



def test_smm_smmrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_SmmRelationship)


def test_smm_smmrelationship_constructor_exists():
    assert callable(smm_SmmRelationship.__init__)


def test_smm_smmrelationship_constructor_args():
    sig = inspect.signature(smm_SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(smm_AbstractMeasureElement)


def test_smm_abstractmeasureelement_constructor_exists():
    assert callable(smm_AbstractMeasureElement.__init__)


def test_smm_abstractmeasureelement_constructor_args():
    sig = inspect.signature(smm_AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())

def test_influence_exists():
    # Check that the Enumeration exists
    assert Influence is not None

def test_influence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Influence]
    expected_literals = [
        "positive",
        "negative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Influence"

def test_accumulator_exists():
    # Check that the Enumeration exists
    assert Accumulator is not None

def test_accumulator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Accumulator]
    expected_literals = [
        "minimum",
        "standardDeviation",
        "product",
        "average",
        "maximum",
        "sum",
        "custom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Accumulator"

def test_binaryfunctor_exists():
    # Check that the Enumeration exists
    assert BinaryFunctor is not None

def test_binaryfunctor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryFunctor]
    expected_literals = [
        "minus",
        "plus",
        "multiply",
        "divide",
        "custom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryFunctor"

def test_scaleofmeasurement_exists():
    # Check that the Enumeration exists
    assert ScaleOfMeasurement is not None

def test_scaleofmeasurement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleOfMeasurement]
    expected_literals = [
        "ordinal",
        "interval",
        "nominal",
        "ratio",
        "custom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleOfMeasurement"

def test_measurementscale_exists():
    # Check that the Enumeration exists
    assert MeasurementScale is not None

def test_measurementscale_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasurementScale]
    expected_literals = [
        "nominal",
        "interval",
        "ratio",
        "ordinal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasurementScale"


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
UnitOfMeasure_strategy = st.builds(
    UnitOfMeasure,
)
smm_CountingUnit_strategy = st.builds(
    smm_CountingUnit,
)
smm_SmmElement_strategy = st.builds(
    smm_SmmElement,
    description=
        safe_text,
    shortDescription=
        safe_text,
    name=
        safe_text
)
BaseMeasurementRelationship_strategy = st.builds(
    BaseMeasurementRelationship,
)
smm_ScaledBaseMeasurementRelationship_strategy = st.builds(
    smm_ScaledBaseMeasurementRelationship,
)
BinaryMeasurement_strategy = st.builds(
    BinaryMeasurement,
)
smm_RatioMeasurement_strategy = st.builds(
    smm_RatioMeasurement,
)
BinaryMeasure_strategy = st.builds(
    BinaryMeasure,
)
smm_RatioMeasure_strategy = st.builds(
    smm_RatioMeasure,
)
Interval_strategy = st.builds(
    Interval,
)
smm_RankingInterval_strategy = st.builds(
    smm_RankingInterval,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm_GradeInterval_strategy = st.builds(
    smm_GradeInterval,
    symbol=
        safe_text
)
BaseMeasureRelationship_strategy = st.builds(
    BaseMeasureRelationship,
)
smm_ScaledBaseMeasureRelationship_strategy = st.builds(
    smm_ScaledBaseMeasureRelationship,
)
smm_EObject_strategy = st.builds(
    smm_EObject,
)
smm_RescaledMeasurementRelationship_strategy = st.builds(
    smm_RescaledMeasurementRelationship,
)
Measurement_strategy = st.builds(
    Measurement,
)
smm_DimensionalMeasurement_strategy = st.builds(
    smm_DimensionalMeasurement,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm_RescaledMeasureRelationship_strategy = st.builds(
    smm_RescaledMeasureRelationship,
)
Measure_strategy = st.builds(
    Measure,
)
smm_GradeMeasure_strategy = st.builds(
    smm_GradeMeasure,
)
smm_DimensionalMeasure_strategy = st.builds(
    smm_DimensionalMeasure,
    formula=
        safe_text
)
smm_GradeMeasurement_strategy = st.builds(
    smm_GradeMeasurement,
    value=
        safe_text,
    isBaseSupplied=
        st.booleans()
)
MeasurementRelationship_strategy = st.builds(
    MeasurementRelationship,
)
smm_RefinementMeasurementRelationship_strategy = st.builds(
    smm_RefinementMeasurementRelationship,
)
smm_BaseMeasurementRelationship_strategy = st.builds(
    smm_BaseMeasurementRelationship,
)
smm_EquivalentMeasurementRelationship_strategy = st.builds(
    smm_EquivalentMeasurementRelationship,
)
MeasureRelationship_strategy = st.builds(
    MeasureRelationship,
)
smm_RefinementMeasureRelationship_strategy = st.builds(
    smm_RefinementMeasureRelationship,
)
smm_BaseMeasureRelationship_strategy = st.builds(
    smm_BaseMeasureRelationship,
)
smm_EquivalentMeasureRelationship_strategy = st.builds(
    smm_EquivalentMeasureRelationship,
)
DimensionalMeasurement_strategy = st.builds(
    DimensionalMeasurement,
)
smm_RankingMeasurement_strategy = st.builds(
    smm_RankingMeasurement,
    isBaseSupplied=
        safe_text
)
smm_RescaledMeasurement_strategy = st.builds(
    smm_RescaledMeasurement,
    isBaseSupplied=
        safe_text
)
smm_NamedMeasurement_strategy = st.builds(
    smm_NamedMeasurement,
)
smm_DirectMeasurement_strategy = st.builds(
    smm_DirectMeasurement,
)
smm_BinaryMeasurement_strategy = st.builds(
    smm_BinaryMeasurement,
    isBaseSupplied=
        safe_text
)
DimensionalMeasure_strategy = st.builds(
    DimensionalMeasure,
)
smm_RankingMeasure_strategy = st.builds(
    smm_RankingMeasure,
)
smm_DirectMeasure_strategy = st.builds(
    smm_DirectMeasure,
)
smm_RescaledMeasure_strategy = st.builds(
    smm_RescaledMeasure,
    multiplier=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    operationFirst=
        safe_text,
    offset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm_NamedMeasure_strategy = st.builds(
    smm_NamedMeasure,
)
smm_BinaryMeasure_strategy = st.builds(
    smm_BinaryMeasure,
    functor=
        safe_text
)
ScaledBaseMeasurementRelationship_strategy = st.builds(
    ScaledBaseMeasurementRelationship,
)
smm_BaseNMeasurementRelationship_strategy = st.builds(
    smm_BaseNMeasurementRelationship,
)
smm_Base2MeasurementRelationship_strategy = st.builds(
    smm_Base2MeasurementRelationship,
)
smm_RankingMeasurementRelationship_strategy = st.builds(
    smm_RankingMeasurementRelationship,
)
smm_GradeMeasurementRelationship_strategy = st.builds(
    smm_GradeMeasurementRelationship,
)
smm_Base1MeasurementRelationship_strategy = st.builds(
    smm_Base1MeasurementRelationship,
)
ScaledBaseMeasureRelationship_strategy = st.builds(
    ScaledBaseMeasureRelationship,
)
smm_GradeMeasureRelationship_strategy = st.builds(
    smm_GradeMeasureRelationship,
)
smm_RankingMeasureRelationship_strategy = st.builds(
    smm_RankingMeasureRelationship,
)
smm_BaseNMeasureRelationship_strategy = st.builds(
    smm_BaseNMeasureRelationship,
)
smm_Base2MeasureRelationship_strategy = st.builds(
    smm_Base2MeasureRelationship,
)
smm_Base1MeasureRelationship_strategy = st.builds(
    smm_Base1MeasureRelationship,
)
smm_CollectiveMeasurement_strategy = st.builds(
    smm_CollectiveMeasurement,
    isBaseSupplied=
        safe_text
)
smm_CollectiveMeasure_strategy = st.builds(
    smm_CollectiveMeasure,
    accumulator=
        safe_text
)
AbstractMeasureElement_strategy = st.builds(
    AbstractMeasureElement,
)
smm_OCLOperation_strategy = st.builds(
    smm_OCLOperation,
    body=
        safe_text,
    context=
        safe_text
)
smm_Scope_strategy = st.builds(
    smm_Scope,
)
smm_UnitOfMeasure_strategy = st.builds(
    smm_UnitOfMeasure,
)
smm_MeasureCategory_strategy = st.builds(
    smm_MeasureCategory,
)
smm_Operation_strategy = st.builds(
    smm_Operation,
    body=
        safe_text,
    language=
        safe_text
)
smm_Measure_strategy = st.builds(
    smm_Measure,
    visible=
        safe_text,
    measureLabelFormat=
        safe_text,
    measurementLabelFormat=
        safe_text,
    scale=
        safe_text,
    customScale=
        safe_text,
    source=
        safe_text
)
smm_Characteristic_strategy = st.builds(
    smm_Characteristic,
)
SmmRelationship_strategy = st.builds(
    SmmRelationship,
)
smm_MeasureRelationship_strategy = st.builds(
    smm_MeasureRelationship,
    influence=
        safe_text
)
smm_MeasurementRelationship_strategy = st.builds(
    smm_MeasurementRelationship,
)
smm_CategoryRelationship_strategy = st.builds(
    smm_CategoryRelationship,
)
SmmElement_strategy = st.builds(
    SmmElement,
)
smm_Attribute_strategy = st.builds(
    smm_Attribute,
    value=
        safe_text,
    tag=
        safe_text
)
smm_Argument_strategy = st.builds(
    smm_Argument,
    value=
        safe_text,
    Type=
        safe_text
)
smm_SmmModel_strategy = st.builds(
    smm_SmmModel,
)
smm_MeasureLibrary_strategy = st.builds(
    smm_MeasureLibrary,
)
smm_Annotation_strategy = st.builds(
    smm_Annotation,
    text=
        safe_text
)
smm_Observation_strategy = st.builds(
    smm_Observation,
    whenObserved=
        safe_text,
    observer=
        safe_text,
    tool=
        safe_text
)
smm_ObservedMeasure_strategy = st.builds(
    smm_ObservedMeasure,
)
smm_Interval_strategy = st.builds(
    smm_Interval,
    maximumOpen=
        safe_text,
    maximum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimumOpen=
        safe_text
)
smm_ObservationScope_strategy = st.builds(
    smm_ObservationScope,
    scopeUri=
        safe_text
)
smm_Measurement_strategy = st.builds(
    smm_Measurement,
    breakValue=
        safe_text,
    error=
        safe_text
)
smm_SmmRelationship_strategy = st.builds(
    smm_SmmRelationship,
)
smm_AbstractMeasureElement_strategy = st.builds(
    smm_AbstractMeasureElement,
)

@given(instance=UnitOfMeasure_strategy)
@settings(max_examples=50)
def test_unitofmeasure_instantiation(instance):
    assert isinstance(instance, UnitOfMeasure)

@given(instance=smm_CountingUnit_strategy)
@settings(max_examples=50)
def test_smm_countingunit_instantiation(instance):
    assert isinstance(instance, smm_CountingUnit)

@given(instance=smm_SmmElement_strategy)
@settings(max_examples=50)
def test_smm_smmelement_instantiation(instance):
    assert isinstance(instance, smm_SmmElement)



@given(instance=smm_SmmElement_strategy)
def test_smm_smmelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=smm_SmmElement_strategy)
def test_smm_smmelement_shortDescription_setter(instance):
    original = instance.shortDescription
    instance.shortDescription = original
    assert instance.shortDescription == original



@given(instance=smm_SmmElement_strategy)
def test_smm_smmelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_basemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, BaseMeasurementRelationship)

@given(instance=smm_ScaledBaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_scaledbasemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_ScaledBaseMeasurementRelationship)

@given(instance=BinaryMeasurement_strategy)
@settings(max_examples=50)
def test_binarymeasurement_instantiation(instance):
    assert isinstance(instance, BinaryMeasurement)

@given(instance=smm_RatioMeasurement_strategy)
@settings(max_examples=50)
def test_smm_ratiomeasurement_instantiation(instance):
    assert isinstance(instance, smm_RatioMeasurement)

@given(instance=BinaryMeasure_strategy)
@settings(max_examples=50)
def test_binarymeasure_instantiation(instance):
    assert isinstance(instance, BinaryMeasure)

@given(instance=smm_RatioMeasure_strategy)
@settings(max_examples=50)
def test_smm_ratiomeasure_instantiation(instance):
    assert isinstance(instance, smm_RatioMeasure)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=smm_RankingInterval_strategy)
@settings(max_examples=50)
def test_smm_rankinginterval_instantiation(instance):
    assert isinstance(instance, smm_RankingInterval)



@given(instance=smm_RankingInterval_strategy)
def test_smm_rankinginterval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm_GradeInterval_strategy)
@settings(max_examples=50)
def test_smm_gradeinterval_instantiation(instance):
    assert isinstance(instance, smm_GradeInterval)



@given(instance=smm_GradeInterval_strategy)
def test_smm_gradeinterval_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=BaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_basemeasurerelationship_instantiation(instance):
    assert isinstance(instance, BaseMeasureRelationship)

@given(instance=smm_ScaledBaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_scaledbasemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_ScaledBaseMeasureRelationship)

@given(instance=smm_EObject_strategy)
@settings(max_examples=50)
def test_smm_eobject_instantiation(instance):
    assert isinstance(instance, smm_EObject)

@given(instance=smm_RescaledMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_rescaledmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RescaledMeasurementRelationship)

@given(instance=Measurement_strategy)
@settings(max_examples=50)
def test_measurement_instantiation(instance):
    assert isinstance(instance, Measurement)

@given(instance=smm_DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_smm_dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, smm_DimensionalMeasurement)



@given(instance=smm_DimensionalMeasurement_strategy)
def test_smm_dimensionalmeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm_RescaledMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_rescaledmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RescaledMeasureRelationship)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=smm_GradeMeasure_strategy)
@settings(max_examples=50)
def test_smm_grademeasure_instantiation(instance):
    assert isinstance(instance, smm_GradeMeasure)

@given(instance=smm_DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_smm_dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, smm_DimensionalMeasure)



@given(instance=smm_DimensionalMeasure_strategy)
def test_smm_dimensionalmeasure_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=smm_GradeMeasurement_strategy)
@settings(max_examples=50)
def test_smm_grademeasurement_instantiation(instance):
    assert isinstance(instance, smm_GradeMeasurement)



@given(instance=smm_GradeMeasurement_strategy)
def test_smm_grademeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=smm_GradeMeasurement_strategy)
def test_smm_grademeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_measurementrelationship_instantiation(instance):
    assert isinstance(instance, MeasurementRelationship)

@given(instance=smm_RefinementMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_refinementmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RefinementMeasurementRelationship)

@given(instance=smm_BaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_basemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_BaseMeasurementRelationship)

@given(instance=smm_EquivalentMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_equivalentmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_EquivalentMeasurementRelationship)

@given(instance=MeasureRelationship_strategy)
@settings(max_examples=50)
def test_measurerelationship_instantiation(instance):
    assert isinstance(instance, MeasureRelationship)

@given(instance=smm_RefinementMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_refinementmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RefinementMeasureRelationship)

@given(instance=smm_BaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_basemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_BaseMeasureRelationship)

@given(instance=smm_EquivalentMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_equivalentmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_EquivalentMeasureRelationship)

@given(instance=DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, DimensionalMeasurement)

@given(instance=smm_RankingMeasurement_strategy)
@settings(max_examples=50)
def test_smm_rankingmeasurement_instantiation(instance):
    assert isinstance(instance, smm_RankingMeasurement)



@given(instance=smm_RankingMeasurement_strategy)
def test_smm_rankingmeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm_RescaledMeasurement_strategy)
@settings(max_examples=50)
def test_smm_rescaledmeasurement_instantiation(instance):
    assert isinstance(instance, smm_RescaledMeasurement)



@given(instance=smm_RescaledMeasurement_strategy)
def test_smm_rescaledmeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm_NamedMeasurement_strategy)
@settings(max_examples=50)
def test_smm_namedmeasurement_instantiation(instance):
    assert isinstance(instance, smm_NamedMeasurement)

@given(instance=smm_DirectMeasurement_strategy)
@settings(max_examples=50)
def test_smm_directmeasurement_instantiation(instance):
    assert isinstance(instance, smm_DirectMeasurement)

@given(instance=smm_BinaryMeasurement_strategy)
@settings(max_examples=50)
def test_smm_binarymeasurement_instantiation(instance):
    assert isinstance(instance, smm_BinaryMeasurement)



@given(instance=smm_BinaryMeasurement_strategy)
def test_smm_binarymeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, DimensionalMeasure)

@given(instance=smm_RankingMeasure_strategy)
@settings(max_examples=50)
def test_smm_rankingmeasure_instantiation(instance):
    assert isinstance(instance, smm_RankingMeasure)

@given(instance=smm_DirectMeasure_strategy)
@settings(max_examples=50)
def test_smm_directmeasure_instantiation(instance):
    assert isinstance(instance, smm_DirectMeasure)

@given(instance=smm_RescaledMeasure_strategy)
@settings(max_examples=50)
def test_smm_rescaledmeasure_instantiation(instance):
    assert isinstance(instance, smm_RescaledMeasure)



@given(instance=smm_RescaledMeasure_strategy)
def test_smm_rescaledmeasure_multiplier_setter(instance):
    original = instance.multiplier
    instance.multiplier = original
    assert instance.multiplier == original



@given(instance=smm_RescaledMeasure_strategy)
def test_smm_rescaledmeasure_operationFirst_setter(instance):
    original = instance.operationFirst
    instance.operationFirst = original
    assert instance.operationFirst == original



@given(instance=smm_RescaledMeasure_strategy)
def test_smm_rescaledmeasure_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=smm_NamedMeasure_strategy)
@settings(max_examples=50)
def test_smm_namedmeasure_instantiation(instance):
    assert isinstance(instance, smm_NamedMeasure)

@given(instance=smm_BinaryMeasure_strategy)
@settings(max_examples=50)
def test_smm_binarymeasure_instantiation(instance):
    assert isinstance(instance, smm_BinaryMeasure)



@given(instance=smm_BinaryMeasure_strategy)
def test_smm_binarymeasure_functor_setter(instance):
    original = instance.functor
    instance.functor = original
    assert instance.functor == original

@given(instance=ScaledBaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_scaledbasemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, ScaledBaseMeasurementRelationship)

@given(instance=smm_BaseNMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_basenmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_BaseNMeasurementRelationship)

@given(instance=smm_Base2MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_base2measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_Base2MeasurementRelationship)

@given(instance=smm_RankingMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_rankingmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RankingMeasurementRelationship)

@given(instance=smm_GradeMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_grademeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_GradeMeasurementRelationship)

@given(instance=smm_Base1MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_base1measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_Base1MeasurementRelationship)

@given(instance=ScaledBaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_scaledbasemeasurerelationship_instantiation(instance):
    assert isinstance(instance, ScaledBaseMeasureRelationship)

@given(instance=smm_GradeMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_grademeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_GradeMeasureRelationship)

@given(instance=smm_RankingMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_rankingmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RankingMeasureRelationship)

@given(instance=smm_BaseNMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_basenmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_BaseNMeasureRelationship)

@given(instance=smm_Base2MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_base2measurerelationship_instantiation(instance):
    assert isinstance(instance, smm_Base2MeasureRelationship)

@given(instance=smm_Base1MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_base1measurerelationship_instantiation(instance):
    assert isinstance(instance, smm_Base1MeasureRelationship)

@given(instance=smm_CollectiveMeasurement_strategy)
@settings(max_examples=50)
def test_smm_collectivemeasurement_instantiation(instance):
    assert isinstance(instance, smm_CollectiveMeasurement)



@given(instance=smm_CollectiveMeasurement_strategy)
def test_smm_collectivemeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm_CollectiveMeasure_strategy)
@settings(max_examples=50)
def test_smm_collectivemeasure_instantiation(instance):
    assert isinstance(instance, smm_CollectiveMeasure)



@given(instance=smm_CollectiveMeasure_strategy)
def test_smm_collectivemeasure_accumulator_setter(instance):
    original = instance.accumulator
    instance.accumulator = original
    assert instance.accumulator == original

@given(instance=AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, AbstractMeasureElement)

@given(instance=smm_OCLOperation_strategy)
@settings(max_examples=50)
def test_smm_ocloperation_instantiation(instance):
    assert isinstance(instance, smm_OCLOperation)



@given(instance=smm_OCLOperation_strategy)
def test_smm_ocloperation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=smm_OCLOperation_strategy)
def test_smm_ocloperation_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=smm_Scope_strategy)
@settings(max_examples=50)
def test_smm_scope_instantiation(instance):
    assert isinstance(instance, smm_Scope)

@given(instance=smm_UnitOfMeasure_strategy)
@settings(max_examples=50)
def test_smm_unitofmeasure_instantiation(instance):
    assert isinstance(instance, smm_UnitOfMeasure)

@given(instance=smm_MeasureCategory_strategy)
@settings(max_examples=50)
def test_smm_measurecategory_instantiation(instance):
    assert isinstance(instance, smm_MeasureCategory)

@given(instance=smm_Operation_strategy)
@settings(max_examples=50)
def test_smm_operation_instantiation(instance):
    assert isinstance(instance, smm_Operation)



@given(instance=smm_Operation_strategy)
def test_smm_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=smm_Operation_strategy)
def test_smm_operation_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=smm_Measure_strategy)
@settings(max_examples=50)
def test_smm_measure_instantiation(instance):
    assert isinstance(instance, smm_Measure)



@given(instance=smm_Measure_strategy)
def test_smm_measure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=smm_Measure_strategy)
def test_smm_measure_measureLabelFormat_setter(instance):
    original = instance.measureLabelFormat
    instance.measureLabelFormat = original
    assert instance.measureLabelFormat == original



@given(instance=smm_Measure_strategy)
def test_smm_measure_measurementLabelFormat_setter(instance):
    original = instance.measurementLabelFormat
    instance.measurementLabelFormat = original
    assert instance.measurementLabelFormat == original



@given(instance=smm_Measure_strategy)
def test_smm_measure_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=smm_Measure_strategy)
def test_smm_measure_customScale_setter(instance):
    original = instance.customScale
    instance.customScale = original
    assert instance.customScale == original



@given(instance=smm_Measure_strategy)
def test_smm_measure_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=smm_Characteristic_strategy)
@settings(max_examples=50)
def test_smm_characteristic_instantiation(instance):
    assert isinstance(instance, smm_Characteristic)

@given(instance=SmmRelationship_strategy)
@settings(max_examples=50)
def test_smmrelationship_instantiation(instance):
    assert isinstance(instance, SmmRelationship)

@given(instance=smm_MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_measurerelationship_instantiation(instance):
    assert isinstance(instance, smm_MeasureRelationship)



@given(instance=smm_MeasureRelationship_strategy)
def test_smm_measurerelationship_influence_setter(instance):
    original = instance.influence
    instance.influence = original
    assert instance.influence == original

@given(instance=smm_MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_MeasurementRelationship)

@given(instance=smm_CategoryRelationship_strategy)
@settings(max_examples=50)
def test_smm_categoryrelationship_instantiation(instance):
    assert isinstance(instance, smm_CategoryRelationship)

@given(instance=SmmElement_strategy)
@settings(max_examples=50)
def test_smmelement_instantiation(instance):
    assert isinstance(instance, SmmElement)

@given(instance=smm_Attribute_strategy)
@settings(max_examples=50)
def test_smm_attribute_instantiation(instance):
    assert isinstance(instance, smm_Attribute)



@given(instance=smm_Attribute_strategy)
def test_smm_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=smm_Attribute_strategy)
def test_smm_attribute_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=smm_Argument_strategy)
@settings(max_examples=50)
def test_smm_argument_instantiation(instance):
    assert isinstance(instance, smm_Argument)



@given(instance=smm_Argument_strategy)
def test_smm_argument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=smm_Argument_strategy)
def test_smm_argument_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=smm_SmmModel_strategy)
@settings(max_examples=50)
def test_smm_smmmodel_instantiation(instance):
    assert isinstance(instance, smm_SmmModel)

@given(instance=smm_MeasureLibrary_strategy)
@settings(max_examples=50)
def test_smm_measurelibrary_instantiation(instance):
    assert isinstance(instance, smm_MeasureLibrary)

@given(instance=smm_Annotation_strategy)
@settings(max_examples=50)
def test_smm_annotation_instantiation(instance):
    assert isinstance(instance, smm_Annotation)



@given(instance=smm_Annotation_strategy)
def test_smm_annotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=smm_Observation_strategy)
@settings(max_examples=50)
def test_smm_observation_instantiation(instance):
    assert isinstance(instance, smm_Observation)



@given(instance=smm_Observation_strategy)
def test_smm_observation_whenObserved_setter(instance):
    original = instance.whenObserved
    instance.whenObserved = original
    assert instance.whenObserved == original



@given(instance=smm_Observation_strategy)
def test_smm_observation_observer_setter(instance):
    original = instance.observer
    instance.observer = original
    assert instance.observer == original



@given(instance=smm_Observation_strategy)
def test_smm_observation_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=smm_ObservedMeasure_strategy)
@settings(max_examples=50)
def test_smm_observedmeasure_instantiation(instance):
    assert isinstance(instance, smm_ObservedMeasure)

@given(instance=smm_Interval_strategy)
@settings(max_examples=50)
def test_smm_interval_instantiation(instance):
    assert isinstance(instance, smm_Interval)



@given(instance=smm_Interval_strategy)
def test_smm_interval_maximumOpen_setter(instance):
    original = instance.maximumOpen
    instance.maximumOpen = original
    assert instance.maximumOpen == original



@given(instance=smm_Interval_strategy)
def test_smm_interval_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=smm_Interval_strategy)
def test_smm_interval_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=smm_Interval_strategy)
def test_smm_interval_minimumOpen_setter(instance):
    original = instance.minimumOpen
    instance.minimumOpen = original
    assert instance.minimumOpen == original

@given(instance=smm_ObservationScope_strategy)
@settings(max_examples=50)
def test_smm_observationscope_instantiation(instance):
    assert isinstance(instance, smm_ObservationScope)



@given(instance=smm_ObservationScope_strategy)
def test_smm_observationscope_scopeUri_setter(instance):
    original = instance.scopeUri
    instance.scopeUri = original
    assert instance.scopeUri == original

@given(instance=smm_Measurement_strategy)
@settings(max_examples=50)
def test_smm_measurement_instantiation(instance):
    assert isinstance(instance, smm_Measurement)



@given(instance=smm_Measurement_strategy)
def test_smm_measurement_breakValue_setter(instance):
    original = instance.breakValue
    instance.breakValue = original
    assert instance.breakValue == original



@given(instance=smm_Measurement_strategy)
def test_smm_measurement_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=smm_SmmRelationship_strategy)
@settings(max_examples=50)
def test_smm_smmrelationship_instantiation(instance):
    assert isinstance(instance, smm_SmmRelationship)

@given(instance=smm_AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_smm_abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, smm_AbstractMeasureElement)
