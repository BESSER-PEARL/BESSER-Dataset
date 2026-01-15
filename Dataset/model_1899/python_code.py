from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class File:

    pass
class dsl_Css(File):

    pass
class dsl_Json(File):

    pass
class dsl_Js(File):

    pass
class dsl_Md(File):

    pass
class dsl_UIComponent:

    pass
class UIComponent:

    pass
class dsl_AbstractFrontElement:

    pass
class dsl_Einterface:

    def __init__(self, name: str, dsl_Einterface94: set["dsl_AbstractMethod"] = None, dsl_Einterface: "dsl_GenericClass" = None, dsl_Einterface91: set["dsl_Attribute"] = None):
        self.name = name
        self.dsl_Einterface94 = dsl_Einterface94 if dsl_Einterface94 is not None else set()
        self.dsl_Einterface = dsl_Einterface
        self.dsl_Einterface91 = dsl_Einterface91 if dsl_Einterface91 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Einterface(self):
        return self.__dsl_Einterface

    @dsl_Einterface.setter
    def dsl_Einterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Einterface__dsl_Einterface", None)
        self.__dsl_Einterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_GenericClass89"):
                opp_val = getattr(old_value, "dsl_GenericClass89", None)
                if opp_val == self:
                    setattr(old_value, "dsl_GenericClass89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_GenericClass89"):
                opp_val = getattr(value, "dsl_GenericClass89", None)
                setattr(value, "dsl_GenericClass89", self)

    @property
    def dsl_Einterface91(self):
        return self.__dsl_Einterface91

    @dsl_Einterface91.setter
    def dsl_Einterface91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Einterface__dsl_Einterface91", None)
        self.__dsl_Einterface91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Attribute92"):
                    opp_val = getattr(item, "dsl_Attribute92", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Attribute92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Attribute92"):
                    opp_val = getattr(item, "dsl_Attribute92", None)
                    
                    setattr(item, "dsl_Attribute92", self)
                    

    @property
    def dsl_Einterface94(self):
        return self.__dsl_Einterface94

    @dsl_Einterface94.setter
    def dsl_Einterface94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Einterface__dsl_Einterface94", None)
        self.__dsl_Einterface94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_AbstractMethod95"):
                    opp_val = getattr(item, "dsl_AbstractMethod95", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_AbstractMethod95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_AbstractMethod95"):
                    opp_val = getattr(item, "dsl_AbstractMethod95", None)
                    
                    setattr(item, "dsl_AbstractMethod95", self)
                    

class dsl_Eclass:

    def __init__(self, name: str, dsl_Eclass108: "dsl_MethodBack" = None, dsl_Eclass111: "dsl_MethodBack" = None, dsl_Eclass114: "dsl_AbstractMethod" = None, dsl_Eclass117: "dsl_AbstractMethod" = None, dsl_Eclass: "dsl_Attribute" = None, dsl_Eclass105: "dsl_Epackage" = None):
        self.name = name
        self.dsl_Eclass108 = dsl_Eclass108
        self.dsl_Eclass111 = dsl_Eclass111
        self.dsl_Eclass114 = dsl_Eclass114
        self.dsl_Eclass117 = dsl_Eclass117
        self.dsl_Eclass = dsl_Eclass
        self.dsl_Eclass105 = dsl_Eclass105
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Eclass108(self):
        return self.__dsl_Eclass108

    @dsl_Eclass108.setter
    def dsl_Eclass108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Eclass__dsl_Eclass108", None)
        self.__dsl_Eclass108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MethodBack107"):
                opp_val = getattr(old_value, "dsl_MethodBack107", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MethodBack107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MethodBack107"):
                opp_val = getattr(value, "dsl_MethodBack107", None)
                setattr(value, "dsl_MethodBack107", self)

    @property
    def dsl_Eclass117(self):
        return self.__dsl_Eclass117

    @dsl_Eclass117.setter
    def dsl_Eclass117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Eclass__dsl_Eclass117", None)
        self.__dsl_Eclass117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractMethod116"):
                opp_val = getattr(old_value, "dsl_AbstractMethod116", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractMethod116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractMethod116"):
                opp_val = getattr(value, "dsl_AbstractMethod116", None)
                setattr(value, "dsl_AbstractMethod116", self)

    @property
    def dsl_Eclass111(self):
        return self.__dsl_Eclass111

    @dsl_Eclass111.setter
    def dsl_Eclass111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Eclass__dsl_Eclass111", None)
        self.__dsl_Eclass111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_MethodBack110"):
                opp_val = getattr(old_value, "dsl_MethodBack110", None)
                if opp_val == self:
                    setattr(old_value, "dsl_MethodBack110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_MethodBack110"):
                opp_val = getattr(value, "dsl_MethodBack110", None)
                setattr(value, "dsl_MethodBack110", self)

    @property
    def dsl_Eclass114(self):
        return self.__dsl_Eclass114

    @dsl_Eclass114.setter
    def dsl_Eclass114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Eclass__dsl_Eclass114", None)
        self.__dsl_Eclass114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractMethod113"):
                opp_val = getattr(old_value, "dsl_AbstractMethod113", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractMethod113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractMethod113"):
                opp_val = getattr(value, "dsl_AbstractMethod113", None)
                setattr(value, "dsl_AbstractMethod113", self)

    @property
    def dsl_Eclass105(self):
        return self.__dsl_Eclass105

    @dsl_Eclass105.setter
    def dsl_Eclass105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Eclass__dsl_Eclass105", None)
        self.__dsl_Eclass105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Epackage104"):
                opp_val = getattr(old_value, "dsl_Epackage104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Epackage104"):
                opp_val = getattr(value, "dsl_Epackage104", None)
                if opp_val is None:
                    setattr(value, "dsl_Epackage104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Eclass(self):
        return self.__dsl_Eclass

    @dsl_Eclass.setter
    def dsl_Eclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Eclass__dsl_Eclass", None)
        self.__dsl_Eclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Attribute102"):
                opp_val = getattr(old_value, "dsl_Attribute102", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Attribute102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Attribute102"):
                opp_val = getattr(value, "dsl_Attribute102", None)
                setattr(value, "dsl_Attribute102", self)

class dsl_MethodBack:

    def __init__(self, name: str, dsl_MethodBack81: "dsl_GenericClass" = None, dsl_MethodBack: "dsl_AbstractClass" = None, dsl_MethodBack100: "dsl_NativeClass" = None, dsl_MethodBack107: "dsl_Eclass" = None, dsl_MethodBack110: "dsl_Eclass" = None):
        self.name = name
        self.dsl_MethodBack81 = dsl_MethodBack81
        self.dsl_MethodBack = dsl_MethodBack
        self.dsl_MethodBack100 = dsl_MethodBack100
        self.dsl_MethodBack107 = dsl_MethodBack107
        self.dsl_MethodBack110 = dsl_MethodBack110
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_MethodBack110(self):
        return self.__dsl_MethodBack110

    @dsl_MethodBack110.setter
    def dsl_MethodBack110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodBack__dsl_MethodBack110", None)
        self.__dsl_MethodBack110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Eclass111"):
                opp_val = getattr(old_value, "dsl_Eclass111", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Eclass111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Eclass111"):
                opp_val = getattr(value, "dsl_Eclass111", None)
                setattr(value, "dsl_Eclass111", self)

    @property
    def dsl_MethodBack100(self):
        return self.__dsl_MethodBack100

    @dsl_MethodBack100.setter
    def dsl_MethodBack100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodBack__dsl_MethodBack100", None)
        self.__dsl_MethodBack100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_NativeClass99"):
                opp_val = getattr(old_value, "dsl_NativeClass99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_NativeClass99"):
                opp_val = getattr(value, "dsl_NativeClass99", None)
                if opp_val is None:
                    setattr(value, "dsl_NativeClass99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_MethodBack107(self):
        return self.__dsl_MethodBack107

    @dsl_MethodBack107.setter
    def dsl_MethodBack107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodBack__dsl_MethodBack107", None)
        self.__dsl_MethodBack107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Eclass108"):
                opp_val = getattr(old_value, "dsl_Eclass108", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Eclass108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Eclass108"):
                opp_val = getattr(value, "dsl_Eclass108", None)
                setattr(value, "dsl_Eclass108", self)

    @property
    def dsl_MethodBack(self):
        return self.__dsl_MethodBack

    @dsl_MethodBack.setter
    def dsl_MethodBack(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodBack__dsl_MethodBack", None)
        self.__dsl_MethodBack = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractClass72"):
                opp_val = getattr(old_value, "dsl_AbstractClass72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractClass72"):
                opp_val = getattr(value, "dsl_AbstractClass72", None)
                if opp_val is None:
                    setattr(value, "dsl_AbstractClass72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_MethodBack81(self):
        return self.__dsl_MethodBack81

    @dsl_MethodBack81.setter
    def dsl_MethodBack81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_MethodBack__dsl_MethodBack81", None)
        self.__dsl_MethodBack81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_GenericClass80"):
                opp_val = getattr(old_value, "dsl_GenericClass80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_GenericClass80"):
                opp_val = getattr(value, "dsl_GenericClass80", None)
                if opp_val is None:
                    setattr(value, "dsl_GenericClass80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Attribute:

    def __init__(self, name: str, dsl_Attribute78: "dsl_GenericClass" = None, dsl_Attribute: "dsl_AbstractClass" = None, dsl_Attribute97: "dsl_NativeClass" = None, dsl_Attribute92: "dsl_Einterface" = None, dsl_Attribute102: "dsl_Eclass" = None):
        self.name = name
        self.dsl_Attribute78 = dsl_Attribute78
        self.dsl_Attribute = dsl_Attribute
        self.dsl_Attribute97 = dsl_Attribute97
        self.dsl_Attribute92 = dsl_Attribute92
        self.dsl_Attribute102 = dsl_Attribute102
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Attribute(self):
        return self.__dsl_Attribute

    @dsl_Attribute.setter
    def dsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Attribute__dsl_Attribute", None)
        self.__dsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractClass"):
                opp_val = getattr(old_value, "dsl_AbstractClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractClass"):
                opp_val = getattr(value, "dsl_AbstractClass", None)
                if opp_val is None:
                    setattr(value, "dsl_AbstractClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Attribute78(self):
        return self.__dsl_Attribute78

    @dsl_Attribute78.setter
    def dsl_Attribute78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Attribute__dsl_Attribute78", None)
        self.__dsl_Attribute78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_GenericClass"):
                opp_val = getattr(old_value, "dsl_GenericClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_GenericClass"):
                opp_val = getattr(value, "dsl_GenericClass", None)
                if opp_val is None:
                    setattr(value, "dsl_GenericClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Attribute102(self):
        return self.__dsl_Attribute102

    @dsl_Attribute102.setter
    def dsl_Attribute102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Attribute__dsl_Attribute102", None)
        self.__dsl_Attribute102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Eclass"):
                opp_val = getattr(old_value, "dsl_Eclass", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Eclass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Eclass"):
                opp_val = getattr(value, "dsl_Eclass", None)
                setattr(value, "dsl_Eclass", self)

    @property
    def dsl_Attribute92(self):
        return self.__dsl_Attribute92

    @dsl_Attribute92.setter
    def dsl_Attribute92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Attribute__dsl_Attribute92", None)
        self.__dsl_Attribute92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Einterface91"):
                opp_val = getattr(old_value, "dsl_Einterface91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Einterface91"):
                opp_val = getattr(value, "dsl_Einterface91", None)
                if opp_val is None:
                    setattr(value, "dsl_Einterface91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Attribute97(self):
        return self.__dsl_Attribute97

    @dsl_Attribute97.setter
    def dsl_Attribute97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Attribute__dsl_Attribute97", None)
        self.__dsl_Attribute97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_NativeClass"):
                opp_val = getattr(old_value, "dsl_NativeClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_NativeClass"):
                opp_val = getattr(value, "dsl_NativeClass", None)
                if opp_val is None:
                    setattr(value, "dsl_NativeClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Eclass:

    pass
class dsl_Annotation(Eclass):

    def __init__(self, propertie: str, dsl_Annotation84: "dsl_GenericClass" = None, dsl_Annotation: "dsl_AbstractClass" = None, dsl_Annotation120: "dsl_Library" = None):
        self.propertie = propertie
        self.dsl_Annotation84 = dsl_Annotation84
        self.dsl_Annotation = dsl_Annotation
        self.dsl_Annotation120 = dsl_Annotation120
        
    @property
    def propertie(self) -> str:
        return self.__propertie

    @propertie.setter
    def propertie(self, propertie: str):
        self.__propertie = propertie

    @property
    def dsl_Annotation120(self):
        return self.__dsl_Annotation120

    @dsl_Annotation120.setter
    def dsl_Annotation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Annotation__dsl_Annotation120", None)
        self.__dsl_Annotation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Library119"):
                opp_val = getattr(old_value, "dsl_Library119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Library119"):
                opp_val = getattr(value, "dsl_Library119", None)
                if opp_val is None:
                    setattr(value, "dsl_Library119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Annotation84(self):
        return self.__dsl_Annotation84

    @dsl_Annotation84.setter
    def dsl_Annotation84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Annotation__dsl_Annotation84", None)
        self.__dsl_Annotation84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_GenericClass83"):
                opp_val = getattr(old_value, "dsl_GenericClass83", None)
                if opp_val == self:
                    setattr(old_value, "dsl_GenericClass83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_GenericClass83"):
                opp_val = getattr(value, "dsl_GenericClass83", None)
                setattr(value, "dsl_GenericClass83", self)

    @property
    def dsl_Annotation(self):
        return self.__dsl_Annotation

    @dsl_Annotation.setter
    def dsl_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Annotation__dsl_Annotation", None)
        self.__dsl_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractClass74"):
                opp_val = getattr(old_value, "dsl_AbstractClass74", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractClass74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractClass74"):
                opp_val = getattr(value, "dsl_AbstractClass74", None)
                setattr(value, "dsl_AbstractClass74", self)

class dsl_NativeClass(Eclass):

    pass
class dsl_AbstractClass(Eclass):

    pass
class dsl_GenericClass(Eclass):

    pass
class dsl_AbstractMethod:

    def __init__(self, name: str, dsl_AbstractMethod: "dsl_AbstractClass" = None, dsl_AbstractMethod95: "dsl_Einterface" = None, dsl_AbstractMethod113: "dsl_Eclass" = None, dsl_AbstractMethod116: "dsl_Eclass" = None):
        self.name = name
        self.dsl_AbstractMethod = dsl_AbstractMethod
        self.dsl_AbstractMethod95 = dsl_AbstractMethod95
        self.dsl_AbstractMethod113 = dsl_AbstractMethod113
        self.dsl_AbstractMethod116 = dsl_AbstractMethod116
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_AbstractMethod95(self):
        return self.__dsl_AbstractMethod95

    @dsl_AbstractMethod95.setter
    def dsl_AbstractMethod95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AbstractMethod__dsl_AbstractMethod95", None)
        self.__dsl_AbstractMethod95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Einterface94"):
                opp_val = getattr(old_value, "dsl_Einterface94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Einterface94"):
                opp_val = getattr(value, "dsl_Einterface94", None)
                if opp_val is None:
                    setattr(value, "dsl_Einterface94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_AbstractMethod116(self):
        return self.__dsl_AbstractMethod116

    @dsl_AbstractMethod116.setter
    def dsl_AbstractMethod116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AbstractMethod__dsl_AbstractMethod116", None)
        self.__dsl_AbstractMethod116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Eclass117"):
                opp_val = getattr(old_value, "dsl_Eclass117", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Eclass117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Eclass117"):
                opp_val = getattr(value, "dsl_Eclass117", None)
                setattr(value, "dsl_Eclass117", self)

    @property
    def dsl_AbstractMethod113(self):
        return self.__dsl_AbstractMethod113

    @dsl_AbstractMethod113.setter
    def dsl_AbstractMethod113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AbstractMethod__dsl_AbstractMethod113", None)
        self.__dsl_AbstractMethod113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Eclass114"):
                opp_val = getattr(old_value, "dsl_Eclass114", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Eclass114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Eclass114"):
                opp_val = getattr(value, "dsl_Eclass114", None)
                setattr(value, "dsl_Eclass114", self)

    @property
    def dsl_AbstractMethod(self):
        return self.__dsl_AbstractMethod

    @dsl_AbstractMethod.setter
    def dsl_AbstractMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AbstractMethod__dsl_AbstractMethod", None)
        self.__dsl_AbstractMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractClass76"):
                opp_val = getattr(old_value, "dsl_AbstractClass76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractClass76"):
                opp_val = getattr(value, "dsl_AbstractClass76", None)
                if opp_val is None:
                    setattr(value, "dsl_AbstractClass76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Subproject:

    def __init__(self, name: str, dsl_Subproject65: set["dsl_Epackage"] = None, dsl_Subproject67: set["dsl_Library"] = None, dsl_Subproject69: set["dsl_Descriptor"] = None, dsl_Subproject: "dsl_JeeProject" = None):
        self.name = name
        self.dsl_Subproject65 = dsl_Subproject65 if dsl_Subproject65 is not None else set()
        self.dsl_Subproject67 = dsl_Subproject67 if dsl_Subproject67 is not None else set()
        self.dsl_Subproject69 = dsl_Subproject69 if dsl_Subproject69 is not None else set()
        self.dsl_Subproject = dsl_Subproject
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Subproject(self):
        return self.__dsl_Subproject

    @dsl_Subproject.setter
    def dsl_Subproject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Subproject__dsl_Subproject", None)
        self.__dsl_Subproject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_JeeProject63"):
                opp_val = getattr(old_value, "dsl_JeeProject63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_JeeProject63"):
                opp_val = getattr(value, "dsl_JeeProject63", None)
                if opp_val is None:
                    setattr(value, "dsl_JeeProject63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Subproject67(self):
        return self.__dsl_Subproject67

    @dsl_Subproject67.setter
    def dsl_Subproject67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Subproject__dsl_Subproject67", None)
        self.__dsl_Subproject67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Library"):
                    opp_val = getattr(item, "dsl_Library", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Library", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Library"):
                    opp_val = getattr(item, "dsl_Library", None)
                    
                    setattr(item, "dsl_Library", self)
                    

    @property
    def dsl_Subproject65(self):
        return self.__dsl_Subproject65

    @dsl_Subproject65.setter
    def dsl_Subproject65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Subproject__dsl_Subproject65", None)
        self.__dsl_Subproject65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Epackage"):
                    opp_val = getattr(item, "dsl_Epackage", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Epackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Epackage"):
                    opp_val = getattr(item, "dsl_Epackage", None)
                    
                    setattr(item, "dsl_Epackage", self)
                    

    @property
    def dsl_Subproject69(self):
        return self.__dsl_Subproject69

    @dsl_Subproject69.setter
    def dsl_Subproject69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Subproject__dsl_Subproject69", None)
        self.__dsl_Subproject69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Descriptor"):
                    opp_val = getattr(item, "dsl_Descriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Descriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Descriptor"):
                    opp_val = getattr(item, "dsl_Descriptor", None)
                    
                    setattr(item, "dsl_Descriptor", self)
                    

class dsl_Descriptor:

    def __init__(self, name: str, dsl_Descriptor: "dsl_Subproject" = None):
        self.name = name
        self.dsl_Descriptor = dsl_Descriptor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Descriptor(self):
        return self.__dsl_Descriptor

    @dsl_Descriptor.setter
    def dsl_Descriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Descriptor__dsl_Descriptor", None)
        self.__dsl_Descriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Subproject69"):
                opp_val = getattr(old_value, "dsl_Subproject69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Subproject69"):
                opp_val = getattr(value, "dsl_Subproject69", None)
                if opp_val is None:
                    setattr(value, "dsl_Subproject69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Library:

    def __init__(self, name: str, isNative: str, dsl_Library: "dsl_Subproject" = None, dsl_Library119: set["dsl_Annotation"] = None):
        self.name = name
        self.isNative = isNative
        self.dsl_Library = dsl_Library
        self.dsl_Library119 = dsl_Library119 if dsl_Library119 is not None else set()
        
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
    def dsl_Library119(self):
        return self.__dsl_Library119

    @dsl_Library119.setter
    def dsl_Library119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Library__dsl_Library119", None)
        self.__dsl_Library119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Annotation120"):
                    opp_val = getattr(item, "dsl_Annotation120", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Annotation120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Annotation120"):
                    opp_val = getattr(item, "dsl_Annotation120", None)
                    
                    setattr(item, "dsl_Annotation120", self)
                    

    @property
    def dsl_Library(self):
        return self.__dsl_Library

    @dsl_Library.setter
    def dsl_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Library__dsl_Library", None)
        self.__dsl_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Subproject67"):
                opp_val = getattr(old_value, "dsl_Subproject67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Subproject67"):
                opp_val = getattr(value, "dsl_Subproject67", None)
                if opp_val is None:
                    setattr(value, "dsl_Subproject67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Epackage:

    def __init__(self, name: str, dsl_Epackage: "dsl_Subproject" = None, dsl_Epackage104: set["dsl_Eclass"] = None):
        self.name = name
        self.dsl_Epackage = dsl_Epackage
        self.dsl_Epackage104 = dsl_Epackage104 if dsl_Epackage104 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Epackage104(self):
        return self.__dsl_Epackage104

    @dsl_Epackage104.setter
    def dsl_Epackage104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Epackage__dsl_Epackage104", None)
        self.__dsl_Epackage104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Eclass105"):
                    opp_val = getattr(item, "dsl_Eclass105", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Eclass105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Eclass105"):
                    opp_val = getattr(item, "dsl_Eclass105", None)
                    
                    setattr(item, "dsl_Eclass105", self)
                    

    @property
    def dsl_Epackage(self):
        return self.__dsl_Epackage

    @dsl_Epackage.setter
    def dsl_Epackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Epackage__dsl_Epackage", None)
        self.__dsl_Epackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Subproject65"):
                opp_val = getattr(old_value, "dsl_Subproject65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Subproject65"):
                opp_val = getattr(value, "dsl_Subproject65", None)
                if opp_val is None:
                    setattr(value, "dsl_Subproject65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_JeeProject:

    def __init__(self, name: str, dsl_JeeProject: "dsl_JavaApp" = None, dsl_JeeProject63: set["dsl_Subproject"] = None):
        self.name = name
        self.dsl_JeeProject = dsl_JeeProject
        self.dsl_JeeProject63 = dsl_JeeProject63 if dsl_JeeProject63 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_JeeProject63(self):
        return self.__dsl_JeeProject63

    @dsl_JeeProject63.setter
    def dsl_JeeProject63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_JeeProject__dsl_JeeProject63", None)
        self.__dsl_JeeProject63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Subproject"):
                    opp_val = getattr(item, "dsl_Subproject", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Subproject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Subproject"):
                    opp_val = getattr(item, "dsl_Subproject", None)
                    
                    setattr(item, "dsl_Subproject", self)
                    

    @property
    def dsl_JeeProject(self):
        return self.__dsl_JeeProject

    @dsl_JeeProject.setter
    def dsl_JeeProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_JeeProject__dsl_JeeProject", None)
        self.__dsl_JeeProject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_JavaApp61"):
                opp_val = getattr(old_value, "dsl_JavaApp61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_JavaApp61"):
                opp_val = getattr(value, "dsl_JavaApp61", None)
                if opp_val is None:
                    setattr(value, "dsl_JavaApp61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_JavaApp:

    pass
class dsl_LayerSegmentRelation:

    def __init__(self, layerSegment: str, dsl_LayerSegmentRelation: "dsl_LayerSegment" = None):
        self.layerSegment = layerSegment
        self.dsl_LayerSegmentRelation = dsl_LayerSegmentRelation
        
    @property
    def layerSegment(self) -> str:
        return self.__layerSegment

    @layerSegment.setter
    def layerSegment(self, layerSegment: str):
        self.__layerSegment = layerSegment

    @property
    def dsl_LayerSegmentRelation(self):
        return self.__dsl_LayerSegmentRelation

    @dsl_LayerSegmentRelation.setter
    def dsl_LayerSegmentRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LayerSegmentRelation__dsl_LayerSegmentRelation", None)
        self.__dsl_LayerSegmentRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_LayerSegment53"):
                opp_val = getattr(old_value, "dsl_LayerSegment53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_LayerSegment53"):
                opp_val = getattr(value, "dsl_LayerSegment53", None)
                if opp_val is None:
                    setattr(value, "dsl_LayerSegment53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_SublayerSegment:

    def __init__(self, name: str, dsl_SublayerSegment: "dsl_LayerSegment" = None):
        self.name = name
        self.dsl_SublayerSegment = dsl_SublayerSegment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_SublayerSegment(self):
        return self.__dsl_SublayerSegment

    @dsl_SublayerSegment.setter
    def dsl_SublayerSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_SublayerSegment__dsl_SublayerSegment", None)
        self.__dsl_SublayerSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_LayerSegment55"):
                opp_val = getattr(old_value, "dsl_LayerSegment55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_LayerSegment55"):
                opp_val = getattr(value, "dsl_LayerSegment55", None)
                if opp_val is None:
                    setattr(value, "dsl_LayerSegment55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_LayerSegment:

    def __init__(self, name: str, dsl_LayerSegment: "dsl_Layer" = None, dsl_LayerSegment53: set["dsl_LayerSegmentRelation"] = None, dsl_LayerSegment55: set["dsl_SublayerSegment"] = None):
        self.name = name
        self.dsl_LayerSegment = dsl_LayerSegment
        self.dsl_LayerSegment53 = dsl_LayerSegment53 if dsl_LayerSegment53 is not None else set()
        self.dsl_LayerSegment55 = dsl_LayerSegment55 if dsl_LayerSegment55 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_LayerSegment53(self):
        return self.__dsl_LayerSegment53

    @dsl_LayerSegment53.setter
    def dsl_LayerSegment53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LayerSegment__dsl_LayerSegment53", None)
        self.__dsl_LayerSegment53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_LayerSegmentRelation"):
                    opp_val = getattr(item, "dsl_LayerSegmentRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_LayerSegmentRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_LayerSegmentRelation"):
                    opp_val = getattr(item, "dsl_LayerSegmentRelation", None)
                    
                    setattr(item, "dsl_LayerSegmentRelation", self)
                    

    @property
    def dsl_LayerSegment55(self):
        return self.__dsl_LayerSegment55

    @dsl_LayerSegment55.setter
    def dsl_LayerSegment55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LayerSegment__dsl_LayerSegment55", None)
        self.__dsl_LayerSegment55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_SublayerSegment"):
                    opp_val = getattr(item, "dsl_SublayerSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_SublayerSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_SublayerSegment"):
                    opp_val = getattr(item, "dsl_SublayerSegment", None)
                    
                    setattr(item, "dsl_SublayerSegment", self)
                    

    @property
    def dsl_LayerSegment(self):
        return self.__dsl_LayerSegment

    @dsl_LayerSegment.setter
    def dsl_LayerSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_LayerSegment__dsl_LayerSegment", None)
        self.__dsl_LayerSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Layer51"):
                opp_val = getattr(old_value, "dsl_Layer51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Layer51"):
                opp_val = getattr(value, "dsl_Layer51", None)
                if opp_val is None:
                    setattr(value, "dsl_Layer51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_RelationArch:

    def __init__(self, name: str, source: str, dsl_RelationArch: "dsl_Architecture" = None):
        self.name = name
        self.source = source
        self.dsl_RelationArch = dsl_RelationArch
        
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
    def dsl_RelationArch(self):
        return self.__dsl_RelationArch

    @dsl_RelationArch.setter
    def dsl_RelationArch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RelationArch__dsl_RelationArch", None)
        self.__dsl_RelationArch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Architecture47"):
                opp_val = getattr(old_value, "dsl_Architecture47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Architecture47"):
                opp_val = getattr(value, "dsl_Architecture47", None)
                if opp_val is None:
                    setattr(value, "dsl_Architecture47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Layer:

    def __init__(self, name: str, dsl_Layer51: set["dsl_LayerSegment"] = None, dsl_Layer: "dsl_Component" = None):
        self.name = name
        self.dsl_Layer51 = dsl_Layer51 if dsl_Layer51 is not None else set()
        self.dsl_Layer = dsl_Layer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Layer51(self):
        return self.__dsl_Layer51

    @dsl_Layer51.setter
    def dsl_Layer51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Layer__dsl_Layer51", None)
        self.__dsl_Layer51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_LayerSegment"):
                    opp_val = getattr(item, "dsl_LayerSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_LayerSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_LayerSegment"):
                    opp_val = getattr(item, "dsl_LayerSegment", None)
                    
                    setattr(item, "dsl_LayerSegment", self)
                    

    @property
    def dsl_Layer(self):
        return self.__dsl_Layer

    @dsl_Layer.setter
    def dsl_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Layer__dsl_Layer", None)
        self.__dsl_Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Component49"):
                opp_val = getattr(old_value, "dsl_Component49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Component49"):
                opp_val = getattr(value, "dsl_Component49", None)
                if opp_val is None:
                    setattr(value, "dsl_Component49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Component:

    def __init__(self, name: str, dsl_Component: "dsl_Architecture" = None, dsl_Component49: set["dsl_Layer"] = None):
        self.name = name
        self.dsl_Component = dsl_Component
        self.dsl_Component49 = dsl_Component49 if dsl_Component49 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Component49(self):
        return self.__dsl_Component49

    @dsl_Component49.setter
    def dsl_Component49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Component__dsl_Component49", None)
        self.__dsl_Component49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Layer"):
                    opp_val = getattr(item, "dsl_Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Layer"):
                    opp_val = getattr(item, "dsl_Layer", None)
                    
                    setattr(item, "dsl_Layer", self)
                    

    @property
    def dsl_Component(self):
        return self.__dsl_Component

    @dsl_Component.setter
    def dsl_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Component__dsl_Component", None)
        self.__dsl_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Architecture45"):
                opp_val = getattr(old_value, "dsl_Architecture45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Architecture45"):
                opp_val = getattr(value, "dsl_Architecture45", None)
                if opp_val is None:
                    setattr(value, "dsl_Architecture45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Transaction:

    def __init__(self, type: str, dsl_Transaction34: set["dsl_Operateson"] = None, dsl_Transaction: "dsl_SpecialEntity" = None):
        self.type = type
        self.dsl_Transaction34 = dsl_Transaction34 if dsl_Transaction34 is not None else set()
        self.dsl_Transaction = dsl_Transaction
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dsl_Transaction34(self):
        return self.__dsl_Transaction34

    @dsl_Transaction34.setter
    def dsl_Transaction34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Transaction__dsl_Transaction34", None)
        self.__dsl_Transaction34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Operateson"):
                    opp_val = getattr(item, "dsl_Operateson", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Operateson", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Operateson"):
                    opp_val = getattr(item, "dsl_Operateson", None)
                    
                    setattr(item, "dsl_Operateson", self)
                    

    @property
    def dsl_Transaction(self):
        return self.__dsl_Transaction

    @dsl_Transaction.setter
    def dsl_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Transaction__dsl_Transaction", None)
        self.__dsl_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SpecialEntity32"):
                opp_val = getattr(old_value, "dsl_SpecialEntity32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SpecialEntity32"):
                opp_val = getattr(value, "dsl_SpecialEntity32", None)
                if opp_val is None:
                    setattr(value, "dsl_SpecialEntity32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_SpecialEntity:

    pass
class dsl_Operateson:

    pass
class dsl_EntityName:

    def __init__(self, name: str, dsl_EntityName20: "dsl_GeneralEntity" = None, dsl_EntityName: "dsl_Operation" = None, dsl_EntityName37: "dsl_Operateson" = None, dsl_EntityName27: "dsl_SpecialEntity" = None, dsl_EntityName40: "dsl_RelationDom" = None, dsl_EntityName43: "dsl_RelationDom" = None):
        self.name = name
        self.dsl_EntityName20 = dsl_EntityName20
        self.dsl_EntityName = dsl_EntityName
        self.dsl_EntityName37 = dsl_EntityName37
        self.dsl_EntityName27 = dsl_EntityName27
        self.dsl_EntityName40 = dsl_EntityName40
        self.dsl_EntityName43 = dsl_EntityName43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_EntityName37(self):
        return self.__dsl_EntityName37

    @dsl_EntityName37.setter
    def dsl_EntityName37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EntityName__dsl_EntityName37", None)
        self.__dsl_EntityName37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Operateson36"):
                opp_val = getattr(old_value, "dsl_Operateson36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Operateson36"):
                opp_val = getattr(value, "dsl_Operateson36", None)
                if opp_val is None:
                    setattr(value, "dsl_Operateson36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_EntityName27(self):
        return self.__dsl_EntityName27

    @dsl_EntityName27.setter
    def dsl_EntityName27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EntityName__dsl_EntityName27", None)
        self.__dsl_EntityName27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SpecialEntity"):
                opp_val = getattr(old_value, "dsl_SpecialEntity", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SpecialEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SpecialEntity"):
                opp_val = getattr(value, "dsl_SpecialEntity", None)
                setattr(value, "dsl_SpecialEntity", self)

    @property
    def dsl_EntityName40(self):
        return self.__dsl_EntityName40

    @dsl_EntityName40.setter
    def dsl_EntityName40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EntityName__dsl_EntityName40", None)
        self.__dsl_EntityName40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_RelationDom39"):
                opp_val = getattr(old_value, "dsl_RelationDom39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_RelationDom39"):
                opp_val = getattr(value, "dsl_RelationDom39", None)
                if opp_val is None:
                    setattr(value, "dsl_RelationDom39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_EntityName20(self):
        return self.__dsl_EntityName20

    @dsl_EntityName20.setter
    def dsl_EntityName20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EntityName__dsl_EntityName20", None)
        self.__dsl_EntityName20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_GeneralEntity"):
                opp_val = getattr(old_value, "dsl_GeneralEntity", None)
                if opp_val == self:
                    setattr(old_value, "dsl_GeneralEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_GeneralEntity"):
                opp_val = getattr(value, "dsl_GeneralEntity", None)
                setattr(value, "dsl_GeneralEntity", self)

    @property
    def dsl_EntityName43(self):
        return self.__dsl_EntityName43

    @dsl_EntityName43.setter
    def dsl_EntityName43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EntityName__dsl_EntityName43", None)
        self.__dsl_EntityName43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_RelationDom42"):
                opp_val = getattr(old_value, "dsl_RelationDom42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_RelationDom42"):
                opp_val = getattr(value, "dsl_RelationDom42", None)
                if opp_val is None:
                    setattr(value, "dsl_RelationDom42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_EntityName(self):
        return self.__dsl_EntityName

    @dsl_EntityName.setter
    def dsl_EntityName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_EntityName__dsl_EntityName", None)
        self.__dsl_EntityName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Operation18"):
                opp_val = getattr(old_value, "dsl_Operation18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Operation18"):
                opp_val = getattr(value, "dsl_Operation18", None)
                if opp_val is None:
                    setattr(value, "dsl_Operation18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_EObject:

    pass
class AbstractFrontElement:

    pass
class dsl_Visualizer(AbstractFrontElement, UIComponent):

    def __init__(self, name: str, dsl_Visualizer: "dsl_Functionality" = None, dsl_Visualizer151: "dsl_AbstractFrontElement" = None):
        self.name = name
        self.dsl_Visualizer = dsl_Visualizer
        self.dsl_Visualizer151 = dsl_Visualizer151
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Visualizer151(self):
        return self.__dsl_Visualizer151

    @dsl_Visualizer151.setter
    def dsl_Visualizer151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Visualizer__dsl_Visualizer151", None)
        self.__dsl_Visualizer151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractFrontElement152"):
                opp_val = getattr(old_value, "dsl_AbstractFrontElement152", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractFrontElement152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractFrontElement152"):
                opp_val = getattr(value, "dsl_AbstractFrontElement152", None)
                setattr(value, "dsl_AbstractFrontElement152", self)

    @property
    def dsl_Visualizer(self):
        return self.__dsl_Visualizer

    @dsl_Visualizer.setter
    def dsl_Visualizer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Visualizer__dsl_Visualizer", None)
        self.__dsl_Visualizer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Functionality134"):
                opp_val = getattr(old_value, "dsl_Functionality134", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Functionality134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Functionality134"):
                opp_val = getattr(value, "dsl_Functionality134", None)
                setattr(value, "dsl_Functionality134", self)

class dsl_ReactApp(AbstractFrontElement):

    pass
class dsl_JsModule(AbstractFrontElement):

    def __init__(self, name: str, dsl_JsModule: "dsl_ReactApp" = None, dsl_JsModule155: "dsl_ServiceFront" = None, dsl_JsModule179: "dsl_Directory" = None):
        self.name = name
        self.dsl_JsModule = dsl_JsModule
        self.dsl_JsModule155 = dsl_JsModule155
        self.dsl_JsModule179 = dsl_JsModule179
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_JsModule(self):
        return self.__dsl_JsModule

    @dsl_JsModule.setter
    def dsl_JsModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_JsModule__dsl_JsModule", None)
        self.__dsl_JsModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReactApp128"):
                opp_val = getattr(old_value, "dsl_ReactApp128", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReactApp128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReactApp128"):
                opp_val = getattr(value, "dsl_ReactApp128", None)
                setattr(value, "dsl_ReactApp128", self)

    @property
    def dsl_JsModule155(self):
        return self.__dsl_JsModule155

    @dsl_JsModule155.setter
    def dsl_JsModule155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_JsModule__dsl_JsModule155", None)
        self.__dsl_JsModule155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ServiceFront154"):
                opp_val = getattr(old_value, "dsl_ServiceFront154", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ServiceFront154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ServiceFront154"):
                opp_val = getattr(value, "dsl_ServiceFront154", None)
                setattr(value, "dsl_ServiceFront154", self)

    @property
    def dsl_JsModule179(self):
        return self.__dsl_JsModule179

    @dsl_JsModule179.setter
    def dsl_JsModule179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_JsModule__dsl_JsModule179", None)
        self.__dsl_JsModule179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Directory180"):
                opp_val = getattr(old_value, "dsl_Directory180", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Directory180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Directory180"):
                opp_val = getattr(value, "dsl_Directory180", None)
                setattr(value, "dsl_Directory180", self)

class dsl_State(AbstractFrontElement):

    def __init__(self, name: str, dsl_State: "dsl_Functionality" = None, dsl_State164: "dsl_Reducer" = None, dsl_State162: "dsl_Action" = None):
        self.name = name
        self.dsl_State = dsl_State
        self.dsl_State164 = dsl_State164
        self.dsl_State162 = dsl_State162
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_State162(self):
        return self.__dsl_State162

    @dsl_State162.setter
    def dsl_State162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State162", None)
        self.__dsl_State162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action"):
                opp_val = getattr(old_value, "dsl_Action", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action"):
                opp_val = getattr(value, "dsl_Action", None)
                setattr(value, "dsl_Action", self)

    @property
    def dsl_State(self):
        return self.__dsl_State

    @dsl_State.setter
    def dsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State", None)
        self.__dsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Functionality136"):
                opp_val = getattr(old_value, "dsl_Functionality136", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Functionality136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Functionality136"):
                opp_val = getattr(value, "dsl_Functionality136", None)
                setattr(value, "dsl_Functionality136", self)

    @property
    def dsl_State164(self):
        return self.__dsl_State164

    @dsl_State164.setter
    def dsl_State164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State164", None)
        self.__dsl_State164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Reducer"):
                opp_val = getattr(old_value, "dsl_Reducer", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Reducer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Reducer"):
                opp_val = getattr(value, "dsl_Reducer", None)
                setattr(value, "dsl_Reducer", self)

class dsl_Action(AbstractFrontElement):

    def __init__(self, name: str, dsl_Action: "dsl_State" = None, dsl_Action166: "dsl_ActionCreator" = None, dsl_Action170: "dsl_Directory" = None, dsl_Action168: "dsl_ActionDispatcher" = None):
        self.name = name
        self.dsl_Action = dsl_Action
        self.dsl_Action166 = dsl_Action166
        self.dsl_Action170 = dsl_Action170
        self.dsl_Action168 = dsl_Action168
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Action168(self):
        return self.__dsl_Action168

    @dsl_Action168.setter
    def dsl_Action168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action168", None)
        self.__dsl_Action168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ActionDispatcher"):
                opp_val = getattr(old_value, "dsl_ActionDispatcher", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ActionDispatcher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ActionDispatcher"):
                opp_val = getattr(value, "dsl_ActionDispatcher", None)
                setattr(value, "dsl_ActionDispatcher", self)

    @property
    def dsl_Action166(self):
        return self.__dsl_Action166

    @dsl_Action166.setter
    def dsl_Action166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action166", None)
        self.__dsl_Action166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ActionCreator"):
                opp_val = getattr(old_value, "dsl_ActionCreator", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ActionCreator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ActionCreator"):
                opp_val = getattr(value, "dsl_ActionCreator", None)
                setattr(value, "dsl_ActionCreator", self)

    @property
    def dsl_Action(self):
        return self.__dsl_Action

    @dsl_Action.setter
    def dsl_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action", None)
        self.__dsl_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State162"):
                opp_val = getattr(old_value, "dsl_State162", None)
                if opp_val == self:
                    setattr(old_value, "dsl_State162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State162"):
                opp_val = getattr(value, "dsl_State162", None)
                setattr(value, "dsl_State162", self)

    @property
    def dsl_Action170(self):
        return self.__dsl_Action170

    @dsl_Action170.setter
    def dsl_Action170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action170", None)
        self.__dsl_Action170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Directory171"):
                opp_val = getattr(old_value, "dsl_Directory171", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Directory171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Directory171"):
                opp_val = getattr(value, "dsl_Directory171", None)
                setattr(value, "dsl_Directory171", self)

class dsl_ActionDispatcher(AbstractFrontElement):

    def __init__(self, name: str, dsl_ActionDispatcher: "dsl_Action" = None, dsl_ActionDispatcher173: "dsl_ActionCreator" = None):
        self.name = name
        self.dsl_ActionDispatcher = dsl_ActionDispatcher
        self.dsl_ActionDispatcher173 = dsl_ActionDispatcher173
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_ActionDispatcher(self):
        return self.__dsl_ActionDispatcher

    @dsl_ActionDispatcher.setter
    def dsl_ActionDispatcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ActionDispatcher__dsl_ActionDispatcher", None)
        self.__dsl_ActionDispatcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action168"):
                opp_val = getattr(old_value, "dsl_Action168", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action168"):
                opp_val = getattr(value, "dsl_Action168", None)
                setattr(value, "dsl_Action168", self)

    @property
    def dsl_ActionDispatcher173(self):
        return self.__dsl_ActionDispatcher173

    @dsl_ActionDispatcher173.setter
    def dsl_ActionDispatcher173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ActionDispatcher__dsl_ActionDispatcher173", None)
        self.__dsl_ActionDispatcher173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ActionCreator174"):
                opp_val = getattr(old_value, "dsl_ActionCreator174", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ActionCreator174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ActionCreator174"):
                opp_val = getattr(value, "dsl_ActionCreator174", None)
                setattr(value, "dsl_ActionCreator174", self)

class dsl_Container(AbstractFrontElement):

    def __init__(self, name: str, dsl_Container: "dsl_Functionality" = None, dsl_Container148: "dsl_AbstractFrontElement" = None):
        self.name = name
        self.dsl_Container = dsl_Container
        self.dsl_Container148 = dsl_Container148
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Container148(self):
        return self.__dsl_Container148

    @dsl_Container148.setter
    def dsl_Container148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Container__dsl_Container148", None)
        self.__dsl_Container148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractFrontElement149"):
                opp_val = getattr(old_value, "dsl_AbstractFrontElement149", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractFrontElement149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractFrontElement149"):
                opp_val = getattr(value, "dsl_AbstractFrontElement149", None)
                setattr(value, "dsl_AbstractFrontElement149", self)

    @property
    def dsl_Container(self):
        return self.__dsl_Container

    @dsl_Container.setter
    def dsl_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Container__dsl_Container", None)
        self.__dsl_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Functionality132"):
                opp_val = getattr(old_value, "dsl_Functionality132", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Functionality132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Functionality132"):
                opp_val = getattr(value, "dsl_Functionality132", None)
                setattr(value, "dsl_Functionality132", self)

class dsl_File(AbstractFrontElement):

    def __init__(self, name: str, type: str, dsl_File: "dsl_Directory" = None):
        self.name = name
        self.type = type
        self.dsl_File = dsl_File
        
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
    def dsl_File(self):
        return self.__dsl_File

    @dsl_File.setter
    def dsl_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_File__dsl_File", None)
        self.__dsl_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Directory157"):
                opp_val = getattr(old_value, "dsl_Directory157", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Directory157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Directory157"):
                opp_val = getattr(value, "dsl_Directory157", None)
                setattr(value, "dsl_Directory157", self)

class dsl_ServiceFront(AbstractFrontElement):

    def __init__(self, name: str, method: str, dsl_ServiceFront: "dsl_Functionality" = None, dsl_ServiceFront154: "dsl_JsModule" = None):
        self.name = name
        self.method = method
        self.dsl_ServiceFront = dsl_ServiceFront
        self.dsl_ServiceFront154 = dsl_ServiceFront154
        
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
    def dsl_ServiceFront(self):
        return self.__dsl_ServiceFront

    @dsl_ServiceFront.setter
    def dsl_ServiceFront(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ServiceFront__dsl_ServiceFront", None)
        self.__dsl_ServiceFront = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Functionality138"):
                opp_val = getattr(old_value, "dsl_Functionality138", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Functionality138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Functionality138"):
                opp_val = getattr(value, "dsl_Functionality138", None)
                setattr(value, "dsl_Functionality138", self)

    @property
    def dsl_ServiceFront154(self):
        return self.__dsl_ServiceFront154

    @dsl_ServiceFront154.setter
    def dsl_ServiceFront154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ServiceFront__dsl_ServiceFront154", None)
        self.__dsl_ServiceFront154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_JsModule155"):
                opp_val = getattr(old_value, "dsl_JsModule155", None)
                if opp_val == self:
                    setattr(old_value, "dsl_JsModule155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_JsModule155"):
                opp_val = getattr(value, "dsl_JsModule155", None)
                setattr(value, "dsl_JsModule155", self)

class dsl_Reducer(AbstractFrontElement):

    def __init__(self, name: str, dsl_Reducer: "dsl_State" = None, dsl_Reducer176: "dsl_AbstractFrontElement" = None):
        self.name = name
        self.dsl_Reducer = dsl_Reducer
        self.dsl_Reducer176 = dsl_Reducer176
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Reducer(self):
        return self.__dsl_Reducer

    @dsl_Reducer.setter
    def dsl_Reducer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Reducer__dsl_Reducer", None)
        self.__dsl_Reducer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State164"):
                opp_val = getattr(old_value, "dsl_State164", None)
                if opp_val == self:
                    setattr(old_value, "dsl_State164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State164"):
                opp_val = getattr(value, "dsl_State164", None)
                setattr(value, "dsl_State164", self)

    @property
    def dsl_Reducer176(self):
        return self.__dsl_Reducer176

    @dsl_Reducer176.setter
    def dsl_Reducer176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Reducer__dsl_Reducer176", None)
        self.__dsl_Reducer176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractFrontElement177"):
                opp_val = getattr(old_value, "dsl_AbstractFrontElement177", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractFrontElement177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractFrontElement177"):
                opp_val = getattr(value, "dsl_AbstractFrontElement177", None)
                setattr(value, "dsl_AbstractFrontElement177", self)

class dsl_Functionality(AbstractFrontElement):

    def __init__(self, name: str, dsl_Functionality: "dsl_ReactApp" = None, dsl_Functionality132: "dsl_Container" = None, dsl_Functionality134: "dsl_Visualizer" = None, dsl_Functionality136: "dsl_State" = None, dsl_Functionality138: "dsl_ServiceFront" = None, dsl_Functionality140: "dsl_Directory" = None, dsl_Functionality130: "dsl_RouterComponent" = None):
        self.name = name
        self.dsl_Functionality = dsl_Functionality
        self.dsl_Functionality132 = dsl_Functionality132
        self.dsl_Functionality134 = dsl_Functionality134
        self.dsl_Functionality136 = dsl_Functionality136
        self.dsl_Functionality138 = dsl_Functionality138
        self.dsl_Functionality140 = dsl_Functionality140
        self.dsl_Functionality130 = dsl_Functionality130
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Functionality132(self):
        return self.__dsl_Functionality132

    @dsl_Functionality132.setter
    def dsl_Functionality132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality132", None)
        self.__dsl_Functionality132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Container"):
                opp_val = getattr(old_value, "dsl_Container", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Container"):
                opp_val = getattr(value, "dsl_Container", None)
                setattr(value, "dsl_Container", self)

    @property
    def dsl_Functionality136(self):
        return self.__dsl_Functionality136

    @dsl_Functionality136.setter
    def dsl_Functionality136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality136", None)
        self.__dsl_Functionality136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State"):
                opp_val = getattr(old_value, "dsl_State", None)
                if opp_val == self:
                    setattr(old_value, "dsl_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State"):
                opp_val = getattr(value, "dsl_State", None)
                setattr(value, "dsl_State", self)

    @property
    def dsl_Functionality130(self):
        return self.__dsl_Functionality130

    @dsl_Functionality130.setter
    def dsl_Functionality130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality130", None)
        self.__dsl_Functionality130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_RouterComponent"):
                opp_val = getattr(old_value, "dsl_RouterComponent", None)
                if opp_val == self:
                    setattr(old_value, "dsl_RouterComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_RouterComponent"):
                opp_val = getattr(value, "dsl_RouterComponent", None)
                setattr(value, "dsl_RouterComponent", self)

    @property
    def dsl_Functionality134(self):
        return self.__dsl_Functionality134

    @dsl_Functionality134.setter
    def dsl_Functionality134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality134", None)
        self.__dsl_Functionality134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Visualizer"):
                opp_val = getattr(old_value, "dsl_Visualizer", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Visualizer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Visualizer"):
                opp_val = getattr(value, "dsl_Visualizer", None)
                setattr(value, "dsl_Visualizer", self)

    @property
    def dsl_Functionality138(self):
        return self.__dsl_Functionality138

    @dsl_Functionality138.setter
    def dsl_Functionality138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality138", None)
        self.__dsl_Functionality138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ServiceFront"):
                opp_val = getattr(old_value, "dsl_ServiceFront", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ServiceFront", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ServiceFront"):
                opp_val = getattr(value, "dsl_ServiceFront", None)
                setattr(value, "dsl_ServiceFront", self)

    @property
    def dsl_Functionality140(self):
        return self.__dsl_Functionality140

    @dsl_Functionality140.setter
    def dsl_Functionality140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality140", None)
        self.__dsl_Functionality140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Directory141"):
                opp_val = getattr(old_value, "dsl_Directory141", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Directory141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Directory141"):
                opp_val = getattr(value, "dsl_Directory141", None)
                setattr(value, "dsl_Directory141", self)

    @property
    def dsl_Functionality(self):
        return self.__dsl_Functionality

    @dsl_Functionality.setter
    def dsl_Functionality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Functionality__dsl_Functionality", None)
        self.__dsl_Functionality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReactApp124"):
                opp_val = getattr(old_value, "dsl_ReactApp124", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReactApp124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReactApp124"):
                opp_val = getattr(value, "dsl_ReactApp124", None)
                setattr(value, "dsl_ReactApp124", self)

class dsl_ActionCreator(AbstractFrontElement):

    def __init__(self, name: str, type: str, dsl_ActionCreator: "dsl_Action" = None, dsl_ActionCreator174: "dsl_ActionDispatcher" = None):
        self.name = name
        self.type = type
        self.dsl_ActionCreator = dsl_ActionCreator
        self.dsl_ActionCreator174 = dsl_ActionCreator174
        
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
    def dsl_ActionCreator(self):
        return self.__dsl_ActionCreator

    @dsl_ActionCreator.setter
    def dsl_ActionCreator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ActionCreator__dsl_ActionCreator", None)
        self.__dsl_ActionCreator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action166"):
                opp_val = getattr(old_value, "dsl_Action166", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action166"):
                opp_val = getattr(value, "dsl_Action166", None)
                setattr(value, "dsl_Action166", self)

    @property
    def dsl_ActionCreator174(self):
        return self.__dsl_ActionCreator174

    @dsl_ActionCreator174.setter
    def dsl_ActionCreator174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ActionCreator__dsl_ActionCreator174", None)
        self.__dsl_ActionCreator174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ActionDispatcher173"):
                opp_val = getattr(old_value, "dsl_ActionDispatcher173", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ActionDispatcher173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ActionDispatcher173"):
                opp_val = getattr(value, "dsl_ActionDispatcher173", None)
                setattr(value, "dsl_ActionDispatcher173", self)

class dsl_RouterComponent(AbstractFrontElement, UIComponent):

    def __init__(self, name: str, dsl_RouterComponent: "dsl_Functionality" = None, dsl_RouterComponent143: "dsl_AbstractFrontElement" = None, dsl_RouterComponent146: "dsl_UIComponent" = None):
        self.name = name
        self.dsl_RouterComponent = dsl_RouterComponent
        self.dsl_RouterComponent143 = dsl_RouterComponent143
        self.dsl_RouterComponent146 = dsl_RouterComponent146
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_RouterComponent143(self):
        return self.__dsl_RouterComponent143

    @dsl_RouterComponent143.setter
    def dsl_RouterComponent143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RouterComponent__dsl_RouterComponent143", None)
        self.__dsl_RouterComponent143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AbstractFrontElement144"):
                opp_val = getattr(old_value, "dsl_AbstractFrontElement144", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AbstractFrontElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AbstractFrontElement144"):
                opp_val = getattr(value, "dsl_AbstractFrontElement144", None)
                setattr(value, "dsl_AbstractFrontElement144", self)

    @property
    def dsl_RouterComponent146(self):
        return self.__dsl_RouterComponent146

    @dsl_RouterComponent146.setter
    def dsl_RouterComponent146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RouterComponent__dsl_RouterComponent146", None)
        self.__dsl_RouterComponent146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UIComponent"):
                opp_val = getattr(old_value, "dsl_UIComponent", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UIComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UIComponent"):
                opp_val = getattr(value, "dsl_UIComponent", None)
                setattr(value, "dsl_UIComponent", self)

    @property
    def dsl_RouterComponent(self):
        return self.__dsl_RouterComponent

    @dsl_RouterComponent.setter
    def dsl_RouterComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RouterComponent__dsl_RouterComponent", None)
        self.__dsl_RouterComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Functionality130"):
                opp_val = getattr(old_value, "dsl_Functionality130", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Functionality130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Functionality130"):
                opp_val = getattr(value, "dsl_Functionality130", None)
                setattr(value, "dsl_Functionality130", self)

class dsl_Directory(AbstractFrontElement):

    def __init__(self, purpose: str, name: str, dsl_Directory: "dsl_ReactApp" = None, dsl_Directory141: "dsl_Functionality" = None, dsl_Directory160: "dsl_Directory" = None, dsl_Directory158: "dsl_Directory" = None, dsl_Directory157: "dsl_File" = None, dsl_Directory171: "dsl_Action" = None, dsl_Directory180: "dsl_JsModule" = None):
        self.purpose = purpose
        self.name = name
        self.dsl_Directory = dsl_Directory
        self.dsl_Directory141 = dsl_Directory141
        self.dsl_Directory160 = dsl_Directory160
        self.dsl_Directory158 = dsl_Directory158
        self.dsl_Directory157 = dsl_Directory157
        self.dsl_Directory171 = dsl_Directory171
        self.dsl_Directory180 = dsl_Directory180
        
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
    def dsl_Directory141(self):
        return self.__dsl_Directory141

    @dsl_Directory141.setter
    def dsl_Directory141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory141", None)
        self.__dsl_Directory141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Functionality140"):
                opp_val = getattr(old_value, "dsl_Functionality140", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Functionality140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Functionality140"):
                opp_val = getattr(value, "dsl_Functionality140", None)
                setattr(value, "dsl_Functionality140", self)

    @property
    def dsl_Directory160(self):
        return self.__dsl_Directory160

    @dsl_Directory160.setter
    def dsl_Directory160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory160", None)
        self.__dsl_Directory160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Directory158"):
                opp_val = getattr(old_value, "dsl_Directory158", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Directory158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Directory158"):
                opp_val = getattr(value, "dsl_Directory158", None)
                setattr(value, "dsl_Directory158", self)

    @property
    def dsl_Directory157(self):
        return self.__dsl_Directory157

    @dsl_Directory157.setter
    def dsl_Directory157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory157", None)
        self.__dsl_Directory157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_File"):
                opp_val = getattr(old_value, "dsl_File", None)
                if opp_val == self:
                    setattr(old_value, "dsl_File", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_File"):
                opp_val = getattr(value, "dsl_File", None)
                setattr(value, "dsl_File", self)

    @property
    def dsl_Directory(self):
        return self.__dsl_Directory

    @dsl_Directory.setter
    def dsl_Directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory", None)
        self.__dsl_Directory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ReactApp126"):
                opp_val = getattr(old_value, "dsl_ReactApp126", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ReactApp126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ReactApp126"):
                opp_val = getattr(value, "dsl_ReactApp126", None)
                setattr(value, "dsl_ReactApp126", self)

    @property
    def dsl_Directory158(self):
        return self.__dsl_Directory158

    @dsl_Directory158.setter
    def dsl_Directory158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory158", None)
        self.__dsl_Directory158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Directory160"):
                opp_val = getattr(old_value, "dsl_Directory160", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Directory160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Directory160"):
                opp_val = getattr(value, "dsl_Directory160", None)
                setattr(value, "dsl_Directory160", self)

    @property
    def dsl_Directory171(self):
        return self.__dsl_Directory171

    @dsl_Directory171.setter
    def dsl_Directory171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory171", None)
        self.__dsl_Directory171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action170"):
                opp_val = getattr(old_value, "dsl_Action170", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action170"):
                opp_val = getattr(value, "dsl_Action170", None)
                setattr(value, "dsl_Action170", self)

    @property
    def dsl_Directory180(self):
        return self.__dsl_Directory180

    @dsl_Directory180.setter
    def dsl_Directory180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Directory__dsl_Directory180", None)
        self.__dsl_Directory180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_JsModule179"):
                opp_val = getattr(old_value, "dsl_JsModule179", None)
                if opp_val == self:
                    setattr(old_value, "dsl_JsModule179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_JsModule179"):
                opp_val = getattr(value, "dsl_JsModule179", None)
                setattr(value, "dsl_JsModule179", self)

class dsl_Property:

    def __init__(self, name: str, dsl_Property: "dsl_GeneralEntity" = None, dsl_Property24: "dsl_Type" = None, dsl_Property30: "dsl_SpecialEntity" = None):
        self.name = name
        self.dsl_Property = dsl_Property
        self.dsl_Property24 = dsl_Property24
        self.dsl_Property30 = dsl_Property30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Property(self):
        return self.__dsl_Property

    @dsl_Property.setter
    def dsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Property__dsl_Property", None)
        self.__dsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_GeneralEntity22"):
                opp_val = getattr(old_value, "dsl_GeneralEntity22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_GeneralEntity22"):
                opp_val = getattr(value, "dsl_GeneralEntity22", None)
                if opp_val is None:
                    setattr(value, "dsl_GeneralEntity22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Property24(self):
        return self.__dsl_Property24

    @dsl_Property24.setter
    def dsl_Property24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Property__dsl_Property24", None)
        self.__dsl_Property24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Type25"):
                opp_val = getattr(old_value, "dsl_Type25", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Type25"):
                opp_val = getattr(value, "dsl_Type25", None)
                setattr(value, "dsl_Type25", self)

    @property
    def dsl_Property30(self):
        return self.__dsl_Property30

    @dsl_Property30.setter
    def dsl_Property30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Property__dsl_Property30", None)
        self.__dsl_Property30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SpecialEntity29"):
                opp_val = getattr(old_value, "dsl_SpecialEntity29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SpecialEntity29"):
                opp_val = getattr(value, "dsl_SpecialEntity29", None)
                if opp_val is None:
                    setattr(value, "dsl_SpecialEntity29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_GeneralEntity:

    pass
class dsl_Module:

    def __init__(self, name: str, dsl_Module12: set["dsl_Submodule"] = None, dsl_Module: "dsl_Domain" = None):
        self.name = name
        self.dsl_Module12 = dsl_Module12 if dsl_Module12 is not None else set()
        self.dsl_Module = dsl_Module
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Module(self):
        return self.__dsl_Module

    @dsl_Module.setter
    def dsl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Module__dsl_Module", None)
        self.__dsl_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Domain8"):
                opp_val = getattr(old_value, "dsl_Domain8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Domain8"):
                opp_val = getattr(value, "dsl_Domain8", None)
                if opp_val is None:
                    setattr(value, "dsl_Domain8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Module12(self):
        return self.__dsl_Module12

    @dsl_Module12.setter
    def dsl_Module12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Module__dsl_Module12", None)
        self.__dsl_Module12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Submodule"):
                    opp_val = getattr(item, "dsl_Submodule", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Submodule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Submodule"):
                    opp_val = getattr(item, "dsl_Submodule", None)
                    
                    setattr(item, "dsl_Submodule", self)
                    

class dsl_Type(AbstractFrontElement):

    def __init__(self, name: str, dsl_Type: "dsl_Domain" = None, dsl_Type25: "dsl_Property" = None):
        self.name = name
        self.dsl_Type = dsl_Type
        self.dsl_Type25 = dsl_Type25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Type(self):
        return self.__dsl_Type

    @dsl_Type.setter
    def dsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type", None)
        self.__dsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Domain6"):
                opp_val = getattr(old_value, "dsl_Domain6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Domain6"):
                opp_val = getattr(value, "dsl_Domain6", None)
                if opp_val is None:
                    setattr(value, "dsl_Domain6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Type25(self):
        return self.__dsl_Type25

    @dsl_Type25.setter
    def dsl_Type25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Type__dsl_Type25", None)
        self.__dsl_Type25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Property24"):
                opp_val = getattr(old_value, "dsl_Property24", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Property24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Property24"):
                opp_val = getattr(value, "dsl_Property24", None)
                setattr(value, "dsl_Property24", self)

class dsl_Technology:

    pass
class dsl_Operation:

    def __init__(self, type: str, dsl_Operation: "dsl_Submodule" = None, dsl_Operation18: set["dsl_EntityName"] = None):
        self.type = type
        self.dsl_Operation = dsl_Operation
        self.dsl_Operation18 = dsl_Operation18 if dsl_Operation18 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dsl_Operation(self):
        return self.__dsl_Operation

    @dsl_Operation.setter
    def dsl_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Operation__dsl_Operation", None)
        self.__dsl_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Submodule14"):
                opp_val = getattr(old_value, "dsl_Submodule14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Submodule14"):
                opp_val = getattr(value, "dsl_Submodule14", None)
                if opp_val is None:
                    setattr(value, "dsl_Submodule14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Operation18(self):
        return self.__dsl_Operation18

    @dsl_Operation18.setter
    def dsl_Operation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Operation__dsl_Operation18", None)
        self.__dsl_Operation18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_EntityName"):
                    opp_val = getattr(item, "dsl_EntityName", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_EntityName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_EntityName"):
                    opp_val = getattr(item, "dsl_EntityName", None)
                    
                    setattr(item, "dsl_EntityName", self)
                    

class dsl_Submodule:

    def __init__(self, name: str, dsl_Submodule: "dsl_Module" = None, dsl_Submodule14: set["dsl_Operation"] = None, dsl_Submodule16: set["dsl_EObject"] = None):
        self.name = name
        self.dsl_Submodule = dsl_Submodule
        self.dsl_Submodule14 = dsl_Submodule14 if dsl_Submodule14 is not None else set()
        self.dsl_Submodule16 = dsl_Submodule16 if dsl_Submodule16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Submodule14(self):
        return self.__dsl_Submodule14

    @dsl_Submodule14.setter
    def dsl_Submodule14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Submodule__dsl_Submodule14", None)
        self.__dsl_Submodule14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Operation"):
                    opp_val = getattr(item, "dsl_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Operation"):
                    opp_val = getattr(item, "dsl_Operation", None)
                    
                    setattr(item, "dsl_Operation", self)
                    

    @property
    def dsl_Submodule16(self):
        return self.__dsl_Submodule16

    @dsl_Submodule16.setter
    def dsl_Submodule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Submodule__dsl_Submodule16", None)
        self.__dsl_Submodule16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_EObject"):
                    opp_val = getattr(item, "dsl_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_EObject"):
                    opp_val = getattr(item, "dsl_EObject", None)
                    
                    setattr(item, "dsl_EObject", self)
                    

    @property
    def dsl_Submodule(self):
        return self.__dsl_Submodule

    @dsl_Submodule.setter
    def dsl_Submodule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Submodule__dsl_Submodule", None)
        self.__dsl_Submodule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Module12"):
                opp_val = getattr(old_value, "dsl_Module12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Module12"):
                opp_val = getattr(value, "dsl_Module12", None)
                if opp_val is None:
                    setattr(value, "dsl_Module12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_RelationDom:

    pass
class dsl_Architecture:

    pass
class dsl_Domain:

    pass
class dsl_System:

    pass