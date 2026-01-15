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
            EnumerationLiteral(name="PERIOD"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="METRIC")
    }
)

# Classes
metrics_DataKind = Class(name="metrics::DataKind")
metrics_IdentifierDataKind = Class(name="metrics::IdentifierDataKind")
metrics_Mapping = Class(name="metrics::Mapping")
metrics_MappingCSV = Class(name="metrics::MappingCSV")
Mapping = Class(name="Mapping")
metrics_MappingRDBMS = Class(name="metrics::MappingRDBMS")
metrics_MappingRecord = Class(name="metrics::MappingRecord")
metrics_MappingRecordXLS = Class(name="metrics::MappingRecordXLS")
MappingRecord = Class(name="MappingRecord")
DataKind = Class(name="DataKind")
metrics_MappingStatistic = Class(name="metrics::MappingStatistic")
metrics_DateTimeRange = Class(name="metrics::DateTimeRange")
metrics_MappingXLS = Class(name="metrics::MappingXLS")
metrics_MappingXLSColumn = Class(name="metrics::MappingXLSColumn")
metrics_Metric = Class(name="metrics::Metric")
metrics_MetricSource = Class(name="metrics::MetricSource")
metrics_Unit = Class(name="metrics::Unit")
metrics_MetricValueRange = Class(name="metrics::MetricValueRange")
metrics_Value = Class(name="metrics::Value")
metrics_ValueDataKind = Class(name="metrics::ValueDataKind")

# metrics_DataKind class attributes and methods

# metrics_IdentifierDataKind class attributes and methods
metrics_IdentifierDataKind_objectKind: Property = Property(name="objectKind", type=StringType)
metrics_IdentifierDataKind_objectProperty: Property = Property(name="objectProperty", type=StringType)
metrics_IdentifierDataKind.attributes={metrics_IdentifierDataKind_objectProperty, metrics_IdentifierDataKind_objectKind}

# metrics_Mapping class attributes and methods

# metrics_MappingCSV class attributes and methods

# Mapping class attributes and methods

# metrics_MappingRDBMS class attributes and methods

# metrics_MappingRecord class attributes and methods
metrics_MappingRecord_message: Property = Property(name="message", type=StringType)
metrics_MappingRecord.attributes={metrics_MappingRecord_message}

# metrics_MappingRecordXLS class attributes and methods
metrics_MappingRecordXLS_column: Property = Property(name="column", type=StringType)
metrics_MappingRecordXLS_row: Property = Property(name="row", type=StringType)
metrics_MappingRecordXLS.attributes={metrics_MappingRecordXLS_column, metrics_MappingRecordXLS_row}

# MappingRecord class attributes and methods

# DataKind class attributes and methods

# metrics_MappingStatistic class attributes and methods
metrics_MappingStatistic_message: Property = Property(name="message", type=StringType)
metrics_MappingStatistic_totalRecords: Property = Property(name="totalRecords", type=StringType)
metrics_MappingStatistic.attributes={metrics_MappingStatistic_totalRecords, metrics_MappingStatistic_message}

# metrics_DateTimeRange class attributes and methods

# metrics_MappingXLS class attributes and methods
metrics_MappingXLS_firstDataRow: Property = Property(name="firstDataRow", type=StringType)
metrics_MappingXLS_headerRow: Property = Property(name="headerRow", type=StringType)
metrics_MappingXLS_sheetNumber: Property = Property(name="sheetNumber", type=StringType)
metrics_MappingXLS.attributes={metrics_MappingXLS_headerRow, metrics_MappingXLS_firstDataRow, metrics_MappingXLS_sheetNumber}

# metrics_MappingXLSColumn class attributes and methods
metrics_MappingXLSColumn_column: Property = Property(name="column", type=StringType)
metrics_MappingXLSColumn.attributes={metrics_MappingXLSColumn_column}

# metrics_Metric class attributes and methods
metrics_Metric_description: Property = Property(name="description", type=StringType)
metrics_Metric_measurementKind: Property = Property(name="measurementKind", type=StringType)
metrics_Metric_measurementPoint: Property = Property(name="measurementPoint", type=StringType)
metrics_Metric_metricCalculation: Property = Property(name="metricCalculation", type=StringType)
metrics_Metric_name: Property = Property(name="name", type=StringType)
metrics_Metric.attributes={metrics_Metric_name, metrics_Metric_measurementPoint, metrics_Metric_description, metrics_Metric_measurementKind, metrics_Metric_metricCalculation}

# metrics_MetricSource class attributes and methods
metrics_MetricSource_metricLocation: Property = Property(name="metricLocation", type=StringType)
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_name, metrics_MetricSource_metricLocation}

# metrics_Unit class attributes and methods

# metrics_MetricValueRange class attributes and methods
metrics_MetricValueRange_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_MetricValueRange_periodHint: Property = Property(name="periodHint", type=StringType)
metrics_MetricValueRange.attributes={metrics_MetricValueRange_kindHint, metrics_MetricValueRange_periodHint}

# metrics_Value class attributes and methods

# metrics_ValueDataKind class attributes and methods
metrics_ValueDataKind_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_ValueDataKind_valueKind: Property = Property(name="valueKind", type=StringType)
metrics_ValueDataKind.attributes={metrics_ValueDataKind_kindHint, metrics_ValueDataKind_valueKind}

# Relationships
failedRecords0: BinaryAssociation = BinaryAssociation(
    name="failedRecords0",
    ends={
        Property(name="metrics_MappingRecord", type=metrics_MappingStatistic, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingStatistic", type=metrics_MappingRecord, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingDuration1: BinaryAssociation = BinaryAssociation(
    name="mappingDuration1",
    ends={
        Property(name="metrics_DateTimeRange", type=metrics_MappingStatistic, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingStatistic2", type=metrics_DateTimeRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappingColumns3: BinaryAssociation = BinaryAssociation(
    name="mappingColumns3",
    ends={
        Property(name="metrics_MappingXLSColumn", type=metrics_MappingXLS, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingXLS", type=metrics_MappingXLSColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType4: BinaryAssociation = BinaryAssociation(
    name="dataType4",
    ends={
        Property(name="metrics_DataKind", type=metrics_MappingXLSColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingXLSColumn5", type=metrics_DataKind, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metrics7: BinaryAssociation = BinaryAssociation(
    name="metrics7",
    ends={
        Property(name="metrics_Metric", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric6", type=metrics_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSourceRef8: BinaryAssociation = BinaryAssociation(
    name="metricSourceRef8",
    ends={
        Property(name="MetricSource", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricRefs", type=metrics_MetricSource, multiplicity=Multiplicity(0, 1))
    }
)
unitRef9: BinaryAssociation = BinaryAssociation(
    name="unitRef9",
    ends={
        Property(name="metrics_Unit", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric10", type=metrics_Unit, multiplicity=Multiplicity(0, 1))
    }
)
metricRefs11: BinaryAssociation = BinaryAssociation(
    name="metricRefs11",
    ends={
        Property(name="Metric", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metricSourceRef", type=metrics_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
metricMapping12: BinaryAssociation = BinaryAssociation(
    name="metricMapping12",
    ends={
        Property(name="metrics_Mapping", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource", type=metrics_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statistics13: BinaryAssociation = BinaryAssociation(
    name="statistics13",
    ends={
        Property(name="metrics_MappingStatistic15", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource14", type=metrics_MappingStatistic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricValues16: BinaryAssociation = BinaryAssociation(
    name="metricValues16",
    ends={
        Property(name="metrics_Value", type=metrics_MetricValueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricValueRange", type=metrics_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricRef17: BinaryAssociation = BinaryAssociation(
    name="metricRef17",
    ends={
        Property(name="metrics_Metric18", type=metrics_ValueDataKind, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_ValueDataKind", type=metrics_Metric, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_metrics_MappingCSV_Mapping = Generalization(general=Mapping, specific=metrics_MappingCSV)
gen_metrics_MappingRDBMS_Mapping = Generalization(general=Mapping, specific=metrics_MappingRDBMS)
gen_metrics_MappingRecordXLS_MappingRecord = Generalization(general=MappingRecord, specific=metrics_MappingRecordXLS)
gen_metrics_IdentifierDataKind_DataKind = Generalization(general=DataKind, specific=metrics_IdentifierDataKind)
gen_metrics_MappingXLS_Mapping = Generalization(general=Mapping, specific=metrics_MappingXLS)
gen_metrics_ValueDataKind_DataKind = Generalization(general=DataKind, specific=metrics_ValueDataKind)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_DataKind, metrics_IdentifierDataKind, metrics_Mapping, metrics_MappingCSV, Mapping, metrics_MappingRDBMS, metrics_MappingRecord, metrics_MappingRecordXLS, MappingRecord, DataKind, metrics_MappingStatistic, metrics_DateTimeRange, metrics_MappingXLS, metrics_MappingXLSColumn, metrics_Metric, metrics_MetricSource, metrics_Unit, metrics_MetricValueRange, metrics_Value, metrics_ValueDataKind, KindHintType, ObjectKindType, ValueKindType},
    associations={failedRecords0, mappingDuration1, mappingColumns3, dataType4, metrics7, metricSourceRef8, unitRef9, metricRefs11, metricMapping12, statistics13, metricValues16, metricRef17},
    generalizations={gen_metrics_MappingCSV_Mapping, gen_metrics_MappingRDBMS_Mapping, gen_metrics_MappingRecordXLS_MappingRecord, gen_metrics_IdentifierDataKind_DataKind, gen_metrics_MappingXLS_Mapping, gen_metrics_ValueDataKind_DataKind},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)