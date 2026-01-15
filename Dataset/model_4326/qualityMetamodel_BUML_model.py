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
QualityMetamodel_ValueType = Class(name="QualityMetamodel::ValueType", is_abstract=True)
QualityMetamodel_QualityAttribute = Class(name="QualityMetamodel::QualityAttribute")
QualityMetamodel_Value = Class(name="QualityMetamodel::Value", is_abstract=True)
QualityMetamodel_SingleValue = Class(name="QualityMetamodel::SingleValue")
Value = Class(name="Value")
QualityMetamodel_AggregatedValue = Class(name="QualityMetamodel::AggregatedValue")
QualityMetamodel_Operation = Class(name="QualityMetamodel::Operation")
QualityMetamodel_QualityModel = Class(name="QualityMetamodel::QualityModel")
QualityMetamodel_MetricProvider = Class(name="QualityMetamodel::MetricProvider")
QualityMetamodel_TextValueType = Class(name="QualityMetamodel::TextValueType")
ValueType = Class(name="ValueType")
QualityMetamodel_RangeValueType = Class(name="QualityMetamodel::RangeValueType")
QualityMetamodel_AggregatedValueMetric = Class(name="QualityMetamodel::AggregatedValueMetric")
QualityMetamodel_EnumerationMetric = Class(name="QualityMetamodel::EnumerationMetric")
QualityMetamodel_EnumerationItem = Class(name="QualityMetamodel::EnumerationItem")
QualityMetamodel_RealValueType = Class(name="QualityMetamodel::RealValueType")
QualityMetamodel_BooleanValueType = Class(name="QualityMetamodel::BooleanValueType")
QualityMetamodel_IntegerValueType = Class(name="QualityMetamodel::IntegerValueType")

# QualityMetamodel_ValueType class attributes and methods
QualityMetamodel_ValueType_name: Property = Property(name="name", type=StringType)
QualityMetamodel_ValueType.attributes={QualityMetamodel_ValueType_name}

# QualityMetamodel_QualityAttribute class attributes and methods
QualityMetamodel_QualityAttribute_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QualityAttribute.attributes={QualityMetamodel_QualityAttribute_name}

# QualityMetamodel_Value class attributes and methods
QualityMetamodel_Value_name: Property = Property(name="name", type=StringType)
QualityMetamodel_Value_description: Property = Property(name="description", type=StringType)
QualityMetamodel_Value.attributes={QualityMetamodel_Value_name, QualityMetamodel_Value_description}

# QualityMetamodel_SingleValue class attributes and methods

# Value class attributes and methods

# QualityMetamodel_AggregatedValue class attributes and methods

# QualityMetamodel_Operation class attributes and methods
QualityMetamodel_Operation_name: Property = Property(name="name", type=StringType)
QualityMetamodel_Operation_body: Property = Property(name="body", type=StringType)
QualityMetamodel_Operation.attributes={QualityMetamodel_Operation_body, QualityMetamodel_Operation_name}

# QualityMetamodel_QualityModel class attributes and methods
QualityMetamodel_QualityModel_name: Property = Property(name="name", type=StringType)
QualityMetamodel_QualityModel.attributes={QualityMetamodel_QualityModel_name}

# QualityMetamodel_MetricProvider class attributes and methods
QualityMetamodel_MetricProvider_name: Property = Property(name="name", type=StringType)
QualityMetamodel_MetricProvider_description: Property = Property(name="description", type=StringType)
QualityMetamodel_MetricProvider_id: Property = Property(name="id", type=StringType)
QualityMetamodel_MetricProvider.attributes={QualityMetamodel_MetricProvider_name, QualityMetamodel_MetricProvider_description, QualityMetamodel_MetricProvider_id}

# QualityMetamodel_TextValueType class attributes and methods
QualityMetamodel_TextValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_TextValueType.attributes={QualityMetamodel_TextValueType_value}

# ValueType class attributes and methods

# QualityMetamodel_RangeValueType class attributes and methods
QualityMetamodel_RangeValueType_min: Property = Property(name="min", type=StringType)
QualityMetamodel_RangeValueType_max: Property = Property(name="max", type=StringType)
QualityMetamodel_RangeValueType.attributes={QualityMetamodel_RangeValueType_max, QualityMetamodel_RangeValueType_min}

# QualityMetamodel_AggregatedValueMetric class attributes and methods
QualityMetamodel_AggregatedValueMetric_minimum: Property = Property(name="minimum", type=StringType)
QualityMetamodel_AggregatedValueMetric_maximum: Property = Property(name="maximum", type=StringType)
QualityMetamodel_AggregatedValueMetric_average: Property = Property(name="average", type=StringType)
QualityMetamodel_AggregatedValueMetric_median: Property = Property(name="median", type=StringType)
QualityMetamodel_AggregatedValueMetric_standardDeviation: Property = Property(name="standardDeviation", type=StringType)
QualityMetamodel_AggregatedValueMetric.attributes={QualityMetamodel_AggregatedValueMetric_standardDeviation, QualityMetamodel_AggregatedValueMetric_median, QualityMetamodel_AggregatedValueMetric_maximum, QualityMetamodel_AggregatedValueMetric_minimum, QualityMetamodel_AggregatedValueMetric_average}

# QualityMetamodel_EnumerationMetric class attributes and methods

# QualityMetamodel_EnumerationItem class attributes and methods
QualityMetamodel_EnumerationItem_name: Property = Property(name="name", type=StringType)
QualityMetamodel_EnumerationItem.attributes={QualityMetamodel_EnumerationItem_name}

# QualityMetamodel_RealValueType class attributes and methods
QualityMetamodel_RealValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_RealValueType.attributes={QualityMetamodel_RealValueType_value}

# QualityMetamodel_BooleanValueType class attributes and methods
QualityMetamodel_BooleanValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_BooleanValueType.attributes={QualityMetamodel_BooleanValueType_value}

# QualityMetamodel_IntegerValueType class attributes and methods
QualityMetamodel_IntegerValueType_value: Property = Property(name="value", type=StringType)
QualityMetamodel_IntegerValueType.attributes={QualityMetamodel_IntegerValueType_value}

# Relationships
metricProviders0: BinaryAssociation = BinaryAssociation(
    name="metricProviders0",
    ends={
        Property(name="QualityMetamodel_QualityModel", type=QualityMetamodel_MetricProvider, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="QualityMetamodel_MetricProvider", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1))
    }
)
qualityTypes1: BinaryAssociation = BinaryAssociation(
    name="qualityTypes1",
    ends={
        Property(name="QualityMetamodel_ValueType", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel2", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualityAttributes3: BinaryAssociation = BinaryAssociation(
    name="qualityAttributes3",
    ends={
        Property(name="QualityMetamodel_QualityAttribute", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel4", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualityValues5: BinaryAssociation = BinaryAssociation(
    name="qualityValues5",
    ends={
        Property(name="QualityMetamodel_Value", type=QualityMetamodel_QualityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityModel6", type=QualityMetamodel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="QualityMetamodel_Value9", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityAttribute8", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 1))
    }
)
qualityAttributes11: BinaryAssociation = BinaryAssociation(
    name="qualityAttributes11",
    ends={
        Property(name="QualityMetamodel_QualityAttribute12", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_QualityAttribute10", type=QualityMetamodel_QualityAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="ValueType", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="val", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(1, 1))
    }
)
val14: BinaryAssociation = BinaryAssociation(
    name="val14",
    ends={
        Property(name="Value", type=QualityMetamodel_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 1))
    }
)
measuredBy15: BinaryAssociation = BinaryAssociation(
    name="measuredBy15",
    ends={
        Property(name="QualityMetamodel_MetricProvider16", type=QualityMetamodel_SingleValue, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_SingleValue", type=QualityMetamodel_MetricProvider, multiplicity=Multiplicity(1, 1))
    }
)
calculatedBy17: BinaryAssociation = BinaryAssociation(
    name="calculatedBy17",
    ends={
        Property(name="QualityMetamodel_Operation", type=QualityMetamodel_AggregatedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_AggregatedValue", type=QualityMetamodel_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aggregatedValues18: BinaryAssociation = BinaryAssociation(
    name="aggregatedValues18",
    ends={
        Property(name="QualityMetamodel_Value20", type=QualityMetamodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_Operation19", type=QualityMetamodel_Value, multiplicity=Multiplicity(1, 9999))
    }
)
set21: BinaryAssociation = BinaryAssociation(
    name="set21",
    ends={
        Property(name="QualityMetamodel_EnumerationItem", type=QualityMetamodel_EnumerationMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_EnumerationMetric", type=QualityMetamodel_EnumerationItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="QualityMetamodel_EnumerationItem24", type=QualityMetamodel_EnumerationMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetamodel_EnumerationMetric23", type=QualityMetamodel_EnumerationItem, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_QualityMetamodel_SingleValue_Value = Generalization(general=Value, specific=QualityMetamodel_SingleValue)
gen_QualityMetamodel_AggregatedValue_Value = Generalization(general=Value, specific=QualityMetamodel_AggregatedValue)
gen_QualityMetamodel_TextValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_TextValueType)
gen_QualityMetamodel_RangeValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RangeValueType)
gen_QualityMetamodel_AggregatedValueMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_AggregatedValueMetric)
gen_QualityMetamodel_EnumerationMetric_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_EnumerationMetric)
gen_QualityMetamodel_RealValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_RealValueType)
gen_QualityMetamodel_BooleanValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_BooleanValueType)
gen_QualityMetamodel_IntegerValueType_ValueType = Generalization(general=ValueType, specific=QualityMetamodel_IntegerValueType)

# Domain Model
domain_model = DomainModel(
    name="QualityMetamodel",
    types={QualityMetamodel_ValueType, QualityMetamodel_QualityAttribute, QualityMetamodel_Value, QualityMetamodel_SingleValue, Value, QualityMetamodel_AggregatedValue, QualityMetamodel_Operation, QualityMetamodel_QualityModel, QualityMetamodel_MetricProvider, QualityMetamodel_TextValueType, ValueType, QualityMetamodel_RangeValueType, QualityMetamodel_AggregatedValueMetric, QualityMetamodel_EnumerationMetric, QualityMetamodel_EnumerationItem, QualityMetamodel_RealValueType, QualityMetamodel_BooleanValueType, QualityMetamodel_IntegerValueType},
    associations={metricProviders0, qualityTypes1, qualityAttributes3, qualityValues5, value7, qualityAttributes11, type13, val14, measuredBy15, calculatedBy17, aggregatedValues18, set21, value22},
    generalizations={gen_QualityMetamodel_SingleValue_Value, gen_QualityMetamodel_AggregatedValue_Value, gen_QualityMetamodel_TextValueType_ValueType, gen_QualityMetamodel_RangeValueType_ValueType, gen_QualityMetamodel_AggregatedValueMetric_ValueType, gen_QualityMetamodel_EnumerationMetric_ValueType, gen_QualityMetamodel_RealValueType_ValueType, gen_QualityMetamodel_BooleanValueType_ValueType, gen_QualityMetamodel_IntegerValueType_ValueType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)