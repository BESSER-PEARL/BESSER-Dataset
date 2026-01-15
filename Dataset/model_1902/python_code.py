from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_JsMethodArgs:

    def __init__(self, name: str, myDsl_JsMethodArgs: "myDsl_JsMethod" = None, myDsl_JsMethodArgs189: "myDsl_AxiosRequest" = None):
        self.name = name
        self.myDsl_JsMethodArgs = myDsl_JsMethodArgs
        self.myDsl_JsMethodArgs189 = myDsl_JsMethodArgs189
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_JsMethodArgs189(self):
        return self.__myDsl_JsMethodArgs189

    @myDsl_JsMethodArgs189.setter
    def myDsl_JsMethodArgs189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsMethodArgs__myDsl_JsMethodArgs189", None)
        self.__myDsl_JsMethodArgs189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AxiosRequest188"):
                opp_val = getattr(old_value, "myDsl_AxiosRequest188", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AxiosRequest188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AxiosRequest188"):
                opp_val = getattr(value, "myDsl_AxiosRequest188", None)
                setattr(value, "myDsl_AxiosRequest188", self)

    @property
    def myDsl_JsMethodArgs(self):
        return self.__myDsl_JsMethodArgs

    @myDsl_JsMethodArgs.setter
    def myDsl_JsMethodArgs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsMethodArgs__myDsl_JsMethodArgs", None)
        self.__myDsl_JsMethodArgs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JsMethod186"):
                opp_val = getattr(old_value, "myDsl_JsMethod186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JsMethod186"):
                opp_val = getattr(value, "myDsl_JsMethod186", None)
                if opp_val is None:
                    setattr(value, "myDsl_JsMethod186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class File:

    pass
class myDsl_Json(File):

    pass
class myDsl_Js(File):

    pass
class myDsl_Css(File):

    pass
class myDsl_Md(File):

    pass
class myDsl_JsMethod:

    def __init__(self, name: str, type: str, myDsl_JsMethod: "myDsl_Visualizer" = None, myDsl_JsMethod186: set["myDsl_JsMethodArgs"] = None):
        self.name = name
        self.type = type
        self.myDsl_JsMethod = myDsl_JsMethod
        self.myDsl_JsMethod186 = myDsl_JsMethod186 if myDsl_JsMethod186 is not None else set()
        
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
    def myDsl_JsMethod(self):
        return self.__myDsl_JsMethod

    @myDsl_JsMethod.setter
    def myDsl_JsMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsMethod__myDsl_JsMethod", None)
        self.__myDsl_JsMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Visualizer154"):
                opp_val = getattr(old_value, "myDsl_Visualizer154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Visualizer154"):
                opp_val = getattr(value, "myDsl_Visualizer154", None)
                if opp_val is None:
                    setattr(value, "myDsl_Visualizer154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_JsMethod186(self):
        return self.__myDsl_JsMethod186

    @myDsl_JsMethod186.setter
    def myDsl_JsMethod186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsMethod__myDsl_JsMethod186", None)
        self.__myDsl_JsMethod186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_JsMethodArgs"):
                    opp_val = getattr(item, "myDsl_JsMethodArgs", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_JsMethodArgs", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_JsMethodArgs"):
                    opp_val = getattr(item, "myDsl_JsMethodArgs", None)
                    
                    setattr(item, "myDsl_JsMethodArgs", self)
                    

class myDsl_UIComponent:

    pass
class UIComponent:

    pass
class myDsl_AbstractFrontElement:

    pass
class Eclass:

    pass
class myDsl_AbstractClass(Eclass):

    pass
class myDsl_Descriptor:

    def __init__(self, name: str, path: str, myDsl_Descriptor: "myDsl_Subproject" = None):
        self.name = name
        self.path = path
        self.myDsl_Descriptor = myDsl_Descriptor
        
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
    def myDsl_Descriptor(self):
        return self.__myDsl_Descriptor

    @myDsl_Descriptor.setter
    def myDsl_Descriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Descriptor__myDsl_Descriptor", None)
        self.__myDsl_Descriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Subproject69"):
                opp_val = getattr(old_value, "myDsl_Subproject69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Subproject69"):
                opp_val = getattr(value, "myDsl_Subproject69", None)
                if opp_val is None:
                    setattr(value, "myDsl_Subproject69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Eclass:

    def __init__(self, name: str, myDsl_Eclass105: "myDsl_Epackage" = None, myDsl_Eclass108: "myDsl_MethodBack" = None, myDsl_Eclass111: "myDsl_MethodBack" = None, myDsl_Eclass114: "myDsl_AbstractMethod" = None, myDsl_Eclass117: "myDsl_AbstractMethod" = None, myDsl_Eclass: "myDsl_Attribute" = None):
        self.name = name
        self.myDsl_Eclass105 = myDsl_Eclass105
        self.myDsl_Eclass108 = myDsl_Eclass108
        self.myDsl_Eclass111 = myDsl_Eclass111
        self.myDsl_Eclass114 = myDsl_Eclass114
        self.myDsl_Eclass117 = myDsl_Eclass117
        self.myDsl_Eclass = myDsl_Eclass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Eclass108(self):
        return self.__myDsl_Eclass108

    @myDsl_Eclass108.setter
    def myDsl_Eclass108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Eclass__myDsl_Eclass108", None)
        self.__myDsl_Eclass108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_MethodBack107"):
                opp_val = getattr(old_value, "myDsl_MethodBack107", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_MethodBack107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_MethodBack107"):
                opp_val = getattr(value, "myDsl_MethodBack107", None)
                setattr(value, "myDsl_MethodBack107", self)

    @property
    def myDsl_Eclass111(self):
        return self.__myDsl_Eclass111

    @myDsl_Eclass111.setter
    def myDsl_Eclass111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Eclass__myDsl_Eclass111", None)
        self.__myDsl_Eclass111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_MethodBack110"):
                opp_val = getattr(old_value, "myDsl_MethodBack110", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_MethodBack110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_MethodBack110"):
                opp_val = getattr(value, "myDsl_MethodBack110", None)
                setattr(value, "myDsl_MethodBack110", self)

    @property
    def myDsl_Eclass(self):
        return self.__myDsl_Eclass

    @myDsl_Eclass.setter
    def myDsl_Eclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Eclass__myDsl_Eclass", None)
        self.__myDsl_Eclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Attribute102"):
                opp_val = getattr(old_value, "myDsl_Attribute102", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Attribute102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Attribute102"):
                opp_val = getattr(value, "myDsl_Attribute102", None)
                setattr(value, "myDsl_Attribute102", self)

    @property
    def myDsl_Eclass105(self):
        return self.__myDsl_Eclass105

    @myDsl_Eclass105.setter
    def myDsl_Eclass105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Eclass__myDsl_Eclass105", None)
        self.__myDsl_Eclass105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Epackage104"):
                opp_val = getattr(old_value, "myDsl_Epackage104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Epackage104"):
                opp_val = getattr(value, "myDsl_Epackage104", None)
                if opp_val is None:
                    setattr(value, "myDsl_Epackage104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Eclass117(self):
        return self.__myDsl_Eclass117

    @myDsl_Eclass117.setter
    def myDsl_Eclass117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Eclass__myDsl_Eclass117", None)
        self.__myDsl_Eclass117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractMethod116"):
                opp_val = getattr(old_value, "myDsl_AbstractMethod116", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractMethod116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractMethod116"):
                opp_val = getattr(value, "myDsl_AbstractMethod116", None)
                setattr(value, "myDsl_AbstractMethod116", self)

    @property
    def myDsl_Eclass114(self):
        return self.__myDsl_Eclass114

    @myDsl_Eclass114.setter
    def myDsl_Eclass114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Eclass__myDsl_Eclass114", None)
        self.__myDsl_Eclass114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractMethod113"):
                opp_val = getattr(old_value, "myDsl_AbstractMethod113", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractMethod113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractMethod113"):
                opp_val = getattr(value, "myDsl_AbstractMethod113", None)
                setattr(value, "myDsl_AbstractMethod113", self)

class myDsl_NativeClass(Eclass):

    pass
class myDsl_Einterface:

    def __init__(self, name: str, myDsl_Einterface: "myDsl_GenericClass" = None, myDsl_Einterface91: set["myDsl_Attribute"] = None, myDsl_Einterface94: set["myDsl_AbstractMethod"] = None):
        self.name = name
        self.myDsl_Einterface = myDsl_Einterface
        self.myDsl_Einterface91 = myDsl_Einterface91 if myDsl_Einterface91 is not None else set()
        self.myDsl_Einterface94 = myDsl_Einterface94 if myDsl_Einterface94 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Einterface91(self):
        return self.__myDsl_Einterface91

    @myDsl_Einterface91.setter
    def myDsl_Einterface91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Einterface__myDsl_Einterface91", None)
        self.__myDsl_Einterface91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Attribute92"):
                    opp_val = getattr(item, "myDsl_Attribute92", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Attribute92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Attribute92"):
                    opp_val = getattr(item, "myDsl_Attribute92", None)
                    
                    setattr(item, "myDsl_Attribute92", self)
                    

    @property
    def myDsl_Einterface(self):
        return self.__myDsl_Einterface

    @myDsl_Einterface.setter
    def myDsl_Einterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Einterface__myDsl_Einterface", None)
        self.__myDsl_Einterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GenericClass89"):
                opp_val = getattr(old_value, "myDsl_GenericClass89", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_GenericClass89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GenericClass89"):
                opp_val = getattr(value, "myDsl_GenericClass89", None)
                setattr(value, "myDsl_GenericClass89", self)

    @property
    def myDsl_Einterface94(self):
        return self.__myDsl_Einterface94

    @myDsl_Einterface94.setter
    def myDsl_Einterface94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Einterface__myDsl_Einterface94", None)
        self.__myDsl_Einterface94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_AbstractMethod95"):
                    opp_val = getattr(item, "myDsl_AbstractMethod95", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_AbstractMethod95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_AbstractMethod95"):
                    opp_val = getattr(item, "myDsl_AbstractMethod95", None)
                    
                    setattr(item, "myDsl_AbstractMethod95", self)
                    

class myDsl_GenericClass(Eclass):

    pass
class myDsl_AbstractMethod:

    def __init__(self, name: str, myDsl_AbstractMethod: "myDsl_AbstractClass" = None, myDsl_AbstractMethod95: "myDsl_Einterface" = None, myDsl_AbstractMethod113: "myDsl_Eclass" = None, myDsl_AbstractMethod116: "myDsl_Eclass" = None):
        self.name = name
        self.myDsl_AbstractMethod = myDsl_AbstractMethod
        self.myDsl_AbstractMethod95 = myDsl_AbstractMethod95
        self.myDsl_AbstractMethod113 = myDsl_AbstractMethod113
        self.myDsl_AbstractMethod116 = myDsl_AbstractMethod116
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_AbstractMethod(self):
        return self.__myDsl_AbstractMethod

    @myDsl_AbstractMethod.setter
    def myDsl_AbstractMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AbstractMethod__myDsl_AbstractMethod", None)
        self.__myDsl_AbstractMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractClass76"):
                opp_val = getattr(old_value, "myDsl_AbstractClass76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractClass76"):
                opp_val = getattr(value, "myDsl_AbstractClass76", None)
                if opp_val is None:
                    setattr(value, "myDsl_AbstractClass76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_AbstractMethod95(self):
        return self.__myDsl_AbstractMethod95

    @myDsl_AbstractMethod95.setter
    def myDsl_AbstractMethod95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AbstractMethod__myDsl_AbstractMethod95", None)
        self.__myDsl_AbstractMethod95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Einterface94"):
                opp_val = getattr(old_value, "myDsl_Einterface94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Einterface94"):
                opp_val = getattr(value, "myDsl_Einterface94", None)
                if opp_val is None:
                    setattr(value, "myDsl_Einterface94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_AbstractMethod113(self):
        return self.__myDsl_AbstractMethod113

    @myDsl_AbstractMethod113.setter
    def myDsl_AbstractMethod113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AbstractMethod__myDsl_AbstractMethod113", None)
        self.__myDsl_AbstractMethod113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Eclass114"):
                opp_val = getattr(old_value, "myDsl_Eclass114", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Eclass114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Eclass114"):
                opp_val = getattr(value, "myDsl_Eclass114", None)
                setattr(value, "myDsl_Eclass114", self)

    @property
    def myDsl_AbstractMethod116(self):
        return self.__myDsl_AbstractMethod116

    @myDsl_AbstractMethod116.setter
    def myDsl_AbstractMethod116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AbstractMethod__myDsl_AbstractMethod116", None)
        self.__myDsl_AbstractMethod116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Eclass117"):
                opp_val = getattr(old_value, "myDsl_Eclass117", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Eclass117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Eclass117"):
                opp_val = getattr(value, "myDsl_Eclass117", None)
                setattr(value, "myDsl_Eclass117", self)

class myDsl_Annotation(Eclass):

    def __init__(self, propertie: str, myDsl_Annotation: "myDsl_AbstractClass" = None, myDsl_Annotation84: "myDsl_GenericClass" = None, myDsl_Annotation120: "myDsl_Library" = None):
        self.propertie = propertie
        self.myDsl_Annotation = myDsl_Annotation
        self.myDsl_Annotation84 = myDsl_Annotation84
        self.myDsl_Annotation120 = myDsl_Annotation120
        
    @property
    def propertie(self) -> str:
        return self.__propertie

    @propertie.setter
    def propertie(self, propertie: str):
        self.__propertie = propertie

    @property
    def myDsl_Annotation84(self):
        return self.__myDsl_Annotation84

    @myDsl_Annotation84.setter
    def myDsl_Annotation84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Annotation__myDsl_Annotation84", None)
        self.__myDsl_Annotation84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GenericClass83"):
                opp_val = getattr(old_value, "myDsl_GenericClass83", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_GenericClass83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GenericClass83"):
                opp_val = getattr(value, "myDsl_GenericClass83", None)
                setattr(value, "myDsl_GenericClass83", self)

    @property
    def myDsl_Annotation(self):
        return self.__myDsl_Annotation

    @myDsl_Annotation.setter
    def myDsl_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Annotation__myDsl_Annotation", None)
        self.__myDsl_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractClass74"):
                opp_val = getattr(old_value, "myDsl_AbstractClass74", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractClass74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractClass74"):
                opp_val = getattr(value, "myDsl_AbstractClass74", None)
                setattr(value, "myDsl_AbstractClass74", self)

    @property
    def myDsl_Annotation120(self):
        return self.__myDsl_Annotation120

    @myDsl_Annotation120.setter
    def myDsl_Annotation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Annotation__myDsl_Annotation120", None)
        self.__myDsl_Annotation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Library119"):
                opp_val = getattr(old_value, "myDsl_Library119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Library119"):
                opp_val = getattr(value, "myDsl_Library119", None)
                if opp_val is None:
                    setattr(value, "myDsl_Library119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_MethodBack:

    def __init__(self, name: str, myDsl_MethodBack: "myDsl_AbstractClass" = None, myDsl_MethodBack81: "myDsl_GenericClass" = None, myDsl_MethodBack100: "myDsl_NativeClass" = None, myDsl_MethodBack107: "myDsl_Eclass" = None, myDsl_MethodBack110: "myDsl_Eclass" = None):
        self.name = name
        self.myDsl_MethodBack = myDsl_MethodBack
        self.myDsl_MethodBack81 = myDsl_MethodBack81
        self.myDsl_MethodBack100 = myDsl_MethodBack100
        self.myDsl_MethodBack107 = myDsl_MethodBack107
        self.myDsl_MethodBack110 = myDsl_MethodBack110
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_MethodBack(self):
        return self.__myDsl_MethodBack

    @myDsl_MethodBack.setter
    def myDsl_MethodBack(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodBack__myDsl_MethodBack", None)
        self.__myDsl_MethodBack = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractClass72"):
                opp_val = getattr(old_value, "myDsl_AbstractClass72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractClass72"):
                opp_val = getattr(value, "myDsl_AbstractClass72", None)
                if opp_val is None:
                    setattr(value, "myDsl_AbstractClass72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_MethodBack81(self):
        return self.__myDsl_MethodBack81

    @myDsl_MethodBack81.setter
    def myDsl_MethodBack81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodBack__myDsl_MethodBack81", None)
        self.__myDsl_MethodBack81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GenericClass80"):
                opp_val = getattr(old_value, "myDsl_GenericClass80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GenericClass80"):
                opp_val = getattr(value, "myDsl_GenericClass80", None)
                if opp_val is None:
                    setattr(value, "myDsl_GenericClass80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_MethodBack110(self):
        return self.__myDsl_MethodBack110

    @myDsl_MethodBack110.setter
    def myDsl_MethodBack110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodBack__myDsl_MethodBack110", None)
        self.__myDsl_MethodBack110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Eclass111"):
                opp_val = getattr(old_value, "myDsl_Eclass111", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Eclass111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Eclass111"):
                opp_val = getattr(value, "myDsl_Eclass111", None)
                setattr(value, "myDsl_Eclass111", self)

    @property
    def myDsl_MethodBack100(self):
        return self.__myDsl_MethodBack100

    @myDsl_MethodBack100.setter
    def myDsl_MethodBack100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodBack__myDsl_MethodBack100", None)
        self.__myDsl_MethodBack100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_NativeClass99"):
                opp_val = getattr(old_value, "myDsl_NativeClass99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_NativeClass99"):
                opp_val = getattr(value, "myDsl_NativeClass99", None)
                if opp_val is None:
                    setattr(value, "myDsl_NativeClass99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_MethodBack107(self):
        return self.__myDsl_MethodBack107

    @myDsl_MethodBack107.setter
    def myDsl_MethodBack107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MethodBack__myDsl_MethodBack107", None)
        self.__myDsl_MethodBack107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Eclass108"):
                opp_val = getattr(old_value, "myDsl_Eclass108", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Eclass108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Eclass108"):
                opp_val = getattr(value, "myDsl_Eclass108", None)
                setattr(value, "myDsl_Eclass108", self)

class myDsl_Attribute:

    def __init__(self, name: str, myDsl_Attribute: "myDsl_AbstractClass" = None, myDsl_Attribute78: "myDsl_GenericClass" = None, myDsl_Attribute92: "myDsl_Einterface" = None, myDsl_Attribute97: "myDsl_NativeClass" = None, myDsl_Attribute102: "myDsl_Eclass" = None):
        self.name = name
        self.myDsl_Attribute = myDsl_Attribute
        self.myDsl_Attribute78 = myDsl_Attribute78
        self.myDsl_Attribute92 = myDsl_Attribute92
        self.myDsl_Attribute97 = myDsl_Attribute97
        self.myDsl_Attribute102 = myDsl_Attribute102
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Attribute97(self):
        return self.__myDsl_Attribute97

    @myDsl_Attribute97.setter
    def myDsl_Attribute97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute97", None)
        self.__myDsl_Attribute97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_NativeClass"):
                opp_val = getattr(old_value, "myDsl_NativeClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_NativeClass"):
                opp_val = getattr(value, "myDsl_NativeClass", None)
                if opp_val is None:
                    setattr(value, "myDsl_NativeClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Attribute92(self):
        return self.__myDsl_Attribute92

    @myDsl_Attribute92.setter
    def myDsl_Attribute92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute92", None)
        self.__myDsl_Attribute92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Einterface91"):
                opp_val = getattr(old_value, "myDsl_Einterface91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Einterface91"):
                opp_val = getattr(value, "myDsl_Einterface91", None)
                if opp_val is None:
                    setattr(value, "myDsl_Einterface91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Attribute(self):
        return self.__myDsl_Attribute

    @myDsl_Attribute.setter
    def myDsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute", None)
        self.__myDsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractClass"):
                opp_val = getattr(old_value, "myDsl_AbstractClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractClass"):
                opp_val = getattr(value, "myDsl_AbstractClass", None)
                if opp_val is None:
                    setattr(value, "myDsl_AbstractClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Attribute102(self):
        return self.__myDsl_Attribute102

    @myDsl_Attribute102.setter
    def myDsl_Attribute102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute102", None)
        self.__myDsl_Attribute102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Eclass"):
                opp_val = getattr(old_value, "myDsl_Eclass", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Eclass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Eclass"):
                opp_val = getattr(value, "myDsl_Eclass", None)
                setattr(value, "myDsl_Eclass", self)

    @property
    def myDsl_Attribute78(self):
        return self.__myDsl_Attribute78

    @myDsl_Attribute78.setter
    def myDsl_Attribute78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute78", None)
        self.__myDsl_Attribute78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GenericClass"):
                opp_val = getattr(old_value, "myDsl_GenericClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GenericClass"):
                opp_val = getattr(value, "myDsl_GenericClass", None)
                if opp_val is None:
                    setattr(value, "myDsl_GenericClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_RelationArch:

    def __init__(self, name: str, source: str, target: str, myDsl_RelationArch: "myDsl_Architecture" = None):
        self.name = name
        self.source = source
        self.target = target
        self.myDsl_RelationArch = myDsl_RelationArch
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_RelationArch(self):
        return self.__myDsl_RelationArch

    @myDsl_RelationArch.setter
    def myDsl_RelationArch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RelationArch__myDsl_RelationArch", None)
        self.__myDsl_RelationArch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Architecture47"):
                opp_val = getattr(old_value, "myDsl_Architecture47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Architecture47"):
                opp_val = getattr(value, "myDsl_Architecture47", None)
                if opp_val is None:
                    setattr(value, "myDsl_Architecture47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Library:

    def __init__(self, name: str, isNative: str, myDsl_Library: "myDsl_Subproject" = None, myDsl_Library119: set["myDsl_Annotation"] = None):
        self.name = name
        self.isNative = isNative
        self.myDsl_Library = myDsl_Library
        self.myDsl_Library119 = myDsl_Library119 if myDsl_Library119 is not None else set()
        
    @property
    def isNative(self) -> str:
        return self.__isNative

    @isNative.setter
    def isNative(self, isNative: str):
        self.__isNative = isNative

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Library(self):
        return self.__myDsl_Library

    @myDsl_Library.setter
    def myDsl_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Library__myDsl_Library", None)
        self.__myDsl_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Subproject67"):
                opp_val = getattr(old_value, "myDsl_Subproject67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Subproject67"):
                opp_val = getattr(value, "myDsl_Subproject67", None)
                if opp_val is None:
                    setattr(value, "myDsl_Subproject67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Library119(self):
        return self.__myDsl_Library119

    @myDsl_Library119.setter
    def myDsl_Library119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Library__myDsl_Library119", None)
        self.__myDsl_Library119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Annotation120"):
                    opp_val = getattr(item, "myDsl_Annotation120", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Annotation120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Annotation120"):
                    opp_val = getattr(item, "myDsl_Annotation120", None)
                    
                    setattr(item, "myDsl_Annotation120", self)
                    

class myDsl_Component:

    def __init__(self, name: str, myDsl_Component49: set["myDsl_Layer"] = None, myDsl_Component: "myDsl_Architecture" = None):
        self.name = name
        self.myDsl_Component49 = myDsl_Component49 if myDsl_Component49 is not None else set()
        self.myDsl_Component = myDsl_Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Component(self):
        return self.__myDsl_Component

    @myDsl_Component.setter
    def myDsl_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Component__myDsl_Component", None)
        self.__myDsl_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Architecture45"):
                opp_val = getattr(old_value, "myDsl_Architecture45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Architecture45"):
                opp_val = getattr(value, "myDsl_Architecture45", None)
                if opp_val is None:
                    setattr(value, "myDsl_Architecture45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Component49(self):
        return self.__myDsl_Component49

    @myDsl_Component49.setter
    def myDsl_Component49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Component__myDsl_Component49", None)
        self.__myDsl_Component49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Layer"):
                    opp_val = getattr(item, "myDsl_Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Layer"):
                    opp_val = getattr(item, "myDsl_Layer", None)
                    
                    setattr(item, "myDsl_Layer", self)
                    

class myDsl_Epackage:

    def __init__(self, name: str, myDsl_Epackage: "myDsl_Subproject" = None, myDsl_Epackage104: set["myDsl_Eclass"] = None):
        self.name = name
        self.myDsl_Epackage = myDsl_Epackage
        self.myDsl_Epackage104 = myDsl_Epackage104 if myDsl_Epackage104 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Epackage(self):
        return self.__myDsl_Epackage

    @myDsl_Epackage.setter
    def myDsl_Epackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Epackage__myDsl_Epackage", None)
        self.__myDsl_Epackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Subproject65"):
                opp_val = getattr(old_value, "myDsl_Subproject65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Subproject65"):
                opp_val = getattr(value, "myDsl_Subproject65", None)
                if opp_val is None:
                    setattr(value, "myDsl_Subproject65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Epackage104(self):
        return self.__myDsl_Epackage104

    @myDsl_Epackage104.setter
    def myDsl_Epackage104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Epackage__myDsl_Epackage104", None)
        self.__myDsl_Epackage104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Eclass105"):
                    opp_val = getattr(item, "myDsl_Eclass105", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Eclass105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Eclass105"):
                    opp_val = getattr(item, "myDsl_Eclass105", None)
                    
                    setattr(item, "myDsl_Eclass105", self)
                    

class myDsl_Subproject:

    def __init__(self, name: str, myDsl_Subproject: "myDsl_JeeProject" = None, myDsl_Subproject65: set["myDsl_Epackage"] = None, myDsl_Subproject67: set["myDsl_Library"] = None, myDsl_Subproject69: set["myDsl_Descriptor"] = None):
        self.name = name
        self.myDsl_Subproject = myDsl_Subproject
        self.myDsl_Subproject65 = myDsl_Subproject65 if myDsl_Subproject65 is not None else set()
        self.myDsl_Subproject67 = myDsl_Subproject67 if myDsl_Subproject67 is not None else set()
        self.myDsl_Subproject69 = myDsl_Subproject69 if myDsl_Subproject69 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Subproject69(self):
        return self.__myDsl_Subproject69

    @myDsl_Subproject69.setter
    def myDsl_Subproject69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Subproject__myDsl_Subproject69", None)
        self.__myDsl_Subproject69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Descriptor"):
                    opp_val = getattr(item, "myDsl_Descriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Descriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Descriptor"):
                    opp_val = getattr(item, "myDsl_Descriptor", None)
                    
                    setattr(item, "myDsl_Descriptor", self)
                    

    @property
    def myDsl_Subproject65(self):
        return self.__myDsl_Subproject65

    @myDsl_Subproject65.setter
    def myDsl_Subproject65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Subproject__myDsl_Subproject65", None)
        self.__myDsl_Subproject65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Epackage"):
                    opp_val = getattr(item, "myDsl_Epackage", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Epackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Epackage"):
                    opp_val = getattr(item, "myDsl_Epackage", None)
                    
                    setattr(item, "myDsl_Epackage", self)
                    

    @property
    def myDsl_Subproject67(self):
        return self.__myDsl_Subproject67

    @myDsl_Subproject67.setter
    def myDsl_Subproject67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Subproject__myDsl_Subproject67", None)
        self.__myDsl_Subproject67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Library"):
                    opp_val = getattr(item, "myDsl_Library", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Library", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Library"):
                    opp_val = getattr(item, "myDsl_Library", None)
                    
                    setattr(item, "myDsl_Library", self)
                    

    @property
    def myDsl_Subproject(self):
        return self.__myDsl_Subproject

    @myDsl_Subproject.setter
    def myDsl_Subproject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Subproject__myDsl_Subproject", None)
        self.__myDsl_Subproject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JeeProject63"):
                opp_val = getattr(old_value, "myDsl_JeeProject63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JeeProject63"):
                opp_val = getattr(value, "myDsl_JeeProject63", None)
                if opp_val is None:
                    setattr(value, "myDsl_JeeProject63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_JeeProject:

    def __init__(self, name: str, myDsl_JeeProject: "myDsl_JavaApp" = None, myDsl_JeeProject63: set["myDsl_Subproject"] = None):
        self.name = name
        self.myDsl_JeeProject = myDsl_JeeProject
        self.myDsl_JeeProject63 = myDsl_JeeProject63 if myDsl_JeeProject63 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_JeeProject(self):
        return self.__myDsl_JeeProject

    @myDsl_JeeProject.setter
    def myDsl_JeeProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JeeProject__myDsl_JeeProject", None)
        self.__myDsl_JeeProject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JavaApp61"):
                opp_val = getattr(old_value, "myDsl_JavaApp61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JavaApp61"):
                opp_val = getattr(value, "myDsl_JavaApp61", None)
                if opp_val is None:
                    setattr(value, "myDsl_JavaApp61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_JeeProject63(self):
        return self.__myDsl_JeeProject63

    @myDsl_JeeProject63.setter
    def myDsl_JeeProject63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JeeProject__myDsl_JeeProject63", None)
        self.__myDsl_JeeProject63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Subproject"):
                    opp_val = getattr(item, "myDsl_Subproject", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Subproject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Subproject"):
                    opp_val = getattr(item, "myDsl_Subproject", None)
                    
                    setattr(item, "myDsl_Subproject", self)
                    

class myDsl_Operateson:

    pass
class myDsl_Transaction:

    def __init__(self, type: str, myDsl_Transaction: "myDsl_SpecialEntity" = None, myDsl_Transaction34: set["myDsl_Operateson"] = None):
        self.type = type
        self.myDsl_Transaction = myDsl_Transaction
        self.myDsl_Transaction34 = myDsl_Transaction34 if myDsl_Transaction34 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def myDsl_Transaction34(self):
        return self.__myDsl_Transaction34

    @myDsl_Transaction34.setter
    def myDsl_Transaction34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Transaction__myDsl_Transaction34", None)
        self.__myDsl_Transaction34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Operateson"):
                    opp_val = getattr(item, "myDsl_Operateson", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Operateson", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Operateson"):
                    opp_val = getattr(item, "myDsl_Operateson", None)
                    
                    setattr(item, "myDsl_Operateson", self)
                    

    @property
    def myDsl_Transaction(self):
        return self.__myDsl_Transaction

    @myDsl_Transaction.setter
    def myDsl_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Transaction__myDsl_Transaction", None)
        self.__myDsl_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SpecialEntity32"):
                opp_val = getattr(old_value, "myDsl_SpecialEntity32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SpecialEntity32"):
                opp_val = getattr(value, "myDsl_SpecialEntity32", None)
                if opp_val is None:
                    setattr(value, "myDsl_SpecialEntity32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_JavaApp:

    pass
class myDsl_SpecialEntity:

    pass
class AbstractFrontElement:

    pass
class myDsl_ActionDispatcher(AbstractFrontElement):

    def __init__(self, name: str, myDsl_ActionDispatcher: "myDsl_Action" = None, myDsl_ActionDispatcher177: "myDsl_ActionCreator" = None):
        self.name = name
        self.myDsl_ActionDispatcher = myDsl_ActionDispatcher
        self.myDsl_ActionDispatcher177 = myDsl_ActionDispatcher177
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ActionDispatcher177(self):
        return self.__myDsl_ActionDispatcher177

    @myDsl_ActionDispatcher177.setter
    def myDsl_ActionDispatcher177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ActionDispatcher__myDsl_ActionDispatcher177", None)
        self.__myDsl_ActionDispatcher177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ActionCreator178"):
                opp_val = getattr(old_value, "myDsl_ActionCreator178", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ActionCreator178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ActionCreator178"):
                opp_val = getattr(value, "myDsl_ActionCreator178", None)
                setattr(value, "myDsl_ActionCreator178", self)

    @property
    def myDsl_ActionDispatcher(self):
        return self.__myDsl_ActionDispatcher

    @myDsl_ActionDispatcher.setter
    def myDsl_ActionDispatcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ActionDispatcher__myDsl_ActionDispatcher", None)
        self.__myDsl_ActionDispatcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Action172"):
                opp_val = getattr(old_value, "myDsl_Action172", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Action172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Action172"):
                opp_val = getattr(value, "myDsl_Action172", None)
                setattr(value, "myDsl_Action172", self)

class myDsl_Visualizer(AbstractFrontElement, UIComponent):

    def __init__(self, name: str, myDsl_Visualizer: "myDsl_Functionality" = None, myDsl_Visualizer151: "myDsl_AbstractFrontElement" = None, myDsl_Visualizer154: set["myDsl_JsMethod"] = None):
        self.name = name
        self.myDsl_Visualizer = myDsl_Visualizer
        self.myDsl_Visualizer151 = myDsl_Visualizer151
        self.myDsl_Visualizer154 = myDsl_Visualizer154 if myDsl_Visualizer154 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Visualizer154(self):
        return self.__myDsl_Visualizer154

    @myDsl_Visualizer154.setter
    def myDsl_Visualizer154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Visualizer__myDsl_Visualizer154", None)
        self.__myDsl_Visualizer154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_JsMethod"):
                    opp_val = getattr(item, "myDsl_JsMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_JsMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_JsMethod"):
                    opp_val = getattr(item, "myDsl_JsMethod", None)
                    
                    setattr(item, "myDsl_JsMethod", self)
                    

    @property
    def myDsl_Visualizer(self):
        return self.__myDsl_Visualizer

    @myDsl_Visualizer.setter
    def myDsl_Visualizer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Visualizer__myDsl_Visualizer", None)
        self.__myDsl_Visualizer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Functionality134"):
                opp_val = getattr(old_value, "myDsl_Functionality134", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Functionality134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Functionality134"):
                opp_val = getattr(value, "myDsl_Functionality134", None)
                setattr(value, "myDsl_Functionality134", self)

    @property
    def myDsl_Visualizer151(self):
        return self.__myDsl_Visualizer151

    @myDsl_Visualizer151.setter
    def myDsl_Visualizer151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Visualizer__myDsl_Visualizer151", None)
        self.__myDsl_Visualizer151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractFrontElement152"):
                opp_val = getattr(old_value, "myDsl_AbstractFrontElement152", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractFrontElement152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractFrontElement152"):
                opp_val = getattr(value, "myDsl_AbstractFrontElement152", None)
                setattr(value, "myDsl_AbstractFrontElement152", self)

class myDsl_Directory(AbstractFrontElement):

    def __init__(self, name: str, purpose: str, myDsl_Directory: "myDsl_ReactApp" = None, myDsl_Directory141: "myDsl_Functionality" = None, myDsl_Directory161: "myDsl_File" = None, myDsl_Directory164: "myDsl_Directory" = None, myDsl_Directory162: "myDsl_Directory" = None, myDsl_Directory175: "myDsl_Action" = None, myDsl_Directory184: "myDsl_JsModule" = None):
        self.name = name
        self.purpose = purpose
        self.myDsl_Directory = myDsl_Directory
        self.myDsl_Directory141 = myDsl_Directory141
        self.myDsl_Directory161 = myDsl_Directory161
        self.myDsl_Directory164 = myDsl_Directory164
        self.myDsl_Directory162 = myDsl_Directory162
        self.myDsl_Directory175 = myDsl_Directory175
        self.myDsl_Directory184 = myDsl_Directory184
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def myDsl_Directory184(self):
        return self.__myDsl_Directory184

    @myDsl_Directory184.setter
    def myDsl_Directory184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory184", None)
        self.__myDsl_Directory184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JsModule183"):
                opp_val = getattr(old_value, "myDsl_JsModule183", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_JsModule183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JsModule183"):
                opp_val = getattr(value, "myDsl_JsModule183", None)
                setattr(value, "myDsl_JsModule183", self)

    @property
    def myDsl_Directory164(self):
        return self.__myDsl_Directory164

    @myDsl_Directory164.setter
    def myDsl_Directory164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory164", None)
        self.__myDsl_Directory164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directory162"):
                opp_val = getattr(old_value, "myDsl_Directory162", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Directory162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directory162"):
                opp_val = getattr(value, "myDsl_Directory162", None)
                setattr(value, "myDsl_Directory162", self)

    @property
    def myDsl_Directory175(self):
        return self.__myDsl_Directory175

    @myDsl_Directory175.setter
    def myDsl_Directory175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory175", None)
        self.__myDsl_Directory175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Action174"):
                opp_val = getattr(old_value, "myDsl_Action174", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Action174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Action174"):
                opp_val = getattr(value, "myDsl_Action174", None)
                setattr(value, "myDsl_Action174", self)

    @property
    def myDsl_Directory141(self):
        return self.__myDsl_Directory141

    @myDsl_Directory141.setter
    def myDsl_Directory141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory141", None)
        self.__myDsl_Directory141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Functionality140"):
                opp_val = getattr(old_value, "myDsl_Functionality140", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Functionality140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Functionality140"):
                opp_val = getattr(value, "myDsl_Functionality140", None)
                setattr(value, "myDsl_Functionality140", self)

    @property
    def myDsl_Directory(self):
        return self.__myDsl_Directory

    @myDsl_Directory.setter
    def myDsl_Directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory", None)
        self.__myDsl_Directory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactApp126"):
                opp_val = getattr(old_value, "myDsl_ReactApp126", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ReactApp126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactApp126"):
                opp_val = getattr(value, "myDsl_ReactApp126", None)
                setattr(value, "myDsl_ReactApp126", self)

    @property
    def myDsl_Directory162(self):
        return self.__myDsl_Directory162

    @myDsl_Directory162.setter
    def myDsl_Directory162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory162", None)
        self.__myDsl_Directory162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directory164"):
                opp_val = getattr(old_value, "myDsl_Directory164", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Directory164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directory164"):
                opp_val = getattr(value, "myDsl_Directory164", None)
                setattr(value, "myDsl_Directory164", self)

    @property
    def myDsl_Directory161(self):
        return self.__myDsl_Directory161

    @myDsl_Directory161.setter
    def myDsl_Directory161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Directory__myDsl_Directory161", None)
        self.__myDsl_Directory161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_File"):
                opp_val = getattr(old_value, "myDsl_File", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_File", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_File"):
                opp_val = getattr(value, "myDsl_File", None)
                setattr(value, "myDsl_File", self)

class myDsl_ReactApp(AbstractFrontElement):

    pass
class myDsl_AxiosRequest(AbstractFrontElement):

    def __init__(self, name: str, axiosRestMethod: str, url: str, myDsl_AxiosRequest: "myDsl_ServiceFront" = None, myDsl_AxiosRequest188: "myDsl_JsMethodArgs" = None):
        self.name = name
        self.axiosRestMethod = axiosRestMethod
        self.url = url
        self.myDsl_AxiosRequest = myDsl_AxiosRequest
        self.myDsl_AxiosRequest188 = myDsl_AxiosRequest188
        
    @property
    def axiosRestMethod(self) -> str:
        return self.__axiosRestMethod

    @axiosRestMethod.setter
    def axiosRestMethod(self, axiosRestMethod: str):
        self.__axiosRestMethod = axiosRestMethod

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def myDsl_AxiosRequest188(self):
        return self.__myDsl_AxiosRequest188

    @myDsl_AxiosRequest188.setter
    def myDsl_AxiosRequest188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AxiosRequest__myDsl_AxiosRequest188", None)
        self.__myDsl_AxiosRequest188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JsMethodArgs189"):
                opp_val = getattr(old_value, "myDsl_JsMethodArgs189", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_JsMethodArgs189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JsMethodArgs189"):
                opp_val = getattr(value, "myDsl_JsMethodArgs189", None)
                setattr(value, "myDsl_JsMethodArgs189", self)

    @property
    def myDsl_AxiosRequest(self):
        return self.__myDsl_AxiosRequest

    @myDsl_AxiosRequest.setter
    def myDsl_AxiosRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AxiosRequest__myDsl_AxiosRequest", None)
        self.__myDsl_AxiosRequest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ServiceFront159"):
                opp_val = getattr(old_value, "myDsl_ServiceFront159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ServiceFront159"):
                opp_val = getattr(value, "myDsl_ServiceFront159", None)
                if opp_val is None:
                    setattr(value, "myDsl_ServiceFront159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Action(AbstractFrontElement):

    def __init__(self, name: str, myDsl_Action170: "myDsl_ActionCreator" = None, myDsl_Action172: "myDsl_ActionDispatcher" = None, myDsl_Action174: "myDsl_Directory" = None, myDsl_Action: "myDsl_State" = None):
        self.name = name
        self.myDsl_Action170 = myDsl_Action170
        self.myDsl_Action172 = myDsl_Action172
        self.myDsl_Action174 = myDsl_Action174
        self.myDsl_Action = myDsl_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Action172(self):
        return self.__myDsl_Action172

    @myDsl_Action172.setter
    def myDsl_Action172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Action__myDsl_Action172", None)
        self.__myDsl_Action172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ActionDispatcher"):
                opp_val = getattr(old_value, "myDsl_ActionDispatcher", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ActionDispatcher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ActionDispatcher"):
                opp_val = getattr(value, "myDsl_ActionDispatcher", None)
                setattr(value, "myDsl_ActionDispatcher", self)

    @property
    def myDsl_Action170(self):
        return self.__myDsl_Action170

    @myDsl_Action170.setter
    def myDsl_Action170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Action__myDsl_Action170", None)
        self.__myDsl_Action170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ActionCreator"):
                opp_val = getattr(old_value, "myDsl_ActionCreator", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ActionCreator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ActionCreator"):
                opp_val = getattr(value, "myDsl_ActionCreator", None)
                setattr(value, "myDsl_ActionCreator", self)

    @property
    def myDsl_Action(self):
        return self.__myDsl_Action

    @myDsl_Action.setter
    def myDsl_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Action__myDsl_Action", None)
        self.__myDsl_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_State166"):
                opp_val = getattr(old_value, "myDsl_State166", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_State166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_State166"):
                opp_val = getattr(value, "myDsl_State166", None)
                setattr(value, "myDsl_State166", self)

    @property
    def myDsl_Action174(self):
        return self.__myDsl_Action174

    @myDsl_Action174.setter
    def myDsl_Action174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Action__myDsl_Action174", None)
        self.__myDsl_Action174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directory175"):
                opp_val = getattr(old_value, "myDsl_Directory175", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Directory175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directory175"):
                opp_val = getattr(value, "myDsl_Directory175", None)
                setattr(value, "myDsl_Directory175", self)

class myDsl_JsModule(AbstractFrontElement):

    def __init__(self, name: str, myDsl_JsModule: "myDsl_ReactApp" = None, myDsl_JsModule157: "myDsl_ServiceFront" = None, myDsl_JsModule183: "myDsl_Directory" = None):
        self.name = name
        self.myDsl_JsModule = myDsl_JsModule
        self.myDsl_JsModule157 = myDsl_JsModule157
        self.myDsl_JsModule183 = myDsl_JsModule183
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_JsModule157(self):
        return self.__myDsl_JsModule157

    @myDsl_JsModule157.setter
    def myDsl_JsModule157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsModule__myDsl_JsModule157", None)
        self.__myDsl_JsModule157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ServiceFront156"):
                opp_val = getattr(old_value, "myDsl_ServiceFront156", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ServiceFront156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ServiceFront156"):
                opp_val = getattr(value, "myDsl_ServiceFront156", None)
                setattr(value, "myDsl_ServiceFront156", self)

    @property
    def myDsl_JsModule183(self):
        return self.__myDsl_JsModule183

    @myDsl_JsModule183.setter
    def myDsl_JsModule183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsModule__myDsl_JsModule183", None)
        self.__myDsl_JsModule183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directory184"):
                opp_val = getattr(old_value, "myDsl_Directory184", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Directory184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directory184"):
                opp_val = getattr(value, "myDsl_Directory184", None)
                setattr(value, "myDsl_Directory184", self)

    @property
    def myDsl_JsModule(self):
        return self.__myDsl_JsModule

    @myDsl_JsModule.setter
    def myDsl_JsModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JsModule__myDsl_JsModule", None)
        self.__myDsl_JsModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactApp128"):
                opp_val = getattr(old_value, "myDsl_ReactApp128", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ReactApp128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactApp128"):
                opp_val = getattr(value, "myDsl_ReactApp128", None)
                setattr(value, "myDsl_ReactApp128", self)

class myDsl_ServiceFront(AbstractFrontElement):

    def __init__(self, name: str, method: str, myDsl_ServiceFront156: "myDsl_JsModule" = None, myDsl_ServiceFront: "myDsl_Functionality" = None, myDsl_ServiceFront159: set["myDsl_AxiosRequest"] = None):
        self.name = name
        self.method = method
        self.myDsl_ServiceFront156 = myDsl_ServiceFront156
        self.myDsl_ServiceFront = myDsl_ServiceFront
        self.myDsl_ServiceFront159 = myDsl_ServiceFront159 if myDsl_ServiceFront159 is not None else set()
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ServiceFront159(self):
        return self.__myDsl_ServiceFront159

    @myDsl_ServiceFront159.setter
    def myDsl_ServiceFront159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ServiceFront__myDsl_ServiceFront159", None)
        self.__myDsl_ServiceFront159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_AxiosRequest"):
                    opp_val = getattr(item, "myDsl_AxiosRequest", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_AxiosRequest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_AxiosRequest"):
                    opp_val = getattr(item, "myDsl_AxiosRequest", None)
                    
                    setattr(item, "myDsl_AxiosRequest", self)
                    

    @property
    def myDsl_ServiceFront156(self):
        return self.__myDsl_ServiceFront156

    @myDsl_ServiceFront156.setter
    def myDsl_ServiceFront156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ServiceFront__myDsl_ServiceFront156", None)
        self.__myDsl_ServiceFront156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JsModule157"):
                opp_val = getattr(old_value, "myDsl_JsModule157", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_JsModule157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JsModule157"):
                opp_val = getattr(value, "myDsl_JsModule157", None)
                setattr(value, "myDsl_JsModule157", self)

    @property
    def myDsl_ServiceFront(self):
        return self.__myDsl_ServiceFront

    @myDsl_ServiceFront.setter
    def myDsl_ServiceFront(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ServiceFront__myDsl_ServiceFront", None)
        self.__myDsl_ServiceFront = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Functionality138"):
                opp_val = getattr(old_value, "myDsl_Functionality138", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Functionality138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Functionality138"):
                opp_val = getattr(value, "myDsl_Functionality138", None)
                setattr(value, "myDsl_Functionality138", self)

class myDsl_Container(AbstractFrontElement):

    def __init__(self, name: str, myDsl_Container: "myDsl_Functionality" = None, myDsl_Container148: "myDsl_AbstractFrontElement" = None):
        self.name = name
        self.myDsl_Container = myDsl_Container
        self.myDsl_Container148 = myDsl_Container148
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Container148(self):
        return self.__myDsl_Container148

    @myDsl_Container148.setter
    def myDsl_Container148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Container__myDsl_Container148", None)
        self.__myDsl_Container148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractFrontElement149"):
                opp_val = getattr(old_value, "myDsl_AbstractFrontElement149", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractFrontElement149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractFrontElement149"):
                opp_val = getattr(value, "myDsl_AbstractFrontElement149", None)
                setattr(value, "myDsl_AbstractFrontElement149", self)

    @property
    def myDsl_Container(self):
        return self.__myDsl_Container

    @myDsl_Container.setter
    def myDsl_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Container__myDsl_Container", None)
        self.__myDsl_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Functionality132"):
                opp_val = getattr(old_value, "myDsl_Functionality132", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Functionality132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Functionality132"):
                opp_val = getattr(value, "myDsl_Functionality132", None)
                setattr(value, "myDsl_Functionality132", self)

class myDsl_RouterComponent(AbstractFrontElement, UIComponent):

    def __init__(self, name: str, myDsl_RouterComponent: "myDsl_Functionality" = None, myDsl_RouterComponent143: "myDsl_AbstractFrontElement" = None, myDsl_RouterComponent146: "myDsl_UIComponent" = None):
        self.name = name
        self.myDsl_RouterComponent = myDsl_RouterComponent
        self.myDsl_RouterComponent143 = myDsl_RouterComponent143
        self.myDsl_RouterComponent146 = myDsl_RouterComponent146
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_RouterComponent143(self):
        return self.__myDsl_RouterComponent143

    @myDsl_RouterComponent143.setter
    def myDsl_RouterComponent143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RouterComponent__myDsl_RouterComponent143", None)
        self.__myDsl_RouterComponent143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractFrontElement144"):
                opp_val = getattr(old_value, "myDsl_AbstractFrontElement144", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractFrontElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractFrontElement144"):
                opp_val = getattr(value, "myDsl_AbstractFrontElement144", None)
                setattr(value, "myDsl_AbstractFrontElement144", self)

    @property
    def myDsl_RouterComponent(self):
        return self.__myDsl_RouterComponent

    @myDsl_RouterComponent.setter
    def myDsl_RouterComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RouterComponent__myDsl_RouterComponent", None)
        self.__myDsl_RouterComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Functionality130"):
                opp_val = getattr(old_value, "myDsl_Functionality130", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Functionality130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Functionality130"):
                opp_val = getattr(value, "myDsl_Functionality130", None)
                setattr(value, "myDsl_Functionality130", self)

    @property
    def myDsl_RouterComponent146(self):
        return self.__myDsl_RouterComponent146

    @myDsl_RouterComponent146.setter
    def myDsl_RouterComponent146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RouterComponent__myDsl_RouterComponent146", None)
        self.__myDsl_RouterComponent146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_UIComponent"):
                opp_val = getattr(old_value, "myDsl_UIComponent", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_UIComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_UIComponent"):
                opp_val = getattr(value, "myDsl_UIComponent", None)
                setattr(value, "myDsl_UIComponent", self)

class myDsl_Reducer(AbstractFrontElement):

    def __init__(self, name: str, myDsl_Reducer: "myDsl_State" = None, myDsl_Reducer180: "myDsl_AbstractFrontElement" = None):
        self.name = name
        self.myDsl_Reducer = myDsl_Reducer
        self.myDsl_Reducer180 = myDsl_Reducer180
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Reducer180(self):
        return self.__myDsl_Reducer180

    @myDsl_Reducer180.setter
    def myDsl_Reducer180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Reducer__myDsl_Reducer180", None)
        self.__myDsl_Reducer180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AbstractFrontElement181"):
                opp_val = getattr(old_value, "myDsl_AbstractFrontElement181", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AbstractFrontElement181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AbstractFrontElement181"):
                opp_val = getattr(value, "myDsl_AbstractFrontElement181", None)
                setattr(value, "myDsl_AbstractFrontElement181", self)

    @property
    def myDsl_Reducer(self):
        return self.__myDsl_Reducer

    @myDsl_Reducer.setter
    def myDsl_Reducer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Reducer__myDsl_Reducer", None)
        self.__myDsl_Reducer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_State168"):
                opp_val = getattr(old_value, "myDsl_State168", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_State168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_State168"):
                opp_val = getattr(value, "myDsl_State168", None)
                setattr(value, "myDsl_State168", self)

class myDsl_ActionCreator(AbstractFrontElement):

    def __init__(self, name: str, type: str, myDsl_ActionCreator: "myDsl_Action" = None, myDsl_ActionCreator178: "myDsl_ActionDispatcher" = None):
        self.name = name
        self.type = type
        self.myDsl_ActionCreator = myDsl_ActionCreator
        self.myDsl_ActionCreator178 = myDsl_ActionCreator178
        
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
    def myDsl_ActionCreator(self):
        return self.__myDsl_ActionCreator

    @myDsl_ActionCreator.setter
    def myDsl_ActionCreator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ActionCreator__myDsl_ActionCreator", None)
        self.__myDsl_ActionCreator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Action170"):
                opp_val = getattr(old_value, "myDsl_Action170", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Action170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Action170"):
                opp_val = getattr(value, "myDsl_Action170", None)
                setattr(value, "myDsl_Action170", self)

    @property
    def myDsl_ActionCreator178(self):
        return self.__myDsl_ActionCreator178

    @myDsl_ActionCreator178.setter
    def myDsl_ActionCreator178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ActionCreator__myDsl_ActionCreator178", None)
        self.__myDsl_ActionCreator178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ActionDispatcher177"):
                opp_val = getattr(old_value, "myDsl_ActionDispatcher177", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ActionDispatcher177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ActionDispatcher177"):
                opp_val = getattr(value, "myDsl_ActionDispatcher177", None)
                setattr(value, "myDsl_ActionDispatcher177", self)

class myDsl_State(AbstractFrontElement):

    def __init__(self, name: str, myDsl_State: "myDsl_Functionality" = None, myDsl_State168: "myDsl_Reducer" = None, myDsl_State166: "myDsl_Action" = None):
        self.name = name
        self.myDsl_State = myDsl_State
        self.myDsl_State168 = myDsl_State168
        self.myDsl_State166 = myDsl_State166
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_State168(self):
        return self.__myDsl_State168

    @myDsl_State168.setter
    def myDsl_State168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State168", None)
        self.__myDsl_State168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Reducer"):
                opp_val = getattr(old_value, "myDsl_Reducer", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Reducer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Reducer"):
                opp_val = getattr(value, "myDsl_Reducer", None)
                setattr(value, "myDsl_Reducer", self)

    @property
    def myDsl_State(self):
        return self.__myDsl_State

    @myDsl_State.setter
    def myDsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State", None)
        self.__myDsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Functionality136"):
                opp_val = getattr(old_value, "myDsl_Functionality136", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Functionality136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Functionality136"):
                opp_val = getattr(value, "myDsl_Functionality136", None)
                setattr(value, "myDsl_Functionality136", self)

    @property
    def myDsl_State166(self):
        return self.__myDsl_State166

    @myDsl_State166.setter
    def myDsl_State166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State166", None)
        self.__myDsl_State166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Action"):
                opp_val = getattr(old_value, "myDsl_Action", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Action"):
                opp_val = getattr(value, "myDsl_Action", None)
                setattr(value, "myDsl_Action", self)

class myDsl_Functionality(AbstractFrontElement):

    def __init__(self, name: str, myDsl_Functionality: "myDsl_ReactApp" = None, myDsl_Functionality130: "myDsl_RouterComponent" = None, myDsl_Functionality132: "myDsl_Container" = None, myDsl_Functionality134: "myDsl_Visualizer" = None, myDsl_Functionality136: "myDsl_State" = None, myDsl_Functionality138: "myDsl_ServiceFront" = None, myDsl_Functionality140: "myDsl_Directory" = None):
        self.name = name
        self.myDsl_Functionality = myDsl_Functionality
        self.myDsl_Functionality130 = myDsl_Functionality130
        self.myDsl_Functionality132 = myDsl_Functionality132
        self.myDsl_Functionality134 = myDsl_Functionality134
        self.myDsl_Functionality136 = myDsl_Functionality136
        self.myDsl_Functionality138 = myDsl_Functionality138
        self.myDsl_Functionality140 = myDsl_Functionality140
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Functionality138(self):
        return self.__myDsl_Functionality138

    @myDsl_Functionality138.setter
    def myDsl_Functionality138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality138", None)
        self.__myDsl_Functionality138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ServiceFront"):
                opp_val = getattr(old_value, "myDsl_ServiceFront", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ServiceFront", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ServiceFront"):
                opp_val = getattr(value, "myDsl_ServiceFront", None)
                setattr(value, "myDsl_ServiceFront", self)

    @property
    def myDsl_Functionality140(self):
        return self.__myDsl_Functionality140

    @myDsl_Functionality140.setter
    def myDsl_Functionality140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality140", None)
        self.__myDsl_Functionality140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directory141"):
                opp_val = getattr(old_value, "myDsl_Directory141", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Directory141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directory141"):
                opp_val = getattr(value, "myDsl_Directory141", None)
                setattr(value, "myDsl_Directory141", self)

    @property
    def myDsl_Functionality132(self):
        return self.__myDsl_Functionality132

    @myDsl_Functionality132.setter
    def myDsl_Functionality132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality132", None)
        self.__myDsl_Functionality132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Container"):
                opp_val = getattr(old_value, "myDsl_Container", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Container"):
                opp_val = getattr(value, "myDsl_Container", None)
                setattr(value, "myDsl_Container", self)

    @property
    def myDsl_Functionality130(self):
        return self.__myDsl_Functionality130

    @myDsl_Functionality130.setter
    def myDsl_Functionality130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality130", None)
        self.__myDsl_Functionality130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RouterComponent"):
                opp_val = getattr(old_value, "myDsl_RouterComponent", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RouterComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RouterComponent"):
                opp_val = getattr(value, "myDsl_RouterComponent", None)
                setattr(value, "myDsl_RouterComponent", self)

    @property
    def myDsl_Functionality(self):
        return self.__myDsl_Functionality

    @myDsl_Functionality.setter
    def myDsl_Functionality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality", None)
        self.__myDsl_Functionality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactApp124"):
                opp_val = getattr(old_value, "myDsl_ReactApp124", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ReactApp124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactApp124"):
                opp_val = getattr(value, "myDsl_ReactApp124", None)
                setattr(value, "myDsl_ReactApp124", self)

    @property
    def myDsl_Functionality136(self):
        return self.__myDsl_Functionality136

    @myDsl_Functionality136.setter
    def myDsl_Functionality136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality136", None)
        self.__myDsl_Functionality136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_State"):
                opp_val = getattr(old_value, "myDsl_State", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_State"):
                opp_val = getattr(value, "myDsl_State", None)
                setattr(value, "myDsl_State", self)

    @property
    def myDsl_Functionality134(self):
        return self.__myDsl_Functionality134

    @myDsl_Functionality134.setter
    def myDsl_Functionality134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Functionality__myDsl_Functionality134", None)
        self.__myDsl_Functionality134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Visualizer"):
                opp_val = getattr(old_value, "myDsl_Visualizer", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Visualizer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Visualizer"):
                opp_val = getattr(value, "myDsl_Visualizer", None)
                setattr(value, "myDsl_Visualizer", self)

class myDsl_File(AbstractFrontElement):

    def __init__(self, name: str, type: str, myDsl_File: "myDsl_Directory" = None):
        self.name = name
        self.type = type
        self.myDsl_File = myDsl_File
        
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
    def myDsl_File(self):
        return self.__myDsl_File

    @myDsl_File.setter
    def myDsl_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_File__myDsl_File", None)
        self.__myDsl_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directory161"):
                opp_val = getattr(old_value, "myDsl_Directory161", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Directory161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directory161"):
                opp_val = getattr(value, "myDsl_Directory161", None)
                setattr(value, "myDsl_Directory161", self)

class myDsl_SublayerSegment:

    def __init__(self, name: str, myDsl_SublayerSegment: "myDsl_LayerSegment" = None):
        self.name = name
        self.myDsl_SublayerSegment = myDsl_SublayerSegment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_SublayerSegment(self):
        return self.__myDsl_SublayerSegment

    @myDsl_SublayerSegment.setter
    def myDsl_SublayerSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SublayerSegment__myDsl_SublayerSegment", None)
        self.__myDsl_SublayerSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LayerSegment55"):
                opp_val = getattr(old_value, "myDsl_LayerSegment55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LayerSegment55"):
                opp_val = getattr(value, "myDsl_LayerSegment55", None)
                if opp_val is None:
                    setattr(value, "myDsl_LayerSegment55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_LayerSegmentRelation:

    def __init__(self, layerSegment: str, myDsl_LayerSegmentRelation: "myDsl_LayerSegment" = None):
        self.layerSegment = layerSegment
        self.myDsl_LayerSegmentRelation = myDsl_LayerSegmentRelation
        
    @property
    def layerSegment(self) -> str:
        return self.__layerSegment

    @layerSegment.setter
    def layerSegment(self, layerSegment: str):
        self.__layerSegment = layerSegment

    @property
    def myDsl_LayerSegmentRelation(self):
        return self.__myDsl_LayerSegmentRelation

    @myDsl_LayerSegmentRelation.setter
    def myDsl_LayerSegmentRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerSegmentRelation__myDsl_LayerSegmentRelation", None)
        self.__myDsl_LayerSegmentRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LayerSegment53"):
                opp_val = getattr(old_value, "myDsl_LayerSegment53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LayerSegment53"):
                opp_val = getattr(value, "myDsl_LayerSegment53", None)
                if opp_val is None:
                    setattr(value, "myDsl_LayerSegment53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_LayerSegment:

    def __init__(self, name: str, myDsl_LayerSegment: "myDsl_Layer" = None, myDsl_LayerSegment53: set["myDsl_LayerSegmentRelation"] = None, myDsl_LayerSegment55: set["myDsl_SublayerSegment"] = None):
        self.name = name
        self.myDsl_LayerSegment = myDsl_LayerSegment
        self.myDsl_LayerSegment53 = myDsl_LayerSegment53 if myDsl_LayerSegment53 is not None else set()
        self.myDsl_LayerSegment55 = myDsl_LayerSegment55 if myDsl_LayerSegment55 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_LayerSegment53(self):
        return self.__myDsl_LayerSegment53

    @myDsl_LayerSegment53.setter
    def myDsl_LayerSegment53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerSegment__myDsl_LayerSegment53", None)
        self.__myDsl_LayerSegment53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_LayerSegmentRelation"):
                    opp_val = getattr(item, "myDsl_LayerSegmentRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_LayerSegmentRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_LayerSegmentRelation"):
                    opp_val = getattr(item, "myDsl_LayerSegmentRelation", None)
                    
                    setattr(item, "myDsl_LayerSegmentRelation", self)
                    

    @property
    def myDsl_LayerSegment55(self):
        return self.__myDsl_LayerSegment55

    @myDsl_LayerSegment55.setter
    def myDsl_LayerSegment55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerSegment__myDsl_LayerSegment55", None)
        self.__myDsl_LayerSegment55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_SublayerSegment"):
                    opp_val = getattr(item, "myDsl_SublayerSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_SublayerSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_SublayerSegment"):
                    opp_val = getattr(item, "myDsl_SublayerSegment", None)
                    
                    setattr(item, "myDsl_SublayerSegment", self)
                    

    @property
    def myDsl_LayerSegment(self):
        return self.__myDsl_LayerSegment

    @myDsl_LayerSegment.setter
    def myDsl_LayerSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerSegment__myDsl_LayerSegment", None)
        self.__myDsl_LayerSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Layer51"):
                opp_val = getattr(old_value, "myDsl_Layer51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Layer51"):
                opp_val = getattr(value, "myDsl_Layer51", None)
                if opp_val is None:
                    setattr(value, "myDsl_Layer51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Layer:

    def __init__(self, name: str, myDsl_Layer: "myDsl_Component" = None, myDsl_Layer51: set["myDsl_LayerSegment"] = None):
        self.name = name
        self.myDsl_Layer = myDsl_Layer
        self.myDsl_Layer51 = myDsl_Layer51 if myDsl_Layer51 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Layer51(self):
        return self.__myDsl_Layer51

    @myDsl_Layer51.setter
    def myDsl_Layer51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Layer__myDsl_Layer51", None)
        self.__myDsl_Layer51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_LayerSegment"):
                    opp_val = getattr(item, "myDsl_LayerSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_LayerSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_LayerSegment"):
                    opp_val = getattr(item, "myDsl_LayerSegment", None)
                    
                    setattr(item, "myDsl_LayerSegment", self)
                    

    @property
    def myDsl_Layer(self):
        return self.__myDsl_Layer

    @myDsl_Layer.setter
    def myDsl_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Layer__myDsl_Layer", None)
        self.__myDsl_Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Component49"):
                opp_val = getattr(old_value, "myDsl_Component49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Component49"):
                opp_val = getattr(value, "myDsl_Component49", None)
                if opp_val is None:
                    setattr(value, "myDsl_Component49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_EObject:

    pass
class myDsl_Operation:

    def __init__(self, type: str, myDsl_Operation18: set["myDsl_EntityName"] = None, myDsl_Operation: "myDsl_Submodule" = None):
        self.type = type
        self.myDsl_Operation18 = myDsl_Operation18 if myDsl_Operation18 is not None else set()
        self.myDsl_Operation = myDsl_Operation
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def myDsl_Operation18(self):
        return self.__myDsl_Operation18

    @myDsl_Operation18.setter
    def myDsl_Operation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Operation__myDsl_Operation18", None)
        self.__myDsl_Operation18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_EntityName"):
                    opp_val = getattr(item, "myDsl_EntityName", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_EntityName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_EntityName"):
                    opp_val = getattr(item, "myDsl_EntityName", None)
                    
                    setattr(item, "myDsl_EntityName", self)
                    

    @property
    def myDsl_Operation(self):
        return self.__myDsl_Operation

    @myDsl_Operation.setter
    def myDsl_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Operation__myDsl_Operation", None)
        self.__myDsl_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Submodule14"):
                opp_val = getattr(old_value, "myDsl_Submodule14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Submodule14"):
                opp_val = getattr(value, "myDsl_Submodule14", None)
                if opp_val is None:
                    setattr(value, "myDsl_Submodule14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Submodule:

    def __init__(self, name: str, myDsl_Submodule: "myDsl_Module" = None, myDsl_Submodule14: set["myDsl_Operation"] = None, myDsl_Submodule16: set["myDsl_EObject"] = None):
        self.name = name
        self.myDsl_Submodule = myDsl_Submodule
        self.myDsl_Submodule14 = myDsl_Submodule14 if myDsl_Submodule14 is not None else set()
        self.myDsl_Submodule16 = myDsl_Submodule16 if myDsl_Submodule16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Submodule16(self):
        return self.__myDsl_Submodule16

    @myDsl_Submodule16.setter
    def myDsl_Submodule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Submodule__myDsl_Submodule16", None)
        self.__myDsl_Submodule16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_EObject"):
                    opp_val = getattr(item, "myDsl_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_EObject"):
                    opp_val = getattr(item, "myDsl_EObject", None)
                    
                    setattr(item, "myDsl_EObject", self)
                    

    @property
    def myDsl_Submodule(self):
        return self.__myDsl_Submodule

    @myDsl_Submodule.setter
    def myDsl_Submodule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Submodule__myDsl_Submodule", None)
        self.__myDsl_Submodule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Module12"):
                opp_val = getattr(old_value, "myDsl_Module12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Module12"):
                opp_val = getattr(value, "myDsl_Module12", None)
                if opp_val is None:
                    setattr(value, "myDsl_Module12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Submodule14(self):
        return self.__myDsl_Submodule14

    @myDsl_Submodule14.setter
    def myDsl_Submodule14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Submodule__myDsl_Submodule14", None)
        self.__myDsl_Submodule14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Operation"):
                    opp_val = getattr(item, "myDsl_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Operation"):
                    opp_val = getattr(item, "myDsl_Operation", None)
                    
                    setattr(item, "myDsl_Operation", self)
                    

class myDsl_RelationDom:

    pass
class myDsl_Module:

    def __init__(self, name: str, myDsl_Module: "myDsl_Domain" = None, myDsl_Module12: set["myDsl_Submodule"] = None):
        self.name = name
        self.myDsl_Module = myDsl_Module
        self.myDsl_Module12 = myDsl_Module12 if myDsl_Module12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Module12(self):
        return self.__myDsl_Module12

    @myDsl_Module12.setter
    def myDsl_Module12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Module__myDsl_Module12", None)
        self.__myDsl_Module12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Submodule"):
                    opp_val = getattr(item, "myDsl_Submodule", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Submodule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Submodule"):
                    opp_val = getattr(item, "myDsl_Submodule", None)
                    
                    setattr(item, "myDsl_Submodule", self)
                    

    @property
    def myDsl_Module(self):
        return self.__myDsl_Module

    @myDsl_Module.setter
    def myDsl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Module__myDsl_Module", None)
        self.__myDsl_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Domain8"):
                opp_val = getattr(old_value, "myDsl_Domain8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Domain8"):
                opp_val = getattr(value, "myDsl_Domain8", None)
                if opp_val is None:
                    setattr(value, "myDsl_Domain8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Type(AbstractFrontElement):

    def __init__(self, name: str, myDsl_Type: "myDsl_Domain" = None, myDsl_Type25: "myDsl_Property" = None):
        self.name = name
        self.myDsl_Type = myDsl_Type
        self.myDsl_Type25 = myDsl_Type25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type(self):
        return self.__myDsl_Type

    @myDsl_Type.setter
    def myDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type", None)
        self.__myDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Domain6"):
                opp_val = getattr(old_value, "myDsl_Domain6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Domain6"):
                opp_val = getattr(value, "myDsl_Domain6", None)
                if opp_val is None:
                    setattr(value, "myDsl_Domain6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Type25(self):
        return self.__myDsl_Type25

    @myDsl_Type25.setter
    def myDsl_Type25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type25", None)
        self.__myDsl_Type25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Property24"):
                opp_val = getattr(old_value, "myDsl_Property24", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Property24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Property24"):
                opp_val = getattr(value, "myDsl_Property24", None)
                setattr(value, "myDsl_Property24", self)

class myDsl_Technology:

    pass
class myDsl_Architecture:

    pass
class myDsl_Property:

    def __init__(self, name: str, myDsl_Property: "myDsl_GeneralEntity" = None, myDsl_Property24: "myDsl_Type" = None, myDsl_Property30: "myDsl_SpecialEntity" = None):
        self.name = name
        self.myDsl_Property = myDsl_Property
        self.myDsl_Property24 = myDsl_Property24
        self.myDsl_Property30 = myDsl_Property30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Property24(self):
        return self.__myDsl_Property24

    @myDsl_Property24.setter
    def myDsl_Property24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Property__myDsl_Property24", None)
        self.__myDsl_Property24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type25"):
                opp_val = getattr(old_value, "myDsl_Type25", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type25"):
                opp_val = getattr(value, "myDsl_Type25", None)
                setattr(value, "myDsl_Type25", self)

    @property
    def myDsl_Property(self):
        return self.__myDsl_Property

    @myDsl_Property.setter
    def myDsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Property__myDsl_Property", None)
        self.__myDsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GeneralEntity22"):
                opp_val = getattr(old_value, "myDsl_GeneralEntity22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GeneralEntity22"):
                opp_val = getattr(value, "myDsl_GeneralEntity22", None)
                if opp_val is None:
                    setattr(value, "myDsl_GeneralEntity22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Property30(self):
        return self.__myDsl_Property30

    @myDsl_Property30.setter
    def myDsl_Property30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Property__myDsl_Property30", None)
        self.__myDsl_Property30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SpecialEntity29"):
                opp_val = getattr(old_value, "myDsl_SpecialEntity29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SpecialEntity29"):
                opp_val = getattr(value, "myDsl_SpecialEntity29", None)
                if opp_val is None:
                    setattr(value, "myDsl_SpecialEntity29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Domain:

    pass
class myDsl_GeneralEntity:

    pass
class myDsl_EntityName:

    def __init__(self, name: str, myDsl_EntityName: "myDsl_Operation" = None, myDsl_EntityName20: "myDsl_GeneralEntity" = None, myDsl_EntityName27: "myDsl_SpecialEntity" = None, myDsl_EntityName37: "myDsl_Operateson" = None, myDsl_EntityName40: "myDsl_RelationDom" = None, myDsl_EntityName43: "myDsl_RelationDom" = None):
        self.name = name
        self.myDsl_EntityName = myDsl_EntityName
        self.myDsl_EntityName20 = myDsl_EntityName20
        self.myDsl_EntityName27 = myDsl_EntityName27
        self.myDsl_EntityName37 = myDsl_EntityName37
        self.myDsl_EntityName40 = myDsl_EntityName40
        self.myDsl_EntityName43 = myDsl_EntityName43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_EntityName(self):
        return self.__myDsl_EntityName

    @myDsl_EntityName.setter
    def myDsl_EntityName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EntityName__myDsl_EntityName", None)
        self.__myDsl_EntityName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Operation18"):
                opp_val = getattr(old_value, "myDsl_Operation18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Operation18"):
                opp_val = getattr(value, "myDsl_Operation18", None)
                if opp_val is None:
                    setattr(value, "myDsl_Operation18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_EntityName27(self):
        return self.__myDsl_EntityName27

    @myDsl_EntityName27.setter
    def myDsl_EntityName27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EntityName__myDsl_EntityName27", None)
        self.__myDsl_EntityName27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SpecialEntity"):
                opp_val = getattr(old_value, "myDsl_SpecialEntity", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SpecialEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SpecialEntity"):
                opp_val = getattr(value, "myDsl_SpecialEntity", None)
                setattr(value, "myDsl_SpecialEntity", self)

    @property
    def myDsl_EntityName40(self):
        return self.__myDsl_EntityName40

    @myDsl_EntityName40.setter
    def myDsl_EntityName40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EntityName__myDsl_EntityName40", None)
        self.__myDsl_EntityName40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RelationDom39"):
                opp_val = getattr(old_value, "myDsl_RelationDom39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RelationDom39"):
                opp_val = getattr(value, "myDsl_RelationDom39", None)
                if opp_val is None:
                    setattr(value, "myDsl_RelationDom39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_EntityName43(self):
        return self.__myDsl_EntityName43

    @myDsl_EntityName43.setter
    def myDsl_EntityName43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EntityName__myDsl_EntityName43", None)
        self.__myDsl_EntityName43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RelationDom42"):
                opp_val = getattr(old_value, "myDsl_RelationDom42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RelationDom42"):
                opp_val = getattr(value, "myDsl_RelationDom42", None)
                if opp_val is None:
                    setattr(value, "myDsl_RelationDom42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_EntityName20(self):
        return self.__myDsl_EntityName20

    @myDsl_EntityName20.setter
    def myDsl_EntityName20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EntityName__myDsl_EntityName20", None)
        self.__myDsl_EntityName20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GeneralEntity"):
                opp_val = getattr(old_value, "myDsl_GeneralEntity", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_GeneralEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GeneralEntity"):
                opp_val = getattr(value, "myDsl_GeneralEntity", None)
                setattr(value, "myDsl_GeneralEntity", self)

    @property
    def myDsl_EntityName37(self):
        return self.__myDsl_EntityName37

    @myDsl_EntityName37.setter
    def myDsl_EntityName37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_EntityName__myDsl_EntityName37", None)
        self.__myDsl_EntityName37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Operateson36"):
                opp_val = getattr(old_value, "myDsl_Operateson36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Operateson36"):
                opp_val = getattr(value, "myDsl_Operateson36", None)
                if opp_val is None:
                    setattr(value, "myDsl_Operateson36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_System:

    pass