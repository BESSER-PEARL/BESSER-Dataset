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
Accumulator: Enumeration = Enumeration(
    name="Accumulator",
    literals={
            EnumerationLiteral(name="maximum"),
			EnumerationLiteral(name="minimum"),
			EnumerationLiteral(name="average"),
			EnumerationLiteral(name="standardDeviation"),
			EnumerationLiteral(name="product"),
			EnumerationLiteral(name="custom"),
			EnumerationLiteral(name="sum")
    }
)

MeasurementScale: Enumeration = Enumeration(
    name="MeasurementScale",
    literals={
            EnumerationLiteral(name="ordinal"),
			EnumerationLiteral(name="nominal"),
			EnumerationLiteral(name="ratio"),
			EnumerationLiteral(name="interval")
    }
)

Influence: Enumeration = Enumeration(
    name="Influence",
    literals={
            EnumerationLiteral(name="positive"),
			EnumerationLiteral(name="negative")
    }
)

BinaryFunctor: Enumeration = Enumeration(
    name="BinaryFunctor",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="custom")
    }
)

ScaleOfMeasurement: Enumeration = Enumeration(
    name="ScaleOfMeasurement",
    literals={
            EnumerationLiteral(name="nominal"),
			EnumerationLiteral(name="ordinal"),
			EnumerationLiteral(name="interval"),
			EnumerationLiteral(name="ratio"),
			EnumerationLiteral(name="custom")
    }
)

# Classes
smm_Annotation = Class(name="smm::Annotation")
smm_Argument = Class(name="smm::Argument")
smm_AbstractMeasureElement = Class(name="smm::AbstractMeasureElement", is_abstract=True)
SmmElement = Class(name="SmmElement")
smm_CategoryRelationship = Class(name="smm::CategoryRelationship")
SmmRelationship = Class(name="SmmRelationship")
smm_Characteristic = Class(name="smm::Characteristic")
AbstractMeasureElement = Class(name="AbstractMeasureElement")
smm_CollectiveMeasure = Class(name="smm::CollectiveMeasure")
smm_ObservedMeasure = Class(name="smm::ObservedMeasure")
smm_Attribute = Class(name="smm::Attribute")
smm_Base1MeasureRelationship = Class(name="smm::Base1MeasureRelationship")
ScaledBaseMeasureRelationship = Class(name="ScaledBaseMeasureRelationship")
smm_Base1MeasurementRelationship = Class(name="smm::Base1MeasurementRelationship")
ScaledBaseMeasurementRelationship = Class(name="ScaledBaseMeasurementRelationship")
smm_Base2MeasureRelationship = Class(name="smm::Base2MeasureRelationship")
smm_Base2MeasurementRelationship = Class(name="smm::Base2MeasurementRelationship")
smm_BaseNMeasureRelationship = Class(name="smm::BaseNMeasureRelationship")
smm_BaseNMeasurementRelationship = Class(name="smm::BaseNMeasurementRelationship")
smm_BinaryMeasure = Class(name="smm::BinaryMeasure")
DimensionalMeasure = Class(name="DimensionalMeasure")
smm_Operation = Class(name="smm::Operation")
smm_BinaryMeasurement = Class(name="smm::BinaryMeasurement")
DimensionalMeasurement = Class(name="DimensionalMeasurement")
smm_DimensionalMeasurement = Class(name="smm::DimensionalMeasurement", is_abstract=True)
Measurement = Class(name="Measurement")
smm_GradeMeasurementRelationship = Class(name="smm::GradeMeasurementRelationship")
smm_RescaledMeasurementRelationship = Class(name="smm::RescaledMeasurementRelationship")
smm_RankingMeasurementRelationship = Class(name="smm::RankingMeasurementRelationship")
smm_DirectMeasure = Class(name="smm::DirectMeasure")
smm_CollectiveMeasurement = Class(name="smm::CollectiveMeasurement")
smm_DirectMeasurement = Class(name="smm::DirectMeasurement")
smm_EquivalentMeasureRelationship = Class(name="smm::EquivalentMeasureRelationship")
MeasureRelationship = Class(name="MeasureRelationship")
smm_EquivalentMeasurementRelationship = Class(name="smm::EquivalentMeasurementRelationship")
MeasurementRelationship = Class(name="MeasurementRelationship")
smm_GradeMeasurement = Class(name="smm::GradeMeasurement")
smm_DimensionalMeasure = Class(name="smm::DimensionalMeasure", is_abstract=True)
Measure = Class(name="Measure")
smm_Measure = Class(name="smm::Measure", is_abstract=True)
smm_RankingMeasureRelationship = Class(name="smm::RankingMeasureRelationship")
smm_RescaledMeasureRelationship = Class(name="smm::RescaledMeasureRelationship")
smm_GradeMeasureRelationship = Class(name="smm::GradeMeasureRelationship")
smm_UnitOfMeasure = Class(name="smm::UnitOfMeasure")
smm_RefinementMeasureRelationship = Class(name="smm::RefinementMeasureRelationship")
smm_MeasureRelationship = Class(name="smm::MeasureRelationship", is_abstract=True)
smm_MeasureCategory = Class(name="smm::MeasureCategory")
smm_Scope = Class(name="smm::Scope")
smm_MeasurementRelationship = Class(name="smm::MeasurementRelationship", is_abstract=True)
smm_MeasureLibrary = Class(name="smm::MeasureLibrary")
smm_Measurement = Class(name="smm::Measurement", is_abstract=True)
smm_Observation = Class(name="smm::Observation")
smm_RefinementMeasurementRelationship = Class(name="smm::RefinementMeasurementRelationship")
smm_ObservationScope = Class(name="smm::ObservationScope")
smm_EObject = Class(name="smm::EObject")
smm_NamedMeasure = Class(name="smm::NamedMeasure")
smm_NamedMeasurement = Class(name="smm::NamedMeasurement")
smm_OCLOperation = Class(name="smm::OCLOperation")
smm_GradeInterval = Class(name="smm::GradeInterval")
Interval = Class(name="Interval")
smm_GradeMeasure = Class(name="smm::GradeMeasure")
smm_RatioMeasure = Class(name="smm::RatioMeasure")
BinaryMeasure = Class(name="BinaryMeasure")
smm_RatioMeasurement = Class(name="smm::RatioMeasurement")
BinaryMeasurement = Class(name="BinaryMeasurement")
smm_RescaledMeasure = Class(name="smm::RescaledMeasure")
smm_ScaledBaseMeasureRelationship = Class(name="smm::ScaledBaseMeasureRelationship", is_abstract=True)
BaseMeasureRelationship = Class(name="BaseMeasureRelationship")
smm_RescaledMeasurement = Class(name="smm::RescaledMeasurement")
BaseMeasurementRelationship = Class(name="BaseMeasurementRelationship")
smm_SmmElement = Class(name="smm::SmmElement", is_abstract=True)
smm_SmmRelationship = Class(name="smm::SmmRelationship", is_abstract=True)
smm_SmmModel = Class(name="smm::SmmModel")
smm_RankingMeasurement = Class(name="smm::RankingMeasurement")
smm_RankingMeasure = Class(name="smm::RankingMeasure")
smm_RankingInterval = Class(name="smm::RankingInterval")
smm_Interval = Class(name="smm::Interval", is_abstract=True)
smm_ScaledBaseMeasurementRelationship = Class(name="smm::ScaledBaseMeasurementRelationship", is_abstract=True)
smm_CountingUnit = Class(name="smm::CountingUnit")
UnitOfMeasure = Class(name="UnitOfMeasure")
smm_BaseMeasureRelationship = Class(name="smm::BaseMeasureRelationship", is_abstract=True)
smm_BaseMeasurementRelationship = Class(name="smm::BaseMeasurementRelationship", is_abstract=True)

# smm_Annotation class attributes and methods
smm_Annotation_text: Property = Property(name="text", type=StringType)
smm_Annotation.attributes={smm_Annotation_text}

# smm_Argument class attributes and methods
smm_Argument_Type: Property = Property(name="Type", type=StringType)
smm_Argument_value: Property = Property(name="value", type=StringType)
smm_Argument.attributes={smm_Argument_Type, smm_Argument_value}

# smm_AbstractMeasureElement class attributes and methods

# SmmElement class attributes and methods

# smm_CategoryRelationship class attributes and methods

# SmmRelationship class attributes and methods

# smm_Characteristic class attributes and methods

# AbstractMeasureElement class attributes and methods

# smm_CollectiveMeasure class attributes and methods
smm_CollectiveMeasure_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasure.attributes={smm_CollectiveMeasure_accumulator}

# smm_ObservedMeasure class attributes and methods

# smm_Attribute class attributes and methods
smm_Attribute_tag: Property = Property(name="tag", type=StringType)
smm_Attribute_value: Property = Property(name="value", type=StringType)
smm_Attribute.attributes={smm_Attribute_tag, smm_Attribute_value}

# smm_Base1MeasureRelationship class attributes and methods

# ScaledBaseMeasureRelationship class attributes and methods

# smm_Base1MeasurementRelationship class attributes and methods

# ScaledBaseMeasurementRelationship class attributes and methods

# smm_Base2MeasureRelationship class attributes and methods

# smm_Base2MeasurementRelationship class attributes and methods

# smm_BaseNMeasureRelationship class attributes and methods

# smm_BaseNMeasurementRelationship class attributes and methods

# smm_BinaryMeasure class attributes and methods
smm_BinaryMeasure_functor: Property = Property(name="functor", type=StringType)
smm_BinaryMeasure.attributes={smm_BinaryMeasure_functor}

# DimensionalMeasure class attributes and methods

# smm_Operation class attributes and methods
smm_Operation_body: Property = Property(name="body", type=StringType)
smm_Operation_language: Property = Property(name="language", type=StringType)
smm_Operation_m_getParamStrings: Method = Method(name="getParamStrings", parameters={}, type=StringType)
smm_Operation.attributes={smm_Operation_language, smm_Operation_body}
smm_Operation.methods={smm_Operation_m_getParamStrings}

# smm_BinaryMeasurement class attributes and methods
smm_BinaryMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_BinaryMeasurement.attributes={smm_BinaryMeasurement_isBaseSupplied}

# DimensionalMeasurement class attributes and methods

# smm_DimensionalMeasurement class attributes and methods
smm_DimensionalMeasurement_value: Property = Property(name="value", type=FloatType)
smm_DimensionalMeasurement.attributes={smm_DimensionalMeasurement_value}

# Measurement class attributes and methods

# smm_GradeMeasurementRelationship class attributes and methods

# smm_RescaledMeasurementRelationship class attributes and methods

# smm_RankingMeasurementRelationship class attributes and methods

# smm_DirectMeasure class attributes and methods

# smm_CollectiveMeasurement class attributes and methods
smm_CollectiveMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_CollectiveMeasurement.attributes={smm_CollectiveMeasurement_isBaseSupplied}

# smm_DirectMeasurement class attributes and methods

# smm_EquivalentMeasureRelationship class attributes and methods

# MeasureRelationship class attributes and methods

# smm_EquivalentMeasurementRelationship class attributes and methods

# MeasurementRelationship class attributes and methods

# smm_GradeMeasurement class attributes and methods
smm_GradeMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_GradeMeasurement_value: Property = Property(name="value", type=StringType)
smm_GradeMeasurement.attributes={smm_GradeMeasurement_isBaseSupplied, smm_GradeMeasurement_value}

# smm_DimensionalMeasure class attributes and methods
smm_DimensionalMeasure_formula: Property = Property(name="formula", type=StringType)
smm_DimensionalMeasure.attributes={smm_DimensionalMeasure_formula}

# Measure class attributes and methods

# smm_Measure class attributes and methods
smm_Measure_source: Property = Property(name="source", type=StringType)
smm_Measure_measureLabelFormat: Property = Property(name="measureLabelFormat", type=StringType)
smm_Measure_measurementLabelFormat: Property = Property(name="measurementLabelFormat", type=StringType)
smm_Measure_scale: Property = Property(name="scale", type=StringType)
smm_Measure_customScale: Property = Property(name="customScale", type=StringType)
smm_Measure_visible: Property = Property(name="visible", type=StringType)
smm_Measure_m_getArguments: Method = Method(name="getArguments", parameters={}, type=StringType)
smm_Measure_m_getAllArguments: Method = Method(name="getAllArguments", parameters={}, type=StringType)
smm_Measure.attributes={smm_Measure_measureLabelFormat, smm_Measure_scale, smm_Measure_source, smm_Measure_customScale, smm_Measure_measurementLabelFormat, smm_Measure_visible}
smm_Measure.methods={smm_Measure_m_getAllArguments, smm_Measure_m_getArguments}

# smm_RankingMeasureRelationship class attributes and methods

# smm_RescaledMeasureRelationship class attributes and methods

# smm_GradeMeasureRelationship class attributes and methods

# smm_UnitOfMeasure class attributes and methods

# smm_RefinementMeasureRelationship class attributes and methods

# smm_MeasureRelationship class attributes and methods
smm_MeasureRelationship_influence: Property = Property(name="influence", type=StringType)
smm_MeasureRelationship.attributes={smm_MeasureRelationship_influence}

# smm_MeasureCategory class attributes and methods

# smm_Scope class attributes and methods

# smm_MeasurementRelationship class attributes and methods

# smm_MeasureLibrary class attributes and methods

# smm_Measurement class attributes and methods
smm_Measurement_breakValue: Property = Property(name="breakValue", type=StringType)
smm_Measurement_error: Property = Property(name="error", type=StringType)
smm_Measurement_m_getMeasurementLabel: Method = Method(name="getMeasurementLabel", parameters={}, type=StringType)
smm_Measurement_m_getMeasureLabel: Method = Method(name="getMeasureLabel", parameters={}, type=StringType)
smm_Measurement.attributes={smm_Measurement_breakValue, smm_Measurement_error}
smm_Measurement.methods={smm_Measurement_m_getMeasureLabel, smm_Measurement_m_getMeasurementLabel}

# smm_Observation class attributes and methods
smm_Observation_observer: Property = Property(name="observer", type=StringType)
smm_Observation_tool: Property = Property(name="tool", type=StringType)
smm_Observation_whenObserved: Property = Property(name="whenObserved", type=StringType)
smm_Observation.attributes={smm_Observation_whenObserved, smm_Observation_tool, smm_Observation_observer}

# smm_RefinementMeasurementRelationship class attributes and methods

# smm_ObservationScope class attributes and methods
smm_ObservationScope_scopeUri: Property = Property(name="scopeUri", type=StringType)
smm_ObservationScope.attributes={smm_ObservationScope_scopeUri}

# smm_EObject class attributes and methods

# smm_NamedMeasure class attributes and methods

# smm_NamedMeasurement class attributes and methods

# smm_OCLOperation class attributes and methods
smm_OCLOperation_body: Property = Property(name="body", type=StringType)
smm_OCLOperation_context: Property = Property(name="context", type=StringType)
smm_OCLOperation.attributes={smm_OCLOperation_body, smm_OCLOperation_context}

# smm_GradeInterval class attributes and methods
smm_GradeInterval_symbol: Property = Property(name="symbol", type=StringType)
smm_GradeInterval.attributes={smm_GradeInterval_symbol}

# Interval class attributes and methods

# smm_GradeMeasure class attributes and methods

# smm_RatioMeasure class attributes and methods

# BinaryMeasure class attributes and methods

# smm_RatioMeasurement class attributes and methods

# BinaryMeasurement class attributes and methods

# smm_RescaledMeasure class attributes and methods
smm_RescaledMeasure_offset: Property = Property(name="offset", type=FloatType)
smm_RescaledMeasure_multiplier: Property = Property(name="multiplier", type=FloatType)
smm_RescaledMeasure_operationFirst: Property = Property(name="operationFirst", type=StringType)
smm_RescaledMeasure.attributes={smm_RescaledMeasure_multiplier, smm_RescaledMeasure_operationFirst, smm_RescaledMeasure_offset}

# smm_ScaledBaseMeasureRelationship class attributes and methods

# BaseMeasureRelationship class attributes and methods

# smm_RescaledMeasurement class attributes and methods
smm_RescaledMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_RescaledMeasurement.attributes={smm_RescaledMeasurement_isBaseSupplied}

# BaseMeasurementRelationship class attributes and methods

# smm_SmmElement class attributes and methods
smm_SmmElement_name: Property = Property(name="name", type=StringType)
smm_SmmElement_shortDescription: Property = Property(name="shortDescription", type=StringType)
smm_SmmElement_description: Property = Property(name="description", type=StringType)
smm_SmmElement.attributes={smm_SmmElement_name, smm_SmmElement_shortDescription, smm_SmmElement_description}

# smm_SmmRelationship class attributes and methods

# smm_SmmModel class attributes and methods

# smm_RankingMeasurement class attributes and methods
smm_RankingMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_RankingMeasurement.attributes={smm_RankingMeasurement_isBaseSupplied}

# smm_RankingMeasure class attributes and methods

# smm_RankingInterval class attributes and methods
smm_RankingInterval_value: Property = Property(name="value", type=FloatType)
smm_RankingInterval.attributes={smm_RankingInterval_value}

# smm_Interval class attributes and methods
smm_Interval_maximumOpen: Property = Property(name="maximumOpen", type=StringType)
smm_Interval_minimum: Property = Property(name="minimum", type=FloatType)
smm_Interval_minimumOpen: Property = Property(name="minimumOpen", type=StringType)
smm_Interval_maximum: Property = Property(name="maximum", type=FloatType)
smm_Interval.attributes={smm_Interval_maximum, smm_Interval_minimumOpen, smm_Interval_maximumOpen, smm_Interval_minimum}

# smm_ScaledBaseMeasurementRelationship class attributes and methods

# smm_CountingUnit class attributes and methods

# UnitOfMeasure class attributes and methods

# smm_BaseMeasureRelationship class attributes and methods

# smm_BaseMeasurementRelationship class attributes and methods

# Relationships
baseMeasurement2To8: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement2To8",
    ends={
        Property(name="smm_Base2MeasurementRelationship", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasurement", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasurement1To9: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1To9",
    ends={
        Property(name="smm_Base1MeasurementRelationship", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasurement10", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
baseQuery11: BinaryAssociation = BinaryAssociation(
    name="baseQuery11",
    ends={
        Property(name="smm_Operation13", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasurement12", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
parent15: BinaryAssociation = BinaryAssociation(
    name="parent15",
    ends={
        Property(name="smm_Characteristic", type=smm_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Characteristic14", type=smm_Characteristic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observedMeasure0: BinaryAssociation = BinaryAssociation(
    name="observedMeasure0",
    ends={
        Property(name="ObservedMeasure", type=smm_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=smm_ObservedMeasure, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasureTo16: BinaryAssociation = BinaryAssociation(
    name="baseMeasureTo16",
    ends={
        Property(name="smm_BaseNMeasureRelationship", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CollectiveMeasure", type=smm_BaseNMeasureRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
customAccumulator17: BinaryAssociation = BinaryAssociation(
    name="customAccumulator17",
    ends={
        Property(name="smm_Operation19", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CollectiveMeasure18", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
mappedFrom1: BinaryAssociation = BinaryAssociation(
    name="mappedFrom1",
    ends={
        Property(name="BaseNMeasurementRelationship", type=smm_BaseNMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=smm_BaseNMeasurementRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
mapsTo2: BinaryAssociation = BinaryAssociation(
    name="mapsTo2",
    ends={
        Property(name="BaseNMeasureRelationship", type=smm_BaseNMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="mappedFrom", type=smm_BaseNMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasure1To3: BinaryAssociation = BinaryAssociation(
    name="baseMeasure1To3",
    ends={
        Property(name="smm_Base1MeasureRelationship", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasure", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure2To4: BinaryAssociation = BinaryAssociation(
    name="baseMeasure2To4",
    ends={
        Property(name="smm_Base2MeasureRelationship", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasure5", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
customFunctor6: BinaryAssociation = BinaryAssociation(
    name="customFunctor6",
    ends={
        Property(name="smm_Operation", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasure7", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasurement1From40: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1From40",
    ends={
        Property(name="smm_Base1MeasurementRelationship41", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasurement", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurementFrom42: BinaryAssociation = BinaryAssociation(
    name="baseMeasurementFrom42",
    ends={
        Property(name="smm_BaseNMeasurementRelationship44", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasurement43", type=smm_BaseNMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement2From45: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement2From45",
    ends={
        Property(name="smm_Base2MeasurementRelationship47", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasurement46", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
gradeFrom48: BinaryAssociation = BinaryAssociation(
    name="gradeFrom48",
    ends={
        Property(name="smm_GradeMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasurement49", type=smm_GradeMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rescaleTo50: BinaryAssociation = BinaryAssociation(
    name="rescaleTo50",
    ends={
        Property(name="smm_RescaledMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasurement51", type=smm_RescaledMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rankingFrom52: BinaryAssociation = BinaryAssociation(
    name="rankingFrom52",
    ends={
        Property(name="smm_RankingMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasurement53", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
operation54: BinaryAssociation = BinaryAssociation(
    name="operation54",
    ends={
        Property(name="smm_Operation55", type=smm_DirectMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DirectMeasure", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasurementTo20: BinaryAssociation = BinaryAssociation(
    name="baseMeasurementTo20",
    ends={
        Property(name="smm_BaseNMeasurementRelationship", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CollectiveMeasurement", type=smm_BaseNMeasurementRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
mapping56: BinaryAssociation = BinaryAssociation(
    name="mapping56",
    ends={
        Property(name="smm_Operation57", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_EquivalentMeasureRelationship", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseQuery21: BinaryAssociation = BinaryAssociation(
    name="baseQuery21",
    ends={
        Property(name="smm_Operation23", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CollectiveMeasurement22", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasure1From24: BinaryAssociation = BinaryAssociation(
    name="baseMeasure1From24",
    ends={
        Property(name="smm_Base1MeasureRelationship25", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
gradeTo58: BinaryAssociation = BinaryAssociation(
    name="gradeTo58",
    ends={
        Property(name="smm_GradeMeasurementRelationship59", type=smm_GradeMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_GradeMeasurement", type=smm_GradeMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasureFrom26: BinaryAssociation = BinaryAssociation(
    name="baseMeasureFrom26",
    ends={
        Property(name="smm_BaseNMeasureRelationship28", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure27", type=smm_BaseNMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseQuery60: BinaryAssociation = BinaryAssociation(
    name="baseQuery60",
    ends={
        Property(name="smm_Operation62", type=smm_GradeMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_GradeMeasurement61", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasure2From29: BinaryAssociation = BinaryAssociation(
    name="baseMeasure2From29",
    ends={
        Property(name="smm_Base2MeasureRelationship31", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure30", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rankingFrom32: BinaryAssociation = BinaryAssociation(
    name="rankingFrom32",
    ends={
        Property(name="smm_RankingMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure33", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rescaleTo34: BinaryAssociation = BinaryAssociation(
    name="rescaleTo34",
    ends={
        Property(name="smm_RescaledMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure35", type=smm_RescaledMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
gradeFrom36: BinaryAssociation = BinaryAssociation(
    name="gradeFrom36",
    ends={
        Property(name="smm_GradeMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure37", type=smm_GradeMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
unit38: BinaryAssociation = BinaryAssociation(
    name="unit38",
    ends={
        Property(name="smm_UnitOfMeasure", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DimensionalMeasure39", type=smm_UnitOfMeasure, multiplicity=Multiplicity(1, 1))
    }
)
refinementFrom63: BinaryAssociation = BinaryAssociation(
    name="refinementFrom63",
    ends={
        Property(name="smm_RefinementMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementTo64: BinaryAssociation = BinaryAssociation(
    name="refinementTo64",
    ends={
        Property(name="smm_RefinementMeasureRelationship66", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure65", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
inbound67: BinaryAssociation = BinaryAssociation(
    name="inbound67",
    ends={
        Property(name="smm_MeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure68", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
outbound69: BinaryAssociation = BinaryAssociation(
    name="outbound69",
    ends={
        Property(name="smm_MeasureRelationship71", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure70", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentTo72: BinaryAssociation = BinaryAssociation(
    name="equivalentTo72",
    ends={
        Property(name="smm_EquivalentMeasureRelationship74", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure73", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentFrom75: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom75",
    ends={
        Property(name="smm_EquivalentMeasureRelationship77", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure76", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
defaultQuery78: BinaryAssociation = BinaryAssociation(
    name="defaultQuery78",
    ends={
        Property(name="smm_Operation80", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure79", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
category81: BinaryAssociation = BinaryAssociation(
    name="category81",
    ends={
        Property(name="MeasureCategory", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryMeasure", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
scope82: BinaryAssociation = BinaryAssociation(
    name="scope82",
    ends={
        Property(name="smm_Scope", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure83", type=smm_Scope, multiplicity=Multiplicity(1, 1))
    }
)
trait84: BinaryAssociation = BinaryAssociation(
    name="trait84",
    ends={
        Property(name="smm_Characteristic86", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure85", type=smm_Characteristic, multiplicity=Multiplicity(1, 1))
    }
)
measureRelationships87: BinaryAssociation = BinaryAssociation(
    name="measureRelationships87",
    ends={
        Property(name="smm_MeasureRelationship89", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure88", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryMeasure90: BinaryAssociation = BinaryAssociation(
    name="categoryMeasure90",
    ends={
        Property(name="Measure", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
measurementRelationships104: BinaryAssociation = BinaryAssociation(
    name="measurementRelationships104",
    ends={
        Property(name="smm_MeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equivalentFrom105: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom105",
    ends={
        Property(name="smm_EquivalentMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement106", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
category92: BinaryAssociation = BinaryAssociation(
    name="category92",
    ends={
        Property(name="MeasureCategory93", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryElement", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
categoryElement95: BinaryAssociation = BinaryAssociation(
    name="categoryElement95",
    ends={
        Property(name="MeasureCategory97", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="category96", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
measureElements98: BinaryAssociation = BinaryAssociation(
    name="measureElements98",
    ends={
        Property(name="smm_AbstractMeasureElement", type=smm_MeasureLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_MeasureLibrary", type=smm_AbstractMeasureElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryRelationships99: BinaryAssociation = BinaryAssociation(
    name="categoryRelationships99",
    ends={
        Property(name="smm_CategoryRelationship", type=smm_MeasureLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_MeasureLibrary100", type=smm_CategoryRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurandQuery101: BinaryAssociation = BinaryAssociation(
    name="measurandQuery101",
    ends={
        Property(name="smm_Operation103", type=smm_MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_MeasureRelationship102", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
equivalentTo107: BinaryAssociation = BinaryAssociation(
    name="equivalentTo107",
    ends={
        Property(name="smm_EquivalentMeasurementRelationship109", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement108", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
outbound110: BinaryAssociation = BinaryAssociation(
    name="outbound110",
    ends={
        Property(name="smm_MeasurementRelationship112", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement111", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
inbound113: BinaryAssociation = BinaryAssociation(
    name="inbound113",
    ends={
        Property(name="smm_MeasurementRelationship115", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement114", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementTo116: BinaryAssociation = BinaryAssociation(
    name="refinementTo116",
    ends={
        Property(name="smm_RefinementMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement117", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementFrom118: BinaryAssociation = BinaryAssociation(
    name="refinementFrom118",
    ends={
        Property(name="smm_RefinementMeasurementRelationship120", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement119", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
scopes125: BinaryAssociation = BinaryAssociation(
    name="scopes125",
    ends={
        Property(name="smm_ObservationScope", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation", type=smm_ObservationScope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observedMeasure121: BinaryAssociation = BinaryAssociation(
    name="observedMeasure121",
    ends={
        Property(name="ObservedMeasure122", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="measurements", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1))
    }
)
measurand123: BinaryAssociation = BinaryAssociation(
    name="measurand123",
    ends={
        Property(name="smm_EObject", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement124", type=smm_EObject, multiplicity=Multiplicity(0, 1))
    }
)
observedMeasures126: BinaryAssociation = BinaryAssociation(
    name="observedMeasures126",
    ends={
        Property(name="smm_ObservedMeasure", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation127", type=smm_ObservedMeasure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gradeTo139: BinaryAssociation = BinaryAssociation(
    name="gradeTo139",
    ends={
        Property(name="smm_GradeMeasureRelationship140", type=smm_GradeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_GradeMeasure", type=smm_GradeMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
interval141: BinaryAssociation = BinaryAssociation(
    name="interval141",
    ends={
        Property(name="smm_GradeInterval", type=smm_GradeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_GradeMeasure142", type=smm_GradeInterval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arguments133: BinaryAssociation = BinaryAssociation(
    name="arguments133",
    ends={
        Property(name="Argument", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="observedMeasure", type=smm_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurements134: BinaryAssociation = BinaryAssociation(
    name="measurements134",
    ends={
        Property(name="Measurement", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="observedMeasure135", type=smm_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measure136: BinaryAssociation = BinaryAssociation(
    name="measure136",
    ends={
        Property(name="smm_Measure138", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_ObservedMeasure137", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
arguments128: BinaryAssociation = BinaryAssociation(
    name="arguments128",
    ends={
        Property(name="smm_Argument", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation129", type=smm_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requestedMeasures130: BinaryAssociation = BinaryAssociation(
    name="requestedMeasures130",
    ends={
        Property(name="smm_AbstractMeasureElement132", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation131", type=smm_AbstractMeasureElement, multiplicity=Multiplicity(0, 9999))
    }
)
breakCondition154: BinaryAssociation = BinaryAssociation(
    name="breakCondition154",
    ends={
        Property(name="smm_Operation156", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope155", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
recognizer157: BinaryAssociation = BinaryAssociation(
    name="recognizer157",
    ends={
        Property(name="smm_Operation159", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope158", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
rescaleFrom143: BinaryAssociation = BinaryAssociation(
    name="rescaleFrom143",
    ends={
        Property(name="smm_RescaledMeasureRelationship144", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RescaledMeasure", type=smm_RescaledMeasureRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
rescales145: BinaryAssociation = BinaryAssociation(
    name="rescales145",
    ends={
        Property(name="ScaledBaseMeasureRelationship", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaledMeasure", type=smm_ScaledBaseMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
operation146: BinaryAssociation = BinaryAssociation(
    name="operation146",
    ends={
        Property(name="smm_Operation148", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RescaledMeasure147", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
rescaleFrom149: BinaryAssociation = BinaryAssociation(
    name="rescaleFrom149",
    ends={
        Property(name="smm_RescaledMeasurementRelationship150", type=smm_RescaledMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RescaledMeasurement", type=smm_RescaledMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
baseQuery151: BinaryAssociation = BinaryAssociation(
    name="baseQuery151",
    ends={
        Property(name="smm_Operation153", type=smm_RescaledMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RescaledMeasurement152", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
from178: BinaryAssociation = BinaryAssociation(
    name="from178",
    ends={
        Property(name="SmmElement179", type=smm_SmmRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="outRelationships", type=smm_SmmElement, multiplicity=Multiplicity(1, 1))
    }
)
Class160: BinaryAssociation = BinaryAssociation(
    name="Class160",
    ends={
        Property(name="smm_EObject162", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope161", type=smm_EObject, multiplicity=Multiplicity(0, 1))
    }
)
stereotype163: BinaryAssociation = BinaryAssociation(
    name="stereotype163",
    ends={
        Property(name="smm_EObject165", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope164", type=smm_EObject, multiplicity=Multiplicity(0, 1))
    }
)
attributes166: BinaryAssociation = BinaryAssociation(
    name="attributes166",
    ends={
        Property(name="smm_Attribute", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmElement", type=smm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations167: BinaryAssociation = BinaryAssociation(
    name="annotations167",
    ends={
        Property(name="smm_Annotation", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmElement168", type=smm_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inRelationships169: BinaryAssociation = BinaryAssociation(
    name="inRelationships169",
    ends={
        Property(name="SmmRelationship", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=smm_SmmRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
outRelationships170: BinaryAssociation = BinaryAssociation(
    name="outRelationships170",
    ends={
        Property(name="SmmRelationship171", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=smm_SmmRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
libraries172: BinaryAssociation = BinaryAssociation(
    name="libraries172",
    ends={
        Property(name="smm_MeasureLibrary173", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmModel", type=smm_MeasureLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observations174: BinaryAssociation = BinaryAssociation(
    name="observations174",
    ends={
        Property(name="smm_Observation176", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmModel175", type=smm_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to177: BinaryAssociation = BinaryAssociation(
    name="to177",
    ends={
        Property(name="SmmElement", type=smm_SmmRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="inRelationships", type=smm_SmmElement, multiplicity=Multiplicity(1, 1))
    }
)
baseQuery185: BinaryAssociation = BinaryAssociation(
    name="baseQuery185",
    ends={
        Property(name="smm_Operation186", type=smm_RankingMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RankingMeasurement", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
rankingTo187: BinaryAssociation = BinaryAssociation(
    name="rankingTo187",
    ends={
        Property(name="smm_RankingMeasurementRelationship189", type=smm_RankingMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RankingMeasurement188", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
interval180: BinaryAssociation = BinaryAssociation(
    name="interval180",
    ends={
        Property(name="RankingInterval", type=smm_RankingMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="ranking", type=smm_RankingInterval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rankingTo181: BinaryAssociation = BinaryAssociation(
    name="rankingTo181",
    ends={
        Property(name="smm_RankingMeasureRelationship182", type=smm_RankingMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_RankingMeasure", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
ranking183: BinaryAssociation = BinaryAssociation(
    name="ranking183",
    ends={
        Property(name="RankingMeasure", type=smm_RankingInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="interval", type=smm_RankingMeasure, multiplicity=Multiplicity(1, 1))
    }
)
rescaledMeasure184: BinaryAssociation = BinaryAssociation(
    name="rescaledMeasure184",
    ends={
        Property(name="RescaledMeasure", type=smm_ScaledBaseMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescales", type=smm_RescaledMeasure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope190: BinaryAssociation = BinaryAssociation(
    name="scope190",
    ends={
        Property(name="smm_Scope191", type=smm_CountingUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CountingUnit", type=smm_Scope, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_smm_Annotation_SmmElement = Generalization(general=SmmElement, specific=smm_Annotation)
gen_smm_Argument_SmmElement = Generalization(general=SmmElement, specific=smm_Argument)
gen_smm_AbstractMeasureElement_SmmElement = Generalization(general=SmmElement, specific=smm_AbstractMeasureElement)
gen_smm_CategoryRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_CategoryRelationship)
gen_smm_Characteristic_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Characteristic)
gen_smm_CollectiveMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_CollectiveMeasure)
gen_smm_Attribute_SmmElement = Generalization(general=SmmElement, specific=smm_Attribute)
gen_smm_Base1MeasureRelationship_ScaledBaseMeasureRelationship = Generalization(general=ScaledBaseMeasureRelationship, specific=smm_Base1MeasureRelationship)
gen_smm_Base1MeasurementRelationship_ScaledBaseMeasurementRelationship = Generalization(general=ScaledBaseMeasurementRelationship, specific=smm_Base1MeasurementRelationship)
gen_smm_Base2MeasureRelationship_ScaledBaseMeasureRelationship = Generalization(general=ScaledBaseMeasureRelationship, specific=smm_Base2MeasureRelationship)
gen_smm_Base2MeasurementRelationship_ScaledBaseMeasurementRelationship = Generalization(general=ScaledBaseMeasurementRelationship, specific=smm_Base2MeasurementRelationship)
gen_smm_BaseNMeasureRelationship_ScaledBaseMeasureRelationship = Generalization(general=ScaledBaseMeasureRelationship, specific=smm_BaseNMeasureRelationship)
gen_smm_BaseNMeasurementRelationship_ScaledBaseMeasurementRelationship = Generalization(general=ScaledBaseMeasurementRelationship, specific=smm_BaseNMeasurementRelationship)
gen_smm_BinaryMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_BinaryMeasure)
gen_smm_BinaryMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_BinaryMeasurement)
gen_smm_DimensionalMeasurement_Measurement = Generalization(general=Measurement, specific=smm_DimensionalMeasurement)
gen_smm_DirectMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_DirectMeasure)
gen_smm_CollectiveMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_CollectiveMeasurement)
gen_smm_DirectMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_DirectMeasurement)
gen_smm_EquivalentMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_EquivalentMeasureRelationship)
gen_smm_EquivalentMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_EquivalentMeasurementRelationship)
gen_smm_GradeMeasurement_Measurement = Generalization(general=Measurement, specific=smm_GradeMeasurement)
gen_smm_DimensionalMeasure_Measure = Generalization(general=Measure, specific=smm_DimensionalMeasure)
gen_smm_Measure_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Measure)
gen_smm_MeasureCategory_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_MeasureCategory)
gen_smm_MeasureLibrary_SmmElement = Generalization(general=SmmElement, specific=smm_MeasureLibrary)
gen_smm_MeasureRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasureRelationship)
gen_smm_Measurement_SmmElement = Generalization(general=SmmElement, specific=smm_Measurement)
gen_smm_Observation_SmmElement = Generalization(general=SmmElement, specific=smm_Observation)
gen_smm_MeasurementRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasurementRelationship)
gen_smm_NamedMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_NamedMeasure)
gen_smm_NamedMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_NamedMeasurement)
gen_smm_OCLOperation_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_OCLOperation)
gen_smm_GradeInterval_Interval = Generalization(general=Interval, specific=smm_GradeInterval)
gen_smm_Operation_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Operation)
gen_smm_ObservationScope_SmmElement = Generalization(general=SmmElement, specific=smm_ObservationScope)
gen_smm_GradeMeasure_Measure = Generalization(general=Measure, specific=smm_GradeMeasure)
gen_smm_ObservedMeasure_SmmElement = Generalization(general=SmmElement, specific=smm_ObservedMeasure)
gen_smm_Scope_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Scope)
gen_smm_RankingMeasureRelationship_ScaledBaseMeasureRelationship = Generalization(general=ScaledBaseMeasureRelationship, specific=smm_RankingMeasureRelationship)
gen_smm_GradeMeasurementRelationship_ScaledBaseMeasurementRelationship = Generalization(general=ScaledBaseMeasurementRelationship, specific=smm_GradeMeasurementRelationship)
gen_smm_RatioMeasure_BinaryMeasure = Generalization(general=BinaryMeasure, specific=smm_RatioMeasure)
gen_smm_RatioMeasurement_BinaryMeasurement = Generalization(general=BinaryMeasurement, specific=smm_RatioMeasurement)
gen_smm_RefinementMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RefinementMeasureRelationship)
gen_smm_RefinementMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RefinementMeasurementRelationship)
gen_smm_RescaledMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_RescaledMeasure)
gen_smm_RescaledMeasureRelationship_BaseMeasureRelationship = Generalization(general=BaseMeasureRelationship, specific=smm_RescaledMeasureRelationship)
gen_smm_RescaledMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_RescaledMeasurement)
gen_smm_RescaledMeasurementRelationship_BaseMeasurementRelationship = Generalization(general=BaseMeasurementRelationship, specific=smm_RescaledMeasurementRelationship)
gen_smm_SmmModel_SmmElement = Generalization(general=SmmElement, specific=smm_SmmModel)
gen_smm_SmmRelationship_SmmElement = Generalization(general=SmmElement, specific=smm_SmmRelationship)
gen_smm_RankingMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_RankingMeasurement)
gen_smm_RankingMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_RankingMeasure)
gen_smm_RankingInterval_Interval = Generalization(general=Interval, specific=smm_RankingInterval)
gen_smm_GradeMeasureRelationship_ScaledBaseMeasureRelationship = Generalization(general=ScaledBaseMeasureRelationship, specific=smm_GradeMeasureRelationship)
gen_smm_ScaledBaseMeasureRelationship_BaseMeasureRelationship = Generalization(general=BaseMeasureRelationship, specific=smm_ScaledBaseMeasureRelationship)
gen_smm_Interval_SmmElement = Generalization(general=SmmElement, specific=smm_Interval)
gen_smm_RankingMeasurementRelationship_ScaledBaseMeasurementRelationship = Generalization(general=ScaledBaseMeasurementRelationship, specific=smm_RankingMeasurementRelationship)
gen_smm_UnitOfMeasure_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_UnitOfMeasure)
gen_smm_ScaledBaseMeasurementRelationship_BaseMeasurementRelationship = Generalization(general=BaseMeasurementRelationship, specific=smm_ScaledBaseMeasurementRelationship)
gen_smm_CountingUnit_UnitOfMeasure = Generalization(general=UnitOfMeasure, specific=smm_CountingUnit)
gen_smm_BaseMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_BaseMeasureRelationship)
gen_smm_BaseMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_BaseMeasurementRelationship)

# Domain Model
domain_model = DomainModel(
    name="smm",
    types={smm_Annotation, smm_Argument, smm_AbstractMeasureElement, SmmElement, smm_CategoryRelationship, SmmRelationship, smm_Characteristic, AbstractMeasureElement, smm_CollectiveMeasure, smm_ObservedMeasure, smm_Attribute, smm_Base1MeasureRelationship, ScaledBaseMeasureRelationship, smm_Base1MeasurementRelationship, ScaledBaseMeasurementRelationship, smm_Base2MeasureRelationship, smm_Base2MeasurementRelationship, smm_BaseNMeasureRelationship, smm_BaseNMeasurementRelationship, smm_BinaryMeasure, DimensionalMeasure, smm_Operation, smm_BinaryMeasurement, DimensionalMeasurement, smm_DimensionalMeasurement, Measurement, smm_GradeMeasurementRelationship, smm_RescaledMeasurementRelationship, smm_RankingMeasurementRelationship, smm_DirectMeasure, smm_CollectiveMeasurement, smm_DirectMeasurement, smm_EquivalentMeasureRelationship, MeasureRelationship, smm_EquivalentMeasurementRelationship, MeasurementRelationship, smm_GradeMeasurement, smm_DimensionalMeasure, Measure, smm_Measure, smm_RankingMeasureRelationship, smm_RescaledMeasureRelationship, smm_GradeMeasureRelationship, smm_UnitOfMeasure, smm_RefinementMeasureRelationship, smm_MeasureRelationship, smm_MeasureCategory, smm_Scope, smm_MeasurementRelationship, smm_MeasureLibrary, smm_Measurement, smm_Observation, smm_RefinementMeasurementRelationship, smm_ObservationScope, smm_EObject, smm_NamedMeasure, smm_NamedMeasurement, smm_OCLOperation, smm_GradeInterval, Interval, smm_GradeMeasure, smm_RatioMeasure, BinaryMeasure, smm_RatioMeasurement, BinaryMeasurement, smm_RescaledMeasure, smm_ScaledBaseMeasureRelationship, BaseMeasureRelationship, smm_RescaledMeasurement, BaseMeasurementRelationship, smm_SmmElement, smm_SmmRelationship, smm_SmmModel, smm_RankingMeasurement, smm_RankingMeasure, smm_RankingInterval, smm_Interval, smm_ScaledBaseMeasurementRelationship, smm_CountingUnit, UnitOfMeasure, smm_BaseMeasureRelationship, smm_BaseMeasurementRelationship, Accumulator, MeasurementScale, Influence, BinaryFunctor, ScaleOfMeasurement},
    associations={baseMeasurement2To8, baseMeasurement1To9, baseQuery11, parent15, observedMeasure0, baseMeasureTo16, customAccumulator17, mappedFrom1, mapsTo2, baseMeasure1To3, baseMeasure2To4, customFunctor6, baseMeasurement1From40, baseMeasurementFrom42, baseMeasurement2From45, gradeFrom48, rescaleTo50, rankingFrom52, operation54, baseMeasurementTo20, mapping56, baseQuery21, baseMeasure1From24, gradeTo58, baseMeasureFrom26, baseQuery60, baseMeasure2From29, rankingFrom32, rescaleTo34, gradeFrom36, unit38, refinementFrom63, refinementTo64, inbound67, outbound69, equivalentTo72, equivalentFrom75, defaultQuery78, category81, scope82, trait84, measureRelationships87, categoryMeasure90, measurementRelationships104, equivalentFrom105, category92, categoryElement95, measureElements98, categoryRelationships99, measurandQuery101, equivalentTo107, outbound110, inbound113, refinementTo116, refinementFrom118, scopes125, observedMeasure121, measurand123, observedMeasures126, gradeTo139, interval141, arguments133, measurements134, measure136, arguments128, requestedMeasures130, breakCondition154, recognizer157, rescaleFrom143, rescales145, operation146, rescaleFrom149, baseQuery151, from178, Class160, stereotype163, attributes166, annotations167, inRelationships169, outRelationships170, libraries172, observations174, to177, baseQuery185, rankingTo187, interval180, rankingTo181, ranking183, rescaledMeasure184, scope190},
    generalizations={gen_smm_Annotation_SmmElement, gen_smm_Argument_SmmElement, gen_smm_AbstractMeasureElement_SmmElement, gen_smm_CategoryRelationship_SmmRelationship, gen_smm_Characteristic_AbstractMeasureElement, gen_smm_CollectiveMeasure_DimensionalMeasure, gen_smm_Attribute_SmmElement, gen_smm_Base1MeasureRelationship_ScaledBaseMeasureRelationship, gen_smm_Base1MeasurementRelationship_ScaledBaseMeasurementRelationship, gen_smm_Base2MeasureRelationship_ScaledBaseMeasureRelationship, gen_smm_Base2MeasurementRelationship_ScaledBaseMeasurementRelationship, gen_smm_BaseNMeasureRelationship_ScaledBaseMeasureRelationship, gen_smm_BaseNMeasurementRelationship_ScaledBaseMeasurementRelationship, gen_smm_BinaryMeasure_DimensionalMeasure, gen_smm_BinaryMeasurement_DimensionalMeasurement, gen_smm_DimensionalMeasurement_Measurement, gen_smm_DirectMeasure_DimensionalMeasure, gen_smm_CollectiveMeasurement_DimensionalMeasurement, gen_smm_DirectMeasurement_DimensionalMeasurement, gen_smm_EquivalentMeasureRelationship_MeasureRelationship, gen_smm_EquivalentMeasurementRelationship_MeasurementRelationship, gen_smm_GradeMeasurement_Measurement, gen_smm_DimensionalMeasure_Measure, gen_smm_Measure_AbstractMeasureElement, gen_smm_MeasureCategory_AbstractMeasureElement, gen_smm_MeasureLibrary_SmmElement, gen_smm_MeasureRelationship_SmmRelationship, gen_smm_Measurement_SmmElement, gen_smm_Observation_SmmElement, gen_smm_MeasurementRelationship_SmmRelationship, gen_smm_NamedMeasure_DimensionalMeasure, gen_smm_NamedMeasurement_DimensionalMeasurement, gen_smm_OCLOperation_AbstractMeasureElement, gen_smm_GradeInterval_Interval, gen_smm_Operation_AbstractMeasureElement, gen_smm_ObservationScope_SmmElement, gen_smm_GradeMeasure_Measure, gen_smm_ObservedMeasure_SmmElement, gen_smm_Scope_AbstractMeasureElement, gen_smm_RankingMeasureRelationship_ScaledBaseMeasureRelationship, gen_smm_GradeMeasurementRelationship_ScaledBaseMeasurementRelationship, gen_smm_RatioMeasure_BinaryMeasure, gen_smm_RatioMeasurement_BinaryMeasurement, gen_smm_RefinementMeasureRelationship_MeasureRelationship, gen_smm_RefinementMeasurementRelationship_MeasurementRelationship, gen_smm_RescaledMeasure_DimensionalMeasure, gen_smm_RescaledMeasureRelationship_BaseMeasureRelationship, gen_smm_RescaledMeasurement_DimensionalMeasurement, gen_smm_RescaledMeasurementRelationship_BaseMeasurementRelationship, gen_smm_SmmModel_SmmElement, gen_smm_SmmRelationship_SmmElement, gen_smm_RankingMeasurement_DimensionalMeasurement, gen_smm_RankingMeasure_DimensionalMeasure, gen_smm_RankingInterval_Interval, gen_smm_GradeMeasureRelationship_ScaledBaseMeasureRelationship, gen_smm_ScaledBaseMeasureRelationship_BaseMeasureRelationship, gen_smm_Interval_SmmElement, gen_smm_RankingMeasurementRelationship_ScaledBaseMeasurementRelationship, gen_smm_UnitOfMeasure_AbstractMeasureElement, gen_smm_ScaledBaseMeasurementRelationship_BaseMeasurementRelationship, gen_smm_CountingUnit_UnitOfMeasure, gen_smm_BaseMeasureRelationship_MeasureRelationship, gen_smm_BaseMeasurementRelationship_MeasurementRelationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)