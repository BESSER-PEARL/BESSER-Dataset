import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Measurement,
    smm_Grade,
    Measure,
    DirectMeasure,
    smm_Counting,
    DirectMeasurement,
    smm_Count,
    AbstractMeasureElement,
    smm_Scope,
    smm_Operation,
    smm_Measure,
    BinaryMeasurement,
    smm_RatioMeasurement,
    BinaryMeasure,
    smm_RatioMeasure,
    smm_OCLOperation,
    smm_SmmElement,
    smm_Ranking,
    smm_EObject,
    smm_Characteristic,
    smm_MeasureCategory,
    SmmRelationship,
    smm_ObservedMeasure,
    smm_MeasureRelationship,
    smm_MeasurementRelationship,
    DimensionalMeasure,
    smm_RescaledMeasure,
    smm_DirectMeasure,
    smm_NamedMeasure,
    smm_CollectiveMeasure,
    smm_DimensionalMeasure,
    smm_BinaryMeasure,
    MeasureRelationship,
    smm_RecursiveMeasureRelationship,
    smm_EquivalentMeasureRelationship,
    smm_RankingMeasureRelationship,
    smm_BaseMeasureRelationship,
    smm_RefinementMeasureRelationship,
    smm_RescaleMeasureRelationship,
    smm_Base2MeasureRelationship,
    smm_Base1MeasureRelationship,
    MeasurementRelationship,
    smm_RescaleMeasurementRelationship,
    smm_Base2MeasurementRelationship,
    smm_BaseMeasurementRelationship,
    smm_RankingMeasurementRelationship,
    smm_RecursiveMeasurementRelationship,
    smm_RefinementMeasurementRelationship,
    smm_EquivalentMeasurementRelationship,
    smm_Base1MeasurementRelationship,
    smm_DimensionalMeasurement,
    DimensionalMeasurement,
    smm_DirectMeasurement,
    smm_RescaledMeasurement,
    smm_CollectiveMeasurement,
    smm_BinaryMeasurement,
    smm_NamedMeasurement,
    smm_AggregatedMeasurement,
    smm_CategoryRelationship,
    SmmElement,
    smm_SmmRelationship,
    smm_Observation,
    smm_ObservationScope,
    smm_Attribute,
    smm_Measurement,
    smm_Argument,
    smm_SmmModel,
    smm_MeasureLibrary,
    smm_Annotation,
    smm_RankingInterval,
    smm_AbstractMeasureElement,
    Accumulator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_measurement_is_not_abstract():
    assert not inspect.isabstract(Measurement)


def test_measurement_constructor_exists():
    assert callable(Measurement.__init__)


def test_measurement_constructor_args():
    sig = inspect.signature(Measurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_grade_is_not_abstract():
    assert not inspect.isabstract(smm_Grade)


def test_smm_grade_constructor_exists():
    assert callable(smm_Grade.__init__)


def test_smm_grade_constructor_args():
    sig = inspect.signature(smm_Grade.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"
    assert "value" in params, "Missing parameter 'value'"

def test_smm_grade_has_isBaseSupplied():
    assert hasattr(smm_Grade, "isBaseSupplied")
    descriptor = None
    for klass in smm_Grade.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)

def test_smm_grade_has_value():
    assert hasattr(smm_Grade, "value")
    descriptor = None
    for klass in smm_Grade.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_directmeasure_is_not_abstract():
    assert not inspect.isabstract(DirectMeasure)


def test_directmeasure_constructor_exists():
    assert callable(DirectMeasure.__init__)


def test_directmeasure_constructor_args():
    sig = inspect.signature(DirectMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_counting_is_not_abstract():
    assert not inspect.isabstract(smm_Counting)


def test_smm_counting_constructor_exists():
    assert callable(smm_Counting.__init__)


def test_smm_counting_constructor_args():
    sig = inspect.signature(smm_Counting.__init__)
    params = list(sig.parameters.keys())



def test_directmeasurement_is_not_abstract():
    assert not inspect.isabstract(DirectMeasurement)


def test_directmeasurement_constructor_exists():
    assert callable(DirectMeasurement.__init__)


def test_directmeasurement_constructor_args():
    sig = inspect.signature(DirectMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_count_is_not_abstract():
    assert not inspect.isabstract(smm_Count)


def test_smm_count_constructor_exists():
    assert callable(smm_Count.__init__)


def test_smm_count_constructor_args():
    sig = inspect.signature(smm_Count.__init__)
    params = list(sig.parameters.keys())



def test_abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(AbstractMeasureElement)


def test_abstractmeasureelement_constructor_exists():
    assert callable(AbstractMeasureElement.__init__)


def test_abstractmeasureelement_constructor_args():
    sig = inspect.signature(AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())



def test_smm_scope_is_not_abstract():
    assert not inspect.isabstract(smm_Scope)


def test_smm_scope_constructor_exists():
    assert callable(smm_Scope.__init__)


def test_smm_scope_constructor_args():
    sig = inspect.signature(smm_Scope.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_smm_scope_has_class_():
    assert hasattr(smm_Scope, "class_")
    descriptor = None
    for klass in smm_Scope.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_smm_operation_is_not_abstract():
    assert not inspect.isabstract(smm_Operation)


def test_smm_operation_constructor_exists():
    assert callable(smm_Operation.__init__)


def test_smm_operation_constructor_args():
    sig = inspect.signature(smm_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_smm_operation_has_language():
    assert hasattr(smm_Operation, "language")
    descriptor = None
    for klass in smm_Operation.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_smm_operation_has_body():
    assert hasattr(smm_Operation, "body")
    descriptor = None
    for klass in smm_Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
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
    assert "measurementLabelFormat" in params, "Missing parameter 'measurementLabelFormat'"
    assert "measureLabelFormat" in params, "Missing parameter 'measureLabelFormat'"

def test_smm_measure_has_visible():
    assert hasattr(smm_Measure, "visible")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
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

def test_smm_measure_has_measureLabelFormat():
    assert hasattr(smm_Measure, "measureLabelFormat")
    descriptor = None
    for klass in smm_Measure.__mro__:
        if "measureLabelFormat" in klass.__dict__:
            descriptor = klass.__dict__["measureLabelFormat"]
            break
    assert isinstance(descriptor, property)



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



def test_smm_smmelement_is_not_abstract():
    assert not inspect.isabstract(smm_SmmElement)


def test_smm_smmelement_constructor_exists():
    assert callable(smm_SmmElement.__init__)


def test_smm_smmelement_constructor_args():
    sig = inspect.signature(smm_SmmElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "shortDescription" in params, "Missing parameter 'shortDescription'"

def test_smm_smmelement_has_name():
    assert hasattr(smm_SmmElement, "name")
    descriptor = None
    for klass in smm_SmmElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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



def test_smm_ranking_is_not_abstract():
    assert not inspect.isabstract(smm_Ranking)


def test_smm_ranking_constructor_exists():
    assert callable(smm_Ranking.__init__)


def test_smm_ranking_constructor_args():
    sig = inspect.signature(smm_Ranking.__init__)
    params = list(sig.parameters.keys())



def test_smm_eobject_is_not_abstract():
    assert not inspect.isabstract(smm_EObject)


def test_smm_eobject_constructor_exists():
    assert callable(smm_EObject.__init__)


def test_smm_eobject_constructor_args():
    sig = inspect.signature(smm_EObject.__init__)
    params = list(sig.parameters.keys())



def test_smm_characteristic_is_not_abstract():
    assert not inspect.isabstract(smm_Characteristic)


def test_smm_characteristic_constructor_exists():
    assert callable(smm_Characteristic.__init__)


def test_smm_characteristic_constructor_args():
    sig = inspect.signature(smm_Characteristic.__init__)
    params = list(sig.parameters.keys())



def test_smm_measurecategory_is_not_abstract():
    assert not inspect.isabstract(smm_MeasureCategory)


def test_smm_measurecategory_constructor_exists():
    assert callable(smm_MeasureCategory.__init__)


def test_smm_measurecategory_constructor_args():
    sig = inspect.signature(smm_MeasureCategory.__init__)
    params = list(sig.parameters.keys())



def test_smmrelationship_is_not_abstract():
    assert not inspect.isabstract(SmmRelationship)


def test_smmrelationship_constructor_exists():
    assert callable(SmmRelationship.__init__)


def test_smmrelationship_constructor_args():
    sig = inspect.signature(SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_observedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_ObservedMeasure)


def test_smm_observedmeasure_constructor_exists():
    assert callable(smm_ObservedMeasure.__init__)


def test_smm_observedmeasure_constructor_args():
    sig = inspect.signature(smm_ObservedMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_MeasureRelationship)


def test_smm_measurerelationship_constructor_exists():
    assert callable(smm_MeasureRelationship.__init__)


def test_smm_measurerelationship_constructor_args():
    sig = inspect.signature(smm_MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_MeasurementRelationship)


def test_smm_measurementrelationship_constructor_exists():
    assert callable(smm_MeasurementRelationship.__init__)


def test_smm_measurementrelationship_constructor_args():
    sig = inspect.signature(smm_MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasure)


def test_dimensionalmeasure_constructor_exists():
    assert callable(DimensionalMeasure.__init__)


def test_dimensionalmeasure_constructor_args():
    sig = inspect.signature(DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_rescaledmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_RescaledMeasure)


def test_smm_rescaledmeasure_constructor_exists():
    assert callable(smm_RescaledMeasure.__init__)


def test_smm_rescaledmeasure_constructor_args():
    sig = inspect.signature(smm_RescaledMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"

def test_smm_rescaledmeasure_has_formula():
    assert hasattr(smm_RescaledMeasure, "formula")
    descriptor = None
    for klass in smm_RescaledMeasure.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_smm_directmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_DirectMeasure)


def test_smm_directmeasure_constructor_exists():
    assert callable(smm_DirectMeasure.__init__)


def test_smm_directmeasure_constructor_args():
    sig = inspect.signature(smm_DirectMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm_namedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_NamedMeasure)


def test_smm_namedmeasure_constructor_exists():
    assert callable(smm_NamedMeasure.__init__)


def test_smm_namedmeasure_constructor_args():
    sig = inspect.signature(smm_NamedMeasure.__init__)
    params = list(sig.parameters.keys())



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



def test_smm_dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(smm_DimensionalMeasure)


def test_smm_dimensionalmeasure_constructor_exists():
    assert callable(smm_DimensionalMeasure.__init__)


def test_smm_dimensionalmeasure_constructor_args():
    sig = inspect.signature(smm_DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_smm_dimensionalmeasure_has_unit():
    assert hasattr(smm_DimensionalMeasure, "unit")
    descriptor = None
    for klass in smm_DimensionalMeasure.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



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



def test_measurerelationship_is_not_abstract():
    assert not inspect.isabstract(MeasureRelationship)


def test_measurerelationship_constructor_exists():
    assert callable(MeasureRelationship.__init__)


def test_measurerelationship_constructor_args():
    sig = inspect.signature(MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_recursivemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RecursiveMeasureRelationship)


def test_smm_recursivemeasurerelationship_constructor_exists():
    assert callable(smm_RecursiveMeasureRelationship.__init__)


def test_smm_recursivemeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RecursiveMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_equivalentmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_EquivalentMeasureRelationship)


def test_smm_equivalentmeasurerelationship_constructor_exists():
    assert callable(smm_EquivalentMeasureRelationship.__init__)


def test_smm_equivalentmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_EquivalentMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankingmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RankingMeasureRelationship)


def test_smm_rankingmeasurerelationship_constructor_exists():
    assert callable(smm_RankingMeasureRelationship.__init__)


def test_smm_rankingmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RankingMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_basemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_BaseMeasureRelationship)


def test_smm_basemeasurerelationship_constructor_exists():
    assert callable(smm_BaseMeasureRelationship.__init__)


def test_smm_basemeasurerelationship_constructor_args():
    sig = inspect.signature(smm_BaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_refinementmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RefinementMeasureRelationship)


def test_smm_refinementmeasurerelationship_constructor_exists():
    assert callable(smm_RefinementMeasureRelationship.__init__)


def test_smm_refinementmeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RefinementMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_rescalemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RescaleMeasureRelationship)


def test_smm_rescalemeasurerelationship_constructor_exists():
    assert callable(smm_RescaleMeasureRelationship.__init__)


def test_smm_rescalemeasurerelationship_constructor_args():
    sig = inspect.signature(smm_RescaleMeasureRelationship.__init__)
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



def test_measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(MeasurementRelationship)


def test_measurementrelationship_constructor_exists():
    assert callable(MeasurementRelationship.__init__)


def test_measurementrelationship_constructor_args():
    sig = inspect.signature(MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_rescalemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RescaleMeasurementRelationship)


def test_smm_rescalemeasurementrelationship_constructor_exists():
    assert callable(smm_RescaleMeasurementRelationship.__init__)


def test_smm_rescalemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RescaleMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_base2measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_Base2MeasurementRelationship)


def test_smm_base2measurementrelationship_constructor_exists():
    assert callable(smm_Base2MeasurementRelationship.__init__)


def test_smm_base2measurementrelationship_constructor_args():
    sig = inspect.signature(smm_Base2MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_basemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_BaseMeasurementRelationship)


def test_smm_basemeasurementrelationship_constructor_exists():
    assert callable(smm_BaseMeasurementRelationship.__init__)


def test_smm_basemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_BaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_rankingmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RankingMeasurementRelationship)


def test_smm_rankingmeasurementrelationship_constructor_exists():
    assert callable(smm_RankingMeasurementRelationship.__init__)


def test_smm_rankingmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RankingMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_recursivemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RecursiveMeasurementRelationship)


def test_smm_recursivemeasurementrelationship_constructor_exists():
    assert callable(smm_RecursiveMeasurementRelationship.__init__)


def test_smm_recursivemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RecursiveMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_refinementmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_RefinementMeasurementRelationship)


def test_smm_refinementmeasurementrelationship_constructor_exists():
    assert callable(smm_RefinementMeasurementRelationship.__init__)


def test_smm_refinementmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_RefinementMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_equivalentmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_EquivalentMeasurementRelationship)


def test_smm_equivalentmeasurementrelationship_constructor_exists():
    assert callable(smm_EquivalentMeasurementRelationship.__init__)


def test_smm_equivalentmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm_EquivalentMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_base1measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_Base1MeasurementRelationship)


def test_smm_base1measurementrelationship_constructor_exists():
    assert callable(smm_Base1MeasurementRelationship.__init__)


def test_smm_base1measurementrelationship_constructor_args():
    sig = inspect.signature(smm_Base1MeasurementRelationship.__init__)
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



def test_dimensionalmeasurement_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasurement)


def test_dimensionalmeasurement_constructor_exists():
    assert callable(DimensionalMeasurement.__init__)


def test_dimensionalmeasurement_constructor_args():
    sig = inspect.signature(DimensionalMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_directmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_DirectMeasurement)


def test_smm_directmeasurement_constructor_exists():
    assert callable(smm_DirectMeasurement.__init__)


def test_smm_directmeasurement_constructor_args():
    sig = inspect.signature(smm_DirectMeasurement.__init__)
    params = list(sig.parameters.keys())



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



def test_smm_collectivemeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_CollectiveMeasurement)


def test_smm_collectivemeasurement_constructor_exists():
    assert callable(smm_CollectiveMeasurement.__init__)


def test_smm_collectivemeasurement_constructor_args():
    sig = inspect.signature(smm_CollectiveMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "accumulator" in params, "Missing parameter 'accumulator'"
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm_collectivemeasurement_has_accumulator():
    assert hasattr(smm_CollectiveMeasurement, "accumulator")
    descriptor = None
    for klass in smm_CollectiveMeasurement.__mro__:
        if "accumulator" in klass.__dict__:
            descriptor = klass.__dict__["accumulator"]
            break
    assert isinstance(descriptor, property)

def test_smm_collectivemeasurement_has_isBaseSupplied():
    assert hasattr(smm_CollectiveMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm_CollectiveMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



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



def test_smm_namedmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_NamedMeasurement)


def test_smm_namedmeasurement_constructor_exists():
    assert callable(smm_NamedMeasurement.__init__)


def test_smm_namedmeasurement_constructor_args():
    sig = inspect.signature(smm_NamedMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm_aggregatedmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm_AggregatedMeasurement)


def test_smm_aggregatedmeasurement_constructor_exists():
    assert callable(smm_AggregatedMeasurement.__init__)


def test_smm_aggregatedmeasurement_constructor_args():
    sig = inspect.signature(smm_AggregatedMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSuppled" in params, "Missing parameter 'isBaseSuppled'"

def test_smm_aggregatedmeasurement_has_isBaseSuppled():
    assert hasattr(smm_AggregatedMeasurement, "isBaseSuppled")
    descriptor = None
    for klass in smm_AggregatedMeasurement.__mro__:
        if "isBaseSuppled" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSuppled"]
            break
    assert isinstance(descriptor, property)



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



def test_smm_smmrelationship_is_not_abstract():
    assert not inspect.isabstract(smm_SmmRelationship)


def test_smm_smmrelationship_constructor_exists():
    assert callable(smm_SmmRelationship.__init__)


def test_smm_smmrelationship_constructor_args():
    sig = inspect.signature(smm_SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm_observation_is_not_abstract():
    assert not inspect.isabstract(smm_Observation)


def test_smm_observation_constructor_exists():
    assert callable(smm_Observation.__init__)


def test_smm_observation_constructor_args():
    sig = inspect.signature(smm_Observation.__init__)
    params = list(sig.parameters.keys())
    assert "observer" in params, "Missing parameter 'observer'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "whenObserved" in params, "Missing parameter 'whenObserved'"

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

def test_smm_observation_has_whenObserved():
    assert hasattr(smm_Observation, "whenObserved")
    descriptor = None
    for klass in smm_Observation.__mro__:
        if "whenObserved" in klass.__dict__:
            descriptor = klass.__dict__["whenObserved"]
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



def test_smm_measurement_is_not_abstract():
    assert not inspect.isabstract(smm_Measurement)


def test_smm_measurement_constructor_exists():
    assert callable(smm_Measurement.__init__)


def test_smm_measurement_constructor_args():
    sig = inspect.signature(smm_Measurement.__init__)
    params = list(sig.parameters.keys())
    assert "error" in params, "Missing parameter 'error'"
    assert "breakValue" in params, "Missing parameter 'breakValue'"

def test_smm_measurement_has_error():
    assert hasattr(smm_Measurement, "error")
    descriptor = None
    for klass in smm_Measurement.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_smm_measurement_has_breakValue():
    assert hasattr(smm_Measurement, "breakValue")
    descriptor = None
    for klass in smm_Measurement.__mro__:
        if "breakValue" in klass.__dict__:
            descriptor = klass.__dict__["breakValue"]
            break
    assert isinstance(descriptor, property)



def test_smm_argument_is_not_abstract():
    assert not inspect.isabstract(smm_Argument)


def test_smm_argument_constructor_exists():
    assert callable(smm_Argument.__init__)


def test_smm_argument_constructor_args():
    sig = inspect.signature(smm_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_smm_argument_has_type():
    assert hasattr(smm_Argument, "type")
    descriptor = None
    for klass in smm_Argument.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_smm_argument_has_value():
    assert hasattr(smm_Argument, "value")
    descriptor = None
    for klass in smm_Argument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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



def test_smm_rankinginterval_is_not_abstract():
    assert not inspect.isabstract(smm_RankingInterval)


def test_smm_rankinginterval_constructor_exists():
    assert callable(smm_RankingInterval.__init__)


def test_smm_rankinginterval_constructor_args():
    sig = inspect.signature(smm_RankingInterval.__init__)
    params = list(sig.parameters.keys())
    assert "minimumOpen" in params, "Missing parameter 'minimumOpen'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "maximumOpen" in params, "Missing parameter 'maximumOpen'"
    assert "maximumEndpoint" in params, "Missing parameter 'maximumEndpoint'"
    assert "minimumEndpoint" in params, "Missing parameter 'minimumEndpoint'"

def test_smm_rankinginterval_has_minimumOpen():
    assert hasattr(smm_RankingInterval, "minimumOpen")
    descriptor = None
    for klass in smm_RankingInterval.__mro__:
        if "minimumOpen" in klass.__dict__:
            descriptor = klass.__dict__["minimumOpen"]
            break
    assert isinstance(descriptor, property)

def test_smm_rankinginterval_has_symbol():
    assert hasattr(smm_RankingInterval, "symbol")
    descriptor = None
    for klass in smm_RankingInterval.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_smm_rankinginterval_has_maximumOpen():
    assert hasattr(smm_RankingInterval, "maximumOpen")
    descriptor = None
    for klass in smm_RankingInterval.__mro__:
        if "maximumOpen" in klass.__dict__:
            descriptor = klass.__dict__["maximumOpen"]
            break
    assert isinstance(descriptor, property)

def test_smm_rankinginterval_has_maximumEndpoint():
    assert hasattr(smm_RankingInterval, "maximumEndpoint")
    descriptor = None
    for klass in smm_RankingInterval.__mro__:
        if "maximumEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["maximumEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_smm_rankinginterval_has_minimumEndpoint():
    assert hasattr(smm_RankingInterval, "minimumEndpoint")
    descriptor = None
    for klass in smm_RankingInterval.__mro__:
        if "minimumEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["minimumEndpoint"]
            break
    assert isinstance(descriptor, property)



def test_smm_abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(smm_AbstractMeasureElement)


def test_smm_abstractmeasureelement_constructor_exists():
    assert callable(smm_AbstractMeasureElement.__init__)


def test_smm_abstractmeasureelement_constructor_args():
    sig = inspect.signature(smm_AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())

def test_accumulator_exists():
    # Check that the Enumeration exists
    assert Accumulator is not None

def test_accumulator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Accumulator]
    expected_literals = [
        "standardDeviation",
        "average",
        "minimum",
        "maximum",
        "sum",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Accumulator"


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
Measurement_strategy = st.builds(
    Measurement,
)
smm_Grade_strategy = st.builds(
    smm_Grade,
    isBaseSupplied=
        st.booleans(),
    value=
        safe_text
)
Measure_strategy = st.builds(
    Measure,
)
DirectMeasure_strategy = st.builds(
    DirectMeasure,
)
smm_Counting_strategy = st.builds(
    smm_Counting,
)
DirectMeasurement_strategy = st.builds(
    DirectMeasurement,
)
smm_Count_strategy = st.builds(
    smm_Count,
)
AbstractMeasureElement_strategy = st.builds(
    AbstractMeasureElement,
)
smm_Scope_strategy = st.builds(
    smm_Scope,
    class_=
        safe_text
)
smm_Operation_strategy = st.builds(
    smm_Operation,
    language=
        safe_text,
    body=
        safe_text
)
smm_Measure_strategy = st.builds(
    smm_Measure,
    visible=
        st.booleans(),
    measurementLabelFormat=
        safe_text,
    measureLabelFormat=
        safe_text
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
smm_OCLOperation_strategy = st.builds(
    smm_OCLOperation,
    body=
        safe_text,
    context=
        safe_text
)
smm_SmmElement_strategy = st.builds(
    smm_SmmElement,
    name=
        safe_text,
    description=
        safe_text,
    shortDescription=
        safe_text
)
smm_Ranking_strategy = st.builds(
    smm_Ranking,
)
smm_EObject_strategy = st.builds(
    smm_EObject,
)
smm_Characteristic_strategy = st.builds(
    smm_Characteristic,
)
smm_MeasureCategory_strategy = st.builds(
    smm_MeasureCategory,
)
SmmRelationship_strategy = st.builds(
    SmmRelationship,
)
smm_ObservedMeasure_strategy = st.builds(
    smm_ObservedMeasure,
)
smm_MeasureRelationship_strategy = st.builds(
    smm_MeasureRelationship,
)
smm_MeasurementRelationship_strategy = st.builds(
    smm_MeasurementRelationship,
)
DimensionalMeasure_strategy = st.builds(
    DimensionalMeasure,
)
smm_RescaledMeasure_strategy = st.builds(
    smm_RescaledMeasure,
    formula=
        safe_text
)
smm_DirectMeasure_strategy = st.builds(
    smm_DirectMeasure,
)
smm_NamedMeasure_strategy = st.builds(
    smm_NamedMeasure,
)
smm_CollectiveMeasure_strategy = st.builds(
    smm_CollectiveMeasure,
    accumulator=
        safe_text
)
smm_DimensionalMeasure_strategy = st.builds(
    smm_DimensionalMeasure,
    unit=
        safe_text
)
smm_BinaryMeasure_strategy = st.builds(
    smm_BinaryMeasure,
    functor=
        safe_text
)
MeasureRelationship_strategy = st.builds(
    MeasureRelationship,
)
smm_RecursiveMeasureRelationship_strategy = st.builds(
    smm_RecursiveMeasureRelationship,
)
smm_EquivalentMeasureRelationship_strategy = st.builds(
    smm_EquivalentMeasureRelationship,
)
smm_RankingMeasureRelationship_strategy = st.builds(
    smm_RankingMeasureRelationship,
)
smm_BaseMeasureRelationship_strategy = st.builds(
    smm_BaseMeasureRelationship,
)
smm_RefinementMeasureRelationship_strategy = st.builds(
    smm_RefinementMeasureRelationship,
)
smm_RescaleMeasureRelationship_strategy = st.builds(
    smm_RescaleMeasureRelationship,
)
smm_Base2MeasureRelationship_strategy = st.builds(
    smm_Base2MeasureRelationship,
)
smm_Base1MeasureRelationship_strategy = st.builds(
    smm_Base1MeasureRelationship,
)
MeasurementRelationship_strategy = st.builds(
    MeasurementRelationship,
)
smm_RescaleMeasurementRelationship_strategy = st.builds(
    smm_RescaleMeasurementRelationship,
)
smm_Base2MeasurementRelationship_strategy = st.builds(
    smm_Base2MeasurementRelationship,
)
smm_BaseMeasurementRelationship_strategy = st.builds(
    smm_BaseMeasurementRelationship,
)
smm_RankingMeasurementRelationship_strategy = st.builds(
    smm_RankingMeasurementRelationship,
)
smm_RecursiveMeasurementRelationship_strategy = st.builds(
    smm_RecursiveMeasurementRelationship,
)
smm_RefinementMeasurementRelationship_strategy = st.builds(
    smm_RefinementMeasurementRelationship,
)
smm_EquivalentMeasurementRelationship_strategy = st.builds(
    smm_EquivalentMeasurementRelationship,
)
smm_Base1MeasurementRelationship_strategy = st.builds(
    smm_Base1MeasurementRelationship,
)
smm_DimensionalMeasurement_strategy = st.builds(
    smm_DimensionalMeasurement,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
DimensionalMeasurement_strategy = st.builds(
    DimensionalMeasurement,
)
smm_DirectMeasurement_strategy = st.builds(
    smm_DirectMeasurement,
)
smm_RescaledMeasurement_strategy = st.builds(
    smm_RescaledMeasurement,
    isBaseSupplied=
        st.booleans()
)
smm_CollectiveMeasurement_strategy = st.builds(
    smm_CollectiveMeasurement,
    accumulator=
        safe_text,
    isBaseSupplied=
        st.booleans()
)
smm_BinaryMeasurement_strategy = st.builds(
    smm_BinaryMeasurement,
    isBaseSupplied=
        st.booleans()
)
smm_NamedMeasurement_strategy = st.builds(
    smm_NamedMeasurement,
)
smm_AggregatedMeasurement_strategy = st.builds(
    smm_AggregatedMeasurement,
    isBaseSuppled=
        st.booleans()
)
smm_CategoryRelationship_strategy = st.builds(
    smm_CategoryRelationship,
)
SmmElement_strategy = st.builds(
    SmmElement,
)
smm_SmmRelationship_strategy = st.builds(
    smm_SmmRelationship,
)
smm_Observation_strategy = st.builds(
    smm_Observation,
    observer=
        safe_text,
    tool=
        safe_text,
    whenObserved=
        safe_text
)
smm_ObservationScope_strategy = st.builds(
    smm_ObservationScope,
    scopeUri=
        safe_text
)
smm_Attribute_strategy = st.builds(
    smm_Attribute,
    value=
        safe_text,
    tag=
        safe_text
)
smm_Measurement_strategy = st.builds(
    smm_Measurement,
    error=
        safe_text,
    breakValue=
        safe_text
)
smm_Argument_strategy = st.builds(
    smm_Argument,
    type=
        safe_text,
    value=
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
smm_RankingInterval_strategy = st.builds(
    smm_RankingInterval,
    minimumOpen=
        st.booleans(),
    symbol=
        safe_text,
    maximumOpen=
        st.booleans(),
    maximumEndpoint=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimumEndpoint=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm_AbstractMeasureElement_strategy = st.builds(
    smm_AbstractMeasureElement,
)

@given(instance=Measurement_strategy)
@settings(max_examples=50)
def test_measurement_instantiation(instance):
    assert isinstance(instance, Measurement)

@given(instance=smm_Grade_strategy)
@settings(max_examples=50)
def test_smm_grade_instantiation(instance):
    assert isinstance(instance, smm_Grade)



@given(instance=smm_Grade_strategy)
def test_smm_grade_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original



@given(instance=smm_Grade_strategy)
def test_smm_grade_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=DirectMeasure_strategy)
@settings(max_examples=50)
def test_directmeasure_instantiation(instance):
    assert isinstance(instance, DirectMeasure)

@given(instance=smm_Counting_strategy)
@settings(max_examples=50)
def test_smm_counting_instantiation(instance):
    assert isinstance(instance, smm_Counting)

@given(instance=DirectMeasurement_strategy)
@settings(max_examples=50)
def test_directmeasurement_instantiation(instance):
    assert isinstance(instance, DirectMeasurement)

@given(instance=smm_Count_strategy)
@settings(max_examples=50)
def test_smm_count_instantiation(instance):
    assert isinstance(instance, smm_Count)

@given(instance=AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, AbstractMeasureElement)

@given(instance=smm_Scope_strategy)
@settings(max_examples=50)
def test_smm_scope_instantiation(instance):
    assert isinstance(instance, smm_Scope)



@given(instance=smm_Scope_strategy)
def test_smm_scope_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=smm_Operation_strategy)
@settings(max_examples=50)
def test_smm_operation_instantiation(instance):
    assert isinstance(instance, smm_Operation)



@given(instance=smm_Operation_strategy)
def test_smm_operation_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=smm_Operation_strategy)
def test_smm_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

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
def test_smm_measure_measurementLabelFormat_setter(instance):
    original = instance.measurementLabelFormat
    instance.measurementLabelFormat = original
    assert instance.measurementLabelFormat == original



@given(instance=smm_Measure_strategy)
def test_smm_measure_measureLabelFormat_setter(instance):
    original = instance.measureLabelFormat
    instance.measureLabelFormat = original
    assert instance.measureLabelFormat == original

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

@given(instance=smm_SmmElement_strategy)
@settings(max_examples=50)
def test_smm_smmelement_instantiation(instance):
    assert isinstance(instance, smm_SmmElement)



@given(instance=smm_SmmElement_strategy)
def test_smm_smmelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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

@given(instance=smm_Ranking_strategy)
@settings(max_examples=50)
def test_smm_ranking_instantiation(instance):
    assert isinstance(instance, smm_Ranking)

@given(instance=smm_EObject_strategy)
@settings(max_examples=50)
def test_smm_eobject_instantiation(instance):
    assert isinstance(instance, smm_EObject)

@given(instance=smm_Characteristic_strategy)
@settings(max_examples=50)
def test_smm_characteristic_instantiation(instance):
    assert isinstance(instance, smm_Characteristic)

@given(instance=smm_MeasureCategory_strategy)
@settings(max_examples=50)
def test_smm_measurecategory_instantiation(instance):
    assert isinstance(instance, smm_MeasureCategory)

@given(instance=SmmRelationship_strategy)
@settings(max_examples=50)
def test_smmrelationship_instantiation(instance):
    assert isinstance(instance, SmmRelationship)

@given(instance=smm_ObservedMeasure_strategy)
@settings(max_examples=50)
def test_smm_observedmeasure_instantiation(instance):
    assert isinstance(instance, smm_ObservedMeasure)

@given(instance=smm_MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_measurerelationship_instantiation(instance):
    assert isinstance(instance, smm_MeasureRelationship)

@given(instance=smm_MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_MeasurementRelationship)

@given(instance=DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, DimensionalMeasure)

@given(instance=smm_RescaledMeasure_strategy)
@settings(max_examples=50)
def test_smm_rescaledmeasure_instantiation(instance):
    assert isinstance(instance, smm_RescaledMeasure)



@given(instance=smm_RescaledMeasure_strategy)
def test_smm_rescaledmeasure_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=smm_DirectMeasure_strategy)
@settings(max_examples=50)
def test_smm_directmeasure_instantiation(instance):
    assert isinstance(instance, smm_DirectMeasure)

@given(instance=smm_NamedMeasure_strategy)
@settings(max_examples=50)
def test_smm_namedmeasure_instantiation(instance):
    assert isinstance(instance, smm_NamedMeasure)

@given(instance=smm_CollectiveMeasure_strategy)
@settings(max_examples=50)
def test_smm_collectivemeasure_instantiation(instance):
    assert isinstance(instance, smm_CollectiveMeasure)



@given(instance=smm_CollectiveMeasure_strategy)
def test_smm_collectivemeasure_accumulator_setter(instance):
    original = instance.accumulator
    instance.accumulator = original
    assert instance.accumulator == original

@given(instance=smm_DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_smm_dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, smm_DimensionalMeasure)



@given(instance=smm_DimensionalMeasure_strategy)
def test_smm_dimensionalmeasure_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=smm_BinaryMeasure_strategy)
@settings(max_examples=50)
def test_smm_binarymeasure_instantiation(instance):
    assert isinstance(instance, smm_BinaryMeasure)



@given(instance=smm_BinaryMeasure_strategy)
def test_smm_binarymeasure_functor_setter(instance):
    original = instance.functor
    instance.functor = original
    assert instance.functor == original

@given(instance=MeasureRelationship_strategy)
@settings(max_examples=50)
def test_measurerelationship_instantiation(instance):
    assert isinstance(instance, MeasureRelationship)

@given(instance=smm_RecursiveMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_recursivemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RecursiveMeasureRelationship)

@given(instance=smm_EquivalentMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_equivalentmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_EquivalentMeasureRelationship)

@given(instance=smm_RankingMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_rankingmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RankingMeasureRelationship)

@given(instance=smm_BaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_basemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_BaseMeasureRelationship)

@given(instance=smm_RefinementMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_refinementmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RefinementMeasureRelationship)

@given(instance=smm_RescaleMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_rescalemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm_RescaleMeasureRelationship)

@given(instance=smm_Base2MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_base2measurerelationship_instantiation(instance):
    assert isinstance(instance, smm_Base2MeasureRelationship)

@given(instance=smm_Base1MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm_base1measurerelationship_instantiation(instance):
    assert isinstance(instance, smm_Base1MeasureRelationship)

@given(instance=MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_measurementrelationship_instantiation(instance):
    assert isinstance(instance, MeasurementRelationship)

@given(instance=smm_RescaleMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_rescalemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RescaleMeasurementRelationship)

@given(instance=smm_Base2MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_base2measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_Base2MeasurementRelationship)

@given(instance=smm_BaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_basemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_BaseMeasurementRelationship)

@given(instance=smm_RankingMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_rankingmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RankingMeasurementRelationship)

@given(instance=smm_RecursiveMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_recursivemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RecursiveMeasurementRelationship)

@given(instance=smm_RefinementMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_refinementmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_RefinementMeasurementRelationship)

@given(instance=smm_EquivalentMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_equivalentmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_EquivalentMeasurementRelationship)

@given(instance=smm_Base1MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm_base1measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm_Base1MeasurementRelationship)

@given(instance=smm_DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_smm_dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, smm_DimensionalMeasurement)



@given(instance=smm_DimensionalMeasurement_strategy)
def test_smm_dimensionalmeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, DimensionalMeasurement)

@given(instance=smm_DirectMeasurement_strategy)
@settings(max_examples=50)
def test_smm_directmeasurement_instantiation(instance):
    assert isinstance(instance, smm_DirectMeasurement)

@given(instance=smm_RescaledMeasurement_strategy)
@settings(max_examples=50)
def test_smm_rescaledmeasurement_instantiation(instance):
    assert isinstance(instance, smm_RescaledMeasurement)



@given(instance=smm_RescaledMeasurement_strategy)
def test_smm_rescaledmeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm_CollectiveMeasurement_strategy)
@settings(max_examples=50)
def test_smm_collectivemeasurement_instantiation(instance):
    assert isinstance(instance, smm_CollectiveMeasurement)



@given(instance=smm_CollectiveMeasurement_strategy)
def test_smm_collectivemeasurement_accumulator_setter(instance):
    original = instance.accumulator
    instance.accumulator = original
    assert instance.accumulator == original



@given(instance=smm_CollectiveMeasurement_strategy)
def test_smm_collectivemeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm_BinaryMeasurement_strategy)
@settings(max_examples=50)
def test_smm_binarymeasurement_instantiation(instance):
    assert isinstance(instance, smm_BinaryMeasurement)



@given(instance=smm_BinaryMeasurement_strategy)
def test_smm_binarymeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm_NamedMeasurement_strategy)
@settings(max_examples=50)
def test_smm_namedmeasurement_instantiation(instance):
    assert isinstance(instance, smm_NamedMeasurement)

@given(instance=smm_AggregatedMeasurement_strategy)
@settings(max_examples=50)
def test_smm_aggregatedmeasurement_instantiation(instance):
    assert isinstance(instance, smm_AggregatedMeasurement)



@given(instance=smm_AggregatedMeasurement_strategy)
def test_smm_aggregatedmeasurement_isBaseSuppled_setter(instance):
    original = instance.isBaseSuppled
    instance.isBaseSuppled = original
    assert instance.isBaseSuppled == original

@given(instance=smm_CategoryRelationship_strategy)
@settings(max_examples=50)
def test_smm_categoryrelationship_instantiation(instance):
    assert isinstance(instance, smm_CategoryRelationship)

@given(instance=SmmElement_strategy)
@settings(max_examples=50)
def test_smmelement_instantiation(instance):
    assert isinstance(instance, SmmElement)

@given(instance=smm_SmmRelationship_strategy)
@settings(max_examples=50)
def test_smm_smmrelationship_instantiation(instance):
    assert isinstance(instance, smm_SmmRelationship)

@given(instance=smm_Observation_strategy)
@settings(max_examples=50)
def test_smm_observation_instantiation(instance):
    assert isinstance(instance, smm_Observation)



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



@given(instance=smm_Observation_strategy)
def test_smm_observation_whenObserved_setter(instance):
    original = instance.whenObserved
    instance.whenObserved = original
    assert instance.whenObserved == original

@given(instance=smm_ObservationScope_strategy)
@settings(max_examples=50)
def test_smm_observationscope_instantiation(instance):
    assert isinstance(instance, smm_ObservationScope)



@given(instance=smm_ObservationScope_strategy)
def test_smm_observationscope_scopeUri_setter(instance):
    original = instance.scopeUri
    instance.scopeUri = original
    assert instance.scopeUri == original

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

@given(instance=smm_Measurement_strategy)
@settings(max_examples=50)
def test_smm_measurement_instantiation(instance):
    assert isinstance(instance, smm_Measurement)



@given(instance=smm_Measurement_strategy)
def test_smm_measurement_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original



@given(instance=smm_Measurement_strategy)
def test_smm_measurement_breakValue_setter(instance):
    original = instance.breakValue
    instance.breakValue = original
    assert instance.breakValue == original

@given(instance=smm_Argument_strategy)
@settings(max_examples=50)
def test_smm_argument_instantiation(instance):
    assert isinstance(instance, smm_Argument)



@given(instance=smm_Argument_strategy)
def test_smm_argument_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=smm_Argument_strategy)
def test_smm_argument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=smm_RankingInterval_strategy)
@settings(max_examples=50)
def test_smm_rankinginterval_instantiation(instance):
    assert isinstance(instance, smm_RankingInterval)



@given(instance=smm_RankingInterval_strategy)
def test_smm_rankinginterval_minimumOpen_setter(instance):
    original = instance.minimumOpen
    instance.minimumOpen = original
    assert instance.minimumOpen == original



@given(instance=smm_RankingInterval_strategy)
def test_smm_rankinginterval_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=smm_RankingInterval_strategy)
def test_smm_rankinginterval_maximumOpen_setter(instance):
    original = instance.maximumOpen
    instance.maximumOpen = original
    assert instance.maximumOpen == original



@given(instance=smm_RankingInterval_strategy)
def test_smm_rankinginterval_maximumEndpoint_setter(instance):
    original = instance.maximumEndpoint
    instance.maximumEndpoint = original
    assert instance.maximumEndpoint == original



@given(instance=smm_RankingInterval_strategy)
def test_smm_rankinginterval_minimumEndpoint_setter(instance):
    original = instance.minimumEndpoint
    instance.minimumEndpoint = original
    assert instance.minimumEndpoint == original

@given(instance=smm_AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_smm_abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, smm_AbstractMeasureElement)
