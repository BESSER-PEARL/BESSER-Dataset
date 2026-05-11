import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Unit,
    model::BaseQuantityUnit,
    Quantity,
    model::DerivedQuantity,
    model::BaseQuantity,
    model::Sample,
    model::DerivedQuantityUnit,
    ConversionFactor,
    model::TimeConversionFactor,
    model::MassConversionFactor,
    model::LengthConversionFactor,
    MeasurementUncertaintyInformation,
    model::Sampling,
    model::Interval,
    model::NormalDistribution,
    model::LevelConversionFactor,
    model::TrafficIntensityConversionFactor,
    model::EntropyConversionFactor,
    model::DataStorageCapacityConversionFactor,
    model::AngleConversionFactor,
    model::LuminousIntensityConversionFactor,
    model::AmountOfSubstanceConversionFactor,
    model::ThermodynamicTemperatureConversionFactor,
    model::ElectricCurrentConversionFactor,
    model::MeasurementUncertaintyInformation,
    model::MeasurementUncertainty,
    Dimension,
    model::TrafficIntensityDimension,
    model::ThermodynamicTemperatureDimension,
    model::LevelDimension,
    model::DataStorageCapacityDimension,
    model::EntropyDimension,
    model::LuminousIntensityDimension,
    model::ElectricCurrentDimension,
    model::AngleDimension,
    model::TimeDimension,
    model::MassDimension,
    model::AmountOfSubstanceDimension,
    model::LengthDimension,
    model::SystemOfUnits,
    BaseQuantityUnit,
    model::ThermodynamicTemperatureUnit,
    model::EntropyUnit,
    model::ElectricCurrentUnit,
    model::TimeUnit,
    model::AngleUnit,
    model::MassUnit,
    model::TrafficIntensityUnit,
    model::LevelUnit,
    model::AmountOfSubstanceUnit,
    model::LuminousIntensityUnit,
    model::DataStorageCapacityUnit,
    model::LengthUnit,
    model::ConversionFactor,
    model::Dimension,
    BaseQuantity,
    model::LuminousIntensity,
    model::Mass,
    model::DataStorageCapacity,
    model::Level,
    model::AmountOfSubstance,
    model::ElectricCurrent,
    model::TrafficIntensity,
    model::Time,
    model::Entropy,
    model::ThermodynamicTemperature,
    model::Angle,
    model::Length,
    model::QuantityValue,
    model::Unit,
    model::Quantity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_model::basequantityunit_is_not_abstract():
    assert not inspect.isabstract(model::BaseQuantityUnit)


def test_model::basequantityunit_constructor_exists():
    assert callable(model::BaseQuantityUnit.__init__)


def test_model::basequantityunit_constructor_args():
    sig = inspect.signature(model::BaseQuantityUnit.__init__)
    params = list(sig.parameters.keys())



def test_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_model::derivedquantity_is_not_abstract():
    assert not inspect.isabstract(model::DerivedQuantity)


def test_model::derivedquantity_constructor_exists():
    assert callable(model::DerivedQuantity.__init__)


def test_model::derivedquantity_constructor_args():
    sig = inspect.signature(model::DerivedQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model::basequantity_is_not_abstract():
    assert not inspect.isabstract(model::BaseQuantity)


def test_model::basequantity_constructor_exists():
    assert callable(model::BaseQuantity.__init__)


def test_model::basequantity_constructor_args():
    sig = inspect.signature(model::BaseQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model::sample_is_not_abstract():
    assert not inspect.isabstract(model::Sample)


def test_model::sample_constructor_exists():
    assert callable(model::Sample.__init__)


def test_model::sample_constructor_args():
    sig = inspect.signature(model::Sample.__init__)
    params = list(sig.parameters.keys())



def test_model::derivedquantityunit_is_not_abstract():
    assert not inspect.isabstract(model::DerivedQuantityUnit)


def test_model::derivedquantityunit_constructor_exists():
    assert callable(model::DerivedQuantityUnit.__init__)


def test_model::derivedquantityunit_constructor_args():
    sig = inspect.signature(model::DerivedQuantityUnit.__init__)
    params = list(sig.parameters.keys())



def test_conversionfactor_is_not_abstract():
    assert not inspect.isabstract(ConversionFactor)


def test_conversionfactor_constructor_exists():
    assert callable(ConversionFactor.__init__)


def test_conversionfactor_constructor_args():
    sig = inspect.signature(ConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::timeconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::TimeConversionFactor)


def test_model::timeconversionfactor_constructor_exists():
    assert callable(model::TimeConversionFactor.__init__)


def test_model::timeconversionfactor_constructor_args():
    sig = inspect.signature(model::TimeConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::massconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::MassConversionFactor)


def test_model::massconversionfactor_constructor_exists():
    assert callable(model::MassConversionFactor.__init__)


def test_model::massconversionfactor_constructor_args():
    sig = inspect.signature(model::MassConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::lengthconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::LengthConversionFactor)


def test_model::lengthconversionfactor_constructor_exists():
    assert callable(model::LengthConversionFactor.__init__)


def test_model::lengthconversionfactor_constructor_args():
    sig = inspect.signature(model::LengthConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_measurementuncertaintyinformation_is_not_abstract():
    assert not inspect.isabstract(MeasurementUncertaintyInformation)


def test_measurementuncertaintyinformation_constructor_exists():
    assert callable(MeasurementUncertaintyInformation.__init__)


def test_measurementuncertaintyinformation_constructor_args():
    sig = inspect.signature(MeasurementUncertaintyInformation.__init__)
    params = list(sig.parameters.keys())



def test_model::sampling_is_not_abstract():
    assert not inspect.isabstract(model::Sampling)


def test_model::sampling_constructor_exists():
    assert callable(model::Sampling.__init__)


def test_model::sampling_constructor_args():
    sig = inspect.signature(model::Sampling.__init__)
    params = list(sig.parameters.keys())
    assert "measurementProcedure" in params, "Missing parameter 'measurementProcedure'"

def test_model::sampling_has_measurementProcedure():
    assert hasattr(model::Sampling, "measurementProcedure")
    descriptor = None
    for klass in model::Sampling.__mro__:
        if "measurementProcedure" in klass.__dict__:
            descriptor = klass.__dict__["measurementProcedure"]
            break
    assert isinstance(descriptor, property)



def test_model::interval_is_not_abstract():
    assert not inspect.isabstract(model::Interval)


def test_model::interval_constructor_exists():
    assert callable(model::Interval.__init__)


def test_model::interval_constructor_args():
    sig = inspect.signature(model::Interval.__init__)
    params = list(sig.parameters.keys())



def test_model::normaldistribution_is_not_abstract():
    assert not inspect.isabstract(model::NormalDistribution)


def test_model::normaldistribution_constructor_exists():
    assert callable(model::NormalDistribution.__init__)


def test_model::normaldistribution_constructor_args():
    sig = inspect.signature(model::NormalDistribution.__init__)
    params = list(sig.parameters.keys())
    assert "meanValue" in params, "Missing parameter 'meanValue'"
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"

def test_model::normaldistribution_has_meanValue():
    assert hasattr(model::NormalDistribution, "meanValue")
    descriptor = None
    for klass in model::NormalDistribution.__mro__:
        if "meanValue" in klass.__dict__:
            descriptor = klass.__dict__["meanValue"]
            break
    assert isinstance(descriptor, property)

def test_model::normaldistribution_has_standardDeviation():
    assert hasattr(model::NormalDistribution, "standardDeviation")
    descriptor = None
    for klass in model::NormalDistribution.__mro__:
        if "standardDeviation" in klass.__dict__:
            descriptor = klass.__dict__["standardDeviation"]
            break
    assert isinstance(descriptor, property)



def test_model::levelconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::LevelConversionFactor)


def test_model::levelconversionfactor_constructor_exists():
    assert callable(model::LevelConversionFactor.__init__)


def test_model::levelconversionfactor_constructor_args():
    sig = inspect.signature(model::LevelConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::trafficintensityconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::TrafficIntensityConversionFactor)


def test_model::trafficintensityconversionfactor_constructor_exists():
    assert callable(model::TrafficIntensityConversionFactor.__init__)


def test_model::trafficintensityconversionfactor_constructor_args():
    sig = inspect.signature(model::TrafficIntensityConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::entropyconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::EntropyConversionFactor)


def test_model::entropyconversionfactor_constructor_exists():
    assert callable(model::EntropyConversionFactor.__init__)


def test_model::entropyconversionfactor_constructor_args():
    sig = inspect.signature(model::EntropyConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::datastoragecapacityconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::DataStorageCapacityConversionFactor)


def test_model::datastoragecapacityconversionfactor_constructor_exists():
    assert callable(model::DataStorageCapacityConversionFactor.__init__)


def test_model::datastoragecapacityconversionfactor_constructor_args():
    sig = inspect.signature(model::DataStorageCapacityConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::angleconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::AngleConversionFactor)


def test_model::angleconversionfactor_constructor_exists():
    assert callable(model::AngleConversionFactor.__init__)


def test_model::angleconversionfactor_constructor_args():
    sig = inspect.signature(model::AngleConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::luminousintensityconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::LuminousIntensityConversionFactor)


def test_model::luminousintensityconversionfactor_constructor_exists():
    assert callable(model::LuminousIntensityConversionFactor.__init__)


def test_model::luminousintensityconversionfactor_constructor_args():
    sig = inspect.signature(model::LuminousIntensityConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::amountofsubstanceconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::AmountOfSubstanceConversionFactor)


def test_model::amountofsubstanceconversionfactor_constructor_exists():
    assert callable(model::AmountOfSubstanceConversionFactor.__init__)


def test_model::amountofsubstanceconversionfactor_constructor_args():
    sig = inspect.signature(model::AmountOfSubstanceConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::thermodynamictemperatureconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::ThermodynamicTemperatureConversionFactor)


def test_model::thermodynamictemperatureconversionfactor_constructor_exists():
    assert callable(model::ThermodynamicTemperatureConversionFactor.__init__)


def test_model::thermodynamictemperatureconversionfactor_constructor_args():
    sig = inspect.signature(model::ThermodynamicTemperatureConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::electriccurrentconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::ElectricCurrentConversionFactor)


def test_model::electriccurrentconversionfactor_constructor_exists():
    assert callable(model::ElectricCurrentConversionFactor.__init__)


def test_model::electriccurrentconversionfactor_constructor_args():
    sig = inspect.signature(model::ElectricCurrentConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model::measurementuncertaintyinformation_is_not_abstract():
    assert not inspect.isabstract(model::MeasurementUncertaintyInformation)


def test_model::measurementuncertaintyinformation_constructor_exists():
    assert callable(model::MeasurementUncertaintyInformation.__init__)


def test_model::measurementuncertaintyinformation_constructor_args():
    sig = inspect.signature(model::MeasurementUncertaintyInformation.__init__)
    params = list(sig.parameters.keys())



def test_model::measurementuncertainty_is_not_abstract():
    assert not inspect.isabstract(model::MeasurementUncertainty)


def test_model::measurementuncertainty_constructor_exists():
    assert callable(model::MeasurementUncertainty.__init__)


def test_model::measurementuncertainty_constructor_args():
    sig = inspect.signature(model::MeasurementUncertainty.__init__)
    params = list(sig.parameters.keys())
    assert "standardUncertainty" in params, "Missing parameter 'standardUncertainty'"

def test_model::measurementuncertainty_has_standardUncertainty():
    assert hasattr(model::MeasurementUncertainty, "standardUncertainty")
    descriptor = None
    for klass in model::MeasurementUncertainty.__mro__:
        if "standardUncertainty" in klass.__dict__:
            descriptor = klass.__dict__["standardUncertainty"]
            break
    assert isinstance(descriptor, property)



def test_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
    params = list(sig.parameters.keys())



def test_model::trafficintensitydimension_is_not_abstract():
    assert not inspect.isabstract(model::TrafficIntensityDimension)


def test_model::trafficintensitydimension_constructor_exists():
    assert callable(model::TrafficIntensityDimension.__init__)


def test_model::trafficintensitydimension_constructor_args():
    sig = inspect.signature(model::TrafficIntensityDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::thermodynamictemperaturedimension_is_not_abstract():
    assert not inspect.isabstract(model::ThermodynamicTemperatureDimension)


def test_model::thermodynamictemperaturedimension_constructor_exists():
    assert callable(model::ThermodynamicTemperatureDimension.__init__)


def test_model::thermodynamictemperaturedimension_constructor_args():
    sig = inspect.signature(model::ThermodynamicTemperatureDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::leveldimension_is_not_abstract():
    assert not inspect.isabstract(model::LevelDimension)


def test_model::leveldimension_constructor_exists():
    assert callable(model::LevelDimension.__init__)


def test_model::leveldimension_constructor_args():
    sig = inspect.signature(model::LevelDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::datastoragecapacitydimension_is_not_abstract():
    assert not inspect.isabstract(model::DataStorageCapacityDimension)


def test_model::datastoragecapacitydimension_constructor_exists():
    assert callable(model::DataStorageCapacityDimension.__init__)


def test_model::datastoragecapacitydimension_constructor_args():
    sig = inspect.signature(model::DataStorageCapacityDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::entropydimension_is_not_abstract():
    assert not inspect.isabstract(model::EntropyDimension)


def test_model::entropydimension_constructor_exists():
    assert callable(model::EntropyDimension.__init__)


def test_model::entropydimension_constructor_args():
    sig = inspect.signature(model::EntropyDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::luminousintensitydimension_is_not_abstract():
    assert not inspect.isabstract(model::LuminousIntensityDimension)


def test_model::luminousintensitydimension_constructor_exists():
    assert callable(model::LuminousIntensityDimension.__init__)


def test_model::luminousintensitydimension_constructor_args():
    sig = inspect.signature(model::LuminousIntensityDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::electriccurrentdimension_is_not_abstract():
    assert not inspect.isabstract(model::ElectricCurrentDimension)


def test_model::electriccurrentdimension_constructor_exists():
    assert callable(model::ElectricCurrentDimension.__init__)


def test_model::electriccurrentdimension_constructor_args():
    sig = inspect.signature(model::ElectricCurrentDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::angledimension_is_not_abstract():
    assert not inspect.isabstract(model::AngleDimension)


def test_model::angledimension_constructor_exists():
    assert callable(model::AngleDimension.__init__)


def test_model::angledimension_constructor_args():
    sig = inspect.signature(model::AngleDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::timedimension_is_not_abstract():
    assert not inspect.isabstract(model::TimeDimension)


def test_model::timedimension_constructor_exists():
    assert callable(model::TimeDimension.__init__)


def test_model::timedimension_constructor_args():
    sig = inspect.signature(model::TimeDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::massdimension_is_not_abstract():
    assert not inspect.isabstract(model::MassDimension)


def test_model::massdimension_constructor_exists():
    assert callable(model::MassDimension.__init__)


def test_model::massdimension_constructor_args():
    sig = inspect.signature(model::MassDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::amountofsubstancedimension_is_not_abstract():
    assert not inspect.isabstract(model::AmountOfSubstanceDimension)


def test_model::amountofsubstancedimension_constructor_exists():
    assert callable(model::AmountOfSubstanceDimension.__init__)


def test_model::amountofsubstancedimension_constructor_args():
    sig = inspect.signature(model::AmountOfSubstanceDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::lengthdimension_is_not_abstract():
    assert not inspect.isabstract(model::LengthDimension)


def test_model::lengthdimension_constructor_exists():
    assert callable(model::LengthDimension.__init__)


def test_model::lengthdimension_constructor_args():
    sig = inspect.signature(model::LengthDimension.__init__)
    params = list(sig.parameters.keys())



def test_model::systemofunits_is_not_abstract():
    assert not inspect.isabstract(model::SystemOfUnits)


def test_model::systemofunits_constructor_exists():
    assert callable(model::SystemOfUnits.__init__)


def test_model::systemofunits_constructor_args():
    sig = inspect.signature(model::SystemOfUnits.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "standardizationBody" in params, "Missing parameter 'standardizationBody'"

def test_model::systemofunits_has_name():
    assert hasattr(model::SystemOfUnits, "name")
    descriptor = None
    for klass in model::SystemOfUnits.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::systemofunits_has_standardizationBody():
    assert hasattr(model::SystemOfUnits, "standardizationBody")
    descriptor = None
    for klass in model::SystemOfUnits.__mro__:
        if "standardizationBody" in klass.__dict__:
            descriptor = klass.__dict__["standardizationBody"]
            break
    assert isinstance(descriptor, property)



def test_basequantityunit_is_not_abstract():
    assert not inspect.isabstract(BaseQuantityUnit)


def test_basequantityunit_constructor_exists():
    assert callable(BaseQuantityUnit.__init__)


def test_basequantityunit_constructor_args():
    sig = inspect.signature(BaseQuantityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::thermodynamictemperatureunit_is_not_abstract():
    assert not inspect.isabstract(model::ThermodynamicTemperatureUnit)


def test_model::thermodynamictemperatureunit_constructor_exists():
    assert callable(model::ThermodynamicTemperatureUnit.__init__)


def test_model::thermodynamictemperatureunit_constructor_args():
    sig = inspect.signature(model::ThermodynamicTemperatureUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::entropyunit_is_not_abstract():
    assert not inspect.isabstract(model::EntropyUnit)


def test_model::entropyunit_constructor_exists():
    assert callable(model::EntropyUnit.__init__)


def test_model::entropyunit_constructor_args():
    sig = inspect.signature(model::EntropyUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::electriccurrentunit_is_not_abstract():
    assert not inspect.isabstract(model::ElectricCurrentUnit)


def test_model::electriccurrentunit_constructor_exists():
    assert callable(model::ElectricCurrentUnit.__init__)


def test_model::electriccurrentunit_constructor_args():
    sig = inspect.signature(model::ElectricCurrentUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::timeunit_is_not_abstract():
    assert not inspect.isabstract(model::TimeUnit)


def test_model::timeunit_constructor_exists():
    assert callable(model::TimeUnit.__init__)


def test_model::timeunit_constructor_args():
    sig = inspect.signature(model::TimeUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::angleunit_is_not_abstract():
    assert not inspect.isabstract(model::AngleUnit)


def test_model::angleunit_constructor_exists():
    assert callable(model::AngleUnit.__init__)


def test_model::angleunit_constructor_args():
    sig = inspect.signature(model::AngleUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::massunit_is_not_abstract():
    assert not inspect.isabstract(model::MassUnit)


def test_model::massunit_constructor_exists():
    assert callable(model::MassUnit.__init__)


def test_model::massunit_constructor_args():
    sig = inspect.signature(model::MassUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::trafficintensityunit_is_not_abstract():
    assert not inspect.isabstract(model::TrafficIntensityUnit)


def test_model::trafficintensityunit_constructor_exists():
    assert callable(model::TrafficIntensityUnit.__init__)


def test_model::trafficintensityunit_constructor_args():
    sig = inspect.signature(model::TrafficIntensityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::levelunit_is_not_abstract():
    assert not inspect.isabstract(model::LevelUnit)


def test_model::levelunit_constructor_exists():
    assert callable(model::LevelUnit.__init__)


def test_model::levelunit_constructor_args():
    sig = inspect.signature(model::LevelUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::amountofsubstanceunit_is_not_abstract():
    assert not inspect.isabstract(model::AmountOfSubstanceUnit)


def test_model::amountofsubstanceunit_constructor_exists():
    assert callable(model::AmountOfSubstanceUnit.__init__)


def test_model::amountofsubstanceunit_constructor_args():
    sig = inspect.signature(model::AmountOfSubstanceUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::luminousintensityunit_is_not_abstract():
    assert not inspect.isabstract(model::LuminousIntensityUnit)


def test_model::luminousintensityunit_constructor_exists():
    assert callable(model::LuminousIntensityUnit.__init__)


def test_model::luminousintensityunit_constructor_args():
    sig = inspect.signature(model::LuminousIntensityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::datastoragecapacityunit_is_not_abstract():
    assert not inspect.isabstract(model::DataStorageCapacityUnit)


def test_model::datastoragecapacityunit_constructor_exists():
    assert callable(model::DataStorageCapacityUnit.__init__)


def test_model::datastoragecapacityunit_constructor_args():
    sig = inspect.signature(model::DataStorageCapacityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::lengthunit_is_not_abstract():
    assert not inspect.isabstract(model::LengthUnit)


def test_model::lengthunit_constructor_exists():
    assert callable(model::LengthUnit.__init__)


def test_model::lengthunit_constructor_args():
    sig = inspect.signature(model::LengthUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::conversionfactor_is_not_abstract():
    assert not inspect.isabstract(model::ConversionFactor)


def test_model::conversionfactor_constructor_exists():
    assert callable(model::ConversionFactor.__init__)


def test_model::conversionfactor_constructor_args():
    sig = inspect.signature(model::ConversionFactor.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicator" in params, "Missing parameter 'multiplicator'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_model::conversionfactor_has_multiplicator():
    assert hasattr(model::ConversionFactor, "multiplicator")
    descriptor = None
    for klass in model::ConversionFactor.__mro__:
        if "multiplicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicator"]
            break
    assert isinstance(descriptor, property)

def test_model::conversionfactor_has_offset():
    assert hasattr(model::ConversionFactor, "offset")
    descriptor = None
    for klass in model::ConversionFactor.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_model::dimension_is_not_abstract():
    assert not inspect.isabstract(model::Dimension)


def test_model::dimension_constructor_exists():
    assert callable(model::Dimension.__init__)


def test_model::dimension_constructor_args():
    sig = inspect.signature(model::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"

def test_model::dimension_has_exponent():
    assert hasattr(model::Dimension, "exponent")
    descriptor = None
    for klass in model::Dimension.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)



def test_basequantity_is_not_abstract():
    assert not inspect.isabstract(BaseQuantity)


def test_basequantity_constructor_exists():
    assert callable(BaseQuantity.__init__)


def test_basequantity_constructor_args():
    sig = inspect.signature(BaseQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model::luminousintensity_is_not_abstract():
    assert not inspect.isabstract(model::LuminousIntensity)


def test_model::luminousintensity_constructor_exists():
    assert callable(model::LuminousIntensity.__init__)


def test_model::luminousintensity_constructor_args():
    sig = inspect.signature(model::LuminousIntensity.__init__)
    params = list(sig.parameters.keys())



def test_model::mass_is_not_abstract():
    assert not inspect.isabstract(model::Mass)


def test_model::mass_constructor_exists():
    assert callable(model::Mass.__init__)


def test_model::mass_constructor_args():
    sig = inspect.signature(model::Mass.__init__)
    params = list(sig.parameters.keys())



def test_model::datastoragecapacity_is_not_abstract():
    assert not inspect.isabstract(model::DataStorageCapacity)


def test_model::datastoragecapacity_constructor_exists():
    assert callable(model::DataStorageCapacity.__init__)


def test_model::datastoragecapacity_constructor_args():
    sig = inspect.signature(model::DataStorageCapacity.__init__)
    params = list(sig.parameters.keys())



def test_model::level_is_not_abstract():
    assert not inspect.isabstract(model::Level)


def test_model::level_constructor_exists():
    assert callable(model::Level.__init__)


def test_model::level_constructor_args():
    sig = inspect.signature(model::Level.__init__)
    params = list(sig.parameters.keys())



def test_model::amountofsubstance_is_not_abstract():
    assert not inspect.isabstract(model::AmountOfSubstance)


def test_model::amountofsubstance_constructor_exists():
    assert callable(model::AmountOfSubstance.__init__)


def test_model::amountofsubstance_constructor_args():
    sig = inspect.signature(model::AmountOfSubstance.__init__)
    params = list(sig.parameters.keys())



def test_model::electriccurrent_is_not_abstract():
    assert not inspect.isabstract(model::ElectricCurrent)


def test_model::electriccurrent_constructor_exists():
    assert callable(model::ElectricCurrent.__init__)


def test_model::electriccurrent_constructor_args():
    sig = inspect.signature(model::ElectricCurrent.__init__)
    params = list(sig.parameters.keys())



def test_model::trafficintensity_is_not_abstract():
    assert not inspect.isabstract(model::TrafficIntensity)


def test_model::trafficintensity_constructor_exists():
    assert callable(model::TrafficIntensity.__init__)


def test_model::trafficintensity_constructor_args():
    sig = inspect.signature(model::TrafficIntensity.__init__)
    params = list(sig.parameters.keys())



def test_model::time_is_not_abstract():
    assert not inspect.isabstract(model::Time)


def test_model::time_constructor_exists():
    assert callable(model::Time.__init__)


def test_model::time_constructor_args():
    sig = inspect.signature(model::Time.__init__)
    params = list(sig.parameters.keys())



def test_model::entropy_is_not_abstract():
    assert not inspect.isabstract(model::Entropy)


def test_model::entropy_constructor_exists():
    assert callable(model::Entropy.__init__)


def test_model::entropy_constructor_args():
    sig = inspect.signature(model::Entropy.__init__)
    params = list(sig.parameters.keys())



def test_model::thermodynamictemperature_is_not_abstract():
    assert not inspect.isabstract(model::ThermodynamicTemperature)


def test_model::thermodynamictemperature_constructor_exists():
    assert callable(model::ThermodynamicTemperature.__init__)


def test_model::thermodynamictemperature_constructor_args():
    sig = inspect.signature(model::ThermodynamicTemperature.__init__)
    params = list(sig.parameters.keys())



def test_model::angle_is_not_abstract():
    assert not inspect.isabstract(model::Angle)


def test_model::angle_constructor_exists():
    assert callable(model::Angle.__init__)


def test_model::angle_constructor_args():
    sig = inspect.signature(model::Angle.__init__)
    params = list(sig.parameters.keys())



def test_model::length_is_not_abstract():
    assert not inspect.isabstract(model::Length)


def test_model::length_constructor_exists():
    assert callable(model::Length.__init__)


def test_model::length_constructor_args():
    sig = inspect.signature(model::Length.__init__)
    params = list(sig.parameters.keys())



def test_model::quantityvalue_is_not_abstract():
    assert not inspect.isabstract(model::QuantityValue)


def test_model::quantityvalue_constructor_exists():
    assert callable(model::QuantityValue.__init__)


def test_model::quantityvalue_constructor_args():
    sig = inspect.signature(model::QuantityValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::quantityvalue_has_value():
    assert hasattr(model::QuantityValue, "value")
    descriptor = None
    for klass in model::QuantityValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::unit_is_not_abstract():
    assert not inspect.isabstract(model::Unit)


def test_model::unit_constructor_exists():
    assert callable(model::Unit.__init__)


def test_model::unit_constructor_args():
    sig = inspect.signature(model::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "isIntervalScaled" in params, "Missing parameter 'isIntervalScaled'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "isRatioScaled" in params, "Missing parameter 'isRatioScaled'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isDerivedUnit" in params, "Missing parameter 'isDerivedUnit'"
    assert "isCoherentDerivedUnit" in params, "Missing parameter 'isCoherentDerivedUnit'"
    assert "isBaseUnit" in params, "Missing parameter 'isBaseUnit'"

def test_model::unit_has_isIntervalScaled():
    assert hasattr(model::Unit, "isIntervalScaled")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "isIntervalScaled" in klass.__dict__:
            descriptor = klass.__dict__["isIntervalScaled"]
            break
    assert isinstance(descriptor, property)

def test_model::unit_has_symbol():
    assert hasattr(model::Unit, "symbol")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_model::unit_has_isRatioScaled():
    assert hasattr(model::Unit, "isRatioScaled")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "isRatioScaled" in klass.__dict__:
            descriptor = klass.__dict__["isRatioScaled"]
            break
    assert isinstance(descriptor, property)

def test_model::unit_has_name():
    assert hasattr(model::Unit, "name")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::unit_has_isDerivedUnit():
    assert hasattr(model::Unit, "isDerivedUnit")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "isDerivedUnit" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnit"]
            break
    assert isinstance(descriptor, property)

def test_model::unit_has_isCoherentDerivedUnit():
    assert hasattr(model::Unit, "isCoherentDerivedUnit")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "isCoherentDerivedUnit" in klass.__dict__:
            descriptor = klass.__dict__["isCoherentDerivedUnit"]
            break
    assert isinstance(descriptor, property)

def test_model::unit_has_isBaseUnit():
    assert hasattr(model::Unit, "isBaseUnit")
    descriptor = None
    for klass in model::Unit.__mro__:
        if "isBaseUnit" in klass.__dict__:
            descriptor = klass.__dict__["isBaseUnit"]
            break
    assert isinstance(descriptor, property)



def test_model::quantity_is_not_abstract():
    assert not inspect.isabstract(model::Quantity)


def test_model::quantity_constructor_exists():
    assert callable(model::Quantity.__init__)


def test_model::quantity_constructor_args():
    sig = inspect.signature(model::Quantity.__init__)
    params = list(sig.parameters.keys())


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
Unit_strategy = st.builds(
    Unit,
)
model::BaseQuantityUnit_strategy = st.builds(
    model::BaseQuantityUnit,
)
Quantity_strategy = st.builds(
    Quantity,
)
model::DerivedQuantity_strategy = st.builds(
    model::DerivedQuantity,
)
model::BaseQuantity_strategy = st.builds(
    model::BaseQuantity,
)
model::Sample_strategy = st.builds(
    model::Sample,
)
model::DerivedQuantityUnit_strategy = st.builds(
    model::DerivedQuantityUnit,
)
ConversionFactor_strategy = st.builds(
    ConversionFactor,
)
model::TimeConversionFactor_strategy = st.builds(
    model::TimeConversionFactor,
)
model::MassConversionFactor_strategy = st.builds(
    model::MassConversionFactor,
)
model::LengthConversionFactor_strategy = st.builds(
    model::LengthConversionFactor,
)
MeasurementUncertaintyInformation_strategy = st.builds(
    MeasurementUncertaintyInformation,
)
model::Sampling_strategy = st.builds(
    model::Sampling,
    measurementProcedure=
        safe_text
)
model::Interval_strategy = st.builds(
    model::Interval,
)
model::NormalDistribution_strategy = st.builds(
    model::NormalDistribution,
    meanValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    standardDeviation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::LevelConversionFactor_strategy = st.builds(
    model::LevelConversionFactor,
)
model::TrafficIntensityConversionFactor_strategy = st.builds(
    model::TrafficIntensityConversionFactor,
)
model::EntropyConversionFactor_strategy = st.builds(
    model::EntropyConversionFactor,
)
model::DataStorageCapacityConversionFactor_strategy = st.builds(
    model::DataStorageCapacityConversionFactor,
)
model::AngleConversionFactor_strategy = st.builds(
    model::AngleConversionFactor,
)
model::LuminousIntensityConversionFactor_strategy = st.builds(
    model::LuminousIntensityConversionFactor,
)
model::AmountOfSubstanceConversionFactor_strategy = st.builds(
    model::AmountOfSubstanceConversionFactor,
)
model::ThermodynamicTemperatureConversionFactor_strategy = st.builds(
    model::ThermodynamicTemperatureConversionFactor,
)
model::ElectricCurrentConversionFactor_strategy = st.builds(
    model::ElectricCurrentConversionFactor,
)
model::MeasurementUncertaintyInformation_strategy = st.builds(
    model::MeasurementUncertaintyInformation,
)
model::MeasurementUncertainty_strategy = st.builds(
    model::MeasurementUncertainty,
    standardUncertainty=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Dimension_strategy = st.builds(
    Dimension,
)
model::TrafficIntensityDimension_strategy = st.builds(
    model::TrafficIntensityDimension,
)
model::ThermodynamicTemperatureDimension_strategy = st.builds(
    model::ThermodynamicTemperatureDimension,
)
model::LevelDimension_strategy = st.builds(
    model::LevelDimension,
)
model::DataStorageCapacityDimension_strategy = st.builds(
    model::DataStorageCapacityDimension,
)
model::EntropyDimension_strategy = st.builds(
    model::EntropyDimension,
)
model::LuminousIntensityDimension_strategy = st.builds(
    model::LuminousIntensityDimension,
)
model::ElectricCurrentDimension_strategy = st.builds(
    model::ElectricCurrentDimension,
)
model::AngleDimension_strategy = st.builds(
    model::AngleDimension,
)
model::TimeDimension_strategy = st.builds(
    model::TimeDimension,
)
model::MassDimension_strategy = st.builds(
    model::MassDimension,
)
model::AmountOfSubstanceDimension_strategy = st.builds(
    model::AmountOfSubstanceDimension,
)
model::LengthDimension_strategy = st.builds(
    model::LengthDimension,
)
model::SystemOfUnits_strategy = st.builds(
    model::SystemOfUnits,
    name=
        safe_text,
    standardizationBody=
        safe_text
)
BaseQuantityUnit_strategy = st.builds(
    BaseQuantityUnit,
)
model::ThermodynamicTemperatureUnit_strategy = st.builds(
    model::ThermodynamicTemperatureUnit,
)
model::EntropyUnit_strategy = st.builds(
    model::EntropyUnit,
)
model::ElectricCurrentUnit_strategy = st.builds(
    model::ElectricCurrentUnit,
)
model::TimeUnit_strategy = st.builds(
    model::TimeUnit,
)
model::AngleUnit_strategy = st.builds(
    model::AngleUnit,
)
model::MassUnit_strategy = st.builds(
    model::MassUnit,
)
model::TrafficIntensityUnit_strategy = st.builds(
    model::TrafficIntensityUnit,
)
model::LevelUnit_strategy = st.builds(
    model::LevelUnit,
)
model::AmountOfSubstanceUnit_strategy = st.builds(
    model::AmountOfSubstanceUnit,
)
model::LuminousIntensityUnit_strategy = st.builds(
    model::LuminousIntensityUnit,
)
model::DataStorageCapacityUnit_strategy = st.builds(
    model::DataStorageCapacityUnit,
)
model::LengthUnit_strategy = st.builds(
    model::LengthUnit,
)
model::ConversionFactor_strategy = st.builds(
    model::ConversionFactor,
    multiplicator=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    offset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::Dimension_strategy = st.builds(
    model::Dimension,
    exponent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BaseQuantity_strategy = st.builds(
    BaseQuantity,
)
model::LuminousIntensity_strategy = st.builds(
    model::LuminousIntensity,
)
model::Mass_strategy = st.builds(
    model::Mass,
)
model::DataStorageCapacity_strategy = st.builds(
    model::DataStorageCapacity,
)
model::Level_strategy = st.builds(
    model::Level,
)
model::AmountOfSubstance_strategy = st.builds(
    model::AmountOfSubstance,
)
model::ElectricCurrent_strategy = st.builds(
    model::ElectricCurrent,
)
model::TrafficIntensity_strategy = st.builds(
    model::TrafficIntensity,
)
model::Time_strategy = st.builds(
    model::Time,
)
model::Entropy_strategy = st.builds(
    model::Entropy,
)
model::ThermodynamicTemperature_strategy = st.builds(
    model::ThermodynamicTemperature,
)
model::Angle_strategy = st.builds(
    model::Angle,
)
model::Length_strategy = st.builds(
    model::Length,
)
model::QuantityValue_strategy = st.builds(
    model::QuantityValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::Unit_strategy = st.builds(
    model::Unit,
    isIntervalScaled=
        st.booleans(),
    symbol=
        safe_text,
    isRatioScaled=
        st.booleans(),
    name=
        safe_text,
    isDerivedUnit=
        st.booleans(),
    isCoherentDerivedUnit=
        st.booleans(),
    isBaseUnit=
        st.booleans()
)
model::Quantity_strategy = st.builds(
    model::Quantity,
)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=model::BaseQuantityUnit_strategy)
@settings(max_examples=50)
def test_model::basequantityunit_instantiation(instance):
    assert isinstance(instance, model::BaseQuantityUnit)

@given(instance=Quantity_strategy)
@settings(max_examples=50)
def test_quantity_instantiation(instance):
    assert isinstance(instance, Quantity)

@given(instance=model::DerivedQuantity_strategy)
@settings(max_examples=50)
def test_model::derivedquantity_instantiation(instance):
    assert isinstance(instance, model::DerivedQuantity)

@given(instance=model::BaseQuantity_strategy)
@settings(max_examples=50)
def test_model::basequantity_instantiation(instance):
    assert isinstance(instance, model::BaseQuantity)

@given(instance=model::Sample_strategy)
@settings(max_examples=50)
def test_model::sample_instantiation(instance):
    assert isinstance(instance, model::Sample)

@given(instance=model::DerivedQuantityUnit_strategy)
@settings(max_examples=50)
def test_model::derivedquantityunit_instantiation(instance):
    assert isinstance(instance, model::DerivedQuantityUnit)

@given(instance=ConversionFactor_strategy)
@settings(max_examples=50)
def test_conversionfactor_instantiation(instance):
    assert isinstance(instance, ConversionFactor)

@given(instance=model::TimeConversionFactor_strategy)
@settings(max_examples=50)
def test_model::timeconversionfactor_instantiation(instance):
    assert isinstance(instance, model::TimeConversionFactor)

@given(instance=model::MassConversionFactor_strategy)
@settings(max_examples=50)
def test_model::massconversionfactor_instantiation(instance):
    assert isinstance(instance, model::MassConversionFactor)

@given(instance=model::LengthConversionFactor_strategy)
@settings(max_examples=50)
def test_model::lengthconversionfactor_instantiation(instance):
    assert isinstance(instance, model::LengthConversionFactor)

@given(instance=MeasurementUncertaintyInformation_strategy)
@settings(max_examples=50)
def test_measurementuncertaintyinformation_instantiation(instance):
    assert isinstance(instance, MeasurementUncertaintyInformation)

@given(instance=model::Sampling_strategy)
@settings(max_examples=50)
def test_model::sampling_instantiation(instance):
    assert isinstance(instance, model::Sampling)

@given(instance=model::Sampling_strategy)
def test_model::sampling_measurementProcedure_type(instance):
    assert isinstance(instance.measurementProcedure, str)


@given(instance=model::Sampling_strategy)
def test_model::sampling_measurementProcedure_setter(instance):
    original = instance.measurementProcedure
    instance.measurementProcedure = original
    assert instance.measurementProcedure == original

@given(instance=model::Interval_strategy)
@settings(max_examples=50)
def test_model::interval_instantiation(instance):
    assert isinstance(instance, model::Interval)

@given(instance=model::NormalDistribution_strategy)
@settings(max_examples=50)
def test_model::normaldistribution_instantiation(instance):
    assert isinstance(instance, model::NormalDistribution)

@given(instance=model::NormalDistribution_strategy)
def test_model::normaldistribution_meanValue_type(instance):
    assert isinstance(instance.meanValue, float)


@given(instance=model::NormalDistribution_strategy)
def test_model::normaldistribution_meanValue_setter(instance):
    original = instance.meanValue
    instance.meanValue = original
    assert instance.meanValue == original

@given(instance=model::NormalDistribution_strategy)
def test_model::normaldistribution_standardDeviation_type(instance):
    assert isinstance(instance.standardDeviation, float)


@given(instance=model::NormalDistribution_strategy)
def test_model::normaldistribution_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original

@given(instance=model::LevelConversionFactor_strategy)
@settings(max_examples=50)
def test_model::levelconversionfactor_instantiation(instance):
    assert isinstance(instance, model::LevelConversionFactor)

@given(instance=model::TrafficIntensityConversionFactor_strategy)
@settings(max_examples=50)
def test_model::trafficintensityconversionfactor_instantiation(instance):
    assert isinstance(instance, model::TrafficIntensityConversionFactor)

@given(instance=model::EntropyConversionFactor_strategy)
@settings(max_examples=50)
def test_model::entropyconversionfactor_instantiation(instance):
    assert isinstance(instance, model::EntropyConversionFactor)

@given(instance=model::DataStorageCapacityConversionFactor_strategy)
@settings(max_examples=50)
def test_model::datastoragecapacityconversionfactor_instantiation(instance):
    assert isinstance(instance, model::DataStorageCapacityConversionFactor)

@given(instance=model::AngleConversionFactor_strategy)
@settings(max_examples=50)
def test_model::angleconversionfactor_instantiation(instance):
    assert isinstance(instance, model::AngleConversionFactor)

@given(instance=model::LuminousIntensityConversionFactor_strategy)
@settings(max_examples=50)
def test_model::luminousintensityconversionfactor_instantiation(instance):
    assert isinstance(instance, model::LuminousIntensityConversionFactor)

@given(instance=model::AmountOfSubstanceConversionFactor_strategy)
@settings(max_examples=50)
def test_model::amountofsubstanceconversionfactor_instantiation(instance):
    assert isinstance(instance, model::AmountOfSubstanceConversionFactor)

@given(instance=model::ThermodynamicTemperatureConversionFactor_strategy)
@settings(max_examples=50)
def test_model::thermodynamictemperatureconversionfactor_instantiation(instance):
    assert isinstance(instance, model::ThermodynamicTemperatureConversionFactor)

@given(instance=model::ElectricCurrentConversionFactor_strategy)
@settings(max_examples=50)
def test_model::electriccurrentconversionfactor_instantiation(instance):
    assert isinstance(instance, model::ElectricCurrentConversionFactor)

@given(instance=model::MeasurementUncertaintyInformation_strategy)
@settings(max_examples=50)
def test_model::measurementuncertaintyinformation_instantiation(instance):
    assert isinstance(instance, model::MeasurementUncertaintyInformation)

@given(instance=model::MeasurementUncertainty_strategy)
@settings(max_examples=50)
def test_model::measurementuncertainty_instantiation(instance):
    assert isinstance(instance, model::MeasurementUncertainty)

@given(instance=model::MeasurementUncertainty_strategy)
def test_model::measurementuncertainty_standardUncertainty_type(instance):
    assert isinstance(instance.standardUncertainty, float)


@given(instance=model::MeasurementUncertainty_strategy)
def test_model::measurementuncertainty_standardUncertainty_setter(instance):
    original = instance.standardUncertainty
    instance.standardUncertainty = original
    assert instance.standardUncertainty == original

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=model::TrafficIntensityDimension_strategy)
@settings(max_examples=50)
def test_model::trafficintensitydimension_instantiation(instance):
    assert isinstance(instance, model::TrafficIntensityDimension)

@given(instance=model::ThermodynamicTemperatureDimension_strategy)
@settings(max_examples=50)
def test_model::thermodynamictemperaturedimension_instantiation(instance):
    assert isinstance(instance, model::ThermodynamicTemperatureDimension)

@given(instance=model::LevelDimension_strategy)
@settings(max_examples=50)
def test_model::leveldimension_instantiation(instance):
    assert isinstance(instance, model::LevelDimension)

@given(instance=model::DataStorageCapacityDimension_strategy)
@settings(max_examples=50)
def test_model::datastoragecapacitydimension_instantiation(instance):
    assert isinstance(instance, model::DataStorageCapacityDimension)

@given(instance=model::EntropyDimension_strategy)
@settings(max_examples=50)
def test_model::entropydimension_instantiation(instance):
    assert isinstance(instance, model::EntropyDimension)

@given(instance=model::LuminousIntensityDimension_strategy)
@settings(max_examples=50)
def test_model::luminousintensitydimension_instantiation(instance):
    assert isinstance(instance, model::LuminousIntensityDimension)

@given(instance=model::ElectricCurrentDimension_strategy)
@settings(max_examples=50)
def test_model::electriccurrentdimension_instantiation(instance):
    assert isinstance(instance, model::ElectricCurrentDimension)

@given(instance=model::AngleDimension_strategy)
@settings(max_examples=50)
def test_model::angledimension_instantiation(instance):
    assert isinstance(instance, model::AngleDimension)

@given(instance=model::TimeDimension_strategy)
@settings(max_examples=50)
def test_model::timedimension_instantiation(instance):
    assert isinstance(instance, model::TimeDimension)

@given(instance=model::MassDimension_strategy)
@settings(max_examples=50)
def test_model::massdimension_instantiation(instance):
    assert isinstance(instance, model::MassDimension)

@given(instance=model::AmountOfSubstanceDimension_strategy)
@settings(max_examples=50)
def test_model::amountofsubstancedimension_instantiation(instance):
    assert isinstance(instance, model::AmountOfSubstanceDimension)

@given(instance=model::LengthDimension_strategy)
@settings(max_examples=50)
def test_model::lengthdimension_instantiation(instance):
    assert isinstance(instance, model::LengthDimension)

@given(instance=model::SystemOfUnits_strategy)
@settings(max_examples=50)
def test_model::systemofunits_instantiation(instance):
    assert isinstance(instance, model::SystemOfUnits)

@given(instance=model::SystemOfUnits_strategy)
def test_model::systemofunits_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::SystemOfUnits_strategy)
def test_model::systemofunits_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::SystemOfUnits_strategy)
def test_model::systemofunits_standardizationBody_type(instance):
    assert isinstance(instance.standardizationBody, str)


@given(instance=model::SystemOfUnits_strategy)
def test_model::systemofunits_standardizationBody_setter(instance):
    original = instance.standardizationBody
    instance.standardizationBody = original
    assert instance.standardizationBody == original

@given(instance=BaseQuantityUnit_strategy)
@settings(max_examples=50)
def test_basequantityunit_instantiation(instance):
    assert isinstance(instance, BaseQuantityUnit)

@given(instance=model::ThermodynamicTemperatureUnit_strategy)
@settings(max_examples=50)
def test_model::thermodynamictemperatureunit_instantiation(instance):
    assert isinstance(instance, model::ThermodynamicTemperatureUnit)

@given(instance=model::EntropyUnit_strategy)
@settings(max_examples=50)
def test_model::entropyunit_instantiation(instance):
    assert isinstance(instance, model::EntropyUnit)

@given(instance=model::ElectricCurrentUnit_strategy)
@settings(max_examples=50)
def test_model::electriccurrentunit_instantiation(instance):
    assert isinstance(instance, model::ElectricCurrentUnit)

@given(instance=model::TimeUnit_strategy)
@settings(max_examples=50)
def test_model::timeunit_instantiation(instance):
    assert isinstance(instance, model::TimeUnit)

@given(instance=model::AngleUnit_strategy)
@settings(max_examples=50)
def test_model::angleunit_instantiation(instance):
    assert isinstance(instance, model::AngleUnit)

@given(instance=model::MassUnit_strategy)
@settings(max_examples=50)
def test_model::massunit_instantiation(instance):
    assert isinstance(instance, model::MassUnit)

@given(instance=model::TrafficIntensityUnit_strategy)
@settings(max_examples=50)
def test_model::trafficintensityunit_instantiation(instance):
    assert isinstance(instance, model::TrafficIntensityUnit)

@given(instance=model::LevelUnit_strategy)
@settings(max_examples=50)
def test_model::levelunit_instantiation(instance):
    assert isinstance(instance, model::LevelUnit)

@given(instance=model::AmountOfSubstanceUnit_strategy)
@settings(max_examples=50)
def test_model::amountofsubstanceunit_instantiation(instance):
    assert isinstance(instance, model::AmountOfSubstanceUnit)

@given(instance=model::LuminousIntensityUnit_strategy)
@settings(max_examples=50)
def test_model::luminousintensityunit_instantiation(instance):
    assert isinstance(instance, model::LuminousIntensityUnit)

@given(instance=model::DataStorageCapacityUnit_strategy)
@settings(max_examples=50)
def test_model::datastoragecapacityunit_instantiation(instance):
    assert isinstance(instance, model::DataStorageCapacityUnit)

@given(instance=model::LengthUnit_strategy)
@settings(max_examples=50)
def test_model::lengthunit_instantiation(instance):
    assert isinstance(instance, model::LengthUnit)

@given(instance=model::ConversionFactor_strategy)
@settings(max_examples=50)
def test_model::conversionfactor_instantiation(instance):
    assert isinstance(instance, model::ConversionFactor)

@given(instance=model::ConversionFactor_strategy)
def test_model::conversionfactor_multiplicator_type(instance):
    assert isinstance(instance.multiplicator, float)


@given(instance=model::ConversionFactor_strategy)
def test_model::conversionfactor_multiplicator_setter(instance):
    original = instance.multiplicator
    instance.multiplicator = original
    assert instance.multiplicator == original

@given(instance=model::ConversionFactor_strategy)
def test_model::conversionfactor_offset_type(instance):
    assert isinstance(instance.offset, float)


@given(instance=model::ConversionFactor_strategy)
def test_model::conversionfactor_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=model::Dimension_strategy)
@settings(max_examples=50)
def test_model::dimension_instantiation(instance):
    assert isinstance(instance, model::Dimension)

@given(instance=model::Dimension_strategy)
def test_model::dimension_exponent_type(instance):
    assert isinstance(instance.exponent, float)


@given(instance=model::Dimension_strategy)
def test_model::dimension_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original

@given(instance=BaseQuantity_strategy)
@settings(max_examples=50)
def test_basequantity_instantiation(instance):
    assert isinstance(instance, BaseQuantity)

@given(instance=model::LuminousIntensity_strategy)
@settings(max_examples=50)
def test_model::luminousintensity_instantiation(instance):
    assert isinstance(instance, model::LuminousIntensity)

@given(instance=model::Mass_strategy)
@settings(max_examples=50)
def test_model::mass_instantiation(instance):
    assert isinstance(instance, model::Mass)

@given(instance=model::DataStorageCapacity_strategy)
@settings(max_examples=50)
def test_model::datastoragecapacity_instantiation(instance):
    assert isinstance(instance, model::DataStorageCapacity)

@given(instance=model::Level_strategy)
@settings(max_examples=50)
def test_model::level_instantiation(instance):
    assert isinstance(instance, model::Level)

@given(instance=model::AmountOfSubstance_strategy)
@settings(max_examples=50)
def test_model::amountofsubstance_instantiation(instance):
    assert isinstance(instance, model::AmountOfSubstance)

@given(instance=model::ElectricCurrent_strategy)
@settings(max_examples=50)
def test_model::electriccurrent_instantiation(instance):
    assert isinstance(instance, model::ElectricCurrent)

@given(instance=model::TrafficIntensity_strategy)
@settings(max_examples=50)
def test_model::trafficintensity_instantiation(instance):
    assert isinstance(instance, model::TrafficIntensity)

@given(instance=model::Time_strategy)
@settings(max_examples=50)
def test_model::time_instantiation(instance):
    assert isinstance(instance, model::Time)

@given(instance=model::Entropy_strategy)
@settings(max_examples=50)
def test_model::entropy_instantiation(instance):
    assert isinstance(instance, model::Entropy)

@given(instance=model::ThermodynamicTemperature_strategy)
@settings(max_examples=50)
def test_model::thermodynamictemperature_instantiation(instance):
    assert isinstance(instance, model::ThermodynamicTemperature)

@given(instance=model::Angle_strategy)
@settings(max_examples=50)
def test_model::angle_instantiation(instance):
    assert isinstance(instance, model::Angle)

@given(instance=model::Length_strategy)
@settings(max_examples=50)
def test_model::length_instantiation(instance):
    assert isinstance(instance, model::Length)

@given(instance=model::QuantityValue_strategy)
@settings(max_examples=50)
def test_model::quantityvalue_instantiation(instance):
    assert isinstance(instance, model::QuantityValue)

@given(instance=model::QuantityValue_strategy)
def test_model::quantityvalue_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=model::QuantityValue_strategy)
def test_model::quantityvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::Unit_strategy)
@settings(max_examples=50)
def test_model::unit_instantiation(instance):
    assert isinstance(instance, model::Unit)

@given(instance=model::Unit_strategy)
def test_model::unit_isIntervalScaled_type(instance):
    assert isinstance(instance.isIntervalScaled, bool)


@given(instance=model::Unit_strategy)
def test_model::unit_isIntervalScaled_setter(instance):
    original = instance.isIntervalScaled
    instance.isIntervalScaled = original
    assert instance.isIntervalScaled == original

@given(instance=model::Unit_strategy)
def test_model::unit_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=model::Unit_strategy)
def test_model::unit_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=model::Unit_strategy)
def test_model::unit_isRatioScaled_type(instance):
    assert isinstance(instance.isRatioScaled, bool)


@given(instance=model::Unit_strategy)
def test_model::unit_isRatioScaled_setter(instance):
    original = instance.isRatioScaled
    instance.isRatioScaled = original
    assert instance.isRatioScaled == original

@given(instance=model::Unit_strategy)
def test_model::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Unit_strategy)
def test_model::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Unit_strategy)
def test_model::unit_isDerivedUnit_type(instance):
    assert isinstance(instance.isDerivedUnit, bool)


@given(instance=model::Unit_strategy)
def test_model::unit_isDerivedUnit_setter(instance):
    original = instance.isDerivedUnit
    instance.isDerivedUnit = original
    assert instance.isDerivedUnit == original

@given(instance=model::Unit_strategy)
def test_model::unit_isCoherentDerivedUnit_type(instance):
    assert isinstance(instance.isCoherentDerivedUnit, bool)


@given(instance=model::Unit_strategy)
def test_model::unit_isCoherentDerivedUnit_setter(instance):
    original = instance.isCoherentDerivedUnit
    instance.isCoherentDerivedUnit = original
    assert instance.isCoherentDerivedUnit == original

@given(instance=model::Unit_strategy)
def test_model::unit_isBaseUnit_type(instance):
    assert isinstance(instance.isBaseUnit, bool)


@given(instance=model::Unit_strategy)
def test_model::unit_isBaseUnit_setter(instance):
    original = instance.isBaseUnit
    instance.isBaseUnit = original
    assert instance.isBaseUnit == original

@given(instance=model::Quantity_strategy)
@settings(max_examples=50)
def test_model::quantity_instantiation(instance):
    assert isinstance(instance, model::Quantity)
