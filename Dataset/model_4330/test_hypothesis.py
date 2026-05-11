import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryMeasurement,
    smm::RatioMeasurement,
    BinaryMeasure,
    smm::RatioMeasure,
    smm::SmmElement,
    smm::EObject,
    Measurement,
    smm::Grade,
    Measure,
    smm::Ranking,
    DirectMeasure,
    smm::Counting,
    DirectMeasurement,
    smm::Count,
    AbstractMeasureElement,
    smm::Scope,
    smm::OCLOperation,
    smm::Measure,
    smm::Operation,
    smm::Characteristic,
    smm::MeasureCategory,
    SmmRelationship,
    smm::ObservedMeasure,
    smm::MeasureRelationship,
    smm::MeasurementRelationship,
    DimensionalMeasure,
    smm::DirectMeasure,
    smm::RescaledMeasure,
    smm::NamedMeasure,
    smm::CollectiveMeasure,
    smm::DimensionalMeasure,
    smm::BinaryMeasure,
    MeasureRelationship,
    smm::RankingMeasureRelationship,
    smm::EquivalentMeasureRelationship,
    smm::RefinementMeasureRelationship,
    smm::RescaleMeasureRelationship,
    smm::RecursiveMeasureRelationship,
    smm::Base2MeasureRelationship,
    smm::BaseMeasureRelationship,
    smm::Base1MeasureRelationship,
    MeasurementRelationship,
    smm::BaseMeasurementRelationship,
    smm::RecursiveMeasurementRelationship,
    smm::RefinementMeasurementRelationship,
    smm::RescaleMeasurementRelationship,
    smm::RankingMeasurementRelationship,
    smm::EquivalentMeasurementRelationship,
    smm::Base2MeasurementRelationship,
    smm::Base1MeasurementRelationship,
    smm::DimensionalMeasurement,
    DimensionalMeasurement,
    smm::CollectiveMeasurement,
    smm::BinaryMeasurement,
    smm::RescaledMeasurement,
    smm::DirectMeasurement,
    smm::NamedMeasurement,
    smm::AggregatedMeasurement,
    smm::CategoryRelationship,
    SmmElement,
    smm::SmmRelationship,
    smm::RankingInterval,
    smm::Argument,
    smm::Annotation,
    smm::SmmModel,
    smm::Observation,
    smm::Attribute,
    smm::MeasureLibrary,
    smm::ObservationScope,
    smm::Measurement,
    smm::AbstractMeasureElement,
    Accumulator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_smm::smmelement_is_not_abstract():
    assert not inspect.isabstract(smm::SmmElement)


def test_smm::smmelement_constructor_exists():
    assert callable(smm::SmmElement.__init__)


def test_smm::smmelement_constructor_args():
    sig = inspect.signature(smm::SmmElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "shortDescription" in params, "Missing parameter 'shortDescription'"
    assert "name" in params, "Missing parameter 'name'"

def test_smm::smmelement_has_description():
    assert hasattr(smm::SmmElement, "description")
    descriptor = None
    for klass in smm::SmmElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

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



def test_smm::eobject_is_not_abstract():
    assert not inspect.isabstract(smm::EObject)


def test_smm::eobject_constructor_exists():
    assert callable(smm::EObject.__init__)


def test_smm::eobject_constructor_args():
    sig = inspect.signature(smm::EObject.__init__)
    params = list(sig.parameters.keys())



def test_measurement_is_not_abstract():
    assert not inspect.isabstract(Measurement)


def test_measurement_constructor_exists():
    assert callable(Measurement.__init__)


def test_measurement_constructor_args():
    sig = inspect.signature(Measurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::grade_is_not_abstract():
    assert not inspect.isabstract(smm::Grade)


def test_smm::grade_constructor_exists():
    assert callable(smm::Grade.__init__)


def test_smm::grade_constructor_args():
    sig = inspect.signature(smm::Grade.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"

def test_smm::grade_has_value():
    assert hasattr(smm::Grade, "value")
    descriptor = None
    for klass in smm::Grade.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smm::grade_has_isBaseSupplied():
    assert hasattr(smm::Grade, "isBaseSupplied")
    descriptor = None
    for klass in smm::Grade.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_smm::ranking_is_not_abstract():
    assert not inspect.isabstract(smm::Ranking)


def test_smm::ranking_constructor_exists():
    assert callable(smm::Ranking.__init__)


def test_smm::ranking_constructor_args():
    sig = inspect.signature(smm::Ranking.__init__)
    params = list(sig.parameters.keys())



def test_directmeasure_is_not_abstract():
    assert not inspect.isabstract(DirectMeasure)


def test_directmeasure_constructor_exists():
    assert callable(DirectMeasure.__init__)


def test_directmeasure_constructor_args():
    sig = inspect.signature(DirectMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::counting_is_not_abstract():
    assert not inspect.isabstract(smm::Counting)


def test_smm::counting_constructor_exists():
    assert callable(smm::Counting.__init__)


def test_smm::counting_constructor_args():
    sig = inspect.signature(smm::Counting.__init__)
    params = list(sig.parameters.keys())



def test_directmeasurement_is_not_abstract():
    assert not inspect.isabstract(DirectMeasurement)


def test_directmeasurement_constructor_exists():
    assert callable(DirectMeasurement.__init__)


def test_directmeasurement_constructor_args():
    sig = inspect.signature(DirectMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::count_is_not_abstract():
    assert not inspect.isabstract(smm::Count)


def test_smm::count_constructor_exists():
    assert callable(smm::Count.__init__)


def test_smm::count_constructor_args():
    sig = inspect.signature(smm::Count.__init__)
    params = list(sig.parameters.keys())



def test_abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(AbstractMeasureElement)


def test_abstractmeasureelement_constructor_exists():
    assert callable(AbstractMeasureElement.__init__)


def test_abstractmeasureelement_constructor_args():
    sig = inspect.signature(AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())



def test_smm::scope_is_not_abstract():
    assert not inspect.isabstract(smm::Scope)


def test_smm::scope_constructor_exists():
    assert callable(smm::Scope.__init__)


def test_smm::scope_constructor_args():
    sig = inspect.signature(smm::Scope.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_smm::scope_has_class_():
    assert hasattr(smm::Scope, "class_")
    descriptor = None
    for klass in smm::Scope.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_smm::ocloperation_is_not_abstract():
    assert not inspect.isabstract(smm::OCLOperation)


def test_smm::ocloperation_constructor_exists():
    assert callable(smm::OCLOperation.__init__)


def test_smm::ocloperation_constructor_args():
    sig = inspect.signature(smm::OCLOperation.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"
    assert "body" in params, "Missing parameter 'body'"

def test_smm::ocloperation_has_context():
    assert hasattr(smm::OCLOperation, "context")
    descriptor = None
    for klass in smm::OCLOperation.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_smm::ocloperation_has_body():
    assert hasattr(smm::OCLOperation, "body")
    descriptor = None
    for klass in smm::OCLOperation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_smm::measure_is_not_abstract():
    assert not inspect.isabstract(smm::Measure)


def test_smm::measure_constructor_exists():
    assert callable(smm::Measure.__init__)


def test_smm::measure_constructor_args():
    sig = inspect.signature(smm::Measure.__init__)
    params = list(sig.parameters.keys())
    assert "measureLabelFormat" in params, "Missing parameter 'measureLabelFormat'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "measurementLabelFormat" in params, "Missing parameter 'measurementLabelFormat'"

def test_smm::measure_has_measureLabelFormat():
    assert hasattr(smm::Measure, "measureLabelFormat")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "measureLabelFormat" in klass.__dict__:
            descriptor = klass.__dict__["measureLabelFormat"]
            break
    assert isinstance(descriptor, property)

def test_smm::measure_has_visible():
    assert hasattr(smm::Measure, "visible")
    descriptor = None
    for klass in smm::Measure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
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



def test_smm::characteristic_is_not_abstract():
    assert not inspect.isabstract(smm::Characteristic)


def test_smm::characteristic_constructor_exists():
    assert callable(smm::Characteristic.__init__)


def test_smm::characteristic_constructor_args():
    sig = inspect.signature(smm::Characteristic.__init__)
    params = list(sig.parameters.keys())



def test_smm::measurecategory_is_not_abstract():
    assert not inspect.isabstract(smm::MeasureCategory)


def test_smm::measurecategory_constructor_exists():
    assert callable(smm::MeasureCategory.__init__)


def test_smm::measurecategory_constructor_args():
    sig = inspect.signature(smm::MeasureCategory.__init__)
    params = list(sig.parameters.keys())



def test_smmrelationship_is_not_abstract():
    assert not inspect.isabstract(SmmRelationship)


def test_smmrelationship_constructor_exists():
    assert callable(SmmRelationship.__init__)


def test_smmrelationship_constructor_args():
    sig = inspect.signature(SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::observedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::ObservedMeasure)


def test_smm::observedmeasure_constructor_exists():
    assert callable(smm::ObservedMeasure.__init__)


def test_smm::observedmeasure_constructor_args():
    sig = inspect.signature(smm::ObservedMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::MeasureRelationship)


def test_smm::measurerelationship_constructor_exists():
    assert callable(smm::MeasureRelationship.__init__)


def test_smm::measurerelationship_constructor_args():
    sig = inspect.signature(smm::MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::MeasurementRelationship)


def test_smm::measurementrelationship_constructor_exists():
    assert callable(smm::MeasurementRelationship.__init__)


def test_smm::measurementrelationship_constructor_args():
    sig = inspect.signature(smm::MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasure)


def test_dimensionalmeasure_constructor_exists():
    assert callable(DimensionalMeasure.__init__)


def test_dimensionalmeasure_constructor_args():
    sig = inspect.signature(DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::directmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::DirectMeasure)


def test_smm::directmeasure_constructor_exists():
    assert callable(smm::DirectMeasure.__init__)


def test_smm::directmeasure_constructor_args():
    sig = inspect.signature(smm::DirectMeasure.__init__)
    params = list(sig.parameters.keys())



def test_smm::rescaledmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::RescaledMeasure)


def test_smm::rescaledmeasure_constructor_exists():
    assert callable(smm::RescaledMeasure.__init__)


def test_smm::rescaledmeasure_constructor_args():
    sig = inspect.signature(smm::RescaledMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"

def test_smm::rescaledmeasure_has_formula():
    assert hasattr(smm::RescaledMeasure, "formula")
    descriptor = None
    for klass in smm::RescaledMeasure.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_smm::namedmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::NamedMeasure)


def test_smm::namedmeasure_constructor_exists():
    assert callable(smm::NamedMeasure.__init__)


def test_smm::namedmeasure_constructor_args():
    sig = inspect.signature(smm::NamedMeasure.__init__)
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



def test_smm::dimensionalmeasure_is_not_abstract():
    assert not inspect.isabstract(smm::DimensionalMeasure)


def test_smm::dimensionalmeasure_constructor_exists():
    assert callable(smm::DimensionalMeasure.__init__)


def test_smm::dimensionalmeasure_constructor_args():
    sig = inspect.signature(smm::DimensionalMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_smm::dimensionalmeasure_has_unit():
    assert hasattr(smm::DimensionalMeasure, "unit")
    descriptor = None
    for klass in smm::DimensionalMeasure.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



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



def test_measurerelationship_is_not_abstract():
    assert not inspect.isabstract(MeasureRelationship)


def test_measurerelationship_constructor_exists():
    assert callable(MeasureRelationship.__init__)


def test_measurerelationship_constructor_args():
    sig = inspect.signature(MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::rankingmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RankingMeasureRelationship)


def test_smm::rankingmeasurerelationship_constructor_exists():
    assert callable(smm::RankingMeasureRelationship.__init__)


def test_smm::rankingmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RankingMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::equivalentmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::EquivalentMeasureRelationship)


def test_smm::equivalentmeasurerelationship_constructor_exists():
    assert callable(smm::EquivalentMeasureRelationship.__init__)


def test_smm::equivalentmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::EquivalentMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::refinementmeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RefinementMeasureRelationship)


def test_smm::refinementmeasurerelationship_constructor_exists():
    assert callable(smm::RefinementMeasureRelationship.__init__)


def test_smm::refinementmeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RefinementMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::rescalemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RescaleMeasureRelationship)


def test_smm::rescalemeasurerelationship_constructor_exists():
    assert callable(smm::RescaleMeasureRelationship.__init__)


def test_smm::rescalemeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RescaleMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::recursivemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RecursiveMeasureRelationship)


def test_smm::recursivemeasurerelationship_constructor_exists():
    assert callable(smm::RecursiveMeasureRelationship.__init__)


def test_smm::recursivemeasurerelationship_constructor_args():
    sig = inspect.signature(smm::RecursiveMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base2measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base2MeasureRelationship)


def test_smm::base2measurerelationship_constructor_exists():
    assert callable(smm::Base2MeasureRelationship.__init__)


def test_smm::base2measurerelationship_constructor_args():
    sig = inspect.signature(smm::Base2MeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::basemeasurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::BaseMeasureRelationship)


def test_smm::basemeasurerelationship_constructor_exists():
    assert callable(smm::BaseMeasureRelationship.__init__)


def test_smm::basemeasurerelationship_constructor_args():
    sig = inspect.signature(smm::BaseMeasureRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base1measurerelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base1MeasureRelationship)


def test_smm::base1measurerelationship_constructor_exists():
    assert callable(smm::Base1MeasureRelationship.__init__)


def test_smm::base1measurerelationship_constructor_args():
    sig = inspect.signature(smm::Base1MeasureRelationship.__init__)
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



def test_smm::recursivemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RecursiveMeasurementRelationship)


def test_smm::recursivemeasurementrelationship_constructor_exists():
    assert callable(smm::RecursiveMeasurementRelationship.__init__)


def test_smm::recursivemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RecursiveMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::refinementmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RefinementMeasurementRelationship)


def test_smm::refinementmeasurementrelationship_constructor_exists():
    assert callable(smm::RefinementMeasurementRelationship.__init__)


def test_smm::refinementmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RefinementMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::rescalemeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RescaleMeasurementRelationship)


def test_smm::rescalemeasurementrelationship_constructor_exists():
    assert callable(smm::RescaleMeasurementRelationship.__init__)


def test_smm::rescalemeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RescaleMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::rankingmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::RankingMeasurementRelationship)


def test_smm::rankingmeasurementrelationship_constructor_exists():
    assert callable(smm::RankingMeasurementRelationship.__init__)


def test_smm::rankingmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::RankingMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::equivalentmeasurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::EquivalentMeasurementRelationship)


def test_smm::equivalentmeasurementrelationship_constructor_exists():
    assert callable(smm::EquivalentMeasurementRelationship.__init__)


def test_smm::equivalentmeasurementrelationship_constructor_args():
    sig = inspect.signature(smm::EquivalentMeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base2measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base2MeasurementRelationship)


def test_smm::base2measurementrelationship_constructor_exists():
    assert callable(smm::Base2MeasurementRelationship.__init__)


def test_smm::base2measurementrelationship_constructor_args():
    sig = inspect.signature(smm::Base2MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::base1measurementrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::Base1MeasurementRelationship)


def test_smm::base1measurementrelationship_constructor_exists():
    assert callable(smm::Base1MeasurementRelationship.__init__)


def test_smm::base1measurementrelationship_constructor_args():
    sig = inspect.signature(smm::Base1MeasurementRelationship.__init__)
    params = list(sig.parameters.keys())



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



def test_dimensionalmeasurement_is_not_abstract():
    assert not inspect.isabstract(DimensionalMeasurement)


def test_dimensionalmeasurement_constructor_exists():
    assert callable(DimensionalMeasurement.__init__)


def test_dimensionalmeasurement_constructor_args():
    sig = inspect.signature(DimensionalMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_smm::collectivemeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::CollectiveMeasurement)


def test_smm::collectivemeasurement_constructor_exists():
    assert callable(smm::CollectiveMeasurement.__init__)


def test_smm::collectivemeasurement_constructor_args():
    sig = inspect.signature(smm::CollectiveMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSupplied" in params, "Missing parameter 'isBaseSupplied'"
    assert "accumulator" in params, "Missing parameter 'accumulator'"

def test_smm::collectivemeasurement_has_isBaseSupplied():
    assert hasattr(smm::CollectiveMeasurement, "isBaseSupplied")
    descriptor = None
    for klass in smm::CollectiveMeasurement.__mro__:
        if "isBaseSupplied" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSupplied"]
            break
    assert isinstance(descriptor, property)

def test_smm::collectivemeasurement_has_accumulator():
    assert hasattr(smm::CollectiveMeasurement, "accumulator")
    descriptor = None
    for klass in smm::CollectiveMeasurement.__mro__:
        if "accumulator" in klass.__dict__:
            descriptor = klass.__dict__["accumulator"]
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



def test_smm::aggregatedmeasurement_is_not_abstract():
    assert not inspect.isabstract(smm::AggregatedMeasurement)


def test_smm::aggregatedmeasurement_constructor_exists():
    assert callable(smm::AggregatedMeasurement.__init__)


def test_smm::aggregatedmeasurement_constructor_args():
    sig = inspect.signature(smm::AggregatedMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "isBaseSuppled" in params, "Missing parameter 'isBaseSuppled'"

def test_smm::aggregatedmeasurement_has_isBaseSuppled():
    assert hasattr(smm::AggregatedMeasurement, "isBaseSuppled")
    descriptor = None
    for klass in smm::AggregatedMeasurement.__mro__:
        if "isBaseSuppled" in klass.__dict__:
            descriptor = klass.__dict__["isBaseSuppled"]
            break
    assert isinstance(descriptor, property)



def test_smm::categoryrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::CategoryRelationship)


def test_smm::categoryrelationship_constructor_exists():
    assert callable(smm::CategoryRelationship.__init__)


def test_smm::categoryrelationship_constructor_args():
    sig = inspect.signature(smm::CategoryRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smmelement_is_not_abstract():
    assert not inspect.isabstract(SmmElement)


def test_smmelement_constructor_exists():
    assert callable(SmmElement.__init__)


def test_smmelement_constructor_args():
    sig = inspect.signature(SmmElement.__init__)
    params = list(sig.parameters.keys())



def test_smm::smmrelationship_is_not_abstract():
    assert not inspect.isabstract(smm::SmmRelationship)


def test_smm::smmrelationship_constructor_exists():
    assert callable(smm::SmmRelationship.__init__)


def test_smm::smmrelationship_constructor_args():
    sig = inspect.signature(smm::SmmRelationship.__init__)
    params = list(sig.parameters.keys())



def test_smm::rankinginterval_is_not_abstract():
    assert not inspect.isabstract(smm::RankingInterval)


def test_smm::rankinginterval_constructor_exists():
    assert callable(smm::RankingInterval.__init__)


def test_smm::rankinginterval_constructor_args():
    sig = inspect.signature(smm::RankingInterval.__init__)
    params = list(sig.parameters.keys())
    assert "minimumOpen" in params, "Missing parameter 'minimumOpen'"
    assert "minimumEndpoint" in params, "Missing parameter 'minimumEndpoint'"
    assert "maximumEndpoint" in params, "Missing parameter 'maximumEndpoint'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "maximumOpen" in params, "Missing parameter 'maximumOpen'"

def test_smm::rankinginterval_has_minimumOpen():
    assert hasattr(smm::RankingInterval, "minimumOpen")
    descriptor = None
    for klass in smm::RankingInterval.__mro__:
        if "minimumOpen" in klass.__dict__:
            descriptor = klass.__dict__["minimumOpen"]
            break
    assert isinstance(descriptor, property)

def test_smm::rankinginterval_has_minimumEndpoint():
    assert hasattr(smm::RankingInterval, "minimumEndpoint")
    descriptor = None
    for klass in smm::RankingInterval.__mro__:
        if "minimumEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["minimumEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_smm::rankinginterval_has_maximumEndpoint():
    assert hasattr(smm::RankingInterval, "maximumEndpoint")
    descriptor = None
    for klass in smm::RankingInterval.__mro__:
        if "maximumEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["maximumEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_smm::rankinginterval_has_symbol():
    assert hasattr(smm::RankingInterval, "symbol")
    descriptor = None
    for klass in smm::RankingInterval.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_smm::rankinginterval_has_maximumOpen():
    assert hasattr(smm::RankingInterval, "maximumOpen")
    descriptor = None
    for klass in smm::RankingInterval.__mro__:
        if "maximumOpen" in klass.__dict__:
            descriptor = klass.__dict__["maximumOpen"]
            break
    assert isinstance(descriptor, property)



def test_smm::argument_is_not_abstract():
    assert not inspect.isabstract(smm::Argument)


def test_smm::argument_constructor_exists():
    assert callable(smm::Argument.__init__)


def test_smm::argument_constructor_args():
    sig = inspect.signature(smm::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_smm::argument_has_value():
    assert hasattr(smm::Argument, "value")
    descriptor = None
    for klass in smm::Argument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smm::argument_has_type():
    assert hasattr(smm::Argument, "type")
    descriptor = None
    for klass in smm::Argument.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



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



def test_smm::smmmodel_is_not_abstract():
    assert not inspect.isabstract(smm::SmmModel)


def test_smm::smmmodel_constructor_exists():
    assert callable(smm::SmmModel.__init__)


def test_smm::smmmodel_constructor_args():
    sig = inspect.signature(smm::SmmModel.__init__)
    params = list(sig.parameters.keys())



def test_smm::observation_is_not_abstract():
    assert not inspect.isabstract(smm::Observation)


def test_smm::observation_constructor_exists():
    assert callable(smm::Observation.__init__)


def test_smm::observation_constructor_args():
    sig = inspect.signature(smm::Observation.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"
    assert "observer" in params, "Missing parameter 'observer'"
    assert "whenObserved" in params, "Missing parameter 'whenObserved'"

def test_smm::observation_has_tool():
    assert hasattr(smm::Observation, "tool")
    descriptor = None
    for klass in smm::Observation.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_smm::observation_has_observer():
    assert hasattr(smm::Observation, "observer")
    descriptor = None
    for klass in smm::Observation.__mro__:
        if "observer" in klass.__dict__:
            descriptor = klass.__dict__["observer"]
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



def test_smm::attribute_is_not_abstract():
    assert not inspect.isabstract(smm::Attribute)


def test_smm::attribute_constructor_exists():
    assert callable(smm::Attribute.__init__)


def test_smm::attribute_constructor_args():
    sig = inspect.signature(smm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_smm::attribute_has_value():
    assert hasattr(smm::Attribute, "value")
    descriptor = None
    for klass in smm::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smm::attribute_has_tag():
    assert hasattr(smm::Attribute, "tag")
    descriptor = None
    for klass in smm::Attribute.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_smm::measurelibrary_is_not_abstract():
    assert not inspect.isabstract(smm::MeasureLibrary)


def test_smm::measurelibrary_constructor_exists():
    assert callable(smm::MeasureLibrary.__init__)


def test_smm::measurelibrary_constructor_args():
    sig = inspect.signature(smm::MeasureLibrary.__init__)
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
    assert "error" in params, "Missing parameter 'error'"
    assert "breakValue" in params, "Missing parameter 'breakValue'"

def test_smm::measurement_has_error():
    assert hasattr(smm::Measurement, "error")
    descriptor = None
    for klass in smm::Measurement.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_smm::measurement_has_breakValue():
    assert hasattr(smm::Measurement, "breakValue")
    descriptor = None
    for klass in smm::Measurement.__mro__:
        if "breakValue" in klass.__dict__:
            descriptor = klass.__dict__["breakValue"]
            break
    assert isinstance(descriptor, property)



def test_smm::abstractmeasureelement_is_not_abstract():
    assert not inspect.isabstract(smm::AbstractMeasureElement)


def test_smm::abstractmeasureelement_constructor_exists():
    assert callable(smm::AbstractMeasureElement.__init__)


def test_smm::abstractmeasureelement_constructor_args():
    sig = inspect.signature(smm::AbstractMeasureElement.__init__)
    params = list(sig.parameters.keys())

def test_accumulator_exists():
    # Check that the Enumeration exists
    assert Accumulator is not None

def test_accumulator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Accumulator]
    expected_literals = [
        "minimum",
        "standardDeviation",
        "maximum",
        "sum",
        "average",
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
smm::SmmElement_strategy = st.builds(
    smm::SmmElement,
    description=
        safe_text,
    shortDescription=
        safe_text,
    name=
        safe_text
)
smm::EObject_strategy = st.builds(
    smm::EObject,
)
Measurement_strategy = st.builds(
    Measurement,
)
smm::Grade_strategy = st.builds(
    smm::Grade,
    value=
        safe_text,
    isBaseSupplied=
        st.booleans()
)
Measure_strategy = st.builds(
    Measure,
)
smm::Ranking_strategy = st.builds(
    smm::Ranking,
)
DirectMeasure_strategy = st.builds(
    DirectMeasure,
)
smm::Counting_strategy = st.builds(
    smm::Counting,
)
DirectMeasurement_strategy = st.builds(
    DirectMeasurement,
)
smm::Count_strategy = st.builds(
    smm::Count,
)
AbstractMeasureElement_strategy = st.builds(
    AbstractMeasureElement,
)
smm::Scope_strategy = st.builds(
    smm::Scope,
    class_=
        safe_text
)
smm::OCLOperation_strategy = st.builds(
    smm::OCLOperation,
    context=
        safe_text,
    body=
        safe_text
)
smm::Measure_strategy = st.builds(
    smm::Measure,
    measureLabelFormat=
        safe_text,
    visible=
        st.booleans(),
    measurementLabelFormat=
        safe_text
)
smm::Operation_strategy = st.builds(
    smm::Operation,
    language=
        safe_text,
    body=
        safe_text
)
smm::Characteristic_strategy = st.builds(
    smm::Characteristic,
)
smm::MeasureCategory_strategy = st.builds(
    smm::MeasureCategory,
)
SmmRelationship_strategy = st.builds(
    SmmRelationship,
)
smm::ObservedMeasure_strategy = st.builds(
    smm::ObservedMeasure,
)
smm::MeasureRelationship_strategy = st.builds(
    smm::MeasureRelationship,
)
smm::MeasurementRelationship_strategy = st.builds(
    smm::MeasurementRelationship,
)
DimensionalMeasure_strategy = st.builds(
    DimensionalMeasure,
)
smm::DirectMeasure_strategy = st.builds(
    smm::DirectMeasure,
)
smm::RescaledMeasure_strategy = st.builds(
    smm::RescaledMeasure,
    formula=
        safe_text
)
smm::NamedMeasure_strategy = st.builds(
    smm::NamedMeasure,
)
smm::CollectiveMeasure_strategy = st.builds(
    smm::CollectiveMeasure,
    accumulator=
        safe_text
)
smm::DimensionalMeasure_strategy = st.builds(
    smm::DimensionalMeasure,
    unit=
        safe_text
)
smm::BinaryMeasure_strategy = st.builds(
    smm::BinaryMeasure,
    functor=
        safe_text
)
MeasureRelationship_strategy = st.builds(
    MeasureRelationship,
)
smm::RankingMeasureRelationship_strategy = st.builds(
    smm::RankingMeasureRelationship,
)
smm::EquivalentMeasureRelationship_strategy = st.builds(
    smm::EquivalentMeasureRelationship,
)
smm::RefinementMeasureRelationship_strategy = st.builds(
    smm::RefinementMeasureRelationship,
)
smm::RescaleMeasureRelationship_strategy = st.builds(
    smm::RescaleMeasureRelationship,
)
smm::RecursiveMeasureRelationship_strategy = st.builds(
    smm::RecursiveMeasureRelationship,
)
smm::Base2MeasureRelationship_strategy = st.builds(
    smm::Base2MeasureRelationship,
)
smm::BaseMeasureRelationship_strategy = st.builds(
    smm::BaseMeasureRelationship,
)
smm::Base1MeasureRelationship_strategy = st.builds(
    smm::Base1MeasureRelationship,
)
MeasurementRelationship_strategy = st.builds(
    MeasurementRelationship,
)
smm::BaseMeasurementRelationship_strategy = st.builds(
    smm::BaseMeasurementRelationship,
)
smm::RecursiveMeasurementRelationship_strategy = st.builds(
    smm::RecursiveMeasurementRelationship,
)
smm::RefinementMeasurementRelationship_strategy = st.builds(
    smm::RefinementMeasurementRelationship,
)
smm::RescaleMeasurementRelationship_strategy = st.builds(
    smm::RescaleMeasurementRelationship,
)
smm::RankingMeasurementRelationship_strategy = st.builds(
    smm::RankingMeasurementRelationship,
)
smm::EquivalentMeasurementRelationship_strategy = st.builds(
    smm::EquivalentMeasurementRelationship,
)
smm::Base2MeasurementRelationship_strategy = st.builds(
    smm::Base2MeasurementRelationship,
)
smm::Base1MeasurementRelationship_strategy = st.builds(
    smm::Base1MeasurementRelationship,
)
smm::DimensionalMeasurement_strategy = st.builds(
    smm::DimensionalMeasurement,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
DimensionalMeasurement_strategy = st.builds(
    DimensionalMeasurement,
)
smm::CollectiveMeasurement_strategy = st.builds(
    smm::CollectiveMeasurement,
    isBaseSupplied=
        st.booleans(),
    accumulator=
        safe_text
)
smm::BinaryMeasurement_strategy = st.builds(
    smm::BinaryMeasurement,
    isBaseSupplied=
        st.booleans()
)
smm::RescaledMeasurement_strategy = st.builds(
    smm::RescaledMeasurement,
    isBaseSupplied=
        st.booleans()
)
smm::DirectMeasurement_strategy = st.builds(
    smm::DirectMeasurement,
)
smm::NamedMeasurement_strategy = st.builds(
    smm::NamedMeasurement,
)
smm::AggregatedMeasurement_strategy = st.builds(
    smm::AggregatedMeasurement,
    isBaseSuppled=
        st.booleans()
)
smm::CategoryRelationship_strategy = st.builds(
    smm::CategoryRelationship,
)
SmmElement_strategy = st.builds(
    SmmElement,
)
smm::SmmRelationship_strategy = st.builds(
    smm::SmmRelationship,
)
smm::RankingInterval_strategy = st.builds(
    smm::RankingInterval,
    minimumOpen=
        st.booleans(),
    minimumEndpoint=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maximumEndpoint=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    symbol=
        safe_text,
    maximumOpen=
        st.booleans()
)
smm::Argument_strategy = st.builds(
    smm::Argument,
    value=
        safe_text,
    type=
        safe_text
)
smm::Annotation_strategy = st.builds(
    smm::Annotation,
    text=
        safe_text
)
smm::SmmModel_strategy = st.builds(
    smm::SmmModel,
)
smm::Observation_strategy = st.builds(
    smm::Observation,
    tool=
        safe_text,
    observer=
        safe_text,
    whenObserved=
        safe_text
)
smm::Attribute_strategy = st.builds(
    smm::Attribute,
    value=
        safe_text,
    tag=
        safe_text
)
smm::MeasureLibrary_strategy = st.builds(
    smm::MeasureLibrary,
)
smm::ObservationScope_strategy = st.builds(
    smm::ObservationScope,
    scopeUri=
        safe_text
)
smm::Measurement_strategy = st.builds(
    smm::Measurement,
    error=
        safe_text,
    breakValue=
        safe_text
)
smm::AbstractMeasureElement_strategy = st.builds(
    smm::AbstractMeasureElement,
)

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

@given(instance=smm::SmmElement_strategy)
@settings(max_examples=50)
def test_smm::smmelement_instantiation(instance):
    assert isinstance(instance, smm::SmmElement)

@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=smm::SmmElement_strategy)
def test_smm::smmelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

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

@given(instance=smm::EObject_strategy)
@settings(max_examples=50)
def test_smm::eobject_instantiation(instance):
    assert isinstance(instance, smm::EObject)

@given(instance=Measurement_strategy)
@settings(max_examples=50)
def test_measurement_instantiation(instance):
    assert isinstance(instance, Measurement)

@given(instance=smm::Grade_strategy)
@settings(max_examples=50)
def test_smm::grade_instantiation(instance):
    assert isinstance(instance, smm::Grade)

@given(instance=smm::Grade_strategy)
def test_smm::grade_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smm::Grade_strategy)
def test_smm::grade_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::Grade_strategy)
def test_smm::grade_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, bool)


@given(instance=smm::Grade_strategy)
def test_smm::grade_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=smm::Ranking_strategy)
@settings(max_examples=50)
def test_smm::ranking_instantiation(instance):
    assert isinstance(instance, smm::Ranking)

@given(instance=DirectMeasure_strategy)
@settings(max_examples=50)
def test_directmeasure_instantiation(instance):
    assert isinstance(instance, DirectMeasure)

@given(instance=smm::Counting_strategy)
@settings(max_examples=50)
def test_smm::counting_instantiation(instance):
    assert isinstance(instance, smm::Counting)

@given(instance=DirectMeasurement_strategy)
@settings(max_examples=50)
def test_directmeasurement_instantiation(instance):
    assert isinstance(instance, DirectMeasurement)

@given(instance=smm::Count_strategy)
@settings(max_examples=50)
def test_smm::count_instantiation(instance):
    assert isinstance(instance, smm::Count)

@given(instance=AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, AbstractMeasureElement)

@given(instance=smm::Scope_strategy)
@settings(max_examples=50)
def test_smm::scope_instantiation(instance):
    assert isinstance(instance, smm::Scope)

@given(instance=smm::Scope_strategy)
def test_smm::scope_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=smm::Scope_strategy)
def test_smm::scope_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=smm::OCLOperation_strategy)
@settings(max_examples=50)
def test_smm::ocloperation_instantiation(instance):
    assert isinstance(instance, smm::OCLOperation)

@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=smm::OCLOperation_strategy)
def test_smm::ocloperation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=smm::Measure_strategy)
@settings(max_examples=50)
def test_smm::measure_instantiation(instance):
    assert isinstance(instance, smm::Measure)

@given(instance=smm::Measure_strategy)
def test_smm::measure_measureLabelFormat_type(instance):
    assert isinstance(instance.measureLabelFormat, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_measureLabelFormat_setter(instance):
    original = instance.measureLabelFormat
    instance.measureLabelFormat = original
    assert instance.measureLabelFormat == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=smm::Measure_strategy)
def test_smm::measure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=smm::Measure_strategy)
def test_smm::measure_measurementLabelFormat_type(instance):
    assert isinstance(instance.measurementLabelFormat, str)


@given(instance=smm::Measure_strategy)
def test_smm::measure_measurementLabelFormat_setter(instance):
    original = instance.measurementLabelFormat
    instance.measurementLabelFormat = original
    assert instance.measurementLabelFormat == original

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

@given(instance=smm::Characteristic_strategy)
@settings(max_examples=50)
def test_smm::characteristic_instantiation(instance):
    assert isinstance(instance, smm::Characteristic)

@given(instance=smm::MeasureCategory_strategy)
@settings(max_examples=50)
def test_smm::measurecategory_instantiation(instance):
    assert isinstance(instance, smm::MeasureCategory)

@given(instance=SmmRelationship_strategy)
@settings(max_examples=50)
def test_smmrelationship_instantiation(instance):
    assert isinstance(instance, SmmRelationship)

@given(instance=smm::ObservedMeasure_strategy)
@settings(max_examples=50)
def test_smm::observedmeasure_instantiation(instance):
    assert isinstance(instance, smm::ObservedMeasure)

@given(instance=smm::MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::measurerelationship_instantiation(instance):
    assert isinstance(instance, smm::MeasureRelationship)

@given(instance=smm::MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::MeasurementRelationship)

@given(instance=DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, DimensionalMeasure)

@given(instance=smm::DirectMeasure_strategy)
@settings(max_examples=50)
def test_smm::directmeasure_instantiation(instance):
    assert isinstance(instance, smm::DirectMeasure)

@given(instance=smm::RescaledMeasure_strategy)
@settings(max_examples=50)
def test_smm::rescaledmeasure_instantiation(instance):
    assert isinstance(instance, smm::RescaledMeasure)

@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=smm::RescaledMeasure_strategy)
def test_smm::rescaledmeasure_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=smm::NamedMeasure_strategy)
@settings(max_examples=50)
def test_smm::namedmeasure_instantiation(instance):
    assert isinstance(instance, smm::NamedMeasure)

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

@given(instance=smm::DimensionalMeasure_strategy)
@settings(max_examples=50)
def test_smm::dimensionalmeasure_instantiation(instance):
    assert isinstance(instance, smm::DimensionalMeasure)

@given(instance=smm::DimensionalMeasure_strategy)
def test_smm::dimensionalmeasure_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=smm::DimensionalMeasure_strategy)
def test_smm::dimensionalmeasure_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

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

@given(instance=MeasureRelationship_strategy)
@settings(max_examples=50)
def test_measurerelationship_instantiation(instance):
    assert isinstance(instance, MeasureRelationship)

@given(instance=smm::RankingMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::rankingmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RankingMeasureRelationship)

@given(instance=smm::EquivalentMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::equivalentmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::EquivalentMeasureRelationship)

@given(instance=smm::RefinementMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::refinementmeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RefinementMeasureRelationship)

@given(instance=smm::RescaleMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::rescalemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RescaleMeasureRelationship)

@given(instance=smm::RecursiveMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::recursivemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::RecursiveMeasureRelationship)

@given(instance=smm::Base2MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::base2measurerelationship_instantiation(instance):
    assert isinstance(instance, smm::Base2MeasureRelationship)

@given(instance=smm::BaseMeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::basemeasurerelationship_instantiation(instance):
    assert isinstance(instance, smm::BaseMeasureRelationship)

@given(instance=smm::Base1MeasureRelationship_strategy)
@settings(max_examples=50)
def test_smm::base1measurerelationship_instantiation(instance):
    assert isinstance(instance, smm::Base1MeasureRelationship)

@given(instance=MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_measurementrelationship_instantiation(instance):
    assert isinstance(instance, MeasurementRelationship)

@given(instance=smm::BaseMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::basemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::BaseMeasurementRelationship)

@given(instance=smm::RecursiveMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::recursivemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RecursiveMeasurementRelationship)

@given(instance=smm::RefinementMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::refinementmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RefinementMeasurementRelationship)

@given(instance=smm::RescaleMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::rescalemeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RescaleMeasurementRelationship)

@given(instance=smm::RankingMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::rankingmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::RankingMeasurementRelationship)

@given(instance=smm::EquivalentMeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::equivalentmeasurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::EquivalentMeasurementRelationship)

@given(instance=smm::Base2MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::base2measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::Base2MeasurementRelationship)

@given(instance=smm::Base1MeasurementRelationship_strategy)
@settings(max_examples=50)
def test_smm::base1measurementrelationship_instantiation(instance):
    assert isinstance(instance, smm::Base1MeasurementRelationship)

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

@given(instance=DimensionalMeasurement_strategy)
@settings(max_examples=50)
def test_dimensionalmeasurement_instantiation(instance):
    assert isinstance(instance, DimensionalMeasurement)

@given(instance=smm::CollectiveMeasurement_strategy)
@settings(max_examples=50)
def test_smm::collectivemeasurement_instantiation(instance):
    assert isinstance(instance, smm::CollectiveMeasurement)

@given(instance=smm::CollectiveMeasurement_strategy)
def test_smm::collectivemeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, bool)


@given(instance=smm::CollectiveMeasurement_strategy)
def test_smm::collectivemeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::CollectiveMeasurement_strategy)
def test_smm::collectivemeasurement_accumulator_type(instance):
    assert isinstance(instance.accumulator, str)


@given(instance=smm::CollectiveMeasurement_strategy)
def test_smm::collectivemeasurement_accumulator_setter(instance):
    original = instance.accumulator
    instance.accumulator = original
    assert instance.accumulator == original

@given(instance=smm::BinaryMeasurement_strategy)
@settings(max_examples=50)
def test_smm::binarymeasurement_instantiation(instance):
    assert isinstance(instance, smm::BinaryMeasurement)

@given(instance=smm::BinaryMeasurement_strategy)
def test_smm::binarymeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, bool)


@given(instance=smm::BinaryMeasurement_strategy)
def test_smm::binarymeasurement_isBaseSupplied_setter(instance):
    original = instance.isBaseSupplied
    instance.isBaseSupplied = original
    assert instance.isBaseSupplied == original

@given(instance=smm::RescaledMeasurement_strategy)
@settings(max_examples=50)
def test_smm::rescaledmeasurement_instantiation(instance):
    assert isinstance(instance, smm::RescaledMeasurement)

@given(instance=smm::RescaledMeasurement_strategy)
def test_smm::rescaledmeasurement_isBaseSupplied_type(instance):
    assert isinstance(instance.isBaseSupplied, bool)


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

@given(instance=smm::AggregatedMeasurement_strategy)
@settings(max_examples=50)
def test_smm::aggregatedmeasurement_instantiation(instance):
    assert isinstance(instance, smm::AggregatedMeasurement)

@given(instance=smm::AggregatedMeasurement_strategy)
def test_smm::aggregatedmeasurement_isBaseSuppled_type(instance):
    assert isinstance(instance.isBaseSuppled, bool)


@given(instance=smm::AggregatedMeasurement_strategy)
def test_smm::aggregatedmeasurement_isBaseSuppled_setter(instance):
    original = instance.isBaseSuppled
    instance.isBaseSuppled = original
    assert instance.isBaseSuppled == original

@given(instance=smm::CategoryRelationship_strategy)
@settings(max_examples=50)
def test_smm::categoryrelationship_instantiation(instance):
    assert isinstance(instance, smm::CategoryRelationship)

@given(instance=SmmElement_strategy)
@settings(max_examples=50)
def test_smmelement_instantiation(instance):
    assert isinstance(instance, SmmElement)

@given(instance=smm::SmmRelationship_strategy)
@settings(max_examples=50)
def test_smm::smmrelationship_instantiation(instance):
    assert isinstance(instance, smm::SmmRelationship)

@given(instance=smm::RankingInterval_strategy)
@settings(max_examples=50)
def test_smm::rankinginterval_instantiation(instance):
    assert isinstance(instance, smm::RankingInterval)

@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_minimumOpen_type(instance):
    assert isinstance(instance.minimumOpen, bool)


@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_minimumOpen_setter(instance):
    original = instance.minimumOpen
    instance.minimumOpen = original
    assert instance.minimumOpen == original

@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_minimumEndpoint_type(instance):
    assert isinstance(instance.minimumEndpoint, float)


@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_minimumEndpoint_setter(instance):
    original = instance.minimumEndpoint
    instance.minimumEndpoint = original
    assert instance.minimumEndpoint == original

@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_maximumEndpoint_type(instance):
    assert isinstance(instance.maximumEndpoint, float)


@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_maximumEndpoint_setter(instance):
    original = instance.maximumEndpoint
    instance.maximumEndpoint = original
    assert instance.maximumEndpoint == original

@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_maximumOpen_type(instance):
    assert isinstance(instance.maximumOpen, bool)


@given(instance=smm::RankingInterval_strategy)
def test_smm::rankinginterval_maximumOpen_setter(instance):
    original = instance.maximumOpen
    instance.maximumOpen = original
    assert instance.maximumOpen == original

@given(instance=smm::Argument_strategy)
@settings(max_examples=50)
def test_smm::argument_instantiation(instance):
    assert isinstance(instance, smm::Argument)

@given(instance=smm::Argument_strategy)
def test_smm::argument_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smm::Argument_strategy)
def test_smm::argument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::Argument_strategy)
def test_smm::argument_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=smm::Argument_strategy)
def test_smm::argument_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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

@given(instance=smm::SmmModel_strategy)
@settings(max_examples=50)
def test_smm::smmmodel_instantiation(instance):
    assert isinstance(instance, smm::SmmModel)

@given(instance=smm::Observation_strategy)
@settings(max_examples=50)
def test_smm::observation_instantiation(instance):
    assert isinstance(instance, smm::Observation)

@given(instance=smm::Observation_strategy)
def test_smm::observation_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=smm::Observation_strategy)
def test_smm::observation_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=smm::Observation_strategy)
def test_smm::observation_observer_type(instance):
    assert isinstance(instance.observer, str)


@given(instance=smm::Observation_strategy)
def test_smm::observation_observer_setter(instance):
    original = instance.observer
    instance.observer = original
    assert instance.observer == original

@given(instance=smm::Observation_strategy)
def test_smm::observation_whenObserved_type(instance):
    assert isinstance(instance.whenObserved, str)


@given(instance=smm::Observation_strategy)
def test_smm::observation_whenObserved_setter(instance):
    original = instance.whenObserved
    instance.whenObserved = original
    assert instance.whenObserved == original

@given(instance=smm::Attribute_strategy)
@settings(max_examples=50)
def test_smm::attribute_instantiation(instance):
    assert isinstance(instance, smm::Attribute)

@given(instance=smm::Attribute_strategy)
def test_smm::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smm::Attribute_strategy)
def test_smm::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smm::Attribute_strategy)
def test_smm::attribute_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=smm::Attribute_strategy)
def test_smm::attribute_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=smm::MeasureLibrary_strategy)
@settings(max_examples=50)
def test_smm::measurelibrary_instantiation(instance):
    assert isinstance(instance, smm::MeasureLibrary)

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
def test_smm::measurement_error_type(instance):
    assert isinstance(instance.error, str)


@given(instance=smm::Measurement_strategy)
def test_smm::measurement_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=smm::Measurement_strategy)
def test_smm::measurement_breakValue_type(instance):
    assert isinstance(instance.breakValue, str)


@given(instance=smm::Measurement_strategy)
def test_smm::measurement_breakValue_setter(instance):
    original = instance.breakValue
    instance.breakValue = original
    assert instance.breakValue == original

@given(instance=smm::AbstractMeasureElement_strategy)
@settings(max_examples=50)
def test_smm::abstractmeasureelement_instantiation(instance):
    assert isinstance(instance, smm::AbstractMeasureElement)
