from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mongoQuery_Array:

    pass
class mongoQuery_JsonDate:

    def __init__(self, dateString: str, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, milliseconds: int, mongoQuery_JsonDate: "mongoQuery_Query" = None):
        self.dateString = dateString
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
        self.milliseconds = milliseconds
        self.mongoQuery_JsonDate = mongoQuery_JsonDate
        
        pass
    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: int):
        self.__second = second


    @property
    def milliseconds(self):
        return self.__milliseconds

    @milliseconds.setter
    def milliseconds(self, milliseconds: int):
        self.__milliseconds = milliseconds


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: int):
        self.__minute = minute


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year


    @property
    def dateString(self):
        return self.__dateString

    @dateString.setter
    def dateString(self, dateString: str):
        self.__dateString = dateString


    @property
    def millisecond(self):
        return self.__millisecond

    @millisecond.setter
    def millisecond(self, millisecond: int):
        self.__millisecond = millisecond


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: int):
        self.__hour = hour


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day


    @property
    def mongoQuery_JsonDate(self):
        return self.__mongoQuery_JsonDate

    @mongoQuery_JsonDate.setter
    def mongoQuery_JsonDate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_JsonDate__mongoQuery_JsonDate", None)
        self.__mongoQuery_JsonDate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Query9"):
                opp_val = getattr(old_value, "mongoQuery_Query9", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Query9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Query9"):
                opp_val = getattr(value, "mongoQuery_Query9", None)
                setattr(value, "mongoQuery_Query9", self)

class Query:

    pass
class mongoQuery_QueryObject(Query):

    pass
class mongoQuery_FieldSelection:

    def __init__(self, key: str, enabled: int, mongoQuery_FieldSelection: "mongoQuery_Selection" = None):
        self.key = key
        self.enabled = enabled
        self.mongoQuery_FieldSelection = mongoQuery_FieldSelection
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: int):
        self.__enabled = enabled


    @property
    def mongoQuery_FieldSelection(self):
        return self.__mongoQuery_FieldSelection

    @mongoQuery_FieldSelection.setter
    def mongoQuery_FieldSelection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_FieldSelection__mongoQuery_FieldSelection", None)
        self.__mongoQuery_FieldSelection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Selection4"):
                opp_val = getattr(old_value, "mongoQuery_Selection4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Selection4"):
                opp_val = getattr(value, "mongoQuery_Selection4", None)
                if opp_val is None:
                    setattr(value, "mongoQuery_Selection4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mongoQuery_Selection:

    pass
class mongoQuery_Query:

    def __init__(self, key: str, stringValue: str, numberValue: float, integerValue: int, mongoQuery_Query: "mongoQuery_Selector" = None, mongoQuery_Query7: "mongoQuery_Query" = None, mongoQuery_Query5: "mongoQuery_Query" = None, mongoQuery_Query19: "mongoQuery_QueryObject" = None, mongoQuery_Query9: "mongoQuery_JsonDate" = None, mongoQuery_Query11: "mongoQuery_Array" = None, mongoQuery_Query14: "mongoQuery_Query" = None, mongoQuery_Query12: "mongoQuery_Query" = None, mongoQuery_Query17: "mongoQuery_Array" = None):
        self.key = key
        self.stringValue = stringValue
        self.numberValue = numberValue
        self.integerValue = integerValue
        self.mongoQuery_Query = mongoQuery_Query
        self.mongoQuery_Query7 = mongoQuery_Query7
        self.mongoQuery_Query5 = mongoQuery_Query5
        self.mongoQuery_Query19 = mongoQuery_Query19
        self.mongoQuery_Query9 = mongoQuery_Query9
        self.mongoQuery_Query11 = mongoQuery_Query11
        self.mongoQuery_Query14 = mongoQuery_Query14
        self.mongoQuery_Query12 = mongoQuery_Query12
        self.mongoQuery_Query17 = mongoQuery_Query17
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def stringValue(self):
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue


    @property
    def numberValue(self):
        return self.__numberValue

    @numberValue.setter
    def numberValue(self, numberValue: float):
        self.__numberValue = numberValue


    @property
    def integerValue(self):
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue


    @property
    def mongoQuery_Query(self):
        return self.__mongoQuery_Query

    @mongoQuery_Query.setter
    def mongoQuery_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query", None)
        self.__mongoQuery_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Selector"):
                opp_val = getattr(old_value, "mongoQuery_Selector", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Selector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Selector"):
                opp_val = getattr(value, "mongoQuery_Selector", None)
                setattr(value, "mongoQuery_Selector", self)

    @property
    def mongoQuery_Query14(self):
        return self.__mongoQuery_Query14

    @mongoQuery_Query14.setter
    def mongoQuery_Query14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query14", None)
        self.__mongoQuery_Query14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Query12"):
                opp_val = getattr(old_value, "mongoQuery_Query12", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Query12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Query12"):
                opp_val = getattr(value, "mongoQuery_Query12", None)
                setattr(value, "mongoQuery_Query12", self)

    @property
    def mongoQuery_Query12(self):
        return self.__mongoQuery_Query12

    @mongoQuery_Query12.setter
    def mongoQuery_Query12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query12", None)
        self.__mongoQuery_Query12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Query14"):
                opp_val = getattr(old_value, "mongoQuery_Query14", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Query14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Query14"):
                opp_val = getattr(value, "mongoQuery_Query14", None)
                setattr(value, "mongoQuery_Query14", self)

    @property
    def mongoQuery_Query5(self):
        return self.__mongoQuery_Query5

    @mongoQuery_Query5.setter
    def mongoQuery_Query5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query5", None)
        self.__mongoQuery_Query5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Query7"):
                opp_val = getattr(old_value, "mongoQuery_Query7", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Query7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Query7"):
                opp_val = getattr(value, "mongoQuery_Query7", None)
                setattr(value, "mongoQuery_Query7", self)

    @property
    def mongoQuery_Query17(self):
        return self.__mongoQuery_Query17

    @mongoQuery_Query17.setter
    def mongoQuery_Query17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query17", None)
        self.__mongoQuery_Query17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Array16"):
                opp_val = getattr(old_value, "mongoQuery_Array16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Array16"):
                opp_val = getattr(value, "mongoQuery_Array16", None)
                if opp_val is None:
                    setattr(value, "mongoQuery_Array16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mongoQuery_Query9(self):
        return self.__mongoQuery_Query9

    @mongoQuery_Query9.setter
    def mongoQuery_Query9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query9", None)
        self.__mongoQuery_Query9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_JsonDate"):
                opp_val = getattr(old_value, "mongoQuery_JsonDate", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_JsonDate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_JsonDate"):
                opp_val = getattr(value, "mongoQuery_JsonDate", None)
                setattr(value, "mongoQuery_JsonDate", self)

    @property
    def mongoQuery_Query19(self):
        return self.__mongoQuery_Query19

    @mongoQuery_Query19.setter
    def mongoQuery_Query19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query19", None)
        self.__mongoQuery_Query19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_QueryObject"):
                opp_val = getattr(old_value, "mongoQuery_QueryObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_QueryObject"):
                opp_val = getattr(value, "mongoQuery_QueryObject", None)
                if opp_val is None:
                    setattr(value, "mongoQuery_QueryObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mongoQuery_Query11(self):
        return self.__mongoQuery_Query11

    @mongoQuery_Query11.setter
    def mongoQuery_Query11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query11", None)
        self.__mongoQuery_Query11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Array"):
                opp_val = getattr(old_value, "mongoQuery_Array", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Array", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Array"):
                opp_val = getattr(value, "mongoQuery_Array", None)
                setattr(value, "mongoQuery_Array", self)

    @property
    def mongoQuery_Query7(self):
        return self.__mongoQuery_Query7

    @mongoQuery_Query7.setter
    def mongoQuery_Query7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongoQuery_Query__mongoQuery_Query7", None)
        self.__mongoQuery_Query7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongoQuery_Query5"):
                opp_val = getattr(old_value, "mongoQuery_Query5", None)
                if opp_val == self:
                    setattr(old_value, "mongoQuery_Query5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongoQuery_Query5"):
                opp_val = getattr(value, "mongoQuery_Query5", None)
                setattr(value, "mongoQuery_Query5", self)

class mongoQuery_Selector:

    pass