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
			EnumerationLiteral(name="average")
    }
)

# Classes
smm_SmmElement = Class(name="smm::SmmElement", is_abstract=True)
smm_SmmModel = Class(name="smm::SmmModel")
smm_Attribute = Class(name="smm::Attribute")
smm_Annotation = Class(name="smm::Annotation")
SmmElement = Class(name="SmmElement")
smm_SmmRelationship = Class(name="smm::SmmRelationship", is_abstract=True)
smm_CategoryRelationship = Class(name="smm::CategoryRelationship")
SmmRelationship = Class(name="SmmRelationship")
smm_Category = Class(name="smm::Category")
smm_Measurement = Class(name="smm::Measurement", is_abstract=True)
smm_MeasureRelationship = Class(name="smm::MeasureRelationship")
smm_Characteristic = Class(name="smm::Characteristic")
smm_Scope = Class(name="smm::Scope")
smm_Observation = Class(name="smm::Observation")
smm_MeasurementRelationship = Class(name="smm::MeasurementRelationship", is_abstract=True)
smm_Measure = Class(name="smm::Measure", is_abstract=True)
smm_DimensionalMeasure = Class(name="smm::DimensionalMeasure")
Measure = Class(name="Measure")
smm_Ranking = Class(name="smm::Ranking")
smm_RankingInterval = Class(name="smm::RankingInterval")
smm_CollectiveMeasure = Class(name="smm::CollectiveMeasure")
smm_NamedMeasure = Class(name="smm::NamedMeasure")
smm_RescaledMeasure = Class(name="smm::RescaledMeasure")
smm_RatioMeasure = Class(name="smm::RatioMeasure")
BinaryMeasure = Class(name="BinaryMeasure")
smm_Counting = Class(name="smm::Counting")
DirectMeasure = Class(name="DirectMeasure")
smm_DimensionalMeasurement = Class(name="smm::DimensionalMeasurement", is_abstract=True)
Measurement = Class(name="Measurement")
smm_Grade = Class(name="smm::Grade")
smm_DirectMeasurement = Class(name="smm::DirectMeasurement")
DimensionalMeasurement = Class(name="DimensionalMeasurement")
smm_BinaryMeasure = Class(name="smm::BinaryMeasure")
DimensionalMeasure = Class(name="DimensionalMeasure")
smm_DirectMeasure = Class(name="smm::DirectMeasure")
smm_CollectiveMeasurement = Class(name="smm::CollectiveMeasurement")
smm_AggregatedMeasurement = Class(name="smm::AggregatedMeasurement")
smm_NamedMeasurement = Class(name="smm::NamedMeasurement")
smm_ReScaledMeasurement = Class(name="smm::ReScaledMeasurement")
smm_Count = Class(name="smm::Count")
DirectMeasurement = Class(name="DirectMeasurement")

# smm_SmmElement class attributes and methods
smm_SmmElement_m_getInbound: Method = Method(name="getInbound", parameters={}, type=StringType)
smm_SmmElement_m_getOutbound: Method = Method(name="getOutbound", parameters={}, type=StringType)
smm_SmmElement.methods={smm_SmmElement_m_getInbound, smm_SmmElement_m_getOutbound}

# smm_SmmModel class attributes and methods

# smm_Attribute class attributes and methods
smm_Attribute_tag: Property = Property(name="tag", type=StringType)
smm_Attribute_value: Property = Property(name="value", type=StringType)
smm_Attribute.attributes={smm_Attribute_value, smm_Attribute_tag}

# smm_Annotation class attributes and methods
smm_Annotation_text: Property = Property(name="text", type=StringType)
smm_Annotation.attributes={smm_Annotation_text}

# SmmElement class attributes and methods

# smm_SmmRelationship class attributes and methods
smm_SmmRelationship_m_getTo: Method = Method(name="getTo", parameters={}, type=SmmElement)
smm_SmmRelationship_m_getFrom: Method = Method(name="getFrom", parameters={}, type=SmmElement)
smm_SmmRelationship.methods={smm_SmmRelationship_m_getTo, smm_SmmRelationship_m_getFrom}

# smm_CategoryRelationship class attributes and methods
smm_CategoryRelationship_name: Property = Property(name="name", type=StringType)
smm_CategoryRelationship.attributes={smm_CategoryRelationship_name}

# SmmRelationship class attributes and methods

# smm_Category class attributes and methods
smm_Category_name: Property = Property(name="name", type=StringType)
smm_Category.attributes={smm_Category_name}

# smm_Measurement class attributes and methods
smm_Measurement_error: Property = Property(name="error", type=StringType)
smm_Measurement.attributes={smm_Measurement_error}

# smm_MeasureRelationship class attributes and methods

# smm_Characteristic class attributes and methods
smm_Characteristic_name: Property = Property(name="name", type=StringType)
smm_Characteristic.attributes={smm_Characteristic_name}

# smm_Scope class attributes and methods
smm_Scope_class: Property = Property(name="class", type=StringType)
smm_Scope_enumerated: Property = Property(name="enumerated", type=BooleanType)
smm_Scope_name: Property = Property(name="name", type=StringType)
smm_Scope_recognizer: Property = Property(name="recognizer", type=StringType)
smm_Scope.attributes={smm_Scope_enumerated, smm_Scope_recognizer, smm_Scope_name, smm_Scope_class}

# smm_Observation class attributes and methods
smm_Observation_observer: Property = Property(name="observer", type=StringType)
smm_Observation_tool: Property = Property(name="tool", type=StringType)
smm_Observation_whenObserved: Property = Property(name="whenObserved", type=StringType)
smm_Observation.attributes={smm_Observation_observer, smm_Observation_tool, smm_Observation_whenObserved}

# smm_MeasurementRelationship class attributes and methods
smm_MeasurementRelationship_name: Property = Property(name="name", type=StringType)
smm_MeasurementRelationship.attributes={smm_MeasurementRelationship_name}

# smm_Measure class attributes and methods
smm_Measure_library: Property = Property(name="library", type=StringType)
smm_Measure_name: Property = Property(name="name", type=StringType)
smm_Measure.attributes={smm_Measure_name, smm_Measure_library}

# smm_DimensionalMeasure class attributes and methods
smm_DimensionalMeasure_unit: Property = Property(name="unit", type=StringType)
smm_DimensionalMeasure.attributes={smm_DimensionalMeasure_unit}

# Measure class attributes and methods

# smm_Ranking class attributes and methods

# smm_RankingInterval class attributes and methods
smm_RankingInterval_maximumEndpoint: Property = Property(name="maximumEndpoint", type=FloatType)
smm_RankingInterval_maximumOpen: Property = Property(name="maximumOpen", type=BooleanType)
smm_RankingInterval_minimumEndpoint: Property = Property(name="minimumEndpoint", type=FloatType)
smm_RankingInterval_minimumOpen: Property = Property(name="minimumOpen", type=BooleanType)
smm_RankingInterval_symbol: Property = Property(name="symbol", type=StringType)
smm_RankingInterval.attributes={smm_RankingInterval_maximumEndpoint, smm_RankingInterval_symbol, smm_RankingInterval_minimumOpen, smm_RankingInterval_minimumEndpoint, smm_RankingInterval_maximumOpen}

# smm_CollectiveMeasure class attributes and methods
smm_CollectiveMeasure_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasure.attributes={smm_CollectiveMeasure_accumulator}

# smm_NamedMeasure class attributes and methods

# smm_RescaledMeasure class attributes and methods
smm_RescaledMeasure_formula: Property = Property(name="formula", type=StringType)
smm_RescaledMeasure.attributes={smm_RescaledMeasure_formula}

# smm_RatioMeasure class attributes and methods

# BinaryMeasure class attributes and methods

# smm_Counting class attributes and methods

# DirectMeasure class attributes and methods

# smm_DimensionalMeasurement class attributes and methods
smm_DimensionalMeasurement_value: Property = Property(name="value", type=FloatType)
smm_DimensionalMeasurement.attributes={smm_DimensionalMeasurement_value}

# Measurement class attributes and methods

# smm_Grade class attributes and methods
smm_Grade_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_Grade_value: Property = Property(name="value", type=StringType)
smm_Grade.attributes={smm_Grade_value, smm_Grade_isBaseSupplied}

# smm_DirectMeasurement class attributes and methods

# DimensionalMeasurement class attributes and methods

# smm_BinaryMeasure class attributes and methods
smm_BinaryMeasure_functor: Property = Property(name="functor", type=StringType)
smm_BinaryMeasure.attributes={smm_BinaryMeasure_functor}

# DimensionalMeasure class attributes and methods

# smm_DirectMeasure class attributes and methods
smm_DirectMeasure_operation: Property = Property(name="operation", type=StringType)
smm_DirectMeasure.attributes={smm_DirectMeasure_operation}

# smm_CollectiveMeasurement class attributes and methods
smm_CollectiveMeasurement_accumulator: Property = Property(name="accumulator", type=StringType)
smm_CollectiveMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_CollectiveMeasurement.attributes={smm_CollectiveMeasurement_accumulator, smm_CollectiveMeasurement_isBaseSupplied}

# smm_AggregatedMeasurement class attributes and methods
smm_AggregatedMeasurement_isBaseSuppled: Property = Property(name="isBaseSuppled", type=BooleanType)
smm_AggregatedMeasurement.attributes={smm_AggregatedMeasurement_isBaseSuppled}

# smm_NamedMeasurement class attributes and methods

# smm_ReScaledMeasurement class attributes and methods
smm_ReScaledMeasurement_isBaseSupplied: Property = Property(name="isBaseSupplied", type=BooleanType)
smm_ReScaledMeasurement.attributes={smm_ReScaledMeasurement_isBaseSupplied}

# smm_Count class attributes and methods

# DirectMeasurement class attributes and methods

# Relationships
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="SmmModel", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElement", type=smm_SmmModel, multiplicity=Multiplicity(0, 1))
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="Attribute", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=smm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation2: BinaryAssociation = BinaryAssociation(
    name="annotation2",
    ends={
        Property(name="Annotation", type=smm_SmmElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owner3", type=smm_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElement4: BinaryAssociation = BinaryAssociation(
    name="modelElement4",
    ends={
        Property(name="SmmElement", type=smm_SmmModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=smm_SmmElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="Category", type=smm_CategoryRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="outCategory", type=smm_Category, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="Category7", type=smm_CategoryRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="inCategory", type=smm_Category, multiplicity=Multiplicity(1, 1))
    }
)
category9: BinaryAssociation = BinaryAssociation(
    name="category9",
    ends={
        Property(name="Category10", type=smm_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryElement", type=smm_Category, multiplicity=Multiplicity(0, 9999))
    }
)
categoryMeasure17: BinaryAssociation = BinaryAssociation(
    name="categoryMeasure17",
    ends={
        Property(name="Measure", type=smm_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category18", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
category19: BinaryAssociation = BinaryAssociation(
    name="category19",
    ends={
        Property(name="Category20", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryMeasure", type=smm_Category, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentFrom22: BinaryAssociation = BinaryAssociation(
    name="equivalentFrom22",
    ends={
        Property(name="Measure23", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentTo", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentTo25: BinaryAssociation = BinaryAssociation(
    name="equivalentTo25",
    ends={
        Property(name="Measure26", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="equivalentFrom", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
refinement28: BinaryAssociation = BinaryAssociation(
    name="refinement28",
    ends={
        Property(name="smm_Measure", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measure27", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
measurement29: BinaryAssociation = BinaryAssociation(
    name="measurement29",
    ends={
        Property(name="Measurement", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="measure", type=smm_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outMeasure30: BinaryAssociation = BinaryAssociation(
    name="outMeasure30",
    ends={
        Property(name="MeasureRelationship", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="from31", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
inMeasure32: BinaryAssociation = BinaryAssociation(
    name="inMeasure32",
    ends={
        Property(name="MeasureRelationship34", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="to33", type=smm_MeasureRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trait35: BinaryAssociation = BinaryAssociation(
    name="trait35",
    ends={
        Property(name="Characteristic", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="characteristics", type=smm_Characteristic, multiplicity=Multiplicity(1, 1))
    }
)
scope36: BinaryAssociation = BinaryAssociation(
    name="scope36",
    ends={
        Property(name="Scope", type=smm_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="measures", type=smm_Scope, multiplicity=Multiplicity(1, 1))
    }
)
measure37: BinaryAssociation = BinaryAssociation(
    name="measure37",
    ends={
        Property(name="Measure38", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="measurement", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
observation39: BinaryAssociation = BinaryAssociation(
    name="observation39",
    ends={
        Property(name="smm_Observation", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Measurement", type=smm_Observation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outMeasurement40: BinaryAssociation = BinaryAssociation(
    name="outMeasurement40",
    ends={
        Property(name="MeasurementRelationship", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="from41", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
categoryElement12: BinaryAssociation = BinaryAssociation(
    name="categoryElement12",
    ends={
        Property(name="Category13", type=smm_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=smm_Category, multiplicity=Multiplicity(0, 9999))
    }
)
outCategory14: BinaryAssociation = BinaryAssociation(
    name="outCategory14",
    ends={
        Property(name="CategoryRelationship", type=smm_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=smm_CategoryRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
inCategory15: BinaryAssociation = BinaryAssociation(
    name="inCategory15",
    ends={
        Property(name="CategoryRelationship16", type=smm_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=smm_CategoryRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
from45: BinaryAssociation = BinaryAssociation(
    name="from45",
    ends={
        Property(name="Measure46", type=smm_MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="outMeasure", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
to47: BinaryAssociation = BinaryAssociation(
    name="to47",
    ends={
        Property(name="Measure48", type=smm_MeasureRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="inMeasure", type=smm_Measure, multiplicity=Multiplicity(1, 1))
    }
)
interval49: BinaryAssociation = BinaryAssociation(
    name="interval49",
    ends={
        Property(name="RankingInterval", type=smm_Ranking, multiplicity=Multiplicity(1, 1)),
        Property(name="rank", type=smm_RankingInterval, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rank50: BinaryAssociation = BinaryAssociation(
    name="rank50",
    ends={
        Property(name="Ranking", type=smm_RankingInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="interval", type=smm_Ranking, multiplicity=Multiplicity(0, 1))
    }
)
parent52: BinaryAssociation = BinaryAssociation(
    name="parent52",
    ends={
        Property(name="smm_Characteristic", type=smm_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Characteristic51", type=smm_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
characteristics53: BinaryAssociation = BinaryAssociation(
    name="characteristics53",
    ends={
        Property(name="Measure54", type=smm_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="trait", type=smm_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measures55: BinaryAssociation = BinaryAssociation(
    name="measures55",
    ends={
        Property(name="Measure56", type=smm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=smm_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
inMeasurement42: BinaryAssociation = BinaryAssociation(
    name="inMeasurement42",
    ends={
        Property(name="MeasurementRelationship44", type=smm_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="to43", type=smm_MeasurementRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasure61: BinaryAssociation = BinaryAssociation(
    name="baseMeasure61",
    ends={
        Property(name="smm_DimensionalMeasure62", type=smm_CollectiveMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CollectiveMeasure", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasurement63: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement63",
    ends={
        Property(name="smm_DimensionalMeasurement", type=smm_Grade, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_Grade", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(0, 1))
    }
)
from64: BinaryAssociation = BinaryAssociation(
    name="from64",
    ends={
        Property(name="Measurement65", type=smm_MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="outMeasurement", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
to66: BinaryAssociation = BinaryAssociation(
    name="to66",
    ends={
        Property(name="Measurement67", type=smm_MeasurementRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="inMeasurement", type=smm_Measurement, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure157: BinaryAssociation = BinaryAssociation(
    name="baseMeasure157",
    ends={
        Property(name="smm_DimensionalMeasure", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasure", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasure258: BinaryAssociation = BinaryAssociation(
    name="baseMeasure258",
    ends={
        Property(name="smm_DimensionalMeasure60", type=smm_BinaryMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_BinaryMeasure59", type=smm_DimensionalMeasure, multiplicity=Multiplicity(1, 1))
    }
)
baseMeasurement68: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement68",
    ends={
        Property(name="smm_DimensionalMeasurement69", type=smm_CollectiveMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_CollectiveMeasurement", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(0, 9999))
    }
)
baseMeasurement70: BinaryAssociation = BinaryAssociation(
    name="baseMeasurement70",
    ends={
        Property(name="smm_DimensionalMeasurement71", type=smm_AggregatedMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="smm_AggregatedMeasurement", type=smm_DimensionalMeasurement, multiplicity=Multiplicity(0, 9999))
    }
)
owner72: BinaryAssociation = BinaryAssociation(
    name="owner72",
    ends={
        Property(name="SmmElement73", type=smm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=smm_SmmElement, multiplicity=Multiplicity(0, 1))
    }
)
owner74: BinaryAssociation = BinaryAssociation(
    name="owner74",
    ends={
        Property(name="SmmElement75", type=smm_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotation", type=smm_SmmElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_smm_SmmModel_SmmElement = Generalization(general=SmmElement, specific=smm_SmmModel)
gen_smm_SmmRelationship_SmmElement = Generalization(general=SmmElement, specific=smm_SmmRelationship)
gen_smm_CategoryRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_CategoryRelationship)
gen_smm_Category_SmmElement = Generalization(general=SmmElement, specific=smm_Category)
gen_smm_Measure_SmmElement = Generalization(general=SmmElement, specific=smm_Measure)
gen_smm_Measurement_SmmElement = Generalization(general=SmmElement, specific=smm_Measurement)
gen_smm_MeasureRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasureRelationship)
gen_smm_DimensionalMeasure_Measure = Generalization(general=Measure, specific=smm_DimensionalMeasure)
gen_smm_Ranking_Measure = Generalization(general=Measure, specific=smm_Ranking)
gen_smm_RankingInterval_SmmElement = Generalization(general=SmmElement, specific=smm_RankingInterval)
gen_smm_Characteristic_SmmElement = Generalization(general=SmmElement, specific=smm_Characteristic)
gen_smm_Scope_SmmElement = Generalization(general=SmmElement, specific=smm_Scope)
gen_smm_Observation_SmmElement = Generalization(general=SmmElement, specific=smm_Observation)
gen_smm_CollectiveMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_CollectiveMeasure)
gen_smm_NamedMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_NamedMeasure)
gen_smm_RescaledMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_RescaledMeasure)
gen_smm_RatioMeasure_BinaryMeasure = Generalization(general=BinaryMeasure, specific=smm_RatioMeasure)
gen_smm_Counting_DirectMeasure = Generalization(general=DirectMeasure, specific=smm_Counting)
gen_smm_DimensionalMeasurement_Measurement = Generalization(general=Measurement, specific=smm_DimensionalMeasurement)
gen_smm_Grade_Measurement = Generalization(general=Measurement, specific=smm_Grade)
gen_smm_MeasurementRelationship_SmmRelationship = Generalization(general=SmmRelationship, specific=smm_MeasurementRelationship)
gen_smm_DirectMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_DirectMeasurement)
gen_smm_BinaryMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_BinaryMeasure)
gen_smm_DirectMeasure_DimensionalMeasure = Generalization(general=DimensionalMeasure, specific=smm_DirectMeasure)
gen_smm_CollectiveMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_CollectiveMeasurement)
gen_smm_AggregatedMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_AggregatedMeasurement)
gen_smm_NamedMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_NamedMeasurement)
gen_smm_ReScaledMeasurement_DimensionalMeasurement = Generalization(general=DimensionalMeasurement, specific=smm_ReScaledMeasurement)
gen_smm_Count_DirectMeasurement = Generalization(general=DirectMeasurement, specific=smm_Count)
gen_smm_Attribute_SmmElement = Generalization(general=SmmElement, specific=smm_Attribute)
gen_smm_Annotation_SmmElement = Generalization(general=SmmElement, specific=smm_Annotation)

# Domain Model
domain_model = DomainModel(
    name="smm",
    types={smm_SmmElement, smm_SmmModel, smm_Attribute, smm_Annotation, SmmElement, smm_SmmRelationship, smm_CategoryRelationship, SmmRelationship, smm_Category, smm_Measurement, smm_MeasureRelationship, smm_Characteristic, smm_Scope, smm_Observation, smm_MeasurementRelationship, smm_Measure, smm_DimensionalMeasure, Measure, smm_Ranking, smm_RankingInterval, smm_CollectiveMeasure, smm_NamedMeasure, smm_RescaledMeasure, smm_RatioMeasure, BinaryMeasure, smm_Counting, DirectMeasure, smm_DimensionalMeasurement, Measurement, smm_Grade, smm_DirectMeasurement, DimensionalMeasurement, smm_BinaryMeasure, DimensionalMeasure, smm_DirectMeasure, smm_CollectiveMeasurement, smm_AggregatedMeasurement, smm_NamedMeasurement, smm_ReScaledMeasurement, smm_Count, DirectMeasurement, Accumulator},
    associations={model0, attribute1, annotation2, modelElement4, from5, to6, category9, categoryMeasure17, category19, equivalentFrom22, equivalentTo25, refinement28, measurement29, outMeasure30, inMeasure32, trait35, scope36, measure37, observation39, outMeasurement40, categoryElement12, outCategory14, inCategory15, from45, to47, interval49, rank50, parent52, characteristics53, measures55, inMeasurement42, baseMeasure61, baseMeasurement63, from64, to66, baseMeasure157, baseMeasure258, baseMeasurement68, baseMeasurement70, owner72, owner74},
    generalizations={gen_smm_SmmModel_SmmElement, gen_smm_SmmRelationship_SmmElement, gen_smm_CategoryRelationship_SmmRelationship, gen_smm_Category_SmmElement, gen_smm_Measure_SmmElement, gen_smm_Measurement_SmmElement, gen_smm_MeasureRelationship_SmmRelationship, gen_smm_DimensionalMeasure_Measure, gen_smm_Ranking_Measure, gen_smm_RankingInterval_SmmElement, gen_smm_Characteristic_SmmElement, gen_smm_Scope_SmmElement, gen_smm_Observation_SmmElement, gen_smm_CollectiveMeasure_DimensionalMeasure, gen_smm_NamedMeasure_DimensionalMeasure, gen_smm_RescaledMeasure_DimensionalMeasure, gen_smm_RatioMeasure_BinaryMeasure, gen_smm_Counting_DirectMeasure, gen_smm_DimensionalMeasurement_Measurement, gen_smm_Grade_Measurement, gen_smm_MeasurementRelationship_SmmRelationship, gen_smm_DirectMeasurement_DimensionalMeasurement, gen_smm_BinaryMeasure_DimensionalMeasure, gen_smm_DirectMeasure_DimensionalMeasure, gen_smm_CollectiveMeasurement_DimensionalMeasurement, gen_smm_AggregatedMeasurement_DimensionalMeasurement, gen_smm_NamedMeasurement_DimensionalMeasurement, gen_smm_ReScaledMeasurement_DimensionalMeasurement, gen_smm_Count_DirectMeasurement, gen_smm_Attribute_SmmElement, gen_smm_Annotation_SmmElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)