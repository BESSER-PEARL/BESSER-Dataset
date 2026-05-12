import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConversionFactor,
    model_TimeConversionFactor,
    model_MassConversionFactor,
    model_LengthConversionFactor,
    MeasurementUncertaintyInformation,
    model_NormalDistribution,
    model_LevelConversionFactor,
    model_TrafficIntensityConversionFactor,
    model_EntropyConversionFactor,
    model_DataStorageCapacityConversionFactor,
    model_AngleConversionFactor,
    model_LuminousIntensityConversionFactor,
    model_AmountOfSubstanceConversionFactor,
    model_ThermodynamicTemperatureConversionFactor,
    model_ElectricCurrentConversionFactor,
    model_MeasurementUncertaintyInformation,
    model_MeasurementUncertainty,
    Dimension,
    model_EntropyDimension,
    model_ElectricCurrentDimension,
    model_AmountOfSubstanceDimension,
    model_LevelDimension,
    model_LuminousIntensityDimension,
    model_MassDimension,
    model_TimeDimension,
    model_TrafficIntensityDimension,
    model_DataStorageCapacityDimension,
    model_ThermodynamicTemperatureDimension,
    model_AngleDimension,
    model_LengthDimension,
    model_SystemOfUnits,
    BaseQuantityUnit,
    model_MassUnit,
    model_ElectricCurrentUnit,
    model_TimeUnit,
    model_DataStorageCapacityUnit,
    model_AmountOfSubstanceUnit,
    model_LuminousIntensityUnit,
    model_ThermodynamicTemperatureUnit,
    model_TrafficIntensityUnit,
    model_LevelUnit,
    model_AngleUnit,
    model_EntropyUnit,
    model_LengthUnit,
    model_ConversionFactor,
    model_Dimension,
    BaseQuantity,
    model_ThermodynamicTemperature,
    model_ElectricCurrent,
    model_TrafficIntensity,
    model_Angle,
    model_DataStorageCapacity,
    model_LuminousIntensity,
    model_Mass,
    model_AmountOfSubstance,
    model_Level,
    model_Entropy,
    model_Time,
    model_Length,
    model_QuantityValue,
    model_Unit,
    model_Quantity,
    Unit,
    model_DerivedQuantityUnit,
    model_BaseQuantityUnit,
    Quantity,
    model_DerivedQuantity,
    model_BaseQuantity,
    model_Sample,
    model_Sampling,
    model_Interval,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conversionfactor_is_not_abstract():
    assert not inspect.isabstract(ConversionFactor)


def test_conversionfactor_constructor_exists():
    assert callable(ConversionFactor.__init__)


def test_conversionfactor_constructor_args():
    sig = inspect.signature(ConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_timeconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_TimeConversionFactor)


def test_model_timeconversionfactor_constructor_exists():
    assert callable(model_TimeConversionFactor.__init__)


def test_model_timeconversionfactor_constructor_args():
    sig = inspect.signature(model_TimeConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_massconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_MassConversionFactor)


def test_model_massconversionfactor_constructor_exists():
    assert callable(model_MassConversionFactor.__init__)


def test_model_massconversionfactor_constructor_args():
    sig = inspect.signature(model_MassConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_lengthconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_LengthConversionFactor)


def test_model_lengthconversionfactor_constructor_exists():
    assert callable(model_LengthConversionFactor.__init__)


def test_model_lengthconversionfactor_constructor_args():
    sig = inspect.signature(model_LengthConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_measurementuncertaintyinformation_is_not_abstract():
    assert not inspect.isabstract(MeasurementUncertaintyInformation)


def test_measurementuncertaintyinformation_constructor_exists():
    assert callable(MeasurementUncertaintyInformation.__init__)


def test_measurementuncertaintyinformation_constructor_args():
    sig = inspect.signature(MeasurementUncertaintyInformation.__init__)
    params = list(sig.parameters.keys())



def test_model_normaldistribution_is_not_abstract():
    assert not inspect.isabstract(model_NormalDistribution)


def test_model_normaldistribution_constructor_exists():
    assert callable(model_NormalDistribution.__init__)


def test_model_normaldistribution_constructor_args():
    sig = inspect.signature(model_NormalDistribution.__init__)
    params = list(sig.parameters.keys())
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "meanValue" in params, "Missing parameter 'meanValue'"

def test_model_normaldistribution_has_standardDeviation():
    assert hasattr(model_NormalDistribution, "standardDeviation")
    descriptor = None
    for klass in model_NormalDistribution.__mro__:
        if "standardDeviation" in klass.__dict__:
            descriptor = klass.__dict__["standardDeviation"]
            break
    assert isinstance(descriptor, property)

def test_model_normaldistribution_has_meanValue():
    assert hasattr(model_NormalDistribution, "meanValue")
    descriptor = None
    for klass in model_NormalDistribution.__mro__:
        if "meanValue" in klass.__dict__:
            descriptor = klass.__dict__["meanValue"]
            break
    assert isinstance(descriptor, property)



def test_model_levelconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_LevelConversionFactor)


def test_model_levelconversionfactor_constructor_exists():
    assert callable(model_LevelConversionFactor.__init__)


def test_model_levelconversionfactor_constructor_args():
    sig = inspect.signature(model_LevelConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_trafficintensityconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_TrafficIntensityConversionFactor)


def test_model_trafficintensityconversionfactor_constructor_exists():
    assert callable(model_TrafficIntensityConversionFactor.__init__)


def test_model_trafficintensityconversionfactor_constructor_args():
    sig = inspect.signature(model_TrafficIntensityConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_entropyconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_EntropyConversionFactor)


def test_model_entropyconversionfactor_constructor_exists():
    assert callable(model_EntropyConversionFactor.__init__)


def test_model_entropyconversionfactor_constructor_args():
    sig = inspect.signature(model_EntropyConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_datastoragecapacityconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_DataStorageCapacityConversionFactor)


def test_model_datastoragecapacityconversionfactor_constructor_exists():
    assert callable(model_DataStorageCapacityConversionFactor.__init__)


def test_model_datastoragecapacityconversionfactor_constructor_args():
    sig = inspect.signature(model_DataStorageCapacityConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_angleconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_AngleConversionFactor)


def test_model_angleconversionfactor_constructor_exists():
    assert callable(model_AngleConversionFactor.__init__)


def test_model_angleconversionfactor_constructor_args():
    sig = inspect.signature(model_AngleConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_luminousintensityconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_LuminousIntensityConversionFactor)


def test_model_luminousintensityconversionfactor_constructor_exists():
    assert callable(model_LuminousIntensityConversionFactor.__init__)


def test_model_luminousintensityconversionfactor_constructor_args():
    sig = inspect.signature(model_LuminousIntensityConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_amountofsubstanceconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_AmountOfSubstanceConversionFactor)


def test_model_amountofsubstanceconversionfactor_constructor_exists():
    assert callable(model_AmountOfSubstanceConversionFactor.__init__)


def test_model_amountofsubstanceconversionfactor_constructor_args():
    sig = inspect.signature(model_AmountOfSubstanceConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_thermodynamictemperatureconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_ThermodynamicTemperatureConversionFactor)


def test_model_thermodynamictemperatureconversionfactor_constructor_exists():
    assert callable(model_ThermodynamicTemperatureConversionFactor.__init__)


def test_model_thermodynamictemperatureconversionfactor_constructor_args():
    sig = inspect.signature(model_ThermodynamicTemperatureConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_electriccurrentconversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_ElectricCurrentConversionFactor)


def test_model_electriccurrentconversionfactor_constructor_exists():
    assert callable(model_ElectricCurrentConversionFactor.__init__)


def test_model_electriccurrentconversionfactor_constructor_args():
    sig = inspect.signature(model_ElectricCurrentConversionFactor.__init__)
    params = list(sig.parameters.keys())



def test_model_measurementuncertaintyinformation_is_not_abstract():
    assert not inspect.isabstract(model_MeasurementUncertaintyInformation)


def test_model_measurementuncertaintyinformation_constructor_exists():
    assert callable(model_MeasurementUncertaintyInformation.__init__)


def test_model_measurementuncertaintyinformation_constructor_args():
    sig = inspect.signature(model_MeasurementUncertaintyInformation.__init__)
    params = list(sig.parameters.keys())



def test_model_measurementuncertainty_is_not_abstract():
    assert not inspect.isabstract(model_MeasurementUncertainty)


def test_model_measurementuncertainty_constructor_exists():
    assert callable(model_MeasurementUncertainty.__init__)


def test_model_measurementuncertainty_constructor_args():
    sig = inspect.signature(model_MeasurementUncertainty.__init__)
    params = list(sig.parameters.keys())
    assert "standardUncertainty" in params, "Missing parameter 'standardUncertainty'"

def test_model_measurementuncertainty_has_standardUncertainty():
    assert hasattr(model_MeasurementUncertainty, "standardUncertainty")
    descriptor = None
    for klass in model_MeasurementUncertainty.__mro__:
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



def test_model_entropydimension_is_not_abstract():
    assert not inspect.isabstract(model_EntropyDimension)


def test_model_entropydimension_constructor_exists():
    assert callable(model_EntropyDimension.__init__)


def test_model_entropydimension_constructor_args():
    sig = inspect.signature(model_EntropyDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_electriccurrentdimension_is_not_abstract():
    assert not inspect.isabstract(model_ElectricCurrentDimension)


def test_model_electriccurrentdimension_constructor_exists():
    assert callable(model_ElectricCurrentDimension.__init__)


def test_model_electriccurrentdimension_constructor_args():
    sig = inspect.signature(model_ElectricCurrentDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_amountofsubstancedimension_is_not_abstract():
    assert not inspect.isabstract(model_AmountOfSubstanceDimension)


def test_model_amountofsubstancedimension_constructor_exists():
    assert callable(model_AmountOfSubstanceDimension.__init__)


def test_model_amountofsubstancedimension_constructor_args():
    sig = inspect.signature(model_AmountOfSubstanceDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_leveldimension_is_not_abstract():
    assert not inspect.isabstract(model_LevelDimension)


def test_model_leveldimension_constructor_exists():
    assert callable(model_LevelDimension.__init__)


def test_model_leveldimension_constructor_args():
    sig = inspect.signature(model_LevelDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_luminousintensitydimension_is_not_abstract():
    assert not inspect.isabstract(model_LuminousIntensityDimension)


def test_model_luminousintensitydimension_constructor_exists():
    assert callable(model_LuminousIntensityDimension.__init__)


def test_model_luminousintensitydimension_constructor_args():
    sig = inspect.signature(model_LuminousIntensityDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_massdimension_is_not_abstract():
    assert not inspect.isabstract(model_MassDimension)


def test_model_massdimension_constructor_exists():
    assert callable(model_MassDimension.__init__)


def test_model_massdimension_constructor_args():
    sig = inspect.signature(model_MassDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_timedimension_is_not_abstract():
    assert not inspect.isabstract(model_TimeDimension)


def test_model_timedimension_constructor_exists():
    assert callable(model_TimeDimension.__init__)


def test_model_timedimension_constructor_args():
    sig = inspect.signature(model_TimeDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_trafficintensitydimension_is_not_abstract():
    assert not inspect.isabstract(model_TrafficIntensityDimension)


def test_model_trafficintensitydimension_constructor_exists():
    assert callable(model_TrafficIntensityDimension.__init__)


def test_model_trafficintensitydimension_constructor_args():
    sig = inspect.signature(model_TrafficIntensityDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_datastoragecapacitydimension_is_not_abstract():
    assert not inspect.isabstract(model_DataStorageCapacityDimension)


def test_model_datastoragecapacitydimension_constructor_exists():
    assert callable(model_DataStorageCapacityDimension.__init__)


def test_model_datastoragecapacitydimension_constructor_args():
    sig = inspect.signature(model_DataStorageCapacityDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_thermodynamictemperaturedimension_is_not_abstract():
    assert not inspect.isabstract(model_ThermodynamicTemperatureDimension)


def test_model_thermodynamictemperaturedimension_constructor_exists():
    assert callable(model_ThermodynamicTemperatureDimension.__init__)


def test_model_thermodynamictemperaturedimension_constructor_args():
    sig = inspect.signature(model_ThermodynamicTemperatureDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_angledimension_is_not_abstract():
    assert not inspect.isabstract(model_AngleDimension)


def test_model_angledimension_constructor_exists():
    assert callable(model_AngleDimension.__init__)


def test_model_angledimension_constructor_args():
    sig = inspect.signature(model_AngleDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_lengthdimension_is_not_abstract():
    assert not inspect.isabstract(model_LengthDimension)


def test_model_lengthdimension_constructor_exists():
    assert callable(model_LengthDimension.__init__)


def test_model_lengthdimension_constructor_args():
    sig = inspect.signature(model_LengthDimension.__init__)
    params = list(sig.parameters.keys())



def test_model_systemofunits_is_not_abstract():
    assert not inspect.isabstract(model_SystemOfUnits)


def test_model_systemofunits_constructor_exists():
    assert callable(model_SystemOfUnits.__init__)


def test_model_systemofunits_constructor_args():
    sig = inspect.signature(model_SystemOfUnits.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "standardizationBody" in params, "Missing parameter 'standardizationBody'"

def test_model_systemofunits_has_name():
    assert hasattr(model_SystemOfUnits, "name")
    descriptor = None
    for klass in model_SystemOfUnits.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_systemofunits_has_standardizationBody():
    assert hasattr(model_SystemOfUnits, "standardizationBody")
    descriptor = None
    for klass in model_SystemOfUnits.__mro__:
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



def test_model_massunit_is_not_abstract():
    assert not inspect.isabstract(model_MassUnit)


def test_model_massunit_constructor_exists():
    assert callable(model_MassUnit.__init__)


def test_model_massunit_constructor_args():
    sig = inspect.signature(model_MassUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_electriccurrentunit_is_not_abstract():
    assert not inspect.isabstract(model_ElectricCurrentUnit)


def test_model_electriccurrentunit_constructor_exists():
    assert callable(model_ElectricCurrentUnit.__init__)


def test_model_electriccurrentunit_constructor_args():
    sig = inspect.signature(model_ElectricCurrentUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_timeunit_is_not_abstract():
    assert not inspect.isabstract(model_TimeUnit)


def test_model_timeunit_constructor_exists():
    assert callable(model_TimeUnit.__init__)


def test_model_timeunit_constructor_args():
    sig = inspect.signature(model_TimeUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_datastoragecapacityunit_is_not_abstract():
    assert not inspect.isabstract(model_DataStorageCapacityUnit)


def test_model_datastoragecapacityunit_constructor_exists():
    assert callable(model_DataStorageCapacityUnit.__init__)


def test_model_datastoragecapacityunit_constructor_args():
    sig = inspect.signature(model_DataStorageCapacityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_amountofsubstanceunit_is_not_abstract():
    assert not inspect.isabstract(model_AmountOfSubstanceUnit)


def test_model_amountofsubstanceunit_constructor_exists():
    assert callable(model_AmountOfSubstanceUnit.__init__)


def test_model_amountofsubstanceunit_constructor_args():
    sig = inspect.signature(model_AmountOfSubstanceUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_luminousintensityunit_is_not_abstract():
    assert not inspect.isabstract(model_LuminousIntensityUnit)


def test_model_luminousintensityunit_constructor_exists():
    assert callable(model_LuminousIntensityUnit.__init__)


def test_model_luminousintensityunit_constructor_args():
    sig = inspect.signature(model_LuminousIntensityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_thermodynamictemperatureunit_is_not_abstract():
    assert not inspect.isabstract(model_ThermodynamicTemperatureUnit)


def test_model_thermodynamictemperatureunit_constructor_exists():
    assert callable(model_ThermodynamicTemperatureUnit.__init__)


def test_model_thermodynamictemperatureunit_constructor_args():
    sig = inspect.signature(model_ThermodynamicTemperatureUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_trafficintensityunit_is_not_abstract():
    assert not inspect.isabstract(model_TrafficIntensityUnit)


def test_model_trafficintensityunit_constructor_exists():
    assert callable(model_TrafficIntensityUnit.__init__)


def test_model_trafficintensityunit_constructor_args():
    sig = inspect.signature(model_TrafficIntensityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_levelunit_is_not_abstract():
    assert not inspect.isabstract(model_LevelUnit)


def test_model_levelunit_constructor_exists():
    assert callable(model_LevelUnit.__init__)


def test_model_levelunit_constructor_args():
    sig = inspect.signature(model_LevelUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_angleunit_is_not_abstract():
    assert not inspect.isabstract(model_AngleUnit)


def test_model_angleunit_constructor_exists():
    assert callable(model_AngleUnit.__init__)


def test_model_angleunit_constructor_args():
    sig = inspect.signature(model_AngleUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_entropyunit_is_not_abstract():
    assert not inspect.isabstract(model_EntropyUnit)


def test_model_entropyunit_constructor_exists():
    assert callable(model_EntropyUnit.__init__)


def test_model_entropyunit_constructor_args():
    sig = inspect.signature(model_EntropyUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_lengthunit_is_not_abstract():
    assert not inspect.isabstract(model_LengthUnit)


def test_model_lengthunit_constructor_exists():
    assert callable(model_LengthUnit.__init__)


def test_model_lengthunit_constructor_args():
    sig = inspect.signature(model_LengthUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_conversionfactor_is_not_abstract():
    assert not inspect.isabstract(model_ConversionFactor)


def test_model_conversionfactor_constructor_exists():
    assert callable(model_ConversionFactor.__init__)


def test_model_conversionfactor_constructor_args():
    sig = inspect.signature(model_ConversionFactor.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "multiplicator" in params, "Missing parameter 'multiplicator'"

def test_model_conversionfactor_has_offset():
    assert hasattr(model_ConversionFactor, "offset")
    descriptor = None
    for klass in model_ConversionFactor.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_model_conversionfactor_has_multiplicator():
    assert hasattr(model_ConversionFactor, "multiplicator")
    descriptor = None
    for klass in model_ConversionFactor.__mro__:
        if "multiplicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicator"]
            break
    assert isinstance(descriptor, property)



def test_model_dimension_is_not_abstract():
    assert not inspect.isabstract(model_Dimension)


def test_model_dimension_constructor_exists():
    assert callable(model_Dimension.__init__)


def test_model_dimension_constructor_args():
    sig = inspect.signature(model_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"

def test_model_dimension_has_exponent():
    assert hasattr(model_Dimension, "exponent")
    descriptor = None
    for klass in model_Dimension.__mro__:
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



def test_model_thermodynamictemperature_is_not_abstract():
    assert not inspect.isabstract(model_ThermodynamicTemperature)


def test_model_thermodynamictemperature_constructor_exists():
    assert callable(model_ThermodynamicTemperature.__init__)


def test_model_thermodynamictemperature_constructor_args():
    sig = inspect.signature(model_ThermodynamicTemperature.__init__)
    params = list(sig.parameters.keys())



def test_model_electriccurrent_is_not_abstract():
    assert not inspect.isabstract(model_ElectricCurrent)


def test_model_electriccurrent_constructor_exists():
    assert callable(model_ElectricCurrent.__init__)


def test_model_electriccurrent_constructor_args():
    sig = inspect.signature(model_ElectricCurrent.__init__)
    params = list(sig.parameters.keys())



def test_model_trafficintensity_is_not_abstract():
    assert not inspect.isabstract(model_TrafficIntensity)


def test_model_trafficintensity_constructor_exists():
    assert callable(model_TrafficIntensity.__init__)


def test_model_trafficintensity_constructor_args():
    sig = inspect.signature(model_TrafficIntensity.__init__)
    params = list(sig.parameters.keys())



def test_model_angle_is_not_abstract():
    assert not inspect.isabstract(model_Angle)


def test_model_angle_constructor_exists():
    assert callable(model_Angle.__init__)


def test_model_angle_constructor_args():
    sig = inspect.signature(model_Angle.__init__)
    params = list(sig.parameters.keys())



def test_model_datastoragecapacity_is_not_abstract():
    assert not inspect.isabstract(model_DataStorageCapacity)


def test_model_datastoragecapacity_constructor_exists():
    assert callable(model_DataStorageCapacity.__init__)


def test_model_datastoragecapacity_constructor_args():
    sig = inspect.signature(model_DataStorageCapacity.__init__)
    params = list(sig.parameters.keys())



def test_model_luminousintensity_is_not_abstract():
    assert not inspect.isabstract(model_LuminousIntensity)


def test_model_luminousintensity_constructor_exists():
    assert callable(model_LuminousIntensity.__init__)


def test_model_luminousintensity_constructor_args():
    sig = inspect.signature(model_LuminousIntensity.__init__)
    params = list(sig.parameters.keys())



def test_model_mass_is_not_abstract():
    assert not inspect.isabstract(model_Mass)


def test_model_mass_constructor_exists():
    assert callable(model_Mass.__init__)


def test_model_mass_constructor_args():
    sig = inspect.signature(model_Mass.__init__)
    params = list(sig.parameters.keys())



def test_model_amountofsubstance_is_not_abstract():
    assert not inspect.isabstract(model_AmountOfSubstance)


def test_model_amountofsubstance_constructor_exists():
    assert callable(model_AmountOfSubstance.__init__)


def test_model_amountofsubstance_constructor_args():
    sig = inspect.signature(model_AmountOfSubstance.__init__)
    params = list(sig.parameters.keys())



def test_model_level_is_not_abstract():
    assert not inspect.isabstract(model_Level)


def test_model_level_constructor_exists():
    assert callable(model_Level.__init__)


def test_model_level_constructor_args():
    sig = inspect.signature(model_Level.__init__)
    params = list(sig.parameters.keys())



def test_model_entropy_is_not_abstract():
    assert not inspect.isabstract(model_Entropy)


def test_model_entropy_constructor_exists():
    assert callable(model_Entropy.__init__)


def test_model_entropy_constructor_args():
    sig = inspect.signature(model_Entropy.__init__)
    params = list(sig.parameters.keys())



def test_model_time_is_not_abstract():
    assert not inspect.isabstract(model_Time)


def test_model_time_constructor_exists():
    assert callable(model_Time.__init__)


def test_model_time_constructor_args():
    sig = inspect.signature(model_Time.__init__)
    params = list(sig.parameters.keys())



def test_model_length_is_not_abstract():
    assert not inspect.isabstract(model_Length)


def test_model_length_constructor_exists():
    assert callable(model_Length.__init__)


def test_model_length_constructor_args():
    sig = inspect.signature(model_Length.__init__)
    params = list(sig.parameters.keys())



def test_model_quantityvalue_is_not_abstract():
    assert not inspect.isabstract(model_QuantityValue)


def test_model_quantityvalue_constructor_exists():
    assert callable(model_QuantityValue.__init__)


def test_model_quantityvalue_constructor_args():
    sig = inspect.signature(model_QuantityValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_quantityvalue_has_value():
    assert hasattr(model_QuantityValue, "value")
    descriptor = None
    for klass in model_QuantityValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_unit_is_not_abstract():
    assert not inspect.isabstract(model_Unit)


def test_model_unit_constructor_exists():
    assert callable(model_Unit.__init__)


def test_model_unit_constructor_args():
    sig = inspect.signature(model_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnit" in params, "Missing parameter 'isDerivedUnit'"
    assert "isRatioScaled" in params, "Missing parameter 'isRatioScaled'"
    assert "isIntervalScaled" in params, "Missing parameter 'isIntervalScaled'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isCoherentDerivedUnit" in params, "Missing parameter 'isCoherentDerivedUnit'"
    assert "isBaseUnit" in params, "Missing parameter 'isBaseUnit'"
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_model_unit_has_isDerivedUnit():
    assert hasattr(model_Unit, "isDerivedUnit")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "isDerivedUnit" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnit"]
            break
    assert isinstance(descriptor, property)

def test_model_unit_has_isRatioScaled():
    assert hasattr(model_Unit, "isRatioScaled")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "isRatioScaled" in klass.__dict__:
            descriptor = klass.__dict__["isRatioScaled"]
            break
    assert isinstance(descriptor, property)

def test_model_unit_has_isIntervalScaled():
    assert hasattr(model_Unit, "isIntervalScaled")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "isIntervalScaled" in klass.__dict__:
            descriptor = klass.__dict__["isIntervalScaled"]
            break
    assert isinstance(descriptor, property)

def test_model_unit_has_name():
    assert hasattr(model_Unit, "name")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_unit_has_isCoherentDerivedUnit():
    assert hasattr(model_Unit, "isCoherentDerivedUnit")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "isCoherentDerivedUnit" in klass.__dict__:
            descriptor = klass.__dict__["isCoherentDerivedUnit"]
            break
    assert isinstance(descriptor, property)

def test_model_unit_has_isBaseUnit():
    assert hasattr(model_Unit, "isBaseUnit")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "isBaseUnit" in klass.__dict__:
            descriptor = klass.__dict__["isBaseUnit"]
            break
    assert isinstance(descriptor, property)

def test_model_unit_has_symbol():
    assert hasattr(model_Unit, "symbol")
    descriptor = None
    for klass in model_Unit.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_model_quantity_is_not_abstract():
    assert not inspect.isabstract(model_Quantity)


def test_model_quantity_constructor_exists():
    assert callable(model_Quantity.__init__)


def test_model_quantity_constructor_args():
    sig = inspect.signature(model_Quantity.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_model_derivedquantityunit_is_not_abstract():
    assert not inspect.isabstract(model_DerivedQuantityUnit)


def test_model_derivedquantityunit_constructor_exists():
    assert callable(model_DerivedQuantityUnit.__init__)


def test_model_derivedquantityunit_constructor_args():
    sig = inspect.signature(model_DerivedQuantityUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_basequantityunit_is_not_abstract():
    assert not inspect.isabstract(model_BaseQuantityUnit)


def test_model_basequantityunit_constructor_exists():
    assert callable(model_BaseQuantityUnit.__init__)


def test_model_basequantityunit_constructor_args():
    sig = inspect.signature(model_BaseQuantityUnit.__init__)
    params = list(sig.parameters.keys())



def test_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_model_derivedquantity_is_not_abstract():
    assert not inspect.isabstract(model_DerivedQuantity)


def test_model_derivedquantity_constructor_exists():
    assert callable(model_DerivedQuantity.__init__)


def test_model_derivedquantity_constructor_args():
    sig = inspect.signature(model_DerivedQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model_basequantity_is_not_abstract():
    assert not inspect.isabstract(model_BaseQuantity)


def test_model_basequantity_constructor_exists():
    assert callable(model_BaseQuantity.__init__)


def test_model_basequantity_constructor_args():
    sig = inspect.signature(model_BaseQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model_sample_is_not_abstract():
    assert not inspect.isabstract(model_Sample)


def test_model_sample_constructor_exists():
    assert callable(model_Sample.__init__)


def test_model_sample_constructor_args():
    sig = inspect.signature(model_Sample.__init__)
    params = list(sig.parameters.keys())



def test_model_sampling_is_not_abstract():
    assert not inspect.isabstract(model_Sampling)


def test_model_sampling_constructor_exists():
    assert callable(model_Sampling.__init__)


def test_model_sampling_constructor_args():
    sig = inspect.signature(model_Sampling.__init__)
    params = list(sig.parameters.keys())
    assert "measurementProcedure" in params, "Missing parameter 'measurementProcedure'"

def test_model_sampling_has_measurementProcedure():
    assert hasattr(model_Sampling, "measurementProcedure")
    descriptor = None
    for klass in model_Sampling.__mro__:
        if "measurementProcedure" in klass.__dict__:
            descriptor = klass.__dict__["measurementProcedure"]
            break
    assert isinstance(descriptor, property)



def test_model_interval_is_not_abstract():
    assert not inspect.isabstract(model_Interval)


def test_model_interval_constructor_exists():
    assert callable(model_Interval.__init__)


def test_model_interval_constructor_args():
    sig = inspect.signature(model_Interval.__init__)
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
ConversionFactor_strategy = st.builds(
    ConversionFactor,
)
model_TimeConversionFactor_strategy = st.builds(
    model_TimeConversionFactor,
)
model_MassConversionFactor_strategy = st.builds(
    model_MassConversionFactor,
)
model_LengthConversionFactor_strategy = st.builds(
    model_LengthConversionFactor,
)
MeasurementUncertaintyInformation_strategy = st.builds(
    MeasurementUncertaintyInformation,
)
model_NormalDistribution_strategy = st.builds(
    model_NormalDistribution,
    standardDeviation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    meanValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_LevelConversionFactor_strategy = st.builds(
    model_LevelConversionFactor,
)
model_TrafficIntensityConversionFactor_strategy = st.builds(
    model_TrafficIntensityConversionFactor,
)
model_EntropyConversionFactor_strategy = st.builds(
    model_EntropyConversionFactor,
)
model_DataStorageCapacityConversionFactor_strategy = st.builds(
    model_DataStorageCapacityConversionFactor,
)
model_AngleConversionFactor_strategy = st.builds(
    model_AngleConversionFactor,
)
model_LuminousIntensityConversionFactor_strategy = st.builds(
    model_LuminousIntensityConversionFactor,
)
model_AmountOfSubstanceConversionFactor_strategy = st.builds(
    model_AmountOfSubstanceConversionFactor,
)
model_ThermodynamicTemperatureConversionFactor_strategy = st.builds(
    model_ThermodynamicTemperatureConversionFactor,
)
model_ElectricCurrentConversionFactor_strategy = st.builds(
    model_ElectricCurrentConversionFactor,
)
model_MeasurementUncertaintyInformation_strategy = st.builds(
    model_MeasurementUncertaintyInformation,
)
model_MeasurementUncertainty_strategy = st.builds(
    model_MeasurementUncertainty,
    standardUncertainty=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Dimension_strategy = st.builds(
    Dimension,
)
model_EntropyDimension_strategy = st.builds(
    model_EntropyDimension,
)
model_ElectricCurrentDimension_strategy = st.builds(
    model_ElectricCurrentDimension,
)
model_AmountOfSubstanceDimension_strategy = st.builds(
    model_AmountOfSubstanceDimension,
)
model_LevelDimension_strategy = st.builds(
    model_LevelDimension,
)
model_LuminousIntensityDimension_strategy = st.builds(
    model_LuminousIntensityDimension,
)
model_MassDimension_strategy = st.builds(
    model_MassDimension,
)
model_TimeDimension_strategy = st.builds(
    model_TimeDimension,
)
model_TrafficIntensityDimension_strategy = st.builds(
    model_TrafficIntensityDimension,
)
model_DataStorageCapacityDimension_strategy = st.builds(
    model_DataStorageCapacityDimension,
)
model_ThermodynamicTemperatureDimension_strategy = st.builds(
    model_ThermodynamicTemperatureDimension,
)
model_AngleDimension_strategy = st.builds(
    model_AngleDimension,
)
model_LengthDimension_strategy = st.builds(
    model_LengthDimension,
)
model_SystemOfUnits_strategy = st.builds(
    model_SystemOfUnits,
    name=
        safe_text,
    standardizationBody=
        safe_text
)
BaseQuantityUnit_strategy = st.builds(
    BaseQuantityUnit,
)
model_MassUnit_strategy = st.builds(
    model_MassUnit,
)
model_ElectricCurrentUnit_strategy = st.builds(
    model_ElectricCurrentUnit,
)
model_TimeUnit_strategy = st.builds(
    model_TimeUnit,
)
model_DataStorageCapacityUnit_strategy = st.builds(
    model_DataStorageCapacityUnit,
)
model_AmountOfSubstanceUnit_strategy = st.builds(
    model_AmountOfSubstanceUnit,
)
model_LuminousIntensityUnit_strategy = st.builds(
    model_LuminousIntensityUnit,
)
model_ThermodynamicTemperatureUnit_strategy = st.builds(
    model_ThermodynamicTemperatureUnit,
)
model_TrafficIntensityUnit_strategy = st.builds(
    model_TrafficIntensityUnit,
)
model_LevelUnit_strategy = st.builds(
    model_LevelUnit,
)
model_AngleUnit_strategy = st.builds(
    model_AngleUnit,
)
model_EntropyUnit_strategy = st.builds(
    model_EntropyUnit,
)
model_LengthUnit_strategy = st.builds(
    model_LengthUnit,
)
model_ConversionFactor_strategy = st.builds(
    model_ConversionFactor,
    offset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    multiplicator=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_Dimension_strategy = st.builds(
    model_Dimension,
    exponent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BaseQuantity_strategy = st.builds(
    BaseQuantity,
)
model_ThermodynamicTemperature_strategy = st.builds(
    model_ThermodynamicTemperature,
)
model_ElectricCurrent_strategy = st.builds(
    model_ElectricCurrent,
)
model_TrafficIntensity_strategy = st.builds(
    model_TrafficIntensity,
)
model_Angle_strategy = st.builds(
    model_Angle,
)
model_DataStorageCapacity_strategy = st.builds(
    model_DataStorageCapacity,
)
model_LuminousIntensity_strategy = st.builds(
    model_LuminousIntensity,
)
model_Mass_strategy = st.builds(
    model_Mass,
)
model_AmountOfSubstance_strategy = st.builds(
    model_AmountOfSubstance,
)
model_Level_strategy = st.builds(
    model_Level,
)
model_Entropy_strategy = st.builds(
    model_Entropy,
)
model_Time_strategy = st.builds(
    model_Time,
)
model_Length_strategy = st.builds(
    model_Length,
)
model_QuantityValue_strategy = st.builds(
    model_QuantityValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_Unit_strategy = st.builds(
    model_Unit,
    isDerivedUnit=
        st.booleans(),
    isRatioScaled=
        st.booleans(),
    isIntervalScaled=
        st.booleans(),
    name=
        safe_text,
    isCoherentDerivedUnit=
        st.booleans(),
    isBaseUnit=
        st.booleans(),
    symbol=
        safe_text
)
model_Quantity_strategy = st.builds(
    model_Quantity,
)
Unit_strategy = st.builds(
    Unit,
)
model_DerivedQuantityUnit_strategy = st.builds(
    model_DerivedQuantityUnit,
)
model_BaseQuantityUnit_strategy = st.builds(
    model_BaseQuantityUnit,
)
Quantity_strategy = st.builds(
    Quantity,
)
model_DerivedQuantity_strategy = st.builds(
    model_DerivedQuantity,
)
model_BaseQuantity_strategy = st.builds(
    model_BaseQuantity,
)
model_Sample_strategy = st.builds(
    model_Sample,
)
model_Sampling_strategy = st.builds(
    model_Sampling,
    measurementProcedure=
        safe_text
)
model_Interval_strategy = st.builds(
    model_Interval,
)

@given(instance=ConversionFactor_strategy)
@settings(max_examples=50)
def test_conversionfactor_instantiation(instance):
    assert isinstance(instance, ConversionFactor)

@given(instance=model_TimeConversionFactor_strategy)
@settings(max_examples=50)
def test_model_timeconversionfactor_instantiation(instance):
    assert isinstance(instance, model_TimeConversionFactor)

@given(instance=model_MassConversionFactor_strategy)
@settings(max_examples=50)
def test_model_massconversionfactor_instantiation(instance):
    assert isinstance(instance, model_MassConversionFactor)

@given(instance=model_LengthConversionFactor_strategy)
@settings(max_examples=50)
def test_model_lengthconversionfactor_instantiation(instance):
    assert isinstance(instance, model_LengthConversionFactor)

@given(instance=MeasurementUncertaintyInformation_strategy)
@settings(max_examples=50)
def test_measurementuncertaintyinformation_instantiation(instance):
    assert isinstance(instance, MeasurementUncertaintyInformation)

@given(instance=model_NormalDistribution_strategy)
@settings(max_examples=50)
def test_model_normaldistribution_instantiation(instance):
    assert isinstance(instance, model_NormalDistribution)



@given(instance=model_NormalDistribution_strategy)
def test_model_normaldistribution_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original



@given(instance=model_NormalDistribution_strategy)
def test_model_normaldistribution_meanValue_setter(instance):
    original = instance.meanValue
    instance.meanValue = original
    assert instance.meanValue == original

@given(instance=model_LevelConversionFactor_strategy)
@settings(max_examples=50)
def test_model_levelconversionfactor_instantiation(instance):
    assert isinstance(instance, model_LevelConversionFactor)

@given(instance=model_TrafficIntensityConversionFactor_strategy)
@settings(max_examples=50)
def test_model_trafficintensityconversionfactor_instantiation(instance):
    assert isinstance(instance, model_TrafficIntensityConversionFactor)

@given(instance=model_EntropyConversionFactor_strategy)
@settings(max_examples=50)
def test_model_entropyconversionfactor_instantiation(instance):
    assert isinstance(instance, model_EntropyConversionFactor)

@given(instance=model_DataStorageCapacityConversionFactor_strategy)
@settings(max_examples=50)
def test_model_datastoragecapacityconversionfactor_instantiation(instance):
    assert isinstance(instance, model_DataStorageCapacityConversionFactor)

@given(instance=model_AngleConversionFactor_strategy)
@settings(max_examples=50)
def test_model_angleconversionfactor_instantiation(instance):
    assert isinstance(instance, model_AngleConversionFactor)

@given(instance=model_LuminousIntensityConversionFactor_strategy)
@settings(max_examples=50)
def test_model_luminousintensityconversionfactor_instantiation(instance):
    assert isinstance(instance, model_LuminousIntensityConversionFactor)

@given(instance=model_AmountOfSubstanceConversionFactor_strategy)
@settings(max_examples=50)
def test_model_amountofsubstanceconversionfactor_instantiation(instance):
    assert isinstance(instance, model_AmountOfSubstanceConversionFactor)

@given(instance=model_ThermodynamicTemperatureConversionFactor_strategy)
@settings(max_examples=50)
def test_model_thermodynamictemperatureconversionfactor_instantiation(instance):
    assert isinstance(instance, model_ThermodynamicTemperatureConversionFactor)

@given(instance=model_ElectricCurrentConversionFactor_strategy)
@settings(max_examples=50)
def test_model_electriccurrentconversionfactor_instantiation(instance):
    assert isinstance(instance, model_ElectricCurrentConversionFactor)

@given(instance=model_MeasurementUncertaintyInformation_strategy)
@settings(max_examples=50)
def test_model_measurementuncertaintyinformation_instantiation(instance):
    assert isinstance(instance, model_MeasurementUncertaintyInformation)

@given(instance=model_MeasurementUncertainty_strategy)
@settings(max_examples=50)
def test_model_measurementuncertainty_instantiation(instance):
    assert isinstance(instance, model_MeasurementUncertainty)



@given(instance=model_MeasurementUncertainty_strategy)
def test_model_measurementuncertainty_standardUncertainty_setter(instance):
    original = instance.standardUncertainty
    instance.standardUncertainty = original
    assert instance.standardUncertainty == original

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=model_EntropyDimension_strategy)
@settings(max_examples=50)
def test_model_entropydimension_instantiation(instance):
    assert isinstance(instance, model_EntropyDimension)

@given(instance=model_ElectricCurrentDimension_strategy)
@settings(max_examples=50)
def test_model_electriccurrentdimension_instantiation(instance):
    assert isinstance(instance, model_ElectricCurrentDimension)

@given(instance=model_AmountOfSubstanceDimension_strategy)
@settings(max_examples=50)
def test_model_amountofsubstancedimension_instantiation(instance):
    assert isinstance(instance, model_AmountOfSubstanceDimension)

@given(instance=model_LevelDimension_strategy)
@settings(max_examples=50)
def test_model_leveldimension_instantiation(instance):
    assert isinstance(instance, model_LevelDimension)

@given(instance=model_LuminousIntensityDimension_strategy)
@settings(max_examples=50)
def test_model_luminousintensitydimension_instantiation(instance):
    assert isinstance(instance, model_LuminousIntensityDimension)

@given(instance=model_MassDimension_strategy)
@settings(max_examples=50)
def test_model_massdimension_instantiation(instance):
    assert isinstance(instance, model_MassDimension)

@given(instance=model_TimeDimension_strategy)
@settings(max_examples=50)
def test_model_timedimension_instantiation(instance):
    assert isinstance(instance, model_TimeDimension)

@given(instance=model_TrafficIntensityDimension_strategy)
@settings(max_examples=50)
def test_model_trafficintensitydimension_instantiation(instance):
    assert isinstance(instance, model_TrafficIntensityDimension)

@given(instance=model_DataStorageCapacityDimension_strategy)
@settings(max_examples=50)
def test_model_datastoragecapacitydimension_instantiation(instance):
    assert isinstance(instance, model_DataStorageCapacityDimension)

@given(instance=model_ThermodynamicTemperatureDimension_strategy)
@settings(max_examples=50)
def test_model_thermodynamictemperaturedimension_instantiation(instance):
    assert isinstance(instance, model_ThermodynamicTemperatureDimension)

@given(instance=model_AngleDimension_strategy)
@settings(max_examples=50)
def test_model_angledimension_instantiation(instance):
    assert isinstance(instance, model_AngleDimension)

@given(instance=model_LengthDimension_strategy)
@settings(max_examples=50)
def test_model_lengthdimension_instantiation(instance):
    assert isinstance(instance, model_LengthDimension)

@given(instance=model_SystemOfUnits_strategy)
@settings(max_examples=50)
def test_model_systemofunits_instantiation(instance):
    assert isinstance(instance, model_SystemOfUnits)



@given(instance=model_SystemOfUnits_strategy)
def test_model_systemofunits_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_SystemOfUnits_strategy)
def test_model_systemofunits_standardizationBody_setter(instance):
    original = instance.standardizationBody
    instance.standardizationBody = original
    assert instance.standardizationBody == original

@given(instance=BaseQuantityUnit_strategy)
@settings(max_examples=50)
def test_basequantityunit_instantiation(instance):
    assert isinstance(instance, BaseQuantityUnit)

@given(instance=model_MassUnit_strategy)
@settings(max_examples=50)
def test_model_massunit_instantiation(instance):
    assert isinstance(instance, model_MassUnit)

@given(instance=model_ElectricCurrentUnit_strategy)
@settings(max_examples=50)
def test_model_electriccurrentunit_instantiation(instance):
    assert isinstance(instance, model_ElectricCurrentUnit)

@given(instance=model_TimeUnit_strategy)
@settings(max_examples=50)
def test_model_timeunit_instantiation(instance):
    assert isinstance(instance, model_TimeUnit)

@given(instance=model_DataStorageCapacityUnit_strategy)
@settings(max_examples=50)
def test_model_datastoragecapacityunit_instantiation(instance):
    assert isinstance(instance, model_DataStorageCapacityUnit)

@given(instance=model_AmountOfSubstanceUnit_strategy)
@settings(max_examples=50)
def test_model_amountofsubstanceunit_instantiation(instance):
    assert isinstance(instance, model_AmountOfSubstanceUnit)

@given(instance=model_LuminousIntensityUnit_strategy)
@settings(max_examples=50)
def test_model_luminousintensityunit_instantiation(instance):
    assert isinstance(instance, model_LuminousIntensityUnit)

@given(instance=model_ThermodynamicTemperatureUnit_strategy)
@settings(max_examples=50)
def test_model_thermodynamictemperatureunit_instantiation(instance):
    assert isinstance(instance, model_ThermodynamicTemperatureUnit)

@given(instance=model_TrafficIntensityUnit_strategy)
@settings(max_examples=50)
def test_model_trafficintensityunit_instantiation(instance):
    assert isinstance(instance, model_TrafficIntensityUnit)

@given(instance=model_LevelUnit_strategy)
@settings(max_examples=50)
def test_model_levelunit_instantiation(instance):
    assert isinstance(instance, model_LevelUnit)

@given(instance=model_AngleUnit_strategy)
@settings(max_examples=50)
def test_model_angleunit_instantiation(instance):
    assert isinstance(instance, model_AngleUnit)

@given(instance=model_EntropyUnit_strategy)
@settings(max_examples=50)
def test_model_entropyunit_instantiation(instance):
    assert isinstance(instance, model_EntropyUnit)

@given(instance=model_LengthUnit_strategy)
@settings(max_examples=50)
def test_model_lengthunit_instantiation(instance):
    assert isinstance(instance, model_LengthUnit)

@given(instance=model_ConversionFactor_strategy)
@settings(max_examples=50)
def test_model_conversionfactor_instantiation(instance):
    assert isinstance(instance, model_ConversionFactor)



@given(instance=model_ConversionFactor_strategy)
def test_model_conversionfactor_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original



@given(instance=model_ConversionFactor_strategy)
def test_model_conversionfactor_multiplicator_setter(instance):
    original = instance.multiplicator
    instance.multiplicator = original
    assert instance.multiplicator == original

@given(instance=model_Dimension_strategy)
@settings(max_examples=50)
def test_model_dimension_instantiation(instance):
    assert isinstance(instance, model_Dimension)



@given(instance=model_Dimension_strategy)
def test_model_dimension_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original

@given(instance=BaseQuantity_strategy)
@settings(max_examples=50)
def test_basequantity_instantiation(instance):
    assert isinstance(instance, BaseQuantity)

@given(instance=model_ThermodynamicTemperature_strategy)
@settings(max_examples=50)
def test_model_thermodynamictemperature_instantiation(instance):
    assert isinstance(instance, model_ThermodynamicTemperature)

@given(instance=model_ElectricCurrent_strategy)
@settings(max_examples=50)
def test_model_electriccurrent_instantiation(instance):
    assert isinstance(instance, model_ElectricCurrent)

@given(instance=model_TrafficIntensity_strategy)
@settings(max_examples=50)
def test_model_trafficintensity_instantiation(instance):
    assert isinstance(instance, model_TrafficIntensity)

@given(instance=model_Angle_strategy)
@settings(max_examples=50)
def test_model_angle_instantiation(instance):
    assert isinstance(instance, model_Angle)

@given(instance=model_DataStorageCapacity_strategy)
@settings(max_examples=50)
def test_model_datastoragecapacity_instantiation(instance):
    assert isinstance(instance, model_DataStorageCapacity)

@given(instance=model_LuminousIntensity_strategy)
@settings(max_examples=50)
def test_model_luminousintensity_instantiation(instance):
    assert isinstance(instance, model_LuminousIntensity)

@given(instance=model_Mass_strategy)
@settings(max_examples=50)
def test_model_mass_instantiation(instance):
    assert isinstance(instance, model_Mass)

@given(instance=model_AmountOfSubstance_strategy)
@settings(max_examples=50)
def test_model_amountofsubstance_instantiation(instance):
    assert isinstance(instance, model_AmountOfSubstance)

@given(instance=model_Level_strategy)
@settings(max_examples=50)
def test_model_level_instantiation(instance):
    assert isinstance(instance, model_Level)

@given(instance=model_Entropy_strategy)
@settings(max_examples=50)
def test_model_entropy_instantiation(instance):
    assert isinstance(instance, model_Entropy)

@given(instance=model_Time_strategy)
@settings(max_examples=50)
def test_model_time_instantiation(instance):
    assert isinstance(instance, model_Time)

@given(instance=model_Length_strategy)
@settings(max_examples=50)
def test_model_length_instantiation(instance):
    assert isinstance(instance, model_Length)

@given(instance=model_QuantityValue_strategy)
@settings(max_examples=50)
def test_model_quantityvalue_instantiation(instance):
    assert isinstance(instance, model_QuantityValue)



@given(instance=model_QuantityValue_strategy)
def test_model_quantityvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_Unit_strategy)
@settings(max_examples=50)
def test_model_unit_instantiation(instance):
    assert isinstance(instance, model_Unit)



@given(instance=model_Unit_strategy)
def test_model_unit_isDerivedUnit_setter(instance):
    original = instance.isDerivedUnit
    instance.isDerivedUnit = original
    assert instance.isDerivedUnit == original



@given(instance=model_Unit_strategy)
def test_model_unit_isRatioScaled_setter(instance):
    original = instance.isRatioScaled
    instance.isRatioScaled = original
    assert instance.isRatioScaled == original



@given(instance=model_Unit_strategy)
def test_model_unit_isIntervalScaled_setter(instance):
    original = instance.isIntervalScaled
    instance.isIntervalScaled = original
    assert instance.isIntervalScaled == original



@given(instance=model_Unit_strategy)
def test_model_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Unit_strategy)
def test_model_unit_isCoherentDerivedUnit_setter(instance):
    original = instance.isCoherentDerivedUnit
    instance.isCoherentDerivedUnit = original
    assert instance.isCoherentDerivedUnit == original



@given(instance=model_Unit_strategy)
def test_model_unit_isBaseUnit_setter(instance):
    original = instance.isBaseUnit
    instance.isBaseUnit = original
    assert instance.isBaseUnit == original



@given(instance=model_Unit_strategy)
def test_model_unit_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=model_Quantity_strategy)
@settings(max_examples=50)
def test_model_quantity_instantiation(instance):
    assert isinstance(instance, model_Quantity)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=model_DerivedQuantityUnit_strategy)
@settings(max_examples=50)
def test_model_derivedquantityunit_instantiation(instance):
    assert isinstance(instance, model_DerivedQuantityUnit)

@given(instance=model_BaseQuantityUnit_strategy)
@settings(max_examples=50)
def test_model_basequantityunit_instantiation(instance):
    assert isinstance(instance, model_BaseQuantityUnit)

@given(instance=Quantity_strategy)
@settings(max_examples=50)
def test_quantity_instantiation(instance):
    assert isinstance(instance, Quantity)

@given(instance=model_DerivedQuantity_strategy)
@settings(max_examples=50)
def test_model_derivedquantity_instantiation(instance):
    assert isinstance(instance, model_DerivedQuantity)

@given(instance=model_BaseQuantity_strategy)
@settings(max_examples=50)
def test_model_basequantity_instantiation(instance):
    assert isinstance(instance, model_BaseQuantity)

@given(instance=model_Sample_strategy)
@settings(max_examples=50)
def test_model_sample_instantiation(instance):
    assert isinstance(instance, model_Sample)

@given(instance=model_Sampling_strategy)
@settings(max_examples=50)
def test_model_sampling_instantiation(instance):
    assert isinstance(instance, model_Sampling)



@given(instance=model_Sampling_strategy)
def test_model_sampling_measurementProcedure_setter(instance):
    original = instance.measurementProcedure
    instance.measurementProcedure = original
    assert instance.measurementProcedure == original

@given(instance=model_Interval_strategy)
@settings(max_examples=50)
def test_model_interval_instantiation(instance):
    assert isinstance(instance, model_Interval)
