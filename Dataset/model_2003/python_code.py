from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_Step:

    def __init__(self, number: str, thread: str, hidden: str, trace_Step9: "trace_Trace" = None, trace_Step: "trace_Location" = None):
        self.number = number
        self.thread = thread
        self.hidden = hidden
        self.trace_Step9 = trace_Step9
        self.trace_Step = trace_Step
        
        pass
    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def thread(self):
        return self.__thread

    @thread.setter
    def thread(self, thread: str):
        self.__thread = thread


    @property
    def trace_Step9(self):
        return self.__trace_Step9

    @trace_Step9.setter
    def trace_Step9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Step__trace_Step9", None)
        self.__trace_Step9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace"):
                opp_val = getattr(old_value, "trace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace"):
                opp_val = getattr(value, "trace_Trace", None)
                if opp_val is None:
                    setattr(value, "trace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_Step(self):
        return self.__trace_Step

    @trace_Step.setter
    def trace_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Step__trace_Step", None)
        self.__trace_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Location"):
                opp_val = getattr(old_value, "trace_Location", None)
                if opp_val == self:
                    setattr(old_value, "trace_Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Location"):
                opp_val = getattr(value, "trace_Location", None)
                setattr(value, "trace_Location", self)

    def interpret(self, trace_context) :
        # TODO: Implement interpret method
        pass

class StructValue:

    pass
class trace_UnionValue(StructValue):

    pass
class trace_Trace:

    pass
class trace_Location:

    def __init__(self, function: str, line: str, file: str, trace_Location: "trace_Step" = None):
        self.function = function
        self.line = line
        self.file = file
        self.trace_Location = trace_Location
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function


    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line


    @property
    def trace_Location(self):
        return self.__trace_Location

    @trace_Location.setter
    def trace_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Location__trace_Location", None)
        self.__trace_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Step"):
                opp_val = getattr(old_value, "trace_Step", None)
                if opp_val == self:
                    setattr(old_value, "trace_Step", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Step"):
                opp_val = getattr(value, "trace_Step", None)
                setattr(value, "trace_Step", self)

class trace_NameToValueMap:

    def __init__(self, key: str, trace_NameToValueMap: "trace_Value" = None, trace_NameToValueMap7: "trace_StructValue" = None):
        self.key = key
        self.trace_NameToValueMap = trace_NameToValueMap
        self.trace_NameToValueMap7 = trace_NameToValueMap7
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def trace_NameToValueMap(self):
        return self.__trace_NameToValueMap

    @trace_NameToValueMap.setter
    def trace_NameToValueMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_NameToValueMap__trace_NameToValueMap", None)
        self.__trace_NameToValueMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Value4"):
                opp_val = getattr(old_value, "trace_Value4", None)
                if opp_val == self:
                    setattr(old_value, "trace_Value4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Value4"):
                opp_val = getattr(value, "trace_Value4", None)
                setattr(value, "trace_Value4", self)

    @property
    def trace_NameToValueMap7(self):
        return self.__trace_NameToValueMap7

    @trace_NameToValueMap7.setter
    def trace_NameToValueMap7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_NameToValueMap__trace_NameToValueMap7", None)
        self.__trace_NameToValueMap7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_StructValue"):
                opp_val = getattr(old_value, "trace_StructValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_StructValue"):
                opp_val = getattr(value, "trace_StructValue", None)
                if opp_val is None:
                    setattr(value, "trace_StructValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Step:

    pass
class trace_LocationOnly(Step):

    pass
class trace_Output(Step):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class trace_FunctionReturn(Step):

    def __init__(self, id: str, displayName: str):
        self.id = id
        self.displayName = displayName
        
        pass
    @property
    def displayName(self):
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class trace_Assignment(Step):

    def __init__(self, id: str, displayName: str, baseName: str, assignmentType: str, trace_Assignment: "trace_Value" = None):
        self.id = id
        self.displayName = displayName
        self.baseName = baseName
        self.assignmentType = assignmentType
        self.trace_Assignment = trace_Assignment
        
        pass
    @property
    def assignmentType(self):
        return self.__assignmentType

    @assignmentType.setter
    def assignmentType(self, assignmentType: str):
        self.__assignmentType = assignmentType


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def displayName(self):
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName


    @property
    def baseName(self):
        return self.__baseName

    @baseName.setter
    def baseName(self, baseName: str):
        self.__baseName = baseName


    @property
    def trace_Assignment(self):
        return self.__trace_Assignment

    @trace_Assignment.setter
    def trace_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Assignment__trace_Assignment", None)
        self.__trace_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Value2"):
                opp_val = getattr(old_value, "trace_Value2", None)
                if opp_val == self:
                    setattr(old_value, "trace_Value2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Value2"):
                opp_val = getattr(value, "trace_Value2", None)
                setattr(value, "trace_Value2", self)

    def getValue(self, trace_expression) :
        # TODO: Implement getValue method
        pass

    def getType(self) :
        # TODO: Implement getType method
        pass

class trace_Value:

    def __init__(self, type: str, trace_Value2: "trace_Assignment" = None, trace_Value: "trace_ArrayValue" = None, trace_Value4: "trace_NameToValueMap" = None):
        self.type = type
        self.trace_Value2 = trace_Value2
        self.trace_Value = trace_Value
        self.trace_Value4 = trace_Value4
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def trace_Value4(self):
        return self.__trace_Value4

    @trace_Value4.setter
    def trace_Value4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Value__trace_Value4", None)
        self.__trace_Value4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_NameToValueMap"):
                opp_val = getattr(old_value, "trace_NameToValueMap", None)
                if opp_val == self:
                    setattr(old_value, "trace_NameToValueMap", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_NameToValueMap"):
                opp_val = getattr(value, "trace_NameToValueMap", None)
                setattr(value, "trace_NameToValueMap", self)

    @property
    def trace_Value2(self):
        return self.__trace_Value2

    @trace_Value2.setter
    def trace_Value2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Value__trace_Value2", None)
        self.__trace_Value2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Assignment"):
                opp_val = getattr(old_value, "trace_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "trace_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Assignment"):
                opp_val = getattr(value, "trace_Assignment", None)
                setattr(value, "trace_Assignment", self)

    @property
    def trace_Value(self):
        return self.__trace_Value

    @trace_Value.setter
    def trace_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Value__trace_Value", None)
        self.__trace_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_ArrayValue"):
                opp_val = getattr(old_value, "trace_ArrayValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_ArrayValue"):
                opp_val = getattr(value, "trace_ArrayValue", None)
                if opp_val is None:
                    setattr(value, "trace_ArrayValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def listChildren(self, trace_requestedExpression):
        # TODO: Implement listChildren method
        pass

    def compare(self, trace_parentPath, trace_old):
        # TODO: Implement compare method
        pass

    def getUserFriendlyRepresentation(self, trace_abridged) :
        # TODO: Implement getUserFriendlyRepresentation method
        pass

    def getChildrenCount(self) :
        # TODO: Implement getChildrenCount method
        pass

    def getValue(self, trace_expression) :
        # TODO: Implement getValue method
        pass

class Value:

    pass
class trace_StructValue(Value):

    pass
class trace_SimpleValue(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class trace_ArrayValue(Value):

    pass
class trace_FunctionCall(Step):

    def __init__(self, id: str, displayName: str):
        self.id = id
        self.displayName = displayName
        
        pass
    @property
    def displayName(self):
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class trace_Failure(Step):

    def __init__(self, reason: str):
        self.reason = reason
        
        pass
    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

