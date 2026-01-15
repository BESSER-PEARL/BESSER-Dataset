from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Component:

    pass
class UnifiedMetamodel__Front(Component):

    pass
class UnifiedMetamodel__Back(Component):

    pass
class SubLayerSegment:

    pass
class UnifiedMetamodel__Actions(SubLayerSegment):

    pass
class UnifiedMetamodel__Reducers(SubLayerSegment):

    pass
class UnifiedMetamodel__Descriptor:

    def __init__(self, name: str, path: str, UnifiedMetamodel__Descriptor: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__Descriptor158: "UnifiedMetamodel__Subproject" = None):
        self.name = name
        self.path = path
        self.UnifiedMetamodel__Descriptor = UnifiedMetamodel__Descriptor
        self.UnifiedMetamodel__Descriptor158 = UnifiedMetamodel__Descriptor158
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def UnifiedMetamodel__Descriptor158(self):
        return self.__UnifiedMetamodel__Descriptor158

    @UnifiedMetamodel__Descriptor158.setter
    def UnifiedMetamodel__Descriptor158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Descriptor__UnifiedMetamodel__Descriptor158", None)
        self.__UnifiedMetamodel__Descriptor158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Subproject157"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Subproject157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Subproject157"):
                opp_val = getattr(value, "UnifiedMetamodel__Subproject157", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Subproject157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Descriptor(self):
        return self.__UnifiedMetamodel__Descriptor

    @UnifiedMetamodel__Descriptor.setter
    def UnifiedMetamodel__Descriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Descriptor__UnifiedMetamodel__Descriptor", None)
        self.__UnifiedMetamodel__Descriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Annotation155"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation155", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation155"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation155", None)
                setattr(value, "UnifiedMetamodel__Annotation155", self)

class UnifiedMetamodel__MethodBack:

    def __init__(self, name: str, UnifiedMetamodel__MethodBack135: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__MethodBack138: set["UnifiedMetamodel__EClass"] = None, UnifiedMetamodel__MethodBack: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__MethodBack150: "UnifiedMetamodel__EClass" = None):
        self.name = name
        self.UnifiedMetamodel__MethodBack135 = UnifiedMetamodel__MethodBack135
        self.UnifiedMetamodel__MethodBack138 = UnifiedMetamodel__MethodBack138 if UnifiedMetamodel__MethodBack138 is not None else set()
        self.UnifiedMetamodel__MethodBack = UnifiedMetamodel__MethodBack
        self.UnifiedMetamodel__MethodBack150 = UnifiedMetamodel__MethodBack150
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__MethodBack150(self):
        return self.__UnifiedMetamodel__MethodBack150

    @UnifiedMetamodel__MethodBack150.setter
    def UnifiedMetamodel__MethodBack150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack150", None)
        self.__UnifiedMetamodel__MethodBack150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass149"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass149"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass149", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__EClass149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__MethodBack138(self):
        return self.__UnifiedMetamodel__MethodBack138

    @UnifiedMetamodel__MethodBack138.setter
    def UnifiedMetamodel__MethodBack138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack138", None)
        self.__UnifiedMetamodel__MethodBack138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__EClass139"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass139", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__EClass139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__EClass139"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass139", None)
                    
                    setattr(item, "UnifiedMetamodel__EClass139", self)
                    

    @property
    def UnifiedMetamodel__MethodBack(self):
        return self.__UnifiedMetamodel__MethodBack

    @UnifiedMetamodel__MethodBack.setter
    def UnifiedMetamodel__MethodBack(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack", None)
        self.__UnifiedMetamodel__MethodBack = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Annotation133"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation133", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation133"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation133", None)
                setattr(value, "UnifiedMetamodel__Annotation133", self)

    @property
    def UnifiedMetamodel__MethodBack135(self):
        return self.__UnifiedMetamodel__MethodBack135

    @UnifiedMetamodel__MethodBack135.setter
    def UnifiedMetamodel__MethodBack135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack135", None)
        self.__UnifiedMetamodel__MethodBack135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass136"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass136", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass136"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass136", None)
                setattr(value, "UnifiedMetamodel__EClass136", self)

class UnifiedMetamodel__Epackage:

    def __init__(self, name: str, UnifiedMetamodel__Epackage: set["UnifiedMetamodel__EClass"] = None, UnifiedMetamodel__Epackage161: "UnifiedMetamodel__Subproject" = None):
        self.name = name
        self.UnifiedMetamodel__Epackage = UnifiedMetamodel__Epackage if UnifiedMetamodel__Epackage is not None else set()
        self.UnifiedMetamodel__Epackage161 = UnifiedMetamodel__Epackage161
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Epackage(self):
        return self.__UnifiedMetamodel__Epackage

    @UnifiedMetamodel__Epackage.setter
    def UnifiedMetamodel__Epackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Epackage__UnifiedMetamodel__Epackage", None)
        self.__UnifiedMetamodel__Epackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__EClass144"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass144", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__EClass144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__EClass144"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass144", None)
                    
                    setattr(item, "UnifiedMetamodel__EClass144", self)
                    

    @property
    def UnifiedMetamodel__Epackage161(self):
        return self.__UnifiedMetamodel__Epackage161

    @UnifiedMetamodel__Epackage161.setter
    def UnifiedMetamodel__Epackage161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Epackage__UnifiedMetamodel__Epackage161", None)
        self.__UnifiedMetamodel__Epackage161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Subproject160"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Subproject160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Subproject160"):
                opp_val = getattr(value, "UnifiedMetamodel__Subproject160", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Subproject160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Library:

    def __init__(self, name: str, isNative: bool, UnifiedMetamodel__Library: set["UnifiedMetamodel__NativeClass"] = None, UnifiedMetamodel__Library123: set["UnifiedMetamodel__Annotation"] = None, UnifiedMetamodel__Library164: "UnifiedMetamodel__Subproject" = None):
        self.name = name
        self.isNative = isNative
        self.UnifiedMetamodel__Library = UnifiedMetamodel__Library if UnifiedMetamodel__Library is not None else set()
        self.UnifiedMetamodel__Library123 = UnifiedMetamodel__Library123 if UnifiedMetamodel__Library123 is not None else set()
        self.UnifiedMetamodel__Library164 = UnifiedMetamodel__Library164
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isNative(self) -> bool:
        return self.__isNative

    @isNative.setter
    def isNative(self, isNative: bool):
        self.__isNative = isNative

    @property
    def UnifiedMetamodel__Library(self):
        return self.__UnifiedMetamodel__Library

    @UnifiedMetamodel__Library.setter
    def UnifiedMetamodel__Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Library__UnifiedMetamodel__Library", None)
        self.__UnifiedMetamodel__Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__NativeClass"):
                    opp_val = getattr(item, "UnifiedMetamodel__NativeClass", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__NativeClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__NativeClass"):
                    opp_val = getattr(item, "UnifiedMetamodel__NativeClass", None)
                    
                    setattr(item, "UnifiedMetamodel__NativeClass", self)
                    

    @property
    def UnifiedMetamodel__Library123(self):
        return self.__UnifiedMetamodel__Library123

    @UnifiedMetamodel__Library123.setter
    def UnifiedMetamodel__Library123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Library__UnifiedMetamodel__Library123", None)
        self.__UnifiedMetamodel__Library123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Annotation"):
                    opp_val = getattr(item, "UnifiedMetamodel__Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Annotation"):
                    opp_val = getattr(item, "UnifiedMetamodel__Annotation", None)
                    
                    setattr(item, "UnifiedMetamodel__Annotation", self)
                    

    @property
    def UnifiedMetamodel__Library164(self):
        return self.__UnifiedMetamodel__Library164

    @UnifiedMetamodel__Library164.setter
    def UnifiedMetamodel__Library164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Library__UnifiedMetamodel__Library164", None)
        self.__UnifiedMetamodel__Library164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Subproject163"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Subproject163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Subproject163"):
                opp_val = getattr(value, "UnifiedMetamodel__Subproject163", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Subproject163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__AbstractMethod:

    def __init__(self, name: str, UnifiedMetamodel__AbstractMethod: "UnifiedMetamodel__EInterface" = None, UnifiedMetamodel__AbstractMethod142: "UnifiedMetamodel__AbstractClass" = None, UnifiedMetamodel__AbstractMethod166: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__AbstractMethod169: set["UnifiedMetamodel__EClass"] = None):
        self.name = name
        self.UnifiedMetamodel__AbstractMethod = UnifiedMetamodel__AbstractMethod
        self.UnifiedMetamodel__AbstractMethod142 = UnifiedMetamodel__AbstractMethod142
        self.UnifiedMetamodel__AbstractMethod166 = UnifiedMetamodel__AbstractMethod166
        self.UnifiedMetamodel__AbstractMethod169 = UnifiedMetamodel__AbstractMethod169 if UnifiedMetamodel__AbstractMethod169 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__AbstractMethod(self):
        return self.__UnifiedMetamodel__AbstractMethod

    @UnifiedMetamodel__AbstractMethod.setter
    def UnifiedMetamodel__AbstractMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod", None)
        self.__UnifiedMetamodel__AbstractMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EInterface"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EInterface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EInterface"):
                opp_val = getattr(value, "UnifiedMetamodel__EInterface", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__EInterface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__AbstractMethod142(self):
        return self.__UnifiedMetamodel__AbstractMethod142

    @UnifiedMetamodel__AbstractMethod142.setter
    def UnifiedMetamodel__AbstractMethod142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod142", None)
        self.__UnifiedMetamodel__AbstractMethod142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__AbstractClass141"):
                opp_val = getattr(old_value, "UnifiedMetamodel__AbstractClass141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__AbstractClass141"):
                opp_val = getattr(value, "UnifiedMetamodel__AbstractClass141", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__AbstractClass141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__AbstractMethod166(self):
        return self.__UnifiedMetamodel__AbstractMethod166

    @UnifiedMetamodel__AbstractMethod166.setter
    def UnifiedMetamodel__AbstractMethod166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod166", None)
        self.__UnifiedMetamodel__AbstractMethod166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass167"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass167", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass167"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass167", None)
                setattr(value, "UnifiedMetamodel__EClass167", self)

    @property
    def UnifiedMetamodel__AbstractMethod169(self):
        return self.__UnifiedMetamodel__AbstractMethod169

    @UnifiedMetamodel__AbstractMethod169.setter
    def UnifiedMetamodel__AbstractMethod169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod169", None)
        self.__UnifiedMetamodel__AbstractMethod169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__EClass170"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass170", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__EClass170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__EClass170"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass170", None)
                    
                    setattr(item, "UnifiedMetamodel__EClass170", self)
                    

class UnifiedMetamodel__EInterface:

    def __init__(self, name: str, UnifiedMetamodel__EInterface: set["UnifiedMetamodel__AbstractMethod"] = None, UnifiedMetamodel__EInterface129: "UnifiedMetamodel__GenericClass" = None):
        self.name = name
        self.UnifiedMetamodel__EInterface = UnifiedMetamodel__EInterface if UnifiedMetamodel__EInterface is not None else set()
        self.UnifiedMetamodel__EInterface129 = UnifiedMetamodel__EInterface129
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__EInterface(self):
        return self.__UnifiedMetamodel__EInterface

    @UnifiedMetamodel__EInterface.setter
    def UnifiedMetamodel__EInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EInterface__UnifiedMetamodel__EInterface", None)
        self.__UnifiedMetamodel__EInterface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__AbstractMethod"):
                    opp_val = getattr(item, "UnifiedMetamodel__AbstractMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__AbstractMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__AbstractMethod"):
                    opp_val = getattr(item, "UnifiedMetamodel__AbstractMethod", None)
                    
                    setattr(item, "UnifiedMetamodel__AbstractMethod", self)
                    

    @property
    def UnifiedMetamodel__EInterface129(self):
        return self.__UnifiedMetamodel__EInterface129

    @UnifiedMetamodel__EInterface129.setter
    def UnifiedMetamodel__EInterface129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EInterface__UnifiedMetamodel__EInterface129", None)
        self.__UnifiedMetamodel__EInterface129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__GenericClass"):
                opp_val = getattr(old_value, "UnifiedMetamodel__GenericClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__GenericClass"):
                opp_val = getattr(value, "UnifiedMetamodel__GenericClass", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__GenericClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EClass:

    pass
class UnifiedMetamodel__AbstractClass(EClass):

    pass
class UnifiedMetamodel__NativeClass(EClass):

    def __init__(self, primitiveRef: str, UnifiedMetamodel__NativeClass: "UnifiedMetamodel__Library" = None):
        self.primitiveRef = primitiveRef
        self.UnifiedMetamodel__NativeClass = UnifiedMetamodel__NativeClass
        
    @property
    def primitiveRef(self) -> str:
        return self.__primitiveRef

    @primitiveRef.setter
    def primitiveRef(self, primitiveRef: str):
        self.__primitiveRef = primitiveRef

    @property
    def UnifiedMetamodel__NativeClass(self):
        return self.__UnifiedMetamodel__NativeClass

    @UnifiedMetamodel__NativeClass.setter
    def UnifiedMetamodel__NativeClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__NativeClass__UnifiedMetamodel__NativeClass", None)
        self.__UnifiedMetamodel__NativeClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Library"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Library"):
                opp_val = getattr(value, "UnifiedMetamodel__Library", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__GenericClass(EClass):

    pass
class UnifiedMetamodel__EClass:

    def __init__(self, name: str, UnifiedMetamodel__EClass: "UnifiedMetamodel__Attribute" = None, UnifiedMetamodel__EClass136: "UnifiedMetamodel__MethodBack" = None, UnifiedMetamodel__EClass139: "UnifiedMetamodel__MethodBack" = None, UnifiedMetamodel__EClass144: "UnifiedMetamodel__Epackage" = None, UnifiedMetamodel__EClass146: set["UnifiedMetamodel__Attribute"] = None, UnifiedMetamodel__EClass149: set["UnifiedMetamodel__MethodBack"] = None, UnifiedMetamodel__EClass152: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__EClass167: "UnifiedMetamodel__AbstractMethod" = None, UnifiedMetamodel__EClass170: "UnifiedMetamodel__AbstractMethod" = None):
        self.name = name
        self.UnifiedMetamodel__EClass = UnifiedMetamodel__EClass
        self.UnifiedMetamodel__EClass136 = UnifiedMetamodel__EClass136
        self.UnifiedMetamodel__EClass139 = UnifiedMetamodel__EClass139
        self.UnifiedMetamodel__EClass144 = UnifiedMetamodel__EClass144
        self.UnifiedMetamodel__EClass146 = UnifiedMetamodel__EClass146 if UnifiedMetamodel__EClass146 is not None else set()
        self.UnifiedMetamodel__EClass149 = UnifiedMetamodel__EClass149 if UnifiedMetamodel__EClass149 is not None else set()
        self.UnifiedMetamodel__EClass152 = UnifiedMetamodel__EClass152
        self.UnifiedMetamodel__EClass167 = UnifiedMetamodel__EClass167
        self.UnifiedMetamodel__EClass170 = UnifiedMetamodel__EClass170
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__EClass167(self):
        return self.__UnifiedMetamodel__EClass167

    @UnifiedMetamodel__EClass167.setter
    def UnifiedMetamodel__EClass167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass167", None)
        self.__UnifiedMetamodel__EClass167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__AbstractMethod166"):
                opp_val = getattr(old_value, "UnifiedMetamodel__AbstractMethod166", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__AbstractMethod166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__AbstractMethod166"):
                opp_val = getattr(value, "UnifiedMetamodel__AbstractMethod166", None)
                setattr(value, "UnifiedMetamodel__AbstractMethod166", self)

    @property
    def UnifiedMetamodel__EClass146(self):
        return self.__UnifiedMetamodel__EClass146

    @UnifiedMetamodel__EClass146.setter
    def UnifiedMetamodel__EClass146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass146", None)
        self.__UnifiedMetamodel__EClass146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Attribute147"):
                    opp_val = getattr(item, "UnifiedMetamodel__Attribute147", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Attribute147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Attribute147"):
                    opp_val = getattr(item, "UnifiedMetamodel__Attribute147", None)
                    
                    setattr(item, "UnifiedMetamodel__Attribute147", self)
                    

    @property
    def UnifiedMetamodel__EClass139(self):
        return self.__UnifiedMetamodel__EClass139

    @UnifiedMetamodel__EClass139.setter
    def UnifiedMetamodel__EClass139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass139", None)
        self.__UnifiedMetamodel__EClass139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__MethodBack138"):
                opp_val = getattr(old_value, "UnifiedMetamodel__MethodBack138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__MethodBack138"):
                opp_val = getattr(value, "UnifiedMetamodel__MethodBack138", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__MethodBack138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__EClass152(self):
        return self.__UnifiedMetamodel__EClass152

    @UnifiedMetamodel__EClass152.setter
    def UnifiedMetamodel__EClass152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass152", None)
        self.__UnifiedMetamodel__EClass152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Annotation153"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation153", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation153"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation153", None)
                setattr(value, "UnifiedMetamodel__Annotation153", self)

    @property
    def UnifiedMetamodel__EClass144(self):
        return self.__UnifiedMetamodel__EClass144

    @UnifiedMetamodel__EClass144.setter
    def UnifiedMetamodel__EClass144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass144", None)
        self.__UnifiedMetamodel__EClass144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Epackage"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Epackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Epackage"):
                opp_val = getattr(value, "UnifiedMetamodel__Epackage", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Epackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__EClass170(self):
        return self.__UnifiedMetamodel__EClass170

    @UnifiedMetamodel__EClass170.setter
    def UnifiedMetamodel__EClass170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass170", None)
        self.__UnifiedMetamodel__EClass170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__AbstractMethod169"):
                opp_val = getattr(old_value, "UnifiedMetamodel__AbstractMethod169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__AbstractMethod169"):
                opp_val = getattr(value, "UnifiedMetamodel__AbstractMethod169", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__AbstractMethod169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__EClass(self):
        return self.__UnifiedMetamodel__EClass

    @UnifiedMetamodel__EClass.setter
    def UnifiedMetamodel__EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass", None)
        self.__UnifiedMetamodel__EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Attribute127"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Attribute127", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Attribute127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Attribute127"):
                opp_val = getattr(value, "UnifiedMetamodel__Attribute127", None)
                setattr(value, "UnifiedMetamodel__Attribute127", self)

    @property
    def UnifiedMetamodel__EClass136(self):
        return self.__UnifiedMetamodel__EClass136

    @UnifiedMetamodel__EClass136.setter
    def UnifiedMetamodel__EClass136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass136", None)
        self.__UnifiedMetamodel__EClass136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__MethodBack135"):
                opp_val = getattr(old_value, "UnifiedMetamodel__MethodBack135", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__MethodBack135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__MethodBack135"):
                opp_val = getattr(value, "UnifiedMetamodel__MethodBack135", None)
                setattr(value, "UnifiedMetamodel__MethodBack135", self)

    @property
    def UnifiedMetamodel__EClass149(self):
        return self.__UnifiedMetamodel__EClass149

    @UnifiedMetamodel__EClass149.setter
    def UnifiedMetamodel__EClass149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass149", None)
        self.__UnifiedMetamodel__EClass149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__MethodBack150"):
                    opp_val = getattr(item, "UnifiedMetamodel__MethodBack150", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__MethodBack150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__MethodBack150"):
                    opp_val = getattr(item, "UnifiedMetamodel__MethodBack150", None)
                    
                    setattr(item, "UnifiedMetamodel__MethodBack150", self)
                    

class UnifiedMetamodel__Attribute:

    def __init__(self, name: str, UnifiedMetamodel__Attribute: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__Attribute127: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__Attribute147: "UnifiedMetamodel__EClass" = None):
        self.name = name
        self.UnifiedMetamodel__Attribute = UnifiedMetamodel__Attribute
        self.UnifiedMetamodel__Attribute127 = UnifiedMetamodel__Attribute127
        self.UnifiedMetamodel__Attribute147 = UnifiedMetamodel__Attribute147
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Attribute127(self):
        return self.__UnifiedMetamodel__Attribute127

    @UnifiedMetamodel__Attribute127.setter
    def UnifiedMetamodel__Attribute127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Attribute__UnifiedMetamodel__Attribute127", None)
        self.__UnifiedMetamodel__Attribute127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass", None)
                setattr(value, "UnifiedMetamodel__EClass", self)

    @property
    def UnifiedMetamodel__Attribute147(self):
        return self.__UnifiedMetamodel__Attribute147

    @UnifiedMetamodel__Attribute147.setter
    def UnifiedMetamodel__Attribute147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Attribute__UnifiedMetamodel__Attribute147", None)
        self.__UnifiedMetamodel__Attribute147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass146"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass146"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass146", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__EClass146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Attribute(self):
        return self.__UnifiedMetamodel__Attribute

    @UnifiedMetamodel__Attribute.setter
    def UnifiedMetamodel__Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Attribute__UnifiedMetamodel__Attribute", None)
        self.__UnifiedMetamodel__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Annotation125"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation125", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation125"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation125", None)
                setattr(value, "UnifiedMetamodel__Annotation125", self)

class UnifiedMetamodel__Annotation(EClass):

    def __init__(self, properties: str, UnifiedMetamodel__Annotation: "UnifiedMetamodel__Library" = None, UnifiedMetamodel__Annotation125: "UnifiedMetamodel__Attribute" = None, UnifiedMetamodel__Annotation133: "UnifiedMetamodel__MethodBack" = None, UnifiedMetamodel__Annotation155: "UnifiedMetamodel__Descriptor" = None, UnifiedMetamodel__Annotation153: "UnifiedMetamodel__EClass" = None):
        self.properties = properties
        self.UnifiedMetamodel__Annotation = UnifiedMetamodel__Annotation
        self.UnifiedMetamodel__Annotation125 = UnifiedMetamodel__Annotation125
        self.UnifiedMetamodel__Annotation133 = UnifiedMetamodel__Annotation133
        self.UnifiedMetamodel__Annotation155 = UnifiedMetamodel__Annotation155
        self.UnifiedMetamodel__Annotation153 = UnifiedMetamodel__Annotation153
        
    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def UnifiedMetamodel__Annotation155(self):
        return self.__UnifiedMetamodel__Annotation155

    @UnifiedMetamodel__Annotation155.setter
    def UnifiedMetamodel__Annotation155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation155", None)
        self.__UnifiedMetamodel__Annotation155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Descriptor"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Descriptor", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Descriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Descriptor"):
                opp_val = getattr(value, "UnifiedMetamodel__Descriptor", None)
                setattr(value, "UnifiedMetamodel__Descriptor", self)

    @property
    def UnifiedMetamodel__Annotation153(self):
        return self.__UnifiedMetamodel__Annotation153

    @UnifiedMetamodel__Annotation153.setter
    def UnifiedMetamodel__Annotation153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation153", None)
        self.__UnifiedMetamodel__Annotation153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass152"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass152", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass152"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass152", None)
                setattr(value, "UnifiedMetamodel__EClass152", self)

    @property
    def UnifiedMetamodel__Annotation133(self):
        return self.__UnifiedMetamodel__Annotation133

    @UnifiedMetamodel__Annotation133.setter
    def UnifiedMetamodel__Annotation133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation133", None)
        self.__UnifiedMetamodel__Annotation133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__MethodBack"):
                opp_val = getattr(old_value, "UnifiedMetamodel__MethodBack", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__MethodBack", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__MethodBack"):
                opp_val = getattr(value, "UnifiedMetamodel__MethodBack", None)
                setattr(value, "UnifiedMetamodel__MethodBack", self)

    @property
    def UnifiedMetamodel__Annotation(self):
        return self.__UnifiedMetamodel__Annotation

    @UnifiedMetamodel__Annotation.setter
    def UnifiedMetamodel__Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation", None)
        self.__UnifiedMetamodel__Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Library123"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Library123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Library123"):
                opp_val = getattr(value, "UnifiedMetamodel__Library123", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Library123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Annotation125(self):
        return self.__UnifiedMetamodel__Annotation125

    @UnifiedMetamodel__Annotation125.setter
    def UnifiedMetamodel__Annotation125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation125", None)
        self.__UnifiedMetamodel__Annotation125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Attribute"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Attribute", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Attribute"):
                opp_val = getattr(value, "UnifiedMetamodel__Attribute", None)
                setattr(value, "UnifiedMetamodel__Attribute", self)

class UnifiedMetamodel__Subproject:

    def __init__(self, name: str, UnifiedMetamodel__Subproject: "UnifiedMetamodel__JEE_Project" = None, UnifiedMetamodel__Subproject157: set["UnifiedMetamodel__Descriptor"] = None, UnifiedMetamodel__Subproject160: set["UnifiedMetamodel__Epackage"] = None, UnifiedMetamodel__Subproject163: set["UnifiedMetamodel__Library"] = None):
        self.name = name
        self.UnifiedMetamodel__Subproject = UnifiedMetamodel__Subproject
        self.UnifiedMetamodel__Subproject157 = UnifiedMetamodel__Subproject157 if UnifiedMetamodel__Subproject157 is not None else set()
        self.UnifiedMetamodel__Subproject160 = UnifiedMetamodel__Subproject160 if UnifiedMetamodel__Subproject160 is not None else set()
        self.UnifiedMetamodel__Subproject163 = UnifiedMetamodel__Subproject163 if UnifiedMetamodel__Subproject163 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Subproject160(self):
        return self.__UnifiedMetamodel__Subproject160

    @UnifiedMetamodel__Subproject160.setter
    def UnifiedMetamodel__Subproject160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject160", None)
        self.__UnifiedMetamodel__Subproject160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Epackage161"):
                    opp_val = getattr(item, "UnifiedMetamodel__Epackage161", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Epackage161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Epackage161"):
                    opp_val = getattr(item, "UnifiedMetamodel__Epackage161", None)
                    
                    setattr(item, "UnifiedMetamodel__Epackage161", self)
                    

    @property
    def UnifiedMetamodel__Subproject163(self):
        return self.__UnifiedMetamodel__Subproject163

    @UnifiedMetamodel__Subproject163.setter
    def UnifiedMetamodel__Subproject163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject163", None)
        self.__UnifiedMetamodel__Subproject163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Library164"):
                    opp_val = getattr(item, "UnifiedMetamodel__Library164", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Library164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Library164"):
                    opp_val = getattr(item, "UnifiedMetamodel__Library164", None)
                    
                    setattr(item, "UnifiedMetamodel__Library164", self)
                    

    @property
    def UnifiedMetamodel__Subproject157(self):
        return self.__UnifiedMetamodel__Subproject157

    @UnifiedMetamodel__Subproject157.setter
    def UnifiedMetamodel__Subproject157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject157", None)
        self.__UnifiedMetamodel__Subproject157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Descriptor158"):
                    opp_val = getattr(item, "UnifiedMetamodel__Descriptor158", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Descriptor158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Descriptor158"):
                    opp_val = getattr(item, "UnifiedMetamodel__Descriptor158", None)
                    
                    setattr(item, "UnifiedMetamodel__Descriptor158", self)
                    

    @property
    def UnifiedMetamodel__Subproject(self):
        return self.__UnifiedMetamodel__Subproject

    @UnifiedMetamodel__Subproject.setter
    def UnifiedMetamodel__Subproject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject", None)
        self.__UnifiedMetamodel__Subproject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__JEE_Project119"):
                opp_val = getattr(old_value, "UnifiedMetamodel__JEE_Project119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__JEE_Project119"):
                opp_val = getattr(value, "UnifiedMetamodel__JEE_Project119", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__JEE_Project119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__JEE_Project:

    def __init__(self, name: str, UnifiedMetamodel__JEE_Project: "UnifiedMetamodel__JavaApp" = None, UnifiedMetamodel__JEE_Project119: set["UnifiedMetamodel__Subproject"] = None):
        self.name = name
        self.UnifiedMetamodel__JEE_Project = UnifiedMetamodel__JEE_Project
        self.UnifiedMetamodel__JEE_Project119 = UnifiedMetamodel__JEE_Project119 if UnifiedMetamodel__JEE_Project119 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__JEE_Project119(self):
        return self.__UnifiedMetamodel__JEE_Project119

    @UnifiedMetamodel__JEE_Project119.setter
    def UnifiedMetamodel__JEE_Project119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__JEE_Project__UnifiedMetamodel__JEE_Project119", None)
        self.__UnifiedMetamodel__JEE_Project119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Subproject"):
                    opp_val = getattr(item, "UnifiedMetamodel__Subproject", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Subproject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Subproject"):
                    opp_val = getattr(item, "UnifiedMetamodel__Subproject", None)
                    
                    setattr(item, "UnifiedMetamodel__Subproject", self)
                    

    @property
    def UnifiedMetamodel__JEE_Project(self):
        return self.__UnifiedMetamodel__JEE_Project

    @UnifiedMetamodel__JEE_Project.setter
    def UnifiedMetamodel__JEE_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__JEE_Project__UnifiedMetamodel__JEE_Project", None)
        self.__UnifiedMetamodel__JEE_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__JavaApp117"):
                opp_val = getattr(old_value, "UnifiedMetamodel__JavaApp117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__JavaApp117"):
                opp_val = getattr(value, "UnifiedMetamodel__JavaApp117", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__JavaApp117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__JavaApp:

    pass
class UnifiedMetamodel__ReactApp:

    pass
class UnifiedMetamodel__ServicesFront:

    def __init__(self, name: str, UnifiedMetamodel__ServicesFront75: "UnifiedMetamodel__Functionality" = None, UnifiedMetamodel__ServicesFront: set["UnifiedMetamodel__ModuleFront"] = None, UnifiedMetamodel__ServicesFront67: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__ServicesFront75 = UnifiedMetamodel__ServicesFront75
        self.UnifiedMetamodel__ServicesFront = UnifiedMetamodel__ServicesFront if UnifiedMetamodel__ServicesFront is not None else set()
        self.UnifiedMetamodel__ServicesFront67 = UnifiedMetamodel__ServicesFront67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ServicesFront75(self):
        return self.__UnifiedMetamodel__ServicesFront75

    @UnifiedMetamodel__ServicesFront75.setter
    def UnifiedMetamodel__ServicesFront75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ServicesFront__UnifiedMetamodel__ServicesFront75", None)
        self.__UnifiedMetamodel__ServicesFront75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Functionality74"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Functionality74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Functionality74"):
                opp_val = getattr(value, "UnifiedMetamodel__Functionality74", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Functionality74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ServicesFront67(self):
        return self.__UnifiedMetamodel__ServicesFront67

    @UnifiedMetamodel__ServicesFront67.setter
    def UnifiedMetamodel__ServicesFront67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ServicesFront__UnifiedMetamodel__ServicesFront67", None)
        self.__UnifiedMetamodel__ServicesFront67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory68"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory68", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory68"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory68", None)
                setattr(value, "UnifiedMetamodel__Directory68", self)

    @property
    def UnifiedMetamodel__ServicesFront(self):
        return self.__UnifiedMetamodel__ServicesFront

    @UnifiedMetamodel__ServicesFront.setter
    def UnifiedMetamodel__ServicesFront(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ServicesFront__UnifiedMetamodel__ServicesFront", None)
        self.__UnifiedMetamodel__ServicesFront = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront65"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront65", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ModuleFront65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront65"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront65", None)
                    
                    setattr(item, "UnifiedMetamodel__ModuleFront65", self)
                    

class UnifiedMetamodel__ComponentFront:

    def __init__(self, name: str, UnifiedMetamodel__ComponentFront: "UnifiedMetamodel__Functionality" = None, UnifiedMetamodel__ComponentFront97: set["UnifiedMetamodel__ModuleFront"] = None, UnifiedMetamodel__ComponentFront100: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__ComponentFront = UnifiedMetamodel__ComponentFront
        self.UnifiedMetamodel__ComponentFront97 = UnifiedMetamodel__ComponentFront97 if UnifiedMetamodel__ComponentFront97 is not None else set()
        self.UnifiedMetamodel__ComponentFront100 = UnifiedMetamodel__ComponentFront100
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ComponentFront100(self):
        return self.__UnifiedMetamodel__ComponentFront100

    @UnifiedMetamodel__ComponentFront100.setter
    def UnifiedMetamodel__ComponentFront100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ComponentFront__UnifiedMetamodel__ComponentFront100", None)
        self.__UnifiedMetamodel__ComponentFront100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory101"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory101", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory101"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory101", None)
                setattr(value, "UnifiedMetamodel__Directory101", self)

    @property
    def UnifiedMetamodel__ComponentFront(self):
        return self.__UnifiedMetamodel__ComponentFront

    @UnifiedMetamodel__ComponentFront.setter
    def UnifiedMetamodel__ComponentFront(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ComponentFront__UnifiedMetamodel__ComponentFront", None)
        self.__UnifiedMetamodel__ComponentFront = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Functionality"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Functionality", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Functionality"):
                opp_val = getattr(value, "UnifiedMetamodel__Functionality", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Functionality", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ComponentFront97(self):
        return self.__UnifiedMetamodel__ComponentFront97

    @UnifiedMetamodel__ComponentFront97.setter
    def UnifiedMetamodel__ComponentFront97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ComponentFront__UnifiedMetamodel__ComponentFront97", None)
        self.__UnifiedMetamodel__ComponentFront97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront98"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront98", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ModuleFront98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront98"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront98", None)
                    
                    setattr(item, "UnifiedMetamodel__ModuleFront98", self)
                    

class UnifiedMetamodel__Functionality:

    def __init__(self, name: str, UnifiedMetamodel__Functionality: set["UnifiedMetamodel__ComponentFront"] = None, UnifiedMetamodel__Functionality71: "UnifiedMetamodel__State" = None, UnifiedMetamodel__Functionality74: set["UnifiedMetamodel__ServicesFront"] = None, UnifiedMetamodel__Functionality77: "UnifiedMetamodel__Directory" = None, UnifiedMetamodel__Functionality89: "UnifiedMetamodel__ReactApp" = None):
        self.name = name
        self.UnifiedMetamodel__Functionality = UnifiedMetamodel__Functionality if UnifiedMetamodel__Functionality is not None else set()
        self.UnifiedMetamodel__Functionality71 = UnifiedMetamodel__Functionality71
        self.UnifiedMetamodel__Functionality74 = UnifiedMetamodel__Functionality74 if UnifiedMetamodel__Functionality74 is not None else set()
        self.UnifiedMetamodel__Functionality77 = UnifiedMetamodel__Functionality77
        self.UnifiedMetamodel__Functionality89 = UnifiedMetamodel__Functionality89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Functionality77(self):
        return self.__UnifiedMetamodel__Functionality77

    @UnifiedMetamodel__Functionality77.setter
    def UnifiedMetamodel__Functionality77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality77", None)
        self.__UnifiedMetamodel__Functionality77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory78"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory78", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory78"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory78", None)
                setattr(value, "UnifiedMetamodel__Directory78", self)

    @property
    def UnifiedMetamodel__Functionality(self):
        return self.__UnifiedMetamodel__Functionality

    @UnifiedMetamodel__Functionality.setter
    def UnifiedMetamodel__Functionality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality", None)
        self.__UnifiedMetamodel__Functionality = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ComponentFront"):
                    opp_val = getattr(item, "UnifiedMetamodel__ComponentFront", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ComponentFront", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ComponentFront"):
                    opp_val = getattr(item, "UnifiedMetamodel__ComponentFront", None)
                    
                    setattr(item, "UnifiedMetamodel__ComponentFront", self)
                    

    @property
    def UnifiedMetamodel__Functionality89(self):
        return self.__UnifiedMetamodel__Functionality89

    @UnifiedMetamodel__Functionality89.setter
    def UnifiedMetamodel__Functionality89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality89", None)
        self.__UnifiedMetamodel__Functionality89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ReactApp"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ReactApp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ReactApp"):
                opp_val = getattr(value, "UnifiedMetamodel__ReactApp", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ReactApp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Functionality71(self):
        return self.__UnifiedMetamodel__Functionality71

    @UnifiedMetamodel__Functionality71.setter
    def UnifiedMetamodel__Functionality71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality71", None)
        self.__UnifiedMetamodel__Functionality71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__State72"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State72", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State72"):
                opp_val = getattr(value, "UnifiedMetamodel__State72", None)
                setattr(value, "UnifiedMetamodel__State72", self)

    @property
    def UnifiedMetamodel__Functionality74(self):
        return self.__UnifiedMetamodel__Functionality74

    @UnifiedMetamodel__Functionality74.setter
    def UnifiedMetamodel__Functionality74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality74", None)
        self.__UnifiedMetamodel__Functionality74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ServicesFront75"):
                    opp_val = getattr(item, "UnifiedMetamodel__ServicesFront75", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ServicesFront75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ServicesFront75"):
                    opp_val = getattr(item, "UnifiedMetamodel__ServicesFront75", None)
                    
                    setattr(item, "UnifiedMetamodel__ServicesFront75", self)
                    

class UnifiedMetamodel__ModuleFront:

    def __init__(self, name: str, UnifiedMetamodel__ModuleFront: "UnifiedMetamodel__State" = None, UnifiedMetamodel__ModuleFront65: "UnifiedMetamodel__ServicesFront" = None, UnifiedMetamodel__ModuleFront92: "UnifiedMetamodel__ReactApp" = None, UnifiedMetamodel__ModuleFront98: "UnifiedMetamodel__ComponentFront" = None, UnifiedMetamodel__ModuleFront109: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__ModuleFront = UnifiedMetamodel__ModuleFront
        self.UnifiedMetamodel__ModuleFront65 = UnifiedMetamodel__ModuleFront65
        self.UnifiedMetamodel__ModuleFront92 = UnifiedMetamodel__ModuleFront92
        self.UnifiedMetamodel__ModuleFront98 = UnifiedMetamodel__ModuleFront98
        self.UnifiedMetamodel__ModuleFront109 = UnifiedMetamodel__ModuleFront109
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ModuleFront92(self):
        return self.__UnifiedMetamodel__ModuleFront92

    @UnifiedMetamodel__ModuleFront92.setter
    def UnifiedMetamodel__ModuleFront92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront92", None)
        self.__UnifiedMetamodel__ModuleFront92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ReactApp91"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ReactApp91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ReactApp91"):
                opp_val = getattr(value, "UnifiedMetamodel__ReactApp91", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ReactApp91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ModuleFront109(self):
        return self.__UnifiedMetamodel__ModuleFront109

    @UnifiedMetamodel__ModuleFront109.setter
    def UnifiedMetamodel__ModuleFront109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront109", None)
        self.__UnifiedMetamodel__ModuleFront109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory110"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory110", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory110"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory110", None)
                setattr(value, "UnifiedMetamodel__Directory110", self)

    @property
    def UnifiedMetamodel__ModuleFront65(self):
        return self.__UnifiedMetamodel__ModuleFront65

    @UnifiedMetamodel__ModuleFront65.setter
    def UnifiedMetamodel__ModuleFront65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront65", None)
        self.__UnifiedMetamodel__ModuleFront65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ServicesFront"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ServicesFront", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ServicesFront"):
                opp_val = getattr(value, "UnifiedMetamodel__ServicesFront", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ServicesFront", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ModuleFront98(self):
        return self.__UnifiedMetamodel__ModuleFront98

    @UnifiedMetamodel__ModuleFront98.setter
    def UnifiedMetamodel__ModuleFront98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront98", None)
        self.__UnifiedMetamodel__ModuleFront98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ComponentFront97"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ComponentFront97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ComponentFront97"):
                opp_val = getattr(value, "UnifiedMetamodel__ComponentFront97", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ComponentFront97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ModuleFront(self):
        return self.__UnifiedMetamodel__ModuleFront

    @UnifiedMetamodel__ModuleFront.setter
    def UnifiedMetamodel__ModuleFront(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront", None)
        self.__UnifiedMetamodel__ModuleFront = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__State57"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State57"):
                opp_val = getattr(value, "UnifiedMetamodel__State57", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__State57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Reducer:

    def __init__(self, name: str, UnifiedMetamodel__Reducer: "UnifiedMetamodel__State" = None, UnifiedMetamodel__Reducer63: "UnifiedMetamodel__Container" = None, UnifiedMetamodel__Reducer103: set["UnifiedMetamodel__ActionCreator"] = None, UnifiedMetamodel__Reducer106: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__Reducer = UnifiedMetamodel__Reducer
        self.UnifiedMetamodel__Reducer63 = UnifiedMetamodel__Reducer63
        self.UnifiedMetamodel__Reducer103 = UnifiedMetamodel__Reducer103 if UnifiedMetamodel__Reducer103 is not None else set()
        self.UnifiedMetamodel__Reducer106 = UnifiedMetamodel__Reducer106
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Reducer103(self):
        return self.__UnifiedMetamodel__Reducer103

    @UnifiedMetamodel__Reducer103.setter
    def UnifiedMetamodel__Reducer103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer103", None)
        self.__UnifiedMetamodel__Reducer103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator104"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator104", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ActionCreator104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator104"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator104", None)
                    
                    setattr(item, "UnifiedMetamodel__ActionCreator104", self)
                    

    @property
    def UnifiedMetamodel__Reducer106(self):
        return self.__UnifiedMetamodel__Reducer106

    @UnifiedMetamodel__Reducer106.setter
    def UnifiedMetamodel__Reducer106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer106", None)
        self.__UnifiedMetamodel__Reducer106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory107"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory107", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory107"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory107", None)
                setattr(value, "UnifiedMetamodel__Directory107", self)

    @property
    def UnifiedMetamodel__Reducer(self):
        return self.__UnifiedMetamodel__Reducer

    @UnifiedMetamodel__Reducer.setter
    def UnifiedMetamodel__Reducer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer", None)
        self.__UnifiedMetamodel__Reducer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__State55"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State55"):
                opp_val = getattr(value, "UnifiedMetamodel__State55", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__State55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Reducer63(self):
        return self.__UnifiedMetamodel__Reducer63

    @UnifiedMetamodel__Reducer63.setter
    def UnifiedMetamodel__Reducer63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer63", None)
        self.__UnifiedMetamodel__Reducer63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Container62"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Container62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Container62"):
                opp_val = getattr(value, "UnifiedMetamodel__Container62", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Container62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Action:

    def __init__(self, name: str, UnifiedMetamodel__Action: "UnifiedMetamodel__State" = None, UnifiedMetamodel__Action80: set["UnifiedMetamodel__ActionDispatcher"] = None, UnifiedMetamodel__Action83: set["UnifiedMetamodel__ActionCreator"] = None, UnifiedMetamodel__Action86: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__Action = UnifiedMetamodel__Action
        self.UnifiedMetamodel__Action80 = UnifiedMetamodel__Action80 if UnifiedMetamodel__Action80 is not None else set()
        self.UnifiedMetamodel__Action83 = UnifiedMetamodel__Action83 if UnifiedMetamodel__Action83 is not None else set()
        self.UnifiedMetamodel__Action86 = UnifiedMetamodel__Action86
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Action86(self):
        return self.__UnifiedMetamodel__Action86

    @UnifiedMetamodel__Action86.setter
    def UnifiedMetamodel__Action86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action86", None)
        self.__UnifiedMetamodel__Action86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory87"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory87", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory87"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory87", None)
                setattr(value, "UnifiedMetamodel__Directory87", self)

    @property
    def UnifiedMetamodel__Action(self):
        return self.__UnifiedMetamodel__Action

    @UnifiedMetamodel__Action.setter
    def UnifiedMetamodel__Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action", None)
        self.__UnifiedMetamodel__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__State"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State"):
                opp_val = getattr(value, "UnifiedMetamodel__State", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Action83(self):
        return self.__UnifiedMetamodel__Action83

    @UnifiedMetamodel__Action83.setter
    def UnifiedMetamodel__Action83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action83", None)
        self.__UnifiedMetamodel__Action83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator84"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator84", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ActionCreator84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator84"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator84", None)
                    
                    setattr(item, "UnifiedMetamodel__ActionCreator84", self)
                    

    @property
    def UnifiedMetamodel__Action80(self):
        return self.__UnifiedMetamodel__Action80

    @UnifiedMetamodel__Action80.setter
    def UnifiedMetamodel__Action80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action80", None)
        self.__UnifiedMetamodel__Action80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ActionDispatcher81"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionDispatcher81", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ActionDispatcher81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ActionDispatcher81"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionDispatcher81", None)
                    
                    setattr(item, "UnifiedMetamodel__ActionDispatcher81", self)
                    

class UnifiedMetamodel__State:

    pass
class UIFront:

    pass
class UnifiedMetamodel__RouterComponent(UIFront):

    pass
class UnifiedMetamodel__Visualizer(UIFront):

    pass
class ComponentFront:

    pass
class UnifiedMetamodel__Container(ComponentFront):

    pass
class File:

    pass
class UnifiedMetamodel__JS(File):

    pass
class UnifiedMetamodel__UIFront(ComponentFront):

    pass
class UnifiedMetamodel__JSON(File):

    pass
class ModuleFront:

    pass
class UnifiedMetamodel__Redux(ModuleFront):

    pass
class UnifiedMetamodel__Design(ModuleFront):

    pass
class UnifiedMetamodel__React(ModuleFront):

    pass
class UnifiedMetamodel__Router(ModuleFront):

    pass
class UnifiedMetamodel__ActionCreator:

    def __init__(self, name: str, UnifiedMetamodel__ActionCreator: "UnifiedMetamodel__ActionDispatcher" = None, UnifiedMetamodel__ActionCreator84: "UnifiedMetamodel__Action" = None, UnifiedMetamodel__ActionCreator104: "UnifiedMetamodel__Reducer" = None):
        self.name = name
        self.UnifiedMetamodel__ActionCreator = UnifiedMetamodel__ActionCreator
        self.UnifiedMetamodel__ActionCreator84 = UnifiedMetamodel__ActionCreator84
        self.UnifiedMetamodel__ActionCreator104 = UnifiedMetamodel__ActionCreator104
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ActionCreator84(self):
        return self.__UnifiedMetamodel__ActionCreator84

    @UnifiedMetamodel__ActionCreator84.setter
    def UnifiedMetamodel__ActionCreator84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionCreator__UnifiedMetamodel__ActionCreator84", None)
        self.__UnifiedMetamodel__ActionCreator84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Action83"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Action83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Action83"):
                opp_val = getattr(value, "UnifiedMetamodel__Action83", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Action83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ActionCreator104(self):
        return self.__UnifiedMetamodel__ActionCreator104

    @UnifiedMetamodel__ActionCreator104.setter
    def UnifiedMetamodel__ActionCreator104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionCreator__UnifiedMetamodel__ActionCreator104", None)
        self.__UnifiedMetamodel__ActionCreator104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Reducer103"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Reducer103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Reducer103"):
                opp_val = getattr(value, "UnifiedMetamodel__Reducer103", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Reducer103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ActionCreator(self):
        return self.__UnifiedMetamodel__ActionCreator

    @UnifiedMetamodel__ActionCreator.setter
    def UnifiedMetamodel__ActionCreator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionCreator__UnifiedMetamodel__ActionCreator", None)
        self.__UnifiedMetamodel__ActionCreator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ActionDispatcher"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ActionDispatcher", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ActionDispatcher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ActionDispatcher"):
                opp_val = getattr(value, "UnifiedMetamodel__ActionDispatcher", None)
                setattr(value, "UnifiedMetamodel__ActionDispatcher", self)

class UnifiedMetamodel__ActionDispatcher:

    def __init__(self, name: str, UnifiedMetamodel__ActionDispatcher: "UnifiedMetamodel__ActionCreator" = None, UnifiedMetamodel__ActionDispatcher60: "UnifiedMetamodel__Container" = None, UnifiedMetamodel__ActionDispatcher81: "UnifiedMetamodel__Action" = None):
        self.name = name
        self.UnifiedMetamodel__ActionDispatcher = UnifiedMetamodel__ActionDispatcher
        self.UnifiedMetamodel__ActionDispatcher60 = UnifiedMetamodel__ActionDispatcher60
        self.UnifiedMetamodel__ActionDispatcher81 = UnifiedMetamodel__ActionDispatcher81
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ActionDispatcher(self):
        return self.__UnifiedMetamodel__ActionDispatcher

    @UnifiedMetamodel__ActionDispatcher.setter
    def UnifiedMetamodel__ActionDispatcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionDispatcher__UnifiedMetamodel__ActionDispatcher", None)
        self.__UnifiedMetamodel__ActionDispatcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ActionCreator"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ActionCreator", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ActionCreator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ActionCreator"):
                opp_val = getattr(value, "UnifiedMetamodel__ActionCreator", None)
                setattr(value, "UnifiedMetamodel__ActionCreator", self)

    @property
    def UnifiedMetamodel__ActionDispatcher60(self):
        return self.__UnifiedMetamodel__ActionDispatcher60

    @UnifiedMetamodel__ActionDispatcher60.setter
    def UnifiedMetamodel__ActionDispatcher60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionDispatcher__UnifiedMetamodel__ActionDispatcher60", None)
        self.__UnifiedMetamodel__ActionDispatcher60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Container"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Container"):
                opp_val = getattr(value, "UnifiedMetamodel__Container", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ActionDispatcher81(self):
        return self.__UnifiedMetamodel__ActionDispatcher81

    @UnifiedMetamodel__ActionDispatcher81.setter
    def UnifiedMetamodel__ActionDispatcher81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionDispatcher__UnifiedMetamodel__ActionDispatcher81", None)
        self.__UnifiedMetamodel__ActionDispatcher81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Action80"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Action80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Action80"):
                opp_val = getattr(value, "UnifiedMetamodel__Action80", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Action80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__File:

    def __init__(self, type: str, name: str, UnifiedMetamodel__File: "UnifiedMetamodel__Directory" = None):
        self.type = type
        self.name = name
        self.UnifiedMetamodel__File = UnifiedMetamodel__File
        
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
    def UnifiedMetamodel__File(self):
        return self.__UnifiedMetamodel__File

    @UnifiedMetamodel__File.setter
    def UnifiedMetamodel__File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__File__UnifiedMetamodel__File", None)
        self.__UnifiedMetamodel__File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory52"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory52"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory52", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Directory52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Directory:

    def __init__(self, purpose: str, isRoot: bool, name: str, UnifiedMetamodel__Directory: "UnifiedMetamodel__Directory" = None, UnifiedMetamodel__Directory49: set["UnifiedMetamodel__Directory"] = None, UnifiedMetamodel__Directory52: set["UnifiedMetamodel__File"] = None, UnifiedMetamodel__Directory78: "UnifiedMetamodel__Functionality" = None, UnifiedMetamodel__Directory68: "UnifiedMetamodel__ServicesFront" = None, UnifiedMetamodel__Directory95: "UnifiedMetamodel__ReactApp" = None, UnifiedMetamodel__Directory101: "UnifiedMetamodel__ComponentFront" = None, UnifiedMetamodel__Directory87: "UnifiedMetamodel__Action" = None, UnifiedMetamodel__Directory110: "UnifiedMetamodel__ModuleFront" = None, UnifiedMetamodel__Directory107: "UnifiedMetamodel__Reducer" = None):
        self.purpose = purpose
        self.isRoot = isRoot
        self.name = name
        self.UnifiedMetamodel__Directory = UnifiedMetamodel__Directory
        self.UnifiedMetamodel__Directory49 = UnifiedMetamodel__Directory49 if UnifiedMetamodel__Directory49 is not None else set()
        self.UnifiedMetamodel__Directory52 = UnifiedMetamodel__Directory52 if UnifiedMetamodel__Directory52 is not None else set()
        self.UnifiedMetamodel__Directory78 = UnifiedMetamodel__Directory78
        self.UnifiedMetamodel__Directory68 = UnifiedMetamodel__Directory68
        self.UnifiedMetamodel__Directory95 = UnifiedMetamodel__Directory95
        self.UnifiedMetamodel__Directory101 = UnifiedMetamodel__Directory101
        self.UnifiedMetamodel__Directory87 = UnifiedMetamodel__Directory87
        self.UnifiedMetamodel__Directory110 = UnifiedMetamodel__Directory110
        self.UnifiedMetamodel__Directory107 = UnifiedMetamodel__Directory107
        
    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isRoot(self) -> bool:
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: bool):
        self.__isRoot = isRoot

    @property
    def UnifiedMetamodel__Directory68(self):
        return self.__UnifiedMetamodel__Directory68

    @UnifiedMetamodel__Directory68.setter
    def UnifiedMetamodel__Directory68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory68", None)
        self.__UnifiedMetamodel__Directory68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ServicesFront67"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ServicesFront67", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ServicesFront67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ServicesFront67"):
                opp_val = getattr(value, "UnifiedMetamodel__ServicesFront67", None)
                setattr(value, "UnifiedMetamodel__ServicesFront67", self)

    @property
    def UnifiedMetamodel__Directory(self):
        return self.__UnifiedMetamodel__Directory

    @UnifiedMetamodel__Directory.setter
    def UnifiedMetamodel__Directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory", None)
        self.__UnifiedMetamodel__Directory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory49"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory49"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory49", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Directory49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Directory110(self):
        return self.__UnifiedMetamodel__Directory110

    @UnifiedMetamodel__Directory110.setter
    def UnifiedMetamodel__Directory110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory110", None)
        self.__UnifiedMetamodel__Directory110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ModuleFront109"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ModuleFront109", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ModuleFront109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ModuleFront109"):
                opp_val = getattr(value, "UnifiedMetamodel__ModuleFront109", None)
                setattr(value, "UnifiedMetamodel__ModuleFront109", self)

    @property
    def UnifiedMetamodel__Directory78(self):
        return self.__UnifiedMetamodel__Directory78

    @UnifiedMetamodel__Directory78.setter
    def UnifiedMetamodel__Directory78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory78", None)
        self.__UnifiedMetamodel__Directory78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Functionality77"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Functionality77", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Functionality77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Functionality77"):
                opp_val = getattr(value, "UnifiedMetamodel__Functionality77", None)
                setattr(value, "UnifiedMetamodel__Functionality77", self)

    @property
    def UnifiedMetamodel__Directory52(self):
        return self.__UnifiedMetamodel__Directory52

    @UnifiedMetamodel__Directory52.setter
    def UnifiedMetamodel__Directory52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory52", None)
        self.__UnifiedMetamodel__Directory52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__File"):
                    opp_val = getattr(item, "UnifiedMetamodel__File", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__File", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__File"):
                    opp_val = getattr(item, "UnifiedMetamodel__File", None)
                    
                    setattr(item, "UnifiedMetamodel__File", self)
                    

    @property
    def UnifiedMetamodel__Directory87(self):
        return self.__UnifiedMetamodel__Directory87

    @UnifiedMetamodel__Directory87.setter
    def UnifiedMetamodel__Directory87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory87", None)
        self.__UnifiedMetamodel__Directory87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Action86"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Action86", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Action86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Action86"):
                opp_val = getattr(value, "UnifiedMetamodel__Action86", None)
                setattr(value, "UnifiedMetamodel__Action86", self)

    @property
    def UnifiedMetamodel__Directory49(self):
        return self.__UnifiedMetamodel__Directory49

    @UnifiedMetamodel__Directory49.setter
    def UnifiedMetamodel__Directory49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory49", None)
        self.__UnifiedMetamodel__Directory49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Directory"):
                    opp_val = getattr(item, "UnifiedMetamodel__Directory", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Directory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Directory"):
                    opp_val = getattr(item, "UnifiedMetamodel__Directory", None)
                    
                    setattr(item, "UnifiedMetamodel__Directory", self)
                    

    @property
    def UnifiedMetamodel__Directory107(self):
        return self.__UnifiedMetamodel__Directory107

    @UnifiedMetamodel__Directory107.setter
    def UnifiedMetamodel__Directory107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory107", None)
        self.__UnifiedMetamodel__Directory107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Reducer106"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Reducer106", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Reducer106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Reducer106"):
                opp_val = getattr(value, "UnifiedMetamodel__Reducer106", None)
                setattr(value, "UnifiedMetamodel__Reducer106", self)

    @property
    def UnifiedMetamodel__Directory95(self):
        return self.__UnifiedMetamodel__Directory95

    @UnifiedMetamodel__Directory95.setter
    def UnifiedMetamodel__Directory95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory95", None)
        self.__UnifiedMetamodel__Directory95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ReactApp94"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ReactApp94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ReactApp94"):
                opp_val = getattr(value, "UnifiedMetamodel__ReactApp94", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ReactApp94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Directory101(self):
        return self.__UnifiedMetamodel__Directory101

    @UnifiedMetamodel__Directory101.setter
    def UnifiedMetamodel__Directory101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory101", None)
        self.__UnifiedMetamodel__Directory101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ComponentFront100"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ComponentFront100", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ComponentFront100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ComponentFront100"):
                opp_val = getattr(value, "UnifiedMetamodel__ComponentFront100", None)
                setattr(value, "UnifiedMetamodel__ComponentFront100", self)

class UnifiedMetamodel__APICall(ModuleFront):

    pass
class UnifiedMetamodel__CSS(File):

    pass
class UnifiedMetamodel__MD(File):

    pass
class UnifiedMetamodel__RelationDom:

    pass
class UnifiedMetamodel__Property:

    def __init__(self, name: str, type: str, UnifiedMetamodel__Property: "UnifiedMetamodel__Entity" = None):
        self.name = name
        self.type = type
        self.UnifiedMetamodel__Property = UnifiedMetamodel__Property
        
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
    def UnifiedMetamodel__Property(self):
        return self.__UnifiedMetamodel__Property

    @UnifiedMetamodel__Property.setter
    def UnifiedMetamodel__Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Property__UnifiedMetamodel__Property", None)
        self.__UnifiedMetamodel__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Entity28"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Entity28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Entity28"):
                opp_val = getattr(value, "UnifiedMetamodel__Entity28", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Entity28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transaction:

    pass
class UnifiedMetamodel__Exchange(Transaction):

    pass
class UnifiedMetamodel__Sale(Transaction):

    pass
class Operations:

    pass
class UnifiedMetamodel__Create(Operations):

    pass
class UnifiedMetamodel__Read(Operations):

    pass
class UnifiedMetamodel__Transaction:

    pass
class Entity:

    pass
class UnifiedMetamodel__GeneralEntity(Entity):

    pass
class UnifiedMetamodel__SpecialEntity(Entity):

    pass
class UnifiedMetamodel__Submodule:

    def __init__(self, name: str, UnifiedMetamodel__Submodule: "UnifiedMetamodel__Module" = None, UnifiedMetamodel__Submodule37: set["UnifiedMetamodel__Operations"] = None, UnifiedMetamodel__Submodule40: set["UnifiedMetamodel__Entity"] = None):
        self.name = name
        self.UnifiedMetamodel__Submodule = UnifiedMetamodel__Submodule
        self.UnifiedMetamodel__Submodule37 = UnifiedMetamodel__Submodule37 if UnifiedMetamodel__Submodule37 is not None else set()
        self.UnifiedMetamodel__Submodule40 = UnifiedMetamodel__Submodule40 if UnifiedMetamodel__Submodule40 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Submodule(self):
        return self.__UnifiedMetamodel__Submodule

    @UnifiedMetamodel__Submodule.setter
    def UnifiedMetamodel__Submodule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Submodule__UnifiedMetamodel__Submodule", None)
        self.__UnifiedMetamodel__Submodule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Module"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Module"):
                opp_val = getattr(value, "UnifiedMetamodel__Module", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Submodule40(self):
        return self.__UnifiedMetamodel__Submodule40

    @UnifiedMetamodel__Submodule40.setter
    def UnifiedMetamodel__Submodule40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Submodule__UnifiedMetamodel__Submodule40", None)
        self.__UnifiedMetamodel__Submodule40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Entity41"):
                    opp_val = getattr(item, "UnifiedMetamodel__Entity41", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Entity41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Entity41"):
                    opp_val = getattr(item, "UnifiedMetamodel__Entity41", None)
                    
                    setattr(item, "UnifiedMetamodel__Entity41", self)
                    

    @property
    def UnifiedMetamodel__Submodule37(self):
        return self.__UnifiedMetamodel__Submodule37

    @UnifiedMetamodel__Submodule37.setter
    def UnifiedMetamodel__Submodule37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Submodule__UnifiedMetamodel__Submodule37", None)
        self.__UnifiedMetamodel__Submodule37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Operations38"):
                    opp_val = getattr(item, "UnifiedMetamodel__Operations38", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Operations38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Operations38"):
                    opp_val = getattr(item, "UnifiedMetamodel__Operations38", None)
                    
                    setattr(item, "UnifiedMetamodel__Operations38", self)
                    

class UnifiedMetamodel__Module:

    def __init__(self, name: str, UnifiedMetamodel__Module: set["UnifiedMetamodel__Submodule"] = None, UnifiedMetamodel__Module44: "UnifiedMetamodel__DomainMetamodel" = None):
        self.name = name
        self.UnifiedMetamodel__Module = UnifiedMetamodel__Module if UnifiedMetamodel__Module is not None else set()
        self.UnifiedMetamodel__Module44 = UnifiedMetamodel__Module44
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Module(self):
        return self.__UnifiedMetamodel__Module

    @UnifiedMetamodel__Module.setter
    def UnifiedMetamodel__Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Module__UnifiedMetamodel__Module", None)
        self.__UnifiedMetamodel__Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Submodule"):
                    opp_val = getattr(item, "UnifiedMetamodel__Submodule", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Submodule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Submodule"):
                    opp_val = getattr(item, "UnifiedMetamodel__Submodule", None)
                    
                    setattr(item, "UnifiedMetamodel__Submodule", self)
                    

    @property
    def UnifiedMetamodel__Module44(self):
        return self.__UnifiedMetamodel__Module44

    @UnifiedMetamodel__Module44.setter
    def UnifiedMetamodel__Module44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Module__UnifiedMetamodel__Module44", None)
        self.__UnifiedMetamodel__Module44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__DomainMetamodel43"):
                opp_val = getattr(old_value, "UnifiedMetamodel__DomainMetamodel43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__DomainMetamodel43"):
                opp_val = getattr(value, "UnifiedMetamodel__DomainMetamodel43", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__DomainMetamodel43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Entity:

    def __init__(self, name: str, UnifiedMetamodel__Entity: "UnifiedMetamodel__Operations" = None, UnifiedMetamodel__Entity41: "UnifiedMetamodel__Submodule" = None, UnifiedMetamodel__Entity28: set["UnifiedMetamodel__Property"] = None, UnifiedMetamodel__Entity30: "UnifiedMetamodel__RelationDom" = None, UnifiedMetamodel__Entity33: "UnifiedMetamodel__RelationDom" = None):
        self.name = name
        self.UnifiedMetamodel__Entity = UnifiedMetamodel__Entity
        self.UnifiedMetamodel__Entity41 = UnifiedMetamodel__Entity41
        self.UnifiedMetamodel__Entity28 = UnifiedMetamodel__Entity28 if UnifiedMetamodel__Entity28 is not None else set()
        self.UnifiedMetamodel__Entity30 = UnifiedMetamodel__Entity30
        self.UnifiedMetamodel__Entity33 = UnifiedMetamodel__Entity33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Entity(self):
        return self.__UnifiedMetamodel__Entity

    @UnifiedMetamodel__Entity.setter
    def UnifiedMetamodel__Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity", None)
        self.__UnifiedMetamodel__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Operations"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Operations", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Operations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Operations"):
                opp_val = getattr(value, "UnifiedMetamodel__Operations", None)
                setattr(value, "UnifiedMetamodel__Operations", self)

    @property
    def UnifiedMetamodel__Entity30(self):
        return self.__UnifiedMetamodel__Entity30

    @UnifiedMetamodel__Entity30.setter
    def UnifiedMetamodel__Entity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity30", None)
        self.__UnifiedMetamodel__Entity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationDom"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationDom", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationDom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationDom"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationDom", None)
                setattr(value, "UnifiedMetamodel__RelationDom", self)

    @property
    def UnifiedMetamodel__Entity28(self):
        return self.__UnifiedMetamodel__Entity28

    @UnifiedMetamodel__Entity28.setter
    def UnifiedMetamodel__Entity28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity28", None)
        self.__UnifiedMetamodel__Entity28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Property"):
                    opp_val = getattr(item, "UnifiedMetamodel__Property", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Property"):
                    opp_val = getattr(item, "UnifiedMetamodel__Property", None)
                    
                    setattr(item, "UnifiedMetamodel__Property", self)
                    

    @property
    def UnifiedMetamodel__Entity33(self):
        return self.__UnifiedMetamodel__Entity33

    @UnifiedMetamodel__Entity33.setter
    def UnifiedMetamodel__Entity33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity33", None)
        self.__UnifiedMetamodel__Entity33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationDom32"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationDom32", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationDom32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationDom32"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationDom32", None)
                setattr(value, "UnifiedMetamodel__RelationDom32", self)

    @property
    def UnifiedMetamodel__Entity41(self):
        return self.__UnifiedMetamodel__Entity41

    @UnifiedMetamodel__Entity41.setter
    def UnifiedMetamodel__Entity41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity41", None)
        self.__UnifiedMetamodel__Entity41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Submodule40"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Submodule40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Submodule40"):
                opp_val = getattr(value, "UnifiedMetamodel__Submodule40", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Submodule40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Operations:

    pass
class RelationDom:

    pass
class UnifiedMetamodel__Composition(RelationDom):

    pass
class UnifiedMetamodel__ArquitectureMetamodel:

    pass
class UnifiedMetamodel__RelationArch:

    def __init__(self, name: str, UnifiedMetamodel__RelationArch17: "UnifiedMetamodel__ArquitectureMetamodel" = None, UnifiedMetamodel__RelationArch: "UnifiedMetamodel__Layer" = None, UnifiedMetamodel__RelationArch11: "UnifiedMetamodel__Layer" = None):
        self.name = name
        self.UnifiedMetamodel__RelationArch17 = UnifiedMetamodel__RelationArch17
        self.UnifiedMetamodel__RelationArch = UnifiedMetamodel__RelationArch
        self.UnifiedMetamodel__RelationArch11 = UnifiedMetamodel__RelationArch11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__RelationArch11(self):
        return self.__UnifiedMetamodel__RelationArch11

    @UnifiedMetamodel__RelationArch11.setter
    def UnifiedMetamodel__RelationArch11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__RelationArch__UnifiedMetamodel__RelationArch11", None)
        self.__UnifiedMetamodel__RelationArch11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Layer12"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Layer12", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Layer12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Layer12"):
                opp_val = getattr(value, "UnifiedMetamodel__Layer12", None)
                setattr(value, "UnifiedMetamodel__Layer12", self)

    @property
    def UnifiedMetamodel__RelationArch17(self):
        return self.__UnifiedMetamodel__RelationArch17

    @UnifiedMetamodel__RelationArch17.setter
    def UnifiedMetamodel__RelationArch17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__RelationArch__UnifiedMetamodel__RelationArch17", None)
        self.__UnifiedMetamodel__RelationArch17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel16"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ArquitectureMetamodel16"):
                opp_val = getattr(value, "UnifiedMetamodel__ArquitectureMetamodel16", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ArquitectureMetamodel16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__RelationArch(self):
        return self.__UnifiedMetamodel__RelationArch

    @UnifiedMetamodel__RelationArch.setter
    def UnifiedMetamodel__RelationArch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__RelationArch__UnifiedMetamodel__RelationArch", None)
        self.__UnifiedMetamodel__RelationArch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Layer9"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Layer9", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Layer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Layer9"):
                opp_val = getattr(value, "UnifiedMetamodel__Layer9", None)
                setattr(value, "UnifiedMetamodel__Layer9", self)

class UnifiedMetamodel__TechnologyMetamodel:

    pass
class UnifiedMetamodel__DomainMetamodel:

    pass
class UnifiedMetamodel__Metamodel:

    def __init__(self, name: str, UnifiedMetamodel__Metamodel: "UnifiedMetamodel__ArquitectureMetamodel" = None, UnifiedMetamodel__Metamodel21: "UnifiedMetamodel__DomainMetamodel" = None, UnifiedMetamodel__Metamodel23: "UnifiedMetamodel__TechnologyMetamodel" = None):
        self.name = name
        self.UnifiedMetamodel__Metamodel = UnifiedMetamodel__Metamodel
        self.UnifiedMetamodel__Metamodel21 = UnifiedMetamodel__Metamodel21
        self.UnifiedMetamodel__Metamodel23 = UnifiedMetamodel__Metamodel23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Metamodel(self):
        return self.__UnifiedMetamodel__Metamodel

    @UnifiedMetamodel__Metamodel.setter
    def UnifiedMetamodel__Metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Metamodel__UnifiedMetamodel__Metamodel", None)
        self.__UnifiedMetamodel__Metamodel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel19"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel19", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ArquitectureMetamodel19"):
                opp_val = getattr(value, "UnifiedMetamodel__ArquitectureMetamodel19", None)
                setattr(value, "UnifiedMetamodel__ArquitectureMetamodel19", self)

    @property
    def UnifiedMetamodel__Metamodel23(self):
        return self.__UnifiedMetamodel__Metamodel23

    @UnifiedMetamodel__Metamodel23.setter
    def UnifiedMetamodel__Metamodel23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Metamodel__UnifiedMetamodel__Metamodel23", None)
        self.__UnifiedMetamodel__Metamodel23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__TechnologyMetamodel"):
                opp_val = getattr(old_value, "UnifiedMetamodel__TechnologyMetamodel", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__TechnologyMetamodel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__TechnologyMetamodel"):
                opp_val = getattr(value, "UnifiedMetamodel__TechnologyMetamodel", None)
                setattr(value, "UnifiedMetamodel__TechnologyMetamodel", self)

    @property
    def UnifiedMetamodel__Metamodel21(self):
        return self.__UnifiedMetamodel__Metamodel21

    @UnifiedMetamodel__Metamodel21.setter
    def UnifiedMetamodel__Metamodel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Metamodel__UnifiedMetamodel__Metamodel21", None)
        self.__UnifiedMetamodel__Metamodel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__DomainMetamodel"):
                opp_val = getattr(old_value, "UnifiedMetamodel__DomainMetamodel", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__DomainMetamodel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__DomainMetamodel"):
                opp_val = getattr(value, "UnifiedMetamodel__DomainMetamodel", None)
                setattr(value, "UnifiedMetamodel__DomainMetamodel", self)

class LayerSegment:

    pass
class UnifiedMetamodel__Util(LayerSegment):

    pass
class UnifiedMetamodel__Pojo(LayerSegment):

    pass
class UnifiedMetamodel__Containers(LayerSegment):

    pass
class UnifiedMetamodel__Services(LayerSegment):

    pass
class UnifiedMetamodel__Dto(LayerSegment):

    pass
class UnifiedMetamodel__SubLayerSegment:

    pass
class UnifiedMetamodel__LayerSegment:

    pass
class UnifiedMetamodel__Component:

    def __init__(self, name: str, UnifiedMetamodel__Component: set["UnifiedMetamodel__Layer"] = None, UnifiedMetamodel__Component14: "UnifiedMetamodel__ArquitectureMetamodel" = None):
        self.name = name
        self.UnifiedMetamodel__Component = UnifiedMetamodel__Component if UnifiedMetamodel__Component is not None else set()
        self.UnifiedMetamodel__Component14 = UnifiedMetamodel__Component14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Component(self):
        return self.__UnifiedMetamodel__Component

    @UnifiedMetamodel__Component.setter
    def UnifiedMetamodel__Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Component__UnifiedMetamodel__Component", None)
        self.__UnifiedMetamodel__Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Layer7"):
                    opp_val = getattr(item, "UnifiedMetamodel__Layer7", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Layer7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Layer7"):
                    opp_val = getattr(item, "UnifiedMetamodel__Layer7", None)
                    
                    setattr(item, "UnifiedMetamodel__Layer7", self)
                    

    @property
    def UnifiedMetamodel__Component14(self):
        return self.__UnifiedMetamodel__Component14

    @UnifiedMetamodel__Component14.setter
    def UnifiedMetamodel__Component14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Component__UnifiedMetamodel__Component14", None)
        self.__UnifiedMetamodel__Component14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ArquitectureMetamodel"):
                opp_val = getattr(value, "UnifiedMetamodel__ArquitectureMetamodel", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ArquitectureMetamodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Facade(LayerSegment):

    pass
class UnifiedMetamodel__RestEntity(LayerSegment):

    pass
class UnifiedMetamodel__Layer:

    def __init__(self, name: str, UnifiedMetamodel__Layer: set["UnifiedMetamodel__LayerSegment"] = None, UnifiedMetamodel__Layer7: "UnifiedMetamodel__Component" = None, UnifiedMetamodel__Layer9: "UnifiedMetamodel__RelationArch" = None, UnifiedMetamodel__Layer12: "UnifiedMetamodel__RelationArch" = None):
        self.name = name
        self.UnifiedMetamodel__Layer = UnifiedMetamodel__Layer if UnifiedMetamodel__Layer is not None else set()
        self.UnifiedMetamodel__Layer7 = UnifiedMetamodel__Layer7
        self.UnifiedMetamodel__Layer9 = UnifiedMetamodel__Layer9
        self.UnifiedMetamodel__Layer12 = UnifiedMetamodel__Layer12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Layer7(self):
        return self.__UnifiedMetamodel__Layer7

    @UnifiedMetamodel__Layer7.setter
    def UnifiedMetamodel__Layer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer7", None)
        self.__UnifiedMetamodel__Layer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Component"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Component"):
                opp_val = getattr(value, "UnifiedMetamodel__Component", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Layer(self):
        return self.__UnifiedMetamodel__Layer

    @UnifiedMetamodel__Layer.setter
    def UnifiedMetamodel__Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer", None)
        self.__UnifiedMetamodel__Layer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment5"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment5", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__LayerSegment5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment5"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment5", None)
                    
                    setattr(item, "UnifiedMetamodel__LayerSegment5", self)
                    

    @property
    def UnifiedMetamodel__Layer9(self):
        return self.__UnifiedMetamodel__Layer9

    @UnifiedMetamodel__Layer9.setter
    def UnifiedMetamodel__Layer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer9", None)
        self.__UnifiedMetamodel__Layer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationArch"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationArch", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationArch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationArch"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationArch", None)
                setattr(value, "UnifiedMetamodel__RelationArch", self)

    @property
    def UnifiedMetamodel__Layer12(self):
        return self.__UnifiedMetamodel__Layer12

    @UnifiedMetamodel__Layer12.setter
    def UnifiedMetamodel__Layer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer12", None)
        self.__UnifiedMetamodel__Layer12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationArch11"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationArch11", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationArch11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationArch11"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationArch11", None)
                setattr(value, "UnifiedMetamodel__RelationArch11", self)

class UnifiedMetamodel__UI(LayerSegment):

    pass
class UnifiedMetamodel__Store(LayerSegment):

    pass
class Layer:

    pass
class UnifiedMetamodel__War(Layer):

    pass
class UnifiedMetamodel__JavaScript(Layer):

    pass
class UnifiedMetamodel__Ejb(Layer):

    pass