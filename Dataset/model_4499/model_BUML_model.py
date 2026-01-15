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

# Classes
model_Quantity = Class(name="model::Quantity", is_abstract=True)
model_Unit = Class(name="model::Unit", is_abstract=True)
model_QuantityValue = Class(name="model::QuantityValue")
model_Length = Class(name="model::Length")
BaseQuantity = Class(name="BaseQuantity")
model_Angle = Class(name="model::Angle")
model_Dimension = Class(name="model::Dimension", is_abstract=True)
model_ConversionFactor = Class(name="model::ConversionFactor", is_abstract=True)
model_ElectricCurrent = Class(name="model::ElectricCurrent")
model_ThermodynamicTemperature = Class(name="model::ThermodynamicTemperature")
model_AmountOfSubstance = Class(name="model::AmountOfSubstance")
model_LuminousIntensity = Class(name="model::LuminousIntensity")
model_LengthUnit = Class(name="model::LengthUnit")
BaseQuantityUnit = Class(name="BaseQuantityUnit")
model_MassUnit = Class(name="model::MassUnit")
model_Mass = Class(name="model::Mass")
model_Time = Class(name="model::Time")
model_LuminousIntensityUnit = Class(name="model::LuminousIntensityUnit")
model_AngleUnit = Class(name="model::AngleUnit")
model_SystemOfUnits = Class(name="model::SystemOfUnits")
model_LengthDimension = Class(name="model::LengthDimension")
Dimension = Class(name="Dimension")
model_MassDimension = Class(name="model::MassDimension")
model_TimeDimension = Class(name="model::TimeDimension")
model_ElectricCurrentDimension = Class(name="model::ElectricCurrentDimension")
model_TimeUnit = Class(name="model::TimeUnit")
model_ElectricCurrentUnit = Class(name="model::ElectricCurrentUnit")
model_ThermodynamicTemperatureUnit = Class(name="model::ThermodynamicTemperatureUnit")
model_AmountOfSubstanceUnit = Class(name="model::AmountOfSubstanceUnit")
model_DataStorageCapacity = Class(name="model::DataStorageCapacity")
model_Entropy = Class(name="model::Entropy")
model_TrafficIntensity = Class(name="model::TrafficIntensity")
model_Level = Class(name="model::Level")
model_DataStorageCapacityUnit = Class(name="model::DataStorageCapacityUnit")
model_EntropyUnit = Class(name="model::EntropyUnit")
model_TrafficIntensityUnit = Class(name="model::TrafficIntensityUnit")
model_LevelUnit = Class(name="model::LevelUnit")
model_ThermodynamicTemperatureDimension = Class(name="model::ThermodynamicTemperatureDimension")
model_AmountOfSubstanceDimension = Class(name="model::AmountOfSubstanceDimension")
model_LuminousIntensityDimension = Class(name="model::LuminousIntensityDimension")
model_AngleDimension = Class(name="model::AngleDimension")
model_MeasurementUncertainty = Class(name="model::MeasurementUncertainty")
model_MeasurementUncertaintyInformation = Class(name="model::MeasurementUncertaintyInformation", is_abstract=True)
model_DataStorageCapacityConversionFactor = Class(name="model::DataStorageCapacityConversionFactor")
model_EntropyConversionFactor = Class(name="model::EntropyConversionFactor")
model_TrafficIntensityConversionFactor = Class(name="model::TrafficIntensityConversionFactor")
model_LevelConversionFactor = Class(name="model::LevelConversionFactor")
model_NormalDistribution = Class(name="model::NormalDistribution")
MeasurementUncertaintyInformation = Class(name="MeasurementUncertaintyInformation")
model_Interval = Class(name="model::Interval")
model_Sampling = Class(name="model::Sampling")
model_Sample = Class(name="model::Sample")
model_BaseQuantity = Class(name="model::BaseQuantity", is_abstract=True)
Quantity = Class(name="Quantity")
model_DerivedQuantity = Class(name="model::DerivedQuantity", is_abstract=True)
model_DataStorageCapacityDimension = Class(name="model::DataStorageCapacityDimension")
model_EntropyDimension = Class(name="model::EntropyDimension")
model_TrafficIntensityDimension = Class(name="model::TrafficIntensityDimension")
model_LevelDimension = Class(name="model::LevelDimension")
model_LengthConversionFactor = Class(name="model::LengthConversionFactor")
ConversionFactor = Class(name="ConversionFactor")
model_MassConversionFactor = Class(name="model::MassConversionFactor")
model_TimeConversionFactor = Class(name="model::TimeConversionFactor")
model_ElectricCurrentConversionFactor = Class(name="model::ElectricCurrentConversionFactor")
model_ThermodynamicTemperatureConversionFactor = Class(name="model::ThermodynamicTemperatureConversionFactor")
model_AmountOfSubstanceConversionFactor = Class(name="model::AmountOfSubstanceConversionFactor")
model_LuminousIntensityConversionFactor = Class(name="model::LuminousIntensityConversionFactor")
model_AngleConversionFactor = Class(name="model::AngleConversionFactor")
model_BaseQuantityUnit = Class(name="model::BaseQuantityUnit", is_abstract=True)
Unit = Class(name="Unit")
model_DerivedQuantityUnit = Class(name="model::DerivedQuantityUnit", is_abstract=True)

# model_Quantity class attributes and methods

# model_Unit class attributes and methods
model_Unit_name: Property = Property(name="name", type=StringType)
model_Unit_symbol: Property = Property(name="symbol", type=StringType)
model_Unit_isRatioScaled: Property = Property(name="isRatioScaled", type=BooleanType)
model_Unit_isBaseUnit: Property = Property(name="isBaseUnit", type=BooleanType)
model_Unit_isDerivedUnit: Property = Property(name="isDerivedUnit", type=BooleanType)
model_Unit_isCoherentDerivedUnit: Property = Property(name="isCoherentDerivedUnit", type=BooleanType)
model_Unit_isIntervalScaled: Property = Property(name="isIntervalScaled", type=BooleanType)
model_Unit.attributes={model_Unit_isDerivedUnit, model_Unit_isCoherentDerivedUnit, model_Unit_name, model_Unit_isIntervalScaled, model_Unit_symbol, model_Unit_isBaseUnit, model_Unit_isRatioScaled}

# model_QuantityValue class attributes and methods
model_QuantityValue_value: Property = Property(name="value", type=FloatType)
model_QuantityValue.attributes={model_QuantityValue_value}

# model_Length class attributes and methods

# BaseQuantity class attributes and methods

# model_Angle class attributes and methods

# model_Dimension class attributes and methods
model_Dimension_exponent: Property = Property(name="exponent", type=FloatType)
model_Dimension.attributes={model_Dimension_exponent}

# model_ConversionFactor class attributes and methods
model_ConversionFactor_multiplicator: Property = Property(name="multiplicator", type=FloatType)
model_ConversionFactor_offset: Property = Property(name="offset", type=FloatType)
model_ConversionFactor.attributes={model_ConversionFactor_offset, model_ConversionFactor_multiplicator}

# model_ElectricCurrent class attributes and methods

# model_ThermodynamicTemperature class attributes and methods

# model_AmountOfSubstance class attributes and methods

# model_LuminousIntensity class attributes and methods

# model_LengthUnit class attributes and methods

# BaseQuantityUnit class attributes and methods

# model_MassUnit class attributes and methods

# model_Mass class attributes and methods

# model_Time class attributes and methods

# model_LuminousIntensityUnit class attributes and methods

# model_AngleUnit class attributes and methods

# model_SystemOfUnits class attributes and methods
model_SystemOfUnits_name: Property = Property(name="name", type=StringType)
model_SystemOfUnits_standardizationBody: Property = Property(name="standardizationBody", type=StringType)
model_SystemOfUnits.attributes={model_SystemOfUnits_name, model_SystemOfUnits_standardizationBody}

# model_LengthDimension class attributes and methods

# Dimension class attributes and methods

# model_MassDimension class attributes and methods

# model_TimeDimension class attributes and methods

# model_ElectricCurrentDimension class attributes and methods

# model_TimeUnit class attributes and methods

# model_ElectricCurrentUnit class attributes and methods

# model_ThermodynamicTemperatureUnit class attributes and methods

# model_AmountOfSubstanceUnit class attributes and methods

# model_DataStorageCapacity class attributes and methods

# model_Entropy class attributes and methods

# model_TrafficIntensity class attributes and methods

# model_Level class attributes and methods

# model_DataStorageCapacityUnit class attributes and methods

# model_EntropyUnit class attributes and methods

# model_TrafficIntensityUnit class attributes and methods

# model_LevelUnit class attributes and methods

# model_ThermodynamicTemperatureDimension class attributes and methods

# model_AmountOfSubstanceDimension class attributes and methods

# model_LuminousIntensityDimension class attributes and methods

# model_AngleDimension class attributes and methods

# model_MeasurementUncertainty class attributes and methods
model_MeasurementUncertainty_standardUncertainty: Property = Property(name="standardUncertainty", type=FloatType)
model_MeasurementUncertainty.attributes={model_MeasurementUncertainty_standardUncertainty}

# model_MeasurementUncertaintyInformation class attributes and methods

# model_DataStorageCapacityConversionFactor class attributes and methods

# model_EntropyConversionFactor class attributes and methods

# model_TrafficIntensityConversionFactor class attributes and methods

# model_LevelConversionFactor class attributes and methods

# model_NormalDistribution class attributes and methods
model_NormalDistribution_meanValue: Property = Property(name="meanValue", type=FloatType)
model_NormalDistribution_standardDeviation: Property = Property(name="standardDeviation", type=FloatType)
model_NormalDistribution.attributes={model_NormalDistribution_standardDeviation, model_NormalDistribution_meanValue}

# MeasurementUncertaintyInformation class attributes and methods

# model_Interval class attributes and methods

# model_Sampling class attributes and methods
model_Sampling_measurementProcedure: Property = Property(name="measurementProcedure", type=StringType)
model_Sampling.attributes={model_Sampling_measurementProcedure}

# model_Sample class attributes and methods

# model_BaseQuantity class attributes and methods

# Quantity class attributes and methods

# model_DerivedQuantity class attributes and methods

# model_DataStorageCapacityDimension class attributes and methods

# model_EntropyDimension class attributes and methods

# model_TrafficIntensityDimension class attributes and methods

# model_LevelDimension class attributes and methods

# model_LengthConversionFactor class attributes and methods

# ConversionFactor class attributes and methods

# model_MassConversionFactor class attributes and methods

# model_TimeConversionFactor class attributes and methods

# model_ElectricCurrentConversionFactor class attributes and methods

# model_ThermodynamicTemperatureConversionFactor class attributes and methods

# model_AmountOfSubstanceConversionFactor class attributes and methods

# model_LuminousIntensityConversionFactor class attributes and methods

# model_AngleConversionFactor class attributes and methods

# model_BaseQuantityUnit class attributes and methods

# Unit class attributes and methods

# model_DerivedQuantityUnit class attributes and methods

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="model_Unit", type=model_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Quantity", type=model_Unit, multiplicity=Multiplicity(1, 1))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="model_QuantityValue", type=model_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Quantity2", type=model_QuantityValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions3: BinaryAssociation = BinaryAssociation(
    name="dimensions3",
    ends={
        Property(name="model_Dimension", type=model_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Unit4", type=model_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversionFactors5: BinaryAssociation = BinaryAssociation(
    name="conversionFactors5",
    ends={
        Property(name="model_ConversionFactor", type=model_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Unit6", type=model_ConversionFactor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units7: BinaryAssociation = BinaryAssociation(
    name="units7",
    ends={
        Property(name="model_Unit8", type=model_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SystemOfUnits", type=model_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseUnit9: BinaryAssociation = BinaryAssociation(
    name="baseUnit9",
    ends={
        Property(name="model_Unit11", type=model_ConversionFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ConversionFactor10", type=model_Unit, multiplicity=Multiplicity(1, 1))
    }
)
uncertainty12: BinaryAssociation = BinaryAssociation(
    name="uncertainty12",
    ends={
        Property(name="model_MeasurementUncertainty", type=model_QuantityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_QuantityValue13", type=model_MeasurementUncertainty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
information14: BinaryAssociation = BinaryAssociation(
    name="information14",
    ends={
        Property(name="model_MeasurementUncertaintyInformation", type=model_MeasurementUncertainty, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MeasurementUncertainty15", type=model_MeasurementUncertaintyInformation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerEndpoint16: BinaryAssociation = BinaryAssociation(
    name="lowerEndpoint16",
    ends={
        Property(name="model_Quantity17", type=model_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Interval", type=model_Quantity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperEndpoint18: BinaryAssociation = BinaryAssociation(
    name="upperEndpoint18",
    ends={
        Property(name="model_Quantity20", type=model_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Interval19", type=model_Quantity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
samples21: BinaryAssociation = BinaryAssociation(
    name="samples21",
    ends={
        Property(name="model_Sample", type=model_Sampling, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Sampling", type=model_Sample, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
quantity22: BinaryAssociation = BinaryAssociation(
    name="quantity22",
    ends={
        Property(name="model_Quantity24", type=model_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Sample23", type=model_Quantity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_Length_BaseQuantity = Generalization(general=BaseQuantity, specific=model_Length)
gen_model_Angle_BaseQuantity = Generalization(general=BaseQuantity, specific=model_Angle)
gen_model_ElectricCurrent_BaseQuantity = Generalization(general=BaseQuantity, specific=model_ElectricCurrent)
gen_model_ThermodynamicTemperature_BaseQuantity = Generalization(general=BaseQuantity, specific=model_ThermodynamicTemperature)
gen_model_AmountOfSubstance_BaseQuantity = Generalization(general=BaseQuantity, specific=model_AmountOfSubstance)
gen_model_LuminousIntensity_BaseQuantity = Generalization(general=BaseQuantity, specific=model_LuminousIntensity)
gen_model_LengthUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_LengthUnit)
gen_model_MassUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_MassUnit)
gen_model_Mass_BaseQuantity = Generalization(general=BaseQuantity, specific=model_Mass)
gen_model_Time_BaseQuantity = Generalization(general=BaseQuantity, specific=model_Time)
gen_model_LuminousIntensityUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_LuminousIntensityUnit)
gen_model_AngleUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_AngleUnit)
gen_model_LengthDimension_Dimension = Generalization(general=Dimension, specific=model_LengthDimension)
gen_model_MassDimension_Dimension = Generalization(general=Dimension, specific=model_MassDimension)
gen_model_TimeDimension_Dimension = Generalization(general=Dimension, specific=model_TimeDimension)
gen_model_ElectricCurrentDimension_Dimension = Generalization(general=Dimension, specific=model_ElectricCurrentDimension)
gen_model_TimeUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_TimeUnit)
gen_model_ElectricCurrentUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_ElectricCurrentUnit)
gen_model_ThermodynamicTemperatureUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_ThermodynamicTemperatureUnit)
gen_model_AmountOfSubstanceUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_AmountOfSubstanceUnit)
gen_model_DataStorageCapacity_BaseQuantity = Generalization(general=BaseQuantity, specific=model_DataStorageCapacity)
gen_model_Entropy_BaseQuantity = Generalization(general=BaseQuantity, specific=model_Entropy)
gen_model_TrafficIntensity_BaseQuantity = Generalization(general=BaseQuantity, specific=model_TrafficIntensity)
gen_model_Level_BaseQuantity = Generalization(general=BaseQuantity, specific=model_Level)
gen_model_DataStorageCapacityUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_DataStorageCapacityUnit)
gen_model_EntropyUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_EntropyUnit)
gen_model_TrafficIntensityUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_TrafficIntensityUnit)
gen_model_LevelUnit_BaseQuantityUnit = Generalization(general=BaseQuantityUnit, specific=model_LevelUnit)
gen_model_ThermodynamicTemperatureDimension_Dimension = Generalization(general=Dimension, specific=model_ThermodynamicTemperatureDimension)
gen_model_AmountOfSubstanceDimension_Dimension = Generalization(general=Dimension, specific=model_AmountOfSubstanceDimension)
gen_model_LuminousIntensityDimension_Dimension = Generalization(general=Dimension, specific=model_LuminousIntensityDimension)
gen_model_AngleDimension_Dimension = Generalization(general=Dimension, specific=model_AngleDimension)
gen_model_AngleConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_AngleConversionFactor)
gen_model_DataStorageCapacityConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_DataStorageCapacityConversionFactor)
gen_model_EntropyConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_EntropyConversionFactor)
gen_model_TrafficIntensityConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_TrafficIntensityConversionFactor)
gen_model_LevelConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_LevelConversionFactor)
gen_model_NormalDistribution_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=model_NormalDistribution)
gen_model_Interval_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=model_Interval)
gen_model_Sampling_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=model_Sampling)
gen_model_BaseQuantity_Quantity = Generalization(general=Quantity, specific=model_BaseQuantity)
gen_model_DerivedQuantity_Quantity = Generalization(general=Quantity, specific=model_DerivedQuantity)
gen_model_DataStorageCapacityDimension_Dimension = Generalization(general=Dimension, specific=model_DataStorageCapacityDimension)
gen_model_EntropyDimension_Dimension = Generalization(general=Dimension, specific=model_EntropyDimension)
gen_model_TrafficIntensityDimension_Dimension = Generalization(general=Dimension, specific=model_TrafficIntensityDimension)
gen_model_LevelDimension_Dimension = Generalization(general=Dimension, specific=model_LevelDimension)
gen_model_LengthConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_LengthConversionFactor)
gen_model_MassConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_MassConversionFactor)
gen_model_TimeConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_TimeConversionFactor)
gen_model_ElectricCurrentConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_ElectricCurrentConversionFactor)
gen_model_ThermodynamicTemperatureConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_ThermodynamicTemperatureConversionFactor)
gen_model_AmountOfSubstanceConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_AmountOfSubstanceConversionFactor)
gen_model_LuminousIntensityConversionFactor_ConversionFactor = Generalization(general=ConversionFactor, specific=model_LuminousIntensityConversionFactor)
gen_model_BaseQuantityUnit_Unit = Generalization(general=Unit, specific=model_BaseQuantityUnit)
gen_model_DerivedQuantityUnit_Unit = Generalization(general=Unit, specific=model_DerivedQuantityUnit)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Quantity, model_Unit, model_QuantityValue, model_Length, BaseQuantity, model_Angle, model_Dimension, model_ConversionFactor, model_ElectricCurrent, model_ThermodynamicTemperature, model_AmountOfSubstance, model_LuminousIntensity, model_LengthUnit, BaseQuantityUnit, model_MassUnit, model_Mass, model_Time, model_LuminousIntensityUnit, model_AngleUnit, model_SystemOfUnits, model_LengthDimension, Dimension, model_MassDimension, model_TimeDimension, model_ElectricCurrentDimension, model_TimeUnit, model_ElectricCurrentUnit, model_ThermodynamicTemperatureUnit, model_AmountOfSubstanceUnit, model_DataStorageCapacity, model_Entropy, model_TrafficIntensity, model_Level, model_DataStorageCapacityUnit, model_EntropyUnit, model_TrafficIntensityUnit, model_LevelUnit, model_ThermodynamicTemperatureDimension, model_AmountOfSubstanceDimension, model_LuminousIntensityDimension, model_AngleDimension, model_MeasurementUncertainty, model_MeasurementUncertaintyInformation, model_DataStorageCapacityConversionFactor, model_EntropyConversionFactor, model_TrafficIntensityConversionFactor, model_LevelConversionFactor, model_NormalDistribution, MeasurementUncertaintyInformation, model_Interval, model_Sampling, model_Sample, model_BaseQuantity, Quantity, model_DerivedQuantity, model_DataStorageCapacityDimension, model_EntropyDimension, model_TrafficIntensityDimension, model_LevelDimension, model_LengthConversionFactor, ConversionFactor, model_MassConversionFactor, model_TimeConversionFactor, model_ElectricCurrentConversionFactor, model_ThermodynamicTemperatureConversionFactor, model_AmountOfSubstanceConversionFactor, model_LuminousIntensityConversionFactor, model_AngleConversionFactor, model_BaseQuantityUnit, Unit, model_DerivedQuantityUnit},
    associations={unit0, value1, dimensions3, conversionFactors5, units7, baseUnit9, uncertainty12, information14, lowerEndpoint16, upperEndpoint18, samples21, quantity22},
    generalizations={gen_model_Length_BaseQuantity, gen_model_Angle_BaseQuantity, gen_model_ElectricCurrent_BaseQuantity, gen_model_ThermodynamicTemperature_BaseQuantity, gen_model_AmountOfSubstance_BaseQuantity, gen_model_LuminousIntensity_BaseQuantity, gen_model_LengthUnit_BaseQuantityUnit, gen_model_MassUnit_BaseQuantityUnit, gen_model_Mass_BaseQuantity, gen_model_Time_BaseQuantity, gen_model_LuminousIntensityUnit_BaseQuantityUnit, gen_model_AngleUnit_BaseQuantityUnit, gen_model_LengthDimension_Dimension, gen_model_MassDimension_Dimension, gen_model_TimeDimension_Dimension, gen_model_ElectricCurrentDimension_Dimension, gen_model_TimeUnit_BaseQuantityUnit, gen_model_ElectricCurrentUnit_BaseQuantityUnit, gen_model_ThermodynamicTemperatureUnit_BaseQuantityUnit, gen_model_AmountOfSubstanceUnit_BaseQuantityUnit, gen_model_DataStorageCapacity_BaseQuantity, gen_model_Entropy_BaseQuantity, gen_model_TrafficIntensity_BaseQuantity, gen_model_Level_BaseQuantity, gen_model_DataStorageCapacityUnit_BaseQuantityUnit, gen_model_EntropyUnit_BaseQuantityUnit, gen_model_TrafficIntensityUnit_BaseQuantityUnit, gen_model_LevelUnit_BaseQuantityUnit, gen_model_ThermodynamicTemperatureDimension_Dimension, gen_model_AmountOfSubstanceDimension_Dimension, gen_model_LuminousIntensityDimension_Dimension, gen_model_AngleDimension_Dimension, gen_model_AngleConversionFactor_ConversionFactor, gen_model_DataStorageCapacityConversionFactor_ConversionFactor, gen_model_EntropyConversionFactor_ConversionFactor, gen_model_TrafficIntensityConversionFactor_ConversionFactor, gen_model_LevelConversionFactor_ConversionFactor, gen_model_NormalDistribution_MeasurementUncertaintyInformation, gen_model_Interval_MeasurementUncertaintyInformation, gen_model_Sampling_MeasurementUncertaintyInformation, gen_model_BaseQuantity_Quantity, gen_model_DerivedQuantity_Quantity, gen_model_DataStorageCapacityDimension_Dimension, gen_model_EntropyDimension_Dimension, gen_model_TrafficIntensityDimension_Dimension, gen_model_LevelDimension_Dimension, gen_model_LengthConversionFactor_ConversionFactor, gen_model_MassConversionFactor_ConversionFactor, gen_model_TimeConversionFactor_ConversionFactor, gen_model_ElectricCurrentConversionFactor_ConversionFactor, gen_model_ThermodynamicTemperatureConversionFactor_ConversionFactor, gen_model_AmountOfSubstanceConversionFactor_ConversionFactor, gen_model_LuminousIntensityConversionFactor_ConversionFactor, gen_model_BaseQuantityUnit_Unit, gen_model_DerivedQuantityUnit_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)