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
			EnumerationLiteral(name="sum")
    }
)

# Classes
smm_Annotation = Class(name="smm::Annotation")
smm_Argument = Class(name="smm::Argument")
smm_Attribute = Class(name="smm::Attribute")
smm_Base1MeasureRelationship = Class(name="smm::Base1MeasureRelationship")
MeasureRelationship = Class(name="MeasureRelationship")
smm_BinaryMeasure = Class(name="smm::BinaryMeasure")
smm_DimensionalMeasure = Class(name="smm::DimensionalMeasure")
smm_Base1MeasurementRelationship = Class(name="smm::Base1MeasurementRelationship")
MeasurementRelationship = Class(name="MeasurementRelationship")
smm_BinaryMeasurement = Class(name="smm::BinaryMeasurement")
smm_DimensionalMeasurement = Class(name="smm::DimensionalMeasurement", is_abstract=True)
smm_Base2MeasureRelationship = Class(name="smm::Base2MeasureRelationship")
smm_Base2MeasurementRelationship = Class(name="smm::Base2MeasurementRelationship")
smm_AbstractMeasureElement = Class(name="smm::AbstractMeasureElement", is_abstract=True)
SmmElement = Class(name="SmmElement")
smm_BaseMeasurementRelationship = Class(name="smm::BaseMeasurementRelationship")
smm_CollectiveMeasurement = Class(name="smm::CollectiveMeasurement")
DimensionalMeasure = Class(name="DimensionalMeasure")
DimensionalMeasurement = Class(name="DimensionalMeasurement")
smm_CategoryRelationship = Class(name="smm::CategoryRelationship")
SmmRelationship = Class(name="SmmRelationship")
smm_MeasureCategory = Class(name="smm::MeasureCategory")
smm_Characteristic = Class(name="smm::Characteristic")
AbstractMeasureElement = Class(name="AbstractMeasureElement")
smm_BaseMeasureRelationship = Class(name="smm::BaseMeasureRelationship")
smm_CollectiveMeasure = Class(name="smm::CollectiveMeasure")
Measure = Class(name="Measure")
smm_RescaleMeasureRelationship = Class(name="smm::RescaleMeasureRelationship")
smm_RankingMeasureRelationship = Class(name="smm::RankingMeasureRelationship")
Measurement = Class(name="Measurement")
smm_RescaleMeasurementRelationship = Class(name="smm::RescaleMeasurementRelationship")
smm_RankingMeasurementRelationship = Class(name="smm::RankingMeasurementRelationship")
smm_DirectMeasure = Class(name="smm::DirectMeasure")
smm_Operation = Class(name="smm::Operation")
smm_DirectMeasurement = Class(name="smm::DirectMeasurement")
smm_Count = Class(name="smm::Count")
DirectMeasurement = Class(name="DirectMeasurement")
smm_Counting = Class(name="smm::Counting")
DirectMeasure = Class(name="DirectMeasure")
smm_Grade = Class(name="smm::Grade")
smm_Scope = Class(name="smm::Scope")
smm_RefinementMeasureRelationship = Class(name="smm::RefinementMeasureRelationship")
smm_RecursiveMeasureRelationship = Class(name="smm::RecursiveMeasureRelationship")
smm_MeasureRelationship = Class(name="smm::MeasureRelationship", is_abstract=True)
smm_EquivalentMeasureRelationship = Class(name="smm::EquivalentMeasureRelationship")
smm_Measure = Class(name="smm::Measure", is_abstract=True)
smm_EquivalentMeasurementRelationship = Class(name="smm::EquivalentMeasurementRelationship")
smm_Measurement = Class(name="smm::Measurement", is_abstract=True)
smm_MeasureLibrary = Class(name="smm::MeasureLibrary")
smm_MofElement = Class(name="smm::MofElement")
smm_RecursiveMeasurementRelationship = Class(name="smm::RecursiveMeasurementRelationship")
smm_MeasurementRelationship = Class(name="smm::MeasurementRelationship", is_abstract=True)
smm_NamedMeasure = Class(name="smm::NamedMeasure")
smm_NamedMeasurement = Class(name="smm::NamedMeasurement")
smm_OCLOperation = Class(name="smm::OCLOperation")
smm_Observation = Class(name="smm::Observation")
smm_ObservationScope = Class(name="smm::ObservationScope")
smm_ObservedMeasure = Class(name="smm::ObservedMeasure")
smm_SmmElement = Class(name="smm::SmmElement", is_abstract=True)
smm_SmmRelationship = Class(name="smm::SmmRelationship", is_abstract=True)
smm_RefinementMeasurementRelationship = Class(name="smm::RefinementMeasurementRelationship")
smm_Ranking = Class(name="smm::Ranking")
smm_RankingInterval = Class(name="smm::RankingInterval")
smm_RatioMeasure = Class(name="smm::RatioMeasure")
BinaryMeasure = Class(name="BinaryMeasure")
smm_RatioMeasurement = Class(name="smm::RatioMeasurement")
BinaryMeasurement = Class(name="BinaryMeasurement")
smm_RescaledMeasure = Class(name="smm::RescaledMeasure")
smm_RescaledMeasurement = Class(name="smm::RescaledMeasurement")
smm_SmmModel = Class(name="smm::SmmModel")

# smm_Annotation class attributes and methods
smm_Annotation_text: Property = Property(name="text", type=StringType)
smm_Annotation.attributes={smm_Annotation_text}

# smm_Argument class attributes and methods
smm_Argument_type: Property = Property(name="type", type=StringType)
smm_Argument_value: Property = Property(name="value", type=StringType)
smm_Argument.attributes={smm_Argument_type, smm_Argument_value}

# smm_Attribute class attributes and methods
smm_Attribute_tag: Property = Property(name="tag", type=StringType)
smm_Attribute_value: Property = Property(name="value", type=StringType)
smm_Attribute.attributes={smm_Attribute_value, smm_Attribute_tag}

# smm_Base1MeasureRelationship class attributes and methods

# MeasureRelationship class attributes and methods

# smm_BinaryMeasure class attributes and methods
smm_BinaryMeasure_functor: Property = Property(name="functor", type=StringType)
smm_BinaryMeasure.attributes={smm_BinaryMeasure_functor}

# smm_DimensionalMeasure class attributes and methods
smm_DimensionalMeasure_unit: Property = Property(name="unit", type=StringType)
smm_DimensionalMeasure.attributes={smm_DimensionalMeasure_unit}

# smm_Base1MeasurementRelationship class attributes and methods

# MeasurementRelationship class attributes and methods

# smm_BinaryMeasurement class attributes and methods
smm_BinaryMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_BinaryMeasurement.attributes={smm_BinaryMeasurement_isBaseSupplied}

# smm_DimensionalMeasurement class attributes and methods
smm_DimensionalMeasurement_value: Property = Property(name="value", type=StringType)
smm_DimensionalMeasurement.attributes={smm_DimensionalMeasurement_value}

# smm_Base2MeasureRelationship class attributes and methods

# smm_Base2MeasurementRelationship class attributes and methods

# smm_AbstractMeasureElement class attributes and methods

# SmmElement class attributes and methods

# smm_BaseMeasurementRelationship class attributes and methods

# smm_CollectiveMeasurement class attributes and methods
smm_CollectiveMeasurement_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_CollectiveMeasurement.attributes={smm_CollectiveMeasurement_accumulator, smm_CollectiveMeasurement_isBaseSupplied}

# DimensionalMeasure class attributes and methods

# DimensionalMeasurement class attributes and methods

# smm_CategoryRelationship class attributes and methods

# SmmRelationship class attributes and methods

# smm_MeasureCategory class attributes and methods

# smm_Characteristic class attributes and methods

# AbstractMeasureElement class attributes and methods

# smm_BaseMeasureRelationship class attributes and methods

# smm_CollectiveMeasure class attributes and methods
smm_CollectiveMeasure_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasure.attributes={smm_CollectiveMeasure_accumulator}

# Measure class attributes and methods

# smm_RescaleMeasureRelationship class attributes and methods

# smm_RankingMeasureRelationship class attributes and methods

# Measurement class attributes and methods

# smm_RescaleMeasurementRelationship class attributes and methods

# smm_RankingMeasurementRelationship class attributes and methods

# smm_DirectMeasure class attributes and methods

# smm_Operation class attributes and methods
smm_Operation_language: Property = Property(name="language", type=StringType)
smm_Operation_body: Property = Property(name="body", type=StringType)
smm_Operation_m_getParamStrings: Method = Method(name="getParamStrings", parameters={}, type=StringType)
smm_Operation.attributes={smm_Operation_language, smm_Operation_body}
smm_Operation.methods={smm_Operation_m_getParamStrings}

# smm_DirectMeasurement class attributes and methods

# smm_Count class attributes and methods

# DirectMeasurement class attributes and methods

# smm_Counting class attributes and methods

# DirectMeasure class attributes and methods

# smm_Grade class attributes and methods
smm_Grade_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_Grade_value: Property = Property(name="value", type=StringType)
smm_Grade.attributes={smm_Grade_value, smm_Grade_isBaseSupplied}

# smm_Scope class attributes and methods
smm_Scope_class: Property = Property(name="class", type=StringType)
smm_Scope.attributes={smm_Scope_class}

# smm_RefinementMeasureRelationship class attributes and methods

# smm_RecursiveMeasureRelationship class attributes and methods

# smm_MeasureRelationship class attributes and methods

# smm_EquivalentMeasureRelationship class attributes and methods

# smm_Measure class attributes and methods
smm_Measure_measureLabelFormat: Property = Property(name="measureLabelFormat", type=StringType)
smm_Measure_measurementLabelFormat: Property = Property(name="measurementLabelFormat", type=StringType)
smm_Measure_visible: Property = Property(name="visible", type=StringType)
smm_Measure_m_getArguments: Method = Method(name="getArguments", parameters={}, type=StringType)
smm_Measure_m_getAllArguments: Method = Method(name="getAllArguments", parameters={}, type=StringType)
smm_Measure.attributes={smm_Measure_measureLabelFormat, smm_Measure_measurementLabelFormat, smm_Measure_visible}
smm_Measure.methods={smm_Measure_m_getAllArguments, smm_Measure_m_getArguments}

# smm_EquivalentMeasurementRelationship class attributes and methods

# smm_Measurement class attributes and methods
smm_Measurement_error: Property = Property(name="error", type=StringType)
smm_Measurement_breakValue: Property = Property(name="breakValue", type=StringType)
smm_Measurement_m_getMeasureLabel: Method = Method(name="getMeasureLabel", parameters={}, type=StringType)
smm_Measurement_m_getMeasurementLabel: Method = Method(name="getMeasurementLabel", parameters={}, type=StringType)
smm_Measurement.attributes={smm_Measurement_error, smm_Measurement_breakValue}
smm_Measurement.methods={smm_Measurement_m_getMeasurementLabel, smm_Measurement_m_getMeasureLabel}

# smm_MeasureLibrary class attributes and methods
smm_MeasureLibrary_m_getOperations: Method = Method(name="getOperations", parameters={}, type=AbstractMeasureElement)
smm_MeasureLibrary_m_getOclOperations: Method = Method(name="getOclOperations", parameters={}, type=AbstractMeasureElement)
smm_MeasureLibrary.methods={smm_MeasureLibrary_m_getOclOperations, smm_MeasureLibrary_m_getOperations}

# smm_MofElement class attributes and methods

# smm_RecursiveMeasurementRelationship class attributes and methods

# smm_MeasurementRelationship class attributes and methods
smm_MeasurementRelationship_m_getTo: Method = Method(name="getTo", parameters={}, type=Measurement)
smm_MeasurementRelationship_m_getFrom: Method = Method(name="getFrom", parameters={}, type=Measurement)
smm_MeasurementRelationship.methods={smm_MeasurementRelationship_m_getTo, smm_MeasurementRelationship_m_getFrom}

# smm_NamedMeasure class attributes and methods

# smm_NamedMeasurement class attributes and methods

# smm_OCLOperation class attributes and methods
smm_OCLOperation_context: Property = Property(name="context", type=StringType)
smm_OCLOperation_body: Property = Property(name="body", type=StringType)
smm_OCLOperation.attributes={smm_OCLOperation_context, smm_OCLOperation_body}

# smm_Observation class attributes and methods
smm_Observation_observer: Property = Property(name="observer", type=StringType)
smm_Observation_tool: Property = Property(name="tool", type=StringType)
smm_Observation_whenObserved: Property = Property(name="whenObserved", type=StringType)
smm_Observation.attributes={smm_Observation_observer, smm_Observation_tool, smm_Observation_whenObserved}

# smm_ObservationScope class attributes and methods
smm_ObservationScope_scopeUri: Property = Property(name="scopeUri", type=StringType)
smm_ObservationScope.attributes={smm_ObservationScope_scopeUri}

# smm_ObservedMeasure class attributes and methods

# smm_SmmElement class attributes and methods
smm_SmmElement_name: Property = Property(name="name", type=StringType)
smm_SmmElement_shortDescription: Property = Property(name="shortDescription", type=StringType)
smm_SmmElement_description: Property = Property(name="description", type=StringType)
smm_SmmElement_m_getInbound: Method = Method(name="getInbound", parameters={}, type=SmmRelationship)
smm_SmmElement_m_getOutbound: Method = Method(name="getOutbound", parameters={}, type=SmmRelationship)
smm_SmmElement.attributes={smm_SmmElement_description, smm_SmmElement_name, smm_SmmElement_shortDescription}
smm_SmmElement.methods={smm_SmmElement_m_getOutbound, smm_SmmElement_m_getInbound}

# smm_SmmRelationship class attributes and methods
smm_SmmRelationship_m_getTo: Method = Method(name="getTo", parameters={}, type=SmmElement)
smm_SmmRelationship_m_getFrom: Method = Method(name="getFrom", parameters={}, type=SmmElement)
smm_SmmRelationship.methods={smm_SmmRelationship_m_getTo, smm_SmmRelationship_m_getFrom}

# smm_RefinementMeasurementRelationship class attributes and methods

# smm_Ranking class attributes and methods

# smm_RankingInterval class attributes and methods
smm_RankingInterval_maximumEndpoint: Property = Property(name="maximumEndpoint", type=StringType)
smm_RankingInterval_maximumOpen: Property = Property(name="maximumOpen", type=StringType)
smm_RankingInterval_minimumEndpoint: Property = Property(name="minimumEndpoint", type=StringType)
smm_RankingInterval_minimumOpen: Property = Property(name="minimumOpen", type=StringType)
smm_RankingInterval_symbol: Property = Property(name="symbol", type=StringType)
smm_RankingInterval.attributes={smm_RankingInterval_minimumOpen, smm_RankingInterval_minimumEndpoint, smm_RankingInterval_maximumOpen, smm_RankingInterval_symbol, smm_RankingInterval_maximumEndpoint}

# smm_RatioMeasure class attributes and methods

# BinaryMeasure class attributes and methods

# smm_RatioMeasurement class attributes and methods

# BinaryMeasurement class attributes and methods

# smm_RescaledMeasure class attributes and methods
smm_RescaledMeasure_formula: Property = Property(name="formula", type=StringType)
smm_RescaledMeasure.attributes={smm_RescaledMeasure_formula}

# smm_RescaledMeasurement class attributes and methods
smm_RescaledMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=StringType)
smm_RescaledMeasurement.attributes={smm_RescaledMeasurement_isBaseSupplied}

# smm_SmmModel class attributes and methods

# Relationships
from0: BinaryAssociation = BinaryAssociation(
    name="from0",
    ends={
        Property(name="BinaryMeasure", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure1To", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="DimensionalMeasure", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure1From", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from2: BinaryAssociation = BinaryAssociation(
    name="from2",
    ends={
        Property(name="BinaryMeasurement", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement1To", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
to3: BinaryAssociation = BinaryAssociation(
    name="to3",
    ends={
        Property(name="DimensionalMeasurement", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement1From", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from4: BinaryAssociation = BinaryAssociation(
    name="from4",
    ends={
        Property(name="BinaryMeasure5", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure2To", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="DimensionalMeasure7", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure2From", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from15: BinaryAssociation = BinaryAssociation(
    name="from15",
    ends={
        Property(name="CollectiveMeasurement", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurementTo", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
to16: BinaryAssociation = BinaryAssociation(
    name="to16",
    ends={
        Property(name="DimensionalMeasurement17", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurementFrom", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure1To18: BinaryAssociation = BinaryAssociation(
    name="baseMeasure1To18",
    ends={
        Property(name="Base1MeasureRelationship", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure2To19: BinaryAssociation = BinaryAssociation(
    name="baseMeasure2To19",
    ends={
        Property(name="Base2MeasureRelationship", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from20", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasurement1To21: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1To21",
    ends={
        Property(name="Base1MeasurementRelationship", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from22", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseMeasurement2To23: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement2To23",
    ends={
        Property(name="Base2MeasurementRelationship", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from24", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from25: BinaryAssociation = BinaryAssociation(
    name="from25",
    ends={
        Property(name="smm_MeasureCategory", type=smm_CategoryRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CategoryRelationship", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1))
    }
)
to26: BinaryAssociation = BinaryAssociation(
    name="to26",
    ends={
        Property(name="smm_AbstractMeasureElement", type=smm_CategoryRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CategoryRelationship27", type=smm_AbstractMeasureElement, multiplicity=Multiplicity(1, 1))
    }
)
parent29: BinaryAssociation = BinaryAssociation(
    name="parent29",
    ends={
        Property(name="smm_Characteristic", type=smm_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Characteristic28", type=smm_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasureTo30: BinaryAssociation = BinaryAssociation(
    name="baseMeasureTo30",
    ends={
        Property(name="BaseMeasureRelationship", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from31", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="BinaryMeasurement9", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement2To", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
to10: BinaryAssociation = BinaryAssociation(
    name="to10",
    ends={
        Property(name="DimensionalMeasurement11", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement2From", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from12: BinaryAssociation = BinaryAssociation(
    name="from12",
    ends={
        Property(name="CollectiveMeasure", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasureTo", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="DimensionalMeasure14", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasureFrom", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasureFrom34: BinaryAssociation = BinaryAssociation(
    name="baseMeasureFrom34",
    ends={
        Property(name="BaseMeasureRelationship35", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasure1From36: BinaryAssociation = BinaryAssociation(
    name="baseMeasure1From36",
    ends={
        Property(name="Base1MeasureRelationship38", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to37", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasure2From39: BinaryAssociation = BinaryAssociation(
    name="baseMeasure2From39",
    ends={
        Property(name="Base2MeasureRelationship41", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to40", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rescaleTo42: BinaryAssociation = BinaryAssociation(
    name="rescaleTo42",
    ends={
        Property(name="RescaleMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from43", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rankingFrom44: BinaryAssociation = BinaryAssociation(
    name="rankingFrom44",
    ends={
        Property(name="RankingMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to45", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurementFrom46: BinaryAssociation = BinaryAssociation(
    name="baseMeasurementFrom46",
    ends={
        Property(name="BaseMeasurementRelationship48", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to47", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement1From49: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1From49",
    ends={
        Property(name="Base1MeasurementRelationship51", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to50", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement2From52: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement2From52",
    ends={
        Property(name="Base2MeasurementRelationship54", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to53", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rescaleTo55: BinaryAssociation = BinaryAssociation(
    name="rescaleTo55",
    ends={
        Property(name="RescaleMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from56", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rankingFrom57: BinaryAssociation = BinaryAssociation(
    name="rankingFrom57",
    ends={
        Property(name="RankingMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to58", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
operation59: BinaryAssociation = BinaryAssociation(
    name="operation59",
    ends={
        Property(name="smm_Operation", type=smm_DirectMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DirectMeasure", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasurementTo32: BinaryAssociation = BinaryAssociation(
    name="baseMeasurementTo32",
    ends={
        Property(name="BaseMeasurementRelationship", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from33", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
from65: BinaryAssociation = BinaryAssociation(
    name="from65",
    ends={
        Property(name="equivalentTo66", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="Measurement", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(1, 1))
    }
)
to67: BinaryAssociation = BinaryAssociation(
    name="to67",
    ends={
        Property(name="Measurement69", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentFrom68", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
rankingTo70: BinaryAssociation = BinaryAssociation(
    name="rankingTo70",
    ends={
        Property(name="RankingMeasurementRelationship72", type=smm_Grade, multiplicity=Multiplicity(1, 1)),
        Property(name="from71", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
category73: BinaryAssociation = BinaryAssociation(
    name="category73",
    ends={
        Property(name="MeasureCategory", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryMeasure", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
trait74: BinaryAssociation = BinaryAssociation(
    name="trait74",
    ends={
        Property(name="smm_Characteristic75", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure", type=smm_Characteristic, multiplicity=Multiplicity(1, 1))
    }
)
scope76: BinaryAssociation = BinaryAssociation(
    name="scope76",
    ends={
        Property(name="smm_Scope", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure77", type=smm_Scope, multiplicity=Multiplicity(1, 1))
    }
)
refinementTo78: BinaryAssociation = BinaryAssociation(
    name="refinementTo78",
    ends={
        Property(name="RefinementMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from79", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementFrom80: BinaryAssociation = BinaryAssociation(
    name="refinementFrom80",
    ends={
        Property(name="RefinementMeasureRelationship82", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to81", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentTo83: BinaryAssociation = BinaryAssociation(
    name="equivalentTo83",
    ends={
        Property(name="EquivalentMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from84", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentFrom85: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom85",
    ends={
        Property(name="EquivalentMeasureRelationship87", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to86", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
recursiveTo88: BinaryAssociation = BinaryAssociation(
    name="recursiveTo88",
    ends={
        Property(name="RecursiveMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from89", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
recursiveFrom90: BinaryAssociation = BinaryAssociation(
    name="recursiveFrom90",
    ends={
        Property(name="RecursiveMeasureRelationship92", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to91", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
measureRelationships93: BinaryAssociation = BinaryAssociation(
    name="measureRelationships93",
    ends={
        Property(name="smm_MeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure94", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapping60: BinaryAssociation = BinaryAssociation(
    name="mapping60",
    ends={
        Property(name="smm_Operation61", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_EquivalentMeasureRelationship", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
from62: BinaryAssociation = BinaryAssociation(
    name="from62",
    ends={
        Property(name="Measure", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentTo", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
to63: BinaryAssociation = BinaryAssociation(
    name="to63",
    ends={
        Property(name="Measure64", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentFrom", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
inbound98: BinaryAssociation = BinaryAssociation(
    name="inbound98",
    ends={
        Property(name="smm_MeasureRelationship100", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure99", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
outbound101: BinaryAssociation = BinaryAssociation(
    name="outbound101",
    ends={
        Property(name="smm_MeasureRelationship103", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure102", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
category105: BinaryAssociation = BinaryAssociation(
    name="category105",
    ends={
        Property(name="MeasureCategory106", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryElement", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
categoryElement108: BinaryAssociation = BinaryAssociation(
    name="categoryElement108",
    ends={
        Property(name="MeasureCategory109", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
categoryMeasure110: BinaryAssociation = BinaryAssociation(
    name="categoryMeasure110",
    ends={
        Property(name="Measure112", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="category111", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
measureElements113: BinaryAssociation = BinaryAssociation(
    name="measureElements113",
    ends={
        Property(name="smm_AbstractMeasureElement114", type=smm_MeasureLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_MeasureLibrary", type=smm_AbstractMeasureElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryRelationships115: BinaryAssociation = BinaryAssociation(
    name="categoryRelationships115",
    ends={
        Property(name="smm_CategoryRelationship117", type=smm_MeasureLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_MeasureLibrary116", type=smm_CategoryRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurandQuery118: BinaryAssociation = BinaryAssociation(
    name="measurandQuery118",
    ends={
        Property(name="smm_Operation120", type=smm_MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_MeasureRelationship119", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
defaultQuery95: BinaryAssociation = BinaryAssociation(
    name="defaultQuery95",
    ends={
        Property(name="smm_Operation97", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure96", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
equivalentTo127: BinaryAssociation = BinaryAssociation(
    name="equivalentTo127",
    ends={
        Property(name="EquivalentMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from128", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentFrom129: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom129",
    ends={
        Property(name="EquivalentMeasurementRelationship131", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to130", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
recursiveTo132: BinaryAssociation = BinaryAssociation(
    name="recursiveTo132",
    ends={
        Property(name="RecursiveMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from133", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
recursiveFrom134: BinaryAssociation = BinaryAssociation(
    name="recursiveFrom134",
    ends={
        Property(name="RecursiveMeasurementRelationship136", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to135", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
measurementRelationships137: BinaryAssociation = BinaryAssociation(
    name="measurementRelationships137",
    ends={
        Property(name="smm_MeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement138", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inbound139: BinaryAssociation = BinaryAssociation(
    name="inbound139",
    ends={
        Property(name="smm_MeasurementRelationship141", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement140", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
outbound142: BinaryAssociation = BinaryAssociation(
    name="outbound142",
    ends={
        Property(name="smm_MeasurementRelationship144", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement143", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
scopes145: BinaryAssociation = BinaryAssociation(
    name="scopes145",
    ends={
        Property(name="smm_ObservationScope", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation", type=smm_ObservationScope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observedMeasures146: BinaryAssociation = BinaryAssociation(
    name="observedMeasures146",
    ends={
        Property(name="smm_ObservedMeasure", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation147", type=smm_ObservedMeasure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requestedMeasures148: BinaryAssociation = BinaryAssociation(
    name="requestedMeasures148",
    ends={
        Property(name="smm_SmmElement", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation149", type=smm_SmmElement, multiplicity=Multiplicity(0, 9999))
    }
)
measurementRelations150: BinaryAssociation = BinaryAssociation(
    name="measurementRelations150",
    ends={
        Property(name="smm_SmmRelationship", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation151", type=smm_SmmRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments152: BinaryAssociation = BinaryAssociation(
    name="arguments152",
    ends={
        Property(name="smm_Argument", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation153", type=smm_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurand121: BinaryAssociation = BinaryAssociation(
    name="measurand121",
    ends={
        Property(name="smm_MofElement", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement", type=smm_MofElement, multiplicity=Multiplicity(0, 1))
    }
)
refinementTo122: BinaryAssociation = BinaryAssociation(
    name="refinementTo122",
    ends={
        Property(name="RefinementMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from123", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementFrom124: BinaryAssociation = BinaryAssociation(
    name="refinementFrom124",
    ends={
        Property(name="RefinementMeasurementRelationship126", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to125", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
interval160: BinaryAssociation = BinaryAssociation(
    name="interval160",
    ends={
        Property(name="smm_RankingInterval", type=smm_Ranking, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Ranking", type=smm_RankingInterval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rankingTo161: BinaryAssociation = BinaryAssociation(
    name="rankingTo161",
    ends={
        Property(name="RankingMeasureRelationship163", type=smm_Ranking, multiplicity=Multiplicity(1, 1)),
        Property(name="from162", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
from164: BinaryAssociation = BinaryAssociation(
    name="from164",
    ends={
        Property(name="Ranking", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingTo", type=smm_Ranking, multiplicity=Multiplicity(1, 1))
    }
)
to165: BinaryAssociation = BinaryAssociation(
    name="to165",
    ends={
        Property(name="DimensionalMeasure166", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingFrom", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from167: BinaryAssociation = BinaryAssociation(
    name="from167",
    ends={
        Property(name="Grade", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingTo168", type=smm_Grade, multiplicity=Multiplicity(1, 1))
    }
)
to169: BinaryAssociation = BinaryAssociation(
    name="to169",
    ends={
        Property(name="DimensionalMeasurement171", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingFrom170", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from172: BinaryAssociation = BinaryAssociation(
    name="from172",
    ends={
        Property(name="Measure173", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveTo", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
to174: BinaryAssociation = BinaryAssociation(
    name="to174",
    ends={
        Property(name="Measure175", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveFrom", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
measure154: BinaryAssociation = BinaryAssociation(
    name="measure154",
    ends={
        Property(name="smm_Measure156", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_ObservedMeasure155", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
measurements157: BinaryAssociation = BinaryAssociation(
    name="measurements157",
    ends={
        Property(name="smm_Measurement159", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_ObservedMeasure158", type=smm_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to184: BinaryAssociation = BinaryAssociation(
    name="to184",
    ends={
        Property(name="Measure185", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementFrom", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
from186: BinaryAssociation = BinaryAssociation(
    name="from186",
    ends={
        Property(name="Measurement188", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementTo187", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
to189: BinaryAssociation = BinaryAssociation(
    name="to189",
    ends={
        Property(name="Measurement191", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementFrom190", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
rescaleFrom192: BinaryAssociation = BinaryAssociation(
    name="rescaleFrom192",
    ends={
        Property(name="RescaleMeasureRelationship194", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to193", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
to195: BinaryAssociation = BinaryAssociation(
    name="to195",
    ends={
        Property(name="RescaledMeasure", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleFrom", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from196: BinaryAssociation = BinaryAssociation(
    name="from196",
    ends={
        Property(name="DimensionalMeasure197", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleTo", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
rescaleFrom198: BinaryAssociation = BinaryAssociation(
    name="rescaleFrom198",
    ends={
        Property(name="RescaleMeasurementRelationship200", type=smm_RescaledMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to199", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
to201: BinaryAssociation = BinaryAssociation(
    name="to201",
    ends={
        Property(name="RescaledMeasurement", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleFrom202", type=smm_RescaledMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from203: BinaryAssociation = BinaryAssociation(
    name="from203",
    ends={
        Property(name="DimensionalMeasurement205", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleTo204", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
recognizer206: BinaryAssociation = BinaryAssociation(
    name="recognizer206",
    ends={
        Property(name="smm_Operation208", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope207", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
breakCondition209: BinaryAssociation = BinaryAssociation(
    name="breakCondition209",
    ends={
        Property(name="smm_Operation211", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope210", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
from176: BinaryAssociation = BinaryAssociation(
    name="from176",
    ends={
        Property(name="Measurement178", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveTo177", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
to179: BinaryAssociation = BinaryAssociation(
    name="to179",
    ends={
        Property(name="Measurement181", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveFrom180", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
from182: BinaryAssociation = BinaryAssociation(
    name="from182",
    ends={
        Property(name="Measure183", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementTo", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
observations216: BinaryAssociation = BinaryAssociation(
    name="observations216",
    ends={
        Property(name="smm_Observation217", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmModel", type=smm_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
librairies218: BinaryAssociation = BinaryAssociation(
    name="librairies218",
    ends={
        Property(name="smm_MeasureLibrary220", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmModel219", type=smm_MeasureLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes212: BinaryAssociation = BinaryAssociation(
    name="attributes212",
    ends={
        Property(name="smm_Attribute", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmElement213", type=smm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations214: BinaryAssociation = BinaryAssociation(
    name="annotations214",
    ends={
        Property(name="smm_Annotation", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmElement215", type=smm_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smm_Annotation_SmmElement = Generalization(general=SmmElement, specific=smm_Annotation)
gen_smm_Argument_SmmElement = Generalization(general=SmmElement, specific=smm_Argument)
gen_smm_Attribute_SmmElement = Generalization(general=SmmElement, specific=smm_Attribute)
gen_smm_Base1MeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_Base1MeasureRelationship)
gen_smm_Base1MeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_Base1MeasurementRelationship)
gen_smm_Base2MeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_Base2MeasureRelationship)
gen_smm_Base2MeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_Base2MeasurementRelationship)
gen_smm_AbstractMeasureElement_SmmElement = Generalization(general=SmmElement, specific=smm_AbstractMeasureElement)
gen_smm_BaseMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_BaseMeasurementRelationship)
gen_smm_BinaryMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_BinaryMeasure)
gen_smm_BinaryMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_BinaryMeasurement)
gen_smm_CategoryRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_CategoryRelationship)
gen_smm_Characteristic_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Characteristic)
gen_smm_CollectiveMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_CollectiveMeasure)
gen_smm_CollectiveMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_CollectiveMeasurement)
gen_smm_BaseMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_BaseMeasureRelationship)
gen_smm_DimensionalMeasure_Measure = Generalization(general=Measure, specific=smm_DimensionalMeasure)
gen_smm_DimensionalMeasurement_Measurement = Generalization(general=Measurement, specific=smm_DimensionalMeasurement)
gen_smm_DirectMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_DirectMeasure)
gen_smm_DirectMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_DirectMeasurement)
gen_smm_Count_DirectMeasurement = Generalization(general=DirectMeasurement, specific=smm_Count)
gen_smm_Counting_DirectMeasure = Generalization(general=DirectMeasure, specific=smm_Counting)
gen_smm_Grade_Measurement = Generalization(general=Measurement, specific=smm_Grade)
gen_smm_Measure_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Measure)
gen_smm_EquivalentMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_EquivalentMeasureRelationship)
gen_smm_EquivalentMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_EquivalentMeasurementRelationship)
gen_smm_MeasureCategory_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_MeasureCategory)
gen_smm_MeasureLibrary_SmmElement = Generalization(general=SmmElement, specific=smm_MeasureLibrary)
gen_smm_MeasureRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasureRelationship)
gen_smm_Measurement_SmmElement = Generalization(general=SmmElement, specific=smm_Measurement)
gen_smm_MeasurementRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasurementRelationship)
gen_smm_NamedMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_NamedMeasure)
gen_smm_NamedMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_NamedMeasurement)
gen_smm_OCLOperation_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_OCLOperation)
gen_smm_Observation_SmmElement = Generalization(general=SmmElement, specific=smm_Observation)
gen_smm_ObservationScope_SmmElement = Generalization(general=SmmElement, specific=smm_ObservationScope)
gen_smm_Ranking_Measure = Generalization(general=Measure, specific=smm_Ranking)
gen_smm_RankingInterval_SmmElement = Generalization(general=SmmElement, specific=smm_RankingInterval)
gen_smm_RankingMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RankingMeasureRelationship)
gen_smm_RankingMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RankingMeasurementRelationship)
gen_smm_RatioMeasure_BinaryMeasure = Generalization(general=BinaryMeasure, specific=smm_RatioMeasure)
gen_smm_RatioMeasurement_BinaryMeasurement = Generalization(general=BinaryMeasurement, specific=smm_RatioMeasurement)
gen_smm_RecursiveMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RecursiveMeasureRelationship)
gen_smm_RecursiveMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RecursiveMeasurementRelationship)
gen_smm_ObservedMeasure_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_ObservedMeasure)
gen_smm_Operation_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Operation)
gen_smm_RefinementMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RefinementMeasurementRelationship)
gen_smm_RescaledMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_RescaledMeasure)
gen_smm_RescaleMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RescaleMeasureRelationship)
gen_smm_RescaledMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_RescaledMeasurement)
gen_smm_RescaleMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RescaleMeasurementRelationship)
gen_smm_Scope_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Scope)
gen_smm_RefinementMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RefinementMeasureRelationship)
gen_smm_SmmModel_SmmElement = Generalization(general=SmmElement, specific=smm_SmmModel)
gen_smm_SmmRelationship_SmmElement = Generalization(general=SmmElement, specific=smm_SmmRelationship)

# Domain Model
domain_model = DomainModel(
    name="smm",
    types={smm_Annotation, smm_Argument, smm_Attribute, smm_Base1MeasureRelationship, MeasureRelationship, smm_BinaryMeasure, smm_DimensionalMeasure, smm_Base1MeasurementRelationship, MeasurementRelationship, smm_BinaryMeasurement, smm_DimensionalMeasurement, smm_Base2MeasureRelationship, smm_Base2MeasurementRelationship, smm_AbstractMeasureElement, SmmElement, smm_BaseMeasurementRelationship, smm_CollectiveMeasurement, DimensionalMeasure, DimensionalMeasurement, smm_CategoryRelationship, SmmRelationship, smm_MeasureCategory, smm_Characteristic, AbstractMeasureElement, smm_BaseMeasureRelationship, smm_CollectiveMeasure, Measure, smm_RescaleMeasureRelationship, smm_RankingMeasureRelationship, Measurement, smm_RescaleMeasurementRelationship, smm_RankingMeasurementRelationship, smm_DirectMeasure, smm_Operation, smm_DirectMeasurement, smm_Count, DirectMeasurement, smm_Counting, DirectMeasure, smm_Grade, smm_Scope, smm_RefinementMeasureRelationship, smm_RecursiveMeasureRelationship, smm_MeasureRelationship, smm_EquivalentMeasureRelationship, smm_Measure, smm_EquivalentMeasurementRelationship, smm_Measurement, smm_MeasureLibrary, smm_MofElement, smm_RecursiveMeasurementRelationship, smm_MeasurementRelationship, smm_NamedMeasure, smm_NamedMeasurement, smm_OCLOperation, smm_Observation, smm_ObservationScope, smm_ObservedMeasure, smm_SmmElement, smm_SmmRelationship, smm_RefinementMeasurementRelationship, smm_Ranking, smm_RankingInterval, smm_RatioMeasure, BinaryMeasure, smm_RatioMeasurement, BinaryMeasurement, smm_RescaledMeasure, smm_RescaledMeasurement, smm_SmmModel, Accumulator},
    associations={from0, to1, from2, to3, from4, to6, from15, to16, baseMeasure1To18, baseMeasure2To19, baseMeasurement1To21, baseMeasurement2To23, from25, to26, parent29, baseMeasureTo30, from8, to10, from12, to13, baseMeasureFrom34, baseMeasure1From36, baseMeasure2From39, rescaleTo42, rankingFrom44, baseMeasurementFrom46, baseMeasurement1From49, baseMeasurement2From52, rescaleTo55, rankingFrom57, operation59, baseMeasurementTo32, from65, to67, rankingTo70, category73, trait74, scope76, refinementTo78, refinementFrom80, equivalentTo83, equivalentFrom85, recursiveTo88, recursiveFrom90, measureRelationships93, mapping60, from62, to63, inbound98, outbound101, category105, categoryElement108, categoryMeasure110, measureElements113, categoryRelationships115, measurandQuery118, defaultQuery95, equivalentTo127, equivalentFrom129, recursiveTo132, recursiveFrom134, measurementRelationships137, inbound139, outbound142, scopes145, observedMeasures146, requestedMeasures148, measurementRelations150, arguments152, measurand121, refinementTo122, refinementFrom124, interval160, rankingTo161, from164, to165, from167, to169, from172, to174, measure154, measurements157, to184, from186, to189, rescaleFrom192, to195, from196, rescaleFrom198, to201, from203, recognizer206, breakCondition209, from176, to179, from182, observations216, librairies218, attributes212, annotations214},
    generalizations={gen_smm_Annotation_SmmElement, gen_smm_Argument_SmmElement, gen_smm_Attribute_SmmElement, gen_smm_Base1MeasureRelationship_MeasureRelationship, gen_smm_Base1MeasurementRelationship_MeasurementRelationship, gen_smm_Base2MeasureRelationship_MeasureRelationship, gen_smm_Base2MeasurementRelationship_MeasurementRelationship, gen_smm_AbstractMeasureElement_SmmElement, gen_smm_BaseMeasurementRelationship_MeasurementRelationship, gen_smm_BinaryMeasure_DimensionalMeasure, gen_smm_BinaryMeasurement_DimensionalMeasurement, gen_smm_CategoryRelationship_SmmRelationship, gen_smm_Characteristic_AbstractMeasureElement, gen_smm_CollectiveMeasure_DimensionalMeasure, gen_smm_CollectiveMeasurement_DimensionalMeasurement, gen_smm_BaseMeasureRelationship_MeasureRelationship, gen_smm_DimensionalMeasure_Measure, gen_smm_DimensionalMeasurement_Measurement, gen_smm_DirectMeasure_DimensionalMeasure, gen_smm_DirectMeasurement_DimensionalMeasurement, gen_smm_Count_DirectMeasurement, gen_smm_Counting_DirectMeasure, gen_smm_Grade_Measurement, gen_smm_Measure_AbstractMeasureElement, gen_smm_EquivalentMeasureRelationship_MeasureRelationship, gen_smm_EquivalentMeasurementRelationship_MeasurementRelationship, gen_smm_MeasureCategory_AbstractMeasureElement, gen_smm_MeasureLibrary_SmmElement, gen_smm_MeasureRelationship_SmmRelationship, gen_smm_Measurement_SmmElement, gen_smm_MeasurementRelationship_SmmRelationship, gen_smm_NamedMeasure_DimensionalMeasure, gen_smm_NamedMeasurement_DimensionalMeasurement, gen_smm_OCLOperation_AbstractMeasureElement, gen_smm_Observation_SmmElement, gen_smm_ObservationScope_SmmElement, gen_smm_Ranking_Measure, gen_smm_RankingInterval_SmmElement, gen_smm_RankingMeasureRelationship_MeasureRelationship, gen_smm_RankingMeasurementRelationship_MeasurementRelationship, gen_smm_RatioMeasure_BinaryMeasure, gen_smm_RatioMeasurement_BinaryMeasurement, gen_smm_RecursiveMeasureRelationship_MeasureRelationship, gen_smm_RecursiveMeasurementRelationship_MeasurementRelationship, gen_smm_ObservedMeasure_SmmRelationship, gen_smm_Operation_AbstractMeasureElement, gen_smm_RefinementMeasurementRelationship_MeasurementRelationship, gen_smm_RescaledMeasure_DimensionalMeasure, gen_smm_RescaleMeasureRelationship_MeasureRelationship, gen_smm_RescaledMeasurement_DimensionalMeasurement, gen_smm_RescaleMeasurementRelationship_MeasurementRelationship, gen_smm_Scope_AbstractMeasureElement, gen_smm_RefinementMeasureRelationship_MeasureRelationship, gen_smm_SmmModel_SmmElement, gen_smm_SmmRelationship_SmmElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)