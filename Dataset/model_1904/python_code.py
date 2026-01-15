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
class UnifiedMetamodel__Descriptor:

    def __init__(self, name: str, path: str, UnifiedMetamodel__Descriptor: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__Descriptor159: "UnifiedMetamodel__Subproject" = None):
        self.name = name
        self.path = path
        self.UnifiedMetamodel__Descriptor = UnifiedMetamodel__Descriptor
        self.UnifiedMetamodel__Descriptor159 = UnifiedMetamodel__Descriptor159
        
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
    def UnifiedMetamodel__Descriptor159(self):
        return self.__UnifiedMetamodel__Descriptor159

    @UnifiedMetamodel__Descriptor159.setter
    def UnifiedMetamodel__Descriptor159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Descriptor__UnifiedMetamodel__Descriptor159", None)
        self.__UnifiedMetamodel__Descriptor159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Subproject158"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Subproject158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Subproject158"):
                opp_val = getattr(value, "UnifiedMetamodel__Subproject158", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Subproject158", set([self]))
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
            if hasattr(old_value, "UnifiedMetamodel__Annotation156"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation156", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation156"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation156", None)
                setattr(value, "UnifiedMetamodel__Annotation156", self)

class UnifiedMetamodel__MethodBack:

    def __init__(self, name: str, UnifiedMetamodel__MethodBack151: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__MethodBack: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__MethodBack136: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__MethodBack139: set["UnifiedMetamodel__EClass"] = None):
        self.name = name
        self.UnifiedMetamodel__MethodBack151 = UnifiedMetamodel__MethodBack151
        self.UnifiedMetamodel__MethodBack = UnifiedMetamodel__MethodBack
        self.UnifiedMetamodel__MethodBack136 = UnifiedMetamodel__MethodBack136
        self.UnifiedMetamodel__MethodBack139 = UnifiedMetamodel__MethodBack139 if UnifiedMetamodel__MethodBack139 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "UnifiedMetamodel__Annotation134"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation134", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation134"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation134", None)
                setattr(value, "UnifiedMetamodel__Annotation134", self)

    @property
    def UnifiedMetamodel__MethodBack136(self):
        return self.__UnifiedMetamodel__MethodBack136

    @UnifiedMetamodel__MethodBack136.setter
    def UnifiedMetamodel__MethodBack136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack136", None)
        self.__UnifiedMetamodel__MethodBack136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass137"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass137", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass137"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass137", None)
                setattr(value, "UnifiedMetamodel__EClass137", self)

    @property
    def UnifiedMetamodel__MethodBack151(self):
        return self.__UnifiedMetamodel__MethodBack151

    @UnifiedMetamodel__MethodBack151.setter
    def UnifiedMetamodel__MethodBack151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack151", None)
        self.__UnifiedMetamodel__MethodBack151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass150"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass150"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass150", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__EClass150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__MethodBack139(self):
        return self.__UnifiedMetamodel__MethodBack139

    @UnifiedMetamodel__MethodBack139.setter
    def UnifiedMetamodel__MethodBack139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__MethodBack__UnifiedMetamodel__MethodBack139", None)
        self.__UnifiedMetamodel__MethodBack139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__EClass140"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass140", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__EClass140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__EClass140"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass140", None)
                    
                    setattr(item, "UnifiedMetamodel__EClass140", self)
                    

class UnifiedMetamodel__EClass:

    def __init__(self, name: str, UnifiedMetamodel__EClass145: "UnifiedMetamodel__Epackage" = None, UnifiedMetamodel__EClass147: set["UnifiedMetamodel__Attribute"] = None, UnifiedMetamodel__EClass150: set["UnifiedMetamodel__MethodBack"] = None, UnifiedMetamodel__EClass153: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__EClass: "UnifiedMetamodel__Attribute" = None, UnifiedMetamodel__EClass137: "UnifiedMetamodel__MethodBack" = None, UnifiedMetamodel__EClass140: "UnifiedMetamodel__MethodBack" = None, UnifiedMetamodel__EClass168: "UnifiedMetamodel__AbstractMethod" = None, UnifiedMetamodel__EClass171: "UnifiedMetamodel__AbstractMethod" = None):
        self.name = name
        self.UnifiedMetamodel__EClass145 = UnifiedMetamodel__EClass145
        self.UnifiedMetamodel__EClass147 = UnifiedMetamodel__EClass147 if UnifiedMetamodel__EClass147 is not None else set()
        self.UnifiedMetamodel__EClass150 = UnifiedMetamodel__EClass150 if UnifiedMetamodel__EClass150 is not None else set()
        self.UnifiedMetamodel__EClass153 = UnifiedMetamodel__EClass153
        self.UnifiedMetamodel__EClass = UnifiedMetamodel__EClass
        self.UnifiedMetamodel__EClass137 = UnifiedMetamodel__EClass137
        self.UnifiedMetamodel__EClass140 = UnifiedMetamodel__EClass140
        self.UnifiedMetamodel__EClass168 = UnifiedMetamodel__EClass168
        self.UnifiedMetamodel__EClass171 = UnifiedMetamodel__EClass171
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__EClass137(self):
        return self.__UnifiedMetamodel__EClass137

    @UnifiedMetamodel__EClass137.setter
    def UnifiedMetamodel__EClass137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass137", None)
        self.__UnifiedMetamodel__EClass137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__MethodBack136"):
                opp_val = getattr(old_value, "UnifiedMetamodel__MethodBack136", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__MethodBack136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__MethodBack136"):
                opp_val = getattr(value, "UnifiedMetamodel__MethodBack136", None)
                setattr(value, "UnifiedMetamodel__MethodBack136", self)

    @property
    def UnifiedMetamodel__EClass147(self):
        return self.__UnifiedMetamodel__EClass147

    @UnifiedMetamodel__EClass147.setter
    def UnifiedMetamodel__EClass147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass147", None)
        self.__UnifiedMetamodel__EClass147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Attribute148"):
                    opp_val = getattr(item, "UnifiedMetamodel__Attribute148", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Attribute148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Attribute148"):
                    opp_val = getattr(item, "UnifiedMetamodel__Attribute148", None)
                    
                    setattr(item, "UnifiedMetamodel__Attribute148", self)
                    

    @property
    def UnifiedMetamodel__EClass145(self):
        return self.__UnifiedMetamodel__EClass145

    @UnifiedMetamodel__EClass145.setter
    def UnifiedMetamodel__EClass145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass145", None)
        self.__UnifiedMetamodel__EClass145 = value
        
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
    def UnifiedMetamodel__EClass140(self):
        return self.__UnifiedMetamodel__EClass140

    @UnifiedMetamodel__EClass140.setter
    def UnifiedMetamodel__EClass140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass140", None)
        self.__UnifiedMetamodel__EClass140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__MethodBack139"):
                opp_val = getattr(old_value, "UnifiedMetamodel__MethodBack139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__MethodBack139"):
                opp_val = getattr(value, "UnifiedMetamodel__MethodBack139", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__MethodBack139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__EClass153(self):
        return self.__UnifiedMetamodel__EClass153

    @UnifiedMetamodel__EClass153.setter
    def UnifiedMetamodel__EClass153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass153", None)
        self.__UnifiedMetamodel__EClass153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Annotation154"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation154", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation154"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation154", None)
                setattr(value, "UnifiedMetamodel__Annotation154", self)

    @property
    def UnifiedMetamodel__EClass171(self):
        return self.__UnifiedMetamodel__EClass171

    @UnifiedMetamodel__EClass171.setter
    def UnifiedMetamodel__EClass171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass171", None)
        self.__UnifiedMetamodel__EClass171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__AbstractMethod170"):
                opp_val = getattr(old_value, "UnifiedMetamodel__AbstractMethod170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__AbstractMethod170"):
                opp_val = getattr(value, "UnifiedMetamodel__AbstractMethod170", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__AbstractMethod170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__EClass168(self):
        return self.__UnifiedMetamodel__EClass168

    @UnifiedMetamodel__EClass168.setter
    def UnifiedMetamodel__EClass168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass168", None)
        self.__UnifiedMetamodel__EClass168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__AbstractMethod167"):
                opp_val = getattr(old_value, "UnifiedMetamodel__AbstractMethod167", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__AbstractMethod167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__AbstractMethod167"):
                opp_val = getattr(value, "UnifiedMetamodel__AbstractMethod167", None)
                setattr(value, "UnifiedMetamodel__AbstractMethod167", self)

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
            if hasattr(old_value, "UnifiedMetamodel__Attribute128"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Attribute128", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Attribute128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Attribute128"):
                opp_val = getattr(value, "UnifiedMetamodel__Attribute128", None)
                setattr(value, "UnifiedMetamodel__Attribute128", self)

    @property
    def UnifiedMetamodel__EClass150(self):
        return self.__UnifiedMetamodel__EClass150

    @UnifiedMetamodel__EClass150.setter
    def UnifiedMetamodel__EClass150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EClass__UnifiedMetamodel__EClass150", None)
        self.__UnifiedMetamodel__EClass150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__MethodBack151"):
                    opp_val = getattr(item, "UnifiedMetamodel__MethodBack151", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__MethodBack151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__MethodBack151"):
                    opp_val = getattr(item, "UnifiedMetamodel__MethodBack151", None)
                    
                    setattr(item, "UnifiedMetamodel__MethodBack151", self)
                    

class UnifiedMetamodel__Attribute:

    def __init__(self, name: str, UnifiedMetamodel__Attribute148: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__Attribute: "UnifiedMetamodel__Annotation" = None, UnifiedMetamodel__Attribute128: "UnifiedMetamodel__EClass" = None):
        self.name = name
        self.UnifiedMetamodel__Attribute148 = UnifiedMetamodel__Attribute148
        self.UnifiedMetamodel__Attribute = UnifiedMetamodel__Attribute
        self.UnifiedMetamodel__Attribute128 = UnifiedMetamodel__Attribute128
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Attribute148(self):
        return self.__UnifiedMetamodel__Attribute148

    @UnifiedMetamodel__Attribute148.setter
    def UnifiedMetamodel__Attribute148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Attribute__UnifiedMetamodel__Attribute148", None)
        self.__UnifiedMetamodel__Attribute148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass147"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass147"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass147", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__EClass147", set([self]))
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
            if hasattr(old_value, "UnifiedMetamodel__Annotation126"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Annotation126", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Annotation126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Annotation126"):
                opp_val = getattr(value, "UnifiedMetamodel__Annotation126", None)
                setattr(value, "UnifiedMetamodel__Annotation126", self)

    @property
    def UnifiedMetamodel__Attribute128(self):
        return self.__UnifiedMetamodel__Attribute128

    @UnifiedMetamodel__Attribute128.setter
    def UnifiedMetamodel__Attribute128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Attribute__UnifiedMetamodel__Attribute128", None)
        self.__UnifiedMetamodel__Attribute128 = value
        
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

class UnifiedMetamodel__Epackage:

    def __init__(self, name: str, UnifiedMetamodel__Epackage: set["UnifiedMetamodel__EClass"] = None, UnifiedMetamodel__Epackage162: "UnifiedMetamodel__Subproject" = None):
        self.name = name
        self.UnifiedMetamodel__Epackage = UnifiedMetamodel__Epackage if UnifiedMetamodel__Epackage is not None else set()
        self.UnifiedMetamodel__Epackage162 = UnifiedMetamodel__Epackage162
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Epackage162(self):
        return self.__UnifiedMetamodel__Epackage162

    @UnifiedMetamodel__Epackage162.setter
    def UnifiedMetamodel__Epackage162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Epackage__UnifiedMetamodel__Epackage162", None)
        self.__UnifiedMetamodel__Epackage162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Subproject161"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Subproject161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Subproject161"):
                opp_val = getattr(value, "UnifiedMetamodel__Subproject161", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Subproject161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "UnifiedMetamodel__EClass145"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass145", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__EClass145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__EClass145"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass145", None)
                    
                    setattr(item, "UnifiedMetamodel__EClass145", self)
                    

class EClass:

    pass
class UnifiedMetamodel__AbstractClass(EClass):

    pass
class UnifiedMetamodel__GenericClass(EClass):

    pass
class UnifiedMetamodel__Annotation(EClass):

    def __init__(self, properties: str, UnifiedMetamodel__Annotation154: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__Annotation: "UnifiedMetamodel__Library" = None, UnifiedMetamodel__Annotation126: "UnifiedMetamodel__Attribute" = None, UnifiedMetamodel__Annotation134: "UnifiedMetamodel__MethodBack" = None, UnifiedMetamodel__Annotation156: "UnifiedMetamodel__Descriptor" = None):
        self.properties = properties
        self.UnifiedMetamodel__Annotation154 = UnifiedMetamodel__Annotation154
        self.UnifiedMetamodel__Annotation = UnifiedMetamodel__Annotation
        self.UnifiedMetamodel__Annotation126 = UnifiedMetamodel__Annotation126
        self.UnifiedMetamodel__Annotation134 = UnifiedMetamodel__Annotation134
        self.UnifiedMetamodel__Annotation156 = UnifiedMetamodel__Annotation156
        
    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def UnifiedMetamodel__Annotation126(self):
        return self.__UnifiedMetamodel__Annotation126

    @UnifiedMetamodel__Annotation126.setter
    def UnifiedMetamodel__Annotation126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation126", None)
        self.__UnifiedMetamodel__Annotation126 = value
        
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

    @property
    def UnifiedMetamodel__Annotation154(self):
        return self.__UnifiedMetamodel__Annotation154

    @UnifiedMetamodel__Annotation154.setter
    def UnifiedMetamodel__Annotation154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation154", None)
        self.__UnifiedMetamodel__Annotation154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass153"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass153", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass153"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass153", None)
                setattr(value, "UnifiedMetamodel__EClass153", self)

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
            if hasattr(old_value, "UnifiedMetamodel__Library124"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Library124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Library124"):
                opp_val = getattr(value, "UnifiedMetamodel__Library124", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Library124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Annotation134(self):
        return self.__UnifiedMetamodel__Annotation134

    @UnifiedMetamodel__Annotation134.setter
    def UnifiedMetamodel__Annotation134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation134", None)
        self.__UnifiedMetamodel__Annotation134 = value
        
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
    def UnifiedMetamodel__Annotation156(self):
        return self.__UnifiedMetamodel__Annotation156

    @UnifiedMetamodel__Annotation156.setter
    def UnifiedMetamodel__Annotation156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Annotation__UnifiedMetamodel__Annotation156", None)
        self.__UnifiedMetamodel__Annotation156 = value
        
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

class UnifiedMetamodel__Subproject:

    def __init__(self, name: str, UnifiedMetamodel__Subproject: "UnifiedMetamodel__JEE_Project" = None, UnifiedMetamodel__Subproject158: set["UnifiedMetamodel__Descriptor"] = None, UnifiedMetamodel__Subproject161: set["UnifiedMetamodel__Epackage"] = None, UnifiedMetamodel__Subproject164: set["UnifiedMetamodel__Library"] = None):
        self.name = name
        self.UnifiedMetamodel__Subproject = UnifiedMetamodel__Subproject
        self.UnifiedMetamodel__Subproject158 = UnifiedMetamodel__Subproject158 if UnifiedMetamodel__Subproject158 is not None else set()
        self.UnifiedMetamodel__Subproject161 = UnifiedMetamodel__Subproject161 if UnifiedMetamodel__Subproject161 is not None else set()
        self.UnifiedMetamodel__Subproject164 = UnifiedMetamodel__Subproject164 if UnifiedMetamodel__Subproject164 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Subproject158(self):
        return self.__UnifiedMetamodel__Subproject158

    @UnifiedMetamodel__Subproject158.setter
    def UnifiedMetamodel__Subproject158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject158", None)
        self.__UnifiedMetamodel__Subproject158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Descriptor159"):
                    opp_val = getattr(item, "UnifiedMetamodel__Descriptor159", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Descriptor159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Descriptor159"):
                    opp_val = getattr(item, "UnifiedMetamodel__Descriptor159", None)
                    
                    setattr(item, "UnifiedMetamodel__Descriptor159", self)
                    

    @property
    def UnifiedMetamodel__Subproject161(self):
        return self.__UnifiedMetamodel__Subproject161

    @UnifiedMetamodel__Subproject161.setter
    def UnifiedMetamodel__Subproject161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject161", None)
        self.__UnifiedMetamodel__Subproject161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Epackage162"):
                    opp_val = getattr(item, "UnifiedMetamodel__Epackage162", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Epackage162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Epackage162"):
                    opp_val = getattr(item, "UnifiedMetamodel__Epackage162", None)
                    
                    setattr(item, "UnifiedMetamodel__Epackage162", self)
                    

    @property
    def UnifiedMetamodel__Subproject164(self):
        return self.__UnifiedMetamodel__Subproject164

    @UnifiedMetamodel__Subproject164.setter
    def UnifiedMetamodel__Subproject164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Subproject__UnifiedMetamodel__Subproject164", None)
        self.__UnifiedMetamodel__Subproject164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Library165"):
                    opp_val = getattr(item, "UnifiedMetamodel__Library165", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Library165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Library165"):
                    opp_val = getattr(item, "UnifiedMetamodel__Library165", None)
                    
                    setattr(item, "UnifiedMetamodel__Library165", self)
                    

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
            if hasattr(old_value, "UnifiedMetamodel__JEE_Project120"):
                opp_val = getattr(old_value, "UnifiedMetamodel__JEE_Project120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__JEE_Project120"):
                opp_val = getattr(value, "UnifiedMetamodel__JEE_Project120", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__JEE_Project120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__JEE_Project:

    def __init__(self, name: str, UnifiedMetamodel__JEE_Project: "UnifiedMetamodel__JavaApp" = None, UnifiedMetamodel__JEE_Project120: set["UnifiedMetamodel__Subproject"] = None):
        self.name = name
        self.UnifiedMetamodel__JEE_Project = UnifiedMetamodel__JEE_Project
        self.UnifiedMetamodel__JEE_Project120 = UnifiedMetamodel__JEE_Project120 if UnifiedMetamodel__JEE_Project120 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "UnifiedMetamodel__JavaApp118"):
                opp_val = getattr(old_value, "UnifiedMetamodel__JavaApp118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__JavaApp118"):
                opp_val = getattr(value, "UnifiedMetamodel__JavaApp118", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__JavaApp118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__JEE_Project120(self):
        return self.__UnifiedMetamodel__JEE_Project120

    @UnifiedMetamodel__JEE_Project120.setter
    def UnifiedMetamodel__JEE_Project120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__JEE_Project__UnifiedMetamodel__JEE_Project120", None)
        self.__UnifiedMetamodel__JEE_Project120 = value if value is not None else set()
        
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
                    

class UnifiedMetamodel__JavaApp:

    pass
class UnifiedMetamodel__Library:

    def __init__(self, name: str, isNative: bool, UnifiedMetamodel__Library: set["UnifiedMetamodel__NativeClass"] = None, UnifiedMetamodel__Library124: set["UnifiedMetamodel__Annotation"] = None, UnifiedMetamodel__Library165: "UnifiedMetamodel__Subproject" = None):
        self.name = name
        self.isNative = isNative
        self.UnifiedMetamodel__Library = UnifiedMetamodel__Library if UnifiedMetamodel__Library is not None else set()
        self.UnifiedMetamodel__Library124 = UnifiedMetamodel__Library124 if UnifiedMetamodel__Library124 is not None else set()
        self.UnifiedMetamodel__Library165 = UnifiedMetamodel__Library165
        
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
    def UnifiedMetamodel__Library165(self):
        return self.__UnifiedMetamodel__Library165

    @UnifiedMetamodel__Library165.setter
    def UnifiedMetamodel__Library165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Library__UnifiedMetamodel__Library165", None)
        self.__UnifiedMetamodel__Library165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Subproject164"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Subproject164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Subproject164"):
                opp_val = getattr(value, "UnifiedMetamodel__Subproject164", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Subproject164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Library124(self):
        return self.__UnifiedMetamodel__Library124

    @UnifiedMetamodel__Library124.setter
    def UnifiedMetamodel__Library124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Library__UnifiedMetamodel__Library124", None)
        self.__UnifiedMetamodel__Library124 = value if value is not None else set()
        
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
                    

class UnifiedMetamodel__AbstractMethod:

    def __init__(self, name: str, UnifiedMetamodel__AbstractMethod: "UnifiedMetamodel__EInterface" = None, UnifiedMetamodel__AbstractMethod143: "UnifiedMetamodel__AbstractClass" = None, UnifiedMetamodel__AbstractMethod167: "UnifiedMetamodel__EClass" = None, UnifiedMetamodel__AbstractMethod170: set["UnifiedMetamodel__EClass"] = None):
        self.name = name
        self.UnifiedMetamodel__AbstractMethod = UnifiedMetamodel__AbstractMethod
        self.UnifiedMetamodel__AbstractMethod143 = UnifiedMetamodel__AbstractMethod143
        self.UnifiedMetamodel__AbstractMethod167 = UnifiedMetamodel__AbstractMethod167
        self.UnifiedMetamodel__AbstractMethod170 = UnifiedMetamodel__AbstractMethod170 if UnifiedMetamodel__AbstractMethod170 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__AbstractMethod170(self):
        return self.__UnifiedMetamodel__AbstractMethod170

    @UnifiedMetamodel__AbstractMethod170.setter
    def UnifiedMetamodel__AbstractMethod170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod170", None)
        self.__UnifiedMetamodel__AbstractMethod170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__EClass171"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass171", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__EClass171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__EClass171"):
                    opp_val = getattr(item, "UnifiedMetamodel__EClass171", None)
                    
                    setattr(item, "UnifiedMetamodel__EClass171", self)
                    

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
    def UnifiedMetamodel__AbstractMethod167(self):
        return self.__UnifiedMetamodel__AbstractMethod167

    @UnifiedMetamodel__AbstractMethod167.setter
    def UnifiedMetamodel__AbstractMethod167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod167", None)
        self.__UnifiedMetamodel__AbstractMethod167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__EClass168"):
                opp_val = getattr(old_value, "UnifiedMetamodel__EClass168", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__EClass168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__EClass168"):
                opp_val = getattr(value, "UnifiedMetamodel__EClass168", None)
                setattr(value, "UnifiedMetamodel__EClass168", self)

    @property
    def UnifiedMetamodel__AbstractMethod143(self):
        return self.__UnifiedMetamodel__AbstractMethod143

    @UnifiedMetamodel__AbstractMethod143.setter
    def UnifiedMetamodel__AbstractMethod143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__AbstractMethod__UnifiedMetamodel__AbstractMethod143", None)
        self.__UnifiedMetamodel__AbstractMethod143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__AbstractClass142"):
                opp_val = getattr(old_value, "UnifiedMetamodel__AbstractClass142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__AbstractClass142"):
                opp_val = getattr(value, "UnifiedMetamodel__AbstractClass142", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__AbstractClass142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__EInterface:

    def __init__(self, name: str, UnifiedMetamodel__EInterface: set["UnifiedMetamodel__AbstractMethod"] = None, UnifiedMetamodel__EInterface130: "UnifiedMetamodel__GenericClass" = None):
        self.name = name
        self.UnifiedMetamodel__EInterface = UnifiedMetamodel__EInterface if UnifiedMetamodel__EInterface is not None else set()
        self.UnifiedMetamodel__EInterface130 = UnifiedMetamodel__EInterface130
        
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
    def UnifiedMetamodel__EInterface130(self):
        return self.__UnifiedMetamodel__EInterface130

    @UnifiedMetamodel__EInterface130.setter
    def UnifiedMetamodel__EInterface130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__EInterface__UnifiedMetamodel__EInterface130", None)
        self.__UnifiedMetamodel__EInterface130 = value
        
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

class UnifiedMetamodel__ReactApp:

    pass
class UnifiedMetamodel__ComponentFront:

    def __init__(self, name: str, UnifiedMetamodel__ComponentFront: "UnifiedMetamodel__Functionality" = None, UnifiedMetamodel__ComponentFront98: set["UnifiedMetamodel__ModuleFront"] = None, UnifiedMetamodel__ComponentFront101: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__ComponentFront = UnifiedMetamodel__ComponentFront
        self.UnifiedMetamodel__ComponentFront98 = UnifiedMetamodel__ComponentFront98 if UnifiedMetamodel__ComponentFront98 is not None else set()
        self.UnifiedMetamodel__ComponentFront101 = UnifiedMetamodel__ComponentFront101
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ComponentFront101(self):
        return self.__UnifiedMetamodel__ComponentFront101

    @UnifiedMetamodel__ComponentFront101.setter
    def UnifiedMetamodel__ComponentFront101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ComponentFront__UnifiedMetamodel__ComponentFront101", None)
        self.__UnifiedMetamodel__ComponentFront101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory102"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory102", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory102"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory102", None)
                setattr(value, "UnifiedMetamodel__Directory102", self)

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
    def UnifiedMetamodel__ComponentFront98(self):
        return self.__UnifiedMetamodel__ComponentFront98

    @UnifiedMetamodel__ComponentFront98.setter
    def UnifiedMetamodel__ComponentFront98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ComponentFront__UnifiedMetamodel__ComponentFront98", None)
        self.__UnifiedMetamodel__ComponentFront98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront99"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront99", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ModuleFront99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront99"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront99", None)
                    
                    setattr(item, "UnifiedMetamodel__ModuleFront99", self)
                    

class UnifiedMetamodel__Functionality:

    def __init__(self, name: str, UnifiedMetamodel__Functionality72: "UnifiedMetamodel__State" = None, UnifiedMetamodel__Functionality75: set["UnifiedMetamodel__ServicesFront"] = None, UnifiedMetamodel__Functionality78: "UnifiedMetamodel__Directory" = None, UnifiedMetamodel__Functionality: set["UnifiedMetamodel__ComponentFront"] = None, UnifiedMetamodel__Functionality90: "UnifiedMetamodel__ReactApp" = None):
        self.name = name
        self.UnifiedMetamodel__Functionality72 = UnifiedMetamodel__Functionality72
        self.UnifiedMetamodel__Functionality75 = UnifiedMetamodel__Functionality75 if UnifiedMetamodel__Functionality75 is not None else set()
        self.UnifiedMetamodel__Functionality78 = UnifiedMetamodel__Functionality78
        self.UnifiedMetamodel__Functionality = UnifiedMetamodel__Functionality if UnifiedMetamodel__Functionality is not None else set()
        self.UnifiedMetamodel__Functionality90 = UnifiedMetamodel__Functionality90
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Functionality72(self):
        return self.__UnifiedMetamodel__Functionality72

    @UnifiedMetamodel__Functionality72.setter
    def UnifiedMetamodel__Functionality72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality72", None)
        self.__UnifiedMetamodel__Functionality72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__State73"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State73", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__State73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State73"):
                opp_val = getattr(value, "UnifiedMetamodel__State73", None)
                setattr(value, "UnifiedMetamodel__State73", self)

    @property
    def UnifiedMetamodel__Functionality78(self):
        return self.__UnifiedMetamodel__Functionality78

    @UnifiedMetamodel__Functionality78.setter
    def UnifiedMetamodel__Functionality78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality78", None)
        self.__UnifiedMetamodel__Functionality78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory79"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory79", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory79"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory79", None)
                setattr(value, "UnifiedMetamodel__Directory79", self)

    @property
    def UnifiedMetamodel__Functionality90(self):
        return self.__UnifiedMetamodel__Functionality90

    @UnifiedMetamodel__Functionality90.setter
    def UnifiedMetamodel__Functionality90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality90", None)
        self.__UnifiedMetamodel__Functionality90 = value
        
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
    def UnifiedMetamodel__Functionality75(self):
        return self.__UnifiedMetamodel__Functionality75

    @UnifiedMetamodel__Functionality75.setter
    def UnifiedMetamodel__Functionality75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Functionality__UnifiedMetamodel__Functionality75", None)
        self.__UnifiedMetamodel__Functionality75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ServicesFront76"):
                    opp_val = getattr(item, "UnifiedMetamodel__ServicesFront76", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ServicesFront76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ServicesFront76"):
                    opp_val = getattr(item, "UnifiedMetamodel__ServicesFront76", None)
                    
                    setattr(item, "UnifiedMetamodel__ServicesFront76", self)
                    

class UnifiedMetamodel__ServicesFront:

    def __init__(self, name: str, UnifiedMetamodel__ServicesFront76: "UnifiedMetamodel__Functionality" = None, UnifiedMetamodel__ServicesFront: set["UnifiedMetamodel__ModuleFront"] = None, UnifiedMetamodel__ServicesFront68: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__ServicesFront76 = UnifiedMetamodel__ServicesFront76
        self.UnifiedMetamodel__ServicesFront = UnifiedMetamodel__ServicesFront if UnifiedMetamodel__ServicesFront is not None else set()
        self.UnifiedMetamodel__ServicesFront68 = UnifiedMetamodel__ServicesFront68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ServicesFront76(self):
        return self.__UnifiedMetamodel__ServicesFront76

    @UnifiedMetamodel__ServicesFront76.setter
    def UnifiedMetamodel__ServicesFront76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ServicesFront__UnifiedMetamodel__ServicesFront76", None)
        self.__UnifiedMetamodel__ServicesFront76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Functionality75"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Functionality75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Functionality75"):
                opp_val = getattr(value, "UnifiedMetamodel__Functionality75", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Functionality75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "UnifiedMetamodel__ModuleFront66"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront66", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ModuleFront66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ModuleFront66"):
                    opp_val = getattr(item, "UnifiedMetamodel__ModuleFront66", None)
                    
                    setattr(item, "UnifiedMetamodel__ModuleFront66", self)
                    

    @property
    def UnifiedMetamodel__ServicesFront68(self):
        return self.__UnifiedMetamodel__ServicesFront68

    @UnifiedMetamodel__ServicesFront68.setter
    def UnifiedMetamodel__ServicesFront68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ServicesFront__UnifiedMetamodel__ServicesFront68", None)
        self.__UnifiedMetamodel__ServicesFront68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory69"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory69", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory69"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory69", None)
                setattr(value, "UnifiedMetamodel__Directory69", self)

class UIFront:

    pass
class UnifiedMetamodel__RouterComponent(UIFront):

    pass
class UnifiedMetamodel__Visualizer(UIFront):

    pass
class ComponentFront:

    pass
class UnifiedMetamodel__UIFront(ComponentFront):

    pass
class UnifiedMetamodel__ModuleFront:

    def __init__(self, name: str, UnifiedMetamodel__ModuleFront: "UnifiedMetamodel__State" = None, UnifiedMetamodel__ModuleFront66: "UnifiedMetamodel__ServicesFront" = None, UnifiedMetamodel__ModuleFront99: "UnifiedMetamodel__ComponentFront" = None, UnifiedMetamodel__ModuleFront93: "UnifiedMetamodel__ReactApp" = None, UnifiedMetamodel__ModuleFront110: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__ModuleFront = UnifiedMetamodel__ModuleFront
        self.UnifiedMetamodel__ModuleFront66 = UnifiedMetamodel__ModuleFront66
        self.UnifiedMetamodel__ModuleFront99 = UnifiedMetamodel__ModuleFront99
        self.UnifiedMetamodel__ModuleFront93 = UnifiedMetamodel__ModuleFront93
        self.UnifiedMetamodel__ModuleFront110 = UnifiedMetamodel__ModuleFront110
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ModuleFront93(self):
        return self.__UnifiedMetamodel__ModuleFront93

    @UnifiedMetamodel__ModuleFront93.setter
    def UnifiedMetamodel__ModuleFront93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront93", None)
        self.__UnifiedMetamodel__ModuleFront93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ReactApp92"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ReactApp92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ReactApp92"):
                opp_val = getattr(value, "UnifiedMetamodel__ReactApp92", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ReactApp92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ModuleFront99(self):
        return self.__UnifiedMetamodel__ModuleFront99

    @UnifiedMetamodel__ModuleFront99.setter
    def UnifiedMetamodel__ModuleFront99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront99", None)
        self.__UnifiedMetamodel__ModuleFront99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ComponentFront98"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ComponentFront98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ComponentFront98"):
                opp_val = getattr(value, "UnifiedMetamodel__ComponentFront98", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ComponentFront98", set([self]))
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
            if hasattr(old_value, "UnifiedMetamodel__State58"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State58"):
                opp_val = getattr(value, "UnifiedMetamodel__State58", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__State58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ModuleFront66(self):
        return self.__UnifiedMetamodel__ModuleFront66

    @UnifiedMetamodel__ModuleFront66.setter
    def UnifiedMetamodel__ModuleFront66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront66", None)
        self.__UnifiedMetamodel__ModuleFront66 = value
        
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
    def UnifiedMetamodel__ModuleFront110(self):
        return self.__UnifiedMetamodel__ModuleFront110

    @UnifiedMetamodel__ModuleFront110.setter
    def UnifiedMetamodel__ModuleFront110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ModuleFront__UnifiedMetamodel__ModuleFront110", None)
        self.__UnifiedMetamodel__ModuleFront110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory111"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory111", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory111"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory111", None)
                setattr(value, "UnifiedMetamodel__Directory111", self)

class UnifiedMetamodel__Reducer:

    def __init__(self, name: str, UnifiedMetamodel__Reducer: "UnifiedMetamodel__State" = None, UnifiedMetamodel__Reducer64: "UnifiedMetamodel__Container" = None, UnifiedMetamodel__Reducer104: set["UnifiedMetamodel__ActionCreator"] = None, UnifiedMetamodel__Reducer107: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__Reducer = UnifiedMetamodel__Reducer
        self.UnifiedMetamodel__Reducer64 = UnifiedMetamodel__Reducer64
        self.UnifiedMetamodel__Reducer104 = UnifiedMetamodel__Reducer104 if UnifiedMetamodel__Reducer104 is not None else set()
        self.UnifiedMetamodel__Reducer107 = UnifiedMetamodel__Reducer107
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Reducer107(self):
        return self.__UnifiedMetamodel__Reducer107

    @UnifiedMetamodel__Reducer107.setter
    def UnifiedMetamodel__Reducer107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer107", None)
        self.__UnifiedMetamodel__Reducer107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory108"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory108", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory108"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory108", None)
                setattr(value, "UnifiedMetamodel__Directory108", self)

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
            if hasattr(old_value, "UnifiedMetamodel__State56"):
                opp_val = getattr(old_value, "UnifiedMetamodel__State56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__State56"):
                opp_val = getattr(value, "UnifiedMetamodel__State56", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__State56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Reducer64(self):
        return self.__UnifiedMetamodel__Reducer64

    @UnifiedMetamodel__Reducer64.setter
    def UnifiedMetamodel__Reducer64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer64", None)
        self.__UnifiedMetamodel__Reducer64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Container63"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Container63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Container63"):
                opp_val = getattr(value, "UnifiedMetamodel__Container63", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Container63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Reducer104(self):
        return self.__UnifiedMetamodel__Reducer104

    @UnifiedMetamodel__Reducer104.setter
    def UnifiedMetamodel__Reducer104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Reducer__UnifiedMetamodel__Reducer104", None)
        self.__UnifiedMetamodel__Reducer104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator105"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator105", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ActionCreator105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator105"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator105", None)
                    
                    setattr(item, "UnifiedMetamodel__ActionCreator105", self)
                    

class UnifiedMetamodel__Action:

    def __init__(self, name: str, UnifiedMetamodel__Action: "UnifiedMetamodel__State" = None, UnifiedMetamodel__Action81: set["UnifiedMetamodel__ActionDispatcher"] = None, UnifiedMetamodel__Action84: set["UnifiedMetamodel__ActionCreator"] = None, UnifiedMetamodel__Action87: "UnifiedMetamodel__Directory" = None):
        self.name = name
        self.UnifiedMetamodel__Action = UnifiedMetamodel__Action
        self.UnifiedMetamodel__Action81 = UnifiedMetamodel__Action81 if UnifiedMetamodel__Action81 is not None else set()
        self.UnifiedMetamodel__Action84 = UnifiedMetamodel__Action84 if UnifiedMetamodel__Action84 is not None else set()
        self.UnifiedMetamodel__Action87 = UnifiedMetamodel__Action87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def UnifiedMetamodel__Action84(self):
        return self.__UnifiedMetamodel__Action84

    @UnifiedMetamodel__Action84.setter
    def UnifiedMetamodel__Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action84", None)
        self.__UnifiedMetamodel__Action84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator85"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator85", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ActionCreator85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ActionCreator85"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionCreator85", None)
                    
                    setattr(item, "UnifiedMetamodel__ActionCreator85", self)
                    

    @property
    def UnifiedMetamodel__Action87(self):
        return self.__UnifiedMetamodel__Action87

    @UnifiedMetamodel__Action87.setter
    def UnifiedMetamodel__Action87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action87", None)
        self.__UnifiedMetamodel__Action87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Directory88"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory88", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Directory88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory88"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory88", None)
                setattr(value, "UnifiedMetamodel__Directory88", self)

    @property
    def UnifiedMetamodel__Action81(self):
        return self.__UnifiedMetamodel__Action81

    @UnifiedMetamodel__Action81.setter
    def UnifiedMetamodel__Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Action__UnifiedMetamodel__Action81", None)
        self.__UnifiedMetamodel__Action81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__ActionDispatcher82"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionDispatcher82", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__ActionDispatcher82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__ActionDispatcher82"):
                    opp_val = getattr(item, "UnifiedMetamodel__ActionDispatcher82", None)
                    
                    setattr(item, "UnifiedMetamodel__ActionDispatcher82", self)
                    

class UnifiedMetamodel__State:

    pass
class UnifiedMetamodel__Container(ComponentFront):

    pass
class UnifiedMetamodel__Directory:

    def __init__(self, purpose: str, isRoot: bool, name: str, UnifiedMetamodel__Directory: "UnifiedMetamodel__Directory" = None, UnifiedMetamodel__Directory50: set["UnifiedMetamodel__Directory"] = None, UnifiedMetamodel__Directory53: set["UnifiedMetamodel__File"] = None, UnifiedMetamodel__Directory79: "UnifiedMetamodel__Functionality" = None, UnifiedMetamodel__Directory69: "UnifiedMetamodel__ServicesFront" = None, UnifiedMetamodel__Directory88: "UnifiedMetamodel__Action" = None, UnifiedMetamodel__Directory96: "UnifiedMetamodel__ReactApp" = None, UnifiedMetamodel__Directory102: "UnifiedMetamodel__ComponentFront" = None, UnifiedMetamodel__Directory108: "UnifiedMetamodel__Reducer" = None, UnifiedMetamodel__Directory111: "UnifiedMetamodel__ModuleFront" = None):
        self.purpose = purpose
        self.isRoot = isRoot
        self.name = name
        self.UnifiedMetamodel__Directory = UnifiedMetamodel__Directory
        self.UnifiedMetamodel__Directory50 = UnifiedMetamodel__Directory50 if UnifiedMetamodel__Directory50 is not None else set()
        self.UnifiedMetamodel__Directory53 = UnifiedMetamodel__Directory53 if UnifiedMetamodel__Directory53 is not None else set()
        self.UnifiedMetamodel__Directory79 = UnifiedMetamodel__Directory79
        self.UnifiedMetamodel__Directory69 = UnifiedMetamodel__Directory69
        self.UnifiedMetamodel__Directory88 = UnifiedMetamodel__Directory88
        self.UnifiedMetamodel__Directory96 = UnifiedMetamodel__Directory96
        self.UnifiedMetamodel__Directory102 = UnifiedMetamodel__Directory102
        self.UnifiedMetamodel__Directory108 = UnifiedMetamodel__Directory108
        self.UnifiedMetamodel__Directory111 = UnifiedMetamodel__Directory111
        
    @property
    def isRoot(self) -> bool:
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: bool):
        self.__isRoot = isRoot

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
    def UnifiedMetamodel__Directory53(self):
        return self.__UnifiedMetamodel__Directory53

    @UnifiedMetamodel__Directory53.setter
    def UnifiedMetamodel__Directory53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory53", None)
        self.__UnifiedMetamodel__Directory53 = value if value is not None else set()
        
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
    def UnifiedMetamodel__Directory88(self):
        return self.__UnifiedMetamodel__Directory88

    @UnifiedMetamodel__Directory88.setter
    def UnifiedMetamodel__Directory88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory88", None)
        self.__UnifiedMetamodel__Directory88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Action87"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Action87", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Action87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Action87"):
                opp_val = getattr(value, "UnifiedMetamodel__Action87", None)
                setattr(value, "UnifiedMetamodel__Action87", self)

    @property
    def UnifiedMetamodel__Directory69(self):
        return self.__UnifiedMetamodel__Directory69

    @UnifiedMetamodel__Directory69.setter
    def UnifiedMetamodel__Directory69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory69", None)
        self.__UnifiedMetamodel__Directory69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ServicesFront68"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ServicesFront68", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ServicesFront68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ServicesFront68"):
                opp_val = getattr(value, "UnifiedMetamodel__ServicesFront68", None)
                setattr(value, "UnifiedMetamodel__ServicesFront68", self)

    @property
    def UnifiedMetamodel__Directory79(self):
        return self.__UnifiedMetamodel__Directory79

    @UnifiedMetamodel__Directory79.setter
    def UnifiedMetamodel__Directory79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory79", None)
        self.__UnifiedMetamodel__Directory79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Functionality78"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Functionality78", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Functionality78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Functionality78"):
                opp_val = getattr(value, "UnifiedMetamodel__Functionality78", None)
                setattr(value, "UnifiedMetamodel__Functionality78", self)

    @property
    def UnifiedMetamodel__Directory111(self):
        return self.__UnifiedMetamodel__Directory111

    @UnifiedMetamodel__Directory111.setter
    def UnifiedMetamodel__Directory111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory111", None)
        self.__UnifiedMetamodel__Directory111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ModuleFront110"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ModuleFront110", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ModuleFront110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ModuleFront110"):
                opp_val = getattr(value, "UnifiedMetamodel__ModuleFront110", None)
                setattr(value, "UnifiedMetamodel__ModuleFront110", self)

    @property
    def UnifiedMetamodel__Directory108(self):
        return self.__UnifiedMetamodel__Directory108

    @UnifiedMetamodel__Directory108.setter
    def UnifiedMetamodel__Directory108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory108", None)
        self.__UnifiedMetamodel__Directory108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Reducer107"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Reducer107", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Reducer107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Reducer107"):
                opp_val = getattr(value, "UnifiedMetamodel__Reducer107", None)
                setattr(value, "UnifiedMetamodel__Reducer107", self)

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
            if hasattr(old_value, "UnifiedMetamodel__Directory50"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory50"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory50", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Directory50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Directory50(self):
        return self.__UnifiedMetamodel__Directory50

    @UnifiedMetamodel__Directory50.setter
    def UnifiedMetamodel__Directory50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory50", None)
        self.__UnifiedMetamodel__Directory50 = value if value is not None else set()
        
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
    def UnifiedMetamodel__Directory96(self):
        return self.__UnifiedMetamodel__Directory96

    @UnifiedMetamodel__Directory96.setter
    def UnifiedMetamodel__Directory96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory96", None)
        self.__UnifiedMetamodel__Directory96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ReactApp95"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ReactApp95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ReactApp95"):
                opp_val = getattr(value, "UnifiedMetamodel__ReactApp95", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__ReactApp95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Directory102(self):
        return self.__UnifiedMetamodel__Directory102

    @UnifiedMetamodel__Directory102.setter
    def UnifiedMetamodel__Directory102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Directory__UnifiedMetamodel__Directory102", None)
        self.__UnifiedMetamodel__Directory102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__ComponentFront101"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ComponentFront101", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ComponentFront101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ComponentFront101"):
                opp_val = getattr(value, "UnifiedMetamodel__ComponentFront101", None)
                setattr(value, "UnifiedMetamodel__ComponentFront101", self)

class File:

    pass
class UnifiedMetamodel__CSS(File):

    pass
class UnifiedMetamodel__MD(File):

    pass
class UnifiedMetamodel__JS(File):

    pass
class UnifiedMetamodel__JSON(File):

    pass
class ModuleFront:

    pass
class UnifiedMetamodel__APICall(ModuleFront):

    pass
class UnifiedMetamodel__Design(ModuleFront):

    pass
class UnifiedMetamodel__Redux(ModuleFront):

    pass
class UnifiedMetamodel__Router(ModuleFront):

    pass
class UnifiedMetamodel__ActionCreator:

    def __init__(self, name: str, UnifiedMetamodel__ActionCreator: "UnifiedMetamodel__ActionDispatcher" = None, UnifiedMetamodel__ActionCreator85: "UnifiedMetamodel__Action" = None, UnifiedMetamodel__ActionCreator105: "UnifiedMetamodel__Reducer" = None):
        self.name = name
        self.UnifiedMetamodel__ActionCreator = UnifiedMetamodel__ActionCreator
        self.UnifiedMetamodel__ActionCreator85 = UnifiedMetamodel__ActionCreator85
        self.UnifiedMetamodel__ActionCreator105 = UnifiedMetamodel__ActionCreator105
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ActionCreator85(self):
        return self.__UnifiedMetamodel__ActionCreator85

    @UnifiedMetamodel__ActionCreator85.setter
    def UnifiedMetamodel__ActionCreator85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionCreator__UnifiedMetamodel__ActionCreator85", None)
        self.__UnifiedMetamodel__ActionCreator85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Action84"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Action84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Action84"):
                opp_val = getattr(value, "UnifiedMetamodel__Action84", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Action84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ActionCreator105(self):
        return self.__UnifiedMetamodel__ActionCreator105

    @UnifiedMetamodel__ActionCreator105.setter
    def UnifiedMetamodel__ActionCreator105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionCreator__UnifiedMetamodel__ActionCreator105", None)
        self.__UnifiedMetamodel__ActionCreator105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Reducer104"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Reducer104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Reducer104"):
                opp_val = getattr(value, "UnifiedMetamodel__Reducer104", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Reducer104", set([self]))
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

    def __init__(self, name: str, UnifiedMetamodel__ActionDispatcher: "UnifiedMetamodel__ActionCreator" = None, UnifiedMetamodel__ActionDispatcher61: "UnifiedMetamodel__Container" = None, UnifiedMetamodel__ActionDispatcher82: "UnifiedMetamodel__Action" = None):
        self.name = name
        self.UnifiedMetamodel__ActionDispatcher = UnifiedMetamodel__ActionDispatcher
        self.UnifiedMetamodel__ActionDispatcher61 = UnifiedMetamodel__ActionDispatcher61
        self.UnifiedMetamodel__ActionDispatcher82 = UnifiedMetamodel__ActionDispatcher82
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__ActionDispatcher82(self):
        return self.__UnifiedMetamodel__ActionDispatcher82

    @UnifiedMetamodel__ActionDispatcher82.setter
    def UnifiedMetamodel__ActionDispatcher82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionDispatcher__UnifiedMetamodel__ActionDispatcher82", None)
        self.__UnifiedMetamodel__ActionDispatcher82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Action81"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Action81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Action81"):
                opp_val = getattr(value, "UnifiedMetamodel__Action81", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Action81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__ActionDispatcher61(self):
        return self.__UnifiedMetamodel__ActionDispatcher61

    @UnifiedMetamodel__ActionDispatcher61.setter
    def UnifiedMetamodel__ActionDispatcher61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__ActionDispatcher__UnifiedMetamodel__ActionDispatcher61", None)
        self.__UnifiedMetamodel__ActionDispatcher61 = value
        
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

class UnifiedMetamodel__File:

    def __init__(self, type: str, name: str, UnifiedMetamodel__File: "UnifiedMetamodel__Directory" = None):
        self.type = type
        self.name = name
        self.UnifiedMetamodel__File = UnifiedMetamodel__File
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "UnifiedMetamodel__Directory53"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Directory53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Directory53"):
                opp_val = getattr(value, "UnifiedMetamodel__Directory53", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Directory53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "UnifiedMetamodel__Entity29"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Entity29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Entity29"):
                opp_val = getattr(value, "UnifiedMetamodel__Entity29", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Entity29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnifiedMetamodel__Transaction:

    pass
class Entity:

    pass
class UnifiedMetamodel__GeneralEntity(Entity):

    pass
class UnifiedMetamodel__SpecialEntity(Entity):

    pass
class UnifiedMetamodel__Submodule:

    def __init__(self, name: str, UnifiedMetamodel__Submodule38: set["UnifiedMetamodel__Operations"] = None, UnifiedMetamodel__Submodule: "UnifiedMetamodel__Module" = None, UnifiedMetamodel__Submodule41: set["UnifiedMetamodel__Entity"] = None):
        self.name = name
        self.UnifiedMetamodel__Submodule38 = UnifiedMetamodel__Submodule38 if UnifiedMetamodel__Submodule38 is not None else set()
        self.UnifiedMetamodel__Submodule = UnifiedMetamodel__Submodule
        self.UnifiedMetamodel__Submodule41 = UnifiedMetamodel__Submodule41 if UnifiedMetamodel__Submodule41 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Submodule38(self):
        return self.__UnifiedMetamodel__Submodule38

    @UnifiedMetamodel__Submodule38.setter
    def UnifiedMetamodel__Submodule38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Submodule__UnifiedMetamodel__Submodule38", None)
        self.__UnifiedMetamodel__Submodule38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Operations39"):
                    opp_val = getattr(item, "UnifiedMetamodel__Operations39", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Operations39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Operations39"):
                    opp_val = getattr(item, "UnifiedMetamodel__Operations39", None)
                    
                    setattr(item, "UnifiedMetamodel__Operations39", self)
                    

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
    def UnifiedMetamodel__Submodule41(self):
        return self.__UnifiedMetamodel__Submodule41

    @UnifiedMetamodel__Submodule41.setter
    def UnifiedMetamodel__Submodule41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Submodule__UnifiedMetamodel__Submodule41", None)
        self.__UnifiedMetamodel__Submodule41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__Entity42"):
                    opp_val = getattr(item, "UnifiedMetamodel__Entity42", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Entity42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Entity42"):
                    opp_val = getattr(item, "UnifiedMetamodel__Entity42", None)
                    
                    setattr(item, "UnifiedMetamodel__Entity42", self)
                    

class UnifiedMetamodel__Module:

    def __init__(self, name: str, UnifiedMetamodel__Module: set["UnifiedMetamodel__Submodule"] = None, UnifiedMetamodel__Module45: "UnifiedMetamodel__DomainMetamodel" = None):
        self.name = name
        self.UnifiedMetamodel__Module = UnifiedMetamodel__Module if UnifiedMetamodel__Module is not None else set()
        self.UnifiedMetamodel__Module45 = UnifiedMetamodel__Module45
        
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
    def UnifiedMetamodel__Module45(self):
        return self.__UnifiedMetamodel__Module45

    @UnifiedMetamodel__Module45.setter
    def UnifiedMetamodel__Module45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Module__UnifiedMetamodel__Module45", None)
        self.__UnifiedMetamodel__Module45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__DomainMetamodel44"):
                opp_val = getattr(old_value, "UnifiedMetamodel__DomainMetamodel44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__DomainMetamodel44"):
                opp_val = getattr(value, "UnifiedMetamodel__DomainMetamodel44", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__DomainMetamodel44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transaction:

    pass
class UnifiedMetamodel__sale(Transaction):

    pass
class Operations:

    pass
class UnifiedMetamodel__Create(Operations):

    pass
class UnifiedMetamodel__Read(Operations):

    pass
class UnifiedMetamodel__TechnologyMetamodel:

    pass
class UnifiedMetamodel__DomainMetamodel:

    pass
class UnifiedMetamodel__Metamodel:

    def __init__(self, name: str, UnifiedMetamodel__Metamodel: "UnifiedMetamodel__ArquitectureMetamodel" = None, UnifiedMetamodel__Metamodel22: "UnifiedMetamodel__DomainMetamodel" = None, UnifiedMetamodel__Metamodel24: "UnifiedMetamodel__TechnologyMetamodel" = None):
        self.name = name
        self.UnifiedMetamodel__Metamodel = UnifiedMetamodel__Metamodel
        self.UnifiedMetamodel__Metamodel22 = UnifiedMetamodel__Metamodel22
        self.UnifiedMetamodel__Metamodel24 = UnifiedMetamodel__Metamodel24
        
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
            if hasattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel20"):
                opp_val = getattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel20", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__ArquitectureMetamodel20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__ArquitectureMetamodel20"):
                opp_val = getattr(value, "UnifiedMetamodel__ArquitectureMetamodel20", None)
                setattr(value, "UnifiedMetamodel__ArquitectureMetamodel20", self)

    @property
    def UnifiedMetamodel__Metamodel22(self):
        return self.__UnifiedMetamodel__Metamodel22

    @UnifiedMetamodel__Metamodel22.setter
    def UnifiedMetamodel__Metamodel22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Metamodel__UnifiedMetamodel__Metamodel22", None)
        self.__UnifiedMetamodel__Metamodel22 = value
        
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

    @property
    def UnifiedMetamodel__Metamodel24(self):
        return self.__UnifiedMetamodel__Metamodel24

    @UnifiedMetamodel__Metamodel24.setter
    def UnifiedMetamodel__Metamodel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Metamodel__UnifiedMetamodel__Metamodel24", None)
        self.__UnifiedMetamodel__Metamodel24 = value
        
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

class UnifiedMetamodel__Entity:

    def __init__(self, name: str, UnifiedMetamodel__Entity: "UnifiedMetamodel__Operations" = None, UnifiedMetamodel__Entity29: set["UnifiedMetamodel__Property"] = None, UnifiedMetamodel__Entity31: "UnifiedMetamodel__RelationDom" = None, UnifiedMetamodel__Entity34: "UnifiedMetamodel__RelationDom" = None, UnifiedMetamodel__Entity42: "UnifiedMetamodel__Submodule" = None):
        self.name = name
        self.UnifiedMetamodel__Entity = UnifiedMetamodel__Entity
        self.UnifiedMetamodel__Entity29 = UnifiedMetamodel__Entity29 if UnifiedMetamodel__Entity29 is not None else set()
        self.UnifiedMetamodel__Entity31 = UnifiedMetamodel__Entity31
        self.UnifiedMetamodel__Entity34 = UnifiedMetamodel__Entity34
        self.UnifiedMetamodel__Entity42 = UnifiedMetamodel__Entity42
        
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
    def UnifiedMetamodel__Entity34(self):
        return self.__UnifiedMetamodel__Entity34

    @UnifiedMetamodel__Entity34.setter
    def UnifiedMetamodel__Entity34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity34", None)
        self.__UnifiedMetamodel__Entity34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationDom33"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationDom33", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationDom33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationDom33"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationDom33", None)
                setattr(value, "UnifiedMetamodel__RelationDom33", self)

    @property
    def UnifiedMetamodel__Entity31(self):
        return self.__UnifiedMetamodel__Entity31

    @UnifiedMetamodel__Entity31.setter
    def UnifiedMetamodel__Entity31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity31", None)
        self.__UnifiedMetamodel__Entity31 = value
        
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
    def UnifiedMetamodel__Entity42(self):
        return self.__UnifiedMetamodel__Entity42

    @UnifiedMetamodel__Entity42.setter
    def UnifiedMetamodel__Entity42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity42", None)
        self.__UnifiedMetamodel__Entity42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Submodule41"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Submodule41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Submodule41"):
                opp_val = getattr(value, "UnifiedMetamodel__Submodule41", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Submodule41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__Entity29(self):
        return self.__UnifiedMetamodel__Entity29

    @UnifiedMetamodel__Entity29.setter
    def UnifiedMetamodel__Entity29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Entity__UnifiedMetamodel__Entity29", None)
        self.__UnifiedMetamodel__Entity29 = value if value is not None else set()
        
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
                    

class UnifiedMetamodel__Operations:

    pass
class RelationDom:

    pass
class UnifiedMetamodel__Composition(RelationDom):

    pass
class UnifiedMetamodel__exchange(Transaction):

    pass
class UnifiedMetamodel__RelationArch:

    def __init__(self, name: str, UnifiedMetamodel__RelationArch12: "UnifiedMetamodel__Layer" = None, UnifiedMetamodel__RelationArch15: "UnifiedMetamodel__Layer" = None, UnifiedMetamodel__RelationArch: "UnifiedMetamodel__Component" = None):
        self.name = name
        self.UnifiedMetamodel__RelationArch12 = UnifiedMetamodel__RelationArch12
        self.UnifiedMetamodel__RelationArch15 = UnifiedMetamodel__RelationArch15
        self.UnifiedMetamodel__RelationArch = UnifiedMetamodel__RelationArch
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "UnifiedMetamodel__Component10"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Component10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Component10"):
                opp_val = getattr(value, "UnifiedMetamodel__Component10", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Component10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__RelationArch12(self):
        return self.__UnifiedMetamodel__RelationArch12

    @UnifiedMetamodel__RelationArch12.setter
    def UnifiedMetamodel__RelationArch12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__RelationArch__UnifiedMetamodel__RelationArch12", None)
        self.__UnifiedMetamodel__RelationArch12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Layer13"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Layer13", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Layer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Layer13"):
                opp_val = getattr(value, "UnifiedMetamodel__Layer13", None)
                setattr(value, "UnifiedMetamodel__Layer13", self)

    @property
    def UnifiedMetamodel__RelationArch15(self):
        return self.__UnifiedMetamodel__RelationArch15

    @UnifiedMetamodel__RelationArch15.setter
    def UnifiedMetamodel__RelationArch15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__RelationArch__UnifiedMetamodel__RelationArch15", None)
        self.__UnifiedMetamodel__RelationArch15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Layer16"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Layer16", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__Layer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Layer16"):
                opp_val = getattr(value, "UnifiedMetamodel__Layer16", None)
                setattr(value, "UnifiedMetamodel__Layer16", self)

class UnifiedMetamodel__Component:

    def __init__(self, name: str, UnifiedMetamodel__Component: set["UnifiedMetamodel__Layer"] = None, UnifiedMetamodel__Component10: set["UnifiedMetamodel__RelationArch"] = None, UnifiedMetamodel__Component18: "UnifiedMetamodel__ArquitectureMetamodel" = None):
        self.name = name
        self.UnifiedMetamodel__Component = UnifiedMetamodel__Component if UnifiedMetamodel__Component is not None else set()
        self.UnifiedMetamodel__Component10 = UnifiedMetamodel__Component10 if UnifiedMetamodel__Component10 is not None else set()
        self.UnifiedMetamodel__Component18 = UnifiedMetamodel__Component18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Component18(self):
        return self.__UnifiedMetamodel__Component18

    @UnifiedMetamodel__Component18.setter
    def UnifiedMetamodel__Component18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Component__UnifiedMetamodel__Component18", None)
        self.__UnifiedMetamodel__Component18 = value
        
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

    @property
    def UnifiedMetamodel__Component10(self):
        return self.__UnifiedMetamodel__Component10

    @UnifiedMetamodel__Component10.setter
    def UnifiedMetamodel__Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Component__UnifiedMetamodel__Component10", None)
        self.__UnifiedMetamodel__Component10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__RelationArch"):
                    opp_val = getattr(item, "UnifiedMetamodel__RelationArch", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__RelationArch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__RelationArch"):
                    opp_val = getattr(item, "UnifiedMetamodel__RelationArch", None)
                    
                    setattr(item, "UnifiedMetamodel__RelationArch", self)
                    

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
                if hasattr(item, "UnifiedMetamodel__Layer8"):
                    opp_val = getattr(item, "UnifiedMetamodel__Layer8", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__Layer8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__Layer8"):
                    opp_val = getattr(item, "UnifiedMetamodel__Layer8", None)
                    
                    setattr(item, "UnifiedMetamodel__Layer8", self)
                    

class UnifiedMetamodel__Layer:

    def __init__(self, name: str, UnifiedMetamodel__Layer13: "UnifiedMetamodel__RelationArch" = None, UnifiedMetamodel__Layer16: "UnifiedMetamodel__RelationArch" = None, UnifiedMetamodel__Layer: set["UnifiedMetamodel__LayerSegment"] = None, UnifiedMetamodel__Layer8: "UnifiedMetamodel__Component" = None):
        self.name = name
        self.UnifiedMetamodel__Layer13 = UnifiedMetamodel__Layer13
        self.UnifiedMetamodel__Layer16 = UnifiedMetamodel__Layer16
        self.UnifiedMetamodel__Layer = UnifiedMetamodel__Layer if UnifiedMetamodel__Layer is not None else set()
        self.UnifiedMetamodel__Layer8 = UnifiedMetamodel__Layer8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__Layer16(self):
        return self.__UnifiedMetamodel__Layer16

    @UnifiedMetamodel__Layer16.setter
    def UnifiedMetamodel__Layer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer16", None)
        self.__UnifiedMetamodel__Layer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationArch15"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationArch15", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationArch15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationArch15"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationArch15", None)
                setattr(value, "UnifiedMetamodel__RelationArch15", self)

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
                if hasattr(item, "UnifiedMetamodel__LayerSegment6"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment6", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__LayerSegment6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment6"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment6", None)
                    
                    setattr(item, "UnifiedMetamodel__LayerSegment6", self)
                    

    @property
    def UnifiedMetamodel__Layer8(self):
        return self.__UnifiedMetamodel__Layer8

    @UnifiedMetamodel__Layer8.setter
    def UnifiedMetamodel__Layer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer8", None)
        self.__UnifiedMetamodel__Layer8 = value
        
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
    def UnifiedMetamodel__Layer13(self):
        return self.__UnifiedMetamodel__Layer13

    @UnifiedMetamodel__Layer13.setter
    def UnifiedMetamodel__Layer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__Layer__UnifiedMetamodel__Layer13", None)
        self.__UnifiedMetamodel__Layer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__RelationArch12"):
                opp_val = getattr(old_value, "UnifiedMetamodel__RelationArch12", None)
                if opp_val == self:
                    setattr(old_value, "UnifiedMetamodel__RelationArch12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__RelationArch12"):
                opp_val = getattr(value, "UnifiedMetamodel__RelationArch12", None)
                setattr(value, "UnifiedMetamodel__RelationArch12", self)

class UnifiedMetamodel__ArquitectureMetamodel:

    pass
class UnifiedMetamodel__LayerSegment:

    def __init__(self, name: str, UnifiedMetamodel__LayerSegment4: "UnifiedMetamodel__LayerSegment" = None, UnifiedMetamodel__LayerSegment2: set["UnifiedMetamodel__LayerSegment"] = None, UnifiedMetamodel__LayerSegment: "UnifiedMetamodel__LayerSegment" = None, UnifiedMetamodel__LayerSegment0: set["UnifiedMetamodel__LayerSegment"] = None, UnifiedMetamodel__LayerSegment6: "UnifiedMetamodel__Layer" = None):
        self.name = name
        self.UnifiedMetamodel__LayerSegment4 = UnifiedMetamodel__LayerSegment4
        self.UnifiedMetamodel__LayerSegment2 = UnifiedMetamodel__LayerSegment2 if UnifiedMetamodel__LayerSegment2 is not None else set()
        self.UnifiedMetamodel__LayerSegment = UnifiedMetamodel__LayerSegment
        self.UnifiedMetamodel__LayerSegment0 = UnifiedMetamodel__LayerSegment0 if UnifiedMetamodel__LayerSegment0 is not None else set()
        self.UnifiedMetamodel__LayerSegment6 = UnifiedMetamodel__LayerSegment6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UnifiedMetamodel__LayerSegment2(self):
        return self.__UnifiedMetamodel__LayerSegment2

    @UnifiedMetamodel__LayerSegment2.setter
    def UnifiedMetamodel__LayerSegment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__LayerSegment__UnifiedMetamodel__LayerSegment2", None)
        self.__UnifiedMetamodel__LayerSegment2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment4"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment4", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__LayerSegment4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment4"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment4", None)
                    
                    setattr(item, "UnifiedMetamodel__LayerSegment4", self)
                    

    @property
    def UnifiedMetamodel__LayerSegment0(self):
        return self.__UnifiedMetamodel__LayerSegment0

    @UnifiedMetamodel__LayerSegment0.setter
    def UnifiedMetamodel__LayerSegment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__LayerSegment__UnifiedMetamodel__LayerSegment0", None)
        self.__UnifiedMetamodel__LayerSegment0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "UnifiedMetamodel__LayerSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnifiedMetamodel__LayerSegment"):
                    opp_val = getattr(item, "UnifiedMetamodel__LayerSegment", None)
                    
                    setattr(item, "UnifiedMetamodel__LayerSegment", self)
                    

    @property
    def UnifiedMetamodel__LayerSegment6(self):
        return self.__UnifiedMetamodel__LayerSegment6

    @UnifiedMetamodel__LayerSegment6.setter
    def UnifiedMetamodel__LayerSegment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__LayerSegment__UnifiedMetamodel__LayerSegment6", None)
        self.__UnifiedMetamodel__LayerSegment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__Layer"):
                opp_val = getattr(old_value, "UnifiedMetamodel__Layer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__Layer"):
                opp_val = getattr(value, "UnifiedMetamodel__Layer", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__Layer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__LayerSegment4(self):
        return self.__UnifiedMetamodel__LayerSegment4

    @UnifiedMetamodel__LayerSegment4.setter
    def UnifiedMetamodel__LayerSegment4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__LayerSegment__UnifiedMetamodel__LayerSegment4", None)
        self.__UnifiedMetamodel__LayerSegment4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__LayerSegment2"):
                opp_val = getattr(old_value, "UnifiedMetamodel__LayerSegment2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__LayerSegment2"):
                opp_val = getattr(value, "UnifiedMetamodel__LayerSegment2", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__LayerSegment2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UnifiedMetamodel__LayerSegment(self):
        return self.__UnifiedMetamodel__LayerSegment

    @UnifiedMetamodel__LayerSegment.setter
    def UnifiedMetamodel__LayerSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UnifiedMetamodel__LayerSegment__UnifiedMetamodel__LayerSegment", None)
        self.__UnifiedMetamodel__LayerSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnifiedMetamodel__LayerSegment0"):
                opp_val = getattr(old_value, "UnifiedMetamodel__LayerSegment0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnifiedMetamodel__LayerSegment0"):
                opp_val = getattr(value, "UnifiedMetamodel__LayerSegment0", None)
                if opp_val is None:
                    setattr(value, "UnifiedMetamodel__LayerSegment0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Layer:

    pass
class UnifiedMetamodel__JavaScript(Layer):

    pass
class UnifiedMetamodel__War(Layer):

    pass
class UnifiedMetamodel__Ejb(Layer):

    pass
class LayerSegment:

    pass
class UnifiedMetamodel__UI(LayerSegment):

    pass
class UnifiedMetamodel__Actions(LayerSegment):

    pass
class UnifiedMetamodel__Services(LayerSegment):

    pass
class UnifiedMetamodel__RestEntity(LayerSegment):

    pass
class UnifiedMetamodel__Store(LayerSegment):

    pass
class UnifiedMetamodel__Util(LayerSegment):

    pass
class UnifiedMetamodel__Pojo(LayerSegment):

    pass
class UnifiedMetamodel__Containers(LayerSegment):

    pass
class UnifiedMetamodel__Facade(LayerSegment):

    pass
class UnifiedMetamodel__Reducers(LayerSegment):

    pass
class UnifiedMetamodel__Dto(LayerSegment):

    pass