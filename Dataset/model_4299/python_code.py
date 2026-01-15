from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectKindType(Enum):
    NODE = "NODE"
    EQUIPMENT = "EQUIPMENT"
    FUNCTION = "FUNCTION"
    RELATIONSHIP = "RELATIONSHIP"
class MetricRetentionPeriod(Enum):
    Always = "Always"
    OneYear = "OneYear"
    OneMonth = "OneMonth"
    OneWeek = "OneWeek"
class DatabaseTypeType(Enum):
    Oracle = "Oracle"
    Postgres = "Postgres"
class ValueKindType(Enum):
    INTERVAL = "INTERVAL"
    DATE = "DATE"
    TIME = "TIME"
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

    def __init__(self, intervalHint: str, kindHint: str, metrics_MetricValueRange: set["metrics_Value"] = None):
        self.intervalHint = intervalHint
        self.kindHint = kindHint
        self.metrics_MetricValueRange = metrics_MetricValueRange if metrics_MetricValueRange is not None else set()
        
    @property
    def kindHint(self) -> str:
        return self.__kindHint

    @kindHint.setter
    def kindHint(self, kindHint: str):
        self.__kindHint = kindHint

    @property
    def intervalHint(self) -> str:
        return self.__intervalHint

    @intervalHint.setter
    def intervalHint(self, intervalHint: str):
        self.__intervalHint = intervalHint

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
                    

class metrics_MetricRetentionRule:

    def __init__(self, intervalHint: str, name: str, period: str, metrics_MetricRetentionRule: "metrics_Expression" = None, metrics_MetricRetentionRule23: "metrics_MetricRetentionRules" = None):
        self.intervalHint = intervalHint
        self.name = name
        self.period = period
        self.metrics_MetricRetentionRule = metrics_MetricRetentionRule
        self.metrics_MetricRetentionRule23 = metrics_MetricRetentionRule23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def period(self) -> str:
        return self.__period

    @period.setter
    def period(self, period: str):
        self.__period = period

    @property
    def intervalHint(self) -> str:
        return self.__intervalHint

    @intervalHint.setter
    def intervalHint(self, intervalHint: str):
        self.__intervalHint = intervalHint

    @property
    def metrics_MetricRetentionRule23(self):
        return self.__metrics_MetricRetentionRule23

    @metrics_MetricRetentionRule23.setter
    def metrics_MetricRetentionRule23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricRetentionRule__metrics_MetricRetentionRule23", None)
        self.__metrics_MetricRetentionRule23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricRetentionRules"):
                opp_val = getattr(old_value, "metrics_MetricRetentionRules", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricRetentionRules"):
                opp_val = getattr(value, "metrics_MetricRetentionRules", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricRetentionRules", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MetricRetentionRule(self):
        return self.__metrics_MetricRetentionRule

    @metrics_MetricRetentionRule.setter
    def metrics_MetricRetentionRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricRetentionRule__metrics_MetricRetentionRule", None)
        self.__metrics_MetricRetentionRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Expression21"):
                opp_val = getattr(old_value, "metrics_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Expression21"):
                opp_val = getattr(value, "metrics_Expression21", None)
                setattr(value, "metrics_Expression21", self)

class metrics_Unit:

    pass
class metrics_MetricRetentionRules:

    pass
class metrics_Expression:

    pass
class metrics_DateTimeRange:

    pass
class Mapping:

    pass
class metrics_MappingXLS(Mapping):

    def __init__(self, filterPattern: str, sheetNumber: str):
        self.filterPattern = filterPattern
        self.sheetNumber = sheetNumber
        
    @property
    def sheetNumber(self) -> str:
        return self.__sheetNumber

    @sheetNumber.setter
    def sheetNumber(self, sheetNumber: str):
        self.__sheetNumber = sheetNumber

    @property
    def filterPattern(self) -> str:
        return self.__filterPattern

    @filterPattern.setter
    def filterPattern(self, filterPattern: str):
        self.__filterPattern = filterPattern

class metrics_MappingRDBMS(Mapping):

    def __init__(self, dateFormat: str, dateTimeFormat: str, password: str, query: str, timeFormat: str, user: str, databaseType: str):
        self.dateFormat = dateFormat
        self.dateTimeFormat = dateTimeFormat
        self.password = password
        self.query = query
        self.timeFormat = timeFormat
        self.user = user
        self.databaseType = databaseType
        
    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def dateFormat(self) -> str:
        return self.__dateFormat

    @dateFormat.setter
    def dateFormat(self, dateFormat: str):
        self.__dateFormat = dateFormat

    @property
    def databaseType(self) -> str:
        return self.__databaseType

    @databaseType.setter
    def databaseType(self, databaseType: str):
        self.__databaseType = databaseType

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def timeFormat(self) -> str:
        return self.__timeFormat

    @timeFormat.setter
    def timeFormat(self, timeFormat: str):
        self.__timeFormat = timeFormat

    @property
    def dateTimeFormat(self) -> str:
        return self.__dateTimeFormat

    @dateTimeFormat.setter
    def dateTimeFormat(self, dateTimeFormat: str):
        self.__dateTimeFormat = dateTimeFormat

class metrics_MappingCSV(Mapping):

    def __init__(self, delimiter: str, filterPattern: str):
        self.delimiter = delimiter
        self.filterPattern = filterPattern
        
    @property
    def delimiter(self) -> str:
        return self.__delimiter

    @delimiter.setter
    def delimiter(self, delimiter: str):
        self.__delimiter = delimiter

    @property
    def filterPattern(self) -> str:
        return self.__filterPattern

    @filterPattern.setter
    def filterPattern(self, filterPattern: str):
        self.__filterPattern = filterPattern

class Base:

    pass
class metrics_MappingRecord(Base):

    def __init__(self, column: str, count: str, message: str, metrics_MappingRecord: "metrics_MappingStatistic" = None):
        self.column = column
        self.count = count
        self.message = message
        self.metrics_MappingRecord = metrics_MappingRecord
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

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

class metrics_MetricSource(Base):

    def __init__(self, name: str, filterPattern: str, metricLocation: str, metrics_MetricSource: "metrics_Metric" = None, metrics_MetricSource25: "metrics_Mapping" = None, metrics_MetricSource28: set["metrics_MappingStatistic"] = None):
        self.name = name
        self.filterPattern = filterPattern
        self.metricLocation = metricLocation
        self.metrics_MetricSource = metrics_MetricSource
        self.metrics_MetricSource25 = metrics_MetricSource25
        self.metrics_MetricSource28 = metrics_MetricSource28 if metrics_MetricSource28 is not None else set()
        
    @property
    def filterPattern(self) -> str:
        return self.__filterPattern

    @filterPattern.setter
    def filterPattern(self, filterPattern: str):
        self.__filterPattern = filterPattern

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
    def metrics_MetricSource(self):
        return self.__metrics_MetricSource

    @metrics_MetricSource.setter
    def metrics_MetricSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource", None)
        self.__metrics_MetricSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Metric17"):
                opp_val = getattr(old_value, "metrics_Metric17", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Metric17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Metric17"):
                opp_val = getattr(value, "metrics_Metric17", None)
                setattr(value, "metrics_Metric17", self)

    @property
    def metrics_MetricSource28(self):
        return self.__metrics_MetricSource28

    @metrics_MetricSource28.setter
    def metrics_MetricSource28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource28", None)
        self.__metrics_MetricSource28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MappingStatistic29"):
                    opp_val = getattr(item, "metrics_MappingStatistic29", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingStatistic29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingStatistic29"):
                    opp_val = getattr(item, "metrics_MappingStatistic29", None)
                    
                    setattr(item, "metrics_MappingStatistic29", self)
                    

    @property
    def metrics_MetricSource25(self):
        return self.__metrics_MetricSource25

    @metrics_MetricSource25.setter
    def metrics_MetricSource25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource25", None)
        self.__metrics_MetricSource25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Mapping26"):
                opp_val = getattr(old_value, "metrics_Mapping26", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Mapping26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Mapping26"):
                opp_val = getattr(value, "metrics_Mapping26", None)
                setattr(value, "metrics_Mapping26", self)

class metrics_MappingColumn(Base):

    def __init__(self, column: str, metrics_MappingColumn3: "metrics_Mapping" = None, metrics_MappingColumn5: "metrics_DataKind" = None, metrics_MappingColumn: "metrics_Mapping" = None):
        self.column = column
        self.metrics_MappingColumn3 = metrics_MappingColumn3
        self.metrics_MappingColumn5 = metrics_MappingColumn5
        self.metrics_MappingColumn = metrics_MappingColumn
        
    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def metrics_MappingColumn3(self):
        return self.__metrics_MappingColumn3

    @metrics_MappingColumn3.setter
    def metrics_MappingColumn3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingColumn__metrics_MappingColumn3", None)
        self.__metrics_MappingColumn3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Mapping2"):
                opp_val = getattr(old_value, "metrics_Mapping2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Mapping2"):
                opp_val = getattr(value, "metrics_Mapping2", None)
                if opp_val is None:
                    setattr(value, "metrics_Mapping2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MappingColumn(self):
        return self.__metrics_MappingColumn

    @metrics_MappingColumn.setter
    def metrics_MappingColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingColumn__metrics_MappingColumn", None)
        self.__metrics_MappingColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Mapping"):
                opp_val = getattr(old_value, "metrics_Mapping", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Mapping"):
                opp_val = getattr(value, "metrics_Mapping", None)
                if opp_val is None:
                    setattr(value, "metrics_Mapping", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MappingColumn5(self):
        return self.__metrics_MappingColumn5

    @metrics_MappingColumn5.setter
    def metrics_MappingColumn5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingColumn__metrics_MappingColumn5", None)
        self.__metrics_MappingColumn5 = value
        
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

class metrics_Metric(Base):

    def __init__(self, description: str, measurementKind: str, measurementPoint: str, name: str, metrics_Metric: "metrics_Metric" = None, metrics_Metric12: set["metrics_Metric"] = None, metrics_Metric15: "metrics_Expression" = None, metrics_Metric17: "metrics_MetricSource" = None, metrics_Metric19: "metrics_Unit" = None, metrics_Metric32: "metrics_ValueDataKind" = None):
        self.description = description
        self.measurementKind = measurementKind
        self.measurementPoint = measurementPoint
        self.name = name
        self.metrics_Metric = metrics_Metric
        self.metrics_Metric12 = metrics_Metric12 if metrics_Metric12 is not None else set()
        self.metrics_Metric15 = metrics_Metric15
        self.metrics_Metric17 = metrics_Metric17
        self.metrics_Metric19 = metrics_Metric19
        self.metrics_Metric32 = metrics_Metric32
        
    @property
    def measurementPoint(self) -> str:
        return self.__measurementPoint

    @measurementPoint.setter
    def measurementPoint(self, measurementPoint: str):
        self.__measurementPoint = measurementPoint

    @property
    def measurementKind(self) -> str:
        return self.__measurementKind

    @measurementKind.setter
    def measurementKind(self, measurementKind: str):
        self.__measurementKind = measurementKind

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_Metric17(self):
        return self.__metrics_Metric17

    @metrics_Metric17.setter
    def metrics_Metric17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric17", None)
        self.__metrics_Metric17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricSource"):
                opp_val = getattr(old_value, "metrics_MetricSource", None)
                if opp_val == self:
                    setattr(old_value, "metrics_MetricSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricSource"):
                opp_val = getattr(value, "metrics_MetricSource", None)
                setattr(value, "metrics_MetricSource", self)

    @property
    def metrics_Metric19(self):
        return self.__metrics_Metric19

    @metrics_Metric19.setter
    def metrics_Metric19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric19", None)
        self.__metrics_Metric19 = value
        
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
    def metrics_Metric32(self):
        return self.__metrics_Metric32

    @metrics_Metric32.setter
    def metrics_Metric32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric32", None)
        self.__metrics_Metric32 = value
        
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
    def metrics_Metric(self):
        return self.__metrics_Metric

    @metrics_Metric.setter
    def metrics_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric", None)
        self.__metrics_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Metric12"):
                opp_val = getattr(old_value, "metrics_Metric12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Metric12"):
                opp_val = getattr(value, "metrics_Metric12", None)
                if opp_val is None:
                    setattr(value, "metrics_Metric12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_Metric12(self):
        return self.__metrics_Metric12

    @metrics_Metric12.setter
    def metrics_Metric12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric12", None)
        self.__metrics_Metric12 = value if value is not None else set()
        
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
    def metrics_Metric15(self):
        return self.__metrics_Metric15

    @metrics_Metric15.setter
    def metrics_Metric15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric15", None)
        self.__metrics_Metric15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Expression"):
                opp_val = getattr(old_value, "metrics_Expression", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Expression"):
                opp_val = getattr(value, "metrics_Expression", None)
                setattr(value, "metrics_Expression", self)

class metrics_MappingStatistic(Base):

    def __init__(self, intervalEstimate: str, message: str, totalRecords: str, metrics_MappingStatistic: set["metrics_MappingRecord"] = None, metrics_MappingStatistic8: "metrics_DateTimeRange" = None, metrics_MappingStatistic10: "metrics_DateTimeRange" = None, metrics_MappingStatistic29: "metrics_MetricSource" = None):
        self.intervalEstimate = intervalEstimate
        self.message = message
        self.totalRecords = totalRecords
        self.metrics_MappingStatistic = metrics_MappingStatistic if metrics_MappingStatistic is not None else set()
        self.metrics_MappingStatistic8 = metrics_MappingStatistic8
        self.metrics_MappingStatistic10 = metrics_MappingStatistic10
        self.metrics_MappingStatistic29 = metrics_MappingStatistic29
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def totalRecords(self) -> str:
        return self.__totalRecords

    @totalRecords.setter
    def totalRecords(self, totalRecords: str):
        self.__totalRecords = totalRecords

    @property
    def intervalEstimate(self) -> str:
        return self.__intervalEstimate

    @intervalEstimate.setter
    def intervalEstimate(self, intervalEstimate: str):
        self.__intervalEstimate = intervalEstimate

    @property
    def metrics_MappingStatistic29(self):
        return self.__metrics_MappingStatistic29

    @metrics_MappingStatistic29.setter
    def metrics_MappingStatistic29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic29", None)
        self.__metrics_MappingStatistic29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricSource28"):
                opp_val = getattr(old_value, "metrics_MetricSource28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricSource28"):
                opp_val = getattr(value, "metrics_MetricSource28", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricSource28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MappingStatistic8(self):
        return self.__metrics_MappingStatistic8

    @metrics_MappingStatistic8.setter
    def metrics_MappingStatistic8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic8", None)
        self.__metrics_MappingStatistic8 = value
        
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

    @property
    def metrics_MappingStatistic10(self):
        return self.__metrics_MappingStatistic10

    @metrics_MappingStatistic10.setter
    def metrics_MappingStatistic10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MappingStatistic__metrics_MappingStatistic10", None)
        self.__metrics_MappingStatistic10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_DateTimeRange11"):
                opp_val = getattr(old_value, "metrics_DateTimeRange11", None)
                if opp_val == self:
                    setattr(old_value, "metrics_DateTimeRange11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_DateTimeRange11"):
                opp_val = getattr(value, "metrics_DateTimeRange11", None)
                setattr(value, "metrics_DateTimeRange11", self)

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
                    

class metrics_Mapping(Base):

    def __init__(self, firstDataRow: str, headerRow: str, intervalHint: str, metrics_Mapping2: set["metrics_MappingColumn"] = None, metrics_Mapping: set["metrics_MappingColumn"] = None, metrics_Mapping26: "metrics_MetricSource" = None):
        self.firstDataRow = firstDataRow
        self.headerRow = headerRow
        self.intervalHint = intervalHint
        self.metrics_Mapping2 = metrics_Mapping2 if metrics_Mapping2 is not None else set()
        self.metrics_Mapping = metrics_Mapping if metrics_Mapping is not None else set()
        self.metrics_Mapping26 = metrics_Mapping26
        
    @property
    def firstDataRow(self) -> str:
        return self.__firstDataRow

    @firstDataRow.setter
    def firstDataRow(self, firstDataRow: str):
        self.__firstDataRow = firstDataRow

    @property
    def intervalHint(self) -> str:
        return self.__intervalHint

    @intervalHint.setter
    def intervalHint(self, intervalHint: str):
        self.__intervalHint = intervalHint

    @property
    def headerRow(self) -> str:
        return self.__headerRow

    @headerRow.setter
    def headerRow(self, headerRow: str):
        self.__headerRow = headerRow

    @property
    def metrics_Mapping26(self):
        return self.__metrics_Mapping26

    @metrics_Mapping26.setter
    def metrics_Mapping26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Mapping__metrics_Mapping26", None)
        self.__metrics_Mapping26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricSource25"):
                opp_val = getattr(old_value, "metrics_MetricSource25", None)
                if opp_val == self:
                    setattr(old_value, "metrics_MetricSource25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricSource25"):
                opp_val = getattr(value, "metrics_MetricSource25", None)
                setattr(value, "metrics_MetricSource25", self)

    @property
    def metrics_Mapping(self):
        return self.__metrics_Mapping

    @metrics_Mapping.setter
    def metrics_Mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Mapping__metrics_Mapping", None)
        self.__metrics_Mapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MappingColumn"):
                    opp_val = getattr(item, "metrics_MappingColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingColumn"):
                    opp_val = getattr(item, "metrics_MappingColumn", None)
                    
                    setattr(item, "metrics_MappingColumn", self)
                    

    @property
    def metrics_Mapping2(self):
        return self.__metrics_Mapping2

    @metrics_Mapping2.setter
    def metrics_Mapping2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Mapping__metrics_Mapping2", None)
        self.__metrics_Mapping2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MappingColumn3"):
                    opp_val = getattr(item, "metrics_MappingColumn3", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MappingColumn3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MappingColumn3"):
                    opp_val = getattr(item, "metrics_MappingColumn3", None)
                    
                    setattr(item, "metrics_MappingColumn3", self)
                    

class DataKind:

    pass
class metrics_ValueDataKind(DataKind):

    def __init__(self, format: str, kindHint: str, valueKind: str, metrics_ValueDataKind: "metrics_Metric" = None):
        self.format = format
        self.kindHint = kindHint
        self.valueKind = valueKind
        self.metrics_ValueDataKind = metrics_ValueDataKind
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def valueKind(self) -> str:
        return self.__valueKind

    @valueKind.setter
    def valueKind(self, valueKind: str):
        self.__valueKind = valueKind

    @property
    def kindHint(self) -> str:
        return self.__kindHint

    @kindHint.setter
    def kindHint(self, kindHint: str):
        self.__kindHint = kindHint

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
            if hasattr(old_value, "metrics_Metric32"):
                opp_val = getattr(old_value, "metrics_Metric32", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Metric32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Metric32"):
                opp_val = getattr(value, "metrics_Metric32", None)
                setattr(value, "metrics_Metric32", self)

class metrics_IdentifierDataKind(DataKind):

    def __init__(self, objectKind: str, objectProperty: str, pattern: str):
        self.objectKind = objectKind
        self.objectProperty = objectProperty
        self.pattern = pattern
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def objectKind(self) -> str:
        return self.__objectKind

    @objectKind.setter
    def objectKind(self, objectKind: str):
        self.__objectKind = objectKind

    @property
    def objectProperty(self) -> str:
        return self.__objectProperty

    @objectProperty.setter
    def objectProperty(self, objectProperty: str):
        self.__objectProperty = objectProperty

class metrics_DataKind:

    pass