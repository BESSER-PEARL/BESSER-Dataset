from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    gMonthDay = "gMonthDay"
    gDay = "gDay"
    gMonth = "gMonth"
    hexBinary = "hexBinary"
    base64Binary = "base64Binary"
    anyURI = "anyURI"
    data = "data"
    string = "string"
    boolean = "boolean"
    decimal = "decimal"
    int = "int"
    long = "long"
    float = "float"
    double = "double"
    duration = "duration"
    dateTime = "dateTime"
    time = "time"
    date = "date"
    gYearMonth = "gYearMonth"
    gYear = "gYear"


############################################
# Definition of Classes
############################################

class sadl_ValueRow:

    pass
class sadl_OrderElement:

    def __init__(self, order: str, sadl_OrderElement337: "sadl_ResourceName" = None, sadl_OrderElement: "sadl_OrderList" = None):
        self.order = order
        self.sadl_OrderElement337 = sadl_OrderElement337
        self.sadl_OrderElement = sadl_OrderElement
        
    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def sadl_OrderElement337(self):
        return self.__sadl_OrderElement337

    @sadl_OrderElement337.setter
    def sadl_OrderElement337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_OrderElement__sadl_OrderElement337", None)
        self.__sadl_OrderElement337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceName338"):
                opp_val = getattr(old_value, "sadl_ResourceName338", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceName338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceName338"):
                opp_val = getattr(value, "sadl_ResourceName338", None)
                setattr(value, "sadl_ResourceName338", self)

    @property
    def sadl_OrderElement(self):
        return self.__sadl_OrderElement

    @sadl_OrderElement.setter
    def sadl_OrderElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_OrderElement__sadl_OrderElement", None)
        self.__sadl_OrderElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_OrderList335"):
                opp_val = getattr(old_value, "sadl_OrderList335", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_OrderList335"):
                opp_val = getattr(value, "sadl_OrderList335", None)
                if opp_val is None:
                    setattr(value, "sadl_OrderList335", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sadl_ValueTable:

    pass
class sadl_IntervalValue:

    def __init__(self, op: str, sadl_IntervalValue: "sadl_Expression" = None, sadl_IntervalValue388: "sadl_Expression" = None):
        self.op = op
        self.sadl_IntervalValue = sadl_IntervalValue
        self.sadl_IntervalValue388 = sadl_IntervalValue388
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sadl_IntervalValue(self):
        return self.__sadl_IntervalValue

    @sadl_IntervalValue.setter
    def sadl_IntervalValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_IntervalValue__sadl_IntervalValue", None)
        self.__sadl_IntervalValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression348"):
                opp_val = getattr(old_value, "sadl_Expression348", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression348"):
                opp_val = getattr(value, "sadl_Expression348", None)
                setattr(value, "sadl_Expression348", self)

    @property
    def sadl_IntervalValue388(self):
        return self.__sadl_IntervalValue388

    @sadl_IntervalValue388.setter
    def sadl_IntervalValue388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_IntervalValue__sadl_IntervalValue388", None)
        self.__sadl_IntervalValue388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression389"):
                opp_val = getattr(old_value, "sadl_Expression389", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression389"):
                opp_val = getattr(value, "sadl_Expression389", None)
                setattr(value, "sadl_Expression389", self)

class sadl_GraphPattern:

    pass
class sadl_OrderList:

    pass
class Expression:

    pass
class sadl_SelectExpression(Expression):

    def __init__(self, distinct: str, allVars: str, orderby: str, sadl_SelectExpression: "sadl_VariableList" = None, sadl_SelectExpression325: "sadl_OrderList" = None):
        self.distinct = distinct
        self.allVars = allVars
        self.orderby = orderby
        self.sadl_SelectExpression = sadl_SelectExpression
        self.sadl_SelectExpression325 = sadl_SelectExpression325
        
    @property
    def allVars(self) -> str:
        return self.__allVars

    @allVars.setter
    def allVars(self, allVars: str):
        self.__allVars = allVars

    @property
    def distinct(self) -> str:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: str):
        self.__distinct = distinct

    @property
    def orderby(self) -> str:
        return self.__orderby

    @orderby.setter
    def orderby(self, orderby: str):
        self.__orderby = orderby

    @property
    def sadl_SelectExpression325(self):
        return self.__sadl_SelectExpression325

    @sadl_SelectExpression325.setter
    def sadl_SelectExpression325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_SelectExpression__sadl_SelectExpression325", None)
        self.__sadl_SelectExpression325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_OrderList"):
                opp_val = getattr(old_value, "sadl_OrderList", None)
                if opp_val == self:
                    setattr(old_value, "sadl_OrderList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_OrderList"):
                opp_val = getattr(value, "sadl_OrderList", None)
                setattr(value, "sadl_OrderList", self)

    @property
    def sadl_SelectExpression(self):
        return self.__sadl_SelectExpression

    @sadl_SelectExpression.setter
    def sadl_SelectExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_SelectExpression__sadl_SelectExpression", None)
        self.__sadl_SelectExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_VariableList323"):
                opp_val = getattr(old_value, "sadl_VariableList323", None)
                if opp_val == self:
                    setattr(old_value, "sadl_VariableList323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_VariableList323"):
                opp_val = getattr(value, "sadl_VariableList323", None)
                setattr(value, "sadl_VariableList323", self)

class sadl_ConstructExpression(Expression):

    pass
class sadl_JunctionExpression(Expression):

    def __init__(self, op: str, sadl_JunctionExpression: "sadl_Expression" = None, sadl_JunctionExpression407: "sadl_Expression" = None):
        self.op = op
        self.sadl_JunctionExpression = sadl_JunctionExpression
        self.sadl_JunctionExpression407 = sadl_JunctionExpression407
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sadl_JunctionExpression407(self):
        return self.__sadl_JunctionExpression407

    @sadl_JunctionExpression407.setter
    def sadl_JunctionExpression407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_JunctionExpression__sadl_JunctionExpression407", None)
        self.__sadl_JunctionExpression407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression408"):
                opp_val = getattr(old_value, "sadl_Expression408", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression408"):
                opp_val = getattr(value, "sadl_Expression408", None)
                setattr(value, "sadl_Expression408", self)

    @property
    def sadl_JunctionExpression(self):
        return self.__sadl_JunctionExpression

    @sadl_JunctionExpression.setter
    def sadl_JunctionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_JunctionExpression__sadl_JunctionExpression", None)
        self.__sadl_JunctionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression405"):
                opp_val = getattr(old_value, "sadl_Expression405", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression405"):
                opp_val = getattr(value, "sadl_Expression405", None)
                setattr(value, "sadl_Expression405", self)

class sadl_AskQueryExpression(Expression):

    pass
class sadl_UnaryOpExpression(Expression):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class sadl_BinaryOpExpression(Expression):

    def __init__(self, op: str, sadl_BinaryOpExpression: "sadl_Expression" = None, sadl_BinaryOpExpression412: "sadl_Expression" = None):
        self.op = op
        self.sadl_BinaryOpExpression = sadl_BinaryOpExpression
        self.sadl_BinaryOpExpression412 = sadl_BinaryOpExpression412
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sadl_BinaryOpExpression412(self):
        return self.__sadl_BinaryOpExpression412

    @sadl_BinaryOpExpression412.setter
    def sadl_BinaryOpExpression412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_BinaryOpExpression__sadl_BinaryOpExpression412", None)
        self.__sadl_BinaryOpExpression412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression413"):
                opp_val = getattr(old_value, "sadl_Expression413", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression413"):
                opp_val = getattr(value, "sadl_Expression413", None)
                setattr(value, "sadl_Expression413", self)

    @property
    def sadl_BinaryOpExpression(self):
        return self.__sadl_BinaryOpExpression

    @sadl_BinaryOpExpression.setter
    def sadl_BinaryOpExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_BinaryOpExpression__sadl_BinaryOpExpression", None)
        self.__sadl_BinaryOpExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression410"):
                opp_val = getattr(old_value, "sadl_Expression410", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression410"):
                opp_val = getattr(value, "sadl_Expression410", None)
                setattr(value, "sadl_Expression410", self)

class sadl_ElementSet:

    pass
class sadl_Expression:

    def __init__(self, func: str, sadl_Expression: "sadl_Query" = None, sadl_Expression314: "sadl_Test" = None, sadl_Expression316: "sadl_Expr" = None, sadl_Expression321: "sadl_ElementSet" = None, sadl_Expression341: "sadl_Expression" = None, sadl_Expression339: "sadl_Expression" = None, sadl_Expression344: "sadl_Expression" = None, sadl_Expression342: set["sadl_Expression"] = None, sadl_Expression346: "sadl_GraphPattern" = None, sadl_Expression348: "sadl_IntervalValue" = None, sadl_Expression350: "sadl_ExplicitValue" = None, sadl_Expression353: "sadl_ValueTable" = None, sadl_Expression371: "sadl_InstAttrSPV" = None, sadl_Expression386: "sadl_ExistentialNegation" = None, sadl_Expression389: "sadl_IntervalValue" = None, sadl_Expression405: "sadl_JunctionExpression" = None, sadl_Expression408: "sadl_JunctionExpression" = None, sadl_Expression410: "sadl_BinaryOpExpression" = None, sadl_Expression413: "sadl_BinaryOpExpression" = None):
        self.func = func
        self.sadl_Expression = sadl_Expression
        self.sadl_Expression314 = sadl_Expression314
        self.sadl_Expression316 = sadl_Expression316
        self.sadl_Expression321 = sadl_Expression321
        self.sadl_Expression341 = sadl_Expression341
        self.sadl_Expression339 = sadl_Expression339
        self.sadl_Expression344 = sadl_Expression344
        self.sadl_Expression342 = sadl_Expression342 if sadl_Expression342 is not None else set()
        self.sadl_Expression346 = sadl_Expression346
        self.sadl_Expression348 = sadl_Expression348
        self.sadl_Expression350 = sadl_Expression350
        self.sadl_Expression353 = sadl_Expression353
        self.sadl_Expression371 = sadl_Expression371
        self.sadl_Expression386 = sadl_Expression386
        self.sadl_Expression389 = sadl_Expression389
        self.sadl_Expression405 = sadl_Expression405
        self.sadl_Expression408 = sadl_Expression408
        self.sadl_Expression410 = sadl_Expression410
        self.sadl_Expression413 = sadl_Expression413
        
    @property
    def func(self) -> str:
        return self.__func

    @func.setter
    def func(self, func: str):
        self.__func = func

    @property
    def sadl_Expression342(self):
        return self.__sadl_Expression342

    @sadl_Expression342.setter
    def sadl_Expression342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression342", None)
        self.__sadl_Expression342 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_Expression344"):
                    opp_val = getattr(item, "sadl_Expression344", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_Expression344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_Expression344"):
                    opp_val = getattr(item, "sadl_Expression344", None)
                    
                    setattr(item, "sadl_Expression344", self)
                    

    @property
    def sadl_Expression(self):
        return self.__sadl_Expression

    @sadl_Expression.setter
    def sadl_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression", None)
        self.__sadl_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Query"):
                opp_val = getattr(old_value, "sadl_Query", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Query", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Query"):
                opp_val = getattr(value, "sadl_Query", None)
                setattr(value, "sadl_Query", self)

    @property
    def sadl_Expression350(self):
        return self.__sadl_Expression350

    @sadl_Expression350.setter
    def sadl_Expression350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression350", None)
        self.__sadl_Expression350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ExplicitValue351"):
                opp_val = getattr(old_value, "sadl_ExplicitValue351", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ExplicitValue351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ExplicitValue351"):
                opp_val = getattr(value, "sadl_ExplicitValue351", None)
                setattr(value, "sadl_ExplicitValue351", self)

    @property
    def sadl_Expression314(self):
        return self.__sadl_Expression314

    @sadl_Expression314.setter
    def sadl_Expression314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression314", None)
        self.__sadl_Expression314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Test"):
                opp_val = getattr(old_value, "sadl_Test", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Test", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Test"):
                opp_val = getattr(value, "sadl_Test", None)
                setattr(value, "sadl_Test", self)

    @property
    def sadl_Expression410(self):
        return self.__sadl_Expression410

    @sadl_Expression410.setter
    def sadl_Expression410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression410", None)
        self.__sadl_Expression410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_BinaryOpExpression"):
                opp_val = getattr(old_value, "sadl_BinaryOpExpression", None)
                if opp_val == self:
                    setattr(old_value, "sadl_BinaryOpExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_BinaryOpExpression"):
                opp_val = getattr(value, "sadl_BinaryOpExpression", None)
                setattr(value, "sadl_BinaryOpExpression", self)

    @property
    def sadl_Expression413(self):
        return self.__sadl_Expression413

    @sadl_Expression413.setter
    def sadl_Expression413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression413", None)
        self.__sadl_Expression413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_BinaryOpExpression412"):
                opp_val = getattr(old_value, "sadl_BinaryOpExpression412", None)
                if opp_val == self:
                    setattr(old_value, "sadl_BinaryOpExpression412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_BinaryOpExpression412"):
                opp_val = getattr(value, "sadl_BinaryOpExpression412", None)
                setattr(value, "sadl_BinaryOpExpression412", self)

    @property
    def sadl_Expression408(self):
        return self.__sadl_Expression408

    @sadl_Expression408.setter
    def sadl_Expression408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression408", None)
        self.__sadl_Expression408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_JunctionExpression407"):
                opp_val = getattr(old_value, "sadl_JunctionExpression407", None)
                if opp_val == self:
                    setattr(old_value, "sadl_JunctionExpression407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_JunctionExpression407"):
                opp_val = getattr(value, "sadl_JunctionExpression407", None)
                setattr(value, "sadl_JunctionExpression407", self)

    @property
    def sadl_Expression348(self):
        return self.__sadl_Expression348

    @sadl_Expression348.setter
    def sadl_Expression348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression348", None)
        self.__sadl_Expression348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_IntervalValue"):
                opp_val = getattr(old_value, "sadl_IntervalValue", None)
                if opp_val == self:
                    setattr(old_value, "sadl_IntervalValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_IntervalValue"):
                opp_val = getattr(value, "sadl_IntervalValue", None)
                setattr(value, "sadl_IntervalValue", self)

    @property
    def sadl_Expression316(self):
        return self.__sadl_Expression316

    @sadl_Expression316.setter
    def sadl_Expression316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression316", None)
        self.__sadl_Expression316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expr"):
                opp_val = getattr(old_value, "sadl_Expr", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expr"):
                opp_val = getattr(value, "sadl_Expr", None)
                setattr(value, "sadl_Expr", self)

    @property
    def sadl_Expression371(self):
        return self.__sadl_Expression371

    @sadl_Expression371.setter
    def sadl_Expression371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression371", None)
        self.__sadl_Expression371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_InstAttrSPV370"):
                opp_val = getattr(old_value, "sadl_InstAttrSPV370", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_InstAttrSPV370"):
                opp_val = getattr(value, "sadl_InstAttrSPV370", None)
                if opp_val is None:
                    setattr(value, "sadl_InstAttrSPV370", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_Expression389(self):
        return self.__sadl_Expression389

    @sadl_Expression389.setter
    def sadl_Expression389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression389", None)
        self.__sadl_Expression389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_IntervalValue388"):
                opp_val = getattr(old_value, "sadl_IntervalValue388", None)
                if opp_val == self:
                    setattr(old_value, "sadl_IntervalValue388", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_IntervalValue388"):
                opp_val = getattr(value, "sadl_IntervalValue388", None)
                setattr(value, "sadl_IntervalValue388", self)

    @property
    def sadl_Expression339(self):
        return self.__sadl_Expression339

    @sadl_Expression339.setter
    def sadl_Expression339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression339", None)
        self.__sadl_Expression339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression341"):
                opp_val = getattr(old_value, "sadl_Expression341", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression341"):
                opp_val = getattr(value, "sadl_Expression341", None)
                setattr(value, "sadl_Expression341", self)

    @property
    def sadl_Expression341(self):
        return self.__sadl_Expression341

    @sadl_Expression341.setter
    def sadl_Expression341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression341", None)
        self.__sadl_Expression341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression339"):
                opp_val = getattr(old_value, "sadl_Expression339", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression339"):
                opp_val = getattr(value, "sadl_Expression339", None)
                setattr(value, "sadl_Expression339", self)

    @property
    def sadl_Expression346(self):
        return self.__sadl_Expression346

    @sadl_Expression346.setter
    def sadl_Expression346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression346", None)
        self.__sadl_Expression346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_GraphPattern"):
                opp_val = getattr(old_value, "sadl_GraphPattern", None)
                if opp_val == self:
                    setattr(old_value, "sadl_GraphPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_GraphPattern"):
                opp_val = getattr(value, "sadl_GraphPattern", None)
                setattr(value, "sadl_GraphPattern", self)

    @property
    def sadl_Expression321(self):
        return self.__sadl_Expression321

    @sadl_Expression321.setter
    def sadl_Expression321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression321", None)
        self.__sadl_Expression321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ElementSet320"):
                opp_val = getattr(old_value, "sadl_ElementSet320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ElementSet320"):
                opp_val = getattr(value, "sadl_ElementSet320", None)
                if opp_val is None:
                    setattr(value, "sadl_ElementSet320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_Expression344(self):
        return self.__sadl_Expression344

    @sadl_Expression344.setter
    def sadl_Expression344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression344", None)
        self.__sadl_Expression344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression342"):
                opp_val = getattr(old_value, "sadl_Expression342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression342"):
                opp_val = getattr(value, "sadl_Expression342", None)
                if opp_val is None:
                    setattr(value, "sadl_Expression342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_Expression405(self):
        return self.__sadl_Expression405

    @sadl_Expression405.setter
    def sadl_Expression405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression405", None)
        self.__sadl_Expression405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_JunctionExpression"):
                opp_val = getattr(old_value, "sadl_JunctionExpression", None)
                if opp_val == self:
                    setattr(old_value, "sadl_JunctionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_JunctionExpression"):
                opp_val = getattr(value, "sadl_JunctionExpression", None)
                setattr(value, "sadl_JunctionExpression", self)

    @property
    def sadl_Expression386(self):
        return self.__sadl_Expression386

    @sadl_Expression386.setter
    def sadl_Expression386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression386", None)
        self.__sadl_Expression386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ExistentialNegation385"):
                opp_val = getattr(old_value, "sadl_ExistentialNegation385", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ExistentialNegation385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ExistentialNegation385"):
                opp_val = getattr(value, "sadl_ExistentialNegation385", None)
                setattr(value, "sadl_ExistentialNegation385", self)

    @property
    def sadl_Expression353(self):
        return self.__sadl_Expression353

    @sadl_Expression353.setter
    def sadl_Expression353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Expression__sadl_Expression353", None)
        self.__sadl_Expression353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ValueTable"):
                opp_val = getattr(old_value, "sadl_ValueTable", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ValueTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ValueTable"):
                opp_val = getattr(value, "sadl_ValueTable", None)
                setattr(value, "sadl_ValueTable", self)

class GraphPattern:

    pass
class sadl_InstAttrSPV(GraphPattern):

    pass
class sadl_ExistentialNegation(GraphPattern):

    pass
class sadl_PropOfSubj(GraphPattern):

    pass
class sadl_SubTypeOf(GraphPattern):

    pass
class sadl_InstAttrPSV(GraphPattern):

    pass
class sadl_SubjProp(GraphPattern):

    pass
class sadl_MergedTriples(GraphPattern):

    pass
class sadl_EmbeddedInstanceDeclaration:

    pass
class sadl_VariableList:

    pass
class sadl_WithPhrase:

    pass
class sadl_WithChain:

    pass
class sadl_OfPhrase:

    def __init__(self, article: str, sadl_OfPhrase: "sadl_OfPatternReturningValues" = None, sadl_OfPhrase293: "sadl_MergedTriples" = None, sadl_OfPhrase301: "sadl_ResourceByName" = None, sadl_OfPhrase355: "sadl_PropOfSubj" = None):
        self.article = article
        self.sadl_OfPhrase = sadl_OfPhrase
        self.sadl_OfPhrase293 = sadl_OfPhrase293
        self.sadl_OfPhrase301 = sadl_OfPhrase301
        self.sadl_OfPhrase355 = sadl_OfPhrase355
        
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def sadl_OfPhrase301(self):
        return self.__sadl_OfPhrase301

    @sadl_OfPhrase301.setter
    def sadl_OfPhrase301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_OfPhrase__sadl_OfPhrase301", None)
        self.__sadl_OfPhrase301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByName302"):
                opp_val = getattr(old_value, "sadl_ResourceByName302", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceByName302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByName302"):
                opp_val = getattr(value, "sadl_ResourceByName302", None)
                setattr(value, "sadl_ResourceByName302", self)

    @property
    def sadl_OfPhrase355(self):
        return self.__sadl_OfPhrase355

    @sadl_OfPhrase355.setter
    def sadl_OfPhrase355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_OfPhrase__sadl_OfPhrase355", None)
        self.__sadl_OfPhrase355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropOfSubj"):
                opp_val = getattr(old_value, "sadl_PropOfSubj", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropOfSubj"):
                opp_val = getattr(value, "sadl_PropOfSubj", None)
                if opp_val is None:
                    setattr(value, "sadl_PropOfSubj", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_OfPhrase293(self):
        return self.__sadl_OfPhrase293

    @sadl_OfPhrase293.setter
    def sadl_OfPhrase293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_OfPhrase__sadl_OfPhrase293", None)
        self.__sadl_OfPhrase293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_MergedTriples"):
                opp_val = getattr(old_value, "sadl_MergedTriples", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_MergedTriples"):
                opp_val = getattr(value, "sadl_MergedTriples", None)
                if opp_val is None:
                    setattr(value, "sadl_MergedTriples", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_OfPhrase(self):
        return self.__sadl_OfPhrase

    @sadl_OfPhrase.setter
    def sadl_OfPhrase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_OfPhrase__sadl_OfPhrase", None)
        self.__sadl_OfPhrase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_OfPatternReturningValues278"):
                opp_val = getattr(old_value, "sadl_OfPatternReturningValues278", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_OfPatternReturningValues278"):
                opp_val = getattr(value, "sadl_OfPatternReturningValues278", None)
                if opp_val is None:
                    setattr(value, "sadl_OfPatternReturningValues278", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sadl_Object:

    pass
class sadl_OfPatternReturningValues:

    pass
class sadl_TypeDeclaration:

    pass
class EmbeddedInstanceDeclaration:

    pass
class InstanceDeclarationStatement:

    pass
class sadl_InstanceDeclaration(InstanceDeclarationStatement, EmbeddedInstanceDeclaration):

    def __init__(self, article: str, sadl_InstanceDeclaration: "sadl_TypeDeclaration" = None, sadl_InstanceDeclaration236: set["sadl_PropValPartialTriple"] = None, sadl_InstanceDeclaration238: "sadl_ResourceByName" = None, sadl_InstanceDeclaration241: "sadl_ResourceName" = None, sadl_InstanceDeclaration276: "sadl_PropValPartialTriple" = None):
        self.article = article
        self.sadl_InstanceDeclaration = sadl_InstanceDeclaration
        self.sadl_InstanceDeclaration236 = sadl_InstanceDeclaration236 if sadl_InstanceDeclaration236 is not None else set()
        self.sadl_InstanceDeclaration238 = sadl_InstanceDeclaration238
        self.sadl_InstanceDeclaration241 = sadl_InstanceDeclaration241
        self.sadl_InstanceDeclaration276 = sadl_InstanceDeclaration276
        
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def sadl_InstanceDeclaration276(self):
        return self.__sadl_InstanceDeclaration276

    @sadl_InstanceDeclaration276.setter
    def sadl_InstanceDeclaration276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_InstanceDeclaration__sadl_InstanceDeclaration276", None)
        self.__sadl_InstanceDeclaration276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropValPartialTriple275"):
                opp_val = getattr(old_value, "sadl_PropValPartialTriple275", None)
                if opp_val == self:
                    setattr(old_value, "sadl_PropValPartialTriple275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropValPartialTriple275"):
                opp_val = getattr(value, "sadl_PropValPartialTriple275", None)
                setattr(value, "sadl_PropValPartialTriple275", self)

    @property
    def sadl_InstanceDeclaration236(self):
        return self.__sadl_InstanceDeclaration236

    @sadl_InstanceDeclaration236.setter
    def sadl_InstanceDeclaration236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_InstanceDeclaration__sadl_InstanceDeclaration236", None)
        self.__sadl_InstanceDeclaration236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_PropValPartialTriple"):
                    opp_val = getattr(item, "sadl_PropValPartialTriple", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_PropValPartialTriple", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_PropValPartialTriple"):
                    opp_val = getattr(item, "sadl_PropValPartialTriple", None)
                    
                    setattr(item, "sadl_PropValPartialTriple", self)
                    

    @property
    def sadl_InstanceDeclaration(self):
        return self.__sadl_InstanceDeclaration

    @sadl_InstanceDeclaration.setter
    def sadl_InstanceDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_InstanceDeclaration__sadl_InstanceDeclaration", None)
        self.__sadl_InstanceDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_TypeDeclaration"):
                opp_val = getattr(old_value, "sadl_TypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "sadl_TypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_TypeDeclaration"):
                opp_val = getattr(value, "sadl_TypeDeclaration", None)
                setattr(value, "sadl_TypeDeclaration", self)

    @property
    def sadl_InstanceDeclaration238(self):
        return self.__sadl_InstanceDeclaration238

    @sadl_InstanceDeclaration238.setter
    def sadl_InstanceDeclaration238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_InstanceDeclaration__sadl_InstanceDeclaration238", None)
        self.__sadl_InstanceDeclaration238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByName239"):
                opp_val = getattr(old_value, "sadl_ResourceByName239", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceByName239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByName239"):
                opp_val = getattr(value, "sadl_ResourceByName239", None)
                setattr(value, "sadl_ResourceByName239", self)

    @property
    def sadl_InstanceDeclaration241(self):
        return self.__sadl_InstanceDeclaration241

    @sadl_InstanceDeclaration241.setter
    def sadl_InstanceDeclaration241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_InstanceDeclaration__sadl_InstanceDeclaration241", None)
        self.__sadl_InstanceDeclaration241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceName242"):
                opp_val = getattr(old_value, "sadl_ResourceName242", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceName242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceName242"):
                opp_val = getattr(value, "sadl_ResourceName242", None)
                setattr(value, "sadl_ResourceName242", self)

class sadl_PropValPartialTriple:

    pass
class sadl_IsInverseOf:

    pass
class sadl_TypedBNode:

    def __init__(self, article: str, sadl_TypedBNode: "sadl_NecessaryAndSufficient" = None, sadl_TypedBNode248: "sadl_TypeDeclaration" = None, sadl_TypedBNode232: "sadl_ResourceIdentifier" = None, sadl_TypedBNode284: "sadl_OfPatternReturningValues" = None, sadl_TypedBNode296: "sadl_MergedTriples" = None):
        self.article = article
        self.sadl_TypedBNode = sadl_TypedBNode
        self.sadl_TypedBNode248 = sadl_TypedBNode248
        self.sadl_TypedBNode232 = sadl_TypedBNode232
        self.sadl_TypedBNode284 = sadl_TypedBNode284
        self.sadl_TypedBNode296 = sadl_TypedBNode296
        
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def sadl_TypedBNode248(self):
        return self.__sadl_TypedBNode248

    @sadl_TypedBNode248.setter
    def sadl_TypedBNode248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_TypedBNode__sadl_TypedBNode248", None)
        self.__sadl_TypedBNode248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_TypeDeclaration247"):
                opp_val = getattr(old_value, "sadl_TypeDeclaration247", None)
                if opp_val == self:
                    setattr(old_value, "sadl_TypeDeclaration247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_TypeDeclaration247"):
                opp_val = getattr(value, "sadl_TypeDeclaration247", None)
                setattr(value, "sadl_TypeDeclaration247", self)

    @property
    def sadl_TypedBNode(self):
        return self.__sadl_TypedBNode

    @sadl_TypedBNode.setter
    def sadl_TypedBNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_TypedBNode__sadl_TypedBNode", None)
        self.__sadl_TypedBNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_NecessaryAndSufficient"):
                opp_val = getattr(old_value, "sadl_NecessaryAndSufficient", None)
                if opp_val == self:
                    setattr(old_value, "sadl_NecessaryAndSufficient", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_NecessaryAndSufficient"):
                opp_val = getattr(value, "sadl_NecessaryAndSufficient", None)
                setattr(value, "sadl_NecessaryAndSufficient", self)

    @property
    def sadl_TypedBNode296(self):
        return self.__sadl_TypedBNode296

    @sadl_TypedBNode296.setter
    def sadl_TypedBNode296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_TypedBNode__sadl_TypedBNode296", None)
        self.__sadl_TypedBNode296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_MergedTriples295"):
                opp_val = getattr(old_value, "sadl_MergedTriples295", None)
                if opp_val == self:
                    setattr(old_value, "sadl_MergedTriples295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_MergedTriples295"):
                opp_val = getattr(value, "sadl_MergedTriples295", None)
                setattr(value, "sadl_MergedTriples295", self)

    @property
    def sadl_TypedBNode284(self):
        return self.__sadl_TypedBNode284

    @sadl_TypedBNode284.setter
    def sadl_TypedBNode284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_TypedBNode__sadl_TypedBNode284", None)
        self.__sadl_TypedBNode284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_OfPatternReturningValues283"):
                opp_val = getattr(old_value, "sadl_OfPatternReturningValues283", None)
                if opp_val == self:
                    setattr(old_value, "sadl_OfPatternReturningValues283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_OfPatternReturningValues283"):
                opp_val = getattr(value, "sadl_OfPatternReturningValues283", None)
                setattr(value, "sadl_OfPatternReturningValues283", self)

    @property
    def sadl_TypedBNode232(self):
        return self.__sadl_TypedBNode232

    @sadl_TypedBNode232.setter
    def sadl_TypedBNode232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_TypedBNode__sadl_TypedBNode232", None)
        self.__sadl_TypedBNode232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier233"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier233", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier233"):
                opp_val = getattr(value, "sadl_ResourceIdentifier233", None)
                setattr(value, "sadl_ResourceIdentifier233", self)

class sadl_AdditionalPropertyInfo:

    def __init__(self, isfunc: str, isinvfunc: str, isSym: str, isTrans: str, sadl_AdditionalPropertyInfo: "sadl_PropertyDeclaration" = None, sadl_AdditionalPropertyInfo208: "sadl_Condition" = None, sadl_AdditionalPropertyInfo211: "sadl_Range" = None, sadl_AdditionalPropertyInfo205: "sadl_ResourceIdentifier" = None, sadl_AdditionalPropertyInfo214: "sadl_IsInverseOf" = None):
        self.isfunc = isfunc
        self.isinvfunc = isinvfunc
        self.isSym = isSym
        self.isTrans = isTrans
        self.sadl_AdditionalPropertyInfo = sadl_AdditionalPropertyInfo
        self.sadl_AdditionalPropertyInfo208 = sadl_AdditionalPropertyInfo208
        self.sadl_AdditionalPropertyInfo211 = sadl_AdditionalPropertyInfo211
        self.sadl_AdditionalPropertyInfo205 = sadl_AdditionalPropertyInfo205
        self.sadl_AdditionalPropertyInfo214 = sadl_AdditionalPropertyInfo214
        
    @property
    def isTrans(self) -> str:
        return self.__isTrans

    @isTrans.setter
    def isTrans(self, isTrans: str):
        self.__isTrans = isTrans

    @property
    def isfunc(self) -> str:
        return self.__isfunc

    @isfunc.setter
    def isfunc(self, isfunc: str):
        self.__isfunc = isfunc

    @property
    def isinvfunc(self) -> str:
        return self.__isinvfunc

    @isinvfunc.setter
    def isinvfunc(self, isinvfunc: str):
        self.__isinvfunc = isinvfunc

    @property
    def isSym(self) -> str:
        return self.__isSym

    @isSym.setter
    def isSym(self, isSym: str):
        self.__isSym = isSym

    @property
    def sadl_AdditionalPropertyInfo205(self):
        return self.__sadl_AdditionalPropertyInfo205

    @sadl_AdditionalPropertyInfo205.setter
    def sadl_AdditionalPropertyInfo205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_AdditionalPropertyInfo__sadl_AdditionalPropertyInfo205", None)
        self.__sadl_AdditionalPropertyInfo205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier206"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier206", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier206"):
                opp_val = getattr(value, "sadl_ResourceIdentifier206", None)
                setattr(value, "sadl_ResourceIdentifier206", self)

    @property
    def sadl_AdditionalPropertyInfo208(self):
        return self.__sadl_AdditionalPropertyInfo208

    @sadl_AdditionalPropertyInfo208.setter
    def sadl_AdditionalPropertyInfo208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_AdditionalPropertyInfo__sadl_AdditionalPropertyInfo208", None)
        self.__sadl_AdditionalPropertyInfo208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Condition209"):
                opp_val = getattr(old_value, "sadl_Condition209", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Condition209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Condition209"):
                opp_val = getattr(value, "sadl_Condition209", None)
                setattr(value, "sadl_Condition209", self)

    @property
    def sadl_AdditionalPropertyInfo211(self):
        return self.__sadl_AdditionalPropertyInfo211

    @sadl_AdditionalPropertyInfo211.setter
    def sadl_AdditionalPropertyInfo211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_AdditionalPropertyInfo__sadl_AdditionalPropertyInfo211", None)
        self.__sadl_AdditionalPropertyInfo211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Range212"):
                opp_val = getattr(old_value, "sadl_Range212", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Range212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Range212"):
                opp_val = getattr(value, "sadl_Range212", None)
                setattr(value, "sadl_Range212", self)

    @property
    def sadl_AdditionalPropertyInfo214(self):
        return self.__sadl_AdditionalPropertyInfo214

    @sadl_AdditionalPropertyInfo214.setter
    def sadl_AdditionalPropertyInfo214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_AdditionalPropertyInfo__sadl_AdditionalPropertyInfo214", None)
        self.__sadl_AdditionalPropertyInfo214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_IsInverseOf"):
                opp_val = getattr(old_value, "sadl_IsInverseOf", None)
                if opp_val == self:
                    setattr(old_value, "sadl_IsInverseOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_IsInverseOf"):
                opp_val = getattr(value, "sadl_IsInverseOf", None)
                setattr(value, "sadl_IsInverseOf", self)

    @property
    def sadl_AdditionalPropertyInfo(self):
        return self.__sadl_AdditionalPropertyInfo

    @sadl_AdditionalPropertyInfo.setter
    def sadl_AdditionalPropertyInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_AdditionalPropertyInfo__sadl_AdditionalPropertyInfo", None)
        self.__sadl_AdditionalPropertyInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropertyDeclaration194"):
                opp_val = getattr(old_value, "sadl_PropertyDeclaration194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropertyDeclaration194"):
                opp_val = getattr(value, "sadl_PropertyDeclaration194", None)
                if opp_val is None:
                    setattr(value, "sadl_PropertyDeclaration194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sadl_ExplicitValue:

    def __init__(self, valueList: str, term: str, sadl_ExplicitValue: "sadl_DefaultValue" = None, sadl_ExplicitValue168: "sadl_HasValueCondition" = None, sadl_ExplicitValue273: "sadl_PropValPartialTriple" = None, sadl_ExplicitValue351: "sadl_Expression" = None, sadl_ExplicitValue376: "sadl_InstAttrPSV" = None, sadl_ExplicitValue391: "sadl_ResourceByName" = None, sadl_ExplicitValue394: "sadl_LiteralValue" = None, sadl_ExplicitValue397: "sadl_ValueRow" = None, sadl_ExplicitValue403: "sadl_ValueRow" = None):
        self.valueList = valueList
        self.term = term
        self.sadl_ExplicitValue = sadl_ExplicitValue
        self.sadl_ExplicitValue168 = sadl_ExplicitValue168
        self.sadl_ExplicitValue273 = sadl_ExplicitValue273
        self.sadl_ExplicitValue351 = sadl_ExplicitValue351
        self.sadl_ExplicitValue376 = sadl_ExplicitValue376
        self.sadl_ExplicitValue391 = sadl_ExplicitValue391
        self.sadl_ExplicitValue394 = sadl_ExplicitValue394
        self.sadl_ExplicitValue397 = sadl_ExplicitValue397
        self.sadl_ExplicitValue403 = sadl_ExplicitValue403
        
    @property
    def valueList(self) -> str:
        return self.__valueList

    @valueList.setter
    def valueList(self, valueList: str):
        self.__valueList = valueList

    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

    @property
    def sadl_ExplicitValue397(self):
        return self.__sadl_ExplicitValue397

    @sadl_ExplicitValue397.setter
    def sadl_ExplicitValue397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue397", None)
        self.__sadl_ExplicitValue397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ValueRow"):
                opp_val = getattr(old_value, "sadl_ValueRow", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ValueRow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ValueRow"):
                opp_val = getattr(value, "sadl_ValueRow", None)
                setattr(value, "sadl_ValueRow", self)

    @property
    def sadl_ExplicitValue273(self):
        return self.__sadl_ExplicitValue273

    @sadl_ExplicitValue273.setter
    def sadl_ExplicitValue273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue273", None)
        self.__sadl_ExplicitValue273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropValPartialTriple272"):
                opp_val = getattr(old_value, "sadl_PropValPartialTriple272", None)
                if opp_val == self:
                    setattr(old_value, "sadl_PropValPartialTriple272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropValPartialTriple272"):
                opp_val = getattr(value, "sadl_PropValPartialTriple272", None)
                setattr(value, "sadl_PropValPartialTriple272", self)

    @property
    def sadl_ExplicitValue168(self):
        return self.__sadl_ExplicitValue168

    @sadl_ExplicitValue168.setter
    def sadl_ExplicitValue168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue168", None)
        self.__sadl_ExplicitValue168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_HasValueCondition167"):
                opp_val = getattr(old_value, "sadl_HasValueCondition167", None)
                if opp_val == self:
                    setattr(old_value, "sadl_HasValueCondition167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_HasValueCondition167"):
                opp_val = getattr(value, "sadl_HasValueCondition167", None)
                setattr(value, "sadl_HasValueCondition167", self)

    @property
    def sadl_ExplicitValue(self):
        return self.__sadl_ExplicitValue

    @sadl_ExplicitValue.setter
    def sadl_ExplicitValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue", None)
        self.__sadl_ExplicitValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_DefaultValue162"):
                opp_val = getattr(old_value, "sadl_DefaultValue162", None)
                if opp_val == self:
                    setattr(old_value, "sadl_DefaultValue162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_DefaultValue162"):
                opp_val = getattr(value, "sadl_DefaultValue162", None)
                setattr(value, "sadl_DefaultValue162", self)

    @property
    def sadl_ExplicitValue351(self):
        return self.__sadl_ExplicitValue351

    @sadl_ExplicitValue351.setter
    def sadl_ExplicitValue351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue351", None)
        self.__sadl_ExplicitValue351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Expression350"):
                opp_val = getattr(old_value, "sadl_Expression350", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Expression350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Expression350"):
                opp_val = getattr(value, "sadl_Expression350", None)
                setattr(value, "sadl_Expression350", self)

    @property
    def sadl_ExplicitValue403(self):
        return self.__sadl_ExplicitValue403

    @sadl_ExplicitValue403.setter
    def sadl_ExplicitValue403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue403", None)
        self.__sadl_ExplicitValue403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ValueRow402"):
                opp_val = getattr(old_value, "sadl_ValueRow402", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ValueRow402"):
                opp_val = getattr(value, "sadl_ValueRow402", None)
                if opp_val is None:
                    setattr(value, "sadl_ValueRow402", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_ExplicitValue391(self):
        return self.__sadl_ExplicitValue391

    @sadl_ExplicitValue391.setter
    def sadl_ExplicitValue391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue391", None)
        self.__sadl_ExplicitValue391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByName392"):
                opp_val = getattr(old_value, "sadl_ResourceByName392", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceByName392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByName392"):
                opp_val = getattr(value, "sadl_ResourceByName392", None)
                setattr(value, "sadl_ResourceByName392", self)

    @property
    def sadl_ExplicitValue394(self):
        return self.__sadl_ExplicitValue394

    @sadl_ExplicitValue394.setter
    def sadl_ExplicitValue394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue394", None)
        self.__sadl_ExplicitValue394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_LiteralValue395"):
                opp_val = getattr(old_value, "sadl_LiteralValue395", None)
                if opp_val == self:
                    setattr(old_value, "sadl_LiteralValue395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_LiteralValue395"):
                opp_val = getattr(value, "sadl_LiteralValue395", None)
                setattr(value, "sadl_LiteralValue395", self)

    @property
    def sadl_ExplicitValue376(self):
        return self.__sadl_ExplicitValue376

    @sadl_ExplicitValue376.setter
    def sadl_ExplicitValue376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ExplicitValue__sadl_ExplicitValue376", None)
        self.__sadl_ExplicitValue376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_InstAttrPSV375"):
                opp_val = getattr(old_value, "sadl_InstAttrPSV375", None)
                if opp_val == self:
                    setattr(old_value, "sadl_InstAttrPSV375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_InstAttrPSV375"):
                opp_val = getattr(value, "sadl_InstAttrPSV375", None)
                setattr(value, "sadl_InstAttrPSV375", self)

class Condition:

    pass
class sadl_EObject:

    pass
class sadl_MinCardCondition(Condition):

    def __init__(self, card: str, sadl_MinCardCondition: "sadl_MinCardinality" = None, sadl_MinCardCondition170: "sadl_ResourceIdentifier" = None):
        self.card = card
        self.sadl_MinCardCondition = sadl_MinCardCondition
        self.sadl_MinCardCondition170 = sadl_MinCardCondition170
        
    @property
    def card(self) -> str:
        return self.__card

    @card.setter
    def card(self, card: str):
        self.__card = card

    @property
    def sadl_MinCardCondition(self):
        return self.__sadl_MinCardCondition

    @sadl_MinCardCondition.setter
    def sadl_MinCardCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_MinCardCondition__sadl_MinCardCondition", None)
        self.__sadl_MinCardCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_MinCardinality124"):
                opp_val = getattr(old_value, "sadl_MinCardinality124", None)
                if opp_val == self:
                    setattr(old_value, "sadl_MinCardinality124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_MinCardinality124"):
                opp_val = getattr(value, "sadl_MinCardinality124", None)
                setattr(value, "sadl_MinCardinality124", self)

    @property
    def sadl_MinCardCondition170(self):
        return self.__sadl_MinCardCondition170

    @sadl_MinCardCondition170.setter
    def sadl_MinCardCondition170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_MinCardCondition__sadl_MinCardCondition170", None)
        self.__sadl_MinCardCondition170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier171"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier171", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier171"):
                opp_val = getattr(value, "sadl_ResourceIdentifier171", None)
                setattr(value, "sadl_ResourceIdentifier171", self)

class sadl_MaxCardCondition(Condition):

    def __init__(self, card: str, sadl_MaxCardCondition: "sadl_MaxCardinality" = None, sadl_MaxCardCondition173: "sadl_ResourceIdentifier" = None):
        self.card = card
        self.sadl_MaxCardCondition = sadl_MaxCardCondition
        self.sadl_MaxCardCondition173 = sadl_MaxCardCondition173
        
    @property
    def card(self) -> str:
        return self.__card

    @card.setter
    def card(self, card: str):
        self.__card = card

    @property
    def sadl_MaxCardCondition173(self):
        return self.__sadl_MaxCardCondition173

    @sadl_MaxCardCondition173.setter
    def sadl_MaxCardCondition173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_MaxCardCondition__sadl_MaxCardCondition173", None)
        self.__sadl_MaxCardCondition173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier174"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier174", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier174"):
                opp_val = getattr(value, "sadl_ResourceIdentifier174", None)
                setattr(value, "sadl_ResourceIdentifier174", self)

    @property
    def sadl_MaxCardCondition(self):
        return self.__sadl_MaxCardCondition

    @sadl_MaxCardCondition.setter
    def sadl_MaxCardCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_MaxCardCondition__sadl_MaxCardCondition", None)
        self.__sadl_MaxCardCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_MaxCardinality134"):
                opp_val = getattr(old_value, "sadl_MaxCardinality134", None)
                if opp_val == self:
                    setattr(old_value, "sadl_MaxCardinality134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_MaxCardinality134"):
                opp_val = getattr(value, "sadl_MaxCardinality134", None)
                setattr(value, "sadl_MaxCardinality134", self)

class sadl_HasValueCondition(Condition):

    pass
class sadl_CardCondition(Condition):

    def __init__(self, card: str, sadl_CardCondition: "sadl_Cardinality" = None, sadl_CardCondition176: "sadl_ResourceIdentifier" = None):
        self.card = card
        self.sadl_CardCondition = sadl_CardCondition
        self.sadl_CardCondition176 = sadl_CardCondition176
        
    @property
    def card(self) -> str:
        return self.__card

    @card.setter
    def card(self, card: str):
        self.__card = card

    @property
    def sadl_CardCondition(self):
        return self.__sadl_CardCondition

    @sadl_CardCondition.setter
    def sadl_CardCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_CardCondition__sadl_CardCondition", None)
        self.__sadl_CardCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Cardinality114"):
                opp_val = getattr(old_value, "sadl_Cardinality114", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Cardinality114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Cardinality114"):
                opp_val = getattr(value, "sadl_Cardinality114", None)
                setattr(value, "sadl_Cardinality114", self)

    @property
    def sadl_CardCondition176(self):
        return self.__sadl_CardCondition176

    @sadl_CardCondition176.setter
    def sadl_CardCondition176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_CardCondition__sadl_CardCondition176", None)
        self.__sadl_CardCondition176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier177"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier177", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier177"):
                opp_val = getattr(value, "sadl_ResourceIdentifier177", None)
                setattr(value, "sadl_ResourceIdentifier177", self)

class sadl_SomeValuesCondition(Condition):

    pass
class sadl_AllValuesCondition(Condition):

    pass
class sadl_PropertyOfClass:

    pass
class sadl_Facets:

    def __init__(self, minexin: str, min: str, max: str, maxexin: str, regex: str, len: str, minlen: str, maxlen: str, values: str, sadl_Facets: "sadl_DataTypeRestriction" = None):
        self.minexin = minexin
        self.min = min
        self.max = max
        self.maxexin = maxexin
        self.regex = regex
        self.len = len
        self.minlen = minlen
        self.maxlen = maxlen
        self.values = values
        self.sadl_Facets = sadl_Facets
        
    @property
    def len(self) -> str:
        return self.__len

    @len.setter
    def len(self, len: str):
        self.__len = len

    @property
    def maxexin(self) -> str:
        return self.__maxexin

    @maxexin.setter
    def maxexin(self, maxexin: str):
        self.__maxexin = maxexin

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def maxlen(self) -> str:
        return self.__maxlen

    @maxlen.setter
    def maxlen(self, maxlen: str):
        self.__maxlen = maxlen

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def regex(self) -> str:
        return self.__regex

    @regex.setter
    def regex(self, regex: str):
        self.__regex = regex

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def minexin(self) -> str:
        return self.__minexin

    @minexin.setter
    def minexin(self, minexin: str):
        self.__minexin = minexin

    @property
    def minlen(self) -> str:
        return self.__minlen

    @minlen.setter
    def minlen(self, minlen: str):
        self.__minlen = minlen

    @property
    def sadl_Facets(self):
        return self.__sadl_Facets

    @sadl_Facets.setter
    def sadl_Facets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Facets__sadl_Facets", None)
        self.__sadl_Facets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_DataTypeRestriction63"):
                opp_val = getattr(old_value, "sadl_DataTypeRestriction63", None)
                if opp_val == self:
                    setattr(old_value, "sadl_DataTypeRestriction63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_DataTypeRestriction63"):
                opp_val = getattr(value, "sadl_DataTypeRestriction63", None)
                setattr(value, "sadl_DataTypeRestriction63", self)

class sadl_DataTypeRestriction:

    def __init__(self, basetypes: str, basetype: str, sadl_DataTypeRestriction: "sadl_UserDefinedDataType" = None, sadl_DataTypeRestriction63: "sadl_Facets" = None):
        self.basetypes = basetypes
        self.basetype = basetype
        self.sadl_DataTypeRestriction = sadl_DataTypeRestriction
        self.sadl_DataTypeRestriction63 = sadl_DataTypeRestriction63
        
    @property
    def basetype(self) -> str:
        return self.__basetype

    @basetype.setter
    def basetype(self, basetype: str):
        self.__basetype = basetype

    @property
    def basetypes(self) -> str:
        return self.__basetypes

    @basetypes.setter
    def basetypes(self, basetypes: str):
        self.__basetypes = basetypes

    @property
    def sadl_DataTypeRestriction63(self):
        return self.__sadl_DataTypeRestriction63

    @sadl_DataTypeRestriction63.setter
    def sadl_DataTypeRestriction63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_DataTypeRestriction__sadl_DataTypeRestriction63", None)
        self.__sadl_DataTypeRestriction63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Facets"):
                opp_val = getattr(old_value, "sadl_Facets", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Facets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Facets"):
                opp_val = getattr(value, "sadl_Facets", None)
                setattr(value, "sadl_Facets", self)

    @property
    def sadl_DataTypeRestriction(self):
        return self.__sadl_DataTypeRestriction

    @sadl_DataTypeRestriction.setter
    def sadl_DataTypeRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_DataTypeRestriction__sadl_DataTypeRestriction", None)
        self.__sadl_DataTypeRestriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_UserDefinedDataType61"):
                opp_val = getattr(old_value, "sadl_UserDefinedDataType61", None)
                if opp_val == self:
                    setattr(old_value, "sadl_UserDefinedDataType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_UserDefinedDataType61"):
                opp_val = getattr(value, "sadl_UserDefinedDataType61", None)
                setattr(value, "sadl_UserDefinedDataType61", self)

class sadl_RangeType:

    def __init__(self, dataType: str, sadl_RangeType: "sadl_Range" = None, sadl_RangeType56: "sadl_ResourceIdentifier" = None):
        self.dataType = dataType
        self.sadl_RangeType = sadl_RangeType
        self.sadl_RangeType56 = sadl_RangeType56
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def sadl_RangeType(self):
        return self.__sadl_RangeType

    @sadl_RangeType.setter
    def sadl_RangeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_RangeType__sadl_RangeType", None)
        self.__sadl_RangeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Range54"):
                opp_val = getattr(old_value, "sadl_Range54", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Range54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Range54"):
                opp_val = getattr(value, "sadl_Range54", None)
                setattr(value, "sadl_Range54", self)

    @property
    def sadl_RangeType56(self):
        return self.__sadl_RangeType56

    @sadl_RangeType56.setter
    def sadl_RangeType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_RangeType__sadl_RangeType56", None)
        self.__sadl_RangeType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier57"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier57", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier57"):
                opp_val = getattr(value, "sadl_ResourceIdentifier57", None)
                setattr(value, "sadl_ResourceIdentifier57", self)

class sadl_Range:

    def __init__(self, single: str, list: str, lists: str, sadl_Range: "sadl_AddlClassInfo" = None, sadl_Range54: "sadl_RangeType" = None, sadl_Range212: "sadl_AdditionalPropertyInfo" = None):
        self.single = single
        self.list = list
        self.lists = lists
        self.sadl_Range = sadl_Range
        self.sadl_Range54 = sadl_Range54
        self.sadl_Range212 = sadl_Range212
        
    @property
    def single(self) -> str:
        return self.__single

    @single.setter
    def single(self, single: str):
        self.__single = single

    @property
    def lists(self) -> str:
        return self.__lists

    @lists.setter
    def lists(self, lists: str):
        self.__lists = lists

    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def sadl_Range(self):
        return self.__sadl_Range

    @sadl_Range.setter
    def sadl_Range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Range__sadl_Range", None)
        self.__sadl_Range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_AddlClassInfo49"):
                opp_val = getattr(old_value, "sadl_AddlClassInfo49", None)
                if opp_val == self:
                    setattr(old_value, "sadl_AddlClassInfo49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_AddlClassInfo49"):
                opp_val = getattr(value, "sadl_AddlClassInfo49", None)
                setattr(value, "sadl_AddlClassInfo49", self)

    @property
    def sadl_Range212(self):
        return self.__sadl_Range212

    @sadl_Range212.setter
    def sadl_Range212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Range__sadl_Range212", None)
        self.__sadl_Range212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_AdditionalPropertyInfo211"):
                opp_val = getattr(old_value, "sadl_AdditionalPropertyInfo211", None)
                if opp_val == self:
                    setattr(old_value, "sadl_AdditionalPropertyInfo211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_AdditionalPropertyInfo211"):
                opp_val = getattr(value, "sadl_AdditionalPropertyInfo211", None)
                setattr(value, "sadl_AdditionalPropertyInfo211", self)

    @property
    def sadl_Range54(self):
        return self.__sadl_Range54

    @sadl_Range54.setter
    def sadl_Range54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Range__sadl_Range54", None)
        self.__sadl_Range54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_RangeType"):
                opp_val = getattr(old_value, "sadl_RangeType", None)
                if opp_val == self:
                    setattr(old_value, "sadl_RangeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_RangeType"):
                opp_val = getattr(value, "sadl_RangeType", None)
                setattr(value, "sadl_RangeType", self)

class sadl_Condition:

    pass
class sadl_AddlClassInfo:

    pass
class sadl_EnumeratedInstances:

    pass
class Statement:

    pass
class sadl_TransitiveProperty(Statement):

    pass
class sadl_AllValuesFrom(Statement):

    pass
class sadl_Cardinality(Statement):

    pass
class sadl_DefaultValue(Statement):

    def __init__(self, level: str, sadl_DefaultValue: "sadl_PropertyOfClass" = None, sadl_DefaultValue162: "sadl_ExplicitValue" = None):
        self.level = level
        self.sadl_DefaultValue = sadl_DefaultValue
        self.sadl_DefaultValue162 = sadl_DefaultValue162
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def sadl_DefaultValue(self):
        return self.__sadl_DefaultValue

    @sadl_DefaultValue.setter
    def sadl_DefaultValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_DefaultValue__sadl_DefaultValue", None)
        self.__sadl_DefaultValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropertyOfClass160"):
                opp_val = getattr(old_value, "sadl_PropertyOfClass160", None)
                if opp_val == self:
                    setattr(old_value, "sadl_PropertyOfClass160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropertyOfClass160"):
                opp_val = getattr(value, "sadl_PropertyOfClass160", None)
                setattr(value, "sadl_PropertyOfClass160", self)

    @property
    def sadl_DefaultValue162(self):
        return self.__sadl_DefaultValue162

    @sadl_DefaultValue162.setter
    def sadl_DefaultValue162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_DefaultValue__sadl_DefaultValue162", None)
        self.__sadl_DefaultValue162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ExplicitValue"):
                opp_val = getattr(old_value, "sadl_ExplicitValue", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ExplicitValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ExplicitValue"):
                opp_val = getattr(value, "sadl_ExplicitValue", None)
                setattr(value, "sadl_ExplicitValue", self)

class sadl_InverseFunctionalProperty(Statement):

    pass
class sadl_ExistingInstanceAttribution(Statement):

    pass
class sadl_SomeValuesFrom(Statement):

    pass
class sadl_EquivalentConcepts(Statement):

    pass
class sadl_InverseProperty(Statement):

    pass
class sadl_PropertyDeclaration(Statement):

    def __init__(self, article: str, sadl_PropertyDeclaration: "sadl_ResourceName" = None, sadl_PropertyDeclaration191: "sadl_ResourceByName" = None, sadl_PropertyDeclaration194: set["sadl_AdditionalPropertyInfo"] = None, sadl_PropertyDeclaration196: "sadl_ResourceIdentifier" = None, sadl_PropertyDeclaration199: "sadl_ResourceIdentifier" = None, sadl_PropertyDeclaration202: "sadl_ResourceName" = None):
        self.article = article
        self.sadl_PropertyDeclaration = sadl_PropertyDeclaration
        self.sadl_PropertyDeclaration191 = sadl_PropertyDeclaration191
        self.sadl_PropertyDeclaration194 = sadl_PropertyDeclaration194 if sadl_PropertyDeclaration194 is not None else set()
        self.sadl_PropertyDeclaration196 = sadl_PropertyDeclaration196
        self.sadl_PropertyDeclaration199 = sadl_PropertyDeclaration199
        self.sadl_PropertyDeclaration202 = sadl_PropertyDeclaration202
        
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def sadl_PropertyDeclaration196(self):
        return self.__sadl_PropertyDeclaration196

    @sadl_PropertyDeclaration196.setter
    def sadl_PropertyDeclaration196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_PropertyDeclaration__sadl_PropertyDeclaration196", None)
        self.__sadl_PropertyDeclaration196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier197"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier197", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier197"):
                opp_val = getattr(value, "sadl_ResourceIdentifier197", None)
                setattr(value, "sadl_ResourceIdentifier197", self)

    @property
    def sadl_PropertyDeclaration191(self):
        return self.__sadl_PropertyDeclaration191

    @sadl_PropertyDeclaration191.setter
    def sadl_PropertyDeclaration191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_PropertyDeclaration__sadl_PropertyDeclaration191", None)
        self.__sadl_PropertyDeclaration191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByName192"):
                opp_val = getattr(old_value, "sadl_ResourceByName192", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceByName192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByName192"):
                opp_val = getattr(value, "sadl_ResourceByName192", None)
                setattr(value, "sadl_ResourceByName192", self)

    @property
    def sadl_PropertyDeclaration194(self):
        return self.__sadl_PropertyDeclaration194

    @sadl_PropertyDeclaration194.setter
    def sadl_PropertyDeclaration194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_PropertyDeclaration__sadl_PropertyDeclaration194", None)
        self.__sadl_PropertyDeclaration194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_AdditionalPropertyInfo"):
                    opp_val = getattr(item, "sadl_AdditionalPropertyInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_AdditionalPropertyInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_AdditionalPropertyInfo"):
                    opp_val = getattr(item, "sadl_AdditionalPropertyInfo", None)
                    
                    setattr(item, "sadl_AdditionalPropertyInfo", self)
                    

    @property
    def sadl_PropertyDeclaration(self):
        return self.__sadl_PropertyDeclaration

    @sadl_PropertyDeclaration.setter
    def sadl_PropertyDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_PropertyDeclaration__sadl_PropertyDeclaration", None)
        self.__sadl_PropertyDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceName189"):
                opp_val = getattr(old_value, "sadl_ResourceName189", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceName189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceName189"):
                opp_val = getattr(value, "sadl_ResourceName189", None)
                setattr(value, "sadl_ResourceName189", self)

    @property
    def sadl_PropertyDeclaration199(self):
        return self.__sadl_PropertyDeclaration199

    @sadl_PropertyDeclaration199.setter
    def sadl_PropertyDeclaration199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_PropertyDeclaration__sadl_PropertyDeclaration199", None)
        self.__sadl_PropertyDeclaration199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceIdentifier200"):
                opp_val = getattr(old_value, "sadl_ResourceIdentifier200", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceIdentifier200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceIdentifier200"):
                opp_val = getattr(value, "sadl_ResourceIdentifier200", None)
                setattr(value, "sadl_ResourceIdentifier200", self)

    @property
    def sadl_PropertyDeclaration202(self):
        return self.__sadl_PropertyDeclaration202

    @sadl_PropertyDeclaration202.setter
    def sadl_PropertyDeclaration202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_PropertyDeclaration__sadl_PropertyDeclaration202", None)
        self.__sadl_PropertyDeclaration202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceName203"):
                opp_val = getattr(old_value, "sadl_ResourceName203", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceName203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceName203"):
                opp_val = getattr(value, "sadl_ResourceName203", None)
                setattr(value, "sadl_ResourceName203", self)

class sadl_InstanceDeclarationStatement(Statement):

    pass
class sadl_NecessaryAndSufficient(Statement):

    def __init__(self, article: str, sadl_NecessaryAndSufficient186: set["sadl_Condition"] = None, sadl_NecessaryAndSufficient: "sadl_TypedBNode" = None, sadl_NecessaryAndSufficient180: "sadl_ResourceName" = None, sadl_NecessaryAndSufficient183: set["sadl_ResourceByName"] = None):
        self.article = article
        self.sadl_NecessaryAndSufficient186 = sadl_NecessaryAndSufficient186 if sadl_NecessaryAndSufficient186 is not None else set()
        self.sadl_NecessaryAndSufficient = sadl_NecessaryAndSufficient
        self.sadl_NecessaryAndSufficient180 = sadl_NecessaryAndSufficient180
        self.sadl_NecessaryAndSufficient183 = sadl_NecessaryAndSufficient183 if sadl_NecessaryAndSufficient183 is not None else set()
        
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def sadl_NecessaryAndSufficient186(self):
        return self.__sadl_NecessaryAndSufficient186

    @sadl_NecessaryAndSufficient186.setter
    def sadl_NecessaryAndSufficient186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_NecessaryAndSufficient__sadl_NecessaryAndSufficient186", None)
        self.__sadl_NecessaryAndSufficient186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_Condition187"):
                    opp_val = getattr(item, "sadl_Condition187", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_Condition187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_Condition187"):
                    opp_val = getattr(item, "sadl_Condition187", None)
                    
                    setattr(item, "sadl_Condition187", self)
                    

    @property
    def sadl_NecessaryAndSufficient(self):
        return self.__sadl_NecessaryAndSufficient

    @sadl_NecessaryAndSufficient.setter
    def sadl_NecessaryAndSufficient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_NecessaryAndSufficient__sadl_NecessaryAndSufficient", None)
        self.__sadl_NecessaryAndSufficient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_TypedBNode"):
                opp_val = getattr(old_value, "sadl_TypedBNode", None)
                if opp_val == self:
                    setattr(old_value, "sadl_TypedBNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_TypedBNode"):
                opp_val = getattr(value, "sadl_TypedBNode", None)
                setattr(value, "sadl_TypedBNode", self)

    @property
    def sadl_NecessaryAndSufficient180(self):
        return self.__sadl_NecessaryAndSufficient180

    @sadl_NecessaryAndSufficient180.setter
    def sadl_NecessaryAndSufficient180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_NecessaryAndSufficient__sadl_NecessaryAndSufficient180", None)
        self.__sadl_NecessaryAndSufficient180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceName181"):
                opp_val = getattr(old_value, "sadl_ResourceName181", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceName181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceName181"):
                opp_val = getattr(value, "sadl_ResourceName181", None)
                setattr(value, "sadl_ResourceName181", self)

    @property
    def sadl_NecessaryAndSufficient183(self):
        return self.__sadl_NecessaryAndSufficient183

    @sadl_NecessaryAndSufficient183.setter
    def sadl_NecessaryAndSufficient183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_NecessaryAndSufficient__sadl_NecessaryAndSufficient183", None)
        self.__sadl_NecessaryAndSufficient183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_ResourceByName184"):
                    opp_val = getattr(item, "sadl_ResourceByName184", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_ResourceByName184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_ResourceByName184"):
                    opp_val = getattr(item, "sadl_ResourceByName184", None)
                    
                    setattr(item, "sadl_ResourceByName184", self)
                    

class sadl_InstancesAllDifferent(Statement):

    pass
class sadl_SymmetricalProperty(Statement):

    pass
class sadl_FunctionalProperty(Statement):

    pass
class sadl_ComplementOfClass(Statement):

    pass
class sadl_MinCardinality(Statement):

    pass
class sadl_DisjointClasses(Statement):

    pass
class sadl_MaxCardinality(Statement):

    pass
class sadl_InstanceDifferentFrom(Statement):

    pass
class sadl_HasValue(Statement):

    pass
class sadl_EnumeratedAllAndSomeValuesFrom(Statement):

    pass
class sadl_UserDefinedDataType(Statement):

    pass
class sadl_EnumeratedAllValuesFrom(Statement):

    pass
class sadl_ClassDeclaration(Statement):

    pass
class ResourceBySetOp:

    pass
class sadl_IntersectionResource(ResourceBySetOp):

    pass
class sadl_UnionResource(ResourceBySetOp):

    pass
class ResourceIdentifier:

    pass
class sadl_ResourceByRestriction(ResourceIdentifier):

    def __init__(self, annType: str, sadl_ResourceByRestriction: set["sadl_ContentList"] = None, sadl_ResourceByRestriction23: "sadl_ResourceByName" = None, sadl_ResourceByRestriction26: "sadl_Condition" = None):
        self.annType = annType
        self.sadl_ResourceByRestriction = sadl_ResourceByRestriction if sadl_ResourceByRestriction is not None else set()
        self.sadl_ResourceByRestriction23 = sadl_ResourceByRestriction23
        self.sadl_ResourceByRestriction26 = sadl_ResourceByRestriction26
        
    @property
    def annType(self) -> str:
        return self.__annType

    @annType.setter
    def annType(self, annType: str):
        self.__annType = annType

    @property
    def sadl_ResourceByRestriction23(self):
        return self.__sadl_ResourceByRestriction23

    @sadl_ResourceByRestriction23.setter
    def sadl_ResourceByRestriction23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceByRestriction__sadl_ResourceByRestriction23", None)
        self.__sadl_ResourceByRestriction23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByName24"):
                opp_val = getattr(old_value, "sadl_ResourceByName24", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceByName24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByName24"):
                opp_val = getattr(value, "sadl_ResourceByName24", None)
                setattr(value, "sadl_ResourceByName24", self)

    @property
    def sadl_ResourceByRestriction(self):
        return self.__sadl_ResourceByRestriction

    @sadl_ResourceByRestriction.setter
    def sadl_ResourceByRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceByRestriction__sadl_ResourceByRestriction", None)
        self.__sadl_ResourceByRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_ContentList21"):
                    opp_val = getattr(item, "sadl_ContentList21", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_ContentList21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_ContentList21"):
                    opp_val = getattr(item, "sadl_ContentList21", None)
                    
                    setattr(item, "sadl_ContentList21", self)
                    

    @property
    def sadl_ResourceByRestriction26(self):
        return self.__sadl_ResourceByRestriction26

    @sadl_ResourceByRestriction26.setter
    def sadl_ResourceByRestriction26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceByRestriction__sadl_ResourceByRestriction26", None)
        self.__sadl_ResourceByRestriction26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Condition"):
                opp_val = getattr(old_value, "sadl_Condition", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Condition"):
                opp_val = getattr(value, "sadl_Condition", None)
                setattr(value, "sadl_Condition", self)

class sadl_ResourceByName(ResourceIdentifier):

    pass
class sadl_LiteralValue:

    def __init__(self, literalNumber: str, literalString: str, literalBoolean: str, sadl_LiteralValue: "sadl_LiteralList" = None, sadl_LiteralValue395: "sadl_ExplicitValue" = None):
        self.literalNumber = literalNumber
        self.literalString = literalString
        self.literalBoolean = literalBoolean
        self.sadl_LiteralValue = sadl_LiteralValue
        self.sadl_LiteralValue395 = sadl_LiteralValue395
        
    @property
    def literalBoolean(self) -> str:
        return self.__literalBoolean

    @literalBoolean.setter
    def literalBoolean(self, literalBoolean: str):
        self.__literalBoolean = literalBoolean

    @property
    def literalString(self) -> str:
        return self.__literalString

    @literalString.setter
    def literalString(self, literalString: str):
        self.__literalString = literalString

    @property
    def literalNumber(self) -> str:
        return self.__literalNumber

    @literalNumber.setter
    def literalNumber(self, literalNumber: str):
        self.__literalNumber = literalNumber

    @property
    def sadl_LiteralValue(self):
        return self.__sadl_LiteralValue

    @sadl_LiteralValue.setter
    def sadl_LiteralValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_LiteralValue__sadl_LiteralValue", None)
        self.__sadl_LiteralValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_LiteralList"):
                opp_val = getattr(old_value, "sadl_LiteralList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_LiteralList"):
                opp_val = getattr(value, "sadl_LiteralList", None)
                if opp_val is None:
                    setattr(value, "sadl_LiteralList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_LiteralValue395(self):
        return self.__sadl_LiteralValue395

    @sadl_LiteralValue395.setter
    def sadl_LiteralValue395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_LiteralValue__sadl_LiteralValue395", None)
        self.__sadl_LiteralValue395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ExplicitValue394"):
                opp_val = getattr(old_value, "sadl_ExplicitValue394", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ExplicitValue394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ExplicitValue394"):
                opp_val = getattr(value, "sadl_ExplicitValue394", None)
                setattr(value, "sadl_ExplicitValue394", self)

class sadl_LiteralList:

    pass
class sadl_ResourceList:

    pass
class sadl_ResourceBySetOp(ResourceIdentifier):

    def __init__(self, annType: str, op: str, sadl_ResourceBySetOp: set["sadl_ContentList"] = None, sadl_ResourceBySetOp18: set["sadl_ResourceIdentifier"] = None):
        self.annType = annType
        self.op = op
        self.sadl_ResourceBySetOp = sadl_ResourceBySetOp if sadl_ResourceBySetOp is not None else set()
        self.sadl_ResourceBySetOp18 = sadl_ResourceBySetOp18 if sadl_ResourceBySetOp18 is not None else set()
        
    @property
    def annType(self) -> str:
        return self.__annType

    @annType.setter
    def annType(self, annType: str):
        self.__annType = annType

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sadl_ResourceBySetOp(self):
        return self.__sadl_ResourceBySetOp

    @sadl_ResourceBySetOp.setter
    def sadl_ResourceBySetOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceBySetOp__sadl_ResourceBySetOp", None)
        self.__sadl_ResourceBySetOp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_ContentList16"):
                    opp_val = getattr(item, "sadl_ContentList16", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_ContentList16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_ContentList16"):
                    opp_val = getattr(item, "sadl_ContentList16", None)
                    
                    setattr(item, "sadl_ContentList16", self)
                    

    @property
    def sadl_ResourceBySetOp18(self):
        return self.__sadl_ResourceBySetOp18

    @sadl_ResourceBySetOp18.setter
    def sadl_ResourceBySetOp18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceBySetOp__sadl_ResourceBySetOp18", None)
        self.__sadl_ResourceBySetOp18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_ResourceIdentifier19"):
                    opp_val = getattr(item, "sadl_ResourceIdentifier19", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_ResourceIdentifier19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_ResourceIdentifier19"):
                    opp_val = getattr(item, "sadl_ResourceIdentifier19", None)
                    
                    setattr(item, "sadl_ResourceIdentifier19", self)
                    

class sadl_ResourceIdentifier:

    pass
class sadl_ExistingResourceList:

    pass
class sadl_ContentList:

    def __init__(self, annContent: str, sadl_ContentList8: "sadl_ResourceName" = None, sadl_ContentList: "sadl_ModelName" = None, sadl_ContentList16: "sadl_ResourceBySetOp" = None, sadl_ContentList21: "sadl_ResourceByRestriction" = None):
        self.annContent = annContent
        self.sadl_ContentList8 = sadl_ContentList8
        self.sadl_ContentList = sadl_ContentList
        self.sadl_ContentList16 = sadl_ContentList16
        self.sadl_ContentList21 = sadl_ContentList21
        
    @property
    def annContent(self) -> str:
        return self.__annContent

    @annContent.setter
    def annContent(self, annContent: str):
        self.__annContent = annContent

    @property
    def sadl_ContentList16(self):
        return self.__sadl_ContentList16

    @sadl_ContentList16.setter
    def sadl_ContentList16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ContentList__sadl_ContentList16", None)
        self.__sadl_ContentList16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceBySetOp"):
                opp_val = getattr(old_value, "sadl_ResourceBySetOp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceBySetOp"):
                opp_val = getattr(value, "sadl_ResourceBySetOp", None)
                if opp_val is None:
                    setattr(value, "sadl_ResourceBySetOp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_ContentList8(self):
        return self.__sadl_ContentList8

    @sadl_ContentList8.setter
    def sadl_ContentList8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ContentList__sadl_ContentList8", None)
        self.__sadl_ContentList8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceName"):
                opp_val = getattr(old_value, "sadl_ResourceName", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceName"):
                opp_val = getattr(value, "sadl_ResourceName", None)
                if opp_val is None:
                    setattr(value, "sadl_ResourceName", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_ContentList(self):
        return self.__sadl_ContentList

    @sadl_ContentList.setter
    def sadl_ContentList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ContentList__sadl_ContentList", None)
        self.__sadl_ContentList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ModelName6"):
                opp_val = getattr(old_value, "sadl_ModelName6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ModelName6"):
                opp_val = getattr(value, "sadl_ModelName6", None)
                if opp_val is None:
                    setattr(value, "sadl_ModelName6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_ContentList21(self):
        return self.__sadl_ContentList21

    @sadl_ContentList21.setter
    def sadl_ContentList21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ContentList__sadl_ContentList21", None)
        self.__sadl_ContentList21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByRestriction"):
                opp_val = getattr(old_value, "sadl_ResourceByRestriction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByRestriction"):
                opp_val = getattr(value, "sadl_ResourceByRestriction", None)
                if opp_val is None:
                    setattr(value, "sadl_ResourceByRestriction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sadl_ModelElement:

    pass
class sadl_Import:

    def __init__(self, importURI: str, alias: str, sadl_Import: "sadl_Model" = None):
        self.importURI = importURI
        self.alias = alias
        self.sadl_Import = sadl_Import
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def sadl_Import(self):
        return self.__sadl_Import

    @sadl_Import.setter
    def sadl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Import__sadl_Import", None)
        self.__sadl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Model2"):
                opp_val = getattr(old_value, "sadl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Model2"):
                opp_val = getattr(value, "sadl_Model2", None)
                if opp_val is None:
                    setattr(value, "sadl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sadl_ResourceName:

    def __init__(self, name: str, annType: str, sadl_ResourceName: set["sadl_ContentList"] = None, sadl_ResourceName10: "sadl_ResourceList" = None, sadl_ResourceName13: "sadl_ResourceByName" = None, sadl_ResourceName28: "sadl_ClassDeclaration" = None, sadl_ResourceName47: "sadl_AddlClassInfo" = None, sadl_ResourceName59: "sadl_UserDefinedDataType" = None, sadl_ResourceName189: "sadl_PropertyDeclaration" = None, sadl_ResourceName181: "sadl_NecessaryAndSufficient" = None, sadl_ResourceName203: "sadl_PropertyDeclaration" = None, sadl_ResourceName242: "sadl_InstanceDeclaration" = None, sadl_ResourceName245: "sadl_TypeDeclaration" = None, sadl_ResourceName304: "sadl_VariableList" = None, sadl_ResourceName327: "sadl_ConstructExpression" = None, sadl_ResourceName330: "sadl_ConstructExpression" = None, sadl_ResourceName333: "sadl_ConstructExpression" = None, sadl_ResourceName338: "sadl_OrderElement" = None):
        self.name = name
        self.annType = annType
        self.sadl_ResourceName = sadl_ResourceName if sadl_ResourceName is not None else set()
        self.sadl_ResourceName10 = sadl_ResourceName10
        self.sadl_ResourceName13 = sadl_ResourceName13
        self.sadl_ResourceName28 = sadl_ResourceName28
        self.sadl_ResourceName47 = sadl_ResourceName47
        self.sadl_ResourceName59 = sadl_ResourceName59
        self.sadl_ResourceName189 = sadl_ResourceName189
        self.sadl_ResourceName181 = sadl_ResourceName181
        self.sadl_ResourceName203 = sadl_ResourceName203
        self.sadl_ResourceName242 = sadl_ResourceName242
        self.sadl_ResourceName245 = sadl_ResourceName245
        self.sadl_ResourceName304 = sadl_ResourceName304
        self.sadl_ResourceName327 = sadl_ResourceName327
        self.sadl_ResourceName330 = sadl_ResourceName330
        self.sadl_ResourceName333 = sadl_ResourceName333
        self.sadl_ResourceName338 = sadl_ResourceName338
        
    @property
    def annType(self) -> str:
        return self.__annType

    @annType.setter
    def annType(self, annType: str):
        self.__annType = annType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sadl_ResourceName13(self):
        return self.__sadl_ResourceName13

    @sadl_ResourceName13.setter
    def sadl_ResourceName13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName13", None)
        self.__sadl_ResourceName13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceByName"):
                opp_val = getattr(old_value, "sadl_ResourceByName", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ResourceByName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceByName"):
                opp_val = getattr(value, "sadl_ResourceByName", None)
                setattr(value, "sadl_ResourceByName", self)

    @property
    def sadl_ResourceName181(self):
        return self.__sadl_ResourceName181

    @sadl_ResourceName181.setter
    def sadl_ResourceName181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName181", None)
        self.__sadl_ResourceName181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_NecessaryAndSufficient180"):
                opp_val = getattr(old_value, "sadl_NecessaryAndSufficient180", None)
                if opp_val == self:
                    setattr(old_value, "sadl_NecessaryAndSufficient180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_NecessaryAndSufficient180"):
                opp_val = getattr(value, "sadl_NecessaryAndSufficient180", None)
                setattr(value, "sadl_NecessaryAndSufficient180", self)

    @property
    def sadl_ResourceName(self):
        return self.__sadl_ResourceName

    @sadl_ResourceName.setter
    def sadl_ResourceName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName", None)
        self.__sadl_ResourceName = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_ContentList8"):
                    opp_val = getattr(item, "sadl_ContentList8", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_ContentList8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_ContentList8"):
                    opp_val = getattr(item, "sadl_ContentList8", None)
                    
                    setattr(item, "sadl_ContentList8", self)
                    

    @property
    def sadl_ResourceName203(self):
        return self.__sadl_ResourceName203

    @sadl_ResourceName203.setter
    def sadl_ResourceName203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName203", None)
        self.__sadl_ResourceName203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropertyDeclaration202"):
                opp_val = getattr(old_value, "sadl_PropertyDeclaration202", None)
                if opp_val == self:
                    setattr(old_value, "sadl_PropertyDeclaration202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropertyDeclaration202"):
                opp_val = getattr(value, "sadl_PropertyDeclaration202", None)
                setattr(value, "sadl_PropertyDeclaration202", self)

    @property
    def sadl_ResourceName59(self):
        return self.__sadl_ResourceName59

    @sadl_ResourceName59.setter
    def sadl_ResourceName59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName59", None)
        self.__sadl_ResourceName59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_UserDefinedDataType"):
                opp_val = getattr(old_value, "sadl_UserDefinedDataType", None)
                if opp_val == self:
                    setattr(old_value, "sadl_UserDefinedDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_UserDefinedDataType"):
                opp_val = getattr(value, "sadl_UserDefinedDataType", None)
                setattr(value, "sadl_UserDefinedDataType", self)

    @property
    def sadl_ResourceName338(self):
        return self.__sadl_ResourceName338

    @sadl_ResourceName338.setter
    def sadl_ResourceName338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName338", None)
        self.__sadl_ResourceName338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_OrderElement337"):
                opp_val = getattr(old_value, "sadl_OrderElement337", None)
                if opp_val == self:
                    setattr(old_value, "sadl_OrderElement337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_OrderElement337"):
                opp_val = getattr(value, "sadl_OrderElement337", None)
                setattr(value, "sadl_OrderElement337", self)

    @property
    def sadl_ResourceName189(self):
        return self.__sadl_ResourceName189

    @sadl_ResourceName189.setter
    def sadl_ResourceName189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName189", None)
        self.__sadl_ResourceName189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_PropertyDeclaration"):
                opp_val = getattr(old_value, "sadl_PropertyDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "sadl_PropertyDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_PropertyDeclaration"):
                opp_val = getattr(value, "sadl_PropertyDeclaration", None)
                setattr(value, "sadl_PropertyDeclaration", self)

    @property
    def sadl_ResourceName245(self):
        return self.__sadl_ResourceName245

    @sadl_ResourceName245.setter
    def sadl_ResourceName245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName245", None)
        self.__sadl_ResourceName245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_TypeDeclaration244"):
                opp_val = getattr(old_value, "sadl_TypeDeclaration244", None)
                if opp_val == self:
                    setattr(old_value, "sadl_TypeDeclaration244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_TypeDeclaration244"):
                opp_val = getattr(value, "sadl_TypeDeclaration244", None)
                setattr(value, "sadl_TypeDeclaration244", self)

    @property
    def sadl_ResourceName304(self):
        return self.__sadl_ResourceName304

    @sadl_ResourceName304.setter
    def sadl_ResourceName304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName304", None)
        self.__sadl_ResourceName304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_VariableList"):
                opp_val = getattr(old_value, "sadl_VariableList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_VariableList"):
                opp_val = getattr(value, "sadl_VariableList", None)
                if opp_val is None:
                    setattr(value, "sadl_VariableList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_ResourceName327(self):
        return self.__sadl_ResourceName327

    @sadl_ResourceName327.setter
    def sadl_ResourceName327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName327", None)
        self.__sadl_ResourceName327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ConstructExpression"):
                opp_val = getattr(old_value, "sadl_ConstructExpression", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ConstructExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ConstructExpression"):
                opp_val = getattr(value, "sadl_ConstructExpression", None)
                setattr(value, "sadl_ConstructExpression", self)

    @property
    def sadl_ResourceName242(self):
        return self.__sadl_ResourceName242

    @sadl_ResourceName242.setter
    def sadl_ResourceName242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName242", None)
        self.__sadl_ResourceName242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_InstanceDeclaration241"):
                opp_val = getattr(old_value, "sadl_InstanceDeclaration241", None)
                if opp_val == self:
                    setattr(old_value, "sadl_InstanceDeclaration241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_InstanceDeclaration241"):
                opp_val = getattr(value, "sadl_InstanceDeclaration241", None)
                setattr(value, "sadl_InstanceDeclaration241", self)

    @property
    def sadl_ResourceName10(self):
        return self.__sadl_ResourceName10

    @sadl_ResourceName10.setter
    def sadl_ResourceName10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName10", None)
        self.__sadl_ResourceName10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ResourceList"):
                opp_val = getattr(old_value, "sadl_ResourceList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ResourceList"):
                opp_val = getattr(value, "sadl_ResourceList", None)
                if opp_val is None:
                    setattr(value, "sadl_ResourceList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sadl_ResourceName333(self):
        return self.__sadl_ResourceName333

    @sadl_ResourceName333.setter
    def sadl_ResourceName333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName333", None)
        self.__sadl_ResourceName333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ConstructExpression332"):
                opp_val = getattr(old_value, "sadl_ConstructExpression332", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ConstructExpression332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ConstructExpression332"):
                opp_val = getattr(value, "sadl_ConstructExpression332", None)
                setattr(value, "sadl_ConstructExpression332", self)

    @property
    def sadl_ResourceName330(self):
        return self.__sadl_ResourceName330

    @sadl_ResourceName330.setter
    def sadl_ResourceName330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName330", None)
        self.__sadl_ResourceName330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ConstructExpression329"):
                opp_val = getattr(old_value, "sadl_ConstructExpression329", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ConstructExpression329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ConstructExpression329"):
                opp_val = getattr(value, "sadl_ConstructExpression329", None)
                setattr(value, "sadl_ConstructExpression329", self)

    @property
    def sadl_ResourceName28(self):
        return self.__sadl_ResourceName28

    @sadl_ResourceName28.setter
    def sadl_ResourceName28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName28", None)
        self.__sadl_ResourceName28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ClassDeclaration"):
                opp_val = getattr(old_value, "sadl_ClassDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ClassDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ClassDeclaration"):
                opp_val = getattr(value, "sadl_ClassDeclaration", None)
                setattr(value, "sadl_ClassDeclaration", self)

    @property
    def sadl_ResourceName47(self):
        return self.__sadl_ResourceName47

    @sadl_ResourceName47.setter
    def sadl_ResourceName47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ResourceName__sadl_ResourceName47", None)
        self.__sadl_ResourceName47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_AddlClassInfo46"):
                opp_val = getattr(old_value, "sadl_AddlClassInfo46", None)
                if opp_val == self:
                    setattr(old_value, "sadl_AddlClassInfo46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_AddlClassInfo46"):
                opp_val = getattr(value, "sadl_AddlClassInfo46", None)
                setattr(value, "sadl_AddlClassInfo46", self)

class ModelElement:

    pass
class sadl_Explanation(ModelElement):

    def __init__(self, rulename: str, sadl_Explanation: "sadl_EObject" = None):
        self.rulename = rulename
        self.sadl_Explanation = sadl_Explanation
        
    @property
    def rulename(self) -> str:
        return self.__rulename

    @rulename.setter
    def rulename(self, rulename: str):
        self.__rulename = rulename

    @property
    def sadl_Explanation(self):
        return self.__sadl_Explanation

    @sadl_Explanation.setter
    def sadl_Explanation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Explanation__sadl_Explanation", None)
        self.__sadl_Explanation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_EObject318"):
                opp_val = getattr(old_value, "sadl_EObject318", None)
                if opp_val == self:
                    setattr(old_value, "sadl_EObject318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_EObject318"):
                opp_val = getattr(value, "sadl_EObject318", None)
                setattr(value, "sadl_EObject318", self)

class sadl_Expr(ModelElement):

    pass
class sadl_Query(ModelElement):

    pass
class sadl_Display(ModelElement):

    def __init__(self, displayString: str, model: str):
        self.displayString = displayString
        self.model = model
        
    @property
    def displayString(self) -> str:
        return self.__displayString

    @displayString.setter
    def displayString(self, displayString: str):
        self.__displayString = displayString

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

class sadl_Rule(ModelElement):

    def __init__(self, name: str, sadl_Rule: "sadl_ElementSet" = None, sadl_Rule307: "sadl_ElementSet" = None, sadl_Rule310: "sadl_ElementSet" = None):
        self.name = name
        self.sadl_Rule = sadl_Rule
        self.sadl_Rule307 = sadl_Rule307
        self.sadl_Rule310 = sadl_Rule310
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sadl_Rule(self):
        return self.__sadl_Rule

    @sadl_Rule.setter
    def sadl_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Rule__sadl_Rule", None)
        self.__sadl_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ElementSet"):
                opp_val = getattr(old_value, "sadl_ElementSet", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ElementSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ElementSet"):
                opp_val = getattr(value, "sadl_ElementSet", None)
                setattr(value, "sadl_ElementSet", self)

    @property
    def sadl_Rule307(self):
        return self.__sadl_Rule307

    @sadl_Rule307.setter
    def sadl_Rule307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Rule__sadl_Rule307", None)
        self.__sadl_Rule307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ElementSet308"):
                opp_val = getattr(old_value, "sadl_ElementSet308", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ElementSet308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ElementSet308"):
                opp_val = getattr(value, "sadl_ElementSet308", None)
                setattr(value, "sadl_ElementSet308", self)

    @property
    def sadl_Rule310(self):
        return self.__sadl_Rule310

    @sadl_Rule310.setter
    def sadl_Rule310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_Rule__sadl_Rule310", None)
        self.__sadl_Rule310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_ElementSet311"):
                opp_val = getattr(old_value, "sadl_ElementSet311", None)
                if opp_val == self:
                    setattr(old_value, "sadl_ElementSet311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_ElementSet311"):
                opp_val = getattr(value, "sadl_ElementSet311", None)
                setattr(value, "sadl_ElementSet311", self)

class sadl_Test(ModelElement):

    pass
class sadl_Statement(ModelElement):

    pass
class sadl_ModelName:

    def __init__(self, baseUri: str, alias: str, version: str, annType: str, sadl_ModelName: "sadl_Model" = None, sadl_ModelName6: set["sadl_ContentList"] = None):
        self.baseUri = baseUri
        self.alias = alias
        self.version = version
        self.annType = annType
        self.sadl_ModelName = sadl_ModelName
        self.sadl_ModelName6 = sadl_ModelName6 if sadl_ModelName6 is not None else set()
        
    @property
    def baseUri(self) -> str:
        return self.__baseUri

    @baseUri.setter
    def baseUri(self, baseUri: str):
        self.__baseUri = baseUri

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def annType(self) -> str:
        return self.__annType

    @annType.setter
    def annType(self, annType: str):
        self.__annType = annType

    @property
    def sadl_ModelName6(self):
        return self.__sadl_ModelName6

    @sadl_ModelName6.setter
    def sadl_ModelName6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ModelName__sadl_ModelName6", None)
        self.__sadl_ModelName6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sadl_ContentList"):
                    opp_val = getattr(item, "sadl_ContentList", None)
                    
                    if opp_val == self:
                        setattr(item, "sadl_ContentList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sadl_ContentList"):
                    opp_val = getattr(item, "sadl_ContentList", None)
                    
                    setattr(item, "sadl_ContentList", self)
                    

    @property
    def sadl_ModelName(self):
        return self.__sadl_ModelName

    @sadl_ModelName.setter
    def sadl_ModelName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sadl_ModelName__sadl_ModelName", None)
        self.__sadl_ModelName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sadl_Model"):
                opp_val = getattr(old_value, "sadl_Model", None)
                if opp_val == self:
                    setattr(old_value, "sadl_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sadl_Model"):
                opp_val = getattr(value, "sadl_Model", None)
                setattr(value, "sadl_Model", self)

class sadl_Model:

    pass