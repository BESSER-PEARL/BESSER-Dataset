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
DatabaseTypeType: Enumeration = Enumeration(
    name="DatabaseTypeType",
    literals={
            EnumerationLiteral(name="Oracle"),
			EnumerationLiteral(name="Postgres")
    }
)

KindHintType: Enumeration = Enumeration(
    name="KindHintType",
    literals={
            EnumerationLiteral(name="BH"),
			EnumerationLiteral(name="AVG")
    }
)

MetricRetentionPeriod: Enumeration = Enumeration(
    name="MetricRetentionPeriod",
    literals={
            EnumerationLiteral(name="Always"),
			EnumerationLiteral(name="OneYear"),
			EnumerationLiteral(name="OneMonth"),
			EnumerationLiteral(name="OneWeek")
    }
)

ObjectKindType: Enumeration = Enumeration(
    name="ObjectKindType",
    literals={
            EnumerationLiteral(name="NODE"),
			EnumerationLiteral(name="EQUIPMENT"),
			EnumerationLiteral(name="FUNCTION"),
			EnumerationLiteral(name="RELATIONSHIP")
    }
)

ValueKindType: Enumeration = Enumeration(
    name="ValueKindType",
    literals={
            EnumerationLiteral(name="INTERVAL"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="METRIC")
    }
)

# Classes
metrics_DataKind = Class(name="metrics::DataKind")
metrics_IdentifierDataKind = Class(name="metrics::IdentifierDataKind")
DataKind = Class(name="DataKind")
metrics_Mapping = Class(name="metrics::Mapping")
Base = Class(name="Base")
metrics_MappingColumn = Class(name="metrics::MappingColumn")
metrics_MappingRecord = Class(name="metrics::MappingRecord")
metrics_MappingCSV = Class(name="metrics::MappingCSV")
Mapping = Class(name="Mapping")
metrics_MappingRDBMS = Class(name="metrics::MappingRDBMS")
metrics_MappingStatistic = Class(name="metrics::MappingStatistic")
metrics_DateTimeRange = Class(name="metrics::DateTimeRange")
metrics_MetricSource = Class(name="metrics::MetricSource")
metrics_Unit = Class(name="metrics::Unit")
metrics_MappingXLS = Class(name="metrics::MappingXLS")
metrics_Metric = Class(name="metrics::Metric")
metrics_Expression = Class(name="metrics::Expression")
metrics_MetricRetentionRules = Class(name="metrics::MetricRetentionRules")
metrics_MetricRetentionRule = Class(name="metrics::MetricRetentionRule")
metrics_ValueDataKind = Class(name="metrics::ValueDataKind")
metrics_MetricValueRange = Class(name="metrics::MetricValueRange")
metrics_Value = Class(name="metrics::Value")

# metrics_DataKind class attributes and methods

# metrics_IdentifierDataKind class attributes and methods
metrics_IdentifierDataKind_objectKind: Property = Property(name="objectKind", type=StringType)
metrics_IdentifierDataKind_objectProperty: Property = Property(name="objectProperty", type=StringType)
metrics_IdentifierDataKind_pattern: Property = Property(name="pattern", type=StringType)
metrics_IdentifierDataKind.attributes={metrics_IdentifierDataKind_objectKind, metrics_IdentifierDataKind_objectProperty, metrics_IdentifierDataKind_pattern}

# DataKind class attributes and methods

# metrics_Mapping class attributes and methods
metrics_Mapping_firstDataRow: Property = Property(name="firstDataRow", type=StringType)
metrics_Mapping_headerRow: Property = Property(name="headerRow", type=StringType)
metrics_Mapping_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_Mapping.attributes={metrics_Mapping_firstDataRow, metrics_Mapping_headerRow, metrics_Mapping_intervalHint}

# Base class attributes and methods

# metrics_MappingColumn class attributes and methods
metrics_MappingColumn_column: Property = Property(name="column", type=StringType)
metrics_MappingColumn.attributes={metrics_MappingColumn_column}

# metrics_MappingRecord class attributes and methods
metrics_MappingRecord_column: Property = Property(name="column", type=StringType)
metrics_MappingRecord_count: Property = Property(name="count", type=StringType)
metrics_MappingRecord_message: Property = Property(name="message", type=StringType)
metrics_MappingRecord.attributes={metrics_MappingRecord_column, metrics_MappingRecord_message, metrics_MappingRecord_count}

# metrics_MappingCSV class attributes and methods
metrics_MappingCSV_delimiter: Property = Property(name="delimiter", type=StringType)
metrics_MappingCSV_filterPattern: Property = Property(name="filterPattern", type=StringType)
metrics_MappingCSV.attributes={metrics_MappingCSV_filterPattern, metrics_MappingCSV_delimiter}

# Mapping class attributes and methods

# metrics_MappingRDBMS class attributes and methods
metrics_MappingRDBMS_dateTimeFormat: Property = Property(name="dateTimeFormat", type=StringType)
metrics_MappingRDBMS_password: Property = Property(name="password", type=StringType)
metrics_MappingRDBMS_query: Property = Property(name="query", type=StringType)
metrics_MappingRDBMS_timeFormat: Property = Property(name="timeFormat", type=StringType)
metrics_MappingRDBMS_user: Property = Property(name="user", type=StringType)
metrics_MappingRDBMS_databaseType: Property = Property(name="databaseType", type=StringType)
metrics_MappingRDBMS_dateFormat: Property = Property(name="dateFormat", type=StringType)
metrics_MappingRDBMS.attributes={metrics_MappingRDBMS_query, metrics_MappingRDBMS_user, metrics_MappingRDBMS_databaseType, metrics_MappingRDBMS_dateTimeFormat, metrics_MappingRDBMS_dateFormat, metrics_MappingRDBMS_timeFormat, metrics_MappingRDBMS_password}

# metrics_MappingStatistic class attributes and methods
metrics_MappingStatistic_intervalEstimate: Property = Property(name="intervalEstimate", type=StringType)
metrics_MappingStatistic_message: Property = Property(name="message", type=StringType)
metrics_MappingStatistic_totalRecords: Property = Property(name="totalRecords", type=StringType)
metrics_MappingStatistic.attributes={metrics_MappingStatistic_message, metrics_MappingStatistic_intervalEstimate, metrics_MappingStatistic_totalRecords}

# metrics_DateTimeRange class attributes and methods

# metrics_MetricSource class attributes and methods
metrics_MetricSource_filterPattern: Property = Property(name="filterPattern", type=StringType)
metrics_MetricSource_metricLocation: Property = Property(name="metricLocation", type=StringType)
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_filterPattern, metrics_MetricSource_metricLocation, metrics_MetricSource_name}

# metrics_Unit class attributes and methods

# metrics_MappingXLS class attributes and methods
metrics_MappingXLS_filterPattern: Property = Property(name="filterPattern", type=StringType)
metrics_MappingXLS_sheetNumber: Property = Property(name="sheetNumber", type=StringType)
metrics_MappingXLS.attributes={metrics_MappingXLS_filterPattern, metrics_MappingXLS_sheetNumber}

# metrics_Metric class attributes and methods
metrics_Metric_description: Property = Property(name="description", type=StringType)
metrics_Metric_measurementKind: Property = Property(name="measurementKind", type=StringType)
metrics_Metric_measurementPoint: Property = Property(name="measurementPoint", type=StringType)
metrics_Metric_name: Property = Property(name="name", type=StringType)
metrics_Metric.attributes={metrics_Metric_measurementPoint, metrics_Metric_measurementKind, metrics_Metric_description, metrics_Metric_name}

# metrics_Expression class attributes and methods

# metrics_MetricRetentionRules class attributes and methods

# metrics_MetricRetentionRule class attributes and methods
metrics_MetricRetentionRule_period: Property = Property(name="period", type=StringType)
metrics_MetricRetentionRule_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_MetricRetentionRule_name: Property = Property(name="name", type=StringType)
metrics_MetricRetentionRule.attributes={metrics_MetricRetentionRule_name, metrics_MetricRetentionRule_period, metrics_MetricRetentionRule_intervalHint}

# metrics_ValueDataKind class attributes and methods
metrics_ValueDataKind_format: Property = Property(name="format", type=StringType)
metrics_ValueDataKind_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_ValueDataKind_valueKind: Property = Property(name="valueKind", type=StringType)
metrics_ValueDataKind.attributes={metrics_ValueDataKind_valueKind, metrics_ValueDataKind_format, metrics_ValueDataKind_kindHint}

# metrics_MetricValueRange class attributes and methods
metrics_MetricValueRange_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_MetricValueRange_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_MetricValueRange.attributes={metrics_MetricValueRange_kindHint, metrics_MetricValueRange_intervalHint}

# metrics_Value class attributes and methods

# Relationships
dataType4: BinaryAssociation = BinaryAssociation(
    name="dataType4",
    ends={
        Property(name="metrics_DataKind", type=metrics_MappingColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingColumn5", type=metrics_DataKind, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headerMappingColumns0: BinaryAssociation = BinaryAssociation(
    name="headerMappingColumns0",
    ends={
        Property(name="metrics_MappingColumn", type=metrics_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Mapping", type=metrics_MappingColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataMappingColumns1: BinaryAssociation = BinaryAssociation(
    name="dataMappingColumns1",
    ends={
        Property(name="metrics_MappingColumn3", type=metrics_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Mapping2", type=metrics_MappingColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
periodEstimate9: BinaryAssociation = BinaryAssociation(
    name="periodEstimate9",
    ends={
        Property(name="metrics_DateTimeRange11", type=metrics_MappingStatistic, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingStatistic10", type=metrics_DateTimeRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subStatistics13: BinaryAssociation = BinaryAssociation(
    name="subStatistics13",
    ends={
        Property(name="metrics_MappingStatistic14", type=metrics_MappingStatistic, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingStatistic12", type=metrics_MappingStatistic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failedRecords6: BinaryAssociation = BinaryAssociation(
    name="failedRecords6",
    ends={
        Property(name="metrics_MappingRecord", type=metrics_MappingStatistic, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingStatistic", type=metrics_MappingRecord, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingDuration7: BinaryAssociation = BinaryAssociation(
    name="mappingDuration7",
    ends={
        Property(name="metrics_DateTimeRange", type=metrics_MappingStatistic, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingStatistic8", type=metrics_DateTimeRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metricSourceRef19: BinaryAssociation = BinaryAssociation(
    name="metricSourceRef19",
    ends={
        Property(name="metrics_MetricSource", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric20", type=metrics_MetricSource, multiplicity=Multiplicity(0, 1))
    }
)
unitRef21: BinaryAssociation = BinaryAssociation(
    name="unitRef21",
    ends={
        Property(name="metrics_Unit", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric22", type=metrics_Unit, multiplicity=Multiplicity(0, 1))
    }
)
metrics16: BinaryAssociation = BinaryAssociation(
    name="metrics16",
    ends={
        Property(name="metrics_Metric", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric15", type=metrics_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRef17: BinaryAssociation = BinaryAssociation(
    name="expressionRef17",
    ends={
        Property(name="metrics_Expression", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric18", type=metrics_Expression, multiplicity=Multiplicity(0, 1))
    }
)
metricRetentionRules25: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRules25",
    ends={
        Property(name="metrics_MetricRetentionRule26", type=metrics_MetricRetentionRules, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricRetentionRules", type=metrics_MetricRetentionRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricMapping27: BinaryAssociation = BinaryAssociation(
    name="metricMapping27",
    ends={
        Property(name="metrics_Mapping29", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource28", type=metrics_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statistics30: BinaryAssociation = BinaryAssociation(
    name="statistics30",
    ends={
        Property(name="metrics_MappingStatistic32", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource31", type=metrics_MappingStatistic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
retentionExpression23: BinaryAssociation = BinaryAssociation(
    name="retentionExpression23",
    ends={
        Property(name="metrics_Expression24", type=metrics_MetricRetentionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricRetentionRule", type=metrics_Expression, multiplicity=Multiplicity(0, 1))
    }
)
metricRef34: BinaryAssociation = BinaryAssociation(
    name="metricRef34",
    ends={
        Property(name="metrics_Metric35", type=metrics_ValueDataKind, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_ValueDataKind", type=metrics_Metric, multiplicity=Multiplicity(0, 1))
    }
)
metricValues33: BinaryAssociation = BinaryAssociation(
    name="metricValues33",
    ends={
        Property(name="metrics_Value", type=metrics_MetricValueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricValueRange", type=metrics_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metrics_IdentifierDataKind_DataKind = Generalization(general=DataKind, specific=metrics_IdentifierDataKind)
gen_metrics_MappingColumn_Base = Generalization(general=Base, specific=metrics_MappingColumn)
gen_metrics_Mapping_Base = Generalization(general=Base, specific=metrics_Mapping)
gen_metrics_MappingRecord_Base = Generalization(general=Base, specific=metrics_MappingRecord)
gen_metrics_MappingCSV_Mapping = Generalization(general=Mapping, specific=metrics_MappingCSV)
gen_metrics_MappingRDBMS_Mapping = Generalization(general=Mapping, specific=metrics_MappingRDBMS)
gen_metrics_MappingStatistic_Base = Generalization(general=Base, specific=metrics_MappingStatistic)
gen_metrics_MappingXLS_Mapping = Generalization(general=Mapping, specific=metrics_MappingXLS)
gen_metrics_Metric_Base = Generalization(general=Base, specific=metrics_Metric)
gen_metrics_MetricSource_Base = Generalization(general=Base, specific=metrics_MetricSource)
gen_metrics_ValueDataKind_DataKind = Generalization(general=DataKind, specific=metrics_ValueDataKind)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_DataKind, metrics_IdentifierDataKind, DataKind, metrics_Mapping, Base, metrics_MappingColumn, metrics_MappingRecord, metrics_MappingCSV, Mapping, metrics_MappingRDBMS, metrics_MappingStatistic, metrics_DateTimeRange, metrics_MetricSource, metrics_Unit, metrics_MappingXLS, metrics_Metric, metrics_Expression, metrics_MetricRetentionRules, metrics_MetricRetentionRule, metrics_ValueDataKind, metrics_MetricValueRange, metrics_Value, DatabaseTypeType, KindHintType, MetricRetentionPeriod, ObjectKindType, ValueKindType},
    associations={dataType4, headerMappingColumns0, dataMappingColumns1, periodEstimate9, subStatistics13, failedRecords6, mappingDuration7, metricSourceRef19, unitRef21, metrics16, expressionRef17, metricRetentionRules25, metricMapping27, statistics30, retentionExpression23, metricRef34, metricValues33},
    generalizations={gen_metrics_IdentifierDataKind_DataKind, gen_metrics_MappingColumn_Base, gen_metrics_Mapping_Base, gen_metrics_MappingRecord_Base, gen_metrics_MappingCSV_Mapping, gen_metrics_MappingRDBMS_Mapping, gen_metrics_MappingStatistic_Base, gen_metrics_MappingXLS_Mapping, gen_metrics_Metric_Base, gen_metrics_MetricSource_Base, gen_metrics_ValueDataKind_DataKind},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)