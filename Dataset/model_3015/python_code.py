from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessLevel(Enum):
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"


############################################
# Definition of Classes
############################################

class Call:

    pass
class miniJava_MethodCall2(Call):

    pass
class miniJava_NewCall(Call):

    pass
class miniJava_ObjectInstance:

    pass
class miniJava_Frame:

    def __init__(self, miniJava_Frame175: "miniJava_Call" = None, miniJava_Frame177: "miniJava_ObjectInstance" = None, 182: "miniJava_Frame" = None, 181: "miniJava_Frame" = None, 186: "miniJava_Frame" = None, 185: "miniJava_Frame" = None, miniJava_Frame: "miniJava_State" = None, miniJava_Frame188: "miniJava_Context" = None, miniJava_Frame191: "miniJava_Value" = None):
        self.miniJava_Frame175 = miniJava_Frame175
        self.miniJava_Frame177 = miniJava_Frame177
        self.182 = 182
        self.181 = 181
        self.186 = 186
        self.185 = 185
        self.miniJava_Frame = miniJava_Frame
        self.miniJava_Frame188 = miniJava_Frame188
        self.miniJava_Frame191 = miniJava_Frame191
        
    @property
    def 182(self):
        return self.__182

    @182.setter
    def 182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__182", None)
        self.__182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "181"):
                opp_val = getattr(old_value, "181", None)
                if opp_val == self:
                    setattr(old_value, "181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "181"):
                opp_val = getattr(value, "181", None)
                setattr(value, "181", self)

    @property
    def 186(self):
        return self.__186

    @186.setter
    def 186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__186", None)
        self.__186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "185"):
                opp_val = getattr(old_value, "185", None)
                if opp_val == self:
                    setattr(old_value, "185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "185"):
                opp_val = getattr(value, "185", None)
                setattr(value, "185", self)

    @property
    def miniJava_Frame175(self):
        return self.__miniJava_Frame175

    @miniJava_Frame175.setter
    def miniJava_Frame175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__miniJava_Frame175", None)
        self.__miniJava_Frame175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Call"):
                opp_val = getattr(old_value, "miniJava_Call", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Call"):
                opp_val = getattr(value, "miniJava_Call", None)
                setattr(value, "miniJava_Call", self)

    @property
    def 181(self):
        return self.__181

    @181.setter
    def 181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__181", None)
        self.__181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "182"):
                opp_val = getattr(old_value, "182", None)
                if opp_val == self:
                    setattr(old_value, "182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "182"):
                opp_val = getattr(value, "182", None)
                setattr(value, "182", self)

    @property
    def miniJava_Frame(self):
        return self.__miniJava_Frame

    @miniJava_Frame.setter
    def miniJava_Frame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__miniJava_Frame", None)
        self.__miniJava_Frame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State167"):
                opp_val = getattr(old_value, "miniJava_State167", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_State167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State167"):
                opp_val = getattr(value, "miniJava_State167", None)
                setattr(value, "miniJava_State167", self)

    @property
    def miniJava_Frame188(self):
        return self.__miniJava_Frame188

    @miniJava_Frame188.setter
    def miniJava_Frame188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__miniJava_Frame188", None)
        self.__miniJava_Frame188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Context189"):
                opp_val = getattr(old_value, "miniJava_Context189", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Context189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Context189"):
                opp_val = getattr(value, "miniJava_Context189", None)
                setattr(value, "miniJava_Context189", self)

    @property
    def 185(self):
        return self.__185

    @185.setter
    def 185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__185", None)
        self.__185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "186"):
                opp_val = getattr(old_value, "186", None)
                if opp_val == self:
                    setattr(old_value, "186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "186"):
                opp_val = getattr(value, "186", None)
                setattr(value, "186", self)

    @property
    def miniJava_Frame177(self):
        return self.__miniJava_Frame177

    @miniJava_Frame177.setter
    def miniJava_Frame177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__miniJava_Frame177", None)
        self.__miniJava_Frame177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ObjectInstance178"):
                opp_val = getattr(old_value, "miniJava_ObjectInstance178", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ObjectInstance178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ObjectInstance178"):
                opp_val = getattr(value, "miniJava_ObjectInstance178", None)
                setattr(value, "miniJava_ObjectInstance178", self)

    @property
    def miniJava_Frame191(self):
        return self.__miniJava_Frame191

    @miniJava_Frame191.setter
    def miniJava_Frame191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Frame__miniJava_Frame191", None)
        self.__miniJava_Frame191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Value192"):
                opp_val = getattr(old_value, "miniJava_Value192", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Value192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Value192"):
                opp_val = getattr(value, "miniJava_Value192", None)
                setattr(value, "miniJava_Value192", self)

    def findCurrentContext(self) -> str:
        # TODO: Implement findCurrentContext method
        pass

    def findCurrentFrame(self) -> str:
        # TODO: Implement findCurrentFrame method
        pass

class miniJava_Call:

    pass
class miniJava_ArrayInstance:

    def __init__(self, size: str, miniJava_ArrayInstance: "miniJava_State" = None, miniJava_ArrayInstance209: "miniJava_ArrayRefValue" = None, miniJava_ArrayInstance204: set["miniJava_Value"] = None):
        self.size = size
        self.miniJava_ArrayInstance = miniJava_ArrayInstance
        self.miniJava_ArrayInstance209 = miniJava_ArrayInstance209
        self.miniJava_ArrayInstance204 = miniJava_ArrayInstance204 if miniJava_ArrayInstance204 is not None else set()
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def miniJava_ArrayInstance209(self):
        return self.__miniJava_ArrayInstance209

    @miniJava_ArrayInstance209.setter
    def miniJava_ArrayInstance209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayInstance__miniJava_ArrayInstance209", None)
        self.__miniJava_ArrayInstance209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayRefValue"):
                opp_val = getattr(old_value, "miniJava_ArrayRefValue", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayRefValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayRefValue"):
                opp_val = getattr(value, "miniJava_ArrayRefValue", None)
                setattr(value, "miniJava_ArrayRefValue", self)

    @property
    def miniJava_ArrayInstance(self):
        return self.__miniJava_ArrayInstance

    @miniJava_ArrayInstance.setter
    def miniJava_ArrayInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayInstance__miniJava_ArrayInstance", None)
        self.__miniJava_ArrayInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State173"):
                opp_val = getattr(old_value, "miniJava_State173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State173"):
                opp_val = getattr(value, "miniJava_State173", None)
                if opp_val is None:
                    setattr(value, "miniJava_State173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_ArrayInstance204(self):
        return self.__miniJava_ArrayInstance204

    @miniJava_ArrayInstance204.setter
    def miniJava_ArrayInstance204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayInstance__miniJava_ArrayInstance204", None)
        self.__miniJava_ArrayInstance204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Value205"):
                    opp_val = getattr(item, "miniJava_Value205", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Value205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Value205"):
                    opp_val = getattr(item, "miniJava_Value205", None)
                    
                    setattr(item, "miniJava_Value205", self)
                    

class miniJava_OutputStream:

    def __init__(self, stream: str, miniJava_OutputStream: "miniJava_State" = None):
        self.stream = stream
        self.miniJava_OutputStream = miniJava_OutputStream
        
    @property
    def stream(self) -> str:
        return self.__stream

    @stream.setter
    def stream(self, stream: str):
        self.__stream = stream

    @property
    def miniJava_OutputStream(self):
        return self.__miniJava_OutputStream

    @miniJava_OutputStream.setter
    def miniJava_OutputStream(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_OutputStream__miniJava_OutputStream", None)
        self.__miniJava_OutputStream = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State171"):
                opp_val = getattr(old_value, "miniJava_State171", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_State171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State171"):
                opp_val = getattr(value, "miniJava_State171", None)
                setattr(value, "miniJava_State171", self)

class miniJava_FieldBinding:

    pass
class miniJava_Value:

    def __init__(self, miniJava_Value: "miniJava_SymbolBinding" = None, miniJava_Value165: "miniJava_FieldBinding" = None, miniJava_Value192: "miniJava_Frame" = None, miniJava_Value205: "miniJava_ArrayInstance" = None):
        self.miniJava_Value = miniJava_Value
        self.miniJava_Value165 = miniJava_Value165
        self.miniJava_Value192 = miniJava_Value192
        self.miniJava_Value205 = miniJava_Value205
        
    @property
    def miniJava_Value192(self):
        return self.__miniJava_Value192

    @miniJava_Value192.setter
    def miniJava_Value192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Value__miniJava_Value192", None)
        self.__miniJava_Value192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Frame191"):
                opp_val = getattr(old_value, "miniJava_Frame191", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Frame191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Frame191"):
                opp_val = getattr(value, "miniJava_Frame191", None)
                setattr(value, "miniJava_Frame191", self)

    @property
    def miniJava_Value205(self):
        return self.__miniJava_Value205

    @miniJava_Value205.setter
    def miniJava_Value205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Value__miniJava_Value205", None)
        self.__miniJava_Value205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayInstance204"):
                opp_val = getattr(old_value, "miniJava_ArrayInstance204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayInstance204"):
                opp_val = getattr(value, "miniJava_ArrayInstance204", None)
                if opp_val is None:
                    setattr(value, "miniJava_ArrayInstance204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_Value165(self):
        return self.__miniJava_Value165

    @miniJava_Value165.setter
    def miniJava_Value165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Value__miniJava_Value165", None)
        self.__miniJava_Value165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_FieldBinding164"):
                opp_val = getattr(old_value, "miniJava_FieldBinding164", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_FieldBinding164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_FieldBinding164"):
                opp_val = getattr(value, "miniJava_FieldBinding164", None)
                setattr(value, "miniJava_FieldBinding164", self)

    @property
    def miniJava_Value(self):
        return self.__miniJava_Value

    @miniJava_Value.setter
    def miniJava_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Value__miniJava_Value", None)
        self.__miniJava_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_SymbolBinding157"):
                opp_val = getattr(old_value, "miniJava_SymbolBinding157", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_SymbolBinding157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_SymbolBinding157"):
                opp_val = getattr(value, "miniJava_SymbolBinding157", None)
                setattr(value, "miniJava_SymbolBinding157", self)

    def copy(self) -> str:
        # TODO: Implement copy method
        pass

    def customToString(self):
        # TODO: Implement customToString method
        pass

class Value:

    pass
class miniJava_StringValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def copy(self) -> Value:
        # TODO: Implement copy method
        pass

    def customToString(self):
        # TODO: Implement customToString method
        pass

class miniJava_NullValue(Value):

    def __init__(self):
        
    def copy(self) -> Value:
        # TODO: Implement copy method
        pass

class miniJava_ArrayRefValue(Value):

    def __init__(self, miniJava_ArrayRefValue: "miniJava_ArrayInstance" = None):
        self.miniJava_ArrayRefValue = miniJava_ArrayRefValue
        
    @property
    def miniJava_ArrayRefValue(self):
        return self.__miniJava_ArrayRefValue

    @miniJava_ArrayRefValue.setter
    def miniJava_ArrayRefValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayRefValue__miniJava_ArrayRefValue", None)
        self.__miniJava_ArrayRefValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayInstance209"):
                opp_val = getattr(old_value, "miniJava_ArrayInstance209", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayInstance209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayInstance209"):
                opp_val = getattr(value, "miniJava_ArrayInstance209", None)
                setattr(value, "miniJava_ArrayInstance209", self)

    def copy(self) -> Value:
        # TODO: Implement copy method
        pass

class miniJava_ObjectRefValue(Value):

    def __init__(self, miniJava_ObjectRefValue: "miniJava_ObjectInstance" = None):
        self.miniJava_ObjectRefValue = miniJava_ObjectRefValue
        
    @property
    def miniJava_ObjectRefValue(self):
        return self.__miniJava_ObjectRefValue

    @miniJava_ObjectRefValue.setter
    def miniJava_ObjectRefValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ObjectRefValue__miniJava_ObjectRefValue", None)
        self.__miniJava_ObjectRefValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ObjectInstance207"):
                opp_val = getattr(old_value, "miniJava_ObjectInstance207", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ObjectInstance207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ObjectInstance207"):
                opp_val = getattr(value, "miniJava_ObjectInstance207", None)
                setattr(value, "miniJava_ObjectInstance207", self)

    def customToString(self):
        # TODO: Implement customToString method
        pass

    def copy(self) -> Value:
        # TODO: Implement copy method
        pass

class miniJava_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    def customToString(self):
        # TODO: Implement customToString method
        pass

    def copy(self) -> Value:
        # TODO: Implement copy method
        pass

class miniJava_IntegerValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def customToString(self):
        # TODO: Implement customToString method
        pass

    def copy(self) -> Value:
        # TODO: Implement copy method
        pass

class miniJava_Context:

    def __init__(self, miniJava_Context: set["miniJava_SymbolBinding"] = None, 151: "miniJava_Context" = None, : "miniJava_Context" = None, 155: "miniJava_Context" = None, 154: "miniJava_Context" = None, miniJava_Context189: "miniJava_Frame" = None):
        self.miniJava_Context = miniJava_Context if miniJava_Context is not None else set()
        self.151 = 151
        self. = 
        self.155 = 155
        self.154 = 154
        self.miniJava_Context189 = miniJava_Context189
        
    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Context__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "151"):
                opp_val = getattr(old_value, "151", None)
                if opp_val == self:
                    setattr(old_value, "151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "151"):
                opp_val = getattr(value, "151", None)
                setattr(value, "151", self)

    @property
    def 154(self):
        return self.__154

    @154.setter
    def 154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Context__154", None)
        self.__154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "155"):
                opp_val = getattr(old_value, "155", None)
                if opp_val == self:
                    setattr(old_value, "155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "155"):
                opp_val = getattr(value, "155", None)
                setattr(value, "155", self)

    @property
    def 151(self):
        return self.__151

    @151.setter
    def 151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Context__151", None)
        self.__151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def miniJava_Context189(self):
        return self.__miniJava_Context189

    @miniJava_Context189.setter
    def miniJava_Context189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Context__miniJava_Context189", None)
        self.__miniJava_Context189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Frame188"):
                opp_val = getattr(old_value, "miniJava_Frame188", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Frame188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Frame188"):
                opp_val = getattr(value, "miniJava_Frame188", None)
                setattr(value, "miniJava_Frame188", self)

    @property
    def miniJava_Context(self):
        return self.__miniJava_Context

    @miniJava_Context.setter
    def miniJava_Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Context__miniJava_Context", None)
        self.__miniJava_Context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_SymbolBinding"):
                    opp_val = getattr(item, "miniJava_SymbolBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_SymbolBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_SymbolBinding"):
                    opp_val = getattr(item, "miniJava_SymbolBinding", None)
                    
                    setattr(item, "miniJava_SymbolBinding", self)
                    

    @property
    def 155(self):
        return self.__155

    @155.setter
    def 155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Context__155", None)
        self.__155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "154"):
                opp_val = getattr(old_value, "154", None)
                if opp_val == self:
                    setattr(old_value, "154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "154"):
                opp_val = getattr(value, "154", None)
                setattr(value, "154", self)

    def createChildContext(self) -> str:
        # TODO: Implement createChildContext method
        pass

    def findBinding(self, symbol: Symbol) -> str:
        # TODO: Implement findBinding method
        pass

    def findCurrentContext(self) -> str:
        # TODO: Implement findCurrentContext method
        pass

class miniJava_SymbolBinding:

    pass
class Expression:

    pass
class miniJava_Neg(Expression):

    def __init__(self, miniJava_Neg: "miniJava_Expression" = None):
        self.miniJava_Neg = miniJava_Neg
        
    @property
    def miniJava_Neg(self):
        return self.__miniJava_Neg

    @miniJava_Neg.setter
    def miniJava_Neg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Neg__miniJava_Neg", None)
        self.__miniJava_Neg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression123"):
                opp_val = getattr(old_value, "miniJava_Expression123", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression123"):
                opp_val = getattr(value, "miniJava_Expression123", None)
                setattr(value, "miniJava_Expression123", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Plus(Expression):

    def __init__(self, miniJava_Plus: "miniJava_Expression" = None, miniJava_Plus96: "miniJava_Expression" = None):
        self.miniJava_Plus = miniJava_Plus
        self.miniJava_Plus96 = miniJava_Plus96
        
    @property
    def miniJava_Plus(self):
        return self.__miniJava_Plus

    @miniJava_Plus.setter
    def miniJava_Plus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Plus__miniJava_Plus", None)
        self.__miniJava_Plus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression94"):
                opp_val = getattr(old_value, "miniJava_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression94"):
                opp_val = getattr(value, "miniJava_Expression94", None)
                setattr(value, "miniJava_Expression94", self)

    @property
    def miniJava_Plus96(self):
        return self.__miniJava_Plus96

    @miniJava_Plus96.setter
    def miniJava_Plus96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Plus__miniJava_Plus96", None)
        self.__miniJava_Plus96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression97"):
                opp_val = getattr(old_value, "miniJava_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression97"):
                opp_val = getattr(value, "miniJava_Expression97", None)
                setattr(value, "miniJava_Expression97", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Inequality(Expression):

    def __init__(self, miniJava_Inequality: "miniJava_Expression" = None, miniJava_Inequality71: "miniJava_Expression" = None):
        self.miniJava_Inequality = miniJava_Inequality
        self.miniJava_Inequality71 = miniJava_Inequality71
        
    @property
    def miniJava_Inequality(self):
        return self.__miniJava_Inequality

    @miniJava_Inequality.setter
    def miniJava_Inequality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Inequality__miniJava_Inequality", None)
        self.__miniJava_Inequality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression69"):
                opp_val = getattr(old_value, "miniJava_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression69"):
                opp_val = getattr(value, "miniJava_Expression69", None)
                setattr(value, "miniJava_Expression69", self)

    @property
    def miniJava_Inequality71(self):
        return self.__miniJava_Inequality71

    @miniJava_Inequality71.setter
    def miniJava_Inequality71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Inequality__miniJava_Inequality71", None)
        self.__miniJava_Inequality71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression72"):
                opp_val = getattr(old_value, "miniJava_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression72"):
                opp_val = getattr(value, "miniJava_Expression72", None)
                setattr(value, "miniJava_Expression72", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Multiplication(Expression):

    def __init__(self, miniJava_Multiplication: "miniJava_Expression" = None, miniJava_Multiplication106: "miniJava_Expression" = None):
        self.miniJava_Multiplication = miniJava_Multiplication
        self.miniJava_Multiplication106 = miniJava_Multiplication106
        
    @property
    def miniJava_Multiplication(self):
        return self.__miniJava_Multiplication

    @miniJava_Multiplication.setter
    def miniJava_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Multiplication__miniJava_Multiplication", None)
        self.__miniJava_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression104"):
                opp_val = getattr(old_value, "miniJava_Expression104", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression104"):
                opp_val = getattr(value, "miniJava_Expression104", None)
                setattr(value, "miniJava_Expression104", self)

    @property
    def miniJava_Multiplication106(self):
        return self.__miniJava_Multiplication106

    @miniJava_Multiplication106.setter
    def miniJava_Multiplication106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Multiplication__miniJava_Multiplication106", None)
        self.__miniJava_Multiplication106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression107"):
                opp_val = getattr(old_value, "miniJava_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression107"):
                opp_val = getattr(value, "miniJava_Expression107", None)
                setattr(value, "miniJava_Expression107", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_ArrayLength(Expression):

    def __init__(self, miniJava_ArrayLength: "miniJava_Expression" = None):
        self.miniJava_ArrayLength = miniJava_ArrayLength
        
    @property
    def miniJava_ArrayLength(self):
        return self.__miniJava_ArrayLength

    @miniJava_ArrayLength.setter
    def miniJava_ArrayLength(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayLength__miniJava_ArrayLength", None)
        self.__miniJava_ArrayLength = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression119"):
                opp_val = getattr(old_value, "miniJava_Expression119", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression119"):
                opp_val = getattr(value, "miniJava_Expression119", None)
                setattr(value, "miniJava_Expression119", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Equality(Expression):

    def __init__(self, miniJava_Equality: "miniJava_Expression" = None, miniJava_Equality66: "miniJava_Expression" = None):
        self.miniJava_Equality = miniJava_Equality
        self.miniJava_Equality66 = miniJava_Equality66
        
    @property
    def miniJava_Equality66(self):
        return self.__miniJava_Equality66

    @miniJava_Equality66.setter
    def miniJava_Equality66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Equality__miniJava_Equality66", None)
        self.__miniJava_Equality66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression67"):
                opp_val = getattr(old_value, "miniJava_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression67"):
                opp_val = getattr(value, "miniJava_Expression67", None)
                setattr(value, "miniJava_Expression67", self)

    @property
    def miniJava_Equality(self):
        return self.__miniJava_Equality

    @miniJava_Equality.setter
    def miniJava_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Equality__miniJava_Equality", None)
        self.__miniJava_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression64"):
                opp_val = getattr(old_value, "miniJava_Expression64", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression64"):
                opp_val = getattr(value, "miniJava_Expression64", None)
                setattr(value, "miniJava_Expression64", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_NewObject(Expression):

    def __init__(self, miniJava_NewObject: "miniJava_Class" = None, miniJava_NewObject140: set["miniJava_Expression"] = None, miniJava_NewObject194: "miniJava_NewCall" = None):
        self.miniJava_NewObject = miniJava_NewObject
        self.miniJava_NewObject140 = miniJava_NewObject140 if miniJava_NewObject140 is not None else set()
        self.miniJava_NewObject194 = miniJava_NewObject194
        
    @property
    def miniJava_NewObject194(self):
        return self.__miniJava_NewObject194

    @miniJava_NewObject194.setter
    def miniJava_NewObject194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_NewObject__miniJava_NewObject194", None)
        self.__miniJava_NewObject194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NewCall"):
                opp_val = getattr(old_value, "miniJava_NewCall", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_NewCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NewCall"):
                opp_val = getattr(value, "miniJava_NewCall", None)
                setattr(value, "miniJava_NewCall", self)

    @property
    def miniJava_NewObject140(self):
        return self.__miniJava_NewObject140

    @miniJava_NewObject140.setter
    def miniJava_NewObject140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_NewObject__miniJava_NewObject140", None)
        self.__miniJava_NewObject140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Expression141"):
                    opp_val = getattr(item, "miniJava_Expression141", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Expression141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Expression141"):
                    opp_val = getattr(item, "miniJava_Expression141", None)
                    
                    setattr(item, "miniJava_Expression141", self)
                    

    @property
    def miniJava_NewObject(self):
        return self.__miniJava_NewObject

    @miniJava_NewObject.setter
    def miniJava_NewObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_NewObject__miniJava_NewObject", None)
        self.__miniJava_NewObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class138"):
                opp_val = getattr(old_value, "miniJava_Class138", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class138"):
                opp_val = getattr(value, "miniJava_Class138", None)
                setattr(value, "miniJava_Class138", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_NewArray(Expression):

    def __init__(self, miniJava_NewArray: "miniJava_TypeRef" = None, miniJava_NewArray145: "miniJava_Expression" = None):
        self.miniJava_NewArray = miniJava_NewArray
        self.miniJava_NewArray145 = miniJava_NewArray145
        
    @property
    def miniJava_NewArray(self):
        return self.__miniJava_NewArray

    @miniJava_NewArray.setter
    def miniJava_NewArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_NewArray__miniJava_NewArray", None)
        self.__miniJava_NewArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_TypeRef143"):
                opp_val = getattr(old_value, "miniJava_TypeRef143", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_TypeRef143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_TypeRef143"):
                opp_val = getattr(value, "miniJava_TypeRef143", None)
                setattr(value, "miniJava_TypeRef143", self)

    @property
    def miniJava_NewArray145(self):
        return self.__miniJava_NewArray145

    @miniJava_NewArray145.setter
    def miniJava_NewArray145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_NewArray__miniJava_NewArray145", None)
        self.__miniJava_NewArray145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression146"):
                opp_val = getattr(old_value, "miniJava_Expression146", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression146"):
                opp_val = getattr(value, "miniJava_Expression146", None)
                setattr(value, "miniJava_Expression146", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Inferior(Expression):

    def __init__(self, miniJava_Inferior: "miniJava_Expression" = None, miniJava_Inferior91: "miniJava_Expression" = None):
        self.miniJava_Inferior = miniJava_Inferior
        self.miniJava_Inferior91 = miniJava_Inferior91
        
    @property
    def miniJava_Inferior91(self):
        return self.__miniJava_Inferior91

    @miniJava_Inferior91.setter
    def miniJava_Inferior91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Inferior__miniJava_Inferior91", None)
        self.__miniJava_Inferior91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression92"):
                opp_val = getattr(old_value, "miniJava_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression92"):
                opp_val = getattr(value, "miniJava_Expression92", None)
                setattr(value, "miniJava_Expression92", self)

    @property
    def miniJava_Inferior(self):
        return self.__miniJava_Inferior

    @miniJava_Inferior.setter
    def miniJava_Inferior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Inferior__miniJava_Inferior", None)
        self.__miniJava_Inferior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression89"):
                opp_val = getattr(old_value, "miniJava_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression89"):
                opp_val = getattr(value, "miniJava_Expression89", None)
                setattr(value, "miniJava_Expression89", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Superior(Expression):

    def __init__(self, miniJava_Superior: "miniJava_Expression" = None, miniJava_Superior86: "miniJava_Expression" = None):
        self.miniJava_Superior = miniJava_Superior
        self.miniJava_Superior86 = miniJava_Superior86
        
    @property
    def miniJava_Superior(self):
        return self.__miniJava_Superior

    @miniJava_Superior.setter
    def miniJava_Superior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Superior__miniJava_Superior", None)
        self.__miniJava_Superior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression84"):
                opp_val = getattr(old_value, "miniJava_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression84"):
                opp_val = getattr(value, "miniJava_Expression84", None)
                setattr(value, "miniJava_Expression84", self)

    @property
    def miniJava_Superior86(self):
        return self.__miniJava_Superior86

    @miniJava_Superior86.setter
    def miniJava_Superior86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Superior__miniJava_Superior86", None)
        self.__miniJava_Superior86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression87"):
                opp_val = getattr(old_value, "miniJava_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression87"):
                opp_val = getattr(value, "miniJava_Expression87", None)
                setattr(value, "miniJava_Expression87", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Super(Expression):

    pass
class miniJava_This(Expression):

    def __init__(self):
        
    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_SymbolRef(Expression):

    def __init__(self, miniJava_SymbolRef: "miniJava_Symbol" = None):
        self.miniJava_SymbolRef = miniJava_SymbolRef
        
    @property
    def miniJava_SymbolRef(self):
        return self.__miniJava_SymbolRef

    @miniJava_SymbolRef.setter
    def miniJava_SymbolRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_SymbolRef__miniJava_SymbolRef", None)
        self.__miniJava_SymbolRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Symbol"):
                opp_val = getattr(old_value, "miniJava_Symbol", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Symbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Symbol"):
                opp_val = getattr(value, "miniJava_Symbol", None)
                setattr(value, "miniJava_Symbol", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_And(Expression):

    def __init__(self, miniJava_And: "miniJava_Expression" = None, miniJava_And61: "miniJava_Expression" = None):
        self.miniJava_And = miniJava_And
        self.miniJava_And61 = miniJava_And61
        
    @property
    def miniJava_And61(self):
        return self.__miniJava_And61

    @miniJava_And61.setter
    def miniJava_And61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_And__miniJava_And61", None)
        self.__miniJava_And61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression62"):
                opp_val = getattr(old_value, "miniJava_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression62"):
                opp_val = getattr(value, "miniJava_Expression62", None)
                setattr(value, "miniJava_Expression62", self)

    @property
    def miniJava_And(self):
        return self.__miniJava_And

    @miniJava_And.setter
    def miniJava_And(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_And__miniJava_And", None)
        self.__miniJava_And = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression59"):
                opp_val = getattr(old_value, "miniJava_Expression59", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression59"):
                opp_val = getattr(value, "miniJava_Expression59", None)
                setattr(value, "miniJava_Expression59", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_SuperiorOrEqual(Expression):

    def __init__(self, miniJava_SuperiorOrEqual: "miniJava_Expression" = None, miniJava_SuperiorOrEqual76: "miniJava_Expression" = None):
        self.miniJava_SuperiorOrEqual = miniJava_SuperiorOrEqual
        self.miniJava_SuperiorOrEqual76 = miniJava_SuperiorOrEqual76
        
    @property
    def miniJava_SuperiorOrEqual(self):
        return self.__miniJava_SuperiorOrEqual

    @miniJava_SuperiorOrEqual.setter
    def miniJava_SuperiorOrEqual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_SuperiorOrEqual__miniJava_SuperiorOrEqual", None)
        self.__miniJava_SuperiorOrEqual = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression74"):
                opp_val = getattr(old_value, "miniJava_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression74"):
                opp_val = getattr(value, "miniJava_Expression74", None)
                setattr(value, "miniJava_Expression74", self)

    @property
    def miniJava_SuperiorOrEqual76(self):
        return self.__miniJava_SuperiorOrEqual76

    @miniJava_SuperiorOrEqual76.setter
    def miniJava_SuperiorOrEqual76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_SuperiorOrEqual__miniJava_SuperiorOrEqual76", None)
        self.__miniJava_SuperiorOrEqual76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression77"):
                opp_val = getattr(old_value, "miniJava_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression77"):
                opp_val = getattr(value, "miniJava_Expression77", None)
                setattr(value, "miniJava_Expression77", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Division(Expression):

    def __init__(self, miniJava_Division: "miniJava_Expression" = None, miniJava_Division111: "miniJava_Expression" = None):
        self.miniJava_Division = miniJava_Division
        self.miniJava_Division111 = miniJava_Division111
        
    @property
    def miniJava_Division(self):
        return self.__miniJava_Division

    @miniJava_Division.setter
    def miniJava_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Division__miniJava_Division", None)
        self.__miniJava_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression109"):
                opp_val = getattr(old_value, "miniJava_Expression109", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression109"):
                opp_val = getattr(value, "miniJava_Expression109", None)
                setattr(value, "miniJava_Expression109", self)

    @property
    def miniJava_Division111(self):
        return self.__miniJava_Division111

    @miniJava_Division111.setter
    def miniJava_Division111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Division__miniJava_Division111", None)
        self.__miniJava_Division111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression112"):
                opp_val = getattr(old_value, "miniJava_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression112"):
                opp_val = getattr(value, "miniJava_Expression112", None)
                setattr(value, "miniJava_Expression112", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_MethodCall(Expression):

    def __init__(self, miniJava_MethodCall: "miniJava_Expression" = None, miniJava_MethodCall132: "miniJava_Method" = None, miniJava_MethodCall135: set["miniJava_Expression"] = None, miniJava_MethodCall196: "miniJava_MethodCall2" = None):
        self.miniJava_MethodCall = miniJava_MethodCall
        self.miniJava_MethodCall132 = miniJava_MethodCall132
        self.miniJava_MethodCall135 = miniJava_MethodCall135 if miniJava_MethodCall135 is not None else set()
        self.miniJava_MethodCall196 = miniJava_MethodCall196
        
    @property
    def miniJava_MethodCall(self):
        return self.__miniJava_MethodCall

    @miniJava_MethodCall.setter
    def miniJava_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_MethodCall__miniJava_MethodCall", None)
        self.__miniJava_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression130"):
                opp_val = getattr(old_value, "miniJava_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression130"):
                opp_val = getattr(value, "miniJava_Expression130", None)
                setattr(value, "miniJava_Expression130", self)

    @property
    def miniJava_MethodCall132(self):
        return self.__miniJava_MethodCall132

    @miniJava_MethodCall132.setter
    def miniJava_MethodCall132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_MethodCall__miniJava_MethodCall132", None)
        self.__miniJava_MethodCall132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method133"):
                opp_val = getattr(old_value, "miniJava_Method133", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Method133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method133"):
                opp_val = getattr(value, "miniJava_Method133", None)
                setattr(value, "miniJava_Method133", self)

    @property
    def miniJava_MethodCall196(self):
        return self.__miniJava_MethodCall196

    @miniJava_MethodCall196.setter
    def miniJava_MethodCall196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_MethodCall__miniJava_MethodCall196", None)
        self.__miniJava_MethodCall196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall2"):
                opp_val = getattr(old_value, "miniJava_MethodCall2", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall2"):
                opp_val = getattr(value, "miniJava_MethodCall2", None)
                setattr(value, "miniJava_MethodCall2", self)

    @property
    def miniJava_MethodCall135(self):
        return self.__miniJava_MethodCall135

    @miniJava_MethodCall135.setter
    def miniJava_MethodCall135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_MethodCall__miniJava_MethodCall135", None)
        self.__miniJava_MethodCall135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Expression136"):
                    opp_val = getattr(item, "miniJava_Expression136", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Expression136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Expression136"):
                    opp_val = getattr(item, "miniJava_Expression136", None)
                    
                    setattr(item, "miniJava_Expression136", self)
                    

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_ArrayAccess(Expression):

    def __init__(self, miniJava_ArrayAccess: "miniJava_Expression" = None, miniJava_ArrayAccess116: "miniJava_Expression" = None):
        self.miniJava_ArrayAccess = miniJava_ArrayAccess
        self.miniJava_ArrayAccess116 = miniJava_ArrayAccess116
        
    @property
    def miniJava_ArrayAccess116(self):
        return self.__miniJava_ArrayAccess116

    @miniJava_ArrayAccess116.setter
    def miniJava_ArrayAccess116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayAccess__miniJava_ArrayAccess116", None)
        self.__miniJava_ArrayAccess116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression117"):
                opp_val = getattr(old_value, "miniJava_Expression117", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression117"):
                opp_val = getattr(value, "miniJava_Expression117", None)
                setattr(value, "miniJava_Expression117", self)

    @property
    def miniJava_ArrayAccess(self):
        return self.__miniJava_ArrayAccess

    @miniJava_ArrayAccess.setter
    def miniJava_ArrayAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayAccess__miniJava_ArrayAccess", None)
        self.__miniJava_ArrayAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression114"):
                opp_val = getattr(old_value, "miniJava_Expression114", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression114"):
                opp_val = getattr(value, "miniJava_Expression114", None)
                setattr(value, "miniJava_Expression114", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Null(Expression):

    def __init__(self):
        
    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_FieldAccess(Expression):

    def __init__(self, miniJava_FieldAccess: "miniJava_Expression" = None, miniJava_FieldAccess127: "miniJava_Field" = None):
        self.miniJava_FieldAccess = miniJava_FieldAccess
        self.miniJava_FieldAccess127 = miniJava_FieldAccess127
        
    @property
    def miniJava_FieldAccess(self):
        return self.__miniJava_FieldAccess

    @miniJava_FieldAccess.setter
    def miniJava_FieldAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_FieldAccess__miniJava_FieldAccess", None)
        self.__miniJava_FieldAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression125"):
                opp_val = getattr(old_value, "miniJava_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression125"):
                opp_val = getattr(value, "miniJava_Expression125", None)
                setattr(value, "miniJava_Expression125", self)

    @property
    def miniJava_FieldAccess127(self):
        return self.__miniJava_FieldAccess127

    @miniJava_FieldAccess127.setter
    def miniJava_FieldAccess127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_FieldAccess__miniJava_FieldAccess127", None)
        self.__miniJava_FieldAccess127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Field128"):
                opp_val = getattr(old_value, "miniJava_Field128", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Field128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Field128"):
                opp_val = getattr(value, "miniJava_Field128", None)
                setattr(value, "miniJava_Field128", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Not(Expression):

    def __init__(self, miniJava_Not: "miniJava_Expression" = None):
        self.miniJava_Not = miniJava_Not
        
    @property
    def miniJava_Not(self):
        return self.__miniJava_Not

    @miniJava_Not.setter
    def miniJava_Not(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Not__miniJava_Not", None)
        self.__miniJava_Not = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression121"):
                opp_val = getattr(old_value, "miniJava_Expression121", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression121"):
                opp_val = getattr(value, "miniJava_Expression121", None)
                setattr(value, "miniJava_Expression121", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Minus(Expression):

    def __init__(self, miniJava_Minus: "miniJava_Expression" = None, miniJava_Minus101: "miniJava_Expression" = None):
        self.miniJava_Minus = miniJava_Minus
        self.miniJava_Minus101 = miniJava_Minus101
        
    @property
    def miniJava_Minus101(self):
        return self.__miniJava_Minus101

    @miniJava_Minus101.setter
    def miniJava_Minus101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Minus__miniJava_Minus101", None)
        self.__miniJava_Minus101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression102"):
                opp_val = getattr(old_value, "miniJava_Expression102", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression102"):
                opp_val = getattr(value, "miniJava_Expression102", None)
                setattr(value, "miniJava_Expression102", self)

    @property
    def miniJava_Minus(self):
        return self.__miniJava_Minus

    @miniJava_Minus.setter
    def miniJava_Minus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Minus__miniJava_Minus", None)
        self.__miniJava_Minus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression99"):
                opp_val = getattr(old_value, "miniJava_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression99"):
                opp_val = getattr(value, "miniJava_Expression99", None)
                setattr(value, "miniJava_Expression99", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_InferiorOrEqual(Expression):

    def __init__(self, miniJava_InferiorOrEqual: "miniJava_Expression" = None, miniJava_InferiorOrEqual81: "miniJava_Expression" = None):
        self.miniJava_InferiorOrEqual = miniJava_InferiorOrEqual
        self.miniJava_InferiorOrEqual81 = miniJava_InferiorOrEqual81
        
    @property
    def miniJava_InferiorOrEqual81(self):
        return self.__miniJava_InferiorOrEqual81

    @miniJava_InferiorOrEqual81.setter
    def miniJava_InferiorOrEqual81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_InferiorOrEqual__miniJava_InferiorOrEqual81", None)
        self.__miniJava_InferiorOrEqual81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression82"):
                opp_val = getattr(old_value, "miniJava_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression82"):
                opp_val = getattr(value, "miniJava_Expression82", None)
                setattr(value, "miniJava_Expression82", self)

    @property
    def miniJava_InferiorOrEqual(self):
        return self.__miniJava_InferiorOrEqual

    @miniJava_InferiorOrEqual.setter
    def miniJava_InferiorOrEqual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_InferiorOrEqual__miniJava_InferiorOrEqual", None)
        self.__miniJava_InferiorOrEqual = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression79"):
                opp_val = getattr(old_value, "miniJava_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression79"):
                opp_val = getattr(value, "miniJava_Expression79", None)
                setattr(value, "miniJava_Expression79", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_Or(Expression):

    def __init__(self, miniJava_Or: "miniJava_Expression" = None, miniJava_Or56: "miniJava_Expression" = None):
        self.miniJava_Or = miniJava_Or
        self.miniJava_Or56 = miniJava_Or56
        
    @property
    def miniJava_Or(self):
        return self.__miniJava_Or

    @miniJava_Or.setter
    def miniJava_Or(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Or__miniJava_Or", None)
        self.__miniJava_Or = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression54"):
                opp_val = getattr(old_value, "miniJava_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression54"):
                opp_val = getattr(value, "miniJava_Expression54", None)
                setattr(value, "miniJava_Expression54", self)

    @property
    def miniJava_Or56(self):
        return self.__miniJava_Or56

    @miniJava_Or56.setter
    def miniJava_Or56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Or__miniJava_Or56", None)
        self.__miniJava_Or56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression57"):
                opp_val = getattr(old_value, "miniJava_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression57"):
                opp_val = getattr(value, "miniJava_Expression57", None)
                setattr(value, "miniJava_Expression57", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

class miniJava_TypeRef:

    def __init__(self, miniJava_TypeRef: "miniJava_TypedDeclaration" = None, miniJava_TypeRef143: "miniJava_NewArray" = None):
        self.miniJava_TypeRef = miniJava_TypeRef
        self.miniJava_TypeRef143 = miniJava_TypeRef143
        
    @property
    def miniJava_TypeRef(self):
        return self.__miniJava_TypeRef

    @miniJava_TypeRef.setter
    def miniJava_TypeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeRef__miniJava_TypeRef", None)
        self.__miniJava_TypeRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_TypedDeclaration"):
                opp_val = getattr(old_value, "miniJava_TypedDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_TypedDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_TypedDeclaration"):
                opp_val = getattr(value, "miniJava_TypedDeclaration", None)
                setattr(value, "miniJava_TypedDeclaration", self)

    @property
    def miniJava_TypeRef143(self):
        return self.__miniJava_TypeRef143

    @miniJava_TypeRef143.setter
    def miniJava_TypeRef143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeRef__miniJava_TypeRef143", None)
        self.__miniJava_TypeRef143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NewArray"):
                opp_val = getattr(old_value, "miniJava_NewArray", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_NewArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NewArray"):
                opp_val = getattr(value, "miniJava_NewArray", None)
                setattr(value, "miniJava_NewArray", self)

    def compare(self, other: str):
        # TODO: Implement compare method
        pass

class miniJava_Assignee:

    pass
class Assignee:

    pass
class miniJava_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SingleTypeRef:

    pass
class miniJava_StringTypeRef(SingleTypeRef):

    pass
class miniJava_BooleanTypeRef(SingleTypeRef):

    pass
class miniJava_IntegerTypeRef(SingleTypeRef):

    pass
class miniJava_VoidTypeRef(SingleTypeRef):

    pass
class miniJava_ClassRef(SingleTypeRef):

    def __init__(self, miniJava_ClassRef: "miniJava_TypeDeclaration" = None):
        self.miniJava_ClassRef = miniJava_ClassRef
        
    @property
    def miniJava_ClassRef(self):
        return self.__miniJava_ClassRef

    @miniJava_ClassRef.setter
    def miniJava_ClassRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassRef__miniJava_ClassRef", None)
        self.__miniJava_ClassRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_TypeDeclaration45"):
                opp_val = getattr(old_value, "miniJava_TypeDeclaration45", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_TypeDeclaration45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_TypeDeclaration45"):
                opp_val = getattr(value, "miniJava_TypeDeclaration45", None)
                setattr(value, "miniJava_TypeDeclaration45", self)

    def compare(self, other: TypeRef):
        # TODO: Implement compare method
        pass

class TypeRef:

    pass
class miniJava_ArrayTypeRef(TypeRef):

    pass
class miniJava_SingleTypeRef(TypeRef):

    pass
class miniJava_Statement:

    def __init__(self, miniJava_Statement: "miniJava_Block" = None):
        self.miniJava_Statement = miniJava_Statement
        
    @property
    def miniJava_Statement(self):
        return self.__miniJava_Statement

    @miniJava_Statement.setter
    def miniJava_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement", None)
        self.__miniJava_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block16"):
                opp_val = getattr(old_value, "miniJava_Block16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block16"):
                opp_val = getattr(value, "miniJava_Block16", None)
                if opp_val is None:
                    setattr(value, "miniJava_Block16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class Statement:

    pass
class miniJava_Assignment(Statement):

    def __init__(self, miniJava_Assignment48: "miniJava_Assignee" = None, miniJava_Assignment: "miniJava_ForStatement" = None, miniJava_Assignment40: "miniJava_ForStatement" = None, miniJava_Assignment50: "miniJava_Expression" = None):
        self.miniJava_Assignment48 = miniJava_Assignment48
        self.miniJava_Assignment = miniJava_Assignment
        self.miniJava_Assignment40 = miniJava_Assignment40
        self.miniJava_Assignment50 = miniJava_Assignment50
        
    @property
    def miniJava_Assignment(self):
        return self.__miniJava_Assignment

    @miniJava_Assignment.setter
    def miniJava_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Assignment__miniJava_Assignment", None)
        self.__miniJava_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ForStatement"):
                opp_val = getattr(old_value, "miniJava_ForStatement", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ForStatement"):
                opp_val = getattr(value, "miniJava_ForStatement", None)
                setattr(value, "miniJava_ForStatement", self)

    @property
    def miniJava_Assignment40(self):
        return self.__miniJava_Assignment40

    @miniJava_Assignment40.setter
    def miniJava_Assignment40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Assignment__miniJava_Assignment40", None)
        self.__miniJava_Assignment40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ForStatement39"):
                opp_val = getattr(old_value, "miniJava_ForStatement39", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ForStatement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ForStatement39"):
                opp_val = getattr(value, "miniJava_ForStatement39", None)
                setattr(value, "miniJava_ForStatement39", self)

    @property
    def miniJava_Assignment50(self):
        return self.__miniJava_Assignment50

    @miniJava_Assignment50.setter
    def miniJava_Assignment50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Assignment__miniJava_Assignment50", None)
        self.__miniJava_Assignment50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression51"):
                opp_val = getattr(old_value, "miniJava_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression51"):
                opp_val = getattr(value, "miniJava_Expression51", None)
                setattr(value, "miniJava_Expression51", self)

    @property
    def miniJava_Assignment48(self):
        return self.__miniJava_Assignment48

    @miniJava_Assignment48.setter
    def miniJava_Assignment48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Assignment__miniJava_Assignment48", None)
        self.__miniJava_Assignment48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Assignee"):
                opp_val = getattr(old_value, "miniJava_Assignee", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Assignee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Assignee"):
                opp_val = getattr(value, "miniJava_Assignee", None)
                setattr(value, "miniJava_Assignee", self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class miniJava_ForStatement(Statement):

    def __init__(self, miniJava_ForStatement: "miniJava_Assignment" = None, miniJava_ForStatement36: "miniJava_Expression" = None, miniJava_ForStatement39: "miniJava_Assignment" = None, miniJava_ForStatement42: "miniJava_Block" = None):
        self.miniJava_ForStatement = miniJava_ForStatement
        self.miniJava_ForStatement36 = miniJava_ForStatement36
        self.miniJava_ForStatement39 = miniJava_ForStatement39
        self.miniJava_ForStatement42 = miniJava_ForStatement42
        
    @property
    def miniJava_ForStatement39(self):
        return self.__miniJava_ForStatement39

    @miniJava_ForStatement39.setter
    def miniJava_ForStatement39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ForStatement__miniJava_ForStatement39", None)
        self.__miniJava_ForStatement39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Assignment40"):
                opp_val = getattr(old_value, "miniJava_Assignment40", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Assignment40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Assignment40"):
                opp_val = getattr(value, "miniJava_Assignment40", None)
                setattr(value, "miniJava_Assignment40", self)

    @property
    def miniJava_ForStatement(self):
        return self.__miniJava_ForStatement

    @miniJava_ForStatement.setter
    def miniJava_ForStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ForStatement__miniJava_ForStatement", None)
        self.__miniJava_ForStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Assignment"):
                opp_val = getattr(old_value, "miniJava_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Assignment"):
                opp_val = getattr(value, "miniJava_Assignment", None)
                setattr(value, "miniJava_Assignment", self)

    @property
    def miniJava_ForStatement36(self):
        return self.__miniJava_ForStatement36

    @miniJava_ForStatement36.setter
    def miniJava_ForStatement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ForStatement__miniJava_ForStatement36", None)
        self.__miniJava_ForStatement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression37"):
                opp_val = getattr(old_value, "miniJava_Expression37", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression37"):
                opp_val = getattr(value, "miniJava_Expression37", None)
                setattr(value, "miniJava_Expression37", self)

    @property
    def miniJava_ForStatement42(self):
        return self.__miniJava_ForStatement42

    @miniJava_ForStatement42.setter
    def miniJava_ForStatement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ForStatement__miniJava_ForStatement42", None)
        self.__miniJava_ForStatement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block43"):
                opp_val = getattr(old_value, "miniJava_Block43", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Block43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block43"):
                opp_val = getattr(value, "miniJava_Block43", None)
                setattr(value, "miniJava_Block43", self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class miniJava_WhileStatement(Statement):

    def __init__(self, miniJava_WhileStatement: "miniJava_Expression" = None, miniJava_WhileStatement32: "miniJava_Block" = None):
        self.miniJava_WhileStatement = miniJava_WhileStatement
        self.miniJava_WhileStatement32 = miniJava_WhileStatement32
        
    @property
    def miniJava_WhileStatement32(self):
        return self.__miniJava_WhileStatement32

    @miniJava_WhileStatement32.setter
    def miniJava_WhileStatement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_WhileStatement__miniJava_WhileStatement32", None)
        self.__miniJava_WhileStatement32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block33"):
                opp_val = getattr(old_value, "miniJava_Block33", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Block33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block33"):
                opp_val = getattr(value, "miniJava_Block33", None)
                setattr(value, "miniJava_Block33", self)

    @property
    def miniJava_WhileStatement(self):
        return self.__miniJava_WhileStatement

    @miniJava_WhileStatement.setter
    def miniJava_WhileStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_WhileStatement__miniJava_WhileStatement", None)
        self.__miniJava_WhileStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression30"):
                opp_val = getattr(old_value, "miniJava_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression30"):
                opp_val = getattr(value, "miniJava_Expression30", None)
                setattr(value, "miniJava_Expression30", self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class miniJava_IfStatement(Statement):

    def __init__(self, miniJava_IfStatement: "miniJava_Expression" = None, miniJava_IfStatement24: "miniJava_Block" = None, miniJava_IfStatement27: "miniJava_Block" = None):
        self.miniJava_IfStatement = miniJava_IfStatement
        self.miniJava_IfStatement24 = miniJava_IfStatement24
        self.miniJava_IfStatement27 = miniJava_IfStatement27
        
    @property
    def miniJava_IfStatement27(self):
        return self.__miniJava_IfStatement27

    @miniJava_IfStatement27.setter
    def miniJava_IfStatement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_IfStatement__miniJava_IfStatement27", None)
        self.__miniJava_IfStatement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block28"):
                opp_val = getattr(old_value, "miniJava_Block28", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Block28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block28"):
                opp_val = getattr(value, "miniJava_Block28", None)
                setattr(value, "miniJava_Block28", self)

    @property
    def miniJava_IfStatement(self):
        return self.__miniJava_IfStatement

    @miniJava_IfStatement.setter
    def miniJava_IfStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_IfStatement__miniJava_IfStatement", None)
        self.__miniJava_IfStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression22"):
                opp_val = getattr(old_value, "miniJava_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression22"):
                opp_val = getattr(value, "miniJava_Expression22", None)
                setattr(value, "miniJava_Expression22", self)

    @property
    def miniJava_IfStatement24(self):
        return self.__miniJava_IfStatement24

    @miniJava_IfStatement24.setter
    def miniJava_IfStatement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_IfStatement__miniJava_IfStatement24", None)
        self.__miniJava_IfStatement24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block25"):
                opp_val = getattr(old_value, "miniJava_Block25", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Block25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block25"):
                opp_val = getattr(value, "miniJava_Block25", None)
                setattr(value, "miniJava_Block25", self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class miniJava_Return(Statement):

    def __init__(self, miniJava_Return: "miniJava_Expression" = None):
        self.miniJava_Return = miniJava_Return
        
    @property
    def miniJava_Return(self):
        return self.__miniJava_Return

    @miniJava_Return.setter
    def miniJava_Return(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Return__miniJava_Return", None)
        self.__miniJava_Return = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression20"):
                opp_val = getattr(old_value, "miniJava_Expression20", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression20"):
                opp_val = getattr(value, "miniJava_Expression20", None)
                setattr(value, "miniJava_Expression20", self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class miniJava_PrintStatement(Statement):

    def __init__(self, miniJava_PrintStatement: "miniJava_Expression" = None):
        self.miniJava_PrintStatement = miniJava_PrintStatement
        
    @property
    def miniJava_PrintStatement(self):
        return self.__miniJava_PrintStatement

    @miniJava_PrintStatement.setter
    def miniJava_PrintStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_PrintStatement__miniJava_PrintStatement", None)
        self.__miniJava_PrintStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expression18"):
                opp_val = getattr(old_value, "miniJava_Expression18", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expression18"):
                opp_val = getattr(value, "miniJava_Expression18", None)
                setattr(value, "miniJava_Expression18", self)

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class TypeDeclaration:

    pass
class miniJava_Class(TypeDeclaration):

    def __init__(self, abstract: bool, miniJava_Class: "miniJava_Class" = None, miniJava_Class9: "miniJava_Class" = None, miniJava_Class138: "miniJava_NewObject" = None, miniJava_Class202: "miniJava_ObjectInstance" = None):
        self.abstract = abstract
        self.miniJava_Class = miniJava_Class
        self.miniJava_Class9 = miniJava_Class9
        self.miniJava_Class138 = miniJava_Class138
        self.miniJava_Class202 = miniJava_Class202
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def miniJava_Class202(self):
        return self.__miniJava_Class202

    @miniJava_Class202.setter
    def miniJava_Class202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class202", None)
        self.__miniJava_Class202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ObjectInstance201"):
                opp_val = getattr(old_value, "miniJava_ObjectInstance201", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ObjectInstance201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ObjectInstance201"):
                opp_val = getattr(value, "miniJava_ObjectInstance201", None)
                setattr(value, "miniJava_ObjectInstance201", self)

    @property
    def miniJava_Class9(self):
        return self.__miniJava_Class9

    @miniJava_Class9.setter
    def miniJava_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class9", None)
        self.__miniJava_Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class"):
                opp_val = getattr(old_value, "miniJava_Class", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class"):
                opp_val = getattr(value, "miniJava_Class", None)
                setattr(value, "miniJava_Class", self)

    @property
    def miniJava_Class138(self):
        return self.__miniJava_Class138

    @miniJava_Class138.setter
    def miniJava_Class138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class138", None)
        self.__miniJava_Class138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NewObject"):
                opp_val = getattr(old_value, "miniJava_NewObject", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_NewObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NewObject"):
                opp_val = getattr(value, "miniJava_NewObject", None)
                setattr(value, "miniJava_NewObject", self)

    @property
    def miniJava_Class(self):
        return self.__miniJava_Class

    @miniJava_Class.setter
    def miniJava_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class", None)
        self.__miniJava_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class9"):
                opp_val = getattr(old_value, "miniJava_Class9", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class9"):
                opp_val = getattr(value, "miniJava_Class9", None)
                setattr(value, "miniJava_Class9", self)

class miniJava_Interface(TypeDeclaration):

    pass
class NamedElement:

    pass
class miniJava_TypedDeclaration(NamedElement):

    pass
class miniJava_Expression(Statement, Assignee):

    def __init__(self, miniJava_Expression: "miniJava_Field" = None, miniJava_Expression18: "miniJava_PrintStatement" = None, miniJava_Expression20: "miniJava_Return" = None, miniJava_Expression22: "miniJava_IfStatement" = None, miniJava_Expression30: "miniJava_WhileStatement" = None, miniJava_Expression37: "miniJava_ForStatement" = None, miniJava_Expression54: "miniJava_Or" = None, miniJava_Expression57: "miniJava_Or" = None, miniJava_Expression59: "miniJava_And" = None, miniJava_Expression62: "miniJava_And" = None, miniJava_Expression51: "miniJava_Assignment" = None, miniJava_Expression74: "miniJava_SuperiorOrEqual" = None, miniJava_Expression77: "miniJava_SuperiorOrEqual" = None, miniJava_Expression79: "miniJava_InferiorOrEqual" = None, miniJava_Expression82: "miniJava_InferiorOrEqual" = None, miniJava_Expression84: "miniJava_Superior" = None, miniJava_Expression87: "miniJava_Superior" = None, miniJava_Expression89: "miniJava_Inferior" = None, miniJava_Expression64: "miniJava_Equality" = None, miniJava_Expression67: "miniJava_Equality" = None, miniJava_Expression69: "miniJava_Inequality" = None, miniJava_Expression72: "miniJava_Inequality" = None, miniJava_Expression99: "miniJava_Minus" = None, miniJava_Expression102: "miniJava_Minus" = None, miniJava_Expression104: "miniJava_Multiplication" = None, miniJava_Expression107: "miniJava_Multiplication" = None, miniJava_Expression109: "miniJava_Division" = None, miniJava_Expression92: "miniJava_Inferior" = None, miniJava_Expression94: "miniJava_Plus" = None, miniJava_Expression97: "miniJava_Plus" = None, miniJava_Expression114: "miniJava_ArrayAccess" = None, miniJava_Expression117: "miniJava_ArrayAccess" = None, miniJava_Expression119: "miniJava_ArrayLength" = None, miniJava_Expression121: "miniJava_Not" = None, miniJava_Expression112: "miniJava_Division" = None, miniJava_Expression125: "miniJava_FieldAccess" = None, miniJava_Expression130: "miniJava_MethodCall" = None, miniJava_Expression136: "miniJava_MethodCall" = None, miniJava_Expression123: "miniJava_Neg" = None, miniJava_Expression146: "miniJava_NewArray" = None, miniJava_Expression141: "miniJava_NewObject" = None):
        self.miniJava_Expression = miniJava_Expression
        self.miniJava_Expression18 = miniJava_Expression18
        self.miniJava_Expression20 = miniJava_Expression20
        self.miniJava_Expression22 = miniJava_Expression22
        self.miniJava_Expression30 = miniJava_Expression30
        self.miniJava_Expression37 = miniJava_Expression37
        self.miniJava_Expression54 = miniJava_Expression54
        self.miniJava_Expression57 = miniJava_Expression57
        self.miniJava_Expression59 = miniJava_Expression59
        self.miniJava_Expression62 = miniJava_Expression62
        self.miniJava_Expression51 = miniJava_Expression51
        self.miniJava_Expression74 = miniJava_Expression74
        self.miniJava_Expression77 = miniJava_Expression77
        self.miniJava_Expression79 = miniJava_Expression79
        self.miniJava_Expression82 = miniJava_Expression82
        self.miniJava_Expression84 = miniJava_Expression84
        self.miniJava_Expression87 = miniJava_Expression87
        self.miniJava_Expression89 = miniJava_Expression89
        self.miniJava_Expression64 = miniJava_Expression64
        self.miniJava_Expression67 = miniJava_Expression67
        self.miniJava_Expression69 = miniJava_Expression69
        self.miniJava_Expression72 = miniJava_Expression72
        self.miniJava_Expression99 = miniJava_Expression99
        self.miniJava_Expression102 = miniJava_Expression102
        self.miniJava_Expression104 = miniJava_Expression104
        self.miniJava_Expression107 = miniJava_Expression107
        self.miniJava_Expression109 = miniJava_Expression109
        self.miniJava_Expression92 = miniJava_Expression92
        self.miniJava_Expression94 = miniJava_Expression94
        self.miniJava_Expression97 = miniJava_Expression97
        self.miniJava_Expression114 = miniJava_Expression114
        self.miniJava_Expression117 = miniJava_Expression117
        self.miniJava_Expression119 = miniJava_Expression119
        self.miniJava_Expression121 = miniJava_Expression121
        self.miniJava_Expression112 = miniJava_Expression112
        self.miniJava_Expression125 = miniJava_Expression125
        self.miniJava_Expression130 = miniJava_Expression130
        self.miniJava_Expression136 = miniJava_Expression136
        self.miniJava_Expression123 = miniJava_Expression123
        self.miniJava_Expression146 = miniJava_Expression146
        self.miniJava_Expression141 = miniJava_Expression141
        
    @property
    def miniJava_Expression121(self):
        return self.__miniJava_Expression121

    @miniJava_Expression121.setter
    def miniJava_Expression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression121", None)
        self.__miniJava_Expression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Not"):
                opp_val = getattr(old_value, "miniJava_Not", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Not", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Not"):
                opp_val = getattr(value, "miniJava_Not", None)
                setattr(value, "miniJava_Not", self)

    @property
    def miniJava_Expression102(self):
        return self.__miniJava_Expression102

    @miniJava_Expression102.setter
    def miniJava_Expression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression102", None)
        self.__miniJava_Expression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Minus101"):
                opp_val = getattr(old_value, "miniJava_Minus101", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Minus101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Minus101"):
                opp_val = getattr(value, "miniJava_Minus101", None)
                setattr(value, "miniJava_Minus101", self)

    @property
    def miniJava_Expression89(self):
        return self.__miniJava_Expression89

    @miniJava_Expression89.setter
    def miniJava_Expression89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression89", None)
        self.__miniJava_Expression89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Inferior"):
                opp_val = getattr(old_value, "miniJava_Inferior", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Inferior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Inferior"):
                opp_val = getattr(value, "miniJava_Inferior", None)
                setattr(value, "miniJava_Inferior", self)

    @property
    def miniJava_Expression141(self):
        return self.__miniJava_Expression141

    @miniJava_Expression141.setter
    def miniJava_Expression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression141", None)
        self.__miniJava_Expression141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NewObject140"):
                opp_val = getattr(old_value, "miniJava_NewObject140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NewObject140"):
                opp_val = getattr(value, "miniJava_NewObject140", None)
                if opp_val is None:
                    setattr(value, "miniJava_NewObject140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_Expression18(self):
        return self.__miniJava_Expression18

    @miniJava_Expression18.setter
    def miniJava_Expression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression18", None)
        self.__miniJava_Expression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_PrintStatement"):
                opp_val = getattr(old_value, "miniJava_PrintStatement", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_PrintStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_PrintStatement"):
                opp_val = getattr(value, "miniJava_PrintStatement", None)
                setattr(value, "miniJava_PrintStatement", self)

    @property
    def miniJava_Expression117(self):
        return self.__miniJava_Expression117

    @miniJava_Expression117.setter
    def miniJava_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression117", None)
        self.__miniJava_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayAccess116"):
                opp_val = getattr(old_value, "miniJava_ArrayAccess116", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayAccess116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayAccess116"):
                opp_val = getattr(value, "miniJava_ArrayAccess116", None)
                setattr(value, "miniJava_ArrayAccess116", self)

    @property
    def miniJava_Expression30(self):
        return self.__miniJava_Expression30

    @miniJava_Expression30.setter
    def miniJava_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression30", None)
        self.__miniJava_Expression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_WhileStatement"):
                opp_val = getattr(old_value, "miniJava_WhileStatement", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_WhileStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_WhileStatement"):
                opp_val = getattr(value, "miniJava_WhileStatement", None)
                setattr(value, "miniJava_WhileStatement", self)

    @property
    def miniJava_Expression69(self):
        return self.__miniJava_Expression69

    @miniJava_Expression69.setter
    def miniJava_Expression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression69", None)
        self.__miniJava_Expression69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Inequality"):
                opp_val = getattr(old_value, "miniJava_Inequality", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Inequality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Inequality"):
                opp_val = getattr(value, "miniJava_Inequality", None)
                setattr(value, "miniJava_Inequality", self)

    @property
    def miniJava_Expression37(self):
        return self.__miniJava_Expression37

    @miniJava_Expression37.setter
    def miniJava_Expression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression37", None)
        self.__miniJava_Expression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ForStatement36"):
                opp_val = getattr(old_value, "miniJava_ForStatement36", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ForStatement36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ForStatement36"):
                opp_val = getattr(value, "miniJava_ForStatement36", None)
                setattr(value, "miniJava_ForStatement36", self)

    @property
    def miniJava_Expression107(self):
        return self.__miniJava_Expression107

    @miniJava_Expression107.setter
    def miniJava_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression107", None)
        self.__miniJava_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Multiplication106"):
                opp_val = getattr(old_value, "miniJava_Multiplication106", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Multiplication106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Multiplication106"):
                opp_val = getattr(value, "miniJava_Multiplication106", None)
                setattr(value, "miniJava_Multiplication106", self)

    @property
    def miniJava_Expression74(self):
        return self.__miniJava_Expression74

    @miniJava_Expression74.setter
    def miniJava_Expression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression74", None)
        self.__miniJava_Expression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_SuperiorOrEqual"):
                opp_val = getattr(old_value, "miniJava_SuperiorOrEqual", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_SuperiorOrEqual", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_SuperiorOrEqual"):
                opp_val = getattr(value, "miniJava_SuperiorOrEqual", None)
                setattr(value, "miniJava_SuperiorOrEqual", self)

    @property
    def miniJava_Expression99(self):
        return self.__miniJava_Expression99

    @miniJava_Expression99.setter
    def miniJava_Expression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression99", None)
        self.__miniJava_Expression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Minus"):
                opp_val = getattr(old_value, "miniJava_Minus", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Minus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Minus"):
                opp_val = getattr(value, "miniJava_Minus", None)
                setattr(value, "miniJava_Minus", self)

    @property
    def miniJava_Expression51(self):
        return self.__miniJava_Expression51

    @miniJava_Expression51.setter
    def miniJava_Expression51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression51", None)
        self.__miniJava_Expression51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Assignment50"):
                opp_val = getattr(old_value, "miniJava_Assignment50", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Assignment50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Assignment50"):
                opp_val = getattr(value, "miniJava_Assignment50", None)
                setattr(value, "miniJava_Assignment50", self)

    @property
    def miniJava_Expression(self):
        return self.__miniJava_Expression

    @miniJava_Expression.setter
    def miniJava_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression", None)
        self.__miniJava_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Field"):
                opp_val = getattr(old_value, "miniJava_Field", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Field"):
                opp_val = getattr(value, "miniJava_Field", None)
                setattr(value, "miniJava_Field", self)

    @property
    def miniJava_Expression77(self):
        return self.__miniJava_Expression77

    @miniJava_Expression77.setter
    def miniJava_Expression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression77", None)
        self.__miniJava_Expression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_SuperiorOrEqual76"):
                opp_val = getattr(old_value, "miniJava_SuperiorOrEqual76", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_SuperiorOrEqual76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_SuperiorOrEqual76"):
                opp_val = getattr(value, "miniJava_SuperiorOrEqual76", None)
                setattr(value, "miniJava_SuperiorOrEqual76", self)

    @property
    def miniJava_Expression20(self):
        return self.__miniJava_Expression20

    @miniJava_Expression20.setter
    def miniJava_Expression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression20", None)
        self.__miniJava_Expression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Return"):
                opp_val = getattr(old_value, "miniJava_Return", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Return", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Return"):
                opp_val = getattr(value, "miniJava_Return", None)
                setattr(value, "miniJava_Return", self)

    @property
    def miniJava_Expression136(self):
        return self.__miniJava_Expression136

    @miniJava_Expression136.setter
    def miniJava_Expression136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression136", None)
        self.__miniJava_Expression136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall135"):
                opp_val = getattr(old_value, "miniJava_MethodCall135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall135"):
                opp_val = getattr(value, "miniJava_MethodCall135", None)
                if opp_val is None:
                    setattr(value, "miniJava_MethodCall135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_Expression114(self):
        return self.__miniJava_Expression114

    @miniJava_Expression114.setter
    def miniJava_Expression114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression114", None)
        self.__miniJava_Expression114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayAccess"):
                opp_val = getattr(old_value, "miniJava_ArrayAccess", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayAccess"):
                opp_val = getattr(value, "miniJava_ArrayAccess", None)
                setattr(value, "miniJava_ArrayAccess", self)

    @property
    def miniJava_Expression123(self):
        return self.__miniJava_Expression123

    @miniJava_Expression123.setter
    def miniJava_Expression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression123", None)
        self.__miniJava_Expression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Neg"):
                opp_val = getattr(old_value, "miniJava_Neg", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Neg", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Neg"):
                opp_val = getattr(value, "miniJava_Neg", None)
                setattr(value, "miniJava_Neg", self)

    @property
    def miniJava_Expression54(self):
        return self.__miniJava_Expression54

    @miniJava_Expression54.setter
    def miniJava_Expression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression54", None)
        self.__miniJava_Expression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Or"):
                opp_val = getattr(old_value, "miniJava_Or", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Or", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Or"):
                opp_val = getattr(value, "miniJava_Or", None)
                setattr(value, "miniJava_Or", self)

    @property
    def miniJava_Expression130(self):
        return self.__miniJava_Expression130

    @miniJava_Expression130.setter
    def miniJava_Expression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression130", None)
        self.__miniJava_Expression130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall"):
                opp_val = getattr(old_value, "miniJava_MethodCall", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall"):
                opp_val = getattr(value, "miniJava_MethodCall", None)
                setattr(value, "miniJava_MethodCall", self)

    @property
    def miniJava_Expression109(self):
        return self.__miniJava_Expression109

    @miniJava_Expression109.setter
    def miniJava_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression109", None)
        self.__miniJava_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Division"):
                opp_val = getattr(old_value, "miniJava_Division", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Division"):
                opp_val = getattr(value, "miniJava_Division", None)
                setattr(value, "miniJava_Division", self)

    @property
    def miniJava_Expression22(self):
        return self.__miniJava_Expression22

    @miniJava_Expression22.setter
    def miniJava_Expression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression22", None)
        self.__miniJava_Expression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_IfStatement"):
                opp_val = getattr(old_value, "miniJava_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_IfStatement"):
                opp_val = getattr(value, "miniJava_IfStatement", None)
                setattr(value, "miniJava_IfStatement", self)

    @property
    def miniJava_Expression57(self):
        return self.__miniJava_Expression57

    @miniJava_Expression57.setter
    def miniJava_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression57", None)
        self.__miniJava_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Or56"):
                opp_val = getattr(old_value, "miniJava_Or56", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Or56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Or56"):
                opp_val = getattr(value, "miniJava_Or56", None)
                setattr(value, "miniJava_Or56", self)

    @property
    def miniJava_Expression112(self):
        return self.__miniJava_Expression112

    @miniJava_Expression112.setter
    def miniJava_Expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression112", None)
        self.__miniJava_Expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Division111"):
                opp_val = getattr(old_value, "miniJava_Division111", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Division111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Division111"):
                opp_val = getattr(value, "miniJava_Division111", None)
                setattr(value, "miniJava_Division111", self)

    @property
    def miniJava_Expression59(self):
        return self.__miniJava_Expression59

    @miniJava_Expression59.setter
    def miniJava_Expression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression59", None)
        self.__miniJava_Expression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_And"):
                opp_val = getattr(old_value, "miniJava_And", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_And"):
                opp_val = getattr(value, "miniJava_And", None)
                setattr(value, "miniJava_And", self)

    @property
    def miniJava_Expression87(self):
        return self.__miniJava_Expression87

    @miniJava_Expression87.setter
    def miniJava_Expression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression87", None)
        self.__miniJava_Expression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Superior86"):
                opp_val = getattr(old_value, "miniJava_Superior86", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Superior86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Superior86"):
                opp_val = getattr(value, "miniJava_Superior86", None)
                setattr(value, "miniJava_Superior86", self)

    @property
    def miniJava_Expression104(self):
        return self.__miniJava_Expression104

    @miniJava_Expression104.setter
    def miniJava_Expression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression104", None)
        self.__miniJava_Expression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Multiplication"):
                opp_val = getattr(old_value, "miniJava_Multiplication", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Multiplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Multiplication"):
                opp_val = getattr(value, "miniJava_Multiplication", None)
                setattr(value, "miniJava_Multiplication", self)

    @property
    def miniJava_Expression82(self):
        return self.__miniJava_Expression82

    @miniJava_Expression82.setter
    def miniJava_Expression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression82", None)
        self.__miniJava_Expression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_InferiorOrEqual81"):
                opp_val = getattr(old_value, "miniJava_InferiorOrEqual81", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_InferiorOrEqual81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_InferiorOrEqual81"):
                opp_val = getattr(value, "miniJava_InferiorOrEqual81", None)
                setattr(value, "miniJava_InferiorOrEqual81", self)

    @property
    def miniJava_Expression97(self):
        return self.__miniJava_Expression97

    @miniJava_Expression97.setter
    def miniJava_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression97", None)
        self.__miniJava_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Plus96"):
                opp_val = getattr(old_value, "miniJava_Plus96", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Plus96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Plus96"):
                opp_val = getattr(value, "miniJava_Plus96", None)
                setattr(value, "miniJava_Plus96", self)

    @property
    def miniJava_Expression92(self):
        return self.__miniJava_Expression92

    @miniJava_Expression92.setter
    def miniJava_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression92", None)
        self.__miniJava_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Inferior91"):
                opp_val = getattr(old_value, "miniJava_Inferior91", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Inferior91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Inferior91"):
                opp_val = getattr(value, "miniJava_Inferior91", None)
                setattr(value, "miniJava_Inferior91", self)

    @property
    def miniJava_Expression64(self):
        return self.__miniJava_Expression64

    @miniJava_Expression64.setter
    def miniJava_Expression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression64", None)
        self.__miniJava_Expression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Equality"):
                opp_val = getattr(old_value, "miniJava_Equality", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Equality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Equality"):
                opp_val = getattr(value, "miniJava_Equality", None)
                setattr(value, "miniJava_Equality", self)

    @property
    def miniJava_Expression72(self):
        return self.__miniJava_Expression72

    @miniJava_Expression72.setter
    def miniJava_Expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression72", None)
        self.__miniJava_Expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Inequality71"):
                opp_val = getattr(old_value, "miniJava_Inequality71", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Inequality71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Inequality71"):
                opp_val = getattr(value, "miniJava_Inequality71", None)
                setattr(value, "miniJava_Inequality71", self)

    @property
    def miniJava_Expression119(self):
        return self.__miniJava_Expression119

    @miniJava_Expression119.setter
    def miniJava_Expression119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression119", None)
        self.__miniJava_Expression119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayLength"):
                opp_val = getattr(old_value, "miniJava_ArrayLength", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayLength", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayLength"):
                opp_val = getattr(value, "miniJava_ArrayLength", None)
                setattr(value, "miniJava_ArrayLength", self)

    @property
    def miniJava_Expression67(self):
        return self.__miniJava_Expression67

    @miniJava_Expression67.setter
    def miniJava_Expression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression67", None)
        self.__miniJava_Expression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Equality66"):
                opp_val = getattr(old_value, "miniJava_Equality66", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Equality66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Equality66"):
                opp_val = getattr(value, "miniJava_Equality66", None)
                setattr(value, "miniJava_Equality66", self)

    @property
    def miniJava_Expression146(self):
        return self.__miniJava_Expression146

    @miniJava_Expression146.setter
    def miniJava_Expression146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression146", None)
        self.__miniJava_Expression146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NewArray145"):
                opp_val = getattr(old_value, "miniJava_NewArray145", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_NewArray145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NewArray145"):
                opp_val = getattr(value, "miniJava_NewArray145", None)
                setattr(value, "miniJava_NewArray145", self)

    @property
    def miniJava_Expression84(self):
        return self.__miniJava_Expression84

    @miniJava_Expression84.setter
    def miniJava_Expression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression84", None)
        self.__miniJava_Expression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Superior"):
                opp_val = getattr(old_value, "miniJava_Superior", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Superior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Superior"):
                opp_val = getattr(value, "miniJava_Superior", None)
                setattr(value, "miniJava_Superior", self)

    @property
    def miniJava_Expression79(self):
        return self.__miniJava_Expression79

    @miniJava_Expression79.setter
    def miniJava_Expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression79", None)
        self.__miniJava_Expression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_InferiorOrEqual"):
                opp_val = getattr(old_value, "miniJava_InferiorOrEqual", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_InferiorOrEqual", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_InferiorOrEqual"):
                opp_val = getattr(value, "miniJava_InferiorOrEqual", None)
                setattr(value, "miniJava_InferiorOrEqual", self)

    @property
    def miniJava_Expression125(self):
        return self.__miniJava_Expression125

    @miniJava_Expression125.setter
    def miniJava_Expression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression125", None)
        self.__miniJava_Expression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_FieldAccess"):
                opp_val = getattr(old_value, "miniJava_FieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_FieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_FieldAccess"):
                opp_val = getattr(value, "miniJava_FieldAccess", None)
                setattr(value, "miniJava_FieldAccess", self)

    @property
    def miniJava_Expression94(self):
        return self.__miniJava_Expression94

    @miniJava_Expression94.setter
    def miniJava_Expression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression94", None)
        self.__miniJava_Expression94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Plus"):
                opp_val = getattr(old_value, "miniJava_Plus", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Plus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Plus"):
                opp_val = getattr(value, "miniJava_Plus", None)
                setattr(value, "miniJava_Plus", self)

    @property
    def miniJava_Expression62(self):
        return self.__miniJava_Expression62

    @miniJava_Expression62.setter
    def miniJava_Expression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expression__miniJava_Expression62", None)
        self.__miniJava_Expression62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_And61"):
                opp_val = getattr(old_value, "miniJava_And61", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_And61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_And61"):
                opp_val = getattr(value, "miniJava_And61", None)
                setattr(value, "miniJava_And61", self)

    def evaluateExpression(self, state: str) -> str:
        # TODO: Implement evaluateExpression method
        pass

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class Symbol:

    pass
class miniJava_VariableDeclaration(Assignee, Symbol):

    pass
class miniJava_Block(Statement):

    def __init__(self, miniJava_Block: "miniJava_Method" = None, miniJava_Block25: "miniJava_IfStatement" = None, miniJava_Block28: "miniJava_IfStatement" = None, miniJava_Block33: "miniJava_WhileStatement" = None, miniJava_Block16: set["miniJava_Statement"] = None, miniJava_Block43: "miniJava_ForStatement" = None):
        self.miniJava_Block = miniJava_Block
        self.miniJava_Block25 = miniJava_Block25
        self.miniJava_Block28 = miniJava_Block28
        self.miniJava_Block33 = miniJava_Block33
        self.miniJava_Block16 = miniJava_Block16 if miniJava_Block16 is not None else set()
        self.miniJava_Block43 = miniJava_Block43
        
    @property
    def miniJava_Block16(self):
        return self.__miniJava_Block16

    @miniJava_Block16.setter
    def miniJava_Block16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Block__miniJava_Block16", None)
        self.__miniJava_Block16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Statement"):
                    opp_val = getattr(item, "miniJava_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Statement"):
                    opp_val = getattr(item, "miniJava_Statement", None)
                    
                    setattr(item, "miniJava_Statement", self)
                    

    @property
    def miniJava_Block43(self):
        return self.__miniJava_Block43

    @miniJava_Block43.setter
    def miniJava_Block43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Block__miniJava_Block43", None)
        self.__miniJava_Block43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ForStatement42"):
                opp_val = getattr(old_value, "miniJava_ForStatement42", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ForStatement42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ForStatement42"):
                opp_val = getattr(value, "miniJava_ForStatement42", None)
                setattr(value, "miniJava_ForStatement42", self)

    @property
    def miniJava_Block33(self):
        return self.__miniJava_Block33

    @miniJava_Block33.setter
    def miniJava_Block33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Block__miniJava_Block33", None)
        self.__miniJava_Block33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_WhileStatement32"):
                opp_val = getattr(old_value, "miniJava_WhileStatement32", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_WhileStatement32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_WhileStatement32"):
                opp_val = getattr(value, "miniJava_WhileStatement32", None)
                setattr(value, "miniJava_WhileStatement32", self)

    @property
    def miniJava_Block25(self):
        return self.__miniJava_Block25

    @miniJava_Block25.setter
    def miniJava_Block25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Block__miniJava_Block25", None)
        self.__miniJava_Block25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_IfStatement24"):
                opp_val = getattr(old_value, "miniJava_IfStatement24", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_IfStatement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_IfStatement24"):
                opp_val = getattr(value, "miniJava_IfStatement24", None)
                setattr(value, "miniJava_IfStatement24", self)

    @property
    def miniJava_Block28(self):
        return self.__miniJava_Block28

    @miniJava_Block28.setter
    def miniJava_Block28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Block__miniJava_Block28", None)
        self.__miniJava_Block28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_IfStatement27"):
                opp_val = getattr(old_value, "miniJava_IfStatement27", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_IfStatement27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_IfStatement27"):
                opp_val = getattr(value, "miniJava_IfStatement27", None)
                setattr(value, "miniJava_IfStatement27", self)

    @property
    def miniJava_Block(self):
        return self.__miniJava_Block

    @miniJava_Block.setter
    def miniJava_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Block__miniJava_Block", None)
        self.__miniJava_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method13"):
                opp_val = getattr(old_value, "miniJava_Method13", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Method13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method13"):
                opp_val = getattr(value, "miniJava_Method13", None)
                setattr(value, "miniJava_Method13", self)

    def evaluateStatementKeepContext(self, state: str):
        # TODO: Implement evaluateStatementKeepContext method
        pass

    def evaluateStatement(self, state: str):
        # TODO: Implement evaluateStatement method
        pass

class miniJava_Parameter(Symbol):

    def __init__(self, miniJava_Parameter: "miniJava_Method" = None):
        self.miniJava_Parameter = miniJava_Parameter
        
    @property
    def miniJava_Parameter(self):
        return self.__miniJava_Parameter

    @miniJava_Parameter.setter
    def miniJava_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Parameter__miniJava_Parameter", None)
        self.__miniJava_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method"):
                opp_val = getattr(old_value, "miniJava_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method"):
                opp_val = getattr(value, "miniJava_Method", None)
                if opp_val is None:
                    setattr(value, "miniJava_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def compare(self, other: str):
        # TODO: Implement compare method
        pass

class Member:

    pass
class miniJava_Field(Member):

    pass
class miniJava_Method(Member):

    def __init__(self, abstract: bool, static: bool, miniJava_Method: set["miniJava_Parameter"] = None, miniJava_Method13: "miniJava_Block" = None, miniJava_Method133: "miniJava_MethodCall" = None):
        self.abstract = abstract
        self.static = static
        self.miniJava_Method = miniJava_Method if miniJava_Method is not None else set()
        self.miniJava_Method13 = miniJava_Method13
        self.miniJava_Method133 = miniJava_Method133
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def miniJava_Method(self):
        return self.__miniJava_Method

    @miniJava_Method.setter
    def miniJava_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method", None)
        self.__miniJava_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Parameter"):
                    opp_val = getattr(item, "miniJava_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Parameter"):
                    opp_val = getattr(item, "miniJava_Parameter", None)
                    
                    setattr(item, "miniJava_Parameter", self)
                    

    @property
    def miniJava_Method13(self):
        return self.__miniJava_Method13

    @miniJava_Method13.setter
    def miniJava_Method13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method13", None)
        self.__miniJava_Method13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block"):
                opp_val = getattr(old_value, "miniJava_Block", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block"):
                opp_val = getattr(value, "miniJava_Block", None)
                setattr(value, "miniJava_Block", self)

    @property
    def miniJava_Method133(self):
        return self.__miniJava_Method133

    @miniJava_Method133.setter
    def miniJava_Method133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method133", None)
        self.__miniJava_Method133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall132"):
                opp_val = getattr(old_value, "miniJava_MethodCall132", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall132"):
                opp_val = getattr(value, "miniJava_MethodCall132", None)
                setattr(value, "miniJava_MethodCall132", self)

    def call(self, state: str):
        # TODO: Implement call method
        pass

    def findOverride(self, c: str) -> str:
        # TODO: Implement findOverride method
        pass

class TypedDeclaration:

    pass
class miniJava_Symbol(TypedDeclaration):

    pass
class miniJava_Member(TypedDeclaration):

    def __init__(self, access: str, miniJava_Member: "miniJava_TypeDeclaration" = None):
        self.access = access
        self.miniJava_Member = miniJava_Member
        
    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def miniJava_Member(self):
        return self.__miniJava_Member

    @miniJava_Member.setter
    def miniJava_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Member__miniJava_Member", None)
        self.__miniJava_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_TypeDeclaration8"):
                opp_val = getattr(old_value, "miniJava_TypeDeclaration8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_TypeDeclaration8"):
                opp_val = getattr(value, "miniJava_TypeDeclaration8", None)
                if opp_val is None:
                    setattr(value, "miniJava_TypeDeclaration8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_Import:

    def __init__(self, importedNamespace: str, miniJava_Import: "miniJava_Program" = None):
        self.importedNamespace = importedNamespace
        self.miniJava_Import = miniJava_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def miniJava_Import(self):
        return self.__miniJava_Import

    @miniJava_Import.setter
    def miniJava_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Import__miniJava_Import", None)
        self.__miniJava_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Program"):
                opp_val = getattr(old_value, "miniJava_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Program"):
                opp_val = getattr(value, "miniJava_Program", None)
                if opp_val is None:
                    setattr(value, "miniJava_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_Program:

    def __init__(self, name: str, miniJava_Program2: set["miniJava_TypeDeclaration"] = None, miniJava_Program4: "miniJava_State" = None, miniJava_Program: set["miniJava_Import"] = None):
        self.name = name
        self.miniJava_Program2 = miniJava_Program2 if miniJava_Program2 is not None else set()
        self.miniJava_Program4 = miniJava_Program4
        self.miniJava_Program = miniJava_Program if miniJava_Program is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniJava_Program(self):
        return self.__miniJava_Program

    @miniJava_Program.setter
    def miniJava_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Program__miniJava_Program", None)
        self.__miniJava_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Import"):
                    opp_val = getattr(item, "miniJava_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Import"):
                    opp_val = getattr(item, "miniJava_Import", None)
                    
                    setattr(item, "miniJava_Import", self)
                    

    @property
    def miniJava_Program4(self):
        return self.__miniJava_Program4

    @miniJava_Program4.setter
    def miniJava_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Program__miniJava_Program4", None)
        self.__miniJava_Program4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State"):
                opp_val = getattr(old_value, "miniJava_State", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State"):
                opp_val = getattr(value, "miniJava_State", None)
                setattr(value, "miniJava_State", self)

    @property
    def miniJava_Program2(self):
        return self.__miniJava_Program2

    @miniJava_Program2.setter
    def miniJava_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Program__miniJava_Program2", None)
        self.__miniJava_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_TypeDeclaration"):
                    opp_val = getattr(item, "miniJava_TypeDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_TypeDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_TypeDeclaration"):
                    opp_val = getattr(item, "miniJava_TypeDeclaration", None)
                    
                    setattr(item, "miniJava_TypeDeclaration", self)
                    

    def main(self):
        # TODO: Implement main method
        pass

    def initialize(self, args: str):
        # TODO: Implement initialize method
        pass

    def execute(self) -> str:
        # TODO: Implement execute method
        pass

class miniJava_State:

    def __init__(self, miniJava_State: "miniJava_Program" = None, miniJava_State171: "miniJava_OutputStream" = None, miniJava_State173: set["miniJava_ArrayInstance"] = None, miniJava_State167: "miniJava_Frame" = None, miniJava_State169: set["miniJava_ObjectInstance"] = None):
        self.miniJava_State = miniJava_State
        self.miniJava_State171 = miniJava_State171
        self.miniJava_State173 = miniJava_State173 if miniJava_State173 is not None else set()
        self.miniJava_State167 = miniJava_State167
        self.miniJava_State169 = miniJava_State169 if miniJava_State169 is not None else set()
        
    @property
    def miniJava_State169(self):
        return self.__miniJava_State169

    @miniJava_State169.setter
    def miniJava_State169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_State__miniJava_State169", None)
        self.__miniJava_State169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_ObjectInstance"):
                    opp_val = getattr(item, "miniJava_ObjectInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_ObjectInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_ObjectInstance"):
                    opp_val = getattr(item, "miniJava_ObjectInstance", None)
                    
                    setattr(item, "miniJava_ObjectInstance", self)
                    

    @property
    def miniJava_State173(self):
        return self.__miniJava_State173

    @miniJava_State173.setter
    def miniJava_State173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_State__miniJava_State173", None)
        self.__miniJava_State173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_ArrayInstance"):
                    opp_val = getattr(item, "miniJava_ArrayInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_ArrayInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_ArrayInstance"):
                    opp_val = getattr(item, "miniJava_ArrayInstance", None)
                    
                    setattr(item, "miniJava_ArrayInstance", self)
                    

    @property
    def miniJava_State167(self):
        return self.__miniJava_State167

    @miniJava_State167.setter
    def miniJava_State167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_State__miniJava_State167", None)
        self.__miniJava_State167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Frame"):
                opp_val = getattr(old_value, "miniJava_Frame", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Frame", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Frame"):
                opp_val = getattr(value, "miniJava_Frame", None)
                setattr(value, "miniJava_Frame", self)

    @property
    def miniJava_State171(self):
        return self.__miniJava_State171

    @miniJava_State171.setter
    def miniJava_State171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_State__miniJava_State171", None)
        self.__miniJava_State171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_OutputStream"):
                opp_val = getattr(old_value, "miniJava_OutputStream", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_OutputStream", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_OutputStream"):
                opp_val = getattr(value, "miniJava_OutputStream", None)
                setattr(value, "miniJava_OutputStream", self)

    @property
    def miniJava_State(self):
        return self.__miniJava_State

    @miniJava_State.setter
    def miniJava_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_State__miniJava_State", None)
        self.__miniJava_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Program4"):
                opp_val = getattr(old_value, "miniJava_Program4", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Program4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Program4"):
                opp_val = getattr(value, "miniJava_Program4", None)
                setattr(value, "miniJava_Program4", self)

    def pushNewFrame(self, newContext: str, c: str, receiver: str):
        # TODO: Implement pushNewFrame method
        pass

    def println(self, string: str):
        # TODO: Implement println method
        pass

    def popCurrentContext(self):
        # TODO: Implement popCurrentContext method
        pass

    def findCurrentFrame(self) -> str:
        # TODO: Implement findCurrentFrame method
        pass

    def popCurrentFrame(self):
        # TODO: Implement popCurrentFrame method
        pass

    def findCurrentContext(self) -> str:
        # TODO: Implement findCurrentContext method
        pass

    def pushNewContext(self):
        # TODO: Implement pushNewContext method
        pass

class miniJava_TypeDeclaration(NamedElement):

    def __init__(self, accessLevel: str, miniJava_TypeDeclaration: "miniJava_Program" = None, miniJava_TypeDeclaration6: set["miniJava_Interface"] = None, miniJava_TypeDeclaration8: set["miniJava_Member"] = None, miniJava_TypeDeclaration45: "miniJava_ClassRef" = None):
        self.accessLevel = accessLevel
        self.miniJava_TypeDeclaration = miniJava_TypeDeclaration
        self.miniJava_TypeDeclaration6 = miniJava_TypeDeclaration6 if miniJava_TypeDeclaration6 is not None else set()
        self.miniJava_TypeDeclaration8 = miniJava_TypeDeclaration8 if miniJava_TypeDeclaration8 is not None else set()
        self.miniJava_TypeDeclaration45 = miniJava_TypeDeclaration45
        
    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def miniJava_TypeDeclaration(self):
        return self.__miniJava_TypeDeclaration

    @miniJava_TypeDeclaration.setter
    def miniJava_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration", None)
        self.__miniJava_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Program2"):
                opp_val = getattr(old_value, "miniJava_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Program2"):
                opp_val = getattr(value, "miniJava_Program2", None)
                if opp_val is None:
                    setattr(value, "miniJava_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_TypeDeclaration45(self):
        return self.__miniJava_TypeDeclaration45

    @miniJava_TypeDeclaration45.setter
    def miniJava_TypeDeclaration45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration45", None)
        self.__miniJava_TypeDeclaration45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassRef"):
                opp_val = getattr(old_value, "miniJava_ClassRef", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassRef"):
                opp_val = getattr(value, "miniJava_ClassRef", None)
                setattr(value, "miniJava_ClassRef", self)

    @property
    def miniJava_TypeDeclaration6(self):
        return self.__miniJava_TypeDeclaration6

    @miniJava_TypeDeclaration6.setter
    def miniJava_TypeDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration6", None)
        self.__miniJava_TypeDeclaration6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Interface"):
                    opp_val = getattr(item, "miniJava_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Interface"):
                    opp_val = getattr(item, "miniJava_Interface", None)
                    
                    setattr(item, "miniJava_Interface", self)
                    

    @property
    def miniJava_TypeDeclaration8(self):
        return self.__miniJava_TypeDeclaration8

    @miniJava_TypeDeclaration8.setter
    def miniJava_TypeDeclaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration8", None)
        self.__miniJava_TypeDeclaration8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Member"):
                    opp_val = getattr(item, "miniJava_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Member"):
                    opp_val = getattr(item, "miniJava_Member", None)
                    
                    setattr(item, "miniJava_Member", self)
                    
