from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scxml_EStringToStringMapEntry:

    pass
class scxml_DocumentRoot:

    def __init__(self, mixed: str, scxml_DocumentRoot: set["scxml_EStringToStringMapEntry"] = None, scxml_DocumentRoot28: set["scxml_EStringToStringMapEntry"] = None, scxml_DocumentRoot31: set["scxml_ScxmlScxmlType"] = None):
        self.mixed = mixed
        self.scxml_DocumentRoot = scxml_DocumentRoot if scxml_DocumentRoot is not None else set()
        self.scxml_DocumentRoot28 = scxml_DocumentRoot28 if scxml_DocumentRoot28 is not None else set()
        self.scxml_DocumentRoot31 = scxml_DocumentRoot31 if scxml_DocumentRoot31 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def scxml_DocumentRoot28(self):
        return self.__scxml_DocumentRoot28

    @scxml_DocumentRoot28.setter
    def scxml_DocumentRoot28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot28", None)
        self.__scxml_DocumentRoot28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_EStringToStringMapEntry29"):
                    opp_val = getattr(item, "scxml_EStringToStringMapEntry29", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_EStringToStringMapEntry29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_EStringToStringMapEntry29"):
                    opp_val = getattr(item, "scxml_EStringToStringMapEntry29", None)
                    
                    setattr(item, "scxml_EStringToStringMapEntry29", self)
                    

    @property
    def scxml_DocumentRoot31(self):
        return self.__scxml_DocumentRoot31

    @scxml_DocumentRoot31.setter
    def scxml_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot31", None)
        self.__scxml_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScxmlType32"):
                    opp_val = getattr(item, "scxml_ScxmlScxmlType32", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScxmlType32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScxmlType32"):
                    opp_val = getattr(item, "scxml_ScxmlScxmlType32", None)
                    
                    setattr(item, "scxml_ScxmlScxmlType32", self)
                    

    @property
    def scxml_DocumentRoot(self):
        return self.__scxml_DocumentRoot

    @scxml_DocumentRoot.setter
    def scxml_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot", None)
        self.__scxml_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "scxml_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "scxml_EStringToStringMapEntry", None)
                    
                    setattr(item, "scxml_EStringToStringMapEntry", self)
                    

class scxml_ScxmlTransitionType:

    def __init__(self, target: str, scxmlExecutablecontent: str, any: str, cond: str, event: str, scxml_ScxmlTransitionType: "scxml_ScxmlStateType" = None, scxml_ScxmlTransitionType21: set["scxml_ScxmlSendType"] = None, scxml_ScxmlTransitionType24: set["scxml_ScxmlScriptType"] = None):
        self.target = target
        self.scxmlExecutablecontent = scxmlExecutablecontent
        self.any = any
        self.cond = cond
        self.event = event
        self.scxml_ScxmlTransitionType = scxml_ScxmlTransitionType
        self.scxml_ScxmlTransitionType21 = scxml_ScxmlTransitionType21 if scxml_ScxmlTransitionType21 is not None else set()
        self.scxml_ScxmlTransitionType24 = scxml_ScxmlTransitionType24 if scxml_ScxmlTransitionType24 is not None else set()
        
    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def scxmlExecutablecontent(self) -> str:
        return self.__scxmlExecutablecontent

    @scxmlExecutablecontent.setter
    def scxmlExecutablecontent(self, scxmlExecutablecontent: str):
        self.__scxmlExecutablecontent = scxmlExecutablecontent

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlTransitionType24(self):
        return self.__scxml_ScxmlTransitionType24

    @scxml_ScxmlTransitionType24.setter
    def scxml_ScxmlTransitionType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType24", None)
        self.__scxml_ScxmlTransitionType24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType25"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType25", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType25"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType25", None)
                    
                    setattr(item, "scxml_ScxmlScriptType25", self)
                    

    @property
    def scxml_ScxmlTransitionType21(self):
        return self.__scxml_ScxmlTransitionType21

    @scxml_ScxmlTransitionType21.setter
    def scxml_ScxmlTransitionType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType21", None)
        self.__scxml_ScxmlTransitionType21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType22"):
                    opp_val = getattr(item, "scxml_ScxmlSendType22", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType22"):
                    opp_val = getattr(item, "scxml_ScxmlSendType22", None)
                    
                    setattr(item, "scxml_ScxmlSendType22", self)
                    

    @property
    def scxml_ScxmlTransitionType(self):
        return self.__scxml_ScxmlTransitionType

    @scxml_ScxmlTransitionType.setter
    def scxml_ScxmlTransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType", None)
        self.__scxml_ScxmlTransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType16"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType16"):
                opp_val = getattr(value, "scxml_ScxmlStateType16", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlStateType:

    def __init__(self, id: str, initial: str, scxml_ScxmlStateType: "scxml_ScxmlScxmlType" = None, scxml_ScxmlStateType19: "scxml_ScxmlStateType" = None, scxml_ScxmlStateType17: set["scxml_ScxmlStateType"] = None, scxml_ScxmlStateType10: set["scxml_ScxmlOnexecuteType"] = None, scxml_ScxmlStateType13: set["scxml_ScxmlOnexecuteType"] = None, scxml_ScxmlStateType16: set["scxml_ScxmlTransitionType"] = None):
        self.id = id
        self.initial = initial
        self.scxml_ScxmlStateType = scxml_ScxmlStateType
        self.scxml_ScxmlStateType19 = scxml_ScxmlStateType19
        self.scxml_ScxmlStateType17 = scxml_ScxmlStateType17 if scxml_ScxmlStateType17 is not None else set()
        self.scxml_ScxmlStateType10 = scxml_ScxmlStateType10 if scxml_ScxmlStateType10 is not None else set()
        self.scxml_ScxmlStateType13 = scxml_ScxmlStateType13 if scxml_ScxmlStateType13 is not None else set()
        self.scxml_ScxmlStateType16 = scxml_ScxmlStateType16 if scxml_ScxmlStateType16 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def scxml_ScxmlStateType13(self):
        return self.__scxml_ScxmlStateType13

    @scxml_ScxmlStateType13.setter
    def scxml_ScxmlStateType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType13", None)
        self.__scxml_ScxmlStateType13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnexecuteType14"):
                    opp_val = getattr(item, "scxml_ScxmlOnexecuteType14", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnexecuteType14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnexecuteType14"):
                    opp_val = getattr(item, "scxml_ScxmlOnexecuteType14", None)
                    
                    setattr(item, "scxml_ScxmlOnexecuteType14", self)
                    

    @property
    def scxml_ScxmlStateType(self):
        return self.__scxml_ScxmlStateType

    @scxml_ScxmlStateType.setter
    def scxml_ScxmlStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType", None)
        self.__scxml_ScxmlStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlStateType16(self):
        return self.__scxml_ScxmlStateType16

    @scxml_ScxmlStateType16.setter
    def scxml_ScxmlStateType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType16", None)
        self.__scxml_ScxmlStateType16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlTransitionType"):
                    opp_val = getattr(item, "scxml_ScxmlTransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlTransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlTransitionType"):
                    opp_val = getattr(item, "scxml_ScxmlTransitionType", None)
                    
                    setattr(item, "scxml_ScxmlTransitionType", self)
                    

    @property
    def scxml_ScxmlStateType17(self):
        return self.__scxml_ScxmlStateType17

    @scxml_ScxmlStateType17.setter
    def scxml_ScxmlStateType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType17", None)
        self.__scxml_ScxmlStateType17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlStateType19"):
                    opp_val = getattr(item, "scxml_ScxmlStateType19", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlStateType19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlStateType19"):
                    opp_val = getattr(item, "scxml_ScxmlStateType19", None)
                    
                    setattr(item, "scxml_ScxmlStateType19", self)
                    

    @property
    def scxml_ScxmlStateType10(self):
        return self.__scxml_ScxmlStateType10

    @scxml_ScxmlStateType10.setter
    def scxml_ScxmlStateType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType10", None)
        self.__scxml_ScxmlStateType10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnexecuteType11"):
                    opp_val = getattr(item, "scxml_ScxmlOnexecuteType11", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnexecuteType11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnexecuteType11"):
                    opp_val = getattr(item, "scxml_ScxmlOnexecuteType11", None)
                    
                    setattr(item, "scxml_ScxmlOnexecuteType11", self)
                    

    @property
    def scxml_ScxmlStateType19(self):
        return self.__scxml_ScxmlStateType19

    @scxml_ScxmlStateType19.setter
    def scxml_ScxmlStateType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType19", None)
        self.__scxml_ScxmlStateType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType17"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType17"):
                opp_val = getattr(value, "scxml_ScxmlStateType17", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlScxmlType:

    def __init__(self, id: str, initial: str, version: str, scxml_ScxmlScxmlType5: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlScxmlType: set["scxml_ScxmlStateType"] = None, scxml_ScxmlScxmlType32: "scxml_DocumentRoot" = None):
        self.id = id
        self.initial = initial
        self.version = version
        self.scxml_ScxmlScxmlType5 = scxml_ScxmlScxmlType5 if scxml_ScxmlScxmlType5 is not None else set()
        self.scxml_ScxmlScxmlType = scxml_ScxmlScxmlType if scxml_ScxmlScxmlType is not None else set()
        self.scxml_ScxmlScxmlType32 = scxml_ScxmlScxmlType32
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def scxml_ScxmlScxmlType(self):
        return self.__scxml_ScxmlScxmlType

    @scxml_ScxmlScxmlType.setter
    def scxml_ScxmlScxmlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType", None)
        self.__scxml_ScxmlScxmlType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlStateType"):
                    opp_val = getattr(item, "scxml_ScxmlStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlStateType"):
                    opp_val = getattr(item, "scxml_ScxmlStateType", None)
                    
                    setattr(item, "scxml_ScxmlStateType", self)
                    

    @property
    def scxml_ScxmlScxmlType5(self):
        return self.__scxml_ScxmlScxmlType5

    @scxml_ScxmlScxmlType5.setter
    def scxml_ScxmlScxmlType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType5", None)
        self.__scxml_ScxmlScxmlType5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType6"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType6", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType6"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType6", None)
                    
                    setattr(item, "scxml_ScxmlScriptType6", self)
                    

    @property
    def scxml_ScxmlScxmlType32(self):
        return self.__scxml_ScxmlScxmlType32

    @scxml_ScxmlScxmlType32.setter
    def scxml_ScxmlScxmlType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType32", None)
        self.__scxml_ScxmlScxmlType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot31"):
                opp_val = getattr(old_value, "scxml_DocumentRoot31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot31"):
                opp_val = getattr(value, "scxml_DocumentRoot31", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlParamType:

    def __init__(self, anyAttribute: str, scxmlExtraContent: str, any: str, expr: str, name: str, scxml_ScxmlParamType: "scxml_ScxmlSendType" = None):
        self.anyAttribute = anyAttribute
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.expr = expr
        self.name = name
        self.scxml_ScxmlParamType = scxml_ScxmlParamType
        
    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scxml_ScxmlParamType(self):
        return self.__scxml_ScxmlParamType

    @scxml_ScxmlParamType.setter
    def scxml_ScxmlParamType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParamType__scxml_ScxmlParamType", None)
        self.__scxml_ScxmlParamType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlSendType8"):
                opp_val = getattr(old_value, "scxml_ScxmlSendType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlSendType8"):
                opp_val = getattr(value, "scxml_ScxmlSendType8", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlSendType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlScriptType:

    def __init__(self, mixed: str, scxmlExtraContent: str, any: str, src: str, content: str, scxml_ScxmlScriptType: "scxml_ScxmlOnexecuteType" = None, scxml_ScxmlScriptType6: "scxml_ScxmlScxmlType" = None, scxml_ScxmlScriptType25: "scxml_ScxmlTransitionType" = None):
        self.mixed = mixed
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.src = src
        self.content = content
        self.scxml_ScxmlScriptType = scxml_ScxmlScriptType
        self.scxml_ScxmlScriptType6 = scxml_ScxmlScriptType6
        self.scxml_ScxmlScriptType25 = scxml_ScxmlScriptType25
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlScriptType6(self):
        return self.__scxml_ScxmlScriptType6

    @scxml_ScxmlScriptType6.setter
    def scxml_ScxmlScriptType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType6", None)
        self.__scxml_ScxmlScriptType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType5"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType5"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType5", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType25(self):
        return self.__scxml_ScxmlScriptType25

    @scxml_ScxmlScriptType25.setter
    def scxml_ScxmlScriptType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType25", None)
        self.__scxml_ScxmlScriptType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType24"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType24"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType24", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType(self):
        return self.__scxml_ScxmlScriptType

    @scxml_ScxmlScriptType.setter
    def scxml_ScxmlScriptType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType", None)
        self.__scxml_ScxmlScriptType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexecuteType2"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexecuteType2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexecuteType2"):
                opp_val = getattr(value, "scxml_ScxmlOnexecuteType2", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexecuteType2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlOnexecuteType:

    def __init__(self, any: str, scxmlExecutablecontent: str, anyAttribute: str, scxml_ScxmlOnexecuteType: set["scxml_ScxmlSendType"] = None, scxml_ScxmlOnexecuteType2: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlOnexecuteType11: "scxml_ScxmlStateType" = None, scxml_ScxmlOnexecuteType14: "scxml_ScxmlStateType" = None):
        self.any = any
        self.scxmlExecutablecontent = scxmlExecutablecontent
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlOnexecuteType = scxml_ScxmlOnexecuteType if scxml_ScxmlOnexecuteType is not None else set()
        self.scxml_ScxmlOnexecuteType2 = scxml_ScxmlOnexecuteType2 if scxml_ScxmlOnexecuteType2 is not None else set()
        self.scxml_ScxmlOnexecuteType11 = scxml_ScxmlOnexecuteType11
        self.scxml_ScxmlOnexecuteType14 = scxml_ScxmlOnexecuteType14
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxmlExecutablecontent(self) -> str:
        return self.__scxmlExecutablecontent

    @scxmlExecutablecontent.setter
    def scxmlExecutablecontent(self, scxmlExecutablecontent: str):
        self.__scxmlExecutablecontent = scxmlExecutablecontent

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlOnexecuteType2(self):
        return self.__scxml_ScxmlOnexecuteType2

    @scxml_ScxmlOnexecuteType2.setter
    def scxml_ScxmlOnexecuteType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexecuteType__scxml_ScxmlOnexecuteType2", None)
        self.__scxml_ScxmlOnexecuteType2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType", None)
                    
                    setattr(item, "scxml_ScxmlScriptType", self)
                    

    @property
    def scxml_ScxmlOnexecuteType14(self):
        return self.__scxml_ScxmlOnexecuteType14

    @scxml_ScxmlOnexecuteType14.setter
    def scxml_ScxmlOnexecuteType14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexecuteType__scxml_ScxmlOnexecuteType14", None)
        self.__scxml_ScxmlOnexecuteType14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType13"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType13"):
                opp_val = getattr(value, "scxml_ScxmlStateType13", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnexecuteType(self):
        return self.__scxml_ScxmlOnexecuteType

    @scxml_ScxmlOnexecuteType.setter
    def scxml_ScxmlOnexecuteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexecuteType__scxml_ScxmlOnexecuteType", None)
        self.__scxml_ScxmlOnexecuteType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType"):
                    opp_val = getattr(item, "scxml_ScxmlSendType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType"):
                    opp_val = getattr(item, "scxml_ScxmlSendType", None)
                    
                    setattr(item, "scxml_ScxmlSendType", self)
                    

    @property
    def scxml_ScxmlOnexecuteType11(self):
        return self.__scxml_ScxmlOnexecuteType11

    @scxml_ScxmlOnexecuteType11.setter
    def scxml_ScxmlOnexecuteType11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexecuteType__scxml_ScxmlOnexecuteType11", None)
        self.__scxml_ScxmlOnexecuteType11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType10"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType10"):
                opp_val = getattr(value, "scxml_ScxmlStateType10", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlSendType:

    def __init__(self, event: str, scxml_ScxmlSendType: "scxml_ScxmlOnexecuteType" = None, scxml_ScxmlSendType8: set["scxml_ScxmlParamType"] = None, scxml_ScxmlSendType22: "scxml_ScxmlTransitionType" = None):
        self.event = event
        self.scxml_ScxmlSendType = scxml_ScxmlSendType
        self.scxml_ScxmlSendType8 = scxml_ScxmlSendType8 if scxml_ScxmlSendType8 is not None else set()
        self.scxml_ScxmlSendType22 = scxml_ScxmlSendType22
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def scxml_ScxmlSendType(self):
        return self.__scxml_ScxmlSendType

    @scxml_ScxmlSendType.setter
    def scxml_ScxmlSendType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType", None)
        self.__scxml_ScxmlSendType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexecuteType"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexecuteType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexecuteType"):
                opp_val = getattr(value, "scxml_ScxmlOnexecuteType", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexecuteType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType8(self):
        return self.__scxml_ScxmlSendType8

    @scxml_ScxmlSendType8.setter
    def scxml_ScxmlSendType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType8", None)
        self.__scxml_ScxmlSendType8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParamType"):
                    opp_val = getattr(item, "scxml_ScxmlParamType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParamType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParamType"):
                    opp_val = getattr(item, "scxml_ScxmlParamType", None)
                    
                    setattr(item, "scxml_ScxmlParamType", self)
                    

    @property
    def scxml_ScxmlSendType22(self):
        return self.__scxml_ScxmlSendType22

    @scxml_ScxmlSendType22.setter
    def scxml_ScxmlSendType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType22", None)
        self.__scxml_ScxmlSendType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType21"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType21"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType21", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
