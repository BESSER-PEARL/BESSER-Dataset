from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class esper2Maude_Field:

    def __init__(self, star: str, eventVariable: str, eventPropName: str, esper2Maude_Field: "esper2Maude_SelectEntry" = None):
        self.star = star
        self.eventVariable = eventVariable
        self.eventPropName = eventPropName
        self.esper2Maude_Field = esper2Maude_Field
        
    @property
    def eventPropName(self) -> str:
        return self.__eventPropName

    @eventPropName.setter
    def eventPropName(self, eventPropName: str):
        self.__eventPropName = eventPropName

    @property
    def eventVariable(self) -> str:
        return self.__eventVariable

    @eventVariable.setter
    def eventVariable(self, eventVariable: str):
        self.__eventVariable = eventVariable

    @property
    def star(self) -> str:
        return self.__star

    @star.setter
    def star(self, star: str):
        self.__star = star

    @property
    def esper2Maude_Field(self):
        return self.__esper2Maude_Field

    @esper2Maude_Field.setter
    def esper2Maude_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Field__esper2Maude_Field", None)
        self.__esper2Maude_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_SelectEntry78"):
                opp_val = getattr(old_value, "esper2Maude_SelectEntry78", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_SelectEntry78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_SelectEntry78"):
                opp_val = getattr(value, "esper2Maude_SelectEntry78", None)
                setattr(value, "esper2Maude_SelectEntry78", self)

class esper2Maude_FilterPart:

    def __init__(self, eventPropName: str, eventVariable: str, neg: str, num: int, dec: int, str: str, t: str, f: str, esper2Maude_FilterPart: "esper2Maude_FilterEvent" = None, esper2Maude_FilterPart66: "esper2Maude_FilterEvent" = None):
        self.eventPropName = eventPropName
        self.eventVariable = eventVariable
        self.neg = neg
        self.num = num
        self.dec = dec
        self.str = str
        self.t = t
        self.f = f
        self.esper2Maude_FilterPart = esper2Maude_FilterPart
        self.esper2Maude_FilterPart66 = esper2Maude_FilterPart66
        
    @property
    def eventPropName(self) -> str:
        return self.__eventPropName

    @eventPropName.setter
    def eventPropName(self, eventPropName: str):
        self.__eventPropName = eventPropName

    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

    @property
    def f(self) -> str:
        return self.__f

    @f.setter
    def f(self, f: str):
        self.__f = f

    @property
    def eventVariable(self) -> str:
        return self.__eventVariable

    @eventVariable.setter
    def eventVariable(self, eventVariable: str):
        self.__eventVariable = eventVariable

    @property
    def dec(self) -> int:
        return self.__dec

    @dec.setter
    def dec(self, dec: int):
        self.__dec = dec

    @property
    def neg(self) -> str:
        return self.__neg

    @neg.setter
    def neg(self, neg: str):
        self.__neg = neg

    @property
    def t(self) -> str:
        return self.__t

    @t.setter
    def t(self, t: str):
        self.__t = t

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def esper2Maude_FilterPart(self):
        return self.__esper2Maude_FilterPart

    @esper2Maude_FilterPart.setter
    def esper2Maude_FilterPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterPart__esper2Maude_FilterPart", None)
        self.__esper2Maude_FilterPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent60"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent60", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent60"):
                opp_val = getattr(value, "esper2Maude_FilterEvent60", None)
                setattr(value, "esper2Maude_FilterEvent60", self)

    @property
    def esper2Maude_FilterPart66(self):
        return self.__esper2Maude_FilterPart66

    @esper2Maude_FilterPart66.setter
    def esper2Maude_FilterPart66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterPart__esper2Maude_FilterPart66", None)
        self.__esper2Maude_FilterPart66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent65"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent65", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent65"):
                opp_val = getattr(value, "esper2Maude_FilterEvent65", None)
                setattr(value, "esper2Maude_FilterEvent65", self)

class esper2Maude_Every:

    def __init__(self, eventVariable: str, eventName: str, esper2Maude_Every: "esper2Maude_SubFilterFollowedBy" = None, esper2Maude_Every54: "esper2Maude_FilterEvent" = None, esper2Maude_Every57: "esper2Maude_FilterFrom" = None):
        self.eventVariable = eventVariable
        self.eventName = eventName
        self.esper2Maude_Every = esper2Maude_Every
        self.esper2Maude_Every54 = esper2Maude_Every54
        self.esper2Maude_Every57 = esper2Maude_Every57
        
    @property
    def eventVariable(self) -> str:
        return self.__eventVariable

    @eventVariable.setter
    def eventVariable(self, eventVariable: str):
        self.__eventVariable = eventVariable

    @property
    def eventName(self) -> str:
        return self.__eventName

    @eventName.setter
    def eventName(self, eventName: str):
        self.__eventName = eventName

    @property
    def esper2Maude_Every(self):
        return self.__esper2Maude_Every

    @esper2Maude_Every.setter
    def esper2Maude_Every(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Every__esper2Maude_Every", None)
        self.__esper2Maude_Every = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_SubFilterFollowedBy52"):
                opp_val = getattr(old_value, "esper2Maude_SubFilterFollowedBy52", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_SubFilterFollowedBy52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_SubFilterFollowedBy52"):
                opp_val = getattr(value, "esper2Maude_SubFilterFollowedBy52", None)
                setattr(value, "esper2Maude_SubFilterFollowedBy52", self)

    @property
    def esper2Maude_Every54(self):
        return self.__esper2Maude_Every54

    @esper2Maude_Every54.setter
    def esper2Maude_Every54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Every__esper2Maude_Every54", None)
        self.__esper2Maude_Every54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent55"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent55", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent55"):
                opp_val = getattr(value, "esper2Maude_FilterEvent55", None)
                setattr(value, "esper2Maude_FilterEvent55", self)

    @property
    def esper2Maude_Every57(self):
        return self.__esper2Maude_Every57

    @esper2Maude_Every57.setter
    def esper2Maude_Every57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Every__esper2Maude_Every57", None)
        self.__esper2Maude_Every57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom58"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom58", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom58"):
                opp_val = getattr(value, "esper2Maude_FilterFrom58", None)
                setattr(value, "esper2Maude_FilterFrom58", self)

class esper2Maude_SelectEntry:

    def __init__(self, alias: str, groupOp: str, esper2Maude_SelectEntry: "esper2Maude_NonLastSelectEntry" = None, esper2Maude_SelectEntry76: "esper2Maude_LastSelectEntry" = None, esper2Maude_SelectEntry78: "esper2Maude_Field" = None):
        self.alias = alias
        self.groupOp = groupOp
        self.esper2Maude_SelectEntry = esper2Maude_SelectEntry
        self.esper2Maude_SelectEntry76 = esper2Maude_SelectEntry76
        self.esper2Maude_SelectEntry78 = esper2Maude_SelectEntry78
        
    @property
    def groupOp(self) -> str:
        return self.__groupOp

    @groupOp.setter
    def groupOp(self, groupOp: str):
        self.__groupOp = groupOp

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def esper2Maude_SelectEntry78(self):
        return self.__esper2Maude_SelectEntry78

    @esper2Maude_SelectEntry78.setter
    def esper2Maude_SelectEntry78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SelectEntry__esper2Maude_SelectEntry78", None)
        self.__esper2Maude_SelectEntry78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Field"):
                opp_val = getattr(old_value, "esper2Maude_Field", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Field"):
                opp_val = getattr(value, "esper2Maude_Field", None)
                setattr(value, "esper2Maude_Field", self)

    @property
    def esper2Maude_SelectEntry76(self):
        return self.__esper2Maude_SelectEntry76

    @esper2Maude_SelectEntry76.setter
    def esper2Maude_SelectEntry76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SelectEntry__esper2Maude_SelectEntry76", None)
        self.__esper2Maude_SelectEntry76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_LastSelectEntry75"):
                opp_val = getattr(old_value, "esper2Maude_LastSelectEntry75", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_LastSelectEntry75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_LastSelectEntry75"):
                opp_val = getattr(value, "esper2Maude_LastSelectEntry75", None)
                setattr(value, "esper2Maude_LastSelectEntry75", self)

    @property
    def esper2Maude_SelectEntry(self):
        return self.__esper2Maude_SelectEntry

    @esper2Maude_SelectEntry.setter
    def esper2Maude_SelectEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SelectEntry__esper2Maude_SelectEntry", None)
        self.__esper2Maude_SelectEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_NonLastSelectEntry73"):
                opp_val = getattr(old_value, "esper2Maude_NonLastSelectEntry73", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_NonLastSelectEntry73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_NonLastSelectEntry73"):
                opp_val = getattr(value, "esper2Maude_NonLastSelectEntry73", None)
                setattr(value, "esper2Maude_NonLastSelectEntry73", self)

class esper2Maude_ComparisonOperator:

    def __init__(self, gt: str, ge: str, eq: str, neq: str, lt: str, le: str, esper2Maude_ComparisonOperator: "esper2Maude_FilterOperator" = None):
        self.gt = gt
        self.ge = ge
        self.eq = eq
        self.neq = neq
        self.lt = lt
        self.le = le
        self.esper2Maude_ComparisonOperator = esper2Maude_ComparisonOperator
        
    @property
    def le(self) -> str:
        return self.__le

    @le.setter
    def le(self, le: str):
        self.__le = le

    @property
    def lt(self) -> str:
        return self.__lt

    @lt.setter
    def lt(self, lt: str):
        self.__lt = lt

    @property
    def gt(self) -> str:
        return self.__gt

    @gt.setter
    def gt(self, gt: str):
        self.__gt = gt

    @property
    def ge(self) -> str:
        return self.__ge

    @ge.setter
    def ge(self, ge: str):
        self.__ge = ge

    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def neq(self) -> str:
        return self.__neq

    @neq.setter
    def neq(self, neq: str):
        self.__neq = neq

    @property
    def esper2Maude_ComparisonOperator(self):
        return self.__esper2Maude_ComparisonOperator

    @esper2Maude_ComparisonOperator.setter
    def esper2Maude_ComparisonOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_ComparisonOperator__esper2Maude_ComparisonOperator", None)
        self.__esper2Maude_ComparisonOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterOperator68"):
                opp_val = getattr(old_value, "esper2Maude_FilterOperator68", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterOperator68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterOperator68"):
                opp_val = getattr(value, "esper2Maude_FilterOperator68", None)
                setattr(value, "esper2Maude_FilterOperator68", self)

class esper2Maude_FilterEvent:

    pass
class esper2Maude_WhereFilter:

    def __init__(self, timer: str, num: int, esper2Maude_WhereFilter20: "esper2Maude_FilterOperator" = None, esper2Maude_WhereFilter22: "esper2Maude_FilterOperator" = None, esper2Maude_WhereFilter25: "esper2Maude_FilterEvent" = None, esper2Maude_WhereFilter47: "esper2Maude_FollowedBy" = None, esper2Maude_WhereFilter: "esper2Maude_FilterEvent" = None):
        self.timer = timer
        self.num = num
        self.esper2Maude_WhereFilter20 = esper2Maude_WhereFilter20
        self.esper2Maude_WhereFilter22 = esper2Maude_WhereFilter22
        self.esper2Maude_WhereFilter25 = esper2Maude_WhereFilter25
        self.esper2Maude_WhereFilter47 = esper2Maude_WhereFilter47
        self.esper2Maude_WhereFilter = esper2Maude_WhereFilter
        
    @property
    def timer(self) -> str:
        return self.__timer

    @timer.setter
    def timer(self, timer: str):
        self.__timer = timer

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def esper2Maude_WhereFilter(self):
        return self.__esper2Maude_WhereFilter

    @esper2Maude_WhereFilter.setter
    def esper2Maude_WhereFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_WhereFilter__esper2Maude_WhereFilter", None)
        self.__esper2Maude_WhereFilter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent"):
                opp_val = getattr(value, "esper2Maude_FilterEvent", None)
                setattr(value, "esper2Maude_FilterEvent", self)

    @property
    def esper2Maude_WhereFilter22(self):
        return self.__esper2Maude_WhereFilter22

    @esper2Maude_WhereFilter22.setter
    def esper2Maude_WhereFilter22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_WhereFilter__esper2Maude_WhereFilter22", None)
        self.__esper2Maude_WhereFilter22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterOperator23"):
                opp_val = getattr(old_value, "esper2Maude_FilterOperator23", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterOperator23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterOperator23"):
                opp_val = getattr(value, "esper2Maude_FilterOperator23", None)
                setattr(value, "esper2Maude_FilterOperator23", self)

    @property
    def esper2Maude_WhereFilter20(self):
        return self.__esper2Maude_WhereFilter20

    @esper2Maude_WhereFilter20.setter
    def esper2Maude_WhereFilter20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_WhereFilter__esper2Maude_WhereFilter20", None)
        self.__esper2Maude_WhereFilter20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterOperator"):
                opp_val = getattr(old_value, "esper2Maude_FilterOperator", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterOperator"):
                opp_val = getattr(value, "esper2Maude_FilterOperator", None)
                setattr(value, "esper2Maude_FilterOperator", self)

    @property
    def esper2Maude_WhereFilter47(self):
        return self.__esper2Maude_WhereFilter47

    @esper2Maude_WhereFilter47.setter
    def esper2Maude_WhereFilter47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_WhereFilter__esper2Maude_WhereFilter47", None)
        self.__esper2Maude_WhereFilter47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FollowedBy46"):
                opp_val = getattr(old_value, "esper2Maude_FollowedBy46", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FollowedBy46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FollowedBy46"):
                opp_val = getattr(value, "esper2Maude_FollowedBy46", None)
                setattr(value, "esper2Maude_FollowedBy46", self)

    @property
    def esper2Maude_WhereFilter25(self):
        return self.__esper2Maude_WhereFilter25

    @esper2Maude_WhereFilter25.setter
    def esper2Maude_WhereFilter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_WhereFilter__esper2Maude_WhereFilter25", None)
        self.__esper2Maude_WhereFilter25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent26"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent26", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent26"):
                opp_val = getattr(value, "esper2Maude_FilterEvent26", None)
                setattr(value, "esper2Maude_FilterEvent26", self)

class esper2Maude_Window:

    def __init__(self, typeTime: str, num: int, typeBatch: str, esper2Maude_Window: "esper2Maude_Pattern" = None):
        self.typeTime = typeTime
        self.num = num
        self.typeBatch = typeBatch
        self.esper2Maude_Window = esper2Maude_Window
        
    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def typeBatch(self) -> str:
        return self.__typeBatch

    @typeBatch.setter
    def typeBatch(self, typeBatch: str):
        self.__typeBatch = typeBatch

    @property
    def typeTime(self) -> str:
        return self.__typeTime

    @typeTime.setter
    def typeTime(self, typeTime: str):
        self.__typeTime = typeTime

    @property
    def esper2Maude_Window(self):
        return self.__esper2Maude_Window

    @esper2Maude_Window.setter
    def esper2Maude_Window(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Window__esper2Maude_Window", None)
        self.__esper2Maude_Window = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Pattern17"):
                opp_val = getattr(old_value, "esper2Maude_Pattern17", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Pattern17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Pattern17"):
                opp_val = getattr(value, "esper2Maude_Pattern17", None)
                setattr(value, "esper2Maude_Pattern17", self)

class esper2Maude_FilterFrom:

    def __init__(self, eventVariable: str, eventName: str, esper2Maude_FilterFrom28: "esper2Maude_FollowedBy" = None, esper2Maude_FilterFrom31: "esper2Maude_FilterFrom" = None, esper2Maude_FilterFrom29: "esper2Maude_FilterFrom" = None, esper2Maude_FilterFrom33: "esper2Maude_LogicalOperator" = None, esper2Maude_FilterFrom36: "esper2Maude_FilterFrom" = None, esper2Maude_FilterFrom34: "esper2Maude_FilterFrom" = None, esper2Maude_FilterFrom38: "esper2Maude_FilterEvent" = None, esper2Maude_FilterFrom: "esper2Maude_Pattern" = None, esper2Maude_FilterFrom58: "esper2Maude_Every" = None):
        self.eventVariable = eventVariable
        self.eventName = eventName
        self.esper2Maude_FilterFrom28 = esper2Maude_FilterFrom28
        self.esper2Maude_FilterFrom31 = esper2Maude_FilterFrom31
        self.esper2Maude_FilterFrom29 = esper2Maude_FilterFrom29
        self.esper2Maude_FilterFrom33 = esper2Maude_FilterFrom33
        self.esper2Maude_FilterFrom36 = esper2Maude_FilterFrom36
        self.esper2Maude_FilterFrom34 = esper2Maude_FilterFrom34
        self.esper2Maude_FilterFrom38 = esper2Maude_FilterFrom38
        self.esper2Maude_FilterFrom = esper2Maude_FilterFrom
        self.esper2Maude_FilterFrom58 = esper2Maude_FilterFrom58
        
    @property
    def eventName(self) -> str:
        return self.__eventName

    @eventName.setter
    def eventName(self, eventName: str):
        self.__eventName = eventName

    @property
    def eventVariable(self) -> str:
        return self.__eventVariable

    @eventVariable.setter
    def eventVariable(self, eventVariable: str):
        self.__eventVariable = eventVariable

    @property
    def esper2Maude_FilterFrom36(self):
        return self.__esper2Maude_FilterFrom36

    @esper2Maude_FilterFrom36.setter
    def esper2Maude_FilterFrom36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom36", None)
        self.__esper2Maude_FilterFrom36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom34"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom34", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom34"):
                opp_val = getattr(value, "esper2Maude_FilterFrom34", None)
                setattr(value, "esper2Maude_FilterFrom34", self)

    @property
    def esper2Maude_FilterFrom58(self):
        return self.__esper2Maude_FilterFrom58

    @esper2Maude_FilterFrom58.setter
    def esper2Maude_FilterFrom58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom58", None)
        self.__esper2Maude_FilterFrom58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Every57"):
                opp_val = getattr(old_value, "esper2Maude_Every57", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Every57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Every57"):
                opp_val = getattr(value, "esper2Maude_Every57", None)
                setattr(value, "esper2Maude_Every57", self)

    @property
    def esper2Maude_FilterFrom31(self):
        return self.__esper2Maude_FilterFrom31

    @esper2Maude_FilterFrom31.setter
    def esper2Maude_FilterFrom31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom31", None)
        self.__esper2Maude_FilterFrom31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom29"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom29", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom29"):
                opp_val = getattr(value, "esper2Maude_FilterFrom29", None)
                setattr(value, "esper2Maude_FilterFrom29", self)

    @property
    def esper2Maude_FilterFrom(self):
        return self.__esper2Maude_FilterFrom

    @esper2Maude_FilterFrom.setter
    def esper2Maude_FilterFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom", None)
        self.__esper2Maude_FilterFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Pattern15"):
                opp_val = getattr(old_value, "esper2Maude_Pattern15", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Pattern15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Pattern15"):
                opp_val = getattr(value, "esper2Maude_Pattern15", None)
                setattr(value, "esper2Maude_Pattern15", self)

    @property
    def esper2Maude_FilterFrom28(self):
        return self.__esper2Maude_FilterFrom28

    @esper2Maude_FilterFrom28.setter
    def esper2Maude_FilterFrom28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom28", None)
        self.__esper2Maude_FilterFrom28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FollowedBy"):
                opp_val = getattr(old_value, "esper2Maude_FollowedBy", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FollowedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FollowedBy"):
                opp_val = getattr(value, "esper2Maude_FollowedBy", None)
                setattr(value, "esper2Maude_FollowedBy", self)

    @property
    def esper2Maude_FilterFrom29(self):
        return self.__esper2Maude_FilterFrom29

    @esper2Maude_FilterFrom29.setter
    def esper2Maude_FilterFrom29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom29", None)
        self.__esper2Maude_FilterFrom29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom31"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom31", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom31"):
                opp_val = getattr(value, "esper2Maude_FilterFrom31", None)
                setattr(value, "esper2Maude_FilterFrom31", self)

    @property
    def esper2Maude_FilterFrom34(self):
        return self.__esper2Maude_FilterFrom34

    @esper2Maude_FilterFrom34.setter
    def esper2Maude_FilterFrom34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom34", None)
        self.__esper2Maude_FilterFrom34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom36"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom36", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom36"):
                opp_val = getattr(value, "esper2Maude_FilterFrom36", None)
                setattr(value, "esper2Maude_FilterFrom36", self)

    @property
    def esper2Maude_FilterFrom33(self):
        return self.__esper2Maude_FilterFrom33

    @esper2Maude_FilterFrom33.setter
    def esper2Maude_FilterFrom33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom33", None)
        self.__esper2Maude_FilterFrom33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_LogicalOperator"):
                opp_val = getattr(old_value, "esper2Maude_LogicalOperator", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_LogicalOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_LogicalOperator"):
                opp_val = getattr(value, "esper2Maude_LogicalOperator", None)
                setattr(value, "esper2Maude_LogicalOperator", self)

    @property
    def esper2Maude_FilterFrom38(self):
        return self.__esper2Maude_FilterFrom38

    @esper2Maude_FilterFrom38.setter
    def esper2Maude_FilterFrom38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_FilterFrom__esper2Maude_FilterFrom38", None)
        self.__esper2Maude_FilterFrom38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent39"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent39", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent39"):
                opp_val = getattr(value, "esper2Maude_FilterEvent39", None)
                setattr(value, "esper2Maude_FilterEvent39", self)

class esper2Maude_LastSelectEntry:

    pass
class esper2Maude_NonLastSelectEntry:

    pass
class esper2Maude_Event:

    def __init__(self, name: str, esper2Maude_Event: "esper2Maude_Pattern" = None):
        self.name = name
        self.esper2Maude_Event = esper2Maude_Event
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esper2Maude_Event(self):
        return self.__esper2Maude_Event

    @esper2Maude_Event.setter
    def esper2Maude_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Event__esper2Maude_Event", None)
        self.__esper2Maude_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Pattern9"):
                opp_val = getattr(old_value, "esper2Maude_Pattern9", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Pattern9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Pattern9"):
                opp_val = getattr(value, "esper2Maude_Pattern9", None)
                setattr(value, "esper2Maude_Pattern9", self)

class esper2Maude_SubFilterFollowedBy:

    def __init__(self, eventVariable: str, eventName: str, esper2Maude_SubFilterFollowedBy: "esper2Maude_FollowedBy" = None, esper2Maude_SubFilterFollowedBy44: "esper2Maude_FollowedBy" = None, esper2Maude_SubFilterFollowedBy49: "esper2Maude_FilterEvent" = None, esper2Maude_SubFilterFollowedBy52: "esper2Maude_Every" = None):
        self.eventVariable = eventVariable
        self.eventName = eventName
        self.esper2Maude_SubFilterFollowedBy = esper2Maude_SubFilterFollowedBy
        self.esper2Maude_SubFilterFollowedBy44 = esper2Maude_SubFilterFollowedBy44
        self.esper2Maude_SubFilterFollowedBy49 = esper2Maude_SubFilterFollowedBy49
        self.esper2Maude_SubFilterFollowedBy52 = esper2Maude_SubFilterFollowedBy52
        
    @property
    def eventVariable(self) -> str:
        return self.__eventVariable

    @eventVariable.setter
    def eventVariable(self, eventVariable: str):
        self.__eventVariable = eventVariable

    @property
    def eventName(self) -> str:
        return self.__eventName

    @eventName.setter
    def eventName(self, eventName: str):
        self.__eventName = eventName

    @property
    def esper2Maude_SubFilterFollowedBy49(self):
        return self.__esper2Maude_SubFilterFollowedBy49

    @esper2Maude_SubFilterFollowedBy49.setter
    def esper2Maude_SubFilterFollowedBy49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SubFilterFollowedBy__esper2Maude_SubFilterFollowedBy49", None)
        self.__esper2Maude_SubFilterFollowedBy49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterEvent50"):
                opp_val = getattr(old_value, "esper2Maude_FilterEvent50", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterEvent50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterEvent50"):
                opp_val = getattr(value, "esper2Maude_FilterEvent50", None)
                setattr(value, "esper2Maude_FilterEvent50", self)

    @property
    def esper2Maude_SubFilterFollowedBy(self):
        return self.__esper2Maude_SubFilterFollowedBy

    @esper2Maude_SubFilterFollowedBy.setter
    def esper2Maude_SubFilterFollowedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SubFilterFollowedBy__esper2Maude_SubFilterFollowedBy", None)
        self.__esper2Maude_SubFilterFollowedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FollowedBy41"):
                opp_val = getattr(old_value, "esper2Maude_FollowedBy41", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FollowedBy41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FollowedBy41"):
                opp_val = getattr(value, "esper2Maude_FollowedBy41", None)
                setattr(value, "esper2Maude_FollowedBy41", self)

    @property
    def esper2Maude_SubFilterFollowedBy44(self):
        return self.__esper2Maude_SubFilterFollowedBy44

    @esper2Maude_SubFilterFollowedBy44.setter
    def esper2Maude_SubFilterFollowedBy44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SubFilterFollowedBy__esper2Maude_SubFilterFollowedBy44", None)
        self.__esper2Maude_SubFilterFollowedBy44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FollowedBy43"):
                opp_val = getattr(old_value, "esper2Maude_FollowedBy43", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FollowedBy43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FollowedBy43"):
                opp_val = getattr(value, "esper2Maude_FollowedBy43", None)
                setattr(value, "esper2Maude_FollowedBy43", self)

    @property
    def esper2Maude_SubFilterFollowedBy52(self):
        return self.__esper2Maude_SubFilterFollowedBy52

    @esper2Maude_SubFilterFollowedBy52.setter
    def esper2Maude_SubFilterFollowedBy52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_SubFilterFollowedBy__esper2Maude_SubFilterFollowedBy52", None)
        self.__esper2Maude_SubFilterFollowedBy52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Every"):
                opp_val = getattr(old_value, "esper2Maude_Every", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Every", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Every"):
                opp_val = getattr(value, "esper2Maude_Every", None)
                setattr(value, "esper2Maude_Every", self)

class esper2Maude_LogicalOperator:

    def __init__(self, and: str, or: str, esper2Maude_LogicalOperator: "esper2Maude_FilterFrom" = None, esper2Maude_LogicalOperator71: "esper2Maude_FilterOperator" = None):
        self.and = and
        self.or = or
        self.esper2Maude_LogicalOperator = esper2Maude_LogicalOperator
        self.esper2Maude_LogicalOperator71 = esper2Maude_LogicalOperator71
        
    @property
    def and(self) -> str:
        return self.__and

    @and.setter
    def and(self, and: str):
        self.__and = and

    @property
    def or(self) -> str:
        return self.__or

    @or.setter
    def or(self, or: str):
        self.__or = or

    @property
    def esper2Maude_LogicalOperator(self):
        return self.__esper2Maude_LogicalOperator

    @esper2Maude_LogicalOperator.setter
    def esper2Maude_LogicalOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_LogicalOperator__esper2Maude_LogicalOperator", None)
        self.__esper2Maude_LogicalOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom33"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom33", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom33"):
                opp_val = getattr(value, "esper2Maude_FilterFrom33", None)
                setattr(value, "esper2Maude_FilterFrom33", self)

    @property
    def esper2Maude_LogicalOperator71(self):
        return self.__esper2Maude_LogicalOperator71

    @esper2Maude_LogicalOperator71.setter
    def esper2Maude_LogicalOperator71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_LogicalOperator__esper2Maude_LogicalOperator71", None)
        self.__esper2Maude_LogicalOperator71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterOperator70"):
                opp_val = getattr(old_value, "esper2Maude_FilterOperator70", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterOperator70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterOperator70"):
                opp_val = getattr(value, "esper2Maude_FilterOperator70", None)
                setattr(value, "esper2Maude_FilterOperator70", self)

class esper2Maude_FollowedBy:

    pass
class esper2Maude_FilterOperator:

    pass
class esper2Maude_EventProperty:

    def __init__(self, name: str, type: str, esper2Maude_EventProperty: "esper2Maude_Schema" = None, esper2Maude_EventProperty7: "esper2Maude_Schema" = None):
        self.name = name
        self.type = type
        self.esper2Maude_EventProperty = esper2Maude_EventProperty
        self.esper2Maude_EventProperty7 = esper2Maude_EventProperty7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def esper2Maude_EventProperty(self):
        return self.__esper2Maude_EventProperty

    @esper2Maude_EventProperty.setter
    def esper2Maude_EventProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_EventProperty__esper2Maude_EventProperty", None)
        self.__esper2Maude_EventProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Schema4"):
                opp_val = getattr(old_value, "esper2Maude_Schema4", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Schema4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Schema4"):
                opp_val = getattr(value, "esper2Maude_Schema4", None)
                setattr(value, "esper2Maude_Schema4", self)

    @property
    def esper2Maude_EventProperty7(self):
        return self.__esper2Maude_EventProperty7

    @esper2Maude_EventProperty7.setter
    def esper2Maude_EventProperty7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_EventProperty__esper2Maude_EventProperty7", None)
        self.__esper2Maude_EventProperty7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Schema6"):
                opp_val = getattr(old_value, "esper2Maude_Schema6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Schema6"):
                opp_val = getattr(value, "esper2Maude_Schema6", None)
                if opp_val is None:
                    setattr(value, "esper2Maude_Schema6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class esper2Maude_Pattern:

    def __init__(self, name: str, num: int, esper2Maude_Pattern: "esper2Maude_Model" = None, esper2Maude_Pattern9: "esper2Maude_Event" = None, esper2Maude_Pattern11: set["esper2Maude_NonLastSelectEntry"] = None, esper2Maude_Pattern13: "esper2Maude_LastSelectEntry" = None, esper2Maude_Pattern15: "esper2Maude_FilterFrom" = None, esper2Maude_Pattern17: "esper2Maude_Window" = None):
        self.name = name
        self.num = num
        self.esper2Maude_Pattern = esper2Maude_Pattern
        self.esper2Maude_Pattern9 = esper2Maude_Pattern9
        self.esper2Maude_Pattern11 = esper2Maude_Pattern11 if esper2Maude_Pattern11 is not None else set()
        self.esper2Maude_Pattern13 = esper2Maude_Pattern13
        self.esper2Maude_Pattern15 = esper2Maude_Pattern15
        self.esper2Maude_Pattern17 = esper2Maude_Pattern17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def esper2Maude_Pattern15(self):
        return self.__esper2Maude_Pattern15

    @esper2Maude_Pattern15.setter
    def esper2Maude_Pattern15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Pattern__esper2Maude_Pattern15", None)
        self.__esper2Maude_Pattern15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_FilterFrom"):
                opp_val = getattr(old_value, "esper2Maude_FilterFrom", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_FilterFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_FilterFrom"):
                opp_val = getattr(value, "esper2Maude_FilterFrom", None)
                setattr(value, "esper2Maude_FilterFrom", self)

    @property
    def esper2Maude_Pattern(self):
        return self.__esper2Maude_Pattern

    @esper2Maude_Pattern.setter
    def esper2Maude_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Pattern__esper2Maude_Pattern", None)
        self.__esper2Maude_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Model2"):
                opp_val = getattr(old_value, "esper2Maude_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Model2"):
                opp_val = getattr(value, "esper2Maude_Model2", None)
                if opp_val is None:
                    setattr(value, "esper2Maude_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper2Maude_Pattern11(self):
        return self.__esper2Maude_Pattern11

    @esper2Maude_Pattern11.setter
    def esper2Maude_Pattern11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Pattern__esper2Maude_Pattern11", None)
        self.__esper2Maude_Pattern11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper2Maude_NonLastSelectEntry"):
                    opp_val = getattr(item, "esper2Maude_NonLastSelectEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "esper2Maude_NonLastSelectEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper2Maude_NonLastSelectEntry"):
                    opp_val = getattr(item, "esper2Maude_NonLastSelectEntry", None)
                    
                    setattr(item, "esper2Maude_NonLastSelectEntry", self)
                    

    @property
    def esper2Maude_Pattern13(self):
        return self.__esper2Maude_Pattern13

    @esper2Maude_Pattern13.setter
    def esper2Maude_Pattern13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Pattern__esper2Maude_Pattern13", None)
        self.__esper2Maude_Pattern13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_LastSelectEntry"):
                opp_val = getattr(old_value, "esper2Maude_LastSelectEntry", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_LastSelectEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_LastSelectEntry"):
                opp_val = getattr(value, "esper2Maude_LastSelectEntry", None)
                setattr(value, "esper2Maude_LastSelectEntry", self)

    @property
    def esper2Maude_Pattern9(self):
        return self.__esper2Maude_Pattern9

    @esper2Maude_Pattern9.setter
    def esper2Maude_Pattern9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Pattern__esper2Maude_Pattern9", None)
        self.__esper2Maude_Pattern9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Event"):
                opp_val = getattr(old_value, "esper2Maude_Event", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Event"):
                opp_val = getattr(value, "esper2Maude_Event", None)
                setattr(value, "esper2Maude_Event", self)

    @property
    def esper2Maude_Pattern17(self):
        return self.__esper2Maude_Pattern17

    @esper2Maude_Pattern17.setter
    def esper2Maude_Pattern17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Pattern__esper2Maude_Pattern17", None)
        self.__esper2Maude_Pattern17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Window"):
                opp_val = getattr(old_value, "esper2Maude_Window", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_Window", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Window"):
                opp_val = getattr(value, "esper2Maude_Window", None)
                setattr(value, "esper2Maude_Window", self)

class esper2Maude_Schema:

    def __init__(self, name: str, esper2Maude_Schema: "esper2Maude_Model" = None, esper2Maude_Schema4: "esper2Maude_EventProperty" = None, esper2Maude_Schema6: set["esper2Maude_EventProperty"] = None):
        self.name = name
        self.esper2Maude_Schema = esper2Maude_Schema
        self.esper2Maude_Schema4 = esper2Maude_Schema4
        self.esper2Maude_Schema6 = esper2Maude_Schema6 if esper2Maude_Schema6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esper2Maude_Schema4(self):
        return self.__esper2Maude_Schema4

    @esper2Maude_Schema4.setter
    def esper2Maude_Schema4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Schema__esper2Maude_Schema4", None)
        self.__esper2Maude_Schema4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_EventProperty"):
                opp_val = getattr(old_value, "esper2Maude_EventProperty", None)
                if opp_val == self:
                    setattr(old_value, "esper2Maude_EventProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_EventProperty"):
                opp_val = getattr(value, "esper2Maude_EventProperty", None)
                setattr(value, "esper2Maude_EventProperty", self)

    @property
    def esper2Maude_Schema(self):
        return self.__esper2Maude_Schema

    @esper2Maude_Schema.setter
    def esper2Maude_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Schema__esper2Maude_Schema", None)
        self.__esper2Maude_Schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper2Maude_Model"):
                opp_val = getattr(old_value, "esper2Maude_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper2Maude_Model"):
                opp_val = getattr(value, "esper2Maude_Model", None)
                if opp_val is None:
                    setattr(value, "esper2Maude_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper2Maude_Schema6(self):
        return self.__esper2Maude_Schema6

    @esper2Maude_Schema6.setter
    def esper2Maude_Schema6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper2Maude_Schema__esper2Maude_Schema6", None)
        self.__esper2Maude_Schema6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper2Maude_EventProperty7"):
                    opp_val = getattr(item, "esper2Maude_EventProperty7", None)
                    
                    if opp_val == self:
                        setattr(item, "esper2Maude_EventProperty7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper2Maude_EventProperty7"):
                    opp_val = getattr(item, "esper2Maude_EventProperty7", None)
                    
                    setattr(item, "esper2Maude_EventProperty7", self)
                    

class esper2Maude_Model:

    pass