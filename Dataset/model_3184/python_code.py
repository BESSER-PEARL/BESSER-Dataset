from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class debugSeq_Sequence:

    def __init__(self, name: str, disable: str, pname: str, info: str, debugSeq_Sequence9: set["debugSeq_CodeBlock"] = None, debugSeq_Sequence: "debugSeq_Sequences" = None):
        self.name = name
        self.disable = disable
        self.pname = pname
        self.info = info
        self.debugSeq_Sequence9 = debugSeq_Sequence9 if debugSeq_Sequence9 is not None else set()
        self.debugSeq_Sequence = debugSeq_Sequence
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pname(self) -> str:
        return self.__pname

    @pname.setter
    def pname(self, pname: str):
        self.__pname = pname

    @property
    def disable(self) -> str:
        return self.__disable

    @disable.setter
    def disable(self, disable: str):
        self.__disable = disable

    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def debugSeq_Sequence9(self):
        return self.__debugSeq_Sequence9

    @debugSeq_Sequence9.setter
    def debugSeq_Sequence9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Sequence__debugSeq_Sequence9", None)
        self.__debugSeq_Sequence9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "debugSeq_CodeBlock"):
                    opp_val = getattr(item, "debugSeq_CodeBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "debugSeq_CodeBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "debugSeq_CodeBlock"):
                    opp_val = getattr(item, "debugSeq_CodeBlock", None)
                    
                    setattr(item, "debugSeq_CodeBlock", self)
                    

    @property
    def debugSeq_Sequence(self):
        return self.__debugSeq_Sequence

    @debugSeq_Sequence.setter
    def debugSeq_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Sequence__debugSeq_Sequence", None)
        self.__debugSeq_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Sequences7"):
                opp_val = getattr(old_value, "debugSeq_Sequences7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Sequences7"):
                opp_val = getattr(value, "debugSeq_Sequences7", None)
                if opp_val is None:
                    setattr(value, "debugSeq_Sequences7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Statement:

    pass
class debugSeq_VariableDeclaration(Statement):

    def __init__(self, name: str, debugSeq_VariableDeclaration: "debugSeq_Expression" = None, debugSeq_VariableDeclaration183: "debugSeq_VariableRef" = None):
        self.name = name
        self.debugSeq_VariableDeclaration = debugSeq_VariableDeclaration
        self.debugSeq_VariableDeclaration183 = debugSeq_VariableDeclaration183
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def debugSeq_VariableDeclaration(self):
        return self.__debugSeq_VariableDeclaration

    @debugSeq_VariableDeclaration.setter
    def debugSeq_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_VariableDeclaration__debugSeq_VariableDeclaration", None)
        self.__debugSeq_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression"):
                opp_val = getattr(old_value, "debugSeq_Expression", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression"):
                opp_val = getattr(value, "debugSeq_Expression", None)
                setattr(value, "debugSeq_Expression", self)

    @property
    def debugSeq_VariableDeclaration183(self):
        return self.__debugSeq_VariableDeclaration183

    @debugSeq_VariableDeclaration183.setter
    def debugSeq_VariableDeclaration183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_VariableDeclaration__debugSeq_VariableDeclaration183", None)
        self.__debugSeq_VariableDeclaration183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_VariableRef"):
                opp_val = getattr(old_value, "debugSeq_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_VariableRef"):
                opp_val = getattr(value, "debugSeq_VariableRef", None)
                setattr(value, "debugSeq_VariableRef", self)

class debugSeq_Statement:

    pass
class debugSeq_Sequences:

    pass
class Expression:

    pass
class debugSeq_Ternary(Expression):

    pass
class debugSeq_Read32(Expression):

    pass
class debugSeq_Query(Expression):

    def __init__(self, message: str, debugSeq_Query: "debugSeq_Expression" = None, debugSeq_Query105: "debugSeq_Expression" = None):
        self.message = message
        self.debugSeq_Query = debugSeq_Query
        self.debugSeq_Query105 = debugSeq_Query105
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def debugSeq_Query105(self):
        return self.__debugSeq_Query105

    @debugSeq_Query105.setter
    def debugSeq_Query105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Query__debugSeq_Query105", None)
        self.__debugSeq_Query105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression106"):
                opp_val = getattr(old_value, "debugSeq_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression106"):
                opp_val = getattr(value, "debugSeq_Expression106", None)
                setattr(value, "debugSeq_Expression106", self)

    @property
    def debugSeq_Query(self):
        return self.__debugSeq_Query

    @debugSeq_Query.setter
    def debugSeq_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Query__debugSeq_Query", None)
        self.__debugSeq_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression103"):
                opp_val = getattr(old_value, "debugSeq_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression103"):
                opp_val = getattr(value, "debugSeq_Expression103", None)
                setattr(value, "debugSeq_Expression103", self)

class debugSeq_Equality(Expression):

    def __init__(self, op: str, debugSeq_Equality: "debugSeq_Expression" = None, debugSeq_Equality61: "debugSeq_Expression" = None):
        self.op = op
        self.debugSeq_Equality = debugSeq_Equality
        self.debugSeq_Equality61 = debugSeq_Equality61
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def debugSeq_Equality61(self):
        return self.__debugSeq_Equality61

    @debugSeq_Equality61.setter
    def debugSeq_Equality61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Equality__debugSeq_Equality61", None)
        self.__debugSeq_Equality61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression62"):
                opp_val = getattr(old_value, "debugSeq_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression62"):
                opp_val = getattr(value, "debugSeq_Expression62", None)
                setattr(value, "debugSeq_Expression62", self)

    @property
    def debugSeq_Equality(self):
        return self.__debugSeq_Equality

    @debugSeq_Equality.setter
    def debugSeq_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Equality__debugSeq_Equality", None)
        self.__debugSeq_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression59"):
                opp_val = getattr(old_value, "debugSeq_Expression59", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression59"):
                opp_val = getattr(value, "debugSeq_Expression59", None)
                setattr(value, "debugSeq_Expression59", self)

class debugSeq_Rem(Expression):

    pass
class debugSeq_Plus(Expression):

    pass
class debugSeq_DapSwjPins(Expression):

    pass
class debugSeq_BitAnd(Expression):

    pass
class debugSeq_BitXor(Expression):

    pass
class debugSeq_DapWriteABORT(Expression):

    pass
class debugSeq_DapJtagSequence(Expression):

    pass
class debugSeq_Message(Expression):

    def __init__(self, format: str, debugSeq_Message: "debugSeq_Expression" = None, debugSeq_Message112: set["debugSeq_Parameter"] = None):
        self.format = format
        self.debugSeq_Message = debugSeq_Message
        self.debugSeq_Message112 = debugSeq_Message112 if debugSeq_Message112 is not None else set()
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def debugSeq_Message(self):
        return self.__debugSeq_Message

    @debugSeq_Message.setter
    def debugSeq_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Message__debugSeq_Message", None)
        self.__debugSeq_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression110"):
                opp_val = getattr(old_value, "debugSeq_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression110"):
                opp_val = getattr(value, "debugSeq_Expression110", None)
                setattr(value, "debugSeq_Expression110", self)

    @property
    def debugSeq_Message112(self):
        return self.__debugSeq_Message112

    @debugSeq_Message112.setter
    def debugSeq_Message112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Message__debugSeq_Message112", None)
        self.__debugSeq_Message112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "debugSeq_Parameter"):
                    opp_val = getattr(item, "debugSeq_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "debugSeq_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "debugSeq_Parameter"):
                    opp_val = getattr(item, "debugSeq_Parameter", None)
                    
                    setattr(item, "debugSeq_Parameter", self)
                    

class debugSeq_VariableRef(Expression):

    pass
class debugSeq_And(Expression):

    pass
class debugSeq_Shift(Expression):

    def __init__(self, op: str, debugSeq_Shift: "debugSeq_Expression" = None, debugSeq_Shift71: "debugSeq_Expression" = None):
        self.op = op
        self.debugSeq_Shift = debugSeq_Shift
        self.debugSeq_Shift71 = debugSeq_Shift71
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def debugSeq_Shift(self):
        return self.__debugSeq_Shift

    @debugSeq_Shift.setter
    def debugSeq_Shift(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Shift__debugSeq_Shift", None)
        self.__debugSeq_Shift = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression69"):
                opp_val = getattr(old_value, "debugSeq_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression69"):
                opp_val = getattr(value, "debugSeq_Expression69", None)
                setattr(value, "debugSeq_Expression69", self)

    @property
    def debugSeq_Shift71(self):
        return self.__debugSeq_Shift71

    @debugSeq_Shift71.setter
    def debugSeq_Shift71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Shift__debugSeq_Shift71", None)
        self.__debugSeq_Shift71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression72"):
                opp_val = getattr(old_value, "debugSeq_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression72"):
                opp_val = getattr(value, "debugSeq_Expression72", None)
                setattr(value, "debugSeq_Expression72", self)

class debugSeq_Minus(Expression):

    pass
class debugSeq_Read8(Expression):

    pass
class debugSeq_DapSwjSequence(Expression):

    pass
class debugSeq_Not(Expression):

    pass
class debugSeq_ReadAP(Expression):

    pass
class debugSeq_Write32(Expression):

    pass
class debugSeq_Write16(Expression):

    pass
class debugSeq_ReadDP(Expression):

    pass
class debugSeq_Read16(Expression):

    pass
class debugSeq_DapSwjClock(Expression):

    pass
class debugSeq_Mul(Expression):

    pass
class debugSeq_Or(Expression):

    pass
class debugSeq_IntConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class debugSeq_Read64(Expression):

    pass
class debugSeq_BitNot(Expression):

    pass
class debugSeq_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class debugSeq_QueryValue(Expression):

    def __init__(self, message: str, debugSeq_QueryValue: "debugSeq_Expression" = None):
        self.message = message
        self.debugSeq_QueryValue = debugSeq_QueryValue
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def debugSeq_QueryValue(self):
        return self.__debugSeq_QueryValue

    @debugSeq_QueryValue.setter
    def debugSeq_QueryValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_QueryValue__debugSeq_QueryValue", None)
        self.__debugSeq_QueryValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression108"):
                opp_val = getattr(old_value, "debugSeq_Expression108", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression108"):
                opp_val = getattr(value, "debugSeq_Expression108", None)
                setattr(value, "debugSeq_Expression108", self)

class debugSeq_DapDelay(Expression):

    pass
class debugSeq_WriteAP(Expression):

    pass
class debugSeq_Div(Expression):

    pass
class debugSeq_Write64(Expression):

    pass
class debugSeq_Write8(Expression):

    pass
class debugSeq_SequenceCall(Expression):

    def __init__(self, seqname: str):
        self.seqname = seqname
        
    @property
    def seqname(self) -> str:
        return self.__seqname

    @seqname.setter
    def seqname(self, seqname: str):
        self.__seqname = seqname

class debugSeq_BitOr(Expression):

    pass
class debugSeq_WriteDP(Expression):

    pass
class debugSeq_LoadDebugInfo(Expression):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class debugSeq_Comparison(Expression):

    def __init__(self, op: str, debugSeq_Comparison: "debugSeq_Expression" = None, debugSeq_Comparison66: "debugSeq_Expression" = None):
        self.op = op
        self.debugSeq_Comparison = debugSeq_Comparison
        self.debugSeq_Comparison66 = debugSeq_Comparison66
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def debugSeq_Comparison66(self):
        return self.__debugSeq_Comparison66

    @debugSeq_Comparison66.setter
    def debugSeq_Comparison66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Comparison__debugSeq_Comparison66", None)
        self.__debugSeq_Comparison66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression67"):
                opp_val = getattr(old_value, "debugSeq_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression67"):
                opp_val = getattr(value, "debugSeq_Expression67", None)
                setattr(value, "debugSeq_Expression67", self)

    @property
    def debugSeq_Comparison(self):
        return self.__debugSeq_Comparison

    @debugSeq_Comparison.setter
    def debugSeq_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Comparison__debugSeq_Comparison", None)
        self.__debugSeq_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression64"):
                opp_val = getattr(old_value, "debugSeq_Expression64", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression64"):
                opp_val = getattr(value, "debugSeq_Expression64", None)
                setattr(value, "debugSeq_Expression64", self)

class debugSeq_Assignment(Expression):

    def __init__(self, op: str, debugSeq_Assignment: "debugSeq_Expression" = None, debugSeq_Assignment23: "debugSeq_Expression" = None):
        self.op = op
        self.debugSeq_Assignment = debugSeq_Assignment
        self.debugSeq_Assignment23 = debugSeq_Assignment23
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def debugSeq_Assignment(self):
        return self.__debugSeq_Assignment

    @debugSeq_Assignment.setter
    def debugSeq_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Assignment__debugSeq_Assignment", None)
        self.__debugSeq_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression21"):
                opp_val = getattr(old_value, "debugSeq_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression21"):
                opp_val = getattr(value, "debugSeq_Expression21", None)
                setattr(value, "debugSeq_Expression21", self)

    @property
    def debugSeq_Assignment23(self):
        return self.__debugSeq_Assignment23

    @debugSeq_Assignment23.setter
    def debugSeq_Assignment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Assignment__debugSeq_Assignment23", None)
        self.__debugSeq_Assignment23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression24"):
                opp_val = getattr(old_value, "debugSeq_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression24"):
                opp_val = getattr(value, "debugSeq_Expression24", None)
                setattr(value, "debugSeq_Expression24", self)

class debugSeq_Parameter:

    pass
class Parameter:

    pass
class debugSeq_Expression(Statement, Parameter):

    pass
class CodeBlock:

    pass
class debugSeq_Control(CodeBlock):

    def __init__(self, timeout: str, debugSeq_Control: "debugSeq_Expression" = None, debugSeq_Control15: "debugSeq_Expression" = None, debugSeq_Control18: set["debugSeq_CodeBlock"] = None):
        self.timeout = timeout
        self.debugSeq_Control = debugSeq_Control
        self.debugSeq_Control15 = debugSeq_Control15
        self.debugSeq_Control18 = debugSeq_Control18 if debugSeq_Control18 is not None else set()
        
    @property
    def timeout(self) -> str:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: str):
        self.__timeout = timeout

    @property
    def debugSeq_Control(self):
        return self.__debugSeq_Control

    @debugSeq_Control.setter
    def debugSeq_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Control__debugSeq_Control", None)
        self.__debugSeq_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression13"):
                opp_val = getattr(old_value, "debugSeq_Expression13", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression13"):
                opp_val = getattr(value, "debugSeq_Expression13", None)
                setattr(value, "debugSeq_Expression13", self)

    @property
    def debugSeq_Control15(self):
        return self.__debugSeq_Control15

    @debugSeq_Control15.setter
    def debugSeq_Control15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Control__debugSeq_Control15", None)
        self.__debugSeq_Control15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Expression16"):
                opp_val = getattr(old_value, "debugSeq_Expression16", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Expression16"):
                opp_val = getattr(value, "debugSeq_Expression16", None)
                setattr(value, "debugSeq_Expression16", self)

    @property
    def debugSeq_Control18(self):
        return self.__debugSeq_Control18

    @debugSeq_Control18.setter
    def debugSeq_Control18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Control__debugSeq_Control18", None)
        self.__debugSeq_Control18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "debugSeq_CodeBlock19"):
                    opp_val = getattr(item, "debugSeq_CodeBlock19", None)
                    
                    if opp_val == self:
                        setattr(item, "debugSeq_CodeBlock19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "debugSeq_CodeBlock19"):
                    opp_val = getattr(item, "debugSeq_CodeBlock19", None)
                    
                    setattr(item, "debugSeq_CodeBlock19", self)
                    

class debugSeq_Block(CodeBlock):

    def __init__(self, atomic: str, debugSeq_Block: set["debugSeq_Statement"] = None):
        self.atomic = atomic
        self.debugSeq_Block = debugSeq_Block if debugSeq_Block is not None else set()
        
    @property
    def atomic(self) -> str:
        return self.__atomic

    @atomic.setter
    def atomic(self, atomic: str):
        self.__atomic = atomic

    @property
    def debugSeq_Block(self):
        return self.__debugSeq_Block

    @debugSeq_Block.setter
    def debugSeq_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_Block__debugSeq_Block", None)
        self.__debugSeq_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "debugSeq_Statement11"):
                    opp_val = getattr(item, "debugSeq_Statement11", None)
                    
                    if opp_val == self:
                        setattr(item, "debugSeq_Statement11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "debugSeq_Statement11"):
                    opp_val = getattr(item, "debugSeq_Statement11", None)
                    
                    setattr(item, "debugSeq_Statement11", self)
                    

class debugSeq_CodeBlock:

    def __init__(self, info: str, debugSeq_CodeBlock: "debugSeq_Sequence" = None, debugSeq_CodeBlock19: "debugSeq_Control" = None):
        self.info = info
        self.debugSeq_CodeBlock = debugSeq_CodeBlock
        self.debugSeq_CodeBlock19 = debugSeq_CodeBlock19
        
    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def debugSeq_CodeBlock(self):
        return self.__debugSeq_CodeBlock

    @debugSeq_CodeBlock.setter
    def debugSeq_CodeBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_CodeBlock__debugSeq_CodeBlock", None)
        self.__debugSeq_CodeBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Sequence9"):
                opp_val = getattr(old_value, "debugSeq_Sequence9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Sequence9"):
                opp_val = getattr(value, "debugSeq_Sequence9", None)
                if opp_val is None:
                    setattr(value, "debugSeq_Sequence9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def debugSeq_CodeBlock19(self):
        return self.__debugSeq_CodeBlock19

    @debugSeq_CodeBlock19.setter
    def debugSeq_CodeBlock19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_CodeBlock__debugSeq_CodeBlock19", None)
        self.__debugSeq_CodeBlock19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_Control18"):
                opp_val = getattr(old_value, "debugSeq_Control18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_Control18"):
                opp_val = getattr(value, "debugSeq_Control18", None)
                if opp_val is None:
                    setattr(value, "debugSeq_Control18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class debugSeq_DebugVars:

    def __init__(self, configfile: str, version: str, pname: str, debugSeq_DebugVars: "debugSeq_DebugSeqModel" = None, debugSeq_DebugVars4: set["debugSeq_Statement"] = None):
        self.configfile = configfile
        self.version = version
        self.pname = pname
        self.debugSeq_DebugVars = debugSeq_DebugVars
        self.debugSeq_DebugVars4 = debugSeq_DebugVars4 if debugSeq_DebugVars4 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def pname(self) -> str:
        return self.__pname

    @pname.setter
    def pname(self, pname: str):
        self.__pname = pname

    @property
    def configfile(self) -> str:
        return self.__configfile

    @configfile.setter
    def configfile(self, configfile: str):
        self.__configfile = configfile

    @property
    def debugSeq_DebugVars(self):
        return self.__debugSeq_DebugVars

    @debugSeq_DebugVars.setter
    def debugSeq_DebugVars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_DebugVars__debugSeq_DebugVars", None)
        self.__debugSeq_DebugVars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debugSeq_DebugSeqModel"):
                opp_val = getattr(old_value, "debugSeq_DebugSeqModel", None)
                if opp_val == self:
                    setattr(old_value, "debugSeq_DebugSeqModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debugSeq_DebugSeqModel"):
                opp_val = getattr(value, "debugSeq_DebugSeqModel", None)
                setattr(value, "debugSeq_DebugSeqModel", self)

    @property
    def debugSeq_DebugVars4(self):
        return self.__debugSeq_DebugVars4

    @debugSeq_DebugVars4.setter
    def debugSeq_DebugVars4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_debugSeq_DebugVars__debugSeq_DebugVars4", None)
        self.__debugSeq_DebugVars4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "debugSeq_Statement"):
                    opp_val = getattr(item, "debugSeq_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "debugSeq_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "debugSeq_Statement"):
                    opp_val = getattr(item, "debugSeq_Statement", None)
                    
                    setattr(item, "debugSeq_Statement", self)
                    

class debugSeq_DebugSeqModel:

    pass