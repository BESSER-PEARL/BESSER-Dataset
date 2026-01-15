from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class JavaParameterKind(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
    RETURN = "RETURN"
class JavaVisibilityKind(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PACKAGE = "PACKAGE"
class JavaKind(Enum):
    CLASS = "CLASS"
    INTERFACE = "INTERFACE"
    EXCEPTION = "EXCEPTION"


############################################
# Definition of Classes
############################################

class javaz_JavaElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class javaz_Block:

    def __init__(self, content: str, javaz_Block: "javaz_Method" = None):
        self.content = content
        self.javaz_Block = javaz_Block
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def javaz_Block(self):
        return self.__javaz_Block

    @javaz_Block.setter
    def javaz_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_Block__javaz_Block", None)
        self.__javaz_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_Method22"):
                opp_val = getattr(old_value, "javaz_Method22", None)
                if opp_val == self:
                    setattr(old_value, "javaz_Method22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_Method22"):
                opp_val = getattr(value, "javaz_Method22", None)
                setattr(value, "javaz_Method22", self)

class JavaElement:

    pass
class javaz_Method(JavaElement):

    def __init__(self, visibility: str, final: bool, static: bool, synchronized: bool, constructor: bool, native: bool, abstract: bool, javaz_Method: "javaz_JavaClass" = None, javaz_Method20: set["javaz_JavaParameter"] = None, javaz_Method22: "javaz_Block" = None):
        self.visibility = visibility
        self.final = final
        self.static = static
        self.synchronized = synchronized
        self.constructor = constructor
        self.native = native
        self.abstract = abstract
        self.javaz_Method = javaz_Method
        self.javaz_Method20 = javaz_Method20 if javaz_Method20 is not None else set()
        self.javaz_Method22 = javaz_Method22
        
    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

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
    def constructor(self) -> bool:
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: bool):
        self.__constructor = constructor

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def javaz_Method(self):
        return self.__javaz_Method

    @javaz_Method.setter
    def javaz_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_Method__javaz_Method", None)
        self.__javaz_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass4"):
                opp_val = getattr(old_value, "javaz_JavaClass4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass4"):
                opp_val = getattr(value, "javaz_JavaClass4", None)
                if opp_val is None:
                    setattr(value, "javaz_JavaClass4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaz_Method20(self):
        return self.__javaz_Method20

    @javaz_Method20.setter
    def javaz_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_Method__javaz_Method20", None)
        self.__javaz_Method20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaz_JavaParameter"):
                    opp_val = getattr(item, "javaz_JavaParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "javaz_JavaParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaz_JavaParameter"):
                    opp_val = getattr(item, "javaz_JavaParameter", None)
                    
                    setattr(item, "javaz_JavaParameter", self)
                    

    @property
    def javaz_Method22(self):
        return self.__javaz_Method22

    @javaz_Method22.setter
    def javaz_Method22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_Method__javaz_Method22", None)
        self.__javaz_Method22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_Block"):
                opp_val = getattr(old_value, "javaz_Block", None)
                if opp_val == self:
                    setattr(old_value, "javaz_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_Block"):
                opp_val = getattr(value, "javaz_Block", None)
                setattr(value, "javaz_Block", self)

class javaz_JavaParameter(JavaElement):

    def __init__(self, final: bool, parameterKind: str, type: str, kind: str, javaz_JavaParameter: "javaz_Method" = None):
        self.final = final
        self.parameterKind = parameterKind
        self.type = type
        self.kind = kind
        self.javaz_JavaParameter = javaz_JavaParameter
        
    @property
    def parameterKind(self) -> str:
        return self.__parameterKind

    @parameterKind.setter
    def parameterKind(self, parameterKind: str):
        self.__parameterKind = parameterKind

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def javaz_JavaParameter(self):
        return self.__javaz_JavaParameter

    @javaz_JavaParameter.setter
    def javaz_JavaParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaParameter__javaz_JavaParameter", None)
        self.__javaz_JavaParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_Method20"):
                opp_val = getattr(old_value, "javaz_Method20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_Method20"):
                opp_val = getattr(value, "javaz_Method20", None)
                if opp_val is None:
                    setattr(value, "javaz_Method20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaz_Field(JavaElement):

    def __init__(self, type: str, visibility: str, static: bool, transient: bool, volatile: bool, final: bool, javaz_Field: "javaz_JavaClass" = None):
        self.type = type
        self.visibility = visibility
        self.static = static
        self.transient = transient
        self.volatile = volatile
        self.final = final
        self.javaz_Field = javaz_Field
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def javaz_Field(self):
        return self.__javaz_Field

    @javaz_Field.setter
    def javaz_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_Field__javaz_Field", None)
        self.__javaz_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass6"):
                opp_val = getattr(old_value, "javaz_JavaClass6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass6"):
                opp_val = getattr(value, "javaz_JavaClass6", None)
                if opp_val is None:
                    setattr(value, "javaz_JavaClass6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaz_JavaClass(JavaElement):

    def __init__(self, kind: str, public: bool, final: bool, rewritable: bool, needToGenerate: bool, javaz_JavaClass9: "javaz_JavaClass" = None, javaz_JavaClass7: set["javaz_JavaClass"] = None, javaz_JavaClass11: "javaz_JavaPackageX" = None, javaz_JavaClass15: "javaz_JavaClass" = None, javaz_JavaClass13: "javaz_JavaClass" = None, javaz_JavaClass18: "javaz_JavaClass" = None, javaz_JavaClass16: set["javaz_JavaClass"] = None, javaz_JavaClass: "javaz_Javaz" = None, javaz_JavaClass4: set["javaz_Method"] = None, javaz_JavaClass6: set["javaz_Field"] = None):
        self.kind = kind
        self.public = public
        self.final = final
        self.rewritable = rewritable
        self.needToGenerate = needToGenerate
        self.javaz_JavaClass9 = javaz_JavaClass9
        self.javaz_JavaClass7 = javaz_JavaClass7 if javaz_JavaClass7 is not None else set()
        self.javaz_JavaClass11 = javaz_JavaClass11
        self.javaz_JavaClass15 = javaz_JavaClass15
        self.javaz_JavaClass13 = javaz_JavaClass13
        self.javaz_JavaClass18 = javaz_JavaClass18
        self.javaz_JavaClass16 = javaz_JavaClass16 if javaz_JavaClass16 is not None else set()
        self.javaz_JavaClass = javaz_JavaClass
        self.javaz_JavaClass4 = javaz_JavaClass4 if javaz_JavaClass4 is not None else set()
        self.javaz_JavaClass6 = javaz_JavaClass6 if javaz_JavaClass6 is not None else set()
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def needToGenerate(self) -> bool:
        return self.__needToGenerate

    @needToGenerate.setter
    def needToGenerate(self, needToGenerate: bool):
        self.__needToGenerate = needToGenerate

    @property
    def public(self) -> bool:
        return self.__public

    @public.setter
    def public(self, public: bool):
        self.__public = public

    @property
    def rewritable(self) -> bool:
        return self.__rewritable

    @rewritable.setter
    def rewritable(self, rewritable: bool):
        self.__rewritable = rewritable

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def javaz_JavaClass7(self):
        return self.__javaz_JavaClass7

    @javaz_JavaClass7.setter
    def javaz_JavaClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass7", None)
        self.__javaz_JavaClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaz_JavaClass9"):
                    opp_val = getattr(item, "javaz_JavaClass9", None)
                    
                    if opp_val == self:
                        setattr(item, "javaz_JavaClass9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaz_JavaClass9"):
                    opp_val = getattr(item, "javaz_JavaClass9", None)
                    
                    setattr(item, "javaz_JavaClass9", self)
                    

    @property
    def javaz_JavaClass(self):
        return self.__javaz_JavaClass

    @javaz_JavaClass.setter
    def javaz_JavaClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass", None)
        self.__javaz_JavaClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_Javaz2"):
                opp_val = getattr(old_value, "javaz_Javaz2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_Javaz2"):
                opp_val = getattr(value, "javaz_Javaz2", None)
                if opp_val is None:
                    setattr(value, "javaz_Javaz2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaz_JavaClass6(self):
        return self.__javaz_JavaClass6

    @javaz_JavaClass6.setter
    def javaz_JavaClass6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass6", None)
        self.__javaz_JavaClass6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaz_Field"):
                    opp_val = getattr(item, "javaz_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "javaz_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaz_Field"):
                    opp_val = getattr(item, "javaz_Field", None)
                    
                    setattr(item, "javaz_Field", self)
                    

    @property
    def javaz_JavaClass4(self):
        return self.__javaz_JavaClass4

    @javaz_JavaClass4.setter
    def javaz_JavaClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass4", None)
        self.__javaz_JavaClass4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaz_Method"):
                    opp_val = getattr(item, "javaz_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "javaz_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaz_Method"):
                    opp_val = getattr(item, "javaz_Method", None)
                    
                    setattr(item, "javaz_Method", self)
                    

    @property
    def javaz_JavaClass13(self):
        return self.__javaz_JavaClass13

    @javaz_JavaClass13.setter
    def javaz_JavaClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass13", None)
        self.__javaz_JavaClass13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass15"):
                opp_val = getattr(old_value, "javaz_JavaClass15", None)
                if opp_val == self:
                    setattr(old_value, "javaz_JavaClass15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass15"):
                opp_val = getattr(value, "javaz_JavaClass15", None)
                setattr(value, "javaz_JavaClass15", self)

    @property
    def javaz_JavaClass16(self):
        return self.__javaz_JavaClass16

    @javaz_JavaClass16.setter
    def javaz_JavaClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass16", None)
        self.__javaz_JavaClass16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaz_JavaClass18"):
                    opp_val = getattr(item, "javaz_JavaClass18", None)
                    
                    if opp_val == self:
                        setattr(item, "javaz_JavaClass18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaz_JavaClass18"):
                    opp_val = getattr(item, "javaz_JavaClass18", None)
                    
                    setattr(item, "javaz_JavaClass18", self)
                    

    @property
    def javaz_JavaClass11(self):
        return self.__javaz_JavaClass11

    @javaz_JavaClass11.setter
    def javaz_JavaClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass11", None)
        self.__javaz_JavaClass11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaPackageX12"):
                opp_val = getattr(old_value, "javaz_JavaPackageX12", None)
                if opp_val == self:
                    setattr(old_value, "javaz_JavaPackageX12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaPackageX12"):
                opp_val = getattr(value, "javaz_JavaPackageX12", None)
                setattr(value, "javaz_JavaPackageX12", self)

    @property
    def javaz_JavaClass9(self):
        return self.__javaz_JavaClass9

    @javaz_JavaClass9.setter
    def javaz_JavaClass9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass9", None)
        self.__javaz_JavaClass9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass7"):
                opp_val = getattr(old_value, "javaz_JavaClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass7"):
                opp_val = getattr(value, "javaz_JavaClass7", None)
                if opp_val is None:
                    setattr(value, "javaz_JavaClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaz_JavaClass18(self):
        return self.__javaz_JavaClass18

    @javaz_JavaClass18.setter
    def javaz_JavaClass18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass18", None)
        self.__javaz_JavaClass18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass16"):
                opp_val = getattr(old_value, "javaz_JavaClass16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass16"):
                opp_val = getattr(value, "javaz_JavaClass16", None)
                if opp_val is None:
                    setattr(value, "javaz_JavaClass16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaz_JavaClass15(self):
        return self.__javaz_JavaClass15

    @javaz_JavaClass15.setter
    def javaz_JavaClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaClass__javaz_JavaClass15", None)
        self.__javaz_JavaClass15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass13"):
                opp_val = getattr(old_value, "javaz_JavaClass13", None)
                if opp_val == self:
                    setattr(old_value, "javaz_JavaClass13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass13"):
                opp_val = getattr(value, "javaz_JavaClass13", None)
                setattr(value, "javaz_JavaClass13", self)

class javaz_JavaPackageX(JavaElement):

    def __init__(self, needToGenerate: bool, javaz_JavaPackageX12: "javaz_JavaClass" = None, javaz_JavaPackageX: "javaz_Javaz" = None):
        self.needToGenerate = needToGenerate
        self.javaz_JavaPackageX12 = javaz_JavaPackageX12
        self.javaz_JavaPackageX = javaz_JavaPackageX
        
    @property
    def needToGenerate(self) -> bool:
        return self.__needToGenerate

    @needToGenerate.setter
    def needToGenerate(self, needToGenerate: bool):
        self.__needToGenerate = needToGenerate

    @property
    def javaz_JavaPackageX12(self):
        return self.__javaz_JavaPackageX12

    @javaz_JavaPackageX12.setter
    def javaz_JavaPackageX12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaPackageX__javaz_JavaPackageX12", None)
        self.__javaz_JavaPackageX12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_JavaClass11"):
                opp_val = getattr(old_value, "javaz_JavaClass11", None)
                if opp_val == self:
                    setattr(old_value, "javaz_JavaClass11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_JavaClass11"):
                opp_val = getattr(value, "javaz_JavaClass11", None)
                setattr(value, "javaz_JavaClass11", self)

    @property
    def javaz_JavaPackageX(self):
        return self.__javaz_JavaPackageX

    @javaz_JavaPackageX.setter
    def javaz_JavaPackageX(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaz_JavaPackageX__javaz_JavaPackageX", None)
        self.__javaz_JavaPackageX = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaz_Javaz"):
                opp_val = getattr(old_value, "javaz_Javaz", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaz_Javaz"):
                opp_val = getattr(value, "javaz_Javaz", None)
                if opp_val is None:
                    setattr(value, "javaz_Javaz", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaz_Javaz(JavaElement):

    pass