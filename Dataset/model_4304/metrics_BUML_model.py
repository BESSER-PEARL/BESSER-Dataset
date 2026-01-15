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

FixedMetricRetentionPeriod: Enumeration = Enumeration(
    name="FixedMetricRetentionPeriod",
    literals={
            EnumerationLiteral(name="Always"),
			EnumerationLiteral(name="OneYear"),
			EnumerationLiteral(name="OneMonth"),
			EnumerationLiteral(name="OneWeek")
    }
)

KindHintType: Enumeration = Enumeration(
    name="KindHintType",
    literals={
            EnumerationLiteral(name="BH"),
			EnumerationLiteral(name="AVG")
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
metrics_MappingCSV = Class(name="metrics::MappingCSV")
Mapping = Class(name="Mapping")
metrics_MappingColumn = Class(name="metrics::MappingColumn")
metrics_MappingRecord = Class(name="metrics::MappingRecord")
metrics_MappingExternal = Class(name="metrics::MappingExternal")
metrics_MappingRDBMS = Class(name="metrics::MappingRDBMS")
metrics_MappingXLS = Class(name="metrics::MappingXLS")
metrics_MappingStatistic = Class(name="metrics::MappingStatistic")
metrics_DateTimeRange = Class(name="metrics::DateTimeRange")
metrics_MetricSource = Class(name="metrics::MetricSource")
metrics_Unit = Class(name="metrics::Unit")
metrics_MetricAggregationRule = Class(name="metrics::MetricAggregationRule")
Rule = Class(name="Rule")
metrics_Metric = Class(name="metrics::Metric")
metrics_Expression = Class(name="metrics::Expression")
metrics_MetricRetentionRule = Class(name="metrics::MetricRetentionRule")
metrics_MetricRetentionRules = Class(name="metrics::MetricRetentionRules")
metrics_MetricAggregationRules = Class(name="metrics::MetricAggregationRules")
metrics_MetricRetentionPeriods = Class(name="metrics::MetricRetentionPeriods")
metrics_MetricValueRange = Class(name="metrics::MetricValueRange")
metrics_Value = Class(name="metrics::Value")
metrics_RuleSet = Class(name="metrics::RuleSet")
metrics_ValueDataKind = Class(name="metrics::ValueDataKind")

# metrics_DataKind class attributes and methods

# metrics_IdentifierDataKind class attributes and methods
metrics_IdentifierDataKind_objectKind: Property = Property(name="objectKind", type=StringType)
metrics_IdentifierDataKind_pattern: Property = Property(name="pattern", type=StringType)
metrics_IdentifierDataKind_objectProperty: Property = Property(name="objectProperty", type=StringType)
metrics_IdentifierDataKind.attributes={metrics_IdentifierDataKind_pattern, metrics_IdentifierDataKind_objectProperty, metrics_IdentifierDataKind_objectKind}

# DataKind class attributes and methods

# metrics_Mapping class attributes and methods
metrics_Mapping_headerRow: Property = Property(name="headerRow", type=StringType)
metrics_Mapping_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_Mapping_firstDataRow: Property = Property(name="firstDataRow", type=StringType)
metrics_Mapping.attributes={metrics_Mapping_intervalHint, metrics_Mapping_headerRow, metrics_Mapping_firstDataRow}

# Base class attributes and methods

# metrics_MappingCSV class attributes and methods
metrics_MappingCSV_delimiter: Property = Property(name="delimiter", type=StringType)
metrics_MappingCSV_filterPattern: Property = Property(name="filterPattern", type=StringType)
metrics_MappingCSV.attributes={metrics_MappingCSV_delimiter, metrics_MappingCSV_filterPattern}

# Mapping class attributes and methods

# metrics_MappingColumn class attributes and methods
metrics_MappingColumn_column: Property = Property(name="column", type=StringType)
metrics_MappingColumn.attributes={metrics_MappingColumn_column}

# metrics_MappingRecord class attributes and methods
metrics_MappingRecord_column: Property = Property(name="column", type=StringType)
metrics_MappingRecord_count: Property = Property(name="count", type=StringType)
metrics_MappingRecord_message: Property = Property(name="message", type=StringType)
metrics_MappingRecord.attributes={metrics_MappingRecord_column, metrics_MappingRecord_count, metrics_MappingRecord_message}

# metrics_MappingExternal class attributes and methods
metrics_MappingExternal_classURI: Property = Property(name="classURI", type=StringType)
metrics_MappingExternal_pluginID: Property = Property(name="pluginID", type=StringType)
metrics_MappingExternal.attributes={metrics_MappingExternal_classURI, metrics_MappingExternal_pluginID}

# metrics_MappingRDBMS class attributes and methods
metrics_MappingRDBMS_dateFormat: Property = Property(name="dateFormat", type=StringType)
metrics_MappingRDBMS_dateTimeFormat: Property = Property(name="dateTimeFormat", type=StringType)
metrics_MappingRDBMS_password: Property = Property(name="password", type=StringType)
metrics_MappingRDBMS_query: Property = Property(name="query", type=StringType)
metrics_MappingRDBMS_timeFormat: Property = Property(name="timeFormat", type=StringType)
metrics_MappingRDBMS_user: Property = Property(name="user", type=StringType)
metrics_MappingRDBMS_databaseType: Property = Property(name="databaseType", type=StringType)
metrics_MappingRDBMS.attributes={metrics_MappingRDBMS_timeFormat, metrics_MappingRDBMS_user, metrics_MappingRDBMS_dateTimeFormat, metrics_MappingRDBMS_query, metrics_MappingRDBMS_password, metrics_MappingRDBMS_dateFormat, metrics_MappingRDBMS_databaseType}

# metrics_MappingXLS class attributes and methods
metrics_MappingXLS_filterPattern: Property = Property(name="filterPattern", type=StringType)
metrics_MappingXLS_sheetNumber: Property = Property(name="sheetNumber", type=StringType)
metrics_MappingXLS.attributes={metrics_MappingXLS_filterPattern, metrics_MappingXLS_sheetNumber}

# metrics_MappingStatistic class attributes and methods
metrics_MappingStatistic_intervalEstimate: Property = Property(name="intervalEstimate", type=StringType)
metrics_MappingStatistic_message: Property = Property(name="message", type=StringType)
metrics_MappingStatistic_totalRecords: Property = Property(name="totalRecords", type=StringType)
metrics_MappingStatistic.attributes={metrics_MappingStatistic_intervalEstimate, metrics_MappingStatistic_message, metrics_MappingStatistic_totalRecords}

# metrics_DateTimeRange class attributes and methods

# metrics_MetricSource class attributes and methods
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource_filterPattern: Property = Property(name="filterPattern", type=StringType)
metrics_MetricSource_metricLocation: Property = Property(name="metricLocation", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_name, metrics_MetricSource_metricLocation, metrics_MetricSource_filterPattern}

# metrics_Unit class attributes and methods

# metrics_MetricAggregationRule class attributes and methods

# Rule class attributes and methods

# metrics_Metric class attributes and methods
metrics_Metric_measurementKind: Property = Property(name="measurementKind", type=StringType)
metrics_Metric_measurementPoint: Property = Property(name="measurementPoint", type=StringType)
metrics_Metric_name: Property = Property(name="name", type=StringType)
metrics_Metric_description: Property = Property(name="description", type=StringType)
metrics_Metric.attributes={metrics_Metric_description, metrics_Metric_name, metrics_Metric_measurementKind, metrics_Metric_measurementPoint}

# metrics_Expression class attributes and methods

# metrics_MetricRetentionRule class attributes and methods
metrics_MetricRetentionRule_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_MetricRetentionRule_period: Property = Property(name="period", type=StringType)
metrics_MetricRetentionRule.attributes={metrics_MetricRetentionRule_intervalHint, metrics_MetricRetentionRule_period}

# metrics_MetricRetentionRules class attributes and methods

# metrics_MetricAggregationRules class attributes and methods

# metrics_MetricRetentionPeriods class attributes and methods
metrics_MetricRetentionPeriods_metricRetentionPeriods: Property = Property(name="metricRetentionPeriods", type=StringType)
metrics_MetricRetentionPeriods.attributes={metrics_MetricRetentionPeriods_metricRetentionPeriods}

# metrics_MetricValueRange class attributes and methods
metrics_MetricValueRange_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_MetricValueRange_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_MetricValueRange.attributes={metrics_MetricValueRange_kindHint, metrics_MetricValueRange_intervalHint}

# metrics_Value class attributes and methods

# metrics_RuleSet class attributes and methods

# metrics_ValueDataKind class attributes and methods
metrics_ValueDataKind_format: Property = Property(name="format", type=StringType)
metrics_ValueDataKind_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_ValueDataKind_valueKind: Property = Property(name="valueKind", type=StringType)
metrics_ValueDataKind.attributes={metrics_ValueDataKind_valueKind, metrics_ValueDataKind_kindHint, metrics_ValueDataKind_format}

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
aggregationExpression23: BinaryAssociation = BinaryAssociation(
    name="aggregationExpression23",
    ends={
        Property(name="metrics_Expression24", type=metrics_MetricAggregationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricAggregationRule", type=metrics_Expression, multiplicity=Multiplicity(0, 1))
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
metricRetentionRules27: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRules27",
    ends={
        Property(name="metrics_MetricRetentionRule", type=metrics_MetricRetentionRules, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricRetentionRules", type=metrics_MetricRetentionRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricMapping28: BinaryAssociation = BinaryAssociation(
    name="metricMapping28",
    ends={
        Property(name="metrics_Mapping30", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource29", type=metrics_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metricAggregationRules25: BinaryAssociation = BinaryAssociation(
    name="metricAggregationRules25",
    ends={
        Property(name="metrics_MetricAggregationRule26", type=metrics_MetricAggregationRules, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricAggregationRules", type=metrics_MetricAggregationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricValues39: BinaryAssociation = BinaryAssociation(
    name="metricValues39",
    ends={
        Property(name="metrics_Value", type=metrics_MetricValueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricValueRange", type=metrics_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statistics31: BinaryAssociation = BinaryAssociation(
    name="statistics31",
    ends={
        Property(name="metrics_MappingStatistic33", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource32", type=metrics_MappingStatistic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricAggregationRules34: BinaryAssociation = BinaryAssociation(
    name="metricAggregationRules34",
    ends={
        Property(name="metrics_RuleSet", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource35", type=metrics_RuleSet, multiplicity=Multiplicity(0, 1))
    }
)
metricRetentionRules36: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRules36",
    ends={
        Property(name="metrics_RuleSet38", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource37", type=metrics_RuleSet, multiplicity=Multiplicity(0, 1))
    }
)
metricRef40: BinaryAssociation = BinaryAssociation(
    name="metricRef40",
    ends={
        Property(name="metrics_Metric41", type=metrics_ValueDataKind, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_ValueDataKind", type=metrics_Metric, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_metrics_IdentifierDataKind_DataKind = Generalization(general=DataKind, specific=metrics_IdentifierDataKind)
gen_metrics_Mapping_Base = Generalization(general=Base, specific=metrics_Mapping)
gen_metrics_MappingColumn_Base = Generalization(general=Base, specific=metrics_MappingColumn)
gen_metrics_MappingCSV_Mapping = Generalization(general=Mapping, specific=metrics_MappingCSV)
gen_metrics_MappingRecord_Base = Generalization(general=Base, specific=metrics_MappingRecord)
gen_metrics_MappingExternal_Mapping = Generalization(general=Mapping, specific=metrics_MappingExternal)
gen_metrics_MappingRDBMS_Mapping = Generalization(general=Mapping, specific=metrics_MappingRDBMS)
gen_metrics_MappingXLS_Mapping = Generalization(general=Mapping, specific=metrics_MappingXLS)
gen_metrics_MappingStatistic_Base = Generalization(general=Base, specific=metrics_MappingStatistic)
gen_metrics_MetricAggregationRule_Rule = Generalization(general=Rule, specific=metrics_MetricAggregationRule)
gen_metrics_Metric_Base = Generalization(general=Base, specific=metrics_Metric)
gen_metrics_MetricRetentionRule_Rule = Generalization(general=Rule, specific=metrics_MetricRetentionRule)
gen_metrics_MetricSource_Base = Generalization(general=Base, specific=metrics_MetricSource)
gen_metrics_ValueDataKind_DataKind = Generalization(general=DataKind, specific=metrics_ValueDataKind)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_DataKind, metrics_IdentifierDataKind, DataKind, metrics_Mapping, Base, metrics_MappingCSV, Mapping, metrics_MappingColumn, metrics_MappingRecord, metrics_MappingExternal, metrics_MappingRDBMS, metrics_MappingXLS, metrics_MappingStatistic, metrics_DateTimeRange, metrics_MetricSource, metrics_Unit, metrics_MetricAggregationRule, Rule, metrics_Metric, metrics_Expression, metrics_MetricRetentionRule, metrics_MetricRetentionRules, metrics_MetricAggregationRules, metrics_MetricRetentionPeriods, metrics_MetricValueRange, metrics_Value, metrics_RuleSet, metrics_ValueDataKind, DatabaseTypeType, FixedMetricRetentionPeriod, KindHintType, ObjectKindType, ValueKindType},
    associations={dataType4, headerMappingColumns0, dataMappingColumns1, periodEstimate9, subStatistics13, failedRecords6, mappingDuration7, metricSourceRef19, unitRef21, aggregationExpression23, metrics16, expressionRef17, metricRetentionRules27, metricMapping28, metricAggregationRules25, metricValues39, statistics31, metricAggregationRules34, metricRetentionRules36, metricRef40},
    generalizations={gen_metrics_IdentifierDataKind_DataKind, gen_metrics_Mapping_Base, gen_metrics_MappingColumn_Base, gen_metrics_MappingCSV_Mapping, gen_metrics_MappingRecord_Base, gen_metrics_MappingExternal_Mapping, gen_metrics_MappingRDBMS_Mapping, gen_metrics_MappingXLS_Mapping, gen_metrics_MappingStatistic_Base, gen_metrics_MetricAggregationRule_Rule, gen_metrics_Metric_Base, gen_metrics_MetricRetentionRule_Rule, gen_metrics_MetricSource_Base, gen_metrics_ValueDataKind_DataKind},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)