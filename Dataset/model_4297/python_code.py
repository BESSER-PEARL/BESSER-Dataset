from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectNameType(Enum):
    NODE = "NODE"
    EQUIPMENT = "EQUIPMENT"
    FUNCTION = "FUNCTION"
class ValueKindType(Enum):
    DATETIME = "DATETIME"
    NULL = "NULL"
    METRIC = "METRIC"
class KindHintType(Enum):
    BH = "BH"
    AVG = "AVG"


############################################
# Definition of Classes
############################################

class metrics_Value:

    pass
class metrics_MetricValueRange:

    def __init__(self, kindHint: str, name: str, periodHint: str, metrics_MetricValueRange: set["metrics_Value"] = None):
        self.kindHint = kindHint
        self.name = name
        self.periodHint = periodHint
        self.metrics_MetricValueRange = metrics_MetricValueRange if metrics_MetricValueRange is not None else set()
        
    @property
    def kindHint(self) -> str:
        return self.__kindHint

    @kindHint.setter
    def kindHint(self, kindHint: str):
        self.__kindHint = kindHint

    @property
    def periodHint(self) -> str:
        return self.__periodHint

    @periodHint.setter
    def periodHint(self, periodHint: str):
        self.__periodHint = periodHint

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_MetricValueRange(self):
        return self.__metrics_MetricValueRange

    @metrics_MetricValueRange.setter
    def metrics_MetricValueRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricValueRange__metrics_MetricValueRange", None)
        self.__metrics_MetricValueRange = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_Value"):
                    opp_val = getattr(item, "metrics_Value", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_Value"):
                    opp_val = getattr(item, "metrics_Value", None)
                    
                    setattr(item, "metrics_Value", self)
                    

class metrics_Metric:

    def __init__(self, description: str, measurementKind: str, measurementPoint: str, metricCalculation: str, name: str, unitRef: str, metricRefs: "metrics_MetricSource" = None, metrics_Metric: "metrics_Metric" = None, metrics_Metric4: set["metrics_Metric"] = None, Metric: "metrics_MetricSource" = None):
        self.description = description
        self.measurementKind = measurementKind
        self.measurementPoint = measurementPoint
        self.metricCalculation = metricCalculation
        self.name = name
        self.unitRef = unitRef
        self.metricRefs = metricRefs
        self.metrics_Metric = metrics_Metric
        self.metrics_Metric4 = metrics_Metric4 if metrics_Metric4 is not None else set()
        self.Metric = Metric
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metricCalculation(self) -> str:
        return self.__metricCalculation

    @metricCalculation.setter
    def metricCalculation(self, metricCalculation: str):
        self.__metricCalculation = metricCalculation

    @property
    def measurementPoint(self) -> str:
        return self.__measurementPoint

    @measurementPoint.setter
    def measurementPoint(self, measurementPoint: str):
        self.__measurementPoint = measurementPoint

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def unitRef(self) -> str:
        return self.__unitRef

    @unitRef.setter
    def unitRef(self, unitRef: str):
        self.__unitRef = unitRef

    @property
    def measurementKind(self) -> str:
        return self.__measurementKind

    @measurementKind.setter
    def measurementKind(self, measurementKind: str):
        self.__measurementKind = measurementKind

    @property
    def metrics_Metric(self):
        return self.__metrics_Metric

    @metrics_Metric.setter
    def metrics_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric", None)
        self.__metrics_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Metric4"):
                opp_val = getattr(old_value, "metrics_Metric4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Metric4"):
                opp_val = getattr(value, "metrics_Metric4", None)
                if opp_val is None:
                    setattr(value, "metrics_Metric4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Metric(self):
        return self.__Metric

    @Metric.setter
    def Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__Metric", None)
        self.__Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricSourceRef"):
                opp_val = getattr(old_value, "metricSourceRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricSourceRef"):
                opp_val = getattr(value, "metricSourceRef", None)
                if opp_val is None:
                    setattr(value, "metricSourceRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_Metric4(self):
        return self.__metrics_Metric4

    @metrics_Metric4.setter
    def metrics_Metric4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric4", None)
        self.__metrics_Metric4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_Metric"):
                    opp_val = getattr(item, "metrics_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_Metric"):
                    opp_val = getattr(item, "metrics_Metric", None)
                    
                    setattr(item, "metrics_Metric", self)
                    

    @property
    def metricRefs(self):
        return self.__metricRefs

    @metricRefs.setter
    def metricRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metricRefs", None)
        self.__metricRefs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricSource"):
                opp_val = getattr(old_value, "MetricSource", None)
                if opp_val == self:
                    setattr(old_value, "MetricSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricSource"):
                opp_val = getattr(value, "MetricSource", None)
                setattr(value, "MetricSource", self)

class metrics_MetricSource:

    def __init__(self, name: str, metricLocation: str, MetricSource: "metrics_Metric" = None, metricSourceRef: set["metrics_Metric"] = None, metrics_MetricSource: "metrics_Mapping" = None, metrics_MetricSource10: set["metrics_MappingStatistic"] = None):
        self.name = name
        self.metricLocation = metricLocation
        self.MetricSource = MetricSource
        self.metricSourceRef = metricSourceRef if metricSourceRef is not None else set()
        self.metrics_MetricSource = metrics_MetricSource
        self.metrics_MetricSource10 = metrics_MetricSource10 if metrics_MetricSource10 is not None else set()
        
    @property
    def metricLocation(self) -> str:
        return self.__metricLocation

    @metricLocation.setter
    def metricLocation(self, metricLocation: str):
        self.__metricLocation = metricLocation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_MetricSource(self):
        return self.__metrics_MetricSource

    @metrics_MetricSource.setter
    def metrics_MetricSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource", None)
        self.__metrics_MetricSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Mapping"):
                opp_val = getattr(old_value, "metrics_Mapping", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Mapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Mapping"):
                opp_val = getattr(value, "metrics_Mapping", None)
                setattr(value, "metrics_Mapping", self)

    @property
    def MetricSource(self):
        return self.__MetricSource

    @MetricSource.setter
    def MetricSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__MetricSource", None)
        self.__MetricSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricRefs"):
                opp_val = getattr(old_value, "metricRefs", None)
                if opp_val == self:
                    setattr(old_value, "metricRefs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricRefs"):
                opp_val = getattr(value, "metricRefs", None)
                setattr(value, "metricRefs", self)

    @property
    def metrics_MetricSource10(self):
        return self.__metrics_MetricSource10

    @metrics_MetricSource10.setter
    def metrics_MetricSource10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource10", None)
        self.__metrics_MetricSource10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MappingStatistic11"):
                    opp_val = getattr(item, "metrics_MappingStatistic11", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingStatistic11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingStatistic11"):
                    opp_val = getattr(item, "metrics_MappingStatistic11", None)
                    
                    setattr(item, "metrics_MappingStatistic11", self)
                    

    @property
    def metricSourceRef(self):
        return self.__metricSourceRef

    @metricSourceRef.setter
    def metricSourceRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metricSourceRef", None)
        self.__metricSourceRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metric"):
                    opp_val = getattr(item, "Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metric"):
                    opp_val = getattr(item, "Metric", None)
                    
                    setattr(item, "Metric", self)
                    

class metrics_MappingStatistic:

    def __init__(self, totalRecords: str, metrics_MappingStatistic: set["metrics_MappingRecord"] = None, metrics_MappingStatistic2: "metrics_DateTimeRange" = None, metrics_MappingStatistic11: "metrics_MetricSource" = None):
        self.totalRecords = totalRecords
        self.metrics_MappingStatistic = metrics_MappingStatistic if metrics_MappingStatistic is not None else set()
        self.metrics_MappingStatistic2 = metrics_MappingStatistic2
        self.metrics_MappingStatistic11 = metrics_MappingStatistic11
        
    @property
    def totalRecords(self) -> str:
        return self.__totalRecords

    @totalRecords.setter
    def totalRecords(self, totalRecords: str):
        self.__totalRecords = totalRecords

    @property
    def metrics_MappingStatistic11(self):
        return self.__metrics_MappingStatistic11

    @metrics_MappingStatistic11.setter
    def metrics_MappingStatistic11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic11", None)
        self.__metrics_MappingStatistic11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricSource10"):
                opp_val = getattr(old_value, "metrics_MetricSource10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricSource10"):
                opp_val = getattr(value, "metrics_MetricSource10", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricSource10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MappingStatistic(self):
        return self.__metrics_MappingStatistic

    @metrics_MappingStatistic.setter
    def metrics_MappingStatistic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic", None)
        self.__metrics_MappingStatistic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MappingRecord"):
                    opp_val = getattr(item, "metrics_MappingRecord", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingRecord", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingRecord"):
                    opp_val = getattr(item, "metrics_MappingRecord", None)
                    
                    setattr(item, "metrics_MappingRecord", self)
                    

    @property
    def metrics_MappingStatistic2(self):
        return self.__metrics_MappingStatistic2

    @metrics_MappingStatistic2.setter
    def metrics_MappingStatistic2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic2", None)
        self.__metrics_MappingStatistic2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_DateTimeRange"):
                opp_val = getattr(old_value, "metrics_DateTimeRange", None)
                if opp_val == self:
                    setattr(old_value, "metrics_DateTimeRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_DateTimeRange"):
                opp_val = getattr(value, "metrics_DateTimeRange", None)
                setattr(value, "metrics_DateTimeRange", self)

class MappingRecord:

    pass
class metrics_MappingRecordXLS(MappingRecord):

    def __init__(self, column: str, row: str):
        self.column = column
        self.row = row
        
    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def row(self) -> str:
        return self.__row

    @row.setter
    def row(self, row: str):
        self.__row = row

class metrics_DateTimeRange:

    pass
class DataKind:

    pass
class metrics_ValueDataKind(DataKind):

    def __init__(self, valueKind: str):
        self.valueKind = valueKind
        
    @property
    def valueKind(self) -> str:
        return self.__valueKind

    @valueKind.setter
    def valueKind(self, valueKind: str):
        self.__valueKind = valueKind

class metrics_IdentifierDataKind(DataKind):

    def __init__(self, objectAttribute: str, objectName: str):
        self.objectAttribute = objectAttribute
        self.objectName = objectName
        
    @property
    def objectAttribute(self) -> str:
        return self.__objectAttribute

    @objectAttribute.setter
    def objectAttribute(self, objectAttribute: str):
        self.__objectAttribute = objectAttribute

    @property
    def objectName(self) -> str:
        return self.__objectName

    @objectName.setter
    def objectName(self, objectName: str):
        self.__objectName = objectName

class metrics_DataKind:

    pass
class metrics_MappingRecord:

    pass
class Mapping:

    pass
class metrics_MappingRDBMS(Mapping):

    pass
class metrics_MappingXLS(Mapping):

    def __init__(self, columnHeaders: str, firstDataRow: str, headerRow: str, sheetNumber: str, metrics_MappingXLS: set["metrics_DataKind"] = None):
        self.columnHeaders = columnHeaders
        self.firstDataRow = firstDataRow
        self.headerRow = headerRow
        self.sheetNumber = sheetNumber
        self.metrics_MappingXLS = metrics_MappingXLS if metrics_MappingXLS is not None else set()
        
    @property
    def sheetNumber(self) -> str:
        return self.__sheetNumber

    @sheetNumber.setter
    def sheetNumber(self, sheetNumber: str):
        self.__sheetNumber = sheetNumber

    @property
    def headerRow(self) -> str:
        return self.__headerRow

    @headerRow.setter
    def headerRow(self, headerRow: str):
        self.__headerRow = headerRow

    @property
    def firstDataRow(self) -> str:
        return self.__firstDataRow

    @firstDataRow.setter
    def firstDataRow(self, firstDataRow: str):
        self.__firstDataRow = firstDataRow

    @property
    def columnHeaders(self) -> str:
        return self.__columnHeaders

    @columnHeaders.setter
    def columnHeaders(self, columnHeaders: str):
        self.__columnHeaders = columnHeaders

    @property
    def metrics_MappingXLS(self):
        return self.__metrics_MappingXLS

    @metrics_MappingXLS.setter
    def metrics_MappingXLS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingXLS__metrics_MappingXLS", None)
        self.__metrics_MappingXLS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_DataKind"):
                    opp_val = getattr(item, "metrics_DataKind", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_DataKind", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_DataKind"):
                    opp_val = getattr(item, "metrics_DataKind", None)
                    
                    setattr(item, "metrics_DataKind", self)
                    

class metrics_MappingCSV(Mapping):

    pass
class metrics_Mapping:

    pass