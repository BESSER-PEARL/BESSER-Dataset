import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UnitOfMeasure,
    smm::CountingUnit,
    smm::SmmElement,
    BaseMeasurementRelationship,
    smm::ScaledBaseMeasurementRelationship,
    BinaryMeasurement,
    smm::RatioMeasurement,
    BinaryMeasure,
    smm::RatioMeasure,
    Interval,
    smm::RankingInterval,
    smm::GradeInterval,
    BaseMeasureRelationship,
    smm::ScaledBaseMeasureRelationship,
    smm::EObject,
    smm::RescaledMeasurementRelationship,
    Measurement,
    smm::GradeMeasurement,
    smm::DimensionalMeasurement,
    smm::RescaledMeasureRelationship,
    MeasurementRelationship,
    smm::BaseMeasurementRelationship,
    smm::RefinementMeasurementRelationship,
    smm::EquivalentMeasurementRelationship,
    MeasureRelationship,
    smm::BaseMeasureRelationship,
    smm::RefinementMeasureRelationship,
    smm::EquivalentMeasureRelationship,
    Measure,
    smm::GradeMeasure,
    smm::DimensionalMeasure,
    AbstractMeasureElement,
    smm::UnitOfMeasure,
    smm::Measure,
    smm::OCLOperation,
    smm::MeasureCategory,
    smm::Scope,
    smm::Characteristic,
    DimensionalMeasure,
    smm::CollectiveMeasure,
    smm::RankingMeasure,
    smm::RescaledMeasure,
    smm::NamedMeasure,
    smm::DirectMeasure,
    smm::BinaryMeasure,
    ScaledBaseMeasurementRelationship,
    smm::RankingMeasurementRelationship,
    smm::GradeMeasurementRelationship,
    smm::Base2MeasurementRelationship,
    smm::BaseNMeasurementRelationship,
    smm::Base1MeasurementRelationship,
    ScaledBaseMeasureRelationship,
    smm::Base2MeasureRelationship,
    smm::BaseNMeasureRelationship,
    smm::GradeMeasureRelationship,
    smm::RankingMeasureRelationship,
    smm::Base1MeasureRelationship,
    SmmRelationship,
    smm::MeasureRelationship,
    smm::MeasurementRelationship,
    smm::CategoryRelationship,
    DimensionalMeasurement,
    smm::RankingMeasurement,
    smm::RescaledMeasurement,
    smm::DirectMeasurement,
    smm::NamedMeasurement,
    smm::CollectiveMeasurement,
    smm::BinaryMeasurement,
    smm::Operation,
    SmmElement,
    smm::Attribute,
    smm::Interval,
    smm::Observation,
    smm::ObservedMeasure,
    smm::ObservationScope,
    smm::Measurement,
    smm::SmmRelationship,
    smm::Annotation,
    smm::MeasureLibrary,
    smm::Argument,
    smm::SmmModel,
    smm::AbstractMeasureElement,
    BinaryFunctor,
    Influence,
    ScaleOfMeasurement,
    MeasurementScale,
    Accumulator,
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



def test_smm::countingunit_is_not_abstract():
    assert not inspect.isabstract(smm::CountingUnit)


def test_smm::countingunit_constructor_exists():
    assert callable(smm::CountingUnit.__init__)


def test_smm::countingunit_constructor_args():
    sig = inspect.signature(smm::CountingUnit.__init__)
    params = list(sig.parameters.keys())



def test_smm::smmelement_is_not_abstract():
    assert not inspect.isabstract(smm::SmmElement)


def test_smm::smmelement_constructor_exists():
    assert callable(smm::SmmElement.__init__)


def test_smm::smmelement_constructor_args():
    sig = inspect.signature(smm::SmmElement.__init__)
    params = list(sig.parameters.keys())
    assert "shortDescription" in params, "Missing parameter 'shortDescription'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_smm::smmelement_has_shortDescription():
    assert hasattr(smm::SmmElement, "shortDescription")
    descriptor = None
    for klass in smm::SmmElement.__mro__:
        if "shortDescription" in klass.__dict__:
            descriptor = klass.__dict__["shortDescription"]
            break
    assert isinstance(descriptor, property)

def test_smm::smmelement_has_name():
    assert hasattr(smm::SmmElement, "name")
    descriptor = None
    for klass in smm::SmmElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smm::smmelement_has_description():
    assert hasattr(smm::SmmElement, "description")
    descriptor = None
    for klass in smm::SmmElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_basemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(BaseMeasurementRelationship)


def test_basemeasurementrelationship_constructor_exists():
    assert callable(BaseMeasurementRelationship.__init__)


def test_basemeasurementrelationship_constructor_args():
    sig = inspect.signature(BaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::scaledbasemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::ScaledBaseMeasurementRelationship)


def test_smm::scaledbasemeasurementrelationship_constructor_exists():
    assert callable(smm::ScaledBaseMeasurementRelationship.__init__)


def test_smm::scaledbasemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::ScaledBaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_binarymeasurement_is_not_abstract():
    assert not inspect.isabstract(BinaryMeasurement)


def test_binarymeasurement_constructor_exists():
    assert callable(BinaryMeasurement.__init__)


def test_binarymeasurement_constructor_args():
    sig = inspect.signature(BinaryMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::ratiomeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::RatioMeasurement)


def test_smm::ratiomeasurement_constructor_exists():
    assert callable(smm::RatioMeasurement.__init__)


def test_smm::ratiomeasurement_constructor_args():
    sig = inspect.signature(smm::RatioMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_binarymeasure_is_not_abstract():
    assert not inspect.isabstract(BinaryMeasure)


def test_binarymeasure_constructor_exists():
    assert callable(BinaryMeasure.__init__)


def test_binarymeasure_constructor_args():
    sig = inspect.signature(BinaryMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::ratiomeasure_is_not_abstract():
    assert not inspect.isabstract(smm::RatioMeasure)


def test_smm::ratiomeasure_constructor_exists():
    assert callable(smm::RatioMeasure.__init__)


def test_smm::ratiomeasure_constructor_args():
    sig = inspect.signature(smm::RatioMeasure.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_smm::rankinginterval_is_not_abstract():
    assert not inspect.isabstract(smm::RankingInterval)


def test_smm::rankinginterval_constructor_exists():
    assert callable(smm::RankingInterval.__init__)


def test_smm::rankinginterval_constructor_args():
    sig = inspect.signature(smm::RankingInterval.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smm::rankinginterval_has_value():
    assert hasattr(smm::RankingInterval, "value")
    descriptor = None
    for klass in smm::RankingInterval.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm::gradeinterval_is_not_abstract():
    assert not inspect.isabstract(smm::GradeInterval)


def test_smm::gradeinterval_constructor_exists():
    assert callable(smm::GradeInterval.__init__)


def test_smm::gradeinterval_constructor_args():
    sig = inspect.signature(smm::GradeInterval.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_smm::gradeinterval_has_symbol():
    assert hasattr(smm::GradeInterval, "symbol")
    descriptor = None
    for klass in smm::GradeInterval.__mro__:
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



def test_smm::scaledbasemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::ScaledBaseMeasureRelationship)


def test_smm::scaledbasemeasurerelationship_constructor_exists():
    assert callable(smm::ScaledBaseMeasureRelationship.__init__)


def test_smm::scaledbasemeasurerelationship_constructor_args():
    sig = inspect.signature(smm::ScaledBaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::eobject_is_not_abstract():
    assert not inspect.isabstract(smm::EObject)


def test_smm::eobject_constructor_exists():
    assert callable(smm::EObject.__init__)


def test_smm::eobject_constructor_args():
    sig = inspect.signature(smm::EObject.__init__)
    params = list(sig.parameters.keys())



def test_smm::rescaledmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RescaledMeasurementRelationship)


def test_smm::rescaledmeasurementrelationship_constructor_exists():
    assert callable(smm::RescaledMeasurementRelationship.__init__)


def test_smm::rescaledmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RescaledMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measurement_is_not_abstract():
    assert not inspect.isabstract(Measurement)


def test_measurement_constructor_exists():
    assert callable(Measurement.__init__)


def test_measurement_constructor_args():
    sig = inspect.signature(Measurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::grademeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::GradeMeasurement)


def test_smm::grademeasurement_constructor_exists():
    assert callable(smm::GradeMeasurement.__init__)


def test_smm::grademeasurement_constructor_args():
    sig = inspect.signature(smm::GradeMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"
    assert "value" in params, "Missing parameter 'value'"

def test_smm::grademeasurement_has_isBaseSupplied():
    assert hasattr(smm::GradeMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm::GradeMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)

def test_smm::grademeasurement_has_value():
    assert hasattr(smm::GradeMeasurement, "value")
    descriptor = None
    for klass in smm::GradeMeasurement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm::dimensionalmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::DimensionalMeasurement)


def test_smm::dimensionalmeasurement_constructor_exists():
    assert callable(smm::DimensionalMeasurement.__init__)


def test_smm::dimensionalmeasurement_constructor_args():
    sig = inspect.signature(smm::DimensionalMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smm::dimensionalmeasurement_has_value():
    assert hasattr(smm::DimensionalMeasurement, "value")
    descriptor = None
    for klass in smm::DimensionalMeasurement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm::rescaledmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RescaledMeasureRelationship)


def test_smm::rescaledmeasurerelationship_constructor_exists():
    assert callable(smm::RescaledMeasureRelationship.__init__)


def test_smm::rescaledmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RescaledMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(MeasurementRelationship)


def test_measurementrelationship_constructor_exists():
    assert callable(MeasurementRelationship.__init__)


def test_measurementrelationship_constructor_args():
    sig = inspect.signature(MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::basemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::BaseMeasurementRelationship)


def test_smm::basemeasurementrelationship_constructor_exists():
    assert callable(smm::BaseMeasurementRelationship.__init__)


def test_smm::basemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::BaseMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::refinementmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RefinementMeasurementRelationship)


def test_smm::refinementmeasurementrelationship_constructor_exists():
    assert callable(smm::RefinementMeasurementRelationship.__init__)


def test_smm::refinementmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RefinementMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::equivalentmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::EquivalentMeasurementRelationship)


def test_smm::equivalentmeasurementrelationship_constructor_exists():
    assert callable(smm::EquivalentMeasurementRelationship.__init__)


def test_smm::equivalentmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::EquivalentMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measurerelationship_is_not_abstract():
    assert not inspect.isabstract(MeasureRelationship)


def test_measurerelationship_constructor_exists():
    assert callable(MeasureRelationship.__init__)


def test_measurerelationship_constructor_args():
    sig = inspect.signature(MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::basemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::BaseMeasureRelationship)


def test_smm::basemeasurerelationship_constructor_exists():
    assert callable(smm::BaseMeasureRelationship.__init__)


def test_smm::basemeasurerelationship_constructor_args():
    sig = inspect.signature(smm::BaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::refinementmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RefinementMeasureRelationship)


def test_smm::refinementmeasurerelationship_constructor_exists():
    assert callable(smm::RefinementMeasureRelationship.__init__)


def test_smm::refinementmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RefinementMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::equivalentmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::EquivalentMeasureRelationship)


def test_smm::equivalentmeasurerelationship_constructor_exists():
    assert callable(smm::EquivalentMeasureRelationship.__init__)


def test_smm::equivalentmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::EquivalentMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_smm::grademeasure_is_not_abstract():
    assert not inspect.isabstract(smm::GradeMeasure)


def test_smm::grademeasure_constructor_exists():
    assert callable(smm::GradeMeasure.__init__)


def test_smm::grademeasure_constructor_args():
    sig = inspect.signature(smm::GradeMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::DimensionalMeasure)


def test_smm::dimensionalmeasure_constructor_exists():
    assert callable(smm::DimensionalMeasure.__init__)


def test_smm::dimensionalmeasure_constructor_args():
    sig = inspect.signature(smm::DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"

def test_smm::dimensionalmeasure_has_formula():
    assert hasattr(smm::DimensionalMeasure, "formula")
    descriptor = None
    for klass in smm::DimensionalMeasure.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(AbstractMeasureElement)


def test_abstractmeasureelement_constructor_exists():
    assert callable(AbstractMeasureElement.__init__)


def test_abstractmeasureelement_constructor_args():
    sig = inspect.signature(AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())



def test_smm::unitofmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::UnitOfMeasure)


def test_smm::unitofmeasure_constructor_exists():
    assert callable(smm::UnitOfMeasure.__init__)


def test_smm::unitofmeasure_constructor_args():
    sig = inspect.signature(smm::UnitOfMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::measure_is_not_abstract():
    assert not inspect.isabstract(smm::Measure)


def test_smm::measure_constructor_exists():
    assert callable(smm::Measure.__init__)


def test_smm::measure_constructor_args():
    sig = inspect.signature(smm::Measure.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "measurementLabelFormat" in params, "Missing parameter 'measurementLabelFormat'"
    assert "measureLabelFormat" in params, "Missing parameter 'measureLabelFormat'"
    assert "customScale" in params, "Missing parameter 'customScale'"
    assert "source" in params, "Missing parameter 'source'"

def test_smm::measure_has_visible():
    assert hasattr(smm::Measure, "visible")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_smm::measure_has_scale():
    assert hasattr(smm::Measure, "scale")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_smm::measure_has_measurementLabelFormat():
    assert hasattr(smm::Measure, "measurementLabelFormat")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "measurementLabelFormat" in klass.__dict__:
            descriptor = klass.__dict__["measurementLabelFormat"]
            break
    assert isinstance(descriptor, property)

def test_smm::measure_has_measureLabelFormat():
    assert hasattr(smm::Measure, "measureLabelFormat")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "measureLabelFormat" in klass.__dict__:
            descriptor = klass.__dict__["measureLabelFormat"]
            break
    assert isinstance(descriptor, property)

def test_smm::measure_has_customScale():
    assert hasattr(smm::Measure, "customScale")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "customScale" in klass.__dict__:
            descriptor = klass.__dict__["customScale"]
            break
    assert isinstance(descriptor, property)

def test_smm::measure_has_source():
    assert hasattr(smm::Measure, "source")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_smm::ocloperation_is_not_abstract():
    assert not inspect.isabstract(smm::OCLOperation)


def test_smm::ocloperation_constructor_exists():
    assert callable(smm::OCLOperation.__init__)


def test_smm::ocloperation_constructor_args():
    sig = inspect.signature(smm::OCLOperation.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "context" in params, "Missing parameter 'context'"

def test_smm::ocloperation_has_body():
    assert hasattr(smm::OCLOperation, "body")
    descriptor = None
    for klass in smm::OCLOperation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_smm::ocloperation_has_context():
    assert hasattr(smm::OCLOperation, "context")
    descriptor = None
    for klass in smm::OCLOperation.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_smm::measurecategory_is_not_abstract():
    assert not inspect.isabstract(smm::MeasureCategory)


def test_smm::measurecategory_constructor_exists():
    assert callable(smm::MeasureCategory.__init__)


def test_smm::measurecategory_constructor_args():
    sig = inspect.signature(smm::MeasureCategory.__init__)
    params = list(sig.parameters.keys())



def test_smm::scope_is_not_abstract():
    assert not inspect.isabstract(smm::Scope)


def test_smm::scope_constructor_exists():
    assert callable(smm::Scope.__init__)


def test_smm::scope_constructor_args():
    sig = inspect.signature(smm::Scope.__init__)
    params = list(sig.parameters.keys())



def test_smm::characteristic_is_not_abstract():
    assert not inspect.isabstract(smm::Characteristic)


def test_smm::characteristic_constructor_exists():
    assert callable(smm::Characteristic.__init__)


def test_smm::characteristic_constructor_args():
    sig = inspect.signature(smm::Characteristic.__init__)
    params = list(sig.parameters.keys())



def test_dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasure)


def test_dimensionalmeasure_constructor_exists():
    assert callable(DimensionalMeasure.__init__)


def test_dimensionalmeasure_constructor_args():
    sig = inspect.signature(DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::collectivemeasure_is_not_abstract():
    assert not inspect.isabstract(smm::CollectiveMeasure)


def test_smm::collectivemeasure_constructor_exists():
    assert callable(smm::CollectiveMeasure.__init__)


def test_smm::collectivemeasure_constructor_args():
    sig = inspect.signature(smm::CollectiveMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "accumulator" in params, "Missing parameter 'accumulator'"

def test_smm::collectivemeasure_has_accumulator():
    assert hasattr(smm::CollectiveMeasure, "accumulator")
    descriptor = None
    for klass in smm::CollectiveMeasure.__mro__:
        if "accumulator" in klass.__dict__:
            descriptor = klass.__dict__["accumulator"]
            break
    assert isinstance(descriptor, property)



def test_smm::rankingmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::RankingMeasure)


def test_smm::rankingmeasure_constructor_exists():
    assert callable(smm::RankingMeasure.__init__)


def test_smm::rankingmeasure_constructor_args():
    sig = inspect.signature(smm::RankingMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::rescaledmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::RescaledMeasure)


def test_smm::rescaledmeasure_constructor_exists():
    assert callable(smm::RescaledMeasure.__init__)


def test_smm::rescaledmeasure_constructor_args():
    sig = inspect.signature(smm::RescaledMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "operationFirst" in params, "Missing parameter 'operationFirst'"
    assert "multiplier" in params, "Missing parameter 'multiplier'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_smm::rescaledmeasure_has_operationFirst():
    assert hasattr(smm::RescaledMeasure, "operationFirst")
    descriptor = None
    for klass in smm::RescaledMeasure.__mro__:
        if "operationFirst" in klass.__dict__:
            descriptor = klass.__dict__["operationFirst"]
            break
    assert isinstance(descriptor, property)

def test_smm::rescaledmeasure_has_multiplier():
    assert hasattr(smm::RescaledMeasure, "multiplier")
    descriptor = None
    for klass in smm::RescaledMeasure.__mro__:
        if "multiplier" in klass.__dict__:
            descriptor = klass.__dict__["multiplier"]
            break
    assert isinstance(descriptor, property)

def test_smm::rescaledmeasure_has_offset():
    assert hasattr(smm::RescaledMeasure, "offset")
    descriptor = None
    for klass in smm::RescaledMeasure.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_smm::namedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::NamedMeasure)


def test_smm::namedmeasure_constructor_exists():
    assert callable(smm::NamedMeasure.__init__)


def test_smm::namedmeasure_constructor_args():
    sig = inspect.signature(smm::NamedMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::directmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::DirectMeasure)


def test_smm::directmeasure_constructor_exists():
    assert callable(smm::DirectMeasure.__init__)


def test_smm::directmeasure_constructor_args():
    sig = inspect.signature(smm::DirectMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::binarymeasure_is_not_abstract():
    assert not inspect.isabstract(smm::BinaryMeasure)


def test_smm::binarymeasure_constructor_exists():
    assert callable(smm::BinaryMeasure.__init__)


def test_smm::binarymeasure_constructor_args():
    sig = inspect.signature(smm::BinaryMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "functor" in params, "Missing parameter 'functor'"

def test_smm::binarymeasure_has_functor():
    assert hasattr(smm::BinaryMeasure, "functor")
    descriptor = None
    for klass in smm::BinaryMeasure.__mro__:
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



def test_smm::rankingmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RankingMeasurementRelationship)


def test_smm::rankingmeasurementrelationship_constructor_exists():
    assert callable(smm::RankingMeasurementRelationship.__init__)


def test_smm::rankingmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RankingMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::grademeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::GradeMeasurementRelationship)


def test_smm::grademeasurementrelationship_constructor_exists():
    assert callable(smm::GradeMeasurementRelationship.__init__)


def test_smm::grademeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::GradeMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base2measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base2MeasurementRelationship)


def test_smm::base2measurementrelationship_constructor_exists():
    assert callable(smm::Base2MeasurementRelationship.__init__)


def test_smm::base2measurementrelationship_constructor_args():
    sig = inspect.signature(smm::Base2MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::basenmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::BaseNMeasurementRelationship)


def test_smm::basenmeasurementrelationship_constructor_exists():
    assert callable(smm::BaseNMeasurementRelationship.__init__)


def test_smm::basenmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::BaseNMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base1measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base1MeasurementRelationship)


def test_smm::base1measurementrelationship_constructor_exists():
    assert callable(smm::Base1MeasurementRelationship.__init__)


def test_smm::base1measurementrelationship_constructor_args():
    sig = inspect.signature(smm::Base1MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_scaledbasemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(ScaledBaseMeasureRelationship)


def test_scaledbasemeasurerelationship_constructor_exists():
    assert callable(ScaledBaseMeasureRelationship.__init__)


def test_scaledbasemeasurerelationship_constructor_args():
    sig = inspect.signature(ScaledBaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base2measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base2MeasureRelationship)


def test_smm::base2measurerelationship_constructor_exists():
    assert callable(smm::Base2MeasureRelationship.__init__)


def test_smm::base2measurerelationship_constructor_args():
    sig = inspect.signature(smm::Base2MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::basenmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::BaseNMeasureRelationship)


def test_smm::basenmeasurerelationship_constructor_exists():
    assert callable(smm::BaseNMeasureRelationship.__init__)


def test_smm::basenmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::BaseNMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::grademeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::GradeMeasureRelationship)


def test_smm::grademeasurerelationship_constructor_exists():
    assert callable(smm::GradeMeasureRelationship.__init__)


def test_smm::grademeasurerelationship_constructor_args():
    sig = inspect.signature(smm::GradeMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::rankingmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RankingMeasureRelationship)


def test_smm::rankingmeasurerelationship_constructor_exists():
    assert callable(smm::RankingMeasureRelationship.__init__)


def test_smm::rankingmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RankingMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base1measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base1MeasureRelationship)


def test_smm::base1measurerelationship_constructor_exists():
    assert callable(smm::Base1MeasureRelationship.__init__)


def test_smm::base1measurerelationship_constructor_args():
    sig = inspect.signature(smm::Base1MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smmrelationship_is_not_abstract():
    assert not inspect.isabstract(SmmRelationship)


def test_smmrelationship_constructor_exists():
    assert callable(SmmRelationship.__init__)


def test_smmrelationship_constructor_args():
    sig = inspect.signature(SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::MeasureRelationship)


def test_smm::measurerelationship_constructor_exists():
    assert callable(smm::MeasureRelationship.__init__)


def test_smm::measurerelationship_constructor_args():
    sig = inspect.signature(smm::MeasureRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "influence" in params, "Missing parameter 'influence'"

def test_smm::measurerelationship_has_influence():
    assert hasattr(smm::MeasureRelationship, "influence")
    descriptor = None
    for klass in smm::MeasureRelationship.__mro__:
        if "influence" in klass.__dict__:
            descriptor = klass.__dict__["influence"]
            break
    assert isinstance(descriptor, property)



def test_smm::measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::MeasurementRelationship)


def test_smm::measurementrelationship_constructor_exists():
    assert callable(smm::MeasurementRelationship.__init__)


def test_smm::measurementrelationship_constructor_args():
    sig = inspect.signature(smm::MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::categoryrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::CategoryRelationship)


def test_smm::categoryrelationship_constructor_exists():
    assert callable(smm::CategoryRelationship.__init__)


def test_smm::categoryrelationship_constructor_args():
    sig = inspect.signature(smm::CategoryRelationship.__init__)
    params = list(sig.parameters.keys())



def test_dimensionalmeasurement_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasurement)


def test_dimensionalmeasurement_constructor_exists():
    assert callable(DimensionalMeasurement.__init__)


def test_dimensionalmeasurement_constructor_args():
    sig = inspect.signature(DimensionalMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::rankingmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::RankingMeasurement)


def test_smm::rankingmeasurement_constructor_exists():
    assert callable(smm::RankingMeasurement.__init__)


def test_smm::rankingmeasurement_constructor_args():
    sig = inspect.signature(smm::RankingMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm::rankingmeasurement_has_isBaseSupplied():
    assert hasattr(smm::RankingMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm::RankingMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm::rescaledmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::RescaledMeasurement)


def test_smm::rescaledmeasurement_constructor_exists():
    assert callable(smm::RescaledMeasurement.__init__)


def test_smm::rescaledmeasurement_constructor_args():
    sig = inspect.signature(smm::RescaledMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm::rescaledmeasurement_has_isBaseSupplied():
    assert hasattr(smm::RescaledMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm::RescaledMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm::directmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::DirectMeasurement)


def test_smm::directmeasurement_constructor_exists():
    assert callable(smm::DirectMeasurement.__init__)


def test_smm::directmeasurement_constructor_args():
    sig = inspect.signature(smm::DirectMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::namedmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::NamedMeasurement)


def test_smm::namedmeasurement_constructor_exists():
    assert callable(smm::NamedMeasurement.__init__)


def test_smm::namedmeasurement_constructor_args():
    sig = inspect.signature(smm::NamedMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::collectivemeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::CollectiveMeasurement)


def test_smm::collectivemeasurement_constructor_exists():
    assert callable(smm::CollectiveMeasurement.__init__)


def test_smm::collectivemeasurement_constructor_args():
    sig = inspect.signature(smm::CollectiveMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm::collectivemeasurement_has_isBaseSupplied():
    assert hasattr(smm::CollectiveMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm::CollectiveMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm::binarymeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::BinaryMeasurement)


def test_smm::binarymeasurement_constructor_exists():
    assert callable(smm::BinaryMeasurement.__init__)


def test_smm::binarymeasurement_constructor_args():
    sig = inspect.signature(smm::BinaryMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm::binarymeasurement_has_isBaseSupplied():
    assert hasattr(smm::BinaryMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm::BinaryMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_smm::operation_is_not_abstract():
    assert not inspect.isabstract(smm::Operation)


def test_smm::operation_constructor_exists():
    assert callable(smm::Operation.__init__)


def test_smm::operation_constructor_args():
    sig = inspect.signature(smm::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_smm::operation_has_language():
    assert hasattr(smm::Operation, "language")
    descriptor = None
    for klass in smm::Operation.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_smm::operation_has_body():
    assert hasattr(smm::Operation, "body")
    descriptor = None
    for klass in smm::Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_smmelement_is_not_abstract():
    assert not inspect.isabstract(SmmElement)


def test_smmelement_constructor_exists():
    assert callable(SmmElement.__init__)


def test_smmelement_constructor_args():
    sig = inspect.signature(SmmElement.__init__)
    params = list(sig.parameters.keys())



def test_smm::attribute_is_not_abstract():
    assert not inspect.isabstract(smm::Attribute)


def test_smm::attribute_constructor_exists():
    assert callable(smm::Attribute.__init__)


def test_smm::attribute_constructor_args():
    sig = inspect.signature(smm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"
    assert "value" in params, "Missing parameter 'value'"

def test_smm::attribute_has_tag():
    assert hasattr(smm::Attribute, "tag")
    descriptor = None
    for klass in smm::Attribute.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_smm::attribute_has_value():
    assert hasattr(smm::Attribute, "value")
    descriptor = None
    for klass in smm::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm::interval_is_not_abstract():
    assert not inspect.isabstract(smm::Interval)


def test_smm::interval_constructor_exists():
    assert callable(smm::Interval.__init__)


def test_smm::interval_constructor_args():
    sig = inspect.signature(smm::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimumOpen" in params, "Missing parameter 'minimumOpen'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximumOpen" in params, "Missing parameter 'maximumOpen'"

def test_smm::interval_has_maximum():
    assert hasattr(smm::Interval, "maximum")
    descriptor = None
    for klass in smm::Interval.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_smm::interval_has_minimumOpen():
    assert hasattr(smm::Interval, "minimumOpen")
    descriptor = None
    for klass in smm::Interval.__mro__:
        if "minimumOpen" in klass.__dict__:
            descriptor = klass.__dict__["minimumOpen"]
            break
    assert isinstance(descriptor, property)

def test_smm::interval_has_minimum():
    assert hasattr(smm::Interval, "minimum")
    descriptor = None
    for klass in smm::Interval.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_smm::interval_has_maximumOpen():
    assert hasattr(smm::Interval, "maximumOpen")
    descriptor = None
    for klass in smm::Interval.__mro__:
        if "maximumOpen" in klass.__dict__:
            descriptor = klass.__dict__["maximumOpen"]
            break
    assert isinstance(descriptor, property)



def test_smm::observation_is_not_abstract():
    assert not inspect.isabstract(smm::Observation)


def test_smm::observation_constructor_exists():
    assert callable(smm::Observation.__init__)


def test_smm::observation_constructor_args():
    sig = inspect.signature(smm::Observation.__init__)
    params = list(sig.parameters.keys())
    assert "observer" in params, "Missing parameter 'observer'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "whenObserved" in params, "Missing parameter 'whenObserved'"

def test_smm::observation_has_observer():
    assert hasattr(smm::Observation, "observer")
    descriptor = None
    for klass in smm::Observation.__mro__:
        if "observer" in klass.__dict__:
            descriptor = klass.__dict__["observer"]
            break
    assert isinstance(descriptor, property)

def test_smm::observation_has_tool():
    assert hasattr(smm::Observation, "tool")
    descriptor = None
    for klass in smm::Observation.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_smm::observation_has_whenObserved():
    assert hasattr(smm::Observation, "whenObserved")
    descriptor = None
    for klass in smm::Observation.__mro__:
        if "whenObserved" in klass.__dict__:
            descriptor = klass.__dict__["whenObserved"]
            break
    assert isinstance(descriptor, property)



def test_smm::observedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::ObservedMeasure)


def test_smm::observedmeasure_constructor_exists():
    assert callable(smm::ObservedMeasure.__init__)


def test_smm::observedmeasure_constructor_args():
    sig = inspect.signature(smm::ObservedMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::observationscope_is_not_abstract():
    assert not inspect.isabstract(smm::ObservationScope)


def test_smm::observationscope_constructor_exists():
    assert callable(smm::ObservationScope.__init__)


def test_smm::observationscope_constructor_args():
    sig = inspect.signature(smm::ObservationScope.__init__)
    params = list(sig.parameters.keys())
    assert "scopeUri" in params, "Missing parameter 'scopeUri'"

def test_smm::observationscope_has_scopeUri():
    assert hasattr(smm::ObservationScope, "scopeUri")
    descriptor = None
    for klass in smm::ObservationScope.__mro__:
        if "scopeUri" in klass.__dict__:
            descriptor = klass.__dict__["scopeUri"]
            break
    assert isinstance(descriptor, property)



def test_smm::measurement_is_not_abstract():
    assert not inspect.isabstract(smm::Measurement)


def test_smm::measurement_constructor_exists():
    assert callable(smm::Measurement.__init__)


def test_smm::measurement_constructor_args():
    sig = inspect.signature(smm::Measurement.__init__)
    params = list(sig.parameters.keys())
    assert "breakValue" in params, "Missing parameter 'breakValue'"
    assert "error" in params, "Missing parameter 'error'"

def test_smm::measurement_has_breakValue():
    assert hasattr(smm::Measurement, "breakValue")
    descriptor = None
    for klass in smm::Measurement.__mro__:
        if "breakValue" in klass.__dict__:
            descriptor = klass.__dict__["breakValue"]
            break
    assert isinstance(descriptor, property)

def test_smm::measurement_has_error():
    assert hasattr(smm::Measurement, "error")
    descriptor = None
    for klass in smm::Measurement.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)



def test_smm::smmrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::SmmRelationship)


def test_smm::smmrelationship_constructor_exists():
    assert callable(smm::SmmRelationship.__init__)


def test_smm::smmrelationship_constructor_args():
    sig = inspect.signature(smm::SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::annotation_is_not_abstract():
    assert not inspect.isabstract(smm::Annotation)


def test_smm::annotation_constructor_exists():
    assert callable(smm::Annotation.__init__)


def test_smm::annotation_constructor_args():
    sig = inspect.signature(smm::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_smm::annotation_has_text():
    assert hasattr(smm::Annotation, "text")
    descriptor = None
    for klass in smm::Annotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_smm::measurelibrary_is_not_abstract():
    assert not inspect.isabstract(smm::MeasureLibrary)


def test_smm::measurelibrary_constructor_exists():
    assert callable(smm::MeasureLibrary.__init__)


def test_smm::measurelibrary_constructor_args():
    sig = inspect.signature(smm::MeasureLibrary.__init__)
    params = list(sig.parameters.keys())



def test_smm::argument_is_not_abstract():
    assert not inspect.isabstract(smm::Argument)


def test_smm::argument_constructor_exists():
    assert callable(smm::Argument.__init__)


def test_smm::argument_constructor_args():
    sig = inspect.signature(smm::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "value" in params, "Missing parameter 'value'"

def test_smm::argument_has_Type():
    assert hasattr(smm::Argument, "Type")
    descriptor = None
    for klass in smm::Argument.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_smm::argument_has_value():
    assert hasattr(smm::Argument, "value")
    descriptor = None
    for klass in smm::Argument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smm::smmmodel_is_not_abstract():
    assert not inspect.isabstract(smm::SmmModel)


def test_smm::smmmodel_constructor_exists():
    assert callable(smm::SmmModel.__init__)


def test_smm::smmmodel_constructor_args():
    sig = inspect.signature(smm::SmmModel.__init__)
    params = list(sig.parameters.keys())



def test_smm::abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(smm::AbstractMeasureElement)


def test_smm::abstractmeasureelement_constructor_exists():
    assert callable(smm::AbstractMeasureElement.__init__)


def test_smm::abstractmeasureelement_constructor_args():
    sig = inspect.signature(smm::AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())

def test_binaryfunctor_exists():
    # Check that the Enumeration exists
    assert BinaryFunctor is not None

def test_binaryfunctor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryFunctor]
    expected_literals = [
        "custom",
        "minus",
        "divide",
        "multiply",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryFunctor"

def test_influence_exists():
    # Check that the Enumeration exists
    assert Influence is not None

def test_influence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Influence]
    expected_literals = [
        "negative",
        "positive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Influence"

def test_scaleofmeasurement_exists():
    # Check that the Enumeration exists
    assert ScaleOfMeasurement is not None

def test_scaleofmeasurement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleOfMeasurement]
    expected_literals = [
        "nominal",
        "interval",
        "ratio",
        "custom",
        "ordinal",
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
        "ordinal",
        "ratio",
        "interval",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasurementScale"

def test_accumulator_exists():
    # Check that the Enumeration exists
    assert Accumulator is not None

def test_accumulator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Accumulator]
    expected_literals = [
        "average",
        "standardDeviation",
        "custom",
        "minimum",
        "maximum",
        "sum",
        "product",
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
UnitOfMeasure_strategy = st.builds(
    UnitOfMeasure,
)
smm::CountingUnit_strategy = st.builds(
    smm::CountingUnit,
)
smm::SmmElement_strategy = st.builds(
    smm::SmmElement,
    shortDescription=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
BaseMeasurementRelationship_strategy = st.builds(
    BaseMeasurementRelationship,
)
smm::ScaledBaseMeasurementRelationship_strategy = st.builds(
    smm::ScaledBaseMeasurementRelationship,
)
BinaryMeasurement_strategy = st.builds(
    BinaryMeasurement,
)
smm::RatioMeasurement_strategy = st.builds(
    smm::RatioMeasurement,
)
BinaryMeasure_strategy = st.builds(
    BinaryMeasure,
)
smm::RatioMeasure_strategy = st.builds(
    smm::RatioMeasure,
)
Interval_strategy = st.builds(
    Interval,
)
smm::RankingInterval_strategy = st.builds(
    smm::RankingInterval,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm::GradeInterval_strategy = st.builds(
    smm::GradeInterval,
    symbol=
        safe_text
)
BaseMeasureRelationship_strategy = st.builds(
    BaseMeasureRelationship,
)
smm::ScaledBaseMeasureRelationship_strategy = st.builds(
    smm::ScaledBaseMeasureRelationship,
)
smm::EObject_strategy = st.builds(
    smm::EObject,
)
smm::RescaledMeasurementRelationship_strategy = st.builds(
    smm::RescaledMeasurementRelationship,
)
Measurement_strategy = st.builds(
    Measurement,
)
smm::GradeMeasurement_strategy = st.builds(
    smm::GradeMeasurement,
    isBaseSupplied=
        st.booleans(),
    value=
        safe_text
)
smm::DimensionalMeasurement_strategy = st.builds(
    smm::DimensionalMeasurement,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm::RescaledMeasureRelationship_strategy = st.builds(
    smm::RescaledMeasureRelationship,
)
MeasurementRelationship_strategy = st.builds(
    MeasurementRelationship,
)
smm::BaseMeasurementRelationship_strategy = st.builds(
    smm::BaseMeasurementRelationship,
)
smm::RefinementMeasurementRelationship_strategy = st.builds(
    smm::RefinementMeasurementRelationship,
)
smm::EquivalentMeasurementRelationship_strategy = st.builds(
    smm::EquivalentMeasurementRelationship,
)
MeasureRelationship_strategy = st.builds(
    MeasureRelationship,
)
smm::BaseMeasureRelationship_strategy = st.builds(
    smm::BaseMeasureRelationship,
)
smm::RefinementMeasureRelationship_strategy = st.builds(
    smm::RefinementMeasureRelationship,
)
smm::EquivalentMeasureRelationship_strategy = st.builds(
    smm::EquivalentMeasureRelationship,
)
Measure_strategy = st.builds(
    Measure,
)
smm::GradeMeasure_strategy = st.builds(
    smm::GradeMeasure,
)
smm::DimensionalMeasure_strategy = st.builds(
    smm::DimensionalMeasure,
    formula=
        safe_text
)
AbstractMeasureElement_strategy = st.builds(
    AbstractMeasureElement,
)
smm::UnitOfMeasure_strategy = st.builds(
    smm::UnitOfMeasure,
)
smm::Measure_strategy = st.builds(
    smm::Measure,
    visible=
        safe_text,
    scale=
        safe_text,
    measurementLabelFormat=
        safe_text,
    measureLabelFormat=
        safe_text,
    customScale=
        safe_text,
    source=
        safe_text
)
smm::OCLOperation_strategy = st.builds(
    smm::OCLOperation,
    body=
        safe_text,
    context=
        safe_text
)
smm::MeasureCategory_strategy = st.builds(
    smm::MeasureCategory,
)
smm::Scope_strategy = st.builds(
    smm::Scope,
)
smm::Characteristic_strategy = st.builds(
    smm::Characteristic,
)
DimensionalMeasure_strategy = st.builds(
    DimensionalMeasure,
)
smm::CollectiveMeasure_strategy = st.builds(
    smm::CollectiveMeasure,
    accumulator=
        safe_text
)
smm::RankingMeasure_strategy = st.builds(
    smm::RankingMeasure,
)
smm::RescaledMeasure_strategy = st.builds(
    smm::RescaledMeasure,
    operationFirst=
        safe_text,
    multiplier=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    offset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smm::NamedMeasure_strategy = st.builds(
    smm::NamedMeasure,
)
smm::DirectMeasure_strategy = st.builds(
    smm::DirectMeasure,
)
smm::BinaryMeasure_strategy = st.builds(
    smm::BinaryMeasure,
    functor=
        safe_text
)
ScaledBaseMeasurementRelationship_strategy = st.builds(
    ScaledBaseMeasurementRelationship,
)
smm::RankingMeasurementRelationship_strategy = st.builds(
    smm::RankingMeasurementRelationship,
)
smm::GradeMeasurementRelationship_strategy = st.builds(
    smm::GradeMeasurementRelationship,
)
smm::Base2MeasurementRelationship_strategy = st.builds(
    smm::Base2MeasurementRelationship,
)
smm::BaseNMeasurementRelationship_strategy = st.builds(
    smm::BaseNMeasurementRelationship,
)
smm::Base1MeasurementRelationship_strategy = st.builds(
    smm::Base1MeasurementRelationship,
)
ScaledBaseMeasureRelationship_strategy = st.builds(
    ScaledBaseMeasureRelationship,
)
smm::Base2MeasureRelationship_strategy = st.builds(
    smm::Base2MeasureRelationship,
)
smm::BaseNMeasureRelationship_strategy = st.builds(
    smm::BaseNMeasureRelationship,
)
smm::GradeMeasureRelationship_strategy = st.builds(
    smm::GradeMeasureRelationship,
)
smm::RankingMeasureRelationship_strategy = st.builds(
    smm::RankingMeasureRelationship,
)
smm::Base1MeasureRelationship_strategy = st.builds(
    smm::Base1MeasureRelationship,
)
SmmRelationship_strategy = st.builds(
    SmmRelationship,
)
smm::MeasureRelationship_strategy = st.builds(
    smm::MeasureRelationship,
    influence=
        safe_text
)
smm::MeasurementRelationship_strategy = st.builds(
    smm::MeasurementRelationship,
)
smm::CategoryRelationship_strategy = st.builds(
    smm::CategoryRelationship,
)
DimensionalMeasurement_strategy = st.builds(
    DimensionalMeasurement,
)
smm::RankingMeasurement_strategy = st.builds(
    smm::RankingMeasurement,
    isBaseSupplied=
        safe_text
)
smm::RescaledMeasurement_strategy = st.builds(
    smm::RescaledMeasurement,
    isBaseSupplied=
        safe_text
)
smm::DirectMeasurement_strategy = st.builds(
    smm::DirectMeasurement,
)
smm::NamedMeasurement_strategy = st.builds(
    smm::NamedMeasurement,
)
smm::CollectiveMeasurement_strategy = st.builds(
    smm::CollectiveMeasurement,
    isBaseSupplied=
        safe_text
)
smm::BinaryMeasurement_strategy = st.builds(
    smm::BinaryMeasurement,
    isBaseSupplied=
        safe_text
)
smm::Operation_strategy = st.builds(
    smm::Operation,
    language=
        safe_text,
    body=
        safe_text
)
SmmElement_strategy = st.builds(
    SmmElement,
)
smm::Attribute_strategy = st.builds(
    smm::Attribute,
    tag=
        safe_text,
    value=
        safe_text
)
smm::Interval_strategy = st.builds(
    smm::Interval,
    maximum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimumOpen=
        safe_text,
    minimum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maximumOpen=
        safe_text
)
smm::Observation_strategy = st.builds(
    smm::Observation,
    observer=
        safe_text,
    tool=
        safe_text,
    whenObserved=
        safe_text
)
smm::ObservedMeasure_strategy = st.builds(
    smm::ObservedMeasure,
)
smm::ObservationScope_strategy = st.builds(
    smm::ObservationScope,
    scopeUri=
        safe_text
)
smm::Measurement_strategy = st.builds(
    smm::Measurement,
    breakValue=
        safe_text,
    error=
        safe_text
)
smm::SmmRelationship_strategy = st.builds(
    smm::SmmRelationship,
)
smm::Annotation_strategy = st.builds(
    smm::Annotation,
    text=
        safe_text
)
smm::MeasureLibrary_strategy = st.builds(
    smm::MeasureLibrary,
)
smm::Argument_strategy = st.builds(
    smm::Argument,
    Type=
        safe_text,
    value=
        safe_text
)
smm::SmmModel_strategy = st.builds(
    smm::SmmModel,
)
smm::AbstractMeasureElement_strategy = st.builds(
    smm::AbstractMeasureElement,
)

@given(instance=UnitOfMeasure_strategy)
@settings(max_examples=50)
def test_unitofmeasure_instantiation(instance):
    assert isinstance(instance, UnitOfMeasure)

@given(instance=smm::CountingUnit_strategy)
@settings(max_examples=50)
def test_smm::countingunit_instantiation(instance):
    assert isinstance(instance, smm::CountingUnit)

@given(instance=smm::SmmElement_strategy)
@settings(max_examples=50)
def test_smm::smmelement_instantiation(instance):
    assert isinstance(instance, smm::SmmElement)

@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_shortDescription_type(instance):
    assert isinstance(instance.shortDescription, str)


@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_shortDescription_setter(instance):
    original = instance.shortDescription
    instance.shortDescription = original
    assert instance.shortDescription == original

@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=BaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_basemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, BaseMeasurementRelationship)

@given(instance=smm::ScaledBaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::scaledbasemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::ScaledBaseMeasurementRelationship)

@given(instance=BinaryMeasurement_strategy)
@settings(max_examples=50)
def test_binarymeasurement_instantiation(instance):
    assert isinstance(instance, BinaryMeasurement)

@given(instance=smm::RatioMeasurement_strategy)
@settings(max_examples=50)
def test_smm::ratiomeasurement_instantiation(instance):
    assert isinstance(instance, smm::RatioMeasurement)

@given(instance=BinaryMeasure_strategy)
@settings(max_examples=50)
def test_binarymeasure_instantiation(instance):
    assert isinstance(instance, BinaryMeasure)

@given(instance=smm::RatioMeasure_strategy)
@settings(max_examples=50)
def test_smm::ratiomeasure_instantiation(instance):
    assert isinstance(instance, smm::RatioMeasure)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=smm::RankingInterval_strategy)
@settings(max_examples=50)
def test_smm::rankinginterval_instantiation(instance):
    assert isinstance(instance, smm::RankingInterval)

@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::GradeInterval_strategy)
@settings(max_examples=50)
def test_smm::gradeinterval_instantiation(instance):
    assert isinstance(instance, smm::GradeInterval)

@given(instance=smm::GradeInterval_strategy)
def test_smm::gradeinterval_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=smm::GradeInterval_strategy)
def test_smm::gradeinterval_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=BaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_basemeasurerelationship_instantiation(instance):
    assert isinstance(instance, BaseMeasureRelationship)

@given(instance=smm::ScaledBaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::scaledbasemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::ScaledBaseMeasureRelationship)

@given(instance=smm::EObject_strategy)
@settings(max_examples=50)
def test_smm::eobject_instantiation(instance):
    assert isinstance(instance, smm::EObject)

@given(instance=smm::RescaledMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::rescaledmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RescaledMeasurementRelationship)

@given(instance=Measurement_strategy)
@settings(max_examples=50)
def test_measurement_instantiation(instance):
    assert isinstance(instance, Measurement)

@given(instance=smm::GradeMeasurement_strategy)
@settings(max_examples=50)
def test_smm::grademeasurement_instantiation(instance):
    assert isinstance(instance, smm::GradeMeasurement)

@given(instance=smm::GradeMeasurement_strategy)
def test_smm::grademeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, bool)


@given(instance=smm::GradeMeasurement_strategy)
def test_smm::grademeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::GradeMeasurement_strategy)
def test_smm::grademeasurement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smm::GradeMeasurement_strategy)
def test_smm::grademeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_smm::dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, smm::DimensionalMeasurement)

@given(instance=smm::DimensionalMeasurement_strategy)
def test_smm::dimensionalmeasurement_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=smm::DimensionalMeasurement_strategy)
def test_smm::dimensionalmeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::RescaledMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::rescaledmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RescaledMeasureRelationship)

@given(instance=MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_measurementrelationship_instantiation(instance):
    assert isinstance(instance, MeasurementRelationship)

@given(instance=smm::BaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::basemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::BaseMeasurementRelationship)

@given(instance=smm::RefinementMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::refinementmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RefinementMeasurementRelationship)

@given(instance=smm::EquivalentMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::equivalentmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::EquivalentMeasurementRelationship)

@given(instance=MeasureRelationship_strategy)
@settings(max_examples=50)
def test_measurerelationship_instantiation(instance):
    assert isinstance(instance, MeasureRelationship)

@given(instance=smm::BaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::basemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::BaseMeasureRelationship)

@given(instance=smm::RefinementMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::refinementmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RefinementMeasureRelationship)

@given(instance=smm::EquivalentMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::equivalentmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::EquivalentMeasureRelationship)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=smm::GradeMeasure_strategy)
@settings(max_examples=50)
def test_smm::grademeasure_instantiation(instance):
    assert isinstance(instance, smm::GradeMeasure)

@given(instance=smm::DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_smm::dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, smm::DimensionalMeasure)

@given(instance=smm::DimensionalMeasure_strategy)
def test_smm::dimensionalmeasure_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=smm::DimensionalMeasure_strategy)
def test_smm::dimensionalmeasure_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, AbstractMeasureElement)

@given(instance=smm::UnitOfMeasure_strategy)
@settings(max_examples=50)
def test_smm::unitofmeasure_instantiation(instance):
    assert isinstance(instance, smm::UnitOfMeasure)

@given(instance=smm::Measure_strategy)
@settings(max_examples=50)
def test_smm::measure_instantiation(instance):
    assert isinstance(instance, smm::Measure)

@given(instance=smm::Measure_strategy)
def test_smm::measure_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_measurementLabelFormat_type(instance):
    assert isinstance(instance.measurementLabelFormat, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_measurementLabelFormat_setter(instance):
    original = instance.measurementLabelFormat
    instance.measurementLabelFormat = original
    assert instance.measurementLabelFormat == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_measureLabelFormat_type(instance):
    assert isinstance(instance.measureLabelFormat, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_measureLabelFormat_setter(instance):
    original = instance.measureLabelFormat
    instance.measureLabelFormat = original
    assert instance.measureLabelFormat == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_customScale_type(instance):
    assert isinstance(instance.customScale, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_customScale_setter(instance):
    original = instance.customScale
    instance.customScale = original
    assert instance.customScale == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=smm::OCLOperation_strategy)
@settings(max_examples=50)
def test_smm::ocloperation_instantiation(instance):
    assert isinstance(instance, smm::OCLOperation)

@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=smm::MeasureCategory_strategy)
@settings(max_examples=50)
def test_smm::measurecategory_instantiation(instance):
    assert isinstance(instance, smm::MeasureCategory)

@given(instance=smm::Scope_strategy)
@settings(max_examples=50)
def test_smm::scope_instantiation(instance):
    assert isinstance(instance, smm::Scope)

@given(instance=smm::Characteristic_strategy)
@settings(max_examples=50)
def test_smm::characteristic_instantiation(instance):
    assert isinstance(instance, smm::Characteristic)

@given(instance=DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, DimensionalMeasure)

@given(instance=smm::CollectiveMeasure_strategy)
@settings(max_examples=50)
def test_smm::collectivemeasure_instantiation(instance):
    assert isinstance(instance, smm::CollectiveMeasure)

@given(instance=smm::CollectiveMeasure_strategy)
def test_smm::collectivemeasure_accumulator_type(instance):
    assert isinstance(instance.accumulator, str)


@given(instance=smm::CollectiveMeasure_strategy)
def test_smm::collectivemeasure_accumulator_setter(instance):
    original = instance.accumulator
    instance.accumulator = original
    assert instance.accumulator == original

@given(instance=smm::RankingMeasure_strategy)
@settings(max_examples=50)
def test_smm::rankingmeasure_instantiation(instance):
    assert isinstance(instance, smm::RankingMeasure)

@given(instance=smm::RescaledMeasure_strategy)
@settings(max_examples=50)
def test_smm::rescaledmeasure_instantiation(instance):
    assert isinstance(instance, smm::RescaledMeasure)

@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_operationFirst_type(instance):
    assert isinstance(instance.operationFirst, str)


@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_operationFirst_setter(instance):
    original = instance.operationFirst
    instance.operationFirst = original
    assert instance.operationFirst == original

@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_multiplier_type(instance):
    assert isinstance(instance.multiplier, float)


@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_multiplier_setter(instance):
    original = instance.multiplier
    instance.multiplier = original
    assert instance.multiplier == original

@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_offset_type(instance):
    assert isinstance(instance.offset, float)


@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=smm::NamedMeasure_strategy)
@settings(max_examples=50)
def test_smm::namedmeasure_instantiation(instance):
    assert isinstance(instance, smm::NamedMeasure)

@given(instance=smm::DirectMeasure_strategy)
@settings(max_examples=50)
def test_smm::directmeasure_instantiation(instance):
    assert isinstance(instance, smm::DirectMeasure)

@given(instance=smm::BinaryMeasure_strategy)
@settings(max_examples=50)
def test_smm::binarymeasure_instantiation(instance):
    assert isinstance(instance, smm::BinaryMeasure)

@given(instance=smm::BinaryMeasure_strategy)
def test_smm::binarymeasure_functor_type(instance):
    assert isinstance(instance.functor, str)


@given(instance=smm::BinaryMeasure_strategy)
def test_smm::binarymeasure_functor_setter(instance):
    original = instance.functor
    instance.functor = original
    assert instance.functor == original

@given(instance=ScaledBaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_scaledbasemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, ScaledBaseMeasurementRelationship)

@given(instance=smm::RankingMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::rankingmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RankingMeasurementRelationship)

@given(instance=smm::GradeMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::grademeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::GradeMeasurementRelationship)

@given(instance=smm::Base2MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::base2measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::Base2MeasurementRelationship)

@given(instance=smm::BaseNMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::basenmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::BaseNMeasurementRelationship)

@given(instance=smm::Base1MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::base1measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::Base1MeasurementRelationship)

@given(instance=ScaledBaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_scaledbasemeasurerelationship_instantiation(instance):
    assert isinstance(instance, ScaledBaseMeasureRelationship)

@given(instance=smm::Base2MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::base2measurerelationship_instantiation(instance):
    assert isinstance(instance, smm::Base2MeasureRelationship)

@given(instance=smm::BaseNMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::basenmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::BaseNMeasureRelationship)

@given(instance=smm::GradeMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::grademeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::GradeMeasureRelationship)

@given(instance=smm::RankingMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::rankingmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RankingMeasureRelationship)

@given(instance=smm::Base1MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::base1measurerelationship_instantiation(instance):
    assert isinstance(instance, smm::Base1MeasureRelationship)

@given(instance=SmmRelationship_strategy)
@settings(max_examples=50)
def test_smmrelationship_instantiation(instance):
    assert isinstance(instance, SmmRelationship)

@given(instance=smm::MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::measurerelationship_instantiation(instance):
    assert isinstance(instance, smm::MeasureRelationship)

@given(instance=smm::MeasureRelationship_strategy)
def test_smm::measurerelationship_influence_type(instance):
    assert isinstance(instance.influence, str)


@given(instance=smm::MeasureRelationship_strategy)
def test_smm::measurerelationship_influence_setter(instance):
    original = instance.influence
    instance.influence = original
    assert instance.influence == original

@given(instance=smm::MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::MeasurementRelationship)

@given(instance=smm::CategoryRelationship_strategy)
@settings(max_examples=50)
def test_smm::categoryrelationship_instantiation(instance):
    assert isinstance(instance, smm::CategoryRelationship)

@given(instance=DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, DimensionalMeasurement)

@given(instance=smm::RankingMeasurement_strategy)
@settings(max_examples=50)
def test_smm::rankingmeasurement_instantiation(instance):
    assert isinstance(instance, smm::RankingMeasurement)

@given(instance=smm::RankingMeasurement_strategy)
def test_smm::rankingmeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, str)


@given(instance=smm::RankingMeasurement_strategy)
def test_smm::rankingmeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::RescaledMeasurement_strategy)
@settings(max_examples=50)
def test_smm::rescaledmeasurement_instantiation(instance):
    assert isinstance(instance, smm::RescaledMeasurement)

@given(instance=smm::RescaledMeasurement_strategy)
def test_smm::rescaledmeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, str)


@given(instance=smm::RescaledMeasurement_strategy)
def test_smm::rescaledmeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::DirectMeasurement_strategy)
@settings(max_examples=50)
def test_smm::directmeasurement_instantiation(instance):
    assert isinstance(instance, smm::DirectMeasurement)

@given(instance=smm::NamedMeasurement_strategy)
@settings(max_examples=50)
def test_smm::namedmeasurement_instantiation(instance):
    assert isinstance(instance, smm::NamedMeasurement)

@given(instance=smm::CollectiveMeasurement_strategy)
@settings(max_examples=50)
def test_smm::collectivemeasurement_instantiation(instance):
    assert isinstance(instance, smm::CollectiveMeasurement)

@given(instance=smm::CollectiveMeasurement_strategy)
def test_smm::collectivemeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, str)


@given(instance=smm::CollectiveMeasurement_strategy)
def test_smm::collectivemeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::BinaryMeasurement_strategy)
@settings(max_examples=50)
def test_smm::binarymeasurement_instantiation(instance):
    assert isinstance(instance, smm::BinaryMeasurement)

@given(instance=smm::BinaryMeasurement_strategy)
def test_smm::binarymeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, str)


@given(instance=smm::BinaryMeasurement_strategy)
def test_smm::binarymeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::Operation_strategy)
@settings(max_examples=50)
def test_smm::operation_instantiation(instance):
    assert isinstance(instance, smm::Operation)

@given(instance=smm::Operation_strategy)
def test_smm::operation_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=smm::Operation_strategy)
def test_smm::operation_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=smm::Operation_strategy)
def test_smm::operation_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=smm::Operation_strategy)
def test_smm::operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=SmmElement_strategy)
@settings(max_examples=50)
def test_smmelement_instantiation(instance):
    assert isinstance(instance, SmmElement)

@given(instance=smm::Attribute_strategy)
@settings(max_examples=50)
def test_smm::attribute_instantiation(instance):
    assert isinstance(instance, smm::Attribute)

@given(instance=smm::Attribute_strategy)
def test_smm::attribute_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=smm::Attribute_strategy)
def test_smm::attribute_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=smm::Attribute_strategy)
def test_smm::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smm::Attribute_strategy)
def test_smm::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::Interval_strategy)
@settings(max_examples=50)
def test_smm::interval_instantiation(instance):
    assert isinstance(instance, smm::Interval)

@given(instance=smm::Interval_strategy)
def test_smm::interval_maximum_type(instance):
    assert isinstance(instance.maximum, float)


@given(instance=smm::Interval_strategy)
def test_smm::interval_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=smm::Interval_strategy)
def test_smm::interval_minimumOpen_type(instance):
    assert isinstance(instance.minimumOpen, str)


@given(instance=smm::Interval_strategy)
def test_smm::interval_minimumOpen_setter(instance):
    original = instance.minimumOpen
    instance.minimumOpen = original
    assert instance.minimumOpen == original

@given(instance=smm::Interval_strategy)
def test_smm::interval_minimum_type(instance):
    assert isinstance(instance.minimum, float)


@given(instance=smm::Interval_strategy)
def test_smm::interval_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=smm::Interval_strategy)
def test_smm::interval_maximumOpen_type(instance):
    assert isinstance(instance.maximumOpen, str)


@given(instance=smm::Interval_strategy)
def test_smm::interval_maximumOpen_setter(instance):
    original = instance.maximumOpen
    instance.maximumOpen = original
    assert instance.maximumOpen == original

@given(instance=smm::Observation_strategy)
@settings(max_examples=50)
def test_smm::observation_instantiation(instance):
    assert isinstance(instance, smm::Observation)

@given(instance=smm::Observation_strategy)
def test_smm::observation_observer_type(instance):
    assert isinstance(instance.observer, str)


@given(instance=smm::Observation_strategy)
def test_smm::observation_observer_setter(instance):
    original = instance.observer
    instance.observer = original
    assert instance.observer == original

@given(instance=smm::Observation_strategy)
def test_smm::observation_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=smm::Observation_strategy)
def test_smm::observation_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=smm::Observation_strategy)
def test_smm::observation_whenObserved_type(instance):
    assert isinstance(instance.whenObserved, str)


@given(instance=smm::Observation_strategy)
def test_smm::observation_whenObserved_setter(instance):
    original = instance.whenObserved
    instance.whenObserved = original
    assert instance.whenObserved == original

@given(instance=smm::ObservedMeasure_strategy)
@settings(max_examples=50)
def test_smm::observedmeasure_instantiation(instance):
    assert isinstance(instance, smm::ObservedMeasure)

@given(instance=smm::ObservationScope_strategy)
@settings(max_examples=50)
def test_smm::observationscope_instantiation(instance):
    assert isinstance(instance, smm::ObservationScope)

@given(instance=smm::ObservationScope_strategy)
def test_smm::observationscope_scopeUri_type(instance):
    assert isinstance(instance.scopeUri, str)


@given(instance=smm::ObservationScope_strategy)
def test_smm::observationscope_scopeUri_setter(instance):
    original = instance.scopeUri
    instance.scopeUri = original
    assert instance.scopeUri == original

@given(instance=smm::Measurement_strategy)
@settings(max_examples=50)
def test_smm::measurement_instantiation(instance):
    assert isinstance(instance, smm::Measurement)

@given(instance=smm::Measurement_strategy)
def test_smm::measurement_breakValue_type(instance):
    assert isinstance(instance.breakValue, str)


@given(instance=smm::Measurement_strategy)
def test_smm::measurement_breakValue_setter(instance):
    original = instance.breakValue
    instance.breakValue = original
    assert instance.breakValue == original

@given(instance=smm::Measurement_strategy)
def test_smm::measurement_error_type(instance):
    assert isinstance(instance.error, str)


@given(instance=smm::Measurement_strategy)
def test_smm::measurement_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=smm::SmmRelationship_strategy)
@settings(max_examples=50)
def test_smm::smmrelationship_instantiation(instance):
    assert isinstance(instance, smm::SmmRelationship)

@given(instance=smm::Annotation_strategy)
@settings(max_examples=50)
def test_smm::annotation_instantiation(instance):
    assert isinstance(instance, smm::Annotation)

@given(instance=smm::Annotation_strategy)
def test_smm::annotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=smm::Annotation_strategy)
def test_smm::annotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=smm::MeasureLibrary_strategy)
@settings(max_examples=50)
def test_smm::measurelibrary_instantiation(instance):
    assert isinstance(instance, smm::MeasureLibrary)

@given(instance=smm::Argument_strategy)
@settings(max_examples=50)
def test_smm::argument_instantiation(instance):
    assert isinstance(instance, smm::Argument)

@given(instance=smm::Argument_strategy)
def test_smm::argument_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=smm::Argument_strategy)
def test_smm::argument_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=smm::Argument_strategy)
def test_smm::argument_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smm::Argument_strategy)
def test_smm::argument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::SmmModel_strategy)
@settings(max_examples=50)
def test_smm::smmmodel_instantiation(instance):
    assert isinstance(instance, smm::SmmModel)

@given(instance=smm::AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_smm::abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, smm::AbstractMeasureElement)
