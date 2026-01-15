from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ValueKindType(Enum):
    PERIOD = "PERIOD"
    DATETIME = "DATETIME"
    NULL = "NULL"
    METRIC = "METRIC"
class KindHintType(Enum):
    BH = "BH"
    AVG = "AVG"
class ObjectKindType(Enum):
    NODE = "NODE"
    EQUIPMENT = "EQUIPMENT"
    FUNCTION = "FUNCTION"
    RELATIONSHIP = "RELATIONSHIP"


############################################
# Definition of Classes
############################################

class metrics_Value:

    pass
class metrics_MetricValueRange:

    def __init__(self, kindHint: str, periodHint: str, metrics_MetricValueRange: set["metrics_Value"] = None):
        self.kindHint = kindHint
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
                    

class metrics_Unit:

    pass
class metrics_MetricSource:

    def __init__(self, metricLocation: str, name: str, MetricSource: "metrics_Metric" = None, metricSourceRef: set["metrics_Metric"] = None, metrics_MetricSource: "metrics_Mapping" = None, metrics_MetricSource14: set["metrics_MappingStatistic"] = None):
        self.metricLocation = metricLocation
        self.name = name
        self.MetricSource = MetricSource
        self.metricSourceRef = metricSourceRef if metricSourceRef is not None else set()
        self.metrics_MetricSource = metrics_MetricSource
        self.metrics_MetricSource14 = metrics_MetricSource14 if metrics_MetricSource14 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metricLocation(self) -> str:
        return self.__metricLocation

    @metricLocation.setter
    def metricLocation(self, metricLocation: str):
        self.__metricLocation = metricLocation

    @property
    def metrics_MetricSource14(self):
        return self.__metrics_MetricSource14

    @metrics_MetricSource14.setter
    def metrics_MetricSource14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource14", None)
        self.__metrics_MetricSource14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MappingStatistic15"):
                    opp_val = getattr(item, "metrics_MappingStatistic15", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingStatistic15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingStatistic15"):
                    opp_val = getattr(item, "metrics_MappingStatistic15", None)
                    
                    setattr(item, "metrics_MappingStatistic15", self)
                    

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
                    

class metrics_Metric:

    def __init__(self, description: str, measurementKind: str, measurementPoint: str, metricCalculation: str, name: str, metrics_Metric: "metrics_Metric" = None, metrics_Metric6: set["metrics_Metric"] = None, metricRefs: "metrics_MetricSource" = None, metrics_Metric10: "metrics_Unit" = None, Metric: "metrics_MetricSource" = None, metrics_Metric18: "metrics_ValueDataKind" = None):
        self.description = description
        self.measurementKind = measurementKind
        self.measurementPoint = measurementPoint
        self.metricCalculation = metricCalculation
        self.name = name
        self.metrics_Metric = metrics_Metric
        self.metrics_Metric6 = metrics_Metric6 if metrics_Metric6 is not None else set()
        self.metricRefs = metricRefs
        self.metrics_Metric10 = metrics_Metric10
        self.Metric = Metric
        self.metrics_Metric18 = metrics_Metric18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def measurementKind(self) -> str:
        return self.__measurementKind

    @measurementKind.setter
    def measurementKind(self, measurementKind: str):
        self.__measurementKind = measurementKind

    @property
    def metricCalculation(self) -> str:
        return self.__metricCalculation

    @metricCalculation.setter
    def metricCalculation(self, metricCalculation: str):
        self.__metricCalculation = metricCalculation

    @property
    def metrics_Metric18(self):
        return self.__metrics_Metric18

    @metrics_Metric18.setter
    def metrics_Metric18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric18", None)
        self.__metrics_Metric18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_ValueDataKind"):
                opp_val = getattr(old_value, "metrics_ValueDataKind", None)
                if opp_val == self:
                    setattr(old_value, "metrics_ValueDataKind", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_ValueDataKind"):
                opp_val = getattr(value, "metrics_ValueDataKind", None)
                setattr(value, "metrics_ValueDataKind", self)

    @property
    def metrics_Metric6(self):
        return self.__metrics_Metric6

    @metrics_Metric6.setter
    def metrics_Metric6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric6", None)
        self.__metrics_Metric6 = value if value is not None else set()
        
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

    @property
    def metrics_Metric10(self):
        return self.__metrics_Metric10

    @metrics_Metric10.setter
    def metrics_Metric10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric10", None)
        self.__metrics_Metric10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Unit"):
                opp_val = getattr(old_value, "metrics_Unit", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Unit"):
                opp_val = getattr(value, "metrics_Unit", None)
                setattr(value, "metrics_Unit", self)

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
            if hasattr(old_value, "metrics_Metric6"):
                opp_val = getattr(old_value, "metrics_Metric6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Metric6"):
                opp_val = getattr(value, "metrics_Metric6", None)
                if opp_val is None:
                    setattr(value, "metrics_Metric6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metrics_MappingXLSColumn:

    def __init__(self, column: str, metrics_MappingXLSColumn: "metrics_MappingXLS" = None, metrics_MappingXLSColumn5: "metrics_DataKind" = None):
        self.column = column
        self.metrics_MappingXLSColumn = metrics_MappingXLSColumn
        self.metrics_MappingXLSColumn5 = metrics_MappingXLSColumn5
        
    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def metrics_MappingXLSColumn(self):
        return self.__metrics_MappingXLSColumn

    @metrics_MappingXLSColumn.setter
    def metrics_MappingXLSColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingXLSColumn__metrics_MappingXLSColumn", None)
        self.__metrics_MappingXLSColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MappingXLS"):
                opp_val = getattr(old_value, "metrics_MappingXLS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MappingXLS"):
                opp_val = getattr(value, "metrics_MappingXLS", None)
                if opp_val is None:
                    setattr(value, "metrics_MappingXLS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MappingXLSColumn5(self):
        return self.__metrics_MappingXLSColumn5

    @metrics_MappingXLSColumn5.setter
    def metrics_MappingXLSColumn5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingXLSColumn__metrics_MappingXLSColumn5", None)
        self.__metrics_MappingXLSColumn5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_DataKind"):
                opp_val = getattr(old_value, "metrics_DataKind", None)
                if opp_val == self:
                    setattr(old_value, "metrics_DataKind", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_DataKind"):
                opp_val = getattr(value, "metrics_DataKind", None)
                setattr(value, "metrics_DataKind", self)

class metrics_DateTimeRange:

    pass
class metrics_MappingStatistic:

    def __init__(self, message: str, totalRecords: str, metrics_MappingStatistic: set["metrics_MappingRecord"] = None, metrics_MappingStatistic2: "metrics_DateTimeRange" = None, metrics_MappingStatistic15: "metrics_MetricSource" = None):
        self.message = message
        self.totalRecords = totalRecords
        self.metrics_MappingStatistic = metrics_MappingStatistic if metrics_MappingStatistic is not None else set()
        self.metrics_MappingStatistic2 = metrics_MappingStatistic2
        self.metrics_MappingStatistic15 = metrics_MappingStatistic15
        
    @property
    def totalRecords(self) -> str:
        return self.__totalRecords

    @totalRecords.setter
    def totalRecords(self, totalRecords: str):
        self.__totalRecords = totalRecords

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

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
    def metrics_MappingStatistic15(self):
        return self.__metrics_MappingStatistic15

    @metrics_MappingStatistic15.setter
    def metrics_MappingStatistic15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic15", None)
        self.__metrics_MappingStatistic15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricSource14"):
                opp_val = getattr(old_value, "metrics_MetricSource14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricSource14"):
                opp_val = getattr(value, "metrics_MetricSource14", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricSource14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class DataKind:

    pass
class metrics_ValueDataKind(DataKind):

    def __init__(self, kindHint: str, valueKind: str, metrics_ValueDataKind: "metrics_Metric" = None):
        self.kindHint = kindHint
        self.valueKind = valueKind
        self.metrics_ValueDataKind = metrics_ValueDataKind
        
    @property
    def kindHint(self) -> str:
        return self.__kindHint

    @kindHint.setter
    def kindHint(self, kindHint: str):
        self.__kindHint = kindHint

    @property
    def valueKind(self) -> str:
        return self.__valueKind

    @valueKind.setter
    def valueKind(self, valueKind: str):
        self.__valueKind = valueKind

    @property
    def metrics_ValueDataKind(self):
        return self.__metrics_ValueDataKind

    @metrics_ValueDataKind.setter
    def metrics_ValueDataKind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_ValueDataKind__metrics_ValueDataKind", None)
        self.__metrics_ValueDataKind = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Metric18"):
                opp_val = getattr(old_value, "metrics_Metric18", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Metric18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Metric18"):
                opp_val = getattr(value, "metrics_Metric18", None)
                setattr(value, "metrics_Metric18", self)

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

class metrics_MappingRecord:

    def __init__(self, message: str, metrics_MappingRecord: "metrics_MappingStatistic" = None):
        self.message = message
        self.metrics_MappingRecord = metrics_MappingRecord
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def metrics_MappingRecord(self):
        return self.__metrics_MappingRecord

    @metrics_MappingRecord.setter
    def metrics_MappingRecord(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingRecord__metrics_MappingRecord", None)
        self.__metrics_MappingRecord = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MappingStatistic"):
                opp_val = getattr(old_value, "metrics_MappingStatistic", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MappingStatistic"):
                opp_val = getattr(value, "metrics_MappingStatistic", None)
                if opp_val is None:
                    setattr(value, "metrics_MappingStatistic", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Mapping:

    pass
class metrics_MappingRDBMS(Mapping):

    pass
class metrics_MappingXLS(Mapping):

    def __init__(self, firstDataRow: str, headerRow: str, sheetNumber: str, metrics_MappingXLS: set["metrics_MappingXLSColumn"] = None):
        self.firstDataRow = firstDataRow
        self.headerRow = headerRow
        self.sheetNumber = sheetNumber
        self.metrics_MappingXLS = metrics_MappingXLS if metrics_MappingXLS is not None else set()
        
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
    def sheetNumber(self) -> str:
        return self.__sheetNumber

    @sheetNumber.setter
    def sheetNumber(self, sheetNumber: str):
        self.__sheetNumber = sheetNumber

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
                if hasattr(item, "metrics_MappingXLSColumn"):
                    opp_val = getattr(item, "metrics_MappingXLSColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingXLSColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingXLSColumn"):
                    opp_val = getattr(item, "metrics_MappingXLSColumn", None)
                    
                    setattr(item, "metrics_MappingXLSColumn", self)
                    

class metrics_MappingCSV(Mapping):

    pass
class metrics_Mapping:

    pass
class metrics_IdentifierDataKind(DataKind):

    def __init__(self, objectKind: str, objectProperty: str):
        self.objectKind = objectKind
        self.objectProperty = objectProperty
        
    @property
    def objectProperty(self) -> str:
        return self.__objectProperty

    @objectProperty.setter
    def objectProperty(self, objectProperty: str):
        self.__objectProperty = objectProperty

    @property
    def objectKind(self) -> str:
        return self.__objectKind

    @objectKind.setter
    def objectKind(self, objectKind: str):
        self.__objectKind = objectKind

class metrics_DataKind:

    pass