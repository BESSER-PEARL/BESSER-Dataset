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

ObjectNameType: Enumeration = Enumeration(
    name="ObjectNameType",
    literals={
            EnumerationLiteral(name="NODE"),
			EnumerationLiteral(name="EQUIPMENT"),
			EnumerationLiteral(name="FUNCTION")
    }
)

ValueKindType: Enumeration = Enumeration(
    name="ValueKindType",
    literals={
            EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="METRIC")
    }
)

# Classes
metrics_Mapping = Class(name="metrics::Mapping")
metrics_MappingCSV = Class(name="metrics::MappingCSV")
Mapping = Class(name="Mapping")
metrics_MappingRDBMS = Class(name="metrics::MappingRDBMS")
metrics_MappingRecord = Class(name="metrics::MappingRecord")
metrics_DataKind = Class(name="metrics::DataKind")
metrics_IdentifierDataKind = Class(name="metrics::IdentifierDataKind")
DataKind = Class(name="DataKind")
metrics_DateTimeRange = Class(name="metrics::DateTimeRange")
metrics_MappingXLS = Class(name="metrics::MappingXLS")
metrics_MappingRecordXLS = Class(name="metrics::MappingRecordXLS")
MappingRecord = Class(name="MappingRecord")
metrics_MappingStatistic = Class(name="metrics::MappingStatistic")
metrics_MetricSource = Class(name="metrics::MetricSource")
metrics_Metric = Class(name="metrics::Metric")
metrics_MetricValueRange = Class(name="metrics::MetricValueRange")
metrics_Value = Class(name="metrics::Value")
metrics_ValueDataKind = Class(name="metrics::ValueDataKind")

# metrics_Mapping class attributes and methods

# metrics_MappingCSV class attributes and methods

# Mapping class attributes and methods

# metrics_MappingRDBMS class attributes and methods

# metrics_MappingRecord class attributes and methods

# metrics_DataKind class attributes and methods

# metrics_IdentifierDataKind class attributes and methods
metrics_IdentifierDataKind_objectAttribute: Property = Property(name="objectAttribute", type=StringType)
metrics_IdentifierDataKind_objectName: Property = Property(name="objectName", type=StringType)
metrics_IdentifierDataKind.attributes={metrics_IdentifierDataKind_objectAttribute, metrics_IdentifierDataKind_objectName}

# DataKind class attributes and methods

# metrics_DateTimeRange class attributes and methods

# metrics_MappingXLS class attributes and methods
metrics_MappingXLS_columnHeaders: Property = Property(name="columnHeaders", type=StringType)
metrics_MappingXLS_firstDataRow: Property = Property(name="firstDataRow", type=StringType)
metrics_MappingXLS_headerRow: Property = Property(name="headerRow", type=StringType)
metrics_MappingXLS_sheetNumber: Property = Property(name="sheetNumber", type=StringType)
metrics_MappingXLS.attributes={metrics_MappingXLS_sheetNumber, metrics_MappingXLS_headerRow, metrics_MappingXLS_firstDataRow, metrics_MappingXLS_columnHeaders}

# metrics_MappingRecordXLS class attributes and methods
metrics_MappingRecordXLS_column: Property = Property(name="column", type=StringType)
metrics_MappingRecordXLS_row: Property = Property(name="row", type=StringType)
metrics_MappingRecordXLS.attributes={metrics_MappingRecordXLS_column, metrics_MappingRecordXLS_row}

# MappingRecord class attributes and methods

# metrics_MappingStatistic class attributes and methods
metrics_MappingStatistic_totalRecords: Property = Property(name="totalRecords", type=StringType)
metrics_MappingStatistic.attributes={metrics_MappingStatistic_totalRecords}

# metrics_MetricSource class attributes and methods
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource_metricLocation: Property = Property(name="metricLocation", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_metricLocation, metrics_MetricSource_name}

# metrics_Metric class attributes and methods
metrics_Metric_description: Property = Property(name="description", type=StringType)
metrics_Metric_measurementKind: Property = Property(name="measurementKind", type=StringType)
metrics_Metric_measurementPoint: Property = Property(name="measurementPoint", type=StringType)
metrics_Metric_metricCalculation: Property = Property(name="metricCalculation", type=StringType)
metrics_Metric_name: Property = Property(name="name", type=StringType)
metrics_Metric_unitRef: Property = Property(name="unitRef", type=StringType)
metrics_Metric.attributes={metrics_Metric_name, metrics_Metric_metricCalculation, metrics_Metric_measurementPoint, metrics_Metric_description, metrics_Metric_unitRef, metrics_Metric_measurementKind}

# metrics_MetricValueRange class attributes and methods
metrics_MetricValueRange_kindHint: Property = Property(name="kindHint", type=StringType)
metrics_MetricValueRange_name: Property = Property(name="name", type=StringType)
metrics_MetricValueRange_periodHint: Property = Property(name="periodHint", type=StringType)
metrics_MetricValueRange.attributes={metrics_MetricValueRange_kindHint, metrics_MetricValueRange_periodHint, metrics_MetricValueRange_name}

# metrics_Value class attributes and methods

# metrics_ValueDataKind class attributes and methods
metrics_ValueDataKind_valueKind: Property = Property(name="valueKind", type=StringType)
metrics_ValueDataKind.attributes={metrics_ValueDataKind_valueKind}

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
columnDataKind3: BinaryAssociation = BinaryAssociation(
    name="columnDataKind3",
    ends={
        Property(name="metrics_DataKind", type=metrics_MappingXLS, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MappingXLS", type=metrics_DataKind, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSourceRef6: BinaryAssociation = BinaryAssociation(
    name="metricSourceRef6",
    ends={
        Property(name="MetricSource", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricRefs", type=metrics_MetricSource, multiplicity=Multiplicity(0, 1))
    }
)
metrics5: BinaryAssociation = BinaryAssociation(
    name="metrics5",
    ends={
        Property(name="metrics_Metric", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric4", type=metrics_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricValues12: BinaryAssociation = BinaryAssociation(
    name="metricValues12",
    ends={
        Property(name="metrics_Value", type=metrics_MetricValueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricValueRange", type=metrics_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricRefs7: BinaryAssociation = BinaryAssociation(
    name="metricRefs7",
    ends={
        Property(name="Metric", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metricSourceRef", type=metrics_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
metricMapping8: BinaryAssociation = BinaryAssociation(
    name="metricMapping8",
    ends={
        Property(name="metrics_Mapping", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource", type=metrics_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statistics9: BinaryAssociation = BinaryAssociation(
    name="statistics9",
    ends={
        Property(name="metrics_MappingStatistic11", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource10", type=metrics_MappingStatistic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metrics_MappingCSV_Mapping = Generalization(general=Mapping, specific=metrics_MappingCSV)
gen_metrics_MappingRDBMS_Mapping = Generalization(general=Mapping, specific=metrics_MappingRDBMS)
gen_metrics_IdentifierDataKind_DataKind = Generalization(general=DataKind, specific=metrics_IdentifierDataKind)
gen_metrics_MappingXLS_Mapping = Generalization(general=Mapping, specific=metrics_MappingXLS)
gen_metrics_MappingRecordXLS_MappingRecord = Generalization(general=MappingRecord, specific=metrics_MappingRecordXLS)
gen_metrics_ValueDataKind_DataKind = Generalization(general=DataKind, specific=metrics_ValueDataKind)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_Mapping, metrics_MappingCSV, Mapping, metrics_MappingRDBMS, metrics_MappingRecord, metrics_DataKind, metrics_IdentifierDataKind, DataKind, metrics_DateTimeRange, metrics_MappingXLS, metrics_MappingRecordXLS, MappingRecord, metrics_MappingStatistic, metrics_MetricSource, metrics_Metric, metrics_MetricValueRange, metrics_Value, metrics_ValueDataKind, KindHintType, ObjectNameType, ValueKindType},
    associations={failedRecords0, mappingDuration1, columnDataKind3, metricSourceRef6, metrics5, metricValues12, metricRefs7, metricMapping8, statistics9},
    generalizations={gen_metrics_MappingCSV_Mapping, gen_metrics_MappingRDBMS_Mapping, gen_metrics_IdentifierDataKind_DataKind, gen_metrics_MappingXLS_Mapping, gen_metrics_MappingRecordXLS_MappingRecord, gen_metrics_ValueDataKind_DataKind},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)