from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectType2(Enum):
    MISC = "MISC"
    SEQUENTIAL = "SEQUENTIAL"
    VERSIONING = "VERSIONING"
    group = "group"
    argument = "argument"
    template = "template"
class ObjectType(Enum):
    template = "template"
    argument = "argument"
    collection = "collection"
    person = "person"
    exhibit = "exhibit"
    memo = "memo"
    group = "group"
    discoveryMethod = "discoveryMethod"
class ObjectType1(Enum):
    template = "template"
    argument = "argument"
    collection = "collection"
    person = "person"
    exhibit = "exhibit"
    memo = "memo"
    group = "group"
    discoveryMethod = "discoveryMethod"
class Type(Enum):
    Url = "Url"
    Template = "Template"
    Urldir = "Urldir"
class ObjectType3(Enum):
    template = "template"
    argument = "argument"
    collection = "collection"
    person = "person"
    exhibit = "exhibit"
    memo = "memo"
    group = "group"
    discoveryMethod = "discoveryMethod"


############################################
# Definition of Classes
############################################

class aml_Value:

    def __init__(self, mixed: str, group: str, type: str, unit: str, aml_Value: "aml_DocumentRoot" = None, aml_Value285: "aml_Parameter" = None, aml_Value326: set["aml_Interval"] = None, aml_Value329: set["aml_List"] = None):
        self.mixed = mixed
        self.group = group
        self.type = type
        self.unit = unit
        self.aml_Value = aml_Value
        self.aml_Value285 = aml_Value285
        self.aml_Value326 = aml_Value326 if aml_Value326 is not None else set()
        self.aml_Value329 = aml_Value329 if aml_Value329 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def aml_Value326(self):
        return self.__aml_Value326

    @aml_Value326.setter
    def aml_Value326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Value__aml_Value326", None)
        self.__aml_Value326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Interval327"):
                    opp_val = getattr(item, "aml_Interval327", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Interval327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Interval327"):
                    opp_val = getattr(item, "aml_Interval327", None)
                    
                    setattr(item, "aml_Interval327", self)
                    

    @property
    def aml_Value285(self):
        return self.__aml_Value285

    @aml_Value285.setter
    def aml_Value285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Value__aml_Value285", None)
        self.__aml_Value285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Parameter284"):
                opp_val = getattr(old_value, "aml_Parameter284", None)
                if opp_val == self:
                    setattr(old_value, "aml_Parameter284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Parameter284"):
                opp_val = getattr(value, "aml_Parameter284", None)
                setattr(value, "aml_Parameter284", self)

    @property
    def aml_Value329(self):
        return self.__aml_Value329

    @aml_Value329.setter
    def aml_Value329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Value__aml_Value329", None)
        self.__aml_Value329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_List330"):
                    opp_val = getattr(item, "aml_List330", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_List330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_List330"):
                    opp_val = getattr(item, "aml_List330", None)
                    
                    setattr(item, "aml_List330", self)
                    

    @property
    def aml_Value(self):
        return self.__aml_Value

    @aml_Value.setter
    def aml_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Value__aml_Value", None)
        self.__aml_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot201"):
                opp_val = getattr(old_value, "aml_DocumentRoot201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot201"):
                opp_val = getattr(value, "aml_DocumentRoot201", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Start:

    def __init__(self, value: str, scheme: str, aml_Start: "aml_DocumentRoot" = None, aml_Start288: "aml_Period" = None):
        self.value = value
        self.scheme = scheme
        self.aml_Start = aml_Start
        self.aml_Start288 = aml_Start288
        
    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def aml_Start(self):
        return self.__aml_Start

    @aml_Start.setter
    def aml_Start(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Start__aml_Start", None)
        self.__aml_Start = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot193"):
                opp_val = getattr(old_value, "aml_DocumentRoot193", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot193"):
                opp_val = getattr(value, "aml_DocumentRoot193", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot193", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Start288(self):
        return self.__aml_Start288

    @aml_Start288.setter
    def aml_Start288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Start__aml_Start288", None)
        self.__aml_Start288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Period287"):
                opp_val = getattr(old_value, "aml_Period287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Period287"):
                opp_val = getattr(value, "aml_Period287", None)
                if opp_val is None:
                    setattr(value, "aml_Period287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Reliability:

    def __init__(self, description: str, label: str, ordinal: str, symbol: str, aml_Reliability: "aml_DocumentRoot" = None, aml_Reliability213: "aml_Evidence" = None):
        self.description = description
        self.label = label
        self.ordinal = ordinal
        self.symbol = symbol
        self.aml_Reliability = aml_Reliability
        self.aml_Reliability213 = aml_Reliability213
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aml_Reliability(self):
        return self.__aml_Reliability

    @aml_Reliability.setter
    def aml_Reliability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Reliability__aml_Reliability", None)
        self.__aml_Reliability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot185"):
                opp_val = getattr(old_value, "aml_DocumentRoot185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot185"):
                opp_val = getattr(value, "aml_DocumentRoot185", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Reliability213(self):
        return self.__aml_Reliability213

    @aml_Reliability213.setter
    def aml_Reliability213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Reliability__aml_Reliability213", None)
        self.__aml_Reliability213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Evidence212"):
                opp_val = getattr(old_value, "aml_Evidence212", None)
                if opp_val == self:
                    setattr(old_value, "aml_Evidence212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Evidence212"):
                opp_val = getattr(value, "aml_Evidence212", None)
                setattr(value, "aml_Evidence212", self)

class aml_Relevance:

    def __init__(self, description: str, label: str, ordinal: str, symbol: str, aml_Relevance: "aml_DocumentRoot" = None, aml_Relevance210: "aml_Evidence" = None):
        self.description = description
        self.label = label
        self.ordinal = ordinal
        self.symbol = symbol
        self.aml_Relevance = aml_Relevance
        self.aml_Relevance210 = aml_Relevance210
        
    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aml_Relevance(self):
        return self.__aml_Relevance

    @aml_Relevance.setter
    def aml_Relevance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Relevance__aml_Relevance", None)
        self.__aml_Relevance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot183"):
                opp_val = getattr(old_value, "aml_DocumentRoot183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot183"):
                opp_val = getattr(value, "aml_DocumentRoot183", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Relevance210(self):
        return self.__aml_Relevance210

    @aml_Relevance210.setter
    def aml_Relevance210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Relevance__aml_Relevance210", None)
        self.__aml_Relevance210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Evidence209"):
                opp_val = getattr(old_value, "aml_Evidence209", None)
                if opp_val == self:
                    setattr(old_value, "aml_Evidence209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Evidence209"):
                opp_val = getattr(value, "aml_Evidence209", None)
                setattr(value, "aml_Evidence209", self)

class aml_Reader:

    def __init__(self, description: str, idRef: str, objectType: str, aml_Reader: "aml_DocumentRoot" = None, aml_Reader240: "aml_Memo" = None, aml_Reader246: "aml_MetaData" = None):
        self.description = description
        self.idRef = idRef
        self.objectType = objectType
        self.aml_Reader = aml_Reader
        self.aml_Reader240 = aml_Reader240
        self.aml_Reader246 = aml_Reader246
        
    @property
    def objectType(self) -> str:
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def aml_Reader(self):
        return self.__aml_Reader

    @aml_Reader.setter
    def aml_Reader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Reader__aml_Reader", None)
        self.__aml_Reader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot178"):
                opp_val = getattr(old_value, "aml_DocumentRoot178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot178"):
                opp_val = getattr(value, "aml_DocumentRoot178", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Reader240(self):
        return self.__aml_Reader240

    @aml_Reader240.setter
    def aml_Reader240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Reader__aml_Reader240", None)
        self.__aml_Reader240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Memo239"):
                opp_val = getattr(old_value, "aml_Memo239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Memo239"):
                opp_val = getattr(value, "aml_Memo239", None)
                if opp_val is None:
                    setattr(value, "aml_Memo239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Reader246(self):
        return self.__aml_Reader246

    @aml_Reader246.setter
    def aml_Reader246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Reader__aml_Reader246", None)
        self.__aml_Reader246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData245"):
                opp_val = getattr(old_value, "aml_MetaData245", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData245"):
                opp_val = getattr(value, "aml_MetaData245", None)
                if opp_val is None:
                    setattr(value, "aml_MetaData245", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_QuestionRelationships:

    pass
class aml_Publisher:

    def __init__(self, description: str, idRef: str, objectType: str, aml_Publisher: "aml_DocumentRoot" = None, aml_Publisher249: "aml_MetaData" = None):
        self.description = description
        self.idRef = idRef
        self.objectType = objectType
        self.aml_Publisher = aml_Publisher
        self.aml_Publisher249 = aml_Publisher249
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def objectType(self) -> str:
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def aml_Publisher249(self):
        return self.__aml_Publisher249

    @aml_Publisher249.setter
    def aml_Publisher249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Publisher__aml_Publisher249", None)
        self.__aml_Publisher249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData248"):
                opp_val = getattr(old_value, "aml_MetaData248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData248"):
                opp_val = getattr(value, "aml_MetaData248", None)
                if opp_val is None:
                    setattr(value, "aml_MetaData248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Publisher(self):
        return self.__aml_Publisher

    @aml_Publisher.setter
    def aml_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Publisher__aml_Publisher", None)
        self.__aml_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot171"):
                opp_val = getattr(old_value, "aml_DocumentRoot171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot171"):
                opp_val = getattr(value, "aml_DocumentRoot171", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Period:

    def __init__(self, group: str, label: str, aml_Period: "aml_DocumentRoot" = None, aml_Period282: "aml_NationState" = None, aml_Period287: set["aml_Start"] = None, aml_Period290: set["aml_End"] = None):
        self.group = group
        self.label = label
        self.aml_Period = aml_Period
        self.aml_Period282 = aml_Period282
        self.aml_Period287 = aml_Period287 if aml_Period287 is not None else set()
        self.aml_Period290 = aml_Period290 if aml_Period290 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aml_Period290(self):
        return self.__aml_Period290

    @aml_Period290.setter
    def aml_Period290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Period__aml_Period290", None)
        self.__aml_Period290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_End291"):
                    opp_val = getattr(item, "aml_End291", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_End291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_End291"):
                    opp_val = getattr(item, "aml_End291", None)
                    
                    setattr(item, "aml_End291", self)
                    

    @property
    def aml_Period(self):
        return self.__aml_Period

    @aml_Period.setter
    def aml_Period(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Period__aml_Period", None)
        self.__aml_Period = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot166"):
                opp_val = getattr(old_value, "aml_DocumentRoot166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot166"):
                opp_val = getattr(value, "aml_DocumentRoot166", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Period282(self):
        return self.__aml_Period282

    @aml_Period282.setter
    def aml_Period282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Period__aml_Period282", None)
        self.__aml_Period282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_NationState281"):
                opp_val = getattr(old_value, "aml_NationState281", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_NationState281"):
                opp_val = getattr(value, "aml_NationState281", None)
                if opp_val is None:
                    setattr(value, "aml_NationState281", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Period287(self):
        return self.__aml_Period287

    @aml_Period287.setter
    def aml_Period287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Period__aml_Period287", None)
        self.__aml_Period287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Start288"):
                    opp_val = getattr(item, "aml_Start288", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Start288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Start288"):
                    opp_val = getattr(item, "aml_Start288", None)
                    
                    setattr(item, "aml_Start288", self)
                    

class aml_List:

    def __init__(self, group: str, aml_List: "aml_DocumentRoot" = None, aml_List233: set["aml_EObject"] = None, aml_List330: "aml_Value" = None):
        self.group = group
        self.aml_List = aml_List
        self.aml_List233 = aml_List233 if aml_List233 is not None else set()
        self.aml_List330 = aml_List330
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def aml_List233(self):
        return self.__aml_List233

    @aml_List233.setter
    def aml_List233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_List__aml_List233", None)
        self.__aml_List233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject234"):
                    opp_val = getattr(item, "aml_EObject234", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject234"):
                    opp_val = getattr(item, "aml_EObject234", None)
                    
                    setattr(item, "aml_EObject234", self)
                    

    @property
    def aml_List330(self):
        return self.__aml_List330

    @aml_List330.setter
    def aml_List330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_List__aml_List330", None)
        self.__aml_List330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Value329"):
                opp_val = getattr(old_value, "aml_Value329", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Value329"):
                opp_val = getattr(value, "aml_Value329", None)
                if opp_val is None:
                    setattr(value, "aml_Value329", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_List(self):
        return self.__aml_List

    @aml_List.setter
    def aml_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_List__aml_List", None)
        self.__aml_List = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot149"):
                opp_val = getattr(old_value, "aml_DocumentRoot149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot149"):
                opp_val = getattr(value, "aml_DocumentRoot149", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Interval:

    def __init__(self, max: str, min: str, aml_Interval: "aml_DocumentRoot" = None, aml_Interval327: "aml_Value" = None):
        self.max = max
        self.min = min
        self.aml_Interval = aml_Interval
        self.aml_Interval327 = aml_Interval327
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def aml_Interval327(self):
        return self.__aml_Interval327

    @aml_Interval327.setter
    def aml_Interval327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Interval__aml_Interval327", None)
        self.__aml_Interval327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Value326"):
                opp_val = getattr(old_value, "aml_Value326", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Value326"):
                opp_val = getattr(value, "aml_Value326", None)
                if opp_val is None:
                    setattr(value, "aml_Value326", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Interval(self):
        return self.__aml_Interval

    @aml_Interval.setter
    def aml_Interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Interval__aml_Interval", None)
        self.__aml_Interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot144"):
                opp_val = getattr(old_value, "aml_DocumentRoot144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot144"):
                opp_val = getattr(value, "aml_DocumentRoot144", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_EvidenceExhibit:

    def __init__(self, questionId: str, value: str, idRef: str, aml_EvidenceExhibit: "aml_DocumentRoot" = None, aml_EvidenceExhibit207: "aml_Evidence" = None):
        self.questionId = questionId
        self.value = value
        self.idRef = idRef
        self.aml_EvidenceExhibit = aml_EvidenceExhibit
        self.aml_EvidenceExhibit207 = aml_EvidenceExhibit207
        
    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def questionId(self) -> str:
        return self.__questionId

    @questionId.setter
    def questionId(self, questionId: str):
        self.__questionId = questionId

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def aml_EvidenceExhibit(self):
        return self.__aml_EvidenceExhibit

    @aml_EvidenceExhibit.setter
    def aml_EvidenceExhibit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_EvidenceExhibit__aml_EvidenceExhibit", None)
        self.__aml_EvidenceExhibit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot127"):
                opp_val = getattr(old_value, "aml_DocumentRoot127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot127"):
                opp_val = getattr(value, "aml_DocumentRoot127", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_EvidenceExhibit207(self):
        return self.__aml_EvidenceExhibit207

    @aml_EvidenceExhibit207.setter
    def aml_EvidenceExhibit207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_EvidenceExhibit__aml_EvidenceExhibit207", None)
        self.__aml_EvidenceExhibit207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Evidence206"):
                opp_val = getattr(old_value, "aml_Evidence206", None)
                if opp_val == self:
                    setattr(old_value, "aml_Evidence206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Evidence206"):
                opp_val = getattr(value, "aml_Evidence206", None)
                setattr(value, "aml_Evidence206", self)

class aml_End:

    def __init__(self, value: str, scheme: str, aml_End: "aml_DocumentRoot" = None, aml_End291: "aml_Period" = None):
        self.value = value
        self.scheme = scheme
        self.aml_End = aml_End
        self.aml_End291 = aml_End291
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def aml_End291(self):
        return self.__aml_End291

    @aml_End291.setter
    def aml_End291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_End__aml_End291", None)
        self.__aml_End291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Period290"):
                opp_val = getattr(old_value, "aml_Period290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Period290"):
                opp_val = getattr(value, "aml_Period290", None)
                if opp_val is None:
                    setattr(value, "aml_Period290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_End(self):
        return self.__aml_End

    @aml_End.setter
    def aml_End(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_End__aml_End", None)
        self.__aml_End = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot122"):
                opp_val = getattr(old_value, "aml_DocumentRoot122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot122"):
                opp_val = getattr(value, "aml_DocumentRoot122", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_DocumentRoot:

    def __init__(self, mixed: str, actor: str, date: str, department: str, body: str, description: str, email: str, event: str, firstName: str, label: str, lastName: str, middleName: str, nickName: str, organization: str, perspective: str, rationale: str, region: str, title: str, securityMarking: str, subject: str, symbol: str, url: str, description1: str, id: str, idRef: str, label1: str, aml_DocumentRoot: set["aml_EStringToStringMapEntry"] = None, aml_DocumentRoot71: set["aml_EStringToStringMapEntry"] = None, aml_DocumentRoot92: set["aml_ArgumentTemplate"] = None, aml_DocumentRoot74: set["aml_AggregationRule"] = None, aml_DocumentRoot77: set["aml_AmlDocument"] = None, aml_DocumentRoot80: set["aml_Annotation"] = None, aml_DocumentRoot83: set["aml_Answer"] = None, aml_DocumentRoot86: set["aml_EObject"] = None, aml_DocumentRoot89: set["aml_Argument"] = None, aml_DocumentRoot95: set["aml_Belief"] = None, aml_DocumentRoot98: set["aml_Choice"] = None, aml_DocumentRoot100: set["aml_Collection"] = None, aml_DocumentRoot103: set["aml_CollectionItem"] = None, aml_DocumentRoot106: set["aml_EObject"] = None, aml_DocumentRoot109: set["aml_Coverage"] = None, aml_DocumentRoot112: set["aml_CreatingTool"] = None, aml_DocumentRoot115: set["aml_Creator"] = None, aml_DocumentRoot117: set["aml_Dependent"] = None, aml_DocumentRoot119: set["aml_DiscoveryMethod"] = None, aml_DocumentRoot122: set["aml_End"] = None, aml_DocumentRoot124: set["aml_Evidence"] = None, aml_DocumentRoot127: set["aml_EvidenceExhibit"] = None, aml_DocumentRoot129: set["aml_Exhibit"] = None, aml_DocumentRoot132: set["aml_Flag"] = None, aml_DocumentRoot135: set["aml_EObject"] = None, aml_DocumentRoot138: set["aml_EObject"] = None, aml_DocumentRoot141: set["aml_EObject"] = None, aml_DocumentRoot144: set["aml_Interval"] = None, aml_DocumentRoot146: set["aml_EObject"] = None, aml_DocumentRoot149: set["aml_List"] = None, aml_DocumentRoot151: set["aml_Memo"] = None, aml_DocumentRoot154: set["aml_MetaData"] = None, aml_DocumentRoot157: set["aml_EObject"] = None, aml_DocumentRoot160: set["aml_NationState"] = None, aml_DocumentRoot163: set["aml_Parameter"] = None, aml_DocumentRoot166: set["aml_Period"] = None, aml_DocumentRoot168: set["aml_Person"] = None, aml_DocumentRoot171: set["aml_Publisher"] = None, aml_DocumentRoot173: set["aml_Question"] = None, aml_DocumentRoot176: set["aml_QuestionRelationships"] = None, aml_DocumentRoot178: set["aml_Reader"] = None, aml_DocumentRoot180: set["aml_EObject"] = None, aml_DocumentRoot183: set["aml_Relevance"] = None, aml_DocumentRoot185: set["aml_Reliability"] = None, aml_DocumentRoot187: set["aml_EObject"] = None, aml_DocumentRoot190: set["aml_EObject"] = None, aml_DocumentRoot193: set["aml_Start"] = None, aml_DocumentRoot195: set["aml_Template"] = None, aml_DocumentRoot198: set["aml_EObject"] = None, aml_DocumentRoot201: set["aml_Value"] = None, aml_DocumentRoot203: set["aml_Witness"] = None):
        self.mixed = mixed
        self.actor = actor
        self.date = date
        self.department = department
        self.body = body
        self.description = description
        self.email = email
        self.event = event
        self.firstName = firstName
        self.label = label
        self.lastName = lastName
        self.middleName = middleName
        self.nickName = nickName
        self.organization = organization
        self.perspective = perspective
        self.rationale = rationale
        self.region = region
        self.title = title
        self.securityMarking = securityMarking
        self.subject = subject
        self.symbol = symbol
        self.url = url
        self.description1 = description1
        self.id = id
        self.idRef = idRef
        self.label1 = label1
        self.aml_DocumentRoot = aml_DocumentRoot if aml_DocumentRoot is not None else set()
        self.aml_DocumentRoot71 = aml_DocumentRoot71 if aml_DocumentRoot71 is not None else set()
        self.aml_DocumentRoot92 = aml_DocumentRoot92 if aml_DocumentRoot92 is not None else set()
        self.aml_DocumentRoot74 = aml_DocumentRoot74 if aml_DocumentRoot74 is not None else set()
        self.aml_DocumentRoot77 = aml_DocumentRoot77 if aml_DocumentRoot77 is not None else set()
        self.aml_DocumentRoot80 = aml_DocumentRoot80 if aml_DocumentRoot80 is not None else set()
        self.aml_DocumentRoot83 = aml_DocumentRoot83 if aml_DocumentRoot83 is not None else set()
        self.aml_DocumentRoot86 = aml_DocumentRoot86 if aml_DocumentRoot86 is not None else set()
        self.aml_DocumentRoot89 = aml_DocumentRoot89 if aml_DocumentRoot89 is not None else set()
        self.aml_DocumentRoot95 = aml_DocumentRoot95 if aml_DocumentRoot95 is not None else set()
        self.aml_DocumentRoot98 = aml_DocumentRoot98 if aml_DocumentRoot98 is not None else set()
        self.aml_DocumentRoot100 = aml_DocumentRoot100 if aml_DocumentRoot100 is not None else set()
        self.aml_DocumentRoot103 = aml_DocumentRoot103 if aml_DocumentRoot103 is not None else set()
        self.aml_DocumentRoot106 = aml_DocumentRoot106 if aml_DocumentRoot106 is not None else set()
        self.aml_DocumentRoot109 = aml_DocumentRoot109 if aml_DocumentRoot109 is not None else set()
        self.aml_DocumentRoot112 = aml_DocumentRoot112 if aml_DocumentRoot112 is not None else set()
        self.aml_DocumentRoot115 = aml_DocumentRoot115 if aml_DocumentRoot115 is not None else set()
        self.aml_DocumentRoot117 = aml_DocumentRoot117 if aml_DocumentRoot117 is not None else set()
        self.aml_DocumentRoot119 = aml_DocumentRoot119 if aml_DocumentRoot119 is not None else set()
        self.aml_DocumentRoot122 = aml_DocumentRoot122 if aml_DocumentRoot122 is not None else set()
        self.aml_DocumentRoot124 = aml_DocumentRoot124 if aml_DocumentRoot124 is not None else set()
        self.aml_DocumentRoot127 = aml_DocumentRoot127 if aml_DocumentRoot127 is not None else set()
        self.aml_DocumentRoot129 = aml_DocumentRoot129 if aml_DocumentRoot129 is not None else set()
        self.aml_DocumentRoot132 = aml_DocumentRoot132 if aml_DocumentRoot132 is not None else set()
        self.aml_DocumentRoot135 = aml_DocumentRoot135 if aml_DocumentRoot135 is not None else set()
        self.aml_DocumentRoot138 = aml_DocumentRoot138 if aml_DocumentRoot138 is not None else set()
        self.aml_DocumentRoot141 = aml_DocumentRoot141 if aml_DocumentRoot141 is not None else set()
        self.aml_DocumentRoot144 = aml_DocumentRoot144 if aml_DocumentRoot144 is not None else set()
        self.aml_DocumentRoot146 = aml_DocumentRoot146 if aml_DocumentRoot146 is not None else set()
        self.aml_DocumentRoot149 = aml_DocumentRoot149 if aml_DocumentRoot149 is not None else set()
        self.aml_DocumentRoot151 = aml_DocumentRoot151 if aml_DocumentRoot151 is not None else set()
        self.aml_DocumentRoot154 = aml_DocumentRoot154 if aml_DocumentRoot154 is not None else set()
        self.aml_DocumentRoot157 = aml_DocumentRoot157 if aml_DocumentRoot157 is not None else set()
        self.aml_DocumentRoot160 = aml_DocumentRoot160 if aml_DocumentRoot160 is not None else set()
        self.aml_DocumentRoot163 = aml_DocumentRoot163 if aml_DocumentRoot163 is not None else set()
        self.aml_DocumentRoot166 = aml_DocumentRoot166 if aml_DocumentRoot166 is not None else set()
        self.aml_DocumentRoot168 = aml_DocumentRoot168 if aml_DocumentRoot168 is not None else set()
        self.aml_DocumentRoot171 = aml_DocumentRoot171 if aml_DocumentRoot171 is not None else set()
        self.aml_DocumentRoot173 = aml_DocumentRoot173 if aml_DocumentRoot173 is not None else set()
        self.aml_DocumentRoot176 = aml_DocumentRoot176 if aml_DocumentRoot176 is not None else set()
        self.aml_DocumentRoot178 = aml_DocumentRoot178 if aml_DocumentRoot178 is not None else set()
        self.aml_DocumentRoot180 = aml_DocumentRoot180 if aml_DocumentRoot180 is not None else set()
        self.aml_DocumentRoot183 = aml_DocumentRoot183 if aml_DocumentRoot183 is not None else set()
        self.aml_DocumentRoot185 = aml_DocumentRoot185 if aml_DocumentRoot185 is not None else set()
        self.aml_DocumentRoot187 = aml_DocumentRoot187 if aml_DocumentRoot187 is not None else set()
        self.aml_DocumentRoot190 = aml_DocumentRoot190 if aml_DocumentRoot190 is not None else set()
        self.aml_DocumentRoot193 = aml_DocumentRoot193 if aml_DocumentRoot193 is not None else set()
        self.aml_DocumentRoot195 = aml_DocumentRoot195 if aml_DocumentRoot195 is not None else set()
        self.aml_DocumentRoot198 = aml_DocumentRoot198 if aml_DocumentRoot198 is not None else set()
        self.aml_DocumentRoot201 = aml_DocumentRoot201 if aml_DocumentRoot201 is not None else set()
        self.aml_DocumentRoot203 = aml_DocumentRoot203 if aml_DocumentRoot203 is not None else set()
        
    @property
    def department(self) -> str:
        return self.__department

    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def actor(self) -> str:
        return self.__actor

    @actor.setter
    def actor(self, actor: str):
        self.__actor = actor

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def perspective(self) -> str:
        return self.__perspective

    @perspective.setter
    def perspective(self, perspective: str):
        self.__perspective = perspective

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def nickName(self) -> str:
        return self.__nickName

    @nickName.setter
    def nickName(self, nickName: str):
        self.__nickName = nickName

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def middleName(self) -> str:
        return self.__middleName

    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def label1(self) -> str:
        return self.__label1

    @label1.setter
    def label1(self, label1: str):
        self.__label1 = label1

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def securityMarking(self) -> str:
        return self.__securityMarking

    @securityMarking.setter
    def securityMarking(self, securityMarking: str):
        self.__securityMarking = securityMarking

    @property
    def description1(self) -> str:
        return self.__description1

    @description1.setter
    def description1(self, description1: str):
        self.__description1 = description1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def region(self) -> str:
        return self.__region

    @region.setter
    def region(self, region: str):
        self.__region = region

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aml_DocumentRoot119(self):
        return self.__aml_DocumentRoot119

    @aml_DocumentRoot119.setter
    def aml_DocumentRoot119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot119", None)
        self.__aml_DocumentRoot119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_DiscoveryMethod120"):
                    opp_val = getattr(item, "aml_DiscoveryMethod120", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_DiscoveryMethod120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_DiscoveryMethod120"):
                    opp_val = getattr(item, "aml_DiscoveryMethod120", None)
                    
                    setattr(item, "aml_DiscoveryMethod120", self)
                    

    @property
    def aml_DocumentRoot92(self):
        return self.__aml_DocumentRoot92

    @aml_DocumentRoot92.setter
    def aml_DocumentRoot92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot92", None)
        self.__aml_DocumentRoot92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_ArgumentTemplate93"):
                    opp_val = getattr(item, "aml_ArgumentTemplate93", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_ArgumentTemplate93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_ArgumentTemplate93"):
                    opp_val = getattr(item, "aml_ArgumentTemplate93", None)
                    
                    setattr(item, "aml_ArgumentTemplate93", self)
                    

    @property
    def aml_DocumentRoot178(self):
        return self.__aml_DocumentRoot178

    @aml_DocumentRoot178.setter
    def aml_DocumentRoot178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot178", None)
        self.__aml_DocumentRoot178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Reader"):
                    opp_val = getattr(item, "aml_Reader", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Reader", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Reader"):
                    opp_val = getattr(item, "aml_Reader", None)
                    
                    setattr(item, "aml_Reader", self)
                    

    @property
    def aml_DocumentRoot98(self):
        return self.__aml_DocumentRoot98

    @aml_DocumentRoot98.setter
    def aml_DocumentRoot98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot98", None)
        self.__aml_DocumentRoot98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Choice"):
                    opp_val = getattr(item, "aml_Choice", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Choice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Choice"):
                    opp_val = getattr(item, "aml_Choice", None)
                    
                    setattr(item, "aml_Choice", self)
                    

    @property
    def aml_DocumentRoot122(self):
        return self.__aml_DocumentRoot122

    @aml_DocumentRoot122.setter
    def aml_DocumentRoot122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot122", None)
        self.__aml_DocumentRoot122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_End"):
                    opp_val = getattr(item, "aml_End", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_End", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_End"):
                    opp_val = getattr(item, "aml_End", None)
                    
                    setattr(item, "aml_End", self)
                    

    @property
    def aml_DocumentRoot163(self):
        return self.__aml_DocumentRoot163

    @aml_DocumentRoot163.setter
    def aml_DocumentRoot163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot163", None)
        self.__aml_DocumentRoot163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Parameter164"):
                    opp_val = getattr(item, "aml_Parameter164", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Parameter164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Parameter164"):
                    opp_val = getattr(item, "aml_Parameter164", None)
                    
                    setattr(item, "aml_Parameter164", self)
                    

    @property
    def aml_DocumentRoot173(self):
        return self.__aml_DocumentRoot173

    @aml_DocumentRoot173.setter
    def aml_DocumentRoot173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot173", None)
        self.__aml_DocumentRoot173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Question174"):
                    opp_val = getattr(item, "aml_Question174", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Question174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Question174"):
                    opp_val = getattr(item, "aml_Question174", None)
                    
                    setattr(item, "aml_Question174", self)
                    

    @property
    def aml_DocumentRoot135(self):
        return self.__aml_DocumentRoot135

    @aml_DocumentRoot135.setter
    def aml_DocumentRoot135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot135", None)
        self.__aml_DocumentRoot135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject136"):
                    opp_val = getattr(item, "aml_EObject136", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject136"):
                    opp_val = getattr(item, "aml_EObject136", None)
                    
                    setattr(item, "aml_EObject136", self)
                    

    @property
    def aml_DocumentRoot83(self):
        return self.__aml_DocumentRoot83

    @aml_DocumentRoot83.setter
    def aml_DocumentRoot83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot83", None)
        self.__aml_DocumentRoot83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Answer84"):
                    opp_val = getattr(item, "aml_Answer84", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Answer84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Answer84"):
                    opp_val = getattr(item, "aml_Answer84", None)
                    
                    setattr(item, "aml_Answer84", self)
                    

    @property
    def aml_DocumentRoot129(self):
        return self.__aml_DocumentRoot129

    @aml_DocumentRoot129.setter
    def aml_DocumentRoot129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot129", None)
        self.__aml_DocumentRoot129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Exhibit130"):
                    opp_val = getattr(item, "aml_Exhibit130", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Exhibit130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Exhibit130"):
                    opp_val = getattr(item, "aml_Exhibit130", None)
                    
                    setattr(item, "aml_Exhibit130", self)
                    

    @property
    def aml_DocumentRoot149(self):
        return self.__aml_DocumentRoot149

    @aml_DocumentRoot149.setter
    def aml_DocumentRoot149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot149", None)
        self.__aml_DocumentRoot149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_List"):
                    opp_val = getattr(item, "aml_List", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_List", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_List"):
                    opp_val = getattr(item, "aml_List", None)
                    
                    setattr(item, "aml_List", self)
                    

    @property
    def aml_DocumentRoot201(self):
        return self.__aml_DocumentRoot201

    @aml_DocumentRoot201.setter
    def aml_DocumentRoot201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot201", None)
        self.__aml_DocumentRoot201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Value"):
                    opp_val = getattr(item, "aml_Value", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Value"):
                    opp_val = getattr(item, "aml_Value", None)
                    
                    setattr(item, "aml_Value", self)
                    

    @property
    def aml_DocumentRoot100(self):
        return self.__aml_DocumentRoot100

    @aml_DocumentRoot100.setter
    def aml_DocumentRoot100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot100", None)
        self.__aml_DocumentRoot100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Collection101"):
                    opp_val = getattr(item, "aml_Collection101", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Collection101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Collection101"):
                    opp_val = getattr(item, "aml_Collection101", None)
                    
                    setattr(item, "aml_Collection101", self)
                    

    @property
    def aml_DocumentRoot195(self):
        return self.__aml_DocumentRoot195

    @aml_DocumentRoot195.setter
    def aml_DocumentRoot195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot195", None)
        self.__aml_DocumentRoot195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Template196"):
                    opp_val = getattr(item, "aml_Template196", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Template196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Template196"):
                    opp_val = getattr(item, "aml_Template196", None)
                    
                    setattr(item, "aml_Template196", self)
                    

    @property
    def aml_DocumentRoot180(self):
        return self.__aml_DocumentRoot180

    @aml_DocumentRoot180.setter
    def aml_DocumentRoot180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot180", None)
        self.__aml_DocumentRoot180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject181"):
                    opp_val = getattr(item, "aml_EObject181", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject181"):
                    opp_val = getattr(item, "aml_EObject181", None)
                    
                    setattr(item, "aml_EObject181", self)
                    

    @property
    def aml_DocumentRoot117(self):
        return self.__aml_DocumentRoot117

    @aml_DocumentRoot117.setter
    def aml_DocumentRoot117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot117", None)
        self.__aml_DocumentRoot117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Dependent"):
                    opp_val = getattr(item, "aml_Dependent", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Dependent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Dependent"):
                    opp_val = getattr(item, "aml_Dependent", None)
                    
                    setattr(item, "aml_Dependent", self)
                    

    @property
    def aml_DocumentRoot203(self):
        return self.__aml_DocumentRoot203

    @aml_DocumentRoot203.setter
    def aml_DocumentRoot203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot203", None)
        self.__aml_DocumentRoot203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Witness204"):
                    opp_val = getattr(item, "aml_Witness204", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Witness204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Witness204"):
                    opp_val = getattr(item, "aml_Witness204", None)
                    
                    setattr(item, "aml_Witness204", self)
                    

    @property
    def aml_DocumentRoot185(self):
        return self.__aml_DocumentRoot185

    @aml_DocumentRoot185.setter
    def aml_DocumentRoot185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot185", None)
        self.__aml_DocumentRoot185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Reliability"):
                    opp_val = getattr(item, "aml_Reliability", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Reliability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Reliability"):
                    opp_val = getattr(item, "aml_Reliability", None)
                    
                    setattr(item, "aml_Reliability", self)
                    

    @property
    def aml_DocumentRoot154(self):
        return self.__aml_DocumentRoot154

    @aml_DocumentRoot154.setter
    def aml_DocumentRoot154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot154", None)
        self.__aml_DocumentRoot154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_MetaData155"):
                    opp_val = getattr(item, "aml_MetaData155", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_MetaData155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_MetaData155"):
                    opp_val = getattr(item, "aml_MetaData155", None)
                    
                    setattr(item, "aml_MetaData155", self)
                    

    @property
    def aml_DocumentRoot190(self):
        return self.__aml_DocumentRoot190

    @aml_DocumentRoot190.setter
    def aml_DocumentRoot190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot190", None)
        self.__aml_DocumentRoot190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject191"):
                    opp_val = getattr(item, "aml_EObject191", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject191"):
                    opp_val = getattr(item, "aml_EObject191", None)
                    
                    setattr(item, "aml_EObject191", self)
                    

    @property
    def aml_DocumentRoot198(self):
        return self.__aml_DocumentRoot198

    @aml_DocumentRoot198.setter
    def aml_DocumentRoot198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot198", None)
        self.__aml_DocumentRoot198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject199"):
                    opp_val = getattr(item, "aml_EObject199", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject199"):
                    opp_val = getattr(item, "aml_EObject199", None)
                    
                    setattr(item, "aml_EObject199", self)
                    

    @property
    def aml_DocumentRoot187(self):
        return self.__aml_DocumentRoot187

    @aml_DocumentRoot187.setter
    def aml_DocumentRoot187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot187", None)
        self.__aml_DocumentRoot187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject188"):
                    opp_val = getattr(item, "aml_EObject188", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject188"):
                    opp_val = getattr(item, "aml_EObject188", None)
                    
                    setattr(item, "aml_EObject188", self)
                    

    @property
    def aml_DocumentRoot95(self):
        return self.__aml_DocumentRoot95

    @aml_DocumentRoot95.setter
    def aml_DocumentRoot95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot95", None)
        self.__aml_DocumentRoot95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Belief96"):
                    opp_val = getattr(item, "aml_Belief96", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Belief96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Belief96"):
                    opp_val = getattr(item, "aml_Belief96", None)
                    
                    setattr(item, "aml_Belief96", self)
                    

    @property
    def aml_DocumentRoot89(self):
        return self.__aml_DocumentRoot89

    @aml_DocumentRoot89.setter
    def aml_DocumentRoot89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot89", None)
        self.__aml_DocumentRoot89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Argument90"):
                    opp_val = getattr(item, "aml_Argument90", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Argument90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Argument90"):
                    opp_val = getattr(item, "aml_Argument90", None)
                    
                    setattr(item, "aml_Argument90", self)
                    

    @property
    def aml_DocumentRoot138(self):
        return self.__aml_DocumentRoot138

    @aml_DocumentRoot138.setter
    def aml_DocumentRoot138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot138", None)
        self.__aml_DocumentRoot138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject139"):
                    opp_val = getattr(item, "aml_EObject139", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject139"):
                    opp_val = getattr(item, "aml_EObject139", None)
                    
                    setattr(item, "aml_EObject139", self)
                    

    @property
    def aml_DocumentRoot168(self):
        return self.__aml_DocumentRoot168

    @aml_DocumentRoot168.setter
    def aml_DocumentRoot168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot168", None)
        self.__aml_DocumentRoot168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Person169"):
                    opp_val = getattr(item, "aml_Person169", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Person169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Person169"):
                    opp_val = getattr(item, "aml_Person169", None)
                    
                    setattr(item, "aml_Person169", self)
                    

    @property
    def aml_DocumentRoot157(self):
        return self.__aml_DocumentRoot157

    @aml_DocumentRoot157.setter
    def aml_DocumentRoot157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot157", None)
        self.__aml_DocumentRoot157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject158"):
                    opp_val = getattr(item, "aml_EObject158", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject158"):
                    opp_val = getattr(item, "aml_EObject158", None)
                    
                    setattr(item, "aml_EObject158", self)
                    

    @property
    def aml_DocumentRoot86(self):
        return self.__aml_DocumentRoot86

    @aml_DocumentRoot86.setter
    def aml_DocumentRoot86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot86", None)
        self.__aml_DocumentRoot86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject87"):
                    opp_val = getattr(item, "aml_EObject87", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject87"):
                    opp_val = getattr(item, "aml_EObject87", None)
                    
                    setattr(item, "aml_EObject87", self)
                    

    @property
    def aml_DocumentRoot193(self):
        return self.__aml_DocumentRoot193

    @aml_DocumentRoot193.setter
    def aml_DocumentRoot193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot193", None)
        self.__aml_DocumentRoot193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Start"):
                    opp_val = getattr(item, "aml_Start", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Start", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Start"):
                    opp_val = getattr(item, "aml_Start", None)
                    
                    setattr(item, "aml_Start", self)
                    

    @property
    def aml_DocumentRoot132(self):
        return self.__aml_DocumentRoot132

    @aml_DocumentRoot132.setter
    def aml_DocumentRoot132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot132", None)
        self.__aml_DocumentRoot132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Flag133"):
                    opp_val = getattr(item, "aml_Flag133", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Flag133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Flag133"):
                    opp_val = getattr(item, "aml_Flag133", None)
                    
                    setattr(item, "aml_Flag133", self)
                    

    @property
    def aml_DocumentRoot171(self):
        return self.__aml_DocumentRoot171

    @aml_DocumentRoot171.setter
    def aml_DocumentRoot171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot171", None)
        self.__aml_DocumentRoot171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Publisher"):
                    opp_val = getattr(item, "aml_Publisher", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Publisher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Publisher"):
                    opp_val = getattr(item, "aml_Publisher", None)
                    
                    setattr(item, "aml_Publisher", self)
                    

    @property
    def aml_DocumentRoot146(self):
        return self.__aml_DocumentRoot146

    @aml_DocumentRoot146.setter
    def aml_DocumentRoot146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot146", None)
        self.__aml_DocumentRoot146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject147"):
                    opp_val = getattr(item, "aml_EObject147", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject147"):
                    opp_val = getattr(item, "aml_EObject147", None)
                    
                    setattr(item, "aml_EObject147", self)
                    

    @property
    def aml_DocumentRoot112(self):
        return self.__aml_DocumentRoot112

    @aml_DocumentRoot112.setter
    def aml_DocumentRoot112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot112", None)
        self.__aml_DocumentRoot112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_CreatingTool113"):
                    opp_val = getattr(item, "aml_CreatingTool113", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_CreatingTool113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_CreatingTool113"):
                    opp_val = getattr(item, "aml_CreatingTool113", None)
                    
                    setattr(item, "aml_CreatingTool113", self)
                    

    @property
    def aml_DocumentRoot115(self):
        return self.__aml_DocumentRoot115

    @aml_DocumentRoot115.setter
    def aml_DocumentRoot115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot115", None)
        self.__aml_DocumentRoot115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Creator"):
                    opp_val = getattr(item, "aml_Creator", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Creator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Creator"):
                    opp_val = getattr(item, "aml_Creator", None)
                    
                    setattr(item, "aml_Creator", self)
                    

    @property
    def aml_DocumentRoot151(self):
        return self.__aml_DocumentRoot151

    @aml_DocumentRoot151.setter
    def aml_DocumentRoot151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot151", None)
        self.__aml_DocumentRoot151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Memo152"):
                    opp_val = getattr(item, "aml_Memo152", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Memo152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Memo152"):
                    opp_val = getattr(item, "aml_Memo152", None)
                    
                    setattr(item, "aml_Memo152", self)
                    

    @property
    def aml_DocumentRoot183(self):
        return self.__aml_DocumentRoot183

    @aml_DocumentRoot183.setter
    def aml_DocumentRoot183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot183", None)
        self.__aml_DocumentRoot183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Relevance"):
                    opp_val = getattr(item, "aml_Relevance", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Relevance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Relevance"):
                    opp_val = getattr(item, "aml_Relevance", None)
                    
                    setattr(item, "aml_Relevance", self)
                    

    @property
    def aml_DocumentRoot176(self):
        return self.__aml_DocumentRoot176

    @aml_DocumentRoot176.setter
    def aml_DocumentRoot176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot176", None)
        self.__aml_DocumentRoot176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_QuestionRelationships"):
                    opp_val = getattr(item, "aml_QuestionRelationships", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_QuestionRelationships", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_QuestionRelationships"):
                    opp_val = getattr(item, "aml_QuestionRelationships", None)
                    
                    setattr(item, "aml_QuestionRelationships", self)
                    

    @property
    def aml_DocumentRoot160(self):
        return self.__aml_DocumentRoot160

    @aml_DocumentRoot160.setter
    def aml_DocumentRoot160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot160", None)
        self.__aml_DocumentRoot160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_NationState161"):
                    opp_val = getattr(item, "aml_NationState161", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_NationState161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_NationState161"):
                    opp_val = getattr(item, "aml_NationState161", None)
                    
                    setattr(item, "aml_NationState161", self)
                    

    @property
    def aml_DocumentRoot144(self):
        return self.__aml_DocumentRoot144

    @aml_DocumentRoot144.setter
    def aml_DocumentRoot144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot144", None)
        self.__aml_DocumentRoot144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Interval"):
                    opp_val = getattr(item, "aml_Interval", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Interval", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Interval"):
                    opp_val = getattr(item, "aml_Interval", None)
                    
                    setattr(item, "aml_Interval", self)
                    

    @property
    def aml_DocumentRoot(self):
        return self.__aml_DocumentRoot

    @aml_DocumentRoot.setter
    def aml_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot", None)
        self.__aml_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "aml_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "aml_EStringToStringMapEntry", None)
                    
                    setattr(item, "aml_EStringToStringMapEntry", self)
                    

    @property
    def aml_DocumentRoot166(self):
        return self.__aml_DocumentRoot166

    @aml_DocumentRoot166.setter
    def aml_DocumentRoot166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot166", None)
        self.__aml_DocumentRoot166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Period"):
                    opp_val = getattr(item, "aml_Period", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Period", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Period"):
                    opp_val = getattr(item, "aml_Period", None)
                    
                    setattr(item, "aml_Period", self)
                    

    @property
    def aml_DocumentRoot77(self):
        return self.__aml_DocumentRoot77

    @aml_DocumentRoot77.setter
    def aml_DocumentRoot77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot77", None)
        self.__aml_DocumentRoot77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_AmlDocument78"):
                    opp_val = getattr(item, "aml_AmlDocument78", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_AmlDocument78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_AmlDocument78"):
                    opp_val = getattr(item, "aml_AmlDocument78", None)
                    
                    setattr(item, "aml_AmlDocument78", self)
                    

    @property
    def aml_DocumentRoot109(self):
        return self.__aml_DocumentRoot109

    @aml_DocumentRoot109.setter
    def aml_DocumentRoot109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot109", None)
        self.__aml_DocumentRoot109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Coverage110"):
                    opp_val = getattr(item, "aml_Coverage110", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Coverage110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Coverage110"):
                    opp_val = getattr(item, "aml_Coverage110", None)
                    
                    setattr(item, "aml_Coverage110", self)
                    

    @property
    def aml_DocumentRoot103(self):
        return self.__aml_DocumentRoot103

    @aml_DocumentRoot103.setter
    def aml_DocumentRoot103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot103", None)
        self.__aml_DocumentRoot103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_CollectionItem104"):
                    opp_val = getattr(item, "aml_CollectionItem104", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_CollectionItem104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_CollectionItem104"):
                    opp_val = getattr(item, "aml_CollectionItem104", None)
                    
                    setattr(item, "aml_CollectionItem104", self)
                    

    @property
    def aml_DocumentRoot80(self):
        return self.__aml_DocumentRoot80

    @aml_DocumentRoot80.setter
    def aml_DocumentRoot80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot80", None)
        self.__aml_DocumentRoot80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation81"):
                    opp_val = getattr(item, "aml_Annotation81", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation81"):
                    opp_val = getattr(item, "aml_Annotation81", None)
                    
                    setattr(item, "aml_Annotation81", self)
                    

    @property
    def aml_DocumentRoot106(self):
        return self.__aml_DocumentRoot106

    @aml_DocumentRoot106.setter
    def aml_DocumentRoot106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot106", None)
        self.__aml_DocumentRoot106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject107"):
                    opp_val = getattr(item, "aml_EObject107", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject107"):
                    opp_val = getattr(item, "aml_EObject107", None)
                    
                    setattr(item, "aml_EObject107", self)
                    

    @property
    def aml_DocumentRoot74(self):
        return self.__aml_DocumentRoot74

    @aml_DocumentRoot74.setter
    def aml_DocumentRoot74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot74", None)
        self.__aml_DocumentRoot74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_AggregationRule75"):
                    opp_val = getattr(item, "aml_AggregationRule75", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_AggregationRule75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_AggregationRule75"):
                    opp_val = getattr(item, "aml_AggregationRule75", None)
                    
                    setattr(item, "aml_AggregationRule75", self)
                    

    @property
    def aml_DocumentRoot127(self):
        return self.__aml_DocumentRoot127

    @aml_DocumentRoot127.setter
    def aml_DocumentRoot127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot127", None)
        self.__aml_DocumentRoot127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EvidenceExhibit"):
                    opp_val = getattr(item, "aml_EvidenceExhibit", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EvidenceExhibit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EvidenceExhibit"):
                    opp_val = getattr(item, "aml_EvidenceExhibit", None)
                    
                    setattr(item, "aml_EvidenceExhibit", self)
                    

    @property
    def aml_DocumentRoot141(self):
        return self.__aml_DocumentRoot141

    @aml_DocumentRoot141.setter
    def aml_DocumentRoot141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot141", None)
        self.__aml_DocumentRoot141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject142"):
                    opp_val = getattr(item, "aml_EObject142", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject142"):
                    opp_val = getattr(item, "aml_EObject142", None)
                    
                    setattr(item, "aml_EObject142", self)
                    

    @property
    def aml_DocumentRoot124(self):
        return self.__aml_DocumentRoot124

    @aml_DocumentRoot124.setter
    def aml_DocumentRoot124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot124", None)
        self.__aml_DocumentRoot124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Evidence125"):
                    opp_val = getattr(item, "aml_Evidence125", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Evidence125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Evidence125"):
                    opp_val = getattr(item, "aml_Evidence125", None)
                    
                    setattr(item, "aml_Evidence125", self)
                    

    @property
    def aml_DocumentRoot71(self):
        return self.__aml_DocumentRoot71

    @aml_DocumentRoot71.setter
    def aml_DocumentRoot71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DocumentRoot__aml_DocumentRoot71", None)
        self.__aml_DocumentRoot71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EStringToStringMapEntry72"):
                    opp_val = getattr(item, "aml_EStringToStringMapEntry72", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EStringToStringMapEntry72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EStringToStringMapEntry72"):
                    opp_val = getattr(item, "aml_EStringToStringMapEntry72", None)
                    
                    setattr(item, "aml_EStringToStringMapEntry72", self)
                    

class aml_EStringToStringMapEntry:

    pass
class aml_Creator:

    def __init__(self, objectType: str, description: str, idRef: str, aml_Creator: "aml_DocumentRoot" = None, aml_Creator243: "aml_MetaData" = None, aml_Creator237: "aml_Memo" = None):
        self.objectType = objectType
        self.description = description
        self.idRef = idRef
        self.aml_Creator = aml_Creator
        self.aml_Creator243 = aml_Creator243
        self.aml_Creator237 = aml_Creator237
        
    @property
    def objectType(self) -> str:
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def aml_Creator243(self):
        return self.__aml_Creator243

    @aml_Creator243.setter
    def aml_Creator243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Creator__aml_Creator243", None)
        self.__aml_Creator243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData242"):
                opp_val = getattr(old_value, "aml_MetaData242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData242"):
                opp_val = getattr(value, "aml_MetaData242", None)
                if opp_val is None:
                    setattr(value, "aml_MetaData242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Creator237(self):
        return self.__aml_Creator237

    @aml_Creator237.setter
    def aml_Creator237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Creator__aml_Creator237", None)
        self.__aml_Creator237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Memo236"):
                opp_val = getattr(old_value, "aml_Memo236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Memo236"):
                opp_val = getattr(value, "aml_Memo236", None)
                if opp_val is None:
                    setattr(value, "aml_Memo236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Creator(self):
        return self.__aml_Creator

    @aml_Creator.setter
    def aml_Creator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Creator__aml_Creator", None)
        self.__aml_Creator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot115"):
                opp_val = getattr(old_value, "aml_DocumentRoot115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot115"):
                opp_val = getattr(value, "aml_DocumentRoot115", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_NationState:

    def __init__(self, group: str, perspective: str, actor: str, region: str, event: str, aml_NationState: "aml_Coverage" = None, aml_NationState161: "aml_DocumentRoot" = None, aml_NationState281: set["aml_Period"] = None):
        self.group = group
        self.perspective = perspective
        self.actor = actor
        self.region = region
        self.event = event
        self.aml_NationState = aml_NationState
        self.aml_NationState161 = aml_NationState161
        self.aml_NationState281 = aml_NationState281 if aml_NationState281 is not None else set()
        
    @property
    def region(self) -> str:
        return self.__region

    @region.setter
    def region(self, region: str):
        self.__region = region

    @property
    def perspective(self) -> str:
        return self.__perspective

    @perspective.setter
    def perspective(self, perspective: str):
        self.__perspective = perspective

    @property
    def actor(self) -> str:
        return self.__actor

    @actor.setter
    def actor(self, actor: str):
        self.__actor = actor

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def aml_NationState281(self):
        return self.__aml_NationState281

    @aml_NationState281.setter
    def aml_NationState281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_NationState__aml_NationState281", None)
        self.__aml_NationState281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Period282"):
                    opp_val = getattr(item, "aml_Period282", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Period282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Period282"):
                    opp_val = getattr(item, "aml_Period282", None)
                    
                    setattr(item, "aml_Period282", self)
                    

    @property
    def aml_NationState161(self):
        return self.__aml_NationState161

    @aml_NationState161.setter
    def aml_NationState161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_NationState__aml_NationState161", None)
        self.__aml_NationState161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot160"):
                opp_val = getattr(old_value, "aml_DocumentRoot160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot160"):
                opp_val = getattr(value, "aml_DocumentRoot160", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_NationState(self):
        return self.__aml_NationState

    @aml_NationState.setter
    def aml_NationState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_NationState__aml_NationState", None)
        self.__aml_NationState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Coverage"):
                opp_val = getattr(old_value, "aml_Coverage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Coverage"):
                opp_val = getattr(value, "aml_Coverage", None)
                if opp_val is None:
                    setattr(value, "aml_Coverage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Coverage:

    def __init__(self, mixed: str, group: str, aml_Coverage: set["aml_NationState"] = None, aml_Coverage110: "aml_DocumentRoot" = None, aml_Coverage273: "aml_MetaData" = None):
        self.mixed = mixed
        self.group = group
        self.aml_Coverage = aml_Coverage if aml_Coverage is not None else set()
        self.aml_Coverage110 = aml_Coverage110
        self.aml_Coverage273 = aml_Coverage273
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def aml_Coverage(self):
        return self.__aml_Coverage

    @aml_Coverage.setter
    def aml_Coverage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Coverage__aml_Coverage", None)
        self.__aml_Coverage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_NationState"):
                    opp_val = getattr(item, "aml_NationState", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_NationState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_NationState"):
                    opp_val = getattr(item, "aml_NationState", None)
                    
                    setattr(item, "aml_NationState", self)
                    

    @property
    def aml_Coverage273(self):
        return self.__aml_Coverage273

    @aml_Coverage273.setter
    def aml_Coverage273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Coverage__aml_Coverage273", None)
        self.__aml_Coverage273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData272"):
                opp_val = getattr(old_value, "aml_MetaData272", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData272"):
                opp_val = getattr(value, "aml_MetaData272", None)
                if opp_val is None:
                    setattr(value, "aml_MetaData272", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Coverage110(self):
        return self.__aml_Coverage110

    @aml_Coverage110.setter
    def aml_Coverage110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Coverage__aml_Coverage110", None)
        self.__aml_Coverage110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot109"):
                opp_val = getattr(old_value, "aml_DocumentRoot109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot109"):
                opp_val = getattr(value, "aml_DocumentRoot109", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Dependent:

    def __init__(self, idRef: str, ordinal: str, aml_Dependent: "aml_DocumentRoot" = None, aml_Dependent294: "aml_QuestionRelationships" = None):
        self.idRef = idRef
        self.ordinal = ordinal
        self.aml_Dependent = aml_Dependent
        self.aml_Dependent294 = aml_Dependent294
        
    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def aml_Dependent294(self):
        return self.__aml_Dependent294

    @aml_Dependent294.setter
    def aml_Dependent294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Dependent__aml_Dependent294", None)
        self.__aml_Dependent294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_QuestionRelationships293"):
                opp_val = getattr(old_value, "aml_QuestionRelationships293", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_QuestionRelationships293"):
                opp_val = getattr(value, "aml_QuestionRelationships293", None)
                if opp_val is None:
                    setattr(value, "aml_QuestionRelationships293", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Dependent(self):
        return self.__aml_Dependent

    @aml_Dependent.setter
    def aml_Dependent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Dependent__aml_Dependent", None)
        self.__aml_Dependent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot117"):
                opp_val = getattr(old_value, "aml_DocumentRoot117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot117"):
                opp_val = getattr(value, "aml_DocumentRoot117", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Question:

    def __init__(self, group: str, amplification: str, description: str, id: str, label: str, aml_Question: "aml_Collection" = None, aml_Question174: "aml_DocumentRoot" = None, aml_Question305: set["aml_AggregationRule"] = None, aml_Question308: set["aml_DiscoveryMethod"] = None, aml_Question311: set["aml_Annotation"] = None, aml_Question296: set["aml_EObject"] = None, aml_Question299: set["aml_Choice"] = None, aml_Question302: set["aml_QuestionRelationships"] = None, aml_Question324: "aml_Template" = None):
        self.group = group
        self.amplification = amplification
        self.description = description
        self.id = id
        self.label = label
        self.aml_Question = aml_Question
        self.aml_Question174 = aml_Question174
        self.aml_Question305 = aml_Question305 if aml_Question305 is not None else set()
        self.aml_Question308 = aml_Question308 if aml_Question308 is not None else set()
        self.aml_Question311 = aml_Question311 if aml_Question311 is not None else set()
        self.aml_Question296 = aml_Question296 if aml_Question296 is not None else set()
        self.aml_Question299 = aml_Question299 if aml_Question299 is not None else set()
        self.aml_Question302 = aml_Question302 if aml_Question302 is not None else set()
        self.aml_Question324 = aml_Question324
        
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
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def amplification(self) -> str:
        return self.__amplification

    @amplification.setter
    def amplification(self, amplification: str):
        self.__amplification = amplification

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aml_Question296(self):
        return self.__aml_Question296

    @aml_Question296.setter
    def aml_Question296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question296", None)
        self.__aml_Question296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject297"):
                    opp_val = getattr(item, "aml_EObject297", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject297"):
                    opp_val = getattr(item, "aml_EObject297", None)
                    
                    setattr(item, "aml_EObject297", self)
                    

    @property
    def aml_Question299(self):
        return self.__aml_Question299

    @aml_Question299.setter
    def aml_Question299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question299", None)
        self.__aml_Question299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Choice300"):
                    opp_val = getattr(item, "aml_Choice300", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Choice300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Choice300"):
                    opp_val = getattr(item, "aml_Choice300", None)
                    
                    setattr(item, "aml_Choice300", self)
                    

    @property
    def aml_Question174(self):
        return self.__aml_Question174

    @aml_Question174.setter
    def aml_Question174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question174", None)
        self.__aml_Question174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot173"):
                opp_val = getattr(old_value, "aml_DocumentRoot173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot173"):
                opp_val = getattr(value, "aml_DocumentRoot173", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Question(self):
        return self.__aml_Question

    @aml_Question.setter
    def aml_Question(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question", None)
        self.__aml_Question = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Collection56"):
                opp_val = getattr(old_value, "aml_Collection56", None)
                if opp_val == self:
                    setattr(old_value, "aml_Collection56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Collection56"):
                opp_val = getattr(value, "aml_Collection56", None)
                setattr(value, "aml_Collection56", self)

    @property
    def aml_Question324(self):
        return self.__aml_Question324

    @aml_Question324.setter
    def aml_Question324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question324", None)
        self.__aml_Question324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Template323"):
                opp_val = getattr(old_value, "aml_Template323", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Template323"):
                opp_val = getattr(value, "aml_Template323", None)
                if opp_val is None:
                    setattr(value, "aml_Template323", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Question308(self):
        return self.__aml_Question308

    @aml_Question308.setter
    def aml_Question308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question308", None)
        self.__aml_Question308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_DiscoveryMethod309"):
                    opp_val = getattr(item, "aml_DiscoveryMethod309", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_DiscoveryMethod309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_DiscoveryMethod309"):
                    opp_val = getattr(item, "aml_DiscoveryMethod309", None)
                    
                    setattr(item, "aml_DiscoveryMethod309", self)
                    

    @property
    def aml_Question302(self):
        return self.__aml_Question302

    @aml_Question302.setter
    def aml_Question302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question302", None)
        self.__aml_Question302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_QuestionRelationships303"):
                    opp_val = getattr(item, "aml_QuestionRelationships303", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_QuestionRelationships303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_QuestionRelationships303"):
                    opp_val = getattr(item, "aml_QuestionRelationships303", None)
                    
                    setattr(item, "aml_QuestionRelationships303", self)
                    

    @property
    def aml_Question305(self):
        return self.__aml_Question305

    @aml_Question305.setter
    def aml_Question305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question305", None)
        self.__aml_Question305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_AggregationRule306"):
                    opp_val = getattr(item, "aml_AggregationRule306", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_AggregationRule306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_AggregationRule306"):
                    opp_val = getattr(item, "aml_AggregationRule306", None)
                    
                    setattr(item, "aml_AggregationRule306", self)
                    

    @property
    def aml_Question311(self):
        return self.__aml_Question311

    @aml_Question311.setter
    def aml_Question311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Question__aml_Question311", None)
        self.__aml_Question311 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation312"):
                    opp_val = getattr(item, "aml_Annotation312", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation312", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation312"):
                    opp_val = getattr(item, "aml_Annotation312", None)
                    
                    setattr(item, "aml_Annotation312", self)
                    

class aml_CollectionItem:

    def __init__(self, idRef: str, objectType: str, ordinal: str, aml_CollectionItem: "aml_Collection" = None, aml_CollectionItem104: "aml_DocumentRoot" = None):
        self.idRef = idRef
        self.objectType = objectType
        self.ordinal = ordinal
        self.aml_CollectionItem = aml_CollectionItem
        self.aml_CollectionItem104 = aml_CollectionItem104
        
    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def objectType(self) -> str:
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def aml_CollectionItem104(self):
        return self.__aml_CollectionItem104

    @aml_CollectionItem104.setter
    def aml_CollectionItem104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_CollectionItem__aml_CollectionItem104", None)
        self.__aml_CollectionItem104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot103"):
                opp_val = getattr(old_value, "aml_DocumentRoot103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot103"):
                opp_val = getattr(value, "aml_DocumentRoot103", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_CollectionItem(self):
        return self.__aml_CollectionItem

    @aml_CollectionItem.setter
    def aml_CollectionItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_CollectionItem__aml_CollectionItem", None)
        self.__aml_CollectionItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Collection61"):
                opp_val = getattr(old_value, "aml_Collection61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Collection61"):
                opp_val = getattr(value, "aml_Collection61", None)
                if opp_val is None:
                    setattr(value, "aml_Collection61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Choice:

    def __init__(self, description: str, label: str, ordinal: str, symbol: str, aml_Choice: "aml_DocumentRoot" = None, aml_Choice300: "aml_Question" = None):
        self.description = description
        self.label = label
        self.ordinal = ordinal
        self.symbol = symbol
        self.aml_Choice = aml_Choice
        self.aml_Choice300 = aml_Choice300
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def aml_Choice(self):
        return self.__aml_Choice

    @aml_Choice.setter
    def aml_Choice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Choice__aml_Choice", None)
        self.__aml_Choice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot98"):
                opp_val = getattr(old_value, "aml_DocumentRoot98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot98"):
                opp_val = getattr(value, "aml_DocumentRoot98", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Choice300(self):
        return self.__aml_Choice300

    @aml_Choice300.setter
    def aml_Choice300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Choice__aml_Choice300", None)
        self.__aml_Choice300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Question299"):
                opp_val = getattr(old_value, "aml_Question299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Question299"):
                opp_val = getattr(value, "aml_Question299", None)
                if opp_val is None:
                    setattr(value, "aml_Question299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_CreatingTool:

    def __init__(self, label: str, toolType: str, version: str, aml_CreatingTool: "aml_Argument" = None, aml_CreatingTool51: "aml_Collection" = None, aml_CreatingTool113: "aml_DocumentRoot" = None, aml_CreatingTool318: "aml_Template" = None):
        self.label = label
        self.toolType = toolType
        self.version = version
        self.aml_CreatingTool = aml_CreatingTool
        self.aml_CreatingTool51 = aml_CreatingTool51
        self.aml_CreatingTool113 = aml_CreatingTool113
        self.aml_CreatingTool318 = aml_CreatingTool318
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def toolType(self) -> str:
        return self.__toolType

    @toolType.setter
    def toolType(self, toolType: str):
        self.__toolType = toolType

    @property
    def aml_CreatingTool51(self):
        return self.__aml_CreatingTool51

    @aml_CreatingTool51.setter
    def aml_CreatingTool51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_CreatingTool__aml_CreatingTool51", None)
        self.__aml_CreatingTool51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Collection50"):
                opp_val = getattr(old_value, "aml_Collection50", None)
                if opp_val == self:
                    setattr(old_value, "aml_Collection50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Collection50"):
                opp_val = getattr(value, "aml_Collection50", None)
                setattr(value, "aml_Collection50", self)

    @property
    def aml_CreatingTool(self):
        return self.__aml_CreatingTool

    @aml_CreatingTool.setter
    def aml_CreatingTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_CreatingTool__aml_CreatingTool", None)
        self.__aml_CreatingTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Argument37"):
                opp_val = getattr(old_value, "aml_Argument37", None)
                if opp_val == self:
                    setattr(old_value, "aml_Argument37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Argument37"):
                opp_val = getattr(value, "aml_Argument37", None)
                setattr(value, "aml_Argument37", self)

    @property
    def aml_CreatingTool113(self):
        return self.__aml_CreatingTool113

    @aml_CreatingTool113.setter
    def aml_CreatingTool113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_CreatingTool__aml_CreatingTool113", None)
        self.__aml_CreatingTool113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot112"):
                opp_val = getattr(old_value, "aml_DocumentRoot112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot112"):
                opp_val = getattr(value, "aml_DocumentRoot112", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_CreatingTool318(self):
        return self.__aml_CreatingTool318

    @aml_CreatingTool318.setter
    def aml_CreatingTool318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_CreatingTool__aml_CreatingTool318", None)
        self.__aml_CreatingTool318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Template317"):
                opp_val = getattr(old_value, "aml_Template317", None)
                if opp_val == self:
                    setattr(old_value, "aml_Template317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Template317"):
                opp_val = getattr(value, "aml_Template317", None)
                setattr(value, "aml_Template317", self)

class aml_MetaData:

    def __init__(self, group: str, title: str, securityMarking: str, date: str, subject: str, description: str, aml_MetaData: "aml_Argument" = None, aml_MetaData48: "aml_Collection" = None, aml_MetaData155: "aml_DocumentRoot" = None, aml_MetaData225: "aml_Exhibit" = None, aml_MetaData251: set["aml_EObject"] = None, aml_MetaData254: set["aml_EObject"] = None, aml_MetaData257: set["aml_EObject"] = None, aml_MetaData260: set["aml_EObject"] = None, aml_MetaData263: set["aml_EObject"] = None, aml_MetaData242: set["aml_Creator"] = None, aml_MetaData245: set["aml_Reader"] = None, aml_MetaData248: set["aml_Publisher"] = None, aml_MetaData275: set["aml_EObject"] = None, aml_MetaData278: set["aml_EObject"] = None, aml_MetaData266: set["aml_EObject"] = None, aml_MetaData269: set["aml_EObject"] = None, aml_MetaData272: set["aml_Coverage"] = None, aml_MetaData315: "aml_Template" = None):
        self.group = group
        self.title = title
        self.securityMarking = securityMarking
        self.date = date
        self.subject = subject
        self.description = description
        self.aml_MetaData = aml_MetaData
        self.aml_MetaData48 = aml_MetaData48
        self.aml_MetaData155 = aml_MetaData155
        self.aml_MetaData225 = aml_MetaData225
        self.aml_MetaData251 = aml_MetaData251 if aml_MetaData251 is not None else set()
        self.aml_MetaData254 = aml_MetaData254 if aml_MetaData254 is not None else set()
        self.aml_MetaData257 = aml_MetaData257 if aml_MetaData257 is not None else set()
        self.aml_MetaData260 = aml_MetaData260 if aml_MetaData260 is not None else set()
        self.aml_MetaData263 = aml_MetaData263 if aml_MetaData263 is not None else set()
        self.aml_MetaData242 = aml_MetaData242 if aml_MetaData242 is not None else set()
        self.aml_MetaData245 = aml_MetaData245 if aml_MetaData245 is not None else set()
        self.aml_MetaData248 = aml_MetaData248 if aml_MetaData248 is not None else set()
        self.aml_MetaData275 = aml_MetaData275 if aml_MetaData275 is not None else set()
        self.aml_MetaData278 = aml_MetaData278 if aml_MetaData278 is not None else set()
        self.aml_MetaData266 = aml_MetaData266 if aml_MetaData266 is not None else set()
        self.aml_MetaData269 = aml_MetaData269 if aml_MetaData269 is not None else set()
        self.aml_MetaData272 = aml_MetaData272 if aml_MetaData272 is not None else set()
        self.aml_MetaData315 = aml_MetaData315
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def securityMarking(self) -> str:
        return self.__securityMarking

    @securityMarking.setter
    def securityMarking(self, securityMarking: str):
        self.__securityMarking = securityMarking

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def aml_MetaData260(self):
        return self.__aml_MetaData260

    @aml_MetaData260.setter
    def aml_MetaData260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData260", None)
        self.__aml_MetaData260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject261"):
                    opp_val = getattr(item, "aml_EObject261", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject261"):
                    opp_val = getattr(item, "aml_EObject261", None)
                    
                    setattr(item, "aml_EObject261", self)
                    

    @property
    def aml_MetaData225(self):
        return self.__aml_MetaData225

    @aml_MetaData225.setter
    def aml_MetaData225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData225", None)
        self.__aml_MetaData225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Exhibit224"):
                opp_val = getattr(old_value, "aml_Exhibit224", None)
                if opp_val == self:
                    setattr(old_value, "aml_Exhibit224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Exhibit224"):
                opp_val = getattr(value, "aml_Exhibit224", None)
                setattr(value, "aml_Exhibit224", self)

    @property
    def aml_MetaData257(self):
        return self.__aml_MetaData257

    @aml_MetaData257.setter
    def aml_MetaData257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData257", None)
        self.__aml_MetaData257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject258"):
                    opp_val = getattr(item, "aml_EObject258", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject258"):
                    opp_val = getattr(item, "aml_EObject258", None)
                    
                    setattr(item, "aml_EObject258", self)
                    

    @property
    def aml_MetaData272(self):
        return self.__aml_MetaData272

    @aml_MetaData272.setter
    def aml_MetaData272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData272", None)
        self.__aml_MetaData272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Coverage273"):
                    opp_val = getattr(item, "aml_Coverage273", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Coverage273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Coverage273"):
                    opp_val = getattr(item, "aml_Coverage273", None)
                    
                    setattr(item, "aml_Coverage273", self)
                    

    @property
    def aml_MetaData263(self):
        return self.__aml_MetaData263

    @aml_MetaData263.setter
    def aml_MetaData263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData263", None)
        self.__aml_MetaData263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject264"):
                    opp_val = getattr(item, "aml_EObject264", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject264"):
                    opp_val = getattr(item, "aml_EObject264", None)
                    
                    setattr(item, "aml_EObject264", self)
                    

    @property
    def aml_MetaData269(self):
        return self.__aml_MetaData269

    @aml_MetaData269.setter
    def aml_MetaData269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData269", None)
        self.__aml_MetaData269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject270"):
                    opp_val = getattr(item, "aml_EObject270", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject270"):
                    opp_val = getattr(item, "aml_EObject270", None)
                    
                    setattr(item, "aml_EObject270", self)
                    

    @property
    def aml_MetaData48(self):
        return self.__aml_MetaData48

    @aml_MetaData48.setter
    def aml_MetaData48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData48", None)
        self.__aml_MetaData48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Collection47"):
                opp_val = getattr(old_value, "aml_Collection47", None)
                if opp_val == self:
                    setattr(old_value, "aml_Collection47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Collection47"):
                opp_val = getattr(value, "aml_Collection47", None)
                setattr(value, "aml_Collection47", self)

    @property
    def aml_MetaData254(self):
        return self.__aml_MetaData254

    @aml_MetaData254.setter
    def aml_MetaData254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData254", None)
        self.__aml_MetaData254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject255"):
                    opp_val = getattr(item, "aml_EObject255", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject255"):
                    opp_val = getattr(item, "aml_EObject255", None)
                    
                    setattr(item, "aml_EObject255", self)
                    

    @property
    def aml_MetaData155(self):
        return self.__aml_MetaData155

    @aml_MetaData155.setter
    def aml_MetaData155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData155", None)
        self.__aml_MetaData155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot154"):
                opp_val = getattr(old_value, "aml_DocumentRoot154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot154"):
                opp_val = getattr(value, "aml_DocumentRoot154", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_MetaData278(self):
        return self.__aml_MetaData278

    @aml_MetaData278.setter
    def aml_MetaData278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData278", None)
        self.__aml_MetaData278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject279"):
                    opp_val = getattr(item, "aml_EObject279", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject279", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject279"):
                    opp_val = getattr(item, "aml_EObject279", None)
                    
                    setattr(item, "aml_EObject279", self)
                    

    @property
    def aml_MetaData242(self):
        return self.__aml_MetaData242

    @aml_MetaData242.setter
    def aml_MetaData242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData242", None)
        self.__aml_MetaData242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Creator243"):
                    opp_val = getattr(item, "aml_Creator243", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Creator243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Creator243"):
                    opp_val = getattr(item, "aml_Creator243", None)
                    
                    setattr(item, "aml_Creator243", self)
                    

    @property
    def aml_MetaData251(self):
        return self.__aml_MetaData251

    @aml_MetaData251.setter
    def aml_MetaData251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData251", None)
        self.__aml_MetaData251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject252"):
                    opp_val = getattr(item, "aml_EObject252", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject252"):
                    opp_val = getattr(item, "aml_EObject252", None)
                    
                    setattr(item, "aml_EObject252", self)
                    

    @property
    def aml_MetaData266(self):
        return self.__aml_MetaData266

    @aml_MetaData266.setter
    def aml_MetaData266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData266", None)
        self.__aml_MetaData266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject267"):
                    opp_val = getattr(item, "aml_EObject267", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject267"):
                    opp_val = getattr(item, "aml_EObject267", None)
                    
                    setattr(item, "aml_EObject267", self)
                    

    @property
    def aml_MetaData(self):
        return self.__aml_MetaData

    @aml_MetaData.setter
    def aml_MetaData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData", None)
        self.__aml_MetaData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Argument35"):
                opp_val = getattr(old_value, "aml_Argument35", None)
                if opp_val == self:
                    setattr(old_value, "aml_Argument35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Argument35"):
                opp_val = getattr(value, "aml_Argument35", None)
                setattr(value, "aml_Argument35", self)

    @property
    def aml_MetaData245(self):
        return self.__aml_MetaData245

    @aml_MetaData245.setter
    def aml_MetaData245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData245", None)
        self.__aml_MetaData245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Reader246"):
                    opp_val = getattr(item, "aml_Reader246", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Reader246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Reader246"):
                    opp_val = getattr(item, "aml_Reader246", None)
                    
                    setattr(item, "aml_Reader246", self)
                    

    @property
    def aml_MetaData248(self):
        return self.__aml_MetaData248

    @aml_MetaData248.setter
    def aml_MetaData248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData248", None)
        self.__aml_MetaData248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Publisher249"):
                    opp_val = getattr(item, "aml_Publisher249", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Publisher249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Publisher249"):
                    opp_val = getattr(item, "aml_Publisher249", None)
                    
                    setattr(item, "aml_Publisher249", self)
                    

    @property
    def aml_MetaData275(self):
        return self.__aml_MetaData275

    @aml_MetaData275.setter
    def aml_MetaData275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData275", None)
        self.__aml_MetaData275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_EObject276"):
                    opp_val = getattr(item, "aml_EObject276", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_EObject276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_EObject276"):
                    opp_val = getattr(item, "aml_EObject276", None)
                    
                    setattr(item, "aml_EObject276", self)
                    

    @property
    def aml_MetaData315(self):
        return self.__aml_MetaData315

    @aml_MetaData315.setter
    def aml_MetaData315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MetaData__aml_MetaData315", None)
        self.__aml_MetaData315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Template314"):
                opp_val = getattr(old_value, "aml_Template314", None)
                if opp_val == self:
                    setattr(old_value, "aml_Template314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Template314"):
                opp_val = getattr(value, "aml_Template314", None)
                setattr(value, "aml_Template314", self)

class aml_Evidence:

    def __init__(self, id: str, label: str, ordinal: str, aml_Evidence: "aml_Answer" = None, aml_Evidence125: "aml_DocumentRoot" = None, aml_Evidence206: "aml_EvidenceExhibit" = None, aml_Evidence209: "aml_Relevance" = None, aml_Evidence212: "aml_Reliability" = None, aml_Evidence215: "aml_Witness" = None, aml_Evidence218: set["aml_Annotation"] = None):
        self.id = id
        self.label = label
        self.ordinal = ordinal
        self.aml_Evidence = aml_Evidence
        self.aml_Evidence125 = aml_Evidence125
        self.aml_Evidence206 = aml_Evidence206
        self.aml_Evidence209 = aml_Evidence209
        self.aml_Evidence212 = aml_Evidence212
        self.aml_Evidence215 = aml_Evidence215
        self.aml_Evidence218 = aml_Evidence218 if aml_Evidence218 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aml_Evidence209(self):
        return self.__aml_Evidence209

    @aml_Evidence209.setter
    def aml_Evidence209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence209", None)
        self.__aml_Evidence209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Relevance210"):
                opp_val = getattr(old_value, "aml_Relevance210", None)
                if opp_val == self:
                    setattr(old_value, "aml_Relevance210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Relevance210"):
                opp_val = getattr(value, "aml_Relevance210", None)
                setattr(value, "aml_Relevance210", self)

    @property
    def aml_Evidence(self):
        return self.__aml_Evidence

    @aml_Evidence.setter
    def aml_Evidence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence", None)
        self.__aml_Evidence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Answer30"):
                opp_val = getattr(old_value, "aml_Answer30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Answer30"):
                opp_val = getattr(value, "aml_Answer30", None)
                if opp_val is None:
                    setattr(value, "aml_Answer30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Evidence125(self):
        return self.__aml_Evidence125

    @aml_Evidence125.setter
    def aml_Evidence125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence125", None)
        self.__aml_Evidence125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot124"):
                opp_val = getattr(old_value, "aml_DocumentRoot124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot124"):
                opp_val = getattr(value, "aml_DocumentRoot124", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Evidence215(self):
        return self.__aml_Evidence215

    @aml_Evidence215.setter
    def aml_Evidence215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence215", None)
        self.__aml_Evidence215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Witness216"):
                opp_val = getattr(old_value, "aml_Witness216", None)
                if opp_val == self:
                    setattr(old_value, "aml_Witness216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Witness216"):
                opp_val = getattr(value, "aml_Witness216", None)
                setattr(value, "aml_Witness216", self)

    @property
    def aml_Evidence206(self):
        return self.__aml_Evidence206

    @aml_Evidence206.setter
    def aml_Evidence206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence206", None)
        self.__aml_Evidence206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_EvidenceExhibit207"):
                opp_val = getattr(old_value, "aml_EvidenceExhibit207", None)
                if opp_val == self:
                    setattr(old_value, "aml_EvidenceExhibit207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_EvidenceExhibit207"):
                opp_val = getattr(value, "aml_EvidenceExhibit207", None)
                setattr(value, "aml_EvidenceExhibit207", self)

    @property
    def aml_Evidence212(self):
        return self.__aml_Evidence212

    @aml_Evidence212.setter
    def aml_Evidence212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence212", None)
        self.__aml_Evidence212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Reliability213"):
                opp_val = getattr(old_value, "aml_Reliability213", None)
                if opp_val == self:
                    setattr(old_value, "aml_Reliability213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Reliability213"):
                opp_val = getattr(value, "aml_Reliability213", None)
                setattr(value, "aml_Reliability213", self)

    @property
    def aml_Evidence218(self):
        return self.__aml_Evidence218

    @aml_Evidence218.setter
    def aml_Evidence218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Evidence__aml_Evidence218", None)
        self.__aml_Evidence218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation219"):
                    opp_val = getattr(item, "aml_Annotation219", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation219"):
                    opp_val = getattr(item, "aml_Annotation219", None)
                    
                    setattr(item, "aml_Annotation219", self)
                    

class aml_Witness:

    def __init__(self, description: str, idRef: str, timestamp: str, aml_Witness: "aml_Answer" = None, aml_Witness204: "aml_DocumentRoot" = None, aml_Witness216: "aml_Evidence" = None, aml_Witness231: "aml_Flag" = None):
        self.description = description
        self.idRef = idRef
        self.timestamp = timestamp
        self.aml_Witness = aml_Witness
        self.aml_Witness204 = aml_Witness204
        self.aml_Witness216 = aml_Witness216
        self.aml_Witness231 = aml_Witness231
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def aml_Witness216(self):
        return self.__aml_Witness216

    @aml_Witness216.setter
    def aml_Witness216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Witness__aml_Witness216", None)
        self.__aml_Witness216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Evidence215"):
                opp_val = getattr(old_value, "aml_Evidence215", None)
                if opp_val == self:
                    setattr(old_value, "aml_Evidence215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Evidence215"):
                opp_val = getattr(value, "aml_Evidence215", None)
                setattr(value, "aml_Evidence215", self)

    @property
    def aml_Witness(self):
        return self.__aml_Witness

    @aml_Witness.setter
    def aml_Witness(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Witness__aml_Witness", None)
        self.__aml_Witness = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Answer22"):
                opp_val = getattr(old_value, "aml_Answer22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Answer22"):
                opp_val = getattr(value, "aml_Answer22", None)
                if opp_val is None:
                    setattr(value, "aml_Answer22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Witness231(self):
        return self.__aml_Witness231

    @aml_Witness231.setter
    def aml_Witness231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Witness__aml_Witness231", None)
        self.__aml_Witness231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Flag230"):
                opp_val = getattr(old_value, "aml_Flag230", None)
                if opp_val == self:
                    setattr(old_value, "aml_Flag230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Flag230"):
                opp_val = getattr(value, "aml_Flag230", None)
                setattr(value, "aml_Flag230", self)

    @property
    def aml_Witness204(self):
        return self.__aml_Witness204

    @aml_Witness204.setter
    def aml_Witness204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Witness__aml_Witness204", None)
        self.__aml_Witness204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot203"):
                opp_val = getattr(old_value, "aml_DocumentRoot203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot203"):
                opp_val = getattr(value, "aml_DocumentRoot203", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Belief:

    def __init__(self, label: str, ordinal: str, description: str, symbol: str, aml_Belief: "aml_Answer" = None, aml_Belief96: "aml_DocumentRoot" = None):
        self.label = label
        self.ordinal = ordinal
        self.description = description
        self.symbol = symbol
        self.aml_Belief = aml_Belief
        self.aml_Belief96 = aml_Belief96
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def aml_Belief(self):
        return self.__aml_Belief

    @aml_Belief.setter
    def aml_Belief(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Belief__aml_Belief", None)
        self.__aml_Belief = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Answer"):
                opp_val = getattr(old_value, "aml_Answer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Answer"):
                opp_val = getattr(value, "aml_Answer", None)
                if opp_val is None:
                    setattr(value, "aml_Answer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Belief96(self):
        return self.__aml_Belief96

    @aml_Belief96.setter
    def aml_Belief96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Belief__aml_Belief96", None)
        self.__aml_Belief96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot95"):
                opp_val = getattr(old_value, "aml_DocumentRoot95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot95"):
                opp_val = getattr(value, "aml_DocumentRoot95", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Answer:

    def __init__(self, questionId: str, group: str, rationale: str, aml_Answer: set["aml_Belief"] = None, aml_Answer22: set["aml_Witness"] = None, aml_Answer24: set["aml_Annotation"] = None, aml_Answer27: set["aml_AggregationRule"] = None, aml_Answer30: set["aml_Evidence"] = None, aml_Answer32: set["aml_DiscoveryMethod"] = None, aml_Answer45: "aml_Argument" = None, aml_Answer84: "aml_DocumentRoot" = None):
        self.questionId = questionId
        self.group = group
        self.rationale = rationale
        self.aml_Answer = aml_Answer if aml_Answer is not None else set()
        self.aml_Answer22 = aml_Answer22 if aml_Answer22 is not None else set()
        self.aml_Answer24 = aml_Answer24 if aml_Answer24 is not None else set()
        self.aml_Answer27 = aml_Answer27 if aml_Answer27 is not None else set()
        self.aml_Answer30 = aml_Answer30 if aml_Answer30 is not None else set()
        self.aml_Answer32 = aml_Answer32 if aml_Answer32 is not None else set()
        self.aml_Answer45 = aml_Answer45
        self.aml_Answer84 = aml_Answer84
        
    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

    @property
    def questionId(self) -> str:
        return self.__questionId

    @questionId.setter
    def questionId(self, questionId: str):
        self.__questionId = questionId

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def aml_Answer32(self):
        return self.__aml_Answer32

    @aml_Answer32.setter
    def aml_Answer32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer32", None)
        self.__aml_Answer32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_DiscoveryMethod33"):
                    opp_val = getattr(item, "aml_DiscoveryMethod33", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_DiscoveryMethod33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_DiscoveryMethod33"):
                    opp_val = getattr(item, "aml_DiscoveryMethod33", None)
                    
                    setattr(item, "aml_DiscoveryMethod33", self)
                    

    @property
    def aml_Answer(self):
        return self.__aml_Answer

    @aml_Answer.setter
    def aml_Answer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer", None)
        self.__aml_Answer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Belief"):
                    opp_val = getattr(item, "aml_Belief", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Belief", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Belief"):
                    opp_val = getattr(item, "aml_Belief", None)
                    
                    setattr(item, "aml_Belief", self)
                    

    @property
    def aml_Answer27(self):
        return self.__aml_Answer27

    @aml_Answer27.setter
    def aml_Answer27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer27", None)
        self.__aml_Answer27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_AggregationRule28"):
                    opp_val = getattr(item, "aml_AggregationRule28", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_AggregationRule28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_AggregationRule28"):
                    opp_val = getattr(item, "aml_AggregationRule28", None)
                    
                    setattr(item, "aml_AggregationRule28", self)
                    

    @property
    def aml_Answer30(self):
        return self.__aml_Answer30

    @aml_Answer30.setter
    def aml_Answer30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer30", None)
        self.__aml_Answer30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Evidence"):
                    opp_val = getattr(item, "aml_Evidence", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Evidence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Evidence"):
                    opp_val = getattr(item, "aml_Evidence", None)
                    
                    setattr(item, "aml_Evidence", self)
                    

    @property
    def aml_Answer22(self):
        return self.__aml_Answer22

    @aml_Answer22.setter
    def aml_Answer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer22", None)
        self.__aml_Answer22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Witness"):
                    opp_val = getattr(item, "aml_Witness", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Witness", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Witness"):
                    opp_val = getattr(item, "aml_Witness", None)
                    
                    setattr(item, "aml_Witness", self)
                    

    @property
    def aml_Answer45(self):
        return self.__aml_Answer45

    @aml_Answer45.setter
    def aml_Answer45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer45", None)
        self.__aml_Answer45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Argument44"):
                opp_val = getattr(old_value, "aml_Argument44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Argument44"):
                opp_val = getattr(value, "aml_Argument44", None)
                if opp_val is None:
                    setattr(value, "aml_Argument44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Answer84(self):
        return self.__aml_Answer84

    @aml_Answer84.setter
    def aml_Answer84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer84", None)
        self.__aml_Answer84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot83"):
                opp_val = getattr(old_value, "aml_DocumentRoot83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot83"):
                opp_val = getattr(value, "aml_DocumentRoot83", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Answer24(self):
        return self.__aml_Answer24

    @aml_Answer24.setter
    def aml_Answer24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Answer__aml_Answer24", None)
        self.__aml_Answer24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation25"):
                    opp_val = getattr(item, "aml_Annotation25", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation25"):
                    opp_val = getattr(item, "aml_Annotation25", None)
                    
                    setattr(item, "aml_Annotation25", self)
                    

class aml_ArgumentTemplate:

    def __init__(self, value: str, idRef: str, aml_ArgumentTemplate: "aml_Argument" = None, aml_ArgumentTemplate59: "aml_Collection" = None, aml_ArgumentTemplate65: "aml_DiscoveryMethod" = None, aml_ArgumentTemplate93: "aml_DocumentRoot" = None):
        self.value = value
        self.idRef = idRef
        self.aml_ArgumentTemplate = aml_ArgumentTemplate
        self.aml_ArgumentTemplate59 = aml_ArgumentTemplate59
        self.aml_ArgumentTemplate65 = aml_ArgumentTemplate65
        self.aml_ArgumentTemplate93 = aml_ArgumentTemplate93
        
    @property
    def idRef(self) -> str:
        return self.__idRef

    @idRef.setter
    def idRef(self, idRef: str):
        self.__idRef = idRef

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def aml_ArgumentTemplate65(self):
        return self.__aml_ArgumentTemplate65

    @aml_ArgumentTemplate65.setter
    def aml_ArgumentTemplate65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_ArgumentTemplate__aml_ArgumentTemplate65", None)
        self.__aml_ArgumentTemplate65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DiscoveryMethod64"):
                opp_val = getattr(old_value, "aml_DiscoveryMethod64", None)
                if opp_val == self:
                    setattr(old_value, "aml_DiscoveryMethod64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DiscoveryMethod64"):
                opp_val = getattr(value, "aml_DiscoveryMethod64", None)
                setattr(value, "aml_DiscoveryMethod64", self)

    @property
    def aml_ArgumentTemplate93(self):
        return self.__aml_ArgumentTemplate93

    @aml_ArgumentTemplate93.setter
    def aml_ArgumentTemplate93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_ArgumentTemplate__aml_ArgumentTemplate93", None)
        self.__aml_ArgumentTemplate93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot92"):
                opp_val = getattr(old_value, "aml_DocumentRoot92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot92"):
                opp_val = getattr(value, "aml_DocumentRoot92", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_ArgumentTemplate(self):
        return self.__aml_ArgumentTemplate

    @aml_ArgumentTemplate.setter
    def aml_ArgumentTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_ArgumentTemplate__aml_ArgumentTemplate", None)
        self.__aml_ArgumentTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Argument42"):
                opp_val = getattr(old_value, "aml_Argument42", None)
                if opp_val == self:
                    setattr(old_value, "aml_Argument42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Argument42"):
                opp_val = getattr(value, "aml_Argument42", None)
                setattr(value, "aml_Argument42", self)

    @property
    def aml_ArgumentTemplate59(self):
        return self.__aml_ArgumentTemplate59

    @aml_ArgumentTemplate59.setter
    def aml_ArgumentTemplate59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_ArgumentTemplate__aml_ArgumentTemplate59", None)
        self.__aml_ArgumentTemplate59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Collection58"):
                opp_val = getattr(old_value, "aml_Collection58", None)
                if opp_val == self:
                    setattr(old_value, "aml_Collection58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Collection58"):
                opp_val = getattr(value, "aml_Collection58", None)
                setattr(value, "aml_Collection58", self)

class aml_Annotation:

    def __init__(self, mixed: str, group: str, id: str, aml_Annotation19: set["aml_Flag"] = None, aml_Annotation: set["aml_Memo"] = None, aml_Annotation25: "aml_Answer" = None, aml_Annotation40: "aml_Argument" = None, aml_Annotation54: "aml_Collection" = None, aml_Annotation68: "aml_DiscoveryMethod" = None, aml_Annotation81: "aml_DocumentRoot" = None, aml_Annotation219: "aml_Evidence" = None, aml_Annotation228: "aml_Exhibit" = None, aml_Annotation312: "aml_Question" = None, aml_Annotation321: "aml_Template" = None):
        self.mixed = mixed
        self.group = group
        self.id = id
        self.aml_Annotation19 = aml_Annotation19 if aml_Annotation19 is not None else set()
        self.aml_Annotation = aml_Annotation if aml_Annotation is not None else set()
        self.aml_Annotation25 = aml_Annotation25
        self.aml_Annotation40 = aml_Annotation40
        self.aml_Annotation54 = aml_Annotation54
        self.aml_Annotation68 = aml_Annotation68
        self.aml_Annotation81 = aml_Annotation81
        self.aml_Annotation219 = aml_Annotation219
        self.aml_Annotation228 = aml_Annotation228
        self.aml_Annotation312 = aml_Annotation312
        self.aml_Annotation321 = aml_Annotation321
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aml_Annotation19(self):
        return self.__aml_Annotation19

    @aml_Annotation19.setter
    def aml_Annotation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation19", None)
        self.__aml_Annotation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Flag"):
                    opp_val = getattr(item, "aml_Flag", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Flag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Flag"):
                    opp_val = getattr(item, "aml_Flag", None)
                    
                    setattr(item, "aml_Flag", self)
                    

    @property
    def aml_Annotation219(self):
        return self.__aml_Annotation219

    @aml_Annotation219.setter
    def aml_Annotation219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation219", None)
        self.__aml_Annotation219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Evidence218"):
                opp_val = getattr(old_value, "aml_Evidence218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Evidence218"):
                opp_val = getattr(value, "aml_Evidence218", None)
                if opp_val is None:
                    setattr(value, "aml_Evidence218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation228(self):
        return self.__aml_Annotation228

    @aml_Annotation228.setter
    def aml_Annotation228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation228", None)
        self.__aml_Annotation228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Exhibit227"):
                opp_val = getattr(old_value, "aml_Exhibit227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Exhibit227"):
                opp_val = getattr(value, "aml_Exhibit227", None)
                if opp_val is None:
                    setattr(value, "aml_Exhibit227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation81(self):
        return self.__aml_Annotation81

    @aml_Annotation81.setter
    def aml_Annotation81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation81", None)
        self.__aml_Annotation81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot80"):
                opp_val = getattr(old_value, "aml_DocumentRoot80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot80"):
                opp_val = getattr(value, "aml_DocumentRoot80", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation68(self):
        return self.__aml_Annotation68

    @aml_Annotation68.setter
    def aml_Annotation68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation68", None)
        self.__aml_Annotation68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DiscoveryMethod67"):
                opp_val = getattr(old_value, "aml_DiscoveryMethod67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DiscoveryMethod67"):
                opp_val = getattr(value, "aml_DiscoveryMethod67", None)
                if opp_val is None:
                    setattr(value, "aml_DiscoveryMethod67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation25(self):
        return self.__aml_Annotation25

    @aml_Annotation25.setter
    def aml_Annotation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation25", None)
        self.__aml_Annotation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Answer24"):
                opp_val = getattr(old_value, "aml_Answer24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Answer24"):
                opp_val = getattr(value, "aml_Answer24", None)
                if opp_val is None:
                    setattr(value, "aml_Answer24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation(self):
        return self.__aml_Annotation

    @aml_Annotation.setter
    def aml_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation", None)
        self.__aml_Annotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Memo17"):
                    opp_val = getattr(item, "aml_Memo17", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Memo17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Memo17"):
                    opp_val = getattr(item, "aml_Memo17", None)
                    
                    setattr(item, "aml_Memo17", self)
                    

    @property
    def aml_Annotation321(self):
        return self.__aml_Annotation321

    @aml_Annotation321.setter
    def aml_Annotation321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation321", None)
        self.__aml_Annotation321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Template320"):
                opp_val = getattr(old_value, "aml_Template320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Template320"):
                opp_val = getattr(value, "aml_Template320", None)
                if opp_val is None:
                    setattr(value, "aml_Template320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation312(self):
        return self.__aml_Annotation312

    @aml_Annotation312.setter
    def aml_Annotation312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation312", None)
        self.__aml_Annotation312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Question311"):
                opp_val = getattr(old_value, "aml_Question311", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Question311"):
                opp_val = getattr(value, "aml_Question311", None)
                if opp_val is None:
                    setattr(value, "aml_Question311", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation54(self):
        return self.__aml_Annotation54

    @aml_Annotation54.setter
    def aml_Annotation54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation54", None)
        self.__aml_Annotation54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Collection53"):
                opp_val = getattr(old_value, "aml_Collection53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Collection53"):
                opp_val = getattr(value, "aml_Collection53", None)
                if opp_val is None:
                    setattr(value, "aml_Collection53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Annotation40(self):
        return self.__aml_Annotation40

    @aml_Annotation40.setter
    def aml_Annotation40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Annotation__aml_Annotation40", None)
        self.__aml_Annotation40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Argument39"):
                opp_val = getattr(old_value, "aml_Argument39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Argument39"):
                opp_val = getattr(value, "aml_Argument39", None)
                if opp_val is None:
                    setattr(value, "aml_Argument39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_DiscoveryMethod:

    def __init__(self, url: str, autoTrigger: str, description: str, id: str, importType: str, label: str, type: str, aml_DiscoveryMethod: "aml_AmlDocument" = None, aml_DiscoveryMethod33: "aml_Answer" = None, aml_DiscoveryMethod64: "aml_ArgumentTemplate" = None, aml_DiscoveryMethod67: set["aml_Annotation"] = None, aml_DiscoveryMethod120: "aml_DocumentRoot" = None, aml_DiscoveryMethod309: "aml_Question" = None):
        self.url = url
        self.autoTrigger = autoTrigger
        self.description = description
        self.id = id
        self.importType = importType
        self.label = label
        self.type = type
        self.aml_DiscoveryMethod = aml_DiscoveryMethod
        self.aml_DiscoveryMethod33 = aml_DiscoveryMethod33
        self.aml_DiscoveryMethod64 = aml_DiscoveryMethod64
        self.aml_DiscoveryMethod67 = aml_DiscoveryMethod67 if aml_DiscoveryMethod67 is not None else set()
        self.aml_DiscoveryMethod120 = aml_DiscoveryMethod120
        self.aml_DiscoveryMethod309 = aml_DiscoveryMethod309
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def autoTrigger(self) -> str:
        return self.__autoTrigger

    @autoTrigger.setter
    def autoTrigger(self, autoTrigger: str):
        self.__autoTrigger = autoTrigger

    @property
    def aml_DiscoveryMethod120(self):
        return self.__aml_DiscoveryMethod120

    @aml_DiscoveryMethod120.setter
    def aml_DiscoveryMethod120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DiscoveryMethod__aml_DiscoveryMethod120", None)
        self.__aml_DiscoveryMethod120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot119"):
                opp_val = getattr(old_value, "aml_DocumentRoot119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot119"):
                opp_val = getattr(value, "aml_DocumentRoot119", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_DiscoveryMethod(self):
        return self.__aml_DiscoveryMethod

    @aml_DiscoveryMethod.setter
    def aml_DiscoveryMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DiscoveryMethod__aml_DiscoveryMethod", None)
        self.__aml_DiscoveryMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument15"):
                opp_val = getattr(old_value, "aml_AmlDocument15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument15"):
                opp_val = getattr(value, "aml_AmlDocument15", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_DiscoveryMethod64(self):
        return self.__aml_DiscoveryMethod64

    @aml_DiscoveryMethod64.setter
    def aml_DiscoveryMethod64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DiscoveryMethod__aml_DiscoveryMethod64", None)
        self.__aml_DiscoveryMethod64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_ArgumentTemplate65"):
                opp_val = getattr(old_value, "aml_ArgumentTemplate65", None)
                if opp_val == self:
                    setattr(old_value, "aml_ArgumentTemplate65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_ArgumentTemplate65"):
                opp_val = getattr(value, "aml_ArgumentTemplate65", None)
                setattr(value, "aml_ArgumentTemplate65", self)

    @property
    def aml_DiscoveryMethod67(self):
        return self.__aml_DiscoveryMethod67

    @aml_DiscoveryMethod67.setter
    def aml_DiscoveryMethod67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DiscoveryMethod__aml_DiscoveryMethod67", None)
        self.__aml_DiscoveryMethod67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation68"):
                    opp_val = getattr(item, "aml_Annotation68", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation68"):
                    opp_val = getattr(item, "aml_Annotation68", None)
                    
                    setattr(item, "aml_Annotation68", self)
                    

    @property
    def aml_DiscoveryMethod309(self):
        return self.__aml_DiscoveryMethod309

    @aml_DiscoveryMethod309.setter
    def aml_DiscoveryMethod309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DiscoveryMethod__aml_DiscoveryMethod309", None)
        self.__aml_DiscoveryMethod309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Question308"):
                opp_val = getattr(old_value, "aml_Question308", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Question308"):
                opp_val = getattr(value, "aml_Question308", None)
                if opp_val is None:
                    setattr(value, "aml_Question308", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_DiscoveryMethod33(self):
        return self.__aml_DiscoveryMethod33

    @aml_DiscoveryMethod33.setter
    def aml_DiscoveryMethod33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_DiscoveryMethod__aml_DiscoveryMethod33", None)
        self.__aml_DiscoveryMethod33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Answer32"):
                opp_val = getattr(old_value, "aml_Answer32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Answer32"):
                opp_val = getattr(value, "aml_Answer32", None)
                if opp_val is None:
                    setattr(value, "aml_Answer32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Memo:

    def __init__(self, subject: str, body: str, id: str, type: str, aml_Memo: "aml_AmlDocument" = None, aml_Memo17: "aml_Annotation" = None, aml_Memo152: "aml_DocumentRoot" = None, aml_Memo239: set["aml_Reader"] = None, aml_Memo236: set["aml_Creator"] = None):
        self.subject = subject
        self.body = body
        self.id = id
        self.type = type
        self.aml_Memo = aml_Memo
        self.aml_Memo17 = aml_Memo17
        self.aml_Memo152 = aml_Memo152
        self.aml_Memo239 = aml_Memo239 if aml_Memo239 is not None else set()
        self.aml_Memo236 = aml_Memo236 if aml_Memo236 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def aml_Memo152(self):
        return self.__aml_Memo152

    @aml_Memo152.setter
    def aml_Memo152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Memo__aml_Memo152", None)
        self.__aml_Memo152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot151"):
                opp_val = getattr(old_value, "aml_DocumentRoot151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot151"):
                opp_val = getattr(value, "aml_DocumentRoot151", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Memo239(self):
        return self.__aml_Memo239

    @aml_Memo239.setter
    def aml_Memo239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Memo__aml_Memo239", None)
        self.__aml_Memo239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Reader240"):
                    opp_val = getattr(item, "aml_Reader240", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Reader240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Reader240"):
                    opp_val = getattr(item, "aml_Reader240", None)
                    
                    setattr(item, "aml_Reader240", self)
                    

    @property
    def aml_Memo(self):
        return self.__aml_Memo

    @aml_Memo.setter
    def aml_Memo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Memo__aml_Memo", None)
        self.__aml_Memo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument13"):
                opp_val = getattr(old_value, "aml_AmlDocument13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument13"):
                opp_val = getattr(value, "aml_AmlDocument13", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Memo236(self):
        return self.__aml_Memo236

    @aml_Memo236.setter
    def aml_Memo236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Memo__aml_Memo236", None)
        self.__aml_Memo236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Creator237"):
                    opp_val = getattr(item, "aml_Creator237", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Creator237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Creator237"):
                    opp_val = getattr(item, "aml_Creator237", None)
                    
                    setattr(item, "aml_Creator237", self)
                    

    @property
    def aml_Memo17(self):
        return self.__aml_Memo17

    @aml_Memo17.setter
    def aml_Memo17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Memo__aml_Memo17", None)
        self.__aml_Memo17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Annotation"):
                opp_val = getattr(old_value, "aml_Annotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Annotation"):
                opp_val = getattr(value, "aml_Annotation", None)
                if opp_val is None:
                    setattr(value, "aml_Annotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Person:

    def __init__(self, department: str, email: str, description: str, id: str, firstName: str, middleName: str, lastName: str, nickName: str, organization: str, aml_Person: "aml_AmlDocument" = None, aml_Person169: "aml_DocumentRoot" = None):
        self.department = department
        self.email = email
        self.description = description
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.nickName = nickName
        self.organization = organization
        self.aml_Person = aml_Person
        self.aml_Person169 = aml_Person169
        
    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def department(self) -> str:
        return self.__department

    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def nickName(self) -> str:
        return self.__nickName

    @nickName.setter
    def nickName(self, nickName: str):
        self.__nickName = nickName

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def middleName(self) -> str:
        return self.__middleName

    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aml_Person(self):
        return self.__aml_Person

    @aml_Person.setter
    def aml_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Person__aml_Person", None)
        self.__aml_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument11"):
                opp_val = getattr(old_value, "aml_AmlDocument11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument11"):
                opp_val = getattr(value, "aml_AmlDocument11", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Person169(self):
        return self.__aml_Person169

    @aml_Person169.setter
    def aml_Person169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Person__aml_Person169", None)
        self.__aml_Person169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot168"):
                opp_val = getattr(old_value, "aml_DocumentRoot168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot168"):
                opp_val = getattr(value, "aml_DocumentRoot168", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Collection:

    def __init__(self, label1: str, group: str, label: str, id: str, objectType: str, aml_Collection: "aml_AmlDocument" = None, aml_Collection47: "aml_MetaData" = None, aml_Collection50: "aml_CreatingTool" = None, aml_Collection53: set["aml_Annotation"] = None, aml_Collection56: "aml_Question" = None, aml_Collection58: "aml_ArgumentTemplate" = None, aml_Collection61: set["aml_CollectionItem"] = None, aml_Collection101: "aml_DocumentRoot" = None):
        self.label1 = label1
        self.group = group
        self.label = label
        self.id = id
        self.objectType = objectType
        self.aml_Collection = aml_Collection
        self.aml_Collection47 = aml_Collection47
        self.aml_Collection50 = aml_Collection50
        self.aml_Collection53 = aml_Collection53 if aml_Collection53 is not None else set()
        self.aml_Collection56 = aml_Collection56
        self.aml_Collection58 = aml_Collection58
        self.aml_Collection61 = aml_Collection61 if aml_Collection61 is not None else set()
        self.aml_Collection101 = aml_Collection101
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def label1(self) -> str:
        return self.__label1

    @label1.setter
    def label1(self, label1: str):
        self.__label1 = label1

    @property
    def objectType(self) -> str:
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aml_Collection47(self):
        return self.__aml_Collection47

    @aml_Collection47.setter
    def aml_Collection47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection47", None)
        self.__aml_Collection47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData48"):
                opp_val = getattr(old_value, "aml_MetaData48", None)
                if opp_val == self:
                    setattr(old_value, "aml_MetaData48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData48"):
                opp_val = getattr(value, "aml_MetaData48", None)
                setattr(value, "aml_MetaData48", self)

    @property
    def aml_Collection101(self):
        return self.__aml_Collection101

    @aml_Collection101.setter
    def aml_Collection101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection101", None)
        self.__aml_Collection101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot100"):
                opp_val = getattr(old_value, "aml_DocumentRoot100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot100"):
                opp_val = getattr(value, "aml_DocumentRoot100", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Collection61(self):
        return self.__aml_Collection61

    @aml_Collection61.setter
    def aml_Collection61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection61", None)
        self.__aml_Collection61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_CollectionItem"):
                    opp_val = getattr(item, "aml_CollectionItem", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_CollectionItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_CollectionItem"):
                    opp_val = getattr(item, "aml_CollectionItem", None)
                    
                    setattr(item, "aml_CollectionItem", self)
                    

    @property
    def aml_Collection58(self):
        return self.__aml_Collection58

    @aml_Collection58.setter
    def aml_Collection58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection58", None)
        self.__aml_Collection58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_ArgumentTemplate59"):
                opp_val = getattr(old_value, "aml_ArgumentTemplate59", None)
                if opp_val == self:
                    setattr(old_value, "aml_ArgumentTemplate59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_ArgumentTemplate59"):
                opp_val = getattr(value, "aml_ArgumentTemplate59", None)
                setattr(value, "aml_ArgumentTemplate59", self)

    @property
    def aml_Collection53(self):
        return self.__aml_Collection53

    @aml_Collection53.setter
    def aml_Collection53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection53", None)
        self.__aml_Collection53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation54"):
                    opp_val = getattr(item, "aml_Annotation54", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation54"):
                    opp_val = getattr(item, "aml_Annotation54", None)
                    
                    setattr(item, "aml_Annotation54", self)
                    

    @property
    def aml_Collection56(self):
        return self.__aml_Collection56

    @aml_Collection56.setter
    def aml_Collection56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection56", None)
        self.__aml_Collection56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Question"):
                opp_val = getattr(old_value, "aml_Question", None)
                if opp_val == self:
                    setattr(old_value, "aml_Question", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Question"):
                opp_val = getattr(value, "aml_Question", None)
                setattr(value, "aml_Question", self)

    @property
    def aml_Collection50(self):
        return self.__aml_Collection50

    @aml_Collection50.setter
    def aml_Collection50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection50", None)
        self.__aml_Collection50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_CreatingTool51"):
                opp_val = getattr(old_value, "aml_CreatingTool51", None)
                if opp_val == self:
                    setattr(old_value, "aml_CreatingTool51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_CreatingTool51"):
                opp_val = getattr(value, "aml_CreatingTool51", None)
                setattr(value, "aml_CreatingTool51", self)

    @property
    def aml_Collection(self):
        return self.__aml_Collection

    @aml_Collection.setter
    def aml_Collection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Collection__aml_Collection", None)
        self.__aml_Collection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument9"):
                opp_val = getattr(old_value, "aml_AmlDocument9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument9"):
                opp_val = getattr(value, "aml_AmlDocument9", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Exhibit:

    def __init__(self, id: str, aml_Exhibit: "aml_AmlDocument" = None, aml_Exhibit130: "aml_DocumentRoot" = None, aml_Exhibit227: set["aml_Annotation"] = None, aml_Exhibit221: "aml_EObject" = None, aml_Exhibit224: "aml_MetaData" = None):
        self.id = id
        self.aml_Exhibit = aml_Exhibit
        self.aml_Exhibit130 = aml_Exhibit130
        self.aml_Exhibit227 = aml_Exhibit227 if aml_Exhibit227 is not None else set()
        self.aml_Exhibit221 = aml_Exhibit221
        self.aml_Exhibit224 = aml_Exhibit224
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aml_Exhibit221(self):
        return self.__aml_Exhibit221

    @aml_Exhibit221.setter
    def aml_Exhibit221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Exhibit__aml_Exhibit221", None)
        self.__aml_Exhibit221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_EObject222"):
                opp_val = getattr(old_value, "aml_EObject222", None)
                if opp_val == self:
                    setattr(old_value, "aml_EObject222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_EObject222"):
                opp_val = getattr(value, "aml_EObject222", None)
                setattr(value, "aml_EObject222", self)

    @property
    def aml_Exhibit224(self):
        return self.__aml_Exhibit224

    @aml_Exhibit224.setter
    def aml_Exhibit224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Exhibit__aml_Exhibit224", None)
        self.__aml_Exhibit224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData225"):
                opp_val = getattr(old_value, "aml_MetaData225", None)
                if opp_val == self:
                    setattr(old_value, "aml_MetaData225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData225"):
                opp_val = getattr(value, "aml_MetaData225", None)
                setattr(value, "aml_MetaData225", self)

    @property
    def aml_Exhibit130(self):
        return self.__aml_Exhibit130

    @aml_Exhibit130.setter
    def aml_Exhibit130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Exhibit__aml_Exhibit130", None)
        self.__aml_Exhibit130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot129"):
                opp_val = getattr(old_value, "aml_DocumentRoot129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot129"):
                opp_val = getattr(value, "aml_DocumentRoot129", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Exhibit(self):
        return self.__aml_Exhibit

    @aml_Exhibit.setter
    def aml_Exhibit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Exhibit__aml_Exhibit", None)
        self.__aml_Exhibit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument7"):
                opp_val = getattr(old_value, "aml_AmlDocument7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument7"):
                opp_val = getattr(value, "aml_AmlDocument7", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Exhibit227(self):
        return self.__aml_Exhibit227

    @aml_Exhibit227.setter
    def aml_Exhibit227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Exhibit__aml_Exhibit227", None)
        self.__aml_Exhibit227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation228"):
                    opp_val = getattr(item, "aml_Annotation228", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation228"):
                    opp_val = getattr(item, "aml_Annotation228", None)
                    
                    setattr(item, "aml_Annotation228", self)
                    

class aml_Flag:

    def __init__(self, description: str, flagType: str, label: str, aml_Flag: "aml_Annotation" = None, aml_Flag133: "aml_DocumentRoot" = None, aml_Flag230: "aml_Witness" = None):
        self.description = description
        self.flagType = flagType
        self.label = label
        self.aml_Flag = aml_Flag
        self.aml_Flag133 = aml_Flag133
        self.aml_Flag230 = aml_Flag230
        
    @property
    def flagType(self) -> str:
        return self.__flagType

    @flagType.setter
    def flagType(self, flagType: str):
        self.__flagType = flagType

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aml_Flag230(self):
        return self.__aml_Flag230

    @aml_Flag230.setter
    def aml_Flag230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Flag__aml_Flag230", None)
        self.__aml_Flag230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Witness231"):
                opp_val = getattr(old_value, "aml_Witness231", None)
                if opp_val == self:
                    setattr(old_value, "aml_Witness231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Witness231"):
                opp_val = getattr(value, "aml_Witness231", None)
                setattr(value, "aml_Witness231", self)

    @property
    def aml_Flag133(self):
        return self.__aml_Flag133

    @aml_Flag133.setter
    def aml_Flag133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Flag__aml_Flag133", None)
        self.__aml_Flag133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot132"):
                opp_val = getattr(old_value, "aml_DocumentRoot132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot132"):
                opp_val = getattr(value, "aml_DocumentRoot132", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Flag(self):
        return self.__aml_Flag

    @aml_Flag.setter
    def aml_Flag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Flag__aml_Flag", None)
        self.__aml_Flag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Annotation19"):
                opp_val = getattr(old_value, "aml_Annotation19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Annotation19"):
                opp_val = getattr(value, "aml_Annotation19", None)
                if opp_val is None:
                    setattr(value, "aml_Annotation19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Argument:

    def __init__(self, id: str, aml_Argument: "aml_AmlDocument" = None, aml_Argument35: "aml_MetaData" = None, aml_Argument37: "aml_CreatingTool" = None, aml_Argument39: set["aml_Annotation"] = None, aml_Argument42: "aml_ArgumentTemplate" = None, aml_Argument44: set["aml_Answer"] = None, aml_Argument90: "aml_DocumentRoot" = None):
        self.id = id
        self.aml_Argument = aml_Argument
        self.aml_Argument35 = aml_Argument35
        self.aml_Argument37 = aml_Argument37
        self.aml_Argument39 = aml_Argument39 if aml_Argument39 is not None else set()
        self.aml_Argument42 = aml_Argument42
        self.aml_Argument44 = aml_Argument44 if aml_Argument44 is not None else set()
        self.aml_Argument90 = aml_Argument90
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aml_Argument(self):
        return self.__aml_Argument

    @aml_Argument.setter
    def aml_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument", None)
        self.__aml_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument5"):
                opp_val = getattr(old_value, "aml_AmlDocument5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument5"):
                opp_val = getattr(value, "aml_AmlDocument5", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Argument90(self):
        return self.__aml_Argument90

    @aml_Argument90.setter
    def aml_Argument90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument90", None)
        self.__aml_Argument90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot89"):
                opp_val = getattr(old_value, "aml_DocumentRoot89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot89"):
                opp_val = getattr(value, "aml_DocumentRoot89", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Argument35(self):
        return self.__aml_Argument35

    @aml_Argument35.setter
    def aml_Argument35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument35", None)
        self.__aml_Argument35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData"):
                opp_val = getattr(old_value, "aml_MetaData", None)
                if opp_val == self:
                    setattr(old_value, "aml_MetaData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData"):
                opp_val = getattr(value, "aml_MetaData", None)
                setattr(value, "aml_MetaData", self)

    @property
    def aml_Argument39(self):
        return self.__aml_Argument39

    @aml_Argument39.setter
    def aml_Argument39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument39", None)
        self.__aml_Argument39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation40"):
                    opp_val = getattr(item, "aml_Annotation40", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation40"):
                    opp_val = getattr(item, "aml_Annotation40", None)
                    
                    setattr(item, "aml_Annotation40", self)
                    

    @property
    def aml_Argument42(self):
        return self.__aml_Argument42

    @aml_Argument42.setter
    def aml_Argument42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument42", None)
        self.__aml_Argument42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_ArgumentTemplate"):
                opp_val = getattr(old_value, "aml_ArgumentTemplate", None)
                if opp_val == self:
                    setattr(old_value, "aml_ArgumentTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_ArgumentTemplate"):
                opp_val = getattr(value, "aml_ArgumentTemplate", None)
                setattr(value, "aml_ArgumentTemplate", self)

    @property
    def aml_Argument44(self):
        return self.__aml_Argument44

    @aml_Argument44.setter
    def aml_Argument44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument44", None)
        self.__aml_Argument44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Answer45"):
                    opp_val = getattr(item, "aml_Answer45", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Answer45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Answer45"):
                    opp_val = getattr(item, "aml_Answer45", None)
                    
                    setattr(item, "aml_Answer45", self)
                    

    @property
    def aml_Argument37(self):
        return self.__aml_Argument37

    @aml_Argument37.setter
    def aml_Argument37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Argument__aml_Argument37", None)
        self.__aml_Argument37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_CreatingTool"):
                opp_val = getattr(old_value, "aml_CreatingTool", None)
                if opp_val == self:
                    setattr(old_value, "aml_CreatingTool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_CreatingTool"):
                opp_val = getattr(value, "aml_CreatingTool", None)
                setattr(value, "aml_CreatingTool", self)

class aml_Template:

    def __init__(self, id: str, aml_Template: "aml_AmlDocument" = None, aml_Template196: "aml_DocumentRoot" = None, aml_Template320: set["aml_Annotation"] = None, aml_Template323: set["aml_Question"] = None, aml_Template314: "aml_MetaData" = None, aml_Template317: "aml_CreatingTool" = None):
        self.id = id
        self.aml_Template = aml_Template
        self.aml_Template196 = aml_Template196
        self.aml_Template320 = aml_Template320 if aml_Template320 is not None else set()
        self.aml_Template323 = aml_Template323 if aml_Template323 is not None else set()
        self.aml_Template314 = aml_Template314
        self.aml_Template317 = aml_Template317
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aml_Template320(self):
        return self.__aml_Template320

    @aml_Template320.setter
    def aml_Template320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Template__aml_Template320", None)
        self.__aml_Template320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Annotation321"):
                    opp_val = getattr(item, "aml_Annotation321", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Annotation321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Annotation321"):
                    opp_val = getattr(item, "aml_Annotation321", None)
                    
                    setattr(item, "aml_Annotation321", self)
                    

    @property
    def aml_Template317(self):
        return self.__aml_Template317

    @aml_Template317.setter
    def aml_Template317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Template__aml_Template317", None)
        self.__aml_Template317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_CreatingTool318"):
                opp_val = getattr(old_value, "aml_CreatingTool318", None)
                if opp_val == self:
                    setattr(old_value, "aml_CreatingTool318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_CreatingTool318"):
                opp_val = getattr(value, "aml_CreatingTool318", None)
                setattr(value, "aml_CreatingTool318", self)

    @property
    def aml_Template196(self):
        return self.__aml_Template196

    @aml_Template196.setter
    def aml_Template196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Template__aml_Template196", None)
        self.__aml_Template196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot195"):
                opp_val = getattr(old_value, "aml_DocumentRoot195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot195"):
                opp_val = getattr(value, "aml_DocumentRoot195", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Template314(self):
        return self.__aml_Template314

    @aml_Template314.setter
    def aml_Template314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Template__aml_Template314", None)
        self.__aml_Template314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MetaData315"):
                opp_val = getattr(old_value, "aml_MetaData315", None)
                if opp_val == self:
                    setattr(old_value, "aml_MetaData315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MetaData315"):
                opp_val = getattr(value, "aml_MetaData315", None)
                setattr(value, "aml_MetaData315", self)

    @property
    def aml_Template323(self):
        return self.__aml_Template323

    @aml_Template323.setter
    def aml_Template323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Template__aml_Template323", None)
        self.__aml_Template323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Question324"):
                    opp_val = getattr(item, "aml_Question324", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Question324", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Question324"):
                    opp_val = getattr(item, "aml_Question324", None)
                    
                    setattr(item, "aml_Question324", self)
                    

    @property
    def aml_Template(self):
        return self.__aml_Template

    @aml_Template.setter
    def aml_Template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Template__aml_Template", None)
        self.__aml_Template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AmlDocument"):
                opp_val = getattr(old_value, "aml_AmlDocument", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AmlDocument"):
                opp_val = getattr(value, "aml_AmlDocument", None)
                if opp_val is None:
                    setattr(value, "aml_AmlDocument", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_AmlDocument:

    def __init__(self, group: str, version: str, aml_AmlDocument5: set["aml_Argument"] = None, aml_AmlDocument: set["aml_Template"] = None, aml_AmlDocument7: set["aml_Exhibit"] = None, aml_AmlDocument9: set["aml_Collection"] = None, aml_AmlDocument11: set["aml_Person"] = None, aml_AmlDocument13: set["aml_Memo"] = None, aml_AmlDocument15: set["aml_DiscoveryMethod"] = None, aml_AmlDocument78: "aml_DocumentRoot" = None):
        self.group = group
        self.version = version
        self.aml_AmlDocument5 = aml_AmlDocument5 if aml_AmlDocument5 is not None else set()
        self.aml_AmlDocument = aml_AmlDocument if aml_AmlDocument is not None else set()
        self.aml_AmlDocument7 = aml_AmlDocument7 if aml_AmlDocument7 is not None else set()
        self.aml_AmlDocument9 = aml_AmlDocument9 if aml_AmlDocument9 is not None else set()
        self.aml_AmlDocument11 = aml_AmlDocument11 if aml_AmlDocument11 is not None else set()
        self.aml_AmlDocument13 = aml_AmlDocument13 if aml_AmlDocument13 is not None else set()
        self.aml_AmlDocument15 = aml_AmlDocument15 if aml_AmlDocument15 is not None else set()
        self.aml_AmlDocument78 = aml_AmlDocument78
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def aml_AmlDocument9(self):
        return self.__aml_AmlDocument9

    @aml_AmlDocument9.setter
    def aml_AmlDocument9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument9", None)
        self.__aml_AmlDocument9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Collection"):
                    opp_val = getattr(item, "aml_Collection", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Collection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Collection"):
                    opp_val = getattr(item, "aml_Collection", None)
                    
                    setattr(item, "aml_Collection", self)
                    

    @property
    def aml_AmlDocument78(self):
        return self.__aml_AmlDocument78

    @aml_AmlDocument78.setter
    def aml_AmlDocument78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument78", None)
        self.__aml_AmlDocument78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot77"):
                opp_val = getattr(old_value, "aml_DocumentRoot77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot77"):
                opp_val = getattr(value, "aml_DocumentRoot77", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_AmlDocument7(self):
        return self.__aml_AmlDocument7

    @aml_AmlDocument7.setter
    def aml_AmlDocument7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument7", None)
        self.__aml_AmlDocument7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Exhibit"):
                    opp_val = getattr(item, "aml_Exhibit", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Exhibit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Exhibit"):
                    opp_val = getattr(item, "aml_Exhibit", None)
                    
                    setattr(item, "aml_Exhibit", self)
                    

    @property
    def aml_AmlDocument13(self):
        return self.__aml_AmlDocument13

    @aml_AmlDocument13.setter
    def aml_AmlDocument13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument13", None)
        self.__aml_AmlDocument13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Memo"):
                    opp_val = getattr(item, "aml_Memo", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Memo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Memo"):
                    opp_val = getattr(item, "aml_Memo", None)
                    
                    setattr(item, "aml_Memo", self)
                    

    @property
    def aml_AmlDocument11(self):
        return self.__aml_AmlDocument11

    @aml_AmlDocument11.setter
    def aml_AmlDocument11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument11", None)
        self.__aml_AmlDocument11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Person"):
                    opp_val = getattr(item, "aml_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Person"):
                    opp_val = getattr(item, "aml_Person", None)
                    
                    setattr(item, "aml_Person", self)
                    

    @property
    def aml_AmlDocument5(self):
        return self.__aml_AmlDocument5

    @aml_AmlDocument5.setter
    def aml_AmlDocument5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument5", None)
        self.__aml_AmlDocument5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Argument"):
                    opp_val = getattr(item, "aml_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Argument"):
                    opp_val = getattr(item, "aml_Argument", None)
                    
                    setattr(item, "aml_Argument", self)
                    

    @property
    def aml_AmlDocument15(self):
        return self.__aml_AmlDocument15

    @aml_AmlDocument15.setter
    def aml_AmlDocument15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument15", None)
        self.__aml_AmlDocument15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_DiscoveryMethod"):
                    opp_val = getattr(item, "aml_DiscoveryMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_DiscoveryMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_DiscoveryMethod"):
                    opp_val = getattr(item, "aml_DiscoveryMethod", None)
                    
                    setattr(item, "aml_DiscoveryMethod", self)
                    

    @property
    def aml_AmlDocument(self):
        return self.__aml_AmlDocument

    @aml_AmlDocument.setter
    def aml_AmlDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AmlDocument__aml_AmlDocument", None)
        self.__aml_AmlDocument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aml_Template"):
                    opp_val = getattr(item, "aml_Template", None)
                    
                    if opp_val == self:
                        setattr(item, "aml_Template", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aml_Template"):
                    opp_val = getattr(item, "aml_Template", None)
                    
                    setattr(item, "aml_Template", self)
                    

class aml_Parameter:

    def __init__(self, symbol: str, aml_Parameter: "aml_AggregationRule" = None, aml_Parameter164: "aml_DocumentRoot" = None, aml_Parameter284: "aml_Value" = None):
        self.symbol = symbol
        self.aml_Parameter = aml_Parameter
        self.aml_Parameter164 = aml_Parameter164
        self.aml_Parameter284 = aml_Parameter284
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def aml_Parameter164(self):
        return self.__aml_Parameter164

    @aml_Parameter164.setter
    def aml_Parameter164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Parameter__aml_Parameter164", None)
        self.__aml_Parameter164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_DocumentRoot163"):
                opp_val = getattr(old_value, "aml_DocumentRoot163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_DocumentRoot163"):
                opp_val = getattr(value, "aml_DocumentRoot163", None)
                if opp_val is None:
                    setattr(value, "aml_DocumentRoot163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Parameter(self):
        return self.__aml_Parameter

    @aml_Parameter.setter
    def aml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Parameter__aml_Parameter", None)
        self.__aml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_AggregationRule2"):
                opp_val = getattr(old_value, "aml_AggregationRule2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_AggregationRule2"):
                opp_val = getattr(value, "aml_AggregationRule2", None)
                if opp_val is None:
                    setattr(value, "aml_AggregationRule2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Parameter284(self):
        return self.__aml_Parameter284

    @aml_Parameter284.setter
    def aml_Parameter284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Parameter__aml_Parameter284", None)
        self.__aml_Parameter284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Value285"):
                opp_val = getattr(old_value, "aml_Value285", None)
                if opp_val == self:
                    setattr(old_value, "aml_Value285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Value285"):
                opp_val = getattr(value, "aml_Value285", None)
                setattr(value, "aml_Value285", self)

class aml_EObject:

    pass
class aml_AggregationRule:

    pass