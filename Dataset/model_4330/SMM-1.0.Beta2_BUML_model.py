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
            EnumerationLiteral(name="sum"),
			EnumerationLiteral(name="maximum"),
			EnumerationLiteral(name="minimum"),
			EnumerationLiteral(name="average"),
			EnumerationLiteral(name="standardDeviation")
    }
)

# Classes
smm_AbstractMeasureElement = Class(name="smm_AbstractMeasureElement", is_abstract=True)
SmmElement = Class(name="SmmElement")
smm_CategoryRelationship = Class(name="smm_CategoryRelationship")
smm_Annotation = Class(name="smm_Annotation")
smm_Argument = Class(name="smm_Argument")
smm_Attribute = Class(name="smm_Attribute")
smm_AggregatedMeasurement = Class(name="smm_AggregatedMeasurement")
DimensionalMeasurement = Class(name="DimensionalMeasurement")
smm_DimensionalMeasurement = Class(name="smm_DimensionalMeasurement", is_abstract=True)
smm_Base1MeasurementRelationship = Class(name="smm_Base1MeasurementRelationship")
MeasurementRelationship = Class(name="MeasurementRelationship")
smm_Base1MeasureRelationship = Class(name="smm_Base1MeasureRelationship")
MeasureRelationship = Class(name="MeasureRelationship")
smm_BinaryMeasure = Class(name="smm_BinaryMeasure")
smm_DimensionalMeasure = Class(name="smm_DimensionalMeasure")
smm_Base2MeasurementRelationship = Class(name="smm_Base2MeasurementRelationship")
smm_Base2MeasureRelationship = Class(name="smm_Base2MeasureRelationship")
smm_BaseMeasurementRelationship = Class(name="smm_BaseMeasurementRelationship")
smm_CollectiveMeasurement = Class(name="smm_CollectiveMeasurement")
smm_BaseMeasureRelationship = Class(name="smm_BaseMeasureRelationship")
smm_CollectiveMeasure = Class(name="smm_CollectiveMeasure")
smm_BinaryMeasurement = Class(name="smm_BinaryMeasurement")
DimensionalMeasure = Class(name="DimensionalMeasure")
SmmRelationship = Class(name="SmmRelationship")
smm_MeasureCategory = Class(name="smm_MeasureCategory")
smm_Characteristic = Class(name="smm_Characteristic")
AbstractMeasureElement = Class(name="AbstractMeasureElement")
smm_Count = Class(name="smm_Count")
DirectMeasurement = Class(name="DirectMeasurement")
smm_Counting = Class(name="smm_Counting")
DirectMeasure = Class(name="DirectMeasure")
Measure = Class(name="Measure")
smm_RescaleMeasureRelationship = Class(name="smm_RescaleMeasureRelationship")
smm_RankingMeasureRelationship = Class(name="smm_RankingMeasureRelationship")
Measurement = Class(name="Measurement")
smm_RescaleMeasurementRelationship = Class(name="smm_RescaleMeasurementRelationship")
smm_RankingMeasurementRelationship = Class(name="smm_RankingMeasurementRelationship")
smm_DirectMeasure = Class(name="smm_DirectMeasure")
smm_Operation = Class(name="smm_Operation")
smm_DirectMeasurement = Class(name="smm_DirectMeasurement")
smm_EquivalentMeasureRelationship = Class(name="smm_EquivalentMeasureRelationship")
smm_Measure = Class(name="smm_Measure", is_abstract=True)
smm_EquivalentMeasurementRelationship = Class(name="smm_EquivalentMeasurementRelationship")
smm_Measurement = Class(name="smm_Measurement", is_abstract=True)
smm_MeasureRelationship = Class(name="smm_MeasureRelationship", is_abstract=True)
smm_Grade = Class(name="smm_Grade")
smm_Scope = Class(name="smm_Scope")
smm_RefinementMeasureRelationship = Class(name="smm_RefinementMeasureRelationship")
smm_RecursiveMeasureRelationship = Class(name="smm_RecursiveMeasureRelationship")
smm_RecursiveMeasurementRelationship = Class(name="smm_RecursiveMeasurementRelationship")
smm_MeasurementRelationship = Class(name="smm_MeasurementRelationship", is_abstract=True)
smm_NamedMeasure = Class(name="smm_NamedMeasure")
smm_MeasureLibrary = Class(name="smm_MeasureLibrary")
smm_EObject = Class(name="smm_EObject")
smm_RefinementMeasurementRelationship = Class(name="smm_RefinementMeasurementRelationship")
smm_Ranking = Class(name="smm_Ranking")
smm_RankingInterval = Class(name="smm_RankingInterval")
smm_NamedMeasurement = Class(name="smm_NamedMeasurement")
smm_Observation = Class(name="smm_Observation")
smm_ObservationScope = Class(name="smm_ObservationScope")
smm_ObservedMeasure = Class(name="smm_ObservedMeasure")
smm_SmmElement = Class(name="smm_SmmElement", is_abstract=True)
smm_SmmRelationship = Class(name="smm_SmmRelationship", is_abstract=True)
smm_OCLOperation = Class(name="smm_OCLOperation")
smm_RatioMeasure = Class(name="smm_RatioMeasure")
BinaryMeasure = Class(name="BinaryMeasure")
smm_RatioMeasurement = Class(name="smm_RatioMeasurement")
BinaryMeasurement = Class(name="BinaryMeasurement")
smm_SmmModel = Class(name="smm_SmmModel")
smm_RescaledMeasure = Class(name="smm_RescaledMeasure")
smm_RescaledMeasurement = Class(name="smm_RescaledMeasurement")

# smm_AbstractMeasureElement class attributes and methods

# SmmElement class attributes and methods

# smm_CategoryRelationship class attributes and methods

# smm_Annotation class attributes and methods
smm_Annotation_text: Property = Property(name="text", type=StringType)
smm_Annotation.attributes={smm_Annotation_text}

# smm_Argument class attributes and methods
smm_Argument_type: Property = Property(name="type", type=StringType)
smm_Argument_value: Property = Property(name="value", type=StringType)
smm_Argument.attributes={smm_Argument_value, smm_Argument_type}

# smm_Attribute class attributes and methods
smm_Attribute_tag: Property = Property(name="tag", type=StringType)
smm_Attribute_value: Property = Property(name="value", type=StringType)
smm_Attribute.attributes={smm_Attribute_value, smm_Attribute_tag}

# smm_AggregatedMeasurement class attributes and methods
smm_AggregatedMeasurement_isBaseSuppled: Property = Property(name="isBaseSuppled", type=BooleanType)
smm_AggregatedMeasurement.attributes={smm_AggregatedMeasurement_isBaseSuppled}

# DimensionalMeasurement class attributes and methods

# smm_DimensionalMeasurement class attributes and methods
smm_DimensionalMeasurement_value: Property = Property(name="value", type=FloatType)
smm_DimensionalMeasurement.attributes={smm_DimensionalMeasurement_value}

# smm_Base1MeasurementRelationship class attributes and methods

# MeasurementRelationship class attributes and methods

# smm_Base1MeasureRelationship class attributes and methods

# MeasureRelationship class attributes and methods

# smm_BinaryMeasure class attributes and methods
smm_BinaryMeasure_functor: Property = Property(name="functor", type=StringType)
smm_BinaryMeasure.attributes={smm_BinaryMeasure_functor}

# smm_DimensionalMeasure class attributes and methods
smm_DimensionalMeasure_unit: Property = Property(name="unit", type=StringType)
smm_DimensionalMeasure.attributes={smm_DimensionalMeasure_unit}

# smm_Base2MeasurementRelationship class attributes and methods

# smm_Base2MeasureRelationship class attributes and methods

# smm_BaseMeasurementRelationship class attributes and methods

# smm_CollectiveMeasurement class attributes and methods
smm_CollectiveMeasurement_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_CollectiveMeasurement.attributes={smm_CollectiveMeasurement_accumulator, smm_CollectiveMeasurement_isBaseSupplied}

# smm_BaseMeasureRelationship class attributes and methods

# smm_CollectiveMeasure class attributes and methods
smm_CollectiveMeasure_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasure.attributes={smm_CollectiveMeasure_accumulator}

# smm_BinaryMeasurement class attributes and methods
smm_BinaryMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_BinaryMeasurement.attributes={smm_BinaryMeasurement_isBaseSupplied}

# DimensionalMeasure class attributes and methods

# SmmRelationship class attributes and methods

# smm_MeasureCategory class attributes and methods

# smm_Characteristic class attributes and methods

# AbstractMeasureElement class attributes and methods

# smm_Count class attributes and methods

# DirectMeasurement class attributes and methods

# smm_Counting class attributes and methods

# DirectMeasure class attributes and methods

# Measure class attributes and methods

# smm_RescaleMeasureRelationship class attributes and methods

# smm_RankingMeasureRelationship class attributes and methods

# Measurement class attributes and methods

# smm_RescaleMeasurementRelationship class attributes and methods

# smm_RankingMeasurementRelationship class attributes and methods

# smm_DirectMeasure class attributes and methods

# smm_Operation class attributes and methods
smm_Operation_body: Property = Property(name="body", type=StringType)
smm_Operation_language: Property = Property(name="language", type=StringType)
smm_Operation_m_getParamStrings: Method = Method(name="getParamStrings", parameters={}, type=StringType)
smm_Operation.attributes={smm_Operation_body, smm_Operation_language}
smm_Operation.methods={smm_Operation_m_getParamStrings}

# smm_DirectMeasurement class attributes and methods

# smm_EquivalentMeasureRelationship class attributes and methods

# smm_Measure class attributes and methods
smm_Measure_measurementLabelFormat: Property = Property(name="measurementLabelFormat", type=StringType)
smm_Measure_visible: Property = Property(name="visible", type=BooleanType)
smm_Measure_measureLabelFormat: Property = Property(name="measureLabelFormat", type=StringType)
smm_Measure_m_getArguments: Method = Method(name="getArguments", parameters={}, type=StringType)
smm_Measure_m_getAllArguments: Method = Method(name="getAllArguments", parameters={}, type=StringType)
smm_Measure.attributes={smm_Measure_visible, smm_Measure_measureLabelFormat, smm_Measure_measurementLabelFormat}
smm_Measure.methods={smm_Measure_m_getArguments, smm_Measure_m_getAllArguments}

# smm_EquivalentMeasurementRelationship class attributes and methods

# smm_Measurement class attributes and methods
smm_Measurement_error: Property = Property(name="error", type=StringType)
smm_Measurement_breakValue: Property = Property(name="breakValue", type=StringType)
smm_Measurement_m_getMeasureLabel: Method = Method(name="getMeasureLabel", parameters={}, type=StringType)
smm_Measurement_m_getMeasurementLabel: Method = Method(name="getMeasurementLabel", parameters={}, type=StringType)
smm_Measurement.attributes={smm_Measurement_breakValue, smm_Measurement_error}
smm_Measurement.methods={smm_Measurement_m_getMeasureLabel, smm_Measurement_m_getMeasurementLabel}

# smm_MeasureRelationship class attributes and methods
smm_MeasureRelationship_m_getTo: Method = Method(name="getTo", parameters={}, type=Measure)
smm_MeasureRelationship_m_getFrom: Method = Method(name="getFrom", parameters={}, type=Measure)
smm_MeasureRelationship.methods={smm_MeasureRelationship_m_getFrom, smm_MeasureRelationship_m_getTo}

# smm_Grade class attributes and methods
smm_Grade_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_Grade_value: Property = Property(name="value", type=StringType)
smm_Grade.attributes={smm_Grade_isBaseSupplied, smm_Grade_value}

# smm_Scope class attributes and methods
smm_Scope_class_: Property = Property(name="class_", type=StringType)
smm_Scope.attributes={smm_Scope_class_}

# smm_RefinementMeasureRelationship class attributes and methods

# smm_RecursiveMeasureRelationship class attributes and methods

# smm_RecursiveMeasurementRelationship class attributes and methods

# smm_MeasurementRelationship class attributes and methods
smm_MeasurementRelationship_m_getTo: Method = Method(name="getTo", parameters={}, type=Measurement)
smm_MeasurementRelationship_m_getFrom: Method = Method(name="getFrom", parameters={}, type=Measurement)
smm_MeasurementRelationship.methods={smm_MeasurementRelationship_m_getTo, smm_MeasurementRelationship_m_getFrom}

# smm_NamedMeasure class attributes and methods

# smm_MeasureLibrary class attributes and methods
smm_MeasureLibrary_m_getOperations: Method = Method(name="getOperations", parameters={}, type=AbstractMeasureElement)
smm_MeasureLibrary_m_getOclOperations: Method = Method(name="getOclOperations", parameters={}, type=AbstractMeasureElement)
smm_MeasureLibrary.methods={smm_MeasureLibrary_m_getOperations, smm_MeasureLibrary_m_getOclOperations}

# smm_EObject class attributes and methods

# smm_RefinementMeasurementRelationship class attributes and methods

# smm_Ranking class attributes and methods

# smm_RankingInterval class attributes and methods
smm_RankingInterval_maximumEndpoint: Property = Property(name="maximumEndpoint", type=FloatType)
smm_RankingInterval_maximumOpen: Property = Property(name="maximumOpen", type=BooleanType)
smm_RankingInterval_minimumEndpoint: Property = Property(name="minimumEndpoint", type=FloatType)
smm_RankingInterval_minimumOpen: Property = Property(name="minimumOpen", type=BooleanType)
smm_RankingInterval_symbol: Property = Property(name="symbol", type=StringType)
smm_RankingInterval.attributes={smm_RankingInterval_symbol, smm_RankingInterval_minimumOpen, smm_RankingInterval_minimumEndpoint, smm_RankingInterval_maximumOpen, smm_RankingInterval_maximumEndpoint}

# smm_NamedMeasurement class attributes and methods

# smm_Observation class attributes and methods
smm_Observation_observer: Property = Property(name="observer", type=StringType)
smm_Observation_tool: Property = Property(name="tool", type=StringType)
smm_Observation_whenObserved: Property = Property(name="whenObserved", type=StringType)
smm_Observation.attributes={smm_Observation_whenObserved, smm_Observation_observer, smm_Observation_tool}

# smm_ObservationScope class attributes and methods
smm_ObservationScope_scopeUri: Property = Property(name="scopeUri", type=StringType)
smm_ObservationScope.attributes={smm_ObservationScope_scopeUri}

# smm_ObservedMeasure class attributes and methods
smm_ObservedMeasure_m_getMeasureRefimentsObservedMeasures: Method = Method(name="getMeasureRefimentsObservedMeasures", parameters={}, type=StringType)
smm_ObservedMeasure.methods={smm_ObservedMeasure_m_getMeasureRefimentsObservedMeasures}

# smm_SmmElement class attributes and methods
smm_SmmElement_shortDescription: Property = Property(name="shortDescription", type=StringType)
smm_SmmElement_description: Property = Property(name="description", type=StringType)
smm_SmmElement_name: Property = Property(name="name", type=StringType)
smm_SmmElement_m_getInbound: Method = Method(name="getInbound", parameters={}, type=SmmRelationship)
smm_SmmElement_m_getOutbound: Method = Method(name="getOutbound", parameters={}, type=SmmRelationship)
smm_SmmElement.attributes={smm_SmmElement_name, smm_SmmElement_description, smm_SmmElement_shortDescription}
smm_SmmElement.methods={smm_SmmElement_m_getOutbound, smm_SmmElement_m_getInbound}

# smm_SmmRelationship class attributes and methods
smm_SmmRelationship_m_getTo: Method = Method(name="getTo", parameters={}, type=SmmElement)
smm_SmmRelationship_m_getFrom: Method = Method(name="getFrom", parameters={}, type=SmmElement)
smm_SmmRelationship.methods={smm_SmmRelationship_m_getTo, smm_SmmRelationship_m_getFrom}

# smm_OCLOperation class attributes and methods
smm_OCLOperation_context: Property = Property(name="context", type=StringType)
smm_OCLOperation_body: Property = Property(name="body", type=StringType)
smm_OCLOperation.attributes={smm_OCLOperation_body, smm_OCLOperation_context}

# smm_RatioMeasure class attributes and methods

# BinaryMeasure class attributes and methods

# smm_RatioMeasurement class attributes and methods

# BinaryMeasurement class attributes and methods

# smm_SmmModel class attributes and methods

# smm_RescaledMeasure class attributes and methods
smm_RescaledMeasure_formula: Property = Property(name="formula", type=StringType)
smm_RescaledMeasure.attributes={smm_RescaledMeasure_formula}

# smm_RescaledMeasurement class attributes and methods
smm_RescaledMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_RescaledMeasurement.attributes={smm_RescaledMeasurement_isBaseSupplied}

# Relationships
inCategory0: BinaryAssociation = BinaryAssociation(
    name="inCategory0",
    ends={
        Property(name="smm_CategoryRelationship", type=smm_AbstractMeasureElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_AbstractMeasureElement", type=smm_CategoryRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement1: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1",
    ends={
        Property(name="smm_DimensionalMeasurement", type=smm_AggregatedMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_AggregatedMeasurement", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(0, 9999))
    }
)
to3: BinaryAssociation = BinaryAssociation(
    name="to3",
    ends={
        Property(name="DimensionalMeasurement", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement1From", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from_4: BinaryAssociation = BinaryAssociation(
    name="from_4",
    ends={
        Property(name="BinaryMeasure", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure1To", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1))
    }
)
to5: BinaryAssociation = BinaryAssociation(
    name="to5",
    ends={
        Property(name="DimensionalMeasure", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure1From", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from_6: BinaryAssociation = BinaryAssociation(
    name="from_6",
    ends={
        Property(name="BinaryMeasurement7", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement2To", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="DimensionalMeasurement9", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement2From", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from_10: BinaryAssociation = BinaryAssociation(
    name="from_10",
    ends={
        Property(name="BinaryMeasure11", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure2To", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1))
    }
)
to12: BinaryAssociation = BinaryAssociation(
    name="to12",
    ends={
        Property(name="DimensionalMeasure13", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasure2From", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from_14: BinaryAssociation = BinaryAssociation(
    name="from_14",
    ends={
        Property(name="CollectiveMeasurement", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurementTo", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="DimensionalMeasurement16", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurementFrom", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
to18: BinaryAssociation = BinaryAssociation(
    name="to18",
    ends={
        Property(name="DimensionalMeasure19", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasureFrom", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from_2: BinaryAssociation = BinaryAssociation(
    name="from_2",
    ends={
        Property(name="BinaryMeasurement", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasurement1To", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure1To20: BinaryAssociation = BinaryAssociation(
    name="baseMeasure1To20",
    ends={
        Property(name="Base1MeasureRelationship", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure2To21: BinaryAssociation = BinaryAssociation(
    name="baseMeasure2To21",
    ends={
        Property(name="Base2MeasureRelationship", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_22", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasurement1To23: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1To23",
    ends={
        Property(name="Base1MeasurementRelationship", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_24", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseMeasurement2To25: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement2To25",
    ends={
        Property(name="Base2MeasurementRelationship", type=smm_BinaryMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_26", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from_27: BinaryAssociation = BinaryAssociation(
    name="from_27",
    ends={
        Property(name="smm_MeasureCategory", type=smm_CategoryRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CategoryRelationship28", type=smm_MeasureCategory, multiplicity=Multiplicity(1, 1))
    }
)
to29: BinaryAssociation = BinaryAssociation(
    name="to29",
    ends={
        Property(name="smm_AbstractMeasureElement31", type=smm_CategoryRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CategoryRelationship30", type=smm_AbstractMeasureElement, multiplicity=Multiplicity(1, 1))
    }
)
parent33: BinaryAssociation = BinaryAssociation(
    name="parent33",
    ends={
        Property(name="smm_Characteristic", type=smm_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Characteristic32", type=smm_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasureTo34: BinaryAssociation = BinaryAssociation(
    name="baseMeasureTo34",
    ends={
        Property(name="BaseMeasureRelationship", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_35", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(1, 9999))
    }
)
baseMeasurementTo36: BinaryAssociation = BinaryAssociation(
    name="baseMeasurementTo36",
    ends={
        Property(name="BaseMeasurementRelationship", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_37", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasureFrom38: BinaryAssociation = BinaryAssociation(
    name="baseMeasureFrom38",
    ends={
        Property(name="BaseMeasureRelationship39", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
from_17: BinaryAssociation = BinaryAssociation(
    name="from_17",
    ends={
        Property(name="CollectiveMeasure", type=smm_BaseMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="baseMeasureTo", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure2From43: BinaryAssociation = BinaryAssociation(
    name="baseMeasure2From43",
    ends={
        Property(name="Base2MeasureRelationship45", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to44", type=smm_Base2MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rescaleTo46: BinaryAssociation = BinaryAssociation(
    name="rescaleTo46",
    ends={
        Property(name="RescaleMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_47", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
rankingFrom48: BinaryAssociation = BinaryAssociation(
    name="rankingFrom48",
    ends={
        Property(name="RankingMeasureRelationship", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to49", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurementFrom50: BinaryAssociation = BinaryAssociation(
    name="baseMeasurementFrom50",
    ends={
        Property(name="BaseMeasurementRelationship52", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to51", type=smm_BaseMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement1From53: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement1From53",
    ends={
        Property(name="Base1MeasurementRelationship55", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to54", type=smm_Base1MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement2From56: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement2From56",
    ends={
        Property(name="Base2MeasurementRelationship58", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to57", type=smm_Base2MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rescaleTo59: BinaryAssociation = BinaryAssociation(
    name="rescaleTo59",
    ends={
        Property(name="RescaleMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_60", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
rankingFrom61: BinaryAssociation = BinaryAssociation(
    name="rankingFrom61",
    ends={
        Property(name="RankingMeasurementRelationship", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to62", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
operation63: BinaryAssociation = BinaryAssociation(
    name="operation63",
    ends={
        Property(name="smm_Operation", type=smm_DirectMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_DirectMeasure", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapping64: BinaryAssociation = BinaryAssociation(
    name="mapping64",
    ends={
        Property(name="smm_Operation65", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_EquivalentMeasureRelationship", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
from_66: BinaryAssociation = BinaryAssociation(
    name="from_66",
    ends={
        Property(name="Measure", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentTo", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
to67: BinaryAssociation = BinaryAssociation(
    name="to67",
    ends={
        Property(name="Measure68", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentFrom", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure1From40: BinaryAssociation = BinaryAssociation(
    name="baseMeasure1From40",
    ends={
        Property(name="Base1MeasureRelationship42", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to41", type=smm_Base1MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
from_69: BinaryAssociation = BinaryAssociation(
    name="from_69",
    ends={
        Property(name="Measurement", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentTo70", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
recursiveFrom96: BinaryAssociation = BinaryAssociation(
    name="recursiveFrom96",
    ends={
        Property(name="RecursiveMeasureRelationship98", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to97", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
to71: BinaryAssociation = BinaryAssociation(
    name="to71",
    ends={
        Property(name="Measurement73", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentFrom72", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
measureRelationships99: BinaryAssociation = BinaryAssociation(
    name="measureRelationships99",
    ends={
        Property(name="smm_MeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure100", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultQuery101: BinaryAssociation = BinaryAssociation(
    name="defaultQuery101",
    ends={
        Property(name="smm_Operation103", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure102", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
baseMeasurement74: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement74",
    ends={
        Property(name="smm_DimensionalMeasurement75", type=smm_Grade, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Grade", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(0, 1))
    }
)
rankingTo76: BinaryAssociation = BinaryAssociation(
    name="rankingTo76",
    ends={
        Property(name="RankingMeasurementRelationship78", type=smm_Grade, multiplicity=Multiplicity(1, 1)),
        Property(name="from_77", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
category79: BinaryAssociation = BinaryAssociation(
    name="category79",
    ends={
        Property(name="MeasureCategory", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryMeasure", type=smm_MeasureCategory, multiplicity=Multiplicity(0, 9999))
    }
)
trait80: BinaryAssociation = BinaryAssociation(
    name="trait80",
    ends={
        Property(name="smm_Characteristic81", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure", type=smm_Characteristic, multiplicity=Multiplicity(1, 1))
    }
)
scope82: BinaryAssociation = BinaryAssociation(
    name="scope82",
    ends={
        Property(name="smm_Scope", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure83", type=smm_Scope, multiplicity=Multiplicity(1, 1))
    }
)
refinementTo84: BinaryAssociation = BinaryAssociation(
    name="refinementTo84",
    ends={
        Property(name="RefinementMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_85", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementFrom86: BinaryAssociation = BinaryAssociation(
    name="refinementFrom86",
    ends={
        Property(name="RefinementMeasureRelationship88", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to87", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentTo89: BinaryAssociation = BinaryAssociation(
    name="equivalentTo89",
    ends={
        Property(name="EquivalentMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_90", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentFrom91: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom91",
    ends={
        Property(name="EquivalentMeasureRelationship93", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to92", type=smm_EquivalentMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
recursiveTo94: BinaryAssociation = BinaryAssociation(
    name="recursiveTo94",
    ends={
        Property(name="RecursiveMeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from_95", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
recursiveTo132: BinaryAssociation = BinaryAssociation(
    name="recursiveTo132",
    ends={
        Property(name="RecursiveMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_133", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(0, 1))
    }
)
recursiveFrom134: BinaryAssociation = BinaryAssociation(
    name="recursiveFrom134",
    ends={
        Property(name="RecursiveMeasurementRelationship136", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to135", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
measurementRelationships137: BinaryAssociation = BinaryAssociation(
    name="measurementRelationships137",
    ends={
        Property(name="smm_MeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement138", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
measurand121: BinaryAssociation = BinaryAssociation(
    name="measurand121",
    ends={
        Property(name="smm_EObject", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement", type=smm_EObject, multiplicity=Multiplicity(0, 1))
    }
)
refinementTo122: BinaryAssociation = BinaryAssociation(
    name="refinementTo122",
    ends={
        Property(name="RefinementMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_123", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
refinementFrom124: BinaryAssociation = BinaryAssociation(
    name="refinementFrom124",
    ends={
        Property(name="RefinementMeasurementRelationship126", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to125", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentTo127: BinaryAssociation = BinaryAssociation(
    name="equivalentTo127",
    ends={
        Property(name="EquivalentMeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from_128", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentFrom129: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom129",
    ends={
        Property(name="EquivalentMeasurementRelationship131", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to130", type=smm_EquivalentMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
interval153: BinaryAssociation = BinaryAssociation(
    name="interval153",
    ends={
        Property(name="RankingInterval", type=smm_Ranking, multiplicity=Multiplicity(1, 1)),
        Property(name="rank", type=smm_RankingInterval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rankingTo154: BinaryAssociation = BinaryAssociation(
    name="rankingTo154",
    ends={
        Property(name="RankingMeasureRelationship156", type=smm_Ranking, multiplicity=Multiplicity(1, 1)),
        Property(name="from_155", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(0, 1))
    }
)
rank157: BinaryAssociation = BinaryAssociation(
    name="rank157",
    ends={
        Property(name="Ranking", type=smm_RankingInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="interval", type=smm_Ranking, multiplicity=Multiplicity(0, 1))
    }
)
scopes139: BinaryAssociation = BinaryAssociation(
    name="scopes139",
    ends={
        Property(name="smm_ObservationScope", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation", type=smm_ObservationScope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observedMeasures140: BinaryAssociation = BinaryAssociation(
    name="observedMeasures140",
    ends={
        Property(name="smm_ObservedMeasure", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation141", type=smm_ObservedMeasure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requestedMeasures142: BinaryAssociation = BinaryAssociation(
    name="requestedMeasures142",
    ends={
        Property(name="SmmElement", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="requestedObservations", type=smm_SmmElement, multiplicity=Multiplicity(0, 9999))
    }
)
measurementRelations143: BinaryAssociation = BinaryAssociation(
    name="measurementRelations143",
    ends={
        Property(name="smm_SmmRelationship", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation144", type=smm_SmmRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments145: BinaryAssociation = BinaryAssociation(
    name="arguments145",
    ends={
        Property(name="smm_Argument", type=smm_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Observation146", type=smm_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measure147: BinaryAssociation = BinaryAssociation(
    name="measure147",
    ends={
        Property(name="smm_Measure149", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_ObservedMeasure148", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
measurements150: BinaryAssociation = BinaryAssociation(
    name="measurements150",
    ends={
        Property(name="smm_Measurement152", type=smm_ObservedMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_ObservedMeasure151", type=smm_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_177: BinaryAssociation = BinaryAssociation(
    name="from_177",
    ends={
        Property(name="Measure178", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementTo", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
to179: BinaryAssociation = BinaryAssociation(
    name="to179",
    ends={
        Property(name="Measure180", type=smm_RefinementMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementFrom", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
from_181: BinaryAssociation = BinaryAssociation(
    name="from_181",
    ends={
        Property(name="Measurement183", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementTo182", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
from_158: BinaryAssociation = BinaryAssociation(
    name="from_158",
    ends={
        Property(name="Ranking159", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingTo", type=smm_Ranking, multiplicity=Multiplicity(1, 1))
    }
)
to160: BinaryAssociation = BinaryAssociation(
    name="to160",
    ends={
        Property(name="DimensionalMeasure161", type=smm_RankingMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingFrom", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from_162: BinaryAssociation = BinaryAssociation(
    name="from_162",
    ends={
        Property(name="Grade", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingTo163", type=smm_Grade, multiplicity=Multiplicity(1, 1))
    }
)
to164: BinaryAssociation = BinaryAssociation(
    name="to164",
    ends={
        Property(name="DimensionalMeasurement166", type=smm_RankingMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rankingFrom165", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from_167: BinaryAssociation = BinaryAssociation(
    name="from_167",
    ends={
        Property(name="Measure168", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveTo", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
to169: BinaryAssociation = BinaryAssociation(
    name="to169",
    ends={
        Property(name="Measure170", type=smm_RecursiveMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveFrom", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
from_171: BinaryAssociation = BinaryAssociation(
    name="from_171",
    ends={
        Property(name="Measurement173", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveTo172", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
to174: BinaryAssociation = BinaryAssociation(
    name="to174",
    ends={
        Property(name="Measurement176", type=smm_RecursiveMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="recursiveFrom175", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
requestedObservations213: BinaryAssociation = BinaryAssociation(
    name="requestedObservations213",
    ends={
        Property(name="Observation", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="requestedMeasures", type=smm_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
observations214: BinaryAssociation = BinaryAssociation(
    name="observations214",
    ends={
        Property(name="smm_Observation215", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmModel", type=smm_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
librairies216: BinaryAssociation = BinaryAssociation(
    name="librairies216",
    ends={
        Property(name="smm_MeasureLibrary218", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmModel217", type=smm_MeasureLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to184: BinaryAssociation = BinaryAssociation(
    name="to184",
    ends={
        Property(name="Measurement186", type=smm_RefinementMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="refinementFrom185", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
rescaleFrom187: BinaryAssociation = BinaryAssociation(
    name="rescaleFrom187",
    ends={
        Property(name="RescaleMeasureRelationship189", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="to188", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
to190: BinaryAssociation = BinaryAssociation(
    name="to190",
    ends={
        Property(name="RescaledMeasure", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleFrom", type=smm_RescaledMeasure, multiplicity=Multiplicity(1, 1))
    }
)
from_191: BinaryAssociation = BinaryAssociation(
    name="from_191",
    ends={
        Property(name="DimensionalMeasure192", type=smm_RescaleMeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleTo", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
rescaleFrom193: BinaryAssociation = BinaryAssociation(
    name="rescaleFrom193",
    ends={
        Property(name="RescaleMeasurementRelationship195", type=smm_RescaledMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to194", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
to196: BinaryAssociation = BinaryAssociation(
    name="to196",
    ends={
        Property(name="RescaledMeasurement", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleFrom197", type=smm_RescaledMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
from_198: BinaryAssociation = BinaryAssociation(
    name="from_198",
    ends={
        Property(name="DimensionalMeasurement200", type=smm_RescaleMeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="rescaleTo199", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(1, 1))
    }
)
elements201: BinaryAssociation = BinaryAssociation(
    name="elements201",
    ends={
        Property(name="smm_EObject203", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope202", type=smm_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
recognizerQuery204: BinaryAssociation = BinaryAssociation(
    name="recognizerQuery204",
    ends={
        Property(name="smm_Operation206", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope205", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
breakCondition207: BinaryAssociation = BinaryAssociation(
    name="breakCondition207",
    ends={
        Property(name="smm_Operation209", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Scope208", type=smm_Operation, multiplicity=Multiplicity(0, 1))
    }
)
attribute210: BinaryAssociation = BinaryAssociation(
    name="attribute210",
    ends={
        Property(name="smm_Attribute", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmElement", type=smm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation211: BinaryAssociation = BinaryAssociation(
    name="annotation211",
    ends={
        Property(name="smm_Annotation", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_SmmElement212", type=smm_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smm_AbstractMeasureElement_SmmElement = Generalization(general=SmmElement, specific=smm_AbstractMeasureElement)
gen_smm_Annotation_SmmElement = Generalization(general=SmmElement, specific=smm_Annotation)
gen_smm_Argument_SmmElement = Generalization(general=SmmElement, specific=smm_Argument)
gen_smm_Attribute_SmmElement = Generalization(general=SmmElement, specific=smm_Attribute)
gen_smm_AggregatedMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_AggregatedMeasurement)
gen_smm_Base1MeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_Base1MeasurementRelationship)
gen_smm_Base1MeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_Base1MeasureRelationship)
gen_smm_Base2MeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_Base2MeasurementRelationship)
gen_smm_Base2MeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_Base2MeasureRelationship)
gen_smm_BaseMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_BaseMeasurementRelationship)
gen_smm_BaseMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_BaseMeasureRelationship)
gen_smm_BinaryMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_BinaryMeasure)
gen_smm_BinaryMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_BinaryMeasurement)
gen_smm_CategoryRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_CategoryRelationship)
gen_smm_Characteristic_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Characteristic)
gen_smm_CollectiveMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_CollectiveMeasure)
gen_smm_CollectiveMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_CollectiveMeasurement)
gen_smm_Count_DirectMeasurement = Generalization(general=DirectMeasurement, specific=smm_Count)
gen_smm_Counting_DirectMeasure = Generalization(general=DirectMeasure, specific=smm_Counting)
gen_smm_DimensionalMeasure_Measure = Generalization(general=Measure, specific=smm_DimensionalMeasure)
gen_smm_DimensionalMeasurement_Measurement = Generalization(general=Measurement, specific=smm_DimensionalMeasurement)
gen_smm_DirectMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_DirectMeasure)
gen_smm_DirectMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_DirectMeasurement)
gen_smm_EquivalentMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_EquivalentMeasureRelationship)
gen_smm_Grade_Measurement = Generalization(general=Measurement, specific=smm_Grade)
gen_smm_Measure_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Measure)
gen_smm_EquivalentMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_EquivalentMeasurementRelationship)
gen_smm_MeasurementRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasurementRelationship)
gen_smm_NamedMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_NamedMeasure)
gen_smm_MeasureCategory_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_MeasureCategory)
gen_smm_MeasureLibrary_SmmElement = Generalization(general=SmmElement, specific=smm_MeasureLibrary)
gen_smm_MeasureRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasureRelationship)
gen_smm_Measurement_SmmElement = Generalization(general=SmmElement, specific=smm_Measurement)
gen_smm_Ranking_Measure = Generalization(general=Measure, specific=smm_Ranking)
gen_smm_RankingInterval_SmmElement = Generalization(general=SmmElement, specific=smm_RankingInterval)
gen_smm_NamedMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_NamedMeasurement)
gen_smm_Observation_SmmElement = Generalization(general=SmmElement, specific=smm_Observation)
gen_smm_ObservationScope_SmmElement = Generalization(general=SmmElement, specific=smm_ObservationScope)
gen_smm_ObservedMeasure_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_ObservedMeasure)
gen_smm_OCLOperation_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_OCLOperation)
gen_smm_Operation_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Operation)
gen_smm_RefinementMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RefinementMeasurementRelationship)
gen_smm_RankingMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RankingMeasureRelationship)
gen_smm_RankingMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RankingMeasurementRelationship)
gen_smm_RatioMeasure_BinaryMeasure = Generalization(general=BinaryMeasure, specific=smm_RatioMeasure)
gen_smm_RatioMeasurement_BinaryMeasurement = Generalization(general=BinaryMeasurement, specific=smm_RatioMeasurement)
gen_smm_RecursiveMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RecursiveMeasureRelationship)
gen_smm_RecursiveMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RecursiveMeasurementRelationship)
gen_smm_RefinementMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RefinementMeasureRelationship)
gen_smm_SmmModel_SmmElement = Generalization(general=SmmElement, specific=smm_SmmModel)
gen_smm_SmmRelationship_SmmElement = Generalization(general=SmmElement, specific=smm_SmmRelationship)
gen_smm_RescaledMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_RescaledMeasure)
gen_smm_RescaleMeasureRelationship_MeasureRelationship = Generalization(general=MeasureRelationship, specific=smm_RescaleMeasureRelationship)
gen_smm_RescaledMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_RescaledMeasurement)
gen_smm_RescaleMeasurementRelationship_MeasurementRelationship = Generalization(general=MeasurementRelationship, specific=smm_RescaleMeasurementRelationship)
gen_smm_Scope_AbstractMeasureElement = Generalization(general=AbstractMeasureElement, specific=smm_Scope)

# Domain Model
domain_model = DomainModel(
    name="smm",
    types={smm_AbstractMeasureElement, SmmElement, smm_CategoryRelationship, smm_Annotation, smm_Argument, smm_Attribute, smm_AggregatedMeasurement, DimensionalMeasurement, smm_DimensionalMeasurement, smm_Base1MeasurementRelationship, MeasurementRelationship, smm_Base1MeasureRelationship, MeasureRelationship, smm_BinaryMeasure, smm_DimensionalMeasure, smm_Base2MeasurementRelationship, smm_Base2MeasureRelationship, smm_BaseMeasurementRelationship, smm_CollectiveMeasurement, smm_BaseMeasureRelationship, smm_CollectiveMeasure, smm_BinaryMeasurement, DimensionalMeasure, SmmRelationship, smm_MeasureCategory, smm_Characteristic, AbstractMeasureElement, smm_Count, DirectMeasurement, smm_Counting, DirectMeasure, Measure, smm_RescaleMeasureRelationship, smm_RankingMeasureRelationship, Measurement, smm_RescaleMeasurementRelationship, smm_RankingMeasurementRelationship, smm_DirectMeasure, smm_Operation, smm_DirectMeasurement, smm_EquivalentMeasureRelationship, smm_Measure, smm_EquivalentMeasurementRelationship, smm_Measurement, smm_MeasureRelationship, smm_Grade, smm_Scope, smm_RefinementMeasureRelationship, smm_RecursiveMeasureRelationship, smm_RecursiveMeasurementRelationship, smm_MeasurementRelationship, smm_NamedMeasure, smm_MeasureLibrary, smm_EObject, smm_RefinementMeasurementRelationship, smm_Ranking, smm_RankingInterval, smm_NamedMeasurement, smm_Observation, smm_ObservationScope, smm_ObservedMeasure, smm_SmmElement, smm_SmmRelationship, smm_OCLOperation, smm_RatioMeasure, BinaryMeasure, smm_RatioMeasurement, BinaryMeasurement, smm_SmmModel, smm_RescaledMeasure, smm_RescaledMeasurement, Accumulator},
    associations={inCategory0, baseMeasurement1, to3, from_4, to5, from_6, to8, from_10, to12, from_14, to15, to18, from_2, baseMeasure1To20, baseMeasure2To21, baseMeasurement1To23, baseMeasurement2To25, from_27, to29, parent33, baseMeasureTo34, baseMeasurementTo36, baseMeasureFrom38, from_17, baseMeasure2From43, rescaleTo46, rankingFrom48, baseMeasurementFrom50, baseMeasurement1From53, baseMeasurement2From56, rescaleTo59, rankingFrom61, operation63, mapping64, from_66, to67, baseMeasure1From40, from_69, recursiveFrom96, to71, measureRelationships99, defaultQuery101, baseMeasurement74, rankingTo76, category79, trait80, scope82, refinementTo84, refinementFrom86, equivalentTo89, equivalentFrom91, recursiveTo94, recursiveTo132, recursiveFrom134, measurementRelationships137, category105, categoryElement108, categoryMeasure110, measureElements113, categoryRelationships115, measurandQuery118, measurand121, refinementTo122, refinementFrom124, equivalentTo127, equivalentFrom129, interval153, rankingTo154, rank157, scopes139, observedMeasures140, requestedMeasures142, measurementRelations143, arguments145, measure147, measurements150, from_177, to179, from_181, from_158, to160, from_162, to164, from_167, to169, from_171, to174, requestedObservations213, observations214, librairies216, to184, rescaleFrom187, to190, from_191, rescaleFrom193, to196, from_198, elements201, recognizerQuery204, breakCondition207, attribute210, annotation211},
    generalizations={gen_smm_AbstractMeasureElement_SmmElement, gen_smm_Annotation_SmmElement, gen_smm_Argument_SmmElement, gen_smm_Attribute_SmmElement, gen_smm_AggregatedMeasurement_DimensionalMeasurement, gen_smm_Base1MeasurementRelationship_MeasurementRelationship, gen_smm_Base1MeasureRelationship_MeasureRelationship, gen_smm_Base2MeasurementRelationship_MeasurementRelationship, gen_smm_Base2MeasureRelationship_MeasureRelationship, gen_smm_BaseMeasurementRelationship_MeasurementRelationship, gen_smm_BaseMeasureRelationship_MeasureRelationship, gen_smm_BinaryMeasure_DimensionalMeasure, gen_smm_BinaryMeasurement_DimensionalMeasurement, gen_smm_CategoryRelationship_SmmRelationship, gen_smm_Characteristic_AbstractMeasureElement, gen_smm_CollectiveMeasure_DimensionalMeasure, gen_smm_CollectiveMeasurement_DimensionalMeasurement, gen_smm_Count_DirectMeasurement, gen_smm_Counting_DirectMeasure, gen_smm_DimensionalMeasure_Measure, gen_smm_DimensionalMeasurement_Measurement, gen_smm_DirectMeasure_DimensionalMeasure, gen_smm_DirectMeasurement_DimensionalMeasurement, gen_smm_EquivalentMeasureRelationship_MeasureRelationship, gen_smm_Grade_Measurement, gen_smm_Measure_AbstractMeasureElement, gen_smm_EquivalentMeasurementRelationship_MeasurementRelationship, gen_smm_MeasurementRelationship_SmmRelationship, gen_smm_NamedMeasure_DimensionalMeasure, gen_smm_MeasureCategory_AbstractMeasureElement, gen_smm_MeasureLibrary_SmmElement, gen_smm_MeasureRelationship_SmmRelationship, gen_smm_Measurement_SmmElement, gen_smm_Ranking_Measure, gen_smm_RankingInterval_SmmElement, gen_smm_NamedMeasurement_DimensionalMeasurement, gen_smm_Observation_SmmElement, gen_smm_ObservationScope_SmmElement, gen_smm_ObservedMeasure_SmmRelationship, gen_smm_OCLOperation_AbstractMeasureElement, gen_smm_Operation_AbstractMeasureElement, gen_smm_RefinementMeasurementRelationship_MeasurementRelationship, gen_smm_RankingMeasureRelationship_MeasureRelationship, gen_smm_RankingMeasurementRelationship_MeasurementRelationship, gen_smm_RatioMeasure_BinaryMeasure, gen_smm_RatioMeasurement_BinaryMeasurement, gen_smm_RecursiveMeasureRelationship_MeasureRelationship, gen_smm_RecursiveMeasurementRelationship_MeasurementRelationship, gen_smm_RefinementMeasureRelationship_MeasureRelationship, gen_smm_SmmModel_SmmElement, gen_smm_SmmRelationship_SmmElement, gen_smm_RescaledMeasure_DimensionalMeasure, gen_smm_RescaleMeasureRelationship_MeasureRelationship, gen_smm_RescaledMeasurement_DimensionalMeasurement, gen_smm_RescaleMeasurementRelationship_MeasurementRelationship, gen_smm_Scope_AbstractMeasureElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)