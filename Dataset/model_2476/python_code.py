from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traceability_Category:

    def __init__(self, name: str, traceability_Category: set["traceability_EObject"] = None):
        self.name = name
        self.traceability_Category = traceability_Category if traceability_Category is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traceability_Category(self):
        return self.__traceability_Category

    @traceability_Category.setter
    def traceability_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Category__traceability_Category", None)
        self.__traceability_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject34"):
                    opp_val = getattr(item, "traceability_EObject34", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject34"):
                    opp_val = getattr(item, "traceability_EObject34", None)
                    
                    setattr(item, "traceability_EObject34", self)
                    

class traceability_TraceDiffs:

    pass
class traceability_DiffCategory:

    def __init__(self, name: str, modelIndex: int, unequal: bool, traceability_DiffCategory: set["traceability_TraceDiff"] = None):
        self.name = name
        self.modelIndex = modelIndex
        self.unequal = unequal
        self.traceability_DiffCategory = traceability_DiffCategory if traceability_DiffCategory is not None else set()
        
    @property
    def unequal(self) -> bool:
        return self.__unequal

    @unequal.setter
    def unequal(self, unequal: bool):
        self.__unequal = unequal

    @property
    def modelIndex(self) -> int:
        return self.__modelIndex

    @modelIndex.setter
    def modelIndex(self, modelIndex: int):
        self.__modelIndex = modelIndex

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traceability_DiffCategory(self):
        return self.__traceability_DiffCategory

    @traceability_DiffCategory.setter
    def traceability_DiffCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_DiffCategory__traceability_DiffCategory", None)
        self.__traceability_DiffCategory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_TraceDiff30"):
                    opp_val = getattr(item, "traceability_TraceDiff30", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_TraceDiff30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_TraceDiff30"):
                    opp_val = getattr(item, "traceability_TraceDiff30", None)
                    
                    setattr(item, "traceability_TraceDiff30", self)
                    

class traceability_TraceDiff:

    def __init__(self, comment: str, traceability_TraceDiff: set["traceability_EObject"] = None, traceability_TraceDiff27: set["traceability_TraceComment"] = None, traceability_TraceDiff30: "traceability_DiffCategory" = None):
        self.comment = comment
        self.traceability_TraceDiff = traceability_TraceDiff if traceability_TraceDiff is not None else set()
        self.traceability_TraceDiff27 = traceability_TraceDiff27 if traceability_TraceDiff27 is not None else set()
        self.traceability_TraceDiff30 = traceability_TraceDiff30
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def traceability_TraceDiff(self):
        return self.__traceability_TraceDiff

    @traceability_TraceDiff.setter
    def traceability_TraceDiff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceDiff__traceability_TraceDiff", None)
        self.__traceability_TraceDiff = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject25"):
                    opp_val = getattr(item, "traceability_EObject25", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject25"):
                    opp_val = getattr(item, "traceability_EObject25", None)
                    
                    setattr(item, "traceability_EObject25", self)
                    

    @property
    def traceability_TraceDiff27(self):
        return self.__traceability_TraceDiff27

    @traceability_TraceDiff27.setter
    def traceability_TraceDiff27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceDiff__traceability_TraceDiff27", None)
        self.__traceability_TraceDiff27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_TraceComment28"):
                    opp_val = getattr(item, "traceability_TraceComment28", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_TraceComment28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_TraceComment28"):
                    opp_val = getattr(item, "traceability_TraceComment28", None)
                    
                    setattr(item, "traceability_TraceComment28", self)
                    

    @property
    def traceability_TraceDiff30(self):
        return self.__traceability_TraceDiff30

    @traceability_TraceDiff30.setter
    def traceability_TraceDiff30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceDiff__traceability_TraceDiff30", None)
        self.__traceability_TraceDiff30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_DiffCategory"):
                opp_val = getattr(old_value, "traceability_DiffCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_DiffCategory"):
                opp_val = getattr(value, "traceability_DiffCategory", None)
                if opp_val is None:
                    setattr(value, "traceability_DiffCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traceability_Traces:

    def __init__(self, uriMap: str, originalSourceURL: str, username: str, fullName: str, date: date, location: str, comments: str, traceability_Traces: "traceability_EObject" = None, traceability_Traces19: "traceability_EObject" = None, traceability_Traces22: set["traceability_EObject"] = None, traceability_Traces32: "traceability_TraceDiffs" = None):
        self.uriMap = uriMap
        self.originalSourceURL = originalSourceURL
        self.username = username
        self.fullName = fullName
        self.date = date
        self.location = location
        self.comments = comments
        self.traceability_Traces = traceability_Traces
        self.traceability_Traces19 = traceability_Traces19
        self.traceability_Traces22 = traceability_Traces22 if traceability_Traces22 is not None else set()
        self.traceability_Traces32 = traceability_Traces32
        
    @property
    def uriMap(self) -> str:
        return self.__uriMap

    @uriMap.setter
    def uriMap(self, uriMap: str):
        self.__uriMap = uriMap

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def originalSourceURL(self) -> str:
        return self.__originalSourceURL

    @originalSourceURL.setter
    def originalSourceURL(self, originalSourceURL: str):
        self.__originalSourceURL = originalSourceURL

    @property
    def traceability_Traces19(self):
        return self.__traceability_Traces19

    @traceability_Traces19.setter
    def traceability_Traces19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Traces__traceability_Traces19", None)
        self.__traceability_Traces19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_EObject20"):
                opp_val = getattr(old_value, "traceability_EObject20", None)
                if opp_val == self:
                    setattr(old_value, "traceability_EObject20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_EObject20"):
                opp_val = getattr(value, "traceability_EObject20", None)
                setattr(value, "traceability_EObject20", self)

    @property
    def traceability_Traces(self):
        return self.__traceability_Traces

    @traceability_Traces.setter
    def traceability_Traces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Traces__traceability_Traces", None)
        self.__traceability_Traces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_EObject17"):
                opp_val = getattr(old_value, "traceability_EObject17", None)
                if opp_val == self:
                    setattr(old_value, "traceability_EObject17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_EObject17"):
                opp_val = getattr(value, "traceability_EObject17", None)
                setattr(value, "traceability_EObject17", self)

    @property
    def traceability_Traces32(self):
        return self.__traceability_Traces32

    @traceability_Traces32.setter
    def traceability_Traces32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Traces__traceability_Traces32", None)
        self.__traceability_Traces32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_TraceDiffs"):
                opp_val = getattr(old_value, "traceability_TraceDiffs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_TraceDiffs"):
                opp_val = getattr(value, "traceability_TraceDiffs", None)
                if opp_val is None:
                    setattr(value, "traceability_TraceDiffs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceability_Traces22(self):
        return self.__traceability_Traces22

    @traceability_Traces22.setter
    def traceability_Traces22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Traces__traceability_Traces22", None)
        self.__traceability_Traces22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject23"):
                    opp_val = getattr(item, "traceability_EObject23", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject23"):
                    opp_val = getattr(item, "traceability_EObject23", None)
                    
                    setattr(item, "traceability_EObject23", self)
                    

class traceability_LogEntry:

    def __init__(self, message: str, severity: int, messageType: int, comment: str, traceability_LogEntry: set["traceability_EObject"] = None, traceability_LogEntry14: set["traceability_TraceComment"] = None):
        self.message = message
        self.severity = severity
        self.messageType = messageType
        self.comment = comment
        self.traceability_LogEntry = traceability_LogEntry if traceability_LogEntry is not None else set()
        self.traceability_LogEntry14 = traceability_LogEntry14 if traceability_LogEntry14 is not None else set()
        
    @property
    def severity(self) -> int:
        return self.__severity

    @severity.setter
    def severity(self, severity: int):
        self.__severity = severity

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def messageType(self) -> int:
        return self.__messageType

    @messageType.setter
    def messageType(self, messageType: int):
        self.__messageType = messageType

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def traceability_LogEntry14(self):
        return self.__traceability_LogEntry14

    @traceability_LogEntry14.setter
    def traceability_LogEntry14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_LogEntry__traceability_LogEntry14", None)
        self.__traceability_LogEntry14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_TraceComment15"):
                    opp_val = getattr(item, "traceability_TraceComment15", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_TraceComment15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_TraceComment15"):
                    opp_val = getattr(item, "traceability_TraceComment15", None)
                    
                    setattr(item, "traceability_TraceComment15", self)
                    

    @property
    def traceability_LogEntry(self):
        return self.__traceability_LogEntry

    @traceability_LogEntry.setter
    def traceability_LogEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_LogEntry__traceability_LogEntry", None)
        self.__traceability_LogEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject12"):
                    opp_val = getattr(item, "traceability_EObject12", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject12"):
                    opp_val = getattr(item, "traceability_EObject12", None)
                    
                    setattr(item, "traceability_EObject12", self)
                    

class traceability_TraceComment:

    def __init__(self, comment: str, username: str, date: date, column: str, traceability_TraceComment: "traceability_Trace" = None, traceability_TraceComment15: "traceability_LogEntry" = None, traceability_TraceComment28: "traceability_TraceDiff" = None, traceability_TraceComment36: "traceability_EObject" = None):
        self.comment = comment
        self.username = username
        self.date = date
        self.column = column
        self.traceability_TraceComment = traceability_TraceComment
        self.traceability_TraceComment15 = traceability_TraceComment15
        self.traceability_TraceComment28 = traceability_TraceComment28
        self.traceability_TraceComment36 = traceability_TraceComment36
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def traceability_TraceComment28(self):
        return self.__traceability_TraceComment28

    @traceability_TraceComment28.setter
    def traceability_TraceComment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceComment__traceability_TraceComment28", None)
        self.__traceability_TraceComment28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_TraceDiff27"):
                opp_val = getattr(old_value, "traceability_TraceDiff27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_TraceDiff27"):
                opp_val = getattr(value, "traceability_TraceDiff27", None)
                if opp_val is None:
                    setattr(value, "traceability_TraceDiff27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceability_TraceComment36(self):
        return self.__traceability_TraceComment36

    @traceability_TraceComment36.setter
    def traceability_TraceComment36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceComment__traceability_TraceComment36", None)
        self.__traceability_TraceComment36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_EObject37"):
                opp_val = getattr(old_value, "traceability_EObject37", None)
                if opp_val == self:
                    setattr(old_value, "traceability_EObject37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_EObject37"):
                opp_val = getattr(value, "traceability_EObject37", None)
                setattr(value, "traceability_EObject37", self)

    @property
    def traceability_TraceComment(self):
        return self.__traceability_TraceComment

    @traceability_TraceComment.setter
    def traceability_TraceComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceComment__traceability_TraceComment", None)
        self.__traceability_TraceComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_Trace10"):
                opp_val = getattr(old_value, "traceability_Trace10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_Trace10"):
                opp_val = getattr(value, "traceability_Trace10", None)
                if opp_val is None:
                    setattr(value, "traceability_Trace10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceability_TraceComment15(self):
        return self.__traceability_TraceComment15

    @traceability_TraceComment15.setter
    def traceability_TraceComment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_TraceComment__traceability_TraceComment15", None)
        self.__traceability_TraceComment15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_LogEntry14"):
                opp_val = getattr(old_value, "traceability_LogEntry14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_LogEntry14"):
                opp_val = getattr(value, "traceability_LogEntry14", None)
                if opp_val is None:
                    setattr(value, "traceability_LogEntry14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traceability_EObject:

    pass
class traceability_Trace:

    def __init__(self, description: str, value: str, comment: str, traceability_Trace: set["traceability_EObject"] = None, traceability_Trace2: set["traceability_EObject"] = None, Trace: "traceability_Trace" = None, parent: set["traceability_Trace"] = None, Trace8: "traceability_Trace" = None, children: "traceability_Trace" = None, traceability_Trace10: set["traceability_TraceComment"] = None):
        self.description = description
        self.value = value
        self.comment = comment
        self.traceability_Trace = traceability_Trace if traceability_Trace is not None else set()
        self.traceability_Trace2 = traceability_Trace2 if traceability_Trace2 is not None else set()
        self.Trace = Trace
        self.parent = parent if parent is not None else set()
        self.Trace8 = Trace8
        self.children = children
        self.traceability_Trace10 = traceability_Trace10 if traceability_Trace10 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def traceability_Trace(self):
        return self.__traceability_Trace

    @traceability_Trace.setter
    def traceability_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__traceability_Trace", None)
        self.__traceability_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject"):
                    opp_val = getattr(item, "traceability_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject"):
                    opp_val = getattr(item, "traceability_EObject", None)
                    
                    setattr(item, "traceability_EObject", self)
                    

    @property
    def traceability_Trace2(self):
        return self.__traceability_Trace2

    @traceability_Trace2.setter
    def traceability_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__traceability_Trace2", None)
        self.__traceability_Trace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject3"):
                    opp_val = getattr(item, "traceability_EObject3", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject3"):
                    opp_val = getattr(item, "traceability_EObject3", None)
                    
                    setattr(item, "traceability_EObject3", self)
                    

    @property
    def Trace8(self):
        return self.__Trace8

    @Trace8.setter
    def Trace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__Trace8", None)
        self.__Trace8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def traceability_Trace10(self):
        return self.__traceability_Trace10

    @traceability_Trace10.setter
    def traceability_Trace10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__traceability_Trace10", None)
        self.__traceability_Trace10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_TraceComment"):
                    opp_val = getattr(item, "traceability_TraceComment", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_TraceComment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_TraceComment"):
                    opp_val = getattr(item, "traceability_TraceComment", None)
                    
                    setattr(item, "traceability_TraceComment", self)
                    

    @property
    def Trace(self):
        return self.__Trace

    @Trace.setter
    def Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__Trace", None)
        self.__Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trace"):
                    opp_val = getattr(item, "Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trace"):
                    opp_val = getattr(item, "Trace", None)
                    
                    setattr(item, "Trace", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trace8"):
                opp_val = getattr(old_value, "Trace8", None)
                if opp_val == self:
                    setattr(old_value, "Trace8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trace8"):
                opp_val = getattr(value, "Trace8", None)
                setattr(value, "Trace8", self)
