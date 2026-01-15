from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class QualityMetamodel_EnumerationItem:

    def __init__(self, name: str, QualityMetamodel_EnumerationItem: "QualityMetamodel_EnumerationMetric" = None, QualityMetamodel_EnumerationItem24: "QualityMetamodel_EnumerationMetric" = None):
        self.name = name
        self.QualityMetamodel_EnumerationItem = QualityMetamodel_EnumerationItem
        self.QualityMetamodel_EnumerationItem24 = QualityMetamodel_EnumerationItem24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_EnumerationItem24(self):
        return self.__QualityMetamodel_EnumerationItem24

    @QualityMetamodel_EnumerationItem24.setter
    def QualityMetamodel_EnumerationItem24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_EnumerationItem__QualityMetamodel_EnumerationItem24", None)
        self.__QualityMetamodel_EnumerationItem24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_EnumerationMetric23"):
                opp_val = getattr(old_value, "QualityMetamodel_EnumerationMetric23", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_EnumerationMetric23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_EnumerationMetric23"):
                opp_val = getattr(value, "QualityMetamodel_EnumerationMetric23", None)
                setattr(value, "QualityMetamodel_EnumerationMetric23", self)

    @property
    def QualityMetamodel_EnumerationItem(self):
        return self.__QualityMetamodel_EnumerationItem

    @QualityMetamodel_EnumerationItem.setter
    def QualityMetamodel_EnumerationItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_EnumerationItem__QualityMetamodel_EnumerationItem", None)
        self.__QualityMetamodel_EnumerationItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_EnumerationMetric"):
                opp_val = getattr(old_value, "QualityMetamodel_EnumerationMetric", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_EnumerationMetric"):
                opp_val = getattr(value, "QualityMetamodel_EnumerationMetric", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_EnumerationMetric", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ValueType:

    pass
class QualityMetamodel_IntegerValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class QualityMetamodel_EnumerationMetric(ValueType):

    pass
class QualityMetamodel_BooleanValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class QualityMetamodel_RealValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class QualityMetamodel_AggregatedValueMetric(ValueType):

    def __init__(self, minimum: str, maximum: str, average: str, median: str, standardDeviation: str):
        self.minimum = minimum
        self.maximum = maximum
        self.average = average
        self.median = median
        self.standardDeviation = standardDeviation
        
    @property
    def standardDeviation(self) -> str:
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: str):
        self.__standardDeviation = standardDeviation

    @property
    def median(self) -> str:
        return self.__median

    @median.setter
    def median(self, median: str):
        self.__median = median

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def average(self) -> str:
        return self.__average

    @average.setter
    def average(self, average: str):
        self.__average = average

class QualityMetamodel_RangeValueType(ValueType):

    def __init__(self, min: str, max: str):
        self.min = min
        self.max = max
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class QualityMetamodel_TextValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class QualityMetamodel_MetricProvider:

    def __init__(self, name: str, description: str, id: str, QualityMetamodel_MetricProvider16: "QualityMetamodel_SingleValue" = None, QualityMetamodel_MetricProvider: "QualityMetamodel_QualityModel" = None):
        self.name = name
        self.description = description
        self.id = id
        self.QualityMetamodel_MetricProvider16 = QualityMetamodel_MetricProvider16
        self.QualityMetamodel_MetricProvider = QualityMetamodel_MetricProvider
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def QualityMetamodel_MetricProvider16(self):
        return self.__QualityMetamodel_MetricProvider16

    @QualityMetamodel_MetricProvider16.setter
    def QualityMetamodel_MetricProvider16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_MetricProvider__QualityMetamodel_MetricProvider16", None)
        self.__QualityMetamodel_MetricProvider16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_SingleValue"):
                opp_val = getattr(old_value, "QualityMetamodel_SingleValue", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_SingleValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_SingleValue"):
                opp_val = getattr(value, "QualityMetamodel_SingleValue", None)
                setattr(value, "QualityMetamodel_SingleValue", self)

    @property
    def QualityMetamodel_MetricProvider(self):
        return self.__QualityMetamodel_MetricProvider

    @QualityMetamodel_MetricProvider.setter
    def QualityMetamodel_MetricProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_MetricProvider__QualityMetamodel_MetricProvider", None)
        self.__QualityMetamodel_MetricProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetamodel_QualityModel:

    def __init__(self, name: str, QualityMetamodel_QualityModel: set["QualityMetamodel_MetricProvider"] = None, QualityMetamodel_QualityModel2: set["QualityMetamodel_ValueType"] = None, QualityMetamodel_QualityModel4: set["QualityMetamodel_QualityAttribute"] = None, QualityMetamodel_QualityModel6: set["QualityMetamodel_Value"] = None):
        self.name = name
        self.QualityMetamodel_QualityModel = QualityMetamodel_QualityModel if QualityMetamodel_QualityModel is not None else set()
        self.QualityMetamodel_QualityModel2 = QualityMetamodel_QualityModel2 if QualityMetamodel_QualityModel2 is not None else set()
        self.QualityMetamodel_QualityModel4 = QualityMetamodel_QualityModel4 if QualityMetamodel_QualityModel4 is not None else set()
        self.QualityMetamodel_QualityModel6 = QualityMetamodel_QualityModel6 if QualityMetamodel_QualityModel6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_QualityModel6(self):
        return self.__QualityMetamodel_QualityModel6

    @QualityMetamodel_QualityModel6.setter
    def QualityMetamodel_QualityModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityModel__QualityMetamodel_QualityModel6", None)
        self.__QualityMetamodel_QualityModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_Value"):
                    opp_val = getattr(item, "QualityMetamodel_Value", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_Value"):
                    opp_val = getattr(item, "QualityMetamodel_Value", None)
                    
                    setattr(item, "QualityMetamodel_Value", self)
                    

    @property
    def QualityMetamodel_QualityModel4(self):
        return self.__QualityMetamodel_QualityModel4

    @QualityMetamodel_QualityModel4.setter
    def QualityMetamodel_QualityModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityModel__QualityMetamodel_QualityModel4", None)
        self.__QualityMetamodel_QualityModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_QualityAttribute"):
                    opp_val = getattr(item, "QualityMetamodel_QualityAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_QualityAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_QualityAttribute"):
                    opp_val = getattr(item, "QualityMetamodel_QualityAttribute", None)
                    
                    setattr(item, "QualityMetamodel_QualityAttribute", self)
                    

    @property
    def QualityMetamodel_QualityModel2(self):
        return self.__QualityMetamodel_QualityModel2

    @QualityMetamodel_QualityModel2.setter
    def QualityMetamodel_QualityModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityModel__QualityMetamodel_QualityModel2", None)
        self.__QualityMetamodel_QualityModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_ValueType"):
                    opp_val = getattr(item, "QualityMetamodel_ValueType", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_ValueType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_ValueType"):
                    opp_val = getattr(item, "QualityMetamodel_ValueType", None)
                    
                    setattr(item, "QualityMetamodel_ValueType", self)
                    

    @property
    def QualityMetamodel_QualityModel(self):
        return self.__QualityMetamodel_QualityModel

    @QualityMetamodel_QualityModel.setter
    def QualityMetamodel_QualityModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityModel__QualityMetamodel_QualityModel", None)
        self.__QualityMetamodel_QualityModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_MetricProvider"):
                    opp_val = getattr(item, "QualityMetamodel_MetricProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_MetricProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_MetricProvider"):
                    opp_val = getattr(item, "QualityMetamodel_MetricProvider", None)
                    
                    setattr(item, "QualityMetamodel_MetricProvider", self)
                    

class QualityMetamodel_Operation:

    def __init__(self, name: str, body: str, QualityMetamodel_Operation: "QualityMetamodel_AggregatedValue" = None, QualityMetamodel_Operation19: set["QualityMetamodel_Value"] = None):
        self.name = name
        self.body = body
        self.QualityMetamodel_Operation = QualityMetamodel_Operation
        self.QualityMetamodel_Operation19 = QualityMetamodel_Operation19 if QualityMetamodel_Operation19 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_Operation(self):
        return self.__QualityMetamodel_Operation

    @QualityMetamodel_Operation.setter
    def QualityMetamodel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation", None)
        self.__QualityMetamodel_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_AggregatedValue"):
                opp_val = getattr(old_value, "QualityMetamodel_AggregatedValue", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_AggregatedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_AggregatedValue"):
                opp_val = getattr(value, "QualityMetamodel_AggregatedValue", None)
                setattr(value, "QualityMetamodel_AggregatedValue", self)

    @property
    def QualityMetamodel_Operation19(self):
        return self.__QualityMetamodel_Operation19

    @QualityMetamodel_Operation19.setter
    def QualityMetamodel_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation19", None)
        self.__QualityMetamodel_Operation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_Value20"):
                    opp_val = getattr(item, "QualityMetamodel_Value20", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_Value20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_Value20"):
                    opp_val = getattr(item, "QualityMetamodel_Value20", None)
                    
                    setattr(item, "QualityMetamodel_Value20", self)
                    

class Value:

    pass
class QualityMetamodel_AggregatedValue(Value):

    pass
class QualityMetamodel_SingleValue(Value):

    pass
class QualityMetamodel_Value(ABC):

    def __init__(self, name: str, description: str, QualityMetamodel_Value: "QualityMetamodel_QualityModel" = None, QualityMetamodel_Value9: "QualityMetamodel_QualityAttribute" = None, val: "QualityMetamodel_ValueType" = None, Value: "QualityMetamodel_ValueType" = None, QualityMetamodel_Value20: "QualityMetamodel_Operation" = None):
        self.name = name
        self.description = description
        self.QualityMetamodel_Value = QualityMetamodel_Value
        self.QualityMetamodel_Value9 = QualityMetamodel_Value9
        self.val = val
        self.Value = Value
        self.QualityMetamodel_Value20 = QualityMetamodel_Value20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def QualityMetamodel_Value9(self):
        return self.__QualityMetamodel_Value9

    @QualityMetamodel_Value9.setter
    def QualityMetamodel_Value9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value9", None)
        self.__QualityMetamodel_Value9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityAttribute8"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityAttribute8", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_QualityAttribute8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityAttribute8"):
                opp_val = getattr(value, "QualityMetamodel_QualityAttribute8", None)
                setattr(value, "QualityMetamodel_QualityAttribute8", self)

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__Value", None)
        self.__Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if opp_val == self:
                    setattr(old_value, "type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                setattr(value, "type", self)

    @property
    def QualityMetamodel_Value20(self):
        return self.__QualityMetamodel_Value20

    @QualityMetamodel_Value20.setter
    def QualityMetamodel_Value20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value20", None)
        self.__QualityMetamodel_Value20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_Operation19"):
                opp_val = getattr(old_value, "QualityMetamodel_Operation19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_Operation19"):
                opp_val = getattr(value, "QualityMetamodel_Operation19", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_Operation19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__val", None)
        self.__val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType"):
                opp_val = getattr(old_value, "ValueType", None)
                if opp_val == self:
                    setattr(old_value, "ValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType"):
                opp_val = getattr(value, "ValueType", None)
                setattr(value, "ValueType", self)

    @property
    def QualityMetamodel_Value(self):
        return self.__QualityMetamodel_Value

    @QualityMetamodel_Value.setter
    def QualityMetamodel_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value", None)
        self.__QualityMetamodel_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel6"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel6"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel6", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetamodel_QualityAttribute:

    def __init__(self, name: str, QualityMetamodel_QualityAttribute: "QualityMetamodel_QualityModel" = None, QualityMetamodel_QualityAttribute8: "QualityMetamodel_Value" = None, QualityMetamodel_QualityAttribute12: "QualityMetamodel_QualityAttribute" = None, QualityMetamodel_QualityAttribute10: set["QualityMetamodel_QualityAttribute"] = None):
        self.name = name
        self.QualityMetamodel_QualityAttribute = QualityMetamodel_QualityAttribute
        self.QualityMetamodel_QualityAttribute8 = QualityMetamodel_QualityAttribute8
        self.QualityMetamodel_QualityAttribute12 = QualityMetamodel_QualityAttribute12
        self.QualityMetamodel_QualityAttribute10 = QualityMetamodel_QualityAttribute10 if QualityMetamodel_QualityAttribute10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_QualityAttribute(self):
        return self.__QualityMetamodel_QualityAttribute

    @QualityMetamodel_QualityAttribute.setter
    def QualityMetamodel_QualityAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityAttribute__QualityMetamodel_QualityAttribute", None)
        self.__QualityMetamodel_QualityAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel4"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel4"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel4", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QualityMetamodel_QualityAttribute10(self):
        return self.__QualityMetamodel_QualityAttribute10

    @QualityMetamodel_QualityAttribute10.setter
    def QualityMetamodel_QualityAttribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityAttribute__QualityMetamodel_QualityAttribute10", None)
        self.__QualityMetamodel_QualityAttribute10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_QualityAttribute12"):
                    opp_val = getattr(item, "QualityMetamodel_QualityAttribute12", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_QualityAttribute12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_QualityAttribute12"):
                    opp_val = getattr(item, "QualityMetamodel_QualityAttribute12", None)
                    
                    setattr(item, "QualityMetamodel_QualityAttribute12", self)
                    

    @property
    def QualityMetamodel_QualityAttribute8(self):
        return self.__QualityMetamodel_QualityAttribute8

    @QualityMetamodel_QualityAttribute8.setter
    def QualityMetamodel_QualityAttribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityAttribute__QualityMetamodel_QualityAttribute8", None)
        self.__QualityMetamodel_QualityAttribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_Value9"):
                opp_val = getattr(old_value, "QualityMetamodel_Value9", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_Value9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_Value9"):
                opp_val = getattr(value, "QualityMetamodel_Value9", None)
                setattr(value, "QualityMetamodel_Value9", self)

    @property
    def QualityMetamodel_QualityAttribute12(self):
        return self.__QualityMetamodel_QualityAttribute12

    @QualityMetamodel_QualityAttribute12.setter
    def QualityMetamodel_QualityAttribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QualityAttribute__QualityMetamodel_QualityAttribute12", None)
        self.__QualityMetamodel_QualityAttribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityAttribute10"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityAttribute10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityAttribute10"):
                opp_val = getattr(value, "QualityMetamodel_QualityAttribute10", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityAttribute10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetamodel_ValueType(ABC):

    def __init__(self, name: str, QualityMetamodel_ValueType: "QualityMetamodel_QualityModel" = None, ValueType: "QualityMetamodel_Value" = None, type: "QualityMetamodel_Value" = None):
        self.name = name
        self.QualityMetamodel_ValueType = QualityMetamodel_ValueType
        self.ValueType = ValueType
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ValueType(self):
        return self.__ValueType

    @ValueType.setter
    def ValueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_ValueType__ValueType", None)
        self.__ValueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "val"):
                opp_val = getattr(old_value, "val", None)
                if opp_val == self:
                    setattr(old_value, "val", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "val"):
                opp_val = getattr(value, "val", None)
                setattr(value, "val", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_ValueType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Value"):
                opp_val = getattr(old_value, "Value", None)
                if opp_val == self:
                    setattr(old_value, "Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Value"):
                opp_val = getattr(value, "Value", None)
                setattr(value, "Value", self)

    @property
    def QualityMetamodel_ValueType(self):
        return self.__QualityMetamodel_ValueType

    @QualityMetamodel_ValueType.setter
    def QualityMetamodel_ValueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_ValueType__QualityMetamodel_ValueType", None)
        self.__QualityMetamodel_ValueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel2"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel2"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel2", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
